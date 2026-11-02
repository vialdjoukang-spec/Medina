import json, pathlib, urllib.request, hashlib, datetime, concurrent.futures, re, subprocess, sys
from lxml import html, etree
ROOT=pathlib.Path(__file__).resolve().parents[5]
# Resolve workspace from script ancestry without assuming another worker's cwd.
ROOT=next(p for p in pathlib.Path(__file__).resolve().parents if (p/'chapters/N04').is_dir())
OUT=pathlib.Path(__file__).parent
CACHE=pathlib.Path('/tmp/medina-n04-source-cache'); CACHE.mkdir(exist_ok=True)
d=json.loads((ROOT/'livraisons/Livraison Claude/N-07-Néphrologie/travail/CYCLE_03_N04/preuves/dossier_sources.json').read_text())
items=[]
for key,s in d['sources'].items():
 u=s['url']
 if 'pmc.ncbi.nlm.nih.gov/articles/' in u:u='https://www.ebi.ac.uk/europepmc/webservices/rest/'+re.search(r'PMC\d+',u)[0]+'/fullTextXML'
 items.append((key,u,s))
for key,s in d['swissmedic_fi'].items():items.append(('FI_'+key,s['url'],s))
def get(item):
 key,u,s=item;p=CACHE/(key+'.raw');t=CACHE/(key+'.txt');r={'id':key,'requested_url':u,'source_url':s['url'],'retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'cache_path':str(t),'status':'unread'}
 try:
  if p.exists() and t.exists(): r['cache_hit']=True;raw=p.read_bytes()
  else:
   with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'MEDINA/1.0 medical educational source review'}),timeout=40) as res:
    raw=res.read(64*1024*1024);r.update(http_status=res.status,final_url=res.url,content_type=res.headers.get('Content-Type'))
   p.write_bytes(raw)
   if raw.startswith(b'%PDF'):
    subprocess.run(['pdftotext','-layout',str(p),str(t)],check=True,capture_output=True)
   elif raw.startswith(b'PK'):
    r['extraction']='zip_not_extracted';t.write_text('')
   else:
    tree=html.fromstring(raw)
    for e in tree.xpath('//script|//style|//noscript'):e.drop_tree()
    text=tree.text_content();text=re.sub(r'[ \t]+',' ',text);text=re.sub(r'\n\s*\n+', '\n',text)
    t.write_text(text)
  r.update(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),text_sha256=hashlib.sha256(t.read_bytes()).hexdigest(),text_bytes=t.stat().st_size)
 except Exception as e:r.update(status='retrieval_failed',error=str(e))
 return r
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(get,items))
(OUT/'retrieval.json').write_text(json.dumps({'note':'Retrieved is not read; excerpts must be consulted before claims. Full documents cached outside repository.','results':results},ensure_ascii=False,indent=2)+'\n')
for x in results:print(x['id'],x['status'],x.get('http_status','cache'),x.get('bytes',0),x.get('error',''))
