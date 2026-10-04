{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "workflow_review",
  "task_id": "case",
  "produced_by": "reviewer",
  "status": "success",
  "revision": "46d377dc-7d99-4213-88bc-174e183ec03e",
  "input_fingerprints": {
    "share/case/reviewer/task.md": "cd52ae7a3ef3b358515681dae670affa0a949edf478911de7cc1c045f435cbd0",
    "share/case/reviewer/plan.md": "2b8fc148b4b5f693892e2511e1032e38175c74b592f8aaa9f06820f6d2233ccb",
    "share/case/reviewer/impl.md": "c2c9df99cd43507b0adc62c619df253c7be8f306830931b0609caaaf1255c445",
    "share/case/reviewer/result.md": "ab2c5391333a62f695707b025e42f7dad2b915007e741aa5d5f7cb3642374be5"
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
      "path": "evidence/report-contents.txt"
    },
    {
      "path": "evidence/report-schema.txt"
    },
    {
      "path": "evidence/review-mirrors.json"
    },
    {
      "source": "Recorded saved-output validation reports under evidence/"
    }
  ],
  "constraints": [
    "Select greatest revision per id before filtering state=active; lower revisions, canceled and pending latest records do not contribute.",
    "Input records are valid; do not invent schema rules.",
    "Write only permitted generated outputs; immutable inputs, rules, controller, audit and peer runs must not be edited.",
    "Use python3 -B agent_loop_poc/loop.py for controller operations.",
    "All five stages run sequentially as same_invocation; nested agents prohibited.",
    "No Git, network, installs, external actions or skill-body loading."
  ],
  "open_questions": [],
  "evidence": [
    {
      "kind": "execution_mode",
      "source": "Outer invocation and review inputs",
      "summary": "same_invocation fallback with retained context. Review is not independent isolated execution; skill body not loaded."
    },
    {
      "kind": "report_review",
      "source": "Review bundle, output/report.json and evidence/selection.json",
      "summary": "Current artifacts preserve greatest-revision-first semantics; report is total 18 and ids a,c,d,f, consistent with a=12,c=5,d=-3,f=4 and exclusion of latest canceled b and pending e."
    },
    {
      "kind": "actual_checks",
      "source": "evidence/report-contents.txt, report-contents.exit, report-schema.txt, report-schema.exit",
      "summary": "Both required checks passed with exit 0; names and required flags match the brief."
    },
    {
      "kind": "lineage",
      "source": "evidence/review-mirrors.json and reviewer input capture",
      "summary": "Three mirrored upstream artifacts are byte-identical to current canonicals. All four prefix saved outputs passed recorded validation."
    },
    {
      "kind": "cleanup",
      "source": "share/case/reviewer/result.md",
      "summary": "Implementation used python3 -B stdin commands and no scratch files or dependencies; required outputs and evidence intentionally retained."
    }
  ],
  "handoff": {
    "next_agent": "NONE",
    "allowed_next_inputs": [],
    "notes": "Current task succeeds within supplied input and checks; no upstream return required."
  },
  "overall_judgment": "success",
  "failure_source": "NONE",
  "confidence": "high",
  "reason": "All current stages preserve latest-revision semantics and scope. Actual report check and strict shape check passed; current saved artifacts validate, review mirrors match, and declared cleanup is consistent with observed commands. Historical stale records did not authorize completion.",
  "recommended_return_target": "NONE",
  "recommended_next_action": "Retain current report, stage records, validation evidence and automatic audit; no further execution required.",
  "artifact_schema_checks": [
    {
      "artifact": "normalized_task",
      "status": "passed",
      "evidence": "Parsed expected artifact type and inspected required fields; recorded CLI validate case tasker exit 0; evidence/tasker-validation.json binds saved digest cd52ae7a3ef3b358515681dae670affa0a949edf478911de7cc1c045f435cbd0."
    },
    {
      "artifact": "research_plan",
      "status": "passed",
      "evidence": "Parsed expected artifact type and inspected required fields; recorded CLI validate case researcher exit 0; evidence/researcher-validation.json binds saved digest 2b8fc148b4b5f693892e2511e1032e38175c74b592f8aaa9f06820f6d2233ccb."
    },
    {
      "artifact": "implementation_brief",
      "status": "passed",
      "evidence": "Parsed expected artifact type and inspected required fields; recorded CLI validate case planner exit 0; evidence/planner-validation.json binds saved digest c2c9df99cd43507b0adc62c619df253c7be8f306830931b0609caaaf1255c445."
    },
    {
      "artifact": "implementation_result",
      "status": "passed",
      "evidence": "Parsed expected artifact type and inspected required fields; recorded CLI validate case implementer exit 0; evidence/implementer-validation.json binds saved digest ab2c5391333a62f695707b025e42f7dad2b915007e741aa5d5f7cb3642374be5."
    }
  ],
  "notes": [
    "Evidence supports only this bounded current local report task.",
    "Controller validation checks structural and declared-result consistency; semantic conclusion also uses current report and command evidence.",
    "same_invocation is the observed execution mode, not fresh isolated execution or independent review.",
    "No blocking owner question remains; no skill body loaded."
  ]
}
