#!/usr/bin/env python3
"""MEDINA — sonde des couleurs rendues (vision photopique diurne).

Ouvre l’Accueil, l’accueil d’un fragment et une Leçon dans Chromium (déjà installé), relève les
couleurs calculées (fonds, bordures, texte, ombres) des éléments visibles et compte :
  - les neutres froids : fonds gris bleuâtres (C OKLCH 0,003–0,011, teinte 200–290°), pondérés par la
    surface, ainsi que les bordures et textes gris bleutés (C jusqu’à 0,04) ;
  - les ombres gris bleuâtre (couleur d’ombre quasi neutre, C 0,004–0,04, de teinte 200–290°) ;
  - le texte bleu saturé (teinte 215–300°, C > 0,085) hors corps des cours (rôles conservés).
Usage : python3 docs/frontend/couleurs/sonde.py --site <dossier construit> --fragment S08 --lesson G45 [--json f]
"""
import argparse
import json
import math
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

JS = r"""() => {
  const out = [];
  const vis = e => { const r = e.getBoundingClientRect(); const s = getComputedStyle(e);
    return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none' && r.bottom > 0 && r.top < innerHeight * 3; };
  for (const e of document.querySelectorAll('body *')) {
    if (!vis(e)) continue;
    const s = getComputedStyle(e), r = e.getBoundingClientRect();
    const area = Math.min(r.width * r.height, innerWidth * innerHeight);
    const inCourse = !!e.closest('.mc-body, .mc-pane, .mc-ilot');
    out.push({tag: e.tagName, cls: (e.className && e.className.baseVal === undefined ? String(e.className) : '').slice(0, 60), area, inCourse,
      bg: s.backgroundColor, bd: [s.borderTopColor, s.borderLeftColor], bw: [s.borderTopWidth, s.borderLeftWidth],
      color: s.color, text: (e.childNodes.length && [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) ? 1 : 0,
      shadow: s.boxShadow});
  }
  out.push({tag: 'BODY', cls: '', area: innerWidth * innerHeight, inCourse: false, bg: getComputedStyle(document.body).backgroundColor, bd: [], bw: [], color: '', text: 0, shadow: 'none'});
  return out;
}"""


def parse(c):
    m = re.match(r'rgba?\(([\d.]+),?\s*([\d.]+),?\s*([\d.]+)(?:\s*[,/]\s*([\d.]+%?))?\)', c or '')
    if not m:
        return None
    a = m.group(4)
    a = 1.0 if a is None else (float(a[:-1]) / 100 if a.endswith('%') else float(a))
    return tuple(float(m.group(i)) / 255 for i in (1, 2, 3)), a


def oklch(rgb):
    lin = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb]
    r, g, b = lin
    l = (0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b) ** (1 / 3)
    m = (0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b) ** (1 / 3)
    s = (0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b) ** (1 / 3)
    L = 0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s
    A = 1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s
    B = 0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s
    return L, math.hypot(A, B), math.degrees(math.atan2(B, A)) % 360


def froid(c, cmin=0.004, cmax=0.04):
    """Gris bleuâtre : quasi neutre (cmin ≤ C ≤ cmax) de teinte 200–290°. Les fonds teintés des
    catégories (C ≥ 0,012 rendu) ne sont pas des neutres : pour les fonds, cmax = 0,011."""
    p = parse(c)
    if not p or p[1] < 0.02:
        return False
    L, C, h = oklch(p[0])
    return cmin <= C <= cmax and 200 <= h <= 290


