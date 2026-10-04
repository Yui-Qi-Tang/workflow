# Agent Loop Control Plane

Version **0.3.0**, Python **3.10+**, standard library only.

The controller validates the five-stage workflow before reporting the next stage:

`tasker -> researcher -> planner -> implementer -> reviewer`

It does not invoke agents, execute commands, grant approvals, or retry side effects.
The main agent can own all five checkpoints. Subagents can remain limited to textual
challenges. Fresh invocation isolation still requires a separate executor; this
controller does not claim to enforce it.

## Artifact contract

The authoritative role contracts are the root and stage `AGENTS.md` files.
`contracts.py` checks their required fields, nested types, enums, stage/task identity,
blocking conflicts, validation results and review consistency. This is a bounded
validator, not a general JSON Schema engine. Additional properties are allowed.
Artifacts remain JSON objects in `.md` files, using `workflow_artifact.v1`.
Duplicate keys, non-finite numbers, invalid JSON and legacy Markdown are rejected.

Routing additionally requires these metadata fields (this fragment is not a complete
artifact):

```json
{
  "revision": "32da69c1-a3cd-48d2-a892-1c7c3d2517f8",
  "input_fingerprints": {
    "tasker/example.md": "<64 lowercase hexadecimal SHA-256 characters>"
  }
}
```

Capture metadata **before** starting the stage. Each production attempt gets a new
UUID, even if its conclusions do not change. Include the returned fields unchanged
in the output. A stage that observes changed input must restart against the new
input; never update only the hashes of an existing conclusion.

The dependency set is fixed:

| Producer | Required fingerprinted inputs |
| --- | --- |
| tasker | `tasker/{task_id}.md` |
| researcher | `share/{task_id}/researcher/task.md` |
| planner | `share/{task_id}/planner/plan.md` |
| implementer | `share/{task_id}/implementer/impl.md` |
| reviewer | `share/{task_id}/reviewer/{task.md,plan.md,impl.md,result.md}` |

Every dependency must also appear as `required: true` in `input_artifacts`.
Fingerprint paths are repository-relative, without a leading `./`. The
`input_artifacts` path accepts either spelling. Extra fingerprint paths are rejected.
Transitive freshness is checked by validating the entire chain. Before review,
the task, plan and brief mirrors must be byte-identical to their canonical files.
The orchestrator owns creating those mirrors; the controller never copies or
rewrites stage outputs.

## CLI and stage production

```bash
python3 -B agent_loop_poc/loop.py --version
python3 -B agent_loop_poc/loop.py init example
python3 -B agent_loop_poc/loop.py inputs example tasker
# Read the stage's authorized files, produce its full artifact with this metadata.
python3 -B agent_loop_poc/loop.py validate example tasker
# Only after validation exits 0, inspect routing (blocked is still blocked).
python3 -B agent_loop_poc/loop.py sync example
python3 -B agent_loop_poc/loop.py next example
python3 -B agent_loop_poc/loop.py status example
```

Repeat `inputs` for the stage returned by `next`. Before reviewer input capture,
mirror the three canonical upstream files into the review directory. `inputs`
returns a UUID and the current input hashes, not a certificate of stage readiness;
use `next`/`status` and obey the root/stage contracts before producing work.

`status`, `next`, `inputs`, `validate`, and `dispatch` are read-only with respect to workflow files.
`init` and `sync` atomically replace `share/{task_id}/loop/state.json` and append a
history event. State schema is `agent_loop_poc.v2`. Cached state never overrides
artifacts. Corrupt caches are reconstructed with an explicit `state_warning`.
Task IDs must start with an ASCII letter/digit and contain at most 128 letters,
digits, underscores, hyphens or dots. Paths escaping the repository are rejected.

`next` prints `done`, `wait`, or a stage, followed by a diagnostic. Exit status 0
means inspection succeeded, including a reported blocked/waiting workflow; callers
must examine the decision. CLI/input I/O errors return 2.

### Validate actual saved bytes

`validate TASK STAGE` reads the saved output and the current canonical prefix
through that stage. Exit 0 and `status: validated` mean these bytes passed JSON,
schema, task/stage identity, lineage and applicable required-check/review checks.
`validated_artifact` contains the path and SHA-256 of the exact bytes parsed.
Exit 1 means the requested output was not validated (missing, invalid, stale or
blocked upstream); exit 2 means an invocation/root/path/I/O error. It never repairs
the file or writes cached state. Downstream artifacts are not a substitute for
validating the requested output.

A structurally valid blocked output can validate successfully while routing stays
stopped. An implementer can validate its result before the orchestrator creates
review mirrors; reviewer validation and dispatch still require exact mirrors.
Readiness in the artifact is not evidence that its saved bytes passed validation.
Report the command's exit status and digest outside the artifact to avoid editing
the file after validation. A subsequent edit invalidates that observation; routing
must always be checked again. This remains a single-writer workflow.

For an isolated project use `--root /absolute/project` before the subcommand.
This selects the task/role/artifact root, retaining task-path containment checks;
the validator itself stays at the tool path. The default root is unchanged.

