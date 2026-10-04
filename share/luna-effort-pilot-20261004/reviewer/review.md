{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "workflow_review",
  "task_id": "luna-effort-pilot-20261004",
  "produced_by": "reviewer",
  "status": "success",
  "revision": "f2683ce2-54fd-40d2-bea2-d4b15bfe9538",
  "input_fingerprints": {
    "share/luna-effort-pilot-20261004/reviewer/task.md": "f3408779fc9e0db9982ffbf4565049be1a97880b21d495b8dbf0cc6b8285ee1a",
    "share/luna-effort-pilot-20261004/reviewer/plan.md": "c53d969100955d7fc2b9f0af0118ceae10863e8f16460c61a56e71482f4349be",
    "share/luna-effort-pilot-20261004/reviewer/impl.md": "5d993abcc7adda49eee71bfd7c86fbb31fceba199e54117aa128de65ef1638c8",
    "share/luna-effort-pilot-20261004/reviewer/result.md": "6a8cbe27c469e605e29dd413715c5b7ed6334f6f7554d618eb9185cf78fbe050"
  },
  "input_artifacts": [
    {
      "path": "share/luna-effort-pilot-20261004/reviewer/task.md",
      "required": true,
      "summary": "Required review bundle artifact"
    },
    {
      "path": "share/luna-effort-pilot-20261004/reviewer/plan.md",
      "required": true,
      "summary": "Required review bundle artifact"
    },
    {
      "path": "share/luna-effort-pilot-20261004/reviewer/impl.md",
      "required": true,
      "summary": "Required review bundle artifact"
    },
    {
      "path": "share/luna-effort-pilot-20261004/reviewer/result.md",
      "required": true,
      "summary": "Required review bundle artifact"
    }
  ],
  "trusted_sources": [
    {
      "path": "AGENTS.md",
      "summary": "Root contract"
    },
    {
      "path": "reviewer/AGENTS.md",
      "summary": "Review contract"
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "experiments/luna-effort-pilot-20261004/scores.json",
      "summary": "Frozen-evaluator results"
    },
    {
      "path": "experiments/luna-effort-pilot-20261004/audit.json",
      "summary": "Post-run evidence audit"
    }
  ],
  "constraints": [
    "Preserve six-cell denominator and failed original outputs.",
    "No product/rule changes, retries, hidden repairs or model ranking."
  ],
  "open_questions": [],
  "evidence": [
    {
      "kind": "command",
      "source": "share/luna-effort-pilot-20261004/evidence/reviewer-schema-checks.json",
      "summary": "All four review input artifacts valid."
    },
    {
      "kind": "command",
      "source": "experiments/luna-effort-pilot-20261004/audit.stdout.json",
      "summary": "14 calls; hashes, original paired inputs, protected files and cleanup verified."
    },
    {
      "kind": "command",
      "source": "experiments/luna-effort-pilot-20261004/recount.stdout.json",
      "summary": "Six cells recounted, three expected outcomes including two legitimate conflict blocks."
    }
  ],
  "handoff": {
    "next_agent": "NONE",
    "allowed_next_inputs": [],
    "notes": "Experiment complete; model result failures and capability limits preserved."
  },
  "overall_judgment": "success",
  "failure_source": "NONE",
  "confidence": "high",
  "reason": "The authorized pilot was completed faithfully with all six cells retained, no model retries or artifact repairs, independent checks and qualified conclusions. Model execution failures were disclosed. Only one solvable cell reached implementation; no relative coding-capability ranking is supported.",
  "recommended_return_target": "NONE",
  "recommended_next_action": "For a future separately frozen follow-up, distinguish schema visibility and outer authorization delivery as separate interventions; preserve this pilot.",
  "artifact_schema_checks": [
    {
      "artifact": "normalized_task",
      "status": "passed",
      "evidence": "share/luna-effort-pilot-20261004/reviewer/task.md passed JSON, artifact and lineage validation; exact mirrors and input fingerprints checked by controller."
    },
    {
      "artifact": "research_plan",
      "status": "passed",
      "evidence": "share/luna-effort-pilot-20261004/reviewer/plan.md passed JSON, artifact and lineage validation; exact mirrors and input fingerprints checked by controller."
    },
    {
      "artifact": "implementation_brief",
      "status": "passed",
      "evidence": "share/luna-effort-pilot-20261004/reviewer/impl.md passed JSON, artifact and lineage validation; exact mirrors and input fingerprints checked by controller."
    },
    {
      "artifact": "implementation_result",
      "status": "passed",
      "evidence": "share/luna-effort-pilot-20261004/reviewer/result.md passed JSON, artifact and lineage validation; exact mirrors and input fingerprints checked by controller."
    }
  ],
  "notes": [
    "Review success concerns experiment execution and reporting, not success of all tested models.",
    "Main reviewed both conflict descriptions and exact malformed outputs.",
    "Main orchestration used same-invocation fallback; 14 tested Luna calls used fork_turns=none.",
    "Full raw tool transcripts and provider snapshot/token usage unavailable; filesystem scope is logical, not OS-isolated."
  ]
}
