"""Codex_Sentinella tests: issue deduplication and fragment audit gates."""
import importlib.util
import io
import json
from pathlib import Path
from contextlib import redirect_stdout
import subprocess
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
BASE = "b" * 40
FINGERPRINT = "f" * 64


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
        self.artifact = {"fingerprint": FINGERPRINT, "artifact_count": 1,
                         "artifact_paths_sample": ["espace_partage/FRAGMENTS_CLAUDE_A_AUDITER_PAR_CODEX/P-02-Pneumologie/MANIFESTE.json"]}

    def scan(self, *_args):
        (self.state / "queue.json").write_text(json.dumps({"integration_commit": BASE,
                                                            "candidates": [self.candidate]}))
        return {"status": "ok", "error": None}

    def test_order_requires_full_fragment_and_coordinator_decision(self):
        order = SENTINELLA._candidate_order(self.candidate, self.artifact)
        self.assertEqual(order["sha"], SHA)
        self.assertEqual(order["fragments_suggested"], ["P-02-Pneumologie"])
        self.assertEqual(order["gates"]["fragment_entier_auto_revu"], "not_verified")
        self.assertEqual(order["gates"]["audit_croise_unique"], "not_performed")
        self.assertEqual(order["gates"]["injection"], "not_performed")
        body = SENTINELLA._issue_body(order)
        self.assertIn("Un chapitre isolé reste en production interne", body)
        self.assertIn("Codex doit lire le diff", body)

    def test_one_issue_per_fingerprint_across_independent_runs(self):
        issues = []
        def request(_repository, _token, method, route, payload=None):
            if route.startswith("/issues?"):
                return issues
            if method == "POST" and route == "/issues":
                issues.append({"title": payload["title"]})
                return {"number": len(issues)}
            raise AssertionError((method, route))
        with mock.patch.object(SENTINELLA.claude_watch, "scan_once", side_effect=self.scan), \
             mock.patch.object(SENTINELLA, "_artifact_fingerprint", return_value=self.artifact), \
             mock.patch.object(SENTINELLA, "_ensure_label"), \
             mock.patch.object(SENTINELLA, "_request", side_effect=request):
            first = SENTINELLA.run(Path("/tmp/medina"), self.state, notify=True,
                                   repository="owner/Medina", token="test")
            second = SENTINELLA.run(Path("/tmp/medina"), self.state, notify=True,
                                    repository="owner/Medina", token="test")
        self.assertEqual(first["notifications"]["created"], [FINGERPRINT])
        self.assertEqual(second["notifications"]["already_present"], [FINGERPRINT])
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
             mock.patch.object(SENTINELLA, "_artifact_fingerprint", return_value=self.artifact), \
             mock.patch.object(SENTINELLA, "_ensure_label", side_effect=SENTINELLA.NotificationError("github_http_403")):
            result = SENTINELLA.run(Path("/tmp/medina"), self.state, notify=True,
                                    repository="owner/Medina", token="test")
        self.assertEqual(result["notifications"]["error"], "github_http_403")
        self.assertEqual(result["entries"][0]["sha"], SHA)

    def test_issue_scan_includes_closed_and_legacy_issues(self):
        captured = []
        def request(_repository, _token, _method, route):
            captured.append(route)
            return [{"title": SENTINELLA.ISSUE_PREFIX + SHA, "state": "closed"},
                    {"title": SENTINELLA.FINGERPRINT_PREFIX + FINGERPRINT, "state": "closed"}]
        with mock.patch.object(SENTINELLA, "_request", side_effect=request):
            fingerprints, legacy = SENTINELLA._existing_issue_identifiers("owner/Medina", "test")
        self.assertEqual(fingerprints, {FINGERPRINT})
        self.assertEqual(legacy, {SHA})
        self.assertIn("state=all", captured[0])

    def test_codex_pr_carrying_claude_files_is_not_claimed_as_claude_delivery(self):
        self.candidate["refs"] = ["refs/heads/codex/integration", "refs/pull/18/head"]
        with mock.patch.object(SENTINELLA.claude_watch, "scan_once", side_effect=self.scan):
            result = SENTINELLA.run(Path("/tmp/medina"), self.state)
        self.assertEqual(result["entries"], [])

    def test_large_delivery_is_bounded_in_issue_with_full_queue_retained(self):
        self.candidate["delivery_paths"] = [f"livraisons/fichier-{n}.html" for n in range(1000)]
        order = SENTINELLA._candidate_order(self.candidate, self.artifact)
        self.assertEqual(order["delivery_path_count"], 1000)
        self.assertEqual(len(order["delivery_paths_sample"]), 12)
        self.assertIn("queue.json", order["full_inventory"])

    @staticmethod
    def git(root, *args):
        result = subprocess.run(["git", "-C", str(root), *args], check=True,
                                capture_output=True, text=True)
        return result.stdout.strip()

    def make_delivery_history(self):
        repo = Path(self.temporary.name) / "producer"
        repo.mkdir()
        self.git(repo, "init", "--initial-branch=main")
        self.git(repo, "config", "user.name", "Sentinella Test")
        self.git(repo, "config", "user.email", "test@example.invalid")
        (repo / "README.md").write_text("Base\n")
        self.git(repo, "add", ".")
        self.git(repo, "commit", "-m", "base")
        base = self.git(repo, "rev-parse", "HEAD")
        packet = repo / "espace_partage/FRAGMENTS_CLAUDE_A_AUDITER_PAR_CODEX/P-02-Pneumologie"
        packet.mkdir(parents=True)
        manifest = packet / "MANIFESTE.json"
        manifest.write_text('{"version":1}\n')
        (packet / "REMISE.md").write_text("Remise P-02 v1\n")
        self.git(repo, "add", ".")
        self.git(repo, "commit", "-m", "fragment handoff")
        first = self.git(repo, "rev-parse", "HEAD")
        draft = repo / "livraisons/Livraison Claude/G-04-Gastroenterologie/travail/K50_a.html"
        draft.parent.mkdir(parents=True)
        draft.write_text("<p>Brouillon G-04</p>\n")
        self.git(repo, "add", ".")
        self.git(repo, "commit", "-m", "new draft only")
        second = self.git(repo, "rev-parse", "HEAD")
        manifest.write_text('{"version":2}\n')
        self.git(repo, "add", ".")
        self.git(repo, "commit", "-m", "new fragment handoff version")
        third = self.git(repo, "rev-parse", "HEAD")
        bare = self.state / "git"
        self.git(Path(self.temporary.name), "clone", "--bare", str(repo), str(bare))
        return base, first, second, third

    def test_draft_only_head_reuses_issue_but_changed_manifest_creates_new_issue(self):
        base, first, second, third = self.make_delivery_history()
        first_artifact = SENTINELLA._artifact_fingerprint(self.state / "git", first, base)
        second_artifact = SENTINELLA._artifact_fingerprint(self.state / "git", second, base)
        third_artifact = SENTINELLA._artifact_fingerprint(self.state / "git", third, base)
        self.assertEqual(first_artifact["fingerprint"], second_artifact["fingerprint"])
        self.assertNotEqual(first_artifact["fingerprint"], third_artifact["fingerprint"])
        self.assertIsNone(SENTINELLA._artifact_fingerprint(self.state / "git", second, first))
        issues = []
        def scan(*_args):
            (self.state / "queue.json").write_text(json.dumps({
                "integration_commit": base, "candidates": [self.candidate],
            }))
            return {"status": "ok", "error": None}
        def request(_repository, _token, method, route, payload=None):
            if route.startswith("/issues?"):
                return issues
            if method == "POST" and route == "/issues":
                issues.append({"title": payload["title"]})
                return {"number": len(issues)}
            raise AssertionError((method, route))
        with mock.patch.object(SENTINELLA.claude_watch, "scan_once", side_effect=scan), \
             mock.patch.object(SENTINELLA, "_ensure_label"), \
             mock.patch.object(SENTINELLA, "_request", side_effect=request):
            self.candidate["commit"] = first
            one = SENTINELLA.run(Path("/tmp/medina"), self.state, notify=True,
                                 repository="owner/Medina", token="test")
            self.candidate["commit"] = second
            two = SENTINELLA.run(Path("/tmp/medina"), self.state, notify=True,
                                 repository="owner/Medina", token="test")
            self.candidate["commit"] = third
            three = SENTINELLA.run(Path("/tmp/medina"), self.state, notify=True,
                                   repository="owner/Medina", token="test")
        self.assertEqual(one["notifications"]["created"], [first_artifact["fingerprint"]])
        self.assertEqual(two["notifications"]["already_present"], [first_artifact["fingerprint"]])
        self.assertEqual(three["notifications"]["created"], [third_artifact["fingerprint"]])
        self.assertEqual(len(issues), 2)

    def test_old_sha_issue_migrates_to_content_fingerprint(self):
        base, first, second, _third = self.make_delivery_history()
        self.candidate["commit"] = second
        def scan(*_args):
            (self.state / "queue.json").write_text(json.dumps({
                "integration_commit": base, "candidates": [self.candidate],
            }))
            return {"status": "ok", "error": None}
        def request(_repository, _token, method, route, _payload=None):
            if route.startswith("/issues?"):
                return [{"title": SENTINELLA.ISSUE_PREFIX + first}]
            raise AssertionError("new issue should not be created")
        with mock.patch.object(SENTINELLA.claude_watch, "scan_once", side_effect=scan), \
             mock.patch.object(SENTINELLA, "_ensure_label"), \
             mock.patch.object(SENTINELLA, "_request", side_effect=request):
            result = SENTINELLA.run(Path("/tmp/medina"), self.state, notify=True,
                                    repository="owner/Medina", token="test")
        self.assertEqual(result["notifications"]["created"], [])
        self.assertEqual(len(result["notifications"]["already_present"]), 1)

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
