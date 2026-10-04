{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "implementation_brief",
  "task_id": "workflow-integrity-20261003",
  "produced_by": "planner",
  "status": "ready",
  "revision": "20bbdb3f-2363-4665-89c5-a318fea72041",
  "input_fingerprints": {
    "share/workflow-integrity-20261003/planner/plan.md": "5f173f543005b09deac751e3dcb881951a27313e4321a7b554eb381e62d7a1b9"
  },
  "input_artifacts": [
    {
      "path": "share/workflow-integrity-20261003/planner/plan.md",
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
      "path": "planner/AGENTS.md",
      "summary": "Stage contract."
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "share/workflow-integrity-20261003/planner/plan.md",
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
      "source": "share/workflow-integrity-20261003/planner/plan.md",
      "summary": "Read and used for this stage."
    }
  ],
  "handoff": {
    "next_agent": "implementer",
    "allowed_next_inputs": [
      "AGENTS.md",
      "implementer/AGENTS.md",
      "share/workflow-integrity-20261003/implementer/impl.md",
      "agent_loop_poc/",
      "README.md",
      "README.en.md",
      "README.zh.md",
      "reviewer/AGENTS.md",
      "tasker/workflow-integrity-20261003.md",
      "share/workflow-integrity-20261003"
    ],
    "notes": "Authorize edits only to the listed task scope. Main agent executes; subagents may only challenge supplied text."
  },
  "summary": "Enforce structural contracts and artifact input freshness before routing.",
  "inputs_used": [
    "share/workflow-integrity-20261003/planner/plan.md",
    "tasker/workflow-integrity-20261003.md",
    "agent_loop_poc/loop.py",
    "agent_loop_poc/test_loop.py"
  ],
  "files_likely_to_change": [
    "agent_loop_poc/contracts.py",
    "agent_loop_poc/loop.py",
    "agent_loop_poc/test_loop.py",
    "agent_loop_poc/test_integrity.py",
    "agent_loop_poc/README.md",
    "README.md",
    "README.en.md",
    "README.zh.md",
    "AGENTS.md",
    "reviewer/AGENTS.md"
  ],
  "ordered_steps": [
    {
      "step": 1,
      "action": "Write frozen regression fixtures and run against the current router.",
      "rationale": "Show baseline failures before changing implementation.",
      "expected_evidence": "Baseline unittest log."
    },
    {
      "step": 2,
      "action": "Add standard-library contract validation and replace routing with sequential dependency checks.",
      "rationale": "Reject malformed and stale artifacts before transitions.",
      "expected_evidence": "Regression cases pass."
    },
    {
      "step": 3,
      "action": "Add read-only input fingerprint CLI, explicit blockers, safe task IDs and atomic state writes.",
      "rationale": "Make correct operation and diagnostics concrete.",
      "expected_evidence": "CLI and filesystem behavior tests."
    },
    {
      "step": 4,
      "action": "Document version, migration, dependency coverage and evidence limits.",
      "rationale": "Prevent unsupported guarantees and hidden compatibility changes.",
      "expected_evidence": "Updated docs."
    },
    {
      "step": 5,
      "action": "Run full unittest suite and diff check, preserve evidence and mirror bundle for review.",
      "rationale": "Validate actual work and make review self-contained.",
      "expected_evidence": "Final command logs and review bundle."
    }
  ],
  "invariants": [
    "No transition based on unvalidated labels.",
    "No completion from missing or stale chain.",
    "Never rewrite historical go-worker records.",
    "No external execution or side-effect replay.",
    "No hidden chat state used as stage authority; isolation unavailable and disclosed."
  ],
  "validation_plan": [
    {
      "check": "unit_and_regression",
      "command_or_method": "python3 -B -m unittest discover -v",
      "expected_result": "All final tests pass; pre-change regressions recorded.",
      "required": true
    },
    {
      "check": "diff",
      "command_or_method": "git diff --check",
      "expected_result": "No whitespace errors.",
      "required": true
    },
    {
      "check": "bundle_and_cli",
      "command_or_method": "Validate five stage artifacts and mirror bytes; run status/next on completed task.",
      "expected_result": "Current valid bundle and completed/done, without writes from read-only commands.",
      "required": true
    }
  ],
  "cleanup_plan": [
    "Use TemporaryDirectory for fixtures and -B for tests.",
    "Keep logs under share/workflow-integrity-20261003/evidence; remove task-created scratch files if any."
  ],
  "escalation_conditions": [
    {
      "condition": "Need executor, parallel task support or external writes.",
      "return_target": "tasker",
      "reason": "Outside approved first milestone."
    }
  ],
  "rollback_hints": [
    "Do not reset user changes; preserve partial work and failure evidence."
  ],
  "expected_output": {
    "result_artifact_path": "share/workflow-integrity-20261003/reviewer/result.md",
    "implementation_summary_requirements": [
      "Changes, actual validations, migration limitations and cleanup."
    ]
  }
}
