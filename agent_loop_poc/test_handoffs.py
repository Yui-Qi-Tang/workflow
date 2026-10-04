"""Saved-file and outer-authorization regressions from the Luna pilot."""

from __future__ import annotations

import contextlib
import hashlib
import io
import json
import shlex
import subprocess
import sys
import tempfile
from pathlib import Path

from agent_loop_poc import loop
from agent_loop_poc.test_integrity import WorkflowFixture


class SavedHandoffTests(WorkflowFixture):
    def cli(self, *args):
        with contextlib.redirect_stdout(io.StringIO()) as out, contextlib.redirect_stderr(io.StringIO()) as err:
            code = loop.main(list(args))
        return code, out.getvalue(), err.getvalue()

    def inventory(self):
        return {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}

    def test_saved_bytes_validated_with_digest_without_mutation(self):
        self.chain("planner")
        path = loop.build_paths(self.task).implementer_impl
        # A digest must describe the original bytes, including CRLF line endings.
        path.write_bytes(path.read_bytes().replace(b"\n", b"\r\n"))
        before = self.inventory()
        code, output, _ = self.cli("validate", self.task, "planner")
        self.assertEqual(code, 0)
        result = json.loads(output)
        self.assertEqual(result["status"], "validated")
        self.assertEqual(result["validated_artifact"]["sha256"], hashlib.sha256(path.read_bytes()).hexdigest())
        self.assertEqual(before, self.inventory())

    def test_literal_backslash_n_in_saved_ready_artifact_is_rejected(self):
        self.chain("researcher")
        path = loop.build_paths(self.task).planner_plan
        path.write_text(path.read_text().replace("\n", r"\n"))
        before = path.read_bytes()
        code, output, _ = self.cli("validate", self.task, "researcher")
        self.assertEqual(code, 1)
        self.assertEqual(json.loads(output)["reason_code"], "artifact_invalid")
        self.assertEqual(before, path.read_bytes())

    def test_planner_summary_requirements_must_be_string_array(self):
        self.chain("planner")
        data = self.artifact("planner")
        for invalid in ("Report checks", [True], {"item": "Report checks"}):
            with self.subTest(value=invalid):
                data["expected_output"]["implementation_summary_requirements"] = invalid
                self.save("planner", data)
                code, output, _ = self.cli("validate", self.task, "planner")
                self.assertEqual(code, 1)
                self.assertIn("implementation_summary_requirements", json.loads(output)["reason"])
        data["expected_output"]["implementation_summary_requirements"] = ["Report checks"]
        self.save("planner", data)
        self.assertEqual(self.cli("validate", self.task, "planner")[0], 0)

    def test_missing_output_is_not_validation_success(self):
        self.assertEqual(self.cli("validate", self.task, "tasker")[0], 1)

    def test_validation_rereads_file_after_previous_success(self):
        self.chain("tasker")
        self.assertEqual(self.cli("validate", self.task, "tasker")[0], 0)
        self.write(self.base + "researcher/task.md", "broken")
        self.assertEqual(self.cli("validate", self.task, "tasker")[0], 1)

    def test_stale_upstream_blocks_target_even_when_direct_input_is_current(self):
        self.chain("planner")
        self.write("tasker/case.md", "New requirements")
        code, output, _ = self.cli("validate", self.task, "planner")
        self.assertEqual(code, 1)
        self.assertEqual(json.loads(output)["reason_code"], "input_changed")

    def test_valid_blocked_target_does_not_authorize_downstream(self):
        blocked = self.artifact("tasker", status="blocked", handoff={"next_agent": "NONE", "allowed_next_inputs": [], "notes": "Conflict"})
        self.save("tasker", blocked)
        self.assertEqual(self.cli("validate", self.task, "tasker")[0], 0)
        self.assertEqual(self.state()["status"], "blocked")
        self.save("researcher", self.artifact("researcher"))
        self.assertEqual(self.cli("validate", self.task, "researcher")[0], 1)

    def test_implementer_validation_does_not_require_future_review_mirrors(self):
        self.chain("implementer")
        self.assertEqual(self.cli("validate", self.task, "implementer")[0], 0)
        self.assertEqual(self.state()["reason_code"], "review_bundle_invalid")

    def test_required_planned_check_cannot_be_omitted(self):
        self.chain("planner")
        data = self.artifact("planner")
        data["validation_plan"] = [{"check": "required_probe", "command_or_method": "run probe", "expected_result": "pass", "required": True}]
        self.save("planner", data)
        self.save("implementer", self.artifact("implementer"))
        code, output, _ = self.cli("validate", self.task, "implementer")
        self.assertEqual(code, 1)
        self.assertEqual(json.loads(output)["reason_code"], "required_validation_missing")

    def test_review_success_cannot_override_failed_implementation(self):
        self.chain("planner")
        self.save("implementer", self.artifact("implementer", status="failed", failure_type="implementation_error"))
        self.mirrors()
        self.save("reviewer", self.artifact("reviewer"))
        code, output, _ = self.cli("validate", self.task, "reviewer")
        self.assertEqual(code, 1)
        self.assertEqual(json.loads(output)["reason_code"], "inconsistent_success")

    def test_review_mirror_tampering_is_rejected(self):
        self.chain()
        self.write(self.base + "reviewer/task.md", "tampered")
        self.assertEqual(self.cli("validate", self.task, "reviewer")[0], 1)

    def test_subprocess_cli_uses_explicit_root_and_real_exit_codes(self):
        self.chain("tasker")
        args = [sys.executable, "-B", str(Path(loop.__file__).resolve()), "--root", str(self.root), "validate", self.task, "tasker"]
        first = subprocess.run(args, capture_output=True, text=True)
        self.assertEqual(first.returncode, 0, first.stderr)
        self.write(self.base + "researcher/task.md", r'{\n"status":"ready"}')
        second = subprocess.run(args, capture_output=True, text=True)
        self.assertEqual(second.returncode, 1, second.stderr)


