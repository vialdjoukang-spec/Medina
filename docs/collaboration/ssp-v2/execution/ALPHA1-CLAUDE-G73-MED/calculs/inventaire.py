#!/usr/bin/env python3
"""Inventaire scripté de toutes les grandeurs chiffrées de la leçon G73 (7 fichiers figés).

Usage (depuis la racine du worktree) :
    python3 docs/collaboration/ssp-v2/execution/ALPHA1-CLAUDE-G73-MED/calculs/inventaire.py
Écrit calculs/inventaire.json : {total, par_fichier, occurrences:[{id, fichier, ancre, valeur, unite, contexte}]}.
Les numéros de code CIM (G73.1, E05.-…), les années isolées des références et les DOI sont exclus :
ce ne sont pas des grandeurs. Les nombres du texte visible (balises retirées) sont seuls relevés.
"""
import html, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
FILES = ["chapters/G73/G73_a.html", "chapters/G73/G73_b.html", "chapters/G73/G73_c.html",
         "chapters/G73/G73_d.html", "chapters/G73/G73_pop1.html", "chapters/G73/G73_pop2.html",
         "glossary/g73.py"]
UNITS = r"(?:mmol/L|mEq/L|µmol/L|mg/dL|U/L|ng/mL|mg/jour|mg/kg|mg|mV|ms|%|‰|pour 100 000|par million de personnes-années|par million|mois|semaines|jours|jour|heures|heure|h\b|ans|an\b|patients|participants|cas|essais|décès|rapports|pays|points?|items?|articles)"
NUM = r"(?<![\w.,/-])(?:≈\s*|≤\s*|≥\s*|>\s*|<\s*|−\s*|\+\s*)?(?:\d{1,3}(?:[  ]\d{3})+|\d+)(?:,\d+)?(?:\s*(?:à|–)\s*\d+(?:,\d+)?)?(?![\w.]\d)"
PAT = re.compile("(" + NUM + r")\s*(" + UNITS + r")?")
SKIP_CTX = re.compile(r"^(?:[A-Z]\d{2}(?:\.\d)?|C00|D48|E10|E14|M0[56])$")

def visible_text(raw, is_py):
    if is_py:
        # glossaire : chaînes littérales seulement
        return " ".join(re.findall(r"'([^']*)'", raw))
    t = re.sub(r"<p class=\"src\">.*?</p>", " ", raw, flags=re.S)   # références bibliographiques
    t = re.sub(r"<svg.*?</svg>", lambda m: " ".join(re.findall(r">([^<]+)<", m.group(0))), t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", html.unescape(t))

def anchors(raw):
    """positions des id/data-pop pour rattacher chaque occurrence à son ancre HTML"""
    out = []
    for m in re.finditer(r'(?:id|data-pop)="([^"]+)"', raw):
        end = raw.find(">", m.end())          # la tranche commence après la balise ouvrante
        out.append((end + 1 if end >= 0 else m.end(), m.group(1)))
    return out

def main():
    occ, par = [], {}
    for f in FILES:
        raw = (ROOT / f).read_text(encoding="utf-8")
        is_py = f.endswith(".py")
        # rattachement : on découpe le brut par ancre, on extrait le texte visible de chaque tranche
        cuts = anchors(raw) if not is_py else [(0, "glossaire")]
        cuts = cuts or [(0, f)]
        cuts.append((len(raw), None))
        n0 = len(occ)
        for (a, name), (b, _) in zip(cuts, cuts[1:]):
            txt = visible_text(raw[a:b], is_py)
            for m in PAT.finditer(txt):
                val, unit = m.group(1).strip(), (m.group(2) or "")
                core = re.sub(r"[^\d,]", "", val)
                # exclusions : codes CIM, numéros d’îlot isolés, années 19xx/20xx sans unité
                left = txt[max(0, m.start() - 2):m.start()]
                if re.match(r"\d", core) and not unit:
                    if re.fullmatch(r"(19|20)\d\d", core):
                        continue
                    if re.search(r"CIM-$|Betta $|\.$", txt[max(0, m.start()-6):m.start()]):
                        continue
                    if re.search(r"[A-Z]$", left.strip()) or re.search(r"[A-Z]\d*\.?$", txt[max(0, m.start()-4):m.start()]):
                        continue
                ctx = txt[max(0, m.start() - 70): m.end() + 70].strip()
                occ.append({"id": f"V{len(occ)+1:04d}", "fichier": f, "ancre": name,
                            "valeur": val, "unite": unit, "contexte": ctx})
        par[f] = len(occ) - n0
    out = {"lecon": "G73", "methode": "regex nombre + unité sur le texte visible des 7 fichiers ; références et codes CIM exclus",
           "total": len(occ), "par_fichier": par, "occurrences": occ}
    dest = Path(__file__).with_name("inventaire.json")
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(occ)} occurrences relevées ->", dest)
    for k, v in par.items():
        print(f"  {k}: {v}")

if __name__ == "__main__":
    main()
