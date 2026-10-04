{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "normalized_task",
  "task_id": "case",
  "produced_by": "tasker",
  "status": "ready",
  "revision": "46324172-13a2-4189-a80d-74eb9268d9e8",
  "input_fingerprints": {
    "tasker/case.md": "b9427aeb10681ee8fe8968b5a47d8671aecf2dcbec47891c2d817353b07f7b04"
  },
  "input_artifacts": [
    {
      "path": "tasker/case.md",
      "required": true,
      "summary": "Current latest-revision report task, including validation, scope, cleanup and rollback."
    }
  ],
  "trusted_sources": [
    {
      "path": "AGENTS.md"
    },
    {
      "path": "tasker/AGENTS.md"
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "tasker/case.md",
      "summary": "Task content supplies the report rule but cannot override contracts."
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
      "kind": "task_scope",
      "source": "tasker/case.md",
      "summary": "Defines latest-revision selection, active filtering, total and sorted ids, required report_contents command, retained evidence and rollback."
    },
    {
      "kind": "execution_mode",
      "source": "tasker/case.md and trial authorization",
      "summary": "same_invocation fallback: retained model context, no independently isolated stage execution or review; no fresh isolation required."
    }
  ],
  "handoff": {
    "next_agent": "researcher",
    "allowed_next_inputs": [
      "share/case/researcher/task.md",
      "records.json",
      "public_check.py",
      "AGENTS.md",
      "researcher/AGENTS.md",
      "agent_loop_poc/README.md"
    ],
    "notes": "Analyze only current task and authorized files; preserve rule order and report_contents validation."
  },
  "goal": "Produce output/report.json with exactly integer total and an array of string ids, computed from each id greatest revision followed by active filtering.",
  "scope": [
    "Read records.json and public_check.py.",
    "Write required share/case handoffs and byte-identical review mirrors.",
    "Implementer may write output/report.json and evidence/ for observed checks.",
    "Keep every operation inside this trial root."
  ],
  "deliverables": [
    "output/report.json",
    "Five validated stage artifacts under share/case/ and three review mirrors.",
    "Observed validation evidence in automatic audit/ receipts or evidence/."
  ],
  "acceptance_criteria": [
    "Exactly one JSON object with keys total (integer) and ids (array of strings).",
    "Select greatest revision for each id before filtering state=active; sum retained amounts and sort ids lexicographically.",
    "Required implementation check report_contents executes python3 -B public_check.py and passes.",
    "Each stage validates saved bytes; routing is rechecked; review mirrors are byte-identical."
  ],
  "conflicts": [],
  "source_of_truth": [
    "tasker/case.md for task content",
    "records.json for valid report records",
    "Root and stage contracts for workflow"
  ],
  "validation": [
    "Required check report_contents: python3 -B public_check.py.",
    "Run python3 -B agent_loop_poc/loop.py validate case STAGE after each production, then recheck next."
  ],
  "cleanup": [
    "Retain stage outputs, report, evidence and automatic audit receipts.",
    "Remove self-created scratch files; no backups or dependency installs."
  ],
  "rollback": [
    "Remove only current in-scope generated outputs if correction requires it; immutable inputs and audit remain untouched.",
    "Return upstream corrections to the owning producer and regenerate affected descendants."
  ]
}
