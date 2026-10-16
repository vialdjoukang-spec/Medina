#!/usr/bin/env python3
"""Inventaire scripté de toutes les valeurs numériques des 7 fichiers de la leçon G80.

Usage : python3 calculs/extraire.py <racine_du_worktree>
Sortie : calculs/inventaire.json (à côté de ce script).
Chaque occurrence d'un nombre dans le texte visible (balises retirées, attributs data-title et
aria-label conservés) est relevée avec son unité éventuelle, son ancre (identifiant HTML le plus
proche) et son contexte (60 caractères de part et d'autre).
"""
import html
import json
import re
import sys
from pathlib import Path

FICHIERS = [
    "chapters/G80/G80_a.html", "chapters/G80/G80_b.html", "chapters/G80/G80_c.html",
    "chapters/G80/G80_d.html", "chapters/G80/G80_pop1.html", "chapters/G80/G80_pop2.html",
    "glossary/g80.py",
]
UNITES = r"(?:U/kg/jambe|U/kg|U\b|unités/kg|unités|mg/kg/jour|mg/kg/j|mg/kg|mg/jour|mg/j|mg|µg/jour|µg|mL|ml|%|pour 1000|‰|SA|mois|ans|an|semaines|semaine|jours|jour|g\b|kg|enfants|patients|participants|registres|essais|femmes|institutions|pays|médecins|prises|h\b)"
NOMBRE = re.compile(r"(?<![\w.])(\d+(?:[   ]\d{3})*(?:,\d+)?)(?:\s*[–-]\s*(\d+(?:,\d+)?))?\s*(" + UNITES + r")?")


def texte_visible(brut: str) -> list[tuple[str, str]]:
    """Découpe en segments (ancre, texte) en suivant les id et data-pop."""
    segs = []
    ancre = "debut"
    pos = 0
    for m in re.finditer(r"<[^>]+>", brut):
        if m.start() > pos:
            segs.append((ancre, html.unescape(brut[pos:m.start()])))
        tag = m.group(0)
        i = re.search(r'\b(?:id|data-pop)="([^"]+)"', tag)
        if i and not tag.startswith("</"):
            ancre = i.group(1)
        for attr in ("data-title", "aria-label"):
            a = re.search(attr + r'="([^"]+)"', tag)
            if a:
                segs.append((ancre, html.unescape(a.group(1))))
        pos = m.end()
    segs.append((ancre, html.unescape(brut[pos:])))
    return segs


def main() -> int:
    racine = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    sortie = Path(__file__).with_name("inventaire.json")
    items = []
    n = 0
    for f in FICHIERS:
        brut = (racine / f).read_text(encoding="utf-8")
        if f.endswith(".py"):
            segs = [("glossaire", brut)]
        else:
            # le contenu des <svg> est conservé (textes des figures)
            segs = texte_visible(brut)
        for ancre, txt in segs:
            txt = re.sub(r"\s+", " ", txt)
            for m in NOMBRE.finditer(txt):
                valeur = m.group(1) + (("–" + m.group(2)) if m.group(2) else "")
                n += 1
                items.append({
                    "id": f"N{n:04d}",
                    "fichier": f,
                    "ancre": ancre,
                    "valeur": valeur,
                    "unite": m.group(3) or "",
                    "contexte": txt[max(0, m.start() - 60): m.end() + 60].strip(),
                })
    data = {"total": len(items), "methode": "regex sur texte visible, attributs data-title et aria-label, textes SVG et glossaire", "items": items}
    sortie.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(items)} occurrences relevées -> {sortie}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
