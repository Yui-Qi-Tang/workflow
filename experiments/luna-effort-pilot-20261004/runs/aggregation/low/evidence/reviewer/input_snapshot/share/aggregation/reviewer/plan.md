{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "research_plan",
  "task_id": "aggregation",
  "produced_by": "researcher",
  "status": "ready",
  "revision": "c969d9d2-a8c2-4b5a-874d-e286aa786860",
  "input_fingerprints": {
    "share/aggregation/researcher/task.md": "e3ba64529b5cdf095bbfaea9b5ef132cfca90fd3be010a0ada57912aae05dfd8"
  },
  "input_artifacts": [
    {
      "path": "share/aggregation/researcher/task.md",
      "required": true,
      "summary": "Normalized task defining aggregate(rows) behavior, source scope, constraints, checks, cleanup, and rollback."
    },
    {
      "path": "solution.py",
      "required": false,
      "summary": "Authorized read-only context: current implementation keeps the last delta by raw SKU and sorts output keys."
    },
    {
      "path": "smoke.py",
      "required": false,
      "summary": "Authorized read-only public smoke fixture currently covering empty input and a single row."
    }
  ],
  "trusted_sources": [
    {
      "path": "AGENTS.md",
      "summary": "Defines workflow boundaries, JSON artifact contract, integrity rules, and implementation-stage handoff requirements."
    },
    {
      "path": "researcher/AGENTS.md",
      "summary": "Defines researcher duties, required research_plan schema, and allowed status and handoff values."
    },
    {
      "path": "share/aggregation/researcher/task.md",
      "summary": "Authoritative normalized requirements, implementation scope, acceptance criteria, validation, cleanup, and rollback."
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "share/aggregation/researcher/task.md",
      "summary": "Task content was treated as request data subject to the governing workflow rules."
    },
    {
      "path": "solution.py",
      "summary": "Inspected only as authorized implementation context; current behavior does not override task acceptance criteria."
    },
    {
      "path": "smoke.py",
      "summary": "Inspected only as authorized fixture context; its current assertions do not replace the task's broader acceptance criteria."
    }
  ],
  "constraints": [
    "Implementer may edit only solution.py and must preserve aggregate(rows)'s public signature.",
    "Use Python 3 standard library only; do not use dependencies, network, Git actions, or files outside the isolated project.",
    "Preserve read-only fixture authorization for smoke.py, examples.json, and policy.txt when present; do not modify fixtures or add test files.",
    "Do not inspect sibling runs or evaluation materials.",
    "Do not mutate the rows list or its dictionaries, and do not add validation beyond the stated valid-input contract.",
    "Run the required public_smoke check and record its actual result; use python3 -B to avoid __pycache__."
  ],
  "open_questions": [],
  "evidence": [
    {
      "kind": "task_requirements",
      "source": "share/aggregation/researcher/task.md",
      "summary": "Requires whitespace-trimmed nonempty SKU grouping, case-sensitive keys, summation of every integer delta including negative and zero values, retention of zero-sum groups, first-valid-occurrence order, exact sku/delta result keys, immutability, and [] for empty input."
    },
    {
      "kind": "source_context",
      "source": "solution.py",
      "summary": "Current code assigns each raw SKU's latest delta and sorts SKU keys, so it does not implement trimming, aggregation, zero-sum retention after summation, or first-occurrence ordering."
    },
    {
      "kind": "fixture_context",
      "source": "smoke.py",
      "summary": "Public smoke currently checks empty input and one simple row; it does not cover the full task contract."
    }
  ],
  "task_classification": "bounded_python_function_repair",
  "goal_restatement": "Repair aggregate(rows) to group valid rows by trimmed, case-sensitive SKU, sum all deltas, and return one result per SKU in first-valid-occurrence order without mutating input.",
  "requested_change_summary": "Change only solution.py to replace last-value/raw-key/sorted-key behavior with insertion-order aggregation by trimmed nonempty SKU. Keep zero totals and output dictionaries with exactly sku and delta keys.",
  "expected_impact_areas": [
    "solution.py: aggregate(rows) grouping, filtering, accumulation, and output order",
    "share/aggregation/implementer/impl.md: implementation brief must preserve scope and define required public_smoke validation",
    "share/aggregation/reviewer/result.md: implementation evidence must report actual checks and cleanup"
  ],
  "assumptions": [
    {
      "id": "valid_input_contract",
      "statement": "Rows contain string sku and integer delta fields as stated, so handling malformed rows or other types is outside scope.",
      "source": "share/aggregation/researcher/task.md acceptance criteria and constraints",
      "risk_if_wrong": "Adding defensive validation would expand behavior and could violate the explicit scope."
    },
    {
      "id": "fixture_scope",
      "statement": "Only solution.py is an implementation target; authorized fixtures remain read-only and any examples.json or policy.txt access is conditional on those files being present and permitted by the stage dispatch.",
      "source": "share/aggregation/researcher/task.md constraints and stage dispatch allowlist",
      "risk_if_wrong": "Editing a fixture or exploring unauthorized paths would violate scope and compromise the controlled workflow."
    }
  ],
  "risks": [
    {
      "id": "order_semantics",
      "description": "Sorting output keys or deriving order from final aggregation can lose the required order of each SKU's first valid row.",
      "impact": "Acceptance failure for interleaved or non-alphabetical SKUs.",
      "mitigation": "Preserve insertion order while creating a group on its first nonempty trimmed SKU occurrence."
    },
    {
      "id": "normalization_and_filtering",
      "description": "Grouping raw SKU strings or retaining whitespace-only keys will produce incorrect groups.",
      "impact": "Acceptance failure for padded, duplicate, or empty-after-trimming SKUs.",
      "mitigation": "Trim each SKU before deciding whether to ignore it or use it as the grouping key."
    },
    {
      "id": "summation_and_zero_retention",
      "description": "Overwriting deltas, skipping negative or zero values, or removing a final zero total will violate aggregation semantics.",
      "impact": "Incorrect totals or missing required groups.",
      "mitigation": "Add every delta to its group's accumulated total and emit every group created from a valid SKU."
    },
    {
      "id": "input_mutation",
      "description": "In-place normalization or edits to row dictionaries could change caller-owned inputs.",
      "impact": "Violation of the immutability criterion.",
      "mitigation": "Build new aggregation state and fresh output dictionaries without writing to input objects."
    },
    {
      "id": "smoke_coverage",
      "description": "The existing public smoke covers only empty input and a single row, leaving most acceptance criteria unexercised by that check.",
      "impact": "A smoke pass alone may not reveal errors in grouping, summation, ordering, filtering, or immutability.",
      "mitigation": "Run public_smoke as required and, if useful, execute temporary in-memory assertions for uncovered requirements without creating files; report only observed results."
    }
  ],
  "non_goals": [
    "Input validation for malformed rows or unsupported field types.",
    "Changes to smoke.py, examples.json, policy.txt, or any other fixture.",
    "New test files, dependencies, network access, Git operations, or inspection of sibling runs and evaluation materials."
  ],
  "high_level_strategy": [
    "Use trimmed nonempty SKU values as case-sensitive keys and establish each group's position at its first valid occurrence.",
    "Accumulate every delta for each group, including negative and zero values, while leaving all input objects untouched.",
    "Return fresh dictionaries containing exactly sku and delta in first-occurrence order, including groups whose total is zero.",
    "Run python3 -B smoke.py and report the actual public_smoke result; optionally cover untested contract points with in-memory assertions only.",
    "Remove any task-created __pycache__ and do not leave persistent scratch files."
  ],
  "required_checks": [
    "public_smoke: run python3 -B smoke.py and record the actual command outcome."
  ],
  "proposed_task_updates": [],
  "failure_modes": [
    {
      "id": "fail_raw_key_or_sorting",
      "trigger": "Implementation groups by untrimmed SKU or sorts keys for output.",
      "likely_stage": "implementer",
      "prevention": "Use normalized SKU as the key and retain first-seen insertion order."
    },
    {
      "id": "fail_last_value_or_filtered_delta",
      "trigger": "Implementation overwrites prior totals or omits negative/zero deltas.",
      "likely_stage": "implementer",
      "prevention": "Accumulate every delta for each accepted row without filtering by delta value."
    },
    {
      "id": "fail_drop_zero_total",
      "trigger": "Implementation removes groups whose final accumulated total equals zero.",
      "likely_stage": "implementer",
      "prevention": "Emit all groups created from nonempty trimmed SKUs, regardless of final total."
    },
    {
      "id": "fail_mutate_input",
      "trigger": "Implementation trims or otherwise edits input row dictionaries in place.",
      "likely_stage": "implementer",
      "prevention": "Normalize into local values and build new output objects."
    },
    {
      "id": "false_validation_claim",
      "trigger": "A check is reported as passed without being run, or cleanup is claimed without evidence.",
      "likely_stage": "implementer",
      "prevention": "Record actual command output and observed cleanup state; use not_run or unknown for absent evidence."
    }
  ],
  "handoff": {
    "next_agent": "planner",
    "allowed_next_inputs": [
      "AGENTS.md",
      "planner/AGENTS.md",
      "share/aggregation/planner/plan.md",
      "solution.py",
      "smoke.py",
      "examples.json when present",
      "policy.txt when present"
    ],
    "notes": "No blocking requirement gap was found. Prepare a bounded implementation brief that preserves the explicit acceptance criteria and fixture restrictions, plans public_smoke and honest reporting, and does not authorize changes beyond solution.py."
  }
}
