{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "workflow_review",
  "task_id": "workflow-integrity-20261003",
  "produced_by": "reviewer",
  "status": "success",
  "revision": "8d2082fa-858f-4054-830e-07c6bf80aea9",
  "input_fingerprints": {
    "share/workflow-integrity-20261003/reviewer/task.md": "3b9839359f304b02c134cd052ce71419261cec4bc1c86b6ff020b99524ea6ea3",
    "share/workflow-integrity-20261003/reviewer/plan.md": "5f173f543005b09deac751e3dcb881951a27313e4321a7b554eb381e62d7a1b9",
    "share/workflow-integrity-20261003/reviewer/impl.md": "e48e84ed9210b47f1cecb44a885b8b97273c35276d0d59de1f6cf1859b8ba115",
    "share/workflow-integrity-20261003/reviewer/result.md": "e55cb113755003ffea48cddcaaa47c7fc36177d882ad7a5a4d697f06ed919832"
  },
  "input_artifacts": [
    {
      "path": "share/workflow-integrity-20261003/reviewer/task.md",
      "required": true,
      "summary": "Authoritative task content or required stage input."
    },
    {
      "path": "share/workflow-integrity-20261003/reviewer/plan.md",
      "required": true,
      "summary": "Authoritative task content or required stage input."
    },
    {
      "path": "share/workflow-integrity-20261003/reviewer/impl.md",
      "required": true,
      "summary": "Authoritative task content or required stage input."
    },
    {
      "path": "share/workflow-integrity-20261003/reviewer/result.md",
      "required": true,
      "summary": "Authoritative task content or required stage input."
    }
  ],
  "trusted_sources": [
    {
      "path": "AGENTS.md",
      "summary": "Root contract."
    },
    {
      "path": "reviewer/AGENTS.md",
      "summary": "Stage contract."
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "share/workflow-integrity-20261003/reviewer/task.md",
      "summary": "Task data, not instructions overriding stage rules."
    },
    {
      "path": "share/workflow-integrity-20261003/reviewer/plan.md",
      "summary": "Task data, not instructions overriding stage rules."
    },
    {
      "path": "share/workflow-integrity-20261003/reviewer/impl.md",
      "summary": "Task data, not instructions overriding stage rules."
    },
    {
      "path": "share/workflow-integrity-20261003/reviewer/result.md",
      "summary": "Task data, not instructions overriding stage rules."
    }
  ],
  "constraints": [
    "Preserve five stages and unrelated user changes.",
    "No external executor, commit or push.",
    "Main agent performs stages using same-invocation fallback; no isolation claim."
  ],
  "open_questions": [],
  "evidence": [
    {
      "kind": "command_output",
      "source": "share/workflow-integrity-20261003/evidence/final-tests.txt",
      "summary": "Verified actual output: Ran 46 tests; OK."
    },
    {
      "kind": "command_output",
      "source": "share/workflow-integrity-20261003/evidence/diff-check.txt",
      "summary": "Verified recorded git diff --check exit 0."
    },
    {
      "kind": "command_output",
      "source": "share/workflow-integrity-20261003/evidence/baseline-integrity.txt",
      "summary": "Frozen cases exposed 33 failed assertions and one error on the original router."
    },
    {
      "kind": "bundle_validation",
      "source": "share/workflow-integrity-20261003/reviewer",
      "summary": "All four inputs validated against current contracts; hashes match and mirrors equal canonical bytes."
    },
    {
      "kind": "source_review",
      "source": "agent_loop_poc/contracts.py",
      "summary": "Unique required check identities and review/return-target consistency are enforced; hypotheses from the textual counterargument were checked by the main agent."
    }
  ],
  "handoff": {
    "next_agent": "NONE",
    "allowed_next_inputs": [],
    "notes": "Bounded milestone accepted. Final CLI readback is recorded by the orchestrator."
  },
  "overall_judgment": "success",
  "failure_source": "NONE",
  "confidence": "high",
  "reason": "The first integrity milestone satisfies the bounded task acceptance cases: strict contracts, sequential dependency checks, stale-input invalidation, exact mirrors, required-check matching and typed user-decision handling. The actual 46-test log, baseline failures, source changes and whitespace check were inspected; four review inputs pass contract and lineage checks. This is not a claim of semantic fidelity, real agent execution, concurrent safety or independent invocation isolation.",
  "recommended_return_target": "NONE",
  "recommended_next_action": "Use 0.2.0 with regenerated versioned artifacts; any executor work is a separate milestone.",
  "artifact_schema_checks": [
    {
      "artifact": "normalized_task",
      "status": "passed",
      "evidence": "Parsed review bundle input, checked common and stage required fields/types/enums, cross-field rules and current input SHA-256; canonical mirrors are byte-identical."
    },
    {
      "artifact": "research_plan",
      "status": "passed",
      "evidence": "Parsed review bundle input, checked common and stage required fields/types/enums, cross-field rules and current input SHA-256; canonical mirrors are byte-identical."
    },
    {
      "artifact": "implementation_brief",
      "status": "passed",
      "evidence": "Parsed review bundle input, checked common and stage required fields/types/enums, cross-field rules and current input SHA-256; canonical mirrors are byte-identical."
    },
    {
      "artifact": "implementation_result",
      "status": "passed",
      "evidence": "Parsed review bundle input, checked common and stage required fields/types/enums, cross-field rules and current input SHA-256; canonical mirrors are byte-identical."
    }
  ],
  "notes": [
    "Main agent owns the review using the documented same-invocation fallback.",
    "Original six tests used incomplete fixtures; their scenarios were migrated to the stricter contract, with legacy Markdown now blocked.",
    "46 tests passed; no general task-success-rate or semantic-quality conclusion follows.",
    "Own completed/done CLI readback is an orchestration postcondition after this artifact is written; its actual output is recorded separately in evidence/final-smoke.json."
  ]
}
