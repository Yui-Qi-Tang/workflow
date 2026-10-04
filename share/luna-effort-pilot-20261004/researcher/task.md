{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "normalized_task",
  "task_id": "luna-effort-pilot-20261004",
  "produced_by": "tasker",
  "status": "ready",
  "revision": "2beb75f6-9ae0-45c8-b0a8-3958a4e375e2",
  "input_fingerprints": {
    "tasker/luna-effort-pilot-20261004.md": "4c9d434753d5d452ee733e5262140768354fe7598f8f579ed95c386b7756d1e2"
  },
  "input_artifacts": [
    {
      "path": "tasker/luna-effort-pilot-20261004.md",
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
      "path": "tasker/AGENTS.md",
      "summary": "Stage contract"
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "tasker/luna-effort-pilot-20261004.md",
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
    "next_agent": "researcher",
    "allowed_next_inputs": [
      "share/luna-effort-pilot-20261004/researcher/task.md"
    ],
    "notes": "Preserve frozen scope and original comparison question."
  },
  "goal": "Compare gpt-6-luna low and high on three identical workflow tasks.",
  "scope": [
    "experiments/luna-effort-pilot-20261004/**",
    "share/luna-effort-pilot-20261004/**"
  ],
  "deliverables": [
    "Frozen protocol and reproducible scoring",
    "Six cell outcomes and all raw artifacts",
    "Comparison report"
  ],
  "acceptance_criteria": [
    "All six cells accounted for.",
    "Only effort intentionally differs; inputs paired.",
    "No unsupported efficacy conclusion."
  ],
  "conflicts": [],
  "source_of_truth": [
    "tasker/luna-effort-pilot-20261004.md"
  ],
  "validation": [
    "Frozen hashes and paired parity",
    "Controller gate evidence",
    "Independent private tests and scope audit"
  ],
  "cleanup": [
    "Keep evidence; remove temporary scripts/caches."
  ],
  "rollback": [
    "Stop isolated runs; preserve pre-existing repository changes."
  ]
}
