#!/usr/bin/env python3
"""Parse explicit downloaded artifact ZIPs; never renew author activity or source bindings."""
import argparse, datetime as dt, hashlib, json, shutil, zipfile
from pathlib import Path
from bs4 import BeautifulSoup

def main():
    p=argparse.ArgumentParser()
    p.add_argument('evidence',type=Path)
    p.add_argument('--previous',type=Path)
    p.add_argument('--artifact',action='append',nargs=3,metavar=('RUN','ID','ZIP'),default=[])
    a=p.parse_args();r=a.evidence;now=dt.datetime.now(dt.timezone.utc).isoformat()
    prior=a.previous/'artifact-connector-access.json' if a.previous else None
    receipt=json.loads(prior.read_text()) if prior and prior.exists() else {'artifacts':[],'prior_failures_preserved':True}
    if a.previous:
        for folder in ['logs','artifacts-connector']:
            if (a.previous/folder).exists():shutil.copytree(a.previous/folder,r/folder,dirs_exist_ok=True)
    meta=json.loads((r/'collection.json').read_text())
    for run,aid,zpath in a.artifact:
        out=r/'artifacts-connector'/run;out.mkdir(parents=True,exist_ok=True)
        zpath=Path(zpath);files={};embedded={}
        with zipfile.ZipFile(zpath) as z:
            for name in ['remote-dashboard.html','remote-status.json','remote-observation.json','rapport-08h00.html']:
                if name not in z.namelist():continue
                data=z.read(name);(out/name).write_bytes(data)
                files[name]={'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}
                if name.endswith('.html'):
                    soup=BeautifulSoup(data,'html.parser')
                    script=soup.find('script',id='data')
                    if not script:
                        script=next((s for s in soup.find_all('script') if s.get('type')=='application/json'),None)
                    if script:
                        d=json.loads(script.string or script.get_text())
                        embedded[name]={'generated_at':d.get('generated_at'),'report_frozen_at':d.get('report_frozen_at'),'completed_lessons':len(d.get('completed_lessons',[])),'agents':[{k:x.get(k) for k in ['id','lesson','stage','activity_at']} for x in d.get('agents',[])]}
                    for s in soup(['script','style']):s.decompose()
                    (out/(name+'.visible.txt')).write_text(soup.get_text(' ',strip=True))
        obs=json.loads((out/'remote-observation.json').read_text());status=json.loads((out/'remote-status.json').read_text())
        entry={'artifact_id':int(aid),'run_id':int(run),'download_method':'GitHub connector, puis URL de fichier autorisée','parsed_at':now,'zip_sha256':hashlib.sha256(zpath.read_bytes()).hexdigest(),'files':files,'observation':obs,'status_generated_at':status.get('generated_at'),'completion_count':len(status.get('completed_lessons',[])),'previous_cli_download_error':next((x.get('download_error') for x in meta['artifacts'] if x['id']==int(aid)),None),'scope':'Extraction automatisée JSON, métadonnées embarquées et texte HTML. Lecture humaine/IA ciblée consignée séparément ; aucune revue visuelle exhaustive déduite.','embedded_html_data_checked':embedded,'frozen_report_limit':'Le nom rapport-08h00 ne prouve pas une génération à 08 h ; les deux horodatages réels sont conservés.'}
        receipt['artifacts']=[x for x in receipt['artifacts'] if x['artifact_id']!=int(aid)]+[entry]
        print(json.dumps(entry,ensure_ascii=False))
    receipt['last_parsed_at']=now;receipt['author_activity_refreshed']=False;receipt['source_bindings_refreshed']=False
    (r/'artifact-connector-access.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')

if __name__=='__main__':main()
