#!/usr/bin/env python3
"""Lire les reçus distants déjà collectés après le dernier snapshot publié.

Ne modifie ni la collecte brute, ni le registre d'achèvements, ni une activité.
"""
import argparse, datetime as dt, hashlib, json
from pathlib import Path

def main():
    p=argparse.ArgumentParser();p.add_argument('evidence',type=Path);a=p.parse_args()
    c=json.loads((a.evidence/'collection.json').read_text())
    known={x['code'] for x in c['completed_lessons']};extra=[]
    for v in c['versions']:
        if v['code'] in known or not v['version_is_remote_head']:continue
        if not v.get('binding_preview_matches') or not v['binding_checks'] or not all(x['ok'] for x in v['binding_checks']):continue
        folder=a.evidence/v['local_evidence_folder'];receipt=folder/'harness-completion.json'
        if not receipt.exists():continue
        r=json.loads(receipt.read_text())
        assert r['code']==v['code'] and r['branch']==v['branch']
        for name,key in [('lesson-manifest.json','manifest_sha256'),('source-binding.json','source_binding_sha256')]:
            assert hashlib.sha256((folder/name).read_bytes()).hexdigest()==r[key]
        assert r['preview_sha256']==v['preview']['sha256']
        assert r['publication_allowed'] is False and r['clinical_certification'] is False
        extra.append({'completion':r,'remote_version':v['version_sha'],
                      'receipt_evidence':v['evidence']['harness-completion.json'],
                      'scope':'Reçu distant exact, postérieur au snapshot publié ; aucune nouvelle clôture créée.'})
        known.add(r['code'])
    out={'checked_at':dt.datetime.now(dt.timezone.utc).isoformat(),
         'snapshot_generated_at':c['status_generated_at'],'snapshot_completed_count':len(c['completed_lessons']),
         'remote_completions_after_snapshot':extra,'activity_refreshed':False,'receipts_refreshed':False}
    (a.evidence/'reconciled-completions.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'snapshot':len(c['completed_lessons']),'additional_remote':[x['completion']['code'] for x in extra]}))

if __name__=='__main__':main()
