import datetime as dt
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("unblock", Path(__file__).resolve().parents[1] / "tools/medina_unblock.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class TestUnblock(unittest.TestCase):
    def setUp(self):
        self.now = dt.datetime(2026, 10, 15, 12, 0, tzinfo=dt.timezone.utc)
        self.cfg = {"enabled": True, "owner": "vialdjoukang-spec", "repository": "vialdjoukang-spec/Medina", "grace_seconds": 300}
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

    def test_owner_response_veto(self):
        reply = {"user": {"login": self.cfg["owner"]}, "created_at": "2026-10-15T12:01:00Z"}
        self.assertIsNone(m.decide(self.pr, [], [], [self.notice(), reply], self.cfg, self.now + dt.timedelta(seconds=500)))

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


if __name__ == "__main__":
    unittest.main()
