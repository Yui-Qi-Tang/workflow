# Workflow README

Current control-plane version: **0.3.0** (`agent_loop_poc.v2` state;
`workflow_artifact.v1` artifacts with required routing lineage metadata).

Choose a language version:

- [中文版本](./README.zh.md)
- [English version](./README.en.md)

This README is explanatory only. The operative workflow rules are in
[`AGENTS.md`](./AGENTS.md) and the stage-specific `AGENTS.md` files.

For starting or resuming a task, use the
[orchestrator entrypoint](./agent_loop_poc/README.md#orchestrator-entrypoint).
The repository includes an instruction-only
[`workflow-orchestrator` skill](./.agents/skills/workflow-orchestrator/SKILL.md)
in Codex's [repository skill location](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills).
It guides existing CLI operations without changing controller version 0.3.0,
permissions, or artifact schemas.
