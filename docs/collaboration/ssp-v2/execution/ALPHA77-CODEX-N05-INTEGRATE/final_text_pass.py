"""Passe typographique sur texte seulement ; ne touche jamais CSS, JS, attributs ou originaux."""
from lesson_helpers import *
from bs4 import BeautifulSoup,NavigableString,Comment
import re
paths=sorted(CH.glob('*.html'))
# Parse the complete lesson, preserving explicit file boundaries in comments.
joined=''.join('<!--MEDINA_FILE:'+p.name+'-->'+p.read_text() for p in paths)
for _ in [None]:
 s=BeautifulSoup(joined,'html.parser')
 for a in s.select('a[data-reference-source]'):
  t=''.join(str(x) for x in a.find_all(string=True));sid=t.split(' — ',1)[0]
  if sid in SOURCES:a.string=SOURCES[sid]['publisher']+' — '+SOURCES[sid]['section']
 for node in list(s.find_all(string=True)):
  if isinstance(node,Comment) or not isinstance(node,NavigableString) or any(x.name in ['style','script'] for x in node.parents):continue
  t=str(node)
  for left,right in [('selonHUG','selon HUG'),('officielleKDIGO','officielle KDIGO'),('encoreAKI','encore AKI'),('atteinteCOL4','atteinte COL4'),('àIgA','à IgA'),('critèresIRA','critères IRA'),('seuil de classeSGLT2','seuil de classe SGLT2'),('limite d’introductionForxiga','limite d’introduction Forxiga'),('guideSGN','guide SGN'),('éventueliSGLT2','éventuel iSGLT2'),('RevoirAINS','Revoir AINS'),('DansPROFILES','Dans PROFILES'),('directivesMEBEKO','directives MEBEKO'),('exercicesMEDINA','exercices MEDINA'),('LasixIV','Lasix IV'),('Lasix40','Lasix 40'),('Les microscopies','Les microscopies'),('maladieanti-MBG','maladie anti-MBG'),('apportpotassique','apport potassique'),('association àIEC','association à IEC'),('cas critiques','cas critiques'),('source de cette image','source de cette image'),('selonCUEN','selon CUEN'),('lacuneN05','lacune N05'),('avantN00','avant N00'),('néphriteN05','néphrite N05'),('codeN05','code N05'),('motN05','mot N05'),('touteFI','toute FI'),('laFI','la FI'),('uneFI','une FI'),('deLasix','de Lasix'),('MRC/IRA','MRC/IRA')]:t=t.replace(left,right)
  t=re.sub(r'(?<=[a-zà-ÿ])(?=(?:HUG|CUEN|KDIGO|PROFILES|MEBEKO|N05|N28|N12|G1|G2|G3|G4|G5|FI|SGN|IEC|ARA|ANCA)\b)',' ',t)
  t=re.sub(r'\b(KDIGO|HUG|CUEN|PROFILES|MEBEKO|SGN|Forxiga|AKD)(?=\d)',r'\1 ',t)
  t=t.replace('mg/dL,','mg/dL,').replace('20–40à','20–40 à').replace('20et','20 et')
  t=re.sub(r'(?<=[a-zà-ÿ])(?=(?:IRA|HUG|CUEN|KDIGO|PROFILES|MEBEKO|SGN|MRC|IV|IM|SSP|MEDINA|PAS|SAI|OFS|COL4))',' ',t)
  t=re.sub(r'(?<=\d)(?=heures)',' ',t)
  t=re.sub(r'(?<=[a-zà-ÿ])(?=\d)', ' ',t)
  t=re.sub(r'(?<=\d)(?=(?:mg|mL|µmol|mmol|min|ans|fois|jours|h\b|semaines|million|comprimé|m²))',' ',t)
  t=re.sub(r'(?<=[\w)])([≥≤<>≈=÷×])',r' \1',t)
  t=re.sub(r'([≥≤<>≈=÷×])(?=[\w(])',r'\1 ',t)
  t=re.sub(r'\b(HUG|RMS|CUEN|KDIGO|PROFILES|MEBEKO)(?=\d)',r'\1 ',t)
  t=re.sub(r'(?<=\d)%',' %',t)
  t=re.sub(r'(?<=\d)(?=(?:g/|mois|heures|minutes))',' ',t)
  t=re.sub(r',(?=[A-Z])',', ',t)
  t=re.sub(r'(?<=[a-zà-ÿ])(?=[GA][1-5])',' ',t)
  t=t.replace('oug/g','ou g/g').replace('catégoriesG','catégories G').replace('etA','et A')
  t=t.replace('24h','24 h').replace('48h','48 h').replace('PAS ;','PAS ;')
  if t!=str(node):node.replace_with(NavigableString(t))
 rendered=str(s)
 for i,p in enumerate(paths):
  start=rendered.index('<!--MEDINA_FILE:'+p.name+'-->')+len('<!--MEDINA_FILE:'+p.name+'-->')
  end=rendered.index('<!--MEDINA_FILE:'+paths[i+1].name+'-->') if i+1<len(paths) else len(rendered)
  p.write_text(rendered[start:end].strip()+'\n')
print('Texte seul formaté ; CSS, attributs, scripts et images protégés.')
