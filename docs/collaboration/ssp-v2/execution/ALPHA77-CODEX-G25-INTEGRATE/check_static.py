from pathlib import Path
from bs4 import BeautifulSoup
import re,json,hashlib,subprocess
O=Path(__file__).resolve().parent;R=O.parents[4];C=R/'chapters/G25'
files=sorted(C.glob('*.html'));assert len(files)==6
raw='\n'.join(p.read_text() for p in files);s=BeautifulSoup(raw,'html.parser')
ids=re.findall(r'\bid="([^"]+)"',raw);assert len(ids)==len(set(ids))
assert len(s.select('.panel'))==4 and len(s.select('.sci'))==6
course=s.find('template',id='ch-G25');assert course is not None and len(course.select('.panel'))==4 and len(course.select('.sci'))==6, 'Four panels and six disciplines must remain inside chapter template'
assert len(s.select('[data-semiology]'))==9
assert all(f'g25-{i}' in ids for i in range(1,15))
pops={x['data-pop'] for x in s.select('template[data-pop]')};assert len(pops)==66
assert len(s.select('.pareto-btn'))==14 and len(s.select('.quiz'))==4
assert all(x['data-k'] in pops for x in s.select('[data-k]'))
for a in s.select('a[href^="#g25-"]'):assert a['href'][1:] in ids
assert len(s.select('[data-g25-figure]'))==10 and len(s.select('[data-g25-mark]'))==34
for im in s.select('[data-g25-figure] img'):assert (R/im['src']).is_file()
for row in json.loads((O/'figures-rights.json').read_text())['figures']:
 assert hashlib.sha256((R/row['path']).read_bytes()).hexdigest()==row['sha256']
for bad in ['G09','g09','D77','d77','N06','n06']:assert bad not in raw,bad
rows=json.loads((O/'source-ledger.json').read_text())['sources'];assert len(rows)==52
assert len([x for x in rows if x['id'].startswith('FI-')])==8
assert all(Path(x['cache_path']).exists() for x in rows)
assert hashlib.sha256((R/'chapters.json').read_bytes()).hexdigest()==hashlib.sha256(subprocess.check_output(['git','show','8a512893acbab9caa0dcfdd0e8682a44ea72fda6:chapters.json'],cwd=R)).hexdigest()
assert '<svg' not in raw
print('PASS : six surfaces, quatre panneaux, six sciences, neuf sémiologie,14points,66fenêtres/14Pareto/4quiz,10figures/34repères ; cibles et assets résolus,52 lectures/huit FI, catalogue inchangé. Contrôle statique ciblé, pas audit médical indépendant.')
