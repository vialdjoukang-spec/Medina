"""Reprise et ligne d'état : fixtures uniquement, sans Git ni réseau."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("medina_resume", ROOT / "tools/medina_resume.py")
RESUME = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RESUME)


def write_json(root, path, payload):
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload), encoding="utf-8")


def fixture(root, canonical=10):
    original = {"systems": [{"id": f"S{i}", "chapters": [[f"{letter}{n:02d}", "mission"] for n in range(30)]}
                            for i, letter in enumerate("ABCD")]}
    write_json(root, RESUME.PLAN, original)
    codes = [row[0] for system in original["systems"] for row in system["chapters"]]
    write_json(root, RESUME.CATALOG, [{"code": code, "integrated": True} for code in codes[:canonical]])
    write_json(root, RESUME.REGISTRY, {"cycles": [{"cycle": 3, "state": "ACTIF", "chapters": [
        {"code": "A02", "status": "PUBLIE_VERIFIE"}, {"code": "B02", "status": "INJECTE"},
        {"code": "C02", "status": "PRET_A_INJECTER"}, {"code": "D02", "status": "PRET_A_INJECTER"}]}]})
    batches = []
    for number in range(1, 10):
        cycles = list(range(4 + (number - 1) * 3, 7 + (number - 1) * 3))
        batches.append({"novo": number, "tetrad_cycles": cycles, "systems": [
            {"id": system["id"], "lessons": [system["chapters"][n - 1][0] for n in cycles]}
            for system in original["systems"]]})
    write_json(root, RESUME.NOVO, {"id": "NOVO_12", "cycles": batches})
    write_json(root, RESUME.BETTA, {"cycles": {"31": {"state": "ACTIF", "lessons": {
        "X01": {"state": "INJECTE"}, "X02": {"state": "LIVRE"},
        "X03": "A_FAIRE", "X04": {"state": "EN_REDACTION"}}}}})
    return original


def novo_betta_fixture(root, count=43):
    codes = [f"X{i:03d}" for i in range(count)]
    groups = [codes[index:index + 12] for index in range(0, count, 12)]
    cycles = [{"number": 42 + index, "lessons": len(group),
               "agents": [{"lessons": [{"code": code} for code in group]}]}
              for index, group in enumerate(groups)]
    write_json(root, RESUME.BETTA_NOVO_PLAN, {"id": "novo12", "first": 42, "last": 41 + len(groups),
                                           "total_lessons": count, "cycles": cycles})
    status = {"plan": RESUME.BETTA_NOVO_PLAN, "cycles": {str(42 + index): {"state": "A_FAIRE", "lessons": {
        code: ("LIVRE" if code == codes[0] else {"state": "INJECTE"} if code == codes[1] else "A_FAIRE")
        for code in group}} for index, group in enumerate(groups)}}
    write_json(root, RESUME.BETTA_NOVO_STATUS, status)
    return codes


class MedinaResumeTests(unittest.TestCase):
    def test_missing_json_is_unavailable_not_zero_progress(self):
        with tempfile.TemporaryDirectory() as tmp:
            report = RESUME.summarize(Path(tmp))
        self.assertEqual(len(report["warnings"]), 5)
        self.assertIsNone(report["sequence_1_30"]["canonical_catalogue"])
        self.assertIsNone(report["sequence_1_30"]["public_confirmed"])
        self.assertIsNone(report["betta_31_plus"])
        self.assertIn("indisponible", RESUME.status_line(report))
        self.assertNotIn("0/120", RESUME.status_line(report))

    def test_invalid_json_and_types_are_explicit(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root)
            (root / RESUME.PLAN).write_text("{invalide", encoding="utf-8")
            write_json(root, RESUME.BETTA, [])
            report = RESUME.summarize(root)
        self.assertIsNone(report["sequence_1_30"]["planned"])
        self.assertIsNone(report["betta_31_plus"])
        self.assertEqual(len(report["warnings"]), 2)

    def test_ten_canonical_lessons_do_not_mean_ten_published(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root, canonical=10)
            report = RESUME.summarize(root)
            text = RESUME.render(report)
        self.assertFalse(report["warnings"])
        self.assertEqual(report["sequence_1_30"]["canonical_catalogue"], 10)
        self.assertEqual(report["sequence_1_30"]["planned"], 120)
        self.assertIsNone(report["sequence_1_30"]["public_confirmed"])
        self.assertIn("10/120 canoniques au catalogue", text)
        self.assertIn("public non vérifié ici", text)
        self.assertNotIn("10 publi", text)
        self.assertIn("A02=PUBLIE_VERIFIE", text)

    def test_false_and_duplicate_catalogue_entries_do_not_inflate_count(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root, canonical=10)
            catalog = json.loads((root / RESUME.CATALOG).read_text())
            catalog.extend([catalog[0], {"code": "A10", "integrated": False}, {"code": "Z99", "integrated": True}])
            write_json(root, RESUME.CATALOG, catalog)
            self.assertEqual(RESUME.summarize(root)["sequence_1_30"]["canonical_catalogue"], 10)

    def test_novo_batch_is_one_anchor_for_three_old_cycles(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            original = fixture(root)
            rows = [{"code": system["chapters"][n - 1][0], "status": "EN_PRODUCTION"}
                    for n in (4, 5, 6) for system in original["systems"]]
            write_json(root, RESUME.REGISTRY, {"cycles": [{"cycle": 4, "novo": 1, "tetrad_cycles": [4, 5, 6],
                                                         "state": "ACTIF", "chapters": rows}]})
            report = RESUME.summarize(root)
        cycle = report["sequence_1_30"]["claude_cycles"][0]
        batches = report["sequence_1_30"]["novo_batches"]
        self.assertFalse(report["warnings"])
        self.assertEqual(cycle["anchor"], 4)
        self.assertEqual(cycle["tetrad_cycles"], [4, 5, 6])
        self.assertEqual(len(cycle["lessons"]), 12)
        self.assertEqual(batches[1]["anchor"], 7)
        self.assertEqual(sum(batch["lesson_count"] for batch in batches), 108)
        self.assertIn("Novo Tétrade 1 (anciens cycles 4, 5, 6)", RESUME.render(report))

    def test_betta_completion_requires_explicit_lesson_state(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root)
            report = RESUME.summarize(root)
        self.assertEqual(report["betta_31_plus"], {"cycles": 1, "lessons": 4,
                         "delivered_including_injected": 2, "injected": 1, "transferred_to_novo": 0})
        self.assertIn("Betta 31+ : 2/4 livrées (dont 1 injectées)", RESUME.status_line(report))

    def test_novo_betta_is_not_mixed_with_novo_tetrade(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root)
            novo_betta_fixture(root)
            report = RESUME.summarize(root)
        self.assertFalse(report["warnings"])
        self.assertEqual(report["sequence_1_30"]["planned"], 120)
        self.assertEqual(len(report["sequence_1_30"]["novo_batches"]), 9)
        self.assertEqual(report["betta_31_plus"]["lessons"], 4)
        self.assertEqual(report["novo_betta"]["lessons"], 43)
        self.assertEqual(report["novo_betta"]["delivered_including_injected"], 2)
        self.assertEqual(report["novo_betta"]["injected"], 1)
        self.assertIn("Novo Betta 42–45 : 2/43", RESUME.status_line(report))

    def test_forty_three_betta_transfers_are_not_double_counted(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root)
            codes = novo_betta_fixture(root)
            status = json.loads((root / RESUME.BETTA).read_text())
            status["cycles"]["42"] = {"state": "TRANSFERE_NOVO12", "lessons": {code: "A_FAIRE" for code in codes}}
            write_json(root, RESUME.BETTA, status)
            report = RESUME.summarize(root)
        self.assertFalse(report["warnings"])
        self.assertEqual(report["betta_31_plus"]["lessons"], 4)
        self.assertEqual(report["betta_31_plus"]["cycles"], 1)
        self.assertEqual(report["betta_31_plus"]["transferred_to_novo"], 43)
        self.assertEqual(report["novo_betta"]["lessons"], 43)
        self.assertIn("43 leçons transférées", RESUME.render(report))

    def test_optional_novo_betta_absence_preserves_legacy_fixtures(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root)
            report = RESUME.summarize(root)
        self.assertIsNone(report["novo_betta"])
        self.assertFalse(report["warnings"])

    def test_novo_betta_mismatched_plan_or_status_is_unavailable(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root)
            novo_betta_fixture(root)
            status = json.loads((root / RESUME.BETTA_NOVO_STATUS).read_text())
            del status["cycles"]["42"]["lessons"]["X000"]
            write_json(root, RESUME.BETTA_NOVO_STATUS, status)
            report = RESUME.summarize(root)
        self.assertIsNone(report["novo_betta"])
        self.assertTrue(any("Novo Betta" in error for error in report["warnings"]))
        self.assertNotIn("Novo Betta 42–45 : 0/", RESUME.status_line(report))

    def test_novo_betta_requires_both_json_files_when_either_exists(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root)
            write_json(root, RESUME.BETTA_NOVO_STATUS, {"cycles": {}})
            report = RESUME.summarize(root)
        self.assertIsNone(report["novo_betta"])
        self.assertTrue(report["warnings"])

    def test_status_line_ignores_stdin_and_never_writes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root)
            before = {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}
            run = subprocess.run([sys.executable, str(ROOT / "tools/medina_resume.py"), "--root", str(root), "--status-line"],
                                 input='{"model": "sans effet"}\n', text=True, capture_output=True)
            after = {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(before, after)
        self.assertEqual(len(run.stdout.splitlines()), 1)
        self.assertIn("Tétrade 1–30", run.stdout)
        self.assertIn("Betta 31+", run.stdout)

    def test_status_line_with_missing_files_does_not_break_ui(self):
        with tempfile.TemporaryDirectory() as tmp:
            run = subprocess.run([sys.executable, str(ROOT / "tools/medina_resume.py"), "--root", tmp, "--status-line"],
                                 input="JSON ignoré même invalide", text=True, capture_output=True)
        self.assertEqual(run.returncode, 0)
        self.assertIn("réserves", run.stdout)

    def test_chat_progress_has_active_cycle_gauges_not_global_public_guess(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root)
            report = RESUME.summarize(root)
            text = RESUME.chat_progress(report)
        self.assertIn("🟦 10/120 canoniques au catalogue ; public non vérifié ici", text)
        self.assertIn("🟩🟦🟨🟨", text)
        self.assertIn("🟩 Déclarées publiées 1/4", text)
        self.assertIn("publication non encore déclarée 1/4", text)
        self.assertIn("🟨 Prêtes à injecter 2/4", text)
        self.assertIn("Cycle 1 absent de ce registre : non compté ici", text)
        self.assertIn("couverture partielle, pas de total public sur 120", text)
        self.assertIsNone(report["sequence_1_30"]["public_confirmed"])
        self.assertNotIn("5/120", text)
        self.assertNotIn("8/120", text)
        self.assertNotIn("9/120", text)

    def test_chat_progress_ignores_closed_cycle_for_active_denominator(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root)
            registry = json.loads((root / RESUME.REGISTRY).read_text())
            registry["cycles"].insert(0, {"cycle": 2, "state": "CLOTURE", "chapters": [
                {"code": f"{letter}01", "status": "PUBLIE_VERIFIE"} for letter in "ABCD"]})
            write_json(root, RESUME.REGISTRY, registry)
            text = RESUME.chat_progress(RESUME.summarize(root))
        self.assertIn("Couverture du registre Claude : 2, 3", text)
        self.assertIn("Déclarées publiées 1/4", text)
        self.assertNotIn("Déclarées publiées 5/", text)

    def test_chat_progress_counts_follow_changed_source_not_fixed_numbers(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root, canonical=11)
            registry = json.loads((root / RESUME.REGISTRY).read_text())
            registry["cycles"][0]["chapters"][1]["status"] = "PUBLIE_VERIFIE"
            write_json(root, RESUME.REGISTRY, registry)
            text = RESUME.chat_progress(RESUME.summarize(root))
        self.assertIn("11/120 canoniques au catalogue", text)
        self.assertIn("Déclarées publiées 2/4", text)
        self.assertIn("publication non encore déclarée 0/4", text)

    def test_chat_progress_novo_cycle_uses_twelve_as_actual_denominator(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            original = fixture(root)
            states = ["PUBLIE_VERIFIE"] * 2 + ["INJECTE"] * 3 + ["PRET_A_INJECTER"] * 4 + ["EN_PRODUCTION"] * 3
            codes = [system["chapters"][n - 1][0] for n in (4, 5, 6) for system in original["systems"]]
            write_json(root, RESUME.REGISTRY, {"cycles": [{"cycle": 4, "novo": 1, "tetrad_cycles": [4, 5, 6],
                "state": "ACTIF", "chapters": [{"code": code, "status": state} for code, state in zip(codes, states)]}]})
            text = RESUME.chat_progress(RESUME.summarize(root))
        self.assertIn("Novo Tétrade 1 (anciens cycles 4, 5, 6) — 12 leçons", text)
        self.assertIn("Déclarées publiées 2/12", text)
        self.assertIn("publication non encore déclarée 3/12", text)
        self.assertIn("Prêtes à injecter 4/12", text)
        self.assertIn("Autres états 3/12", text)

    def test_chat_progress_preserves_distinct_plans_and_transfer_counts(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root)
            codes = novo_betta_fixture(root)
            status = json.loads((root / RESUME.BETTA).read_text())
            status["cycles"]["42"] = {"state": "TRANSFERE_NOVO12", "lessons": {code: "A_FAIRE" for code in codes}}
            write_json(root, RESUME.BETTA, status)
            text = RESUME.chat_progress(RESUME.summarize(root))
        self.assertIn("Novo Tétrade : 9 lots / 108 leçons planifiées", text)
        self.assertIn("Betta 31+ historique : 2/4 livrées déclarées", text)
        self.assertIn("43 leçons transférées au Novo Betta, exclues", text)
        self.assertIn("Novo Betta 42–45 : 2/43 livrées déclarées", text)
        for source in (RESUME.PLAN, RESUME.CATALOG, RESUME.REGISTRY, RESUME.NOVO,
                       RESUME.BETTA, RESUME.BETTA_NOVO_PLAN, RESUME.BETTA_NOVO_STATUS):
            self.assertIn(source, text)

    def test_chat_progress_missing_registry_never_guesses_zero_published(self):
        with tempfile.TemporaryDirectory() as tmp:
            report = RESUME.summarize(Path(tmp))
        text = RESUME.chat_progress(report)
        self.assertIn("Registre Claude indisponible", text)
        self.assertNotIn("Déclarées publiées 0/", text)
        self.assertIn("Limites", text)
        self.assertIn("Réserves", text)

    def test_chat_progress_cli_ignores_stdin_and_writes_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root)
            before = {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}
            run = subprocess.run([sys.executable, str(ROOT / "tools/medina_resume.py"), "--root", str(root), "--chat-progress"],
                                 input='{"untrusted": "aucun effet"}', text=True, capture_output=True)
            after = {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(before, after)
        self.assertIn("🟩 Déclarées publiées 1/4", run.stdout)


if __name__ == "__main__":
    unittest.main()
