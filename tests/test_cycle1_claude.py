"""Fixtures de garde uniquement ; aucune validation clinique simulée."""
import copy
import json
import unittest

from tools import cycle1_claude as E, tetrade_cycle as C
from tests.test_tetrade_cycle import Tree, encode


class ClaudeExceptionTests(unittest.TestCase):
    def setUp(self):
        self.files = {C.AUTHORITY: b"Instruction historique", E.AUTHORITY: b"Exception technique fictive"}
        self.history = {"schema_version": 1, "protocol": C.PROTOCOL, "cycle": 1,
                        "authorized_cycles": [1], "authority": C.AUTHORITY,
                        "coordinator": "Codex — coordinateur du fil", "state": "ACTIF",
                        "execution_stopped": True, "chapters": []}
        baseline = {}
        for code, fragment, tag, crossed in C.MISSIONS:
            names = [f"chapters/{code}/{code}_{s}.html" for s in ("a", "b", "c", "d", "pop1", "pop2")] + [f"glossary/{code.lower()}.py"]
            hashes = {p: C.digest(b"Source de fixture") for p in names}
            directory = f"livraisons/Livraison Codex/{fragment}/travail/CYCLE_01_{code}"
            row = {"code": code, "fragment_id": fragment, "files": hashes, "source_dir": directory,
                   "writer": f"C01-R-{tag}", "cross_reviewer": f"C01-R-{crossed}",
                   "counter_reviewer": f"C01-CA-{tag}", "status": "EN_CONTRE_AUDIT",
                   "counter_audit": None, "control": None, "injection": None, "publication": None}
            for key in ("author", "cross_audit"):
                path = f"preuves/{code}-{key}.json"
                self.files[path] = encode({"final_files": hashes})
                row[key] = self.ref(path)
            self.history["chapters"].append(row)
            for path in hashes:
                self.files[path] = self.files[directory + "/" + path] = b"Source de fixture"
            baseline.update(hashes)
        self.files[E.HISTORY] = encode(self.history)
        self.files[E.STOP_RECEIPT] = encode({"files": baseline})
        self.state = copy.deepcopy(self.history); self.state["execution_stopped"] = False
        self.files[C.REGISTRY] = encode(self.state)
        self.files["chapters.json"] = encode([{"code": c, "integrated": True, "covers": [c],
                                                "production_cycle": 1, "provisional_injection": True} for c in E.CODES])
        self.files["preuves/delta.json"] = encode({"actor": "Codex", "files": {}})
        self.technical = {"files": baseline, "result": "passed", "desktop": True, "mobile": True,
                          "javascript_errors": [], "missing_windows": []}
        self.files["preuves/technical.json"] = encode(self.technical)
        self.receipt = {"schema_version": 1, "cycle": 1, "authority": E.AUTHORITY,
                        "authority_sha256": C.digest(self.files[E.AUTHORITY]),
                        "state": "INJECTE_AUDIT_CLAUDE_DIFFERE", "execution_stopped": False,
                        "open_for_claude": True, "audit_assigned_to": "Claude",
                        "counter_audits_performed": False, "medical_final_control_performed": False,
                        "medical_human_validation": False, "files": baseline, "baseline_files": baseline,
                        "historical_state": self.ref(E.HISTORY), "historical_stop": self.ref(E.STOP_RECEIPT),
                        "change_report": self.ref("preuves/delta.json"), "technical_checks": self.ref("preuves/technical.json")}
        self.save()
        initial = copy.deepcopy(self.files); initial.pop(E.RECEIPT)
        initial[C.REGISTRY] = encode(self.history)
        self.before = Tree(initial)

    def ref(self, path):
        return {"path": path, "sha256": C.digest(self.files[path])}

    def save(self):
        self.files[E.RECEIPT] = encode(self.receipt)

    def guard(self):
        self.save()
        return C.validate_cycle_guard(self.before, Tree(self.files))

    def test_exception_publishes_all_four_without_counter_audit(self):
        authorised, codes = self.guard()
        self.assertEqual(codes, set(E.CODES))
        self.assertEqual(len(authorised), 29)

    def test_current_source_cannot_change_without_trace_and_checks(self):
        self.files["chapters/D50/D50_a.html"] += b"Correction"
        with self.assertRaisesRegex(C.CycleError, "empreinte courante"):
            self.guard()

    def test_claude_can_correct_without_counter_audit_when_changes_are_traced(self):
        self.save(); self.before = Tree(copy.deepcopy(self.files))
        path = "chapters/D50/D50_a.html"
        old = self.receipt["files"][path]
        self.files[path] += b"Correction"
        new = C.digest(self.files[path])
        self.receipt["files"] = dict(self.receipt["files"], **{path: new})
        self.files["preuves/delta-claude.json"] = encode({"actor": "Claude", "files": {path: {"before": old, "after": new, "reason": "Correction de fixture"}}})
        self.receipt["change_report"] = self.ref("preuves/delta-claude.json")
        self.technical["files"] = self.receipt["files"]
        self.files["preuves/technical.json"] = encode(self.technical)
        self.receipt["technical_checks"] = self.ref("preuves/technical.json")
        self.assertEqual(self.guard()[0][path], new)

    def test_false_claim_of_completed_counter_audit_is_refused(self):
        self.receipt["counter_audits_performed"] = True
        with self.assertRaisesRegex(C.CycleError, "non effectué"):
            self.guard()

    def test_old_receipts_remain_immutable(self):
        self.files[E.STOP_RECEIPT] += b" "
        with self.assertRaises(C.CycleError):
            self.guard()

    def test_no_exception_for_a_fifth_chapter(self):
        self.receipt["files"] = dict(self.receipt["files"], **{"chapters/G45/G45_a.html": C.digest(b"Fixture")})
        with self.assertRaisesRegex(C.CycleError, "28 fichiers"):
            self.guard()

    def test_current_checks_cannot_be_reused_after_correction(self):
        self.receipt["files"] = dict(self.receipt["files"])
        path = "chapters/D50/D50_a.html"
        self.files[path] += b"Correction"
        self.receipt["files"][path] = C.digest(self.files[path])
        self.files["preuves/delta.json"] = encode({"actor": "Codex", "files": {path: {"before": self.receipt["baseline_files"][path], "after": self.receipt["files"][path], "reason": "Fixture"}}})
        self.receipt["change_report"] = self.ref("preuves/delta.json")
        with self.assertRaisesRegex(C.CycleError, "technique"):
            self.guard()

    def test_receipt_cannot_be_removed_to_reinstate_untracked_changes(self):
        self.save(); self.before = Tree(copy.deepcopy(self.files))
        self.files.pop(E.RECEIPT)
        with self.assertRaisesRegex(C.CycleError, "reçu supprimé"):
            C.validate_cycle_guard(self.before, Tree(self.files))


if __name__ == "__main__":
    unittest.main()
