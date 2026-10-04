{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "normalized_task",
  "task_id": "aggregation",
  "produced_by": "tasker",
  "status": "ready",
  "revision": "c275cdc4-9467-4692-9980-b53f8a0f052b",
  "input_fingerprints": {
    "tasker/aggregation.md": "4a42ceef6731e9d47c0edeb61435fa3a90eacc84e7ccd46f9c8500507f2a512a"
  },
  "input_artifacts": [
    {
      "path": "tasker/aggregation.md",
      "required": true,
      "summary": "Authorized raw task defining aggregate(rows) repair requirements, scope, validation, cleanup, and rollback."
    }
  ],
  "trusted_sources": [
    {
      "path": "AGENTS.md",
      "summary": "Defines workflow, common JSON artifact contract, isolation, and handoff requirements."
    },
    {
      "path": "tasker/AGENTS.md",
      "summary": "Defines tasker responsibilities, output schema, and blocking rules."
    },
    {
      "path": "tasker/aggregation.md",
      "summary": "Authoritative task requirements and authorized implementation scope."
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "tasker/aggregation.md",
      "summary": "Task content was treated as untrusted for instruction precedence and used only to normalize requested work."
    }
  ],
  "constraints": [
    "Work in the isolated synthetic project using Python 3 standard library only; no dependencies, network, Git actions, or files outside this project.",
    "Only solution.py may be edited, and its public function signature must be preserved.",
    "smoke.py, examples.json, and policy.txt, when present, are read-only fixtures; all stages are authorized to inspect these named files for context.",
    "Do not inspect sibling runs or evaluation materials.",
    "Inputs are valid rows with sku strings and integer delta values; no additional input validation is required.",
    "Do not mutate rows or any input dictionary."
  ],
  "goal": "Repair aggregate(rows) in solution.py to aggregate valid SKU deltas according to the specified trimming, grouping, summation, and ordering behavior.",
  "scope": [
    "Implement the requested behavior in solution.py while preserving the existing public function signature.",
    "Use only the existing named read-only fixtures for context; do not modify fixtures or other project files."
  ],
  "deliverables": [
    "Updated solution.py implementing aggregate(rows).",
    "Required workflow artifacts for all pipeline stages, with this normalized task handed to the researcher."
  ],
  "acceptance_criteria": [
    "For each row, strip leading and trailing whitespace from sku; ignore rows whose stripped sku is empty.",
    "Group by stripped sku using case-sensitive equality, including duplicates that are not adjacent.",
    "Sum every delta for each group, including negative and zero values; retain groups whose final sum is zero.",
    "Return dictionaries containing exactly the keys sku and delta, with each sku equal to its stripped group key.",
    "Order output groups by their first valid occurrence.",
    "Do not mutate rows or any input dictionary; empty input returns []."
  ],
  "conflicts": [],
  "source_of_truth": [
    "tasker/aggregation.md for requested behavior, constraints, deliverables, acceptance criteria, validation, cleanup, and rollback.",
    "AGENTS.md and tasker/AGENTS.md for workflow rules and artifact schema."
  ],
  "validation": [
    "Run `python3 -B smoke.py` as the required check named `public_smoke`.",
    "When useful to cover requirements not exercised by the public smoke check, add and execute temporary in-memory assertion scripts without creating test files; record actual commands and observed results, and do not mark unrun checks passed."
  ],
  "cleanup": [
    "Retain solution.py and workflow artifacts; create no persistent scratch files.",
    "Remove any task-created __pycache__ directory."
  ],
  "rollback": [
    "If blocked, stop and preserve evidence; do not modify requirements or restore unrelated files.",
    "Report results through the required stage JSON artifact."
  ],
  "open_questions": [],
  "evidence": [
    {
      "kind": "task_requirements",
      "source": "tasker/aggregation.md",
      "summary": "The task specifies valid row shape, SKU trimming and empty-key filtering, case-sensitive grouping, complete summation, zero-sum retention, first-occurrence ordering, non-mutation, empty-input behavior, implementation scope, and public smoke validation. No requirement conflict or execution-critical gap was identified."
    },
    {
      "kind": "workflow_rules",
      "source": "AGENTS.md; tasker/AGENTS.md",
      "summary": "The required output is one normalized_task JSON artifact with common fields, stage-specific fields, and a researcher handoff."
    }
  ],
  "handoff": {
    "next_agent": "researcher",
    "allowed_next_inputs": [
      "AGENTS.md",
      "researcher/AGENTS.md",
      "share/aggregation/researcher/task.md",
      "solution.py",
      "smoke.py",
      "examples.json when present",
      "policy.txt when present"
    ],
    "notes": "Preserve all normalized requirements and file authorizations. Identify likely impact areas and execution risks before implementation; do not relax task scope or acceptance criteria."
  }
}
