import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('audit_sciences', Path(__file__).with_name('audit_sciences.py'))
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)

CALLOUTS = ['Science → clinique.', 'Science → examen.', 'Science → traitement.', 'À retenir.']
SVG = '<svg role="img" aria-label="Relation causale non anatomique"></svg>'
IMG = '<img src="assets/original.png" alt="Figure originale documentée">'


def source(media=SVG, count=280, callouts=CALLOUTS):
    return ('<section id="pS"><button data-s="i63-s-normal">Science</button>'
            '<div class="sci" id="i63-s-normal"><p>' + ' '.join(['mécanisme'] * count) + '</p>'
            '<figure>' + media + '<figcaption>Légende et attribution.</figcaption></figure>' +
            ''.join('<p>' + label + '</p>' for label in callouts) + '</div></section>')


class ScienceAuditTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.git('init', '-q')
        self.git('config', 'user.name', 'Test')
        self.git('config', 'user.email', 'test@example.invalid')
        self.write('chapters.json', json.dumps([{'code': 'I63', 'integrated': True}]))

    def git(self, *args):
        return subprocess.check_output(['git', *args], cwd=self.root, text=True).strip()

    def write(self, path, value):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(value)

    def commit(self):
        self.git('add', '.')
        self.git('commit', '-qm', 'fixture')
        return self.git('rev-parse', 'HEAD')

    def run_audit(self, base):
        with patch.object(audit, 'ROOT', self.root), contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises(SystemExit) as result:
                audit.main(['--base', base, '--codes', 'I63', '--out', str(self.root / 'report.json')])
        return result.exception.code, json.loads((self.root / 'report.json').read_text())

    def test_exact_base_measures_actual_committed_source(self):
        self.write('chapters/I63/I63_c.html', source(count=300))
        base = self.commit()
        self.write('chapters/I63/I63_c.html', source(IMG, count=340))
        status, report = self.run_audit(base)
        self.assertFalse(status)
        self.assertEqual(report['base'], base)
        self.assertEqual(report['courses']['I63']['before']['words'], audit.words(audit.science(source(count=300))))
        self.assertGreater(report['totals']['after']['words'], report['totals']['before']['words'])

    def test_branch_abbreviation_nonexistent_commit_and_blob_rejected(self):
        base = self.commit()
        blob = self.git('rev-parse', base + ':chapters.json')
        for value in ['main', 'HEAD', base[:12], '0' * 40, blob]:
            with self.subTest(value=value), patch.object(audit, 'ROOT', self.root), contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit) as result:
                    audit.main(['--base', value])
                self.assertEqual(result.exception.code, 2)

    def test_missing_baseline_is_failure_even_for_former_exemption(self):
        base = self.commit()
        self.write('chapters/I63/I63_c.html', source())
        status, report = self.run_audit(base)
        self.assertTrue(status)
        self.assertIsNone(report['courses']['I63']['before'])
        self.assertFalse(report['courses']['I63']['baseline_present'])
        self.assertIn('preuve de production approuvée requise', report['errors'][0])

    def production(self):
        mission = 'I63-PRODUCE'
        self.write('.medina/7-starter-codex.json', json.dumps({'queue': [
            {'code': 'I63', 'mode': 'production', 'owner': 'Codex', 'missions': {'PRODUCE': mission},
             'production_receipt': 'proof/production.json'}]}))
        self.write('.medina/missions/' + mission + '.json', json.dumps(
            {'id': mission, 'state': 'active', 'role': 'integrator', 'codes': ['I63'], 'actor': 'Codex'}))
        base = self.commit()
        files = {}
        for part in ['a', 'b', 'c', 'd', 'pop1', 'pop2']:
            path = f'chapters/I63/I63_{part}.html'
            self.write(path, source() if part == 'c' else '<p>Fixture</p>')
            files[path] = hashlib.sha256((self.root / path).read_bytes()).hexdigest()
        self.write('glossary/i63.py', '# fixture')
        files['glossary/i63.py'] = hashlib.sha256((self.root / 'glossary/i63.py').read_bytes()).hexdigest()
        self.write('proof/production.json', json.dumps({'complete': True, 'mission': mission, 'final_files': files}))
        return base

    def test_approved_complete_production_can_have_no_baseline(self):
        base = self.production()
        status, report = self.run_audit(base)
        self.assertFalse(status)
        self.assertEqual(report['courses']['I63']['production_proof'], 'proof/production.json')
        self.assertEqual(report['totals']['before']['words'], 0)

    def test_production_receipt_does_not_approve_itself_or_stale_hashes(self):
        base = self.production()
        self.write('glossary/i63.py', '# changed')
        status, report = self.run_audit(base)
        self.assertTrue(status)
        self.assertIn('empreinte', report['errors'][0])
        self.git('rm', '--cached', '.medina/7-starter-codex.json')
        self.git('commit', '-qm', 'without approval')
        status, report = self.run_audit(self.git('rev-parse', 'HEAD'))
        self.assertTrue(status)

    def test_accessible_svg_or_original_img_and_meaningful_caption(self):
        title_svg = '<svg role="img" aria-labelledby="caption"><title id="caption">Schéma causal</title></svg>'
        for media in [SVG, IMG, title_svg]:
            self.assertTrue(audit.accessible_figure(audit.science(source(media)).xpath('.//figure')[0]))
        for media in ['<img src="figure.png" alt=" ">', '<img alt="Figure">', '<svg role="img" aria-label=" "></svg>',
                      '<svg role="img" aria-labelledby="missing"></svg>',
                      IMG.replace('<img ', '<img hidden '), IMG.replace('<img ', '<img aria-hidden="true" '),
                      SVG.replace('<svg ', '<svg style="display: none" ')]:
            self.assertFalse(audit.accessible_figure(audit.science(source(media)).xpath('.//figure')[0]))
        figure = audit.science(source(IMG).replace('Légende et attribution.', ' ')).xpath('.//figure')[0]
        self.assertFalse(audit.accessible_figure(figure))
        figure = audit.science(source(IMG).replace('<figcaption>', '<figcaption hidden>')).xpath('.//figure')[0]
        self.assertFalse(audit.accessible_figure(figure))

    def test_density_navigation_figures_and_each_callout_still_block(self):
        self.write('chapters/I63/I63_c.html', source())
        base = self.commit()
        cases = [source(count=1), source().replace('data-s="i63-s-normal"', 'data-s="missing"'),
                 source().replace('<figure>' + SVG + '<figcaption>Légende et attribution.</figcaption></figure>', ''),
                 source().replace('<div class="sci"', '<div class="other"')]
        cases += [source(callouts=[other for other in CALLOUTS if other != label]) for label in CALLOUTS]
        for value in cases:
            with self.subTest(value=value[:100]):
                self.write('chapters/I63/I63_c.html', value)
                status, report = self.run_audit(base)
                self.assertTrue(status)
                self.assertTrue(report['errors'])

    def test_missing_current_and_malformed_baseline_do_not_pass(self):
        self.write('chapters/I63/I63_c.html', '<p>No science panel</p>')
        base = self.commit()
        self.write('chapters/I63/I63_c.html', source())
        status, report = self.run_audit(base)
        self.assertTrue(status)
        self.assertIsNone(report['courses']['I63']['before'])
        (self.root / 'chapters/I63/I63_c.html').unlink()
        status, report = self.run_audit(base)
        self.assertTrue(status)
        self.assertIn('source actuelle invalide', report['errors'][0])

    def test_empty_current_html_is_reported_as_failure(self):
        self.write('chapters/I63/I63_c.html', source())
        base = self.commit()
        self.write('chapters/I63/I63_c.html', '')
        status, report = self.run_audit(base)
        self.assertTrue(status)
        self.assertIn('source actuelle invalide', report['errors'][0])


if __name__ == '__main__':
    unittest.main()
