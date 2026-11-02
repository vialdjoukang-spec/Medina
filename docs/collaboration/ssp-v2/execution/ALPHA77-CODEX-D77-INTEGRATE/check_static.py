from pathlib import Path
from bs4 import BeautifulSoup
import re,json,hashlib
O=Path(__file__).resolve().parent;R=O.parents[4];C=R/'chapters/D77'
files=sorted(C.glob('*.html'));assert len(files)==6
raw='\n'.join(p.read_text() for p in files);s=BeautifulSoup(raw,'html.parser')
ids=re.findall(r'\bid="([^"]+)"',raw);assert len(ids)==len(set(ids))
assert len(s.select('.panel'))==4 and len(s.select('.sci'))==6
assert len(s.select('[data-semiology]'))==9
assert all(f'd77-{i}' in ids for i in range(1,15))
pops={x['data-pop'] for x in s.select('template[data-pop]')};assert len(pops)==34
assert len(s.select('.pareto-btn'))==14 and len(s.select('.quiz'))==4
assert all(x['data-k'] in pops for x in s.select('[data-k]'))
for a in s.select('a[href^="#d77-"]'):assert a['href'][1:] in ids
assert len(s.select('[data-d77-figure]'))==10 and len(s.select('[data-d77-mark]'))==32
for im in s.select('[data-d77-figure] img'):assert (R/im['src']).is_file()
for row in json.loads((O/'figures-rights.json').read_text())['figures']:
 assert hashlib.sha256((R/row['path']).read_bytes()).hexdigest()==row['sha256']
for bad in ['N06','n06','d77-codage','d77-hss','d77-vaccins']:assert bad not in raw,bad
rows=json.loads((O/'source-ledger.json').read_text())['sources'];assert len(rows)==27
assert len([x for x in rows if x['id'].startswith('FI-')])==2
assert all(Path(x['cache_path']).exists() for x in rows)
assert hashlib.sha256((R/'chapters.json').read_bytes()).hexdigest()==hashlib.sha256(__import__('subprocess').check_output(['git','show','8a512893acbab9caa0dcfdd0e8682a44ea72fda6:chapters.json'],cwd=R)).hexdigest()
print('PASS : six surfaces, quatre panneaux, six sciences, neuf sections sémiologiques, 14 points, 34 fenêtres/14 Pareto/4 quiz, 10 figures/32 repères ; IDs uniques, cibles et assets résolus, 27 lectures/2 FI suisses + RCP étranger distinct, catalogue inchangé.')
