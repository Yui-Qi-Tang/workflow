{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "research_plan",
  "task_id": "case",
  "produced_by": "researcher",
  "status": "ready",
  "revision": "b8dfdab6-d952-50d2-b712-6ec3228cd9e1",
  "input_fingerprints": {
    "share/case/researcher/task.md": "1cd729313d2ab10d9e9ee466a05ce0dff9e89dbf163daad3a46c5f9e9f5e14e0"
  },
  "input_artifacts": [
    {
      "path": "share/case/researcher/task.md",
      "required": true,
      "summary": "Synthetic seed direct input."
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
      "path": "records.json"
    }
  ],
  "constraints": [
    "Immutable records, task, rules and tooling.",
    "No external side effects."
  ],
  "open_questions": [],
  "evidence": [
    {
      "kind": "synthetic_seed",
      "source": "Experiment setup",
      "summary": "Main-authored fixture, not a prior model trial or efficacy evidence."
    },
    {
      "kind": "execution_mode",
      "source": "Fixture setup",
      "summary": "same_invocation seed preparation."
    }
  ],
  "handoff": {
    "next_agent": "planner",
    "allowed_next_inputs": [
      "records.json",
      "public_check.py"
    ],
    "notes": "Synthetic seed; current task is authoritative."
  },
  "task_classification": "local_report",
  "goal_restatement": "Compute all active rows under the prior task.",
  "requested_change_summary": "Write the prior all-row report.",
  "expected_impact_areas": [
    "output/report.json"
  ],
  "assumptions": [],
  "risks": [],
  "non_goals": [
    "Change input records"
  ],
  "high_level_strategy": [
    "Filter active rows, sum and sort."
  ],
  "required_checks": [
    "report_contents"
  ],
  "proposed_task_updates": [],
  "failure_modes": []
}
