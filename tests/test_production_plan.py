"""Contrôles de répartition et réservation ; catalogue réel, aucun réseau."""
import copy
import importlib.util
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("production_plan", ROOT / "tools/production_plan.py")
PLAN = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PLAN)


class ProductionPlanTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = json.loads((ROOT / "organisation/production_plan.json").read_text())
        cls.registry = json.loads((ROOT / "organisation/fragments.json").read_text())
        source = (ROOT / "shell/medina_front.html").read_text()
        entries = json.loads(re.search(
            r'<script id="medora-data" type="application/json">(.*?)</script>', source, re.S
        ).group(1))["entries"]
        cls.titles = {entry["code"]: entry["title"] for entry in entries}
        for chapter in json.loads((ROOT / "chapters.json").read_text()):
            if chapter.get("integrated"):
                cls.titles[chapter["code"]] = chapter["title"]
        cls.temporary = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temporary.cleanup)
        cls.fixture = Path(cls.temporary.name)
        # Copy authoritative inputs: ownership and aliases are computed by load_plan.
        for relative in (
            "organisation/fragments.json", "fragments.json", "chapters.json",
            "shell/medina_front.html",
        ):
            destination = cls.fixture / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, destination)

    def setUp(self):
        self.plan = copy.deepcopy(self.original)
        for agent in self.plan["agents"].values():
            agent["active_chapter"] = None

    def chapter(self, code, fragment_id, **changes):
        chapter = {
            "code": code,
            "title": self.titles[code],
            "fragment_id": fragment_id,
            "stage": "writing",
            "base_commit": "a" * 40,
            "report_path": "docs/collaboration/reviews/" + code + ".md",
        }
        chapter.update(changes)
        return chapter

    def load(self):
        (self.fixture / "organisation/production_plan.json").write_text(
            json.dumps(self.plan, ensure_ascii=False)
        )
        return PLAN.load_plan(self.fixture)

    def test_actual_allocation_covers_each_remaining_fragment_once(self):
        _, assignments = PLAN.load_plan(ROOT)
        expected = {fragment["id"] for fragment in self.registry} - {"S01"}
        self.assertEqual(set(assignments), expected)
        self.assertEqual(len(assignments), 21)
        for owner, count in (("Claude", 11), ("Codex", 10)):
            owned = {fragment: info for fragment, info in assignments.items()
                     if info["owner"] == owner}
            self.assertEqual(len(owned), count)
            self.assertEqual({info["queue_order"] for info in owned.values()},
                             set(range(1, count + 1)))

    def test_chapter_delivery_and_repeated_final_audit_are_rejected(self):
        for key, value in (("delivery_unit", "chapter"), ("cross_audit_rounds", 2)):
            with self.subTest(rule=key):
                self.plan = copy.deepcopy(self.original)
                self.plan["rules"][key] = value
                with self.assertRaisesRegex(ValueError, "fragment entier"):
                    self.load()

    def test_reopening_injected_fragment_and_dark_theme_are_rejected(self):
        for key, value in (("injected_fragment_immutable", False), ("output_theme", "dark")):
            with self.subTest(rule=key):
                self.plan = copy.deepcopy(self.original)
                self.plan["rules"][key] = value
                with self.assertRaisesRegex(ValueError, "immuable"):
                    self.load()

    def test_two_canonical_chapters_can_advance_in_parallel(self):
        self.plan["agents"]["Claude"]["active_chapter"] = self.chapter("J45", "S02")
        self.plan["agents"]["Codex"]["active_chapter"] = self.chapter("A41", "T1")
        loaded, assignments = self.load()
        self.assertEqual(loaded["agents"]["Claude"]["active_chapter"]["title"], self.titles["J45"])
        self.assertEqual(loaded["agents"]["Codex"]["active_chapter"]["title"], self.titles["A41"])
        self.assertEqual(assignments["S02"]["owner"], "Claude")
        self.assertEqual(assignments["T1"]["owner"], "Codex")

    def test_omitted_fragment_is_rejected(self):
        self.plan["agents"]["Claude"]["queue"].pop()
        with self.assertRaises(ValueError):
            self.load()

    def test_duplicate_fragment_within_queue_is_rejected(self):
        queue = self.plan["agents"]["Claude"]["queue"]
        queue[-1] = queue[0]
        with self.assertRaises(ValueError):
            self.load()

    def test_duplicate_fragment_across_agents_is_rejected(self):
        self.plan["agents"]["Codex"]["queue"][0] = "S02"
        with self.assertRaisesRegex(ValueError, "attribué deux fois"):
            self.load()

    def test_reversed_production_order_is_rejected(self):
        self.plan["agents"]["Claude"]["queue"].reverse()
        with self.assertRaisesRegex(ValueError, "rangs de production"):
            self.load()

    def test_a_list_of_active_chapters_is_rejected(self):
        self.plan["agents"]["Claude"]["active_chapter"] = [
            self.chapter("J45", "S02"), self.chapter("J44", "S02")
        ]
        with self.assertRaisesRegex(ValueError, "chapitre actif doit être unique"):
            self.load()

    def test_same_chapter_cannot_be_reserved_by_both_agents(self):
        self.plan["agents"]["Claude"]["active_chapter"] = self.chapter("J45", "S02")
        self.plan["agents"]["Codex"]["active_chapter"] = self.chapter("J45", "T1")
        # Exercise the reservation guard separately from catalogue ownership.
        with self.assertRaisesRegex(ValueError, "actif chez les deux agents"):
            PLAN.validate_plan(self.plan, self.registry)

    def test_short_or_nonhex_base_commit_is_rejected(self):
        for sha in ("a" * 12, "a" * 39, "a" * 41, "g" * 40):
            with self.subTest(base_commit=sha):
                self.plan["agents"]["Claude"]["active_chapter"] = self.chapter(
                    "J45", "S02", base_commit=sha
                )
                with self.assertRaisesRegex(ValueError, "SHA complet"):
                    self.load()

    def test_absolute_or_traversing_report_path_is_rejected(self):
        for path in (
            "/tmp/report.md", "../report.md", "docs/../../report.md",
            "docs\\collaboration\\report.md",
        ):
            with self.subTest(report_path=path):
                self.plan["agents"]["Claude"]["active_chapter"] = self.chapter(
                    "J45", "S02", report_path=path
                )
                with self.assertRaisesRegex(ValueError, "chemin relatif sûr"):
                    self.load()

    def test_cardiology_chapter_cannot_be_claimed_as_pneumology(self):
        self.plan["agents"]["Claude"]["active_chapter"] = self.chapter("I48", "S02")
        with self.assertRaisesRegex(ValueError, "fragment déclaré dans le catalogue"):
            self.load()

    def test_catalogue_alias_cannot_reserve_an_already_grouped_course(self):
        self.plan["agents"]["Claude"]["active_chapter"] = self.chapter("M30", "S10")
        with self.assertRaisesRegex(ValueError, "Réserver le cours primaire"):
            self.load()
        self.plan["agents"]["Claude"]["active_chapter"] = None
        self.plan["agents"]["Codex"]["active_chapter"] = self.chapter("M31", "S07")
        loaded, _ = self.load()
        self.assertEqual(loaded["agents"]["Codex"]["active_chapter"]["code"], "M31")

    def test_title_must_match_canonical_course_title(self):
        self.plan["agents"]["Codex"]["active_chapter"] = self.chapter(
            "A41", "T1", title="Septicémie"
        )
        with self.assertRaisesRegex(ValueError, "sources canoniques"):
            self.load()

    def test_blocked_chapter_keeps_its_single_reservation(self):
        active = self.chapter("J45", "S02", stage="blocked")
        self.plan["agents"]["Claude"]["active_chapter"] = active
        loaded, _ = self.load()
        self.assertEqual(loaded["agents"]["Claude"]["active_chapter"], active)


if __name__ == "__main__":
    unittest.main()