class OuterDispatchTests(WorkflowFixture):
    def setUp(self):
        super().setUp()
        self.write("AGENTS.md", "Root test rules")
        for stage in loop.STAGES:
            self.write(f"{stage}/AGENTS.md", f"{stage} test rules")
        self.authorization = {
            "project_root": str(self.root),
            "task_id": self.task, "stages": ["tasker"],
            "source": "unit-test synthetic message, not actual user permission",
            "statement": "Execute only the test task stage.",
            "exception": "For this test task only, allow stage execution despite the opposition-only role restriction.",
        }

    def dispatch(self, stage="tasker", authorization=None):
        return loop.build_dispatch(loop.build_paths(self.task), stage, self.authorization if authorization is None else authorization)

    def test_entire_authorization_is_in_outer_message_before_file_reads(self):
        packet = self.dispatch()
        message = packet["message"]
        first_read = message.index("Read the root")
        for field in ("source", "statement", "exception"):
            self.assertIn(self.authorization[field], message[:first_read])
        self.assertIn(str(self.root), message[:first_read])
        self.assertIn("stage tasker", message[:first_read])
        self.assertNotIn("read prompt.txt", message)
        self.assertIn("Do not delegate", message)

    def test_dispatch_is_read_only_and_captures_fresh_lineage(self):
        before = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        a, b = self.dispatch(), self.dispatch()
        self.assertNotEqual(a["revision"], b["revision"])
        self.assertEqual(a["input_fingerprints"], self.artifact("tasker")["input_fingerprints"])
        self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()})

    def test_missing_or_mismatched_authorization_is_rejected(self):
        variants = [{}, {**self.authorization, "task_id": "other"}, {**self.authorization, "stages": ["planner"]}, {**self.authorization, "stages": "tasker"}]
        variants += [{**self.authorization, field: " "} for field in ("source", "statement", "exception")]
        for authorization in variants:
            with self.subTest(authorization=authorization), self.assertRaises(ValueError):
                self.dispatch(authorization=authorization)

    def test_authorization_cannot_transfer_between_roots_with_same_task_id(self):
        with tempfile.TemporaryDirectory() as other:
            grant = {**self.authorization, "project_root": other}
            with self.assertRaises(ValueError):
                self.dispatch(authorization=grant)

    def test_wrong_route_and_blocked_prefix_cannot_dispatch(self):
        grant = {**self.authorization, "stages": list(loop.STAGES)}
        with self.assertRaises(ValueError):
            self.dispatch("planner", grant)
        self.save("tasker", self.artifact("tasker", status="blocked", handoff={"next_agent": "NONE", "allowed_next_inputs": [], "notes": "blocked"}))
        with self.assertRaises(ValueError):
            self.dispatch("researcher", grant)

    def test_missing_role_rules_cannot_dispatch(self):
        (self.root / "tasker/AGENTS.md").unlink()
        with self.assertRaises(ValueError):
            self.dispatch()

    def test_subprocess_dispatch_message_contains_working_validation_command(self):
        auth = self.root / "authorization.json"
        auth.write_text(json.dumps(self.authorization))
        result = subprocess.run([sys.executable, "-B", str(Path(loop.__file__).resolve()), "--root", str(self.root), "dispatch", self.task, "tasker", "--authorization", str(auth)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        packet = json.loads(result.stdout)
        data = self.artifact("tasker")
        data.update(revision=packet["revision"], input_fingerprints=packet["input_fingerprints"])
        self.save("tasker", data)
        validation = subprocess.run(shlex.split(packet["validation_command"]), capture_output=True, text=True)
        self.assertEqual(validation.returncode, 0, validation.stderr)
        self.assertEqual(json.loads(validation.stdout)["status"], "validated")

    def test_invalid_authorization_file_returns_error_without_a_message(self):
        self.write("authorization.json", '{"task_id":"case"}')
        with contextlib.redirect_stdout(io.StringIO()) as out, contextlib.redirect_stderr(io.StringIO()):
            status = loop.main(["dispatch", self.task, "tasker", "--authorization", str(self.root / "authorization.json")])
        self.assertEqual(status, 2)
        self.assertEqual(out.getvalue(), "")
