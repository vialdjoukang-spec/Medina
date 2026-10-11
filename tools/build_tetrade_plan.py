#!/usr/bin/env python3
"""Construit le plan de Vial ; aucune source médicale ni jauge n'est modifiée."""
import argparse
import base64
import hashlib
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "organisation/plan_tetrade_30_cycles.json"
ONLINE = "https://vialdjoukang-spec.github.io/Medina/"
REPO = "https://github.com/vialdjoukang-spec/Medina"
STAGES = [
    ("sources", "Sources et périmètre"), ("production", "Rédaction complète"),
    ("audit1", "Audit croisé · passe 1"), ("audit2", "Audit croisé · passe 2"),
    ("counter1", "Contre-audit · passe 1"), ("counter2", "Contre-audit · passe 2"),
    ("control", "Contrôle final Codex"), ("injected", "Injection publiée et vérifiée"),
]
GATES = [
    ("reserves", "Toutes les réserves bloquantes sont closes ; les rapports portent sur les empreintes finales."),
    ("captures", "Les deux captures réelles de chaque leçon sont conservées ; ordinateur et mobile sont contrôlés."),
    ("published", "Les quatre injections successives sont accessibles ; les jauges et renvois sont vérifiés."),
    ("receipt", "Le coordinateur a signé le reçu de cycle et la décision de passage, avec preuves et SHA."),
]

