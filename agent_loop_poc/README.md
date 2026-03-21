# Agent Loop POC

This folder contains a minimal control plane for the existing workflow:

- `tasker -> researcher -> planner -> implementer -> reviewer`

The goal is not to replace the current markdown artifacts. Instead, the POC adds
a small machine-readable state file so a runner can decide:

- which stage should run next
- whether the task is done
- whether the workflow is blocked
- whether the workflow should return to an upstream stage
- whether human input is likely required before the next loop iteration

## Why this exists

Today the repository already has:

- stable stage responsibilities in `AGENTS.md`
- stable handoff artifacts in `share/{task_id}/...`
- reviewer outputs that often include return targets

What it lacks is a simple orchestrator that can inspect those artifacts and make
the next-step decision consistently.

## State layout

For each task, the runner stores state at:

- `share/{task_id}/loop/state.json`

The state file is intentionally small:

```json
{
  "schema_version": "agent_loop_poc.v1",
  "task_id": "24",
  "status": "needs_revision",
  "current_stage": "reviewer",
  "next_stage": "tasker",
  "last_completed_stage": "reviewer",
  "return_target": "tasker",
  "needs_user_input": true,
  "reason": "Reviewer marked the workflow failed and routed it back upstream.",
  "artifacts": {
    "tasker_input": true,
    "researcher_task": true,
    "planner_plan": true,
    "implementer_impl": true,
    "reviewer_result": true,
    "reviewer_review": true
  },
  "history": [
    {
      "event": "sync",
      "status": "needs_revision",
      "current_stage": "reviewer",
      "next_stage": "tasker"
    }
  ]
}
```

## Workflow states

- `initialized`
  - task input exists, but no downstream artifact exists yet
- `ready`
  - the next stage is known and can run now
- `running`
  - reserved for future integration with an actual agent executor
- `needs_revision`
  - a downstream artifact explicitly routed the workflow back upstream
- `waiting_user`
  - the runner believes user clarification/approval is needed before looping
- `blocked`
  - the workflow cannot continue because a required input or decision is missing
- `completed`
  - reviewer marked the workflow successful

## Transition rules

The runner uses the existing artifacts as the source of truth.

1. If `share/{task_id}/reviewer/review.md` exists:
   - `Overall Judgment: success` -> `completed`
   - `Overall Judgment: failed` -> `needs_revision` and follow `Recommended Return Target`
2. Else if `share/{task_id}/reviewer/result.md` exists:
   - `Status: success` -> `ready`, next stage `reviewer`
   - `Status: failed|partial_failure` -> follow `Suggested Return Target` if present, otherwise `blocked`
3. Else if `share/{task_id}/implementer/impl.md` exists:
   - next stage is `implementer`
4. Else if `share/{task_id}/planner/plan.md` exists:
   - next stage is `planner`
5. Else if `share/{task_id}/researcher/task.md` exists:
   - next stage is `researcher`
6. Else if `tasker/{task_id}.md` exists:
   - next stage is `tasker`
7. Otherwise:
   - `blocked`

## Human-in-the-loop heuristic

The POC does not try to fully understand markdown semantics. Instead, it uses a
simple heuristic:

- if the workflow failed and the artifacts mention phrases like `clarify`,
  `approval`, `confirm`, `user`, or `task update`, then `needs_user_input=true`
- otherwise the runner assumes the workflow can loop to the recommended stage

This is intentionally conservative and easy to replace later.

## CLI

The runner lives in:

- `agent_loop_poc/loop.py`

Supported commands:

- `python3 agent_loop_poc/loop.py init <task_id>`
- `python3 agent_loop_poc/loop.py sync <task_id>`
- `python3 agent_loop_poc/loop.py next <task_id>`
- `python3 agent_loop_poc/loop.py status <task_id>`

## Example loop

1. User creates `tasker/25.md`
2. Run `init 25`
3. Run `next 25`
   - returns `tasker`
4. After `tasker` writes `share/25/researcher/task.md`, run `sync 25`
5. Run `next 25`
   - returns `researcher`
6. Repeat until reviewer writes `review.md`
7. If reviewer says `failed` with return target `tasker`, the loop state becomes:
   - `status=needs_revision`
   - `next_stage=tasker`
   - maybe `needs_user_input=true`

## Scope limits

This is only a POC. It does not yet:

- invoke real stage agents automatically
- enforce file locking or leases
- manage retry budgets
- support parallel tasks safely
- validate markdown section schemas beyond a few key fields

Those are the next layer once this control model feels right.
