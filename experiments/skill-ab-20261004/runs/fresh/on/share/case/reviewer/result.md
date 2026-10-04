{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "implementation_result",
  "task_id": "case",
  "produced_by": "implementer",
  "status": "success",
  "revision": "28b98cf7-3745-4050-a649-e3b58aae6a92",
  "input_fingerprints": {
    "share/case/implementer/impl.md": "ed7f0afec078ed5b7707e935d91006a18470a1c56e9a3ef3ecd69c2a4e44b315"
  },
  "input_artifacts": [
    {
      "path": "share/case/implementer/impl.md",
      "required": true,
      "summary": "Approved brief with exact rule, checks, output paths, cleanup and rollback."
    }
  ],
  "trusted_sources": [
    {
      "path": "AGENTS.md"
    },
    {
      "path": "implementer/AGENTS.md"
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "share/case/implementer/impl.md"
    },
    {
      "path": "records.json"
    },
    {
      "path": "public_check.py"
    },
    {
      "path": "evidence/report_contents.json"
    },
    {
      "path": "evidence/report_shape.json"
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
      "source": "trial authorization and implementation brief",
      "summary": "same_invocation fallback; retained context, no independently isolated stage execution or review."
    },
    {
      "kind": "command",
      "source": "evidence/report_contents.json",
      "summary": "python3 -B public_check.py executed, exit_status 0; stdout report_contents: passed; stderr empty."
    },
    {
      "kind": "saved_file_check",
      "source": "evidence/report_shape.json",
      "summary": "Exact keys and JSON types pass; total 18 and ids a,c,d,f. Report SHA-256 a03d9134a1d62fcfa49bc7a8e7469f35837cf73e1facebaf96ac41d1e64989fe."
    }
  ],
  "handoff": {
    "next_agent": "reviewer",
    "allowed_next_inputs": [
      "share/case/reviewer/task.md",
      "share/case/reviewer/plan.md",
      "share/case/reviewer/impl.md",
      "share/case/reviewer/result.md",
      "output/report.json",
      "records.json",
      "public_check.py",
      "evidence/report_contents.json",
      "evidence/report_shape.json",
      "AGENTS.md",
      "reviewer/AGENTS.md",
      "agent_loop_poc/README.md"
    ],
    "notes": "Orchestrator must create byte-identical task/plan/impl mirrors before reviewer input capture and recheck route. Review requires actual four input schema checks."
  },
  "implementation_summary": "Read current records.json, reduced each id to its greatest revision before active filtering, summed signed amounts and sorted ids. Wrote output/report.json with total 18 and ids a,c,d,f. Actual report_contents and report_shape passed. No scratch files were created.",
  "changed_files": [
    {
      "path": "output/report.json",
      "change_type": "created",
      "summary": "Latest-revision active report with exact two-key JSON object."
    },
    {
      "path": "evidence/report_contents.json",
      "change_type": "created",
      "summary": "Observed public checker command, exit status, stdout/stderr and report digest."
    },
    {
      "path": "evidence/report_shape.json",
      "change_type": "created",
      "summary": "Observed exact shape/type check and report digest."
    },
    {
      "path": "share/case/reviewer/result.md",
      "change_type": "created",
      "summary": "Implementation result handoff."
    }
  ],
  "validation_results": [
    {
      "check": "report_contents",
      "status": "passed",
      "evidence": "evidence/report_contents.json: python3 -B public_check.py exited 0, stdout report_contents: passed; report sha256 a03d9134a1d62fcfa49bc7a8e7469f35837cf73e1facebaf96ac41d1e64989fe.",
      "required": true
    },
    {
      "check": "report_shape",
      "status": "passed",
      "evidence": "evidence/report_shape.json: parsed exact object keys, integer total, string ids in sorted order; assertions passed.",
      "required": true
    }
  ],
  "cleanup_results": [
    {
      "item": "Scratch files",
      "status": "complete",
      "evidence": "Generation and checks used stdin Python; no scratch files, backups, caches or installed dependencies created."
    },
    {
      "item": "Intentional retained outputs",
      "status": "retained",
      "evidence": "output/report.json, evidence/report_contents.json, evidence/report_shape.json and workflow artifacts retained under task cleanup policy; controller audit receipts retained automatically."
    }
  ],
  "failure_type": "none",
  "failed_step": "none",
  "failure_details": "none",
  "suspected_cause": "none",
  "suggested_return_target": "NONE",
  "notes": [
    "No upstream scope change or owner decision was required.",
    "Immutable inputs and tooling were not edited.",
    "Validation of this saved artifact is performed after writing; its external result is recorded by the controller audit."
  ]
}
