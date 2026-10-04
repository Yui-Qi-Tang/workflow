{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "workflow_review",
  "task_id": "commit-workflow-skill-20261004",
  "produced_by": "reviewer",
  "status": "success",
  "revision": "5b30cb91-78a5-4d22-b2e5-b02ccb7b1840",
  "input_fingerprints": {
    "share/commit-workflow-skill-20261004/reviewer/task.md": "6e2a7df9f9ac9a5c4a2bf05e6f6b5bc64dde47c9467331243c061ca7b3c77a9e",
    "share/commit-workflow-skill-20261004/reviewer/plan.md": "f3e36dac339c04ffddf61e1af53a99c87dcd6cdc350686b5e284353393482741",
    "share/commit-workflow-skill-20261004/reviewer/impl.md": "a8d250f42f6acdcad1ac0bc68f233943e07382cbef605b2cc06236f0f570f216",
    "share/commit-workflow-skill-20261004/reviewer/result.md": "60479b429947c3b20d466f8a929c33e13bb6ffbac895bb539289274808999a1c"
  },
  "input_artifacts": [
    {
      "path": "share/commit-workflow-skill-20261004/reviewer/task.md",
      "required": true,
      "summary": "Current self-contained commit review input."
    },
    {
      "path": "share/commit-workflow-skill-20261004/reviewer/plan.md",
      "required": true,
      "summary": "Current self-contained commit review input."
    },
    {
      "path": "share/commit-workflow-skill-20261004/reviewer/impl.md",
      "required": true,
      "summary": "Current self-contained commit review input."
    },
    {
      "path": "share/commit-workflow-skill-20261004/reviewer/result.md",
      "required": true,
      "summary": "Current self-contained commit review input."
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
      "path": "share/commit-workflow-skill-20261004/reviewer/task.md"
    },
    {
      "path": "share/commit-workflow-skill-20261004/reviewer/plan.md"
    },
    {
      "path": "share/commit-workflow-skill-20261004/reviewer/impl.md"
    },
    {
      "path": "share/commit-workflow-skill-20261004/reviewer/result.md"
    },
    {
      "path": "share/commit-workflow-skill-20261004/evidence/"
    }
  ],
  "constraints": [
    "Explicit allowlist only; preserve all 556 pre-existing selected file bytes.",
    "Local commit on main after completed review and exact index verification; no push, amend, product edits or model reruns.",
    "Main owns five stages in same_invocation fallback; no independently isolated review."
  ],
  "open_questions": [],
  "evidence": [
    {
      "kind": "execution_mode",
      "source": "Current review bundle",
      "summary": "same_invocation by main; no independent isolation claim."
    },
    {
      "kind": "commit_scope",
      "source": "share/commit-workflow-skill-20261004/evidence/index-review.json",
      "summary": "Initial staged set contains only allowed files and matches working bytes. All 556 existing selected files preserved. Final staging/recheck remains orchestrator publication gate."
    },
    {
      "kind": "raw_evidence",
      "source": "share/commit-workflow-skill-20261004/evidence/nonraw-diff-check.json",
      "summary": "Six raw transcript exports contain intentional EOF blank lines. Full whitespace check exit 2 disclosed; every other staged file passes."
    }
  ],
  "handoff": {
    "next_agent": "NONE",
    "allowed_next_inputs": [],
    "notes": "Prepared bundle reviewed; main now stages final records, verifies exact index bytes and performs already-authorized local Git commit."
  },
  "overall_judgment": "success",
  "failure_source": "NONE",
  "confidence": "high",
  "reason": "Commit preparation preserves requested scope and frozen/raw evidence, validates all three prior completed workflows and all four current review inputs, and discloses the raw-only whitespace findings. The bundle is ready for final index verification and local commit. This does not claim publication already happened.",
  "recommended_return_target": "NONE",
  "recommended_next_action": "Stage final allowlist, recheck exact staged paths/blobs and baseline, commit locally on main, then verify commit parent/content and clean worktree. Do not push.",
  "artifact_schema_checks": [
    {
      "artifact": "normalized_task",
      "status": "passed",
      "evidence": "share/commit-workflow-skill-20261004/reviewer/task.md parsed and passed current schema/lineage validation; current bytes match captured SHA-256."
    },
    {
      "artifact": "research_plan",
      "status": "passed",
      "evidence": "share/commit-workflow-skill-20261004/reviewer/plan.md parsed and passed current schema/lineage validation; current bytes match captured SHA-256."
    },
    {
      "artifact": "implementation_brief",
      "status": "passed",
      "evidence": "share/commit-workflow-skill-20261004/reviewer/impl.md parsed and passed current schema/lineage validation; current bytes match captured SHA-256."
    },
    {
      "artifact": "implementation_result",
      "status": "passed",
      "evidence": "share/commit-workflow-skill-20261004/reviewer/result.md parsed and passed current schema/lineage validation; current bytes match captured SHA-256."
    }
  ],
  "notes": [
    "Final commit hash must be reported after Git succeeds, not embedded in its own tree.",
    "No edits to product, skill or experiment outcomes during commit preparation.",
    "No new model invocation or unit-test run needed for this Git-only operation; prior verified results retained."
  ]
}
