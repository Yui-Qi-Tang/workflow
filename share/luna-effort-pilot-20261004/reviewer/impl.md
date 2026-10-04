{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "implementation_brief",
  "task_id": "luna-effort-pilot-20261004",
  "produced_by": "planner",
  "status": "ready",
  "revision": "cda235bf-754d-40a3-be7e-3aae660fd08c",
  "input_fingerprints": {
    "share/luna-effort-pilot-20261004/planner/plan.md": "c53d969100955d7fc2b9f0af0118ceae10863e8f16460c61a56e71482f4349be"
  },
  "input_artifacts": [
    {
      "path": "share/luna-effort-pilot-20261004/planner/plan.md",
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
      "path": "planner/AGENTS.md",
      "summary": "Stage contract"
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "share/luna-effort-pilot-20261004/planner/plan.md",
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
    "next_agent": "implementer",
    "allowed_next_inputs": [
      "share/luna-effort-pilot-20261004/implementer/impl.md"
    ],
    "notes": "Preserve frozen scope and original comparison question."
  },
  "summary": "Build and run frozen six-cell pilot with main orchestration and independent scoring.",
  "inputs_used": [
    "share/luna-effort-pilot-20261004/planner/plan.md"
  ],
  "files_likely_to_change": [
    "experiments/luna-effort-pilot-20261004/**",
    "share/luna-effort-pilot-20261004/reviewer/**"
  ],
  "ordered_steps": [
    {
      "step": 1,
      "action": "Create protocol, fixtures, evaluator and snapshots; freeze hashes.",
      "rationale": "Prevent post-result changes.",
      "expected_evidence": "manifest.json and identical paired starter/task hashes"
    },
    {
      "step": 2,
      "action": "Dispatch allowed stages as fresh gpt-6-luna low/high invocations; gate every handoff with frozen controller.",
      "rationale": "Test real workflow rather than fabricate outputs.",
      "expected_evidence": "Prompts, raw artifacts, run metadata, gate states"
    },
    {
      "step": 3,
      "action": "Run private evaluation only after each cell terminates; inventory all edits.",
      "rationale": "Distinguish declarations from correctness.",
      "expected_evidence": "scores.json, evaluation logs and report"
    }
  ],
  "invariants": [
    "Do not fix model output.",
    "Use exact frozen inputs and gates.",
    "Count six cells even when blocked.",
    "Keep private evaluator and peer outputs outside model input allowlist."
  ],
  "validation_plan": [
    {
      "check": "frozen_inputs",
      "command_or_method": "Verify manifest digests and pair parity",
      "expected_result": "All frozen files unchanged; low/high input bytes identical.",
      "required": true
    },
    {
      "check": "paired_runs",
      "command_or_method": "Inspect dispatch metadata and stage gates",
      "expected_result": "Six cells accounted for with effort/model identity and actual terminal state.",
      "required": true
    },
    {
      "check": "independent_scoring",
      "command_or_method": "Run frozen evaluator against each final workspace",
      "expected_result": "Machine-readable per-case checks and clear evidence boundaries.",
      "required": true
    },
    {
      "check": "cleanup",
      "command_or_method": "Inventory experiment and temporary paths",
      "expected_result": "Only allowed outputs; no task scratch/cache remains.",
      "required": true
    }
  ],
  "cleanup_plan": [
    "Preserve raw model outputs and frozen evidence.",
    "Delete preparation scratch script and __pycache__ created by this task."
  ],
  "escalation_conditions": [
    {
      "condition": "Requested model unavailable or invocation failure",
      "return_target": "researcher",
      "reason": "Do not substitute a different model silently."
    }
  ],
  "rollback_hints": [
    "Leave isolated experiment evidence; do not revert existing work."
  ],
  "expected_output": {
    "result_artifact_path": "share/luna-effort-pilot-20261004/reviewer/result.md",
    "implementation_summary_requirements": [
      "Actual completed calls and six cell statuses",
      "Validation evidence",
      "Cleanup and limitations"
    ]
  }
}
