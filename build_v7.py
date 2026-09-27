#!/usr/bin/env python3
"""MEDINA V7 : frontend modernisé autonome + cours + moteur + glossaire."""
import json, glob, re, sys
import os
ROOT=os.environ.get('MEDINA_ROOT',os.path.dirname(os.path.abspath(__file__)))
OUT=os.environ.get('MEDINA_OUT','/mnt/user-data/outputs' if os.path.isdir('/mnt/user-data') else ROOT+'/dist')
sys.path.insert(0,ROOT); sys.path.insert(0,ROOT+'/shell')
import build_medina as B
from data import WAVES, PRIO, DONE_SYS, RENVOIS, NOTES
cfg=json.load(open(ROOT+'/chapters.json'))
chap=[c for c in cfg if c.get('integrated')]
WAVE={c['code']:c.get('wave',1) for c in chap}
WAVE_OF=lambda code: WAVE[code]
body='';words=0;report={}
for c in chap:
    B.COVERS[c['code']]=c['covers']
    src=''.join(open(f).read() for f in sorted(glob.glob(f"{ROOT}/chapters/{c['code']}/*.html")))
    words+=B.words(src)
    src=B.wrap_html(B.pareto_ratios(B.transform(src))); report[c['code']]=B.audit(src,c['code']); body+=src
cov={}
for c in chap: cov[WAVE_OF(c['code'])]=cov.get(WAVE_OF(c['code']),0)+len(c['covers'])
data={'waves':[{'n':n,'title':t,'cat':k,'prio':n in PRIO,'covered':cov.get(n,0)} for n,t,k in WAVES],
 'chapters':[{'code':c['code'],'title':c['title'],'covers':c['covers'],'wave':WAVE_OF(c['code']),'note':NOTES.get(c['code'],'20/20'),'added':c.get('added')} for c in chap],
 'done':sorted(DONE_SYS),'renvois':{str(k):v for k,v in RENVOIS.items()},'words':round(words,-3),'build':max((c.get('added') or '') for c in chap)}
alias={x:c['code'] for c in chap for x in c['covers']}
shell=open(ROOT+'/shell/shell.html').read().replace('__DATA__',json.dumps(data,ensure_ascii=False)).replace('__ECG__',open(ROOT+'/modules/ecg.json').read())
fonts='<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,600;1,7..72,400&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600&family=EB+Garamond:ital,wght@0,400;0,600;1,400&family=Atkinson+Hyperlegible:wght@400;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'
shell=shell.replace('<style>',fonts+'<style>',1).replace('</head>','<style>'+open(ROOT+'/engine/medina_course.css').read()+'</style></head>',1)
tail=body+'<script>window.MEDINA_ALIAS='+json.dumps(alias)+'</script><script id="medina-glossary" type="application/json">'+json.dumps(B.G,ensure_ascii=False).replace('</','<\\/')+'</script><script>'+open(ROOT+'/engine/medina_course.js').read()+'</script>'
shell=shell.replace('<!--COURSES-->',tail)
os.makedirs(OUT,exist_ok=True)
open(OUT+'/MEDINA.html','w').write(shell)
print('taille',len(shell.encode()),'mots',words)
for k,v in report.items():
    if v: print(k,'non couvertes',len(v))
