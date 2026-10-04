{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "implementation_brief",
  "task_id": "handoff-repair-20261004",
  "produced_by": "planner",
  "status": "ready",
  "revision": "6387708a-551a-4983-b307-ba2d79f22b8a",
  "input_fingerprints": {
    "share/handoff-repair-20261004/planner/plan.md": "3f30aef003e7b7dc07f1383e00a0d7886397266f0515c61ed8133aaa7a76723a"
  },
  "input_artifacts": [
    {
      "path": "share/handoff-repair-20261004/planner/plan.md",
      "required": true,
      "summary": "Direct required input"
    }
  ],
  "trusted_sources": [
    {
      "path": "AGENTS.md",
      "summary": "Root contract"
    },
    {
      "path": "planner/AGENTS.md",
      "summary": "Stage rules"
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "share/handoff-repair-20261004/planner/plan.md",
      "summary": "Task or handoff content"
    }
  ],
  "constraints": [
    "Fix only authorized three gaps.",
    "Preserve historical experiment and pre-existing edits.",
    "No new model experiment, commit or push.",
    "Main pipeline uses same-invocation fallback."
  ],
  "open_questions": [],
  "evidence": [
    {
      "kind": "user_request",
      "source": "tasker/handoff-repair-20261004.md",
      "summary": "User explicitly authorized all three repairs."
    }
  ],
  "handoff": {
    "next_agent": "implementer",
    "allowed_next_inputs": [
      "share/handoff-repair-20261004/implementer/impl.md"
    ],
    "notes": "Keep work bounded to the task."
  },
  "summary": "Implement three requested handoff repairs without changing historical evidence or validator semantics.",
  "inputs_used": [
    "share/handoff-repair-20261004/planner/plan.md"
  ],
  "files_likely_to_change": [
    "AGENTS.md",
    "*/AGENTS.md",
    "agent_loop_poc/loop.py",
    "agent_loop_poc/test_handoffs.py",
    "agent_loop_poc/README.md",
    "README.md",
    "README.en.md",
    "README.zh.md"
  ],
  "ordered_steps": [
    {
      "step": 1,
      "action": "Add exact planner nested types and post-write validation requirement to role rules.",
      "rationale": "Models need visible types and must check persisted bytes.",
      "expected_evidence": "Explicit array-of-strings documentation and validation instructions."
    },
    {
      "step": 2,
      "action": "Add read-only validate with prefix checking and digest; add scoped outer dispatch preparation.",
      "rationale": "Operationalize actual-file checks and trusted authorization propagation.",
      "expected_evidence": "Exit codes and self-contained outer message."
    },
    {
      "step": 3,
      "action": "Add regression tests, run full suite, verify history hashes and finish self-contained review bundle.",
      "rationale": "Protect existing routing and prior evidence.",
      "expected_evidence": "Recorded suite, CLI and hash results."
    }
  ],
  "invariants": [
    "No automatic human authorization.",
    "Do not accept invalid/stale prefix.",
    "Do not equate valid with success or permission to route.",
    "Preserve all historical experiment files."
  ],
  "validation_plan": [
    {
      "check": "regression_suite",
      "command_or_method": "python3 -B -m unittest discover -v",
      "expected_result": "Existing and new tests pass.",
      "required": true
    },
    {
      "check": "historical_preservation",
      "command_or_method": "Compare all historical paths/bytes to evidence/historical-hashes.json",
      "expected_result": "No change or deletion.",
      "required": true
    },
    {
      "check": "cli_validation",
      "command_or_method": "Run current CLI against valid main artifacts and malformed/stale fixture subprocesses",
      "expected_result": "Valid pass, invalid fail, correct digest; no file mutation.",
      "required": true
    },
    {
      "check": "diff_check",
      "command_or_method": "git diff --check",
      "expected_result": "No whitespace errors.",
      "required": true
    }
  ],
  "cleanup_plan": [
    "Temporary test dirs auto-clean; avoid __pycache__.",
    "Keep task evidence in share."
  ],
  "escalation_conditions": [
    {
      "condition": "A fix requires broader authority, schema migration or historical edits",
      "return_target": "researcher",
      "reason": "Outside the requested repair scope."
    }
  ],
  "rollback_hints": [
    "Revert only this task diff, never reset pre-existing changes."
  ],
  "expected_output": {
    "result_artifact_path": "share/handoff-repair-20261004/reviewer/result.md",
    "implementation_summary_requirements": [
      "Implemented surfaces",
      "Actual test evidence",
      "Unchanged historical evidence",
      "Limits and cleanup"
    ]
  }
}
