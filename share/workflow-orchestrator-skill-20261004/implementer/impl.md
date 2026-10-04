{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "implementation_brief",
  "task_id": "workflow-orchestrator-skill-20261004",
  "produced_by": "planner",
  "status": "ready",
  "revision": "e2536704-4f89-40bd-bb8b-e66d02f7233f",
  "input_fingerprints": {
    "share/workflow-orchestrator-skill-20261004/planner/plan.md": "0bdf5ff61416b708a8bbcf6cf760f2b69292c7c3d9303ff0ae691e1f99052366"
  },
  "input_artifacts": [
    {
      "path": "share/workflow-orchestrator-skill-20261004/planner/plan.md",
      "required": true,
      "summary": "Current direct input captured before production."
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
      "source": "Current human message: 好，開始修改; authorizes previous targeted proposal, no executor-subagent exception."
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "share/workflow-orchestrator-skill-20261004/planner/plan.md"
    }
  ],
  "constraints": [
    "Implement only the approved targeted role documentation and thin project-local skill.",
    "Preserve all five stages, instruction precedence, existing controller semantics and version 0.3.0.",
    "Main agent owns design, edits and checks. Subagents may only provide textual opposition without tools; no prior Luna execution exception applies.",
    "Use same_invocation fallback for this task and disclose lack of fresh-model isolation; no model efficacy experiment.",
    "Preserve frozen experiments and prior task evidence, including untracked assessment records.",
    "No commit, push, new runner, dependency installation, or automatic side-effect retry."
  ],
  "open_questions": [],
  "evidence": [
    {
      "kind": "execution_mode",
      "source": "Current main-agent orchestration",
      "summary": "same_invocation fallback; no isolation or efficacy claim."
    }
  ],
  "handoff": {
    "next_agent": "implementer",
    "allowed_next_inputs": [
      "share/workflow-orchestrator-skill-20261004/implementer/impl.md",
      "AGENTS.md",
      "tasker/AGENTS.md",
      "researcher/AGENTS.md",
      "implementer/AGENTS.md",
      "reviewer/AGENTS.md",
      "README.md",
      "README.en.md",
      "README.zh.md",
      "agent_loop_poc/README.md",
      ".agents/skills/workflow-orchestrator/SKILL.md",
      ".agents/skills/workflow-orchestrator/agents/openai.yaml",
      "planner/AGENTS.md",
      "agent_loop_poc/contracts.py",
      "agent_loop_poc/loop.py",
      "agent_loop_poc/test_handoffs.py",
      "agent_loop_poc/test_integrity.py",
      "agent_loop_poc/test_loop.py"
    ],
    "notes": "Main-owned sequential checkpoints; validate saved bytes and inspect next before continuing."
  },
  "summary": "Make the authorized documentation and skill changes, then validate formats, contracts, controller regressions and scope.",
  "inputs_used": [
    "share/workflow-orchestrator-skill-20261004/planner/plan.md"
  ],
  "files_likely_to_change": [
    "AGENTS.md",
    "tasker/AGENTS.md",
    "researcher/AGENTS.md",
    "implementer/AGENTS.md",
    "reviewer/AGENTS.md",
    "README.md",
    "README.en.md",
    "README.zh.md",
    "agent_loop_poc/README.md",
    ".agents/skills/workflow-orchestrator/SKILL.md",
    ".agents/skills/workflow-orchestrator/agents/openai.yaml",
    "share/workflow-orchestrator-skill-20261004/evidence"
  ],
  "ordered_steps": [
    {
      "step": 1,
      "action": "Complete common and remaining nested field types/enums against contracts.py; clarify execution modes and orchestrator ownership in root rules.",
      "rationale": "Fix observed ambiguity while preserving existing behavior.",
      "expected_evidence": "Allowlisted documentation diff and contract comparison."
    },
    {
      "step": 2,
      "action": "Prepare two-file thin skill candidate and link current CLI/role docs; update README entrypoints and isolation explanation.",
      "rationale": "Make repeated operations discoverable without duplicating schemas.",
      "expected_evidence": "Candidate skill passes bundled validator and local link checks."
    },
    {
      "step": 3,
      "action": "Install exact reviewed candidate into .agents/skills/workflow-orchestrator, using scoped escalation for protected path if needed.",
      "rationale": "Deliver a repository-discoverable skill.",
      "expected_evidence": "Installed bytes match validated candidate; candidate cleaned up."
    },
    {
      "step": 4,
      "action": "Run existing tests, verify documentation/skill and all unchanged baseline hashes outside allowlist, then write result.",
      "rationale": "Bound regression and scope claims to observed evidence.",
      "expected_evidence": "Four required checks passed; saved result validates."
    }
  ],
  "invariants": [
    "Implement only the approved targeted role documentation and thin project-local skill.",
    "Preserve all five stages, instruction precedence, existing controller semantics and version 0.3.0.",
    "Main agent owns design, edits and checks. Subagents may only provide textual opposition without tools; no prior Luna execution exception applies.",
    "Use same_invocation fallback for this task and disclose lack of fresh-model isolation; no model efficacy experiment.",
    "Preserve frozen experiments and prior task evidence, including untracked assessment records.",
    "No commit, push, new runner, dependency installation, or automatic side-effect retry."
  ],
  "validation_plan": [
    {
      "check": "contract_alignment",
      "command_or_method": "Compare common and nested documentation types/enums with current contracts.py and manually review execution/authority semantics.",
      "expected_result": "passed with recorded evidence",
      "required": true
    },
    {
      "check": "skill_validation",
      "command_or_method": "Run bundled quick_validate.py on the skill; check YAML, local links, and metadata; inspect trigger scope and CLI instructions.",
      "expected_result": "passed with recorded evidence",
      "required": true
    },
    {
      "check": "controller_regression",
      "command_or_method": "Run python3 -B -m unittest discover -v and require all tests pass.",
      "expected_result": "passed with recorded evidence",
      "required": true
    },
    {
      "check": "scope_and_whitespace",
      "command_or_method": "Check changed files against explicit allowlist, preserve baseline hashes for other tracked and existing assessment files, and run git diff --check.",
      "expected_result": "passed with recorded evidence",
      "required": true
    }
  ],
  "cleanup_plan": [
    "Remove only skill candidate after successful matching installation; retain audit evidence."
  ],
  "escalation_conditions": [
    {
      "condition": "Requested change requires new runtime semantics, acceptance relaxation or broader permissions",
      "return_target": "tasker",
      "reason": "Outside approved proposal."
    }
  ],
  "rollback_hints": [
    "Use task-specific diff/baseline; preserve pre-existing task records and frozen experiments."
  ],
  "expected_output": {
    "result_artifact_path": "share/workflow-orchestrator-skill-20261004/reviewer/result.md",
    "implementation_summary_requirements": [
      "List actual rule/skill changes and test evidence.",
      "Disclose skill-format vs actual model-efficacy validation.",
      "Record cleanup and unchanged controller version."
    ]
  }
}
