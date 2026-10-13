"""Fixtures de garde sans valeur clinique et sans publication fictive."""
import copy
import json
from pathlib import Path
from datetime import datetime
import unittest
from unittest.mock import patch
from tools import night_cycle as N
from tools import tetrade_cycle as C
from tests.test_tetrade_cycle import Tree, encode

NOW = datetime.fromisoformat('2026-10-14T02:00:00+02:00')

class NightGuardTests(unittest.TestCase):
    def setUp(self):
        root = Path(__file__).resolve().parents[1]
        self.state = json.loads((root/N.REGISTRY).read_text())
        self.files = {p: (root/p).read_bytes() for p in [N.AUTHORITY,N.PLAN,N.CAHIER,N.JOURNAL]}
        self.files['chapters.json'] = b'[]'
        self.save(); self.before = Tree(copy.deepcopy(self.files))

    def save(self): self.files[N.REGISTRY] = encode(self.state)
    def guard(self, now=NOW):
        self.save(); return N.validate(self.before, Tree(self.files), now=now)

    def test_activation_has_four_courses_without_medical_change(self):
        old = copy.deepcopy(self.files); old.pop(N.REGISTRY)
        self.assertEqual(N.validate(Tree(old),Tree(self.files),now=NOW), ({},{'G45','E10','N18','D64'},set()))

    def test_activation_after_deadline_and_exact_deadline_rejected(self):
        old = copy.deepcopy(self.files); old.pop(N.REGISTRY)
        for time in ('2026-10-14T06:00:00+00:00','2026-10-14T06:01:00+00:00'):
            with self.subTest(time=time), self.assertRaisesRegex(C.CycleError,'expirée'):
                N.validate(Tree(old),Tree(self.files),now=datetime.fromisoformat(time))

    def test_unchanged_history_can_be_verified_after_deadline(self):
        self.guard(datetime.fromisoformat('2026-10-15T06:00:00+00:00'))

    def test_second_active_cycle_for_same_owner_rejected(self):
        self.state['assignments'].append(dict(cycle=3,owner='Codex',active=True))
        with self.assertRaisesRegex(C.CycleError,'deux cycles actifs'):self.guard()

    def test_double_owner_rejected(self):
        self.state['assignments'][0]['cycle']=2
        with self.assertRaisesRegex(C.CycleError,'responsabilité simultanée'):self.guard()

    def test_cycle1_cannot_return_to_codex(self):
        self.state['assignments'][0].update(owner='Codex',active=False)
        with self.assertRaisesRegex(C.CycleError,'Cycle 1 réservé'):self.guard()

    def test_exactly_four_courses_and_order(self):
        for action in ('extra','swap'):
            state=copy.deepcopy(self.state)
            if action=='extra':self.state['cycles'][0]['chapters'].append(copy.deepcopy(self.state['cycles'][0]['chapters'][0]))
            else:self.state['cycles'][0]['chapters'].reverse()
            with self.subTest(action=action),self.assertRaises(C.CycleError):self.guard()
            self.state=state

    def test_fake_ready_state_without_four_authors_rejected(self):
        self.state['cycles'][0]['chapters'][0]['status']='PRET_A_INJECTER'
        with self.assertRaises(C.CycleError):self.guard()

    def test_future_start_rejected(self):
        self.state['cycles'][0]['started_at']='2026-10-14T04:00:00+00:00'
        with self.assertRaises(C.CycleError):self.guard()

    def test_start_at_cutoff_rejected(self):
        self.state['cycles'][0]['started_at']=N.LAST_START
        with self.assertRaisesRegex(C.CycleError,'07 h 30'):self.guard()

    def test_canonical_without_injection_rejected(self):
        self.files['chapters/G45/G45_a.html']=b'Fixture technique'
        with self.assertRaisesRegex(C.CycleError,'sans injection'):self.guard()

    def test_catalogue_without_injection_rejected(self):
        self.files['chapters.json']=encode([dict(code='G45',covers=['G45'],integrated=True)])
        with self.assertRaisesRegex(C.CycleError,'catalogue modifié'):self.guard()

    def test_journal_cannot_be_rewritten(self):
        self.state['cycles'][0]['state']='ARRETE'
        self.files[N.JOURNAL]=b'{}\n'
        with self.assertRaisesRegex(C.CycleError,'journal historique'):self.guard()

    def test_plan_or_authority_change_rejected(self):
        self.files[N.AUTHORITY]+=b'Fixture altered'
        with self.assertRaisesRegex(C.CycleError,'autorité ou plan'):self.guard()

    def test_closure_with_unpublished_courses_rejected(self):
        self.state['cycles'][0]['state']='CLOTURE'
        with self.assertRaisesRegex(C.CycleError,'clôture prématurée'):self.guard()

    def test_opening_next_cycle_before_closure_rejected(self):
        next_cycle=copy.deepcopy(self.state['cycles'][0]);next_cycle['cycle']=3
        next_cycle['chapters']=[]
        for code,frag,tag in N.missions(Tree(self.files),3):
            next_cycle['chapters'].append(dict(code=code,fragment_id=frag,production_cycle=3,writer='C03-R-'+tag,cross_reviewer='C03-R-'+N.CROSS[tag],counter_reviewer='C03-CA-'+tag,status='EN_PRODUCTION',**{k:None for k in N.PROOFS}))
        self.state['cycles'][0]['state']='ARRETE';self.state['cycles'].append(next_cycle)
        self.state['assignments'][1]['cycle']=3
        with self.assertRaises(C.CycleError):self.guard()

