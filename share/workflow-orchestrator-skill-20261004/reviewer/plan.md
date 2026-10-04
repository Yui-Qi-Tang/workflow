{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "research_plan",
  "task_id": "workflow-orchestrator-skill-20261004",
  "produced_by": "researcher",
  "status": "ready",
  "revision": "5ab4d564-ce0e-4f68-ab9b-e625628db0dc",
  "input_fingerprints": {
    "share/workflow-orchestrator-skill-20261004/researcher/task.md": "7ee40a6b8107468c30b71b736d72a354ae05db523757feaf1a909b9ba5ee532d"
  },
  "input_artifacts": [
    {
      "path": "share/workflow-orchestrator-skill-20261004/researcher/task.md",
      "required": true,
      "summary": "Current direct input captured before production."
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
      "source": "Current human message: 好，開始修改; authorizes previous targeted proposal, no executor-subagent exception."
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "share/workflow-orchestrator-skill-20261004/researcher/task.md"
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
    "next_agent": "planner",
    "allowed_next_inputs": [
      "share/workflow-orchestrator-skill-20261004/planner/plan.md",
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
  "task_classification": "documentation_and_skill_implementation",
  "goal_restatement": "Apply the approved bounded instruction improvements and create a thin skill.",
  "requested_change_summary": "Complete contract type descriptions and operating guidance without changing runtime behavior.",
  "expected_impact_areas": [
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
  "assumptions": [
    {
      "id": "a1",
      "statement": "The skill belongs to this repository and can live in its discoverable .agents/skills location.",
      "source": "User approved project assessment; official local discovery documentation.",
      "risk_if_wrong": "Broader user-level installation would affect unrelated projects."
    }
  ],
  "risks": [
    {
      "id": "r1",
      "description": "Mode clarification could silently make fallback equivalent to isolation.",
      "impact": "Invalid experiment evidence.",
      "mitigation": "Preserve fresh goal; require blocking when true isolation is an acceptance condition."
    },
    {
      "id": "r2",
      "description": "Skill could duplicate authority or schema.",
      "impact": "Drift or unauthorized execution.",
      "mitigation": "Keep skill thin and reference current rules/CLI, retain verified human scope."
    },
    {
      "id": "r3",
      "description": ".agents is a protected write path in this session.",
      "impact": "Installation requires filesystem approval review.",
      "mitigation": "Prepare/validate exact candidate first, then narrowly install the two approved files using escalation if required."
    }
  ],
  "non_goals": [
    "Preserve all five stages, instruction precedence, existing controller semantics and version 0.3.0.",
    "Main agent owns design, edits and checks. Subagents may only provide textual opposition without tools; no prior Luna execution exception applies.",
    "Use same_invocation fallback for this task and disclose lack of fresh-model isolation; no model efficacy experiment.",
    "Preserve frozen experiments and prior task evidence, including untracked assessment records.",
    "No commit, push, new runner, dependency installation, or automatic side-effect retry."
  ],
  "high_level_strategy": [
    "Complete types from current contract definitions.",
    "Clarify mode and responsibilities using existing rules, not new runner behavior.",
    "Create and validate small project-local skill and link it from docs."
  ],
  "required_checks": [
    "contract_alignment",
    "skill_validation",
    "controller_regression",
    "scope_and_whitespace"
  ],
  "proposed_task_updates": [],
  "failure_modes": [
    {
      "id": "f1",
      "trigger": "A real-isolation requirement meets same-invocation execution.",
      "likely_stage": "planner",
      "prevention": "Block rather than change acceptance."
    },
    {
      "id": "f2",
      "trigger": "Skill guidance confuses next text with JSON or uses exit 0 as route approval.",
      "likely_stage": "implementer",
      "prevention": "Follow documented output types and check actual decision."
    }
  ]
}
