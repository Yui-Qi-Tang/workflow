#!/usr/bin/env python3
"""Validate a five-stage artifact chain and derive the next permitted stage."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

if __package__:
    from .contracts import ContractError, STAGES, needs_user_input, parse_artifact, validate_artifact, validate_lineage
else:
    from contracts import ContractError, STAGES, needs_user_input, parse_artifact, validate_artifact, validate_lineage


ROOT = Path(__file__).resolve().parent.parent
VERSION = "0.2.0"
SCHEMA_VERSION = "agent_loop_poc.v2"


@dataclass
class TaskPaths:
    task_id: str
    tasker_input: Path
    researcher_task: Path
    planner_plan: Path
    implementer_impl: Path
    reviewer_result: Path
    reviewer_review: Path
    state_file: Path

    def outputs(self) -> list[Path]:
        return [self.researcher_task, self.planner_plan, self.implementer_impl, self.reviewer_result, self.reviewer_review]


def build_paths(task_id: str) -> TaskPaths:
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,127}", task_id):
        raise ValueError("task_id must be 1-128 ASCII letters, digits, dots, underscores or hyphens, starting with a letter or digit")
    base = ROOT / "share" / task_id
    paths = TaskPaths(
        task_id, ROOT / "tasker" / f"{task_id}.md",
        base / "researcher/task.md", base / "planner/plan.md", base / "implementer/impl.md",
        base / "reviewer/result.md", base / "reviewer/review.md", base / "loop/state.json",
    )
    for path in [paths.tasker_input, paths.state_file, *paths.outputs(), *review_mirrors(paths)]:
        if not path.resolve().is_relative_to(ROOT.resolve()):
            raise ValueError(f"Workflow path escapes repository: {path}")
    return paths


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def review_mirrors(paths: TaskPaths) -> list[Path]:
    return [paths.reviewer_review.parent / name for name in ("task.md", "plan.md", "impl.md")]


def stage_inputs(paths: TaskPaths, stage: str) -> list[Path]:
    index = STAGES.index(stage)
    if index == 0:
        return [paths.tasker_input]
    if stage == "reviewer":
        return [*review_mirrors(paths), paths.reviewer_result]
    return [paths.outputs()[index - 1]]


def input_fingerprints(paths: TaskPaths, stage: str) -> dict[str, str]:
    return {relative(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in stage_inputs(paths, stage)}


def check_review_bundle(paths: TaskPaths) -> None:
    for canonical, mirror in zip(paths.outputs()[:3], review_mirrors(paths)):
        if canonical.read_bytes() != mirror.read_bytes():
            raise ContractError(f"Review mirror differs from canonical input: {relative(mirror)}")


def _decision(state, status, stage, reason, code, *, target=None, blocker=None):
    state.update(status=status, current_stage=stage, next_stage=target,
                 reason=reason, reason_code=code, blocker=blocker)
    return state


def sync_state(paths: TaskPaths, existing: dict[str, Any] | None = None) -> dict[str, Any]:
    """Read only. Cached state never authorizes progress or completion."""
    outputs = paths.outputs()
    state = {
        "schema_version": SCHEMA_VERSION, "task_id": paths.task_id,
        "status": "blocked", "current_stage": None, "next_stage": None,
        "last_completed_stage": None, "return_target": None,
        "needs_user_input": False, "reason": "", "reason_code": "",
        "blocker": None, "invalidated_artifacts": [],
        "artifacts": {name: path.is_file() for name, path in zip(
            ("tasker_input", "researcher_task", "planner_plan", "implementer_impl", "reviewer_result", "reviewer_review"),
            [paths.tasker_input, *outputs])},
        "history": list((existing or {}).get("history", [])), "updated_at": now_iso(),
    }
    if not paths.tasker_input.is_file():
        return _decision(state, "blocked", None, f"Missing task input: {relative(paths.tasker_input)}", "missing_input")
    accepted = {}
    for index, (stage, path) in enumerate(zip(STAGES, outputs)):
        if stage == "reviewer":
            try:
                check_review_bundle(paths)
            except (OSError, ContractError) as exc:
                return _decision(state, "blocked", stage, str(exc), "review_bundle_invalid")
        if not path.is_file():
            if path.exists():
                return _decision(state, "blocked", stage, f"Artifact is not a file: {relative(path)}", "artifact_invalid")
            if any(p.exists() for p in outputs[index + 1:]):
                state["invalidated_artifacts"] = [relative(p) for p in outputs[index + 1:] if p.exists()]
                state["return_target"] = stage
                return _decision(state, "blocked", stage, f"Missing predecessor artifact: {relative(path)}", "missing_predecessor")
            return _decision(state, "initialized" if index == 0 else "ready", STAGES[index - 1] if index else None,
                             f"Run {stage} with the current required inputs.", "stage_ready", target=stage)
        try:
            data = parse_artifact(path.read_text(encoding="utf-8"))
            errors = validate_artifact(data, stage, paths.task_id)
            if errors:
                raise ContractError("; ".join(errors))
        except (OSError, UnicodeError, ContractError) as exc:
            return _decision(state, "blocked", stage, f"{relative(path)}: {exc}", "artifact_invalid")
        errors = validate_lineage(data)
        if errors:
            return _decision(state, "blocked", stage, "; ".join(errors), "lineage_missing_or_invalid")
        try:
            expected = input_fingerprints(paths, stage)
        except OSError as exc:
            return _decision(state, "blocked", stage, str(exc), "missing_input")
        declared = {entry["path"].removeprefix("./") for entry in data["input_artifacts"] if entry["required"]}
        if not set(expected).issubset(declared) or set(data["input_fingerprints"]) != set(expected):
            return _decision(state, "blocked", stage, "Required input declarations or fingerprint paths do not match this stage.", "input_contract_invalid")
        if data["input_fingerprints"] != expected:
            state["invalidated_artifacts"] = [relative(p) for p in outputs[index:] if p.exists()]
            state["return_target"] = stage
            return _decision(state, "needs_revision", stage, "Input changed; regenerate this stage and its descendants. Existing files were preserved.", "input_changed", target=stage)
        if stage == "implementer" and data["status"] == "success":
            results = {item["check"]: item for item in data["validation_results"]}
            for check in accepted["planner"]["validation_plan"]:
                if check["required"] and (check["check"] not in results or not results[check["check"]]["required"] or results[check["check"]]["status"] != "passed"):
                    return _decision(state, "blocked", stage, f"Required planned check is missing, downgraded or not passed: {check['check']}", "required_validation_missing")
        accepted[stage] = data
        state["last_completed_stage"] = stage
        target = data["handoff"]["next_agent"]
        target = None if target == "NONE" else target
        blocker = data.get("blocker")
        if needs_user_input(data):
            state["needs_user_input"] = True
            state["return_target"] = target
            return _decision(state, "waiting_user", stage, "Resolve the structured blocking question, approval or proposed task update.", "user_decision", blocker=blocker)
        if stage == "reviewer":
            if data["overall_judgment"] == "success":
                if accepted["implementer"]["status"] != "success":
                    return _decision(state, "blocked", stage, "Successful review cannot override an unsuccessful implementation.", "inconsistent_success")
                return _decision(state, "completed", stage, "Current artifact chain passed structural and declared-result checks.", "review_success")
            state["return_target"] = target
            return _decision(state, "needs_revision" if target else "blocked", stage, data["reason"], "review_failed", target=target, blocker=blocker)
        # A failed/blocked implementation can explicitly request reviewer diagnosis.
        if data["status"] == "blocked" and not (stage == "implementer" and target == "reviewer"):
            state["return_target"] = target
            return _decision(state, "blocked", stage, blocker["reason"] if blocker else "Stage reports a blocker; no automatic retry is authorized.", "stage_blocked", blocker=blocker)
        if target != STAGES[index + 1]:
            state["return_target"] = target
            return _decision(state, "needs_revision" if target else "blocked", stage, "Stage requested an upstream handoff." if target else "Stage has no safe handoff.", "stage_return", target=target, blocker=blocker)
    raise AssertionError("Every stage path must yield a decision")


def load_state(paths: TaskPaths) -> dict[str, Any] | None:
    if not paths.state_file.exists():
        return None
    data = parse_artifact(paths.state_file.read_text(encoding="utf-8"))
    if data.get("task_id") != paths.task_id or not isinstance(data.get("history"), list) or any(not isinstance(e, dict) for e in data["history"]):
        raise ContractError("Cached state has invalid task identity or history")
    return data


def save_state(paths: TaskPaths, state: dict[str, Any]) -> None:
    paths.state_file.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=paths.state_file.parent, prefix=".state-", delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(json.dumps(state, indent=2, ensure_ascii=False) + "\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, paths.state_file)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def sync_command(task_id: str, *, event: str = "sync") -> dict[str, Any]:
    paths = build_paths(task_id)
    warning = None
    try:
        existing = load_state(paths)
    except (OSError, UnicodeError, ContractError) as exc:
        existing = None
        warning = f"Rebuilt derived state; prior cache could not be read: {exc}"
    state = sync_state(paths, existing)
    if warning:
        state["state_warning"] = warning
    state["history"].append({"at": now_iso(), "event": event, "status": state["status"],
                             "current_stage": state["current_stage"], "next_stage": state["next_stage"],
                             "reason_code": state["reason_code"]})
    save_state(paths, state)
    return state


def init_state(task_id: str) -> dict[str, Any]:
    return sync_command(task_id, event="init")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", action="version", version=VERSION)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("init", "sync", "next", "status", "inputs"):
        command = sub.add_parser(name)
        command.add_argument("task_id")
        if name == "inputs":
            command.add_argument("stage", choices=STAGES)
    args = parser.parse_args(argv)
    try:
        paths = build_paths(args.task_id)
        if args.command == "inputs":
            if args.stage == "reviewer":
                check_review_bundle(paths)
            print(json.dumps({"revision": str(uuid.uuid4()), "input_fingerprints": input_fingerprints(paths, args.stage)}, indent=2))
            return 0
        if args.command in {"init", "sync"}:
            state = sync_command(args.task_id, event=args.command)
            print(json.dumps(state, indent=2, ensure_ascii=False))
            return 0
        state = sync_state(paths)
        if args.command == "status":
            print(f"task={state['task_id']} status={state['status']} current={state['current_stage']} next={state['next_stage']} needs_user_input={state['needs_user_input']}")
        else:
            print("done" if state["status"] == "completed" else "wait" if state["status"] in {"waiting_user", "blocked"} else state["next_stage"] or "wait")
        print(f"{state['reason_code']}: {state['reason']}")
        return 0
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
