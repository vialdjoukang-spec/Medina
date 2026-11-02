#!/usr/bin/env python3
"""Assembler la rédaction C95 ; les contrôles et relectures restent séparés."""
from pathlib import Path
import subprocess,re,html,json,hashlib,shutil
from bs4 import BeautifulSoup,NavigableString
from PIL import Image
import author_main2,author_popups,author_exams,author_pharma,author_summaries
from author_sciences import sciences
from common import SECTIONS,POP,OUT,ROOT
chapter=ROOT/'chapters/C95'
base=subprocess.check_output(['git','show','8a512893acbab9caa0dcfdd0e8682a44ea72fda6:chapters/C95/C95_a.html'],cwd=ROOT,text=True)
header=base[:base.index('<section class="ilot"')]
header=re.sub(r'<span class="status">.*?</span>','<span class="status">Adulte, avec volet pédiatrique · leucémies de lignée ambiguë et périmètre C95 · sources suisses, classifications OMS/ICC et données européennes · état au 02.11.2026 · auto-relecture IA, distincte d’une validation médicale humaine</span>',header,flags=re.S)
toc='<nav class="toc ui"><b>Plan du cours</b><ol>'
for i in range(15):
 title=BeautifulSoup(SECTIONS[str(i)],'html.parser').h2.get_text(' ',strip=True)
 title=re.sub(r'^'+str(i)+r'\s*','',title)
 toc+=f'<li><a href="#c95-{i}">{html.escape(title)}</a></li>'
toc+='</ol></nav>'
header=re.sub(r'<nav class="toc ui">.*?</nav>',toc,header,flags=re.S)
pager='<div class="pager ui"><button class="prev">← Partie précédente</button><span></span><button class="next">Partie suivante →</button></div>'
index='<details id="c95-reference-index"><summary>Ouvrir une fiche explicative ou une synthèse</summary><ul>'+''.join(f'<li><button class="w" data-k="{ident}">{html.escape(title)}</button></li>' for ident,(title,body) in POP.items())+'</ul></details>'
end=index+'<div class="src"><p>Références liées aux sections et fiches. Les résultats de cohortes gardent leur population et leur horizon. <button class="w" data-k="c95-sources-guides">Sources et limites de lecture</button>. Aucune validation médicale humaine indépendante n’est revendiquée.</p></div>'
files={
'C95_a.html':header+'\n'.join(SECTIONS[str(i)] for i in range(7))+'\n',
'C95_b.html':'\n'.join(SECTIONS[str(i)] for i in range(7,15))+end+'</div>'+pager+'</div>\n',
'C95_c.html':'<div class="panel" id="pE" hidden><div class="chap-body">'+'\n'.join(SECTIONS[f'e-{i}'] for i in range(1,6))+'</div>'+pager+'</div>'+sciences()+'\n',
'C95_d.html':'<div class="panel" id="pP" hidden><div class="chap-body">'+'\n'.join(SECTIONS[f'p-{i}'] for i in range(1,6))+'</div>'+pager+'</div></div></template>\n'}
def title_spacing(title):return re.sub(r'(?<=[a-zàâéèêëîïôöùûüç])(?=20\d\d\b)',' ',title)
items=[f'<template data-pop="{ident}" data-title="{html.escape(title_spacing(title),quote=True)}">{body}</template>\n' for ident,(title,body) in POP.items()]
cut=(len(items)+1)//2
files['C95_pop1.html']=''.join(items[:cut]);files['C95_pop2.html']=''.join(items[cut:])
def typography(s):
 # N'intervient que sur le texte entre balises, jamais les identifiants, URLs ou codes.
 parts=re.split(r'(<[^>]+>)',s)
 for i in range(0,len(parts),2):
  t=parts[i]
  t=re.sub(r'\b(de|en|à|les|sous|entre|sur|dès|après|avant|que|édition|figure|puis|dans)(?=\d)',r'\1 ',t)
  t=re.sub(r'(?<=\d)(?=(?:ans|mois|jours|heures|patients|adultes|enfants|changements|points|mai|octobre|diagnostics|décès|cellules|blastes|mg|kg|mL|min|minutes|secondes|G/L|g/L|G6PD)\b)',' ',t)
  t=re.sub(r'(?<=\d)(?=(?:g/j|mg/j|mg/kg|mg/m²|G/L|g/L))',' ',t)
  t=re.sub(r'\b(CC BY|PROFILES|Child-Pugh)(?=\d|[ABC]\b)',r'\1 ',t)
  t=re.sub(r'(?<=[a-zàâéèêëîïôöùûüç])(?=20(?:1[0-9]|2[0-9])\b)',' ',t)
  t=re.sub(r'\b(EBMT|OMS|HUG|SSP|SEER|OAMal|iBFM|CIM-10-GM)(?=\d)',r'\1 ',t)
  t=t.replace('comprenait53LMA','comprenait 53 LMA').replace('et17LAPM','et 17 LAPM').replace('pas50','pas 50')
  t=t.replace('du18mai','du 18 mai').replace('figure3','figure 3').replace('figure6','figure 6').replace('figure14','figure 14').replace('Suisse2026','Suisse 2026')
  t=re.sub(r'(?<=[A-Za-zÀ-ÿ0-9])(?=[≤≥])',' ',t)
  t=re.sub(r'([≤≥])(?=\d)',r'\1 ',t)
  t=re.sub(r'(?<=[:;])(?=\d)',' ',t)
  t=re.sub(r'(?<!\d),(?=\d)',', ',t)
  parts[i]=t
 return ''.join(parts)
