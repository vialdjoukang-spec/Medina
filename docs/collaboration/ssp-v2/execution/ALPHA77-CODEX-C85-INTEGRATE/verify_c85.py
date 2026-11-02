#!/usr/bin/env python3
"""Rebuild and verify C85 without network calls, source edits, push or closure.

Requires the standard Medina build dependencies, Chromium, Playwright and the
common harness worktree. A new medical edit invalidates earlier human/AI reviews.
"""
from pathlib import Path
import datetime
import hashlib
import json
import os
import subprocess
import sys

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[4]
BASE='8a512893acbab9caa0dcfdd0e8682a44ea72fda6'
BUNDLE=Path('/workspace/Medina-harness/harness/bundle_native.py')
def main():
    receipt={'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'code':'C85','checks':[],'clinical_certification':False,'closure':False}
    commands=[
      ('static',[sys.executable,'test_v7.py','--static','C85']),
      ('sciences',[sys.executable,'tests/audit_sciences.py','--base',BASE,'--codes','C85','--out',str(OUT/'sciences-final.json')]),
      ('verite',[sys.executable,'tools/betta_verite.py',str(OUT/'recherche_C85')]),
      ('build',[sys.executable,'build_front.py','--fragment','S06']),
      ('bundle',[sys.executable,str(BUNDLE),str(OUT/'preview/fragments/MEDINA_S06_hematopoietique-lymphatique.html'),str(ROOT),'C85',str(OUT/'C85-apercu-autonome.html')]),
      ('browser',[sys.executable,str(OUT/'browser_probe.py')])]
    for label,command in commands:
        result=subprocess.run(command,cwd=ROOT,env={**os.environ,'MEDINA_OUT':str(OUT/'preview')},capture_output=True,text=True,timeout=240)
        (OUT/(label+'-verification.log')).write_text(result.stdout+result.stderr)
        receipt['checks'].append({'check':label,'exit_code':result.returncode,'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat()})
        if result.returncode:
            (OUT/'verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
            raise SystemExit(label+' failed; inspect its verification log')
    report=json.loads((OUT/'browser-report-autonomous.json').read_text())
    assert not report['errors']
    for view in report['viewports']:
        assert view['book_font']=='24px' and view['book_overflow']==0 and view['horizontal_overflow']==0
        assert view['popup_visible'] and not view['popup_missing']
        assert view['profiles_g2_scoped']
        assert len(view['science_buttons'])==6 and view['semio_sections']==9
        assert len(view['originals_checked'])==4 and all(x['loaded'] for x in view['originals_checked'])
    paths=[*sorted((ROOT/'chapters/C85').glob('*.html')),ROOT/'glossary/c85.py',*sorted((ROOT/'assets/img/c85/alpha/codex').glob('*'))]
    receipt['final_sources']={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths if p.is_file()}
    receipt['preview_sha256']=hashlib.sha256((OUT/'C85-apercu-autonome.html').read_bytes()).hexdigest()
    receipt['finished_at']=datetime.datetime.now(datetime.timezone.utc).isoformat();receipt['ok']=True
    (OUT/'verification.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'ok':True,'checks':len(commands),'preview_sha256':receipt['preview_sha256'],'closure':False}))
if __name__=='__main__':main()
