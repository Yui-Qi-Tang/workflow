{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "workflow_review",
  "task_id": "case",
  "produced_by": "reviewer",
  "status": "success",
  "revision": "de1a95a1-eeab-4419-ad12-6e6aebca4f53",
  "input_fingerprints": {
    "share/case/reviewer/task.md": "c3718f6962d0f74a5039c3f668462dd732790fa94d0a31cf41e6fed17f0fe883",
    "share/case/reviewer/plan.md": "8715693b3f7be88d54df68559a9e8ff8e603b7b3a7201a7bc5c754896a33afde",
    "share/case/reviewer/impl.md": "36bf22f1476ee95edfa7a2b24041ace99d67d9c6f166556f354dbc643778a99f",
    "share/case/reviewer/result.md": "eba17d5ad582fe38284673075cd3b494cc552702634a9aa685d8e456a3ceca78"
  },
  "input_artifacts": [
    {
      "path": "share/case/reviewer/task.md",
      "required": true,
      "summary": "Current normalized_task review input."
    },
    {
      "path": "share/case/reviewer/plan.md",
      "required": true,
      "summary": "Current research_plan review input."
    },
    {
      "path": "share/case/reviewer/impl.md",
      "required": true,
      "summary": "Current implementation_brief review input."
    },
    {
      "path": "share/case/reviewer/result.md",
      "required": true,
      "summary": "Current implementation_result review input."
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
      "path": "evidence/report_contents.json"
    },
    {
      "path": "evidence/stage_validations.json"
    }
  ],
  "constraints": [
    "Select greatest revision for each id before filtering latest state=active. Lower revisions and canceled or pending latest records contribute nothing.",
    "Inputs have valid ids, revisions, states and integer amounts.",
    "Immutable: records.json, public_check.py, tasker/case.md, rules, README, controller, supplied guidance and audit.",
    "Write only output/report.json, owned stage artifacts, review mirrors and evidence/.",
    "Use python3 -B and controller CLI recorder for all controller operations. No nested agents, Git, network, installs or external actions.",
    "same_invocation fallback retains context and is not independently isolated execution or review.",
    "Regenerate stale stage and descendants from current inputs; do not merely update old hashes."
  ],
  "open_questions": [],
  "evidence": [
    {
      "kind": "execution_mode",
      "source": "Review bundle and trial authorization",
      "summary": "same_invocation fallback retains context; this review is not independently isolated."
    },
    {
      "kind": "schema_and_lineage",
      "source": "evidence/stage_validations.json",
      "summary": "All four input producers saved-file validations exited 0 with exact digests; mirrored task, plan and impl bytes match canonical outputs."
    },
    {
      "kind": "report_validation",
      "source": "evidence/report_contents.json and output/report.json",
      "summary": "Required public check exited 0; exact schema and signed total reconciliation passed. Latest active ids a,c,d,f sum 12+5-3+4=18."
    },
    {
      "kind": "semantic_review",
      "source": "Review bundle",
      "summary": "Task, plan, brief and execution preserve maximum-revision-before-active rule, immutable boundaries, required checks, cleanup and rollback."
    }
  ],
  "handoff": {
    "next_agent": "NONE",
    "allowed_next_inputs": [],
    "notes": "Current bounded local task completed; final reviewer saved-file validation and route inspection remain orchestrator operations."
  },
  "overall_judgment": "success",
  "failure_source": "NONE",
  "confidence": "high",
  "reason": "The current chain was reproduced after input change with fresh UUIDs and fingerprints. Its plan preserves task semantics and the observed generated report passes required checks. No unresolved owner decision or execution blocker is recorded.",
  "recommended_return_target": "NONE",
  "recommended_next_action": "Retain generated report, current stage records, evidence and automatic audit; report bounded completion.",
  "artifact_schema_checks": [
    {
      "artifact": "normalized_task",
      "status": "passed",
      "evidence": "Expected JSON artifact type inspected in share/case/reviewer/task.md; producer saved-file validate exited 0 with SHA-256 c3718f6962d0f74a5039c3f668462dd732790fa94d0a31cf41e6fed17f0fe883, as recorded in evidence/stage_validations.json."
    },
    {
      "artifact": "research_plan",
      "status": "passed",
      "evidence": "Expected JSON artifact type inspected in share/case/reviewer/plan.md; producer saved-file validate exited 0 with SHA-256 8715693b3f7be88d54df68559a9e8ff8e603b7b3a7201a7bc5c754896a33afde, as recorded in evidence/stage_validations.json."
    },
    {
      "artifact": "implementation_brief",
      "status": "passed",
      "evidence": "Expected JSON artifact type inspected in share/case/reviewer/impl.md; producer saved-file validate exited 0 with SHA-256 36bf22f1476ee95edfa7a2b24041ace99d67d9c6f166556f354dbc643778a99f, as recorded in evidence/stage_validations.json."
    },
    {
      "artifact": "implementation_result",
      "status": "passed",
      "evidence": "Expected JSON artifact type inspected in share/case/reviewer/result.md; producer saved-file validate exited 0 with SHA-256 eba17d5ad582fe38284673075cd3b494cc552702634a9aa685d8e456a3ceca78, as recorded in evidence/stage_validations.json."
    }
  ],
  "notes": [
    "No task-created scratch files need removal; required outputs retained.",
    "Controller completion establishes structural and declared-result checks; this single trial does not establish general skill efficacy.",
    "Prior synthetic historical evidence did not authorize completion."
  ]
}
