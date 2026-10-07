"""Surveillance Claude sur des dépôts Git isolés ; aucun appel réseau."""
import hashlib
import fcntl
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


TOOLS = Path(__file__).resolve().parents[1] / "tools"
SPEC = importlib.util.spec_from_file_location("claude_watch", TOOLS / "claude_watch.py")
WATCH = importlib.util.module_from_spec(SPEC)
sys.path.insert(0, str(TOOLS))
try:
    SPEC.loader.exec_module(WATCH)
finally:
    sys.path.remove(str(TOOLS))


class ClaudeWatchTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name)
        self.remote = self.directory / "remote.git"
        self.root = self.directory / "working"
        self.producer = self.directory / "producer"
        self.state = self.directory / "watch-state"
        self.root.mkdir()
        self.git(self.directory, "init", "--bare", "--initial-branch=integration", str(self.remote))
        self.git(self.root, "init", "--initial-branch=integration")
        self.git(self.root, "config", "user.name", "Watch Test")
        self.git(self.root, "config", "user.email", "watch@example.invalid")
        self.git(self.root, "config", "commit.gpgsign", "false")
        self.git(self.root, "config", "core.hooksPath", str(self.directory / "no-hooks"))
        chapters = [
            {"code": "I48", "title": "Fibrillation et flutter auriculaires", "integrated": True},
            {"code": "J45", "title": "Asthme", "integrated": True},
        ]
        fragments = [
            {"id": "S01", "rattachements": ["Cœur", "I48"], "surface": "courses-v1",
             "categories": [{"chapters": ["I48"]}]},
            {"id": "S02", "rattachements": ["Poumon"], "surface": "courses-v1",
             "categories": [{"chapters": ["J45"]}]},
        ]
        names = [
            {"id": "S01", "label": "C-01-Cardiologie", "order": 1},
            {"id": "S02", "label": "P-02-Pneumologie", "order": 2},
        ]
        for path, payload in (
            ("chapters.json", chapters), ("fragments.json", fragments),
            ("organisation/fragments.json", names),
        ):
            self.write(self.root, path, json.dumps(payload, ensure_ascii=False))
        entries = [dict(chapter, system="Cœur" if chapter["code"] == "I48" else "Poumon")
                   for chapter in chapters]
        self.write(self.root, "shell/medina_front.html", '<script id="medora-data" '
                   'type="application/json">' + json.dumps({"entries": entries}) + '</script>')
        self.write(self.root, "chapters/J45/J45_a.html", "<p>Asthme de référence.</p>")
        self.write(self.root, "chapters/I48/I48_a.html", "<p>Fibrillation de référence.</p>")
        self.git(self.root, "add", ".")
        self.git(self.root, "commit", "-m", "Canonical reference")
        self.target = self.git(self.root, "rev-parse", "HEAD")
        self.git(self.root, "remote", "add", "origin", str(self.remote))
        self.git(self.root, "push", "origin", "integration")
        self.git(self.directory, "clone", "--quiet", str(self.remote), str(self.producer))
        self.git(self.producer, "config", "user.name", "Claude Test")
        self.git(self.producer, "config", "user.email", "claude@example.invalid")
        self.git(self.producer, "config", "commit.gpgsign", "false")
        self.git(self.producer, "config", "core.hooksPath", str(self.directory / "no-hooks"))

    @staticmethod
    def git(root, *args):
        result = subprocess.run(["git", "-C", str(root), *args],
                                check=True, capture_output=True, text=True)
        return result.stdout.strip()

    @staticmethod
    def write(root, path, content):
        destination = root / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content, encoding="utf-8")

    def publish(self, text="<p>Asthme relu par Claude.</p>", branch="claude/review", packet=False):
        if self.git(self.producer, "branch", "--show-current") != branch:
            self.git(self.producer, "checkout", "-B", branch, self.target)
        if packet:
            folder = "livraisons/Livraison Claude/P-02-Pneumologie/"
            source = "sources/chapters/J45/J45_a.html"
            self.write(self.producer, folder + source, text)
            manifest = {
                "schema_version": 1, "author": "Claude", "kind": "claude_contribution",
                "source_commit": self.target,
                "fragment": {"id": "S02", "label": "P-02-Pneumologie"},
                "chapters": [{"code": "J45", "title": "Asthme", "owner_fragment": "S02"}],
                "files": [{"target_path": "chapters/J45/J45_a.html", "source_path": source,
                           "sha256": hashlib.sha256(text.encode()).hexdigest()}],
            }
            self.write(self.producer, folder + "livraison.json", json.dumps(manifest))
            self.write(self.producer, folder + "RAPPORT.md", "# J45 — Asthme\nRelecture ciblée.")
        else:
            self.write(self.producer, "chapters/J45/J45_a.html", text)
        self.git(self.producer, "add", ".")
        self.git(self.producer, "commit", "-m", "Claude review")
        commit = self.git(self.producer, "rev-parse", "HEAD")
        self.git(self.producer, "push", "origin", branch)
        return commit

    def scan(self):
        return WATCH.scan_once(self.root, self.state, integration_branch="integration")

    def publish_files(self, branch, files):
        self.git(self.producer, "checkout", "-B", branch, self.target)
        for path, content in files.items():
            self.write(self.producer, path, content)
        self.git(self.producer, "add", ".")
        self.git(self.producer, "commit", "-m", "Review documents")
        commit = self.git(self.producer, "rev-parse", "HEAD")
        self.git(self.producer, "push", "origin", branch)
        return commit

    def queue(self):
        return json.loads((self.state / "queue.json").read_text())["candidates"]

    def test_first_scan_includes_already_published_claude_delivery(self):
        commit = self.publish()
        result = self.scan()
        self.assertEqual(result["status"], "ok")
        self.assertEqual(result["new_candidates"], 1)
        self.assertEqual(result["integration_commit"], self.target)
        self.assertEqual([item["commit"] for item in self.queue()], [commit])
        self.assertEqual(self.queue()[0]["status"], "detected_pending_audit")

    def test_new_head_is_detected_without_erasing_previous_candidate(self):
        first = self.publish()
        self.scan()
        second = self.publish("<p>Asthme relu et corrigé.</p>")
        result = self.scan()
        self.assertEqual(result["new_candidates"], 1)
        self.assertEqual({item["commit"] for item in self.queue()}, {first, second})

    def test_delivery_published_after_empty_scan_is_detected(self):
        first = self.scan()
        self.assertEqual(first["candidate_count"], 0)
        commit = self.publish()
        result = self.scan()
        self.assertEqual(result["new_candidates"], 1)
        self.assertEqual(self.queue()[0]["commit"], commit)

    def test_branches_and_pr_at_same_sha_produce_one_candidate(self):
        commit = self.publish()
        self.git(self.remote, "update-ref", "refs/heads/claude/other-review", commit)
        self.git(self.remote, "update-ref", "refs/pull/23/head", commit)
        result = self.scan()
        self.assertEqual(result["new_candidates"], 1)
        self.assertEqual(len(self.queue()), 1)
        self.assertEqual(set(self.queue()[0]["refs"]), {
            "refs/heads/claude/review", "refs/heads/claude/other-review", "refs/pull/23/head",
        })

    def test_pr_without_claude_named_branch_is_still_detected(self):
        commit = self.publish(branch="review-without-agent-name", packet=True)
        self.git(self.remote, "update-ref", "refs/pull/24/head", commit)
        result = self.scan()
        self.assertEqual(result["new_candidates"], 1)
        self.assertEqual(self.queue()[0]["commit"], commit)
        self.assertIn("refs/pull/24/head", self.queue()[0]["refs"])

    def test_unattributed_pr_is_not_claimed_as_a_claude_delivery(self):
        commit = self.publish(branch="unattributed-medical-review")
        self.git(self.remote, "update-ref", "refs/pull/25/head", commit)
        result = self.scan()
        self.assertEqual(result["status"], "ok")
        self.assertEqual(result["new_candidates"], 0)
        self.assertEqual(self.queue(), [])

    def test_neutral_branch_without_pr_can_deliver_a_claude_packet(self):
        commit = self.publish(branch="legacy-handoff", packet=True)
        result = self.scan()
        self.assertEqual(result["new_candidates"], 1)
        self.assertEqual(self.queue()[0]["commit"], commit)
        self.assertEqual(self.queue()[0]["refs"], ["refs/heads/legacy-handoff"])
        self.assertEqual(self.queue()[0]["manifests"][0]["fragment_id"], "S02")

    def test_old_flat_report_without_manifest_or_pr_is_received(self):
        path = "CLAUDE_RAPPORT_J45.md"
        commit = self.publish_files("old-report", {path: "# J45 — Asthme\nAudit ciblé."})
        result = self.scan()
        self.assertEqual(result["new_candidates"], 1)
        candidate = self.queue()[0]
        self.assertEqual(candidate["commit"], commit)
        self.assertIn(path, candidate["delivery_paths"])
        self.assertEqual(candidate["manifests"], [])
        scope = next(scope for scope in candidate["scopes"] if scope["code"] == "J45")
        self.assertEqual(scope["title"], "Asthme")
        self.assertEqual(scope["fragment_id"], "S02")
        self.assertEqual(candidate["status"], "detected_pending_audit")

    def test_claude_instruction_file_on_codex_pr_is_not_a_delivery(self):
        commit = self.publish_files("codex/instructions", {"CLAUDE.md": "Lire J45 — Asthme."})
        self.git(self.remote, "update-ref", "refs/pull/26/head", commit)
        result = self.scan()
        self.assertEqual(result["status"], "ok")
        self.assertEqual(result["new_candidates"], 0)
        self.assertEqual(self.queue(), [])

    def test_coordinator_copy_of_old_packet_is_not_a_new_incoming_delivery(self):
        self.publish(branch="codex/copied-deliveries", packet=True)
        result = self.scan()
        self.assertEqual(result["status"], "ok")
        self.assertEqual(result["new_candidates"], 0)
        self.assertEqual(self.queue(), [])

    def test_replay_does_not_duplicate_delivery_or_lose_audit_state(self):
        self.publish()
        self.scan()
        original = self.queue()
        result = self.scan()
        self.assertEqual(result["new_candidates"], 0)
        self.assertEqual(result["candidate_count"], 1)
        def stable(items):
            return [{key: value for key, value in item.items() if key != "last_seen_at"}
                    for item in items]
        self.assertEqual(stable(self.queue()), stable(original))

    def test_claude_head_already_in_target_is_not_queued(self):
        self.git(self.remote, "update-ref", "refs/heads/claude/already-integrated", self.target)
        result = self.scan()
        self.assertEqual(result["status"], "ok")
        self.assertEqual(result["new_candidates"], 0)
        self.assertEqual(self.queue(), [])

    def test_failed_remote_access_preserves_queue_and_state(self):
        self.publish()
        self.scan()
        queue_before = (self.state / "queue.json").read_bytes()
        state_before = (self.state / "state.json").read_bytes()
        self.remote.rename(self.directory / "offline.git")
        result = self.scan()
        self.assertEqual(result["status"], "degraded")
        self.assertIsNotNone(result["error"])
        self.assertEqual((self.state / "queue.json").read_bytes(), queue_before)
        self.assertEqual((self.state / "state.json").read_bytes(), state_before)
        self.assertEqual(json.loads((self.state / "status.json").read_text())["status"], "degraded")
        self.assertTrue(all(item["status"] == "detected_pending_audit" for item in self.queue()))

    def test_initial_access_failure_does_not_claim_readiness(self):
        self.remote.rename(self.directory / "offline.git")
        result = self.scan()
        self.assertEqual(result["status"], "degraded")
        self.assertEqual(result["new_candidates"], 0)
        self.assertEqual(result["candidate_count"], 0)
        self.assertIsNone(result["integration_commit"])
        self.assertFalse((self.state / "queue.json").exists())

    def test_partial_storage_failure_restores_last_successful_queue_and_state(self):
        first = self.publish()
        self.scan()
        queue_before = (self.state / "queue.json").read_bytes()
        state_before = (self.state / "state.json").read_bytes()
        self.publish("<p>Correction arrivée pendant la panne de stockage.</p>")
        original_replace = WATCH.os.replace
        failed = False
        def fail_state_once(source, destination):
            nonlocal failed
            if Path(destination) == self.state / "state.json" and not failed:
                failed = True
                raise OSError("Simulated storage failure")
            return original_replace(source, destination)
        with mock.patch.object(WATCH.os, "replace", side_effect=fail_state_once):
            result = self.scan()
        self.assertTrue(failed)
        self.assertEqual(result["status"], "degraded")
        self.assertEqual((self.state / "queue.json").read_bytes(), queue_before)
        self.assertEqual((self.state / "state.json").read_bytes(), state_before)
        self.assertEqual([candidate["commit"] for candidate in self.queue()], [first])
        self.assertEqual(self.scan()["new_candidates"], 1)

    def test_malformed_state_returns_degraded_without_resetting_it(self):
        self.state.mkdir()
        path = self.state / "state.json"
        path.write_text("[]")
        result = self.scan()
        self.assertEqual(result["status"], "degraded")
        self.assertEqual(result["new_candidates"], 0)
        self.assertEqual(path.read_text(), "[]")
        self.assertFalse((self.state / "queue.json").exists())

    def test_reusing_state_for_another_checkout_is_rejected(self):
        self.publish()
        self.scan()
        queue_before = (self.state / "queue.json").read_bytes()
        state_before = (self.state / "state.json").read_bytes()
        result = WATCH.scan_once(self.producer, self.state, integration_branch="integration")
        self.assertEqual(result["status"], "degraded")
        self.assertEqual(result["new_candidates"], 0)
        self.assertEqual(result["error"]["category"], "state_repository_context_mismatch")
        self.assertEqual((self.state / "queue.json").read_bytes(), queue_before)
        self.assertEqual((self.state / "state.json").read_bytes(), state_before)

    def test_packet_scopes_and_manifest_are_recorded_without_validation_claim(self):
        commit = self.publish(packet=True)
        self.scan()
        candidate = self.queue()[0]
        self.assertEqual(candidate["commit"], commit)
        scope = next(scope for scope in candidate["scopes"] if scope["code"] == "J45")
        self.assertEqual(scope["title"], "Asthme")
        self.assertEqual(scope["fragment_id"], "S02")
        self.assertEqual(scope["fragment_label"], "P-02-Pneumologie")
        self.assertIn("J45 — Asthme", scope["display_name"])
        manifest = candidate["manifests"][0]
        self.assertTrue(manifest["path"].endswith("/livraison.json"))
        self.assertEqual(manifest["fragment_id"], "S02")
        self.assertEqual(manifest["declared_codes"], ["J45"])
        self.assertEqual(manifest["validation"], "not_performed")
        self.assertEqual(candidate["status"], "detected_pending_audit")

    def test_concurrent_scan_returns_busy_and_preserves_existing_queue(self):
        self.publish()
        self.scan()
        queue_before = (self.state / "queue.json").read_bytes()
        state_before = (self.state / "state.json").read_bytes()
        with (self.state / ".scan.lock").open("a+") as lock:
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            result = self.scan()
        self.assertEqual(result["status"], "busy")
        self.assertEqual(result["new_candidates"], 0)
        self.assertEqual((self.state / "queue.json").read_bytes(), queue_before)
        self.assertEqual((self.state / "state.json").read_bytes(), state_before)

    def test_state_directory_inside_checkout_is_rejected_before_writing(self):
        unsafe = self.root / "watch-state"
        with self.assertRaises(ValueError):
            WATCH.scan_once(self.root, unsafe, integration_branch="integration")
        self.assertFalse(unsafe.exists())
        self.assertEqual(self.git(self.root, "status", "--porcelain=v1"), "")

    def test_scan_preserves_working_branch_dirty_sources_and_git_index(self):
        self.publish(packet=True)
        self.write(self.root, "chapters/J45/J45_a.html", "<p>Modification locale conservée.</p>")
        self.write(self.root, "local-note.txt", "Travail en cours.")
        self.git(self.root, "add", "local-note.txt")
        branch_before = self.git(self.root, "symbolic-ref", "HEAD")
        head_before = self.git(self.root, "rev-parse", "HEAD")
        status_before = self.git(self.root, "status", "--porcelain=v1")
        index_before = (self.root / ".git/index").read_bytes()
        files_before = {path: path.read_bytes() for path in self.root.rglob("*")
                        if path.is_file() and ".git" not in path.relative_to(self.root).parts}
        self.scan()
        self.assertEqual(self.git(self.root, "symbolic-ref", "HEAD"), branch_before)
        self.assertEqual(self.git(self.root, "rev-parse", "HEAD"), head_before)
        self.assertEqual(self.git(self.root, "status", "--porcelain=v1"), status_before)
        self.assertEqual((self.root / ".git/index").read_bytes(), index_before)
        self.assertEqual({path: path.read_bytes() for path in self.root.rglob("*")
                          if path.is_file() and ".git" not in path.relative_to(self.root).parts}, files_before)


if __name__ == "__main__":
    unittest.main()
