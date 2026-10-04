{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "normalized_task",
  "task_id": "skill-ab-20261004",
  "produced_by": "tasker",
  "status": "ready",
  "revision": "2c1fd75b-3334-4e76-a556-10cbcbaa9e48",
  "input_fingerprints": {
    "tasker/skill-ab-20261004.md": "68058e40161ce7ade1c34b4e87573c83e190876cfb13dfa2f08251971753831c"
  },
  "input_artifacts": [
    {
      "path": "tasker/skill-ab-20261004.md",
      "required": true,
      "summary": "Current direct experiment input."
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
      "source": "Current human skill A/B subagent experiment request."
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "tasker/skill-ab-20261004.md"
    }
  ],
  "constraints": [
    "Only skill-body loading differs between paired arms; common current rules, README, controller, fixtures, model/effort inheritance, time limit and scoring are frozen.",
    "Six fresh trial agents: three cases times skill on/off, one invocation per cell, no cross-invocation retries or outcome-driven assistance.",
    "Human explicitly authorizes these tested subagents to execute their isolated trials despite the usual opposition-only rule. No other task gets this exception.",
    "Each trial is a sole orchestrator using all five checkpoints in same_invocation mode; valid blockers may stop earlier. No nested agents.",
    "Main agent owns protocol, fixtures, evaluation and conclusions. Protect product files, prior experiments and current uncommitted work.",
    "No network, dependency installs, commits, pushes or real external side effects in trials. Preserve raw evidence; do not repair model outputs."
  ],
  "open_questions": [],
  "evidence": [
    {
      "kind": "execution_mode",
      "source": "Main administrative pipeline",
      "summary": "same_invocation; not one of the six trial cells."
    }
  ],
  "handoff": {
    "next_agent": "researcher",
    "allowed_next_inputs": [
      "share/skill-ab-20261004/researcher/task.md",
      "experiments/skill-ab-20261004",
      "agent_loop_poc",
      "AGENTS.md",
      ".agents/skills/workflow-orchestrator/SKILL.md"
    ],
    "notes": "Only bounded trial agents receive execution exception; freeze before dispatch."
  },
  "goal": "Measure skill-body incremental value in a frozen paired pilot.",
  "scope": [
    "experiments/skill-ab-20261004/**",
    "share/skill-ab-20261004/**"
  ],
  "deliverables": [
    "Frozen protocol and six trial roots",
    "Raw outputs/CLI receipts",
    "Independent recount and bounded report"
  ],
  "acceptance_criteria": [
    "frozen_protocol",
    "paired_inputs",
    "observed_trials",
    "independent_scores",
    "preservation"
  ],
  "conflicts": [],
  "source_of_truth": [
    "Current human request",
    "Current role rules/controller/skill snapshot",
    "Frozen protocol/evaluator before dispatch"
  ],
  "validation": [
    "frozen_protocol",
    "paired_inputs",
    "observed_trials",
    "independent_scores",
    "preservation"
  ],
  "cleanup": [
    "Retain raw evidence; remove only created scratch/caches."
  ],
  "rollback": [
    "Remove only this new experiment if requested; no product writes."
  ]
}
