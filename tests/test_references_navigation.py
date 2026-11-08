"""Contrôle les liens de navigation épinglés. Ne lance aucun test de chapitre."""
import pathlib
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
INDEX = ROOT / "docs" / "collaboration" / "REFERENCES_NAVIGATION.md"

# commit, chemin, blob du fichier à ce commit
PINS = (
    ("a1c47783e8b1ed8fb8a1e3998e02419a5e6a9eab", "test_v7.py", "9f23427c3a99122e463d2b5dae9b03693e226cc6"),
    ("0f38d9aab4ef051eaa9013c4aebfdcb9d5105070", "test_preview.py", "a0d2e09178398b1317b9f8f2cefed0467e5f0735"),
    ("e986a31987d8e983a20b8211497faa69d779873d", "docs/collaboration/instructions/PARITE_LEVEE_BLOCAGES_2026-10-15.txt", "48e5a01333aa32bca76e4eafdc399d77bfc9454f"),
    ("8f5710c0cbd52ec82e2a5fbd8114fd5952beb294", "docs/collaboration/instructions/SEMIOLOGIE_FONDAMENTALE_ANALYTIQUE_2026-10-15.yaml", "cdfe98e5c13c3966acd7eb18a06823c62a7d45da"),
    ("2673735a07e05b7198e31ca01df98426f660332a", "CHAPTER_SPEC.md", "02d57042df6a056cdf12ce00e0da90d50f43a27a"),
    ("60bb210048ebb80407bc1814dce54bc71ab843b4", "docs/collaboration/betta/PROMPT_VERITE.md", "7cef299591ba21420ad54ec2f967c040fe787e2d"),
    ("e64c813f02212415f86bd71de6bf0886a943e7fa", "PROMPT_MEDINA.md", "967ff9cde4ccad55769ee759dfa8046dfb75eaef"),
    ("d40aaf7c845226429f662b710b0711ea5297d472", "docs/collaboration/ssp-v2/2026-10-15/README-V2.txt", "e74a69c256a7807291a284034da68eb7b0c6f7f4"),
    ("d40aaf7c845226429f662b710b0711ea5297d472", "docs/collaboration/ssp-v2/2026-10-15/prompt-commun-ia.yaml", "7d71fc9e7778311e5b5f30646e31c4662b9b0a63"),
    ("34840aac8123079578cbe0966144b00e0f28e986", "docs/collaboration/instructions/DELEGATION_VIAL_2026-10-15.md", "e1c8bdea849d0c7d20b12a168b8017f67722f386"),
    ("9e07092eccd14b410eb0273579f9f88cde78ccba", "docs/collaboration/instructions/DELEGATION_VIAL_2026-10-15.md", "e37960f8afb53c6c1a651d7e0a690cdafb040d9d"),
    ("e8a79c57dc51643a1c9df21d871a92e9dafe111f", "AGENT_LECON.md", "9e6920e066ec07ef9e88d7bf870a33e5cb894783"),
    ("e8a79c57dc51643a1c9df21d871a92e9dafe111f", "EXIGENCE_CALCULS.md", "7183d40cafe362fae7e8b5ce06b88ae7e5de0f5c"),
    ("e8a79c57dc51643a1c9df21d871a92e9dafe111f", "EXIGENCE_SEMIOLOGIE.md", "1d19c5bc9491543d9c8fc3c4fe6af9ac28ca332d"),
)

UNCHANGED = {
    "pack.py": "fbc15605e51e32b636f2d2530a5c5779121b5f52",
    "test_v7.py": "9f23427c3a99122e463d2b5dae9b03693e226cc6",
    "test_preview.py": "a0d2e09178398b1317b9f8f2cefed0467e5f0735",
    "CHAPTER_SPEC.md": "02d57042df6a056cdf12ce00e0da90d50f43a27a",
    "docs/collaboration/instructions/DELEGATION_VIAL_2026-10-15.md": "e37960f8afb53c6c1a651d7e0a690cdafb040d9d",
    "docs/STYLE_REDACTION.md": "9de895db39e9972bda44bf47b52b2cf47d0462f6",
}


def blob(commit, path):
    proc = subprocess.run(
        ["git", "rev-parse", f"{commit}:{path}"],
        cwd=ROOT, capture_output=True, text=True, check=False,
    )
    if proc.returncode != 0:
        raise AssertionError(proc.stderr.strip() or f"absent {commit}:{path}")
    return proc.stdout.strip()


class NavigationReferencesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = INDEX.read_text(encoding="utf-8")
        cls.readme = (ROOT / "README.md").read_text(encoding="utf-8")

    def test_index_exists_and_pins_every_proven_commit(self):
        self.assertIn("Navigation des versions prouvées", self.index)
        for commit, path, expected in PINS:
            self.assertIn(commit, self.index, commit)
            self.assertIn(path, self.index, path)
            self.assertEqual(blob(commit, path), expected)

    def test_working_tree_keeps_legacy_dependency_and_formats(self):
        for path, expected in UNCHANGED.items():
            proc = subprocess.run(
                ["git", "hash-object", str(ROOT / path)],
                cwd=ROOT, capture_output=True, text=True, check=True,
            )
            self.assertEqual(proc.stdout.strip(), expected, path)

    def test_readme_distinguishes_current_control_and_legacy_tool(self):
        self.assertIn("test_v7.py", self.readme)
        self.assertIn("test_preview.py", self.readme)
        self.assertIn("pack.py", self.readme)
        self.assertIn("REFERENCES_NAVIGATION.md", self.readme)
        self.assertIn("Contrôle courant", self.readme)

    def test_active_entries_pin_unmerged_delegation(self):
        pin = "34840aac8123079578cbe0966144b00e0f28e986"
        kept = "Cette délégation ne constitue pas un compte administrateur ni une validation médicale."
        for name in ("AGENTS.md", "CLAUDE.md", "REPRISE_SESSION.md"):
            text = (ROOT / name).read_text(encoding="utf-8")
            self.assertIn(pin, text, name)
        for name in ("AGENTS.md", "CLAUDE.md"):
            text = (ROOT / name).read_text(encoding="utf-8")
            self.assertIn(kept, text, name)
            self.assertNotIn("[la délégation actuelle](docs/collaboration/instructions/DELEGATION_VIAL_2026-10-15.md)", text)


if __name__ == "__main__":
    unittest.main()
