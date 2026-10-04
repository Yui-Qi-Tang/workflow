# Delete obsolete task and assess workflow instructions

Human request: 幫我刪除 `go-worker-2026050200`；評估目前專案內 AGENTS.md 是否需要修改，以及是否需要建立 skill。

Scope: remove the named local workflow task and its nine untracked files; assess six operative AGENTS and skill suitability. Frozen experiment rules are historical evidence. No production rules or skill changes are authorized by this assessment.

Execution: main agent runs the five roles sequentially using the root same-invocation fallback. This is not a fresh-model experiment. Orchestrator writes this task input, validation receipts and review mirrors. Each stage writes its own output. No special execution-subagent authorization applies.

Constraints:
- Delete only tasker/go-worker-2026050200.md and share/go-worker-2026050200/.
- Assessment only: do not edit operative AGENTS, controller, README, frozen experiment evidence, or create a skill.
- No experiment, commit, push, external messages, or changes to the sibling go-worker project.
- Main agent owns all five stages; same-invocation fallback, no claim of fresh-context isolation.
- Subagents may only challenge supplied propositions in text without tools; prior experiment exception does not apply.
- Preserve current five-stage and saved-output validation requirements.

Authorized reads:
- AGENTS.md
- tasker/AGENTS.md
- researcher/AGENTS.md
- planner/AGENTS.md
- implementer/AGENTS.md
- reviewer/AGENTS.md
- agent_loop_poc/contracts.py
- agent_loop_poc/loop.py
- agent_loop_poc/README.md
- /Users/yuki/.codex/skills/.system/skill-creator/SKILL.md
- Git metadata and exact deletion targets; prior commit excluded-hashes evidence if useful.

Validation:
- deleted_task_absent: Verify exactly nine regular files, no symlinks, contained under the two authorized targets; delete and assert both targets absent.
- unrelated_files_preserved: Compare all pre-existing tracked-file SHA-256 values and index state before/after; only new task records may remain untracked.
- assessment_grounded: Check all six operative rules against current controller and skill-creator guidance; attach source lines, distinguish recommendations from observed defects and untested benefits.
- Each saved stage must pass validate before handoff; recheck routing.

Cleanup: retain this task input and required five-stage audit plus compact evidence under share/workflow-rules-assessment-20261004; create no temporary scripts or deletion-content backups.

Rollback: deleted files are untracked and not recoverable by Git checkout. User directly requested deletion; preserve only names and hashes as evidence, not their contents. Assessment can be withdrawn without changing production files.
