from lesson_helpers import *
from bs4 import BeautifulSoup
import re
course=BeautifulSoup(''.join((CH/f'N02_{p}.html').read_text() for p in ['a','b','c','d']),'html.parser')
for part in ['pop1','pop2']:
 path=CH/f'N02_{part}.html';s=BeautifulSoup(path.read_text(),'html.parser')
 for i in range(1,15):
  t=s.find('template',attrs={'data-pop':f'n02-exp-{i}'})
  if not t:continue
  section=course.find(id=f'n02-{i}');urls={a.get('href') for a in section.select('a[data-reference-source]')}
  ids=[k for k,v in SOURCES.items() if v['url'] in urls]
  assert ids
  for r in t.select('.src'):r.decompose()
  t.append(BeautifulSoup(ref(*ids),'html.parser'))
 path.write_text(str(s)+'\n')
print('14 fenêtres : références des passages alignées sur leur section source, sans suppression du contexte.')
