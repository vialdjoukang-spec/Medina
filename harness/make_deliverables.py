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
    result={'observed_at':now(),'lessons':[],'remote_availability':'Verify branch push separately; a local file does not prove remote availability.'}
    for agent,a in state['agents'].items():
        code=a.get('lesson');root=Path(a.get('worktree','/nonexistent'))
        if not code:continue
        relative=f'docs/collaboration/ssp-v2/execution/ALPHA77-CODEX-{code}-INTEGRATE/{code}-apercu-autonome.html'
        p=root/relative
        head=subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True).strip()
        result['lessons'].append({'code':code,'agent':agent,'branch':a.get('branch'),'head_observed':head,
          'local_preview':str(p),'exists':p.is_file(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else None,
          'bytes':p.stat().st_size if p.is_file() else None,
          'download_url':'https://raw.githubusercontent.com/vialdjoukang-spec/Medina/'+quote(a['branch'],safe='/')+'/'+relative,
          'branch_url':'https://github.com/vialdjoukang-spec/Medina/tree/'+quote(a['branch'],safe='/'),
          'status':'Version de travail à relire; réserves et clôture à vérifier dans le rapport de la branche.',
          'publication_main':False,'clinical_certification':False})
    atomic(HERE/'deliverables.json',result)
    print(json.dumps({'lessons':len(result['lessons']),'existing':sum(x['exists'] for x in result['lessons'])}))
if __name__=='__main__':main()
