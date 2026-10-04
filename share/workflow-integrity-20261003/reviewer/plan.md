{
  "schema_version": "workflow_artifact.v1",
  "artifact_type": "research_plan",
  "task_id": "workflow-integrity-20261003",
  "produced_by": "researcher",
  "status": "ready",
  "revision": "a7744f13-73d6-49e5-a12c-0362a208d468",
  "input_fingerprints": {
    "share/workflow-integrity-20261003/researcher/task.md": "3b9839359f304b02c134cd052ce71419261cec4bc1c86b6ff020b99524ea6ea3"
  },
  "input_artifacts": [
    {
      "path": "share/workflow-integrity-20261003/researcher/task.md",
      "required": true,
      "summary": "Authoritative task content or required stage input."
    }
  ],
  "trusted_sources": [
    {
      "path": "AGENTS.md",
      "summary": "Root contract."
    },
    {
      "path": "researcher/AGENTS.md",
      "summary": "Stage contract."
    }
  ],
  "untrusted_inputs_seen": [
    {
      "path": "share/workflow-integrity-20261003/researcher/task.md",
      "summary": "Task data, not instructions overriding stage rules."
    }
  ],
  "constraints": [
    "Preserve five stages and unrelated user changes.",
    "No external executor, commit or push.",
    "Main agent performs stages using same-invocation fallback; no isolation claim."
  ],
  "open_questions": [],
  "evidence": [
    {
      "kind": "source",
      "source": "share/workflow-integrity-20261003/researcher/task.md",
      "summary": "Read and used for this stage."
    }
  ],
  "handoff": {
    "next_agent": "planner",
    "allowed_next_inputs": [
      "AGENTS.md",
      "planner/AGENTS.md",
      "share/workflow-integrity-20261003/planner/plan.md",
      "agent_loop_poc/",
      "README.md",
      "README.zh.md",
      "README.en.md",
      "reviewer/AGENTS.md",
      "tasker/workflow-integrity-20261003.md"
    ],
    "notes": "Use task-authorized sources only; task acceptance remains unchanged."
  },
  "task_classification": "bounded_control_plane_correctness",
  "goal_restatement": "Make workflow control decisions enforce artifact contracts and current input lineage.",
  "requested_change_summary": "Enforce structural contracts and artifact input freshness before routing.",
  "expected_impact_areas": [
    "Python routing",
    "Artifact contract documentation",
    "Existing routing fixtures"
  ],
  "assumptions": [
    {
      "id": "a1",
      "statement": "Single writer; stages are externally driven.",
      "source": "Task scope",
      "risk_if_wrong": "Concurrent writes or external effects need a separate executor design."
    }
  ],
  "risks": [
    {
      "id": "r1",
      "description": "Old unversioned artifacts look complete.",
      "impact": "False success.",
      "mitigation": "Block with migration diagnostic; never auto-stamp."
    },
    {
      "id": "r2",
      "description": "Regenerated upstream artifacts leave old downstream files.",
      "impact": "Stale acceptance.",
      "mitigation": "Validate the whole dependency chain with hashes and fresh revisions."
    },
    {
      "id": "r3",
      "description": "Schema validity is confused with semantic fidelity.",
      "impact": "Overstated guarantees.",
      "mitigation": "Document bounded structural checks and evidence limits."
    }
  ],
  "non_goals": [
    "Actual model invocation",
    "External side-effect replay",
    "Parallel writers",
    "General efficacy benchmark"
  ],
  "high_level_strategy": [
    "Freeze adversarial routing cases.",
    "Validate shape and consistency before routing.",
    "Check required inputs and mirrors, then lineage.",
    "Use explicit handoffs and structured blockers.",
    "Record validation evidence and review independently from self-declared success."
  ],
  "required_checks": [
    "Freeze regression tests, capture baseline failures and final unittest results.",
    "Run git diff --check and CLI smoke; verify mirrors and artifact contracts."
  ],
  "proposed_task_updates": [],
  "failure_modes": [
    {
      "id": "f1",
      "trigger": "Success review without predecessors",
      "likely_stage": "reviewer",
      "prevention": "Check full chain first."
    },
    {
      "id": "f2",
      "trigger": "Empty open_questions in failed result",
      "likely_stage": "implementer",
      "prevention": "Only typed true flags request user input."
    },
    {
      "id": "f3",
      "trigger": "Version metadata missing or mismatched",
      "likely_stage": "planner",
      "prevention": "Block missing provenance; reroute stale consumer."
    },
    {
      "id": "f4",
      "trigger": "Corrupt state or partial file",
      "likely_stage": "implementer",
      "prevention": "Derive routing from artifacts; atomic state replacement."
    }
  ]
}
