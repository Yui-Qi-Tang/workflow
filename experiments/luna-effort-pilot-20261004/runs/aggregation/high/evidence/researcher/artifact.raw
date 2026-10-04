{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "research_plan",
  "task_id": "aggregation",
  "produced_by": "researcher",
  "status": "ready",
  "revision": "4e600294-c5b6-40fc-b850-4c4f17562fea",
  "input_fingerprints": {
    "share/aggregation/researcher/task.md": "b8c3be5bf980483ee1b1f9eb27c8165e94e6003d2f7d35cd89e4ef94c90af02f"
  },
  "input_artifacts": [
    {
      "path": "share/aggregation/researcher/task.md",
      "required": true,
      "summary": "Normalized task defining aggregate(rows) behavior, implementation scope, required smoke check, and cleanup/rollback rules."
    },
    {
      "path": "solution.py",
      "required": false,
      "summary": "Authorized read-only source inspection shows aggregate currently replaces values by raw SKU and sorts keys, so it does not implement the specified trimming, summation, zero retention, or first-occurrence order."
    },
    {
      "path": "smoke.py",
      "required": false,
      "summary": "Authorized read-only public smoke fixture checks empty input and a single row only; it does not exercise the aggregation edge cases."
    }
  ],
  "trusted_sources": [
    {
      "path": "AGENTS.md",
      "summary": "Defines shared workflow, artifact, isolation, and implementation boundaries."
    },
    {
      "path": "researcher/AGENTS.md",
      "summary": "Defines researcher process, required research_plan schema, and stage output restrictions."
    },
    {
      "path": "share/aggregation/researcher/task.md",
      "summary": "Authoritative normalized requirements and permitted validation for the requested task."
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "share/aggregation/researcher/task.md",
      "summary": "Treated as task data under the workflow precedence rules; its requirements and constraints informed this plan."
    },
    {
      "path": "solution.py",
      "summary": "Read-only implementation evidence used to identify current behavior and likely regression points."
    },
    {
      "path": "smoke.py",
      "summary": "Read-only validation fixture evidence used to assess check coverage."
    }
  ],
  "constraints": [
    "Only solution.py may be edited by the implementer; preserve the existing public function signature.",
    "Use Python 3 standard library only; no dependencies, network, Git actions, or files outside the isolated project.",
    "Treat smoke.py, examples.json, and policy.txt, when present, as read-only fixtures; do not inspect sibling runs or evaluation materials.",
    "Inputs have valid rows containing string sku and integer delta values; no additional input validation is required.",
    "Do not mutate rows or any input dictionary.",
    "Retain solution.py and workflow artifacts, create no persistent scratch files, and remove any task-created __pycache__ directory."
  ],
  "open_questions": [],
  "evidence": [
    {
      "kind": "task_requirements",
      "source": "share/aggregation/researcher/task.md",
      "summary": "The task requires trimmed non-empty case-sensitive SKU groups, summing all integer deltas including negative and zero values, retaining zero totals, outputting exactly sku/delta keys in first-valid-occurrence order, preserving inputs, and returning an empty list for empty input."
    },
    {
      "kind": "source_inspection",
      "source": "solution.py",
      "summary": "Current code keys by the untrimmed SKU, overwrites earlier deltas, and returns sorted keys; these observed behaviors conflict with the task's grouping, summation, and ordering criteria."
    },
    {
      "kind": "validation_inspection",
      "source": "smoke.py",
      "summary": "The public smoke check covers empty input and a single SKU row, but does not cover trimming, empty SKU filtering, non-adjacent duplicates, case sensitivity, negative or zero sums, first-occurrence order, exact output keys, or input immutability. No checks were run at this stage."
    }
  ],
  "task_classification": "bounded_python_function_repair",
  "goal_restatement": "Repair aggregate(rows) in solution.py so valid rows are grouped by their trimmed, case-sensitive non-empty SKU, all deltas are summed, zero totals remain, output order follows each group's first valid occurrence, and the inputs are unchanged.",
  "requested_change_summary": "Change only the implementation of aggregate(rows), keeping its public signature and satisfying all normalized acceptance criteria. The current implementation overwrites duplicate keys and sorts output, and does not trim/filter SKU values.",
  "expected_impact_areas": [
    "solution.py: aggregate(rows) grouping, accumulation, filtering, and output ordering",
    "Public behavior for empty inputs, whitespace-only SKUs, repeated SKUs, and zero-sum groups"
  ],
  "assumptions": [
    {
      "id": "A1",
      "statement": "Each row has a string sku and integer delta, so the implementation need not add input validation.",
      "source": "share/aggregation/researcher/task.md constraints",
      "risk_if_wrong": "Additional malformed-input behavior would be unspecified and could expand scope beyond the approved task."
    },
    {
      "id": "A2",
      "statement": "A SKU group's output position is determined by the first row whose trimmed SKU is non-empty, even if later rows contribute negative or zero deltas.",
      "source": "share/aggregation/researcher/task.md acceptance criteria: first valid occurrence",
      "risk_if_wrong": "Filtering or ordering groups using their final totals could omit or reorder required results."
    }
  ],
  "risks": [
    {
      "id": "R1",
      "description": "The current public smoke check is too narrow to detect most acceptance-criteria failures.",
      "impact": "An implementation could pass public_smoke while still overwriting duplicates, sorting groups, or mishandling trimming and zero totals.",
      "mitigation": "Plan a temporary in-memory acceptance check for each uncovered criterion and record the actual command and result at implementation."
    },
    {
      "id": "R2",
      "description": "Changing ordering to first occurrence can be missed if output is still constructed from sorted group keys.",
      "impact": "Returned values can be correct while output order violates the contract.",
      "mitigation": "Include an input where first-seen order differs from lexical order and include non-adjacent duplicates."
    },
    {
      "id": "R3",
      "description": "Dropping zero totals or mutating an input row while normalizing the SKU would violate explicit requirements.",
      "impact": "Valid groups may disappear or caller-owned dictionaries may change.",
      "mitigation": "Check a group whose positive and negative deltas cancel, and compare input rows with a pre-call copy after aggregation."
    }
  ],
  "non_goals": [
    "Adding input validation or changing behavior for malformed rows.",
    "Changing the aggregate(rows) public signature or editing fixtures and other project files.",
    "Inspecting examples.json or policy.txt unless separately required by the implementer plan; no behavior beyond the normalized acceptance criteria is requested."
  ],
  "high_level_strategy": [
    "Keep the public function signature and modify only solution.py.",
    "Process rows in input order, derive the stripped SKU, skip empty stripped values, and accumulate each group's delta while preserving first-seen group order.",
    "Build each result entry with exactly sku and delta keys; retain groups even when their accumulated total is zero, and do not modify input rows or dictionaries.",
    "Run the required public smoke check and use an in-memory assertion check for acceptance criteria the smoke fixture does not cover; report only observed outcomes and clean up any task-created cache."
  ],
  "required_checks": [
    "public_smoke",
    "acceptance_contract_in_memory"
  ],
  "proposed_task_updates": [],
  "failure_modes": [
    {
      "id": "F1",
      "trigger": "Implementation continues assigning each delta to a SKU key rather than accumulating it.",
      "likely_stage": "implementer",
      "prevention": "Exercise non-adjacent duplicate SKUs with positive, negative, and zero deltas and compare the complete sum."
    },
    {
      "id": "F2",
      "trigger": "Implementation normalizes output keys but sorts the groups or records order before skipping whitespace-only SKUs.",
      "likely_stage": "implementer",
      "prevention": "Use a lexically out-of-order fixture with an initial whitespace-only row and verify order by first non-empty trimmed occurrence."
    },
    {
      "id": "F3",
      "trigger": "Implementation removes groups with zero accumulated totals or treats SKU matching as case-insensitive.",
      "likely_stage": "implementer",
      "prevention": "Check a cancelling group remains in output and differently cased keys remain separate."
    },
    {
      "id": "F4",
      "trigger": "Implementation edits row dictionaries while trimming SKU values or returns extra/missing result keys.",
      "likely_stage": "implementer",
      "prevention": "Compare inputs before and after the call and assert each returned dictionary has exactly sku and delta."
    },
    {
      "id": "F5",
      "trigger": "Public smoke passes and is mistaken for full acceptance coverage.",
      "likely_stage": "planner",
      "prevention": "Retain acceptance_contract_in_memory as a required planned check alongside public_smoke."
    }
  ],
  "handoff": {
    "next_agent": "planner",
    "allowed_next_inputs": [
      "AGENTS.md",
      "researcher/AGENTS.md",
      "planner/AGENTS.md",
      "share/aggregation/researcher/task.md",
      "share/aggregation/planner/plan.md",
      "solution.py",
      "smoke.py",
      "examples.json when present",
      "policy.txt when present"
    ],
    "notes": "Create an implementation brief that keeps all task constraints and acceptance criteria, defines ordered steps and invariants, names public_smoke and acceptance_contract_in_memory as checks, and includes cleanup and escalation details. Do not edit source code during planning."
  }
}
