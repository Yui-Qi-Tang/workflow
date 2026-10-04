{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "implementation_brief",
  "task_id": "commit-workflow-030-20261004",
  "produced_by": "planner",
  "status": "ready",
  "revision": "4785a7a9-daea-4501-94e5-f864754a5695",
  "input_fingerprints": {
    "share/commit-workflow-030-20261004/planner/plan.md": "52ccca9b66ce6d4fb1a4052d02cedae8ea0b79c22f2de8b24a70502ecd59081c"
  },
  "input_artifacts": [
    {
      "path": "share/commit-workflow-030-20261004/planner/plan.md",
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
      "path": "planner/AGENTS.md",
      "summary": "Stage requirements"
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "share/commit-workflow-030-20261004/planner/plan.md",
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
    "next_agent": "implementer",
    "allowed_next_inputs": [
      "share/commit-workflow-030-20261004/implementer/impl.md"
    ],
    "notes": "Final Git publication follows successful review; no commit success is assumed."
  },
  "summary": "Prepare reviewed commit content without changing product code; orchestrator performs authorized Git publication after review.",
  "inputs_used": [
    "share/commit-workflow-030-20261004/planner/plan.md"
  ],
  "files_likely_to_change": [
    "tasker/commit-workflow-030-20261004.md",
    "share/commit-workflow-030-20261004/"
  ],
  "ordered_steps": [
    {
      "step": 1,
      "action": "Verify selected files and run current tests/diff checks.",
      "rationale": "Commit validated current content.",
      "expected_evidence": "Test/check logs"
    },
    {
      "step": 2,
      "action": "Verify frozen historical hashes and complete self-contained review.",
      "rationale": "Preserve original outcomes.",
      "expected_evidence": "Hash evidence and review artifact"
    },
    {
      "step": 3,
      "action": "After review, stage exact allowlist and verify staged blobs before local commit.",
      "rationale": "Git commit is final publication of reviewed bytes.",
      "expected_evidence": "Git tool output and final commit ID"
    }
  ],
  "invariants": [
    "No excluded go-worker bytes staged or modified.",
    "No push, model run or product edit."
  ],
  "validation_plan": [
    {
      "check": "unit_tests",
      "command_or_method": "python3 -B -m unittest discover -v",
      "expected_result": "66 tests pass",
      "required": true
    },
    {
      "check": "diff_check",
      "command_or_method": "git diff --check",
      "expected_result": "Exit0",
      "required": true
    },
    {
      "check": "historical_preservation",
      "command_or_method": "Compare frozen pilot file hash inventory",
      "expected_result": "316 files unchanged",
      "required": true
    }
  ],
  "cleanup_plan": [
    "Temporary test directories clean themselves.",
    "Retain commit-preparation evidence."
  ],
  "escalation_conditions": [
    {
      "condition": "Unexpected staged files or failed checks",
      "return_target": "implementer",
      "reason": "Resolve before publication without discarding unrelated work."
    }
  ],
  "rollback_hints": [
    "Preserve working files if commit fails."
  ],
  "expected_output": {
    "result_artifact_path": "share/commit-workflow-030-20261004/reviewer/result.md",
    "implementation_summary_requirements": [
      "Actual checks",
      "Explicit scope",
      "Commit still pending before final publication"
    ]
  }
}
