{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "normalized_task",
  "task_id": "workflow-rules-assessment-20261004",
  "produced_by": "tasker",
  "status": "ready",
  "revision": "96b9076c-2065-4af2-b9ed-29b31221a41a",
  "input_fingerprints": {
    "tasker/workflow-rules-assessment-20261004.md": "ef89c4a1b2da5c66d88b8c9280684710758c2900f3693846a8327e0832a0bf85"
  },
  "input_artifacts": [
    {
      "path": "tasker/workflow-rules-assessment-20261004.md",
      "required": true,
      "summary": "Current direct input; read before this production attempt."
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
      "source": "Human message in current chat: exact deletion and assessment request; no implementation-subagent exception."
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "tasker/workflow-rules-assessment-20261004.md"
    }
  ],
  "constraints": [
    "Delete only tasker/go-worker-2026050200.md and share/go-worker-2026050200/.",
    "Assessment only: do not edit operative AGENTS, controller, README, frozen experiment evidence, or create a skill.",
    "No experiment, commit, push, external messages, or changes to the sibling go-worker project.",
    "Main agent owns all five stages; same-invocation fallback, no claim of fresh-context isolation.",
    "Subagents may only challenge supplied propositions in text without tools; prior experiment exception does not apply.",
    "Preserve current five-stage and saved-output validation requirements."
  ],
  "open_questions": [],
  "evidence": [
    {
      "kind": "instruction",
      "source": "tasker/workflow-rules-assessment-20261004.md",
      "summary": "User requests deletion plus assessment only; no rule editing or skill creation."
    }
  ],
  "handoff": {
    "next_agent": "researcher",
    "allowed_next_inputs": [
      "share/workflow-rules-assessment-20261004/researcher/task.md",
      "AGENTS.md",
      "tasker/AGENTS.md",
      "researcher/AGENTS.md",
      "planner/AGENTS.md",
      "implementer/AGENTS.md",
      "reviewer/AGENTS.md",
      "agent_loop_poc/contracts.py",
      "agent_loop_poc/loop.py",
      "agent_loop_poc/README.md",
      "/Users/yuki/.codex/skills/.system/skill-creator/SKILL.md"
    ],
    "notes": "Main-owned sequential stage; no fresh invocation isolation claimed. Validate saved bytes and recheck route."
  },
  "goal": "Delete the obsolete local workflow task and assess targeted AGENTS changes and skill need.",
  "scope": [
    "The two exact deletion targets",
    "Six operative AGENTS, current controller and operating README",
    "Optional text-only counterargument"
  ],
  "deliverables": [
    "Deletion evidence with names and hashes",
    "Source-backed recommendation and skill scope",
    "Five-stage audit records"
  ],
  "acceptance_criteria": [
    "deleted_task_absent",
    "unrelated_files_preserved",
    "assessment_grounded"
  ],
  "conflicts": [],
  "source_of_truth": [
    "Current human request",
    "Root and nearest stage AGENTS",
    "Current saved source files"
  ],
  "validation": [
    "Verify exactly nine regular files, no symlinks, contained under the two authorized targets; delete and assert both targets absent.",
    "Compare all pre-existing tracked-file SHA-256 values and index state before/after; only new task records may remain untracked.",
    "Check all six operative rules against current controller and skill-creator guidance; attach source lines, distinguish recommendations from observed defects and untested benefits."
  ],
  "cleanup": [
    "Retain this task audit; no temporary files or content backups."
  ],
  "rollback": [
    "Untracked deleted files cannot be restored from Git; deletion is directly authorized. No product change to roll back."
  ]
}