RULES = [
    ("Un cycle actif, quatre chapitres", "Chaque cycle attribue exactement un chapitre à chacun des quatre systèmes. Quatre auteurs travaillent chacun sur leur seul chapitre. Les quatre textes sont terminés avant l’audit croisé. Il n’existe aucune durée automatique, aucun quota quotidien et aucune autorisation de sauter un chapitre bloqué."),
    ("Un chapitre existant reste une reprise", "L’inventaire de main, de toutes les branches et PR paginées, des brouillons et des covers précède chaque démarrage. Un cours déjà présent est relu, corrigé ou complété ; il n’est pas recréé. Un sujet partiellement traité reçoit une matrice sous-code → passage → source → lacune. Un rattachement à un cours existant exige une couverture démontrée et auditée."),
    ("Production fondée sur les preuves", "Chaque affirmation médicale, mécanisme, chiffre, seuil, dose et décision provient d’un passage réellement lu. Le registre conserve URL, titre, version, date de consultation, page ou section, population et limites. Les sources suisses précèdent les européennes. Aucune recommandation américaine ne fonde une conduite ; un essai peut être analysé comme donnée. Une absence de source reste une lacune, jamais une affirmation de mémoire."),
    ("Contexte suisse et médicaments", "La recommandation suisse pertinente est confrontée au texte applicable. Chaque produit, forme, dose, voie, fréquence, durée, maximum et adaptation est vérifié dans l’information professionnelle suisse approuvée par Swissmedic, lue en texte intégral. Les usages hors indication sont explicites. Les divergences sont attribuées, arbitrées et tracées ; aucune notice inaccessible n’est reconstituée."),
    ("Quatre onglets et profondeur pédagogique", "Le chapitre comprend Pathologie, Examens, Sciences et Pharmacologie. Il suit le plan monographique : question clinique, définition, classifications, épidémiologie, mécanismes, causes, anamnèse, examen, diagnostic, urgences, prise en charge, suivi et situations particulières. Les critères formels et paramètres clés terminent la pathologie. Les mécanismes relient normal, perturbation et décision. Les figures, cas corrigés, fenêtres et Pareto utiles sont complets et sourcés ; les abréviations sont définies et cliquables."),
    ("Deux binômes croisés", "Le binôme NEUR ↔ HEM échange ses deux chapitres ; le binôme ENDO ↔ NEPH fait de même. Aucun auteur n’audite son propre texte. La passe 1 relève les écarts ; l’auteur les corrige. La passe 2 relit le texte corrigé intégralement et rattache son verdict à son empreinte. Le rapport vérifie rédaction, médecine, sources et frontend. Les auditeurs reçoivent le texte et les preuves, sans le raisonnement privé de l’auteur."),
    ("Contre-audit différé indépendant", "Après clôture des audits croisés, quatre nouveaux agents CA sont nommés et démarrent avec un contexte neuf. Ils n’ont ni rédigé ni audité au premier tour. Leur première passe recherche indépendamment erreurs et omissions ; leur seconde relit le résultat corrigé. Ils vérifient les quatre dimensions, tous les points à risque et au moins dix données clés si le chapitre en contient dix. Une erreur ou un changement significatif rouvre les audits concernés."),
    ("Contrôle final par le coordinateur", "Codex, coordinateur du fil, contrôle les rapports, l’indépendance des agents, les matrices de sources suisses, les corrections et les empreintes finales. La cible est 20/20 selon le Prompt ; aucune erreur médicale ni réserve bloquante n’est admise. Une réserve mineure exige une justification écrite, une note au moins égale à 19/20 et une décision motivée du coordinateur. Un score ne dispense d’aucun contrôle."),
    ("Injection strictement séquentielle", "Après les contre-audits, le coordinateur contrôle et injecte un seul chapitre à la fois : Neurologie → Endocrinologie et métabolisme → Néphrologie → Hématologie. Chaque injection possède son commit et son reçu ; sa construction, ses contrôles et son accès publié sont vérifiés avant la suivante. Un échec suspend le cycle ; le travail validé est conservé et toute correction passe par une version tracée."),
    ("Barrière rouge de 0,5 cm", "Le bandeau rouge plein mesure 0,5 cm en CSS et à l’impression à 100 %. Le cycle suivant reste interdit tant que les quatre chapitres ne sont pas injectés, publiés et vérifiés et que les quatre conditions de clôture ne sont pas satisfaites. Le Prompt de vérité est relu avant chaque cycle. Le cycle 30 porte une barrière de clôture finale ; il ne crée aucun cycle 31."),
    ("Contrôles techniques et conservation", "Les contrôles portent sur les sources consommées : glossaire sans abréviation non couverte, fenêtres et Pareto fonctionnels, quatre onglets, figures lisibles, zéro erreur JavaScript, zéro débordement mobile, renvois canoniques et absence de régression. Les tests Python du dépôt, les builds, les audits de fragments et les contrôles navigateur pertinents passent. Deux captures réelles, ouverture et fenêtre explicative, accompagnent chaque leçon. Les originaux, corrections et preuves sont conservés."),
    ("Règles graphiques distinctes", "Ce plan n’utilise aucune couleur bleue. Sa police est Atkinson Hyperlegible Next, celle des cours, embarquée dans le HTML et le PDF. Les futurs cours Codex auront un corps bleu contrasté, lisible et jamais noir ; leurs termes cliquables seront orange foncé. Ces exigences seront vérifiées sur les textes, tableaux, fenêtres et légendes des cours. La présente livraison ne recolore aucun cours existant."),
    ("Avant le premier cycle", "La présente consigne de Vial remplace, pour cette tétrade, les anciennes règles incompatibles de remise par fragment entier, d’interdiction de l’audit croisé ou d’injection avant le contrôle final. Les scripts historiques de production_plan.py et espace.py appliquent encore leur ancien protocole. Leur mise en cohérence documentée et testée avec cette consigne est une condition préalable à la première injection ; on ne désactive aucune garde pour contourner un refus. La publication de ce plan ne démarre pas les 120 missions."),
    ("Suivi déclaré et validation", "Les cases du HTML sont un carnet de suivi local. Elles ne rédigent, n’auditent, n’injectent et ne valident aucun cours sur GitHub. Les références de preuves restent obligatoires. Un utilisateur peut attester une étape ; seul le dossier de preuves et le contrôle du coordinateur permettent le passage réel. Toute revue d’IA et tout test technique restent distincts d’une validation médicale humaine."),
]


def source_targets(system, code):
    if system == "S08":
        if code.startswith("I"):
            return "Société suisse de neurologie / Société cérébrovasculaire suisse ; European Stroke Organisation ; FI Swissmedic."
        if code.startswith("C"):
            return "Références suisses de neuro-oncologie ; EANO / ESMO ; FI Swissmedic."
        if code.startswith("S"):
            return "Références suisses de neurotraumatologie, Suva ; recommandations européennes applicables ; FI Swissmedic."
        return "Société suisse de neurologie / Swiss Medical Forum ; EAN et société européenne pertinente ; FI Swissmedic."
    if system == "S05":
        if code == "E87":
            return "Sociétés suisses d’endocrinologie et de néphrologie ; références européennes et KDIGO applicables en Suisse ; FI Swissmedic."
        return "Société suisse d’endocrinologie et de diabétologie / Swiss Medical Forum ; ESE, EASD et référence européenne adaptée ; FI Swissmedic."
    if system == "S04":
        if code.startswith("C"):
            return "Références suisses de néphrologie et d’urologie oncologique ; EAU / ESMO ; FI Swissmedic."
        return "Société suisse de néphrologie / Swiss Medical Forum ; ERA et KDIGO applicables en Suisse ; FI Swissmedic."
    return "Société suisse d’hématologie / Swiss Medical Forum ; EHA, ESMO et référence européenne adaptée ; FI Swissmedic."