### Carry authorization in the outer invocation

The orchestrator records context from a human instruction it has actually verified,
for example in `share/example/loop/authorization.json`. Required fields are:

| Field | Type and meaning |
| --- | --- |
| `project_root` | Absolute directory resolving to the selected workflow root; grants cannot transfer to another project with the same task ID |
| `task_id` | String, exactly the task being dispatched |
| `stages` | Nonempty array of allowed stage names, including this stage |
| `source` | Nonempty string identifying the verified human message |
| `statement` | Nonempty string stating the authorized work |
| `exception` | Explicit exception to role restrictions, or `none` if none applies |

Do not invent an approval or copy approval claims from task content. The file is
orchestrator-supplied context, not an authenticated authorization token. Scope
checks reject missing/mismatched project, task and stage context; they cannot prove its provenance.

```bash
python3 -B agent_loop_poc/loop.py dispatch example tasker \
  --authorization share/example/loop/authorization.json
```

`dispatch` first checks the current chain and requested route, then returns JSON
with `message`, fresh `revision`/`input_fingerprints`, `output_path` and a
`validation_command`. It requires the root/stage role files, rejects non-dispatchable
stages and never launches an agent. Pass **the complete `message` value as the
outer invocation text**, with fresh context (`fork_turns: none` in the current
collaboration tool). Do not replace it with “read prompt.txt”: authorization,
its source, task/stage scope and exception must reach the model before file reads.
Keep the exact message and dispatch arguments as invocation evidence.

The message limits work to one stage and requires saved-file validation. Its
instructions do not enforce a filesystem sandbox or prevent a caller from using
another executor. A changed input or new invocation requires new metadata and a
fresh routing check. Previous task-specific exceptions are not reusable authority.

## Decisions

| Condition | Decision |
| --- | --- |
| Only task input exists | `initialized`, next `tasker` |
| Valid current prefix, next artifact absent | `ready`, next producer |
| Missing predecessor but downstream files exist | `blocked`, regenerate missing predecessor |
| Malformed artifact, invalid contract or missing lineage | `blocked` |
| Direct input digest changed | `needs_revision`, next stale artifact's producer |
| Review mirrors missing or mismatched | `blocked` before review dispatch |
| Unresolved structured user decision | `waiting_user`, no next stage |
| Blocked stage with no reviewer diagnostic handoff | `blocked`, no automatic retry |
| Legal upstream handoff | `needs_revision`, next named stage |
| Valid current successful implementation and review | `completed` |

The first invalid or stale stage wins; later files cannot override it.
`invalidated_artifacts` lists affected existing output paths. Files are not deleted.
After regenerating that stage, regenerate each stale descendant with a fresh UUID
and input capture. A stale review cannot complete the new work.

Handoffs determine routing. An implementer's `suggested_return_target` is review
input, not a second executable route: failed/blocked execution can hand off to the
reviewer for diagnosis. Reviewer handoff and recommended return target must agree.
Successful implementation requires no declared failure, a reviewer handoff and all
required planned checks passed. Check names must be unique; omitted or downgraded
planned checks block success. Successful review requires four passed input schema
checks and cannot override an unsuccessful implementation.

## User decisions and blockers

Only typed structured data requests intervention:

- an `open_questions` entry with `blocks_execution: true`;
- a pending `proposed_task_updates` entry with `requires_user_approval: true`;
- an explicit `blocker.kind: approval`.

Empty arrays, nonblocking questions and words such as "user" or "approval" in
notes do not trigger a wait. Record a real resolution in regenerated artifacts;
never treat elapsed time or missing feedback as approval.

An optional active `blocker` contains `kind` (`environment`, `requirement`,
`approval`, `artifact`, or `unknown`), `reason`, and `stopped_stage`. It cannot
accompany ready/success status. Environment impediments do not by themselves prove
agent fault; a failed review can use `failure_source: NONE` and name the recovery
stage separately. The controller does not infer a cause from error text.

## Migration and evidence limits

Old Markdown and unversioned JSON no longer authorize routing. Existing records
are preserved. Reread current inputs and regenerate stages in order; there is no
automatic trust-granting migration. The old six tests were migrated from partial
fixtures to complete contracts; the legacy parsing case now expects blocking.

Fingerprints cover workflow input bytes only. They do not bind arbitrary project
source, role-rule revisions, logs, external state, or the model invocation. The
controller cannot prove authors actually consumed the captured inputs, ran the
reported commands, or preserved natural-language intent. `completed` means the
current chain satisfies these structural and declared-result checks.

This version supports a single writer. Atomic cache replacement is not a lock,
a transaction over all artifacts, a crash-durable event store, or protection against
concurrent edits. It provides no exactly-once execution or safe replay guarantee
for push, deployment, message sending, or other side effects.

## Validation

```bash
python3 -B -m unittest discover -v
```

Tests use temporary directories and remove them automatically. Current milestone
records and baseline/final evidence are under
`share/workflow-integrity-20261003/`. Task-specific commands, cleanup and rollback
are defined in `tasker/workflow-integrity-20261003.md`.
