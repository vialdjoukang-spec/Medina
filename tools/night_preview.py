#!/usr/bin/env python3
"""Aperçu d'une livraison nocturne dans un overlay isolé, sans injection."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys


def build(root, code, output):
    sys.path.insert(0, str(root))
    from tools import build_fragment_work_preview as preview
    lessons = json.loads((root/'organisation/execution-20261014/cahier-cycle2.json').read_text())['lessons']
    lesson = next(x for x in lessons if x['code'] == code)
    source = root/lesson['directory']
    paths = sorted((source/'chapters'/code).glob('*.html')) + [source/'glossary'/f'{code.lower()}.py']
    required = {f'{code}_{s}.html' for s in ('a','b','c','d','pop1','pop2')}
    if not required.issubset({p.name for p in paths}) or not all(p.is_file() for p in paths):
        raise ValueError('La livraison ne contient pas encore les six HTML et le glossaire.')
    files = {p.relative_to(source).as_posix():p.read_bytes() for p in paths}
    manifest = {'chapter_codes':[code], 'chapters':[{'code':code,'covers':[code],'title':lesson['title'],'production_cycle':2}],
                'source_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip()}
    output.mkdir(parents=True,exist_ok=True)
    overlay = output/'overlay'
    if overlay.exists(): shutil.rmtree(overlay)
    preview.FRAGMENT = lesson['system']
    preview.create_overlay(root, files, manifest, overlay)
    # The existing helper links assets. Replace that link before adding images.
    asset_link = overlay/'assets'
    if not asset_link.is_symlink(): raise ValueError('Lien assets inattendu ; refus de copie.')
    asset_link.unlink()
    shutil.copytree(root/'assets',asset_link)
    image_root = source/'assets'
    if image_root.exists(): shutil.copytree(image_root,asset_link,dirs_exist_ok=True)
    built = output/'built'
    env = dict(os.environ,MEDINA_ROOT=str(overlay.resolve()),MEDINA_OUT=str(built.resolve()))
    run = subprocess.run([sys.executable,str(overlay/'build_front.py'),'--fragment',lesson['system']],env=env,cwd=overlay,capture_output=True,text=True)
    (output/'build.log').write_text(run.stdout+'\n'+run.stderr)
    if run.returncode: raise RuntimeError('Construction échouée ; consulter build.log')
    htmls = list((built/'fragments').glob('*.html'))
    if len(htmls)!=1: raise RuntimeError('Un seul frontend attendu.')
    html = htmls[0]
    content = html.read_text()
    banner = '<aside role="note" style="padding:12px;background:#fff;border:2px solid #b3261e;color:#111">Version de travail — '+code+' — sources non injectées, audits en cours.</aside>'
    content = content.replace('<body>', '<body>'+banner,1)
    html.write_text(content)
    # Relative <img src="assets/…"> resolves identically under fragment hosting.
    dest = html.parent/'assets'
    if dest.exists(): shutil.rmtree(dest)
    shutil.copytree(asset_link,dest)
    report = {'code':code,'canonical_injection':False,'html':str(html.resolve()),'source_files':{p:hashlib.sha256(b).hexdigest() for p,b in files.items()},'build_exit':run.returncode}
    (output/'preview.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False))
    return report

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('code');parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();build(Path(__file__).resolve().parents[1],args.code,args.output.resolve())
