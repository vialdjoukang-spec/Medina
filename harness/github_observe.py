#!/usr/bin/env python3
"""Read-only observation in Actions. Never turns CI activity into author activity."""
import datetime as dt
import json
import os
from pathlib import Path
from medina_harness import atomic, load, now, age, render

ROOT=Path(__file__).resolve().parent

def observe():
    data=load(ROOT/'status.json')
    stale=age(data['generated_at'])>1200
    inactive=[a['id'] for a in data['agents'] if not a.get('activity_at') or age(a['activity_at'])>1200]
    observation={'observed_at':now(),'run_id':os.getenv('GITHUB_RUN_ID'),
        'run_url':f"https://github.com/{os.getenv('GITHUB_REPOSITORY','vialdjoukang-spec/Medina')}/actions/runs/{os.getenv('GITHUB_RUN_ID','local')}",
        'commit':os.getenv('GITHUB_SHA'),'snapshot_generated_at':data['generated_at'],
        'snapshot_stale':stale,'agents_without_recent_activity':inactive,
        'tests':load(ROOT/'runtime/tests.json',{}),
        'no_native_agent_restart':True,'no_main_write':True,
        'schedule_limit':'Cron natif hors main inactif. Voir monitor.json pour la chaîne indépendante workflow_dispatch et ses preuves; cet événement observe un commit publié.'}
    atomic(ROOT/'github-observation.json',observation)
    data['github_observation']=observation
    data['monitor']={**data.get('monitor',{}),'last_github_observation':observation}
    # Keep source generation time; separate observer timestamp above.
    atomic(ROOT/'status.json',data);render(data,ROOT/'dashboard.html')
    if dt.datetime.now(dt.timezone.utc)>=dt.datetime.fromisoformat(data['deadline']):
        atomic(ROOT/'rapport-08h00.html',(ROOT/'dashboard.html').read_text())
    summary=f"## MEDINA — observation réelle\n\nContrôle : {observation['observed_at']}\n\nDernier état source : {data['generated_at']}\n\nÉtat périmé : {stale}\n\nAgents sans activité récente : {', '.join(inactive) or 'aucun'}\n\nAucune PR, aucune mutation main, aucune validation médicale automatique.\n"
    if os.getenv('GITHUB_STEP_SUMMARY'):
        Path(os.environ['GITHUB_STEP_SUMMARY']).write_text(summary)
    print(json.dumps(observation,ensure_ascii=False))
    if stale or not observation['tests'].get('ok'):return 2
    return 0

if __name__=='__main__':raise SystemExit(observe())
