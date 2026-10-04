{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "research_plan",
  "task_id": "skill-ab-20261004",
  "produced_by": "researcher",
  "status": "ready",
  "revision": "62f0e74f-0955-44a7-828c-1635d674ea5c",
  "input_fingerprints": {
    "share/skill-ab-20261004/researcher/task.md": "e32ff1d854d24b1931257d213165255db1d39639c7a74adf6ffdd208aeab0e64"
  },
  "input_artifacts": [
    {
      "path": "share/skill-ab-20261004/researcher/task.md",
      "required": true,
      "summary": "Current direct experiment input."
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
      "source": "Current human skill A/B subagent experiment request."
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "share/skill-ab-20261004/researcher/task.md"
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
    "next_agent": "planner",
    "allowed_next_inputs": [
      "share/skill-ab-20261004/planner/plan.md",
      "experiments/skill-ab-20261004",
      "agent_loop_poc",
      "AGENTS.md",
      ".agents/skills/workflow-orchestrator/SKILL.md"
    ],
    "notes": "Only bounded trial agents receive execution exception; freeze before dispatch."
  },
  "task_classification": "controlled_skill_ab_pilot",
  "goal_restatement": "Measure incremental skill loading, holding all other intended inputs fixed.",
  "requested_change_summary": "Build and run three paired cases with independent verification.",
  "expected_impact_areas": [
    "New experiment and audit only"
  ],
  "assumptions": [
    {
      "id": "a1",
      "statement": "Skill catalog metadata may be ambient in both arms; control excludes body loading.",
      "source": "Current environment skill catalog.",
      "risk_if_wrong": "Body contamination invalidates treatment contrast."
    }
  ],
  "risks": [
    {
      "id": "r1",
      "description": "Shared filesystem is not OS isolation.",
      "impact": "Cross-arm contamination.",
      "mitigation": "Explicit allowlists, frozen manifests, available trace/receipt audit and candid limits."
    },
    {
      "id": "r2",
      "description": "Only three pairs and provider seed unavailable.",
      "impact": "No general or statistical efficacy inference.",
      "mitigation": "Pilot claim and separate descriptive axes."
    }
  ],
  "non_goals": [
    "Change production skill/rules",
    "Compare reasoning levels",
    "Independent fresh model per stage",
    "General model ranking"
  ],
  "high_level_strategy": [
    "Freeze common snapshots and deterministic expected outcomes.",
    "Use identical transparent CLI instrumentation in both arms.",
    "Run paired fresh trial agents without assistance.",
    "Recount files and receipts, retain failures."
  ],
  "required_checks": [
    "frozen_protocol",
    "paired_inputs",
    "observed_trials",
    "independent_scores",
    "preservation"
  ],
  "proposed_task_updates": [],
  "failure_modes": [
    {
      "id": "f1",
      "trigger": "Control loads skill body or frozen input changes.",
      "likely_stage": "implementer",
      "prevention": "Flag contamination and exclude causal interpretation without silently replacing cell."
    }
  ]
}
