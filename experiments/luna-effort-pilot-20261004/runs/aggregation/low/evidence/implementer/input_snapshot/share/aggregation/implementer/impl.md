{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "implementation_brief",
  "task_id": "aggregation",
  "produced_by": "planner",
  "status": "ready",
  "revision": "4aae321a-bad5-42b1-9857-9a7d0d83bde5",
  "input_fingerprints": {
    "share/aggregation/planner/plan.md": "bc69c07cead183539e34182e1a6efd036f62e0acfee6eb767ad2cbefdb5b0f8e"
  },
  "input_artifacts": [
    {"path": "share/aggregation/planner/plan.md", "required": true, "summary": "Research plan defining aggregate(rows) requirements, authorized scope, risks, required public smoke check, and cleanup."},
    {"path": "solution.py", "required": false, "summary": "Authorized read-only context; current function overwrites by raw SKU then sorts keys."},
    {"path": "smoke.py", "required": false, "summary": "Authorized read-only context; public smoke asserts empty input and a single row."}
  ],
  "trusted_sources": [
    {"path": "AGENTS.md", "summary": "Root workflow contract for artifact integrity, stage boundaries, fingerprints, and truthful evidence."},
    {"path": "planner/AGENTS.md", "summary": "Planner role, implementation_brief schema, and one-artifact write scope."},
    {"path": "share/aggregation/planner/plan.md", "summary": "Authoritative upstream research plan and preserved task scope."}
  ],
  "untrusted_inputs_seen": [
    {"path": "share/aggregation/planner/plan.md", "summary": "Treated as request data subject to governing artifact and stage rules."},
    {"path": "solution.py", "summary": "Inspected as authorized source context; not authoritative over acceptance criteria."},
    {"path": "smoke.py", "summary": "Inspected as authorized fixture context; its limited assertions do not replace acceptance criteria."}
  ],
  "constraints": [
    "Edit only solution.py; preserve aggregate(rows)'s public signature.",
    "Use Python 3 standard library only; no dependencies, network, Git actions, or access outside the isolated project.",
    "Keep smoke.py and any fixtures read-only; do not add test files.",
    "Do not inspect sibling runs or evaluation materials.",
    "Do not mutate the input rows list or dictionaries and do not add validation for malformed inputs or unsupported types.",
    "Use python3 -B for the required public smoke check; report only checks actually run."
  ],
  "open_questions": [],
  "evidence": [
    {"kind": "task_requirements", "source": "share/aggregation/planner/plan.md", "summary": "Requires trimming SKU whitespace, ignoring empty-after-trim keys, case-sensitive grouping, summing every integer delta including negative and zero, retaining zero-sum groups, first-valid-occurrence order, exact output keys, immutability, and [] on empty input."},
    {"kind": "source_context", "source": "solution.py", "summary": "Current code uses raw SKU keys, keeps only latest deltas, and sorts output, conflicting with grouping, summation, normalization, and order requirements."},
    {"kind": "fixture_context", "source": "smoke.py", "summary": "Public smoke checks empty input and a single row only; broader criteria require careful implementation beyond those two assertions."}
  ],
  "summary": "Update aggregate(rows) to group on trimmed nonempty case-sensitive SKU values, sum all deltas, and return fresh result dictionaries in first-valid-occurrence order while leaving inputs untouched.",
  "inputs_used": ["share/aggregation/planner/plan.md", "solution.py", "smoke.py"],
  "files_likely_to_change": ["solution.py"],
  "ordered_steps": [
    {"step": 1, "action": "Inspect the existing aggregate(rows) implementation and preserve its public signature.", "rationale": "The only authorized implementation target is solution.py and callers may rely on the existing entry point.", "expected_evidence": "A focused diff showing changes confined to aggregate(rows) in solution.py."},
    {"step": 2, "action": "Build local insertion-ordered aggregation state keyed by each row's trimmed SKU; skip only keys that become empty and add every associated delta.", "rationale": "This implements normalized grouping, first-valid-occurrence ordering, and complete summation without changing caller-owned data.", "expected_evidence": "Implementation logic uses trimmed case-sensitive keys, accumulates deltas, and does not write to rows or row dictionaries."},
    {"step": 3, "action": "Construct fresh output dictionaries with exactly sku and delta for every group, including groups whose total is zero.", "rationale": "The output contract requires stable first-seen order and retention of zero totals.", "expected_evidence": "Returned list reflects first accepted occurrence order and includes all accepted groups."},
    {"step": 4, "action": "Run the required public smoke check with python3 -B smoke.py and record its actual outcome.", "rationale": "This is the explicitly required validation and avoids bytecode cache creation.", "expected_evidence": "Observed command output and exit status recorded in the implementation result."},
    {"step": 5, "action": "Remove task-created cache or scratch artifacts, if any, and report cleanup evidence.", "rationale": "The task requires temporary artifacts to be cleaned and no persistent scratch files left.", "expected_evidence": "Cleanup status is stated based on observed filesystem state."}
  ],
  "invariants": [
    "Only solution.py may be modified, and aggregate(rows) keeps its existing signature.",
    "SKU grouping uses trimmed, nonempty, case-sensitive strings.",
    "Every accepted row's integer delta contributes to exactly one group's sum, including negative and zero values.",
    "Every accepted group is returned even when its final sum is zero.",
    "Result order is the order in which normalized SKU groups first appear.",
    "Input list and dictionaries remain unchanged; output dictionaries are fresh and contain exactly sku and delta.",
    "Do not add malformed-input validation or change fixtures."
  ],
  "validation_plan": [
    {"check": "public_smoke", "command_or_method": "Run `python3 -B smoke.py` from the isolated project root.", "expected_result": "Command exits successfully and prints `public_smoke: 2 assertions passed`.", "required": true}
  ],
  "cleanup_plan": [
    "Use python3 -B for public_smoke to avoid creating __pycache__.",
    "Remove any task-created __pycache__ or scratch files before handoff; leave no persistent scratch artifacts.",
    "Record observed cleanup status and any intentional leftover with its reason."
  ],
  "escalation_conditions": [
    {"condition": "Implementing the stated behavior appears to require editing a file other than solution.py or changing the public signature.", "return_target": "researcher", "reason": "That would exceed the authorized implementation scope."},
    {"condition": "Acceptance criteria conflict or a required behavior cannot be implemented without changing task scope or assumptions.", "return_target": "researcher", "reason": "The implementer must stop instead of silently relaxing requirements."},
    {"condition": "The required public_smoke command fails for an environmental or fixture reason that cannot be resolved within scope.", "return_target": "planner", "reason": "Preserve the actual failure evidence and route upstream if the blocker is outside implementation scope."}
  ],
  "rollback_hints": [
    "Keep changes limited to solution.py so the implementation can be reverted by restoring that file's prior contents if needed.",
    "Do not revert or alter unrelated files."
  ],
  "expected_output": {
    "result_artifact_path": "share/aggregation/reviewer/result.md",
    "implementation_summary_requirements": ["Describe the change made in solution.py.", "Record public_smoke command, observed output, and exit status.", "State whether inputs were preserved by implementation inspection or observed checks without overstating.", "Report cleanup status and any intentional leftovers."]
  },
  "handoff": {
    "next_agent": "implementer",
    "allowed_next_inputs": ["AGENTS.md", "implementer/AGENTS.md", "share/aggregation/implementer/impl.md", "solution.py", "smoke.py", "examples.json when present and authorized", "policy.txt when present and authorized"],
    "notes": "Implement only the bounded aggregate(rows) repair in solution.py, run the required public_smoke check, and report actual execution and cleanup evidence."
  }
}
