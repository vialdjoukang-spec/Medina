from pathlib import Path
import json,requests,hashlib,concurrent.futures,shutil
from bs4 import BeautifulSoup
OUT=Path(__file__).resolve().parent; ROOT=OUT.parents[4]; CACHE=Path('/tmp/medina-c64-source-cache'); ASSET=ROOT/'assets/img/c64/alpha/codex';ASSET.mkdir(parents=True,exist_ok=True)
rows=json.loads((CACHE/'imagefinder-rcc.json').read_text())['results']; selected=[rows[i] for i in [0,1,3]]
def get(item):
 n=item['title'].split(':',1)[1].replace(' ','_');p=CACHE/('figure-'+n+'.html')
 if not p.exists():
  # Public page returned HTTP403 in first attempt; use already acquired Commons API metadata, no retry.
  p=CACHE/('figure-'+n+'.metadata.json');p.write_text(json.dumps(item,ensure_ascii=False,indent=2))
 dest=ASSET/n
 if not dest.exists():
  r=requests.get(item['original_url'],headers={'User-Agent':'Image_Codex_Finder/1.0 (MEDINA educational; source review)'},timeout=45);r.raise_for_status();assert len(r.content)<20*1024*1024;dest.write_bytes(r.content)
 (CACHE/('figure-'+n+'.txt')).write_text(BeautifulSoup(p.read_bytes(),'lxml').get_text('\n',strip=True))
 return dict(item,path=str(dest.relative_to(ROOT)),sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),proof_path=str(p),proof_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),visual_review_pending=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:result=list(ex.map(get,selected))
for n in ['Kidney_section_vertical.png','2618_Nephron_Secretion_Reabsorption.jpg']:
 src=Path('/workspace/Medina-nephrologie-n29/assets/img/n29/alpha/codex')/n;shutil.copyfile(src,ASSET/n)
(OUT/'figure-acquisition.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print([(x['path'],x['license']) for x in result])
