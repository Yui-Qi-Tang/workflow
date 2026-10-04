{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "implementation_brief",
  "task_id": "aggregation",
  "produced_by": "planner",
  "status": "ready",
  "revision": "f9837d03-e211-4a3c-b677-0de8d8dd32c9",
  "input_fingerprints": {
    "share/aggregation/planner/plan.md": "f434e09ff3a00e8ccf8e1f7550c45b6edfc3034af57352114e279a3448f4a4f8"
  },
  "input_artifacts": [
    {
      "path": "share/aggregation/planner/plan.md",
      "required": true,
      "summary": "Research plan with the authorized aggregate behavior, scope, constraints, risks, and required checks."
    },
    {
      "path": "solution.py",
      "required": false,
      "summary": "Read-only inspection shows aggregate currently overwrites raw SKU values and sorts keys."
    },
    {
      "path": "smoke.py",
      "required": false,
      "summary": "Read-only inspection shows public smoke covers empty input and one row."
    }
  ],
  "trusted_sources": [
    {
      "path": "AGENTS.md",
      "summary": "Defines shared artifact contract, workflow stages, scope, and cleanup rules."
    },
    {
      "path": "planner/AGENTS.md",
      "summary": "Defines planner process, implementation_brief schema, and output restrictions."
    },
    {
      "path": "share/aggregation/planner/plan.md",
      "summary": "Authoritative upstream research plan preserving the approved task requirements and checks."
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "share/aggregation/planner/plan.md",
      "summary": "Workflow artifact treated as task data; its stated requirements and evidence inform this brief."
    },
    {
      "path": "solution.py",
      "summary": "Read-only source evidence used to identify implementation behavior and likely change location."
    },
    {
      "path": "smoke.py",
      "summary": "Read-only fixture evidence used to scope validation coverage."
    }
  ],
  "constraints": [
    "Edit only solution.py and only the aggregate(rows) implementation; preserve its public signature.",
    "Use Python 3 standard library only; no dependencies, network, Git actions, or files outside the isolated project.",
    "Treat smoke.py, examples.json, and policy.txt, when present, as read-only fixtures; do not inspect sibling runs or evaluation materials.",
    "Inputs contain valid rows with string sku and integer delta values; do not add input validation.",
    "Do not mutate input rows or dictionaries.",
    "Retain solution.py and workflow artifacts, create no persistent scratch files, and remove any task-created __pycache__ directory.",
    "Preserve all upstream acceptance criteria and do not expand scope."
  ],
  "open_questions": [],
  "evidence": [
    {
      "kind": "upstream_requirements",
      "source": "share/aggregation/planner/plan.md",
      "summary": "Requirements are trimmed non-empty case-sensitive SKU groups, sum all deltas including negative and zero values, retain zero totals, preserve first valid occurrence order, emit exactly sku/delta keys, preserve inputs, and return an empty list for empty input."
    },
    {
      "kind": "source_inspection",
      "source": "solution.py",
      "summary": "Current function keys by untrimmed SKU, overwrites earlier values, and sorts keys; modify only aggregate(rows)."
    },
    {
      "kind": "validation_inspection",
      "source": "smoke.py",
      "summary": "Public smoke has empty and single-row assertions; broader criteria require the planned in-memory acceptance check. No checks were run during planning."
    }
  ],
  "handoff": {
    "next_agent": "implementer",
    "allowed_next_inputs": [
      "AGENTS.md",
      "implementer/AGENTS.md",
      "share/aggregation/planner/plan.md",
      "share/aggregation/implementer/impl.md",
      "solution.py",
      "smoke.py"
    ],
    "notes": "Implement only the approved aggregate(rows) behavior in solution.py, run both required checks, record actual outcomes, and clean task-created __pycache__."
  },
  "summary": "Implement the specified SKU normalization and aggregation behavior in aggregate(rows), preserving first-valid occurrence order and all upstream constraints.",
  "inputs_used": [
    "share/aggregation/planner/plan.md",
    "solution.py",
    "smoke.py",
    "AGENTS.md",
    "planner/AGENTS.md"
  ],
  "files_likely_to_change": [
    "solution.py"
  ],
  "ordered_steps": [
    {
      "step": 1,
      "action": "Inspect aggregate(rows) and preserve its current public signature; make no fixture or workflow artifact edits.",
      "rationale": "The authorized implementation scope is limited to the function in solution.py.",
      "expected_evidence": "A scoped edit to aggregate(rows) only."
    },
    {
      "step": 2,
      "action": "Process rows in input order, strip each sku, skip rows whose stripped sku is empty, and accumulate integer deltas by the normalized case-sensitive sku while retaining insertion order.",
      "rationale": "This implements grouping, summation, empty-SKU filtering, and first valid occurrence ordering together.",
      "expected_evidence": "Non-adjacent normalized duplicate rows combine and output groups remain in first-seen order."
    },
    {
      "step": 3,
      "action": "Build the returned list from the ordered groups with exactly sku and delta keys, retaining groups whose final sum is zero and without modifying input dictionaries.",
      "rationale": "Zero retention, exact output shape, and input immutability are explicit requirements.",
      "expected_evidence": "Returned values preserve zero totals and input rows compare equal to their pre-call copies."
    },
    {
      "step": 4,
      "action": "Run public_smoke and acceptance_contract_in_memory, recording the actual command and result for each.",
      "rationale": "The public fixture covers only a small subset of the required behavior.",
      "expected_evidence": "Both required checks have observed results in the implementation_result artifact."
    },
    {
      "step": 5,
      "action": "Remove any task-created __pycache__ directory and confirm no persistent scratch files were created.",
      "rationale": "The upstream cleanup constraint requires cache cleanup and prohibits persistent scratch artifacts.",
      "expected_evidence": "Cleanup status is recorded in the implementation_result artifact."
    }
  ],
  "invariants": [
    "Only solution.py may be edited, and the aggregate(rows) signature must remain unchanged.",
    "SKU matching is case-sensitive after stripping surrounding whitespace; empty stripped SKUs are skipped.",
    "Every accepted group's delta is the sum of all its row deltas, including negative and zero deltas.",
    "A group with total zero remains in the output.",
    "Output order follows the first row with a non-empty stripped SKU for each group.",
    "Each returned dictionary has exactly the sku and delta keys.",
    "No input row or dictionary is mutated."
  ],
  "validation_plan": [
    {
      "check": "public_smoke",
      "command_or_method": "python3 -B smoke.py",
      "expected_result": "Process exits successfully and prints public_smoke: 2 assertions passed.",
      "required": true
    },
    {
      "check": "acceptance_contract_in_memory",
      "command_or_method": "python3 -B -c 'from solution import aggregate; rows=[{\"sku\":\" \",\"delta\":99},{\"sku\":\"Beta\",\"delta\":1},{\"sku\":\"alpha\",\"delta\":2},{\"sku\":\"Beta\",\"delta\":-1},{\"sku\":\" Beta \",\"delta\":0},{\"sku\":\"beta\",\"delta\":4}]; before=[dict(row) for row in rows]; expected=[{\"sku\":\"Beta\",\"delta\":0},{\"sku\":\"alpha\",\"delta\":2},{\"sku\":\"beta\",\"delta\":4}]; actual=aggregate(rows); assert actual == expected; assert all(set(item)=={\"sku\",\"delta\"} for item in actual); assert rows == before; print(\"acceptance_contract_in_memory: passed\")'",
      "expected_result": "All assertions pass, confirming whitespace-only filtering, trimming, non-adjacent summation, zero retention, case sensitivity, first-valid order, exact keys, and input immutability.",
      "required": true
    }
  ],
  "cleanup_plan": [
    "Do not create persistent scratch files; keep the acceptance check in memory via python3 -B -c.",
    "Remove any task-created __pycache__ directory after checks.",
    "Record cleanup status and any intentional leftovers in implementation_result."
  ],
  "escalation_conditions": [
    {
      "condition": "A required behavior cannot be implemented by changing only aggregate(rows) in solution.py while preserving the public signature.",
      "return_target": "researcher",
      "reason": "Resolving this would require revisiting scope or task requirements."
    },
    {
      "condition": "A planned required check fails for a reason that cannot be corrected within the approved scope, or execution requires network, dependencies, external files, or relaxing acceptance criteria.",
      "return_target": "researcher",
      "reason": "The implementer must stop and report the blocker rather than expanding authorization."
    }
  ],
  "rollback_hints": [
    "If the focused change causes a required check to fail, revise only aggregate(rows) within the stated invariants.",
    "If the task must be abandoned, restore only the task's aggregate(rows) edit in solution.py; preserve pre-existing files and workflow artifacts."
  ],
  "expected_output": {
    "result_artifact_path": "share/aggregation/reviewer/result.md",
    "implementation_summary_requirements": "Report files actually changed, behavior implemented, each required validation check by its exact name with observed pass/fail evidence, cleanup status, and any unresolved blocker; do not claim unrun checks passed."
  }
}
