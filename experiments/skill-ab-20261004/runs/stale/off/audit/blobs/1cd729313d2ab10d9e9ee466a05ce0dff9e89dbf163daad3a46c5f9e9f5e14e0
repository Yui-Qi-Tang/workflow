{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "normalized_task",
  "task_id": "case",
  "produced_by": "tasker",
  "status": "ready",
  "revision": "0851eab0-ad66-5a19-a7c1-81efa7a5607c",
  "input_fingerprints": {
    "tasker/case.md": "989763e3825cfa61f8ecd95c004f16678a26c34106f552bd092d0b18393c99db"
  },
  "input_artifacts": [
    {
      "path": "tasker/case.md",
      "required": true,
      "summary": "Synthetic seed direct input."
    }
  ],
  "trusted_sources": [
    {
      "path": "AGENTS.md"
    },
    {
      "path": "tasker/AGENTS.md"
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
    "next_agent": "researcher",
    "allowed_next_inputs": [
      "records.json",
      "public_check.py"
    ],
    "notes": "Synthetic seed; current task is authoritative."
  },
  "goal": "Produce the report under the task's selected revision policy.",
  "scope": [
    "output/report.json"
  ],
  "deliverables": [
    "JSON report"
  ],
  "acceptance_criteria": [
    "Correct total and sorted ids"
  ],
  "conflicts": [],
  "source_of_truth": [
    "tasker/case.md",
    "records.json"
  ],
  "validation": [
    "report_contents"
  ],
  "cleanup": [
    "Remove scratch only"
  ],
  "rollback": [
    "Remove generated output only"
  ]
}
