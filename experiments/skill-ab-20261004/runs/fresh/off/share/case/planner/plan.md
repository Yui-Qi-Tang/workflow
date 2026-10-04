{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "research_plan",
  "task_id": "case",
  "produced_by": "researcher",
  "status": "ready",
  "revision": "12b18102-0b30-464c-880a-700e4a63cd05",
  "input_fingerprints": {
    "share/case/researcher/task.md": "67c928fd887904362f1cf9f5bd7ff6da7dc12e842c00b4572ae6b500b62c367f"
  },
  "input_artifacts": [
    {
      "path": "share/case/researcher/task.md",
      "required": true,
      "summary": "Current validated normalized latest-revision report task."
    },
    {
      "path": "records.json",
      "required": false,
      "summary": "Immutable record fixture."
    },
    {
      "path": "public_check.py",
      "required": false,
      "summary": "Immutable required contents validator."
    }
  ],
  "trusted_sources": [
    {
      "path": "AGENTS.md"
    },
    {
      "path": "researcher/AGENTS.md"
    },
    {
      "source": "Outer authorization scopes this trial and same-invocation execution."
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
      "source": "normalized task and outer authorization",
      "summary": "same_invocation; retained context does not provide independent stage isolation or review."
    },
    {
      "kind": "source_inspection",
      "source": "records.json",
      "summary": "a has revisions 1 and 2; b latest revision is canceled; e is pending; d has negative active amount. Expected latest active ids a,c,d,f total 18."
    },
    {
      "kind": "source_inspection",
      "source": "public_check.py",
      "summary": "Selects greatest revision per id before active filtering; compares parsed output to exact expected two-key object. Not executed during research."
    }
  ],
  "handoff": {
    "next_agent": "planner",
    "allowed_next_inputs": [
      "share/case/planner/plan.md",
      "records.json",
      "public_check.py"
    ],
    "notes": "Plan required report_contents check and preserve all immutability, cleanup and rollback limits."
  },
  "task_classification": "bounded_data_report",
  "goal_restatement": "Write output/report.json with exactly total (integer) and ids (array of strings), derived from latest revisions.",
  "requested_change_summary": "Produce latest-revision active-record total and sorted ids as a JSON report, with the full saved and validated workflow chain.",
  "expected_impact_areas": [
    "output/report.json",
    "Required share/case artifacts and review mirrors",
    "evidence/ and automatic controller audit"
  ],
  "assumptions": [
    {
      "id": "valid_input",
      "statement": "Input ids, revisions, states and amounts are valid.",
      "source": "Normalized task acceptance and source summary.",
      "risk_if_wrong": "Report calculation could be undefined; do not invent invalid-input policy."
    }
  ],
  "risks": [
    {
      "id": "filter_order",
      "description": "Filtering active before revision selection revives canceled b.",
      "impact": "Incorrect ids and total.",
      "mitigation": "Select maximum revision across all states first."
    },
    {
      "id": "double_count",
      "description": "Summing both a revisions overcounts.",
      "impact": "Incorrect total.",
      "mitigation": "Use one latest record per id."
    },
    {
      "id": "negative",
      "description": "Dropping negative active d amount violates task.",
      "impact": "Incorrect total and ids.",
      "mitigation": "Include all integer amounts of selected active records."
    },
    {
      "id": "historical_evidence",
      "description": "A synthetic or stale prior result may appear plausible.",
      "impact": "False completion under old task.",
      "mitigation": "Capture current metadata, validate saved bytes and inspect route after each stage."
    }
  ],
  "non_goals": [
    "Edit immutable inputs, controller or rules.",
    "Add policies for invalid data.",
    "Network, installs, Git, subagents or skill body."
  ],
  "high_level_strategy": [
    "Capture current stage lineage; proceed only on permitted route.",
    "Select greatest revision for each id, then active records, then sum and lexicographic id sorting.",
    "Write exactly total integer and ids string array.",
    "Run report_contents using python3 -B public_check.py; validate every saved stage.",
    "Mirror canonical task, plan and impl byte-for-byte before reviewer capture.",
    "Retain report, stage records, evidence and automatic audit; remove own scratch. Rollback only own generated outputs and return upstream corrections to responsible role."
  ],
  "required_checks": [
    "report_contents: python3 -B public_check.py",
    "Verify report keys, integer total and string ids match current latest active semantics.",
    "Every stage saved-output validation and post-validation route check.",
    "Review mirrors identical and four input schema checks passed."
  ],
  "proposed_task_updates": [],
  "failure_modes": [
    {
      "id": "early_filter",
      "trigger": "Active filtering happens before latest revision selection.",
      "likely_stage": "implementer",
      "prevention": "Use latest mapping over every state and expected a,c,d,f total 18 as a cross-check."
    },
    {
      "id": "premature_review",
      "trigger": "Review starts before mirror creation or captures stale inputs.",
      "likely_stage": "reviewer",
      "prevention": "Orchestrator copies canonical bytes, checks route and then captures reviewer metadata."
    },
    {
      "id": "gap_invention",
      "trigger": "A real blocker is discovered.",
      "likely_stage": "planner",
      "prevention": "Stop and record blocking question; do not create report/downstream artifacts."
    }
  ]
}
