#!/usr/bin/env python3
"""Exercise source handoff and lost-update protection using disposable repositories."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location("livraison", Path(__file__).resolve().parents[1] / "tools/livraison.py")
DELIVERY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(DELIVERY)
SHA = "1" * 40


class DeliveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.write_json("fragments.json", [
            {"id": "S01", "slug": "cardio", "rattachements": ["cardio"]},
            {"id": "S02", "slug": "pneumo", "rattachements": ["pneumo"]},
        ])
        self.write_json("organisation/fragments.json", [
            {"id": "S01", "label": "C-01-Cardiologie", "specialty": "Cardiologie", "order": 1},
            {"id": "S02", "label": "P-02-Pneumologie", "specialty": "Pneumologie", "order": 2},
        ])
        self.write_json("chapters.json", [
            {"code": "I21", "title": "Infarctus aigu du myocarde", "integrated": True, "covers": ["I21", "I22"]},
            {"code": "J45", "title": "Asthme", "integrated": True, "covers": ["J45", "J46"]},
        ])
        entries = {"entries": [{"code": "I21", "system": "cardio"}, {"code": "J45", "system": "pneumo"}]}
        self.write("shell/medina_front.html", '<script id="medora-data" type="application/json">' + json.dumps(entries) + '</script>')
        self.write("chapters/I21/a.html", "<p>Texte cardiologique initial.</p>")
        self.write("chapters/I21/b.html", "<p>Questions cardiologiques.</p>")
        self.write_json("chapters/I21/pop_sciences_revision.json", {"contenu": "Initial"})
        self.write("chapters/J45/a.html", "<p>Texte pulmonaire initial.</p>")
        self.codex = self.root / "livraisons/Livraison Codex/C-01-Cardiologie"
        self.claude = self.root / "livraisons/Livraison Claude/C-01-Cardiologie"

    def write(self, relative, value):
        file = self.root / relative
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(value, encoding="utf-8")
        return file

    def write_json(self, relative, value):
        return self.write(relative, json.dumps(value, ensure_ascii=False))

    def prepare(self):
        DELIVERY.export_codex(self.root, "ALL", SHA)
        DELIVERY.prepare_claude(self.root, "S01")
        return json.loads((self.claude / "livraison.json").read_text())

    def manifest(self, value):
        (self.claude / "livraison.json").write_text(json.dumps(value, ensure_ascii=False))

    def propose(self, relative="chapters/I21/a.html", value="<p>Texte cardiologique relu.</p>"):
        file = self.claude / "sources" / relative
        file.write_text(value)
        return file

    def test_export_has_complete_sources_and_lesson_names(self):
        result = DELIVERY.export_codex(self.root, "ALL", SHA)
        self.assertEqual(result["source_files"], 4)
        manifest = json.loads((self.codex / "livraison.json").read_text())
        self.assertEqual(manifest["fragment"]["label"], "C-01-Cardiologie")
        self.assertEqual(manifest["chapters"][0]["title"], "Infarctus aigu du myocarde")
        self.assertIn("CIM-11 non", manifest["code_reference"])
        self.assertIn("partiel", manifest["status"])
        for record in manifest["files"]:
            self.assertEqual((self.codex / record["source_path"]).read_bytes(), (self.root / record["target_path"]).read_bytes())
        self.assertTrue((self.claude / "livraison.template.json").exists())
        self.assertFalse((self.claude / "livraison.json").exists())

    def test_unchanged_work_copy_is_not_a_delivery(self):
        self.prepare()
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "Aucune source corrigée"):
            DELIVERY.check_claude(self.root, self.claude)

    def test_check_is_read_only_and_apply_records_pending_controls(self):
        self.prepare()
        before = (self.root / "chapters/I21/a.html").read_bytes()
        corrected = self.propose().read_bytes()
        result = DELIVERY.check_claude(self.root, self.claude)
        self.assertEqual(result["changed_files"], ["chapters/I21/a.html"])
        self.assertEqual((self.root / "chapters/I21/a.html").read_bytes(), before)
        result = DELIVERY.apply_claude(self.root, self.claude)
        self.assertEqual((self.root / "chapters/I21/a.html").read_bytes(), corrected)
        receipt = json.loads((self.root / result["receipt"]).read_text())
        self.assertIn("contrôles à faire", receipt["status"])
        self.assertIsNone(receipt["integration_commit"])
        self.assertEqual(receipt["checks"], [])
        self.assertEqual(receipt["files"][0]["original_sha256"], DELIVERY.digest(before))
        self.assertEqual(receipt["files"][0]["proposed_sha256"], DELIVERY.digest(corrected))

    def test_canonical_change_prevents_injection(self):
        self.prepare()
        self.propose()
        current = self.write("chapters/I21/a.html", "<p>Correction concurrente.</p>").read_bytes()
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "Source canonique modifiée"):
            DELIVERY.apply_claude(self.root, self.claude)
        self.assertEqual((self.root / "chapters/I21/a.html").read_bytes(), current)
        self.assertFalse((self.root / "docs/collaboration/receipts").exists())

    def test_prepare_claude_preserves_modified_work_copy(self):
        self.prepare()
        self.propose()
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "Copie modifiée"):
            DELIVERY.prepare_claude(self.root, "S01")
        self.assertIn("relu", (self.claude / "sources/chapters/I21/a.html").read_text())

    def test_all_exports_validate_before_any_write(self):
        DELIVERY.export_codex(self.root, "ALL", SHA)
        before = (self.codex / "sources/chapters/I21/a.html").read_bytes()
        self.write("chapters/I21/a.html", "<p>Nouvelle source canonique.</p>")
        pulmonary = self.root / "livraisons/Livraison Codex/P-02-Pneumologie/sources/chapters/J45/a.html"
        pulmonary.write_text("<p>Modification manuelle à préserver.</p>")
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "Copie modifiée"):
            DELIVERY.export_codex(self.root, "ALL", SHA)
        self.assertEqual((self.codex / "sources/chapters/I21/a.html").read_bytes(), before)
        self.assertIn("préserver", pulmonary.read_text())

    def test_stale_codex_packet_cannot_prepare_claude(self):
        self.prepare()
        self.write("chapters/I21/b.html", "<p>Nouvelle question canonique.</p>")
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "Base Codex périmée"):
            DELIVERY.prepare_claude(self.root, "S01")

    def test_empty_second_payload_blocks_all_injection(self):
        self.prepare()
        before = (self.root / "chapters/I21/a.html").read_bytes()
        self.propose()
        self.propose("chapters/I21/b.html", "")
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "Fichier livré vide"):
            DELIVERY.apply_claude(self.root, self.claude)
        self.assertEqual((self.root / "chapters/I21/a.html").read_bytes(), before)

    def test_json_payload_and_proposed_hash_are_checked(self):
        manifest = self.prepare()
        self.propose("chapters/I21/pop_sciences_revision.json", "{invalide}")
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "Source livrée invalide"):
            DELIVERY.check_claude(self.root, self.claude)
        self.propose("chapters/I21/pop_sciences_revision.json", '{"contenu":"Corrigé"}')
        for record in manifest["files"]:
            if record["target_path"].endswith(".json"):
                record["proposed_sha256"] = "0" * 64
        self.manifest(manifest)
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "Empreinte du fichier corrigé incohérente"):
            DELIVERY.check_claude(self.root, self.claude)

    def test_traversal_duplicate_and_wrong_fragment_are_rejected(self):
        manifest = self.prepare()
        self.propose()
        original = json.loads(json.dumps(manifest))
        manifest["files"][0]["target_path"] = "../outside.html"
        self.manifest(manifest)
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "traversée"):
            DELIVERY.check_claude(self.root, self.claude)
        manifest = json.loads(json.dumps(original))
        manifest["files"].append(dict(manifest["files"][0]))
        self.manifest(manifest)
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "déclaré deux fois"):
            DELIVERY.check_claude(self.root, self.claude)
        original["fragment"]["label"] = "Cardiologie"
        self.manifest(original)
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "nom du fragment"):
            DELIVERY.check_claude(self.root, self.claude)

    def test_symlink_payload_is_rejected(self):
        self.prepare()
        target = self.claude / "sources/chapters/I21/a.html"
        target.unlink()
        target.symlink_to(self.root / "chapters/I21/a.html")
        with self.assertRaisesRegex(DELIVERY.DeliveryError, "Lien symbolique"):
            DELIVERY.check_claude(self.root, self.claude)

    def test_apply_rolls_back_if_a_replacement_fails(self):
        self.prepare()
        before = {name: (self.root / name).read_bytes() for name in ["chapters/I21/a.html", "chapters/I21/b.html"]}
        self.propose()
        self.propose("chapters/I21/b.html", "<p>Questions relues.</p>")
        real_replace = DELIVERY.os.replace
        calls = []
        def fail_second(source, target):
            calls.append(target)
            if len(calls) == 2:
                raise OSError("Panne de remplacement simulée")
            return real_replace(source, target)
        with patch.object(DELIVERY.os, "replace", side_effect=fail_second):
            with self.assertRaisesRegex(OSError, "Panne de remplacement"):
                DELIVERY.apply_claude(self.root, self.claude)
        self.assertTrue(all((self.root / name).read_bytes() == value for name, value in before.items()))
        self.assertFalse(any(self.root.rglob(".livraison-*")))
        self.assertFalse((self.root / "docs/collaboration/receipts").exists())


if __name__ == "__main__":
    unittest.main()
