#!/usr/bin/env python3
"""Independent GitHub observer with explicit, stoppable workflow handoff.

No course writes, model calls, main commits or publication approvals. A live
observer never changes the last activity timestamps supplied by authors.
"""
import argparse
import base64
import datetime as dt
import json
import os
from pathlib import Path
import time
import urllib.error
import urllib.parse
import urllib.request
from medina_harness import atomic, render, now

REPO='vialdjoukang-spec/Medina'
CONTROL_REF='codex/harness-20261102'
SOURCE_REF='codex/harness-observations-20261102'
WORKFLOW_ID=404019430
HOME=Path(__file__).resolve().parent

def api(path, payload=None):
    if not path.startswith('/repos/'+REPO+'/'):raise ValueError('Repository outside allowlist')
    headers={'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28','User-Agent':'Medina-Harness-Watchdog'}
    token=os.environ.get('GH_TOKEN')
    if token:headers['Authorization']='Bearer '+token
    raw=None if payload is None else json.dumps(payload).encode()
    if raw:headers['Content-Type']='application/json'
    req=urllib.request.Request('https://api.github.com'+path,data=raw,headers=headers)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req,timeout=25) as response:
                data=response.read(4*1024*1024+1)
                if len(data)>4*1024*1024:raise ValueError('Response size limit')
                return json.loads(data) if data else {'http_status':response.status}
        except urllib.error.HTTPError as exc:
            if exc.code not in (429,500,502,503,504) or attempt==2:raise
            time.sleep(min(10,int(exc.headers.get('Retry-After','2'))))
        except (TimeoutError,urllib.error.URLError):
            if attempt==2:raise
            time.sleep(2*(attempt+1))

def file_json(path,ref):
    result=api('/repos/'+REPO+'/contents/'+path+'?ref='+urllib.parse.quote(ref,safe=''))
    if result.get('encoding')!='base64':raise ValueError('Unexpected content encoding')
    return json.loads(base64.b64decode(result['content'])),result['sha']

def evaluate(data, observed=None):
    observed=observed or dt.datetime.now(dt.timezone.utc)
    def elapsed(value):
        try:return (observed-dt.datetime.fromisoformat(value)).total_seconds()
        except (ValueError,TypeError):return float('inf')
    source_age=elapsed(data.get('generated_at'))
    stale=not 0<=source_age<=1200
    inactive=[a['id'] for a in data.get('agents',[]) if not 0<=elapsed(a.get('activity_at'))<=1200]
    problems=[]
    if stale:problems.append('État source périmé, absent ou daté dans le futur')
    if not data.get('tests',{}).get('ok'):problems.append('Tests du harness non confirmés')
    if not data.get('gate',{}).get('allowed'):problems.append('Garde de production fermée')
    if len(data.get('agents',[]))!=4:problems.append('Roster différent de quatre agents')
    if inactive:problems.append('Activité auteur absente ou ancienne: '+', '.join(inactive))
    return {'observed_at':observed.isoformat(),'snapshot_generated_at':data.get('generated_at'),
            'healthy':not problems,'problems':problems,'agents_without_recent_activity':inactive,
            'no_agent_restart':True,'no_main_write':True,'clinical_certification':False}

def observe():
    control,_=file_json('harness/watchdog-control.json',CONTROL_REF)
    data,blob_sha=file_json('harness/status.json',SOURCE_REF)
    result=evaluate(data)
    result.update(enabled=control.get('enabled') is True,source_blob_sha=blob_sha,
                  run_url=f'https://github.com/{REPO}/actions/runs/'+os.environ.get('GITHUB_RUN_ID','local'),
                  interval_seconds=600,continuity='Handoff GitHub Actions; delays and service outages remain possible')
    data['github_observation']=result
    data['monitor']={**data.get('monitor',{}),'independent_watchdog':result}
    atomic(HOME/'remote-observation.json',result)
    atomic(HOME/'remote-status.json',data)
    render(data,HOME/'remote-dashboard.html')
    if dt.datetime.now(dt.timezone.utc)>=dt.datetime.fromisoformat(data['deadline']):
        render({**data,'report_frozen_at':now()},HOME/'rapport-08h00.html')
    summary='## MEDINA — veille indépendante\n\n'+json.dumps(result,ensure_ascii=False,indent=2)+'\n'
    if os.getenv('GITHUB_STEP_SUMMARY'):Path(os.environ['GITHUB_STEP_SUMMARY']).write_text(summary)
    print(json.dumps(result,ensure_ascii=False))
    return 0 if result['healthy'] else 2

def handoff(bootstrap=False):
    # Normal jobs observe, preserve their artifact, then wait without model use.
    # Bootstrap skips this wait once solely to verify an actual successor run.
    if not bootstrap:
        start=float(os.environ.get('WATCHDOG_STARTED_EPOCH',time.time()))
        time.sleep(max(0,600-(time.time()-start)))
    control,_=file_json('harness/watchdog-control.json',CONTROL_REF)
    if control.get('enabled') is not True:
        print(json.dumps({'stopped':True,'reason':'explicit control enabled != true'}));return 0
    response=api('/repos/'+REPO+'/actions/workflows/'+str(WORKFLOW_ID)+'/dispatches',
                 {'ref':CONTROL_REF,'inputs':{'watchdog':'true','bootstrap':'false'}})
    result={'at':now(),'successor_requested':response.get('http_status')==204,'response':response,
            'ref':CONTROL_REF,'interval_seconds':600,'bootstrap':bootstrap}
    atomic(HOME/'remote-handoff.json',result)
    print(json.dumps(result,ensure_ascii=False))
    if not result['successor_requested']:raise ValueError('Successor not acknowledged')
    return 0

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('command',choices=['observe','handoff']);p.add_argument('--bootstrap',action='store_true');a=p.parse_args()
    raise SystemExit(observe() if a.command=='observe' else handoff(a.bootstrap))
