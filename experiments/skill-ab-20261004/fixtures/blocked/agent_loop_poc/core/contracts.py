"""Structural checks for the contracts in the root and stage AGENTS.md files.

This is a bounded contract validator, not a general JSON Schema implementation.
Extra properties are allowed; required properties are checked recursively.
"""

from __future__ import annotations

import json
import math
import re
import uuid
from typing import Any


STAGES = ("tasker", "researcher", "planner", "implementer", "reviewer")
KINDS = ("normalized_task", "research_plan", "implementation_brief", "implementation_result", "workflow_review")
TARGETS = {
    "tasker": ("researcher", "NONE"),
    "researcher": ("planner", "tasker", "NONE"),
    "planner": ("implementer", "researcher", "tasker", "NONE"),
    "implementer": ("reviewer", "planner", "researcher", "tasker", "NONE"),
    "reviewer": ("tasker", "researcher", "planner", "implementer", "NONE"),
}
QUESTION = {"id": str, "question": str, "blocks_execution": bool, "reason": str}
BLOCKER = {
    "kind": ("environment", "requirement", "approval", "artifact", "unknown"),
    "reason": str,
    "stopped_stage": STAGES,
}
COMMON = {
    "schema_version": ("workflow_artifact.v1",),
    "artifact_type": KINDS,
    "task_id": str,
    "produced_by": STAGES,
    "status": str,
    "input_artifacts": [{"path": str, "required": bool, "summary": str}],
    "trusted_sources": [dict],
    "untrusted_inputs_seen": [dict],
    "constraints": [str],
    "open_questions": [QUESTION],
    "evidence": [{"kind": str, "source": str, "summary": str}],
    "handoff": {"next_agent": str, "allowed_next_inputs": [str], "notes": str},
}
FIELDS = {
    "tasker": {
        "goal": str, "scope": [str], "deliverables": [str], "acceptance_criteria": [str],
        "conflicts": [{"id": str, "description": str, "source_excerpt": str, "blocks_execution": bool}],
        "source_of_truth": [str], "validation": [str], "cleanup": [str], "rollback": [str],
    },
    "researcher": {
        "task_classification": str, "goal_restatement": str, "requested_change_summary": str,
        "expected_impact_areas": [str],
        "assumptions": [{"id": str, "statement": str, "source": str, "risk_if_wrong": str}],
        "risks": [{"id": str, "description": str, "impact": str, "mitigation": str}],
        "non_goals": [str], "high_level_strategy": [str], "required_checks": [str],
        "proposed_task_updates": [{"id": str, "description": str, "reason": str, "requires_user_approval": bool}],
        "failure_modes": [{"id": str, "trigger": str, "likely_stage": STAGES, "prevention": str}],
    },
    "planner": {
        "summary": str, "inputs_used": [str], "files_likely_to_change": [str],
        "ordered_steps": [{"step": int, "action": str, "rationale": str, "expected_evidence": str}],
        "invariants": [str],
        "validation_plan": [{"check": str, "command_or_method": str, "expected_result": str, "required": bool}],
        "cleanup_plan": [str],
        "escalation_conditions": [{"condition": str, "return_target": STAGES + ("NONE",), "reason": str}],
        "rollback_hints": [str],
        "expected_output": {"result_artifact_path": str, "implementation_summary_requirements": [str]},
    },
    "implementer": {
        "implementation_summary": str,
        "changed_files": [{"path": str, "change_type": str, "summary": str}],
        "validation_results": [{"check": str, "status": ("passed", "failed", "not_run", "blocked"), "evidence": str, "required": bool}],
        "cleanup_results": [{"item": str, "status": str, "evidence": str}],
        "failure_type": ("none", "implementation_error", "plan_mismatch", "task_conflict", "validation_not_run", "unknown"),
        "failed_step": str, "failure_details": str, "suspected_cause": str,
        "suggested_return_target": STAGES + ("NONE",), "notes": [str],
    },
    "reviewer": {
        "overall_judgment": ("success", "failed"),
        "failure_source": STAGES[:4] + ("NONE",),
        "confidence": ("low", "medium", "high"), "reason": str,
        "recommended_return_target": STAGES[:4] + ("NONE",), "recommended_next_action": str,
        "artifact_schema_checks": [{"artifact": str, "status": ("passed", "failed"), "evidence": str}],
        "notes": [str],
    },
}


class ContractError(ValueError):
    pass


def _unique_object(pairs):
    data = {}
    for key, value in pairs:
        if key in data:
            raise ContractError(f"Duplicate JSON property: {key}")
        data[key] = value
    return data


def _reject_constant(value):
    raise ContractError(f"Non-finite JSON number: {value}")


def _finite_float(value):
    number = float(value)
    if not math.isfinite(number):
        raise ContractError(f"Non-finite JSON number: {value}")
    return number


def parse_artifact(text: str) -> dict[str, Any]:
    try:
        value = json.loads(text, object_pairs_hook=_unique_object, parse_constant=_reject_constant, parse_float=_finite_float)
    except (ValueError, RecursionError) as exc:
        raise ContractError(f"Invalid JSON artifact: {exc}") from exc
    if not isinstance(value, dict):
        raise ContractError("Artifact must be one JSON object; legacy Markdown cannot authorize routing.")
    return value


