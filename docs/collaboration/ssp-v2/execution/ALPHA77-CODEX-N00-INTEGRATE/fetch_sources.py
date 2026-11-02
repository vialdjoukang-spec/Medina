from pathlib import Path
import requests,json,hashlib,datetime,concurrent.futures
from bs4 import BeautifulSoup
import fitz
CACHE=Path('/tmp/medina-n00-source-cache');CACHE.mkdir(exist_ok=True)
URLS={'CH-RPGN':'https://www.revmed.ch/view/518997/4233572/RMS_419_480.pdf','CH-HEMATURIA':'https://www.hug.ch/sites/interhug/files/2022-09/strategie_microhematurie.pdf','CUEN-INDEX':'https://manuel.cuen.fr/','FR-HEMATURIA':'https://manuel.cuen.fr/wp-content/uploads/2025/10/CUEN-12e-ed-Chap7-hematurie.pdf'}
def fetch(k,u):
 p=CACHE/(k+'.raw');cached=p.exists()
 try:
  if not cached:
   r=requests.get(u,timeout=65);r.raise_for_status();p.write_bytes(r.content)
  b=p.read_bytes()
  if b[:4]==b'%PDF':
   doc=fitz.open(stream=b,filetype='pdf');txt='\n'.join('[PAGE '+str(i+1)+']\n'+page.get_text() for i,page in enumerate(doc))
  else:txt=BeautifulSoup(b,'lxml').get_text(' ',strip=True)
  (CACHE/(k+'.txt')).write_text(txt)
  return dict(id=k,url=u,cached=cached,sha256=hashlib.sha256(b).hexdigest(),bytes=len(b),fetched_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='cached_not_yet_read')
 except Exception as e:return dict(id=k,url=u,error=str(e),status='failed')
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:r=list(ex.map(lambda kv:fetch(*kv),URLS.items()))
 (CACHE/'retrieval.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
