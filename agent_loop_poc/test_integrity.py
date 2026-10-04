"""Frozen behavioral cases for the integrity milestone; fixtures use real files."""

from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
import uuid
from pathlib import Path

from agent_loop_poc import loop


STAGES = ("tasker", "researcher", "planner", "implementer", "reviewer")
KINDS = ("normalized_task", "research_plan", "implementation_brief", "implementation_result", "workflow_review")
OUTPUTS = ("researcher/task.md", "planner/plan.md", "implementer/impl.md", "reviewer/result.md", "reviewer/review.md")


class WorkflowFixture(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        old_root = loop.ROOT
        self.addCleanup(setattr, loop, "ROOT", old_root)
        loop.ROOT = Path(self.temp.name)
        self.root = loop.ROOT
        self.task = "case"
        self.base = "share/case/"
        self.write("tasker/case.md", "Preserve the user requirement.\n")

    def write(self, relative, value):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(value, encoding="utf-8")

    def inputs(self, stage):
        index = STAGES.index(stage)
        if index == 0:
            return ["tasker/case.md"]
        if index < 4:
            return [self.base + OUTPUTS[index - 1]]
        return [self.base + "reviewer/" + name for name in ("task.md", "plan.md", "impl.md", "result.md")]

    def artifact(self, stage, **changes):
        index = STAGES.index(stage)
        data = {
            "schema_version": "workflow_artifact.v1", "artifact_type": KINDS[index],
            "task_id": self.task, "produced_by": stage,
            "status": "ready" if index < 3 else "success",
            "revision": str(uuid.uuid4()),
            "input_fingerprints": {p: hashlib.sha256((self.root / p).read_bytes()).hexdigest() for p in self.inputs(stage)},
            "input_artifacts": [{"path": p, "required": True, "summary": "Stage input."} for p in self.inputs(stage)],
            "trusted_sources": [{"path": "AGENTS.md", "summary": "Rules."}],
            "untrusted_inputs_seen": [], "constraints": ["Preserve requirement."],
            "open_questions": [], "evidence": [{"kind": "fixture", "source": "test", "summary": "Synthetic evidence."}],
            "handoff": {"next_agent": STAGES[index + 1] if index < 4 else "NONE", "allowed_next_inputs": [], "notes": "Fixture."},
        }
        extras = [
            dict(goal="Goal", scope=[], deliverables=[], acceptance_criteria=["Pass check"], conflicts=[], source_of_truth=[], validation=[], cleanup=[], rollback=[]),
            dict(task_classification="test", goal_restatement="Goal", requested_change_summary="Change", expected_impact_areas=[], assumptions=[], risks=[], non_goals=[], high_level_strategy=[], required_checks=[], proposed_task_updates=[], failure_modes=[]),
            dict(summary="Plan", inputs_used=[], files_likely_to_change=[], ordered_steps=[], invariants=[], validation_plan=[], cleanup_plan=[], escalation_conditions=[], rollback_hints=[], expected_output={"result_artifact_path": self.base + "reviewer/result.md", "implementation_summary_requirements": []}),
            dict(implementation_summary="Done", changed_files=[], validation_results=[{"check": "unit", "status": "passed", "evidence": "Fixture", "required": True}], cleanup_results=[], failure_type="none", failed_step="", failure_details="", suspected_cause="", suggested_return_target="NONE", notes=[]),
            dict(overall_judgment="success", failure_source="NONE", confidence="high", reason="Checks passed", recommended_return_target="NONE", recommended_next_action="Done", artifact_schema_checks=[{"artifact": kind, "status": "passed", "evidence": "Fixture"} for kind in KINDS[:4]], notes=[]),
        ]
        data.update(extras[index])
        data.update(changes)
        return data

    def save(self, stage, data):
        self.write(self.base + OUTPUTS[STAGES.index(stage)], json.dumps(data, indent=2) + "\n")

    def mirrors(self):
        for source, name in zip(OUTPUTS[:3], ("task.md", "plan.md", "impl.md")):
            self.write(self.base + "reviewer/" + name, (self.root / (self.base + source)).read_text())

    def chain(self, through="reviewer"):
        for stage in STAGES[:STAGES.index(through) + 1]:
            if stage == "reviewer":
                self.mirrors()
            self.save(stage, self.artifact(stage))

    def state(self):
        return loop.sync_state(loop.build_paths(self.task))


class IntegrityTests(WorkflowFixture):
    def test_complete_current_chain(self):
        self.chain()
        self.assertEqual(self.state()["status"], "completed")

    def test_review_without_predecessors_cannot_complete(self):
        self.write(self.base + "reviewer/review.md", '{"overall_judgment":"success"}')
        state = self.state()
        self.assertEqual(state["status"], "blocked")
        self.assertIsNone(state["next_stage"])

    def test_malformed_intermediate_never_advances(self):
        for content in ("not json", "{}", "[]", '{"status":"invented"}', 'Status: ready\n'):
            with self.subTest(content=content):
                self.write(self.base + OUTPUTS[0], content)
                self.assertEqual(self.state()["status"], "blocked")
                self.assertIsNone(self.state()["next_stage"])

    def test_empty_questions_do_not_wait(self):
        self.save("tasker", self.artifact("tasker", status="blocked", handoff={"next_agent": "NONE", "allowed_next_inputs": [], "notes": "user approval words are data"}))
        self.assertEqual(self.state()["status"], "blocked")
        self.assertFalse(self.state()["needs_user_input"])

    def test_only_blocking_questions_wait(self):
        for blocking in (False, True):
            with self.subTest(blocking=blocking):
                question = {"id": "q1", "question": "選擇目標", "blocks_execution": blocking, "reason": "Required decision"}
                self.save("tasker", self.artifact("tasker", status="blocked", open_questions=[question], handoff={"next_agent": "NONE", "allowed_next_inputs": [], "notes": ""}))
                self.assertEqual(self.state()["needs_user_input"], blocking)
                self.assertEqual(self.state()["status"], "waiting_user" if blocking else "blocked")

    def test_old_review_cannot_accept_changed_task(self):
        self.chain()
        self.write("tasker/case.md", "Changed requirement.\n")
        state = self.state()
        self.assertEqual(state["status"], "needs_revision")
        self.assertEqual(state["next_stage"], "tasker")

    def test_changed_plan_invalidates_implementation(self):
        self.chain()
        self.save("planner", self.artifact("planner", summary="Revised plan"))
        state = self.state()
        self.assertEqual(state["status"], "needs_revision")
        self.assertEqual(state["next_stage"], "implementer")

    def test_unversioned_artifact_requires_regeneration(self):
        data = self.artifact("tasker")
        del data["input_fingerprints"]
        self.save("tasker", data)
        self.assertEqual(self.state()["status"], "blocked")

    def test_wrong_task_or_stage_is_rejected(self):
        for field, value in (("task_id", "another"), ("produced_by", "reviewer"), ("artifact_type", "workflow_review"), ("schema_version", "future")):
            with self.subTest(field=field):
                self.save("tasker", self.artifact("tasker", **{field: value}))
                self.assertEqual(self.state()["status"], "blocked")

    def test_required_fields_and_nested_types(self):
        for mutation in ("missing_goal", "string_bool", "missing_evidence_source", "bad_target"):
            with self.subTest(mutation=mutation):
                data = self.artifact("tasker")
                if mutation == "missing_goal":
                    del data["goal"]
                elif mutation == "string_bool":
                    data["input_artifacts"][0]["required"] = "true"
                elif mutation == "missing_evidence_source":
                    del data["evidence"][0]["source"]
                else:
                    data["handoff"]["next_agent"] = "reviewer"
                self.save("tasker", data)
                self.assertEqual(self.state()["status"], "blocked")

    def test_duplicate_keys_and_nonfinite_json_rejected(self):
        data = json.dumps(self.artifact("tasker"))
        for text in ('{"status":"blocked",' + data[1:], data[:-1] + ',"extra":NaN}'):
            with self.subTest(text=text[:30]):
                self.write(self.base + OUTPUTS[0], text)
                self.assertEqual(self.state()["status"], "blocked")

    def test_review_mirrors_must_match(self):
        self.chain()
        self.write(self.base + "reviewer/plan.md", "{}")
        self.assertEqual(self.state()["status"], "blocked")

    def test_missing_review_bundle_blocks_review_dispatch(self):
        self.chain("implementer")
        self.assertEqual(self.state()["status"], "blocked")
        self.mirrors()
        self.assertEqual(self.state()["next_stage"], "reviewer")

    def test_success_cannot_hide_required_check_failure(self):
        self.chain("planner")
        self.save("implementer", self.artifact("implementer", validation_results=[{"check": "unit", "status": "not_run", "evidence": "Missing", "required": True}]))
        self.mirrors()
        self.save("reviewer", self.artifact("reviewer"))
        self.assertEqual(self.state()["status"], "blocked")

    def test_review_cannot_override_failed_implementation(self):
        self.chain("planner")
        self.save("implementer", self.artifact("implementer", status="failed", failure_type="implementation_error", suggested_return_target="implementer"))
        self.mirrors()
        self.save("reviewer", self.artifact("reviewer"))
        self.assertEqual(self.state()["status"], "blocked")

    def test_valid_failed_review_returns_to_planner(self):
        self.chain("implementer")
        self.mirrors()
        self.save("reviewer", self.artifact("reviewer", status="failed", overall_judgment="failed", failure_source="planner", recommended_return_target="planner", handoff={"next_agent": "planner", "allowed_next_inputs": [], "notes": ""}))
        self.assertEqual(self.state()["status"], "needs_revision")
        self.assertEqual(self.state()["next_stage"], "planner")
        self.assertFalse(self.state()["needs_user_input"])

    def test_pending_task_update_waits(self):
        self.chain("tasker")
        update = {"id": "u1", "description": "Change requirement", "reason": "Gap", "requires_user_approval": True}
        self.save("researcher", self.artifact("researcher", proposed_task_updates=[update], handoff={"next_agent": "tasker", "allowed_next_inputs": [], "notes": ""}))
        self.assertEqual(self.state()["status"], "waiting_user")
        self.assertIsNone(self.state()["next_stage"])

    def test_structured_environment_blocker_is_not_agent_blame(self):
        blocker = {"kind": "environment", "reason": "Dependency unavailable", "stopped_stage": "tasker"}
        self.save("tasker", self.artifact("tasker", status="blocked", blocker=blocker, handoff={"next_agent": "NONE", "allowed_next_inputs": [], "notes": ""}))
        self.assertEqual(self.state()["blocker"], blocker)
        self.assertFalse(self.state()["needs_user_input"])

    def test_task_id_cannot_escape_repository(self):
        for task_id in ("../other", "/tmp/other", "a/b", "", ".", ".."):
            with self.subTest(task_id=task_id):
                with self.assertRaises(ValueError):
                    loop.build_paths(task_id)

    def test_sync_does_not_modify_stage_artifacts(self):
        self.chain()
        before = {p: p.read_bytes() for p in self.root.rglob("*.md")}
        loop.sync_command(self.task)
        self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob("*.md")})

    def test_required_planned_checks_cannot_be_omitted_or_downgraded(self):
        self.chain("researcher")
        plan = [{"check": "must_run", "required": True, "command_or_method": "check", "expected_result": "pass"}]
        self.save("planner", self.artifact("planner", validation_plan=plan))
        for results in ([], [{"check": "must_run", "required": False, "status": "passed", "evidence": "Fixture"}]):
            with self.subTest(results=results):
                self.save("implementer", self.artifact("implementer", validation_results=results))
                self.mirrors()
                self.save("reviewer", self.artifact("reviewer"))
                self.assertEqual(self.state()["status"], "blocked")

    def test_blocked_implementation_can_be_reviewed_but_not_passed(self):
        self.chain("planner")
        self.save("implementer", self.artifact("implementer", status="blocked", failure_type="unknown", suggested_return_target="implementer"))
        self.mirrors()
        self.assertEqual(self.state()["next_stage"], "reviewer")
        self.save("reviewer", self.artifact("reviewer", status="failed", overall_judgment="failed", failure_source="NONE", recommended_return_target="implementer", handoff={"next_agent": "implementer", "allowed_next_inputs": [], "notes": ""}))
        self.assertEqual(self.state()["next_stage"], "implementer")

    def test_repaired_consumer_does_not_reuse_old_review(self):
        self.chain()
        self.save("implementer", self.artifact("implementer", implementation_summary="New execution"))
        self.assertEqual(self.state()["next_stage"], "reviewer")
        self.assertEqual(self.state()["status"], "needs_revision")
        self.save("reviewer", self.artifact("reviewer"))
        self.assertEqual(self.state()["status"], "completed")

    def test_malformed_nested_fields_in_each_stage(self):
        cases = (
            ("tasker", "conflicts", [{"id": "c", "description": "x", "source_excerpt": "x", "blocks_execution": "false"}]),
            ("researcher", "risks", [{"id": "r", "description": "x", "impact": "x"}]),
            ("planner", "ordered_steps", [{"step": True, "action": "x", "rationale": "x", "expected_evidence": "x"}]),
            ("implementer", "changed_files", [{"path": "x", "summary": "x"}]),
            ("reviewer", "artifact_schema_checks", [{"artifact": "normalized_task", "status": "not_run", "evidence": "x"}]),
        )
        for stage, field, value in cases:
            with self.subTest(stage=stage):
                self.chain()
                self.save(stage, self.artifact(stage, **{field: value}))
                self.assertEqual(self.state()["status"], "blocked")

    def test_overflow_json_number_is_not_finite(self):
        text = json.dumps(self.artifact("tasker"))
        self.write(self.base + OUTPUTS[0], text[:-1] + ',"extra":1e999}')
        self.assertEqual(self.state()["status"], "blocked")

    def test_conflicting_review_targets_are_rejected(self):
        self.chain()
        self.save("reviewer", self.artifact("reviewer", status="failed", overall_judgment="failed", recommended_return_target="planner"))
        self.assertEqual(self.state()["status"], "blocked")

    def test_fingerprint_inputs_cannot_point_to_other_tasks(self):
        data = self.artifact("tasker", input_fingerprints={"tasker/other.md": "0" * 64})
        self.save("tasker", data)
        self.assertEqual(self.state()["status"], "blocked")

    def test_no_task_input_cannot_complete(self):
        self.chain()
        (self.root / "tasker/case.md").unlink()
        self.assertEqual(self.state()["status"], "blocked")

    def test_each_missing_predecessor_blocks_old_success(self):
        for output in OUTPUTS[:4]:
            with self.subTest(output=output):
                self.chain()
                (self.root / (self.base + output)).unlink()
                self.assertEqual(self.state()["status"], "blocked")
                self.assertIsNone(self.state()["next_stage"])

    def test_each_changed_handoff_invalidates_its_consumer(self):
        for producer, consumer in zip(STAGES[:4], STAGES[1:]):
            with self.subTest(producer=producer):
                self.chain()
                self.save(producer, self.artifact(producer))
                state = self.state()
                self.assertEqual(state["status"], "needs_revision")
                self.assertEqual(state["next_stage"], consumer)

    def test_duplicate_check_names_cannot_substitute_for_each_other(self):
        self.chain("researcher")
        check = {"check": "same_name", "required": True, "command_or_method": "first", "expected_result": "pass"}
        self.save("planner", self.artifact("planner", validation_plan=[check, dict(check, command_or_method="second")]))
        self.assertEqual(self.state()["status"], "blocked")
        self.save("planner", self.artifact("planner"))
        result = {"check": "same_name", "required": True, "status": "passed", "evidence": "Fixture"}
        self.save("implementer", self.artifact("implementer", validation_results=[result, result]))
        self.assertEqual(self.state()["status"], "blocked")

    def test_success_cannot_carry_active_blocker(self):
        self.chain("planner")
        self.save("implementer", self.artifact("implementer", blocker={"kind": "environment", "stopped_stage": "implementer", "reason": "No dependencies"}))
        self.assertEqual(self.state()["status"], "blocked")

    def test_directory_cannot_stand_in_for_artifact(self):
        (self.root / (self.base + OUTPUTS[0])).mkdir(parents=True)
        self.assertEqual(self.state()["status"], "blocked")


if __name__ == "__main__":
    unittest.main()
