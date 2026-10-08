#!/usr/bin/env python3
"""Captures obligatoires d'un chapitre (consigne de Vial du 8 octobre 2026).

Pour chacun des 4 environnements du chapitre (onglets Pathologie, Examens, Sciences,
Pharmacologie), au moins 3 captures : haut de l'onglet, milieu de l'onglet, fenêtre
explicative ouverte depuis cet onglet. Une vue mobile s'ajoute. Usage :
    python3 tools/captures_chapitre.py <fragment.html> <CODE> <dossier_sortie>
"""
import asyncio, os, sys
from playwright.async_api import async_playwright

CHROME = os.environ.get('MEDINA_CHROME', '/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
TABS = [('pA', 'pathologie'), ('pE', 'examens'), ('pS', 'sciences'), ('pP', 'pharmacologie')]


async def main(page_file, code, out):
    os.makedirs(out, exist_ok=True)
    shots, errors = [], []
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path=CHROME if os.path.exists(CHROME) else None)
        page = await browser.new_page(viewport={'width': 1366, 'height': 900}, color_scheme='dark')
        page.on('pageerror', lambda e: errors.append(str(e)))
        await page.goto('file://' + os.path.abspath(page_file) + '#/entry/' + code)
        await page.wait_for_timeout(3000)
        for n, (tab, name) in enumerate(TABS, 1):
            button = page.locator(f'button[data-p="{tab}"]').first
            if not await button.count():
                errors.append('onglet absent : ' + tab); continue
            await button.click(); await page.wait_for_timeout(700)
            panel = page.locator(f'#{tab}').first
            await panel.scroll_into_view_if_needed(); await page.evaluate('window.scrollBy(0,-120)')
            await page.wait_for_timeout(300)
            path = f'{out}/{code}_{n}{name}_1_debut.png'; await page.screenshot(path=path); shots.append(path)
            height = await panel.evaluate('e => e.getBoundingClientRect().height')
            top = await panel.evaluate('e => e.getBoundingClientRect().top + window.scrollY')
            await page.evaluate(f'window.scrollTo(0,{top + height / 2 - 300})'); await page.wait_for_timeout(300)
            path = f'{out}/{code}_{n}{name}_2_milieu.png'; await page.screenshot(path=path); shots.append(path)
            word = panel.locator('button.w:visible, [data-k]:visible').nth(2)
            if await word.count():
                await word.scroll_into_view_if_needed(); await word.click(); await page.wait_for_timeout(700)
                path = f'{out}/{code}_{n}{name}_3_fenetre.png'; await page.screenshot(path=path); shots.append(path)
                await page.keyboard.press('Escape'); await page.wait_for_timeout(300)
            else:
                await page.evaluate(f'window.scrollTo(0,{top + height - 800})'); await page.wait_for_timeout(300)
                path = f'{out}/{code}_{n}{name}_3_fin.png'; await page.screenshot(path=path); shots.append(path)
        await page.set_viewport_size({'width': 390, 'height': 844})
        await page.evaluate('window.scrollTo(0,0)'); await page.wait_for_timeout(500)
        overflow = await page.evaluate('document.documentElement.scrollWidth > innerWidth')
        path = f'{out}/{code}_5mobile.png'; await page.screenshot(path=path); shots.append(path)
        await browser.close()
    print(f'{code} : {len(shots)} captures ; débordement mobile : {overflow} ; erreurs JS : {errors or "aucune"}')
    for s in shots: print(s)
    return 0 if len(shots) >= 13 and not overflow else 1


if __name__ == '__main__':
    sys.exit(asyncio.run(main(*sys.argv[1:4])))
