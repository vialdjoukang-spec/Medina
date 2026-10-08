"""Verified draft overlays must remain isolated from canonical courses."""
import base64
import copy
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("fragment_work_preview", ROOT / "tools/build_fragment_work_preview.py")
PREVIEW = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PREVIEW)


def pack_html(courses):
    packed = base64.b64encode(gzip.compress(courses.encode(), mtime=0)).decode()
    return '<script>window.MEDINA_COMPLETE=[];</script><script id="mdn-pack" type="application/octet-stream">' + packed + '</script>'


def course_html(code, panels=("pA", "pE", "pS", "pP")):
    return ('<template id="ch-' + code + '"><div class="chap"><div class="chap-head">'
            '<h1>' + code + ' — Cours technique</h1></div>' +
            ''.join('<div class="panel" id="' + panel + '"><p>Fixture technique sans contenu médical.</p></div>' for panel in panels) +
            '</div></template>')


class FragmentWorkPreviewTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="medina-preview-test-")
        self.base = Path(self.temporary.name)
        self.sources = self.base / "packet/sources"
        self.sources.mkdir(parents=True)
        self.manifest = {
            "schema_version": 1, "kind": "internal_fragment_work", "fragment_id": "T1",
            "chapter_codes": ["A41", "B24"],
            "chapters": [{"code": code, "title": code + " — Fixture technique", "covers": [code]} for code in ("A41", "B24")],
            "source_commit": "2f4a7db", "fragment_complete": False, "external_audit": False,
            "canonical_injection": False, "files": [],
        }
        for code in self.manifest["chapter_codes"]:
            for suffix in PREVIEW.REQUIRED_SUFFIXES:
                content = course_html(code) if suffix == "a" else "<!-- Fixture technique -->"
                self.add_file(f"chapters/{code}/{code}_{suffix}.html", content.encode())
            self.add_file(f"glossary/{code.lower()}.py", b"G = {}\n")
        self.write_manifest()

    def tearDown(self):
        self.temporary.cleanup()

    def add_file(self, path, content):
        target = self.sources / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
        self.manifest["files"].append({"path": path, "internal_sha256": hashlib.sha256(content).hexdigest()})

    def write_manifest(self):
        (self.sources.parent / "manifest_interne.json").write_text(json.dumps(self.manifest), encoding="utf-8")

    def read(self):
        return PREVIEW.read_sources(self.sources, ROOT)

    def test_declared_two_chapters_are_accepted(self):
        manifest, files = self.read()
        self.assertEqual(manifest["chapter_codes"], ["A41", "B24"])
        self.assertEqual(len(files), 16)

    def test_a41_optional_internal_sciences_and_justifications_are_accepted(self):
        self.add_file("chapters/A41/A41_pop_sciences_revision.html", b"<!-- internal sciences -->")
        self.add_file("chapters/A41/A41_justifications.json", b"{}")
        self.write_manifest()
        self.assertEqual(len(self.read()[1]), 18)

    def test_each_declared_chapter_accepts_separate_sciences_popups(self):
        for code in self.manifest["chapter_codes"]:
            self.add_file(f"chapters/{code}/{code}_pop_sciences_revision.html", b"<!-- internal sciences -->")
        self.write_manifest()
        manifest, files = self.read()
        self.assertEqual(len(files), 18)
        for code in manifest["chapter_codes"]:
            self.assertIn(f"chapters/{code}/{code}_pop_sciences_revision.html", files)

    def test_changed_bytes_fail_hash_verification(self):
        (self.sources / "chapters/B24/B24_a.html").write_text("changed", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Empreinte interne incorrecte"):
            self.read()

    def test_path_escapes_and_foreign_prefixes_are_rejected(self):
        row = self.manifest["files"][0]
        for path in ("../outside.html", "/tmp/outside.html", "chapters/A41/../B24/B24_a.html",
                     "chapters/A41/A41_unknown.html", "chapters/A41/J45_a.html", "glossary/i83.py", "chapters//A41/A41_a.html"):
            with self.subTest(path=path):
                row["path"] = path
                self.write_manifest()
                with self.assertRaisesRegex(ValueError, "Chemin source non autorisé"):
                    self.read()

    def test_foreign_chapter_or_cover_is_rejected(self):
        changed = copy.deepcopy(self.manifest)
        for mode in ("chapter", "cover"):
            with self.subTest(mode=mode):
                self.manifest = copy.deepcopy(changed)
                if mode == "chapter":
                    self.manifest["chapter_codes"][1] = "J45"
                    self.manifest["chapters"][1].update(code="J45", covers=["J45"])
                else:
                    self.manifest["chapters"][1]["covers"].append("J45")
                self.write_manifest()
                with self.assertRaisesRegex(ValueError, "étranger à l’infectiologie"):
                    self.read()

    def test_unlisted_file_is_rejected(self):
        (self.sources / "extra.html").write_text("extra", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "exactement au manifeste"):
            self.read()

    def test_required_tab_source_cannot_be_omitted(self):
        row = self.manifest["files"].pop(1)
        (self.sources / row["path"]).unlink()
        self.write_manifest()
        with self.assertRaisesRegex(ValueError, "omet des sources"):
            self.read()

    def test_duplicate_file_is_rejected(self):
        self.manifest["files"].append(dict(self.manifest["files"][0]))
        self.write_manifest()
        with self.assertRaisesRegex(ValueError, "doublons"):
            self.read()

    def test_duplicate_chapter_or_overlapping_covers_are_rejected(self):
        original = copy.deepcopy(self.manifest)
        self.manifest["chapter_codes"][1] = "A41"
        self.write_manifest()
        with self.assertRaisesRegex(ValueError, "uniques"):
            self.read()
        self.manifest = original
        self.manifest["chapters"][1]["covers"].append("A41")
        self.write_manifest()
        with self.assertRaisesRegex(ValueError, "même code"):
            self.read()

    def test_final_certification_flags_are_rejected(self):
        for flag in ("fragment_complete", "external_audit", "canonical_injection"):
            with self.subTest(flag=flag):
                self.manifest[flag] = True
                self.write_manifest()
                with self.assertRaisesRegex(ValueError, "statut non final"):
                    self.read()
                self.manifest[flag] = False

    def test_symlink_source_file_and_directory_are_rejected(self):
        original = self.sources / "chapters/A41/A41_a.html"
        outside = self.base / "outside.html"
        outside.write_bytes(original.read_bytes())
        original.unlink()
        original.symlink_to(outside)
        with self.assertRaisesRegex(ValueError, "Lien symbolique interdit"):
            self.read()
        original.unlink()
        original.write_bytes(outside.read_bytes())
        (self.sources / "linked").symlink_to(self.base, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "Lien symbolique interdit"):
            self.read()

    def test_symlink_manifest_is_rejected(self):
        target = self.sources.parent / "manifest_interne.json"
        outside = self.base / "manifest.json"
        outside.write_bytes(target.read_bytes())
        target.unlink()
        target.symlink_to(outside)
        with self.assertRaisesRegex(ValueError, "manifeste ne peut"):
            self.read()

    def test_symlink_packet_parent_is_rejected(self):
        linked = self.base / "linked-packet"
        linked.symlink_to(self.sources.parent, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "dossier réel"):
            PREVIEW.read_sources(linked / "sources", ROOT)

    def test_protected_output_and_symlink_to_canonical_source_are_rejected(self):
        destinations = (ROOT / "chapters/A41/A41_a.html", ROOT / "shell/draft.html",
                        ROOT / "livraisons/draft.html", ROOT / "index.html", ROOT / "fragments/draft.html")
        for destination in destinations:
            with self.subTest(destination=destination):
                with self.assertRaises(ValueError):
                    PREVIEW.check_destination(ROOT, destination)
        linked = self.base / "linked.html"
        linked.symlink_to(ROOT / "chapters/A41/A41_a.html")
        with self.assertRaises(ValueError):
            PREVIEW.check_destination(ROOT, linked)
        self.assertEqual(PREVIEW.check_destination(ROOT, self.base / "preview.html"), self.base / "preview.html")

    def test_overlay_appends_new_chapter_and_clears_historical_certification(self):
        before = (ROOT / "chapters.json").read_bytes()
        manifest, files = self.read()
        overlay = self.base / "overlay"
        PREVIEW.create_overlay(ROOT, files, manifest, overlay)
        chapters = json.loads((overlay / "chapters.json").read_text())
        integrated = {row["code"]: row for row in chapters if row.get("integrated")}
        self.assertEqual(set(integrated), {"A41", "B24"})
        self.assertTrue(integrated["B24"]["work_in_progress"])
        self.assertEqual(integrated["B24"]["owner"], "T1")
        self.assertEqual((ROOT / "chapters.json").read_bytes(), before)
        self.assertTrue((overlay / "engine").is_symlink())
        self.assertEqual((overlay / "chapters/B24/B24_a.html").read_bytes(), files["chapters/B24/B24_a.html"])
        final_glossary = sorted((overlay / "glossary").glob("*.py"))[-1]
        self.assertTrue(final_glossary.name.endswith("_internal_work.py"))
        self.assertFalse(final_glossary.is_symlink())
        shadow = (overlay / "shell/data.py").read_text()
        self.assertIn("DONE_COURSES = set()\nDONE_SYS = set()", shadow)

    def test_compiled_courses_need_four_panels_each(self):
        self.assertEqual(PREVIEW.verify_output(pack_html(course_html("A41") + course_html("B24")), self.manifest), 0)
        for courses in (course_html("A41") + course_html("B24", ("pA", "pE", "pS")),
                        course_html("A41") + course_html("B24") + course_html("J45"),
                        course_html("A41") + course_html("A41") + course_html("B24")):
            with self.subTest(courses=courses[:60]):
                with self.assertRaises(ValueError):
                    PREVIEW.verify_output(pack_html(courses), self.manifest)

    def test_completed_status_in_output_is_rejected(self):
        source = pack_html(course_html("A41") + course_html("B24")).replace("MEDINA_COMPLETE=[]", 'MEDINA_COMPLETE=["A41"]')
        with self.assertRaisesRegex(ValueError, "cours achevé"):
            PREVIEW.verify_output(source, self.manifest)

    def test_unclosed_template_and_non_panel_ids_are_rejected(self):
        cases = ((course_html("A41") + course_html("B24"))[:-11],
                 course_html("A41") + course_html("B24").replace('class="panel"', 'class="unrelated"'))
        for courses in cases:
            with self.subTest(courses=courses[-60:]):
                with self.assertRaises(ValueError):
                    PREVIEW.verify_output(pack_html(courses), self.manifest)

    def test_real_compilation_is_atomic_isolated_and_marks_all_declared_chapters(self):
        # b24 is loaded before i48: the latter has a VIH definition concerning
        # anticoagulant interactions. The local definition must prevail anyway.
        for code, term in (("A41", "SOFA"), ("B24", "VIH")):
            path = f"glossary/{code.lower()}.py"
            content = ("G = " + repr({term: {"full": "Glossaire interne " + code + " prioritaire",
                      "def": "<p>Définition interne de consultation.</p>", "lit": [], "ref": None}}) + "\n").encode()
            (self.sources / path).write_bytes(content)
            for row in self.manifest["files"]:
                if row["path"] == path:
                    row["internal_sha256"] = hashlib.sha256(content).hexdigest()
            chapter_path = f"chapters/{code}/{code}_a.html"
            content = (self.sources / chapter_path).read_text().replace("Fixture technique sans contenu médical.", "Fixture technique " + term + ".").encode()
            (self.sources / chapter_path).write_bytes(content)
            for row in self.manifest["files"]:
                if row["path"] == chapter_path:
                    row["internal_sha256"] = hashlib.sha256(content).hexdigest()
        self.write_manifest()
        canonical = list((ROOT / "chapters").rglob("*")) + list((ROOT / "glossary").rglob("*"))
        canonical += [ROOT / "chapters.json", ROOT / "fragments.json", ROOT / "shell/data.py", ROOT / "organisation/course_groups.json"]
        before = {str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in canonical if path.is_file() and "__pycache__" not in path.parts}
        destination = self.base / "preview.html"
        destination.write_text("previous preview", encoding="utf-8")
        report = PREVIEW.build_preview(ROOT, self.sources, destination)
        self.assertEqual(report["chapter_codes"], ["A41", "B24"])
        source = destination.read_text(encoding="utf-8")
        metadata = json.loads(re.search(r"window\.MEDINA_WORK_PREVIEW=(.*?);</script>", source, re.S).group(1))
        self.assertEqual(metadata["chapter_codes"], ["A41", "B24"])
        for flag in ("fragment_complete", "final_validation", "external_audit", "canonical_injection"):
            self.assertIs(metadata[flag], False)
        organisation = json.loads(re.search(r'<script id="medina-category-organisation-data"[^>]*>(.*?)</script>', source, re.S).group(1))
        lessons = [lesson for block in organisation["blocks"] for lesson in block["lessons"] if lesson.get("integrated")]
        self.assertEqual({lesson["code"] for lesson in lessons}, {"A41", "B24"})
        self.assertTrue(all(lesson["work_in_progress"] for lesson in lessons))
        self.assertTrue(all(course["work_in_progress"] for course in organisation["courses"]))
        glossary = json.loads(re.search(r'<script id="medina-glossary"[^>]*>(.*?)</script>', source, re.S).group(1))
        self.assertEqual(glossary["VIH"]["full"], "Glossaire interne B24 prioritaire")
        self.assertEqual(glossary["SOFA"]["full"], "Glossaire interne A41 prioritaire")
        self.assertNotIn("anticoagulant", glossary["VIH"]["def"])
        self.assertIn("Version de travail · Infectiologie", source)
        self.assertIn("medina.fragment.T1.work.atlas", source)
        self.assertIn(".topbar{display:flex;flex-wrap:wrap}", source)
        self.assertEqual(destination.stat().st_mode & 0o777, 0o644)
        self.assertFalse(list(self.base.glob(".medina-*")))
        after = {path: hashlib.sha256(Path(path).read_bytes()).hexdigest() for path in before}
        self.assertEqual(before, after)
        # A failed rebuild must preserve the previously published consultation.
        previous = destination.read_bytes()
        (self.sources / "chapters/B24/B24_a.html").write_text("corrupted", encoding="utf-8")
        with self.assertRaises(ValueError):
            PREVIEW.build_preview(ROOT, self.sources, destination)
        self.assertEqual(destination.read_bytes(), previous)


if __name__ == "__main__":
    unittest.main()
