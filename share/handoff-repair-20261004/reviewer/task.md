{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "normalized_task",
  "task_id": "handoff-repair-20261004",
  "produced_by": "tasker",
  "status": "ready",
  "revision": "3d5e2d40-4511-499e-8d92-c73850d38fd0",
  "input_fingerprints": {
    "tasker/handoff-repair-20261004.md": "57bfb16bf489adb7f563d40fd2ce0f94c56b7b734cbab1c63759bc5f7eebd6a8"
  },
  "input_artifacts": [
    {
      "path": "tasker/handoff-repair-20261004.md",
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
      "path": "tasker/AGENTS.md",
      "summary": "Stage rules"
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "tasker/handoff-repair-20261004.md",
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
    "next_agent": "researcher",
    "allowed_next_inputs": [
      "share/handoff-repair-20261004/researcher/task.md"
    ],
    "notes": "Keep work bounded to the task."
  },
  "goal": "Repair typed planner documentation, actual-file validation and explicit outer authorization delivery.",
  "scope": [
    "AGENTS.md",
    "tasker/AGENTS.md",
    "researcher/AGENTS.md",
    "planner/AGENTS.md",
    "implementer/AGENTS.md",
    "reviewer/AGENTS.md",
    "agent_loop_poc/",
    "README*.md",
    "share/handoff-repair-20261004/"
  ],
  "deliverables": [
    "Typed planner documentation",
    "Read-only validate and dispatch CLI",
    "Regression tests and recorded evidence"
  ],
  "acceptance_criteria": [
    "Malformed or stale actual outputs cannot pass validation.",
    "Blocked valid artifacts remain non-routable.",
    "Outer dispatch includes verified-human authorization context with exact scope.",
    "Historical experiment bytes unchanged."
  ],
  "conflicts": [],
  "source_of_truth": [
    "tasker/handoff-repair-20261004.md",
    "agent_loop_poc/contracts.py"
  ],
  "validation": [
    "Regression suite",
    "Historical evidence hash comparison",
    "CLI smoke and diff check"
  ],
  "cleanup": [
    "Auto-clean temporary tests; retain evidence."
  ],
  "rollback": [
    "Scoped inverse edits only; preserve unrelated work."
  ]
}
