#!/usr/bin/env python3
"""Jauge d'intégration ALPHA77 Claude : 5 étapes par leçon, lues dans les worktrees (aucun réseau)."""
import os, subprocess, time, json
R='/home/user/medina-taches'; C=['I61','G45','E11','E12','N18','D50','C77']
def st(c):
    d=f'{R}/ALPHA77-CLAUDE-{c}-INTEGRATE-g1'; x=f'{d}/docs/collaboration/ssp-v2/execution/ALPHA77-CLAUDE-{c}-INTEGRATE'
    log=subprocess.run(['git','-C',d,'log','--format=%s','abd681e5..HEAD'],capture_output=True,text=True).stdout
    s=0
    s+=os.path.exists(f'{x}/prep/READY.json')
    s+='Corrections Alpha77' in log
    s+=os.path.isfile(f'{d}/chapters/{c}/{c}_c.html') and f'{c.lower()}-s-semio' in open(f'{d}/chapters/{c}/{c}_c.html').read()
    s+=all(os.path.exists(f'{x}/revue/{k}.json') for k in ('MED','LANG','SEMIO'))
    s+=os.path.isdir(f'{d}/organisation/alpha-publications/Claude/{c}')
    return s
prev=None
while True:
    v={c:st(c) for c in C}
    if v!=prev:
        n=sum(v.values()); w=20; p=round(w*n/35)
        print(f"INTÉGRATION {'🟩'*p}{'⬜'*(w-p)} {n}/35 étapes · "+' '.join(f'{c}:{k}/5' for c,k in v.items())+" (prép · corrections · sémiologie intégrée · revue · reçu)",flush=True)
        try: open('/tmp/claude-0/-home-user-Medina/32d77524-f01f-5b7e-92b4-188dd9e32b87/scratchpad/jauge/integration.txt','w').write(json.dumps({'n':n,'v':v,'maj':time.strftime('%H:%M')}))
        except OSError: pass
        prev=v
        if n==35: break
    time.sleep(60)
