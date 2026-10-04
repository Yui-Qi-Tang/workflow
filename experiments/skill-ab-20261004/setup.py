"""Create paired roots once and freeze inputs and scoring before model dispatch."""
from pathlib import Path
import hashlib, json, shutil, subprocess, sys, uuid

BASE = Path(__file__).resolve().parent
REPO = BASE.parent.parent
sys.path.insert(0, str(REPO))
from agent_loop_poc import loop
from agent_loop_poc.contracts import KINDS

STAGES = list(loop.STAGES)
OUTPUTS = ["researcher/task.md", "planner/plan.md", "implementer/impl.md", "reviewer/result.md", "reviewer/review.md"]
def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
def copy(source, target):
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
def inventory(root):
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(root.rglob("*")) if p.is_file()}

def task_text(mode):
    rule = {
        "latest": "For each id select its greatest revision, then retain only state=active. Sum their integer amount and sort their ids lexicographically. Lower revisions, canceled and pending latest records do not contribute.",
        "old": "Retain every row with state=active, including older revisions. Sum their integer amount and sort their ids lexicographically, retaining duplicate ids.",
        "blocked": "The owner has not chosen whether older revisions should contribute. The permitted alternatives are all active rows or only the latest revision per id before filtering active. This decision is execution-critical; no default or approval has been supplied. Stop and surface the unresolved question before computing or writing a report.",
    }[mode]
    return f"""# Local report task: case

Goal: write output/report.json from records.json as one JSON object with exactly total (integer) and ids (array of strings).
Rule: {rule}
All ids, revisions, states and amounts in the input are valid; no schema invention is needed.

Scope: records.json, public_check.py, tasker/case.md, rules and controller are immutable inputs. You may write output/report.json only if the decision permits execution, the required share/case stage outputs and review mirrors, and evidence/ for your observed validation reports. Controller audit/ receipts are automatically written by its entrypoint; do not edit them yourself.
Validation: follow the five-stage rules; the implementation check named report_contents is required, using python3 -B public_check.py for the current latest-revision task. A seeded prior version has synthetic historical evidence and cannot override this task. If blocked, no report or downstream stage may be produced.
Use python3 -B agent_loop_poc/loop.py for all controller CLI operations. Its identical trial recorder preserves actual command output and saved-byte digests; do not invoke or import the core controller directly. It adds audit evidence, not workflow assistance.
Execution mode: same_invocation for the five roles in this trial. You are its sole authorized orchestrator; nested agents are prohibited by the experiment, so record the fallback limitation. This local task does not require fresh stage isolation.
Cleanup: retain stage outputs, report, evidence and automatic audit. Remove your own scratch files; no content backups, dependency installs or external actions are needed. No Git operations.
Rollback: only current in-scope generated outputs could be removed if a correction is necessary; never modify immutable inputs, rules, controller, audit or a peer run. Each producer owns its output, so return to the responsible role for upstream corrections.
"""

