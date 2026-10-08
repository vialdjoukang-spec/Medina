#!/usr/bin/env python3
"""Contrôles du transfert de nouveaux cours et de son retour arrière."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch


SPEC = importlib.util.spec_from_file_location(
    "new_course_delivery", Path(__file__).resolve().parents[1] / "tools/new_course_delivery.py")
D = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(D)


class NewCourseTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.write("chapters.json", '[{"code":"I80","title":"Thrombose","integrated":true}]')
        self.write("fragments.json", json.dumps([
            {"id": "S01", "rattachements": ["I80"], "categories": [
                {"id": "vaisseaux", "chapters": ["I80"]},
                {"id": "pression", "chapters": []}]}]))
        self.write("chapters/I80/I80_pop.html", '<template data-pop="i80-echo"></template>')
        self.write("shell/medina_front.html", '<span id="shared-heading">Titre partagé</span>')
        self.write("chapters/I83/I83_a.html", '<template id="ch-I83"><div id="pA">'
                   '<button data-k="i83-local">Local</button>'
                   '<button data-k="i80-echo">Partagé</button>'
                   '<a href="#/entry/I80">Thrombose</a>'
                   '<button aria-controls="pE" data-p="pE">Examens</button>'
                   '<p aria-labelledby="shared-heading">Texte</p></div></template>')
        self.write("chapters/I83/I83_b.html", '<section id="pE">Examens</section>')
        self.write("chapters/I83/I83_c.html", '<section id="pS">Sciences</section>')
        self.write("chapters/I83/I83_d.html", '<section id="pP">Traitements</section>')
        self.write("chapters/I83/I83_pop.html", '<template data-pop="i83-local">Explication</template>')
        self.write("glossary/i83.py", "from cardio_1 import a\na('ET', [], 'Écho', '', 'i80-echo')\n")
        self.write("rapport.md", "# I83 — Varices\nSources et réserves médicales.\n")

    def write(self, relative, text):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def packet(self):
        return D.package(self.root, "I83", "Varices des membres inférieurs", ["I83"],
                         "vaisseaux", "rapport.md", "1" * 40)

    def destination_ready(self):
        directory = self.packet()
        shutil.rmtree(self.root / "chapters/I83")
        (self.root / "glossary/i83.py").unlink()
        return directory

    def edit_manifest(self, directory, edit):
        path = directory / "livraison.json"
        data = json.loads(path.read_text())
        edit(data)
        path.write_bytes(D.json_bytes(data))

    def test_registration_shared_references_and_receipt(self):
        directory = self.destination_ready()
        _, _, checks = D.check(self.root, directory)
        self.assertEqual(checks["shared_popup_references"], ["i80-echo"])
        receipt = D.apply(self.root, directory)
        chapters = json.loads((self.root / "chapters.json").read_text())
        self.assertEqual(chapters[-1], {"code": "I83", "title": "Varices des membres inférieurs",
                                      "covers": ["I83"], "integrated": True})
        fragment = json.loads((self.root / "fragments.json").read_text())[0]
        self.assertIn("I83", fragment["rattachements"])
        self.assertEqual(fragment["categories"][0]["chapters"], ["I80", "I83"])
        self.assertEqual(fragment["categories"][1]["chapters"], [])
        self.assertTrue((self.root / "glossary/i83.py").is_file())
        self.assertEqual(json.loads(receipt.read_text())["status"],
                         "injecté, reconstruction/contrôles à faire")
        with self.assertRaises(D.DeliveryError):
            D.apply(self.root, directory)

    def test_existing_source_collision_is_preserved(self):
        directory = self.packet()
        original = (self.root / "chapters/I83/I83_a.html").read_bytes()
        with self.assertRaisesRegex(D.DeliveryError, "Collision"):
            D.apply(self.root, directory)
        self.assertEqual((self.root / "chapters/I83/I83_a.html").read_bytes(), original)

    def test_existing_cover_alias_cannot_be_reassigned(self):
        directory = self.destination_ready()
        self.edit_manifest(directory, lambda m: m["course"].update(covers=["I83", "I80"]))
        with self.assertRaisesRegex(D.DeliveryError, "déjà couvertes"):
            D.apply(self.root, directory)
        self.assertFalse((self.root / "chapters/I83").exists())

    def test_transaction_rollback_after_first_catalog(self):
        directory = self.destination_ready()
        originals = {name: (self.root / name).read_bytes() for name in ("chapters.json", "fragments.json")}
        real = D.replace_catalog
        def fail_second(path, data, expected):
            if path.name == "fragments.json":
                raise OSError("échec simulé")
            return real(path, data, expected)
        with patch.object(D, "replace_catalog", side_effect=fail_second):
            with self.assertRaisesRegex(OSError, "échec simulé"):
                D.apply(self.root, directory)
        for name, data in originals.items():
            self.assertEqual((self.root / name).read_bytes(), data)
        self.assertFalse((self.root / "chapters/I83").exists())
        self.assertFalse((self.root / "glossary/i83.py").exists())
        self.assertEqual(list((self.root / "docs/collaboration/receipts").glob("*.json"))
                         if (self.root / "docs/collaboration/receipts").exists() else [], [])

    def test_concurrent_collision_with_identical_bytes_is_not_removed(self):
        directory = self.destination_ready()
        real = D.write_new
        def collide(path, data):
            if path.name == "i83.py":
                path.write_bytes(data)
            return real(path, data)
        with patch.object(D, "write_new", side_effect=collide):
            with self.assertRaises(FileExistsError):
                D.apply(self.root, directory)
        self.assertTrue((self.root / "glossary/i83.py").exists())
        self.assertFalse((self.root / "chapters/I83").exists())

    def test_paths_escape_and_symlink_are_rejected(self):
        directory = self.packet()
        for target in ("../outside.html", "/tmp/outside.html", "chapters/I83/../I80/I80_a.html"):
            with self.subTest(target=target):
                original = (directory / "livraison.json").read_bytes()
                self.edit_manifest(directory, lambda m: m["files"][0].update(target_path=target))
                with self.assertRaises(D.DeliveryError):
                    D.check(self.root, directory)
                (directory / "livraison.json").write_bytes(original)
        source = directory / "sources/chapters/I83/I83_a.html"
        source.unlink()
        source.symlink_to(self.root / "rapport.md")
        with self.assertRaisesRegex(D.DeliveryError, "symbolique"):
            D.check(self.root, directory)

    def test_source_and_report_tampering(self):
        directory = self.packet()
        source = directory / "sources/chapters/I83/I83_a.html"
        original = source.read_bytes()
        source.write_text("<p>Altération</p>")
        with self.assertRaisesRegex(D.DeliveryError, "Empreinte"):
            D.check(self.root, directory)
        source.write_bytes(original)
        (directory / "rapport.md").write_text("Rapport remplacé")
        with self.assertRaisesRegex(D.DeliveryError, "Rapport"):
            D.check(self.root, directory)

    def test_missing_reference_duplicate_id_and_required_panel(self):
        source = self.root / "chapters/I83/I83_b.html"
        for content, message in [('<section id="pE"><button data-k="absent">X</button></section>', "Références"),
                                 ('<section id="pE"><span id="pA"></span></section>', "double"),
                                 ('<section id="elsewhere"></section>', "quatre panneaux")]:
            with self.subTest(content=content):
                source.write_text(content)
                with self.assertRaisesRegex(D.DeliveryError, message):
                    self.packet()

    def test_parent_commit_report_and_utf8_are_required(self):
        with self.assertRaises(D.DeliveryError):
            D.package(self.root, "I83", "Varices", ["I83"], "vaisseaux", "rapport.md", "bad")
        (self.root / "rapport.md").write_text("")
        with self.assertRaisesRegex(D.DeliveryError, "Rapport vide"):
            self.packet()
        (self.root / "rapport.md").write_text("Rapport")
        (self.root / "chapters/I83/I83_b.html").write_bytes(b"\xff")
        with self.assertRaisesRegex(D.DeliveryError, "UTF-8"):
            self.packet()

    def test_python_glossary_is_parsed_without_execution(self):
        marker = self.root / "executed"
        self.write("glossary/i83.py", f"open({str(marker)!r}, 'w').write('bad')\n")
        self.packet()
        self.assertFalse(marker.exists())

    def test_missing_shared_popup_is_rechecked_on_destination(self):
        directory = self.destination_ready()
        (self.root / "chapters/I80/I80_pop.html").unlink()
        with self.assertRaisesRegex(D.DeliveryError, "i80-echo"):
            D.check(self.root, directory)
        self.assertFalse((self.root / "chapters/I83").exists())

    def test_relative_packet_path_uses_explicit_root(self):
        directory = self.packet()
        manifest, _, _ = D.check(self.root, directory.relative_to(self.root))
        self.assertEqual(manifest["course"]["code"], "I83")

    def test_unregistered_shared_course_cannot_supply_popup(self):
        self.write("chapters/I77/I77_pop.html", '<template data-pop="i77-orphan"></template>')
        self.write("chapters/I83/I83_b.html", '<section id="pE"><button data-k="i77-orphan">X</button></section>')
        with self.assertRaisesRegex(D.DeliveryError, "i77-orphan"):
            self.packet()

    def test_course_outside_fragment_cannot_supply_popup_or_route(self):
        self.write("chapters.json", '[{"code":"I80","integrated":true},{"code":"J45","integrated":true}]')
        self.write("chapters/J45/J45_pop.html", '<template data-pop="j45-spirometrie"></template>')
        target = self.root / "chapters/I83/I83_b.html"
        for content in ('<section id="pE"><button data-k="j45-spirometrie">X</button></section>',
                        '<section id="pE"><a href="#/entry/J45">X</a></section>'):
            target.write_text(content)
            with self.assertRaisesRegex(D.DeliveryError, "Références"):
                self.packet()

    def test_concurrent_catalog_change_is_preserved(self):
        directory = self.destination_ready()
        real = D.replace_catalog
        concurrent = b'[{"code":"I80","title":"Modification concurrente","integrated":true}]'
        def collide(path, data, expected):
            if path.name == "chapters.json":
                path.write_bytes(concurrent)
            return real(path, data, expected)
        with patch.object(D, "replace_catalog", side_effect=collide):
            with self.assertRaisesRegex(D.DeliveryError, "simultanément"):
                D.apply(self.root, directory)
        self.assertEqual((self.root / "chapters.json").read_bytes(), concurrent)
        self.assertFalse((self.root / "chapters/I83").exists())


if __name__ == "__main__":
    unittest.main()
