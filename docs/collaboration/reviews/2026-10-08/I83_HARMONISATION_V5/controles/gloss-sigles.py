from pathlib import Path
import json,os,sys
root=Path(os.environ['I83_CONTROL_ROOT'])
compile((root/'glossary/i83.py').read_text(),str(root/'glossary/i83.py'),'exec')
sys.path.insert(0,str(root))
import build_medina as B
src=''.join(p.read_text() for p in sorted((root/'chapters/I83').glob('*.html')))
missing=B.audit(B.wrap_html(B.transform(src)),'I83')
report={'result':'passed' if not missing else 'failed','syntax_compile':True,'uncovered_sigles':missing,'runtime_glossary_keys':len(B.G)}
Path(os.environ['I83_CONTROL_REPORTS'],'gloss-sigles.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False));assert not missing,missing
