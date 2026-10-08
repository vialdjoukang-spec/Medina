import importlib.util, unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('sg', Path(__file__).resolve().parent.parent / 'tools' / 'sources_guard.py')
sg = importlib.util.module_from_spec(spec); spec.loader.exec_module(sg)


class T(unittest.TestCase):
    pol = sg.load_policy()

    def test_tiers(self):
        self.assertEqual(sg.tier('https://www.swissmedicinfo.ch/x', self.pol), 'A')
        self.assertEqual(sg.tier('https://www.escardio.org/g', self.pol), 'B')
        self.assertEqual(sg.tier('https://pubmed.ncbi.nlm.nih.gov/1/', self.pol), 'J')
        self.assertEqual(sg.tier('https://www.cdc.gov/x', self.pol), 'X')
        self.assertEqual(sg.tier('https://evilswissmedic.ch/', self.pol), 'X')

    def test_rules(self):
        import json, tempfile
        e = {'entries': [{'id': 'e', 'sources': [
            {'url': 'https://www.cdc.gov/a'}, {'url': 'https://www.cdc.gov/b', 'derogation': 'aucune source CH/EU'},
            {'url': 'https://pubmed.ncbi.nlm.nih.gov/1/'}, {'url': 'https://pubmed.ncbi.nlm.nih.gov/2/', 'origine': 'CH'},
            {'url': 'https://www.bag.admin.ch/x'}]}]}
        with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False) as f:
            json.dump(e, f)
        v = sg.violations([f.name], self.pol)
        self.assertEqual({k[1] for k in v}, {'https://www.cdc.gov/a', 'https://pubmed.ncbi.nlm.nih.gov/1/'})


if __name__ == '__main__':
    unittest.main()
