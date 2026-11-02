from pathlib import Path
import re,json,hashlib,subprocess,datetime,runpy
R=Path.cwd();D=R/'docs/collaboration/ssp-v2/execution/ALPHA77-CODEX-E00-INTEGRATE';P=R/'chapters/E00';files=sorted(P.glob('*.html'));s='\n'.join(f.read_text() for f in files)
ids=re.findall(r'\bid="([^"]+)"',s);duplicates=sorted({x for x in ids if ids.count(x)>1});assert not duplicates,duplicates
keys=set(re.findall(r'\bdata-k="([^"]+)"',s));templates=re.findall(r'\bdata-pop="([^"]+)"',s);assert len(templates)==len(set(templates));missing=sorted(keys-set(templates));assert not missing,missing
cover=[x for a in re.findall(r'data-cover="([^"]+)"',s) for x in a.split(',')];assert set(cover)<=set(ids)
assert all(x in ids for x in ['pA','pE','pS','pP'])
assert len(re.findall(r'\bdata-semiology="',s))==9
assert all(m in s for m in ['normal','signs','mechanisms','examination','interpretation','differentials','urgency','limits','sources'])
imgs=re.findall(r'<img[^>]*src="([^"]+)"',s);assert len(imgs)==2
for f in imgs:assert (R/f).is_file()
actual=hashlib.sha256((R/imgs[0]).read_bytes()).hexdigest();assert actual=='f956a9fc58ca589ebfd91ee889a9686ddaaac32001b53fa03f6b7ed5b4640138'
assert not re.search(r'(diminuée|diminue) (?:jusqu’à|à) 20',s)
base='8a512893acbab9caa0dcfdd0e8682a44ea72fda6'
old=''.join(subprocess.run(['git','show',base+':'+str(f.relative_to(R))],capture_output=True,text=True,check=True).stdout for f in files)
word=lambda t:len(re.findall(r"\b[\wÀ-ÿ]+(?:[’'-][\wÀ-ÿ]+)*\b",re.sub('<[^>]+>',' ',t)))
assert word(s)>word(old)
report={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'result':'passed','base_sha':base,'source_html_files':len(files),'unique_ids':len(ids),'popups':len(templates),'popup_references':len(keys),'missing_popup_keys':missing,'pareto_targets':len(set(cover)),'before_words_all_surfaces':word(old),'after_words_all_surfaces':word(s),'image_occurrences':len(imgs),'unique_original_image_sha256':actual,'source_sha256':{str(f.relative_to(R)):hashlib.sha256(f.read_bytes()).hexdigest() for f in files},'limitations':'Static contract and source consistency; not independent clinical review or certification.'}
(D/'static-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False,indent=2))
