from pathlib import Path
import requests,json,hashlib,datetime,concurrent.futures
from bs4 import BeautifulSoup
import fitz
CACHE=Path('/tmp/medina-c64-source-cache');CACHE.mkdir(exist_ok=True)
URLS={
'CH-EPI':'https://krebs-monitoring.bfs.admin.ch/fr/detail/C64',
'CH-RMS-MASSES':'https://www.revmed.ch/view/420513/3655172/RMS_629_2160.pdf',
'CH-INSEL':'https://urologie.insel.ch/fr/prestations/pathologies/tumeurs-du-parenchyme-renal',
'EU-EAU2026':'https://d56bochluxqnz.cloudfront.net/documents/full-guideline/EAU-Guidelines-on-Renal-Cell-Carcinoma-2026_2026-07-05-195750_dguv.pdf'}
def fetch(k,u):
 p=CACHE/(k+'.raw');cached=p.exists()
 try:
  if not cached:
   r=requests.get(u,timeout=60);r.raise_for_status();assert len(r.content)<20*1024*1024,'size limit';p.write_bytes(r.content)
  b=p.read_bytes()
  if b[:4]==b'%PDF':
   doc=fitz.open(stream=b,filetype='pdf');txt='\n'.join('[PAGE '+str(i+1)+']\n'+page.get_text() for i,page in enumerate(doc))
  else:txt=BeautifulSoup(b,'lxml').get_text('\n',strip=True)
  (CACHE/(k+'.txt')).write_text(txt)
  return dict(id=k,url=u,cached=cached,sha256=hashlib.sha256(b).hexdigest(),bytes=len(b),fetched_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='cached_not_yet_read')
 except Exception as e:return dict(id=k,url=u,error=str(e),status='failed_no_automatic_retry')
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:r=list(ex.map(lambda kv:fetch(*kv),URLS.items()))
 (CACHE/'retrieval.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
