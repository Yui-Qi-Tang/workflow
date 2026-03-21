# Workflow README

This repository simulates a staged AI-agent workflow:

`tasker -> researcher -> planner -> implementer -> reviewer`

Workflow rules still come from the `AGENTS.md` files.
This document is the English version for sharing the workflow, writing tasks,
and asking the agent to split work safely.

## Folder Map

- `tasker/{task_id}.md`: user-facing task input
- `share/{task_id}/researcher/task.md`: normalized task spec
- `share/{task_id}/planner/plan.md`: high-level execution plan
- `share/{task_id}/implementer/impl.md`: implementation handoff
- `share/{task_id}/reviewer/{task.md,plan.md,impl.md,result.md,review.md}`: self-contained review bundle
- `share/{task_id}/loop/`: optional loop-state and follow-up artifacts when a task needs iteration

## How To Write `task.md`

The best `task.md` files are explicit about what must happen, what must not
happen, and how success will be checked.

Required fields in this workflow are:

- `task_id`
- `goal`
- `scope`
- `constraints`
- `deliverables`
- `acceptance_criteria`
- `open_questions`

A good task usually also includes:

- `source_of_truth`
- `validation`
- `rollback / cleanup`
- `notes`

Use this as a practical template:

```md
# Goal
- What outcome do you want?

# Scope
- What files, systems, or documents are in scope?

# Source Of Truth
- Which files, pages, tickets, or examples should be treated as authoritative?

# Constraints
- What must not change?
- What must be preserved?
- What should not be inferred or invented?

# Deliverables
- What artifact should be produced?
- What format should it have?

# Validation
- What checks must pass?

# Acceptance Criteria
- What does success look like?

# Rollback / Cleanup
- What temporary files, test outputs, or scratch artifacts should be removed?
- What should be kept?

# Open Questions
- Anything that must be clarified before implementation?
```

Practical rule:

- If a decision would affect implementation, validation, scope, or cleanup,
  put it in `task.md` instead of asking later agents to guess.

## Agent Responsibilities

| Agent | Responsibility | Boundary |
| --- | --- | --- |
| `tasker` | Normalize the raw request into a bounded task spec. | Must stop on conflicts and must not invent missing requirements. |
| `researcher` | Restate the task, classify it, surface risks, and identify likely failure modes. | Must not write code or relax constraints. |
| `planner` | Turn the task into ordered implementation steps, invariants, checks, and escalation rules. | Must not hide upstream gaps or produce vague guidance. |
| `implementer` | Execute conservatively, validate, and record what changed. | Must not expand scope or silently rewrite the plan. |
| `reviewer` | Judge success, identify the earliest likely failure source, and point the loop back correctly. | Must not fix code or invent evidence. |

## How To Ask Me To Split Tasks

If you want me to split a large request into smaller pieces, be explicit about:

- the desired final outcome
- the sources I should trust
- the parts that can be done in parallel
- the parts that must stay serialized
- the validation you care about

Good prompts look like this:

```text
Please split this request into parallelizable subtasks.
Tell me which parts will conflict on files and which parts can be done independently.
If validation, cleanup, or rollback is incomplete, please propose a task update first.
```

Even better, ask me to produce the task file first:

```text
Please turn this request into task.md first, including goal / scope /
constraints / deliverables / acceptance_criteria / open_questions.
If there is a conflict, stop and list the conflict points instead of filling gaps.
```

How this helps:

- I can break the request into independently executable chunks.
- I can warn you early when a requirement is underspecified.
- I can propose the cleanest loop boundary before implementation starts.

## Agent Loop Example

The basic loop is:

`tasker -> researcher -> planner -> implementer -> reviewer`

A concrete iteration looks like this:

1. You describe the task and I turn it into `tasker/{task_id}.md`.
2. `tasker` normalizes the request into `share/{task_id}/researcher/task.md`.
3. `researcher` preserves intent, identifies risks, and restates the task.
4. `planner` turns the restated task into an implementation plan.
5. `implementer` executes the plan and writes the result artifact.
6. `reviewer` decides whether the workflow succeeded.
7. If the workflow failed, the reviewer points to the earliest likely source.

The repo also contains a lightweight loop POC:

- `agent_loop_poc/README.md`

Example commands:

```bash
python3 agent_loop_poc/loop.py init 24
python3 agent_loop_poc/loop.py sync 24
python3 agent_loop_poc/loop.py next 24
python3 agent_loop_poc/loop.py status 24
```

Good loop behavior is:

- stop early when the upstream definition is broken
- return to the earliest stage that actually caused the mismatch
- keep review bundles self-contained
- preserve the original task intent while refining the execution path

## What A Good Task Loop Looks Like

We have already used this workflow in two useful patterns:

- A contract-mismatch task, where the loop had to stop at definition time
  before implementation could continue.
- A source-synthesis task, where the loop extracted facts from multiple pages,
  separated direct findings from supporting signals, and kept inference explicit.

Those examples show the intended style:

- be explicit about the source of truth
- keep the downstream agents narrow and bounded
- do not let implementation guess what the task meant
- make the reviewer able to explain the failure source, not just the failure

## [Review] Underused Ways To Use This Workflow

These are valid ways to use me that you may not have fully exploited yet.
I am marking them for review so you can decide whether they are useful.

- `[Review]` Ask me to draft `task.md` from a rough idea plus a few source files, then ask me to stop if the task is conflicted or underspecified.
- `[Review]` Ask me to split one big task into multiple smaller tasks with clear file ownership before any implementation starts.
- `[Review]` Ask me to produce a task-update proposal when I detect missing validation, cleanup, rollback, or reporting requirements.
- `[Review]` Ask me to write the loop boundary and escalation rules first, then implement only inside that boundary.
- `[Review]` Ask me to act as a contract reviewer, where I compare two artifacts and identify the earliest upstream stage that lost intent.
- `[Review]` Ask me to produce a self-contained review bundle, not just the final answer, so the next stage can read from files instead of chat memory.
- `[Review]` Ask me to create a reusable loop-state artifact when a task needs repeated iteration.

## Rules That Keep The Workflow Healthy

- Put the authoritative task content in `tasker/{task_id}.md`.
- Keep the review bundle self-contained before the reviewer starts.
- Do not rely on chat memory between stages.
- Do not invent validation if the task did not define it.
- Do not silently relax constraints to make implementation easier.
- If a task needs a rule change, update the task first and then rerun the pipeline.

## Where To Look Next

- Workflow rules: `./AGENTS.md`
- Stage-specific rules: `./tasker/AGENTS.md`, `./researcher/AGENTS.md`, `./planner/AGENTS.md`, `./implementer/AGENTS.md`, `./reviewer/AGENTS.md`
- Loop POC: `./agent_loop_poc/README.md`

