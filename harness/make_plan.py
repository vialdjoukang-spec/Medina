#!/usr/bin/env python3
"""Render a complete planning inventory without claiming historical tasks ran."""
import json
from pathlib import Path
from medina_harness import atomic,digest,now
ROOT=Path(__file__).resolve().parent.parent
source=ROOT/'docs/collaboration/ssp-v2/2026-10-15/plan-v2.json'
plan=json.loads(source.read_text());config=json.loads((ROOT/'harness/config.json').read_text())
rows=[]
for kind in ('audit','production','reserve'):
    for item in plan[kind]:
        rows.append({k:item.get(k) for k in ('code','title','fragment','system','owner','subcodes','priority','ssp_documented')}|{'historical_mode':kind,'historical_status':item.get('status'),'live_completion':'not_inferred_from_plan'})
systems=[]
for spec in config['agents']:
    source_system=next(x for x in plan['systems'] if x['id']==spec['system'])
    lessons=[x for x in rows if x['fragment']==spec['system']]
    names={x['code']:x['title'] for x in lessons}
    systems.append({'id':spec['system'],'name':source_system['name'],'agent':spec['id'],
        'historical_existing':source_system['audit_count'],'historical_new_targets':source_system['production_count'],
        'conservative_target':source_system['conservative_categories'],'reserve_count':source_system['reserve_count'],
        'current_queue':[{'order':i,'code':c,'title':names.get(c,c),'reservation':'must_recheck_before_acquisition'} for i,c in enumerate(spec['queue'],1)],
        'reserved_elsewhere':spec['reserved_elsewhere'],'all_planned_lessons':lessons})
result={'generated_at':now(),'source_path':str(source.relative_to(ROOT)),'source_sha256':digest(source.read_bytes()),
    'source_snapshot':'2026-10-15; historical plan, not current completion or live reservation proof',
    'scope':'Four requested systems; existing ownership and remote leases preserved',
    'totals':plan['totals'],'systems':systems,
    'advance_rule':'One lesson per specialty; move only after monographic coverage and required reviews. Refresh remote registry before acquiring the next lesson.',
    'shared_writes':'Only a separately reserved integration after user review; never parallel writes into the same files.',
    'durations':'No delivery dates invented for unstarted lessons; actual throughput tracked separately.'}
atomic(ROOT/'harness/plan.json',result)
print(json.dumps({'systems':len(systems),'planned_records':len(rows),'queue_records':sum(len(x['current_queue']) for x in systems)}))
