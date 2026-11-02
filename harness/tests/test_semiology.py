"""Regression cases from the post-delivery structural findings; synthetic prose."""
import importlib.util,json,tempfile,unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('mh_semio_target',Path(__file__).resolve().parents[1]/'medina_harness.py')
mh=importlib.util.module_from_spec(spec);spec.loader.exec_module(mh)
class SemiologyTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name);self.folder=self.root/'chapters/G02';self.folder.mkdir(parents=True)
  for suffix in 'abcd':(self.folder/f'G02_{suffix}.html').write_text('')
  self.title='Pour la leçon : quelle est la sémiologie fondamentale et analytique ?'
  buttons='<button id="g02-tab-semio" role="tab" aria-selected="true" aria-controls="g02-s-semio" data-s="g02-s-semio">Sémiologie fondamentale et analytique</button>'+''.join(f'<button data-s="g02-s-{i}">Science</button>' for i in range(5))
  units=''.join(f'<section class="ilot" data-semiology="{name}"><h3>{self.title if i==0 else name}</h3><p>Synthetic substantive text.</p>'+('<a href="https://example.org/source">Source</a>' if name=='sources' else '')+'</section>' for i,name in enumerate(['normal','signs','mechanisms','examination','interpretation','differentials','urgency','limits','sources']))
  self.raw='<div id="pA"><p data-semiology-clinical="G02">Synthetic clinical text.</p></div><div id="pS"><div class="sci-bar">'+buttons+'</div><div class="sci" id="g02-s-semio" aria-labelledby="g02-tab-semio">'+units+'</div></div>'
 def check(self,raw):
  (self.folder/'G02_c.html').write_text(raw);return mh.inspect_semiology(self.root,'G02')
 def test_correct_structure_does_not_certify_clinical_content(self):
  r=self.check(self.raw);self.assertTrue(r['passed']);self.assertFalse(r['clinical_certification']);self.assertFalse(r['source_bindings_refreshed'])
 def test_h2_does_not_satisfy_exact_h3_contract(self):
  r=self.check(self.raw.replace('<h3>'+self.title+'</h3>','<h2>'+self.title+'</h2>'));self.assertIn('first_unit_exact_h3',r['findings'])
 def test_popup_only_source_link_is_not_a_direct_source(self):
  r=self.check(self.raw.replace('<a href="https://example.org/source">Source</a>','<button data-k="source">Source</button>'));self.assertIn('linked_sources_in_semio',r['findings'])
 def test_translated_data_markers_are_not_native_contract(self):
  r=self.check(self.raw.replace('data-semiology="mechanisms"','data-semiology="mecanismes"'));self.assertIn('nine_named_sections',r['findings'])
 def test_read_only_inspection_preserves_binding_and_sources(self):
  binding=self.root/'source-binding.json';binding.write_text('{"verified_at":"original"}\n');self.check(self.raw);before={p:p.read_bytes() for p in self.root.rglob('*') if p.is_file()};mh.inspect_semiology(self.root,'G02');self.assertEqual(before,{p:p.read_bytes() for p in self.root.rglob('*') if p.is_file()})
if __name__=='__main__':unittest.main()
