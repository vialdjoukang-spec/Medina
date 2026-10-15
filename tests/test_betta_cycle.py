"""Technical fixtures only; no medical reading, audit or publication simulated."""
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import types
import unittest
from unittest.mock import patch

from tools import betta_cycle as G


def encode(data):
    return json.dumps(data, ensure_ascii=False).encode()


def digest(data):
    return hashlib.sha256(data).hexdigest()


class Tree:
    def __init__(self, files):
        self.files = copy.deepcopy(files)
        self.entries = {p: ("100644", "blob", digest(raw)) for p, raw in files.items()}

    def read(self, path, required=True):
        if required and path not in self.files:
            raise AssertionError("Fixture missing " + str(path))
        return self.files.get(path)


def lesson(code, fragment="S08", label="N-05-Neurologie"):
    return {"code": code, "fragment": fragment, "label": label, "title": code + " — Fixture technique"}


class Novo12GuardTests(unittest.TestCase):
    def setUp(self):
        # Two declared lessons keep fixtures compact; production uses the exact
        # 1001-entry plan, including its explicit last, incomplete group of five.
        self.lessons = [lesson("R25"), lesson("E63", "S05", "E-06-Endocrinologie et métabolisme")]
        self.plan = {"id": "novo12", "first": 42, "last": 42, "total_lessons": 2,
                     "cycles": [{"number": 42, "lessons": 2, "agents": [
                         {"fragment": l["fragment"], "label": l["label"], "lessons": [l]} for l in self.lessons]}]}
        self.status = {"plan": G.NOVO_PLAN, "cycles": {"42": {
            "state": "A_FAIRE", "lessons": {l["code"]: "A_FAIRE" for l in self.lessons}}}}
        old_plan = {"cycles": [{"number": n, "agents": [{"lessons": [lesson(code)]}]} for n, code in ((42, "R25"), (43, "E63"))]}
        self.legacy = {"cycles": {str(n): {"state": "TRANSFERE_NOVO12", "lessons": {code: "A_FAIRE"}}
                                  for n, code in ((42, "R25"), (43, "E63"))}}
        self.files = {G.PLAN: encode(old_plan), G.STATUS: encode(self.legacy),
                      G.NOVO_PLAN: encode(self.plan), G.NOVO_STATUS: encode(self.status),
                      G.TETRADE: encode({"systems": [{"chapters": [["I63", "Fixture"]]}]}),
                      "chapters.json": b"[]"}
        self.before = Tree(self.files)

    def save(self):
        self.files[G.NOVO_PLAN] = encode(self.plan)
        self.files[G.NOVO_STATUS] = encode(self.status)
        self.files[G.STATUS] = encode(self.legacy)

    def guard(self):
        self.save()
        return G.validate(self.before, Tree(self.files))

    def inject(self, codes=None):
        codes = codes or {l["code"] for l in self.lessons}
        rows = json.loads(self.files["chapters.json"])
        for l in self.lessons:
            code = l["code"]
            if code not in codes:
                continue
            directory = f"livraisons/Livraison Claude/{l['label']}/novo12/CYCLE_42_{code}"
            content = {f"chapters/{code}/{code}_{s}.html": b"<!-- Technical fixture, not a medical lesson -->"
                       for s in ("a", "b", "c", "d", "pop1", "pop2")}
            content[f"glossary/{code.lower()}.py"] = b"G = {}\n"
            content["rapport.md"] = b"Fixture technique ; audit non realise."
            content["recherche.md"] = (f"Fixture technique {code}.1 [S1]\n## Matrice de complétude\n" +
                                         "\n".join(f"| Rubrique {i} | ✔ | [S1] |" for i in range(20))).encode()
            content["sources.json"] = encode({"sources": [{"id": "S1", "url": "https://example.ch/fixture",
                "titre": "Fixture sans contenu médical", "editeur": "Fixture suisse", "version_annee": "2026",
                "date_consultation": "2026-10-15", "section_page": "fixture"}]})
            files = {}
            for p, raw in content.items():
                self.files[directory + "/" + p] = raw
                files[directory + "/" + p] = digest(raw)
            canonical = {p: digest(raw) for p, raw in content.items() if G.managed(p, {code})}
            for p in canonical:
                self.files[p] = content[p]
            self.status["cycles"]["42"]["lessons"][code] = {
                "state": "INJECTE", "dir": directory, "files": files, "canonical": canonical}
            rows.append({"code": code, "covers": [code], "title": l["title"], "integrated": True,
                         "owner": l["fragment"], "production_cycle": 42, "novo12": True,
                         "provisional_injection": True, "audit_status": "audit_differe_non_effectue"})
        self.files["chapters.json"] = encode(rows)
        if all(G._state(row) == 'INJECTE' for row in self.status['cycles']['42']['lessons'].values()):
            self.status['cycles']['42']['state'] = 'INJECTE'

    def row(self, code="R25"):
        return self.status["cycles"]["42"]["lessons"][code]

    def test_idle_main_is_compatible(self):
        self.assertEqual(self.guard(), ({}, set()))

    def test_verified_adoption_cannot_promote_novo_historical_status(self):
        self.files['chapters.json'] = encode([dict(code='R25', integrated=True, covers=['R25'],
            provisional_injection=True, publication_mode='en_etat')])
        self.status['cycles']['42']['lessons']['R25'] = {'state': 'INJECTE', 'canonical': {}}
        self.save()
        with self.assertRaisesRegex(G.BettaError, 'état historique publié réécrit'):
            G.validate(self.before, Tree(self.files), publication_in_state_codes={'R25'})

    def test_complete_delivery_and_injection_same_pr_are_allowed(self):
        self.inject()
        authorized, injected = self.guard()
        self.assertEqual(injected, {"R25", "E63"})
        self.assertEqual(len(authorized), 14)
        self.assertNotIn(G.NOVO_STATUS, authorized)

    def test_transferred_e63_uses_new_cycle42_not_old_cycle43(self):
        self.inject()
        rows = json.loads(self.files["chapters.json"])
        next(r for r in rows if r["code"] == "E63")["production_cycle"] = 43
        self.files["chapters.json"] = encode(rows)
        with self.assertRaisesRegex(G.BettaError, "catalogue Novo_12"):
            self.guard()

    def test_wrong_betta_flag_rejected(self):
        self.inject()
        rows = json.loads(self.files["chapters.json"])
        rows[0].update(betta=True, novo12=False)
        self.files["chapters.json"] = encode(rows)
        with self.assertRaisesRegex(G.BettaError, "catalogue Novo_12"):
            self.guard()

    def test_missing_manifest_or_source_rejected(self):
        for damage in ("manifest", "source", "pop", "canonical", "research"):
            with self.subTest(damage=damage):
                self.setUp(); self.inject()
                row = self.row()
                if damage == "manifest": row.pop("files")
                elif damage == "canonical": row.pop("canonical")
                else:
                    suffix = {"source": "rapport.md", "pop": "chapters/R25/R25_pop1.html", "research": "recherche.md"}[damage]
                    self.files.pop(row["dir"] + "/" + suffix)
                with self.assertRaises(G.BettaError): self.guard()

    def test_changed_or_unlisted_source_rejected(self):
        for unlisted in (False, True):
            with self.subTest(unlisted=unlisted):
                self.setUp(); self.inject()
                path = self.row()["dir"] + ("/extra.txt" if unlisted else "/rapport.md")
                self.files[path] = b"new fixture bytes"
                with self.assertRaises(G.BettaError): self.guard()

    def test_invalid_truth_matrix_rejected(self):
        self.inject()
        path = self.row()["dir"] + "/recherche.md"
        self.files[path] = b"No matrix in this technical fixture"
        self.row()["files"][path] = digest(self.files[path])
        with self.assertRaisesRegex(G.BettaError, "porte de vérité"):
            self.guard()

    def test_uses_only_main_controler_api_and_verified_tree_bytes(self):
        from tools import betta_verite as main_validator
        self.inject()
        seen = []
        def controler(packet):
            self.assertEqual(packet.name, 'CYCLE_42_' + packet.name.rsplit('_', 1)[1])
            code = packet.name.rsplit('_', 1)[1]
            self.assertEqual({p.name for p in packet.iterdir()}, {'recherche.md', 'sources.json'})
            directory = self.row(code)['dir']
            for name in ('recherche.md', 'sources.json'):
                self.assertEqual((packet / name).read_bytes(), self.files[directory + '/' + name])
            seen.append(packet)
            return main_validator.controler(packet)
        # main exposes controler(dossier), not controler_contenu. The adapter
        # must work with only that public API, regardless of optional helpers.
        api = types.ModuleType('tools.betta_verite')
        api.controler = controler
        with patch.dict(sys.modules, {'tools.betta_verite': api}):
            self.assertEqual(self.guard()[1], {'R25', 'E63'})
        self.assertEqual(len(seen), 2)
        self.assertTrue(all(not packet.parent.exists() for packet in seen))

    def test_compatibility_with_exact_legacy_main_validator(self):
        # Read the existing historical Git blob, not a copied validator fixture.
        # This blob is unchanged on main after PR101; no network is used.
        root = Path(__file__).resolve().parents[1]
        result = subprocess.run(['git', 'show', '75500d40543cadeafe3bcea97ca074c4c6afed3a:tools/betta_verite.py'],
                                cwd=root, capture_output=True)
        if result.returncode:
            self.skipTest('Historical main validator blob not present in this source export')
        legacy = types.ModuleType('tools.betta_verite')
        exec(compile(result.stdout, 'main75500d40/tools/betta_verite.py', 'exec'), legacy.__dict__)
        self.assertTrue(callable(legacy.controler))
        self.assertFalse(hasattr(legacy, 'controler_contenu'))
        self.inject()
        with patch.dict(sys.modules, {'tools.betta_verite': legacy}):
            self.assertEqual(self.guard()[1], {'R25', 'E63'})
            path = self.row()['dir'] + '/sources.json'
            self.files[path] = b'{"sources": null}'; self.row()['files'][path] = digest(self.files[path])
            with self.assertRaises(G.BettaError): self.guard()

    def test_temporary_truth_packet_is_removed_on_success_refusal_and_exception(self):
        from tools import betta_verite as main_validator
        for outcome in ('success', 'refusal', 'exception', 'io-error'):
            with self.subTest(outcome=outcome), tempfile.TemporaryDirectory(prefix='medina-truth-test-') as parent:
                self.setUp(); self.inject()
                original = tempfile.TemporaryDirectory
                def temporary(**kwargs):
                    return original(dir=parent, **kwargs)
                def controler(packet):
                    if outcome == 'refusal': return ['fixture refusal']
                    if outcome == 'exception': raise TypeError('fixture malformed source')
                    if outcome == 'io-error': raise OSError('fixture temporary I/O failure')
                    return main_validator.controler(packet)
                api = types.ModuleType('tools.betta_verite'); api.controler = controler
                with patch.object(G, 'TemporaryDirectory', side_effect=temporary), \
                        patch.dict(sys.modules, {'tools.betta_verite': api}):
                    if outcome == 'success': self.guard()
                    else:
                        with self.assertRaises(G.BettaError): self.guard()
                self.assertEqual(list(Path(parent).iterdir()), [])

    def test_malformed_truth_packets_are_refused_without_residue(self):
        cases = (b'{', b'[]', b'{"sources": null}', b'{"sources": [null]}', b'{"sources": [{"id": []}]}')
        for malformed in cases:
            with self.subTest(malformed=malformed), tempfile.TemporaryDirectory(prefix='medina-truth-test-') as parent:
                self.setUp(); self.inject()
                path = self.row()['dir'] + '/sources.json'
                self.files[path] = malformed; self.row()['files'][path] = digest(malformed)
                original = tempfile.TemporaryDirectory
                with patch.object(G, 'TemporaryDirectory', side_effect=lambda **kw: original(dir=parent, **kw)):
                    with self.assertRaises(G.BettaError): self.guard()
                self.assertEqual(list(Path(parent).iterdir()), [])

    def test_invalid_research_encoding_is_refused_without_residue(self):
        self.inject()
        path = self.row()['dir'] + '/recherche.md'
        self.files[path] = b'\xffinvalid UTF-8'; self.row()['files'][path] = digest(self.files[path])
        with tempfile.TemporaryDirectory(prefix='medina-truth-test-') as parent:
            original = tempfile.TemporaryDirectory
            with patch.object(G, 'TemporaryDirectory', side_effect=lambda **kw: original(dir=parent, **kw)):
                with self.assertRaises(G.BettaError): self.guard()
            self.assertEqual(list(Path(parent).iterdir()), [])

    def test_bad_source_directory_rejected(self):
        self.inject(); self.row()["dir"] += "/../escape"
        with self.assertRaisesRegex(G.BettaError, "hors mission"):
            self.guard()

    def test_wrong_canonical_hash_rejected(self):
        self.inject(); self.files["chapters/R25/R25_a.html"] = b"different canonical bytes"
        with self.assertRaisesRegex(G.BettaError, "différente des sources"):
            self.guard()

    def test_partial_batch_rejected(self):
        self.inject({"R25"})
        with self.assertRaisesRegex(G.BettaError, "partiellement"):
            self.guard()

    def test_cycle_cannot_claim_injection_before_its_lessons(self):
        self.status['cycles']['42']['state'] = 'INJECTE'
        with self.assertRaisesRegex(G.BettaError, 'état INJECTE'):
            self.guard()

    def test_injected_lessons_cannot_leave_stale_cycle_state(self):
        self.inject(); self.status['cycles']['42']['state'] = 'A_FAIRE'
        with self.assertRaisesRegex(G.BettaError, 'état INJECTE'):
            self.guard()

    def test_initial_registration_cannot_inject(self):
        old = dict(self.before.files); old.pop(G.NOVO_PLAN); old.pop(G.NOVO_STATUS)
        self.before = Tree(old); self.inject()
        with self.assertRaisesRegex(G.BettaError, "activation"):
            self.guard()

    def test_transfer_of_previously_injected_betta_rejected(self):
        old = dict(self.before.files)
        status = copy.deepcopy(self.legacy)
        status["cycles"]["42"] = {"state": "INJECTE", "lessons": {"R25": {"state": "INJECTE", "canonical": {}}}}
        old[G.STATUS] = encode(status); self.before = Tree(old)
        with self.assertRaisesRegex(G.BettaError, "transfert d'une leçon injectée"):
            self.guard()

    def test_transfer_of_currently_injected_betta_rejected(self):
        self.legacy["cycles"]["42"]["lessons"]["R25"] = {"state": "INJECTE", "canonical": {}}
        with self.assertRaisesRegex(G.BettaError, "transfert d'une leçon injectée"):
            self.guard()

    def test_active_betta_collision_rejected(self):
        self.legacy["cycles"]["42"]["state"] = "A_FAIRE"
        with self.assertRaisesRegex(G.BettaError, "commun à Betta actif"):
            self.guard()

    def test_tetrad_collision_rejected(self):
        self.files[G.TETRADE] = encode({"systems": [{"chapters": [["R25", "Fixture"]]}]})
        with self.assertRaisesRegex(G.BettaError, "commun aux 30"):
            self.guard()

    def test_duplicate_or_missing_status_mission_rejected(self):
        self.status["cycles"]["42"]["lessons"].pop("R25")
        with self.assertRaisesRegex(G.BettaError, "différentes du plan"):
            self.guard()

    def test_catalogue_duplicate_and_existing_covered_code_rejected(self):
        for mode in ("duplicate", "covered"):
            with self.subTest(mode=mode):
                self.setUp()
                if mode == "covered":
                    self.files["chapters.json"] = encode([{"code": "R29", "covers": ["R25"]}]); self.before = Tree(self.files)
                self.inject()
                if mode == "duplicate":
                    rows = json.loads(self.files["chapters.json"]); rows.append(rows[0]); self.files["chapters.json"] = encode(rows)
                with self.assertRaises(G.BettaError): self.guard()

    def test_preexisting_novo_course_and_receipt_are_immutable(self):
        self.inject(); self.guard(); self.save(); self.before = Tree(self.files)
        self.files["chapters/R25/R25_a.html"] = b"attempted rewrite"
        with self.assertRaisesRegex(G.BettaError, "cours injecté modifié"):
            self.guard()

    def test_editorial_plan_metadata_can_change_before_injection(self):
        self.plan['cycles'][0]['name'] = 'Editorial regrouping without reassignment'
        self.plan['rule'] = 'Metadata correction, no fabricated validation'
        self.assertEqual(self.guard(), ({}, set()))

    def test_editorial_metadata_can_change_without_rewriting_injected_evidence(self):
        self.inject(); self.guard(); self.save(); self.before = Tree(self.files)
        self.plan['cycles'][0]['name'] = 'Editorial correction'
        self.plan['cycles'][0]['agents'][0]['lessons'][0]['title'] = 'New editorial plan title, course unchanged'
        self.assertEqual(self.guard()[1], {'R25', 'E63'})
        self.save(); self.before = Tree(self.files)
        self.assertEqual(self.guard()[1], {'R25', 'E63'})

    def test_reassignment_with_injection_rejected(self):
        self.inject()
        self.plan['cycles'][0]['agents'][0]['fragment'] = 'T1'
        self.plan['cycles'][0]['agents'][0]['lessons'][0]['fragment'] = 'T1'
        rows = json.loads(self.files['chapters.json']); rows[0]['owner'] = 'T1'; self.files['chapters.json'] = encode(rows)
        with self.assertRaisesRegex(G.BettaError, 'affectations'):
            self.guard()

    def test_injected_assignment_cannot_be_changed(self):
        self.inject(); self.guard(); self.save(); self.before = Tree(self.files)
        self.plan['cycles'][0]['agents'][0]['fragment'] = 'T1'
        self.plan['cycles'][0]['agents'][0]['lessons'][0]['fragment'] = 'T1'
        with self.assertRaisesRegex(G.BettaError, 'attribution'):
            self.guard()

    def test_cannot_delete_plan_or_registry(self):
        for path in (G.NOVO_PLAN, G.NOVO_STATUS):
            files = dict(self.before.files); files.pop(path)
            with self.subTest(path=path), self.assertRaises(G.BettaError):
                G.validate(self.before, Tree(files))


