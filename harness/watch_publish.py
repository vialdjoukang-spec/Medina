#!/usr/bin/env python3
"""600s scheduler; isolated Git index, allowlisted outputs, no main/PR writes.

It cannot survive destruction of its host. GitHub's independent cron is pending
default-branch installation. This limitation is persisted in monitor.json.
"""
import argparse
import fcntl
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time
from medina_harness import Harness, atomic, now

BRANCH='codex/harness-observations-20261102'
FILES=['status.json','dashboard.html','rapport-08h00.html','monitor.json',
       'runtime/state.json','runtime/watch.json','runtime/events.jsonl',
       'runtime/tests.json','runtime/tests.log']
CODE_FILES=['medina_harness.py','bracelet.py','github_observe.py','watch_publish.py',
            'catalog.json','config.json','prompt-lock.json','REPARTITION.md','dashboard-template.html','tests/test_harness.py']

def run(root,publisher):
    h=Harness(root)
    # A new interpreter loads the current tested code on every tick.
    subprocess.run([sys.executable,str(h.home/'medina_harness.py'),'--root',str(root),'watch'],check=True,capture_output=True,timeout=90)
    if not h.readiness()['allowed']:raise ValueError('Harness fermé; conserver les erreurs localement avant publication du candidat')
    actual=subprocess.check_output(['git','-C',str(publisher),'branch','--show-current'],text=True).strip()
    if actual!=BRANCH:raise ValueError('Branche de publication non autorisée')
    staged=[]
    for name in FILES+CODE_FILES:
        src=h.home/name
        if src.exists():
            dest=publisher/'harness'/name;dest.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(src,dest);staged.append('harness/'+name)
    subprocess.run(['git','-C',str(publisher),'add','--',*staged],check=True,capture_output=True)
    diff=subprocess.run(['git','-C',str(publisher),'diff','--cached','--quiet'])
    if diff.returncode==1:
        subprocess.run(['git','-C',str(publisher),'commit','-m','harness: observation '+now()],check=True,capture_output=True)
    elif diff.returncode:raise ValueError('Diff Git échoué')
    subprocess.run(['git','-C',str(publisher),'push','origin','HEAD:refs/heads/'+BRANCH],check=True,capture_output=True,timeout=60)
    result={'at':now(),'published':True,'branch':BRANCH}
    atomic(h.runtime/'publisher.json',result);return result

def main():
    p=argparse.ArgumentParser();p.add_argument('--root',required=True,type=Path);p.add_argument('--publisher',required=True,type=Path);p.add_argument('--once',action='store_true');a=p.parse_args()
    runtime=a.root/'harness/runtime';runtime.mkdir(exist_ok=True)
    with (runtime/'.publisher.lock').open('a+') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        while True:
            started=time.monotonic()
            try:result=run(a.root,a.publisher)
            except Exception as e:
                result={'at':now(),'published':False,'error':str(e)};atomic(runtime/'publisher.json',result)
            print(json.dumps(result,ensure_ascii=False),flush=True)
            if a.once: return 0 if result['published'] else 2
            time.sleep(max(1,600-(time.monotonic()-started)))

if __name__=='__main__':raise SystemExit(main())
