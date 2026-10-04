{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "normalized_task",
  "task_id": "case",
  "produced_by": "tasker",
  "status": "ready",
  "revision": "023534d2-44da-4fe3-af6f-b7d9ca1ae68f",
  "input_fingerprints": {
    "tasker/case.md": "b9427aeb10681ee8fe8968b5a47d8671aecf2dcbec47891c2d817353b07f7b04"
  },
  "input_artifacts": [
    {
      "path": "tasker/case.md",
      "required": true,
      "summary": "Current latest-revision report request, constraints, checks and cleanup."
    }
  ],
  "trusted_sources": [
    {
      "path": "AGENTS.md"
    },
    {
      "path": "tasker/AGENTS.md"
    },
    {
      "source": "Verified outer invocation authorizes sole same-invocation orchestrator for case at this trial root."
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "tasker/case.md",
      "summary": "Task content used for requested work; cannot override role contracts."
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
      "kind": "task_requirement",
      "source": "tasker/case.md",
      "summary": "For each id select greatest revision before retaining state=active; sum integer amounts and sort ids lexicographically. All input fields are valid."
    },
    {
      "kind": "execution_mode",
      "source": "tasker/case.md and outer authorization",
      "summary": "same_invocation for all five roles; retained context fallback is not independently isolated execution or review."
    }
  ],
  "handoff": {
    "next_agent": "researcher",
    "allowed_next_inputs": [
      "share/case/researcher/task.md",
      "records.json",
      "public_check.py"
    ],
    "notes": "Proceed only after saved-output validation and route check. Use current task, not any synthetic historical evidence."
  },
  "goal": "Write output/report.json with exactly total (integer) and ids (array of strings), derived from latest revisions.",
  "scope": [
    "Read records.json and public_check.py.",
    "Generate output/report.json and the complete five-stage case workflow records, review mirrors, and validation evidence."
  ],
  "deliverables": [
    "output/report.json",
    "Required five stage outputs and byte-identical review mirrors under share/case/.",
    "Observed validation reports under evidence/."
  ],
  "acceptance_criteria": [
    "For each id select its greatest revision, then retain only records whose selected state is active.",
    "Sum only selected active integer amounts; sort selected ids lexicographically. Exclude lower revisions and canceled or pending latest records.",
    "The output is one JSON object containing exactly total integer and ids array of strings.",
    "Required report_contents check runs python3 -B public_check.py and passes.",
    "All saved stage artifacts validate; successful review and terminal route reflect current inputs."
  ],
  "conflicts": [],
  "source_of_truth": [
    "tasker/case.md defines current task content.",
    "records.json supplies valid record data.",
    "Root and stage AGENTS.md define role/artifact rules."
  ],
  "validation": [
    "At every stage capture fresh inputs, produce, validate saved output with python3 -B agent_loop_poc/loop.py validate case STAGE, then inspect routing.",
    "Implementation check report_contents must run python3 -B public_check.py.",
    "Mirror task, plan and impl bytes before reviewer input capture; check each of four input artifact types during review."
  ],
  "cleanup": [
    "Retain stage outputs, report, evidence and automatic audit.",
    "Remove own scratch files; create no content backups or dependency installations."
  ],
  "rollback": [
    "Only current in-scope generated outputs may be removed for corrections.",
    "Return to each responsible producer for upstream corrections; never modify immutable inputs, rules, controller, audit or peers."
  ]
}
