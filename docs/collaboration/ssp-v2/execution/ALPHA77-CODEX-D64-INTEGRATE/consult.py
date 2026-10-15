from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
from urllib.request import Request,urlopen
from lxml import html,etree
import json,hashlib,subprocess,sys,re
sys.path.insert(0,str(Path.cwd()));from tools.swissmedic_fi import texte
OUT=Path('/workspace/scratch/D64-integrate-sources');OUT.mkdir(exist_ok=True)
base=Path('/workspace/medina-alpha1-taches/ALPHA1-CODEX-D64-MED/docs/collaboration/ssp-v2/execution/ALPHA1-CODEX-D64-MED')
rows=[r for r in json.loads((base/'sources.json').read_text())['sources'] if r['id'] in ['S2','S3','S4','S5','S7','S8','S9','S11','S13','S14','S16','S17','S18','S19','S20']]
for id,url in [('MAT','https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8953437/fullTextXML'),('REG','https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8269393/fullTextXML'),('PAC','https://pac6.ch/fr/chapitres/06-le-monitorage-en-anesthesie-cardiaque/6-5-catheter-pulmonaire-arteriel-de-swan-ganz/6-5-9-transport-doxygene-et-rapport-do2-vo2')]:rows.append({'id':id,'url':url})
def fetch(row):
 row=dict(row);row['acquired_at']=datetime.now(timezone.utc).isoformat()
 try:
  if row['id'] in ['S17','S18','S19','S20']:value=texte(row['url'].split('=')[-1]);data=value.encode()
  else:
   with urlopen(Request(row['url'],headers={'User-Agent':'Mozilla/5.0'}),timeout=45) as r:data=r.read();row['final_url']=r.url
   if data.startswith(b'%PDF'):
    p=OUT/(row['id']+'.pdf');p.write_bytes(data);subprocess.run(['pdftotext','-layout',str(p),str(OUT/(row['id']+'.txt'))],check=True);value=(OUT/(row['id']+'.txt')).read_text()
   elif 'fullTextXML' in row['url']:
    (OUT/(row['id']+'.xml')).write_bytes(data);root=etree.fromstring(data);value='\n'.join(root.itertext())
   else:
    (OUT/(row['id']+'.html')).write_bytes(data);root=html.fromstring(data)
    for x in root.xpath('//script|//style|//nav|//header|//footer'):x.drop_tree()
    value='\n'.join(x.strip() for x in root.itertext() if x.strip())
  row['sha256_download']=hashlib.sha256(data).hexdigest();(OUT/(row['id']+'.txt')).write_text(value);row['status']='acquired';row['characters']=len(value)
 except Exception as e:row['status']='failed';row['error']=str(e)
 print(row['id'],row['status'],row.get('characters',row.get('error')),flush=True);return row
with ThreadPoolExecutor(max_workers=3) as p:results=list(p.map(fetch,rows))
(OUT/'acquisition-index.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
