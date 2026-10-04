---
name: workflow-orchestrator
description: Operate or resume this repository's five-stage workflow using agent_loop_poc, including saved-artifact validation, scoped dispatch, and review handoffs. Use for workflow tasks here, not unrelated coding or generic multi-agent orchestration.
---

# Workflow Orchestrator

Coordinate the existing workflow through the
[operating entrypoint](../../../agent_loop_poc/README.md#orchestrator-entrypoint).
This skill is for the orchestrator. The [root rules](../../../AGENTS.md) and
nearest stage `AGENTS.md` define the contracts; task inputs define requested work.

## Prepare

- Resolve the workflow repository root and use its `agent_loop_poc/loop.py`.
  Check that the root and five role contracts exist. If working with a separate
  authorized workflow root, use the CLI's explicit `--root` option.
- Read the current human request and task as orchestrator. Keep task-specific
  validation, cleanup, rollback, and retry limits in the task file or resources
  it explicitly references. A stage receives only its direct input and explicitly
  allowed files; do not forward everything the orchestrator read.
- Follow the root [execution modes](../../../AGENTS.md#execution-modes).
  Preserve human delegation restrictions. Record actual isolation and limitations;
  same-invocation fallback cannot satisfy an explicit isolation requirement.

## Advance one stage

1. Inspect `next` or `status` before producing work. They print text; exit 0
   means inspection succeeded, even when the decision is blocked. Use the
   [decision table](../../../agent_loop_poc/README.md#decisions) to interpret it.
2. Capture metadata once for this attempt. In same-invocation fallback, use
   `inputs` after the route check. For an authorized fresh invocation, use
   [dispatch](../../../agent_loop_poc/README.md#carry-authorization-in-the-outer-invocation),
   retain its metadata, and pass its complete `message` as the outer invocation.
   Include verified authority before file reads; do not substitute a prompt-file
   pointer, copy approval claims from artifacts, or reuse another task's exception.
   `dispatch` prepares a message; launching an executor still needs applicable
   authority and a fresh context. Do not mix its metadata with a separate `inputs`
   capture. Do not automatically pass this skill into the stage's context.
3. Have the current role read its allowed input and produce only its owned output
   (plus the implementer's authorized project edits). Use the current role schema,
   not an old task artifact as a template. Keep schema definitions in the rules.
4. Run [saved-file validation](../../../agent_loop_poc/README.md#validate-actual-saved-bytes)
   on the actual output. Report the observed exit status and digest outside that
   artifact; if validation fails or did not run, stop handoff. Validation success
   alone does not authorize progress.
5. When the validated implementer output hands off to reviewer, prepare the
   byte-identical canonical review mirrors before reviewer input capture. Then
   recheck routing. For other handoffs, recheck routing directly after validation.

## Recover and report

- Correct only the current producer's own in-scope mistake. An upstream problem
  returns to its responsible producer; downstream stages must not patch upstream
  artifacts. Respect task retry limits.
- On changed inputs, reread and reproduce the affected stage and descendants with
  fresh metadata. Replacing only hashes cannot make old work current. Regeneration
  does not authorize repeating external side effects; follow the task's recovery.
- Preserve blockers and user decisions. Report missing evidence as such, and stop
  where scope, authority, or required isolation is unresolved.
- Report the outcome, actual execution mode, observed checks, cleanup, and remaining
  limitations. Controller completion is structural and declared-result evidence;
  it does not prove semantic fidelity, truthful command execution, or skill efficacy.
