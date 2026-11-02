from pathlib import Path
import re,json
P=Path('chapters/E07')
for p in P.glob('*.html'):
 s=p.read_text().replace('Dans cette leçon, RCP désigne','Dans cette leçon, ce sigle désigne');parts=re.split('(<[^>]+>)',s);buttons=anchors=refs=0
 for i,t in enumerate(parts):
  if t.startswith('<'):
   if re.match(r'<button\b',t):buttons+=1
   elif t.startswith('</button'):buttons-=1
   if re.match(r'<a\b',t):anchors+=1
   elif t.startswith('</a'):anchors-=1
   if re.match(r'<ul\b',t) and 'data-justification-sources' in t:refs+=1
   elif t.startswith('</ul') and refs:refs-=1
   continue
  if buttons or anchors or refs:continue
  for a,b in [('IA','intelligence artificielle'),('IC','intervalle de confiance'),('ECG','électrocardiogramme'),('ESE','Société européenne d’endocrinologie'),('ESPE','Société européenne d’endocrinologie pédiatrique')]:t=re.sub(r'(?<![\w-])'+a+r'(?![\w-])',b,t)
  for a,key in [('T3','e07-hormones-local'),('T4','e07-hormones-local'),('TSH','e07-hormones-local'),('TBG','e07-tbg'),('ETA','e07-sources-guides'),('PROFILES','e07-sources-guides'),('RCP','e07-rcp-local')]:t=re.sub(r'(?<![\w-])'+a+r'(?![\w-])','<button class="w" data-k="'+key+'">'+a+'</button>',t)
  parts[i]=t
 p.write_text(''.join(parts))
p=P/'E07_pop2.html';s=p.read_text();s+='\n<template data-pop="e07-hormones-local" data-title="Thyroxine, triiodothyronine et thyréostimuline"><p>La thyroxine contient quatre atomes d’iode, la triiodothyronine trois. La fraction totale comprend la réserve liée aux protéines ; la fraction libre doit être interprétée avec la méthode et les normes d’âge. La thyréostimuline hypophysaire participe au rétrocontrôle, mais une valeur normale ou basse n’exclut pas une hypothyroïdie lorsque maladie critique, médicament ou atteinte centrale modifie l’axe. Les références adultes ne sont pas appliquées au nouveau-né. Aucun seuil unique ne remplace le contexte.</p><p class="src"><a data-reference-source="1" href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8001676/" target="_blank" rel="noopener">[S3] ENDO-ERN</a> ; <a data-reference-source="1" href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8285315/" target="_blank" rel="noopener">[S16] NTIS</a> ; <a data-reference-source="1" href="https://openstax.org/books/anatomy-and-physiology-2e/pages/17-4-the-thyroid-gland" target="_blank" rel="noopener">[S42] synthèse normale</a>.</p></template>\n';p.write_text(s)
