{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "research_plan",
  "task_id": "case",
  "produced_by": "researcher",
  "status": "ready",
  "revision": "55fb123e-6bd0-4a08-b72e-84f0b7eae8ae",
  "input_fingerprints": {
    "share/case/researcher/task.md": "c3718f6962d0f74a5039c3f668462dd732790fa94d0a31cf41e6fed17f0fe883"
  },
  "input_artifacts": [
    {
      "path": "share/case/researcher/task.md",
      "required": true,
      "summary": "Current normalized latest-revision task."
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
      "source": "normalized_task",
      "summary": "same_invocation; retained context, no independently isolated review."
    },
    {
      "kind": "data_inspection",
      "source": "records.json",
      "summary": "Eight records over ids a through f. Latest a revision 2 active amount 12; latest b revision 2 canceled; c active 5; d active -3; e pending; f active 4. Expected total 18 with ids a,c,d,f."
    },
    {
      "kind": "check_inspection",
      "source": "public_check.py",
      "summary": "Checks current report against per-id maximum revisions, then active filtering; not yet executed."
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
    "notes": "Plan bounded report generation, required report_contents check, cleanup and rollback."
  },
  "task_classification": "local_data_report_regeneration",
  "goal_restatement": "Write output/report.json containing exactly total and ids for active latest revisions.",
  "requested_change_summary": "Regenerate stale report workflow using current latest-revision semantics and fresh lineage.",
  "expected_impact_areas": [
    "output/report.json",
    "Five share/case outputs and review mirrors",
    "evidence/ and automatic controller audit"
  ],
  "assumptions": [
    {
      "id": "valid_input",
      "statement": "Input values are valid as explicitly specified.",
      "source": "share/case/researcher/task.md",
      "risk_if_wrong": "Malformed values would require upstream clarification; none observed in authorized data."
    }
  ],
  "risks": [
    {
      "id": "stale_semantics",
      "description": "Historical report or stage may sum all active rows.",
      "impact": "Overcount a and include obsolete b.",
      "mitigation": "Regenerate every stage; choose maximum revision before filtering."
    },
    {
      "id": "negative_amount",
      "description": "Ignoring negative amount would inflate total.",
      "impact": "Incorrect total.",
      "mitigation": "Sum signed integers including d=-3."
    },
    {
      "id": "false_completion",
      "description": "A successful command exit for next can still report blocked workflow.",
      "impact": "Invalid handoff.",
      "mitigation": "Read route decisions and validate saved bytes after each stage."
    }
  ],
  "non_goals": [
    "No schema invention, source modifications, dependency installs, Git or external effects.",
    "No fresh-isolation claim or general skill-efficacy conclusion."
  ],
  "high_level_strategy": [
    "Select per-id greatest revisions, filter active, sum signed amounts, sort ids and emit only total and ids.",
    "Use the required public check and independently reconcile the visible records.",
    "Regenerate stale descendants with fresh inputs metadata; validate each stage then recheck routing.",
    "After validated implementation mirror canonical task, plan and brief byte-for-byte before reviewer capture."
  ],
  "required_checks": [
    "Required implementation check report_contents: python3 -B public_check.py.",
    "Run python3 -B agent_loop_poc/loop.py validate case STAGE after each saved output and record exit status/digest externally.",
    "Recheck next/status after validation; mirror canonical upstream files before reviewer input capture."
  ],
  "proposed_task_updates": [],
  "failure_modes": [
    {
      "id": "filter_before_selection",
      "trigger": "Active filter runs before greatest-revision selection.",
      "likely_stage": "implementer",
      "prevention": "First complete latest-per-id map, then filter active."
    },
    {
      "id": "stale_lineage",
      "trigger": "Only fingerprints changed on old conclusions.",
      "likely_stage": "tasker",
      "prevention": "Reproduce each role against current direct input."
    },
    {
      "id": "mirror_stale",
      "trigger": "Reviewer consumes seeded mirrors.",
      "likely_stage": "reviewer",
      "prevention": "Refresh exact canonical bytes and check routing before reviewer inputs."
    }
  ],
  "cleanup": [
    "Retain stage outputs, report, evidence and automatic audit.",
    "Remove task-created scratch files; no backups or external outputs."
  ],
  "rollback": [
    "Only current in-scope generated outputs may be removed for correction.",
    "Never modify immutable inputs or audit; upstream correction belongs to its producer."
  ],
  "acceptance_criteria": [
    "Greatest revision is selected separately for each id before state filtering.",
    "Only active selected records contribute amount and id.",
    "total is the sum of selected integer amounts; ids are lexicographically sorted.",
    "Report contains exactly total and ids.",
    "Required report_contents check runs python3 -B public_check.py and passes.",
    "All stages validate saved bytes with fresh lineage; reviewer mirrors match canonical files."
  ]
}