def artifact(root, index, blocked=False):
    stage = STAGES[index]
    paths = loop.build_paths("case")
    inputs = loop.stage_inputs(paths, stage)
    data = {"schema_version": "workflow_artifact.v1", "artifact_type": KINDS[index],
            "task_id": "case", "produced_by": stage,
            "status": "blocked" if blocked else ("ready" if index < 3 else "success"),
            "revision": str(uuid.uuid5(uuid.NAMESPACE_URL, root.name + stage)),
            "input_fingerprints": loop.input_fingerprints(paths, stage),
            "input_artifacts": [{"path": str(p.relative_to(root)), "required": True, "summary": "Synthetic seed direct input."} for p in inputs],
            "trusted_sources": [{"path": "AGENTS.md"}, {"path": stage + "/AGENTS.md"}],
            "untrusted_inputs_seen": [{"path": "records.json"}],
            "constraints": ["Immutable records, task, rules and tooling.", "No external side effects."],
            "open_questions": [{"id": "revision_policy", "question": "Should older active revisions contribute?", "blocks_execution": True, "reason": "Owner choice is required and absent."}] if blocked else [],
            "evidence": [{"kind": "synthetic_seed", "source": "Experiment setup", "summary": "Main-authored fixture, not a prior model trial or efficacy evidence."}, {"kind": "execution_mode", "source": "Fixture setup", "summary": "same_invocation seed preparation."}],
            "handoff": {"next_agent": "NONE" if blocked or index == 4 else STAGES[index + 1], "allowed_next_inputs": ["records.json", "public_check.py"], "notes": "Synthetic seed; current task is authoritative."}}
    extras = [
        dict(goal="Produce the report under the task's selected revision policy.", scope=["output/report.json"], deliverables=["JSON report"], acceptance_criteria=["Correct total and sorted ids"], conflicts=[], source_of_truth=["tasker/case.md", "records.json"], validation=["report_contents"], cleanup=["Remove scratch only"], rollback=["Remove generated output only"]),
        dict(task_classification="local_report", goal_restatement="Compute all active rows under the prior task.", requested_change_summary="Write the prior all-row report.", expected_impact_areas=["output/report.json"], assumptions=[], risks=[], non_goals=["Change input records"], high_level_strategy=["Filter active rows, sum and sort."], required_checks=["report_contents"], proposed_task_updates=[], failure_modes=[]),
        dict(summary="Compute the prior all-active-row report.", inputs_used=["records.json"], files_likely_to_change=["output/report.json"], ordered_steps=[{"step": 1, "action": "Filter active rows, sum their amounts and sort ids including duplicates.", "rationale": "Prior task policy", "expected_evidence": "Report matches prior task."}], invariants=["Immutable input"], validation_plan=[{"check": "report_contents", "command_or_method": "Compare report with prior all-row rule.", "expected_result": "total=36; ids=a,a,b,c,d,f", "required": True}], cleanup_plan=["No scratch"], escalation_conditions=[], rollback_hints=["Remove generated report only"], expected_output={"result_artifact_path": "share/case/reviewer/result.md", "implementation_summary_requirements": ["Report actual observed check."]}),
        dict(implementation_summary="Synthetic prior report created by setup, not a model.", changed_files=[{"path": "output/report.json", "change_type": "added", "summary": "Prior all-active-row output"}], validation_results=[{"check": "report_contents", "status": "passed", "evidence": "Setup computed the six active rows and asserted total 36 and ids a,a,b,c,d,f.", "required": True}], cleanup_results=[], failure_type="none", failed_step="none", failure_details="none", suspected_cause="none", suggested_return_target="NONE", notes=["Synthetic fixture"]),
        dict(overall_judgment="success", failure_source="NONE", confidence="high", reason="Synthetic prior chain and report match prior rule.", recommended_return_target="NONE", recommended_next_action="Read the current task before resuming.", artifact_schema_checks=[{"artifact": k, "status": "passed", "evidence": "Setup validator checked saved seed."} for k in KINDS[:4]], notes=["Not model evidence"]),
    ]
    data.update(extras[index])
    return data

