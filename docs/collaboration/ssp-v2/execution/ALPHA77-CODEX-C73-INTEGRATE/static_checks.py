from pathlib import Path
from bs4 import BeautifulSoup
from PIL import Image
import re,json,hashlib,datetime,sys,importlib.util
R=Path(__file__).resolve().parents[5];D=Path(__file__).resolve().parent;sys.path.insert(0,str(R));import build_medina as b
files=sorted((R/'chapters/C73').glob('*.html'));raw=''.join(p.read_text()for p in files);so=BeautifulSoup(raw,'html.parser');ids=re.findall(r'\bid="([^"]+)"',raw);assert len(ids)==len(set(ids));assert not so.select('a a,button button');keys=set(re.findall(r'\bdata-k="([^"]+)"',raw));pops=set(re.findall(r'\bdata-pop="([^"]+)"',raw));assert keys==pops,(keys-pops,pops-keys);assert len(so.select('.quiz'))==4
spec=importlib.util.spec_from_file_location('harness_native','/workspace/Medina-harness/harness/medina_harness.py');h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h);strict=h.inspect_semiology(str(R),'C73');(D/'strict-semiology-final.json').write_text(json.dumps(strict,ensure_ascii=False,indent=2)+'\n');assert strict['passed'],strict
findings=b.audit(b.wrap_html(raw),'C73');assert findings=={},findings
transformed=b.wrap_html(b.transform(raw));automatic=sorted(set(re.findall(r'data-ab="([^"]+)"',transformed)));assert automatic==['FI','OpenStax'],automatic
sources={'normal':Path('/tmp/medina-source-cache/endocrinologie/E04/normal-thyroid-openstax2013.jpg'),'pathology':Path('/tmp/medina-source-cache/endocrinologie/C73/histopathology-cameselle2020.jpg')};originals={}
for figure in so.select('figure[data-c73-original]'):
 im=figure.select_one('img');p=R/im['src'];kind=figure['data-c73-original'];assert p.read_bytes()==sources[kind].read_bytes();size=Image.open(p).size;assert size==((737,1410)if kind=='normal'else(1527,1210));originals[im['src']]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'dimensions':size,'source':str(sources[kind])};assert len(figure.select('[data-c73-marker]'))==4
science={x['id']:len(BeautifulSoup(x.decode_contents(),'html.parser').get_text(' ',strip=True).split())for x in so.select('.sci')};assert len(science)==6 and min(science.values())>=280
assert len(so.select('#pA section.ilot'))==14;assert so.select_one('#c73-14 .alert')and so.select_one('#c73-14 .key');assert '[data-c73-table="1"]'in raw and 'min-width:9em'in raw;assert 'min-width:760px'in raw
for p in files:assert p.read_bytes().endswith(b'\n')and not p.read_bytes().endswith(b'\n\n'),p
report={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'result':'passed','source_files':6,'unique_ids':len(ids),'window_references':len(keys),'windows':len(pops),'science_tabs':6,'science_words':science,'strict_semiology_checks':strict['checks'],'quizzes':4,'abbreviation_findings':findings,'automatic_definitions_after_context_review':automatic,'original_images':originals,'total_figures':len(so.select('figure')),'source_files_sha256':{str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in files},'human_validation':False};(D/'static-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False,indent=2))
