#!/usr/bin/env python3
"""Recalcule l'état de la jauge Alpha77 depuis GitHub : branche de leçon = en cours, PR ouverte = auditée,
PR fusionnée = publiée ; session A ou B lue dans la ligne Claude-Session du dernier commit."""
import json, subprocess, urllib.request, datetime, sys
from pathlib import Path
J = Path(__file__).parent; REPO = '/home/user/Medina'; A = 'session_015STHmuYWNmuSZzRgs2rHdW'
e = json.loads((J/'etat.json').read_text())
heads = {}
for line in subprocess.run(['git','-C',REPO,'ls-remote','origin','refs/heads/claude/alpha77/*-integrate-g1'],capture_output=True,text=True).stdout.splitlines():
    sha, ref = line.split('\t'); heads[ref.split('/')[-1].split('-')[0].upper()] = sha
prs = {}
for page in (1, 2, 3):
    req = urllib.request.Request(f'https://api.github.com/repos/vialdjoukang-spec/Medina/pulls?state=all&per_page=100&page={page}&sort=created&direction=desc',headers={'User-Agent':'medina-jauge'})
    for p in json.load(urllib.request.urlopen(req, timeout=30)):
        ref = p['head']['ref']
        if ref.startswith('claude/alpha77/') and ref.endswith('-integrate-g1'):
            c = ref.split('/')[-1].split('-')[0].upper()
            if c not in prs or p['merged_at']: prs[c] = p
subprocess.run(['git','-C',REPO,'fetch','-q','origin']+[f'refs/heads/claude/alpha77/{c.lower()}-integrate-g1' for c in heads],capture_output=True)
for l in e['lecons']:
    c = l['code']; p = prs.get(c)
    if c in heads:
        msg = subprocess.run(['git','-C',REPO,'log','-1','--format=%B',heads[c]],capture_output=True,text=True).stdout
        if 'Claude-Session' in msg: l['session'] = 'A' if A in msg else 'B'
    if p and p.get('merged_at'): l['phase'] = 'publie'; l['pr'] = p['number']
    elif p and p['state'] == 'open': l['phase'] = 'audite'; l['pr'] = p['number']
    elif c in heads and l['phase'] != 'publie': l['phase'] = 'en_cours'
for c in sys.argv[1:]:  # codes lancés mais sans branche encore
    for l in e['lecons']:
        if l['code'] == c and l['phase'] == 'a_faire': l['phase'] = 'en_cours'; l.setdefault('session', 'A')
e['maj'] = (datetime.datetime.utcnow()+datetime.timedelta(hours=2)).strftime('%d.%m.%Y %H:%M')
n = lambda ph: sum(l['phase']==ph for l in e['lecons'])
e['note'] = f"sessions A et B · {n('en_cours')} en cours · {n('audite')} PR à fusionner"
(J/'etat.json').write_text(json.dumps(e, ensure_ascii=False))
print(e['note'], '| publiées', n('publie'))
