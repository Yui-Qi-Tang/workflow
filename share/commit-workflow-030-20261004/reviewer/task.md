{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "normalized_task",
  "task_id": "commit-workflow-030-20261004",
  "produced_by": "tasker",
  "status": "ready",
  "revision": "15e5dd0e-7ab0-4522-b0f2-a8112c0b91f1",
  "input_fingerprints": {
    "tasker/commit-workflow-030-20261004.md": "ca0a5503bacf4f0202e3eeaf14a9a74d49efaf1c2809f60e7a4a96bd92967dc6"
  },
  "input_artifacts": [
    {
      "path": "tasker/commit-workflow-030-20261004.md",
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
      "path": "tasker/AGENTS.md",
      "summary": "Stage requirements"
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "tasker/commit-workflow-030-20261004.md",
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
    "next_agent": "researcher",
    "allowed_next_inputs": [
      "share/commit-workflow-030-20261004/researcher/task.md"
    ],
    "notes": "Final Git publication follows successful review; no commit success is assumed."
  },
  "goal": "Prepare and verify exact local commit contents, then publish the reviewed tree with Git.",
  "scope": [
    "AGENTS.md",
    "README.md",
    "README.en.md",
    "README.zh.md",
    "agent_loop_poc/README.md",
    "agent_loop_poc/loop.py",
    "agent_loop_poc/contracts.py",
    "agent_loop_poc/test_loop.py",
    "agent_loop_poc/test_integrity.py",
    "agent_loop_poc/test_handoffs.py",
    "tasker/AGENTS.md",
    "researcher/AGENTS.md",
    "planner/AGENTS.md",
    "implementer/AGENTS.md",
    "reviewer/AGENTS.md",
    "tasker/workflow-integrity-20261003.md",
    "tasker/luna-effort-pilot-20261004.md",
    "tasker/handoff-repair-20261004.md",
    "share/workflow-integrity-20261003",
    "share/luna-effort-pilot-20261004",
    "share/handoff-repair-20261004",
    "experiments/luna-effort-pilot-20261004",
    "tasker/commit-workflow-030-20261004.md",
    "share/commit-workflow-030-20261004"
  ],
  "deliverables": [
    "Reviewed allowlisted commit bundle",
    "Verified local Git commit identity in final response"
  ],
  "acceptance_criteria": [
    "All selected files included, unrelated files excluded.",
    "Current tests and whitespace checks pass.",
    "Historical evidence unchanged."
  ],
  "conflicts": [],
  "source_of_truth": [
    "tasker/commit-workflow-030-20261004.md"
  ],
  "validation": [
    "Tests",
    "Diff/index review",
    "History and excluded-file hashes"
  ],
  "cleanup": [
    "Keep evidence; no scratch or caches."
  ],
  "rollback": [
    "Preserve files/index if Git fails; no reset."
  ]
}
