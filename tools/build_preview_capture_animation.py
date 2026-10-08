#!/usr/bin/env python3
"""Capture cinq vues réelles d'un cours en rédaction et produire un aperçu animé."""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.parse import urlsplit

from PIL import Image
from playwright.async_api import async_playwright


VIEWPORT = {"width": 1440, "height": 1000}
DURATION_MS = 5000
MAX_GIF_BYTES = 5 * 1024 * 1024
ATKINSON = "'Atkinson Hyperlegible Next','Atkinson Hyperlegible',system-ui,sans-serif"
VIEWS = (
    ("pA", "pathologie", "Pathologie et prise en charge"),
    ("pE", "examens", "Examens complémentaires"),
    ("pS", "sciences", "Sciences fondamentales"),
    ("pP", "pharmacologie", "Pharmacologie"),
)


async def settle(page):
    await page.evaluate("document.fonts.ready")
    await page.evaluate("new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)))")


async def align_tabs(page):
    await page.evaluate("""() => {
      const tabs=document.querySelector('.mc-tabs');
      const topbar=document.querySelector('.topbar');
      const top=topbar ? Math.max(0,topbar.getBoundingClientRect().bottom) : 0;
      scrollTo({top:Math.max(0,scrollY+tabs.getBoundingClientRect().top-top-14),behavior:'instant'});
    }""")
    await settle(page)


async def click_word(trigger):
    """Cliquer dans le texte peint d'un lien qui peut occuper plusieurs lignes."""
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


async def capture(args, directory):
    errors, frames = [], []
    code = args.code
    slug = code.lower()
    url = args.url.split("#", 1)[0] + "#/entry/" + code
    async with async_playwright() as playwright:
        launch = {"headless": True, "args": ["--no-sandbox", "--disable-dev-shm-usage"]}
        if args.browser_executable:
            launch["executable_path"] = str(args.browser_executable)
        browser = await playwright.chromium.launch(**launch)
        try:
            page = await browser.new_page(viewport=VIEWPORT, device_scale_factor=1,
                                          color_scheme="light", reduced_motion="reduce")
            page.set_default_timeout(15000)
            page.on("pageerror", lambda error: errors.append(str(error)))
            response = await page.goto(url, wait_until="domcontentloaded", timeout=60000)
            if response and not response.ok:
                raise RuntimeError(f"Page inaccessible : HTTP {response.status}")
            await page.wait_for_function("window.MDN_READY===true", timeout=60000)
            course = page.locator(f'.mc[data-code="{code}"]')
            await course.wait_for(state="visible")
            if await course.evaluate("el=>el.classList.contains('book')"):
                await page.locator('.mc-book').click()
            await page.locator('.mc-font').select_option(ATKINSON)
            await page.locator('.mc-size-toggle').click()
            await page.locator('.mc-size-range').evaluate("el=>el.value=19")
            await page.locator('.mc-size-range').dispatch_event("input")
            await page.keyboard.press("Escape")
            await settle(page)
            provenance = await page.evaluate("""() => ({url:location.href,
              work_preview:window.MEDINA_WORK_PREVIEW || null,
              font:getComputedStyle(document.querySelector('.mc-panel')).fontFamily})""")
            for number, (panel, view_slug, label) in enumerate(VIEWS, 1):
                await page.locator(f'.mc-tabs button[data-p="{panel}"]').click()
                if panel == "pS" and code == "B24":
                    await page.locator('.mc-sci-bar button[data-s="b24-s-physio"]').click()
                await align_tabs(page)
                active = course.locator('.mc-panel:not([hidden])')
                if await active.get_attribute("id") != panel:
                    raise RuntimeError(f"Onglet {panel} non actif")
                visible_text = await active.inner_text()
                if len(visible_text.strip()) < 100:
                    raise RuntimeError(f"Contenu clinique absent de {panel}")
                name = f"{slug}-{number:02d}-{view_slug}.png"
                await page.screenshot(path=str(directory / name), full_page=False)
                frames.append({"file": name, "label": label, "panel": panel,
                               "visible_text_characters": len(visible_text.strip())})
                print(f"Capture réelle : {label}", flush=True)

                if panel == "pA" and code == "B24":
                    # Montrer la définition clinique, au-delà de la vue d'ouverture.
                    target = active.locator("#b24-pa-1 h2").first
                    await target.evaluate("""el => scrollTo({
                      top: Math.max(0, scrollY + el.getBoundingClientRect().top - 600),
                      behavior: 'instant'
                    })""")
                    await settle(page)
                    detail_name = "b24-passage-maladie-avancee.png"
                    await page.screenshot(path=str(directory / detail_name),
                                          clip={"x": 280, "y": 350, "width": 900, "height": 570})
                    provenance["detail_capture"] = {"file": detail_name,
                                                    "section": "b24-pa-1",
                                                    "heading": (await target.inner_text()).strip()}
                    print("Capture réelle : maladie avancée B24", flush=True)

            # Le premier médicament de l'onglet actif ouvre une explication native.
            trigger = course.locator('.mc-panel:not([hidden]) [data-k]').first
            key = await trigger.get_attribute("data-k")
            await click_word(trigger)
            dialog = page.locator('.mc-dlg[open]')
            await dialog.wait_for(state="visible")
            title = (await dialog.locator('#mc-dlg-t').inner_text()).strip()
            body = (await dialog.locator('.mc-dlg-b').inner_text()).strip()
            if len(body) < 100 or "Fiche absente." in body:
                raise RuntimeError("La fenêtre explicative n'affiche pas son contenu")
            await settle(page)
            name = f"{slug}-05-explication.png"
            await page.screenshot(path=str(directory / name), full_page=False)
            frames.append({"file": name, "label": "Fenêtre explicative ouverte", "panel": "pP",
                           "popup_key": key, "popup_title": title,
                           "visible_text_characters": len(body)})
            print(f"Capture réelle : explication « {title} »", flush=True)
            if errors:
                raise RuntimeError("Erreurs JavaScript : " + "; ".join(errors))
            return {"captured_at_utc": datetime.now(timezone.utc).isoformat(),
                    "chapter_code": code,
                    "browser_version": browser.version, "viewport": VIEWPORT,
                    "duration_per_frame_ms": DURATION_MS, "frames": frames, **provenance}
        finally:
            await browser.close()