def load_data(root=ROOT):
    plan = json.loads((root / "organisation/plan_tetrade_30_cycles.json").read_text())
    ref = json.loads((root / "nosology/reference.json").read_text())
    entities = {e["code"]: e for e in ref["entities"]}
    frequent = set(json.loads((root / "nosology/frequency.json").read_text())["codes"])
    fragments = {f["id"]: f for f in json.loads((root / "fragments.json").read_text())}
    cycles = [{"number": i + 1, "name": name, "chapters": []} for i, name in enumerate(plan["cycle_names"])]
    assert len(cycles) == 30
    inventories, summaries = [], []
    draft_files = list((root / "livraisons").rglob("*_a.html"))
    for system in plan["systems"]:
        fid = system["id"]
        lessons = [l for l in json.loads((root / f"nosology/fragments/{fid}.json").read_text())["lessons"] if "." not in l["code"]]
        by_code = {l["code"]: l for l in lessons}
        assert len(system["chapters"]) == 30
        assert len({c[0] for c in system["chapters"]}) == 30
        assignments = {}
        for i, (code, focus) in enumerate(system["chapters"], 1):
            l = by_code[code]
            assert ref["mapping"][code]["fragment"] == fid
            author = f"C{i:02d}-R-{system['tag']}"
            partner = {"NEUR": "HEM", "HEM": "NEUR", "ENDO": "NEPH", "NEPH": "ENDO"}[system["tag"]]
            drafts = [str(p.relative_to(root)) for p in draft_files if p.name == f"{code}_a.html" and all(p.with_name(f"{code}_{part}.html").exists() for part in "abcd")]
            ch = {"id": f"c{i:02d}-{code}", "code": code, "category_title": entities[code]["title"],
                  "title": l["title"], "system": system["name"], "fragment": fid, "label": system["label"],
                  "covers": l["icd10gm"]["codes"], "mode": "Reprise / complément" if l["state"] == "filled" else "Reprise du brouillon existant" if drafts else "Production nouvelle · inventaire préalable",
                  "drafts": drafts,
                  "present": l["state"] == "filled", "federal": bool(l["gold_star"]["enabled"]),
                  "frequent": bool(set(l["icd10gm"]["codes"]) & frequent), "focus": focus,
                  "author": author, "auditor": f"C{i:02d}-R-{partner}", "counter": f"C{i:02d}-CA-{system['tag']}",
                  "coordinator": "Codex — coordinateur du fil", "sources": source_targets(fid, code),
                  "url": ONLINE + f"fragments/MEDINA_{fid}_{fragments[fid]['slug']}.html#/entry/{code}"}
            cycles[i - 1]["chapters"].append(ch)
            assignments[code] = i
        cover = {}
        for l in lessons:
            for code in l["icd10gm"]["codes"]:
                assert code not in cover, code
                cover[code] = l
        raw = sorted(code for code, meta in ref["mapping"].items() if meta["fragment"] == fid and "." not in code)
        assert set(raw) == set(cover)
        rows = [{"code": code, "title": entities[code]["title"], "block": ref["blocks"][entities[code]["block"]]["title"],
                 "root": cover[code]["code"], "root_title": cover[code]["title"],
                 "present": cover[code]["state"] == "filled", "cycle": assignments.get(cover[code]["code"]),
                 "federal": bool(cover[code]["gold_star"]["enabled"]), "frequent": code in frequent} for code in raw]
        inventories.append({"system": system["name"], "label": system["label"], "fragment": fid, "rows": rows})
        selected = [c for cycle in cycles for c in cycle["chapters"] if c["fragment"] == fid]
        summary = {"name": system["name"], "fragment": fid, "raw_categories": len(raw), "lessons": len(lessons),
                   "present": sum(l["state"] == "filled" for l in lessons), "new": sum(not c["present"] for c in selected),
                   "revisions": sum(c["present"] for c in selected), "federal_total": sum(l["gold_star"]["enabled"] for l in lessons),
                   "federal_present": sum(l["gold_star"]["enabled"] and l["state"] == "filled" for l in lessons),
                   "federal_new": sum(c["federal"] and not c["present"] for c in selected),
                   "freq_total": sum(bool(set(l["icd10gm"]["codes"]) & frequent) for l in lessons),
                   "freq_present": sum(bool(set(l["icd10gm"]["codes"]) & frequent) and l["state"] == "filled" for l in lessons),
                   "freq_new": sum(c["frequent"] and not c["present"] for c in selected)}
        summaries.append(summary)
    assert all(len(c["chapters"]) == 4 for c in cycles)
    payload = {"plan": plan, "cycles": cycles, "inventories": inventories, "summaries": summaries,
               "stages": STAGES, "gates": GATES, "rules": RULES,
               "source_hashes": {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in
                                 [root / "PROMPT_MEDINA.md", root / "PROMPT_TRANSITION.md", root / "docs/STYLE_REDACTION.md",
                                  root / "nosology/reference.json", root / "nosology/frequency.json"] +
                                 [root / f"nosology/fragments/{s['id']}.json" for s in plan["systems"]]}}
    return payload


