"""Le texte des mots verts conserve la couverture des sigles connus."""
import unittest

import build_medina as B


class AuditGlossaryBoundariesTests(unittest.TestCase):
    @staticmethod
    def protected(text):
        return '<span class="mc-w" data-k="audit-fixture">' + text + '</span>'

    def test_known_constituents_in_hyphenated_medical_terms(self):
        for key in ('ERC', 'ESICM', 'BPCO', 'COPD', 'HLA', 'SOFA'):
            self.assertIn(key, B.G)
        text = 'ERC-ESICM ; pré-BPCO ; COPD-exacerbations ; HLA-B ; SOFA-2'
        self.assertEqual(B.audit(self.protected(text), 'fixture'), {})

    def test_known_constituents_in_slash_separated_antibodies(self):
        for key in ('ADN', 'SSA', 'SSB', 'RNP'):
            self.assertIn(key, B.G)
        self.assertEqual(B.audit(self.protected('anti-ADN/SSA/SSB/RNP'), 'fixture'), {})

    def test_unknown_constituents_and_missing_lexical_boundaries_remain_reported(self):
        self.assertNotIn('ZZQINCONNU', B.G)
        cases = {
            'ERC-ZZQINCONNU': {'ZZQINCONNU': 1},
            'ZZQINCONNU/SSA/SSB': {'ZZQINCONNU': 1},
            'ERCZZQINCONNU': {'ERCZZQINCONNU': 1},
        }
        for text, expected in cases.items():
            with self.subTest(text=text):
                self.assertEqual(B.audit(self.protected(text), 'fixture'), expected)


if __name__ == '__main__':
    unittest.main()
