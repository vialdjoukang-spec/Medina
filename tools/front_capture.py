#!/usr/bin/env python3
"""Construit puis capture l’Accueil, un fragment, une catégorie, une leçon, l’onglet Sciences et Navigo.

Usage courant :
  python3 tools/front_capture.py --build fragment --fragment S04 --lesson N18 --out docs/frontend/premium/captures
  python3 tools/front_capture.py --build none --site dist --prefix avant

Les captures sont faites à 390 et 1280 px (option --widths), plus deux états de lecture
(police agrandie, mode Livre) à 1280 px. Un rapport JSON liste les erreurs JavaScript.
Le navigateur utilisé est celui de MEDINA_CHROMIUM, sinon /opt/pw-browsers/chromium,
sinon celui de Playwright ; aucun navigateur n’est téléchargé.
"""
import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def chromium_options():
    exe = os.environ.get('MEDINA_CHROMIUM') or next((x for x in ('/opt/pw-browsers/chromium',) if os.path.exists(x)), None)
    return {'executable_path': exe} if exe else {}


def fragment_file(site, ident):
    fragments = json.loads((ROOT / 'fragments.json').read_text(encoding='utf-8'))
    item = next(f for f in fragments if f['id'].upper() == ident.upper())
    return Path(site) / 'fragments' / f"MEDINA_{item['id']}_{item['slug']}.html"


def build(site, mode, ident):
    env = dict(os.environ, MEDINA_OUT=str(site))
    if mode == 'all':
        subprocess.run([sys.executable, str(ROOT / 'build_front.py'), '--all-fragments'], check=True, env=env, cwd=ROOT)
    elif mode == 'fragment':
        subprocess.run([sys.executable, str(ROOT / 'build_front.py'), '--fragment', ident], check=True, env=env, cwd=ROOT)
    fragments = json.loads((ROOT / 'fragments.json').read_text(encoding='utf-8'))
    if all((Path(site) / 'fragments' / f"MEDINA_{f['id']}_{f['slug']}.html").is_file() for f in fragments):
        subprocess.run([sys.executable, str(ROOT / 'build_index.py'), '--fragments-dir', str(Path(site) / 'fragments'),
                        '--output', str(Path(site) / 'index.html')], check=True, cwd=ROOT)
    else:
        print('Accueil non reconstruit : les 23 fragments ne sont pas tous présents dans', site)


def wait_ready(page):
    page.wait_for_function('() => window.MEDINA_FRAGMENT_READY === true', timeout=30000)
    page.wait_for_function('() => !document.getElementById("mdn-pack") || window.MDN_READY === true', timeout=30000)
    page.evaluate('document.fonts.ready')
    page.wait_for_timeout(250)


def capture(args):
    from playwright.sync_api import sync_playwright
    site = Path(args.site).resolve()
    out = Path(args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    frag = fragment_file(site, args.fragment)
    index = site / 'index.html'
    report = {'site': str(site), 'fragment': args.fragment, 'lesson': args.lesson, 'shots': [], 'errors': []}
    prefix = (args.prefix + '-') if args.prefix else ''
    with sync_playwright() as p:
        browser = p.chromium.launch(**chromium_options())
        for width in args.widths:
            height = 844 if width < 700 else 900
            context = browser.new_context(viewport={'width': width, 'height': height}, device_scale_factor=1)
            page = context.new_page()
            page.on('pageerror', lambda e, w=width: report['errors'].append({'width': w, 'error': str(e)}))

            def shot(name, full=False):
                path = out / f'{prefix}{name}-{width}.png'
                page.screenshot(path=str(path), full_page=full)
                report['shots'].append(str(path.relative_to(out)))

            if index.is_file():
                page.goto(index.as_uri())
                page.evaluate('document.fonts.ready')
                page.wait_for_timeout(200)
                shot('accueil')
                page.locator('#specialty-grid').scroll_into_view_if_needed()
                page.wait_for_timeout(150)
                shot('accueil-specialites')
            page.goto(frag.as_uri() + '#/home')
            wait_ready(page)
            shot('fragment-accueil')
            page.locator('.mcg-category-grid').scroll_into_view_if_needed()
            page.wait_for_timeout(150)
            shot('fragment-categories')
            first = page.locator('[data-mcg-category]').first
            if first.count():
                first.click()
                page.wait_for_timeout(400)
                shot('categorie')
            page.goto(frag.as_uri() + '#/entry/' + args.lesson)
            wait_ready(page)
            page.wait_for_selector('.mc', timeout=30000)
            page.wait_for_timeout(300)
            shot('lecon')
            tabs = page.locator('.mc-tabs [data-p]')
            if tabs.count() >= 3:
                tabs.nth(2).click()
                page.wait_for_timeout(300)
                shot('sciences')
                tabs.nth(0).click()
                page.wait_for_timeout(200)
            trigger = page.locator('.mc-navigo-trigger')
            if trigger.is_visible():
                trigger.click()
                page.wait_for_timeout(300)
            part = page.locator('.mc-navigo-panel .mc-navigo-item.mc-navigo-h2').nth(1)
            if part.count() and part.is_visible():
                part.hover()
                page.wait_for_timeout(300)
            shot('navigo')
            if width >= 1000:
                page.keyboard.press('Escape')
                page.goto(frag.as_uri() + '#/entry/' + args.lesson)
                wait_ready(page)
                page.wait_for_selector('.mc')
                size = page.locator('.mc-size-toggle')
                if size.count():
                    size.click()
                    page.locator('.mc-size-range').evaluate("e=>{e.value='24';e.dispatchEvent(new Event('input',{bubbles:true}))}")
                    page.keyboard.press('Escape')
                    page.wait_for_timeout(200)
                    shot('lecon-police-24')
                    size.click()
                    page.locator('.mc-size-reset').click()
                    page.keyboard.press('Escape')
                book = page.locator('.mc-book')
                if book.count():
                    book.click()
                    page.wait_for_timeout(400)
                    shot('lecon-livre')
                    book.click()
            context.close()
        browser.close()
    (out / f'{prefix}captures.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(len(report['shots']), 'captures dans', out, '·', len(report['errors']), 'erreur(s) JavaScript')
    for error in report['errors']:
        print('  ', error)
    return 1 if report['errors'] else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--site', default=os.environ.get('MEDINA_OUT', str(ROOT / 'dist')), help='dossier construit (MEDINA_OUT)')
    parser.add_argument('--out', default=str(ROOT / 'docs/frontend/premium/captures'))
    parser.add_argument('--build', choices=('none', 'fragment', 'all'), default='fragment')
    parser.add_argument('--fragment', default='S04')
    parser.add_argument('--lesson', default='N18')
    parser.add_argument('--prefix', default='')
    parser.add_argument('--widths', type=lambda v: [int(x) for x in v.split(',')], default=[390, 1280])
    args = parser.parse_args()
    if args.build != 'none':
        build(args.site, args.build, args.fragment)
    sys.exit(capture(args))


if __name__ == '__main__':
    main()
