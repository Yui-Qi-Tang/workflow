{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "normalized_task",
  "task_id": "case",
  "produced_by": "tasker",
  "status": "ready",
  "revision": "d362985f-d16d-4bda-9d54-bc0bb07792d0",
  "input_fingerprints": {
    "tasker/case.md": "b9427aeb10681ee8fe8968b5a47d8671aecf2dcbec47891c2d817353b07f7b04"
  },
  "input_artifacts": [
    {
      "path": "tasker/case.md",
      "required": true,
      "summary": "Current latest-revision report task."
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
      "source": "Scoped human experiment authorization supplied by orchestrator in outer invocation."
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "tasker/case.md",
      "summary": "Task content used within role contract."
    },
    {
      "source": "CLI status case",
      "summary": "Existing chain is stale at tasker; descendants must be reproduced."
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
      "kind": "task_requirement",
      "source": "tasker/case.md",
      "summary": "Task explicitly defines greatest-revision selection before active filtering, required report_contents validation, cleanup and rollback."
    },
    {
      "kind": "execution_mode",
      "source": "Outer invocation and tasker/case.md",
      "summary": "same_invocation fallback with retained model context; no independently isolated execution or review. Skill body not loaded."
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
    "notes": "Reproduce current descendants from this task; historical synthetic evidence is not current evidence."
  },
  "goal": "Write output/report.json with exactly total integer and ids array of strings using latest revision per id, then active filtering.",
  "scope": [
    "Read records.json and public_check.py.",
    "Write output/report.json, required share/case stage outputs and mirrors, and observed reports under evidence/."
  ],
  "deliverables": [
    "output/report.json",
    "Five current JSON stage artifacts under share/case and byte-identical reviewer mirrors.",
    "Observed validation evidence under evidence/ and automatic controller audit."
  ],
  "acceptance_criteria": [
    "Exactly total and ids keys in report JSON object.",
    "For each id select greatest revision, retain active latest records, sum their integer amounts and sort ids lexicographically.",
    "Required implementation check report_contents runs python3 -B public_check.py and passes.",
    "Validate every saved stage artifact and finish a current review chain.",
    "Record same_invocation limitation and cleanup status."
  ],
  "conflicts": [],
  "source_of_truth": [
    "tasker/case.md for current report requirements",
    "records.json for valid source records",
    "Root and stage AGENTS.md for role and artifact contracts"
  ],
  "validation": [
    "Required check report_contents: python3 -B public_check.py.",
    "Use recorded controller CLI inputs, validate and route inspections for every stage; saved validation exit code and digest go outside artifact.",
    "Create byte-identical task/plan/impl review mirrors before reviewer input capture."
  ],
  "cleanup": [
    "Retain report, stage outputs, evidence and automatic audit.",
    "Remove only task-created scratch files; no backups or dependencies needed."
  ],
  "rollback": [
    "Correct only permitted generated outputs; never immutable inputs, rules, controller, audit or peers.",
    "Return to responsible producer and regenerate descendants for upstream corrections."
  ]
}