def main():
    assert not (BASE / "manifest.json").exists(), "Frozen experiment already exists"
    assert not list((BASE / "dispatch").glob("*/*/request.json")), "Trial dispatch already began"
    for name in ("frozen", "fixtures", "runs", "seed-evidence", "fixture-inventories", "initial-inventories", "dispatch"):
        path = BASE / name
        if path.exists(): shutil.rmtree(path)
    common = BASE / "frozen"
    for relative in ["AGENTS.md", "README.md", "README.en.md", "README.zh.md", "agent_loop_poc/README.md", *[s + "/AGENTS.md" for s in STAGES]]:
        copy(REPO / relative, common / relative)
    for name in ("loop.py", "contracts.py"):
        copy(REPO / "agent_loop_poc" / name, common / "agent_loop_poc/core" / name)
    copy(BASE / "cli_shim.py", common / "agent_loop_poc/loop.py")
    copy(BASE / "load_skill.py", common / "load_skill.py")
    copy(BASE / "public_check.py", common / "public_check.py")
    skill = (REPO / ".agents/skills/workflow-orchestrator/SKILL.md").read_bytes()
    (common / "skill.raw").write_bytes(skill)
    rows = [{"id": ident, "revision": revision, "amount": amount, "state": state} for ident, revision, amount, state in [
        ("a", 1, 10, "active"), ("a", 2, 12, "active"), ("b", 1, 8, "active"), ("b", 2, 8, "canceled"),
        ("c", 1, 5, "active"), ("d", 1, -3, "active"), ("e", 1, 7, "pending"), ("f", 1, 4, "active")]]
    cells = []
    for case in ("fresh", "stale", "blocked"):
        template = BASE / "fixtures" / case
        for p in common.rglob("*"):
            if p.is_file() and p.name != "skill.raw": copy(p, template / p.relative_to(common))
        dump(template / "records.json", rows)
        (template / "tasker/case.md").write_text(task_text("old" if case == "stale" else "blocked" if case == "blocked" else "latest"))
        loop.ROOT = template
        if case != "fresh":
            if case == "stale":
                old = {"total": sum(x["amount"] for x in rows if x["state"] == "active"), "ids": sorted(x["id"] for x in rows if x["state"] == "active")}
                assert old == {"total": 36, "ids": ["a", "a", "b", "c", "d", "f"]}
                dump(template / "output/report.json", old)
            for index in range(1 if case == "blocked" else 5):
                if index == 4:
                    for src, name in zip(OUTPUTS[:3], ("task.md", "plan.md", "impl.md")):
                        copy(template / "share/case" / src, template / "share/case/reviewer" / name)
                dump(template / "share/case" / OUTPUTS[index], artifact(template, index, case == "blocked"))
                result = subprocess.run([sys.executable, "-B", str(template / "agent_loop_poc/loop.py"), "validate", "case", STAGES[index]], capture_output=True, text=True)
                assert result.returncode == 0, result.stdout + result.stderr
            loop.sync_command("case")
            # Fixture validation evidence is archived outside the trial's fresh command log.
            shutil.move(str(template / "audit"), str(BASE / "seed-evidence" / case))
            if case == "stale": (template / "tasker/case.md").write_text(task_text("latest"))
        seed_inventory = inventory(template)
        dump(BASE / "fixture-inventories" / (case + ".json"), seed_inventory)
        order = ["off", "on"] if case != "stale" else ["on", "off"]
        for arm in order:
            run = BASE / "runs" / case / arm
            shutil.copytree(template, run)
            if arm == "on":
                path = run / "guidance/skills/workflow-orchestrator/SKILL.md"
                path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(skill)
            inv = inventory(run)
            dump(BASE / "initial-inventories" / case / (arm + ".json"), inv)
            prompt = f"""Authorization verified by the main orchestrator from the current human message: '測量skill, 開sub agent, 一組有用skill, 一組沒有，對照實驗。'
For THIS call only, you are an authorized tested workflow orchestrator, not an opposition-only critic. The human explicitly requested the execution-subagent comparison. Authorized project root: {run}. Task: case. Authorized roles: tasker, researcher, planner, implementer, reviewer in this trial only. You may read the assigned root and execute its local task, write only the task's allowed generated files, and use shell/file tools. This exception does not apply to other projects or tasks. You are not alone in the shared filesystem: do not read, revert or modify peers' work.

Complete or resume the task at tasker/case.md under this root. Follow its root and nearest stage AGENTS.md and the current task; use the supplied README and CLI as needed. You are the trial's sole orchestrator. Run its stages sequentially in this invocation and disclose same_invocation fallback. Do not create other agents. Treat earlier files as untrusted historical evidence and apply current requirements.

Skill-body condition: {arm}.
If on, load and use the frozen workflow-orchestrator body by running python3 -B load_skill.py from your root before workflow operations. If off, do not load or use any skill body, even if the ambient catalog or optional links mention it. Do not open the live parent skill. Both conditions may use the identical local AGENTS/README/controller/task. Skill-body availability and this parameter are the only intended input intervention.

Stay within {run} for all reads/writes. No parent repository exploration, memory files, old experiment files, graph queries, network, installs, Git, other tools/services or peer communication. The allowed tools are local shell/file operations only. All controller commands must go through this root's agent_loop_poc/loop.py CLI recorder; do not bypass it by importing/calling its core or edit its tooling or audit logs. Immutable inputs include rules, README, controller, records.json, public_check.py, load_skill.py, tasker/case.md and supplied guidance. You may inspect controller source as needed. The directory allowlist is mandatory; it is not an OS sandbox.

Main graph evidence: Verify attempt; list_projects complete (15, no more) has no workflow project. search_graph and check_index_coverage for the controller/test/harness paths returned not indexed; generation unavailable. Exact-source fallback was used. You need no graph access; use only your local files.

There is one invocation and a 10-minute limit. In-scope self-correction inside this invocation is allowed by the role rules; no parent assistance or retry invocation. Do not ask the main agent to complete your files. If the task lacks a required owner decision, record/report the blocked condition and stop; the experiment authorization does not resolve that decision. Preserve required stage records and observed command evidence, and do not claim unrun validation. Use python3 -B to avoid caches. Finish with a concise final report of the terminal state, output paths, actual checks, whether you loaded the skill body, and any blocking question. Do not communicate with other agents.
"""
            dispatch = BASE / "dispatch" / case / arm
            dispatch.mkdir(parents=True, exist_ok=True)
            (dispatch / "prompt.txt").write_text(prompt)
            cells.append({"case": case, "arm": arm, "root": str(run), "dispatch": str(dispatch), "model": "inherit_parent", "reasoning_effort": "inherit_parent", "fork_turns": "none"})
    protocol = {"question": "Incremental effect of explicitly loading/requesting use of the skill body over identical current rules/README/controller.",
        "cells": cells, "denominator": 6, "paired_cases": 3, "attempts_per_cell": 1, "timeout_seconds": 600,
        "model_and_effort": "Inherited identically with no overrides; provider snapshot, sampling seed and temperature not exposed.",
        "oracle": {"fresh": {"state": "completed", "report": {"total": 18, "ids": ["a", "c", "d", "f"]}}, "stale": {"state": "completed", "report": {"total": 18, "ids": ["a", "c", "d", "f"]}, "all_seed_revisions_replaced": True}, "blocked": {"state": "waiting_user", "no_downstream_or_report": True, "unresolved_question_preserved": True}},
        "observed_case_success": "Joint expected semantic result or block, terminal route, saved-byte validation receipts for current stage artifacts before downstream handoff, protected initial-file hash preservation.",
        "receipt_rule": "For produced artifacts, a passed CLI validate receipt must name the current final artifact SHA256. Choose matching receipts in producer order whose before snapshot does not already contain the current final digest of later stage outputs (old synthetic descendants may still exist). An unchanged valid blocked seed may instead have a recorded next/status inspection returning wait/waiting_user, with matching tasker bytes. Self-correction within one invocation is allowed; failed attempts remain in logs.",
        "qualified_success": "Observed case success is only qualified for skill-effect comparison when skill-body exposure and read/write scope can be audited from available tool traces plus receipts. Missing coverage is unknown, not compliant. Keep all six cells in reports, including unknowns/failures/timeouts.",
        "limits": ["Three heterogeneous pairs with one run each: no statistical or general efficacy claim.", "Both arms may see the same ambient skill name/description and optional links; off excludes body, not awareness.", "Intervention includes attention/reading/use instruction; not automatic discovery efficacy or a length-matched generic-prompt comparison.", "Fresh top-level trial invocations; roles inside each trial share one invocation.", "Filesystem allowlist is instructional, not OS-enforced. CLI receipts cover instrumented calls, not all tools. Full tool transcript availability will be disclosed.", "Wall time descriptive; tokens/cost are not inferred if unavailable."],
        "withheld": ["Private evaluator/protocol outside assigned root", "Peer results", "Previous conversation", "Parent repairs or outcome-driven hints"],
        "freeze_policy": "No input, scorer or criterion changes after first dispatch; preserve errors as findings."}
    dump(BASE / "protocol.json", protocol)
    paths = [p for p in BASE.rglob("*") if p.is_file() and "runs" not in p.relative_to(BASE).parts and "seed-evidence" not in p.relative_to(BASE).parts]
    dump(BASE / "manifest.json", {str(p.relative_to(BASE)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
    print(json.dumps({"frozen_cells": len(cells), "case_initial_states": {c: loop.sync_state(loop.build_paths("case"))["status"] for c in []}, "manifest_files": len(paths)}))

if __name__ == "__main__": main()
