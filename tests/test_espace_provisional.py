"""Technical fixtures for Vial's narrow provisional C-01 exception.

Fixture reports do not simulate a medical verdict or execute a browser check.
Real project sources are only read to obtain the 22-fragment reference registry.
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

from tools.provisional_integration import ProvisionalError, validate_provisional


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("provisional_espace", ROOT / "tools/espace.py")
ESPACE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ESPACE)
REGISTRY = "organisation/provisional_integrations.json"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def reservation_html(extra="", duplicate=False):
    marker = ('<div class="alert" id="i70-reserve-1" data-claude-reservation="C01-MED-1" '
              'data-reservation-status="open" ' + extra + '><b>Réserve clinique.</b> '
              'La proposition n’est pas validée et ne constitue pas une conduite applicable.</div>')
    return ('<template id="ch-I70"><div class="chap">' + marker * (2 if duplicate else 1) + '</div></template>').encode()


class ProvisionalGuardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.git("init", "-q")
        self.git("config", "user.name", "Fixture locale")
        self.git("config", "user.email", "fixture@example.invalid")
        registry = json.loads((ROOT / ESPACE.FRAGMENT_REGISTRY).read_text())
        self.write_json(ESPACE.FRAGMENT_REGISTRY, registry)
        self.write_json("fragments.json", [{"id": "S01", "rattachements": ["I70"]},
                                            {"id": "S02", "rattachements": ["J45"]}])
        self.fragments = [{"id": item["id"], "label": item["label"],
                           "owner": "Partage historique" if item["id"] == "S01" else "Claude",
                           "status": "A_COMPLETER", "complete": False,
                           "coverage": {"status": "non_etablie", "inventory_path": None},
                           "internal_review": None, "cross_audit": None,
                           "injection": None, "locked_files": {}} for item in registry]
        self.write_json(ESPACE.FRAGMENT_STATUS, {"schema_version": 1, "protocol": ESPACE.PROTOCOL,
                                                 "fragments": self.fragments})
        self.courses = [{"code": "I70", "title": "Cours de fixture artériopathie", "integrated": True},
                        {"code": "J45", "title": "Cours de fixture asthme", "integrated": True}]
        self.write_json("chapters.json", self.courses)
        self.medical = "chapters/I70/I70_a.html"
        self.initial_data = b"Source initiale de fixture, sans valeur clinique."
        self.write(self.medical, self.initial_data)
        self.write("chapters/J45/J45_a.html", b"Ancien cours tiers de fixture")
        self.initial = self.commit()
        self.adapted = reservation_html()
        self.record = {
            "id": "C01-TEST-1", "fragment_id": "S01", "label": "C-01-Cardiologie",
            "status": "PROVISOIRE_AVEC_RESERVES", "base_commit": self.initial,
            "authority": {"requested_by": "Vial", "request_path": "preuves/instruction.md",
                          "request_sha256": digest(b"Instruction explicite de fixture : exception C-01.")},
            "courses": ["I70"], "source_dir": "adaptations/test-1/sources",
            "files": {self.medical: {"before_sha256": digest(self.initial_data), "sha256": digest(self.adapted)}},
            "report_path": "preuves/revue.md", "report_sha256": digest(b"Revue de fixture, sans valeur clinique."),
            "checks": [{"kind": kind, "result": "passed", "evidence_path": f"preuves/{kind}.json",
                        "evidence_sha256": digest((kind + " : preuve technique de fixture").encode())}
                       for kind in ["unit", "static", "build", "desktop", "mobile"]],
            "reservations": [{"id": "C01-MED-1", "course": "I70", "status": "open",
                              "reason": "Source quantitative manquante dans la fixture.",
                              "action": "Claude doit contrôler la source avant de lever la réserve.",
                              "targets": [{"path": self.medical, "marker_id": "i70-reserve-1"}]}],
        }
        self.write("preuves/instruction.md", b"Instruction explicite de fixture : exception C-01.")
        self.write("preuves/revue.md", b"Revue de fixture, sans valeur clinique.")
        for check in self.record["checks"]:
            self.write(check["evidence_path"], (check["kind"] + " : preuve technique de fixture").encode())
        self.write(self.medical, self.adapted)
        self.write(self.record["source_dir"] + "/" + self.medical, self.adapted)
        self.items = [self.record]
        self.save()

    def git(self, *args):
        return subprocess.run(["git", *args], cwd=self.root, check=True,
                              capture_output=True).stdout.decode().strip()

    def write(self, path, data):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)

    def write_json(self, path, value):
        self.write(path, (json.dumps(value, ensure_ascii=False) + "\n").encode())

    def save(self):
        self.write_json(REGISTRY, {"schema_version": 1, "kind": "exception_c01_vial_2026-10-08",
                                   "integrations": self.items})

    def commit(self):
        self.git("add", ".")
        self.git("commit", "-qm", "Fixture locale", "--allow-empty")
        return self.git("rev-parse", "HEAD")

    def guard(self, before=None):
        self.save()
        return ESPACE.validate_fragment_guard(ESPACE.GitTree(self.root, before or self.initial),
                                             ESPACE.GitTree(self.root, self.commit()))

    def replacement(self, data):
        self.adapted = data
        self.record["files"][self.medical]["sha256"] = digest(data)
        self.write(self.medical, data)
        self.write(self.record["source_dir"] + "/" + self.medical, data)

    def test_scoped_provisional_change_preserves_final_registry(self):
        self.assertEqual(self.guard(), [])
        self.assertEqual(json.loads((self.root / ESPACE.FRAGMENT_STATUS).read_text())["fragments"], self.fragments)

    def test_new_course_requires_explicit_owner_and_catalogued_copy(self):
        code, target = "I51", "chapters/I51/I51_a.html"
        body = self.adapted.replace(b"I70", b"I51").replace(b"i70", b"i51")
        self.courses.append({"code": code, "title": "Cours de fixture cardiaque", "integrated": True, "owner": "S01"})
        self.write_json("chapters.json", self.courses)
        catalog_data = (self.root / "chapters.json").read_bytes()
        original_catalog = self.git("show", self.initial + ":chapters.json").encode() + b"\n"
        self.record["courses"] = [code]
        self.record["files"] = {target: {"before_sha256": None, "sha256": digest(body)},
                                "chapters.json": {"before_sha256": digest(original_catalog), "sha256": digest(catalog_data)}}
        self.record["reservations"][0].update({"course": code, "targets": [{"path": target, "marker_id": "i51-reserve-1"}]})
        self.write(self.medical, self.initial_data)
        self.write(target, body)
        self.write(self.record["source_dir"] + "/" + target, body)
        self.write(self.record["source_dir"] + "/chapters.json", catalog_data)
        self.assertEqual(self.guard(), [])

    def test_untracked_medical_change_remains_rejected(self):
        self.write("chapters/J45/J45_a.html", b"Changement tiers interdit")
        self.assertEqual(self.guard(), ["chapters/J45/J45_a.html"])

    def test_partial_operation_commands_remain_disabled(self):
        with patch.object(ESPACE, "R", self.root):
            with self.assertRaisesRegex(ESPACE.FragmentError, "par cours/remise partielle"):
                ESPACE.refuse_chapter_operation("injecter")

    def test_different_baseline_is_rejected(self):
        self.record["base_commit"] = "0" * 40
        with self.assertRaisesRegex(ESPACE.FragmentError, "baseline différente"):
            self.guard()

    def test_false_original_hash_is_rejected(self):
        self.record["files"][self.medical]["before_sha256"] = "0" * 64
        with self.assertRaisesRegex(ESPACE.FragmentError, "source de baseline"):
            self.guard()

    def test_false_proposed_hash_is_rejected(self):
        self.record["files"][self.medical]["sha256"] = "0" * 64
        with self.assertRaisesRegex(ESPACE.FragmentError, "empreinte différente"):
            self.guard()

    def test_live_canonical_differs_from_adaptation_is_rejected(self):
        self.write(self.medical, b"Source autre que la revue")
        with self.assertRaisesRegex(ESPACE.FragmentError, "source injectée différente"):
            self.guard()

    def test_missing_adapted_source_is_rejected(self):
        (self.root / self.record["source_dir"] / self.medical).unlink()
        with self.assertRaisesRegex(ESPACE.FragmentError, "Fichier absent"):
            self.guard()

    def test_sources_cannot_be_canonical_aliases(self):
        self.record["source_dir"] = "chapters"
        with self.assertRaisesRegex(ESPACE.FragmentError, "séparées"):
            self.guard()

    def test_different_fragment_is_rejected(self):
        self.record["fragment_id"] = "S02"
        with self.assertRaisesRegex(ESPACE.FragmentError, "limitée aux cours"):
            self.guard()

    def test_unapproved_c01_course_is_rejected(self):
        self.record["courses"] = ["I83"]
        with self.assertRaisesRegex(ESPACE.FragmentError, "limitée aux cours"):
            self.guard()

    def test_path_of_another_course_is_rejected(self):
        self.record["files"]["chapters/J45/J45_a.html"] = copy.deepcopy(self.record["files"][self.medical])
        with self.assertRaisesRegex(ESPACE.FragmentError, "hors périmètre"):
            self.guard()

    def test_path_traversal_is_rejected(self):
        self.record["source_dir"] = "../exterieur"
        with self.assertRaisesRegex(ESPACE.FragmentError, "chemin relatif sûr"):
            self.guard()

    def test_reservation_target_outside_course_is_rejected(self):
        self.record["reservations"][0]["targets"][0]["path"] = "chapters/J45/J45_a.html"
        with self.assertRaisesRegex(ESPACE.FragmentError, "hors du cours"):
            self.guard()

    def test_missing_marker_is_rejected(self):
        self.replacement(b"<p>Une source sans signal de reserve visible.</p>")
        with self.assertRaisesRegex(ESPACE.FragmentError, "marque de réserve absente"):
            self.guard()

    def test_hidden_or_duplicate_markers_are_rejected(self):
        for extra in ['hidden', 'aria-hidden="true"', 'style="display: none"',
                      'style="visibility:hidden"', 'style="opacity:0"']:
            with self.subTest(extra=extra):
                self.replacement(reservation_html(extra))
                with self.assertRaisesRegex(ESPACE.FragmentError, "non masquée"):
                    self.guard()
        self.replacement(reservation_html(duplicate=True))
        with self.assertRaisesRegex(ESPACE.FragmentError, "dupliquée"):
            self.guard()

    def test_missing_reserve_or_reason_is_rejected(self):
        self.record["reservations"][0]["reason"] = ""
        with self.assertRaisesRegex(ESPACE.FragmentError, "motif et action"):
            self.guard()
        self.record["reservations"] = []
        with self.assertRaisesRegex(ESPACE.FragmentError, "réserves cliniques ouvertes"):
            self.guard()

    def test_unexecuted_or_missing_browser_check_is_rejected(self):
        self.record["checks"][-1]["result"] = "not_executed"
        with self.assertRaisesRegex(ESPACE.FragmentError, "non réussi"):
            self.guard()
        self.record["checks"].pop()
        with self.assertRaisesRegex(ESPACE.FragmentError, "bureau et mobile"):
            self.guard()

    def test_malformed_check_or_catalogue_is_refused_cleanly(self):
        self.record["checks"][0]["kind"] = ["unit"]
        with self.assertRaisesRegex(ESPACE.FragmentError, "bureau et mobile"):
            self.guard()
        self.record["checks"][0]["kind"] = "unit"
        self.courses[0]["code"] = ["I70"]
        self.write_json("chapters.json", self.courses)
        with self.assertRaisesRegex(ESPACE.FragmentError, "catalogue des cours invalide"):
            self.guard()

    def test_missing_evidence_is_rejected(self):
        (self.root / self.record["checks"][0]["evidence_path"]).unlink()
        with self.assertRaisesRegex(ESPACE.FragmentError, "Fichier absent"):
            self.guard()

    def test_symlink_evidence_is_rejected(self):
        evidence = self.root / self.record["checks"][0]["evidence_path"]
        evidence.unlink()
        evidence.symlink_to("/etc/passwd")
        with self.assertRaisesRegex(ESPACE.FragmentError, "non régulière"):
            self.guard()

    def test_explicit_instruction_author_is_required(self):
        self.record["authority"]["requested_by"] = "Claude"
        with self.assertRaisesRegex(ESPACE.FragmentError, "instruction exceptionnelle"):
            self.guard()

    def test_false_final_state_cannot_be_set_by_exception(self):
        self.fragments[0]["status"] = "INJECTE"
        self.write_json(ESPACE.FRAGMENT_STATUS, {"schema_version": 1, "protocol": ESPACE.PROTOCOL, "fragments": self.fragments})
        with self.assertRaisesRegex(ESPACE.FragmentError, "fragment incomplet"):
            self.guard()

    def test_exception_itself_refuses_already_terminal_fragment(self):
        # The normal guard tests separately exercise real locked fragments.
        # This isolates the exception's own check without manufacturing final
        # medical review/completion evidence in a provisional fixture.
        self.save()
        after = self.commit()
        fragment = copy.deepcopy(self.fragments[0])
        fragment["status"] = "INJECTE"
        with self.assertRaisesRegex(ProvisionalError, "INJECTE immuable"):
            validate_provisional(ESPACE.GitTree(self.root, self.initial),
                                 ESPACE.GitTree(self.root, after),
                                 {"S01": fragment}, {"S01": fragment})

    def test_no_complete_claim_in_provisional_catalogue(self):
        original = (self.root / "chapters.json").read_bytes()
        self.courses[0]["complete"] = True
        self.write_json("chapters.json", self.courses)
        final = (self.root / "chapters.json").read_bytes()
        self.record["files"]["chapters.json"] = {"before_sha256": digest(original), "sha256": digest(final)}
        self.write(self.record["source_dir"] + "/chapters.json", final)
        with self.assertRaisesRegex(ESPACE.FragmentError, "cours, code et titre"):
            self.guard()

    def test_catalogue_cannot_change_unannounced_course(self):
        before = (self.root / "chapters.json").read_bytes()
        self.courses[1]["title"] = "Ancien cours tiers modifié sans revue"
        self.write_json("chapters.json", self.courses)
        after = (self.root / "chapters.json").read_bytes()
        self.record["files"]["chapters.json"] = {"before_sha256": digest(before), "sha256": digest(after)}
        self.write(self.record["source_dir"] + "/chapters.json", after)
        with self.assertRaisesRegex(ESPACE.FragmentError, "cours tiers"):
            self.guard()

    def test_ledger_is_append_only(self):
        self.save()
        first = self.commit()
        self.record["report_path"] = "preuves/nouveau.md"
        with self.assertRaisesRegex(ESPACE.FragmentError, "réécriture"):
            self.guard(first)

    def test_unchanged_ledger_can_publish_documents_without_new_authorization(self):
        self.assertEqual(self.guard(), [])
        first = self.git("rev-parse", "HEAD")
        self.write("docs/note.md", b"Nouvelle note documentaire sans correction canonique")
        self.assertEqual(self.guard(first), [])

    def test_old_proof_does_not_authorize_untracked_later_correction(self):
        self.assertEqual(self.guard(), [])
        first = self.git("rev-parse", "HEAD")
        self.write(self.medical, b"Nouvelle correction non inventoriee")
        self.assertEqual(self.guard(first), [self.medical])


if __name__ == "__main__":
    unittest.main()
