{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "implementation_brief",
  "task_id": "case",
  "produced_by": "planner",
  "status": "ready",
  "revision": "a47e5958-3e6a-47cb-bea9-5b99955079e7",
  "input_fingerprints": {
    "share/case/planner/plan.md": "13725a1f11a04c6544b05e8ba45755d2e97e04395a9d41679b204a408e997d92"
  },
  "input_artifacts": [
    {
      "path": "share/case/planner/plan.md",
      "required": true,
      "summary": "Current research plan with selection-order risks and required checks."
    }
  ],
  "trusted_sources": [
    {
      "path": "AGENTS.md"
    },
    {
      "path": "planner/AGENTS.md"
    },
    {
      "source": "Outer authorization for sole same-invocation trial orchestrator."
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "share/case/planner/plan.md"
    }
  ],
  "constraints": [
    "Inputs records.json, public_check.py, tasker/case.md, rules and controller are immutable.",
    "Writes limited to output/report.json when routing permits, required share/case stage outputs and review mirrors, and evidence/. Do not edit automatic audit receipts.",
    "All controller operations use python3 -B agent_loop_poc/loop.py.",
    "No nested agents, skill body, Git, network, installs or access beyond assigned trial root.",
    "If blocked, produce no report or downstream stage."
  ],
  "open_questions": [],
  "evidence": [
    {
      "kind": "execution_mode",
      "source": "research plan and outer authorization",
      "summary": "same_invocation; roles share retained context, so review is not independently isolated."
    },
    {
      "kind": "planning_basis",
      "source": "share/case/planner/plan.md",
      "summary": "Plan preserves latest-before-active selection, required public check, output-only scope, cleanup and rollback. No unresolved execution-critical gap."
    }
  ],
  "handoff": {
    "next_agent": "implementer",
    "allowed_next_inputs": [
      "share/case/implementer/impl.md",
      "records.json",
      "public_check.py"
    ],
    "notes": "Read current fixture, generate report only on permitted route, run named checks and record actual results."
  },
  "summary": "Write output/report.json with exactly total (integer) and ids (array of strings), derived from latest revisions.",
  "inputs_used": [
    "share/case/planner/plan.md"
  ],
  "files_likely_to_change": [
    "output/report.json",
    "share/case/reviewer/result.md",
    "evidence/report_contents.txt",
    "evidence/report_shape.json"
  ],
  "ordered_steps": [
    {
      "step": 1,
      "action": "After route permission and fresh implementer input capture, read records.json and public_check.py.",
      "rationale": "Use immutable current data and prescribed validator.",
      "expected_evidence": "Current data inspected; no immutable edits."
    },
    {
      "step": 2,
      "action": "Build one selected record per id using greatest revision across all states; retain state=active; sum integer amounts and sort ids lexicographically. Write one object with exactly total and ids to output/report.json.",
      "rationale": "Avoid lower-revision double counts and canceled-record revival.",
      "expected_evidence": "Current fixture produces total 18 and ids a,c,d,f."
    },
    {
      "step": 3,
      "action": "Run required report_contents via python3 -B public_check.py, retaining stdout and observed exit status. Run report_shape on saved report for exact keys and integer/string types.",
      "rationale": "Verify semantics and strict requested output shape.",
      "expected_evidence": "Both uniquely named required checks pass with saved evidence."
    },
    {
      "step": 4,
      "action": "Record actual changed files, checks, cleanup and same_invocation limitation in result.md; validate saved implementation artifact using recorder CLI.",
      "rationale": "Make handoff reviewable without claiming unrun checks.",
      "expected_evidence": "Saved result validation exits 0 and digest recorded outside artifact."
    },
    {
      "step": 5,
      "action": "Orchestrator checks route, creates exact canonical task/plan/impl review mirrors, rechecks route and captures reviewer inputs before review.",
      "rationale": "Review needs self-contained current evidence.",
      "expected_evidence": "Mirrors compare equal and reviewer route permitted."
    }
  ],
  "invariants": [
    "Exactly one greatest revision selected for each id before any state filter.",
    "Only latest active ids contribute, including negative amounts; canceled and pending latest records do not.",
    "Report contains exactly integer total and lexicographically sorted string ids.",
    "Immutable inputs, controller, rules and audit must never be edited.",
    "No skipped stages, nested agents, skill body or access outside trial root."
  ],
  "validation_plan": [
    {
      "check": "report_contents",
      "command_or_method": "python3 -B public_check.py",
      "expected_result": "Exit 0 with report_contents: passed for current records.json.",
      "required": true
    },
    {
      "check": "report_shape",
      "command_or_method": "Read saved output/report.json with json.loads; assert one object, exactly keys total and ids, type(total) is int, type(ids) is list, every id is str and ids == sorted(ids).",
      "expected_result": "All strict shape assertions pass; report is total 18 with ids a,c,d,f.",
      "required": true
    }
  ],
  "cleanup_plan": [
    "Retain generated report, stage records, evidence and automatic audit.",
    "Do not create scratch files; remove any own scratch if needed. No backups or installs."
  ],
  "escalation_conditions": [
    {
      "condition": "Needed requirement or owner decision is missing, or constraints require change.",
      "return_target": "tasker",
      "reason": "Record blocker; do not assume authorization or produce downstream/report."
    },
    {
      "condition": "Current implementation check fails due solely to in-scope report mistake.",
      "return_target": "implementer",
      "reason": "Correct own generated output and rerun failed checks without changing criteria."
    },
    {
      "condition": "Research strategy conflicts with current task intent.",
      "return_target": "researcher",
      "reason": "Responsible upstream producer must regenerate affected descendants."
    }
  ],
  "rollback_hints": [
    "Correct or remove only own current generated outputs; never edit immutable inputs, rules, controller, audit or peer paths.",
    "Upstream corrections return to each artifact owner; capture fresh metadata and regenerate descendants."
  ],
  "expected_output": {
    "result_artifact_path": "share/case/reviewer/result.md",
    "implementation_summary_requirements": [
      "Report exact output, actual files changed and observed checks with evidence.",
      "Record cleanup status and intentional retained report, stages, evidence and audit.",
      "Disclose same_invocation retained-context limitation and any actual blocker or deviation."
    ]
  }
}
