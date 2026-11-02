#!/usr/bin/env python3
"""Réduire un ancien checkout propre, en conservant ses preuves et objets Git.

Lecture seule par défaut. --apply exige une clôture enregistrée, tête distante
identique, absence de mission active sur ce worktree et liaison source intacte.
"""
import argparse, datetime as dt, hashlib, json, subprocess, shutil
from pathlib import Path

HOME=Path(__file__).resolve().parents[1]
def git(root,*args):
    return subprocess.check_output(['git','-C',str(root),*args],text=True,timeout=180).strip()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    p=argparse.ArgumentParser();p.add_argument('code');p.add_argument('worktree',type=Path);p.add_argument('--apply',action='store_true');a=p.parse_args()
    root=a.worktree.resolve();state=json.loads((HOME/'runtime/state.json').read_text())
    records=[r for r in state['completed_lessons'] if r['code']==a.code and Path(r['worktree']).resolve()==root]
    assert len(records)==1,'Clôture unique requise'
    assert not any(Path(x['worktree']).resolve()==root and x['stage']!='termine' for x in state['agents'].values()),'Worktree actif'
    assert not git(root,'status','--porcelain'),'Worktree non propre'
    head=git(root,'rev-parse','HEAD');branch=git(root,'branch','--show-current')
    remote=git(root,'ls-remote','origin','refs/heads/'+branch).split()[0];assert head==remote,'Tête distante différente'
    out=root/('docs/collaboration/ssp-v2/execution/ALPHA77-CODEX-'+a.code+'-INTEGRATE')
    binding=json.loads((out/'source-binding.json').read_text())
    assert sha(out/'source-binding.json')==records[0]['source_binding_sha256']
    for n,h in binding['final_sources'].items():assert sha(root/n)==h,n
    assert sha(out/binding['preview'])==binding['preview_sha256']
    protected={str(f.relative_to(root)):sha(f) for f in out.rglob('*') if f.is_file()}
    for n in [*binding['final_sources'],'chapters.json']:
        f=root/n;protected[n]=sha(f)
    patterns=['.medina','tools','tests','organisation','glossary','chapters/'+a.code,'assets/img/'+a.code.lower(),str(out.relative_to(root))]
    record={'at':dt.datetime.now(dt.timezone.utc).isoformat(),'code':a.code,'worktree':str(root),'closed_commit':head,'remote_exact':True,'operation':'reversible_sparse_checkout_of_closed_worktree','apply':a.apply,'protected_sha256':protected,'patterns':patterns,'source_binding_refreshed':False,'active_worktrees_changed':False}
    if a.apply:
        receipt=HOME/'storage'/(a.code+'-sparse-archive.json');assert not receipt.exists(),'Reçu existant conservé'
        before=shutil.disk_usage(root).free
        git(root,'sparse-checkout','set','--cone',*patterns)
        for n,h in protected.items():assert sha(root/n)==h,n
        assert git(root,'rev-parse','HEAD')==head and not git(root,'status','--porcelain')
        record.update(finished_at=dt.datetime.now(dt.timezone.utc).isoformat(),all_protected_unchanged=True,free_bytes_before=before,free_bytes_after=shutil.disk_usage(root).free,restore='git sparse-checkout disable (espace disque suffisant requis)')
        receipt.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in record.items() if k!='protected_sha256'}|{'protected_files':len(protected)},ensure_ascii=False))

if __name__=='__main__':main()
