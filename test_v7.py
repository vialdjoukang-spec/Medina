#!/usr/bin/env python3
"""Contrôles bloquants d'un ou plusieurs chapitres. Usage : python3 test_v7.py [--static] J45 [J44 ...]
--static : contrôles du source seulement (sans navigateur).
Vérifie : abréviations non couvertes, clés de fenêtres, Pareto, rendu, mots verts, onglets, erreurs JavaScript, rendu mobile."""
import sys,os,re,glob
ROOT=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,ROOT)
import build_medina as B
OUT=os.environ.get('MEDINA_OUT','/mnt/user-data/outputs' if os.path.isdir('/mnt/user-data') else ROOT+'/dist')
STATIC='--static' in sys.argv;CODES=[c for c in sys.argv[1:] if not c.startswith('--')]
# I50 est le chapitre modèle, rédigé avant la règle des préfixes : ses clés historiques sont tolérées.
LEGACY_KEYS={'I50'}
fails=[]
for code in CODES:
    src=''.join(open(f).read() for f in sorted(glob.glob(f'{ROOT}/chapters/{code}/*.html')))
    if not src: fails.append(code+': aucun fichier');continue
    s=B.wrap_html(B.pareto_ratios(B.transform(src)))
    m=B.audit(s,code)
    if m: fails.append(f'{code}: abréviations non couvertes {m}')
    keys=set(re.findall(r'data-k="([^"]+)"',src));pops=set(re.findall(r'data-pop="([^"]+)"',src))
    allpops=set(re.findall(r'data-pop="([^"]+)"',''.join(open(f).read() for f in glob.glob(ROOT+'/chapters/*/*.html'))))
    if keys-allpops: fails.append(f'{code}: fenêtres manquantes {sorted(keys-allpops)}')
    bad=[k for k in pops if not (k.startswith(code.lower()+'-') or k.startswith('pareto-'+code.lower()))]
    if bad and code not in LEGACY_KEYS: fails.append(f'{code}: clés sans préfixe {bad}')
    print(code,'mots',B.words(src),'fenêtres',len(pops),'quiz',src.count('class="quiz'),'pareto',src.count('pareto-btn'))
if STATIC:
    print('OK' if not fails else 'ECHEC :\n- '+'\n- '.join(fails));sys.exit(1 if fails else 0)
from playwright.sync_api import sync_playwright
F='file://'+OUT+'/MEDINA.html'
with sync_playwright() as p:
    exe=os.environ.get('MEDINA_CHROMIUM') or next((x for x in ['/opt/pw-browsers/chromium'] if os.path.exists(x)),None)
    b=p.chromium.launch(**({'executable_path':exe} if exe else {}));er=[]
    for vw in [(1300,900),(390,844)]:
        pg=b.new_page(viewport={'width':vw[0],'height':vw[1]});pg.on('pageerror',lambda e:(None if 'lesson-core' in str(e) else er.append(str(e))))
        pg.goto(F);pg.wait_for_timeout(800)
        for code in CODES:
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
                # Apports Alpha : Navigo, Police Taille, mode livre
                pg.click('.mc-navigo-trigger');pg.wait_for_timeout(120)
                items=pg.locator('.mc-navigo-item')
                if items.count()==0: fails.append(code+': Navigo vide')
                else:
                    items.nth(items.count()-1).click();pg.wait_for_timeout(700)
                    if not pg.evaluate("!!document.activeElement&&/^H[234]$/.test(document.activeElement.tagName)"): fails.append(code+': saut Navigo inopérant')
                if pg.locator('.mc-navigo-panel:not([hidden])').count(): pg.keyboard.press('Escape')
                pg.click('.mc-size-toggle');pg.evaluate("(()=>{const r=document.querySelector('.mc-size-range');r.value=21;r.dispatchEvent(new Event('input'))})()")
                if pg.evaluate("getComputedStyle(document.querySelector('.mc')).getPropertyValue('--mc-fs').trim()")!='21px': fails.append(code+': Police Taille inopérante')
                pg.click('.mc-size-reset')
                if pg.evaluate("getComputedStyle(document.querySelector('.mc')).getPropertyValue('--mc-fs').trim()")!='17px': fails.append(code+': réinitialisation Police Taille inopérante')
                pg.keyboard.press('Escape')
                # Phase 2 (si présente) : barre supérieure collante, mode sombre aller-retour sans résidu
                if pg.locator('.mdn-darkbtn').count():
                    pg.evaluate("document.documentElement.style.scrollBehavior='auto';window.scrollTo(0,2500)");pg.wait_for_timeout(150)
                    if abs(pg.evaluate("document.querySelector('.topbar').getBoundingClientRect().top"))>1: fails.append(code+': barre supérieure non collante')
                    pg.evaluate("window.scrollTo(0,0)")
                    pg.click('.mdn-darkbtn');pg.wait_for_timeout(300)
                    if not pg.evaluate("document.documentElement.classList.contains('mdn-dark')"): fails.append(code+': mode sombre inopérant')
                    pg.click('.mdn-darkbtn');pg.wait_for_timeout(150)
                    if pg.evaluate("document.querySelectorAll('.mdn-dk-bg,.mdn-dk-ink,.mdn-dk-tint').length"): fails.append(code+': résidus du mode sombre')
                pg.click('.mc-book');pg.wait_for_timeout(150)
                if not pg.evaluate("document.querySelector('.mc').classList.contains('book')"): fails.append(code+': mode livre inopérant')
                pg.click('.mc-book')
            else:
                w=pg.evaluate('document.documentElement.scrollWidth');
                if w>vw[0]+2: fails.append(f'{code}: débordement horizontal mobile ({w}px)')
    if er: fails.append('JavaScript: '+' | '.join(er[:3]))
    b.close()
print('OK' if not fails else 'ECHEC :\n- '+'\n- '.join(fails))
if fails:
    sys.exit(1)
