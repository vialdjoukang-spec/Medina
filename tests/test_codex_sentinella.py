"""Codex_Sentinella tests: issue deduplication and fragment audit gates."""
import importlib.util
import io
import json
from pathlib import Path
from contextlib import redirect_stdout
import sys
import tempfile
import unittest
from unittest import mock


TOOLS = Path(__file__).resolve().parents[1] / "tools"
SPEC = importlib.util.spec_from_file_location("codex_sentinella", TOOLS / "codex_sentinella.py")
sys.path.insert(0, str(TOOLS))
try:
    SENTINELLA = importlib.util.module_from_spec(SPEC)
    SPEC.loader.exec_module(SENTINELLA)
finally:
    sys.path.remove(str(TOOLS))


SHA = "a" * 40


class SentinellaTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.state = Path(self.temporary.name) / "state"
        self.state.mkdir()
        self.candidate = {
            "commit": SHA,
            "refs": ["refs/heads/claude/new-delivery"],
            "scopes": [{"fragment_label": "P-02-Pneumologie"}],
            "delivery_paths": ["livraisons/Livraison Claude/P-02-Pneumologie/RAPPORT.md"],
            "currently_advertised": True,
            "reachable_from_integration": False,
        }

    def scan(self, *_args):
        (self.state / "queue.json").write_text(json.dumps({"candidates": [self.candidate]}))
        return {"status": "ok", "error": None}

    def test_order_requires_full_fragment_and_coordinator_decision(self):
        order = SENTINELLA._candidate_order(self.candidate)
        self.assertEqual(order["sha"], SHA)
        self.assertEqual(order["fragments_suggested"], ["P-02-Pneumologie"])
        self.assertEqual(order["gates"]["fragment_entier_auto_revu"], "not_verified")
        self.assertEqual(order["gates"]["audit_croise_unique"], "not_performed")
        self.assertEqual(order["gates"]["injection"], "not_performed")
        body = SENTINELLA._issue_body(order)
        self.assertIn("Un chapitre isolé reste en production interne", body)
        self.assertIn("Codex doit lire le diff", body)

    def test_one_issue_per_sha_across_independent_runs(self):
        issues = []
        def request(_repository, _token, method, route, payload=None):
            if route.startswith("/issues?"):
                return issues
            if method == "POST" and route == "/issues":
                issues.append({"title": payload["title"]})
                return {"number": len(issues)}
            raise AssertionError((method, route))
        with mock.patch.object(SENTINELLA.claude_watch, "scan_once", side_effect=self.scan), \
             mock.patch.object(SENTINELLA, "_ensure_label"), \
             mock.patch.object(SENTINELLA, "_request", side_effect=request):
            first = SENTINELLA.run(Path("/tmp/medina"), self.state, notify=True,
                                   repository="owner/Medina", token="test")
            second = SENTINELLA.run(Path("/tmp/medina"), self.state, notify=True,
                                    repository="owner/Medina", token="test")
        self.assertEqual(first["notifications"]["created"], [SHA])
        self.assertEqual(second["notifications"]["already_present"], [SHA])
        self.assertEqual(len(issues), 1)
        self.assertFalse(first["automatic_audit"])
        self.assertFalse(first["automatic_injection"])
        self.assertEqual(json.loads((self.state / "sentinella.json").read_text())["entries"][0]["sha"], SHA)

    def test_failed_scan_does_not_claim_absence_or_post_issue(self):
        with mock.patch.object(SENTINELLA.claude_watch, "scan_once", return_value={
            "status": "degraded", "error": {"category": "git_failed"}
        }), mock.patch.object(SENTINELLA, "_request") as request:
            result = SENTINELLA.run(Path("/tmp/medina"), self.state, notify=True,
                                    repository="owner/Medina", token="test")
        self.assertEqual(result["scan_status"], "degraded")
        self.assertEqual(result["scan_error"]["category"], "git_failed")
        request.assert_not_called()
        self.assertEqual(result["entries"], [])

    def test_notification_error_is_recorded_without_losing_work_order(self):
        with mock.patch.object(SENTINELLA.claude_watch, "scan_once", side_effect=self.scan), \
             mock.patch.object(SENTINELLA, "_ensure_label", side_effect=SENTINELLA.NotificationError("github_http_403")):
            result = SENTINELLA.run(Path("/tmp/medina"), self.state, notify=True,
                                    repository="owner/Medina", token="test")
        self.assertEqual(result["notifications"]["error"], "github_http_403")
        self.assertEqual(result["entries"][0]["sha"], SHA)

    def test_issue_scan_includes_closed_issues(self):
        captured = []
        def request(_repository, _token, _method, route):
            captured.append(route)
            return [{"title": SENTINELLA.ISSUE_PREFIX + SHA, "state": "closed"}]
        with mock.patch.object(SENTINELLA, "_request", side_effect=request):
            found = SENTINELLA._existing_issue_shas("owner/Medina", "test")
        self.assertEqual(found, {SHA})
        self.assertIn("state=all", captured[0])

    def test_codex_pr_carrying_claude_files_is_not_claimed_as_claude_delivery(self):
        self.candidate["refs"] = ["refs/heads/codex/integration", "refs/pull/18/head"]
        with mock.patch.object(SENTINELLA.claude_watch, "scan_once", side_effect=self.scan):
            result = SENTINELLA.run(Path("/tmp/medina"), self.state)
        self.assertEqual(result["entries"], [])

    def test_large_delivery_is_bounded_in_issue_with_full_queue_retained(self):
        self.candidate["delivery_paths"] = [f"livraisons/fichier-{n}.html" for n in range(1000)]
        order = SENTINELLA._candidate_order(self.candidate)
        self.assertEqual(order["delivery_path_count"], 1000)
        self.assertEqual(len(order["delivery_paths_sample"]), 12)
        self.assertIn("queue.json", order["full_inventory"])

    def test_cli_local_error_returns_structured_degraded_result(self):
        output = io.StringIO()
        with mock.patch.object(SENTINELLA, "run", side_effect=ValueError("bad state")), \
             redirect_stdout(output):
            code = SENTINELLA.main(["--state-dir", str(self.state)])
        result = json.loads(output.getvalue())
        self.assertEqual(code, 2)
        self.assertEqual(result["scan_status"], "degraded")
        self.assertEqual(result["scan_error"]["category"], "invalid_local_state_or_paths")
        self.assertEqual(result["notifications"]["error"], None)


if __name__ == "__main__":
    unittest.main()
