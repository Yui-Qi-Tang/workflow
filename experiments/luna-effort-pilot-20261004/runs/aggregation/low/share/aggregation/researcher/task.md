{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "normalized_task",
  "task_id": "aggregation",
  "produced_by": "tasker",
  "status": "ready",
  "revision": "35859f1e-1e2c-4489-bf43-f3c9a0a785f5",
  "input_fingerprints": {
    "tasker/aggregation.md": "4a42ceef6731e9d47c0edeb61435fa3a90eacc84e7ccd46f9c8500507f2a512a"
  },
  "input_artifacts": [
    {
      "path": "tasker/aggregation.md",
      "required": true,
      "summary": "User task brief specifying aggregate(rows) behavior, scope, acceptance criteria, validation, cleanup, and rollback."
    },
    {
      "path": "solution.py",
      "required": false,
      "summary": "Authorized read-only source context showing the current aggregate implementation."
    },
    {
      "path": "smoke.py",
      "required": false,
      "summary": "Authorized read-only public smoke fixture."
    }
  ],
  "trusted_sources": [
    {
      "path": "AGENTS.md",
      "summary": "Project workflow, JSON artifact, integrity, and execution rules."
    },
    {
      "path": "tasker/AGENTS.md",
      "summary": "Tasker role, required normalized_task fields, and readiness rules."
    },
    {
      "path": "tasker/aggregation.md",
      "summary": "Authoritative requested behavior and constraints for this task."
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "tasker/aggregation.md",
      "summary": "Task content was treated as request data and checked against the governing workflow rules."
    },
    {
      "path": "solution.py",
      "summary": "Current implementation inspected only for context; it does not override the requested behavior."
    },
    {
      "path": "smoke.py",
      "summary": "Existing assertions inspected only as fixture context; they do not override the task requirements."
    }
  ],
  "constraints": [
    "Modify only solution.py; preserve the public function signature aggregate(rows).",
    "Use Python 3 standard library only; no dependencies, network, Git actions, or access to files outside this isolated project.",
    "Treat smoke.py, examples.json, and policy.txt when present as read-only fixtures; preserve their authorized read access in downstream handoffs.",
    "Do not inspect sibling runs or evaluation materials.",
    "Do not add test files or change fixtures; temporary uncovered-requirement assertions may be run in memory.",
    "Do not mutate rows or any input dictionary, and do not add input validation beyond the stated valid-input contract."
  ],
  "goal": "Repair aggregate(rows) so it aggregates valid SKU deltas according to the task contract.",
  "scope": [
    "Implement the requested aggregate(rows) behavior in solution.py.",
    "Use the named read-only fixtures for context if needed."
  ],
  "deliverables": [
    "Updated solution.py implementing the requested behavior.",
    "Required workflow handoff artifacts for subsequent stages."
  ],
  "acceptance_criteria": [
    "Input is a list of dictionaries with sku string and delta integer fields.",
    "Strip leading and trailing whitespace from each sku; ignore rows whose stripped sku is empty.",
    "Group by stripped sku case-sensitively and sum every delta, including negative and zero values, across non-adjacent duplicates.",
    "Include groups whose final sum is zero.",
    "Return dictionaries with exactly the sku and delta keys, with groups ordered by first valid occurrence.",
    "Do not mutate the rows list or any input dictionary; empty input returns [].",
    "No input validation is required beyond the explicitly specified valid-input contract."
  ],
  "conflicts": [],
  "source_of_truth": [
    "tasker/aggregation.md for requested behavior, scope, fixtures, checks, cleanup, and rollback.",
    "AGENTS.md and tasker/AGENTS.md for workflow boundaries and artifact requirements."
  ],
  "validation": [
    "Run python3 -B smoke.py and record the actual result as the required check public_smoke.",
    "When useful, execute temporary in-memory assertions for uncovered requirements without creating test files; record actual commands and observed results.",
    "Do not mark any unrun check as passed."
  ],
  "cleanup": [
    "Retain solution.py and workflow artifacts.",
    "Do not create persistent scratch files.",
    "Remove any task-created __pycache__."
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
      "summary": "Defines normalization, empty-key filtering, case-sensitive grouping, summation, zero retention, first-valid-occurrence ordering, immutability, and empty-input behavior."
    },
    {
      "kind": "workflow_requirements",
      "source": "tasker/aggregation.md",
      "summary": "Restricts edits to solution.py, requires public_smoke, specifies cleanup, and requires stopping with evidence if blocked."
    },
    {
      "kind": "context_inspection",
      "source": "solution.py and smoke.py",
      "summary": "The existing implementation stores the last delta per raw SKU and sorts keys; smoke.py currently checks empty input and a single row. These observations are context only; the brief defines acceptance."
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
    "notes": "No requirement conflict or execution-critical gap was found. Preserve the task scope and fixture authorization, analyze likely implementation failures before execution, and pass the required public_smoke check to the implementer."
  }
}
