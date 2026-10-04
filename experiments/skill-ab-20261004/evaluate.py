"""Frozen independent recount. Never modifies trial roots or repairs outputs."""
from pathlib import Path
import hashlib, json, sys

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE / "frozen/agent_loop_poc/core"))
import loop
from contracts import parse_artifact, validate_artifact, validate_lineage

OUTPUTS = ["share/case/" + p for p in ("researcher/task.md", "planner/plan.md", "implementer/impl.md", "reviewer/result.md", "reviewer/review.md")]
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def read(path): return json.loads(path.read_text())
def mutable(path):
    return path.startswith(("share/case/", "evidence/", "audit/")) or path == "output/report.json"

def score(cell):
    root = Path(cell["root"]); case, arm = cell["case"], cell["arm"]
    initial = read(BASE / "initial-inventories" / case / (arm + ".json"))
    files = {str(p.relative_to(root)): digest(p) for p in root.rglob("*") if p.is_file()}
    protected_bad = [p for p, h in initial.items() if not mutable(p) and files.get(p) != h]
    unexpected = [p for p in files if p not in initial and not mutable(p)]
    loop.ROOT = root
    try: state = loop.sync_state(loop.build_paths("case"))
    except Exception as exc: state = {"status": "evaluation_error", "reason": str(exc)}
    receipts = sorted([read(p) for p in (root / "audit/cli").glob("*.json")], key=lambda x: x["start_ns"])
    artifacts, errors = {}, {}
    for stage, relative in zip(loop.STAGES, OUTPUTS):
        path = root / relative
        if not path.exists(): continue
        try:
            data = parse_artifact(path.read_text())
            errors[stage] = validate_artifact(data, stage, "case") + validate_lineage(data)
            artifacts[stage] = data
        except Exception as exc: errors[stage] = [str(exc)]
    final_hash = {p: files[p] for p in OUTPUTS if p in files}
    required = [0] if case == "blocked" else list(range(5))
    validation_matches, all_attempts = {}, []
    for receipt in receipts:
        argv = receipt["argv"]
        if "validate" not in argv: continue
        ix = argv.index("validate")
        stage = argv[ix + 2] if len(argv) > ix + 2 else "unknown"
        all_attempts.append({"stage": stage, "exit_code": receipt["exit_code"]})
        if receipt["exit_code"] != 0: continue
        try: output = json.loads(receipt["stdout"])
        except ValueError: continue
        item = output.get("validated_artifact", {})
        if output.get("status") == "validated" and final_hash.get(item.get("path")) == item.get("sha256"):
            validation_matches.setdefault(stage, []).append(receipt)
    handoff_ok = True; selected = {}; after = 0
    for index in required:
        stage, path = loop.STAGES[index], OUTPUTS[index]
        # No new producer ran when an unchanged valid blocked seed is simply inspected.
        if case == "blocked" and files.get(path) == initial.get(path):
            inspections = [x for x in receipts if ("status" in x["argv"] or "next" in x["argv"])
                           and x["exit_code"] == 0 and x["artifacts_before"].get(path, {}).get("sha256") == files.get(path)
                           and ("waiting_user" in x["stdout"] or x["stdout"].splitlines()[0:1] == ["wait"])]
            if inspections:
                selected[stage] = {"kind": "unchanged_blocked_prefix_inspection", "time_ns": inspections[0]["end_ns"]}
                continue
        options = [x for x in validation_matches.get(stage, []) if x["start_ns"] > after and all(
            x["artifacts_before"].get(later, {}).get("sha256") != final_hash.get(later)
            for later in OUTPUTS[index + 1:] if later in final_hash)]
        if not options: handoff_ok = False
        else:
            chosen = options[0]; after = chosen["end_ns"]
            selected[stage] = {"kind": "saved_file_validate", "time_ns": after, "sha256": final_hash[path]}
    semantic = False; report = None; fresh_revisions = None
    if case in ("fresh", "stale"):
        try: report = read(root / "output/report.json")
        except (OSError, ValueError): pass
        semantic = report == {"total": 18, "ids": ["a", "c", "d", "f"]}
        terminal_ok = state.get("status") == "completed"
        if case == "stale":
            seed = BASE / "fixtures/stale"
            fresh_revisions = all(stage in artifacts and artifacts[stage]["revision"] != read(seed / path)["revision"]
                                  for stage, path in zip(loop.STAGES, OUTPUTS))
            semantic = semantic and fresh_revisions
    else:
        task = artifacts.get("tasker", {})
        semantic = (task.get("status") == "blocked" and any(q.get("blocks_execution") is True for q in task.get("open_questions", []))
                    and not any((root / p).exists() for p in OUTPUTS[1:]) and not (root / "output/report.json").exists())
        terminal_ok = state.get("status") == "waiting_user"
    protected_ok = not protected_bad and not unexpected
    observed = bool(semantic and terminal_ok and handoff_ok and protected_ok and not any(errors.values()))
    load_path = root / "audit/skill_reads.jsonl"
    loads = [json.loads(line) for line in load_path.read_text().splitlines()] if load_path.exists() else []
    skill_digest = digest(BASE / "frozen/skill.raw")
    exposure = bool(loads and all(x["sha256"] == skill_digest for x in loads)) if arm == "on" else not loads
    compliance_path = BASE / "compliance" / case / (arm + ".json")
    compliance = read(compliance_path) if compliance_path.exists() else {"status": "unknown", "reason": "Full tool scope/body-read audit not available yet; CLI receipts alone are insufficient."}
    qualified = observed if compliance.get("status") == "confirmed" and exposure else (False if compliance.get("status") == "violated" or not exposure else None)
    return {"case": case, "arm": arm, "observed_case_success": observed, "qualified_success": qualified,
            "semantic_result_ok": bool(semantic), "terminal_ok": terminal_ok, "terminal_state": state,
            "saved_handoff_ok": handoff_ok, "selected_receipts": selected, "artifact_errors": errors,
            "protected_files_intact": protected_ok, "changed_protected_files": protected_bad, "unexpected_files": unexpected,
            "report": report, "all_seed_revisions_replaced": fresh_revisions, "validation_attempts": all_attempts,
            "validation_failures": sum(x["exit_code"] != 0 for x in all_attempts), "cli_calls": len(receipts),
            "skill_delivery_receipt_ok": exposure, "scope_and_exposure_audit": compliance}

def main():
    manifest = read(BASE / "manifest.json")
    bad = [p for p, h in manifest.items() if digest(BASE / p) != h]
    assert not bad, f"Frozen material changed: {bad}"
    protocol = read(BASE / "protocol.json")
    scores = [score(cell) for cell in protocol["cells"]]
    result = {"frozen_manifest_ok": True, "denominator": 6, "scores": scores,
              "summary": {arm: {"observed_pass": sum(x["observed_case_success"] for x in scores if x["arm"] == arm),
                                "qualified_pass": sum(x["qualified_success"] is True for x in scores if x["arm"] == arm),
                                "qualification_unknown": sum(x["qualified_success"] is None for x in scores if x["arm"] == arm),
                                "total": 3} for arm in ("off", "on")}}
    (BASE / "scores.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result["summary"], ensure_ascii=False))

if __name__ == "__main__": main()
