#!/usr/bin/env python3
"""Contrôles bloquants d'un ou plusieurs chapitres. Usage : python3 test_v7.py J45 [J44 ...]
Vérifie : abréviations non couvertes, clés de fenêtres, Pareto, rendu, mots verts, onglets, erreurs JavaScript, rendu mobile."""
import sys,os,re,glob
ROOT=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,ROOT)
import build_medina as B
OUT=os.environ.get('MEDINA_OUT','/mnt/user-data/outputs' if os.path.isdir('/mnt/user-data') else ROOT+'/dist')
fails=[]
for code in sys.argv[1:]:
    src=''.join(open(f).read() for f in sorted(glob.glob(f'{ROOT}/chapters/{code}/*.html')))
    if not src: fails.append(code+': aucun fichier');continue
    s=B.wrap_html(B.pareto_ratios(B.transform(src)))
    m=B.audit(s,code)
    if m: fails.append(f'{code}: abréviations non couvertes {m}')
    keys=set(re.findall(r'data-k="([^"]+)"',src));pops=set(re.findall(r'data-pop="([^"]+)"',src))
    allpops=set(re.findall(r'data-pop="([^"]+)"',''.join(open(f).read() for f in glob.glob(ROOT+'/chapters/*/*.html'))))
    if keys-allpops: fails.append(f'{code}: fenêtres manquantes {sorted(keys-allpops)}')
    bad=[k for k in pops if not (k.startswith(code.lower()+'-') or k.startswith('pareto-'+code.lower()))]
    if bad: fails.append(f'{code}: clés sans préfixe {bad}')
    print(code,'mots',B.words(src),'fenêtres',len(pops),'quiz',src.count('class="quiz'),'pareto',src.count('pareto-btn'))
from playwright.sync_api import sync_playwright
F='file://'+OUT+'/MEDINA.html'
with sync_playwright() as p:
    b=p.chromium.launch();er=[]
    for vw in [(1300,900),(390,844)]:
        pg=b.new_page(viewport={'width':vw[0],'height':vw[1]});pg.on('pageerror',lambda e:(None if 'lesson-core' in str(e) else er.append(str(e))))
        pg.goto(F);pg.wait_for_timeout(800)
        for code in sys.argv[1:]:
            pg.goto(F+'#/entry/'+code);pg.wait_for_timeout(900)
            if pg.locator('.mc').count()!=1: fails.append(code+': cours non affiché');continue
            if vw[0]>1000:
                n=pg.locator('.mc .mc-w').count()
                for i in range(n):
                    el=pg.locator('.mc .mc-w').nth(i)
                    if not el.is_visible(): continue
                    el.click();pg.wait_for_timeout(50)
                    if 'Fiche absente' in pg.inner_text('.mc-dlg-b'): fails.append(code+': fiche absente '+str(el.get_attribute('data-k')))
                    pg.keyboard.press('Escape')
                for t in ['pE','pS','pP','pA']: pg.locator(f'.mc-tabs button[data-p="{t}"]').click();pg.wait_for_timeout(100)
                pg.click('.mc-book');pg.wait_for_timeout(100);pg.click('.mc-book')
            else:
                w=pg.evaluate('document.documentElement.scrollWidth');
                if w>vw[0]+2: fails.append(f'{code}: débordement horizontal mobile ({w}px)')
    if er: fails.append('JavaScript: '+' | '.join(er[:3]))
    b.close()
print('OK' if not fails else 'ECHEC :\n- '+'\n- '.join(fails))
