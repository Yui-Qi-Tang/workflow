# Workflow integrity milestone

Task ID: workflow-integrity-20261003

Authorization: the user approved implementing the first layer proposed in this
chat: trustworthy handoffs, explicit transitions, upstream invalidation, and
structured human-input decisions.

## Goal and scope

Strengthen the existing single-process Python control plane. Preserve the five
stages and JSON artifact filenames. The main agent performs all stages; any
subagent may only challenge supplied propositions in text without tools.
This run uses the documented same-invocation fallback, not isolated invocations.

Authorized paths: agent_loop_poc/, README.md, README.en.md, README.zh.md,
AGENTS.md, reviewer/AGENTS.md, this task file, and this task's share directory.
Preserve existing go-worker task and share records. No commit, push, executor,
model integration, external project edits, or performance experiment.

## Deliverables and frozen acceptance cases

1. Validate all common and stage-specific required fields, nested requirements,
   enum values, task/stage identity and cross-field consistency. Reject invalid
   JSON, duplicate keys, non-finite values, and legacy Markdown for routing.
2. Missing predecessors, malformed artifacts and unsupported statuses must never
   advance to a downstream stage or declare completion.
3. Add revision identifiers and direct input SHA-256 fingerprints to routed
   artifacts. Provide a read-only CLI command to obtain input fingerprints before
   a stage starts. An absent fingerprint blocks migration; a changed predecessor
   invalidates its consumer and descendants without deleting historical files.
   Cover task input and canonical handoffs, not arbitrary external source files.
4. Require reviewer mirrors to match canonical task/plan/impl bytes. Completion
   requires a valid, current chain, successful implementation, required checks
   passed, and consistent successful review.
5. Decide human intervention from structured blocking questions or pending task
   updates, never keywords. Empty questions and nonblocking questions must not
   cause waiting. Environment blockers remain distinct from stage responsibility.
6. Respect validated handoff targets, reject impossible targets, and route stale
   stages explicitly. Do not interpret old review files as proof of new work.
7. Keep init/sync/next/status usable; status and next are read-only. Write state
   atomically; reject unsafe task IDs. This is a single-writer control plane,
   not a promise of concurrent execution or safe replay of external side effects.
8. Update documentation, including the current tool version and migration limits.

## Validation

Freeze regression tests before replacing routing code. Record baseline failures
and final results from `python3 -B -m unittest discover -v` and
`git diff --check`. Use temporary directories for test data. Include a real CLI
smoke check against this task once its review bundle is complete. Verify canonical
mirrors and all five artifacts against the new validator. These checks establish
bounded control-plane behavior, not model quality or general task success rates.

## Cleanup, rollback and reporting

Tests clean their temporary directories. Use -B to avoid bytecode. Preserve this
task's five-stage records and validation logs under share/workflow-integrity-20261003/.
On failure retain scoped changes and report the blocker; never reset unrelated
changes. Fix implementation mistakes within this scope. Report changed behavior,
actual validation and remaining limitations.
