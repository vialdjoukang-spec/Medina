"""Non-site receipts may skip Pages; changed or unknown site inputs never do."""
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

from tools.pages_scope import CLAUDE_REGISTRY, METADATA_FILES, classify, determine_scope


def registry(status="PRET_A_INJECTER", transfer="Codex", code="G45"):
    return json.dumps({"cycles": [{"cycle": 2, "transferred_from": transfer,
                                   "chapters": [{"code": code, "status": status}]}]})


class PagesScopeTests(unittest.TestCase):
    def test_exact_non_site_metadata_does_not_rebuild(self):
        paths = sorted(METADATA_FILES) + ["organisation/execution-20261014/publications/G45.json"]
        self.assertEqual(classify(paths), (False, []))

    def test_every_site_input_and_unknown_path_keeps_full_build(self):
        for path in (
            "chapters/G45/G45_a.html", "chapters/G45/G45_pop1.html", "chapters.json",
            "glossary/g45.py", "glossary/__init__.py", "assets/img/cycle2/g45/figure.png",
            "assets/images/new.jpg", "assets/fonts/new.woff2", "modules/ecg.json",
            "shell/medina_front.html", "shell/polish.js", "engine/reader.js",
            "fragments.json", "fragment_surface.py", "build_front.py", "build_index.py",
            "organisation/fragments.json", "organisation/production_plan.json",
            "organisation/progression/plan-tetrade-30-cycles.html",
            "organisation/execution-20261014/cycles.json",
            "docs/nosology/captures/example.png", "docs/collaboration/reviews/capture.png",
            "nosology/fragments/T1.json", "tools/build_fragment_work_preview.py",
            "tests/verify_fragment_work_preview.py", ".github/workflows/pages.yml",
            "livraisons/Livraison Codex/I-03-Infectiologie/travail/source.html",
            "REPRISE_SESSION.html", "organisation/CYCLES_CLAUDE_notes.json", "unknown-file",
        ):
            with self.subTest(path=path):
                self.assertTrue(classify([path])[0])

    def test_metadata_mixed_with_site_input_still_builds(self):
        self.assertEqual(classify(["CLAUDE.md", "chapters.json"]), (True, ["chapters.json"]))

    def test_claude_status_proofs_are_not_publication_inputs(self):
        before = registry()
        after = json.loads(registry("PUBLIE_VERIFIE"))
        after["cycles"][0]["chapters"][0]["publication"] = {"path": "receipt.json", "sha256": "a" * 64}
        self.assertEqual(classify([CLAUDE_REGISTRY], before, json.dumps(after)), (False, []))

    def test_effective_transfer_change_always_builds(self):
        for after in (registry(transfer="Claude"), registry(code="E10"), '{"cycles": []}'):
            with self.subTest(after=after):
                self.assertTrue(classify([CLAUDE_REGISTRY], registry(), after)[0])

    def test_invalid_or_unavailable_registry_always_builds(self):
        for broken in (None, "{", "[]", "{}", '{"cycles": [null]}', '{"cycles": [{"chapters": [null]}]}'):
            with self.subTest(broken=broken):
                self.assertTrue(classify([CLAUDE_REGISTRY], registry(), broken)[0])
                self.assertTrue(classify([CLAUDE_REGISTRY], broken, registry())[0])

    def test_manual_or_missing_base_always_builds(self):
        for base, force in ((None, False), ("0" * 40, False), ("unused", True)):
            self.assertTrue(determine_scope(Path("."), base, force=force)[0])

    def test_workflow_scope_does_not_remove_fragment_guard_or_manifest(self):
        root = Path(__file__).resolve().parents[1]
        workflow = (root / ".github/workflows/pages.yml").read_text()
        guard = (root / ".github/workflows/espace.yml").read_text()
        self.assertNotIn("paths-ignore:", workflow)
        self.assertIn("needs: scope", workflow)
        self.assertIn("needs.scope.outputs.build == 'true'", workflow)
        self.assertIn("python3 tools/espace.py garde", workflow)
        self.assertIn("python tools/publication_manifest.py --site _site", workflow)
        self.assertNotIn("paths-ignore:", guard)
        # A dependency cache is not a cache of medical/browser validation results.
        self.assertIn("python tests/verify_fragment_work_preview.py", workflow)
        self.assertIn("node tests/verify_fragment_bootstrap.cjs", workflow)


class PagesScopeGitTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory(prefix="medina-pages-scope-")
        self.root = Path(self.directory.name)
        self.git("init", "-q")
        self.git("config", "user.name", "Scope fixture")
        self.git("config", "user.email", "scope@example.invalid")
        self.write("CLAUDE.md", "fixture before")
        self.write("chapters/G45/G45_a.html", "technical fixture")
        self.write(CLAUDE_REGISTRY, registry())
        self.base = self.commit()

    def tearDown(self):
        self.directory.cleanup()

    def git(self, *args):
        return subprocess.check_output(["git", "-c", "core.hooksPath=/dev/null", *args],
                                       cwd=self.root, stderr=subprocess.PIPE).decode().strip()

    def write(self, path, text):
        destination = self.root / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(text)

    def commit(self):
        self.git("add", ".")
        self.git("commit", "-qm", "technical fixture")
        return self.git("rev-parse", "HEAD")

    def test_whole_push_range_not_only_last_commit(self):
        self.write("chapters/G45/G45_a.html", "changed technical fixture")
        self.commit()
        self.write("CLAUDE.md", "metadata only latest commit")
        self.commit()
        self.assertTrue(determine_scope(self.root, self.base)[0])

    def test_metadata_only_push_does_not_build(self):
        self.write("CLAUDE.md", "metadata only")
        self.write(CLAUDE_REGISTRY, registry("PUBLIE_VERIFIE"))
        self.commit()
        self.assertEqual(determine_scope(self.root, self.base), (False, []))

    def test_rename_into_ignored_metadata_cannot_hide_deleted_course(self):
        self.git("mv", "chapters/G45/G45_a.html", "REPRISE_SESSION.md")
        self.commit()
        self.assertTrue(determine_scope(self.root, self.base)[0])

    def test_unavailable_base_keeps_full_build(self):
        self.assertTrue(determine_scope(self.root, "missing-ref")[0])


if __name__ == "__main__":
    unittest.main()
