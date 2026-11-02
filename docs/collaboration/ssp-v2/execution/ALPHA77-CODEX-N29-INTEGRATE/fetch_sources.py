from pathlib import Path
import requests,json,hashlib,datetime,concurrent.futures
from bs4 import BeautifulSoup
import fitz
CACHE=Path('/tmp/medina-n29-source-cache');CACHE.mkdir(exist_ok=True)
URLS={'S6': 'https://www.bag.admin.ch/dam/fr/sd-web/fPW7HAdyOiZ0/tuberkulose-handbuch.pdf', 'S7': 'https://www.bag.admin.ch/dam/fr/sd-web/KgDGxmnGvfis/Bulletin-2026-Tuberculose.pdf', 'S8': 'https://www.guidelines.fmh.ch/pdfs/f37e3a6a4d278af20655207d1a472f93-fr.pdf', 'S12': 'https://www.who.int/news-room/fact-sheets/detail/schistosomiasis', 'S13': 'https://www.who.int/teams/control-of-neglected-tropical-diseases/schistosomiasis/control-and-elimination-programmes', 'S14': 'https://iusti.org/wp-content/uploads/2020/07/Syphilis2020guideline.pdf', 'S15': 'https://www.bag.admin.ch/fr/syphilis-fr', 'S9': 'https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8614939/fullTextXML', 'S10': 'https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4293885/fullTextXML', 'S11': 'https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12875035/fullTextXML', 'S16': 'https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12824066/fullTextXML', 'S17': 'https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4158338/fullTextXML', 'S20': 'https://amiko.oddb.org/fr/fi?gtin=7680671290011', 'S21': 'https://amiko.oddb.org/fr/fi?gtin=7680673800010', 'S22': 'https://amiko.oddb.org/fr/fi?gtin=7680470630353', 'S23': 'https://amiko.oddb.org/fr/fi?gtin=7680331530013', 'S24': 'https://amiko.oddb.org/fr/fi?gtin=7680576990023', 'S25': 'https://amiko.oddb.org/fr/fi?gtin=7680697650011'}
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
