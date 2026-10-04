{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "workflow_review",
  "task_id": "case",
  "produced_by": "reviewer",
  "status": "success",
  "revision": "98e3a876-b987-4add-964b-93f4a2f19b6a",
  "input_fingerprints": {
    "share/case/reviewer/task.md": "949064042bb7cf858769dbb6930d54d054478d22f4426cff7dace20e1ec0298a",
    "share/case/reviewer/plan.md": "ac718c66a211088dd6835253483535ce908f8e4847289f61de78a1b30d00757d",
    "share/case/reviewer/impl.md": "ed7f0afec078ed5b7707e935d91006a18470a1c56e9a3ef3ecd69c2a4e44b315",
    "share/case/reviewer/result.md": "6c3e979913d73f8817f88caa688853a281541c453379231773376edabc1d7406"
  },
  "input_artifacts": [
    {
      "path": "share/case/reviewer/task.md",
      "required": true,
      "summary": "normalized_task current review input"
    },
    {
      "path": "share/case/reviewer/plan.md",
      "required": true,
      "summary": "research_plan current review input"
    },
    {
      "path": "share/case/reviewer/impl.md",
      "required": true,
      "summary": "implementation_brief current review input"
    },
    {
      "path": "share/case/reviewer/result.md",
      "required": true,
      "summary": "implementation_result current review input"
    }
  ],
  "trusted_sources": [
    {
      "path": "AGENTS.md"
    },
    {
      "path": "reviewer/AGENTS.md"
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "share/case/reviewer/task.md"
    },
    {
      "path": "share/case/reviewer/plan.md"
    },
    {
      "path": "share/case/reviewer/impl.md"
    },
    {
      "path": "share/case/reviewer/result.md"
    },
    {
      "path": "output/report.json"
    },
    {
      "path": "records.json"
    },
    {
      "path": "evidence/report_contents.json"
    },
    {
      "path": "evidence/report_shape.json"
    },
    {
      "source": "Controller CLI validation outputs for the four input producers"
    }
  ],
  "constraints": [
    "Immutable: records.json, public_check.py, tasker/case.md, role rules, README, controller, supplied guidance and audit logs.",
    "Write only output/report.json when routing permits, required share/case stage outputs and review mirrors, and evidence/.",
    "For each id select greatest revision before retaining only state=active; canceled or pending latest versions exclude the id regardless of earlier active versions.",
    "Use python3 -B agent_loop_poc/loop.py for every controller operation; no imports of its core.",
    "Use same_invocation for all five roles; no nested agents, external actions, installs or Git.",
    "Each producer owns its output; block without report or downstream production if an unresolved decision exists."
  ],
  "open_questions": [],
  "evidence": [
    {
      "kind": "execution_mode",
      "source": "trial authorization and review bundle",
      "summary": "same_invocation fallback retains context; this review is not independently isolated and does not establish skill efficacy."
    },
    {
      "kind": "schema_validation",
      "source": "python3 -B agent_loop_poc/loop.py validate case tasker|researcher|planner|implementer (four separate CLI commands)",
      "summary": "Each command exited 0 with status validated and current saved-byte digest. Review input hashes match those canonical digest values."
    },
    {
      "kind": "report_validation",
      "source": "evidence/report_contents.json and evidence/report_shape.json",
      "summary": "Public checker actually exited 0 and exact shape passed. Reviewer verified current report digest against saved check evidence, and independently recalculated via sorting revisions: a=12, c=5, d=-3, f=4, sum 18."
    },
    {
      "kind": "lineage",
      "source": "Reviewer metadata and review bundle",
      "summary": "All four reviewer inputs still match freshly captured fingerprints; task/plan/impl mirrors were created before reviewer input capture and were byte-identical."
    }
  ],
  "handoff": {
    "next_agent": "NONE",
    "allowed_next_inputs": [],
    "notes": "Workflow review succeeds for this local fixture; final controller routing still must be inspected after saved-file validation."
  },
  "overall_judgment": "success",
  "failure_source": "NONE",
  "confidence": "high",
  "reason": "The normalized task preserves current latest-revision semantics and cleanup/rollback constraints; research anticipates canceled-latest and signed-amount risks; plan operationalizes both required checks; actual report is total 18 with sorted ids a,c,d,f. Saved report check evidence, schema validation, lineage, mirrors and cleanup reporting support bounded task success.",
  "recommended_return_target": "NONE",
  "recommended_next_action": "Retain authorized outputs, evidence and automatic audit; inspect final routing after validating this saved review.",
  "artifact_schema_checks": [
    {
      "artifact": "normalized_task",
      "status": "passed",
      "evidence": "Observed CLI validate for corresponding producer exited 0 and returned current SHA-256 949064042bb7cf858769dbb6930d54d054478d22f4426cff7dace20e1ec0298a; review file parses with expected artifact_type and matches validated bytes."
    },
    {
      "artifact": "research_plan",
      "status": "passed",
      "evidence": "Observed CLI validate for corresponding producer exited 0 and returned current SHA-256 ac718c66a211088dd6835253483535ce908f8e4847289f61de78a1b30d00757d; review file parses with expected artifact_type and matches validated bytes."
    },
    {
      "artifact": "implementation_brief",
      "status": "passed",
      "evidence": "Observed CLI validate for corresponding producer exited 0 and returned current SHA-256 ed7f0afec078ed5b7707e935d91006a18470a1c56e9a3ef3ecd69c2a4e44b315; review file parses with expected artifact_type and matches validated bytes."
    },
    {
      "artifact": "implementation_result",
      "status": "passed",
      "evidence": "Observed CLI validate for corresponding producer exited 0 and returned current SHA-256 6c3e979913d73f8817f88caa688853a281541c453379231773376edabc1d7406; review file parses with expected artifact_type and matches validated bytes."
    }
  ],
  "notes": [
    "All checks refer to current task inputs and generated artifacts. No missing owner decision or blocker was found.",
    "Report semantics checked against current records, including canceled latest b and pending e exclusions and negative d amount.",
    "No scratch files were created; report, evidence, workflow artifacts and automatic audit are intentionally retained.",
    "Controller completion certifies structural and declared-result checks; this single trial does not establish general skill efficacy."
  ]
}
