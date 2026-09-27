#!/usr/bin/env python3
"""Captures du front-end MEDINA (PC 1360 px, mobile 390 px, et PC en mode sombre s'il existe) dans audits/FRONT_captures/<jeu>/.
Usage : python3 captures_front.py avant|apres [fichier.html]   (défaut : $MEDINA_OUT/MEDINA.html)
Chaque page est capturée dans la fenêtre visible, notification fermée, sauf la capture dédiée à la notification."""
import os, sys
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get('MEDINA_OUT', '/mnt/user-data/outputs' if os.path.isdir('/mnt/user-data') else ROOT + '/dist')
SET = sys.argv[1] if len(sys.argv) > 1 else 'avant'
SRC = sys.argv[2] if len(sys.argv) > 2 else OUT + '/MEDINA.html'
DST = f'{ROOT}/audits/FRONT_captures/{SET}'
os.makedirs(DST, exist_ok=True)
F = 'file://' + os.path.abspath(SRC)
QUIET = "document.querySelectorAll('.mdn-toast').forEach(t=>t.remove())"

# (nom, route, action JavaScript facultative après chargement, défilement vertical)
PAGES = [
    ('01_accueil', '#/home', None, 0),
    ('02_accueil_directeur', '#/home', "document.querySelector('.mdn-director')&&(document.querySelector('.mdn-director').open=true)", 420),
    ('03_bouton_directeur', '#/home', "document.querySelector('.mdn-dir')&&document.querySelector('.mdn-dir').click()", 0),
    ('04_notification', '#/home', 'KEEP_TOAST', 0),
    ('05_specialite_cardiologie', '#/specialty/cardiologie', None, 0),
    ('06_systeme_cardiologie', '#/specialty/cardiologie?system=cardiac', None, 300),
    ('07_entree_cim_plan', '#/entry/K80', None, 0),
    ('08_cours_entete', '#/entry/J45', None, 0),
    ('09_cours_ilot', '#/entry/J45', "document.querySelector('.mc-ilot h2')&&document.querySelectorAll('.mc-ilot')[3].scrollIntoView()", None),
    ('10_cours_fenetre', '#/entry/J45', "document.querySelectorAll('.mc .mc-w')[2].click()", None),
    ('11_cours_quiz', '#/entry/J45', "(()=>{const b=document.querySelector('.mc-tabs button[data-p=\"pE\"]');b.click();const q=document.querySelector('.mc-panel:not([hidden]) .mc-quiz');q.scrollIntoView();q.querySelector('.mc-opt').click()})()", None),
    ('12_cours_pareto', '#/entry/J45', "document.querySelector('.mc .mc-pareto-btn').click()", None),
    ('13_cours_navigo', '#/entry/A41', "document.querySelector('.mc-navigo-trigger').click()", None),
    ('14_cours_police_taille', '#/entry/A41', "document.querySelector('.mc-size-toggle').click()", None),
    ('15_cours_mode_livre', '#/entry/I26', "document.querySelector('.mc-book').click()", None),
    ('16_cours_sciences', '#/entry/J18', "document.querySelector('.mc-tabs button[data-p=\"pS\"]').click()", None),
    ('17_examen_federal', '#/federal', None, 0),
    ('18_carnet', '#/notebook', None, 0),
    ('19_recherche', '#/search?q=asthme', None, 0),
    ('20_methode', '#/method', None, 0),
    ('21_atlas_ecg', '#/home', "document.querySelector('.mdn-ecgbtn')&&document.querySelector('.mdn-ecgbtn').click()", 0),
]

with sync_playwright() as p:
    exe = os.environ.get('MEDINA_CHROMIUM') or next((x for x in ['/opt/pw-browsers/chromium'] if os.path.exists(x)), None)
    b = p.chromium.launch(**({'executable_path': exe} if exe else {}))
    errors = []
    DARK = {'01_accueil', '05_specialite_cardiologie', '08_cours_entete', '09_cours_ilot', '10_cours_fenetre', '11_cours_quiz', '13_cours_navigo', '17_examen_federal', '19_recherche', '21_atlas_ecg'}
    for label, vw in [('pc', (1360, 900)), ('mobile', (390, 844)), ('pc-sombre', (1360, 900))]:
        ctx = b.new_context(viewport={'width': vw[0], 'height': vw[1]}, device_scale_factor=1)
        if label.endswith('sombre'): ctx.add_init_script("try{localStorage.setItem('medina.dark','1')}catch(e){}")
        for name, route, action, scroll in PAGES:
            if label.endswith('sombre') and name not in DARK: continue
            pg = ctx.new_page()
            pg.on('pageerror', lambda e: None if 'lesson-core' in str(e) else errors.append(f'{name}: {e}'))
            pg.goto(F + route); pg.wait_for_timeout(1600)
            if action != 'KEEP_TOAST':
                pg.evaluate(QUIET)
            else:
                pg.evaluate("try{localStorage.removeItem('medina.seen')}catch(e){}"); pg.reload(); pg.wait_for_timeout(2200)
            if action and action != 'KEEP_TOAST':
                try: pg.evaluate(action)
                except Exception as e: errors.append(f'{name}: action {e}')
                pg.wait_for_timeout(700)
            if scroll: pg.evaluate(f'window.scrollTo(0,{scroll})'); pg.wait_for_timeout(400)
            pg.screenshot(path=f'{DST}/{name}_{label}.png')
            pg.close()
        ctx.close()
    b.close()
print(len(PAGES) * 2 + len(DARK), 'captures dans', DST)
if errors: print('Erreurs :', *errors, sep='\n- ')