def assemble(directory, report):
    originals = [Image.open(directory / frame["file"]).convert("RGB") for frame in report["frames"]]
    slug = report["chapter_code"].lower()
    gif = directory / f"{slug}-apercu-anime.gif"
    try:
        for colors in (256, 192, 128):
            images = [image.quantize(colors=colors, method=Image.Quantize.MEDIANCUT) for image in originals]
            images[0].save(gif, save_all=True, append_images=images[1:], duration=DURATION_MS,
                           loop=0, disposal=2, optimize=True)
            for image in images:
                image.close()
            if gif.stat().st_size <= MAX_GIF_BYTES:
                break
        if gif.stat().st_size > MAX_GIF_BYTES:
            raise RuntimeError("L'animation dépasse la limite de 5 Mio")
        with Image.open(gif) as animation:
            if animation.n_frames != 5 or animation.size != (1440, 1000):
                raise RuntimeError("Métadonnées de l'animation incorrectes")
            for number in range(animation.n_frames):
                animation.seek(number)
                if animation.info.get("duration") != DURATION_MS:
                    raise RuntimeError("Durée d'une image incorrecte")
        contact = Image.new("RGB", (2160, 1000), "white")
        for number, original in enumerate(originals):
            thumbnail = original.resize((720, 500), Image.Resampling.LANCZOS)
            contact.paste(thumbnail, ((number % 3) * 720, (number // 3) * 500))
            thumbnail.close()
        contact.save(directory / f"{slug}-planche-contact.png", optimize=True)
        contact.close()
        report["animation"] = {"file": gif.name, "frames": 5, "bytes": gif.stat().st_size,
                               "colors": colors, "sha256": hashlib.sha256(gif.read_bytes()).hexdigest()}
        (directory / f"{slug}-animation.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    finally:
        for original in originals:
            original.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", required=True, help="URL HTTP(S) ou file:// de l'aperçu Infectiologie")
    parser.add_argument("--code", choices=("B24", "B18", "A54", "A53", "B50", "A04"), default="B24", help="Cours à montrer")
    parser.add_argument("--output", required=True, type=Path, help="Dossier des PNG, GIF et preuves")
    parser.add_argument("--browser-executable", type=Path, help="Navigateur Chromium local facultatif")
    args = parser.parse_args()
    if urlsplit(args.url).scheme not in {"http", "https", "file"}:
        parser.error("L'URL doit commencer par http://, https:// ou file://")
    args.output.mkdir(parents=True, exist_ok=True)
    try:
        with TemporaryDirectory(prefix=args.code.lower() + "-animation-", dir=args.output) as temporary:
            directory = Path(temporary)
            report = asyncio.run(capture(args, directory))
            assemble(directory, report)
            for path in directory.iterdir():
                path.replace(args.output / path.name)
        print(f"Animation prête : {args.output / (args.code.lower() + '-apercu-anime.gif')} ({report['animation']['bytes']} octets)")
    except Exception as error:
        print(f"Échec de la capture : {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
