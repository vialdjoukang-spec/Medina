from pathlib import Path
from bs4 import BeautifulSoup
import re,json,hashlib
O=Path(__file__).resolve().parent;R=O.parents[4];C=R/'chapters/N05'
files=sorted(C.glob('*.html'));assert len(files)==6
raw='\n'.join(p.read_text() for p in files);s=BeautifulSoup(raw,'html.parser')
ids=re.findall(r'\bid="([^"]+)"',raw);assert len(ids)==len(set(ids))
assert len(s.select('.panel'))==4
assert len(s.select('.sci'))==6
assert len(s.select('[data-semiology]'))==9
assert all(f'n05-{i}' in ids for i in range(1,15))
pops={x['data-pop'] for x in s.select('template[data-pop]')};assert len(pops)==34
assert len(s.select('.pareto-btn'))==14 and len(s.select('.quiz'))==4
assert all(x['data-k'] in pops for x in s.select('[data-k]'))
for a in s.select('a[href^="#n05-"]'):assert a['href'][1:] in ids
assert len(s.select('[data-n05-figure]'))==9
assert len(s.select('[data-n05-mark]'))==30
for im in s.select('[data-n05-figure] img'):assert (R/im['src']).is_file()
for bad in ['COL4 A3','COL4 A4','COL4 A5','CYP3 A4','N03','n03','FSGS']:assert bad not in raw,bad
assert 'COL4A3' in raw and 'CYP3A4' in raw
assert '26,5' in raw and '6 h' in raw and 'mars 2025' in raw
assert len(json.loads((R/'chapters.json').read_text()))>0
rows=json.loads((O/'source-ledger.json').read_text())['sources'];assert len(rows)==33
assert len([x for x in rows if x['id'].startswith('FI-')])==6
assert all(Path(x['cache_path']).exists() for x in rows)
print('PASS : six surfaces, quatre panneaux, six sciences, neuf sections sémiologiques,14points,34fenêtres/14Pareto/4quiz,9figures/30repères ; IDs uniques, cibles et assets résolus,33lectures/6FI, nomenclatures scientifiques préservées.')