def detail(items):
    """Principaux contrevenants : (motif, propriété, couleur) → nombre."""
    from collections import Counter
    c = Counter()
    for i in items:
        cle = i['tag'].lower() + ('.' + i['cls'].split()[0] if i['cls'].split() else '')
        if froid(i['bg'], 0.003, 0.011):
            c[(cle, 'fond', i['bg'])] += 1
        for col, w in zip(i['bd'], i['bw']):
            if float(w[:-2] or 0) > 0 and froid(col):
                c[(cle, 'bordure', col)] += 1
        if i['text'] and not i['inCourse'] and parse(i['color']):
            L, C, h = oklch(parse(i['color'])[0])
            if (215 <= h <= 300 and C > 0.085) or froid(i['color'], 0.012):
                c[(cle, 'texte', i['color'])] += 1
        for col in re.findall(r'rgba?\([^)]*\)', i['shadow'] or ''):
            p = parse(col)
            if p and p[1] > 0.02 and (lambda L, C, h: 0.004 <= C <= 0.04 and 200 <= h <= 290)(*oklch(p[0])):
                c[(cle, 'ombre', col)] += 1
    return [f'{n:4d}  {k[1]:8s} {k[2]:28s} {k[0]}' for k, n in c.most_common(25)]


def analyse(items):
    total = sum(i['area'] for i in items if parse(i['bg']) and parse(i['bg'])[1] > 0.5) or 1
    froids = sum(i['area'] for i in items if froid(i['bg'], 0.003, 0.011))
    bords = sum(1 for i in items for c, w in zip(i['bd'], i['bw']) if float(w[:-2] or 0) > 0 and froid(c))
    ombres = 0
    for i in items:
        for c in re.findall(r'rgba?\([^)]*\)', i['shadow'] or ''):
            p = parse(c)
            if p and p[1] > 0.02:
                L, C, h = oklch(p[0])
                if 0.004 <= C <= 0.04 and 200 <= h <= 290:
                    ombres += 1
    texte_bleu = sum(1 for i in items if i['text'] and not i['inCourse'] and parse(i['color'])
                     and (lambda L, C, h: 215 <= h <= 300 and C > 0.085)(*oklch(parse(i['color'])[0])))
    texte_froid = sum(1 for i in items if i['text'] and not i['inCourse'] and froid(i['color'], 0.012))
    fond = oklch(parse(next(i['bg'] for i in items if i['tag'] == 'BODY'))[0]) if parse(next(i['bg'] for i in items if i['tag'] == 'BODY')) else None
    return {'surface_neutre_froide_%': round(100 * froids / total, 1), 'bordures_froides': bords, 'ombres_bleuatres': ombres,
            'texte_bleu_sature_interface': texte_bleu, 'texte_gris_bleute_interface': texte_froid,
            'fond_body_oklch': [round(x, 4) for x in fond] if fond else None}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--site', required=True)
    ap.add_argument('--fragment', default='S08')
    ap.add_argument('--lesson', default='G45')
    ap.add_argument('--json')
    ap.add_argument('--detail', action='store_true', help='liste les principaux contrevenants')
    a = ap.parse_args()
    from playwright.sync_api import sync_playwright
    site = Path(a.site).resolve()
    reg = json.loads((ROOT / 'fragments.json').read_text(encoding='utf-8'))
    f = next(x for x in reg if x['id'].upper() == a.fragment.upper())
    frag = site / 'fragments' / f"MEDINA_{f['id']}_{f['slug']}.html"
    pages = [('accueil', (site / 'index.html').as_uri()), ('fragment', frag.as_uri() + '#/home'), ('lecon', frag.as_uri() + '#/entry/' + a.lesson)]
    exe = os.environ.get('MEDINA_CHROMIUM') or ('/opt/pw-browsers/chromium' if os.path.exists('/opt/pw-browsers/chromium') else None)
    res = {}
    with sync_playwright() as p:
        b = p.chromium.launch(**({'executable_path': exe} if exe else {}))
        pg = b.new_page(viewport={'width': 1280, 'height': 900})
        for nom, url in pages:
            if nom != 'accueil' or (site / 'index.html').is_file():
                pg.goto(url)
                if nom != 'accueil':
                    pg.wait_for_function('() => window.MEDINA_FRAGMENT_READY === true', timeout=60000)
                    if nom == 'lecon':
                        pg.wait_for_selector('.mc', timeout=60000)
                pg.wait_for_timeout(400)
                items = pg.evaluate(JS)
                res[nom] = analyse(items)
                if a.detail:
                    print('==', nom); print('\n'.join(detail(items)))
        b.close()
    print(json.dumps(res, ensure_ascii=False, indent=1))
    if a.json:
        Path(a.json).write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
