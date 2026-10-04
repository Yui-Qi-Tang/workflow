{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "normalized_task",
  "task_id": "case",
  "produced_by": "tasker",
  "status": "ready",
  "revision": "0b28b627-6782-41dd-801b-0c2e21f9e7e8",
  "input_fingerprints": {
    "tasker/case.md": "b9427aeb10681ee8fe8968b5a47d8671aecf2dcbec47891c2d817353b07f7b04"
  },
  "input_artifacts": [
    {
      "path": "tasker/case.md",
      "required": true,
      "summary": "Current latest-revision report task, validation and output boundaries."
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
      "source": "Outer orchestrator authorization for this local trial only"
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "tasker/case.md",
      "summary": "Task content normalized subject to role rules."
    },
    {
      "source": "controller next case",
      "summary": "Reported changed task input and required tasker regeneration; old artifacts have no authority."
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
      "kind": "task_requirement",
      "source": "tasker/case.md",
      "summary": "For each id select its greatest revision, retain active latest records, sum integer amount, and sort ids lexicographically."
    },
    {
      "kind": "execution_mode",
      "source": "Outer trial authorization and tasker/case.md",
      "summary": "same_invocation for all five stages; retained context prevents independent stage isolation."
    }
  ],
  "handoff": {
    "next_agent": "researcher",
    "allowed_next_inputs": [
      "share/case/researcher/task.md",
      "records.json",
      "public_check.py",
      "agent_loop_poc/README.md"
    ],
    "notes": "Produce current research plan with latest-revision semantics and preserve all execution boundaries."
  },
  "goal": "Write output/report.json containing exactly total and ids for active latest revisions.",
  "scope": [
    "Read records.json and public_check.py.",
    "Produce output/report.json after permitted routing and all required share/case artifacts and mirrors.",
    "Retain observed checks under evidence/ and automatic audit receipts."
  ],
  "deliverables": [
    "output/report.json: exactly total integer and ids array of strings.",
    "Five current validated JSON stage artifacts and byte-identical review mirrors.",
    "Observed validation evidence and execution-mode record."
  ],
  "acceptance_criteria": [
    "Greatest revision is selected separately for each id before state filtering.",
    "Only active selected records contribute amount and id.",
    "total is the sum of selected integer amounts; ids are lexicographically sorted.",
    "Report contains exactly total and ids.",
    "Required report_contents check runs python3 -B public_check.py and passes.",
    "All stages validate saved bytes with fresh lineage; reviewer mirrors match canonical files."
  ],
  "conflicts": [],
  "source_of_truth": [
    "Current tasker/case.md requirements; historical synthetic evidence does not override it.",
    "Immutable records.json is the data input."
  ],
  "validation": [
    "Required implementation check report_contents: python3 -B public_check.py.",
    "Run python3 -B agent_loop_poc/loop.py validate case STAGE after each saved output and record exit status/digest externally.",
    "Recheck next/status after validation; mirror canonical upstream files before reviewer input capture."
  ],
  "cleanup": [
    "Retain stage outputs, report, evidence and automatic audit.",
    "Remove task-created scratch files; no backups or external outputs."
  ],
  "rollback": [
    "Only current in-scope generated outputs may be removed for correction.",
    "Never modify immutable inputs or audit; upstream correction belongs to its producer."
  ]
}
