"""L'extension Novo ne périme pas la preuve auteur N04 existante."""
import hashlib
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from tools import claude_cycle_gate as old
from tools import novo_cycle_gate as new


class NovoGateTests(unittest.TestCase):
    def test_legacy_tool_preserves_hash_frozen_in_n04_author_entry(self):
        path = Path(__file__).resolve().parents[1] / 'tools/claude_cycle_gate.py'
        self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(),
                         '3706186994503073a18d67ef52f11f63a4e05f7917813cb72e0523ef6a136ee6')

    def test_new_gate_adds_prompts_without_mutating_legacy_prompt_sets(self):
        prompts = old.PROMPT_SETS.copy()
        with tempfile.TemporaryDirectory() as directory, patch.object(old, 'ROOT', Path(directory)):
            root = Path(directory)
            for path in (*old.PROMPT_SETS['direct'], *new.EXTRA_PROMPTS):
                file = root / path
                file.parent.mkdir(parents=True, exist_ok=True)
                file.write_text('fixture', encoding='utf-8')
            entries = [(key, old.PROMPT_SETS['direct'][0], 'Explication écrite par agent fixture') for key in old.CHECKS]
            gate = new.make_gate('fixture', entries)
            self.assertEqual(set(gate['prompt_files']), set(old.PROMPT_SETS['direct']) | set(new.EXTRA_PROMPTS))
            self.assertEqual(len(gate['checks']), 7)
        self.assertEqual(old.PROMPT_SETS, prompts)
