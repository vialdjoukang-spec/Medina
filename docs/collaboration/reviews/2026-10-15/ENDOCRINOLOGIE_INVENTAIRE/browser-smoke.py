#!/usr/bin/env python3
"""Parcours borné des cours publiés S05 : routes, onglets et une fenêtre par onglet."""
import json
from pathlib import Path
import sys
from playwright.sync_api import sync_playwright

OUT = Path(__file__).resolve().parent
URL = sys.argv[1]
codes = [row["code"] for row in json.loads((OUT / "inventory.json").read_text())["categories"]
         if row["state_at_snapshot"] == "publie_avant_mission"]
result = {"url": URL, "routes": [], "errors": [], "scope": "Contrôle technique ; aucun audit médical"}
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/usr/bin/chromium")
    for width, height in [(1300, 900), (390, 844)]:
        page = browser.new_page(viewport={"width": width, "height": height})
        page.set_default_timeout(7000)
        page.on("pageerror", lambda error: result["errors"].append(str(error))
                if "lesson-core" not in str(error) else None)
        for code in codes:
            row = {"code": code, "viewport": [width, height], "tabs": [], "popups_opened": 0}
            result["routes"].append(row)
            try:
                page.goto(URL + "#/entry/" + code)
                page.wait_for_selector('.mc[data-code="' + code + '"]')
                assert page.locator(".mc h1").inner_text().strip(), "Titre de cours vide"
                for tab in ["pA", "pE", "pS", "pP"]:
                    page.locator('.mc-tabs button[data-p="' + tab + '"]').click()
                    panel = page.locator('.mc .mc-panel#' + tab + ':not([hidden])')
                    assert panel.count() == 1, "Onglet non affiché : " + tab
                    assert panel.inner_text().strip(), "Onglet vide : " + tab
                    row["tabs"].append(tab)
                    key = panel.locator(".mc-w").filter(visible=True).first
                    if key.count():
                        key.click()
                        page.wait_for_selector("dialog.mc-dlg[open]")
                        assert "Fiche absente" not in page.locator(".mc-dlg-b").inner_text()
                        row["popups_opened"] += 1
                        page.keyboard.press("Escape")
                row["scroll_width"] = page.evaluate("document.documentElement.scrollWidth")
                if width == 390:
                    assert row["scroll_width"] <= width + 2, "Débordement horizontal mobile"
                row["ok"] = True
            except Exception as exc:
                row["ok"] = False
                row["error"] = str(exc)
            print(code, width, "OK" if row["ok"] else "ECHEC", flush=True)
        page.close()
    browser.close()
result["ok"] = all(row["ok"] for row in result["routes"]) and not result["errors"]
result["route_count"] = len(result["routes"])
result["tab_count"] = sum(len(row["tabs"]) for row in result["routes"])
result["popup_count"] = sum(row["popups_opened"] for row in result["routes"])
(OUT / "browser-smoke.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({key: result[key] for key in ["ok", "route_count", "tab_count", "popup_count"]}))
raise SystemExit(0 if result["ok"] else 1)