def scope_terms(body):
 # Les liens explicites restent locaux au cours ; aucun glossaire partagé modifié.
 mapping={'BCR::ABL1':'bcrabl1','KMT2A':'kmt2a','CD79a':'crit-b','CD3':'crit-t','CD117':'lai','MPO':'cytometrie','ICC':'who-icc','G6PD':'d-rasburicase'}
 pattern=re.compile(r'(?<![A-Za-zÀ-ÿ0-9])('+ '|'.join(re.escape(k) for k in sorted(mapping,key=len,reverse=True))+r')(?![A-Za-zÀ-ÿ0-9])')
 chunks=re.split(r'(<[^>]+>)',body);protected=[]
 for i,chunk in enumerate(chunks):
  if i%2:
   m=re.match(r'</?(a|button|svg|script|style)\b',chunk,re.I)
   if m:
    if chunk.startswith('</'):
     if protected:protected.pop()
    else:protected.append(m.group(1))
  elif not protected:
   chunk=re.sub(r'\bIA\b','intelligence artificielle',chunk)
   chunk=re.sub(r'\bPCR\b','amplification en chaîne par polymérase',chunk)
   chunk=re.sub(r'\bICANS\b','syndrome de neurotoxicité associé aux cellules effectrices immunitaires',chunk)
   chunk=re.sub(r'\bTNM\b','tumeur–ganglions–métastases',chunk)
   chunks[i]=pattern.sub(lambda m:f'<button class="w" data-k="c95-{mapping[m.group(1)]}">{m.group(1)}</button>',chunk)
 return ''.join(chunks)
for name,body in files.items():
 body=re.sub(r'<(?=\s*[=\d])','&lt;',body)
 body=re.sub(r'(</b>)(?=\d)',r'\1 ',body)
 (chapter/name).write_text(scope_terms(typography(body)))
assets=ROOT/'assets/img/c95/alpha/codex';assets.mkdir(parents=True,exist_ok=True)
rows=[]
for filename,source,credit in [
 ('normal-marrow-openstax2016.jpg','https://commons.wikimedia.org/wiki/File:2205_Bone_Marrow.jpg','OpenStax, Anatomy and Physiology édition8.25, 18mai2016,2205 Bone Marrow'),
 ('flow-g003.png','https://doi.org/10.3390/cancers17050871','Fuda et Chen2025, figure3'),
 ('flow-g006.png','https://doi.org/10.3390/cancers17050871','Fuda et Chen2025, figure6'),
 ('flow-g014.png','https://doi.org/10.3390/cancers17050871','Fuda et Chen2025, figure14')]:
 src=Path('/workspace/medina-source-cache/C95')/filename;dst=assets/filename;shutil.copyfile(src,dst)
 with Image.open(dst) as im:width,height=im.size
 rows.append({'file':str(dst.relative_to(ROOT)),'sha256':hashlib.sha256(dst.read_bytes()).hexdigest(),'width':width,'height':height,'source_url':source,'credit':credit,'license':'CC BY4.0','license_url':'https://creativecommons.org/licenses/by/4.0/','pixel_modification':False,'annotation':'French figcaption identifies original colours/panels and limits; no synthetic anatomy','original_seen':True})
(assets/'provenance.json').write_text(json.dumps({'images':rows,'reviewed_at':'2026-11-02','human_originals':True,'medical_certification':False},ensure_ascii=False,indent=2)+'\n')
(assets/'ATTRIBUTION.md').write_text('# Images originales C95\n\n'+ '\n\n'.join(f'**{r["file"].split("/")[-1]}** — {r["credit"]}. [Source]({r["source_url"]}), [CC BY4.0]({r["license_url"]}). Original inchangé ; annotations explicatives françaises dans les légendes. SHA256 `{r["sha256"]}`.' for r in rows)+'\n\nLa licence de la photographie OpenStax est celle du fichier Commons de2016 explicitement crédité CC BY4.0, pas celle du manuel actuel. Aucune image du manuel actuel n’est copiée. Les diagrammes SVG du cours sont textuels et non anatomiques.\n')
print(json.dumps({'sections':len(SECTIONS),'windows':len(POP),'sciences':6,'originals':len(rows),'status':'assembled_not_yet_validated'}))
