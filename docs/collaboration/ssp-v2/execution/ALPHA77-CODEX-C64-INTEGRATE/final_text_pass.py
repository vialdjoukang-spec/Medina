from lesson_helpers import *
from bs4 import BeautifulSoup,NavigableString,Comment
import re
parts=['a','b','c','d','pop1','pop2'];s=BeautifulSoup(''.join((CH/f'C64_{p}.html').read_text()+f'<!--C64-CUT-{p}-->' for p in parts),'html.parser')
for node in list(s.find_all(string=True)):
 if isinstance(node,Comment) or any(x.name in ['style','script'] for x in node.parents):continue
 t=str(node)
 t=re.sub(r'\b(EAU|RCC|PROFILES|MEBEKO|OMS|TNM|KEYNOTE|CIM)(?=20\d{2})',r'\1 ',t)
 t=re.sub(r'(?<=[a-zà-ÿ])(?=\d)', ' ',t)
 t=re.sub(r'(?<=\d)(?=(?:mg|mL|µmol|mmol|min|ans|fois|jours|h\b|semaines))',' ',t)
 t=t.replace('March2026','March 2026').replace('CIM10GM2024','CIM-10-GM 2024').replace('CCR','CCR')
 if t!=str(node):node.replace_with(NavigableString(t))
t=str(s)
for p in parts:b,t=t.split(f'<!--C64-CUT-{p}-->',1);save(p,b)
print('Passe texte, frontières des six fichiers conservées ; CSS et pixels inchangés.')