class LegacyBettaCompatibilityTests(unittest.TestCase):
    def fixture(self):
        source = b"Historical technical fixture"
        code, path = "G96", "chapters/G96/G96_a.html"
        files = {G.PLAN: encode({"cycles": [{"number": 41, "agents": [{"lessons": [lesson(code)]}]}]}),
                 G.STATUS: encode({"cycles": {"41": {"lessons": {code: {"state": "INJECTE", "canonical": {path: digest(source)}}}}}}),
                 "chapters.json": encode([{"code": code, "integrated": True, "covers": [code], "production_cycle": 41,
                                           "betta": True, "audit_status": "audit_differe_non_effectue"}]), path: source}
        return files, path

    def test_unchanged_historical_proofs_still_pass(self):
        files, path = self.fixture()
        self.assertEqual(G.validate(Tree(files), Tree(files)), ({path: digest(files[path])}, {"G96"}))

    def test_historical_course_is_not_authorized_by_novo(self):
        files, path = self.fixture(); before = Tree(files); files[path] = b"changed historical fixture"
        with self.assertRaisesRegex(G.BettaError, "non enregistré"):
            G.validate(before, Tree(files))

    def test_no_registry_remains_inactive(self):
        self.assertEqual(G.validate(Tree({}), Tree({})), ({}, set()))


if __name__ == "__main__":
    unittest.main()
