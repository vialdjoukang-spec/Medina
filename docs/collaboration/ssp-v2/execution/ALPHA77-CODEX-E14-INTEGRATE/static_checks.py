from pathlib import Path
from bs4 import BeautifulSoup
import re,json,hashlib,datetime
R=Path(__file__).resolve().parents[5];D=Path(__file__).resolve().parent
import sys;sys.path.insert(0,str(R));import build_medina as b
files=sorted((R/'chapters/E14').glob('*.html'));s=''.join(p.read_text() for p in files);so=BeautifulSoup(s,'html.parser');ids=re.findall(r'\bid="([^"]+)"',s);assert len(ids)==len(set(ids));assert not so.select('a a,button button');keys=set(re.findall(r'\bdata-k="([^"]+)"',s));pops=set(re.findall(r'\bdata-pop="([^"]+)"',s));assert keys==pops,(keys-pops,pops-keys);assert len(so.select('[data-semiology]'))==9;assert len(so.select('button[data-s]'))==6;assert len(so.select('[data-semiology-clinical="E14"]'))==1
findings=b.audit(b.wrap_html(s),'E14');assert findings=={},findings
rendered=b.wrap_html(b.transform(s));forbidden=['S1','S3','IA','IC','A1','A2','A3','AA','CMT','TH','T2','RCP','NovoRapid','KCl'];assert not [k for k in forbidden if 'data-ab="'+k+'"' in rendered]
report={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'result':'passed','base_sha':'8a512893acbab9caa0dcfdd0e8682a44ea72fda6','source_files':6,'unique_ids':len(ids),'window_references':len(keys),'windows':len(pops),'science_tabs':6,'semiology_sections':9,'quizzes':len(so.select('.quiz')),'abbreviation_findings':findings,'known_homonyms_or_unrelated_drug_windows_suppressed':forbidden,'nested_anchors':0,'inline_styles':len(re.findall(r'\sstyle=',s)),'original_images':{},'source_files_sha256':{str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},'clinical_certification':False}
for im in so.select('img'):
 p=R/im['src'];report['original_images'][im['src']]=hashlib.sha256(p.read_bytes()).hexdigest();assert p.read_bytes()==Path('/tmp/medina-source-cache/endocrinologie/E14/pancreas-openstax2013.jpg').read_bytes()
(D/'static-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False,indent=2))
