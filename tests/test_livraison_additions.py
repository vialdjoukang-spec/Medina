#!/usr/bin/env python3
"""Exercise new-source delivery, atomic collisions and complete rollback."""
import importlib.util
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SPEC = importlib.util.spec_from_file_location(
    "livraison_additions", Path(__file__).resolve().parents[1] / "tools/livraison.py")
DELIVERY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(DELIVERY)
SHA = "1" * 40


class AdditionTests(unittest.TestCase):
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
        self.write_json("chapters.json", [
            {"code": "I21", "title": "Infarctus aigu du myocarde", "integrated": True},
            {"code": "J45", "title": "Asthme", "integrated": True},
        ])
        entries = {"entries": [{"code": "I21", "system": "cardio"}, {"code": "J45", "system": "pneumo"}]}
        self.write("shell/medina_front.html", '<script id="medora-data" type="application/json">' + json.dumps(entries) + '</script>')
        self.original = '<section id="i21-original"><p>terme initial</p></section>'
        self.write("chapters/I21/I21_a.html", self.original)
        self.write("chapters/J45/J45_a.html", "<p>Contenu initial.</p>")
        DELIVERY.export_codex(self.root, "ALL", SHA)
        DELIVERY.prepare_claude(self.root, "S01")
        self.directory = self.root / "livraisons/Livraison Claude/C-01-Cardiologie"
        self.manifest_path = self.directory / "livraison.json"
        self.manifest = json.loads(self.manifest_path.read_text())

    def write(self, relative, value):
        file = self.root / relative
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(value, encoding="utf-8")
        return file

    def write_json(self, relative, value):
        return self.write(relative, json.dumps(value, ensure_ascii=False))

    def save_manifest(self):
        self.manifest_path.write_text(json.dumps(self.manifest, ensure_ascii=False))

    def add(self, target="chapters/I21/I21_annexe.html", content="<p>Source ajoutée.</p>"):
        self.write((self.directory / "sources" / target).relative_to(self.root), content)
        record = {"operation": "add", "target_path": target, "source_path": "sources/" + target,
                  "sha256": None, "proposed_sha256": DELIVERY.digest(content.encode("utf-8"))}
        self.manifest["files"].append(record)
        self.save_manifest()
        return record

    def bank(self, text="terme initial", anchor="i21-original"):
        return {"version": 1, "course": {"code": "I21", "title": "Infarctus aigu du myocarde"},
                "entries": [{"id": "i21-j-fixture", "title": "Explication de test",
                             "explanation": ["Texte de fixture."], "mechanism": ["Mécanisme de fixture."],
                             "implication": "Conséquence de fixture.", "limits": [],
                             "match": [{"file": "I21_a.html", "anchor": anchor, "text": text}],
                             "sources": [{"title": "Source de fixture", "url": "https://example.org/fixture"}]}]}

    def test_html_and_json_additions_are_read_only_at_check_and_created_0644(self):
        targets = ["chapters/I21/I21_annexe.html", "chapters/I21/I21_annexe.json"]
        self.add(targets[0])
        self.add(targets[1], '{"notes":"Fichier nouveau"}')
        checked = DELIVERY.check_claude(self.root, self.directory)
        self.assertEqual(checked["added_files"], targets)
        self.assertTrue(all(not (self.root / target).exists() for target in targets))
        applied = DELIVERY.apply_claude(self.root, self.directory)
        receipt = json.loads((self.root / applied["receipt"]).read_text())
        for target, record in zip(targets, receipt["files"]):
            path = self.root / target
            self.assertEqual(path.read_bytes(), (self.directory / "sources" / target).read_bytes())
            self.assertEqual(path.stat().st_mode & 0o777, 0o644)
            self.assertEqual(record["operation"], "add")
            self.assertIsNone(record["original_sha256"])
            self.assertEqual(record["proposed_sha256"], DELIVERY.digest(path.read_bytes()))

    def test_new_bank_compiles_only_after_all_replacements_are_injected(self):
        proposed = '<section id="i21-livre"><p>terme livré</p></section>'
        self.write((self.directory / "sources/chapters/I21/I21_a.html").relative_to(self.root), proposed)
        self.add("chapters/I21/I21_justifications.json", json.dumps(self.bank("terme livré", "i21-livre")))
        with patch.object(DELIVERY, "check_injected_justifications", side_effect=AssertionError("Lecture seule")):
            DELIVERY.check_claude(self.root, self.directory)
        applied = DELIVERY.apply_claude(self.root, self.directory)
        receipt = json.loads((self.root / applied["receipt"]).read_text())
        self.assertEqual(receipt["checks"][0]["course"], "I21")
        self.assertEqual(receipt["checks"][0]["windows"], 1)
        self.assertEqual(receipt["checks"][0]["targets"], 1)
        self.assertEqual((self.root / "chapters/I21/I21_a.html").read_text(), proposed)

    def test_invalid_bank_is_technically_readable_but_apply_rolls_back(self):
        target = "chapters/I21/I21_justifications.json"
        self.add(target, json.dumps(self.bank("texte absent")))
        DELIVERY.check_claude(self.root, self.directory)
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "Compilation.*I21"):
            DELIVERY.apply_claude(self.root, self.directory)
        self.assertFalse((self.root / target).exists())
        self.assertEqual((self.root / "chapters/I21/I21_a.html").read_text(), self.original)
        self.assertFalse(any(self.root.rglob(".livraison-*")))
        self.assertFalse((self.root / "docs/collaboration/receipts").exists())

    def test_existing_canonical_is_never_disguised_as_addition(self):
        target = "chapters/I21/I21_annexe.html"
        self.add(target)
        canonical = self.write(target, "Contribution déjà présente")
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "Collision"):
            DELIVERY.apply_claude(self.root, self.directory)
        self.assertEqual(canonical.read_text(), "Contribution déjà présente")

    def test_concurrent_creation_after_inspection_is_preserved(self):
        target = "chapters/I21/I21_annexe.html"
        self.add(target)
        chmod = DELIVERY.os.chmod
        def create_concurrently(path, mode):
            chmod(path, mode)
            self.write(target, "Création concurrente")
        with patch.object(DELIVERY.os, "chmod", side_effect=create_concurrently):
            with self.assertRaisesRegex(DELIVERY.DeliveryError, "Collision concurrente"):
                DELIVERY.apply_claude(self.root, self.directory)
        self.assertEqual((self.root / target).read_text(), "Création concurrente")
        self.assertFalse(any(self.root.rglob(".livraison-*")))

    def test_atomic_addition_does_not_overwrite_a_last_instant_collision(self):
        target = "chapters/I21/I21_annexe.html"
        self.add(target)
        link = DELIVERY.os.link
        def collide(source, destination):
            self.write(target, "Collision au dernier instant")
            return link(source, destination)
        with patch.object(DELIVERY.os, "link", side_effect=collide):
            with self.assertRaisesRegex(DELIVERY.DeliveryError, "Collision lors de l'ajout"):
                DELIVERY.apply_claude(self.root, self.directory)
        self.assertEqual((self.root / target).read_text(), "Collision au dernier instant")
        self.assertFalse(any(self.root.rglob(".livraison-*")))

    def test_other_fragment_and_unannounced_course_are_rejected(self):
        self.add("chapters/J45/J45_annexe.json", "{}")
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "hors des cours autorisés"):
            DELIVERY.check_claude(self.root, self.directory)
        self.manifest["chapters"].append({"code": "J45", "title": "Asthme"})
        self.save_manifest()
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "Code ou titre de cours incohérent"):
            DELIVERY.check_claude(self.root, self.directory)

    def test_unknown_course_cannot_be_announced_with_null_title(self):
        self.add("chapters/J45/J45_annexe.json", "{}")
        self.manifest["chapters"].append({"code": "J45", "title": None})
        self.save_manifest()
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "Code ou titre de cours incohérent"):
            DELIVERY.apply_claude(self.root, self.directory)
        self.assertFalse((self.root / "chapters/J45/J45_annexe.json").exists())

    def test_existing_bank_recompiles_when_only_its_html_changes(self):
        bank = self.write_json("chapters/I21/I21_justifications.json", self.bank())
        bank_bytes = bank.read_bytes()
        self.write((self.directory / "sources/chapters/I21/I21_a.html").relative_to(self.root), "<p>Ancre supprimée.</p>")
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "Compilation.*I21"):
            DELIVERY.apply_claude(self.root, self.directory)
        self.assertEqual((self.root / "chapters/I21/I21_a.html").read_text(), self.original)
        self.assertEqual(bank.read_bytes(), bank_bytes)

    def test_proposed_hash_is_mandatory_and_cannot_be_faked(self):
        record = self.add()
        for value in (None, "invalid", "0" * 64):
            with self.subTest(value=value):
                record["proposed_sha256"] = value
                self.save_manifest()
                with self.assertRaises(DELIVERY.DeliveryError):
                    DELIVERY.check_claude(self.root, self.directory)
        del record["proposed_sha256"]
        self.save_manifest()
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "SHA invalide"):
            DELIVERY.check_claude(self.root, self.directory)

    def test_explicit_add_and_null_original_hash_are_required(self):
        record = self.add()
        for field, value in (("operation", "replace"), ("operation", "unknown"), ("sha256", "0" * 64)):
            with self.subTest(field=field, value=value):
                record["operation"], record["sha256"] = "add", None
                record[field] = value
                self.save_manifest()
                with self.assertRaises(DELIVERY.DeliveryError):
                    DELIVERY.check_claude(self.root, self.directory)
        record["operation"] = "add"
        del record["sha256"]
        self.save_manifest()
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "sha256:null"):
            DELIVERY.check_claude(self.root, self.directory)

    def test_unsafe_names_paths_and_duplicate_records_are_rejected(self):
        record = self.add()
        target = record["target_path"]
        for invalid in ("../outside.json", "chapters/I21/I21_annexe.js", "chapters/I21/J45_annexe.json",
                        "chapters/I21/annexe.json", "chapters/I21/nested/I21_annexe.json"):
            with self.subTest(target=invalid):
                record["target_path"] = invalid
                record["source_path"] = "sources/" + invalid
                self.save_manifest()
                with self.assertRaises(DELIVERY.DeliveryError):
                    DELIVERY.check_claude(self.root, self.directory)
        record["target_path"], record["source_path"] = target, "sources/" + target
        self.manifest["files"].append(dict(record))
        self.save_manifest()
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "déclaré deux fois"):
            DELIVERY.check_claude(self.root, self.directory)

    def test_payload_and_canonical_symlinks_are_rejected(self):
        record = self.add()
        canonical = self.root / record["target_path"]
        outside = self.write("outside.txt", "Contenu extérieur")
        canonical.symlink_to(outside)
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "Lien symbolique"):
            DELIVERY.check_claude(self.root, self.directory)
        canonical.unlink()
        payload = self.directory / record["source_path"]
        payload.unlink()
        payload.symlink_to(outside)
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "Lien symbolique"):
            DELIVERY.check_claude(self.root, self.directory)
        self.assertEqual(outside.read_text(), "Contenu extérieur")

    def test_late_receipt_error_removes_addition_and_restores_replacement(self):
        target = "chapters/I21/I21_annexe.html"
        self.add(target)
        self.write((self.directory / "sources/chapters/I21/I21_a.html").relative_to(self.root), "<p>Texte corrigé.</p>")
        write_bytes = Path.write_bytes
        def fail_receipt(path, data):
            if path.parent.name == "receipts":
                raise OSError("Échec tardif du reçu")
            return write_bytes(path, data)
        with patch.object(Path, "write_bytes", fail_receipt):
            with self.assertRaisesRegex(OSError, "Échec tardif"):
                DELIVERY.apply_claude(self.root, self.directory)
        self.assertFalse((self.root / target).exists())
        self.assertEqual((self.root / "chapters/I21/I21_a.html").read_text(), self.original)
        self.assertTrue((self.directory / "sources" / target).exists())
        self.assertFalse(any(self.root.rglob(".livraison-*")))

    def test_rollback_preserves_a_file_replaced_by_someone_else(self):
        target = "chapters/I21/I21_annexe.html"
        self.add(target)
        def fail_after_concurrent_replacement(root, changes):
            other = self.write("concurrent.html", "Fichier indépendant")
            os.replace(other, self.root / target)
            raise DELIVERY.DeliveryError("Échec après création concurrente")
        with patch.object(DELIVERY, "check_injected_justifications", side_effect=fail_after_concurrent_replacement):
            with self.assertRaisesRegex(DELIVERY.DeliveryError, "création concurrente"):
                DELIVERY.apply_claude(self.root, self.directory)
        self.assertEqual((self.root / target).read_text(), "Fichier indépendant")
        self.assertFalse(any(self.root.rglob(".livraison-*")))

    def test_rollback_preserves_a_replacement_between_stat_and_rename(self):
        target = "chapters/I21/I21_annexe.html"
        self.add(target)
        canonical = self.root / target
        replace = DELIVERY.os.replace
        def race(source, destination):
            if Path(source) == canonical and Path(destination).name.startswith(".livraison-rollback-"):
                other = self.write("concurrent.html", "Écriture entre stat et renommage")
                replace(other, canonical)
            return replace(source, destination)
        with patch.object(DELIVERY, "check_injected_justifications", side_effect=DELIVERY.DeliveryError("Échec tardif")):
            with patch.object(DELIVERY.os, "replace", side_effect=race):
                with self.assertRaisesRegex(DELIVERY.DeliveryError, "Échec tardif"):
                    DELIVERY.apply_claude(self.root, self.directory)
        self.assertEqual(canonical.read_text(), "Écriture entre stat et renommage")
        self.assertFalse(any(self.root.rglob(".livraison-*")))

    def test_injected_addition_can_be_exported_and_prepared_again(self):
        target = "chapters/I21/I21_annexe.json"
        self.add(target, '{"notes":"Fichier nouveau"}')
        DELIVERY.apply_claude(self.root, self.directory)
        DELIVERY.export_codex(self.root, "S01", "2" * 40)
        DELIVERY.prepare_claude(self.root, "S01")
        manifest = json.loads(self.manifest_path.read_text())
        record = next(record for record in manifest["files"] if record["target_path"] == target)
        self.assertEqual(record["sha256"], DELIVERY.digest((self.root / target).read_bytes()))
        self.assertNotIn("operation", record)


if __name__ == "__main__":
    unittest.main()
