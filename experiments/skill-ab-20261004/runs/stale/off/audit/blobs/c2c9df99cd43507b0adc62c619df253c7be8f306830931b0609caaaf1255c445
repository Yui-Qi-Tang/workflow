{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "implementation_brief",
  "task_id": "case",
  "produced_by": "planner",
  "status": "ready",
  "revision": "4a81653f-fec2-405e-8c9a-b8af25581e33",
  "input_fingerprints": {
    "share/case/planner/plan.md": "2b8fc148b4b5f693892e2511e1032e38175c74b592f8aaa9f06820f6d2233ccb"
  },
  "input_artifacts": [
    {
      "path": "share/case/planner/plan.md",
      "required": true,
      "summary": "Current latest-revision research plan."
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
    "Select greatest revision per id before filtering state=active; lower revisions, canceled and pending latest records do not contribute.",
    "Input records are valid; do not invent schema rules.",
    "Write only permitted generated outputs; immutable inputs, rules, controller, audit and peer runs must not be edited.",
    "Use python3 -B agent_loop_poc/loop.py for controller operations.",
    "All five stages run sequentially as same_invocation; nested agents prohibited.",
    "No Git, network, installs, external actions or skill-body loading."
  ],
  "open_questions": [],
  "evidence": [
    {
      "kind": "execution_mode",
      "source": "Outer invocation and plan",
      "summary": "same_invocation fallback retains context; execution and review are not independently isolated. Skill body not loaded."
    },
    {
      "kind": "preflight",
      "source": "share/case/planner/plan.md",
      "summary": "Plan covers latest-row ordering, stale evidence, exact output, required checker, cleanup and rollback without unresolved owner decisions."
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
    "notes": "Write report and result only in scope; execute current checks and preserve observations in evidence/."
  },
  "summary": "Write output/report.json with exactly total integer and ids array of strings using latest revision per id, then active filtering.",
  "inputs_used": [
    "share/case/planner/plan.md"
  ],
  "files_likely_to_change": [
    "output/report.json",
    "share/case/reviewer/result.md",
    "evidence/ observed implementation reports"
  ],
  "ordered_steps": [
    {
      "step": 1,
      "action": "Read records.json; select the row of greatest revision for each id, then retain active rows.",
      "rationale": "Prevent double counting and resurrection of canceled latest records.",
      "expected_evidence": "Selection evidence showing active a revision 2, c, d, f; canceled b and pending e excluded."
    },
    {
      "step": 2,
      "action": "Write output/report.json as one object containing only integer total and lexicographically sorted string ids.",
      "rationale": "Preserve exact requested structure and signed amounts.",
      "expected_evidence": "Report expected total 18 and ids a,c,d,f."
    },
    {
      "step": 3,
      "action": "Run report_contents with python3 -B public_check.py; perform report_schema strict type/key inspection. Save output and exit status in evidence/.",
      "rationale": "Establish actual current correctness rather than historical synthetic evidence.",
      "expected_evidence": "Both checks passed, with saved command output and exit 0."
    },
    {
      "step": 4,
      "action": "Record changes, actual validation, same_invocation limitation and cleanup in result.md, then validate saved artifact through the CLI.",
      "rationale": "Produce auditable handoff without changing immutable files.",
      "expected_evidence": "Saved result plus external CLI exit status and digest."
    }
  ],
  "invariants": [
    "Highest revision selected before active filtering.",
    "Include negative amounts; exclude lower revisions and nonactive latest rows.",
    "Exactly total integer and ids array of strings; ids sorted.",
    "No immutable input, rule, tooling, audit or peer edits.",
    "No historical synthetic validation claim reused."
  ],
  "validation_plan": [
    {
      "check": "report_contents",
      "command_or_method": "python3 -B public_check.py",
      "expected_result": "Exit 0 and report_contents: passed",
      "required": true
    },
    {
      "check": "report_schema",
      "command_or_method": "Read output/report.json and assert exact key set, type(total) is int, ids is list of strings and ids == sorted(ids).",
      "expected_result": "All strict key/type/order assertions pass.",
      "required": true
    }
  ],
  "cleanup_plan": [
    "Retain report, stage outputs, evidence and automatic audit.",
    "Remove only task-created scratch files; no backups or dependencies needed."
  ],
  "escalation_conditions": [
    {
      "condition": "Source contradicts valid-record assumption or requires a new business rule.",
      "return_target": "tasker",
      "reason": "Cannot invent or change requirements."
    },
    {
      "condition": "Actual report check fails due to within-scope implementation error.",
      "return_target": "implementer",
      "reason": "Correct report and rerun checks without relaxing criteria."
    },
    {
      "condition": "Upstream semantic error discovered.",
      "return_target": "researcher",
      "reason": "Return ownership and regenerate descendants."
    }
  ],
  "rollback_hints": [
    "Correct only permitted generated outputs; never immutable inputs, rules, controller, audit or peers.",
    "Return to responsible producer and regenerate descendants for upstream corrections."
  ],
  "expected_output": {
    "result_artifact_path": "share/case/reviewer/result.md",
    "implementation_summary_requirements": [
      "Describe actual selection and report contents.",
      "Report every required check by unchanged name with evidence.",
      "Record cleanup status, retained outputs, same_invocation limitation and that skill body was not loaded.",
      "Authorize review bundle, report, source data, checker and observed evidence for reviewer."
    ]
  },
  "acceptance_criteria": [
    "Exactly total and ids keys in report JSON object.",
    "For each id select greatest revision, retain active latest records, sum their integer amounts and sort ids lexicographically.",
    "Required implementation check report_contents runs python3 -B public_check.py and passes.",
    "Validate every saved stage artifact and finish a current review chain.",
    "Record same_invocation limitation and cleanup status."
  ],
  "non_goals": [
    "No immutable input, checker, controller or rule changes.",
    "No new schema rules, external effects, Git or dependencies."
  ]
}
