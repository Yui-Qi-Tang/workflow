{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "implementation_brief",
  "task_id": "workflow-rules-assessment-20261004",
  "produced_by": "planner",
  "status": "ready",
  "revision": "6a610ebc-347b-477b-9de7-259d2edc418f",
  "input_fingerprints": {
    "share/workflow-rules-assessment-20261004/planner/plan.md": "e5c8cac93b3d87ee2ba48b7086fe0efbaca99863c76ee11630499f9d2b98c938"
  },
  "input_artifacts": [
    {
      "path": "share/workflow-rules-assessment-20261004/planner/plan.md",
      "required": true,
      "summary": "Current direct input read before producing this stage."
    }
  ],
  "trusted_sources": [
    {
      "path": "AGENTS.md"
    },
    {
      "path": "planner/AGENTS.md"
    },
    {
      "source": "Current human deletion and assessment request, verified by main orchestrator."
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "share/workflow-rules-assessment-20261004/planner/plan.md"
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
      "kind": "input",
      "source": "share/workflow-rules-assessment-20261004/planner/plan.md",
      "summary": "Deletion plus assessment only; no product rule edit, skill creation or fresh-model claim."
    }
  ],
  "handoff": {
    "next_agent": "implementer",
    "allowed_next_inputs": [
      "share/workflow-rules-assessment-20261004/implementer/impl.md",
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
    "notes": "Main-agent same-invocation fallback. Preserve scope; validate saved bytes and check routing."
  },
  "summary": "Delete only specified obsolete task, preserve tracked files, and write a source-backed assessment.",
  "inputs_used": [
    "share/workflow-rules-assessment-20261004/planner/plan.md"
  ],
  "files_likely_to_change": [
    "tasker/go-worker-2026050200.md",
    "share/go-worker-2026050200/",
    "share/workflow-rules-assessment-20261004/evidence",
    "share/workflow-rules-assessment-20261004/reviewer/result.md"
  ],
  "authorized_read_paths": [
    "share/workflow-rules-assessment-20261004/planner/plan.md",
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
  "ordered_steps": [
    {
      "step": 1,
      "action": "Verify exact nine regular files and symlink-free containment; record only paths and hashes.",
      "rationale": "Bound deletion.",
      "expected_evidence": "evidence/deletion.json"
    },
    {
      "step": 2,
      "action": "Remove exact target files and empty directories, then check both targets absent.",
      "rationale": "Fulfill human cleanup request.",
      "expected_evidence": "Absence verification."
    },
    {
      "step": 3,
      "action": "Compare six active AGENTS, controller and skill guidance; evaluate text-only opposition if supplied.",
      "rationale": "Separate concrete omissions from optional policy changes.",
      "expected_evidence": "evidence/assessment.json with source paths and lines."
    },
    {
      "step": 4,
      "action": "Verify all tracked hashes and index diff; record results and validate saved implementation artifact.",
      "rationale": "Preserve unrelated work and support handoff.",
      "expected_evidence": "evidence/checks.json and implementation validation receipt."
    }
  ],
  "invariants": [
    "Delete only tasker/go-worker-2026050200.md and share/go-worker-2026050200/.",
    "Assessment only: do not edit operative AGENTS, controller, README, frozen experiment evidence, or create a skill.",
    "No experiment, commit, push, external messages, or changes to the sibling go-worker project.",
    "Main agent owns all five stages; same-invocation fallback, no claim of fresh-context isolation.",
    "Subagents may only challenge supplied propositions in text without tools; prior experiment exception does not apply.",
    "Preserve current five-stage and saved-output validation requirements."
  ],
  "validation_plan": [
    {
      "check": "deleted_task_absent",
      "command_or_method": "Verify exact nine-file, contained, symlink-free inventory; delete only authorized paths and assert absence.",
      "expected_result": "passed with observed evidence",
      "required": true
    },
    {
      "check": "unrelated_files_preserved",
      "command_or_method": "Compare all tracked SHA-256 values and index diff against evidence/baseline.json.",
      "expected_result": "passed with observed evidence",
      "required": true
    },
    {
      "check": "assessment_grounded",
      "command_or_method": "Provide current source lines for findings across six active rules, controller and skill guidance; distinguish recommendations and untested effects.",
      "expected_result": "passed with observed evidence",
      "required": true
    }
  ],
  "cleanup_plan": [
    "Keep only this task audit; no temp files or deleted-content backups."
  ],
  "escalation_conditions": [
    {
      "condition": "Unexpected deletion inventory or need to change task requirements",
      "return_target": "tasker",
      "reason": "Stop before expanding scope."
    }
  ],
  "rollback_hints": [
    "Untracked deletion cannot be restored from Git. Human directly authorized removal. No product edits to roll back."
  ],
  "expected_output": {
    "result_artifact_path": "share/workflow-rules-assessment-20261004/reviewer/result.md",
    "implementation_summary_requirements": [
      "Report deletion count and verification.",
      "Give source-backed AGENTS and skill recommendations.",
      "Disclose same-invocation fallback and no skill efficacy experiment."
    ]
  }
}
