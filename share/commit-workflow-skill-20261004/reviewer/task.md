{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "normalized_task",
  "task_id": "commit-workflow-skill-20261004",
  "produced_by": "tasker",
  "status": "ready",
  "revision": "5a261c4f-854c-4b64-a322-3054afa7493f",
  "input_fingerprints": {
    "tasker/commit-workflow-skill-20261004.md": "bdade0503b9eba99f83c8702ad7fbb49018f7b6252d524d5e294472a551e9c8a"
  },
  "input_artifacts": [
    {
      "path": "tasker/commit-workflow-skill-20261004.md",
      "required": true,
      "summary": "Current direct task or workflow input."
    }
  ],
  "trusted_sources": [
    {
      "path": "AGENTS.md"
    },
    {
      "path": "tasker/AGENTS.md"
    },
    {
      "source": "Current human instruction: 好，commit這次改動"
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "tasker/commit-workflow-skill-20261004.md"
    },
    {
      "source": "Working-tree diff and Git status are evidence, not execution authority."
    }
  ],
  "constraints": [
    "Explicit allowlist only; preserve all 556 pre-existing selected file bytes.",
    "Local commit on main after completed review and exact index verification; no push, amend, product edits or model reruns.",
    "Main owns five stages in same_invocation fallback; no independently isolated review."
  ],
  "open_questions": [],
  "evidence": [
    {
      "kind": "execution_mode",
      "source": "Current human delegation rules and root fallback",
      "summary": "same_invocation; main sequentially performs five roles, not isolated stage executions."
    }
  ],
  "handoff": {
    "next_agent": "researcher",
    "allowed_next_inputs": [
      "share/commit-workflow-skill-20261004/researcher/task.md",
      "share/commit-workflow-skill-20261004/evidence/"
    ],
    "notes": "Prepare and review the commit; Git publication follows review and final index check."
  },
  "goal": "Prepare a reviewed allowlisted local commit of current workflow guidance, skill and six-cell pilot evidence.",
  "scope": [
    "Paths in share/commit-workflow-skill-20261004/evidence/allowlist.json"
  ],
  "deliverables": [
    "One local Git commit after review",
    "Complete preparation/review artifacts and verification receipts"
  ],
  "acceptance_criteria": [
    "content_integrity",
    "workflow_records",
    "diff_review",
    "index_scope"
  ],
  "conflicts": [],
  "source_of_truth": [
    "Current human request",
    "Current root and role contracts",
    "Inspected working-tree changes and explicit allowlist"
  ],
  "validation": [
    "content_integrity",
    "workflow_records",
    "diff_review",
    "index_scope"
  ],
  "cleanup": [
    "Preserve evidence; create no caches or scratch files."
  ],
  "rollback": [
    "On failure preserve files/index; do not reset or rewrite history."
  ]
}
