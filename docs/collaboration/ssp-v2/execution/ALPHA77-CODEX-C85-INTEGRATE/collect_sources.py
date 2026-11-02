#!/usr/bin/env python3
"""C85: cache exact hors dépôt, délais/tailles bornés, aucune preuve de lecture implicite."""
import concurrent.futures,datetime,hashlib,json,time,urllib.request
from pathlib import Path
from lxml import etree,html
OUT=Path(__file__).resolve().parent
CACHE=Path('/workspace/medina-source-cache/C85');CACHE.mkdir(parents=True,exist_ok=True)
URLS={
 'onkopedia':'https://www.onkopedia.com/de/onkopedia/guidelines/diffuses-grosszelliges-b-zell-lymphom/@@guideline/html/index.html',
 'nappi2025':'https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12101282/fullTextXML',
 'juanpere2013':'https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3579993/fullTextXML',
 'eha2025':'https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12456099/fullTextXML',
}
def fetch(item):
 key,url=item;p=CACHE/(key+'.raw');rec={'id':key,'url':url,'fetched_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'read':False}
 try:
  hit=p.exists() and time.time()-p.stat().st_mtime<86400
  if hit: raw=p.read_bytes()
  else:
   with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Medina-Evidence/1.0'}),timeout=35) as r:
    raw=r.read(8*1024*1024+1);rec['status']=r.status;rec['final_url']=r.url
   if len(raw)>8*1024*1024:raise ValueError('source too large')
   p.write_bytes(raw)
  rec.update(sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw),cache_hit=hit)
  tree=html.fromstring(raw)
  for bad in tree.xpath('//script|//style|//nav|//footer|//header'):bad.drop_tree()
  lines=[]
  for el in tree.xpath('//h1|//h2|//h3|//h4|//title|//p|//table|//fig|//license'):
   s=' '.join(' '.join(el.itertext()).split())
   if s:lines.append(s)
  (CACHE/(key+'.txt')).write_text('\n'.join(lines)+'\n')
  rec['extracted_lines']=len(lines)
 except Exception as e:rec['error']=str(e)
 return rec
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:results=list(pool.map(fetch,URLS.items()))
 (OUT/'retrieval.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n');print(json.dumps(results,ensure_ascii=False))
