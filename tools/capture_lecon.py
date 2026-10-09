#!/usr/bin/env python3
"""Produire les deux captures réglementaires d'une ou plusieurs leçons MEDINA.

Capture 1 : ouverture de la leçon (titre, onglets, début de l'onglet Pathologie).
Capture 2 : première fenêtre explicative ouverte depuis un mot interactif.
Les captures sont destinées au panneau latéral, jamais au fil du chat.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from playwright.async_api import async_playwright

VIEWPORT = {"width": 1440, "height": 1000}


async def settle(page):
    await page.evaluate("document.fonts.ready")
    await page.evaluate("new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)))")


async def click_word(trigger):
    """Cliquer dans le texte peint d'un mot interactif, même réparti sur plusieurs lignes."""
    await trigger.scroll_into_view_if_needed()
    position = await trigger.evaluate("""el => {
      const outer=el.getBoundingClientRect();
      for(const r of el.getClientRects()) {
        const left=Math.max(0,r.left),right=Math.min(innerWidth,r.right);
        const top=Math.max(0,r.top),bottom=Math.min(innerHeight,r.bottom);
        if(right<=left || bottom<=top) continue;
        const x=(left+right)/2,y=(top+bottom)/2,hit=document.elementFromPoint(x,y);
        if(hit===el || el.contains(hit)) return {x:x-outer.left,y:y-outer.top};
      }
      throw new Error('Aucun fragment de texte cliquable visible');
    }""")
    await trigger.click(position=position)


async def capture_one(page, base_url, code, output):
    errors = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    await page.goto(f"{base_url}#/entry/{code}", wait_until="domcontentloaded", timeout=60000)
    await page.wait_for_function("window.MDN_READY===true", timeout=60000)
    course = page.locator(f'.mc[data-code="{code}"]')
    await course.wait_for(state="visible")
    if await course.evaluate("el=>el.classList.contains('book')"):
        await page.locator('.mc-book').click()
    await page.locator(f'.mc[data-code="{code}"] .mc-tabs button[data-p="pA"]').click()
    await settle(page)
    await page.evaluate("scrollTo({top:0,behavior:'instant'})")
    await settle(page)
    first = output / f"{code.lower()}-1-ouverture.png"
    await page.screenshot(path=str(first), full_page=False)

    active = course.locator('.mc-panel:not([hidden])')
    trigger = active.locator('[data-k]').first
    if not await trigger.count():
        raise RuntimeError(f"{code} : aucun mot interactif dans l'onglet Pathologie")
    await click_word(trigger)
    dialog = page.locator('.mc-dlg[open]')
    await dialog.wait_for(state="visible")
    title = (await dialog.locator('#mc-dlg-t').inner_text()).strip()
    body = (await dialog.locator('.mc-dlg-b').inner_text()).strip()
    if len(body) < 40 or "Fiche absente." in body:
        raise RuntimeError(f"{code} : fenêtre explicative vide ou absente")
    await settle(page)
    second = output / f"{code.lower()}-2-explication.png"
    await page.screenshot(path=str(second), full_page=False)
    await page.keyboard.press("Escape")
    if errors:
        raise RuntimeError(f"{code} : erreurs JavaScript : " + "; ".join(errors))
    return {"code": code, "captures": [first.name, second.name], "fenetre": title}


async def run(args):
    args.output.mkdir(parents=True, exist_ok=True)
    report = {"captured_at_utc": datetime.now(timezone.utc).isoformat(),
              "source": args.html.resolve().as_uri(), "viewport": VIEWPORT, "lecons": []}
    async with async_playwright() as playwright:
        launch = {"headless": True, "args": ["--no-sandbox", "--disable-dev-shm-usage"]}
        if args.browser_executable:
            launch["executable_path"] = str(args.browser_executable)
        browser = await playwright.chromium.launch(**launch)
        try:
            for code in args.codes:
                page = await browser.new_page(viewport=VIEWPORT, color_scheme="light",
                                              reduced_motion="reduce")
                page.set_default_timeout(15000)
                try:
                    report["lecons"].append(await capture_one(page, report["source"], code, args.output))
                    print(f"{code} : 2 captures", flush=True)
                finally:
                    await page.close()
        finally:
            await browser.close()
    (args.output / "captures.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n",
                                               encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--html", required=True, type=Path, help="Frontend de fragment construit")
    parser.add_argument("--output", required=True, type=Path, help="Dossier des PNG")
    parser.add_argument("--browser-executable", type=Path, help="Chromium local facultatif")
    parser.add_argument("codes", nargs="+", help="Codes CIM des leçons, par exemple J45 J44")
    args = parser.parse_args()
    try:
        asyncio.run(run(args))
    except Exception as error:  # message lisible pour la remise
        print(f"ÉCHEC : {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
