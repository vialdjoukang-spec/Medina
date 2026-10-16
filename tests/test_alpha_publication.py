"""Real-Git adversarial checks for scoped Alpha publication successors."""
import copy
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from tools import espace as E
from tools import publication_en_etat as P
try:
    from tools import alpha_publication as A
except ImportError:
    import alpha_publication as A


class AlphaTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.git('init', '-q')
        # Aucun gc ni maintenance en arrière-plan : ils écrivent dans .git/objects pendant le nettoyage du dossier.
        self.git('config', 'gc.auto', '0')
        self.git('config', 'maintenance.auto', 'false')
        self.git('config', 'user.name', 'Technical fixture')
        self.git('config', 'user.email', 'test@example.invalid')
        self.code, self.actor = 'E11', 'Claude'
        self.mid = 'ALPHA77-CLAUDE-E11-INTEGRATE'
        self.output = 'docs/collaboration/ssp-v2/execution/' + self.mid
        self.receipt_path = A.PREFIX + 'Claude/E11/0001.json'
        self.old = {p: ('<p>Réserves médicales en cours.</p><img src="old.png" alt="Attribution fixture"><figcaption>Attribution fixture</figcaption>' if p.endswith('.html') else '# fixture').encode()
                    for p in A.core_paths(self.code)}
        for path, raw in self.old.items():
            self.write(path, raw)
            self.write('delivery/' + path, raw)
        self.json('chapters.json', [dict(code='E11', integrated=True, provisional_injection=True,
                                       publication_mode='en_etat', audit_deferred='non_realise')])
        self.json('nosology/fragments/S05.json', {'lessons': [{'code': 'E11'}]})
        self.write(P.AUTHORITY, (Path(E.__file__).resolve().parents[1] / P.AUTHORITY).read_bytes())
        provenance = self.commit()
        self.json(P.RECEIPT, dict(schema_version=1, actor='Claude', authority=P.AUTHORITY,
            authority_sha256=A.digest((self.root / P.AUTHORITY).read_bytes()), medical_human_validation=False,
            catalog_sha256=A.digest((self.root / 'chapters.json').read_bytes()),
            catalog_entries=json.loads((self.root / 'chapters.json').read_bytes()),
            courses=[dict(code='E11', fragment_id='S05', files={p: dict(sha256=A.digest(raw),
                provenance_revision=provenance, provenance_path='delivery/' + p) for p, raw in self.old.items()})]))
        self.anchor = self.commit()
        self.patch_anchor = patch.object(A, 'HISTORICAL_ANCHOR', self.anchor)
        self.patch_anchor.start()
        self.addCleanup(self.patch_anchor.stop)
        self.json(A.PLAN, dict(audit=[dict(code='E11', owner='Claude', fragment='S05')], production=[]))
        self.json(A.TOUR, dict(selected={'Claude': ['E11'], 'Codex': ['E10']}, missions=[dict(actor='Claude',
            codes=['E11'], audit_type='medical', source_files_sha256={p: A.digest(v) for p, v in self.old.items()})]))
        self.json('.medina/ai-session-guard.json', dict(schema_version=1, enabled=True,
            registry_ref='refs/heads/medina/session-registry', code_systems={'E11': 'S05', 'E10': 'S05'},
            shared_paths=['chapters.json', A.PREFIX.rstrip('/')]))
        self.mission = dict(schema_version=1, id=self.mid, state='active', actor='Claude', owner='Claude',
            conversation='fixture', assigned_by='Vial fixture', branch='claude/fixture', role='integrator',
            generation=1, base_sha=self.anchor, codes=['E11'], alpha_publication=True,
            paths=['chapters/E11', 'glossary/e11.py', 'assets/img/e11/alpha/claude', self.output,
                   A.PREFIX + 'Claude/E11'])
        self.json('.medina/missions/' + self.mid + '.json', self.mission)
        self.base = self.commit()
        self.new = {p: raw.replace('médicales'.encode(), 'médicales documentées'.encode()) for p, raw in self.old.items()}
        self.receipt = dict(schema_version=1, actor='Claude', code='E11', fragment='S05',
            phase='completed', medical_human_validation=False, base_commit=self.base,
            mission=self.mid, previous_receipt_sha256=None, files={})
        self.prepare_source()

    def git(self, *args):
        return subprocess.check_output(['git', *args], cwd=self.root, stderr=subprocess.DEVNULL).decode().strip()

    def write(self, path, raw):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)

    def json(self, path, value):
        self.write(path, json.dumps(value, ensure_ascii=False).encode())

    def commit(self):
        self.git('add', '.')
        self.git('commit', '--allow-empty', '-qm', 'Technical fixture')
        return self.git('rev-parse', 'HEAD')

    def prepare_source(self, report_status='closed', blockers=None):
        for target, raw in self.new.items():
            source = self.output + '/final/' + target
            self.write(source, raw)
            self.receipt['files'][target] = dict(previous_sha256=A.digest(self.old[target]),
                                                 sha256=A.digest(raw), source_path=source)
        self.receipt['audits'] = {}
        for kind in ('MED', 'LANG', 'SEMIO'):
            report = dict(actor='Claude', code='E11', kind=kind, status=report_status,
                medical_human_validation=False, source_files_sha256={p: A.digest(v) for p, v in self.old.items()},
                reviewed_files_sha256={p: A.digest(v) for p, v in self.new.items()},
                unresolved_blockers=blockers or [], findings=[], evidence=['Fixture review artifact, no human claim'])
            if kind == 'SEMIO':
                report['requirement'] = 'fundamental_analytical_semiology'
            path = self.output + '/' + kind + '.json'
            self.json(path, report)
            self.receipt['audits'][kind] = dict(path=path, sha256=A.digest((self.root / path).read_bytes()))
        self.receipt['source_commit'] = self.commit()

    def publish(self):
        for target, raw in self.new.items():
            self.write(target, raw)
        self.json(self.receipt_path, self.receipt)
        return E.GitTree(self.root, self.commit())

    def test_valid_completed_preserves_historical_receipt_and_originals(self):
        after = self.publish()
        projected, metadata = A.verify(after, E.GitTree(self.root, self.base))
        self.assertEqual(metadata['E11']['phase'], 'completed')
        for path, raw in self.old.items():
            self.assertEqual(projected.read(path), raw)
        self.assertTrue(P.validate(projected, projected, {P.RECEIPT}, adopted=True))

    def test_untouched_old_publication_stays_valid(self):
        tree = E.GitTree(self.root, self.base)
        projected, metadata = A.verify(tree)
        self.assertEqual(metadata, {})
        self.assertTrue(P.validate(projected, projected, {P.RECEIPT}, adopted=True))

    def historical_memory_tree(self):
        from tools import betta_injecter as injector
        files = {path: (self.root / path).read_bytes()
                 for path in E.GitTree(self.root, 'HEAD').entries}
        with patch.object(injector, 'ROOT', self.root):
            return injector._Tree(files)

    def test_historical_memory_transaction_needs_no_alpha_projection(self):
        tree = self.historical_memory_tree()
        self.assertFalse(hasattr(tree, 'revision'))
        projected, receipts = A.verify(tree)
        self.assertIs(projected, tree)
        self.assertEqual(receipts, {})
        self.assertEqual(P.adopted_codes(tree), {'E11'})

    def test_historical_memory_transaction_still_rechecks_real_provenance(self):
        tree = self.historical_memory_tree()
        path = 'chapters/E11/E11_a.html'
        tree.files[path] = b'Unreviewed mutation'
        with self.assertRaisesRegex(P.PublicationError, 'différente du reçu'):
            P.adopted_codes(tree)

    def test_alpha_receipts_cannot_be_verified_as_memory_only_transactions(self):
        self.publish()
        tree = self.historical_memory_tree()
        with self.assertRaisesRegex(A.AlphaError, 'arbre Git immuable'):
            P.adopted_codes(tree)

    def test_forged_new_hash_rejected(self):
        self.new[next(iter(self.new))] = b'Unreviewed alteration'
        with self.assertRaisesRegex(A.AlphaError, 'source finale'):
            A.verify(self.publish(), E.GitTree(self.root, self.base))

    def test_actor_cannot_take_other_course(self):
        self.receipt['actor'] = 'Codex'
        with self.assertRaisesRegex(A.AlphaError, 'identité'):
            A.verify(self.publish())

    def test_missing_audit_rejected(self):
        del self.receipt['audits']['LANG']
        with self.assertRaisesRegex(A.AlphaError, 'rapport hors mission'):
            A.verify(self.publish())

    def test_completed_requires_semio_proof(self):
        del self.receipt['audits']['SEMIO']
        with self.assertRaisesRegex(A.AlphaError, 'rapport hors mission'):
            A.verify(self.publish())

    def test_human_claim_rejected(self):
        self.receipt['medical_human_validation'] = True
        with self.assertRaisesRegex(A.AlphaError, 'validation humaine'):
            A.verify(self.publish())

    def test_wrong_previous_hash_rejected(self):
        self.receipt['files'][next(iter(self.old))]['previous_sha256'] = 'f' * 64
        with self.assertRaisesRegex(A.AlphaError, 'ancienne empreinte'):
            A.verify(self.publish())

    def test_source_commit_must_exist(self):
        self.receipt['source_commit'] = 'f' * 40
        with self.assertRaisesRegex(A.AlphaError, 'ascendance'):
            A.verify(self.publish())

    def test_approval_must_preexist_trusted_base(self):
        with self.assertRaisesRegex(A.AlphaError, 'ascendance'):
            A.verify(self.publish(), E.GitTree(self.root, self.anchor))

    def test_old_receipt_cannot_be_rewritten(self):
        self.publish()
        before = E.GitTree(self.root, 'HEAD')
        self.receipt['extra'] = 'rewrite'
        with self.assertRaisesRegex(A.AlphaError, 'historique réécrit'):
            A.verify(self.publish(), before)

    def test_second_receipt_is_hash_linked_to_first_and_original_remains_valid(self):
        first = self.publish()
        previous_hash = A.digest(first.read(self.receipt_path))
        self.old = dict(self.new)
        self.new = {p: raw.replace('documentées'.encode(), 'documentées et relues'.encode()) for p, raw in self.old.items()}
        self.receipt = copy.deepcopy(self.receipt)
        self.receipt.update(base_commit=first.revision, previous_receipt_sha256=previous_hash)
        self.receipt_path = A.PREFIX + 'Claude/E11/0002.json'
        self.prepare_source()
        second = self.publish()
        projected, metadata = A.verify(second, first)
        self.assertEqual(metadata['E11']['receipt'], self.receipt_path)
        self.assertTrue(P.validate(projected, projected, {P.RECEIPT}, adopted=True))

    def test_wrong_previous_receipt_hash_rejected(self):
        self.receipt['previous_receipt_sha256'] = 'f' * 64
        with self.assertRaisesRegex(A.AlphaError, 'reçu précédent'):
            A.verify(self.publish())

    def test_old_receipt_cannot_be_deleted(self):
        self.publish()
        before = E.GitTree(self.root, 'HEAD')
        (self.root / self.receipt_path).unlink()
        after = E.GitTree(self.root, self.commit())
        with self.assertRaisesRegex(A.AlphaError, 'suppression'):
            A.views(before, after)

    def test_independent_publication_does_not_rewrite_catalog(self):
        self.json('chapters.json', [])
        with self.assertRaisesRegex(A.AlphaError, 'catalogue'):
            A.views(E.GitTree(self.root, self.base), self.publish())

    def test_provisional_with_blockers_is_not_completed(self):
        self.receipt['phase'] = 'provisional'
        self.receipt['visible_reservations'] = ['Réserves médicales documentées en cours.']
        self.prepare_source(report_status='provisional', blockers=['Réserves médicales documentées en cours.'])
        del self.receipt['audits']['SEMIO']
        _, metadata = A.verify(self.publish())
        self.assertEqual(metadata['E11']['phase'], 'provisional')

    def test_completed_cannot_have_blockers(self):
        self.prepare_source(blockers=['Unresolved clinical issue'])
        with self.assertRaisesRegex(A.AlphaError, 'audit non clos'):
            A.verify(self.publish())

    def test_figures_only_cannot_rewrite_medical_text(self):
        self.receipt['phase'] = 'figures_only'
        self.receipt['visible_reservations'] = ['Réserves médicales documentées en cours.']
        with self.assertRaisesRegex(A.AlphaError, 'figure_only'):
            A.verify(self.publish())

    def publish_figure(self):
        self.new = dict(self.old)
        target = 'chapters/E11/E11_a.html'
        asset = 'assets/img/e11/alpha/claude/figure.png'
        old_tag = '<img src="old.png" alt="Attribution fixture">'
        new_tag = '<img src="' + asset + '" alt="Attribution fixture">'
        self.new[target] = self.old[target].replace(old_tag.encode(), new_tag.encode())
        self.receipt.update(phase='figures_only', visible_reservations=['Réserves médicales en cours.'])
        self.prepare_source()
        self.receipt['files'][target]['figure_replacements'] = [dict(old=old_tag, new=new_tag)]
        raw = b'PNG technical fixture'
        source_path = self.output + '/final/' + asset
        self.write(source_path, raw)
        visual_path = self.output + '/visual.json'
        self.json(visual_path, dict(actor='Claude', code='E11', asset_sha256=A.digest(raw),
            status='reviewed', medical_human_validation=False, anatomy_ai_generated=False,
            license_verified=True, medical_observations='Technical fixture review'))
        figure = dict(original_url='https://example.invalid/original.png', source_url='https://example.invalid/source',
            license='CC-BY-4.0 fixture', attribution='Attribution fixture', ai_generated=False,
            visual_review_report=visual_path, visual_review_sha256=A.digest((self.root / visual_path).read_bytes()))
        figure.update(license_url='https://example.invalid/license', original_sha256=A.digest(raw))
        rights = dict(schema_version=1, actor='Claude', code='E11', original_sha256=A.digest(raw),
            transformed=False, ai_generated=False, license_verified=True, author='Fixture author', credit='Attribution fixture',
            retrieved_at='2026-10-15T12:00:00+00:00', license_quote='Fixture CC-BY-4.0 licence statement',
            **{key: figure[key] for key in ('original_url', 'source_url', 'license_url')})
        for key, content in [('source_page', 'Fixture author; Attribution fixture'),
                             ('license_page', 'Fixture CC-BY-4.0 licence statement')]:
            page_path = self.output + '/' + key + '.html'
            self.write(page_path, content.encode())
            rights[key] = dict(path=page_path, sha256=A.digest(content.encode()))
        rights_path = self.output + '/rights.json'
        self.json(rights_path, rights)
        figure['rights_evidence'] = dict(path=rights_path, sha256=A.digest((self.root / rights_path).read_bytes()))
        self.receipt['files'][asset] = dict(previous_sha256=None, sha256=A.digest(raw), source_path=source_path, figure=figure)
        self.receipt['source_commit'] = self.commit()
        self.write(asset, raw)
        self.receipt.pop('audits')
        before = E.GitTree(self.root, self.base)
        after = self.publish()
        return before, after

    def test_verified_figure_can_publish_without_closing_medical_audit(self):
        before, after = self.publish_figure()
        target = 'chapters/E11/E11_a.html'
        asset = 'assets/img/e11/alpha/claude/figure.png'
        historical_before, historical_after, metadata = A.views(before, after)
        self.assertEqual(metadata['E11']['phase'], 'figures_only')
        self.assertEqual(historical_before.read(target), historical_after.read(target))
        self.assertIsNone(historical_after.read(asset, required=False))
        self.assertTrue(P.validate(historical_after, historical_after, {P.RECEIPT}, adopted=True))

    def test_figure_url_credentials_and_non_https_rejected(self):
        for url in ('http://example.invalid/image.png', 'https://user:secret@example.invalid/image.png',
                    'javascript:alert(1)', 'https://example.invalid/a b', 'https://[broken'):
            with self.subTest(url=url):
                self.assertFalse(A.https_url(url))
        self.assertTrue(A.https_url('https://example.invalid/original.png'))

    def alter_rights(self, key, value):
        self.publish_figure()
        figure = self.receipt['files']['assets/img/e11/alpha/claude/figure.png']['figure']
        proof = figure['rights_evidence']
        report = json.loads((self.root / proof['path']).read_bytes())
        report[key] = value
        self.json(proof['path'], report)
        proof['sha256'] = A.digest((self.root / proof['path']).read_bytes())
        self.receipt['source_commit'] = self.commit()

    def test_transformed_figure_cannot_claim_original_bytes(self):
        self.alter_rights('transformed', True)
        with self.assertRaisesRegex(A.AlphaError, 'octets originaux'):
            A.verify(self.publish())

    def test_licence_quote_must_exist_in_retained_page(self):
        self.alter_rights('license_quote', 'Invented licence permission')
        with self.assertRaisesRegex(A.AlphaError, 'licence absent'):
            A.verify(self.publish())

    def test_original_image_hash_cannot_be_declared_arbitrarily(self):
        self.publish_figure()
        self.receipt['files']['assets/img/e11/alpha/claude/figure.png']['figure']['original_sha256'] = 'f' * 64
        with self.assertRaisesRegex(A.AlphaError, 'octets originaux'):
            A.verify(self.publish())

    def new_course(self):
        code = 'E10'
        mid = 'ALPHA77-CODEX-E10-INTEGRATE'
        output = 'docs/collaboration/ssp-v2/execution/' + mid
        self.json('nosology/fragments/S05.json', {'lessons': [{'code': 'E11'}, {'code': 'E10'}]})
        plan = json.loads((self.root / A.PLAN).read_bytes())
        plan['production'] = [dict(code=code, owner='Codex', fragment='S05')]
        self.json(A.PLAN, plan)
        mission = copy.deepcopy(self.mission)
        mission.update(id=mid, actor='Codex', owner='Codex', conversation='new-fixture', branch='codex/new-fixture',
                       codes=[code], allow_new_course=True, paths=['chapters/E10', 'glossary/e10.py', output,
                       'chapters.json', A.PREFIX + 'Codex/E10'])
        self.json('.medina/missions/' + mid + '.json', mission)
        base = self.commit()
        files = {}
        for path in A.core_paths(code):
            source_path = output + '/final/' + path
            self.write(source_path, b'New technical course fixture')
            files[path] = dict(previous_sha256=None, sha256=A.digest(b'New technical course fixture'), source_path=source_path)
        audits = {}
        for kind in ('MED', 'LANG', 'SEMIO'):
            path = output + '/' + kind + '.json'
            self.json(path, dict(actor='Codex', code=code, kind=kind, status='closed', medical_human_validation=False,
                requirement='fundamental_analytical_semiology' if kind == 'SEMIO' else None,
                source_files_sha256={}, reviewed_files_sha256={p: ref['sha256'] for p, ref in files.items()},
                unresolved_blockers=[], findings=[], evidence=['Technical fixture evidence']))
            audits[kind] = dict(path=path, sha256=A.digest((self.root / path).read_bytes()))
        source = self.commit()
        catalog = json.loads((self.root / 'chapters.json').read_bytes())
        entry = dict(code=code, integrated=True, owner='S05', publication_mode='alpha', title='New fixture')
        self.json('chapters.json', catalog + [entry])
        for path, ref in files.items():
            self.write(path, (self.root / ref['source_path']).read_bytes())
        receipt_path = A.PREFIX + 'Codex/E10/0001.json'
        receipt = dict(schema_version=1, actor='Codex', code=code, fragment='S05', phase='completed',
            medical_human_validation=False, base_commit=base, source_commit=source, mission=mid,
            previous_receipt_sha256=None, files=files, audits=audits, catalog_entry=entry)
        self.json(receipt_path, receipt)
        return base, receipt_path, receipt

    def test_new_course_adds_only_own_catalog_row_and_preserves_old_receipt(self):
        base, _, _ = self.new_course()
        after = E.GitTree(self.root, self.commit())
        _, projected, metadata = A.views(E.GitTree(self.root, base), after)
        self.assertEqual(metadata['E10']['phase'], 'completed')
        self.assertIsNone(projected.read('chapters/E10/E10_a.html', required=False))
        self.assertEqual([r['code'] for r in json.loads(projected.read('chapters.json'))], ['E11'])
        self.assertTrue(P.validate(projected, projected, {P.RECEIPT}, adopted=True))

    def test_new_course_cannot_change_other_catalog_rows(self):
        base, _, _ = self.new_course()
        catalog = json.loads((self.root / 'chapters.json').read_bytes())
        catalog[0]['title'] = 'Unrelated rewrite'
        self.json('chapters.json', catalog)
        with self.assertRaisesRegex(A.AlphaError, 'catalogue.*extérieur'):
            A.views(E.GitTree(self.root, base), E.GitTree(self.root, self.commit()))

    def test_later_unrelated_catalog_addition_remains_visible_to_old_guards(self):
        _, _, _ = self.new_course()
        first = E.GitTree(self.root, self.commit())
        catalog = json.loads((self.root / 'chapters.json').read_bytes())
        catalog.append(dict(code='E12', title='Unrelated independent course', integrated=False))
        self.json('chapters.json', catalog)
        after = E.GitTree(self.root, self.commit())
        old_view, new_view, _ = A.views(first, after)
        self.assertIn('E12', [r['code'] for r in json.loads(new_view.read('chapters.json'))])
        self.assertNotIn('E10', [r['code'] for r in json.loads(new_view.read('chapters.json'))])
        self.assertNotEqual(old_view.entries['chapters.json'], new_view.entries['chapters.json'])
        self.assertTrue(P.validate(new_view, new_view, {P.RECEIPT}, adopted=True))




