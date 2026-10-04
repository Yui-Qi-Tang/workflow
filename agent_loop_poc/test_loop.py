from __future__ import annotations

import contextlib
import io
import json
import tempfile
import unittest
from unittest.mock import patch

from agent_loop_poc import loop
from agent_loop_poc.test_integrity import WorkflowFixture


class LoopRoutingTests(WorkflowFixture):
    """Original routing scenarios, migrated to complete current input bundles."""

    def test_json_review_success_completes_workflow(self):
        self.chain()
        state = loop.sync_command(self.task)
        self.assertEqual(state["status"], "completed")
        self.assertIsNone(state["next_stage"])
        self.assertEqual(state["current_stage"], "reviewer")

    def test_json_review_failed_routes_to_return_target(self):
        self.chain()
        self.save("reviewer", self.artifact("reviewer", status="failed", overall_judgment="failed", failure_source="tasker", recommended_return_target="tasker", handoff={"next_agent": "tasker", "allowed_next_inputs": [], "notes": ""}))
        state = loop.sync_command(self.task)
        self.assertEqual(state["status"], "needs_revision")
        self.assertEqual(state["next_stage"], "tasker")

    def test_json_result_failure_routes_to_explicit_handoff(self):
        self.chain("planner")
        self.save("implementer", self.artifact("implementer", status="failed", failure_type="plan_mismatch", suggested_return_target="planner", handoff={"next_agent": "planner", "allowed_next_inputs": [], "notes": ""}))
        state = loop.sync_command(self.task)
        self.assertEqual(state["status"], "needs_revision")
        self.assertEqual(state["next_stage"], "planner")

    def test_legacy_markdown_review_labels_cannot_authorize_routing(self):
        self.chain()
        self.write(self.base + "reviewer/review.md", "Overall Judgment: success\nRecommended Return Target: NONE\n")
        self.assertEqual(self.state()["status"], "blocked")

    def test_valid_json_does_not_fall_back_to_embedded_markdown(self):
        self.chain()
        review = self.artifact("reviewer", notes=["Overall Judgment: success"])
        del review["overall_judgment"]
        self.save("reviewer", review)
        self.assertEqual(self.state()["status"], "blocked")

    def test_blocked_json_intermediate_artifact_stops_next_stage(self):
        self.save("tasker", self.artifact("tasker", status="blocked", open_questions=[{"id": "q", "question": "Need decision", "blocks_execution": True, "reason": "Undefined requirement"}], handoff={"next_agent": "NONE", "allowed_next_inputs": [], "notes": ""}))
        state = loop.sync_command(self.task)
        self.assertEqual(state["status"], "waiting_user")
        self.assertIsNone(state["next_stage"])

    def test_status_and_next_do_not_create_or_change_state(self):
        self.chain()
        for cache_exists in (False, True):
            if cache_exists:
                loop.sync_command(self.task)
            before = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
            for command, expected in (("status", "status=completed"), ("next", "done")):
                with contextlib.redirect_stdout(io.StringIO()) as output:
                    self.assertEqual(loop.main([command, self.task]), 0)
                self.assertIn(expected, output.getvalue())
            self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()})

    def test_inputs_snapshot_is_read_only_and_matches_required_files(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            self.assertEqual(loop.main(["inputs", self.task, "tasker"]), 0)
        metadata = json.loads(output.getvalue())
        self.assertEqual(metadata["input_fingerprints"], self.artifact("tasker")["input_fingerprints"])
        self.assertTrue(metadata["revision"])
        self.assertFalse((self.root / "share").exists())

    def test_cached_completed_state_does_not_override_artifacts(self):
        self.chain()
        loop.sync_command(self.task)
        self.write("tasker/case.md", "Changed")
        self.assertEqual(loop.sync_command(self.task)["status"], "needs_revision")

    def test_corrupt_cache_is_rebuilt_and_reported(self):
        self.chain()
        self.write(self.base + "loop/state.json", "broken")
        state = loop.sync_command(self.task)
        self.assertEqual(state["status"], "completed")
        self.assertIn("state_warning", state)

    def test_atomic_write_failure_preserves_previous_cache(self):
        self.chain()
        loop.sync_command(self.task)
        path = loop.build_paths(self.task).state_file
        previous = path.read_bytes()
        with patch.object(loop.os, "replace", side_effect=OSError("simulated interrupted replace")):
            with self.assertRaises(OSError):
                loop.sync_command(self.task)
        self.assertEqual(path.read_bytes(), previous)
        self.assertEqual(list(path.parent.glob(".state-*")), [])

    def test_bad_task_cli_reports_error(self):
        with contextlib.redirect_stderr(io.StringIO()) as output:
            self.assertEqual(loop.main(["status", "../other"]), 2)
        self.assertIn("task_id", output.getvalue())

    def test_symlink_cannot_redirect_workflow_outside_root(self):
        with tempfile.TemporaryDirectory() as external:
            (self.root / "share").symlink_to(external, target_is_directory=True)
            with self.assertRaises(ValueError):
                loop.build_paths(self.task)


if __name__ == "__main__":
    unittest.main()
