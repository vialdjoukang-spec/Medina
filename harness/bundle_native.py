#!/usr/bin/env python3
"""Make a review copy of native MEDINA HTML with exact local figure bytes.

Only the selected lesson's allowlisted asset directory is embedded. Native
source, course source and image originals remain untouched. No image editing.
"""
import argparse
import base64
import gzip
import hashlib
import json
import mimetypes
from pathlib import Path
import re

def bundle(native,worktree,code,output):
    if not re.fullmatch(r'[A-Z]\d\d',code):raise ValueError('Invalid lesson code')
    root=Path(worktree).resolve();native=Path(native).resolve();output=Path(output).resolve()
    if not native.is_relative_to(root) or not output.is_relative_to(root):raise ValueError('Review files must stay in the claimed worktree')
    if native==output:raise ValueError('Never overwrite the native build')
    original=native.read_bytes();text=original.decode()
    pattern=r'(<script id="mdn-pack" type="application/octet-stream">)([^<]+)(</script>)'
    match=re.search(pattern,text)
    if not match:raise ValueError('Native template pack missing')
    packed=gzip.decompress(base64.b64decode(match[2])).decode()
    prefix='assets/img/'+code.lower()+'/'
    pattern_img=r'''\bsrc=(["'])(\.\./)?('''+re.escape(prefix)+r'''[^"']+)\1'''
    figures={}
    def embed(m):
        path=(root/m[3]).resolve()
        allowed=(root/prefix).resolve()
        if not path.is_relative_to(allowed) or not path.is_file():raise ValueError('Image outside lesson ownership or absent')
        raw=path.read_bytes()
        if len(raw)>8*1024*1024:raise ValueError('Image exceeds8MiB review budget')
        mime=mimetypes.guess_type(str(path))[0]
        if mime not in ('image/jpeg','image/png','image/webp','image/gif','image/svg+xml'):raise ValueError('Unsupported image type')
        figures[m[3]]={'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'pixels_edited':False}
        return 'src="data:'+mime+';base64,'+base64.b64encode(raw).decode()+'"'
    packed,count=re.subn(pattern_img,embed,packed)
    newpack=base64.b64encode(gzip.compress(packed.encode(),9,mtime=0)).decode()
    text=text[:match.start(2)]+newpack+text[match.end(2):]
    text=text.replace('</head>',f'<script>if(!location.hash)location.hash="#/entry/{code}";</script></head>',1)
    output.parent.mkdir(parents=True,exist_ok=True);output.write_text(text)
    report={'code':code,'source_native_sha256':hashlib.sha256(original).hexdigest(),
            'review_html_sha256':hashlib.sha256(output.read_bytes()).hexdigest(),
            'embedded_occurrences':count,'figures':figures,
            'other_courses':'Inherited system navigation is preserved; this review concerns only '+code,
            'clinical_certification':False,'canonical_modified':False}
    output.with_suffix('.bundle.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    return report

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('native',type=Path);p.add_argument('worktree',type=Path);p.add_argument('code');p.add_argument('output',type=Path);a=p.parse_args()
    print(json.dumps(bundle(a.native,a.worktree,a.code,a.output),ensure_ascii=False,indent=2))