class ReachableCourseTests(unittest.TestCase):
    def read(self,body,code='N17'):
        return A.reachable_course_text(body.encode(),code)

    def wrap(self,body):return '<template id="ch-N17"><div class="chap">'+body+'</div></template>'

    def tabs(self,body,aria='pS',target='pS',button_attrs='',target_attrs='hidden'):
        return self.wrap(f'<div class="tabs"><button data-p="{target}" aria-controls="{aria}" {button_attrs}>Sciences</button></div><div class="panel" id="pA">Initial</div><div class="panel" id="pS" {target_attrs}>{body}</div>')

    def science(self,body,button_attrs='',target_attrs='hidden',aria=True):
        controls='aria-controls="n17-anat"' if aria else ''
        return self.tabs(f'<div class="sci-bar"><button data-s="n17-anat" {controls} {button_attrs}>Anatomie</button></div><div class="sci" id="n17-anat" {target_attrs}>{body}</div>')

    def test_real_course_template_reservation(self):
        raw=self.wrap('<p>Réserves encore ouvertes.</p>')
        self.assertIn('Réserves encore ouvertes.',self.read(raw))
        self.assertNotIn('Réserves',A.visible_text(raw.encode()))

    def test_real_navigation_reaches_hidden_science_and_credit(self):
        raw=self.science('<figure><figcaption>Crédit original vérifié</figcaption></figure>')
        self.assertIn('Crédit original vérifié',self.read(raw))
        self.assertNotIn('Crédit original vérifié',A.visible_text(raw.encode()))

    def test_legacy_runtime_button_without_aria_is_supported(self):
        self.assertIn('Crédit',self.read(self.science('<figcaption>Crédit</figcaption>',aria=False)))

    def test_mismatched_or_absent_primary_target_stays_hidden(self):
        for attrs in [dict(aria='foreign'),dict(target='missing')]:
            self.assertNotIn('Secret',self.read(self.tabs('<p>Secret</p>',**attrs)))

    def test_scientific_aria_mismatch_rejected(self):
        raw=self.science('<p>Secret</p>').replace('aria-controls="n17-anat"','aria-controls="other"')
        self.assertNotIn('Secret',self.read(raw))

    def test_duplicate_local_target_is_not_activated(self):
        body=self.science('<p>Secret</p>').replace('</div></template>','<div class="sci" id="n17-anat" hidden>Duplicate</div></div></template>')
        self.assertNotIn('Secret',self.read(body))

    def test_foreign_course_and_nested_templates_are_not_reachable(self):
        self.assertNotIn('Secret',self.read('<template id="ch-I63"><p>Secret</p></template>'))
        for tag in ['template','script','style']:
            self.assertNotIn('Secret',self.read(self.science(f'<{tag}>Secret</{tag}>')))

    def test_explicit_hiding_and_nested_hidden_remain_excluded(self):
        for attrs in ['hidden style="display:none"','hidden style="display: none !important"',
                      'hidden aria-hidden="true"','hidden style="visibility:hidden"']:
            self.assertNotIn('Secret',self.read(self.science('<p>Secret</p>',target_attrs=attrs)))
        for attrs in ['hidden','aria-hidden="true"','style="display:none"']:
            self.assertNotIn('Secret',self.read(self.science(f'<p {attrs}>Secret</p>')))

    def test_hidden_or_disabled_buttons_cannot_activate_targets(self):
        for attrs in ['hidden','disabled','aria-disabled="true"','style="display:none"','inert']:
            self.assertNotIn('Secret',self.read(self.science('<p>Secret</p>',button_attrs=attrs)))

    def test_uncontrolled_science_and_wrong_bar_are_not_activated(self):
        raw=self.science('<p>Secret</p>')
        for value in [raw.replace('class="sci-bar"','class="random"'),raw.replace('data-s="n17-anat"','data-x="n17-anat"')]:
            self.assertNotIn('Secret',self.read(value))

    def test_button_in_inert_template_cannot_activate_target(self):
        raw=self.science('<p>Secret</p>').replace('<div class="sci-bar">','<template><div class="sci-bar">').replace('Anatomie</button></div>','Anatomie</button></div></template>')
        self.assertNotIn('Secret',self.read(raw))

    def test_visible_outside_course_is_not_course_evidence(self):
        raw='<p>Secret</p>'+self.wrap('<p>Course</p>')
        self.assertNotIn('Secret',self.read(raw))
        self.assertIn('Course',self.read(raw))

    def test_plain_fixtures_preserve_existing_visibility_contract(self):
        raw=b'<p>Public</p><p hidden>Secret</p><template>Secret2</template><script>Secret3</script>'
        self.assertEqual('Public',A.visible_text(raw))
        self.assertEqual('Public',A.reachable_course_text(raw,'N17'))



    def test_missing_or_duplicate_course_root_cannot_use_outside_reserves(self):
        for raw in ['<p>Secret</p><template id="ch-I63">Foreign</template>',
                    '<p>Secret</p>'+self.wrap('One')+self.wrap('Two'),
                    '<p>Secret</p><template>'+self.wrap('Secret')+'</template>']:
            self.assertNotIn('Secret', self.read(raw))


    def test_embedded_styles_cannot_supply_computed_hidden_evidence(self):
        for raw in [self.wrap('<style>.secret{display:none}</style><p class="secret">Secret</p>'),
                    '<style>.secret{visibility:hidden}</style>'+self.wrap('<p class="secret">Secret</p>')]:
            self.assertNotIn('Secret', self.read(raw))

    def test_nested_peer_target_cannot_become_reachable(self):
        raw = self.wrap('<div class="tabs"><button data-p="pS">Science</button></div>'
                        '<div class="panel" id="pA"><div class="panel" id="pS" hidden>Secret</div></div>')
        self.assertNotIn('Secret', self.read(raw))
        raw = self.science('<div class="sci-bar"><button data-s="nested">Next</button></div>'
                           '<div class="sci" id="nested" hidden>Secret</div>')
        self.assertNotIn('Secret', self.read(raw))


    def test_untransformed_class_syntax_cannot_activate_hidden_target(self):
        raw = self.science('<p>Secret</p>')
        for old, new in [('class="tabs"', "class='tabs'"),
                         ('class="panel"', "class='panel'"),
                         ('class="sci-bar"', "class='sci-bar'"),
                         ('class="sci"', "class='sci'")]:
            self.assertNotIn('Secret', self.read(raw.replace(old, new)))

    def test_closed_dialog_and_explicit_invisible_styles_excluded(self):
        self.assertNotIn('Secret', self.read(self.wrap('<dialog>Secret</dialog>')))
        self.assertIn('Visible', self.read(self.wrap('<dialog open>Visible</dialog>')))
        for style in ['visibility:collapse', 'content-visibility:hidden', 'opacity:0',
                      'font-size:0px', 'color:transparent', 'display:/* hidden */none']:
            self.assertNotIn('Secret', self.read(self.science('<p>Secret</p>',
                                  target_attrs='hidden style="'+style+'"')))

    def test_active_stylesheet_link_cannot_prove_static_visibility(self):
        self.assertNotIn('Secret', self.read('<link rel="stylesheet" href="hide.css">'+self.wrap('Secret')))


if __name__ == "__main__":
    unittest.main()
