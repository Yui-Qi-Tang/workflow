{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "implementation_brief",
  "task_id": "skill-ab-20261004",
  "produced_by": "planner",
  "status": "ready",
  "revision": "af539845-08e1-4753-a17a-5291171d8584",
  "input_fingerprints": {
    "share/skill-ab-20261004/planner/plan.md": "deb9bce3fc1ab7bca01e0fb582c2ac2d119692622768df900f9598bfbee20de3"
  },
  "input_artifacts": [
    {
      "path": "share/skill-ab-20261004/planner/plan.md",
      "required": true,
      "summary": "Current direct experiment input."
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
      "source": "Current human skill A/B subagent experiment request."
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "share/skill-ab-20261004/planner/plan.md"
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
    "next_agent": "implementer",
    "allowed_next_inputs": [
      "share/skill-ab-20261004/implementer/impl.md",
      "experiments/skill-ab-20261004",
      "agent_loop_poc",
      "AGENTS.md",
      ".agents/skills/workflow-orchestrator/SKILL.md"
    ],
    "notes": "Only bounded trial agents receive execution exception; freeze before dispatch."
  },
  "summary": "Freeze and run the six-cell skill-body pilot, then evaluate without repairing trial outputs.",
  "inputs_used": [
    "share/skill-ab-20261004/planner/plan.md"
  ],
  "files_likely_to_change": [
    "experiments/skill-ab-20261004/**",
    "share/skill-ab-20261004/**"
  ],
  "ordered_steps": [
    {
      "step": 1,
      "action": "Create protocol, paired fixtures, identical instrumented CLI and deterministic evaluator; freeze hashes.",
      "rationale": "Define intervention and denominators before outcomes.",
      "expected_evidence": "protocol.json, manifest.json, initial inventories."
    },
    {
      "step": 2,
      "action": "Dispatch fresh same-model/effort trial agents in three pairs with scoped outer human authorization and no history.",
      "rationale": "Only intended difference is skill-body availability/loading.",
      "expected_evidence": "Exact prompts, spawn request/response, raw artifacts and receipts."
    },
    {
      "step": 3,
      "action": "Independently recount semantics, saved-artifact checks, terminal routes, scope and treatment exposure; preserve raw results.",
      "rationale": "Do not trust self-reported success.",
      "expected_evidence": "scores.json and report with limitations."
    }
  ],
  "invariants": [
    "Only skill-body loading differs between paired arms; common current rules, README, controller, fixtures, model/effort inheritance, time limit and scoring are frozen.",
    "Six fresh trial agents: three cases times skill on/off, one invocation per cell, no cross-invocation retries or outcome-driven assistance.",
    "Human explicitly authorizes these tested subagents to execute their isolated trials despite the usual opposition-only rule. No other task gets this exception.",
    "Each trial is a sole orchestrator using all five checkpoints in same_invocation mode; valid blockers may stop earlier. No nested agents.",
    "Main agent owns protocol, fixtures, evaluation and conclusions. Protect product files, prior experiments and current uncommitted work.",
    "No network, dependency installs, commits, pushes or real external side effects in trials. Preserve raw evidence; do not repair model outputs."
  ],
  "validation_plan": [
    {
      "check": "frozen_protocol",
      "command_or_method": "frozen_protocol evidence checks under frozen protocol",
      "expected_result": "Observed and recorded without outcome-driven changes",
      "required": true
    },
    {
      "check": "paired_inputs",
      "command_or_method": "paired_inputs evidence checks under frozen protocol",
      "expected_result": "Observed and recorded without outcome-driven changes",
      "required": true
    },
    {
      "check": "observed_trials",
      "command_or_method": "observed_trials evidence checks under frozen protocol",
      "expected_result": "Observed and recorded without outcome-driven changes",
      "required": true
    },
    {
      "check": "independent_scores",
      "command_or_method": "independent_scores evidence checks under frozen protocol",
      "expected_result": "Observed and recorded without outcome-driven changes",
      "required": true
    },
    {
      "check": "preservation",
      "command_or_method": "preservation evidence checks under frozen protocol",
      "expected_result": "Observed and recorded without outcome-driven changes",
      "required": true
    }
  ],
  "cleanup_plan": [
    "Keep raw evidence; remove only created scratch/caches."
  ],
  "escalation_conditions": [
    {
      "condition": "Missing essential trial authority or scope escape",
      "return_target": "tasker",
      "reason": "Stop affected cell and report; do not broaden permissions."
    }
  ],
  "rollback_hints": [
    "No production mutation; preserve failed attempts."
  ],
  "expected_output": {
    "result_artifact_path": "share/skill-ab-20261004/reviewer/result.md",
    "implementation_summary_requirements": [
      "Report all six cells and denominator.",
      "Separate skill efficacy from structural checks.",
      "Disclose contamination and instrumentation limits."
    ]
  }
}
