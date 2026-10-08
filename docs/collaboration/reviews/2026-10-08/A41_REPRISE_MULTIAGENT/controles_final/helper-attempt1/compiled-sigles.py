from pathlib import Path
import json,os,sys,hashlib
root=Path(os.environ['A41_CONTROL_ROOT']);sys.path.insert(0,str(root));import build_medina as B
loaded=B.load_course_justifications('A41',root/'chapters/A41');assert loaded is not None
transformed,templates,bank=loaded;assert bank['entries']==bank['windows']==bank['targets']==14
config=next(c for c in json.loads((root/'chapters.json').read_text()) if c['code']=='A41')
ordered=[Path(f).name for f in config['files']]
assert set(ordered)==set(transformed)
compiled=B.wrap_html(B.pareto_ratios(B.transform(''.join(transformed[name] for name in ordered)+templates)))
missing=B.audit(compiled,'A41')
report={'result':'passed' if not missing else 'failed','scope':'All eight authored HTML files after canonical justification insertion, transformation, Pareto filling and glossary wrapping; includes all14 generated justification templates','ordered_files':ordered,'justification_report':bank,'uncovered_sigles':missing,'runtime_glossary_keys':len(B.G),'compiled_bytes':len(compiled.encode()),'compiled_sha256':hashlib.sha256(compiled.encode()).hexdigest()}
Path(os.environ['A41_CONTROL_REPORTS'],'compiled-sigles.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False));assert not missing,missing
