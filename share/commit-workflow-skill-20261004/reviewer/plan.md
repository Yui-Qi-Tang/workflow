{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "research_plan",
  "task_id": "commit-workflow-skill-20261004",
  "produced_by": "researcher",
  "status": "ready",
  "revision": "4fb3f06f-f127-4ee9-9e4f-0daa4d0c20ab",
  "input_fingerprints": {
    "share/commit-workflow-skill-20261004/researcher/task.md": "6e2a7df9f9ac9a5c4a2bf05e6f6b5bc64dde47c9467331243c061ca7b3c77a9e"
  },
  "input_artifacts": [
    {
      "path": "share/commit-workflow-skill-20261004/researcher/task.md",
      "required": true,
      "summary": "Current direct task or workflow input."
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
      "source": "Current human instruction: 好，commit這次改動"
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "share/commit-workflow-skill-20261004/researcher/task.md"
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
    "next_agent": "planner",
    "allowed_next_inputs": [
      "share/commit-workflow-skill-20261004/planner/plan.md",
      "share/commit-workflow-skill-20261004/evidence/"
    ],
    "notes": "Prepare and review the commit; Git publication follows review and final index check."
  },
  "task_classification": "local_commit_preparation",
  "goal_restatement": "Prepare a reviewed allowlisted local commit of current workflow guidance, skill and six-cell pilot evidence.",
  "requested_change_summary": "Commit the existing guidance, skill and experiment with complete retained evidence.",
  "expected_impact_areas": [
    "Local Git index/history",
    "New commit-preparation bundle"
  ],
  "assumptions": [],
  "risks": [
    {
      "id": "scope",
      "description": "Broad staging could include unrelated work or alter frozen evidence.",
      "impact": "Unwanted content in commit or lost audit fidelity.",
      "mitigation": "Explicit allowlist, baseline hashes and staged blob comparison."
    },
    {
      "id": "self_reference",
      "description": "Embedding final commit hash in its own committed artifacts is circular.",
      "impact": "False completion evidence or dirty tree.",
      "mitigation": "Review preparation first, commit as final orchestrator action, report hash in conversation."
    }
  ],
  "non_goals": [
    "Product changes",
    "New experiments",
    "Push or history rewrite"
  ],
  "high_level_strategy": [
    "Freeze existing selected bytes; validate existing completed workflows and experiment integrity.",
    "Stage only allowlisted paths; check exact index bytes and whitespace.",
    "Produce truthful preparation result and review; then commit and verify Git state."
  ],
  "required_checks": [
    "content_integrity",
    "workflow_records",
    "diff_review",
    "index_scope"
  ],
  "proposed_task_updates": [],
  "failure_modes": [
    {
      "id": "raw_whitespace",
      "trigger": "Immutable raw evidence contains trailing spaces.",
      "likely_stage": "implementer",
      "prevention": "Record exact findings and preserve raw bytes; do not silently normalize historical outputs."
    }
  ]
}
