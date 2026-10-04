{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "research_plan",
  "task_id": "luna-effort-pilot-20261004",
  "produced_by": "researcher",
  "status": "ready",
  "revision": "d57ef66d-59dc-44fb-a1c2-01abc7ed8485",
  "input_fingerprints": {
    "share/luna-effort-pilot-20261004/researcher/task.md": "f3408779fc9e0db9982ffbf4565049be1a97880b21d495b8dbf0cc6b8285ee1a"
  },
  "input_artifacts": [
    {
      "path": "share/luna-effort-pilot-20261004/researcher/task.md",
      "required": true,
      "summary": "Direct workflow input"
    }
  ],
  "trusted_sources": [
    {
      "path": "AGENTS.md",
      "summary": "Root workflow contract"
    },
    {
      "path": "researcher/AGENTS.md",
      "summary": "Stage contract"
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "share/luna-effort-pilot-20261004/researcher/task.md",
      "summary": "Task or handoff data"
    }
  ],
  "constraints": [
    "Only experiment directory and its pipeline artifacts may change.",
    "No model substitutions, hidden helper corrections, retries or unpublished excluded cells.",
    "Main orchestration uses same-invocation fallback; model stages fresh."
  ],
  "open_questions": [],
  "evidence": [
    {
      "kind": "task",
      "source": "tasker/luna-effort-pilot-20261004.md",
      "summary": "User authorized Luna low/high experiment and tested-model exception."
    }
  ],
  "handoff": {
    "next_agent": "planner",
    "allowed_next_inputs": [
      "share/luna-effort-pilot-20261004/planner/plan.md"
    ],
    "notes": "Preserve frozen scope and original comparison question."
  },
  "task_classification": "controlled_pilot_experiment",
  "goal_restatement": "Measure paired outcomes for low/high using unchanged workflow.",
  "requested_change_summary": "Add isolated experiment materials, run models, evaluate without product modifications.",
  "expected_impact_areas": [
    "Experiment evidence only"
  ],
  "assumptions": [
    {
      "id": "A1",
      "statement": "Luna means current gpt-6-luna exposed by collaboration tools.",
      "source": "Available tool model metadata and user request",
      "risk_if_wrong": "Different intended model; disclose exact identifier."
    }
  ],
  "risks": [
    {
      "id": "R1",
      "description": "Strict schema may stop before coding.",
      "impact": "Pilot observes workflow compatibility rather than code ability.",
      "mitigation": "Keep stop and denominator; no helper repair."
    },
    {
      "id": "R2",
      "description": "Same model produces correlated stage mistakes.",
      "impact": "Review success can be false.",
      "mitigation": "Independent frozen post-run tests."
    },
    {
      "id": "R3",
      "description": "Filesystem sandbox is logical, not OS-per-model isolation.",
      "impact": "Cross-arm or private-evaluator access would contaminate comparison.",
      "mitigation": "Explicit read/write allowlist; record limits; no claim of security isolation."
    }
  ],
  "non_goals": [
    "Benchmark general intelligence",
    "Prove workflow better than no workflow",
    "Build production runtime"
  ],
  "high_level_strategy": [
    "Freeze fixtures, protocol, evaluator and snapshots.",
    "Invoke fresh gated stages, alternating paired launch order.",
    "Evaluate and report each cell separately."
  ],
  "required_checks": [
    "frozen_inputs",
    "paired_runs",
    "independent_scoring",
    "cleanup"
  ],
  "proposed_task_updates": [],
  "failure_modes": [
    {
      "id": "F1",
      "trigger": "Model emits malformed artifact",
      "likely_stage": "tasker",
      "prevention": "Supply exact role rules and controller-generated lineage metadata; do not fix after run."
    },
    {
      "id": "F2",
      "trigger": "Unexpected infrastructure rejection",
      "likely_stage": "implementer",
      "prevention": "Record environment failure separately; no model substitution."
    }
  ]
}
