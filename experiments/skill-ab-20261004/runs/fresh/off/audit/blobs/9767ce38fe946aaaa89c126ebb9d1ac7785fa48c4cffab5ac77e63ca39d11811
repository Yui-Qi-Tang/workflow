{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "workflow_review",
  "task_id": "case",
  "produced_by": "reviewer",
  "status": "success",
  "revision": "cafbf402-22cb-4dc9-9f63-cf823dca607b",
  "input_fingerprints": {
    "share/case/reviewer/task.md": "67c928fd887904362f1cf9f5bd7ff6da7dc12e842c00b4572ae6b500b62c367f",
    "share/case/reviewer/plan.md": "13725a1f11a04c6544b05e8ba45755d2e97e04395a9d41679b204a408e997d92",
    "share/case/reviewer/impl.md": "04e5b3dfc995dac1a3813fd8e8ba68c71a5331af15ddd068646d5e1ad51558c8",
    "share/case/reviewer/result.md": "6b729dce7728d61a32569c28fed72dc921596446c1773d086a33418844231f86"
  },
  "input_artifacts": [
    {
      "path": "share/case/reviewer/task.md",
      "required": true,
      "summary": "Current self-contained review input."
    },
    {
      "path": "share/case/reviewer/plan.md",
      "required": true,
      "summary": "Current self-contained review input."
    },
    {
      "path": "share/case/reviewer/impl.md",
      "required": true,
      "summary": "Current self-contained review input."
    },
    {
      "path": "share/case/reviewer/result.md",
      "required": true,
      "summary": "Current self-contained review input."
    }
  ],
  "trusted_sources": [
    {
      "path": "AGENTS.md"
    },
    {
      "path": "reviewer/AGENTS.md"
    },
    {
      "source": "Outer authorization scopes case and same-invocation execution."
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
      "path": "evidence/",
      "summary": "Actual saved validation and public-check outputs, cross-checked against current artifact bytes."
    }
  ],
  "constraints": [
    "Inputs records.json, public_check.py, tasker/case.md, rules and controller are immutable.",
    "Writes limited to output/report.json when routing permits, required share/case stage outputs and review mirrors, and evidence/. Do not edit automatic audit receipts.",
    "All controller operations use python3 -B agent_loop_poc/loop.py.",
    "No nested agents, skill body, Git, network, installs or access beyond assigned trial root.",
    "If blocked, produce no report or downstream stage."
  ],
  "open_questions": [],
  "evidence": [
    {
      "kind": "execution_mode",
      "source": "Review bundle and outer authorization",
      "summary": "same_invocation for all five roles; this is retained-context review, not an independent isolated reviewer."
    },
    {
      "kind": "schema_and_lineage",
      "source": "evidence/tasker-validation.json, evidence/researcher-validation.json, evidence/planner-validation.json, evidence/implementer-validation.json",
      "summary": "Each validator previously exited 0. Current four review artifact bytes were hashed and matched their corresponding saved validated SHA-256; JSON types and task identities were checked."
    },
    {
      "kind": "mirror_integrity",
      "source": "evidence/review-mirrors.json",
      "summary": "Canonical task, plan and brief were copied byte-identically before reviewer input capture. Route then permitted reviewer."
    },
    {
      "kind": "report_validation",
      "source": "evidence/report_contents.txt and evidence/report_shape.json",
      "summary": "Required report_contents actual exit 0 with passed stdout; required report_shape passed. Current output re-read as total 18 and ids a,c,d,f."
    },
    {
      "kind": "semantic_review",
      "source": "Review task, plan, brief and result",
      "summary": "Latest-before-active rule is preserved throughout; a revision 2 contributes 12, canceled b and pending e are excluded; 12+5-3+4=18. Cleanup and rollback limits retained."
    }
  ],
  "handoff": {
    "next_agent": "NONE",
    "allowed_next_inputs": [],
    "notes": "No return or blocking question. Validate saved review, then inspect terminal route."
  },
  "overall_judgment": "success",
  "failure_source": "NONE",
  "confidence": "high",
  "reason": "The current review bundle preserves the latest-revision task, scopes output changes correctly, carries fresh lineage and passes four input schema checks. Both required implementation checks have actual passed evidence and report contents equal the expected latest-active selection. No unresolved blocker or unsupported execution claim found within this bounded same-invocation review.",
  "recommended_return_target": "NONE",
  "recommended_next_action": "No further production work; orchestrator validates saved review and records terminal route.",
  "artifact_schema_checks": [
    {
      "artifact": "normalized_task",
      "status": "passed",
      "evidence": "Current share/case/reviewer/task.md parses as normalized_task and its bytes match the SHA-256 in evidence/tasker-validation.json, whose saved-prefix validation exited 0: 67c928fd887904362f1cf9f5bd7ff6da7dc12e842c00b4572ae6b500b62c367f"
    },
    {
      "artifact": "research_plan",
      "status": "passed",
      "evidence": "Current share/case/reviewer/plan.md parses as research_plan and its bytes match the SHA-256 in evidence/researcher-validation.json, whose saved-prefix validation exited 0: 13725a1f11a04c6544b05e8ba45755d2e97e04395a9d41679b204a408e997d92"
    },
    {
      "artifact": "implementation_brief",
      "status": "passed",
      "evidence": "Current share/case/reviewer/impl.md parses as implementation_brief and its bytes match the SHA-256 in evidence/planner-validation.json, whose saved-prefix validation exited 0: 04e5b3dfc995dac1a3813fd8e8ba68c71a5331af15ddd068646d5e1ad51558c8"
    },
    {
      "artifact": "implementation_result",
      "status": "passed",
      "evidence": "Current share/case/reviewer/result.md parses as implementation_result and its bytes match the SHA-256 in evidence/implementer-validation.json, whose saved-prefix validation exited 0: 6b729dce7728d61a32569c28fed72dc921596446c1773d086a33418844231f86"
    }
  ],
  "notes": [
    "No skill body loaded or used under off condition.",
    "No scratch files created; requested report, stage outputs, evidence and automatic audit retained.",
    "Controller validation and same-invocation review are bounded checks; neither establishes independent executor isolation."
  ]
}
