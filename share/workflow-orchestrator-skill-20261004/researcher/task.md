{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "normalized_task",
  "task_id": "workflow-orchestrator-skill-20261004",
  "produced_by": "tasker",
  "status": "ready",
  "revision": "74f81005-8513-4135-ac44-8b0d0c36f225",
  "input_fingerprints": {
    "tasker/workflow-orchestrator-skill-20261004.md": "0e3e66364b8797f929c4733d78290bf012dfa9a497bf75de9b73ba62a9da1d07"
  },
  "input_artifacts": [
    {
      "path": "tasker/workflow-orchestrator-skill-20261004.md",
      "required": true,
      "summary": "Current direct input captured before production."
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
      "source": "Current human message: 好，開始修改; authorizes previous targeted proposal, no executor-subagent exception."
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "tasker/workflow-orchestrator-skill-20261004.md"
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
    "next_agent": "researcher",
    "allowed_next_inputs": [
      "share/workflow-orchestrator-skill-20261004/researcher/task.md",
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
  "goal": "Implement approved rule clarifications and one thin repository-scoped workflow skill.",
  "scope": [
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
    ".agents/skills/workflow-orchestrator/agents/openai.yaml"
  ],
  "deliverables": [
    "Completed typed common/nested role contracts",
    "Clear isolation fallback and centralized orchestrator duties",
    "Discoverable two-file instruction-only skill and validation evidence"
  ],
  "acceptance_criteria": [
    "contract_alignment",
    "skill_validation",
    "controller_regression",
    "scope_and_whitespace"
  ],
  "conflicts": [],
  "source_of_truth": [
    "Current human authorization",
    "Operative AGENTS and existing controller types",
    "Bundled skill-creator instructions",
    "Official repository skill discovery documentation"
  ],
  "validation": [
    "Compare common and nested documentation types/enums with current contracts.py and manually review execution/authority semantics.",
    "Run bundled quick_validate.py on the skill; check YAML, local links, and metadata; inspect trigger scope and CLI instructions.",
    "Run python3 -B -m unittest discover -v and require all tests pass.",
    "Check changed files against explicit allowlist, preserve baseline hashes for other tracked and existing assessment files, and run git diff --check."
  ],
  "cleanup": [
    "Remove installed skill candidate only; preserve task evidence and prior work."
  ],
  "rollback": [
    "Reverse only allowlisted task edits and remove only new skill folder; no external side effects."
  ]
}
