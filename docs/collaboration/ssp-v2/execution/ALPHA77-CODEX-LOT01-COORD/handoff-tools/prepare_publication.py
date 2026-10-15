#!/usr/bin/env python3
"""Operational Alpha preparation; never edits canonical courses or audit reports.
Normalisation preserves original evidence bytes and records the exact prior report.
No commit, push, network request, audit assertion, or receipt write is automatic.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse, copy, hashlib, json, re, subprocess, sys
REPO=Path('/workspace/Medina-audit-gauge')
sys.path.insert(0,str(REPO))
from tools import alpha_publication as A
from tools.espace import GitTree
BASE='3131a5cbf6cc003ead358e25152073959c53c4d9'
CODES=['I63','G01','E10','E05','N17','D69','D64']
SCRATCH=Path('/workspace/scratch/reprise-publication')
def digest(raw): return hashlib.sha256(raw).hexdigest()
def readj(p):return json.loads(p.read_bytes())
def write(p,raw):
 p.parent.mkdir(parents=True,exist_ok=True)
 if p.exists() and p.read_bytes()!=raw:raise ValueError('Refusing overwrite of different evidence: '+str(p))
 if not p.exists():p.write_bytes(raw)
def writej(p,obj):write(p,(json.dumps(obj,ensure_ascii=False,indent=2)+'\n').encode())
def root_for(code):return Path('/workspace/medina-alpha77')/code
def evidence_dir(root,code):return root/f'docs/collaboration/ssp-v2/execution/ALPHA77-CODEX-{code}-INTEGRATE'
class LocalTree:
 def __init__(self,root):self.root=root
 def read(self,path,required=True):
  p=self.root/path
  if not p.exists() and not required:return None
  return p.read_bytes()
def reference(root,path):return {'path':str(path.relative_to(root)),'sha256':digest(path.read_bytes())}
def captions(root,code):
 result=[]
 for path in sorted(A.core_paths(code)):
  if path.endswith('.html'):
   result += [A.visible_text(x) for x in re.findall(rb'<figcaption\b[^>]*>(.*?)</figcaption>',(root/path).read_bytes(),re.I|re.S)]
 return result
def matching_caption(root,code,token):
 matches=[c for c in captions(root,code) if token in c]
 if not matches:raise ValueError(f'{code}: no visible caption for {token}')
 return matches[0]
def copy_original(root,dest,source):
 target=dest/source.name;write(target,source.read_bytes());return reference(root,target)
def derived(root,code,target,provenance,page,source_url,license_url,author,credit,quote,retrieved,observations,license_name,original_url,original_sha):
 """Only values already present in author evidence or its retained raw source."""
 d=evidence_dir(root,code);ev=d/'publication-evidence'/Path(target).name
 page=Path(page);raw=page.read_bytes();text=raw.decode('utf-8',errors='replace')
 assert author in text and credit in text and quote in text,(code,target,'source passage mismatch')
 assert original_sha==digest((root/target).read_bytes()),(code,target,'original asset hash mismatch')
 source_ref=copy_original(root,ev,page)
 rights=dict(schema_version=1,actor='Codex',code=code,original_url=original_url,source_url=source_url,
  license_url=license_url,original_sha256=original_sha,author=author,credit=credit,retrieved_at=retrieved,
  license_quote=quote,transformed=False,ai_generated=False,license_verified=True,
  source_page=source_ref,license_page=source_ref,
  normalization={'prior_evidence':reference(root,provenance),'method':'Exact downloaded original retained; author observations transcribed without a new medical-review claim.'})
 rp=ev/'rights.json';writej(rp,rights)
 visual=dict(schema_version=1,actor='Codex',code=code,asset_sha256=original_sha,status='reviewed',
  medical_human_validation=False,anatomy_ai_generated=False,license_verified=True,
  medical_observations=observations,normalization={'prior_evidence':reference(root,provenance),'new_visual_inspection_claimed':False})
 vp=ev/'visual.json';writej(vp,visual)
 return dict(original_url=original_url,source_url=source_url,license_url=license_url,
  original_sha256=original_sha,license=license_name,attribution=matching_caption(root,code,credit),ai_generated=False,
  rights_evidence=reference(root,rp),visual_review_report=str(vp.relative_to(root)),visual_review_sha256=digest(vp.read_bytes()))
def existing(root,code,target,fig):
 d=evidence_dir(root,code);ev=d/'publication-evidence'/Path(target).name
 rights_path=root/fig['rights_evidence']['path'];rights=readj(rights_path)
 # Retain full raw originals instead of author-generated source excerpts where available.
 full={'N17':{'OpenStax-2618-nephron.jpg':Path('/workspace/scratch/alpha77-n17/figure4-page.html'),
 'case2018-figure1.jpg':Path('/workspace/scratch/alpha77-n17/INT-histo-case.xml')}}
 rawfull=full.get(code,{}).get(Path(target).name)
 if rawfull:
  ref=copy_original(root,ev,rawfull);rights['source_page']=ref;rights['license_page']=ref
  if 'OpenStax' in target:rights['license_quote']='Attribution 3.0 Unported'
 else:
  for key in ['source_page','license_page']:
   rights[key]=copy_original(root,ev,root/rights[key]['path'])
 rights['normalization']={'prior_evidence':reference(root,rights_path),'original_documents_preserved':True}
 rp=ev/'rights.json';writej(rp,rights)
 vp=ev/'visual.json';write(vp,(root/fig['visual_review_report']).read_bytes())
 out=copy.deepcopy(fig);out.update(rights_evidence=reference(root,rp),visual_review_report=str(vp.relative_to(root)),visual_review_sha256=digest(vp.read_bytes()))
 return out

def normalize(code):
 root=root_for(code);d=evidence_dir(root,code);figs={}
 if code=='E05':
  for target,fig in readj(d/'figures.json')['figures'].items():figs[target]=existing(root,code,target,fig)
 elif code=='D69':
  target='assets/img/d69/alpha/codex/purpura-hektor.jpg';figs[target]=existing(root,code,target,readj(d/'figure-purpura.json'))
 elif code=='N17':
  for row in readj(d/'figures-provenance.json')['figures']:
   name='openstax' if 'OpenStax' in row['asset'] else 'case2018';rp=d/f'rights/{name}-rights.json';vp=d/f'rights/{name}-visual.json'
   fig=dict(original_url=row['original_url'],source_url=row['source_page'],license_url=row['license_url'],original_sha256=row['original_sha256'],license=row['license'],attribution=matching_caption(root,code,readj(rp)['credit']),ai_generated=False,rights_evidence=reference(root,rp),visual_review_report=str(vp.relative_to(root)),visual_review_sha256=digest(vp.read_bytes()))
   figs[row['asset']]=existing(root,code,row['asset'],fig)
 elif code in ['I63','G01']:
  pp=d/('figure5-provenance.json' if code=='I63' else 'figure3-provenance.json');p=readj(pp)
  page='/workspace/scratch/alpha77-i63/GRAY.html' if code=='I63' else '/workspace/scratch/g01-integration-sources/FIG-PAGE.raw'
  # Dates transcribed from original retrieval records, never inferred from filesystem time.
  date=readj(d/'figure5-finder.json')['retrieved_at'] if code=='I63' else next(x['retrieved_at'] for x in readj(Path('/workspace/scratch/g01-integration-sources/retrieval.json')) if x['id']=='FIG-PAGE')
  figs[p['asset']]=derived(root,code,p['asset'],pp,page,p['source_page'],p.get('license_url',p.get('license_mark_url')),'Henry Vandyke Carter','Henry Vandyke Carter','life plus 100 years or fewer',date,p['visual_review']['observed'],'Public domain',p['original_url'],p['original_sha256'])
 elif code=='E10':
  pp=d/'figures-provenance.json';p=next(x for x in readj(pp)['figures'] if '/alpha/codex/' in x.get('asset',''));acq=readj(d/'figure8-original-acquisition.json')
  figs[p['asset']]=derived(root,code,p['asset'],pp,'/workspace/scratch/E10-integrate-sources/PMC8656040.xml',p['original_publication'],'https://creativecommons.org/licenses/by/4.0/','Kolb','Kolb','This article is licensed under a Creative Commons Attribution 4.0 International License',acq['acquired_at'],p['visual_review']['observations'],'CC BY 4.0',p['original_url'],p['asset_sha256'])
 elif code=='D64':
  pp=d/'figures-provenance.json';index={x['id']:x for x in readj(Path('/workspace/scratch/D64-integrate-sources/acquisition-index.json'))}
  for p in readj(pp)['figures']:
   sid=p['source_id'];item=index[sid];author={'S11':'Roy','S8':'Lours','REG':'Tomc'}[sid]
   quote='This is an open access article under the terms of the' if sid=='S11' else 'This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license'
   figs[p['asset']]=derived(root,code,p['asset'],pp,f'/workspace/scratch/D64-integrate-sources/{sid}.xml',item['url'],'https://creativecommons.org/licenses/by/4.0/',author,author,quote,item['acquired_at'],p['visual_review']['observations'],'CC BY 4.0',p['original_url'],p['sha256'])
 else:raise ValueError(code)
 mission=str(d.relative_to(root));tree=LocalTree(root)
 for target,fig in figs.items():
  A.figure_rights(tree,fig,tree.read(target),'Codex',code,[mission])
  visual=readj(root/fig['visual_review_report'])
  assert visual['asset_sha256']==digest(tree.read(target)) and visual['status']=='reviewed' and visual['medical_human_validation'] is False and visual['anatomy_ai_generated'] is False and visual['license_verified'] is True and visual['medical_observations']
  assert any(fig['attribution'] in c for c in captions(root,code))
 writej(d/'publication-evidence'/'figures.json',{'schema_version':1,'actor':'Codex','code':code,'figures':figs,'medical_human_validation':False})
 return {'code':code,'normalized_assets':len(figs),'rights_check':'passed','canonical_assets_transformed':False}

def snapshot(code):
 root=root_for(code);d=evidence_dir(root,code);figs=readj(d/'publication-evidence'/'figures.json')['figures'];targets=sorted(A.core_paths(code)|set(figs))
 base=GitTree(root,BASE);anchor=GitTree(root,A.HISTORICAL_ANCHOR);files={}
 for target in targets:
  old=base.read(target,required=False);assert old==anchor.read(target,required=False),(target,'base differs historical anchor')
  raw=(root/target).read_bytes();out=d/'publication-snapshot'/target;write(out,raw)
  ref=dict(source_path=str(out.relative_to(root)),sha256=digest(raw),previous_sha256=digest(old) if old is not None else None)
  if target in figs:ref['figure']=figs[target]
  files[target]=ref
 plan={'schema_version':1,'code':code,'actor':'Codex','mission':f'ALPHA77-CODEX-{code}-INTEGRATE','base_commit':BASE,'files':files,'medical_human_validation':False}
 writej(d/'publication-evidence'/'files.json',plan)
 return {'code':code,'snapshot_files':len(files),'base_matches_historical_anchor':True}

def inspect(code):
 root=root_for(code);d=evidence_dir(root,code);base=GitTree(root,BASE);anchor=GitTree(root,A.HISTORICAL_ANCHOR)
 paths=sorted(A.core_paths(code)|{str(p.relative_to(root)) for p in (root/f'assets/img/{code.lower()}/alpha/codex').glob('*') if p.is_file()})
 return {'code':code,'base_matches_historical_anchor':all(base.read(p,required=False)==anchor.read(p,required=False) for p in paths),
 'source_files_sha256':{p:digest(base.read(p)) for p in sorted(A.core_paths(code))},'reviewed_files_sha256':{p:digest((root/p).read_bytes()) for p in paths},
 'normalized_evidence_exists':(d/'publication-evidence'/'figures.json').exists()}

def verify(code,before,after):
 root=root_for(code);old=GitTree(root,before);new=GitTree(root,after);hb,ha,metadata=A.views(old,new)
 from tools.publication_en_etat import adopted_codes as legacy_verify
 # The same immutable original course bytes are projected for the historical guard.
 legacy_verify(hb);legacy_verify(ha)
 return {'code':code,'before':before,'after':after,'alpha_publications':metadata,'historical_publication_check':'passed'}

def receipt(code,proof_commit,phase,write_receipt=False):
 root=root_for(code);d=evidence_dir(root,code);mission=str(d.relative_to(root))
 source=GitTree(root,proof_commit);base=GitTree(root,BASE)
 A.ancestor(root,BASE,proof_commit)
 plan=A.load(source,mission+'/publication-evidence/files.json');files=plan['files']
 outputs={p:r['sha256'] for p,r in files.items()}
 assert all(digest(source.read(p))==sha for p,sha in outputs.items()),'Committed canonical files differ from snapshot'
 initial={p:digest(base.read(p)) for p in sorted(A.core_paths(code))}
 html_content=b''.join(source.read(files[p]['source_path']) for p in sorted(A.core_paths(code)) if p.endswith('.html'))
 visible=A.visible_text(html_content)
 proofs={};blockers=[]
 for kind in ['MED','LANG','SEMIO']:
  path=mission+'/'+kind+'.json';raw=source.read(path);report=json.loads(raw)
  assert report['actor']=='Codex' and report['code']==code and report['kind']==kind
  assert report['source_files_sha256']==initial and report['reviewed_files_sha256']==outputs,kind+' final bindings differ'
  assert report['medical_human_validation'] is False
  if kind!='SEMIO' or phase=='completed':
   assert report['status']==('closed' if phase=='completed' else 'provisional'),kind+' phase differs'
  assert isinstance(report['unresolved_blockers'],list) and isinstance(report['findings'],list) and report['evidence']
  if phase=='completed':assert not report['unresolved_blockers']
  for b in report['unresolved_blockers']:
   assert isinstance(b,str) and b in visible,(kind,'invisible blocker',b)
   if b not in blockers:blockers.append(b)
  if phase=='completed':
   assert all(f['status'] in ['resolved','non_blocking'] and f['evidence'] for f in report['findings'])
  if kind=='SEMIO':assert report['requirement']=='fundamental_analytical_semiology'
  proofs[kind]={'path':path,'sha256':digest(raw)}
 if phase=='provisional':assert blockers,'No visible reservation recorded by audits'
 allocation=[x for x in A.load(base,A.PLAN)['audit']+A.load(base,A.PLAN)['production'] if x['code']==code]
 assert len(allocation)==1 and allocation[0]['owner']=='Codex'
 for path,ref in files.items():
  assert digest(source.read(ref['source_path']))==ref['sha256']
  assert ref['previous_sha256']==(digest(base.read(path)) if base.read(path,required=False) is not None else None)
  if path.startswith('assets/'):
   A.figure_rights(source,ref['figure'],source.read(ref['source_path']),'Codex',code,[mission])
 result=dict(schema_version=1,actor='Codex',code=code,fragment=allocation[0]['fragment'],mission='ALPHA77-CODEX-'+code+'-INTEGRATE',
  phase=phase,base_commit=BASE,source_commit=proof_commit,previous_receipt_sha256=None,
  medical_human_validation=False,files=files,audits=proofs)
 if phase=='provisional':result['visible_reservations']=blockers
 path=root/f'organisation/alpha-publications/Codex/{code}/0001.json' if write_receipt else SCRATCH/f'{code}-receipt-draft.json'
 writej(path,result)
 return {'code':code,'receipt':str(path),'source_commit':proof_commit,'phase':phase,'files':len(files),'written_to_repository':write_receipt}

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('action',choices=['inspect','normalize','snapshot','verify','receipt']);ap.add_argument('--code',choices=CODES,required=True);ap.add_argument('--code-stable',action='store_true',help='Use only after root has confirmed CODE_STABLE for this code');ap.add_argument('--proof-commit');ap.add_argument('--phase',choices=['provisional','completed'],default='provisional');ap.add_argument('--write-receipt',action='store_true');ap.add_argument('--final-reports-ready',action='store_true',help='Only after explicit root instruction and proof commit supplied');ap.add_argument('--before');ap.add_argument('--after',default='HEAD');args=ap.parse_args()
 if args.action in ['normalize','snapshot'] and not args.code_stable:ap.error('Root CODE_STABLE confirmation required for writes')
 if args.action=='receipt' and (not args.final_reports_ready or not args.proof_commit):ap.error('Receipt requires explicit root FINALREPORTSREADY and immutable proof commit')
 result={'receipt':lambda:receipt(args.code,args.proof_commit,args.phase,args.write_receipt),'inspect':lambda:inspect(args.code),'normalize':lambda:normalize(args.code),'snapshot':lambda:snapshot(args.code),'verify':lambda:verify(args.code,args.before,args.after)}[args.action]()
 print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
