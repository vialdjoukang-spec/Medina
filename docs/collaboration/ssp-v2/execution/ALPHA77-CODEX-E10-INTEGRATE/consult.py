from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib,json,re,subprocess,sys,urllib.request
sys.path.insert(0,str(Path.cwd()))
from tools.swissmedic_fi import texte
from lxml import html as LH
OUT=Path('/workspace/scratch/E10-integrate-sources')
old=json.loads(Path('/workspace/medina-alpha1-taches/ALPHA1-CODEX-E10-MED/docs/collaboration/ssp-v2/execution/ALPHA1-CODEX-E10-MED/sources.json').read_text())['sources']
rows=[x for x in old if x['id'] not in ['S10','S12']]
rows += [dict(id='RMS',url='https://www.revmed.ch/view/415288/3626033/RMS_639_449.pdf'),dict(id='GLU',url='https://www.viollier.ch/fr/analysis/7380'),dict(id='CP',url='https://www.viollier.ch/fr/analysis/9620'),dict(id='NA',url='https://www.viollier.ch/fr/analysis/7090'),dict(id='K',url='https://www.viollier.ch/fr/analysis/7100'),dict(id='OSM',url='https://www.viollier.ch/fr/analysis/18362'),dict(id='BIC',url='https://www.viollier.ch/fr/analysis/10236'),dict(id='GAS',url='https://www.lasource.ch/espace-medecins/laboratoires/catalogue-danalyses/gazometrie')]
s=Path('chapters/E10/E10_c.html').read_text()
for id,needle in [('FIG6','https://med.libretexts.org/'),('FIG9','https://pmc.ncbi.nlm.nih.gov/articles/PMC12730728/'),('FIG8','https://pmc.ncbi.nlm.nih.gov/articles/PMC8656040/'),('PHYS','https://www.mdpi.com/1422-0067/20/6/1351')]:
 url=next(u for u in re.findall(r'href="([^"]+)"',s) if u.startswith(needle)); rows.append(dict(id=id,url=url))
def fetch(row):
 row=dict(row); row['consulted_at']=datetime.now(timezone.utc).isoformat()
 try:
  if row['id'] in ['S5','S6','S7']:
   value=texte(row['url'].split('=')[-1]);data=value.encode()
  else:
   req=urllib.request.Request(row['url'],headers={'User-Agent':'Mozilla/5.0'})
   with urllib.request.urlopen(req,timeout=45) as r: data=r.read();row['final_url']=r.url
   if data[:4]==b'%PDF':
    pdf=OUT/(row['id']+'.pdf');pdf.write_bytes(data)
    subprocess.run(['pdftotext','-layout',str(pdf),str(OUT/(row['id']+'.txt'))],check=True);value=(OUT/(row['id']+'.txt')).read_text()
   else:
    html=data.decode('utf-8','replace');(OUT/(row['id']+'.html')).write_text(html)
    soup=LH.fromstring(html)
    for x in soup.xpath('//script|//style|//nav|//header|//footer'): x.drop_tree()
    value='\n'.join(t.strip() for t in soup.itertext() if t.strip())
  row['sha256_download']=hashlib.sha256(data).hexdigest();row['text_path']=row['id']+'.txt'
  (OUT/row['text_path']).write_text(value)
  row['status']='fetched';row['characters']=len(value)
 except Exception as e:row['status']='failed';row['error']=str(e)
 print(row['id'],row['status'],row.get('characters',row.get('error')),flush=True)
 return row
with ThreadPoolExecutor(max_workers=3) as pool:results=list(pool.map(fetch,rows))
(OUT/'consultation-index.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
