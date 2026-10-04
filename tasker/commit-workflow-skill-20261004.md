# Prepare and commit workflow guidance and skill pilot

Current human request: 好，commit這次改動. The main agent will prepare and review the current approved changes through all five stages, then execute the authorized local Git commit as the final orchestrator action. Do not claim a commit exists before Git succeeds; report its hash outside the committed tree.

Include only evidence/allowlist.json paths under share/commit-workflow-skill-20261004. These are current AGENTS/README guidance, the project workflow-orchestrator skill, assessment/implementation bundles, the complete frozen skill A/B experiment and its administrative bundle, plus this commit-preparation task. Preserve the 556 existing selected files byte-for-byte, including frozen inputs, all trial outputs and raw logs. No product edits, model reruns, other branch changes, amend, merge or push. Stay on current main. Main performs stages sequentially in same_invocation fallback; no independent stage isolation claimed and no execution subagent authorization reused.

Acceptance: reviewed explicit allowlist; preserved baseline bytes and frozen experiment; existing workflow review bundles validate; stage saved files validate before handoff; exact staged path and Git-blob equality; whitespace inspection with any immutable raw-evidence findings disclosed, not rewritten; full review before commit. After commit verify parent, commit file set, empty index and worktree. No new post-commit receipt file is needed.

Validation: content_integrity (baseline plus frozen manifest, final trial inventories and fixed scores), workflow_records (validate three existing completed bundles), diff_review (tracked and then cached whitespace check), index_scope (allowlisted exact staged paths and blobs). Existing 66-test pass and six real trial results are retained evidence; this commit adds no runtime behavior and does not rerun models or alter outcomes.

Cleanup: keep audit and experiment evidence. Use python3 -B; no scratch files, installs or new caches. Rollback: preserve files and index on Git failure; report the failure, never reset unrelated files or rewrite history.
