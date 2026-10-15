import datetime as dt
import importlib.util
from pathlib import Path
import unittest
import urllib.error

spec = importlib.util.spec_from_file_location("unblock", Path(__file__).resolve().parents[1] / "tools/medina_unblock.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class TestUnblock(unittest.TestCase):
    def setUp(self):
        self.now = dt.datetime(2026, 10, 15, 12, 0, tzinfo=dt.timezone.utc)
        self.cfg = {"enabled": True, "owner": "vialdjoukang-spec", "repository": "vialdjoukang-spec/Medina", "control_issue": 97, "grace_seconds": 300, "medical_audits": "suspended"}
        self.pr = {"head": {"sha": "a", "ref": "claude/test", "repo": {"full_name": self.cfg["repository"]}}, "base": {"sha": "b"}, "mergeable": False}

    def notice(self):
        a = m.decide(self.pr, [], [], [], self.cfg, self.now)
        return {"body": m.message(a, self.pr), "created_at": "2026-10-15T12:00:00Z", "id": 1, "user": {"login": "github-actions[bot]", "type": "Bot"}}

    def test_initial_notice(self):
        self.assertEqual(m.decide(self.pr, [], [], [], self.cfg, self.now)["stage"], "notice")

    def test_wait(self):
        self.assertIsNone(m.decide(self.pr, [], [], [self.notice()], self.cfg, self.now + dt.timedelta(seconds=299)))

    def test_delegates_after_five_minutes(self):
        self.assertEqual(m.decide(self.pr, [], [], [self.notice()], self.cfg, self.now + dt.timedelta(seconds=300))["stage"], "delegated")

    def test_pr_thread_reply_does_not_veto(self):
        reply = {"user": {"login": self.cfg["owner"]}, "created_at": "2026-10-15T12:01:00Z"}
        self.assertEqual(m.decide(self.pr, [], [], [self.notice(), reply], self.cfg, self.now + dt.timedelta(seconds=500))["stage"], "delegated")

    def test_changed_head_resets(self):
        n = self.notice()
        self.pr["head"]["sha"] = "new"
        self.assertEqual(m.decide(self.pr, [], [], [n], self.cfg, self.now)["stage"], "notice")

    def test_changed_base_resets(self):
        n = self.notice()
        self.pr["base"]["sha"] = "new"
        self.assertEqual(m.decide(self.pr, [], [], [n], self.cfg, self.now)["stage"], "notice")

    def test_codex_ignored(self):
        self.pr["head"]["ref"] = "codex/test"
        self.assertIsNone(m.decide(self.pr, [], [], [], self.cfg, self.now))

    def test_fork_ignored(self):
        self.pr["head"]["repo"]["full_name"] = "stranger/Medina"
        self.assertIsNone(m.decide(self.pr, [], [], [], self.cfg, self.now))

    def test_unknown_mergeable_not_conflict(self):
        self.pr["mergeable"] = None
        self.assertFalse(any(x.startswith("conflit") for x in m.findings(self.pr, [], [])))

    def test_no_repeat(self):
        n = self.notice()
        a = m.decide(self.pr, [], [], [n], self.cfg, self.now + dt.timedelta(seconds=300))
        done = {**n, "id": 2, "body": m.message(a, self.pr)}
        self.assertIsNone(m.decide(self.pr, [], [], [n, done], self.cfg, self.now + dt.timedelta(seconds=600)))

    def test_off_and_on(self):
        off = {"id": 1, "created_at": "2026-10-15T12:00:00Z", "user": {"login": self.cfg["owner"]}, "body": "/medina off"}
        self.assertFalse(m.enabled(self.cfg, [off]))
        on = {**off, "id": 2, "body": "/medina on"}
        self.assertTrue(m.enabled(self.cfg, [off, on]))

    def test_stranger_cannot_control(self):
        off = {"id": 1, "created_at": "2026-10-15T12:00:00Z", "user": {"login": "stranger"}, "body": "/medina off"}
        self.assertTrue(m.enabled(self.cfg, [off]))

    def test_bot_cannot_control(self):
        off = {"id": 1, "created_at": "2026-10-15T12:00:00Z", "user": {"login": self.cfg["owner"], "type": "Bot"}, "body": "/medina off"}
        self.assertTrue(m.enabled(self.cfg, [off]))

    def test_forged_marker_ignored(self):
        n = self.notice()
        n["user"] = {"login": "stranger"}
        self.assertIsNone(m.marker(n))

    def test_explicit_placeholder_is_suggestion_only(self):
        files = [{"filename": "cours/C01.html", "status": "modified", "additions": 1, "patch": "@@ -1 +1 @@\n+<!-- TODO préciser -->"}]
        suggestion = m.lesson_suggestions(files)
        self.assertEqual(len(suggestion), 1)
        self.assertIn("non bloquante", suggestion[0])

    def test_missing_patch_is_not_a_defect(self):
        self.assertEqual(m.lesson_suggestions([{"filename": "cours/C01.html", "patch": None}]), [])

    def test_audit_and_truth_policy_are_explicit_in_notice(self):
        self.cfg["medical_audits"] = "suspended"
        action = m.decide(self.pr, [], [], [], self.cfg, self.now)
        body = m.message(action, self.pr)
        self.assertIn("suspendus", body)
        self.assertIn("ne prétend pas vérifier cette lecture", body)

    def test_branch_inventory_falls_back_after_403(self):
        class API:
            def pages(self, path):
                if path == "branches":
                    raise urllib.error.HTTPError(path, 403, "forbidden", None, None)
                if path == "git/matching-refs/heads/":
                    return [{"ref": "refs/heads/main"}]
                raise AssertionError(path)
        self.assertEqual(m.branch_inventory(API()), [{"name": "main"}])

    def test_pr_scan_can_continue_when_branch_apis_both_return_403(self):
        class API:
            def pages(self, path):
                if path == "issues/97/comments" or path == "pulls?state=open":
                    return []
                if path in {"branches", "git/matching-refs/heads/"}:
                    raise urllib.error.HTTPError(path, 403, "forbidden", None, None)
                raise AssertionError(path)
        self.assertEqual(m.run(self.cfg, API(), self.now, dry_run=True), [])


if __name__ == "__main__":
    unittest.main()
