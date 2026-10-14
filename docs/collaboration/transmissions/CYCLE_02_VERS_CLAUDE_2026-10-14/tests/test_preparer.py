"""Tests mécaniques sur fixtures minimales, PAS tests du site Medina complet."""
from __future__ import annotations
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
loader = importlib.util.spec_from_file_location('preparer', ROOT/'correctif/preparer_correctif.py')
m = importlib.util.module_from_spec(loader)
loader.loader.exec_module(m)
SPEC = json.loads((ROOT/'correctif/corrections_G45.json').read_text(encoding='utf-8'))
POP = ('<template data-pop="g45-aspirine" data-title="Fixture">'
       '<h3>Exclusions et situations particulières</h3><p>Texte témoin.</p>'
       '<h3>Interactions et surveillance</h3><p>Texte témoin.</p></template>\n'
       '<template data-pop="g45-eliquis" data-title="Fixture">'
       '<h3>Surveillance et interactions</h3><p>Texte témoin.</p>'
       '<p class="src">Sources : témoin.</p></template>')
BODY = ('<section class="ilot" id="g45-p02">'
        '<h3 id="g45-p02-partie-2">2.2 Contre-indications</h3><p>Témoin.</p>'
        '<h3 id="g45-p02-partie-3">2.3 Effets indésirables</h3><p>Témoin.</p>'
        '<h3 id="g45-p02-partie-4">2.4 Surveillance</h3><p>Témoin.</p></section>')


class ProposalTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.home = Path(self.tmp.name).resolve()
        self.repo = self.home/'Medina'
        self.repo.mkdir()
        self.spec = copy.deepcopy(SPEC)
        for entry in self.spec['files']:
            text = POP if entry['path'].endswith('_pop2.html') else BODY
            raw = text.encode('utf-8')
            file = self.repo/entry['path']
            file.parent.mkdir(parents=True, exist_ok=True)
            file.write_bytes(raw)
            # Empreintes de fixtures : seule cette spécification de test les
            # remplace. La spécification livrée conserve les SHA de GitHub.
            entry['expected_git_blob_sha1'] = m.git_blob_sha1(raw)
        self.output = self.home/'sortie'

    def test_git_object_hash(self):
        self.assertEqual(m.git_blob_sha1(b''), 'e69de29bb2d1d6434b8b29ae775ad8c2e48c5391')

    def test_two_files_and_four_operations(self):
        changes = m.prepare_changes(self.repo,self.spec)
        self.assertEqual(len(changes),2)
        self.assertEqual(sum(len(c['markers']) for c in changes),4)

    def test_expected_semantic_markers(self):
        text = '\n'.join(c['after_bytes'].decode() for c in m.prepare_changes(self.repo,self.spec))
        for marker in ['G45-R1-pop','G45-R3-pop','G45-R1-corps','G45-R3-corps-aps','G45-R3-corps-hemorragie']:
            self.assertEqual(text.count(f'data-c02-correction="{marker}"'),1)

    def test_missing_source_file(self):
        (self.repo/self.spec['files'][0]['path']).unlink()
        with self.assertRaises(m.Refusal): m.prepare_changes(self.repo,self.spec)

    def test_mismatched_whole_file_hash(self):
        path = self.repo/self.spec['files'][1]['path']
        path.write_bytes(path.read_bytes()+b' ')
        with self.assertRaises(m.Refusal): m.prepare_changes(self.repo,self.spec)

    def test_production_hashes_do_not_accept_fixtures(self):
        with self.assertRaises(m.Refusal): m.prepare_changes(self.repo,SPEC)

    def test_duplicate_file_is_rejected(self):
        self.spec['files'][1] = copy.deepcopy(self.spec['files'][0])
        with self.assertRaises(m.Refusal): m.prepare_changes(self.repo,self.spec)

    def test_canonical_path_is_rejected(self):
        self.spec['files'][0]['path'] = 'chapters/G45/G45_pop2.html'
        with self.assertRaises(m.Refusal): m.prepare_changes(self.repo,self.spec)

    def test_path_traversal_is_rejected(self):
        with self.assertRaises(m.Refusal): m.checked_path(self.repo,'../outside')

    def test_symlink_is_rejected(self):
        path = self.repo/self.spec['files'][0]['path']
        data = path.read_bytes(); path.unlink()
        other=self.home/'external.html'; other.write_bytes(data); path.symlink_to(other)
        with self.assertRaises(m.Refusal): m.prepare_changes(self.repo,self.spec)

    def test_missing_scope(self):
        with self.assertRaises(m.Refusal): m.transform('<p>Sans fenêtre</p>', self.spec['files'][0]['operations'])

    def test_duplicate_scope(self):
        with self.assertRaises(m.Refusal): m.transform(POP+POP, self.spec['files'][0]['operations'])

    def test_missing_anchor(self):
        text=POP.replace('<h3>Interactions et surveillance</h3>','<h3>Autre</h3>')
        with self.assertRaises(m.Refusal): m.transform(text,self.spec['files'][0]['operations'])

    def test_missing_scope_end(self):
        with self.assertRaises(m.Refusal): m.transform(POP.replace('</template>',''),self.spec['files'][0]['operations'])

    def test_reapplication_is_rejected(self):
        ops=self.spec['files'][0]['operations']
        changed=m.transform(POP,ops)
        with self.assertRaises(m.Refusal): m.transform(changed,ops)

    def test_source_repository_is_unchanged(self):
        before={str(p.relative_to(self.repo)):p.read_bytes() for p in self.repo.rglob('*') if p.is_file()}
        m.build_proposal(self.repo,self.output,self.spec)
        after={str(p.relative_to(self.repo)):p.read_bytes() for p in self.repo.rglob('*') if p.is_file()}
        self.assertEqual(before,after)

    def test_output_inside_repo_is_rejected(self):
        with self.assertRaises(m.Refusal): m.build_proposal(self.repo,self.repo/'sortie',self.spec)

    def test_existing_output_is_preserved(self):
        self.output.mkdir(); (self.output/'temoin').write_text('à conserver')
        with self.assertRaises(m.Refusal): m.build_proposal(self.repo,self.output,self.spec)
        self.assertEqual((self.output/'temoin').read_text(),'à conserver')

    def test_receipt_does_not_certify_audit_or_publication(self):
        m.build_proposal(self.repo,self.output,self.spec)
        report=json.loads((self.output/'recu_proposition.json').read_text())
        self.assertEqual(report['reserves_lifted'],[])
        for name in ['repository_modified','source_ledger_updated','cross_pass2_performed','counter_audit_performed','human_medical_validation','publication_performed']:
            self.assertIs(report[name],False)
        for c in report['files']:
            raw=(self.output/'proposition'/c['path']).read_bytes()
            self.assertEqual(hashlib.sha256(raw).hexdigest(),c['after_sha256'])

    def test_failed_validation_creates_no_output(self):
        self.spec['files'][1]['expected_git_blob_sha1']='0'*40
        with self.assertRaises(m.Refusal): m.build_proposal(self.repo,self.output,self.spec)
        self.assertFalse(self.output.exists())
        self.assertEqual(list(self.home.glob('.medina-c02-*')),[])

    @unittest.skipUnless(shutil.which('git'),'git absent')
    def test_generated_diff_applies_to_fixtures_with_spaces_accents_and_no_final_newline(self):
        m.build_proposal(self.repo,self.output,self.spec)
        patch=self.output/'cycle2-g45-partiel.patch'
        subprocess.run(['git','init','-q',str(self.repo)],check=True,capture_output=True)
        subprocess.run(['git','-C',str(self.repo),'apply','--check',str(patch)],check=True,capture_output=True)
        subprocess.run(['git','-C',str(self.repo),'apply',str(patch)],check=True,capture_output=True)
        for entry in self.spec['files']:
            self.assertEqual((self.repo/entry['path']).read_bytes(),(self.output/'proposition'/entry['path']).read_bytes())


if __name__=='__main__':
    unittest.main(verbosity=2)
