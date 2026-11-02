#!/usr/bin/env python3
"""Inspection statique ciblée de versions immuables ; aucune écriture des cours."""
import argparse,datetime,hashlib,json,re,subprocess,importlib.util
from pathlib import Path
TITLE='Pour la leçon : quelle est la sémiologie fondamentale et analytique ?'
REQUIRED={'normal','signs','mechanisms','examination','interpretation','differentials','urgency','limits','sources'}
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('medina_report_semio',ROOT/'harness/medina_harness.py');mh=importlib.util.module_from_spec(spec);spec.loader.exec_module(mh)
def read(sha,path):
 return subprocess.check_output(['git','show',sha+':'+path],cwd=ROOT)
def main():
 p=argparse.ArgumentParser();p.add_argument('evidence',type=Path);a=p.parse_args()
 collection=json.loads((a.evidence/'collection.json').read_text());completed={x['code'] for x in collection['completed_lessons']};rows=[]
 for v in collection['versions']:
  if v['code'] not in completed or not v.get('binding_preview_matches'):continue
  code=v['code'];sha=v['version_sha'];parts={f'chapters/{code}/{code}_{suffix}.html':read(sha,f'chapters/{code}/{code}_{suffix}.html') for suffix in 'abcd'}
  result=mh.inspect_semiology_parts(code,parts)
  checks=result['checks'];h3=result['checks']['first_unit_exact_h3']
  rows.append({'code':code,'sha':sha,'checks':checks,'passed':all(checks.values()),'findings':[k for k,val in checks.items() if not val],'native_parser':True,'source_hashes':{k:hashlib.sha256(b).hexdigest() for k,b in parts.items()},'scope':'Sept contrôles statiques ciblés issus de starter_codex.py ; pas exécution complète de Starter, ni revue médicale.'})
 report={'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'read_only':True,'author_activity_refreshed':False,'source_bindings_refreshed':False,'rules_reference':'tools/starter_codex.py lignes240–267, base8a512893acbab9caa0dcfdd0e8682a44ea72fda6','rows':rows}
 (a.evidence/'semiology-inspection.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'versions':len(rows),'passed':sum(x['passed'] for x in rows),'findings':[{k:x[k] for k in ['code','sha','findings']} for x in rows if not x['passed']]},ensure_ascii=False))
if __name__=='__main__':main()
