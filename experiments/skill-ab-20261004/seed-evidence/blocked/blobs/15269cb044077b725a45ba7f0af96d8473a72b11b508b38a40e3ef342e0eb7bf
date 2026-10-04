{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "normalized_task",
  "task_id": "case",
  "produced_by": "tasker",
  "status": "blocked",
  "revision": "b9b9823e-3d31-55f2-b541-31630c747ac8",
  "input_fingerprints": {
    "tasker/case.md": "d60dfef143f4484b9b4ada53a45afd4e6b58182e21fb8410f507d8f9f5628e7b"
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
  "open_questions": [
    {
      "id": "revision_policy",
      "question": "Should older active revisions contribute?",
      "blocks_execution": true,
      "reason": "Owner choice is required and absent."
    }
  ],
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
    "next_agent": "NONE",
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