def render(data):
    e = html.escape
    fonts = "".join("@font-face{font-family:'Atkinson Hyperlegible Next';font-style:%s;font-weight:%s;font-display:swap;src:url(data:font/woff2;base64,%s) format('woff2')}" %
                    (style, weight, base64.b64encode((ROOT / "shell/fonts" / file).read_bytes()).decode())
                    for file, style, weight in [("ahn-400.woff2", "normal", "400"), ("ahn-400i.woff2", "italic", "400"),
                                                 ("ahn-600.woff2", "normal", "600"), ("ahn-700.woff2", "normal", "700")])
    rules = "".join(f"<article><h3>{i}. {e(title)}</h3><p>{e(text)}</p></article>" for i, (title, text) in enumerate(RULES, 1))
    summary_rows = "".join(f"<tr><th scope='row'>{e(s['name'])}</th><td>{s['raw_categories']}</td><td>{s['present']} / {s['lessons']}</td><td>{s['new']}</td><td>{s['revisions']}</td><td>{s['present'] + s['new']} / {s['lessons']}</td><td>{s['federal_present'] + s['federal_new']} / {s['federal_total']}</td></tr>" for s in data["summaries"])
    cycle_html = []
    for cycle in data["cycles"]:
        n = cycle["number"]
        cards = []
        for ch in cycle["chapters"]:
            cid = ch["id"]
            steps = "".join(f"<label><input type='checkbox' data-key='{cid}:{k}' data-chapter='{cid}' data-stage='{k}' disabled> {e(v)}</label>" for k, v in STAGES[:-1])
            cards.append(f"""<article class="chapter" data-chapter-card="{cid}">
              <p class="system">Système : {e(ch['label'])} <span class="tag">{e(ch['mode'])}</span></p>
              <p class="category"><b>Catégorie : {ch['code']} — {e(ch['category_title'])}</b></p>
              <h3><label><input type="checkbox" data-key="{cid}:injected" data-chapter="{cid}" data-stage="injected" aria-label="{ch['code']} — injection publiée et vérifiée" disabled><span>Chapitre : {e(ch['title'])}</span></label></h3>
              <p class="mission">{e(ch['focus'])}</p>
              <p class="agents"><b>Auteur :</b> {ch['author']} · <b>Audit croisé :</b> {ch['auditor']} · <b>Contre-audit différé :</b> {ch['counter']}<br><b>Contrôle et injection :</b> {e(ch['coordinator'])}.</p>
              <p class="sources"><b>Sources à rechercher et à lire :</b> {e(ch['sources'])}</p>
              <p class="scope"><b>Périmètre actuel :</b> {e(', '.join(ch['covers']))}. <b>Repérage :</b> {'Étoile fédérale pédagogique' if ch['federal'] else 'Correspondance fédérale non établie'}{' ; sélection fréquente' if ch['frequent'] else ''}. <a href="{e(ch['url'])}">Ouvrir la catégorie MEDINA</a>.</p>
              <div class="steps" aria-label="Étapes de {ch['code']}">{steps}</div>
              <label class="evidence">Preuves : sources, deux audits, contre-audit, empreinte finale, commit et URL publiée<textarea data-evidence="{cid}" rows="2" placeholder="Références vérifiables du dossier de preuves — nécessaires avant le contrôle final." disabled></textarea></label>
            </article>""")
        checks = "".join(f"<label><input type='checkbox' data-key='cycle{n}:{key}' data-gate='{n}' disabled> {e(label)}</label>" for key, label in GATES)
        caption = f"PASSAGE VERS LE CYCLE {n + 1} INTERDIT SANS CLÔTURE ET PROMPT DE VÉRITÉ" if n < 30 else "CLÔTURE FINALE — AUCUNE POURSUITE SANS BILAN ET NOUVELLE FILE DOCUMENTÉE"
        cycle_html.append(f"""<section class="cycle" id="cycle-{n}" data-cycle="{n}">
          <header class="cycle-head"><p class="eyebrow">Cycle {n:02d} / 30 · quatre chapitres · un auteur par chapitre</p><h2>Cycle {n} : {e(cycle['name'])}</h2><p class="cycle-state" data-cycle-state="{n}">Planifié — suivi non démarré.</p></header>
          <p class="open-cycle"><label><input type="checkbox" data-key="cycle{n}:preflight" data-preflight="{n}" disabled> Le Prompt est relu ; l’inventaire, les doublons, les sources à lire et les gardes opérationnelles sont vérifiés avant ouverture.</label></p>
          <div class="chapter-grid">{''.join(cards)}</div>
          <div class="closure"><h3>Conditions de passage du cycle {n}</h3><p>La case près du titre signifie « injection publiée et vérifiée ». Les quatre injections suivent l’ordre NEUR → ENDO → NEPH → HEM. Les cases ci-dessous ne sont accessibles qu’après ces quatre injections.</p><div class="gate-checks">{checks}</div></div>
          <div class="red-bar" role="separator" aria-label="Barrière rouge de 0,5 cm"></div><p class="barrier-note">{caption}</p>
        </section>""")
    inventory_html = []
    for inventory in data["inventories"]:
        fid = inventory["fragment"]
        rows = []
        for row in inventory["rows"]:
            status = "Cours présent · à reprendre" if row["present"] else "Catégorie sans cours intégré"
            when = f"Cycle {row['cycle']}" if row["cycle"] else "Hors des 30 cycles"
            cycle_link = f"<a href='#cycle-{row['cycle']}'>{when}</a>" if row["cycle"] else when
            rows.append(f"<tr data-inventory-row data-system='{fid}' data-present='{str(row['present']).lower()}'><th scope='row'>{row['code']}</th><td>{e(row['title'])}</td><td>{row['root']} — {e(row['root_title'])}</td><td>{status}</td><td>{cycle_link}</td></tr>")
        inventory_html.append(f"<section class='inventory-system' data-inventory-system='{fid}'><h3>{e(inventory['label'])} · {len(rows)} catégories</h3><p>Les intitulés de catégories sont ceux de l’OFS. Le chapitre canonique peut regrouper plusieurs catégories ; un seul agent en traite alors les variantes et documente leur couverture.</p><div class='table-wrap'><table class='inventory-table'><thead><tr><th>Code</th><th>Catégorie CIM-10-GM 2024</th><th>Chapitre canonique actuel</th><th>État de présence</th><th>Programmation</th></tr></thead><tbody>{''.join(rows)}</tbody></table></div><p class='inventory-note'>« Cours présent » désigne une présence structurée, sans certification de complétude, d’exactitude ou de validation médicale humaine. « Hors des 30 cycles » reste dans le reliquat et ne vaut pas exclusion de l’examen.</p></section>")
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    template = (ROOT / "organisation/tetrade_plan_template.html").read_text()
    substitutions = {"__FONTS__": fonts, "__RULES__": rules, "__SUMMARY__": summary_rows,
                     "__CYCLES__": "".join(cycle_html), "__INVENTORY__": "".join(inventory_html), "__DATA__": payload,
                     "__BASELINE__": data["plan"]["baseline"], "__TOTAL_RAW__": str(sum(s["raw_categories"] for s in data["summaries"]))}
    for marker, value in substitutions.items():
        assert template.count(marker) >= 1, marker
        template = template.replace(marker, value)
    return template


def main():
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "organisation/progression/plan-tetrade-30-cycles.html")
    args = parser.parse_args()
    data = load_data()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render(data))
    args.output.with_suffix(".json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print(f"Plan : 30 cycles, 120 missions, {sum(s['raw_categories'] for s in data['summaries'])} catégories ; aucun cours démarré.")


if __name__ == "__main__":
    main()
