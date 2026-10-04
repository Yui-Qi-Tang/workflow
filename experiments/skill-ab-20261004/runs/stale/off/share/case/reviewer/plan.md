{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "research_plan",
  "task_id": "case",
  "produced_by": "researcher",
  "status": "ready",
  "revision": "fd56c9f6-cbc3-40fc-88ad-824d4436e885",
  "input_fingerprints": {
    "share/case/researcher/task.md": "cd52ae7a3ef3b358515681dae670affa0a949edf478911de7cc1c045f435cbd0"
  },
  "input_artifacts": [
    {
      "path": "share/case/researcher/task.md",
      "required": true,
      "summary": "Current ready normalized latest-revision task."
    }
  ],
  "trusted_sources": [
    {
      "path": "AGENTS.md"
    },
    {
      "path": "researcher/AGENTS.md"
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "share/case/researcher/task.md"
    },
    {
      "path": "records.json"
    },
    {
      "path": "public_check.py"
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
      "source": "Outer invocation and normalized task",
      "summary": "same_invocation fallback retains context and is not independent isolated review; skill body not loaded."
    },
    {
      "kind": "source_inspection",
      "source": "records.json",
      "summary": "a revisions 1/2 active amounts 10/12; b latest revision 2 canceled, e pending, c=5 d=-3 f=4 active. Latest active total should be 18 with a,c,d,f."
    },
    {
      "kind": "validation_inspection",
      "source": "public_check.py",
      "summary": "Checker selects latest revisions first then active rows and compares report object equality."
    }
  ],
  "handoff": {
    "next_agent": "planner",
    "allowed_next_inputs": [
      "share/case/planner/plan.md",
      "records.json",
      "public_check.py",
      "agent_loop_poc/README.md"
    ],
    "notes": "Translate strategy and all constraints into bounded steps; no pending owner decision identified."
  },
  "task_classification": "bounded_data_report",
  "goal_restatement": "Write output/report.json with exactly total integer and ids array of strings using latest revision per id, then active filtering.",
  "requested_change_summary": "Regenerate a stale workflow chain and report using current greatest-revision semantics.",
  "expected_impact_areas": [
    "Read records.json and public_check.py.",
    "Write output/report.json, required share/case stage outputs and mirrors, and observed reports under evidence/."
  ],
  "assumptions": [
    {
      "id": "valid_records",
      "statement": "All ids, revisions, states and amounts are valid as supplied.",
      "source": "Normalized task from current human task",
      "risk_if_wrong": "Input repair would need a requirement decision; do not invent rules."
    }
  ],
  "risks": [
    {
      "id": "filter_order",
      "description": "Filtering active first would resurrect canceled b.",
      "impact": "Wrong total and ids.",
      "mitigation": "Select maximum revision for each id before filtering."
    },
    {
      "id": "historical_evidence",
      "description": "Seeded earlier results may appear complete despite changed task.",
      "impact": "False completion or stale review.",
      "mitigation": "Reproduce each descendant with fresh metadata and actual checks."
    }
  ],
  "non_goals": [
    "No immutable input, checker, controller or rule changes.",
    "No new schema rules, external effects, Git or dependencies."
  ],
  "high_level_strategy": [
    "Preserve highest revision row for each id; filter the selected rows by active state.",
    "Sum integer amounts including negatives and sort retained ids lexicographically.",
    "Produce exact report object and execute required report_contents check.",
    "Preserve task workflow records and observed evidence; remove own scratch if any.",
    "Regenerate every downstream stage, validate actual bytes, mirror canonical files and review current chain."
  ],
  "required_checks": [
    "report_contents: python3 -B public_check.py",
    "Exact report object keys total and ids; integer total and string array ids.",
    "Saved-output CLI validation for every stage; byte-identical review mirrors."
  ],
  "proposed_task_updates": [],
  "failure_modes": [
    {
      "id": "double_count",
      "trigger": "Summing all active rows retains lower revision of a.",
      "likely_stage": "implementer",
      "prevention": "Greatest revision selection precedes sum."
    },
    {
      "id": "canceled_latest",
      "trigger": "Filtering active before latest selection includes b revision 1.",
      "likely_stage": "implementer",
      "prevention": "Filter only selected latest rows."
    },
    {
      "id": "stale_review",
      "trigger": "Reuse synthetic historical checks or stale mirrors.",
      "likely_stage": "reviewer",
      "prevention": "Require current checks, new metadata and byte-identical review mirrors."
    }
  ],
  "cleanup": [
    "Retain report, stage outputs, evidence and automatic audit.",
    "Remove only task-created scratch files; no backups or dependencies needed."
  ],
  "rollback": [
    "Correct only permitted generated outputs; never immutable inputs, rules, controller, audit or peers.",
    "Return to responsible producer and regenerate descendants for upstream corrections."
  ],
  "acceptance_criteria": [
    "Exactly total and ids keys in report JSON object.",
    "For each id select greatest revision, retain active latest records, sum their integer amounts and sort ids lexicographically.",
    "Required implementation check report_contents runs python3 -B public_check.py and passes.",
    "Validate every saved stage artifact and finish a current review chain.",
    "Record same_invocation limitation and cleanup status."
  ],
  "deliverables": [
    "output/report.json",
    "Five current JSON stage artifacts under share/case and byte-identical reviewer mirrors.",
    "Observed validation evidence under evidence/ and automatic controller audit."
  ]
}
