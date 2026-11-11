from pathlib import Path
import json,os,sys
root=Path(os.environ['A41_CONTROL_ROOT']);sys.path.insert(0,str(root/'tools'))
from insert_justifications import load_course_justifications
loaded=load_course_justifications('A41',root/'chapters/A41');assert loaded is not None
transformed,templates,report=loaded
assert report['entries']==report['windows']==report['targets']==14,report
assert len(transformed)==8
Path(os.environ['A41_CONTROL_REPORTS'],'bank-a41.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
