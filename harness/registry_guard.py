#!/usr/bin/env python3
"""Run the existing reservation guard with an isolated fetched Git reference.

All trusted-base, mission, scope, generation and compare-and-swap checks stay in
the repository guard. Only its FETCH_HEAD transport is replaced: Git worktrees
share FETCH_HEAD, so simultaneous readers can otherwise observe another fetch.
"""
import importlib.util
from pathlib import Path
import sys
import uuid

def isolated_fetch(guard, root, remote, cfg):
    guard.require(isinstance(remote,str) and guard.re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*',remote),'Use a configured Git remote name')
    reference='refs/medina/harness-observations/'+uuid.uuid4().hex
    try:
        guard.git(root,'fetch','--no-tags','--no-write-fetch-head',remote,cfg['registry_ref']+':'+reference)
        revision=guard.git(root,'rev-parse',reference+'^{commit}').decode().strip()
        return guard.commit(root,revision)
    finally:
        # This UUID reference belongs only to this process. No branch is deleted.
        guard.git(root,'update-ref','-d',reference,optional=True)

def main(argv=None):
    args=list(sys.argv[1:] if argv is None else argv)
    root=Path('.')
    if '--root' in args:
        at=args.index('--root')
        if at+1>=len(args):raise SystemExit('--root requires a worktree')
        root=Path(args[at+1])
    path=root.resolve()/'tools/ai_session_guard.py'
    spec=importlib.util.spec_from_file_location('medina_original_reservation_guard',path)
    guard=importlib.util.module_from_spec(spec);spec.loader.exec_module(guard)
    guard.fetch_registry=lambda task_root,remote,cfg:isolated_fetch(guard,task_root,remote,cfg)
    return guard.main(args)

if __name__=='__main__':raise SystemExit(main())
