#!/usr/bin/env python3
"""Vérifie les verrous du carnet HTML ; ne réalise aucun audit médical."""
import argparse
import functools
import io
import json
import shutil
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from playwright.sync_api import sync_playwright


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_):
        pass


def main():
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument("--html", type=Path, required=True)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--pdf", type=Path)
    parser.add_argument("--captures", type=Path)
    args = parser.parse_args()
    path = args.html.resolve()
    server = ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(QuietHandler, directory=str(path.parent)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    url = f"http://127.0.0.1:{server.server_port}/{path.name}"
    checks = []
    with sync_playwright() as pw:
        options = {"headless": True, "args": ["--no-sandbox"]}
        if shutil.which("chromium"):
            options["executable_path"] = shutil.which("chromium")
        browser = pw.chromium.launch(**options)
        context = browser.new_context(viewport={"width": 1360, "height": 1000}, accept_downloads=True)
        page = context.new_page()
        errors = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.goto(url, wait_until="networkidle")
        page.evaluate("document.fonts.ready")
        assert page.locator("[data-cycle]").count() == 30
        assert page.locator("[data-chapter-card]").count() == 120
        assert page.locator("[data-inventory-row]").count() == 270
        assert page.locator("[data-preflight='1']").is_enabled()
        assert page.locator("[data-preflight='2']").is_disabled()
        assert page.locator("[data-stage='injected']:checked").count() == 0
        checks.append("30 cycles / 120 missions / 270 catégories ; état initial non démarré")
        for width in [1360, 390]:
            page.set_viewport_size({"width": width, "height": 1000})
            result = page.evaluate("""()=>({overflow:document.documentElement.scrollWidth>innerWidth,
                bars:[...document.querySelectorAll('.red-bar')].map(b=>({height:b.getBoundingClientRect().height,color:getComputedStyle(b).backgroundColor})),
                font:getComputedStyle(document.body).fontFamily,
                fontReady:document.fonts.check('17px "Atkinson Hyperlegible Next"'),
                blues:[...document.querySelectorAll('body *')].filter(e=>!['SCRIPT','STYLE'].includes(e.tagName)).map(e=>getComputedStyle(e).color).filter(c=>{const a=c.match(/\\d+/g)?.map(Number)||[];return a[2]>a[0]+25&&a[2]>a[1]+25;})})""")
            assert not result["overflow"], width
            assert len(result["bars"]) == 30
            assert all(abs(b["height"] - 96 / 2.54 * 0.5) < 0.1 and b["color"] == "rgb(179, 38, 30)" for b in result["bars"])
            assert result["fontReady"] and "Atkinson Hyperlegible Next" in result["font"]
            assert not result["blues"], result["blues"][:3]
            if args.captures:
                args.captures.mkdir(parents=True, exist_ok=True)
                page.screenshot(path=str(args.captures / f"plan-{width}.png"), full_page=False)
                page.locator("#cycle-1").screenshot(path=str(args.captures / f"cycle-1-{width}.png"))
            checks.append(f"Largeur {width} : police embarquée, aucun bleu, aucun débordement, 30 barrières de 0,5 cm")
        page.set_viewport_size({"width": 1360, "height": 1000})
        data = json.loads(page.locator("#plan-data").text_content())
        first = data["cycles"][0]["chapters"]
        selector = lambda cid, stage: f"[data-key='{cid}:{stage}']"
        page.locator("[data-preflight='1']").check()
        for i, chapter in enumerate(first):
            cid = chapter["id"]
            page.locator(selector(cid, "sources")).check()
            page.locator(selector(cid, "production")).check()
            if i < 3:
                assert page.locator(selector(first[0]["id"], "audit1")).is_disabled()
        for i, chapter in enumerate(first):
            cid = chapter["id"]
            page.locator(selector(cid, "audit1")).check()
            page.locator(selector(cid, "audit2")).check()
            if i < 3:
                assert page.locator(selector(first[0]["id"], "counter1")).is_disabled()
        for chapter in first:
            for stage in ["counter1", "counter2"]:
                page.locator(selector(chapter["id"], stage)).check()
        assert page.locator(selector(first[0]["id"], "control")).is_disabled()
        for chapter in first:
            cid = chapter["id"]
            page.locator(f"[data-evidence='{cid}']").fill("Dossier de preuves fictif de test : sources, audits et SHA ; aucune injection réelle.")
            page.locator(selector(cid, "control")).check()
        assert page.locator(selector(first[1]["id"], "injected")).is_disabled()
        for chapter in first:
            page.locator(selector(chapter["id"], "injected")).check()
        assert page.locator("[data-preflight='2']").is_disabled()
        for gate, _ in data["gates"]:
            page.locator(f"[data-key='cycle1:{gate}']").check()
        assert page.locator("[data-preflight='2']").is_enabled()
        page.locator("[data-preflight='2']").check()
        page.reload(wait_until="networkidle")
        assert page.locator("[data-preflight='2']").is_checked()
        checks.append("Audit après quatre productions ; contre-audit après audit corrigé ; preuves requises ; quatre injections séquentielles ; passage après quatre clôtures ; persistance après rechargement")
        page.locator(selector(first[0]["id"], "audit1")).uncheck()
        assert not page.locator("[data-preflight='2']").is_checked()
        assert page.locator("[data-preflight='2']").is_disabled()
        assert page.locator("[data-stage='injected']:checked").count() == 0
        checks.append("Réouverture d’une réserve : étapes dépendantes et cycle suivant invalidés")
        # Un import ne peut sauter les dépendances, même avec une version correcte.
        invalid = {"version": data["plan"]["id"], "checks": {"cycle30:preflight": True}, "evidence": {}}
        page.locator("#import-state").set_input_files({"name": "invalid.json", "mimeType": "application/json", "buffer": json.dumps(invalid).encode()})
        page.wait_for_function("document.getElementById('feedback').textContent.includes('Import refusé')")
        assert page.locator("[data-preflight='30']").is_disabled()
        checks.append("Import qui contourne un verrou refusé")
        # Parcours complet des 30 cycles par les événements publics des contrôles.
        page.evaluate("localStorage.clear()")
        page.reload(wait_until="networkidle")
        page.evaluate("""()=>{
          const d=JSON.parse(document.getElementById('plan-data').textContent);
          const check=k=>{const b=document.querySelector(`[data-key="${k}"]`);if(b.disabled)throw Error('Verrou inattendu : '+k);b.click();};
          for(const c of d.cycles){const n=c.number;check(`cycle${n}:preflight`);
            for(const ch of c.chapters)for(const s of ['sources','production'])check(`${ch.id}:${s}`);
            for(const ch of c.chapters)for(const s of ['audit1','audit2'])check(`${ch.id}:${s}`);
            for(const ch of c.chapters)for(const s of ['counter1','counter2'])check(`${ch.id}:${s}`);
            for(const ch of c.chapters){const t=document.querySelector(`[data-evidence="${ch.id}"]`);t.value='Dossier de preuves de test, sans production ou injection médicale réelle.';t.dispatchEvent(new Event('input',{bubbles:true}));check(`${ch.id}:control`);}
            for(const ch of c.chapters)check(`${ch.id}:injected`);
            for(const [g]of d.gates)check(`cycle${n}:${g}`);
          }
        }""")
        assert page.locator("[data-stage='injected']:checked").count() == 120
        assert "30 / 30" in page.locator("#progress-label").text_content()
        with page.expect_download() as dl:
            page.locator("#export-state").click()
        exported = json.loads(Path(dl.value.path()).read_text())
        assert sum(k.endswith(":injected") for k, v in exported["checks"].items() if v) == 120
        page.evaluate("localStorage.clear()")
        page.reload(wait_until="networkidle")
        page.locator("#import-state").set_input_files({"name": "valid.json", "mimeType": "application/json", "buffer": json.dumps(exported).encode()})
        page.wait_for_function("document.getElementById('feedback').textContent.includes('a été importé')")
        assert page.locator("[data-stage='injected']:checked").count() == 120
        checks.append("Parcours complet : 120 missions et 30 clôtures ; export/import fidèle")
        page.locator("#category-system").select_option("S08")
        assert page.locator("[data-inventory-row]:visible").count() == 116
        page.locator("#category-search").fill("SclÉrose en plaques")
        assert page.locator("[data-inventory-row]:visible").count() == 1
        checks.append("Filtres de l’inventaire et recherche accentuée")
        assert not errors, errors
        if args.pdf:
            fresh = browser.new_context(viewport={"width": 1360, "height": 1000})
            print_page = fresh.new_page()
            print_page.goto(url, wait_until="networkidle")
            print_page.evaluate("document.fonts.ready")
            args.pdf.parent.mkdir(parents=True, exist_ok=True)
            print_page.pdf(path=str(args.pdf), format="A4", print_background=True, prefer_css_page_size=True, scale=1, tagged=True, outline=True)
            # Même police dans la pagination que dans le corps du document.
            import fitz
            from fontTools.ttLib import TTFont
            font = TTFont(Path(__file__).resolve().parents[1] / "shell/fonts/ahn-400.woff2")
            font.flavor = None
            buffer = io.BytesIO()
            font.save(buffer)
            font_bytes = buffer.getvalue()
            regular = fitz.Font(fontbuffer=font_bytes)
            pdf = fitz.open(args.pdf)
            for number, sheet in enumerate(pdf, 1):
                sheet.insert_font(fontname="AHNplan", fontbuffer=font_bytes)
                color = (21 / 255, 63 / 255, 37 / 255)
                # Chromium arrondit parfois la hauteur peinte au pixel : la barre
                # PDF est tracée en points pour garantir exactement cinq millimètres.
                for drawing in sheet.get_drawings():
                    fill = drawing.get("fill")
                    rect = drawing["rect"]
                    if fill and fill[0] > 0.6 and fill[1] < 0.2 and fill[2] < 0.2 and rect.width > 400 and 12 < rect.height < 16:
                        bar = fitz.Rect(rect.x0, rect.y0, rect.x1, rect.y0 + 72 / 25.4 * 5)
                        sheet.draw_rect(bar, color=None, fill=(179 / 255, 38 / 255, 30 / 255), overlay=True)
                sheet.insert_text((31, sheet.rect.height - 19), "MEDINA · Progression de la tétrade · 11 octobre 2026", fontname="AHNplan", fontsize=8, color=color)
                label = f"{number} / {len(pdf)}"
                sheet.insert_text((sheet.rect.width - 31 - regular.text_length(label, fontsize=8), sheet.rect.height - 19), label, fontname="AHNplan", fontsize=8, color=color)
            paginated = args.pdf.with_suffix(".paginated.pdf")
            pdf.save(paginated, garbage=4, deflate=True)
            pdf.close()
            paginated.replace(args.pdf)
            fresh.close()
            checks.append("PDF A4 à 100 %, police et pagination Atkinson, barrières vectorielles de 5 mm, version initiale sans suivi de test")
        browser.close()
    server.shutdown()
    result = {"medical_audit": False, "checks": checks, "javascript_errors": errors}
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
