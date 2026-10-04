# Implement approved workflow documentation and skill

Human authorization: after the source-backed assessment, the user said 好，開始修改. Implement the proposed nested type/enum clarifications, execution-mode distinction, orchestrator entrypoint and one thin workflow-orchestrator skill.

Execution mode: same_invocation. Main agent produces all five stages directly; fresh isolation is unavailable under current opposition-only delegation rules. This documentation task does not require isolated model execution. Record this mode in stage evidence.

Write allowlist:
- AGENTS.md
- tasker/AGENTS.md
- researcher/AGENTS.md
- implementer/AGENTS.md
- reviewer/AGENTS.md
- README.md
- README.en.md
- README.zh.md
- agent_loop_poc/README.md
- .agents/skills/workflow-orchestrator/SKILL.md
- .agents/skills/workflow-orchestrator/agents/openai.yaml
- This task input and share/workflow-orchestrator-skill-20261004/** audit; orchestrator owns mirrors and validation receipts.

Constraints:
- Implement only the approved targeted role documentation and thin project-local skill.
- Preserve all five stages, instruction precedence, existing controller semantics and version 0.3.0.
- Main agent owns design, edits and checks. Subagents may only provide textual opposition without tools; no prior Luna execution exception applies.
- Use same_invocation fallback for this task and disclose lack of fresh-model isolation; no model efficacy experiment.
- Preserve frozen experiments and prior task evidence, including untracked assessment records.
- No commit, push, new runner, dependency installation, or automatic side-effect retry.

Authorized reads: root and five role AGENTS, README variants, controller and existing tests, skill-creator and OpenAI Docs instructions, current official skill discovery documentation, current task artifacts and necessary Git metadata. Historical assessment may inform requested scope but never override schema.

Plan: complete document field types from existing controller; preserve fresh invocation as goal for all tasks and block fallback when isolation is an acceptance requirement; centralize existing orchestrator duties via links; allow task-referenced reusable skill/CLI without new authority. Create two-file instruction-only project skill at .agents/skills/workflow-orchestrator, using the repo scope verified in official documentation. Keep default implicit selection enabled. Prepare and validate candidate bytes before requesting any filesystem escalation required for protected .agents.

Validation:
- contract_alignment: Compare common and nested documentation types/enums with current contracts.py and manually review execution/authority semantics.
- skill_validation: Run bundled quick_validate.py on the skill; check YAML, local links, and metadata; inspect trigger scope and CLI instructions.
- controller_regression: Run python3 -B -m unittest discover -v and require all tests pass.
- scope_and_whitespace: Check changed files against explicit allowlist, preserve baseline hashes for other tracked and existing assessment files, and run git diff --check.
- Validate saved artifacts after each stage; inspect next text decision before handoff.

Cleanup: retain task and audit evidence. Remove temporary skill candidate after identical installation and validation. Standard-library tests clean their own temporary directories; use -B to avoid bytecode.

Rollback: reverse only this task edits from recorded baseline/reviewable diff; remove only this new skill directory if necessary. Preserve all pre-existing untracked work. No public side effects.
