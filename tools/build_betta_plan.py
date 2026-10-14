#!/usr/bin/env python3
"""Plan Betta : cycles 31 à n, huit leçons fédérales par cycle (4 agents × 2 leçons).

Reliquat des Leçons Examen fédéral (étoile SSP/PROFILES) des quatre systèmes de la
tétrade, non programmées dans les 30 premiers cycles. Aucune source médicale modifiée.
"""
import argparse, base64, html, json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from build_tetrade_plan import load_data, source_targets  # noqa: E402

OUT = ROOT / "organisation/progression/plan-betta-cycles"
ORDER = ["S08", "S05", "S04", "S06"]
TAG = {"S08": "NEUR", "S05": "ENDO", "S04": "NEPH", "S06": "HEM"}
PRIO = {"S08": ["I6", "G0", "G2", "G3", "G5", "G6", "G7", "G8", "G9", "C7", "R", "Q", "S"],
        "S05": ["E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7", "C7"], "S04": ["N"], "S06": ["D", "C8", "C9", "C7"]}
NAMES = ["Relier vaisseaux, iode, interstitium et moelle", "Prévenir les occlusions et les carences thyroïdiennes",
         "Diagnostiquer les méningites et les diabètes particuliers", "Distinguer encéphalites, glandes et lymphomes rares",
         "Reconnaître abcès, hormones et leucémies", "Maîtriser l’extrapyramidal et la dénutrition",
         "Comprendre la démyélinisation et les nerfs crâniens", "Explorer mononévrites et polyneuropathies",
         "Traiter muscles, vitamines et paralysies", "Relier paralysies, système autonome et liquide cérébrospinal",
         "Compléter l’encéphale, les carences et les tumeurs du névraxe", "Lire les symptômes moteurs, la parole et les minéraux",
         "Comprendre les malformations et la nutrition", "Prévenir le tube neural et l’obésité",
         "Reconnaître les lésions nerveuses et les erreurs innées", "Approfondir les nerfs des membres et le métabolisme",
         "Clore la série Betta par les tumeurs endocrines"]
STAGES = [("research", "Recherche · Opus 5.5"), ("writing", "Rédaction · Sonnet 5.5"),
          ("checks", "Contrôles techniques"), ("injected", "Injecté et publié")]


def build(root=ROOT):
    base = load_data(root)
    meta = {r["code"]: (inv, r) for inv in base["inventories"] for r in inv["rows"]}
    pairs = {}
    for inv in base["inventories"]:
        fid = inv["fragment"]
        rows = [r for r in inv["rows"] if r["federal"] and r["cycle"] is None and r["root"] == r["code"]]
        rows.sort(key=lambda r: (next(i for i, x in enumerate(PRIO[fid]) if r["code"].startswith(x)), r["code"]))
        codes = [r["code"] for r in rows]
        pairs[fid] = [codes[i:i + 2] for i in range(0, len(codes), 2)]
    cycles, n = [], 31
    while any(pairs.values()):
        slots = [(s, pairs[s].pop(0)) for s in ORDER if pairs[s]]
        while len(slots) < 4 and any(pairs.values()):
            s = max(ORDER, key=lambda s: len(pairs[s]))
            slots.append((s, pairs[s].pop(0)))
        agents = []
        for k, (fid, codes) in enumerate(slots, 1):
            aid = f"C{n}-A{k}-{TAG[fid]}"
            lessons = []
            for j, code in enumerate(codes, 1):
                inv, r = meta[code]
                lessons.append({"id": f"c{n}-{code}", "code": code, "title": r["title"], "block": r["block"],
                                "order": j, "fragment": fid, "label": inv["label"], "system": inv["system"],
                                "frequent": r["frequent"], "sources": source_targets(fid, code),
                                "focus": f"Monographie complète de {code} — {r['title']} : définition, classifications, mécanismes, clinique, examens, diagnostic différentiel, prise en charge suisse et suivi ; sous-codes CIM-10-GM couverts.",
                                "url": f"https://vialdjoukang-spec.github.io/Medina/fragments/#/entry/{code}"})
            agents.append({"id": aid, "fragment": fid, "tag": TAG[fid], "label": lessons[0]["label"],
                           "research_model": "Opus 5.5", "writing_model": "Sonnet 5.5", "lessons": lessons})
        cycles.append({"number": n, "name": NAMES[n - 31] if n - 31 < len(NAMES) else f"Cycle {n}", "agents": agents,
                       "lessons": sum(len(a["lessons"]) for a in agents)})
        n += 1
    total = sum(c["lessons"] for c in cycles)
    summ = [{"fragment": f, "label": next(i["label"] for i in base["inventories"] if i["fragment"] == f),
             "lessons": sum(len(a["lessons"]) for c in cycles for a in c["agents"] if a["fragment"] == f)} for f in ORDER]
    return {"id": "medina-betta-31-20261014-v1", "date": "2026-10-14", "first": 31, "last": cycles[-1]["number"],
            "total_lessons": total, "summaries": summ, "stages": STAGES, "cycles": cycles,
            "basis": "Leçons Examen fédéral (étoile SSP/PROFILES 2017) des quatre systèmes non programmées dans les cycles 1 à 30 : organisation/progression/plan-tetrade-30-cycles.json."}