def _check(value, spec, path, errors):
    if isinstance(spec, dict):
        if not isinstance(value, dict):
            errors.append(f"{path}: expected object")
            return
        for key, child in spec.items():
            if key not in value:
                errors.append(f"{path}.{key}: required")
            else:
                _check(value[key], child, f"{path}.{key}", errors)
    elif isinstance(spec, list):
        if not isinstance(value, list):
            errors.append(f"{path}: expected array")
            return
        for index, child in enumerate(value):
            _check(child, spec[0], f"{path}[{index}]", errors)
    elif isinstance(spec, tuple):
        if not isinstance(value, str) or value not in spec:
            errors.append(f"{path}: expected one of {spec}")
    elif type(value) is not spec:
        errors.append(f"{path}: expected {spec.__name__}")


def needs_user_input(data: dict[str, Any]) -> bool:
    return any(q["blocks_execution"] for q in data["open_questions"]) or any(
        update["requires_user_approval"] for update in data.get("proposed_task_updates", [])
    ) or data.get("blocker", {}).get("kind") == "approval"


def validate_artifact(data: dict[str, Any], stage: str, task_id: str) -> list[str]:
    errors: list[str] = []
    _check(data, COMMON | FIELDS[stage], "$", errors)
    if "blocker" in data:
        _check(data["blocker"], BLOCKER, "$.blocker", errors)
    if errors:
        return errors
    for field in ("trusted_sources", "untrusted_inputs_seen"):
        for entry in data[field]:
            if not any(isinstance(entry.get(key), str) and entry[key].strip() for key in ("path", "source", "rule")):
                errors.append(f"{field}: each entry must identify a path, source or rule")
    index = STAGES.index(stage)
    for field, expected in (("task_id", task_id), ("produced_by", stage), ("artifact_type", KINDS[index])):
        if data[field] != expected:
            errors.append(f"{field}: expected {expected}")
    statuses = ("ready", "blocked") if index < 3 else (
        ("success", "partial_failure", "failed", "blocked") if stage == "implementer" else ("success", "failed")
    )
    if data["status"] not in statuses:
        errors.append(f"status: expected one of {statuses}")
    if "blocker" in data and data["status"] in {"ready", "success"}:
        errors.append("Active blocker cannot accompany ready or successful status.")
    target = data["handoff"]["next_agent"]
    if target not in TARGETS[stage]:
        errors.append(f"handoff.next_agent: illegal target for {stage}")
    if index < 3:
        if data["status"] == "blocked" and target == STAGES[index + 1]:
            errors.append("Blocked pre-implementation artifact cannot hand off forward.")
        if data["status"] == "ready" and target == "NONE":
            errors.append("Ready artifact must name a legal handoff target.")
    if stage == "tasker" and any(c["blocks_execution"] for c in data["conflicts"]) and data["status"] != "blocked":
        errors.append("Blocking task conflicts require blocked status.")
    if stage == "implementer" and data["status"] == "success":
        if data["failure_type"] != "none" or target != "reviewer" or data["suggested_return_target"] != "NONE":
            errors.append("Successful implementation requires no failure and a reviewer handoff.")
        if any(v["required"] and v["status"] != "passed" for v in data["validation_results"]):
            errors.append("Successful implementation requires every required validation to pass.")
    if stage == "implementer":
        checks = data["validation_results"]
        if len({v["check"] for v in checks}) != len(checks):
            errors.append("validation_results: duplicate check names")
        if any(not v["check"].strip() or not v["evidence"].strip() for v in checks):
            errors.append("validation_results: check and evidence must be nonempty")
    if stage == "planner":
        checks = data["validation_plan"]
        if len({v["check"] for v in checks}) != len(checks) or any(not v["check"].strip() for v in checks):
            errors.append("validation_plan: check names must be nonempty and unique")
    if stage == "reviewer":
        if data["status"] != data["overall_judgment"]:
            errors.append("Review status and overall_judgment disagree.")
        if target != data["recommended_return_target"]:
            errors.append("Review return target and handoff disagree.")
        if data["overall_judgment"] == "success":
            if data["failure_source"] != "NONE" or target != "NONE":
                errors.append("Successful review cannot name a failure source or return target.")
            checks = data["artifact_schema_checks"]
            if sorted(c["artifact"] for c in checks) != sorted(KINDS[:4]) or any(c["status"] != "passed" for c in checks):
                errors.append("Successful review requires one passed schema check for each input artifact type.")
    return errors


def validate_lineage(data: dict[str, Any]) -> list[str]:
    errors = []
    try:
        uuid.UUID(data.get("revision", ""))
    except (ValueError, TypeError, AttributeError):
        errors.append("revision: required UUID identifying this production attempt")
    fingerprints = data.get("input_fingerprints")
    if not isinstance(fingerprints, dict) or not fingerprints:
        errors.append("input_fingerprints: required nonempty SHA-256 map; regenerate legacy artifacts")
    elif any(not isinstance(p, str) or not isinstance(h, str) or not re.fullmatch(r"[0-9a-f]{64}", h) for p, h in fingerprints.items()):
        errors.append("input_fingerprints: keys must be input paths and values lowercase SHA-256 digests")
    return errors
