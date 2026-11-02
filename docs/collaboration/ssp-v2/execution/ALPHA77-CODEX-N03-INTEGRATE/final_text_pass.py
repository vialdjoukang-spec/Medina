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
  t=a.get_text();sid=t.split(' — ',1)[0]
  if sid in SOURCES:a.string=SOURCES[sid]['publisher']+' — '+SOURCES[sid]['section']
 for node in list(s.find_all(string=True)):
  if isinstance(node,Comment) or not isinstance(node,NavigableString) or any(x.name in ['style','script'] for x in node.parents):continue
  t=str(node)
  t=re.sub(r'(?<=[a-zà-ÿ])(?=\d)', ' ',t)
  t=re.sub(r'(?<=\d)(?=(?:mg|mL|µmol|mmol|min|ans|fois|jours|h\b|semaines|million|comprimé|m²))',' ',t)
  t=re.sub(r'(?<=[\w)])([≥≤<>≈=÷×])',r' \1',t)
  t=re.sub(r'([≥≤<>≈=÷×])(?=[\w(])',r'\1 ',t)
  t=re.sub(r'\b(HUG|RMS|CUEN|KDIGO|PROFILES|MEBEKO)(?=\d)',r'\1 ',t)
  t=re.sub(r'(?<=\d)%',' %',t)
  t=t.replace('24h','24 h').replace('48h','48 h').replace('PAS ;','PAS ;')
  if t!=str(node):node.replace_with(NavigableString(t))
 rendered=str(s)
 for i,p in enumerate(paths):
  start=rendered.index('<!--MEDINA_FILE:'+p.name+'-->')+len('<!--MEDINA_FILE:'+p.name+'-->')
  end=rendered.index('<!--MEDINA_FILE:'+paths[i+1].name+'-->') if i+1<len(paths) else len(rendered)
  p.write_text(rendered[start:end].strip()+'\n')
print('Texte seul formaté ; CSS, attributs, scripts et images protégés.')
