{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "implementation_result",
  "task_id": "case",
  "produced_by": "implementer",
  "status": "success",
  "revision": "01493282-5767-4edf-9e59-2c0b20bb073d",
  "input_fingerprints": {
    "share/case/implementer/impl.md": "04e5b3dfc995dac1a3813fd8e8ba68c71a5331af15ddd068646d5e1ad51558c8"
  },
  "input_artifacts": [
    {
      "path": "share/case/implementer/impl.md",
      "required": true,
      "summary": "Current implementation brief authorizing report and required validation."
    },
    {
      "path": "records.json",
      "required": false,
      "summary": "Current immutable record data."
    },
    {
      "path": "public_check.py",
      "required": false,
      "summary": "Required immutable validator."
    }
  ],
  "trusted_sources": [
    {
      "path": "AGENTS.md"
    },
    {
      "path": "implementer/AGENTS.md"
    },
    {
      "source": "Outer invocation authorizes case and scoped same-invocation execution."
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
      "source": "Observed report_contents and report_shape command outputs."
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
      "source": "Outer authorization and current brief",
      "summary": "same_invocation; retained stage context means no independent stage isolation or review."
    },
    {
      "kind": "execution",
      "source": "output/report.json",
      "summary": "Selected latest revision per id, then active only. Saved exact report total 18 and ids a,c,d,f."
    },
    {
      "kind": "validation",
      "source": "evidence/report_contents.txt",
      "summary": "python3 -B public_check.py returned exit 0, stdout report_contents: passed, no stderr. Rerun captured explicit subprocess exit status."
    },
    {
      "kind": "validation",
      "source": "evidence/report_shape.json",
      "summary": "Saved JSON exact key set, integer total, string array ids, lexicographic order, and expected current fixture values passed."
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
      "evidence/"
    ],
    "notes": "Orchestrator must mirror canonical upstream bytes and check route before reviewer input capture."
  },
  "implementation_summary": "Created output/report.json with total 18 and ids [a,c,d,f]. Latest a contributes 12; b canceled and e pending are excluded; c=5,d=-3,f=4 contribute. Both required checks passed.",
  "changed_files": [
    {
      "path": "output/report.json",
      "change_type": "created",
      "summary": "Current latest-active report, exact total and ids keys."
    },
    {
      "path": "evidence/report_contents.txt",
      "change_type": "created",
      "summary": "Actual public-check exit status, stdout and stderr."
    },
    {
      "path": "evidence/report_shape.json",
      "change_type": "created",
      "summary": "Passed strict saved-report shape and fixture-value assertions."
    },
    {
      "path": "share/case/reviewer/result.md",
      "change_type": "created",
      "summary": "Implementation stage result and observed evidence."
    }
  ],
  "validation_results": [
    {
      "check": "report_contents",
      "status": "passed",
      "evidence": "evidence/report_contents.txt: python3 -B public_check.py exit_status 0; report_contents: passed.",
      "required": true
    },
    {
      "check": "report_shape",
      "status": "passed",
      "evidence": "evidence/report_shape.json: strict saved JSON type/key/order and {total:18, ids:[a,c,d,f]} assertions passed; command exit 0.",
      "required": true
    }
  ],
  "cleanup_results": [
    {
      "item": "scratch files",
      "status": "not_created",
      "evidence": "Implementation used inline Python only; no scratch, backup, install or cache files created."
    },
    {
      "item": "report, stage outputs, evidence and automatic audit",
      "status": "retained",
      "evidence": "Task explicitly requires retaining these generated outputs; immutable inputs unchanged by commands."
    }
  ],
  "failure_type": "none",
  "failed_step": "none",
  "failure_details": "none",
  "suspected_cause": "none",
  "suggested_return_target": "NONE",
  "notes": [
    "No scope changes, input edits, blocker or owner decision needed.",
    "Skill-body condition off: no skill body loaded or used.",
    "Saved-output validation occurs after this write and is reported outside this artifact."
  ]
}
