from pathlib import Path
from bs4 import BeautifulSoup
from PIL import Image
import re,json,hashlib,datetime,sys
R=Path(__file__).resolve().parents[5];D=Path(__file__).resolve().parent;C=Path('/tmp/medina-source-cache/endocrinologie/E30');sys.path.insert(0,str(R));import build_medina as b
files=sorted((R/'chapters/E30').glob('*.html'));s=''.join(p.read_text() for p in files);so=BeautifulSoup(s,'html.parser');ids=re.findall(r'\bid="([^"]+)"',s);assert len(ids)==len(set(ids));assert not so.select('a a,button button');keys=set(re.findall(r'\bdata-k="([^"]+)"',s));pops=set(re.findall(r'\bdata-pop="([^"]+)"',s));assert keys==pops,(keys-pops,pops-keys)
# Seven strict structural checks, in addition to native science and abbreviation audits.
tab=so.select_one('#pS button[data-s]');assert len(so.select('#pS button[data-s]'))==6 and tab['id']=='e30-tab-semio' and tab['data-s']=='e30-s-semio' and tab.string=='Sémiologie fondamentale et analytique' and tab['role']=='tab' and tab['aria-controls']=='e30-s-semio' and tab['aria-selected']=='true'
panel=so.select_one('#e30-s-semio');assert panel['role']=='tabpanel' and panel['aria-labelledby']=='e30-tab-semio' and not panel.has_attr('hidden');assert panel.select_one('.ilot h3').string=='Pour la leçon : quelle est la sémiologie fondamentale et analytique ?'
required={'normal','signs','mechanisms','examination','interpretation','differentials','urgency','limits','sources'};sections=panel.select('[data-semiology]');assert len(sections)==9 and {x['data-semiology'] for x in sections}==required;assert all(x.select_one('h3') and x.select_one('p').decode_contents().strip() for x in sections);assert panel.select_one('[data-semiology="sources"] a[href^="https://"]')
clinical=so.select('[data-semiology-clinical="E30"]');assert len(clinical)==1 and clinical[0].select_one('p').decode_contents().strip() and any(x.get('id')=='pA' for x in clinical[0].parents)
findings=b.audit(b.wrap_html(s),'E30');assert findings=={},findings
rendered=b.wrap_html(b.transform(s));automatic=sorted(set(re.findall(r'data-ab="([^"]+)"',rendered)));assert automatic==['FI','OFS','OpenStax'],automatic
report=dict(at=datetime.datetime.now(datetime.timezone.utc).isoformat(),result='passed',base_sha='8a512893acbab9caa0dcfdd0e8682a44ea72fda6',source_files=6,unique_ids=len(ids),window_references=len(keys),windows=len(pops),science_tabs=6,semiology_sections=9,strict_semiology_checks=7,strict_semiology_structure='passed',quizzes=len(so.select('.quiz')),abbreviation_findings=findings,automatic_definitions_after_context_review=automatic,nested_anchors=0,inline_styles=len(re.findall(r'\sstyle=',s)),original_images={},source_files_sha256={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},clinical_certification=False)
for im in so.select('img'):
 p=R/im['src'];assert p.read_bytes()==(C/p.name).read_bytes();report['original_images'][im['src']]=hashlib.sha256(p.read_bytes()).hexdigest()
(D/'static-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False,indent=2))
