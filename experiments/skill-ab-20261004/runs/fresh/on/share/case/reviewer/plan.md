{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "research_plan",
  "task_id": "case",
  "produced_by": "researcher",
  "status": "ready",
  "revision": "22eda9e5-b153-4ce8-b8b6-a7a844bf807a",
  "input_fingerprints": {
    "share/case/researcher/task.md": "949064042bb7cf858769dbb6930d54d054478d22f4426cff7dace20e1ec0298a"
  },
  "input_artifacts": [
    {
      "path": "share/case/researcher/task.md",
      "required": true,
      "summary": "Normalized current report task."
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
      "source": "trial authorization and normalized task",
      "summary": "same_invocation fallback retains context and provides no independent stage isolation or review."
    },
    {
      "kind": "source_inspection",
      "source": "records.json",
      "summary": "Latest a is revision 2 amount 12; latest b is canceled; c=5, d=-3, f=4 are active, e is pending. Expected retained ids a,c,d,f, total 18."
    },
    {
      "kind": "source_inspection",
      "source": "public_check.py",
      "summary": "Checker selects greatest revision before active filtering and compares parsed report to expected values; execution not_run at this pre-implementation stage."
    }
  ],
  "handoff": {
    "next_agent": "planner",
    "allowed_next_inputs": [
      "share/case/planner/plan.md",
      "records.json",
      "public_check.py",
      "AGENTS.md",
      "planner/AGENTS.md",
      "agent_loop_poc/README.md"
    ],
    "notes": "Preserve report rule, required check report_contents, cleanup and rollback. No unresolved owner decisions."
  },
  "task_classification": "bounded_local_report",
  "goal_restatement": "Produce output/report.json with exactly integer total and an array of string ids, computed from each id greatest revision followed by active filtering.",
  "requested_change_summary": "Generate exactly total and sorted ids from greatest-revision active records; retain full workflow evidence.",
  "expected_impact_areas": [
    "output/report.json",
    "Required share/case artifacts and review mirrors",
    "evidence/ and automatic audit receipts"
  ],
  "assumptions": [
    {
      "id": "valid_input",
      "statement": "Ids, revisions, states and amounts are valid as stated by the task.",
      "source": "normalized task and current records.json",
      "risk_if_wrong": "Would require an upstream task clarification; do not invent repair rules."
    }
  ],
  "risks": [
    {
      "id": "selection_order",
      "description": "Filtering active before revision selection resurrects canceled id b.",
      "impact": "Wrong ids and total.",
      "mitigation": "Reduce by greatest revision first, then filter active."
    },
    {
      "id": "signs",
      "description": "Dropping negative amount d changes the required total.",
      "impact": "Incorrect integer total.",
      "mitigation": "Sum signed amounts unchanged."
    },
    {
      "id": "evidence",
      "description": "Schema validation alone does not prove the report calculation.",
      "impact": "False success report.",
      "mitigation": "Run required public check and inspect report shape; record actual results."
    }
  ],
  "non_goals": [
    "Changing immutable input or tooling",
    "Adding schemas or resolving hypothetical invalid records",
    "External actions, installs, Git, nested agents",
    "Claiming independently isolated review"
  ],
  "high_level_strategy": [
    "After permitted route and fresh metadata, implementer reads records.json, chooses each id greatest revision, filters state=active, sums integer amount, sorts ids and writes one JSON object with exactly total and ids.",
    "Run required report_contents using python3 -B public_check.py and check exact JSON shape.",
    "Record actual result and cleanup; validate saved result, mirror canonical artifacts byte-for-byte, capture reviewer input only after mirrors, review and validate."
  ],
  "required_checks": [
    "report_contents: python3 -B public_check.py must pass.",
    "Exact output shape: one object with only total integer and ids array of strings.",
    "Each saved stage validation exits 0; routing rechecked; review mirrors byte-identical."
  ],
  "proposed_task_updates": [],
  "failure_modes": [
    {
      "id": "stale_active",
      "trigger": "An earlier active record precedes latest canceled record for b.",
      "likely_stage": "implementer",
      "prevention": "Choose greatest revision regardless of state before filtering."
    },
    {
      "id": "old_success",
      "trigger": "Historical artifacts claim success without current input lineage or command evidence.",
      "likely_stage": "reviewer",
      "prevention": "Validate current chain and use current saved report plus observed check evidence."
    }
  ],
  "cleanup": [
    "Retain stage outputs, report, evidence and automatic audit receipts.",
    "Remove self-created scratch files; no backups or dependency installs."
  ],
  "rollback": [
    "Remove only current in-scope generated outputs if correction requires it; immutable inputs and audit remain untouched.",
    "Return upstream corrections to the owning producer and regenerate affected descendants."
  ],
  "acceptance_criteria": [
    "Exactly one JSON object with keys total (integer) and ids (array of strings).",
    "Select greatest revision for each id before filtering state=active; sum retained amounts and sort ids lexicographically.",
    "Required implementation check report_contents executes python3 -B public_check.py and passes.",
    "Each stage validates saved bytes; routing is rechecked; review mirrors are byte-identical."
  ]
}
