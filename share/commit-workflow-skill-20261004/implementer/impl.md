{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "implementation_brief",
  "task_id": "commit-workflow-skill-20261004",
  "produced_by": "planner",
  "status": "ready",
  "revision": "63468bc0-7cf3-43e7-bd44-c56c27778f4f",
  "input_fingerprints": {
    "share/commit-workflow-skill-20261004/planner/plan.md": "f3e36dac339c04ffddf61e1af53a99c87dcd6cdc350686b5e284353393482741"
  },
  "input_artifacts": [
    {
      "path": "share/commit-workflow-skill-20261004/planner/plan.md",
      "required": true,
      "summary": "Current direct task or workflow input."
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
      "source": "Current human instruction: 好，commit這次改動"
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "share/commit-workflow-skill-20261004/planner/plan.md"
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
    "next_agent": "implementer",
    "allowed_next_inputs": [
      "share/commit-workflow-skill-20261004/implementer/impl.md",
      "share/commit-workflow-skill-20261004/evidence/"
    ],
    "notes": "Prepare and review the commit; Git publication follows review and final index check."
  },
  "summary": "Verify and prepare the authorized local commit, preserving existing files and raw evidence.",
  "inputs_used": [
    "share/commit-workflow-skill-20261004/planner/plan.md"
  ],
  "files_likely_to_change": [
    "tasker/commit-workflow-skill-20261004.md",
    "share/commit-workflow-skill-20261004/",
    "Local Git index and history after review"
  ],
  "ordered_steps": [
    {
      "step": 1,
      "action": "Check baseline and frozen experiment, validate the three current completed workflows, inspect whitespace.",
      "rationale": "Review exact existing content without altering evidence.",
      "expected_evidence": "Content and workflow validation receipts."
    },
    {
      "step": 2,
      "action": "Stage explicit allowlist and compare every staged blob with current reviewed bytes.",
      "rationale": "Prevent accidental inclusion or stale staging.",
      "expected_evidence": "Index path/byte agreement and whitespace report."
    },
    {
      "step": 3,
      "action": "Record preparation result, mirror current inputs and complete review before final orchestrator Git commit.",
      "rationale": "No pre-commit claim that publication already happened.",
      "expected_evidence": "Validated review then actual Git commit output and clean status."
    }
  ],
  "invariants": [
    "Explicit allowlist only; preserve all 556 pre-existing selected file bytes.",
    "Local commit on main after completed review and exact index verification; no push, amend, product edits or model reruns.",
    "Main owns five stages in same_invocation fallback; no independently isolated review."
  ],
  "validation_plan": [
    {
      "check": "content_integrity",
      "command_or_method": "content_integrity verification with saved receipts",
      "expected_result": "All required conditions met; raw-only whitespace findings explicitly recorded.",
      "required": true
    },
    {
      "check": "workflow_records",
      "command_or_method": "workflow_records verification with saved receipts",
      "expected_result": "All required conditions met; raw-only whitespace findings explicitly recorded.",
      "required": true
    },
    {
      "check": "diff_review",
      "command_or_method": "diff_review verification with saved receipts",
      "expected_result": "All required conditions met; raw-only whitespace findings explicitly recorded.",
      "required": true
    },
    {
      "check": "index_scope",
      "command_or_method": "index_scope verification with saved receipts",
      "expected_result": "All required conditions met; raw-only whitespace findings explicitly recorded.",
      "required": true
    }
  ],
  "cleanup_plan": [
    "Keep all authorized evidence; no temp/caches."
  ],
  "escalation_conditions": [
    {
      "condition": "Unexpected path/content change or failed integrity check",
      "return_target": "implementer",
      "reason": "Stop publication until scope and evidence are reconciled."
    }
  ],
  "rollback_hints": [
    "Preserve working files/index on failure; no reset or history rewrite."
  ],
  "expected_output": {
    "result_artifact_path": "share/commit-workflow-skill-20261004/reviewer/result.md",
    "implementation_summary_requirements": [
      "State actual checks and allowed content.",
      "Make clear Git commit remains pending final review; report hash after Git succeeds."
    ]
  }
}
