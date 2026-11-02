"""Behavioral safety tests; fixtures are synthetic and contain no medical advice."""
import copy
import datetime as dt
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest import mock

MODULE = Path(__file__).resolve().parents[1] / 'medina_harness.py'
SPEC = importlib.util.spec_from_file_location('medina_harness_test_target', MODULE)
mh = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mh)


class HarnessCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'repo'
        self.home = self.root / 'harness'
        self.home.mkdir(parents=True)
        self.config = {
            'base_sha': 'a' * 40, 'deadline': '2100-11-02T08:00:00+01:00',
            'agents': [
                {'id': 'neuro', 'specialty': 'neurologie', 'model': 'gpt-6-astra', 'reasoning': 'high', 'queue': ['G02', 'G05']},
                {'id': 'endo', 'specialty': 'endocrinologie', 'model': 'gpt-6-astra', 'reasoning': 'high', 'queue': ['E00']},
                {'id': 'nephro', 'specialty': 'nephrologie', 'model': 'gpt-6-astra', 'reasoning': 'high', 'queue': ['N04']},
                {'id': 'hemato', 'specialty': 'hematologie', 'model': 'Codex', 'queue': ['C85']},
            ],
        }
        mh.atomic(self.home / 'config.json', self.config)
        self.h = mh.Harness(self.root)
        self.prompt = self.root / 'PROMPT.md'
        self.prompt.write_text('Versioned test-only prompt.\n')
        mh.atomic(self.home / 'prompt-lock.json', {'files': [{'path': 'PROMPT.md', 'sha256': mh.digest(self.prompt.read_bytes())}]})
        (self.home / 'REPARTITION.md').write_text('Four exclusive specialties.\n')
        (self.home / 'dashboard.html').write_text('<html>Test dashboard</html>')
        self.healthy()

    def healthy(self):
        mh.atomic(self.h.runtime / 'tests.json', {'ok': True, 'code_sha256': mh.code_hash()})
        mh.atomic(self.h.runtime / 'watch.json', {'ok': True, 'observed_at': mh.now()})

    def worktree_and_receipt(self, code='G02', name=None):
        name = name or code.lower()
        worktree = self.root / ('worktree-' + name)
        worktree.mkdir()
        branch = 'codex/test-' + name
        subprocess.run(['git', 'init', '--quiet', '--initial-branch', branch, str(worktree)], check=True, capture_output=True)
        receipt = self.root / ('receipt-' + name + '.json')
        mh.atomic(receipt, {'mission': {'id': 'TEST-' + code, 'codes': [code], 'branch': branch, 'actor': 'Codex', 'state': 'active', 'generation': 1, 'base_sha': self.config['base_sha'], 'paths': ['chapters/' + code]}, 'registry_sha': 'b' * 40, 'identity': 'declarative, not authenticated'})
        return worktree, receipt

    def claim(self):
        worktree, receipt = self.worktree_and_receipt()
        self.h.claim('neuro', 'G02', worktree, receipt)
        return worktree, receipt

    def state(self):
        return mh.load(self.h.runtime / 'state.json')

    def test_gate_healthy_is_permission_to_work_not_clinical_approval(self):
        gate = self.h.readiness()
        self.assertTrue(gate['allowed'], gate['problems'])
        self.assertIn('jamais', gate['scope'])

    def test_deadline_report_is_frozen_once_while_live_report_advances(self):
        self.h.config['deadline']='2020-01-01T08:00:00+01:00'
        self.h.report()
        frozen=self.home/'rapport-08h00.html'
        original=frozen.read_bytes()
        self.assertIn(b'report_frozen_at',original)
        state={'agents':{},'events':[],'cache':{},'completed_lessons':[{'code':'G02','test_marker':'later-completion'}]}
        mh.atomic(self.h.runtime/'state.json',state)
        self.h.report()
        self.assertEqual(frozen.read_bytes(),original)
        self.assertIn('later-completion',(self.home/'status.json').read_text())

    def test_missing_or_failed_tests_close_gate(self):
        for receipt in ({}, {'ok': False, 'code_sha256': mh.code_hash()}):
            with self.subTest(receipt=receipt):
                mh.atomic(self.h.runtime / 'tests.json', receipt)
                self.assertFalse(self.h.readiness()['allowed'])

    def test_code_change_invalidates_test_receipt(self):
        with mock.patch.object(mh, 'code_hash', return_value='c' * 64):
            self.assertFalse(self.h.readiness()['allowed'])

    def test_test_source_change_changes_harness_hash(self):
        # Tests themselves are part of the evidence, not an unversioned exemption.
        source = self.root / 'hash-fixture'
        (source / 'tests').mkdir(parents=True)
        (source / 'main.py').write_text('x = 1\n')
        test = source / 'tests' / 'test_contract.py'
        test.write_text('assert True\n')
        with mock.patch.object(mh, 'HERE', source):
            before = mh.code_hash()
            test.write_text('assert False\n')
            self.assertNotEqual(before, mh.code_hash())

    def test_stale_future_or_failed_watch_closes_gate(self):
        for seconds, ok in ((-901, True), (60, True), (0, False)):
            with self.subTest(seconds=seconds, ok=ok):
                observed = (dt.datetime.now(dt.timezone.utc) + dt.timedelta(seconds=seconds)).isoformat()
                mh.atomic(self.h.runtime / 'watch.json', {'ok': ok, 'observed_at': observed})
                self.assertFalse(self.h.readiness()['allowed'])

    def test_changed_prompt_and_duplicate_specialties_close_gate(self):
        self.prompt.write_text('Changed after lock.\n')
        self.assertFalse(self.h.readiness()['allowed'])
        self.healthy()
        self.h.config['agents'][1]['specialty'] = 'neurologie'
        self.assertTrue(any('affectations' in x for x in self.h.readiness()['problems']))

    def test_real_start_shape_without_ok_is_accepted(self):
        worktree, receipt = self.worktree_and_receipt()
        self.assertNotIn('ok', mh.load(receipt))
        self.assertEqual(self.h.claim('neuro', 'G02', worktree, receipt)['claimed'], 'G02')

    def test_boolean_receipt_wrong_code_and_wrong_branch_are_rejected(self):
        worktree, receipt = self.worktree_and_receipt()
        original = mh.load(receipt)
        invalid = [
            {'ok': True, 'mission': original['mission']},
            {**original, 'mission': {**original['mission'], 'codes': ['G05']}},
            {**original, 'mission': {**original['mission'], 'branch': 'codex/someone-else'}},
        ]
        for value in invalid:
            with self.subTest(receipt=value):
                mh.atomic(receipt, value)
                with self.assertRaises(ValueError):
                    self.h.claim('neuro', 'G02', worktree, receipt)

    def test_one_active_lesson_per_agent(self):
        self.claim()
        worktree, receipt = self.worktree_and_receipt('G05')
        with self.assertRaisesRegex(ValueError, 'Une seule leçon'):
            self.h.claim('neuro', 'G05', worktree, receipt)
        self.assertEqual(self.state()['agents']['neuro']['lesson'], 'G02')

    def test_same_lesson_cannot_be_claimed_by_second_agent(self):
        self.claim()
        self.h.config['agents'][1]['queue'].append('G02')
        worktree, receipt = self.worktree_and_receipt('G02', 'second')
        with self.assertRaisesRegex(ValueError, 'Leçon déjà réservée'):
            self.h.claim('endo', 'G02', worktree, receipt)

    def test_worktree_cannot_be_shared_between_lessons(self):
        worktree, receipt = self.claim()
        proof = mh.load(receipt)
        proof['mission']['codes'] = ['E00']
        second_receipt = self.root / 'e00-start.json'
        mh.atomic(second_receipt, proof)
        with self.assertRaisesRegex(ValueError, 'Worktree déjà affecté'):
            self.h.claim('endo', 'E00', worktree, second_receipt)

    def test_progress_cannot_start_without_claim_or_close_lesson(self):
        with self.assertRaises(ValueError):
            self.h.progress('neuro', 'redaction', 'Test-only progress')
        self.claim()
        with self.assertRaises(ValueError):
            self.h.progress('neuro', 'termine', 'Cannot certify by progress')

    def bound_package(self):
        worktree,_=self.claim();folder=worktree/'reports';folder.mkdir()
        paths=[f'chapters/G02/G02_{x}.html' for x in ('a','b','c','d','pop1','pop2')]+['glossary/g02.py']
        for name in paths:
            p=worktree/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text('Synthetic test fixture')
        (folder/'preview.html').write_text('Synthetic rendered fixture')
        binding={'code':'G02','verified_at':mh.now(),'checks':['synthetic fixture'],'preview':'preview.html',
                 'preview_sha256':mh.digest((folder/'preview.html').read_bytes()),
                 'final_sources':{name:mh.digest((worktree/name).read_bytes()) for name in paths}}
        mh.atomic(folder/'source-binding.json',binding)
        mh.atomic(folder/'lesson-manifest.json',{'code':'G02','matrix20':[{'point':n,'status':'covered','evidence':'synthetic fixture'} for n in range(1,21)]})
        return worktree,folder

    def test_bound_source_and_preview_changes_invalidate_verification(self):
        worktree,folder=self.bound_package()
        self.assertEqual(mh.verify_binding(worktree,'G02',folder)['code'],'G02')
        (folder/'preview.html').write_text('Changed rendering')
        with self.assertRaisesRegex(ValueError,'Aperçu modifié'):mh.verify_binding(worktree,'G02',folder)
        (worktree/'chapters/G02/G02_a.html').write_text('Changed dose in synthetic fixture')
        with self.assertRaisesRegex(ValueError,'Source modifiée'):mh.verify_binding(worktree,'G02',folder)

    def test_binding_cannot_omit_a_source_or_escape_the_lesson(self):
        worktree,folder=self.bound_package();p=folder/'source-binding.json';binding=mh.load(p)
        del binding['final_sources']['glossary/g02.py'];mh.atomic(p,binding)
        with self.assertRaisesRegex(ValueError,'sept sources'):mh.verify_binding(worktree,'G02',folder)
        binding['final_sources']['glossary/g02.py']=mh.digest((worktree/'glossary/g02.py').read_bytes())
        binding['final_sources']['../outside']='a'*64;mh.atomic(p,binding)
        with self.assertRaisesRegex(ValueError,'hors leçon'):mh.verify_binding(worktree,'G02',folder)

    def test_completion_requires_twenty_covered_points_and_records_history(self):
        worktree,folder=self.bound_package();p=folder/'lesson-manifest.json';manifest=mh.load(p)
        proof={'technical_contract_pass':True,'errors':[],'review_modes':{'medical':'self_review'}}
        with mock.patch.object(mh,'validate_lesson',return_value=proof):
            manifest['matrix20'][0]['status']='LACUNE';mh.atomic(p,manifest)
            with self.assertRaisesRegex(ValueError,'Matrice20'):self.h.complete('neuro',folder)
            manifest['matrix20'][0]['status']='covered';mh.atomic(p,manifest)
            result=self.h.complete('neuro',folder)
            self.assertFalse(result['clinical_certification']);self.assertFalse(result['publication_allowed'])
            self.assertEqual(self.state()['agents']['neuro']['stage'],'termine')
            self.assertEqual(len(self.state()['completed_lessons']),1)
            with self.assertRaisesRegex(ValueError,'déjà enregistré'):self.h.complete('neuro',folder)
            next_worktree,receipt=self.worktree_and_receipt('G05')
            self.h.claim('neuro','G05',next_worktree,receipt)
            self.assertEqual(len(self.state()['completed_lessons']),1)

    def test_completion_cannot_ignore_failed_contract(self):
        _,folder=self.bound_package()
        with mock.patch.object(mh,'validate_lesson',return_value={'technical_contract_pass':False,'errors':['Images non vérifiées']}):
            with self.assertRaisesRegex(ValueError,'Images'):self.h.complete('neuro',folder)
        self.assertNotEqual(self.state()['agents']['neuro']['stage'],'termine')

    def test_stale_watch_prevents_transition_to_writing(self):
        self.claim()
        old = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(minutes=16)).isoformat()
        mh.atomic(self.h.runtime / 'watch.json', {'ok': True, 'observed_at': old})
        with self.assertRaises(ValueError):
            self.h.progress('neuro', 'redaction', 'Should be blocked')
        self.assertEqual(self.state()['agents']['neuro']['stage'], 'recherche')

    def test_usage_remains_unknown_after_progress_and_cache_activity(self):
        self.claim()
        self.h.progress('neuro', 'recherche', 'Synthetic progress', completed_sections=2)
        self.h.extract('PROMPT.md', 1, 1)
        a = self.state()['agents']['neuro']
        for field in ('tokens_input', 'tokens_output', 'cost_usd', 'medical_score'):
            self.assertIsNone(a[field], field)
        self.assertIn('non exposé', a['usage_source'])

    def test_watch_does_not_refresh_authors_heartbeat(self):
        self.claim()
        old = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(minutes=25)).isoformat()
        with self.h.transaction() as state:
            state['agents']['neuro']['activity_at'] = old
        with mock.patch.object(self.h, 'report'):
            report = self.h.watch()
        self.assertFalse(report['agent_activity_refreshed'])
        self.assertEqual(self.state()['agents']['neuro']['activity_at'], old)
        self.assertTrue(any(x['agent'] == 'neuro' for x in report['findings']))

    def test_cache_exact_content_and_range_then_invalidated_by_change(self):
        path = self.root / 'source.txt'
        path.write_text('first\nsecond\nthird\n')
        first = self.h.extract('source.txt', 1, 2)
        hit = self.h.extract('source.txt', 1, 2)
        other_range = self.h.extract('source.txt', 2, 3)
        self.assertFalse(first['cache_hit'])
        self.assertTrue(hit['cache_hit'])
        self.assertNotIn('excerpt', hit)
        self.assertFalse(other_range['cache_hit'])
        path.write_text('changed\nsecond\nthird\n')
        changed = self.h.extract('source.txt', 1, 2)
        self.assertFalse(changed['cache_hit'])
        self.assertNotEqual(first['sha256'], changed['sha256'])
        self.assertEqual(changed['excerpt'], 'changed\nsecond')
        repeated = self.h.extract('source.txt', 1, 2, repeat=True)
        self.assertEqual(repeated['excerpt'], changed['excerpt'])
        self.assertIn('ne constitue pas', repeated['savings_kind'])

    def test_bounded_reads_and_path_escape_rejected(self):
        with self.assertRaises(ValueError):
            self.h.extract('PROMPT.md', 1, 201)
        (self.root / 'long.txt').write_text('x' * 24001)
        with self.assertRaises(ValueError):
            self.h.extract('long.txt', 1, 1)
        outside = Path(self.tmp.name) / 'outside.txt'
        outside.write_text('outside')
        (self.root / 'escape.txt').symlink_to(outside)
        for path in ('../outside.txt', str(outside), 'escape.txt'):
            with self.subTest(path=path), self.assertRaises(ValueError):
                self.h.extract(path, 1, 1)


class LessonContractCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.folder = Path(self.tmp.name)
        anchors = [f'point-{i}' for i in range(1, 15)]
        semio = [f'semio-{i}' for i in range(1, 10)]
        (self.folder / 'lesson.html').write_text('\n'.join(f'<section id="{a}">Synthetic test fixture; no medical claim.</section>' for a in anchors + semio))
        image = self.folder / 'figure.fixture'
        image.write_bytes(b'Synthetic bytes; deliberately no anatomical image.')
        review = self.folder / 'review.json'
        mh.atomic(review, {'scope': 'Synthetic structural fixture; not a clinical review'})
        self.manifest = {
            'author': 'test-author',
            'sources': [{'id': 'S1', 'url': 'https://example.invalid/source', 'publisher': 'Test only', 'read_at': mh.now(), 'section': 'Test section', 'passage': 'Synthetic test passage; no medical advice.', 'population': 'No real population', 'limits': 'No clinical validity'}],
            'monograph': [{'point': i, 'anchor': f'point-{i}', 'sources': ['S1'], 'coverage_explanation': 'Synthetic fixture checks field presence only; this statement is not a clinical coverage or validation claim.'} for i in range(1, 15)],
            'images': [{'path': image.name, 'sha256': mh.digest(image.read_bytes()), 'original_url': 'https://example.invalid/image', 'license': 'TEST-ONLY', 'author': 'Test fixture', 'annotations': 'Synthetic test label', 'medical_review': 'Not clinically reviewed: structural fixture'}],
            'semiology': {'section_anchors': semio}, 'blocking_findings': 0,
            'reviews': {kind: {'path': review.name, 'sha256': mh.digest(review.read_bytes()), 'reviewer': 'test-reviewer'} for kind in ('medical', 'language', 'visual_desktop', 'visual_mobile')},
        }

    def validate(self):
        mh.atomic(self.folder / 'lesson-manifest.json', self.manifest)
        return mh.validate_lesson(self.folder)

    def test_structurally_complete_fixture_never_certifies_medicine_or_publication(self):
        result = self.validate()
        self.assertTrue(result['technical_contract_pass'], result['errors'])
        self.assertFalse(result['clinical_certification'])
        self.assertFalse(result['publication_allowed'])

    def test_missing_monograph_cannot_pass_or_be_certified(self):
        self.manifest['monograph'] = []
        result = self.validate()
        self.assertFalse(result['technical_contract_pass'])
        self.assertEqual(sum('Point monographique' in x for x in result['errors']), 14)
        self.assertFalse(result['clinical_certification'])

    def test_duplicate_point_missing_anchor_unknown_source_and_missing_passage_rejected(self):
        self.manifest['monograph'][0]['anchor'] = 'missing-anchor'
        self.manifest['monograph'][1]['sources'] = ['UNKNOWN']
        self.manifest['monograph'].append(copy.deepcopy(self.manifest['monograph'][2]))
        del self.manifest['sources'][0]['passage']
        result = self.validate()
        self.assertFalse(result['technical_contract_pass'])
        for fragment in ('Ancre', 'Preuves', 'dupliqué', 'Métadonnées'):
            self.assertTrue(any(fragment in e for e in result['errors']), fragment)

    def test_changed_figure_or_review_invalidates_evidence(self):
        (self.folder / 'figure.fixture').write_bytes(b'Changed figure')
        (self.folder / 'review.json').write_text('{"changed":true}')
        result = self.validate()
        self.assertFalse(result['technical_contract_pass'])
        self.assertTrue(any('Figure' in e for e in result['errors']))
        self.assertTrue(any('revue absente' in e for e in result['errors']))

    def test_author_review_and_blocking_findings_do_not_pass(self):
        self.manifest['reviews']['medical']['reviewer'] = 'test-author'
        self.manifest['blocking_findings'] = 1
        result = self.validate()
        self.assertFalse(result['technical_contract_pass'])
        self.assertTrue(any('Revue distincte' in e for e in result['errors']))
        self.assertTrue(any('Réserves' in e for e in result['errors']))

    def test_explicit_self_review_is_honest_and_never_an_independent_certification(self):
        for review in self.manifest['reviews'].values():
            review['reviewer']='test-author';review['mode']='self_review'
        result=self.validate()
        self.assertTrue(result['technical_contract_pass'],result['errors'])
        self.assertFalse(result['clinical_certification'])
        self.assertFalse(result['publication_allowed'])
        self.assertEqual(set(result['review_modes'].values()),{'self_review'})

    def test_unknown_review_mode_cannot_bypass_identity_check(self):
        self.manifest['reviews']['medical']['mode']='approved_by_magic'
        self.assertFalse(self.validate()['technical_contract_pass'])

    def test_semiology_boolean_or_unresolved_sections_rejected(self):
        for semio in (True, {'section_anchors': ['missing'] * 9}):
            with self.subTest(semio=semio):
                self.manifest['semiology'] = semio
                self.assertFalse(self.validate()['technical_contract_pass'])

    def test_nine_repeated_anchors_are_not_nine_sections(self):
        self.manifest['semiology'] = {'section_anchors': ['semio-1'] * 9}
        self.assertFalse(self.validate()['technical_contract_pass'])

    def test_reviewer_identity_cannot_be_missing(self):
        del self.manifest['reviews']['medical']['reviewer']
        self.assertFalse(self.validate()['technical_contract_pass'])

    def test_review_traversal_is_rejected(self):
        self.manifest['reviews']['medical']['path'] = '../outside-review.json'
        with self.assertRaises(ValueError):
            self.validate()


if __name__ == '__main__':
    unittest.main()
