{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "implementation_brief",
  "task_id": "case",
  "produced_by": "planner",
  "status": "ready",
  "revision": "e7ca27d5-1f3c-4011-8670-19c02721e1b4",
  "input_fingerprints": {
    "share/case/planner/plan.md": "8715693b3f7be88d54df68559a9e8ff8e603b7b3a7201a7bc5c754896a33afde"
  },
  "input_artifacts": [
    {
      "path": "share/case/planner/plan.md",
      "required": true,
      "summary": "Research strategy and preflight risks for current task."
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
    "Select greatest revision for each id before filtering latest state=active. Lower revisions and canceled or pending latest records contribute nothing.",
    "Inputs have valid ids, revisions, states and integer amounts.",
    "Immutable: records.json, public_check.py, tasker/case.md, rules, README, controller, supplied guidance and audit.",
    "Write only output/report.json, owned stage artifacts, review mirrors and evidence/.",
    "Use python3 -B and controller CLI recorder for all controller operations. No nested agents, Git, network, installs or external actions.",
    "same_invocation fallback retains context and is not independently isolated execution or review.",
    "Regenerate stale stage and descendants from current inputs; do not merely update old hashes."
  ],
  "open_questions": [],
  "evidence": [
    {
      "kind": "execution_mode",
      "source": "research_plan",
      "summary": "same_invocation fallback retains context; no independent stage isolation."
    },
    {
      "kind": "preflight",
      "source": "share/case/planner/plan.md",
      "summary": "Requirements, signed amount handling, stale lineage, validation, cleanup and rollback are defined; no owner decision is missing."
    }
  ],
  "handoff": {
    "next_agent": "implementer",
    "allowed_next_inputs": [
      "share/case/implementer/impl.md",
      "records.json",
      "public_check.py",
      "agent_loop_poc/README.md"
    ],
    "notes": "Implement only the permitted generated report and owned result; retain check evidence for reviewer."
  },
  "summary": "Regenerate output/report.json from latest records before filtering active; expected total 18 and ids a,c,d,f from inspected data.",
  "inputs_used": [
    "share/case/planner/plan.md"
  ],
  "files_likely_to_change": [
    "output/report.json",
    "share/case/reviewer/result.md",
    "evidence/report_contents.json"
  ],
  "ordered_steps": [
    {
      "step": 1,
      "action": "Read records.json and public_check.py, confirming current per-id revision rule.",
      "rationale": "Old synthetic outputs cannot establish current correctness.",
      "expected_evidence": "Latest a=12, b=canceled, c=5, d=-3, e=pending, f=4."
    },
    {
      "step": 2,
      "action": "Build a map keyed by id containing the greatest revision row, then filter active values. Write output/report.json as exactly total integer and lexicographically sorted ids array.",
      "rationale": "Selection order prevents obsolete active rows from contributing.",
      "expected_evidence": "Report {\"total\":18,\"ids\":[\"a\",\"c\",\"d\",\"f\"]}."
    },
    {
      "step": 3,
      "action": "Run python3 -B public_check.py; retain observed exit status and output in evidence/report_contents.json. Also inspect exact keys, types and arithmetic.",
      "rationale": "Required report_contents check establishes current report correspondence.",
      "expected_evidence": "Exit 0 and report_contents: passed."
    },
    {
      "step": 4,
      "action": "Write current implementation_result with actual changes, checks, cleanup and same_invocation limitation; validate saved output using recorder CLI.",
      "rationale": "Handoff requires current artifact evidence.",
      "expected_evidence": "Saved result validated with observed digest outside result artifact."
    }
  ],
  "invariants": [
    "Select maximum revision for each id before active filtering.",
    "Sum negative amounts normally.",
    "No input, rules, controller, audit, peer or historical requirement edits.",
    "Only current producer edits its output.",
    "Report contains exactly total and ids; no annotations."
  ],
  "validation_plan": [
    {
      "check": "report_contents",
      "command_or_method": "python3 -B public_check.py",
      "expected_result": "Exit 0 with report_contents: passed and report total 18, ids a,c,d,f.",
      "required": true
    },
    {
      "check": "report_shape_and_reconciliation",
      "command_or_method": "Inspect parsed output keys and types, verify expected total 12+5-3+4=18 and ids a,c,d,f.",
      "expected_result": "Exact fields total integer and ids array of strings; expected values match.",
      "required": true
    }
  ],
  "cleanup_plan": [
    "Retain stage outputs, report, evidence and automatic audit.",
    "Remove task-created scratch files; no backups or external outputs."
  ],
  "escalation_conditions": [
    {
      "condition": "Current direct workflow input changes or upstream requirements are inconsistent.",
      "return_target": "planner",
      "reason": "Stop and reproduce responsible producer instead of patching hashes."
    },
    {
      "condition": "Success requires immutable edits or relaxed acceptance criteria.",
      "return_target": "researcher",
      "reason": "Preserve scope and obtain owner decision before any requirement changes."
    }
  ],
  "rollback_hints": [
    "Only current in-scope generated outputs may be removed for correction.",
    "Never modify immutable inputs or audit; upstream correction belongs to its producer."
  ],
  "expected_output": {
    "result_artifact_path": "share/case/reviewer/result.md",
    "implementation_summary_requirements": [
      "State exact report output and algorithm.",
      "Record both required checks with evidence, actual cleanup and no external effects.",
      "Record same_invocation retained context and reviewer handoff."
    ]
  },
  "acceptance_criteria": [
    "Greatest revision is selected separately for each id before state filtering.",
    "Only active selected records contribute amount and id.",
    "total is the sum of selected integer amounts; ids are lexicographically sorted.",
    "Report contains exactly total and ids.",
    "Required report_contents check runs python3 -B public_check.py and passes.",
    "All stages validate saved bytes with fresh lineage; reviewer mirrors match canonical files."
  ]
}
