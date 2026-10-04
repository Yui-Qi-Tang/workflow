{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "research_plan",
  "task_id": "handoff-repair-20261004",
  "produced_by": "researcher",
  "status": "ready",
  "revision": "742e1a9d-ab5b-424f-9800-7945b1803f92",
  "input_fingerprints": {
    "share/handoff-repair-20261004/researcher/task.md": "2625f2f50cd6cf9988170c5be54c468108c559f9c2230ccc3c84bd5161fcd90c"
  },
  "input_artifacts": [
    {
      "path": "share/handoff-repair-20261004/researcher/task.md",
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
      "path": "researcher/AGENTS.md",
      "summary": "Stage rules"
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "share/handoff-repair-20261004/researcher/task.md",
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
    "next_agent": "planner",
    "allowed_next_inputs": [
      "share/handoff-repair-20261004/planner/plan.md"
    ],
    "notes": "Keep work bounded to the task."
  },
  "task_classification": "workflow_contract_repair",
  "goal_restatement": "Make stage contracts explicit and validate serialized outputs; remove authority delivery ambiguity.",
  "requested_change_summary": "Add bounded validation/message-preparation surfaces and update operative rules.",
  "expected_impact_areas": [
    "CLI validation and dispatch preparation",
    "Stage instructions",
    "Regression suite"
  ],
  "assumptions": [],
  "risks": [
    {
      "id": "R1",
      "description": "Authorization text in a file is not proof of human approval.",
      "impact": "Builder could overstate authority.",
      "mitigation": "Require scoped context; label source verification as orchestrator responsibility; never auto-grant."
    },
    {
      "id": "R2",
      "description": "Whole-chain sync checks future reviewer mirrors.",
      "impact": "Valid implementer output could fail local validation prematurely.",
      "mitigation": "Validate only through requested stage without bypassing upstream or cross-stage checks."
    },
    {
      "id": "R3",
      "description": "Updating frozen pilot would invalidate old observations.",
      "impact": "Lose reproducibility.",
      "mitigation": "Inventory all historical bytes and introduce fixes only in current tool paths."
    }
  ],
  "non_goals": [
    "Rerun Luna",
    "Build an executor",
    "Authenticate human identity",
    "Prove semantic correctness"
  ],
  "high_level_strategy": [
    "Document exact types.",
    "Reuse upstream validation with an explicit stop point.",
    "Build gated dispatch outer message from supplied scoped authorization.",
    "Test concrete regressions and preserve old evidence."
  ],
  "required_checks": [
    "regression_suite",
    "historical_preservation",
    "cli_validation",
    "diff_check"
  ],
  "proposed_task_updates": [],
  "failure_modes": [
    {
      "id": "F1",
      "trigger": "Validation ignores failed required checks or stale predecessor",
      "likely_stage": "implementer",
      "prevention": "Exercise real-file upstream/cross-stage cases."
    },
    {
      "id": "F2",
      "trigger": "Outer message points only to authorization inside file",
      "likely_stage": "planner",
      "prevention": "Assert statement/source/exception precede first read instruction in returned message."
    }
  ]
}
