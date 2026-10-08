#!/usr/bin/env python3
"""Bootstrap de cours annoncé ; exports stricts et ajouts sans écrasement."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SPEC = importlib.util.spec_from_file_location(
    "livraison_new_course", Path(__file__).resolve().parents[1] / "tools/livraison.py")
DELIVERY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(DELIVERY)
SHA = "1" * 40
SUFFIXES = ("a", "b", "c", "d", "pop1", "pop2", "pop3", "pop4")


class NewCourseTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.write_json("fragments.json", [
            {"id": "S01", "slug": "cardio", "rattachements": ["cardio"]},
            {"id": "S02", "slug": "pneumo", "rattachements": ["pneumo"]},
        ])
        self.write_json("organisation/fragments.json", [
            {"id": "S01", "label": "C-01-Cardiologie", "specialty": "Cardiologie"},
            {"id": "S02", "label": "P-02-Pneumologie", "specialty": "Pneumologie"},
        ])
        self.chapters = [{"code": "I21", "title": "Infarctus", "integrated": True}]
        self.write_json("chapters.json", self.chapters)
        self.write("shell/medina_front.html", '<script id="medora-data" type="application/json">'
                   + json.dumps({"entries": [{"code": "I21", "system": "cardio"},
                                             {"code": "I51", "system": "cardio"},
                                             {"code": "I70", "system": "cardio"},
                                             {"code": "J45", "system": "pneumo"}]}) + '</script>')
        self.original = "<p>Contenu canonique conservé.</p>"
        self.write("chapters/I21/I21_a.html", self.original)
        DELIVERY.export_codex(self.root, "S01", SHA)
        self.declaration = {"code": "I51", "title": "Complications des cardiopathies",
                            "integrated": True, "provisional": True, "owner": "S01"}
        self.chapters.append(self.declaration)
        self.write_json("chapters.json", self.chapters)
        self.directory = self.root / "packet"
        self.manifest = {"schema_version": 1, "kind": "claude_contribution", "author": "Claude",
                         "source_commit": SHA,
                         "fragment": {"id": "S01", "label": "C-01-Cardiologie"},
                         "chapters": [{"code": "I51", "title": self.declaration["title"]}], "files": []}
        for suffix in SUFFIXES:
            target = f"chapters/I51/I51_{suffix}.html"
            content = f"<section><p>Source complète de fixture {suffix}.</p></section>"
            self.write("packet/sources/" + target, content)
            self.manifest["files"].append({"target_path": target, "source_path": "sources/" + target,
                                           "operation": "add", "sha256": None,
                                           "proposed_sha256": DELIVERY.digest(content.encode())})
        self.save()

    def write(self, relative, content):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def write_json(self, relative, content):
        return self.write(relative, json.dumps(content, ensure_ascii=False))

    def save(self):
        self.write_json("packet/livraison.json", self.manifest)

    def check(self):
        return DELIVERY.check_claude(self.root, self.directory)

    def test_complete_packet_is_read_only_then_creates_exact_eight_sources(self):
        checked = self.check()
        self.assertEqual(checked["bootstrapped_courses"], ["I51"])
        self.assertEqual(checked["verified_files"], 8)
        self.assertFalse((self.root / "chapters/I51").exists())
        applied = DELIVERY.apply_claude(self.root, self.directory)
        self.assertEqual(applied["bootstrapped_courses"], ["I51"])
        receipt = json.loads((self.root / applied["receipt"]).read_text())
        self.assertEqual(receipt["bootstrapped_courses"], ["I51"])
        self.assertIn("contrôles à faire", receipt["status"])
        self.assertIsNone(receipt["integration_commit"])
        self.assertEqual(receipt["publication"], "non effectuée par cet outil")
        self.assertEqual(len(list((self.root / "chapters/I51").iterdir())), 8)
        for entry in self.manifest["files"]:
            canonical = self.root / entry["target_path"]
            self.assertEqual(canonical.read_bytes(), (self.directory / entry["source_path"]).read_bytes())
            self.assertEqual(canonical.stat().st_mode & 0o777, 0o644)
        self.assertEqual((self.root / "chapters/I21/I21_a.html").read_text(), self.original)

    def test_existing_empty_course_directory_is_allowed(self):
        (self.root / "chapters/I51").mkdir()
        self.assertEqual(self.check()["bootstrapped_courses"], ["I51"])
        self.assertEqual(DELIVERY.apply_claude(self.root, self.directory)["verified_files"], 8)

    def test_exports_and_preparation_still_refuse_missing_canonical_sources(self):
        for call in (lambda: DELIVERY.export_codex(self.root, "S01", SHA),
                     lambda: DELIVERY.prepare_claude(self.root, "S01")):
            with self.subTest(call=call):
                with self.assertRaisesRegex(DELIVERY.DeliveryError, "Dossier de cours absent"):
                    call()
        (self.root / "chapters/I51").mkdir()
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "Aucun HTML source"):
            DELIVERY.export_codex(self.root, "S01", SHA)

    def test_declared_owner_and_provisional_status_are_mandatory(self):
        for key, value in (("owner", "S02"), ("owner", None), ("provisional", False),
                           ("provisional", None), ("provisional", 1)):
            original = self.declaration[key]
            self.declaration[key] = value
            self.write_json("chapters.json", self.chapters)
            with self.subTest(key=key, value=value):
                with self.assertRaisesRegex(DELIVERY.DeliveryError, "Création non déclarée"):
                    self.check()
            self.declaration[key] = original
        self.write_json("chapters.json", self.chapters)
        self.manifest["chapters"][0]["owner_fragment"] = "S02"
        self.save()
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "appartenance incohérente"):
            self.check()

    def test_course_must_be_in_catalog_and_announced_once_with_exact_title(self):
        self.chapters.remove(self.declaration)
        self.write_json("chapters.json", self.chapters)
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "Code ou titre"):
            self.check()
        self.chapters.append(self.declaration)
        self.write_json("chapters.json", self.chapters)
        self.manifest["chapters"][0]["title"] = "Autre titre"
        self.save()
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "Code ou titre"):
            self.check()
        self.manifest["chapters"][0]["title"] = self.declaration["title"]
        self.manifest["chapters"].append(dict(self.manifest["chapters"][0]))
        self.save()
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "plusieurs fois"):
            self.check()

    def test_missing_duplicate_or_extra_record_is_not_complete(self):
        original = list(self.manifest["files"])
        for entries in (original[:-1], original[:-1] + [original[0]], original + [original[0]]):
            self.manifest["files"] = entries
            self.save()
            with self.subTest(count=len(entries)):
                with self.assertRaisesRegex(DELIVERY.DeliveryError, "huit HTML"):
                    self.check()
        extra = dict(original[-1], target_path="chapters/I51/I51_annexe.json")
        self.manifest["files"] = original + [extra]
        self.save()
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "huit HTML"):
            self.check()

    def test_all_creation_records_need_explicit_add_null_baseline_and_exact_hash(self):
        entry = self.manifest["files"][0]
        original = dict(entry)
        for changes in ({"operation": "replace"}, {"sha256": "0" * 64},
                        {"proposed_sha256": None}, {"proposed_sha256": "0" * 64},
                        {"source_path": "sources/chapters/I51/I51_b.html"}):
            entry.clear()
            entry.update(original)
            entry.update(changes)
            self.save()
            with self.subTest(changes=changes):
                with self.assertRaises(DELIVERY.DeliveryError):
                    self.check()
        entry.clear()
        entry.update(original)
        del entry["operation"]
        self.save()
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "operation:add"):
            self.check()

    def test_missing_empty_whitespace_and_invalid_utf8_payloads_are_rejected(self):
        entry = self.manifest["files"][0]
        payload = self.directory / entry["source_path"]
        original = payload.read_bytes()
        payload.unlink()
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "Fichier livré absent"):
            self.check()
        for content in (b"", b" \n\t", b"\xff"):
            payload.write_bytes(content)
            entry["proposed_sha256"] = DELIVERY.digest(content)
            self.save()
            with self.subTest(content=content):
                with self.assertRaisesRegex(DELIVERY.DeliveryError, "vide|invalide"):
                    self.check()
        payload.write_bytes(original)

    def test_partial_existing_html_json_or_target_collision_is_preserved(self):
        for filename in ("I51_a.html", "I51_annexe.html", "I51_notes.json"):
            path = self.write("chapters/I51/" + filename, "Contenu concurrent à conserver")
            with self.subTest(filename=filename):
                with self.assertRaisesRegex(DELIVERY.DeliveryError, "Collision"):
                    self.check()
                self.assertEqual(path.read_text(), "Contenu concurrent à conserver")
            path.unlink()

    def test_bootstrap_does_not_skip_other_course_missing_sources(self):
        self.chapters.append({"code": "I70", "title": "Athérosclérose", "integrated": True})
        self.write_json("chapters.json", self.chapters)
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "Dossier de cours absent.*I70"):
            self.check()
        self.assertFalse((self.root / "chapters/I51").exists())

    def test_foreign_course_and_symlink_cannot_bootstrap(self):
        self.manifest["chapters"][0] = {"code": "J45", "title": "Asthme"}
        self.chapters.append({"code": "J45", "title": "Asthme", "integrated": True,
                              "owner": "S02", "provisional": True})
        self.write_json("chapters.json", self.chapters)
        self.save()
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "Code ou titre"):
            self.check()
        self.manifest["chapters"][0] = {"code": "I51", "title": self.declaration["title"]}
        self.save()
        payload = self.directory / self.manifest["files"][0]["source_path"]
        payload.unlink()
        payload.symlink_to(self.root / "chapters/I21/I21_a.html")
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "Lien symbolique"):
            self.check()

    def test_failure_rolls_back_eight_additions_and_owned_empty_directory(self):
        with patch.object(DELIVERY, "check_injected_justifications", side_effect=RuntimeError("échec tardif")):
            with self.assertRaisesRegex(RuntimeError, "échec tardif"):
                DELIVERY.apply_claude(self.root, self.directory)
        self.assertFalse((self.root / "chapters/I51").exists())
        self.assertEqual((self.root / "chapters/I21/I21_a.html").read_text(), self.original)
        self.assertFalse(any(self.root.rglob(".livraison-*")))

    def test_concurrent_unannounced_source_after_staging_blocks_bootstrap(self):
        chmod = DELIVERY.os.chmod
        def introduce_concurrent_source(path, mode):
            chmod(path, mode)
            self.write("chapters/I51/I51_concurrent.html", "Contribution concurrente")
        with patch.object(DELIVERY.os, "chmod", side_effect=introduce_concurrent_source):
            with self.assertRaisesRegex(DELIVERY.DeliveryError, "Collision concurrente de sources"):
                DELIVERY.apply_claude(self.root, self.directory)
        self.assertEqual((self.root / "chapters/I51/I51_concurrent.html").read_text(), "Contribution concurrente")
        self.assertEqual(len(list((self.root / "chapters/I51").iterdir())), 1)
        self.assertFalse(any(self.root.rglob(".livraison-*")))

    def test_last_instant_collision_does_not_overwrite_concurrent_source(self):
        link = DELIVERY.os.link
        target = self.root / self.manifest["files"][1]["target_path"]
        def collide(source, destination):
            if Path(destination) == target:
                target.write_text("Contribution concurrente")
            return link(source, destination)
        with patch.object(DELIVERY.os, "link", side_effect=collide):
            with self.assertRaisesRegex(DELIVERY.DeliveryError, "Collision lors de l'ajout"):
                DELIVERY.apply_claude(self.root, self.directory)
        self.assertEqual(target.read_text(), "Contribution concurrente")
        self.assertEqual(len(list((self.root / "chapters/I51").iterdir())), 1)
        self.assertFalse(any(self.root.rglob(".livraison-*")))


if __name__ == "__main__":
    unittest.main()
