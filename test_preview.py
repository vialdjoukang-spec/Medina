import sys,re,os
from playwright.sync_api import sync_playwright
ROOT=os.path.dirname(os.path.abspath(__file__))
code=sys.argv[1]; path=os.path.join(ROOT,'preview',f'{code}.html'); F='file://'+path
src=open(path).read()
body=src[src.index(f'<template id="ch-{code}"'):src.index('<script id="medina-glossary"')]
keys=set(re.findall(r'data-k="([^"]+)"',body)); pops=set(re.findall(r'data-pop="([^"]+)"',src))
missing=sorted(keys-pops); fails=[]
if missing: fails.append('fenetres manquantes: '+','.join(missing))
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1300,'height':900});er=[]
    pg.on('pageerror',lambda e:er.append(str(e)))
    pg.goto(F+'#/entry/'+code);pg.wait_for_timeout(1500)
    if pg.locator('.mc').count()!=1: fails.append('cours non affiché')
    else:
        pg.locator('.mc .mc-ab').first.click();pg.wait_for_timeout(200)
        if not pg.eval_on_selector('dialog.mc-dlg','d=>d.open'): fails.append('fenêtre abréviation')
        pg.keyboard.press('Escape')
        n=pg.locator('.mc .mc-w').count()
        for i in range(0,n,max(1,n//15)):
            el=pg.locator('.mc .mc-w').nth(i)
            if not el.is_visible(): continue
            el.click();pg.wait_for_timeout(120)
            if 'Fiche absente' in pg.inner_text('.mc-dlg-b'): fails.append('fiche absente '+el.get_attribute('data-k'))
            pg.keyboard.press('Escape')
        pg.click('.mc-book')
        for tab in ['pA','pE','pS','pP']:
            bt=pg.locator(f'.mc-tabs button[data-p="{tab}"]')
            if bt.count()==0: fails.append('onglet absent '+tab);continue
            bt.click();pg.wait_for_timeout(200)
        pg.click('.mc-book')
        pg.screenshot(path=os.path.join(ROOT,'preview',f'{code}.png'))
    if er: fails.append('JS: '+' | '.join(er[:3]))
    b.close()
print('OK' if not fails else 'ECHEC: '+' ; '.join(fails))
