"""Tests de garde à passages fictifs, sans validation médicale simulée."""
import copy
import hashlib
from pathlib import Path
import unittest

from tools import n17_calcium_import as I
from tools.espace import FragmentError, swiss_context_proof
from tools.tetrade_cycle import CycleError, validate_cycle_guard
from tests import test_tetrade_cycle as fixtures
from tests.test_tetrade_cycle import Tree, encode


class CalciumImportTests(unittest.TestCase):
    def setUp(self):
        root = Path(__file__).resolve().parents[1]
        self.data = {I.AUTHORITY: (root / I.AUTHORITY).read_bytes()}
        self.source = {
            'organization': 'Organisme fictif de test', 'title': 'Texte fictif',
            'url': 'https://example.invalid/fixture', 'version_date': '2026-10-11',
            'section': 'Fixture', 'passage': 'Aucune assertion clinique : fixture de schéma.',
            'accessed_on': '2026-10-11', 'download_sha256': 'a' * 64,
        }
        self.product = {
            'authority': {'path': I.AUTHORITY, 'sha256': I.AUTHORITY_SHA256},
            'product_name': I.PRODUCT, 'presentation': 'Mini-Plasco connect 10 ml',
            'country_of_origin': 'DE', 'status': 'import_hospitalier',
            'swiss_authorization_number': None,
            'swiss_hospital_source': dict(self.source, country='CH'),
            'professional_information': dict(self.source, country='DE',
                type='fachinformation_allemande', product_name=I.PRODUCT),
            'clinical_arbitration': 'Arbitrage fictif de test structurel, sans valeur médicale.',
            'indication_status': 'Usage fictif documenté uniquement pour tester le schéma.',
        }
        self.row = {'chapter_code': 'N17', 'kind': 'medication', 'imported_product': self.product}

    def validate(self, ident='S04', scope='chapter', code='N17'):
        I.validate_product(Tree(self.data), self.row, ident, scope, code)

    def test_scoped_documentary_contract_is_accepted(self):
        self.validate()
        self.product['professional_information'] = dict(self.source, country='CH',
            type='monographie_hospitaliere_suisse', product_name=I.PRODUCT)
        self.validate()

    def test_other_chapter_fragment_or_whole_fragment_cannot_use_exception(self):
        for args in [('S08', 'chapter', 'I63'), ('S04', 'fragment_complet', None), ('S05', 'chapter', 'E11')]:
            with self.subTest(args=args), self.assertRaisesRegex(ValueError, 'périmètre'):
                self.validate(*args)

    def test_other_product_or_presentation_is_rejected(self):
        for field, value in [('product_name', 'Calrecia'), ('presentation', 'Solution pour citrate')]:
            with self.subTest(field=field):
                old = self.product[field]; self.product[field] = value
                with self.assertRaisesRegex(ValueError, 'produit exact'):
                    self.validate()
                self.product[field] = old

    def test_fake_swiss_authorization_or_product_record_is_rejected(self):
        self.product['swiss_authorization_number'] = 'Numéro fictif'
        with self.assertRaisesRegex(ValueError, 'Swissmedic fictive'):
            self.validate()
        self.product['swiss_authorization_number'] = None
        self.row['swissmedic_product'] = {'authorization_number': 'Fictif'}
        with self.assertRaisesRegex(ValueError, 'Swissmedic fictive'):
            self.validate()

    def test_missing_local_source_or_unread_document_hash_is_rejected(self):
        hospital = self.product.pop('swiss_hospital_source')
        with self.assertRaisesRegex(ValueError, 'hospitalier suisse'):
            self.validate()
        self.product['swiss_hospital_source'] = hospital
        self.product['professional_information']['download_sha256'] = ''
        with self.assertRaisesRegex(ValueError, 'effectivement lu'):
            self.validate()

    def test_foreign_information_for_another_product_is_rejected(self):
        self.product['professional_information']['product_name'] = 'Autre spécialité'
        with self.assertRaisesRegex(ValueError, 'autre produit'):
            self.validate()

    def test_unattributed_import_or_missing_arbitration_is_rejected(self):
        for field, value in [('status', 'autorise_suisse'), ('country_of_origin', 'US'),
                             ('clinical_arbitration', ''), ('indication_status', '')]:
            with self.subTest(field=field):
                old = self.product[field]; self.product[field] = value
                with self.assertRaises(ValueError):
                    self.validate()
                self.product[field] = old

    def test_missing_or_altered_authority_is_rejected(self):
        self.data[I.AUTHORITY] += b'Alteration de fixture'
        with self.assertRaisesRegex(ValueError, 'instruction explicite'):
            self.validate()
        self.data.pop(I.AUTHORITY)
        with self.assertRaises(ValueError):
            self.validate()

    def test_real_swiss_gate_accepts_import_only_in_authorized_chapter_scope(self):
        files = {f'chapters/N17/N17_{part}.html': 'b' * 64 for part in ('a', 'd')}
        row = dict(self.row, id='fixture', claim='Assertion fictive de test',
            auditor_verdict='conforme', initial_primary_origin='swiss', final_primary_origin='swiss',
            divergence_status='none', foreign_sources=[],
            swiss_guideline=dict(self.source, status='applicable'))
        matrix = {'schema_version': 1, 'fragment_id': 'S04', 'scope': 'chapter',
                  'chapter_code': 'N17', 'source_files': files, 'unresolved_divergences': [],
                  'decisions': [row]}
        def check(scope='chapter'):
            matrix['scope'] = scope
            raw = encode(matrix); self.data['fixture/matrice.json'] = raw
            audit = {'swiss_context': {'verdict': 'conforme', 'matrix_path': 'fixture/matrice.json',
                    'matrix_sha256': hashlib.sha256(raw).hexdigest()}}
            swiss_context_proof(Tree(self.data), audit, 'S04', files, scope=scope, chapter_code='N17')
        check()
        with self.assertRaisesRegex(FragmentError, 'périmètre'):
            check('fragment_complet')
        matrix['unresolved_divergences'] = ['Divergence fictive non résolue']
        with self.assertRaisesRegex(FragmentError, 'divergence ouverte'):
            check()
        matrix['unresolved_divergences'] = []
        row.pop('imported_product')
        with self.assertRaisesRegex(FragmentError, 'FI Swissmedic du produit exact'):
            check()

    def test_import_authority_cannot_be_changed_or_deleted_during_cycle(self):
        fixture = fixtures.TetradeGuardTests(); fixture.setUp()
        fixture.files[I.AUTHORITY] = self.data[I.AUTHORITY]
        before = Tree(copy.deepcopy(fixture.files))
        for content in (None, b'Instruction remplacee'):
            with self.subTest(content=content):
                after = copy.deepcopy(fixture.files)
                if content is None:
                    after.pop(I.AUTHORITY)
                else:
                    after[I.AUTHORITY] = content
                with self.assertRaisesRegex(CycleError, 'modifiée ou supprimée'):
                    validate_cycle_guard(before, Tree(after))

    def test_n17_author_must_read_supplement_at_both_gates(self):
        fixture = fixtures.TetradeGuardTests(); fixture.setUp()
        _, data, _, _, _ = fixture.complete_review()
        fixture.files[I.AUTHORITY] = self.data[I.AUTHORITY]
        actor = 'C01-R-NEPH'
        files = {f'chapters/N17/N17_{part}.html': 'c' * 64 for part in ('a', 'b', 'c', 'd', 'pop1', 'pop2')}
        files['glossary/n17.py'] = 'c' * 64
        data.update(code='N17', actor=actor, final_files=files)
        for gate in ('entry', 'exit'):
            data[gate]['actor'] = actor
        def check():
            row = {'code': 'N17', 'author': fixture.reference('fixture/revue-n17.json', data)}
            from tools.tetrade_cycle import review
            review(Tree(fixture.files), row, 'author', actor, files)
        with self.assertRaisesRegex(CycleError, 'instruction ciblée.*entry'):
            check()
        data['entry']['supplemental_prompt_files'] = {I.AUTHORITY: I.AUTHORITY_SHA256}
        with self.assertRaisesRegex(CycleError, 'instruction ciblée.*exit'):
            check()
        data['exit']['supplemental_prompt_files'] = {I.AUTHORITY: I.AUTHORITY_SHA256}
        check()


if __name__ == '__main__':
    unittest.main()
