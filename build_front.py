#!/usr/bin/env python3
"""Construit MEDINA.html sur le front-end d'origine (shell/medina_front.html) + cours + moteur + glossaire + embellissement + atlas ECG."""
import os,sys,json,glob
ROOT=os.environ.get('MEDINA_ROOT',os.path.dirname(os.path.abspath(__file__)))
OUT=os.environ.get('MEDINA_OUT','/mnt/user-data/outputs' if os.path.isdir('/mnt/user-data') else ROOT+'/dist')
os.environ['MEDINA_V6']=ROOT+'/shell/medina_front.html'
sys.path.insert(0,ROOT);sys.path.insert(0,ROOT+'/shell')
import build_medina as B
from data import WAVES,DONE_SYS,DONE_COURSES,PRIO,PLAN
cfg=json.load(open(ROOT+'/chapters.json'))
chap=[c for c in cfg if c.get('integrated')]
for c in cfg: B.COVERS[c['code']]=c.get('covers',[c['code']])
chapters=[(c['code'],sorted(glob.glob(f"{ROOT}/chapters/{c['code']}/*.html"))) for c in chap]
os.makedirs(OUT,exist_ok=True);out=OUT+'/MEDINA.html'
rep,size=B.build(chapters,out)
build=max(c.get('added','') or '' for c in chap)
CAT={}
for k in 'normal tachy brady fa flutter tsv'.split():CAT[k]='Rythme'
for k in 'bav1 mobitz1 mobitz2 bav3 bbg bbd wpw'.split():CAT[k]='Conduction'
for k in 'stemi sousST pericard hyperk hypok qtl brugada'.split():CAT[k]='Ischémie et repolarisation'
for k in 'esv tv tdp fv'.split():CAT[k]='Arythmies ventriculaires'
# Couverture : catégories CIM distinctes (union des covers), 100 % pour un système achevé (cours + renvois).
sysd=[]
for n,t,k in WAVES:
    courses=[c for c in chap if c.get('wave',1)==n]
    covered=k if n in DONE_SYS else min(k,len({x for c in courses for x in c.get('covers',[c['code']])}))
    ch=[{'code':c['code'],'title':c['title'],'complete':c['code'] in DONE_COURSES} for c in courses]
    sysd.append({'n':n,'t':t,'title':t,'cat':k,'total':k,'covered':covered,'prio':n in PRIO,'done':n in DONE_SYS,
                 'pct':round(100*covered/k),'ch':ch,'courses':ch,'plan':PLAN.get(n,[])})
completed=[c['code'] for c in chap if c['code'] in DONE_COURSES]
data={'systems':sysd,'build':build,'news':[{'code':c['code'],'title':c['title'],'complete':c['code'] in DONE_COURSES} for c in chap if c.get('added')==build],
      'doneNames':[t for n,t,_ in WAVES if n in DONE_SYS],'ecgCat':CAT,'complete':completed}
s=open(out,encoding='utf-8').read()
# Insigne « 100 % rédigé » : seuls les chapitres de DONE_COURSES (audités), distincts des chapitres intégrés.
assert '<script>window.MEDINA_ALIAS=' in s
s=s.replace('<script>window.MEDINA_ALIAS=','<script>window.MEDINA_COMPLETE='+json.dumps(completed)+';</script><script>window.MEDINA_ALIAS=',1)
s=s.replace('</head>','<style id="medina-polish">'+open(ROOT+'/shell/polish.css').read()+'</style></head>',1)
tail='<script>window.MDN_DATA='+json.dumps(data,ensure_ascii=False)+';window.MDN_ECG='+open(ROOT+'/modules/ecg.json').read()+'</script><script>'+open(ROOT+'/shell/polish.js').read()+'</script>'
i=s.rindex('</body>');s=s[:i]+tail+s[i:]
open(out,'w',encoding='utf-8').write(s)
print('fichier',out,'taille',len(s.encode()))
for c,m in rep.items():
    if m: print(c,'non couvertes',len(m))

# ===== Compression des cours (gzip + base64), décompressés à l'ouverture par DecompressionStream =====
import re,gzip,base64
s=open(out,encoding='utf-8').read()
tpls=[]
def grab(m):
    tpls.append(m.group(0));return ''
s2=re.sub(r'<template (?:id="ch-[^"]+"|data-pop="[^"]+")[\s\S]*?</template>',grab,s)
if tpls:
    pack=base64.b64encode(gzip.compress(''.join(tpls).encode('utf-8'),9)).decode()
    loader=('<div id="mdn-tpl" hidden></div><script id="mdn-pack" type="application/octet-stream">'+pack+'</script>'
     '<script>(async()=>{try{const b=Uint8Array.from(atob(document.getElementById("mdn-pack").textContent),c=>c.charCodeAt(0));'
     'const t=await new Response(new Blob([b]).stream().pipeThrough(new DecompressionStream("gzip"))).text();'
     'document.getElementById("mdn-tpl").innerHTML=t;window.MDN_READY=true;if(typeof render==="function")render();}catch(e){console.error("MEDINA décompression",e)}})()</script>')
    i=s2.rindex('<script id="medina-glossary"') if '<script id="medina-glossary"' in s2 else s2.rindex('</body>')
    s2=s2[:i]+loader+s2[i:]
    open(out,'w',encoding='utf-8').write(s2)
    print('compression :',len(s.encode()),'→',len(s2.encode()),'octets ;',len(tpls),'gabarits')
