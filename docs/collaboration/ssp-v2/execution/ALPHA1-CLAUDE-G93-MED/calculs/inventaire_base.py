#!/usr/bin/env python3
"""Audit ALPHA77 G93 — extraction scriptée de toutes les occurrences numériques des 7 fichiers.

Module importé par verifier.py ; lecture seule des fichiers canoniques.
"""
from __future__ import annotations

import html
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
FILES = [
    "chapters/G93/G93_a.html", "chapters/G93/G93_b.html", "chapters/G93/G93_c.html",
    "chapters/G93/G93_d.html", "chapters/G93/G93_pop1.html", "chapters/G93/G93_pop2.html",
    "glossary/g93.py",
]
NUM = re.compile(r"(?<![\w.,\-–])([+−−]?(?:\d{1,3}(?:[   ]\d{3})+(?!\d)|\d+)(?:[.,]\d+)?)"
                 r"(?:\s?[–-]\s?(\d+(?:[.,]\d+)?))?")
UNIT = re.compile(r"^\s?(%|mmHg|kPa|cm d’eau|cmH2O|mm\b|mL/kg/h|mL/min|mL|µg/L|g/kg|mg|g/jour|g\b|kg/m²|kg|°C|"
                  r"pour 100 000|heures?|h\b|minutes|jours|mois|ans?|semaines|patients|sujets|sur|cas|"
                  r"pays|révisions|trimestre|millions?|questions)")


def texte(path: Path) -> list[tuple[str, str]]:
    """[(ancre, texte)] : le texte est découpé à chaque id ou data-pop rencontré."""
    s = path.read_text(encoding="utf-8")
    if path.suffix == ".py":
        return [("glossary/g93.py", re.sub(r"\s+", " ", s))]
    s = re.sub(r"<svg.*?</svg>", lambda m: " " + " ".join(re.findall(r">([^<]+)<", m.group(0))) + " ", s, flags=re.S)
    s = re.sub(r'<(?:a|svg|path|rect|g|text)\b[^>]*>', ' ', s)  # attributs href/coordonnées ignorés
    parts, last, anchor = [], 0, path.name
    for m in re.finditer(r'(?:\bid|data-pop)="([^"]+)"', s):
        parts.append((anchor, s[last:m.start()]))
        anchor, last = m.group(1), m.end()
    parts.append((anchor, s[last:]))
    out = []
    for a, chunk in parts:
        t = re.sub(r"<[^>]+>", " ", chunk)
        t = re.sub(r"\s+", " ", html.unescape(t))
        out.append((a, t))
    return out


def classer(tok: str, avant: str, apres: str) -> str:
    v = tok.lstrip("+−−")
    if re.search(r"(G ?|[A-Z]|CIM-10-GM |[A-Z]\d\d\.)$", avant[-12:]) or re.match(r"^[.]\d", apres):
        if re.search(r"[A-Z]\s?$", avant) or re.search(r"[A-Z]\d{2}$", avant + tok):
            return "NON_CALCULABLE:code_CIM"
    if re.search(r"[A-Z]$", avant) and re.fullmatch(r"\d{1,2}(\.\d+)?", v):
        return "NON_CALCULABLE:code_ou_sigle"
    if re.fullmatch(r"(19|20)\d\d", v) and not re.match(r"\s?(%|patients|cas|mL|mg)", apres):
        return "NON_CALCULABLE:date"
    if re.match(r"\.\d{2}\.\d{4}", apres) or (re.fullmatch(r"\d{1,2}", v) and re.match(r"\.\d{2}\.20", apres)):
        return "NON_CALCULABLE:date"
    if re.search(r"(Figure|Cas|Vignette|Étape|vignette|cas|type|rang|grade|N|HIT-|SUR|TRPM|aquaporine-|NKCC|GLP-|"
                 r"métalloprotéinases matricielles|syndromes? de|e-|p-|configuration|Configuration)\s?$", avant) \
            or re.match(r"^\s?(e\b|re\b|er\b|ᵉ)", apres) or re.match(r"^\s?:", apres) and len(v) <= 2 and re.search(r"(Cas|Figure)", avant):
        return "NON_CALCULABLE:identifiant"
    if avant.rstrip().endswith(">") or re.search(r"(Rang Diagnostic Argument|Étape Moyen Justification et limite|toujours|cause|HII|ophtalmologique|bariatrique|dose|associée|Sevr\S*)\s?$", avant) and re.fullmatch(r"[1-5]", v) and re.match(r"^\s[A-ZÉ]", apres):
        return "NON_CALCULABLE:identifiant"
    if re.search(r"(îlot|ilot|section|onglet|numéro|chapitre|\bn)\s?$", avant):
        return "NON_CALCULABLE:identifiant"
    if re.search(r"(sinus |nerf |onde |N)$", avant) or re.match(r"^\s?(β|beta)", apres):
        return "NON_CALCULABLE:identifiant"
    return "GRANDEUR"


def inventaire() -> list[dict]:
    items, n = [], 0
    for f in FILES:
        for ancre, t in texte(ROOT / f):
            for m in NUM.finditer(t):
                n += 1
                avant, apres = t[max(0, m.start() - 45):m.start()], t[m.end():m.end() + 35]
                u = UNIT.match(apres)
                items.append({
                    "id": f"I{n:03d}", "fichier": f, "ancre": ancre, "valeur": m.group(0).strip(),
                    "unite": (u.group(1) if u else ""),
                    "contexte": (avant + m.group(0) + apres).strip(),
                    "categorie": classer(m.group(1), avant, apres),
                })
    return items


if __name__ == "__main__":
    it = inventaire()
    g = [i for i in it if i["categorie"] == "GRANDEUR"]
    print(len(it), len(g))
    for i in g:
        print(i["id"], i["fichier"][-10:], i["ancre"], "|", i["valeur"], "|", i["contexte"])