def render(d):
    e = html.escape
    fonts = "".join("@font-face{font-family:'AHN';font-style:%s;font-weight:%s;src:url(data:font/woff2;base64,%s) format('woff2')}" %
                    (st, w, base64.b64encode((ROOT / "shell/fonts" / f).read_bytes()).decode())
                    for f, st, w in [("ahn-400.woff2", "normal", "400"), ("ahn-700.woff2", "normal", "700")])
    rows = "".join(f"<tr><th>{e(s['label'])}</th><td>{s['lessons']}</td></tr>" for s in d["summaries"])
    toc = "".join(f"<a href='#c{c['number']}'>{c['number']}</a>" for c in d["cycles"])
    cyc = []
    for c in d["cycles"]:
        cards = []
        for a in c["agents"]:
            ls = "".join(f"""<div class="lesson"><p class="code"><b>Leçon {l['order']} · {l['code']} — {e(l['title'])}</b></p>
              <p class="mission">{e(l['focus'])}</p><p class="src"><b>Sources :</b> {e(l['sources'])}</p>
              <p class="steps">{''.join(f'<span>☐ {e(v)}</span>' for _, v in STAGES)}</p></div>""" for l in a["lessons"])
            cards.append(f"""<article class="agent"><p class="sys">{e(a['label'])}</p><h3>Agent {a['id']}</h3>
              <p class="models">Recherche : <b>{a['research_model']}</b> → Rédaction : <b>{a['writing_model']}</b> · leçons traitées l’une après l’autre</p>{ls}</article>""")
        cyc.append(f"""<section class="cycle" id="c{c['number']}"><p class="eyebrow">Cycle {c['number']} / {d['last']} · {c['lessons']} leçons · {len(c['agents'])} agents</p>
          <h2>Cycle {c['number']} : {e(c['name'])}</h2><div class="grid">{''.join(cards)}</div>
          <p class="gate">Clôture : 8 leçons injectées, fragments reconstruits, publication vérifiée, jauge cochée. Audit différé.</p><div class="bar"></div></section>""")
    return f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>MEDINA — Cycles Betta {d['first']} à {d['last']}</title><style>{fonts}
