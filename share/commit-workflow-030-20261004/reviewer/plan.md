{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "research_plan",
  "task_id": "commit-workflow-030-20261004",
  "produced_by": "researcher",
  "status": "ready",
  "revision": "0e9482c7-da94-424a-be27-2cb320ee08f2",
  "input_fingerprints": {
    "share/commit-workflow-030-20261004/researcher/task.md": "2bd27e2e05ebce039b08d7ed1b46d049b9d66a9d44d038f14acc6be5b50d8d22"
  },
  "input_artifacts": [
    {
      "path": "share/commit-workflow-030-20261004/researcher/task.md",
      "required": true,
      "summary": "Direct workflow input"
    }
  ],
  "trusted_sources": [
    {
      "path": "AGENTS.md",
      "summary": "Workflow contract"
    },
    {
      "path": "researcher/AGENTS.md",
      "summary": "Stage requirements"
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "share/commit-workflow-030-20261004/researcher/task.md",
      "summary": "Task/handoff data"
    }
  ],
  "constraints": [
    "Explicit allowlist only; preserve excluded go-worker files.",
    "Local commit after preparation/review; no push or product edits.",
    "Main owns stages using same-invocation fallback."
  ],
  "open_questions": [],
  "evidence": [
    {
      "kind": "user_request",
      "source": "tasker/commit-workflow-030-20261004.md",
      "summary": "Current human request authorizes local commit."
    }
  ],
  "handoff": {
    "next_agent": "planner",
    "allowed_next_inputs": [
      "share/commit-workflow-030-20261004/planner/plan.md"
    ],
    "notes": "Final Git publication follows successful review; no commit success is assumed."
  },
  "task_classification": "local_commit_preparation",
  "goal_restatement": "Commit current workflow work with a bounded, verified index.",
  "requested_change_summary": "No implementation changes; stage, verify and locally commit completed work.",
  "expected_impact_areas": [
    "Git index/history",
    "This preparation bundle"
  ],
  "assumptions": [],
  "risks": [
    {
      "id": "R1",
      "description": "Blanket git add would include unrelated go-worker records.",
      "impact": "Incorrect commit scope.",
      "mitigation": "Explicit path allowlist and exact index comparison."
    },
    {
      "id": "R2",
      "description": "Historical raw failures might be rewritten by rerunning evaluation.",
      "impact": "Loss of original evidence.",
      "mitigation": "Hash-verify only; no experiment reruns."
    }
  ],
  "non_goals": [
    "Push",
    "New features",
    "Model retest"
  ],
  "high_level_strategy": [
    "Define allowlist and preserve exclusions.",
    "Run checks and complete bundle review.",
    "Stage exact reviewed files, verify index, commit and inspect Git result."
  ],
  "required_checks": [
    "unit_tests",
    "diff_check",
    "historical_preservation"
  ],
  "proposed_task_updates": [],
  "failure_modes": [
    {
      "id": "F1",
      "trigger": "Index has out-of-scope paths",
      "likely_stage": "implementer",
      "prevention": "Compare full staged names against the explicit allowlist before committing."
    }
  ]
}