if __name__=='__main__':unittest.main()

class NightInjectionTests(NightGuardTests):
    def prepared(self):
        for row in self.state['cycles'][0]['chapters']:
            row['status']='PRET_A_INJECTER'
            row['files']={f"chapters/{row['code']}/{row['code']}_a.html":C.digest(b'Fixture')}
            for k in ('author','cross_audit','counter_audit','control'):row[k]={'path':'Fixture technique non clinique'}
        self.save();self.before=Tree(copy.deepcopy(self.files))

    def inject(self, i):
        row=self.state['cycles'][0]['chapters'][i];row['status']='INJECTE'
        p=f'preuves/injection-{i}.json'
        self.files[p]=encode(dict(code=row['code'],files=row['files'],injector='Codex — coordinateur du fil'))
        row['injection']={'path':p,'sha256':C.digest(self.files[p])}
        for f in row['files']:self.files[f]=b'Fixture'
        catalog=json.loads(self.files['chapters.json']);catalog.append(dict(code=row['code'],covers=[row['code']],integrated=True));self.files['chapters.json']=encode(catalog)

    def validate_mocked_clinical_proofs(self):
        with patch.object(N,'ready',side_effect=lambda tree,row,rows:row['files']),patch.object(N,'temporal_proofs'),patch.object(N,'journal_proof'):
            return self.guard()

    def test_exact_single_injection(self):
        self.prepared();self.inject(0)
        result=self.validate_mocked_clinical_proofs()
        self.assertEqual(set(result[0]),{'chapters/G45/G45_a.html','chapters.json'})
        self.assertEqual(result[2],{'G45'})

    def test_double_injection_rejected(self):
        self.prepared();self.inject(0);self.inject(1)
        with self.assertRaisesRegex(C.CycleError,'une seule injection'):self.validate_mocked_clinical_proofs()

    def test_skipped_publication_rejected(self):
        self.prepared();self.inject(1)
        with self.assertRaisesRegex(C.CycleError,'ordre de publication'):self.validate_mocked_clinical_proofs()

    def test_extra_catalogue_row_rejected(self):
        self.prepared();self.inject(0)
        rows=json.loads(self.files['chapters.json']);rows.append(dict(code='J45',covers=['J45'],integrated=True));self.files['chapters.json']=encode(rows)
        with self.assertRaisesRegex(C.CycleError,'ajout unique'):self.validate_mocked_clinical_proofs()

    def test_extra_image_change_rejected(self):
        self.prepared();self.inject(0);self.files['assets/img/cycle2/e10/unreviewed.png']=b'Fixture'
        with self.assertRaisesRegex(C.CycleError,'supplémentaires'):self.validate_mocked_clinical_proofs()