:root{{--ink:#153f25;--muted:#31593f;--red:#b3261e;--green:#176331;--lime:#daff93;--line:#84b875;--tint:#f0ffe4}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--tint);color:var(--ink);font-family:AHN,Arial,sans-serif;font-size:15px;line-height:1.45}}
.wrap{{max-width:1100px;margin:auto;padding:0 16px}}.hero{{background:var(--ink);color:#fff;padding:32px;border-radius:14px;margin:18px 0}}
.hero h1{{font-size:38px;margin:10px 0;color:var(--lime)}}.eyebrow{{text-transform:uppercase;letter-spacing:.08em;font-size:12px;color:var(--muted);margin:0}}
.hero .eyebrow{{color:var(--lime)}}table{{border-collapse:collapse;width:100%;background:#fff}}td,th{{border:1px solid var(--line);padding:6px 9px;text-align:left}}
.section{{background:#fff;border:1px solid var(--line);border-radius:12px;padding:18px;margin:14px 0}}.toc a{{display:inline-block;margin:3px;padding:4px 9px;border:1px solid var(--line);border-radius:7px;color:var(--green);text-decoration:none;font-weight:700}}
.cycle{{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px;margin:16px 0;break-inside:auto}}.cycle h2{{margin:4px 0 10px;color:var(--ink)}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:10px}}.agent{{border:1px solid var(--line);border-left:5px solid var(--green);border-radius:9px;padding:9px 11px;break-inside:avoid}}
.agent h3{{margin:2px 0;font-size:16px}}.sys{{margin:0;font-size:12px;color:var(--muted);font-weight:700}}.models{{font-size:12.5px;margin:3px 0 6px}}
.lesson{{border-top:1px dashed var(--line);padding-top:5px;margin-top:5px}}.lesson p{{margin:2px 0}}.code{{color:var(--red)}}.mission,.src{{font-size:12.5px}}
.steps span{{display:inline-block;font-size:11.5px;margin-right:9px;color:var(--muted)}}.gate{{font-size:13px;margin:10px 0 6px}}.bar{{height:.5cm;background:var(--red);border-radius:2px}}
@media(max-width:760px){{.grid{{grid-template-columns:1fr}}.hero h1{{font-size:28px}}}}
@page{{size:A4;margin:11mm}}@media print{{body{{background:#fff;font-size:9.5pt}}*{{print-color-adjust:exact;-webkit-print-color-adjust:exact}}.cycle{{break-before:page}}.hero{{break-after:page;min-height:250mm}}.mission,.src{{font-size:8.3pt}}.agent h3{{font-size:10.5pt}}}}
</style></head><body><main class="wrap">
<section class="hero"><p class="eyebrow">Instruction du Dr Vial · 14 octobre 2026 · série Betta</p><h1>Cycles {d['first']} à {d['last']}</h1>
<p>Neurologie · Endocrinologie et métabolisme · Néphrologie · Hématologie</p>
<p><b>{d['total_lessons']} Leçons Examen fédéral</b> restantes après la première trentaine, en {len(d['cycles'])} cycles de huit leçons : quatre agents, deux leçons par agent, un seul fragment par agent. Chaque leçon passe d’abord par la recherche (Opus 5.5), puis par la rédaction de haute qualité (Sonnet 5.5) ; l’agent enchaîne ensuite sa seconde leçon. Injection et publication au fil de l’eau ; audit différé.</p>
<p>Lorsqu’un système est épuisé, ses places d’agent reviennent au système le plus chargé, sans jamais mêler deux fragments chez un même agent. Le dernier cycle porte le reliquat.</p></section>
<section class="section"><h2>Répartition des leçons</h2><table><tr><th>Fragment</th><th>Leçons Betta</th></tr>{rows}<tr><th>Total</th><td>{d['total_lessons']}</td></tr></table>
<p>Base : {e(d['basis'])}</p><p class="toc">{toc}</p></section>
<section class="section"><h2>Chaîne d’un agent</h2><p>1. Recherche Opus 5.5 : dossier de sources réellement lues (suisses, puis européennes ; FI Swissmedic pour chaque médicament), sous-codes et plan monographique. 2. Rédaction Sonnet 5.5 : quatre onglets, fenêtres, glossaire, critères formels et paramètres clés, Pareto. 3. Contrôles techniques (glossaire, construction, navigateur). 4. Injection dans <code>chapters/</code>, reconstruction des fragments, publication. 5. Seconde leçon. Commande : <code>/cycle_Betta-medina &lt;n&gt;</code>.</p></section>
{''.join(cyc)}</main></body></html>"""


def main():
    ap = argparse.ArgumentParser(__doc__)
    ap.add_argument("--pdf", action="store_true")
    a = ap.parse_args()
    d = build()
    OUT.with_suffix(".json").write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
    OUT.with_suffix(".html").write_text(render(d))
    if a.pdf:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            b = p.chromium.launch(executable_path=next((str(x) for x in Path("/opt/pw-browsers").glob("chromium-*/chrome-linux*/chrome")), None)); pg = b.new_page()
            pg.goto(OUT.with_suffix(".html").as_uri()); pg.wait_for_timeout(500)
            pg.pdf(path=str(OUT.with_suffix(".pdf")), format="A4", print_background=True); b.close()
    print(f"Betta : cycles {d['first']}–{d['last']}, {d['total_lessons']} leçons.")


if __name__ == "__main__":
    main()
