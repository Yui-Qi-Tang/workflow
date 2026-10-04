{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "implementation_result",
  "task_id": "case",
  "produced_by": "implementer",
  "status": "success",
  "revision": "778e7baf-b45e-4511-a2ae-0a2f91410007",
  "input_fingerprints": {
    "share/case/implementer/impl.md": "c2c9df99cd43507b0adc62c619df253c7be8f306830931b0609caaaf1255c445"
  },
  "input_artifacts": [
    {
      "path": "share/case/implementer/impl.md",
      "required": true,
      "summary": "Current ready implementation brief."
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
      "path": "evidence/report-contents.txt"
    },
    {
      "path": "evidence/report-schema.txt"
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
      "source": "Outer invocation and implementation brief",
      "summary": "same_invocation fallback retains context; execution and review are not independently isolated. Skill body not loaded."
    },
    {
      "kind": "implementation",
      "source": "evidence/selection.json",
      "summary": "Selected greatest revisions before filtering; active a=12,c=5,d=-3,f=4 give 18; b latest canceled and e pending excluded."
    },
    {
      "kind": "command_result",
      "source": "evidence/report-contents.txt and evidence/report-contents.exit",
      "summary": "python3 -B public_check.py exited 0 and printed report_contents: passed."
    },
    {
      "kind": "command_result",
      "source": "evidence/report-schema.txt and evidence/report-schema.exit",
      "summary": "Python strict key/type/order assertions exited 0 and printed report_schema: passed."
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
      "evidence/",
      "agent_loop_poc/README.md"
    ],
    "notes": "Orchestrator must create byte-identical canonical review mirrors before capturing reviewer inputs; review current observed evidence."
  },
  "implementation_summary": "Produced report total 18 with ids a,c,d,f by maximum-revision selection followed by active filtering. Required content and strict schema checks passed.",
  "changed_files": [
    {
      "path": "output/report.json",
      "change_type": "regenerated",
      "summary": "Current report with exact total/ids object."
    },
    {
      "path": "evidence/selection.json",
      "change_type": "created",
      "summary": "Observed selected latest rows and output."
    },
    {
      "path": "evidence/report-contents.txt",
      "change_type": "created",
      "summary": "Actual public checker output; paired exit status saved in report-contents.exit."
    },
    {
      "path": "evidence/report-schema.txt",
      "change_type": "created",
      "summary": "Actual strict key/type/order check output; paired exit status saved in report-schema.exit."
    },
    {
      "path": "share/case/reviewer/result.md",
      "change_type": "regenerated",
      "summary": "Current result with fresh lineage and actual checks."
    }
  ],
  "validation_results": [
    {
      "check": "report_contents",
      "status": "passed",
      "evidence": "python3 -B public_check.py exit 0; evidence/report-contents.txt reports report_contents: passed; evidence/report-contents.exit is 0.",
      "required": true
    },
    {
      "check": "report_schema",
      "status": "passed",
      "evidence": "Python strict exact-key, integer-total, string-array and lexical-order assertions passed with exit 0; evidence/report-schema.txt and evidence/report-schema.exit.",
      "required": true
    }
  ],
  "cleanup_results": [
    {
      "item": "Task-created scratch files",
      "status": "not_needed",
      "evidence": "No scratch files, caches, dependencies or content backups created; scripts ran as python3 -B via stdin."
    },
    {
      "item": "Intentional retained outputs",
      "status": "retained",
      "evidence": "Report, required stage artifacts, evidence and automatic audit retained as requested."
    }
  ],
  "failure_type": "none",
  "failed_step": "none",
  "failure_details": "none",
  "suspected_cause": "none",
  "suggested_return_target": "NONE",
  "notes": [
    "Prior synthetic evidence was not reused; stages were regenerated under current task.",
    "No immutable inputs or peer files modified; no Git, network or skill-body load."
  ]
}
