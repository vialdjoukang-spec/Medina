#!/usr/bin/env python3
"""Standalone draft validator; not an installed application Stop hook."""
import argparse,json,sys,time
from pathlib import Path
try:
 from tools.audit_gauge import TTL,digest,snapshot
except ModuleNotFoundError:
 from audit_gauge import TTL,digest,snapshot

def validate(draft,s,now=None):
 now=time.time() if now is None else now
 if not isinstance(s,dict) or not s:return False,'invalid snapshot'
 age=now-s.get('generated_at',0)
 if not 0<=age<TTL:return False,'stale snapshot'
 payload={k:v for k,v in s.items() if k not in {'snapshot_sha256','receipt_line'}}
 payload['gauge_line']=payload.get('gauge_line','').removesuffix(' '+s.get('receipt_line',''))
 if digest(payload)!=s.get('snapshot_sha256'):return False,'invalid snapshot hash'
 if s.get('receipt_line')!=f'[G:{s["snapshot_sha256"][:8]}:{s.get("nonce")}]':return False,'invalid receipt token'
 lines=draft.splitlines()
 if s.get('gauge_line') not in lines:return False,'missing or outdated gauge line'
 if s.get('receipt_line') not in draft:return False,'missing snapshot nonce/hash'
 if sum(line.startswith('CODEX ') for line in lines)!=1:return False,'ambiguous gauge lines'
 return True,'ok'
def stop_decision(payload,s):
 if not isinstance(payload,dict) or payload.get('hook_event_name')!='Stop':
  return {'decision':'block','reason':'Invalid Stop hook input; repair input before finalizing.'}
 ok,reason=validate(payload.get('last_assistant_message') or '',s)
 if ok:return {}
 prefix='Already continued: repair the final response now. ' if payload.get('stop_hook_active') else ''
 return {'decision':'block','reason':prefix+reason+'. Include these exact current lines in the final response:\n'+s['gauge_line']}
def main():
 p=argparse.ArgumentParser();p.add_argument('draft',nargs='?',help='UTF-8 assistant draft file, or - for raw text stdin');p.add_argument('--root',default=str(Path(__file__).resolve().parents[1]));p.add_argument('--cache',default=str(Path.home()/'.cache/medina-audit-gauge.json'));p.add_argument('--local-snapshot');p.add_argument('--snapshot',help='Previously generated JSON gauge receipt; must still match current cache snapshot')
 p.add_argument('--stop-hook',action='store_true',help='Documented Codex Stop structured stdin adapter')
 a=p.parse_args()
 if not a.stop_hook and not a.draft:p.error('draft is required unless --stop-hook')
 if a.stop_hook:
  try:
   payload=json.load(sys.stdin);current=snapshot(a.root,a.local_snapshot,a.cache)
   result=stop_decision(payload,current)
  except Exception as exc:result={'decision':'block','reason':'Gauge verification failed: '+type(exc).__name__+'. Refresh gauge before finalizing.'}
  print(json.dumps(result,ensure_ascii=False));return 0
 draft=sys.stdin.read() if a.draft=='-' else Path(a.draft).read_text()
 try:
  current=snapshot(a.root,a.local_snapshot,a.cache)
  s=json.loads(Path(a.snapshot).read_text()) if a.snapshot else current
  if s.get('snapshot_sha256')!=current.get('snapshot_sha256'):ok,reason=False,'snapshot differs from current state'
  else:ok,reason=validate(draft,s)
 except (ValueError,OSError,KeyError) as exc:ok,reason=False,str(exc)
 print(json.dumps({'allow':ok,'reason':reason},ensure_ascii=False));return 0 if ok else 2
if __name__=='__main__':sys.exit(main())
