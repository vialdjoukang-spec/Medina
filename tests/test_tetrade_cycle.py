"""Fixtures techniques fictives : aucune revue ou validation clinique simulée."""
import copy
import hashlib
import json
from pathlib import Path
import unittest
from unittest.mock import patch

from tools import tetrade_cycle as C
from tools.espace import swiss_context_proof, FragmentError


class Tree:
    def __init__(self, files):
        self.files = files
        self.entries = {p: ("100644", "blob", C.digest(v)) for p, v in files.items()}

    def read(self, path, required=True):
        if path not in self.files and required:
            raise C.CycleError("Absent " + str(path))
        return self.files.get(path)


def encode(data):
    return (json.dumps(data, ensure_ascii=False) + "\n").encode()


class TetradeGuardTests(unittest.TestCase):
    def setUp(self):
        root = Path(__file__).resolve().parents[1]
        self.state = json.loads((root / C.REGISTRY).read_text())
        self.state.update(state="ACTIF", closure=None)
        for row in self.state["chapters"]:
            row.update(status="EN_PRODUCTION", source_dir=None, files={})
            for key in ("author", "cross_audit", "counter_audit", "control", "injection", "publication"):
                row[key] = None
        self.files = {p: (root / p).read_bytes() for p in C.PROMPTS}
        self.files["chapters.json"] = b"[]\n"
        self.save()
        self.before = Tree(copy.deepcopy(self.files))

    def save(self):
        self.files[C.REGISTRY] = encode(self.state)

    def guard(self):
        self.save()
        return C.validate_cycle_guard(self.before, Tree(self.files))

    def test_activation_is_nonmedical_and_has_four_unique_missions(self):
        before = dict(self.files); before.pop(C.REGISTRY)
        self.assertEqual(C.validate_cycle_guard(Tree(before), Tree(self.files)), ({}, {"I63", "E11", "N17", "D50"}))

    def test_activation_cannot_inject_a_chapter(self):
        before = dict(self.files); before.pop(C.REGISTRY)
        self.files["chapters/I63/I63_a.html"] = b"Fixture medicale"
        with self.assertRaisesRegex(C.CycleError, "Activation"):
            C.validate_cycle_guard(Tree(before), Tree(self.files))

    def test_registry_cannot_be_deleted(self):
        self.files.pop(C.REGISTRY)
        with self.assertRaisesRegex(C.CycleError, "Suppression"):
            C.validate_cycle_guard(self.before, Tree(self.files))

    def test_injection_without_all_reviews_is_rejected(self):
        self.state["chapters"][0]["status"] = "INJECTE"
        with self.assertRaisesRegex(C.CycleError, "quatre productions"):
            self.guard()

    def test_legacy_claude_registry_cannot_authorize_cycle_files(self):
        self.files["chapters/I63/I63_a.html"] = b"Fixture medicale"
        self.files["organisation/SCELLES.json"] = encode({"scelle": False, "fichiers": {"chapters/I63/I63_a.html": C.digest(b"Fixture medicale")}})
        with self.assertRaisesRegex(C.CycleError, "sans injection"):
            self.guard()

    def test_self_audit_or_existing_counter_auditor_is_rejected(self):
        for key in ("cross_reviewer", "counter_reviewer"):
            with self.subTest(key=key):
                state = copy.deepcopy(self.state)
                self.state["chapters"][0][key] = "C01-R-NEUR"
                with self.assertRaisesRegex(C.CycleError, "indépendance"):
                    self.guard()
                self.state = state

    def test_second_cycle_is_not_authorized(self):
        self.state["authorized_cycles"] = [1, 2]
        with self.assertRaisesRegex(C.CycleError, "cycle 1"):
            self.guard()

    def test_authority_cannot_change_during_cycle(self):
        self.files[C.AUTHORITY] += b"Alteration de fixture"
        with self.assertRaisesRegex(C.CycleError, "Autorité"):
            self.guard()

    def test_source_files_are_complete_and_scoped(self):
        row = self.state["chapters"][0]
        row["source_dir"] = "livraisons/Livraison Codex/N-05-Neurologie/travail/CYCLE_01_I63"
        row["files"] = {f"chapters/I63/I63_{s}.html": C.digest(b"Fixture") for s in ("a", "b", "c", "d", "pop1", "pop2")}
        row["files"]["glossary/i63.py"] = C.digest(b"Fixture")
        for path in row["files"]:
            self.files[row["source_dir"] + "/" + path] = b"Fixture"
        self.assertEqual(C.source_files(Tree(self.files), row), row["files"])
        row["files"]["chapters/J45/J45_a.html"] = C.digest(b"Fixture")
        with self.assertRaisesRegex(C.CycleError, "étrangère"):
            C.source_files(Tree(self.files), row)

    def prepared(self):
        for row in self.state["chapters"]:
            row["status"] = "PRET_A_INJECTER"
            row["files"] = {f"chapters/{row['code']}/{row['code']}_a.html": C.digest(b"Fixture")}
            for key in ("author", "cross_audit", "counter_audit", "control"):
                row[key] = {"path": "Fixture technique mockée, sans valeur clinique"}
        self.save(); self.before = Tree(copy.deepcopy(self.files))

    def inject(self, index):
        row = self.state["chapters"][index]; row["status"] = "INJECTE"
        row["injection"] = {"path": f"preuves/injection-{index}.json"}
        raw = encode({"code": row["code"], "files": row["files"], "injector": self.state["coordinator"]})
        self.files[row["injection"]["path"]] = raw; row["injection"]["sha256"] = C.digest(raw)
        for path in row["files"]:
            self.files[path] = b"Fixture"
        self.files["chapters.json"] = encode([{"code": row["code"], "covers": [row["code"]], "integrated": True}])

    def test_successful_sequence_authorizes_exactly_one_chapter(self):
        self.prepared(); self.inject(0)
        with patch.object(C, "ready", side_effect=lambda tree, row: row["files"]):
            authorized, codes = self.guard()
        self.assertEqual(set(authorized), {"chapters/I63/I63_a.html", "chapters.json"})
        self.assertEqual(codes, {"I63", "E11", "N17", "D50"})

    def test_multiple_injections_are_rejected(self):
        self.prepared(); self.inject(0); self.inject(1)
        with patch.object(C, "ready", side_effect=lambda tree, row: row["files"]):
            with self.assertRaisesRegex(C.CycleError, "Un seul chapitre"):
                self.guard()

    def test_skipping_publication_of_previous_chapter_is_rejected(self):
        self.prepared(); self.inject(1)
        with patch.object(C, "ready", side_effect=lambda tree, row: row["files"]):
            with self.assertRaisesRegex(C.CycleError, "précédent"):
                self.guard()

    def test_catalogue_can_only_append_the_injected_chapter(self):
        self.prepared(); self.inject(0)
        self.files["chapters.json"] = encode([{"code": "E11", "covers": ["E11"], "integrated": True}])
        with patch.object(C, "ready", side_effect=lambda tree, row: row["files"]):
            with self.assertRaisesRegex(C.CycleError, "Enregistrement"):
                self.guard()

    def test_closure_requires_four_public_readbacks(self):
        self.state["state"] = "CLOTURE"
        with self.assertRaisesRegex(C.CycleError, "quatre publications"):
            self.guard()

    def test_prompt_reading_alone_does_not_satisfy_application(self):
        gate = {"actor": "Fixture", "verdict": "conforme", "checked_at": "2026-10-11T12:00:00+02:00",
                "prompt_files": {p: C.digest(self.files[p]) for p in C.PROMPTS}, "checks": []}
        with self.assertRaisesRegex(C.CycleError, "matrice"):
            C.prompt_gate(Tree(self.files), gate, "Fixture", "Entrée")

    def test_prompt_evidence_must_exist_and_match_hash(self):
        checks = ["autorisation", "perimetre_provenance", "sources_lues", "contexte_suisse", "independance", "contrat_cours", "honnetete"]
        self.files["preuves/application.md"] = b"Fixture technique sans valeur clinique"
        gate = {"actor": "Fixture", "verdict": "conforme", "checked_at": "2026-10-11T12:00:00+02:00",
                "prompt_files": {p: C.digest(self.files[p]) for p in C.PROMPTS},
                "checks": [{"id": key, "status": "conforme", "evidence": [{"path": "preuves/application.md", "sha256": C.digest(self.files["preuves/application.md"]), "explanation": "Fixture de contrat"}]} for key in checks]}
        C.prompt_gate(Tree(self.files), gate, "Fixture", "Entrée")
        self.files["preuves/application.md"] += b"Modification"
        with self.assertRaisesRegex(C.CycleError, "preuve"):
            C.prompt_gate(Tree(self.files), gate, "Fixture", "Entrée")

    def reference(self, path, data):
        raw = encode(data); self.files[path] = raw
        return {"path": path, "sha256": C.digest(raw)}

    def complete_review(self):
        actor = "C01-R-HEM"; files = {"chapters/I63/I63_a.html": C.digest(b"Fixture technique")}
        self.files["preuves/observation.md"] = b"Fixture technique, aucune revue clinique"
        evidence = [{"path": "preuves/observation.md", "sha256": C.digest(self.files["preuves/observation.md"]), "explanation": "Preuve de test de contrat uniquement"}]
        keys = ["autorisation", "perimetre_provenance", "sources_lues", "contexte_suisse", "independance", "contrat_cours", "honnetete"]
        gate = {"actor": actor, "verdict": "conforme", "checked_at": "2026-10-11T12:00:00+02:00", "prompt_files": {p: C.digest(self.files[p]) for p in C.PROMPTS}, "checks": [{"id": k, "status": "conforme", "evidence": evidence} for k in keys]}
        review = {"actor": actor, "code": "I63", "runtime_agent_id": "fixture-reviewer", "medical_human_validation": False, "entry": gate, "exit": dict(gate, checked_at="2026-10-11T14:00:00+02:00"), "final_files": files, "blocking_reserves": [], "passes": []}
        reports = []
        for n in (1, 2):
            report = {"actor": actor, "code": "I63", "pass": n, "started_at": f"2026-10-11T{11+n}:00:00+02:00", "finished_at": f"2026-10-11T{11+n}:30:00+02:00", "dimensions": {k: "Observation de fixture technique" for k in C.DIMENSIONS}, "numerical_checks": [{"claim": f"Donnée fictive distincte {i}", "source": "https://example.invalid/fixture", "section": "Fixture", "passage": "Aucune assertion clinique", "finding": "Exigence structurelle de test"} for i in range(10)], "verdict": "favorable", "final_files": files, "blocking_reserves": [], "score": 20}
            reports.append(report)
            review["passes"].append({"number": n, "report": self.reference(f"preuves/passe-{n}.json", report)})
        row = {"code": "I63", "cross_audit": self.reference("preuves/revue.json", review)}
        return row, review, reports, actor, files

    def test_two_pass_review_contract_can_be_satisfied_by_explicit_technical_fixture(self):
        row, _, _, actor, files = self.complete_review()
        C.review(Tree(self.files), row, "cross_audit", actor, files)

    def test_stale_final_hash_or_open_reserve_invalidates_second_pass(self):
        for change in ({"final_files": {}}, {"blocking_reserves": ["Réserve fictive ouverte"]}):
            with self.subTest(change=change):
                row, data, reports, actor, files = self.complete_review()
                reports[1].update(change)
                data["passes"][1]["report"] = self.reference("preuves/passe-2.json", reports[1])
                row["cross_audit"] = self.reference("preuves/revue.json", data)
                with self.assertRaisesRegex(C.CycleError, "Seconde passe"):
                    C.review(Tree(self.files), row, "cross_audit", actor, files)

    def test_nine_checks_or_ten_duplicates_are_insufficient(self):
        for duplicates in (False, True):
            with self.subTest(duplicates=duplicates):
                row, data, reports, actor, files = self.complete_review()
                reports[1]["numerical_checks"] = ([reports[1]["numerical_checks"][0]] * 10 if duplicates else reports[1]["numerical_checks"][:9])
                data["passes"][1]["report"] = self.reference("preuves/passe-2.json", reports[1])
                row["cross_audit"] = self.reference("preuves/revue.json", data)
                with self.assertRaisesRegex(C.CycleError, "dix"):
                    C.review(Tree(self.files), row, "cross_audit", actor, files)

    def test_overlapping_passes_are_rejected(self):
        row, data, reports, actor, files = self.complete_review()
        reports[1]["started_at"] = reports[0]["started_at"]
        data["passes"][1]["report"] = self.reference("preuves/passe-2.json", reports[1])
        row["cross_audit"] = self.reference("preuves/revue.json", data)
        with self.assertRaisesRegex(C.CycleError, "chevauchent"):
            C.review(Tree(self.files), row, "cross_audit", actor, files)

    def test_technical_review_cannot_claim_human_validation(self):
        row, data, _, actor, files = self.complete_review()
        data["medical_human_validation"] = True
        row["cross_audit"] = self.reference("preuves/revue.json", data)
        with self.assertRaisesRegex(C.CycleError, "qualification"):
            C.review(Tree(self.files), row, "cross_audit", actor, files)

    def swiss_fixture(self):
        files = {"chapters/I63/I63_a.html": C.digest(b"Fixture"),
                 "chapters/I63/I63_d.html": C.digest(b"Fixture")}
        source = {"organization": "Organisme fictif", "title": "Texte fictif",
                  "url": "https://example.invalid/fixture", "version_date": "2026-10-11",
                  "section": "Fixture", "passage": "Passage technique sans valeur clinique"}
        decision = {"id": "fixture", "chapter_code": "I63", "kind": "medication",
                    "claim": "Assertion fictive", "auditor_verdict": "conforme",
                    "initial_primary_origin": "swiss", "final_primary_origin": "swiss",
                    "divergence_status": "none", "foreign_sources": [],
                    "swiss_guideline": dict(source, status="applicable"),
                    "swissmedic_product": {"product_name": "Produit fictif",
                        "authorization_number": "Fixture", "url": source["url"],
                        "accessed_on": "2026-10-11", "section": "Fixture", "passage": source["passage"]}}
        matrix = {"schema_version": 1, "fragment_id": "S08", "scope": "chapter",
                  "chapter_code": "I63", "source_files": files,
                  "unresolved_divergences": [], "decisions": [decision]}
        return files, source, decision, matrix

    def swiss_guard(self, files, matrix):
        ref = self.reference("preuves/suisse.json", matrix)
        swiss_context_proof(Tree(self.files), {"swiss_context": {"verdict": "conforme",
            "matrix_path": ref["path"], "matrix_sha256": ref["sha256"]}}, "S08", files,
            scope="chapter", chapter_code="I63")

    def test_swiss_chapter_scope_requires_exact_product_information(self):
        files, _, decision, matrix = self.swiss_fixture()
        self.swiss_guard(files, matrix)
        decision.pop("swissmedic_product")
        with self.assertRaisesRegex(FragmentError, "produit exact"):
            self.swiss_guard(files, matrix)

    def test_swiss_chapter_scope_cannot_claim_whole_fragment(self):
        files, _, _, matrix = self.swiss_fixture()
        matrix["scope"] = "fragment_complet"
        with self.assertRaisesRegex(FragmentError, "incomplète"):
            self.swiss_guard(files, matrix)

    def test_international_primary_text_requires_documented_swiss_gap(self):
        files, source, decision, matrix = self.swiss_fixture()
        decision["final_primary_origin"] = "international"
        decision["foreign_sources"] = [dict(source, origin="international")]
        decision["resolution"] = "Choix international documenté dans cette fixture technique."
        decision["swiss_guideline"] = {"status": "documented_gap", "searched_on": "2026-10-11",
            "search_scope": "Fixture", "searched_sources": "Sources fictives", "gap_reason": "Fixture"}
        self.swiss_guard(files, matrix)
        decision["swiss_guideline"].pop("gap_reason")
        with self.assertRaisesRegex(FragmentError, "absence de directive"):
            self.swiss_guard(files, matrix)

    def test_american_recommendation_cannot_found_cycle_prescription(self):
        files, source, decision, matrix = self.swiss_fixture()
        decision["final_primary_origin"] = "american"
        decision["foreign_sources"] = [dict(source, origin="american")]
        decision["resolution"] = "Fixture"
        decision["swiss_european_gap"] = "Fixture"
        with self.assertRaisesRegex(FragmentError, "américaine interdite"):
            self.swiss_guard(files, matrix)

    def test_audit_pass_cannot_finish_before_it_starts(self):
        row, data, reports, actor, files = self.complete_review()
        reports[1]["finished_at"] = "2026-10-11T10:00:00+02:00"
        data["passes"][1]["report"] = self.reference("preuves/passe-2.json", reports[1])
        row["cross_audit"] = self.reference("preuves/revue.json", data)
        with self.assertRaisesRegex(C.CycleError, "fin antérieure"):
            C.review(Tree(self.files), row, "cross_audit", actor, files)


if __name__ == "__main__":
    unittest.main()
