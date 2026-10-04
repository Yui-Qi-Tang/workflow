{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "implementation_brief",
  "task_id": "case",
  "produced_by": "planner",
  "status": "ready",
  "revision": "1a1e0a0c-7f9f-4699-87eb-01b8f24cd427",
  "input_fingerprints": {
    "share/case/planner/plan.md": "ac718c66a211088dd6835253483535ce908f8e4847289f61de78a1b30d00757d"
  },
  "input_artifacts": [
    {
      "path": "share/case/planner/plan.md",
      "required": true,
      "summary": "Current research plan preserving ordered report computation and checks."
    }
  ],
  "trusted_sources": [
    {
      "path": "AGENTS.md"
    },
    {
      "path": "planner/AGENTS.md"
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "share/case/planner/plan.md"
    }
  ],
  "constraints": [
    "Immutable: records.json, public_check.py, tasker/case.md, role rules, README, controller, supplied guidance and audit logs.",
    "Write only output/report.json when routing permits, required share/case stage outputs and review mirrors, and evidence/.",
    "For each id select greatest revision before retaining only state=active; canceled or pending latest versions exclude the id regardless of earlier active versions.",
    "Use python3 -B agent_loop_poc/loop.py for every controller operation; no imports of its core.",
    "Use same_invocation for all five roles; no nested agents, external actions, installs or Git.",
    "Each producer owns its output; block without report or downstream production if an unresolved decision exists."
  ],
  "open_questions": [],
  "evidence": [
    {
      "kind": "execution_mode",
      "source": "trial authorization and research plan",
      "summary": "same_invocation fallback retains context; implementation and review are not independently isolated."
    },
    {
      "kind": "preflight",
      "source": "share/case/planner/plan.md",
      "summary": "Selection order, signed amounts, exact shape, actual report_contents execution, cleanup and rollback are defined; no blocking question remains."
    }
  ],
  "handoff": {
    "next_agent": "implementer",
    "allowed_next_inputs": [
      "share/case/implementer/impl.md",
      "records.json",
      "public_check.py",
      "AGENTS.md",
      "implementer/AGENTS.md",
      "agent_loop_poc/README.md"
    ],
    "notes": "Write report only after route permits; preserve required check names and observed evidence."
  },
  "summary": "Generate the latest-revision active-record report and preserve actual validation evidence.",
  "inputs_used": [
    "share/case/planner/plan.md"
  ],
  "files_likely_to_change": [
    "output/report.json",
    "evidence/report_contents.json",
    "evidence/report_shape.json",
    "share/case/reviewer/result.md"
  ],
  "ordered_steps": [
    {
      "step": 1,
      "action": "Read records.json; for each id retain the row with greatest revision, irrespective of state.",
      "rationale": "Avoid resurrecting earlier active versions.",
      "expected_evidence": "Latest-row interpretation reflected in result."
    },
    {
      "step": 2,
      "action": "Retain only latest rows whose state is active, sum signed integer amounts and sort ids lexicographically; write output/report.json as one JSON object with exactly total and ids.",
      "rationale": "Implements the task without altering input.",
      "expected_evidence": "Saved report expected total 18 and ids a,c,d,f from current fixture."
    },
    {
      "step": 3,
      "action": "Run python3 -B public_check.py as required report_contents and save command, exit status and stdout/stderr in evidence/report_contents.json. Check report JSON shape and save observed result in evidence/report_shape.json.",
      "rationale": "Task success needs actual semantic and shape checks.",
      "expected_evidence": "Both named required checks passed with saved evidence."
    },
    {
      "step": 4,
      "action": "Record changed files, checks, execution mode, cleanup and remaining risks in the implementation_result; run saved-file validation.",
      "rationale": "Truthful, inspectable handoff.",
      "expected_evidence": "Validated result and controller audit receipt."
    }
  ],
  "invariants": [
    "Immutable inputs, rules, tooling and automatic audit logs remain unedited.",
    "Greatest revision selected before active filtering; signed amounts preserved.",
    "Exact report keys total and ids, integer total and string ids sorted lexicographically.",
    "Only trial-root generated allowlisted outputs may be written.",
    "Do not produce report or descendants if required owner decision blocks execution."
  ],
  "validation_plan": [
    {
      "check": "report_contents",
      "command_or_method": "python3 -B public_check.py",
      "expected_result": "exit 0 and report_contents: passed",
      "required": true
    },
    {
      "check": "report_shape",
      "command_or_method": "Parse output/report.json as one object, assert exactly total and ids, type(total) is int and ids is a list of strings sorted lexicographically.",
      "expected_result": "Assertions pass.",
      "required": true
    }
  ],
  "cleanup_plan": [
    "Retain stage outputs, report, evidence and automatic audit receipts.",
    "Remove self-created scratch files; no backups or dependency installs."
  ],
  "escalation_conditions": [
    {
      "condition": "Correct output requires changing task requirements or immutable inputs.",
      "return_target": "researcher",
      "reason": "Upstream task update needed; do not silently relax scope."
    },
    {
      "condition": "Local report calculation or serialization check fails without upstream gap.",
      "return_target": "implementer",
      "reason": "Self-correct owned generated output within unchanged requirements, rerun checks."
    }
  ],
  "rollback_hints": [
    "Remove only current in-scope generated outputs if correction requires it; immutable inputs and audit remain untouched.",
    "Return upstream corrections to the owning producer and regenerate affected descendants."
  ],
  "expected_output": {
    "result_artifact_path": "share/case/reviewer/result.md",
    "implementation_summary_requirements": [
      "Describe actual report computation and changed files.",
      "Report required report_contents and report_shape results with evidence paths.",
      "Disclose same_invocation retained context and lack of independent isolated review.",
      "State cleanup status and intentional retained outputs."
    ]
  },
  "acceptance_criteria": [
    "Exactly one JSON object with keys total (integer) and ids (array of strings).",
    "Select greatest revision for each id before filtering state=active; sum retained amounts and sort ids lexicographically.",
    "Required implementation check report_contents executes python3 -B public_check.py and passes.",
    "Each stage validates saved bytes; routing is rechecked; review mirrors are byte-identical."
  ],
  "non_goals": [
    "Changing immutable input or tooling",
    "Adding schemas or resolving hypothetical invalid records",
    "External actions, installs, Git, nested agents",
    "Claiming independently isolated review"
  ]
}
