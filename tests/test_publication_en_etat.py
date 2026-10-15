"""Publication de vrais blobs de provenance, sans audit clinique inventé."""
import copy
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from tools import espace as E
from tools import publication_en_etat as P


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.git('init', '-q'); self.git('config', 'user.name', 'Test technique')
        self.git('config', 'user.email', 'test@example.invalid')
        self.write(P.AUTHORITY, (Path(__file__).resolve().parents[1] / P.AUTHORITY).read_bytes())
        self.json('chapters.json', [])
        self.json('nosology/fragments/S08.json', {'lessons': [{'code': 'R25'}]})
        self.source_dir = 'livraisons/Livraison Claude/N-05-Neurologie/TEST'
        self.source = self.source_dir + '/chapters/R25/R25_a.html'
        self.content = b'<p>Brouillon de fixture incomplet, sans validation.</p>'
        self.write(self.source, self.content)
        self.asset = 'assets/img/cycle42/r25/figure.png'
        self.asset_content = b'\x89PNG\r\n\x1a\nFigure technique de fixture'
        self.write(self.source_dir + '/' + self.asset, self.asset_content)
        self.base = self.commit()
        self.path = 'chapters/R25/R25_a.html'
        self.write(self.path, self.content)
        self.json('chapters.json', [dict(code='R25', title='Fixture', covers=['R25'], integrated=True,
                                       provisional_injection=True, publication_mode='en_etat', audit_deferred='non_realise')])
        self.receipt = dict(schema_version=1, actor='Codex', authority=P.AUTHORITY,
                            authority_sha256=P.digest((self.root / P.AUTHORITY).read_bytes()),
                            medical_human_validation=False, catalog_sha256=P.digest((self.root / 'chapters.json').read_bytes()),
                            courses=[dict(code='R25', fragment_id='S08', files={self.path: dict(sha256=P.digest(self.content),
                                          provenance_path=self.source, provenance_revision=self.base)})])
        self.json(P.RECEIPT, self.receipt)

    def git(self, *args):
        return subprocess.check_output(['git', *args], cwd=self.root, stderr=subprocess.DEVNULL).decode().strip()

    def write(self, name, raw):
        path = self.root / name; path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(raw)

    def json(self, path, data):
        self.write(path, (json.dumps(data) + '\n').encode())

    def commit(self):
        self.git('add', '.'); self.git('commit', '-qm', 'Fixture technique')
        return self.git('rev-parse', 'HEAD')

    def validate(self):
        self.json(P.RECEIPT, self.receipt)
        after = E.GitTree(self.root, self.commit())
        return E.validate_fragment_guard(E.GitTree(self.root, self.base), after)

    def test_incomplete_source_published_exactly_from_real_commit(self):
        self.assertEqual(self.validate(), [])

    def test_same_permission_for_claude(self):
        self.receipt['actor'] = 'Claude'
        self.assertEqual(self.validate(), [])

    def test_cli_includes_images_copied_from_delivery(self):
        self.write(self.asset, self.asset_content)
        catalog = json.loads((self.root / 'chapters.json').read_bytes())
        catalog[0].update(owner='S08', source_dir=self.source_dir)
        self.json('chapters.json', catalog)
        script = Path(__file__).resolve().parents[1] / 'tools/publication_en_etat.py'
        subprocess.run(['python3', str(script), '--root', str(self.root), '--actor', 'Codex',
                        '--provenance-revision', self.base, '--courses', 'R25'], check=True, capture_output=True)
        self.receipt = json.loads((self.root / P.RECEIPT).read_bytes())
        self.assertEqual(self.receipt['courses'][0]['files'][self.asset]['sha256'], P.digest(self.asset_content))
        self.assertEqual(self.validate(), [])

    def test_copied_image_cannot_be_edited(self):
        self.write(self.asset, b'Image modifiee')
        self.receipt['courses'][0]['files'][self.asset] = dict(sha256=P.digest(b'Image modifiee'),
            provenance_revision=self.base, provenance_path=self.source_dir + '/' + self.asset)
        with self.assertRaisesRegex(E.FragmentError, 'différente de la provenance'):
            self.validate()

    def test_preparatory_commits_validated_as_one_publication(self):
        # Les copies peuvent précéder le reçu final dans la branche de travail.
        (self.root / P.RECEIPT).unlink()
        self.commit()
        self.json(P.RECEIPT, self.receipt)
        final = self.commit()
        with patch.object(E, 'R', self.root):
            self.assertEqual(E.garde(self.base, final), 0)

    def test_content_rewrite_rejected_even_with_new_hash(self):
        self.write(self.path, b'Nouvelle affirmation')
        self.receipt['courses'][0]['files'][self.path]['sha256'] = P.digest(b'Nouvelle affirmation')
        with self.assertRaisesRegex(E.FragmentError, 'différente de la provenance'):
            self.validate()

    def test_missing_provenance_commit_rejected(self):
        self.receipt['courses'][0]['files'][self.path]['provenance_revision'] = 'f' * 40
        with self.assertRaisesRegex(E.FragmentError, 'provenance absent'):
            self.validate()

    def test_existing_canonical_source_cannot_regress_to_old_provenance(self):
        # Une ancienne source réellement présente dans Git ne remplace jamais
        # une version canonique préexistante plus récente.
        (self.root / P.RECEIPT).unlink()
        self.json('chapters.json', [])
        self.write(self.path, b'Version canonique recente de fixture')
        self.base = self.commit()
        self.write(self.path, self.content)
        self.json('chapters.json', [dict(code='R25', title='Fixture', covers=['R25'], integrated=True,
                                       provisional_injection=True, publication_mode='en_etat', audit_deferred='non_realise')])
        with self.assertRaisesRegex(E.FragmentError, 'déjà canonique modifiée'):
            self.validate()

    def test_outside_system_rejected(self):
        self.receipt['courses'][0]['fragment_id'] = 'S01'
        with self.assertRaisesRegex(E.FragmentError, 'hors des quatre'):
            self.validate()

    def test_unlisted_medical_change_rejected(self):
        self.write('chapters/I50/I50_a.html', b'Autre cours')
        with self.assertRaisesRegex(E.FragmentError, 'sans provenance'):
            self.validate()

    def test_historical_status_cannot_be_promoted(self):
        self.json('organisation/CYCLES_CLAUDE.json', {'cycles': 'clotures'})
        with self.assertRaisesRegex(E.FragmentError, 'historique modifié'):
            self.validate()

    def test_validation_cannot_be_claimed(self):
        self.receipt['medical_human_validation'] = True
        with self.assertRaisesRegex(E.FragmentError, 'absence de validation'):
            self.validate()
