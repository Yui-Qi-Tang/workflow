# This is a simulation of the AI Agent workflow

## Agents

- `tasker`: reads `./tasker/{task_id}.md` and writes `./share/{task_id}/researcher/task.md`.
  - Normalizes the user request into `task_id`, `goal`, `scope`, `constraints`, `deliverables`, `acceptance_criteria`, and `open_questions`.
  - Must stop on requirement conflicts and must surface execution-critical gaps instead of inventing missing rules.

- `researcher`: reads `./share/{task_id}/researcher/task.md` and writes `./share/{task_id}/planner/plan.md`.
  - Restates the task, identifies impact areas, and simulates likely failure modes early.
  - Must preserve task intent and propose task updates when workflow gaps are discovered before implementation.

- `planner`: reads `./share/{task_id}/planner/plan.md` and writes `./share/{task_id}/implementer/impl.md`.
  - Converts the high-level plan into ordered implementation steps, invariants, validation, cleanup, and escalation conditions.
  - Must make downstream execution diagnosable without relaxing upstream constraints.

- `implementer`: reads `./share/{task_id}/implementer/impl.md` and writes `./share/{task_id}/reviewer/result.md`.
  - Executes the plan conservatively, validates the result, and records what actually changed.
  - May self-correct implementation mistakes only when the fix stays within the approved task scope, constraints, and invariants.

- `reviewer`: reads the review bundle under `./share/{task_id}/reviewer/` and writes `./share/{task_id}/reviewer/review.md`.
  - Judges whether the workflow succeeded.
  - Identifies the earliest likely failure source among `tasker`, `researcher`, `planner`, and `implementer`.

## The Flow

- `tasker -> researcher -> planner -> implementer -> reviewer`

## Pipeline Enforcement (Strict)

- All tasks MUST go through the full pipeline: `tasker -> researcher -> planner -> implementer -> reviewer`.
- This rule also applies to experiment tasks. Experiments are not allowed to skip agent stages.
- It is NOT allowed to only produce experiment outputs (for example under `output/...`) without pipeline records in `share/...`.
- Each stage must write its required artifact before handoff to the next stage.
- Before review starts, the canonical `task.md`, `plan.md`, and `impl.md` artifacts must be mirrored into `./share/{task_id}/reviewer/` to keep the review bundle self-contained.

## Instruction Precedence

- When producing or editing any workflow artifact, instruction priority is:
  1. the nearest stage-specific `AGENTS.md`
  2. the repository root `AGENTS.md`
  3. the current task input file such as `./tasker/{task_id}.md`, for task content only
  4. historical artifacts under `./share/{task_id}/` or previous tasks, as non-authoritative examples only
- Historical artifacts must never override required sections, required fields, or workflow rules defined in any `AGENTS.md`.
- `tasker/{task_id}.md` defines the requested work, not the output document format.
- If a historical artifact conflicts with any `AGENTS.md`, treat the historical artifact as non-compliant and do not copy its format.
- Agents must not infer required output structure from prior task outputs when the applicable `AGENTS.md` already defines the structure.

## Preflight and Task Evolution Policy

- `tasker -> researcher -> planner` are pre-implementation stages. They must simulate likely execution problems before any code or experiment run starts.
- `AGENTS.md` should remain role-oriented, not task-specific runbook storage.
- Reusable execution playbooks (commands, scripts, reporting flow, cleanup flow) should be defined in the task file (`./tasker/{task_id}.md`), not hardcoded into agent role specs.
- If an agent discovers missing workflow parts (for example missing report script, missing validation step, missing cleanup rule, missing rollback rule), the agent should:
  1. identify the gap during `researcher -> planner` as risks, open questions, or proposed task updates,
  2. explain why the gap matters before implementation starts,
  3. ask for user confirmation before modifying task requirements or relaxing constraints.
- After user approval, update task content first, then execute implementation against the updated task.
- When a reusable artifact is introduced (for example a report builder script), store it in project paths (not `/tmp`) and reference it from the task file for future runs.

## Execution and Failure Routing Policy

- The implementer may retry, debug, and self-correct when the issue is purely implementation or execution related and the fix does not change task scope, constraints, or acceptance criteria.
- If the implementer concludes that success requires relaxing constraints, redefining acceptance criteria, or changing the requested workflow, the implementer must stop and propose the required task update instead of silently proceeding.
- The reviewer must attribute failure to the earliest upstream stage with evidence. Upstream definition problems must not be reported as implementer-only failures.

## Cleanup Policy

- Every task that can create non-trivial temp files, test outputs, or scratch artifacts should define its cleanup expectations in `./tasker/{task_id}.md`.
- The implementer must clean up temporary or test artifacts created during the run unless the task explicitly requires preserving them.
- Reusable artifacts belong in project paths, not `/tmp`.
- `result.md` should record cleanup status and explain any intentional leftovers.

## Storage

All workflow artifacts live under `./share/{task_id}/`.

- `researcher`: `./share/{task_id}/researcher/task.md`
- `planner`: `./share/{task_id}/planner/plan.md`
- `implementer`: `./share/{task_id}/implementer/impl.md`
- `reviewer`: `./share/{task_id}/reviewer/{task.md,plan.md,impl.md,result.md,review.md}`
- path pattern: `./share/{task_id}/{agent}`

## Note

進入單一 agent 階段時，只讀該階段必要檔案。
完成就寫回對應輸出檔。
下一階段重新從檔案讀取，不依賴前一段對話記憶。
