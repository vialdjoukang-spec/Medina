"""Acquire exact Commons originals and page provenance; no certification from metadata."""
from pathlib import Path
import urllib.request,urllib.parse,json,hashlib,datetime,time
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[5]
CACHE=Path('/tmp/medina-n00-source-cache')
DEST=ROOT/'assets/img/n00/alpha/codex';DEST.mkdir(parents=True,exist_ok=True)
names=['Post-infectious_glomerulonephritis_-_high_mag.jpg','Crescentic_glomerulonephritis_-_high_mag.jpg','RTE_cast,_muddy_granular_cast,_WBC_cast_and_RBC_cast_in_urine.jpg']
def get(url):
 req=urllib.request.Request(url,headers={'User-Agent':'Image_Codex_Finder/1.0 (MEDINA educational; source review)'})
 with urllib.request.urlopen(req,timeout=60) as r:return r.read()
rows=[]
for i,n in enumerate(names):
 u='https://commons.wikimedia.org/wiki/File:'+urllib.parse.quote(n)
 p=CACHE/('figure-page-'+str(i)+'.html')
 if not p.exists():p.write_bytes(get(u))
 s=BeautifulSoup(p.read_bytes(),'html.parser')
 (CACHE/('figure-page-'+str(i)+'.txt')).write_text(s.get_text('\n',strip=True))
 original=s.select_one('.fullImageLink a')['href']
 d=DEST/n
 if not d.exists():d.write_bytes(get(original))
 rows.append(dict(name=n,source_url=u,original_url=original,path=str(d.relative_to(ROOT)),sha256=hashlib.sha256(d.read_bytes()).hexdigest(),source_page_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),retrieved_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='awaiting_rights_and_visual_review'))
 print(rows[-1],flush=True)
 time.sleep(.5)
(Path(__file__).parent/'figure-acquisition.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
