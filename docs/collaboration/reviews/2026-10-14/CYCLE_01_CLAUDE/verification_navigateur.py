#!/usr/bin/env python3
"""Contrôle technique réel des quatre cours du Cycle 1 (reprise Claude, 14 octobre 2026).

Usage : python3 docs/collaboration/reviews/2026-10-14/CYCLE_01_CLAUDE/verification_navigateur.py
Construit les quatre fragments, assemble un site local identique à GitHub Pages, ouvre chaque cours
à 1440 px et à 390 px, parcourt les quatre onglets, vérifie chaque fenêtre (cours et fenêtres imbriquées),
chaque image, l'encre bleue renforcée, le débordement horizontal et les erreurs JavaScript.
Écrit controle_technique.json à côté de ce script ; aucun verdict médical.
"""
import datetime, functools, hashlib, http.server, json, os, shutil, subprocess, sys, tempfile, threading
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[5]
HERE = Path(__file__).resolve().parent
RECEIPT = ROOT / "organisation/CYCLE_01_REPRISE_CLAUDE_2026-10-13.json"
COURSES = {"I63": "S08", "E11": "S05", "N17": "S04", "D50": "S06"}
INK, TERM, TITLE = "rgb(15, 44, 102)", "rgb(155, 57, 0)", "rgb(179, 38, 30)"


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    files = {p: sha(ROOT / p) for p in json.loads(RECEIPT.read_text())["files"]}
    work = Path(tempfile.mkdtemp(prefix="medina-c1-"))
    env = dict(os.environ, MEDINA_OUT=str(work / "dist"))
    for frag in sorted(set(COURSES.values())):
        subprocess.run([sys.executable, "build_front.py", "--fragment", frag], cwd=ROOT, env=env, check=True,
                       stdout=subprocess.DEVNULL)
    site = work / "site"
    shutil.copytree(work / "dist/fragments", site / "fragments")
    if (ROOT / "assets/img").is_dir():
        shutil.copytree(ROOT / "assets/img", site / "fragments/assets/img")
    pages = {f: next((site / "fragments").glob(f"MEDINA_{f}_*.html")).name for f in set(COURSES.values())}
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass
    handler = functools.partial(Quiet, directory=str(site))
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{srv.server_address[1]}/fragments/"
    caps = HERE / "captures"
    caps.mkdir(exist_ok=True)
    report = {"scope": "Contrôle technique navigateur ; aucun audit médical ni validation humaine.",
              "started_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "files": files, "surfaces": [], "failures": []}
    js_all, missing_all = [], []
    with sync_playwright() as p:
        exe = os.environ.get("MEDINA_CHROMIUM") or next((x for x in ("/opt/pw-browsers/chromium", "/usr/bin/chromium") if Path(x).exists()), None)
        b = p.chromium.launch(executable_path=exe, args=["--no-sandbox", "--disable-dev-shm-usage"])
        for vp, (w, h) in {"desktop": (1440, 1000), "mobile": (390, 844)}.items():
            for code, frag in COURSES.items():
                pg = b.new_page(viewport={"width": w, "height": h})
                errs = []
                pg.on("pageerror", lambda e: errs.append(str(e)))
                pg.goto(base + pages[frag] + "#/entry/" + code, wait_until="domcontentloaded")
                pg.wait_for_function("window.MDN_READY===true", timeout=60000)
                pg.locator(f'.mc[data-code="{code}"]').wait_for()
                pg.evaluate("document.fonts.ready")
                tabs = pg.locator(".mc-tabs button[data-p]").evaluate_all("e=>e.map(x=>x.dataset.p)")
                for t in tabs:
                    pg.locator(f'.mc-tabs button[data-p="{t}"]').click()
                    pg.wait_for_timeout(150)
                pg.locator('.mc-tabs button[data-p="pA"]').click()
                # Toutes les clés appelées dans le cours et dans les fenêtres doivent avoir leur fenêtre.
                state = pg.evaluate("""()=>{
                  const pops=new Set([...document.querySelectorAll('template[data-pop]')].map(t=>t.dataset.pop));
                  const keys=new Set([...document.querySelectorAll('.mc [data-k]')].map(e=>e.dataset.k));
                  document.querySelectorAll('template[data-pop]').forEach(t=>t.content.querySelectorAll('[data-k]').forEach(e=>keys.add(e.dataset.k)));
                  const imgs=[...document.querySelectorAll('.mc img')].map(i=>({src:i.getAttribute('src'),ok:i.complete&&i.naturalWidth>0,alt:!!i.alt}));
                  const p=document.querySelector('.mc .mc-panel p, .mc p');
                  return {keys:[...keys],missing:[...keys].filter(k=>!pops.has(k)),images:imgs,
                    active:document.documentElement.dataset.medinaActiveCycle,
                    ink:p?getComputedStyle(p).color:null,
                    overflow:document.documentElement.scrollWidth>innerWidth+2}}""")
                # Images différées : faire défiler chaque onglet pour forcer leur chargement réel.
                bad_img = []
                for t in tabs:
                    pg.locator(f'.mc-tabs button[data-p="{t}"]').click()
                    for im in pg.locator(".mc img:visible").all():
                        im.scroll_into_view_if_needed()
                        ok = im.evaluate("i=>new Promise(r=>{if(i.complete)return r(i.naturalWidth>0);i.onload=()=>r(true);i.onerror=()=>r(false);setTimeout(()=>r(i.naturalWidth>0),8000)})")
                        if not ok:
                            bad_img.append(im.get_attribute("src"))
                pg.locator('.mc-tabs button[data-p="pA"]').click()
                pg.evaluate("window.scrollTo(0,0)")
                c1 = caps / f"{code}-{vp}-ouverture.png"
                pg.screenshot(path=str(c1))
                # Ouvrir réellement chaque fenêtre et vérifier son contenu.
                opened, absent = 0, []
                for k in state["keys"]:
                    r = pg.evaluate("""k=>{MC_open({k},false);const b=document.querySelector('.mc-dlg-b');
                      const ok=document.getElementById('mc-dialog').open&&!/Fiche absente/.test(b.textContent)&&b.textContent.trim().length>20;
                      return ok}""", k)
                    opened += 1
                    if not r:
                        absent.append(k)
                first = state["keys"][0] if state["keys"] else None
                win = {}
                if first:
                    pg.evaluate("k=>{MC_open({k},false)}", first)
                    win = pg.evaluate("""()=>{const p=document.querySelector('.mc-dlg-b p');const hd=document.querySelector('#mc-dialog h3');
                      return {ink:p?getComputedStyle(p).color:null,title:hd?getComputedStyle(hd).color:null}}""")
                c2 = caps / f"{code}-{vp}-explication.png"
                pg.screenshot(path=str(c2))
                surf = {"code": code, "viewport": vp, "tabs": tabs, "windows": opened,
                        "missing_windows": sorted(set(state["missing"]) | set(absent)),
                        "images": len(state["images"]), "broken_images": bad_img,
                        "active_cycle": state["active"], "body_ink": state["ink"], "window_ink": win.get("ink"),
                        "window_title": win.get("title"), "overflow": state["overflow"], "javascript_errors": errs,
                        "captures": [{"path": str(c.relative_to(ROOT)), "sha256": sha(c)} for c in (c1, c2)]}
                report["surfaces"].append(surf)
                js_all += errs
                missing_all += surf["missing_windows"]
                if tabs != ["pA", "pE", "pS", "pP"]: report["failures"].append(f"{code} {vp} onglets {tabs}")
                if surf["missing_windows"]: report["failures"].append(f"{code} {vp} fenêtres {surf['missing_windows']}")
                if bad_img: report["failures"].append(f"{code} {vp} images {bad_img}")
                if state["active"] != "1" or state["ink"] != INK or (win and win.get("ink") not in (INK, None)):
                    report["failures"].append(f"{code} {vp} encre {state['active']} {state['ink']} {win.get('ink')}")
                if state["overflow"]: report["failures"].append(f"{code} {vp} débordement")
                if errs: report["failures"].append(f"{code} {vp} JavaScript {errs}")
                pg.close()
        b.close()
    srv.shutdown()
    report["javascript_errors"] = js_all
    report["missing_windows"] = sorted(set(missing_all))
    report["desktop"] = not any(" desktop " in f for f in report["failures"])
    report["mobile"] = not any(" mobile " in f for f in report["failures"])
    report["result"] = "passed" if not report["failures"] else "failed"
    report["medical_audit_performed"] = False
    report["finished_at"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    (HERE / "controle_technique.json").write_text(json.dumps(report, ensure_ascii=False, indent=1) + "\n")
    print(json.dumps({k: report[k] for k in ("result", "failures", "desktop", "mobile")}, ensure_ascii=False, indent=1))
    return 0 if report["result"] == "passed" else 1


if __name__ == "__main__":
    sys.exit(main())
