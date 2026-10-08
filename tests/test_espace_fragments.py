"""Garde des fragments : vrais commits temporaires, aucun réseau ni revue simulée.

Les rapports et inventories de ces fixtures sont des preuves techniques de test,
sans valeur clinique. Les sources réelles du dépôt ne sont jamais modifiées.
"""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("espace", ROOT / "tools/espace.py")
ESPACE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ESPACE)


def digest(data):
    return hashlib.sha256(data).hexdigest()


class FragmentGuardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.git("init", "-q")
        self.git("config", "user.name", "Test local")
        self.git("config", "user.email", "test@example.invalid")
        registry = json.loads((ROOT / ESPACE.FRAGMENT_REGISTRY).read_text())
        self.write_json(ESPACE.FRAGMENT_REGISTRY, registry)
        self.records = [{"id": f["id"], "label": f["label"],
                         "owner": "Claude" if f["id"] == "S01" else "Codex",
                         "status": "A_COMPLETER", "complete": False,
                         "coverage": {"status": "non_etablie", "inventory_path": None},
                         "internal_review": None, "cross_audit": None,
                         "injection": None, "locked_files": {}} for f in registry]
        self.fragment = self.records[0]
        self.medical = "chapters/I50/I50_a.html"
        self.write(self.medical, b"Source de test initiale")
        self.save()
        self.initial = self.commit()

    def git(self, *args):
        return subprocess.run(["git", *args], cwd=self.root, check=True,
                              capture_output=True).stdout.decode().strip()

    def write(self, path, data):
        destination = self.root / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)

    def write_json(self, path, value):
        self.write(path, (json.dumps(value, ensure_ascii=False) + "\n").encode())

    def save(self):
        self.write_json(ESPACE.FRAGMENT_STATUS, {
            "schema_version": 1, "protocol": ESPACE.PROTOCOL, "fragments": self.records})

    def commit(self):
        self.git("add", ".")
        self.git("commit", "-qm", "Fixture locale", "--allow-empty")
        return self.git("rev-parse", "HEAD")

    def guard(self, before, after):
        return ESPACE.validate_fragment_guard(ESPACE.GitTree(self.root, before),
                                             ESPACE.GitTree(self.root, after))

    def complete(self):
        files = {self.medical: digest(b"Remise auteur de test")}
        source_dir = "remises/S01/auteur/sources"
        self.write(f"{source_dir}/{self.medical}", b"Remise auteur de test")
        inventory_path = "preuves/S01/inventaire.json"
        self.write_json(inventory_path, {"fragment_id": "S01", "scope": "fragment_complet",
                                        "complete": True, "files": files,
                                        "categories": [{"id": "test", "title": "Catégorie de fixture"}],
                                        "uncovered_categories": []})
        report_path = "preuves/S01/auto-revue.md"
        self.write(report_path, b"Rapport de fixture : auto-revue auteur, sans valeur clinique.")
        self.fragment.update({
            "status": "PRET_A_TRANSMETTRE", "complete": True,
            "coverage": {"status": "verifiee", "scope": "fragment_complet", "files": files,
                         "inventory_path": inventory_path,
                         "inventory_sha256": digest((self.root / inventory_path).read_bytes())},
            "internal_review": {"reviewer": "Claude", "scope": "fragment_complet", "files": files,
                                "source_dir": source_dir, "report_path": report_path,
                                "report_sha256": digest((self.root / report_path).read_bytes())}})
        self.save()

    def audit(self, auditor="Codex"):
        final_data = b"Remise corrigee par auditeur de test"
        source_dir = "remises/S01/auditeur/sources"
        self.write(f"{source_dir}/{self.medical}", final_data)
        report_path = "preuves/S01/audit.md"
        self.write(report_path, b"Rapport de fixture : audit unique, sans valeur clinique.")
        files = {self.medical: digest(final_data)}
        matrix_path = "preuves/S01/contexte-suisse.json"
        self.write_json(matrix_path, {
            "schema_version": 1, "fragment_id": "S01", "scope": "fragment_complet",
            "source_files": files, "unresolved_divergences": [],
            "decisions": [{"id": "i50-diagnostic-fixture", "chapter_code": "I50",
                           "kind": "diagnostic", "claim": "Décision fictive de test",
                           "initial_primary_origin": "american", "final_primary_origin": "swiss",
                           "divergence_status": "resolved", "resolution": "Comparaison fictive de test",
                           "auditor_verdict": "conforme",
                           "foreign_sources": [{"origin": "american", "organization": "Organisme US fictif",
                                                "title": "Texte fictif", "url": "https://example.invalid/us",
                                                "version_date": "2026-10-08", "section": "Diagnostic",
                                                "passage": "Passage fictif de fixture"}],
                           "swiss_guideline": {"status": "applicable",
                                               "organization": "Société suisse fictive de test",
                                               "title": "Directive fictive", "url": "https://example.invalid/ssi",
                                               "version_date": "2026-10-08", "section": "Diagnostic",
                                               "passage": "Texte fictif de fixture"}}]})
        self.fragment.update({"status": "AUDITE", "cross_audit": {
            "auditor": auditor, "scope": "fragment_complet", "verdict": "favorable",
            "input_files": self.fragment["internal_review"]["files"],
            "files": files, "source_dir": source_dir,
            "report_path": report_path, "report_sha256": digest((self.root / report_path).read_bytes()),
            "swiss_context": {"verdict": "conforme", "matrix_path": matrix_path,
                              "matrix_sha256": digest((self.root / matrix_path).read_bytes())}}})
        self.save()

    def inject(self, injector="Codex"):
        audit = self.fragment["cross_audit"]
        self.write(self.medical, (self.root / audit["source_dir"] / self.medical).read_bytes())
        self.fragment.update({"status": "INJECTE", "locked_files": copy.deepcopy(audit["files"]),
                              "injection": {"injector": injector, "files": copy.deepcopy(audit["files"])}})
        self.save()

    def injected(self):
        self.complete()
        ready = self.commit()
        self.audit()
        self.inject()
        injected = self.commit()
        self.assertEqual(self.guard(self.initial, ready), [])
        self.assertEqual(self.guard(ready, injected), [])
        return injected

    def test_incomplete_registry_and_historical_owner_are_readable(self):
        self.fragment["owner"] = "Partage historique"
        self.save()
        before = self.commit()
        self.write("docs/rapport.md", b"Consultation seulement")
        self.assertEqual(self.guard(before, self.commit()), [])

    def test_historical_unassigned_owner_can_be_assigned_before_submission(self):
        self.fragment["owner"] = "Partage historique"
        self.save()
        unassigned = self.commit()
        self.fragment["owner"] = "Claude"
        self.save()
        self.assertEqual(self.guard(unassigned, self.commit()), [])

    def test_already_assigned_owner_cannot_be_replaced(self):
        self.fragment["owner"] = "Codex"
        self.save()
        with self.assertRaisesRegex(ESPACE.FragmentError, "déjà attribué"):
            self.guard(self.initial, self.commit())

    def test_chapter_mutations_fail_before_any_network_or_worktree(self):
        with patch.object(ESPACE, "R", self.root), patch.object(ESPACE, "main_frais") as fresh:
            for operation in (
                    lambda: ESPACE.deposer("dossier-inexistant", "Claude"),
                    lambda: ESPACE.auditer("I50", "Codex", "favorable", "rapport"),
                    lambda: ESPACE.injecter("I50")):
                with self.assertRaisesRegex(ESPACE.FragmentError, "par cours/remise partielle interdit"):
                    operation()
            fresh.assert_not_called()

    def test_ouvrir_and_consulter_are_read_only(self):
        with patch.object(ESPACE, "R", self.root), patch.object(ESPACE, "main_frais") as fresh, patch("builtins.print"):
            ESPACE.ouvrir("I50")
            ESPACE.consulter("S01")
            fresh.assert_not_called()
        self.assertEqual(self.git("status", "--porcelain"), "")

    def test_incomplete_fragment_cannot_be_audited_or_injected(self):
        for state in ("EN_AUDIT_CROISE", "INJECTE"):
            with self.subTest(state=state):
                self.fragment["status"] = state
                self.save()
                with self.assertRaisesRegex(ESPACE.FragmentError, "fragment incomplet"):
                    self.guard(self.initial, self.commit())

    def test_chapter_audit_cannot_bypass_complete_fragment(self):
        new = b"Modification medicale non transmise"
        self.write(self.medical, new)
        self.write_json("espace_partage/COURS_CLAUDE_A_AUDITER_PAR_CODEX/I50/ETAT.json", {
            "auteur": "Claude", "audits": [{"auditeur": "Codex", "verdict": "favorable",
                                             "fichiers": {self.medical: digest(new)}}]})
        self.assertEqual(self.guard(self.initial, self.commit()), [self.medical])

    def test_complete_declaration_without_actual_report_is_rejected(self):
        self.complete()
        (self.root / self.fragment["internal_review"]["report_path"]).unlink()
        with self.assertRaisesRegex(ESPACE.FragmentError, "Fichier absent"):
            self.guard(self.initial, self.commit())

    def test_inventory_with_uncovered_categories_is_rejected(self):
        self.complete()
        coverage = self.fragment["coverage"]
        path = self.root / coverage["inventory_path"]
        inventory = json.loads(path.read_text())
        inventory["uncovered_categories"] = ["categorie non couverte"]
        self.write_json(coverage["inventory_path"], inventory)
        coverage["inventory_sha256"] = digest(path.read_bytes())
        self.save()
        with self.assertRaisesRegex(ESPACE.FragmentError, "inventaire complet structuré"):
            self.guard(self.initial, self.commit())

    def test_audit_requires_preexisting_complete_author_submission(self):
        self.complete()
        self.audit()
        with self.assertRaisesRegex(ESPACE.FragmentError, "fragment incomplet"):
            self.guard(self.initial, self.commit())

    def test_author_cannot_audit_own_fragment(self):
        self.complete()
        ready = self.commit()
        self.audit(auditor="Claude")
        with self.assertRaisesRegex(ESPACE.FragmentError, "autre IA"):
            self.guard(ready, self.commit())

    def test_auditor_may_correct_then_inject_in_one_turn(self):
        self.injected()

    def test_author_cannot_inject_after_other_actor_audit(self):
        self.complete()
        ready = self.commit()
        self.audit()
        self.inject(injector="Claude")
        with self.assertRaisesRegex(ESPACE.FragmentError, "injection par l'auditeur"):
            self.guard(ready, self.commit())

    def test_audit_refuses_missing_swiss_context(self):
        self.complete()
        ready = self.commit()
        self.audit()
        del self.fragment["cross_audit"]["swiss_context"]
        self.save()
        with self.assertRaisesRegex(ESPACE.FragmentError, "contexte suisse non conforme ou absent"):
            self.guard(ready, self.commit())

    def test_audit_refuses_unresolved_swiss_divergence(self):
        self.complete()
        ready = self.commit()
        self.audit()
        proof = self.fragment["cross_audit"]["swiss_context"]
        path = self.root / proof["matrix_path"]
        matrix = json.loads(path.read_text())
        matrix["unresolved_divergences"] = ["Écart suisse non arbitré"]
        self.write_json(proof["matrix_path"], matrix)
        proof["matrix_sha256"] = digest(path.read_bytes())
        self.save()
        with self.assertRaisesRegex(ESPACE.FragmentError, "divergence ouverte"):
            self.guard(ready, self.commit())

    def test_audit_refuses_american_origin_without_passage(self):
        self.complete()
        ready = self.commit()
        self.audit()
        proof = self.fragment["cross_audit"]["swiss_context"]
        path = self.root / proof["matrix_path"]
        matrix = json.loads(path.read_text())
        matrix["decisions"][0]["foreign_sources"] = []
        self.write_json(proof["matrix_path"], matrix)
        proof["matrix_sha256"] = digest(path.read_bytes())
        self.save()
        with self.assertRaisesRegex(ESPACE.FragmentError, "origine étrangère sans passage"):
            self.guard(ready, self.commit())

    def test_audit_refuses_american_prescription_without_local_gap(self):
        self.complete()
        ready = self.commit()
        self.audit()
        proof = self.fragment["cross_audit"]["swiss_context"]
        path = self.root / proof["matrix_path"]
        matrix = json.loads(path.read_text())
        matrix["decisions"][0]["final_primary_origin"] = "american"
        self.write_json(proof["matrix_path"], matrix)
        proof["matrix_sha256"] = digest(path.read_bytes())
        self.save()
        with self.assertRaisesRegex(ESPACE.FragmentError, "sans justification du manque suisse/européen"):
            self.guard(ready, self.commit())

    def test_documented_swiss_gap_can_use_european_source(self):
        self.complete()
        ready = self.commit()
        self.audit()
        proof = self.fragment["cross_audit"]["swiss_context"]
        path = self.root / proof["matrix_path"]
        matrix = json.loads(path.read_text())
        row = matrix["decisions"][0]
        row["swiss_guideline"] = {"status": "documented_gap", "searched_on": "2026-10-08",
                                  "search_scope": "Décision fictive de fixture",
                                  "searched_sources": "Répertoire suisse fictif de test",
                                  "gap_reason": "Aucun texte applicable dans la fixture"}
        row["final_primary_origin"] = "european"
        row["foreign_sources"].append({"origin": "european", "organization": "Société européenne fictive",
                                       "title": "Directive fictive", "url": "https://example.invalid/eu",
                                       "version_date": "2026-10-08", "section": "Diagnostic",
                                       "passage": "Passage européen fictif"})
        self.write_json(proof["matrix_path"], matrix)
        proof["matrix_sha256"] = digest(path.read_bytes())
        self.save()
        self.assertEqual(self.guard(ready, self.commit()), [])

    def test_audit_refuses_medication_without_exact_swissmedic_product(self):
        self.complete()
        ready = self.commit()
        self.audit()
        audit = self.fragment["cross_audit"]
        medication = "chapters/I50/I50_d.html"
        body = b"Fixture posologie sans FI suisse"
        self.write(audit["source_dir"] + "/" + medication, body)
        audit["files"][medication] = digest(body)
        proof = audit["swiss_context"]
        path = self.root / proof["matrix_path"]
        matrix = json.loads(path.read_text())
        matrix["source_files"] = audit["files"]
        row = copy.deepcopy(matrix["decisions"][0])
        row.update(id="i50-medicament-fixture", kind="medication")
        matrix["decisions"].append(row)
        self.write_json(proof["matrix_path"], matrix)
        proof["matrix_sha256"] = digest(path.read_bytes())
        self.save()
        with self.assertRaisesRegex(ESPACE.FragmentError, "FI Swissmedic du produit exact absente"):
            self.guard(ready, self.commit())

    def test_audit_accepts_medication_with_exact_swissmedic_product(self):
        self.complete()
        ready = self.commit()
        self.audit()
        audit = self.fragment["cross_audit"]
        medication = "chapters/I50/I50_d.html"
        body = b"Fixture produit exact"
        self.write(audit["source_dir"] + "/" + medication, body)
        audit["files"][medication] = digest(body)
        proof = audit["swiss_context"]
        path = self.root / proof["matrix_path"]
        matrix = json.loads(path.read_text())
        matrix["source_files"] = audit["files"]
        row = copy.deepcopy(matrix["decisions"][0])
        row.update(id="i50-medicament-fixture", kind="medication", swissmedic_product={
            "product_name": "Produit suisse fictif", "authorization_number": "00000",
            "url": "https://example.invalid/fi", "accessed_on": "2026-10-08",
            "section": "Posologie", "passage": "Passage fictif de FI"})
        matrix["decisions"].append(row)
        self.write_json(proof["matrix_path"], matrix)
        proof["matrix_sha256"] = digest(path.read_bytes())
        self.save()
        self.assertEqual(self.guard(ready, self.commit()), [])

    def test_staged_audit_sources_must_match_report_hashes(self):
        self.complete()
        ready = self.commit()
        self.audit()
        self.write(self.fragment["cross_audit"]["source_dir"] + "/" + self.medical, b"Apres audit")
        with self.assertRaisesRegex(ESPACE.FragmentError, "empreinte source différente"):
            self.guard(ready, self.commit())

    def test_second_audit_is_rejected(self):
        self.complete()
        self.commit()
        self.audit()
        audited = self.commit()
        self.fragment["cross_audit"]["verdict"] = "favorable_sous_reserves_mineures"
        self.save()
        with self.assertRaisesRegex(ESPACE.FragmentError, "second audit"):
            self.guard(audited, self.commit())

    def test_injected_entry_cannot_be_reopened_or_even_annotated(self):
        injected = self.injected()
        self.fragment["note"] = "Relecture apres injection"
        self.save()
        with self.assertRaisesRegex(ESPACE.FragmentError, "INJECTE immuable"):
            self.guard(injected, self.commit())
        del self.fragment["note"]
        self.fragment["status"] = "EN_PRODUCTION"
        self.save()
        with self.assertRaisesRegex(ESPACE.FragmentError, "INJECTE immuable"):
            self.guard(injected, self.commit())

    def test_locked_medical_content_cannot_change_or_disappear(self):
        injected = self.injected()
        self.write(self.medical, b"Reouverture interdite")
        with self.assertRaisesRegex(ESPACE.FragmentError, "contenu injecté différent"):
            self.guard(injected, self.commit())
        (self.root / self.medical).unlink()
        with self.assertRaisesRegex(ESPACE.FragmentError, "Fichier absent"):
            self.guard(injected, self.commit())

    def test_register_removal_or_replacement_is_rejected(self):
        (self.root / ESPACE.FRAGMENT_STATUS).unlink()
        with self.assertRaisesRegex(ESPACE.FragmentError, "Suppression du registre"):
            self.guard(self.initial, self.commit())
        self.records.pop()
        self.save()
        with self.assertRaisesRegex(ESPACE.FragmentError, "exactement 22"):
            self.guard(self.initial, self.commit())

    def test_protocol_activation_cannot_inject_a_fabricated_submission(self):
        (self.root / ESPACE.FRAGMENT_STATUS).unlink()
        legacy = self.commit()
        self.complete()
        self.audit()
        self.inject()
        with self.assertRaisesRegex(ESPACE.FragmentError, "Activation du protocole"):
            self.guard(legacy, self.commit())

    def test_initial_protocol_activation_with_no_claim_is_allowed(self):
        (self.root / ESPACE.FRAGMENT_STATUS).unlink()
        legacy = self.commit()
        self.save()
        self.assertEqual(self.guard(legacy, self.commit()), [])

    def test_reports_and_sources_cannot_escape_repository(self):
        self.complete()
        self.fragment["internal_review"]["report_path"] = "../hors-depot.md"
        self.save()
        with self.assertRaisesRegex(ESPACE.FragmentError, "Chemin relatif sûr"):
            self.guard(self.initial, self.commit())

    def test_symlink_cannot_substitute_for_review_evidence(self):
        self.complete()
        report = self.root / self.fragment["internal_review"]["report_path"]
        report.unlink()
        report.symlink_to("/etc/passwd")
        with self.assertRaisesRegex(ESPACE.FragmentError, "non régulière"):
            self.guard(self.initial, self.commit())


if __name__ == "__main__":
    unittest.main()
