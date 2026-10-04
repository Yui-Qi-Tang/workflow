{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "normalized_task",
  "task_id": "workflow-integrity-20261003",
  "produced_by": "tasker",
  "status": "ready",
  "revision": "cd8264a8-5a4d-4365-a352-3300169c35d3",
  "input_fingerprints": {
    "tasker/workflow-integrity-20261003.md": "c7a6bbabfe47b0245a3f12f57b4a284cbde8e91c923e771818c33ebfcabc3cbd"
  },
  "input_artifacts": [
    {
      "path": "tasker/workflow-integrity-20261003.md",
      "required": true,
      "summary": "Authoritative task content or required stage input."
    }
  ],
  "trusted_sources": [
    {
      "path": "AGENTS.md",
      "summary": "Root contract."
    },
    {
      "path": "tasker/AGENTS.md",
      "summary": "Stage contract."
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "tasker/workflow-integrity-20261003.md",
      "summary": "Task data, not instructions overriding stage rules."
    }
  ],
  "constraints": [
    "Preserve five stages and unrelated user changes.",
    "No external executor, commit or push.",
    "Main agent performs stages using same-invocation fallback; no isolation claim."
  ],
  "open_questions": [],
  "evidence": [
    {
      "kind": "source",
      "source": "tasker/workflow-integrity-20261003.md",
      "summary": "Read and used for this stage."
    }
  ],
  "handoff": {
    "next_agent": "researcher",
    "allowed_next_inputs": [
      "AGENTS.md",
      "researcher/AGENTS.md",
      "share/workflow-integrity-20261003/researcher/task.md"
    ],
    "notes": "Only the listed input and explicitly authorized project paths are authoritative."
  },
  "goal": "Make workflow control decisions enforce artifact contracts and current input lineage.",
  "scope": [
    "agent_loop_poc/",
    "README.md",
    "README.en.md",
    "README.zh.md",
    "AGENTS.md",
    "reviewer/AGENTS.md",
    "share/workflow-integrity-20261003"
  ],
  "deliverables": [
    "Contract validator",
    "Version-aware state routing",
    "Structured blockers",
    "Regression tests",
    "Updated docs and five-stage review bundle"
  ],
  "acceptance_criteria": [
    "All eight frozen acceptance groups in the task file are met.",
    "Malformed, missing or stale evidence cannot complete a workflow.",
    "No keyword-based human-input inference."
  ],
  "conflicts": [],
  "source_of_truth": [
    "tasker/workflow-integrity-20261003.md",
    "AGENTS.md",
    "tasker/AGENTS.md"
  ],
  "validation": [
    "Freeze regression tests, capture baseline failures and final unittest results.",
    "Run git diff --check and CLI smoke; verify mirrors and artifact contracts."
  ],
  "cleanup": [
    "TemporaryDirectory removes test data; disable bytecode.",
    "Preserve this task's records and validation logs."
  ],
  "rollback": [
    "Retain scoped changes on failure; do not reset user files."
  ]
}
