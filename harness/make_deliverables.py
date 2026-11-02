#!/usr/bin/env python3
"""Index actual local review packages. Does not infer closure or remote upload."""
import hashlib
import json
from pathlib import Path
import subprocess
from urllib.parse import quote
from medina_harness import atomic, now

HERE=Path(__file__).resolve().parent
def main():
    state=json.loads((HERE/'runtime/state.json').read_text())
    completed={x['code']:x for x in state.get('completed_lessons',[])}
    previous=json.loads((HERE/'deliverables.json').read_text()) if (HERE/'deliverables.json').exists() else {}
    indexed={x['code']:x for x in previous.get('lessons',[]) if x['code'] in completed}
    result={'observed_at':now(),'lessons':[],'remote_availability':'Verify branch push separately; a local file does not prove remote availability.'}
    # Completed worktrees remain readable after their author claims another
    # lesson. Refresh their final receipts/HEAD instead of freezing an older
    # index entry from before the last push.
    entries={code:(a['agent'],{**a,'lesson':code}) for code,a in completed.items() if a.get('worktree') and a.get('branch')}
    entries.update({a['lesson']:(agent,a) for agent,a in state['agents'].items() if a.get('lesson')})
    for agent,a in entries.values():
        code=a.get('lesson');root=Path(a.get('worktree','/nonexistent'))
        if not code:continue
        relative=f'docs/collaboration/ssp-v2/execution/ALPHA77-CODEX-{code}-INTEGRATE/{code}-apercu-autonome.html'
        p=root/relative
        head=subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True).strip()
        indexed[code]={'code':code,'agent':agent,'branch':a.get('branch'),'head_observed':head,
          'local_preview':str(p),'exists':p.is_file(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else None,
          'bytes':p.stat().st_size if p.is_file() else None,
          'download_url':'https://raw.githubusercontent.com/vialdjoukang-spec/Medina/'+quote(a['branch'],safe='/')+'/'+relative,
          'branch_url':'https://github.com/vialdjoukang-spec/Medina/tree/'+quote(a['branch'],safe='/'),
          'status':'Version de travail à relire; réserves et clôture à vérifier dans le rapport de la branche.',
          'publication_main':False,'clinical_certification':False}
    for code,item in indexed.items():
        if code in completed:
            item['status']='Achèvement de projet documenté; version en attente de revue utilisateur avant PR main.'
            item['completion']=completed[code]
    result['lessons']=list(indexed.values())
    atomic(HERE/'deliverables.json',result)
    print(json.dumps({'lessons':len(result['lessons']),'existing':sum(x['exists'] for x in result['lessons'])}))
if __name__=='__main__':main()
