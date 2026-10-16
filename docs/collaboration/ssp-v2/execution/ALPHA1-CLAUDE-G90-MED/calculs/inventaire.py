#!/usr/bin/env python3
"""Inventaire exhaustif des valeurs numériques de la leçon G90 (7 fichiers figés du manifeste).
Usage : python3 inventaire.py <racine_du_depot> > inventaire.json
Lecture seule : les fichiers sont lus via `git show <SHA>:<chemin>` pour garantir l'empreinte du manifeste."""
import sys, re, json, html, subprocess, hashlib
SHA = "523832d9ef6097607d3443f4398deee9cd0add11"
FILES = ["chapters/G90/G90_a.html", "chapters/G90/G90_b.html", "chapters/G90/G90_c.html",
         "chapters/G90/G90_d.html", "chapters/G90/G90_pop1.html", "chapters/G90/G90_pop2.html", "glossary/g90.py"]
root = sys.argv[1] if len(sys.argv) > 1 else "."
UNITS = (r"mmHg|mm|µg/kg|mg|g|litres?|L|%|°|battements par minute|par minute|/min|minutes?|min|secondes?|s|heures?|h|"
         r"jours?|semaines?|mois|ans?|pour 100 000(?: personnes-années)?|patients|cas|personnes?")
NUM = r"(?<![\w.,])(\d+(?:[  ]\d{3})*(?:,\d+)?)"
PAT = re.compile(NUM + r"(?:\s*(?:à|–|-|/)\s*(\d+(?:,\d+)?))?\s*(" + UNITS + r")?(?![\w])")
def text_of(fragment):
    fragment = re.sub(r'^[^<]*?>', ' ', fragment, count=1)
    s = re.sub(r"<svg[^>]*>", " [SVG] ", fragment)
    s = re.sub(r"<[a-zA-Z/!][^>]*>", " ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s)
out = []
total = 0
for f in FILES:
    raw = subprocess.run(["git", "-C", root, "show", f"{SHA}:{f}"], capture_output=True, check=True).stdout
    sha = hashlib.sha256(raw).hexdigest()
    s = raw.decode("utf-8")
    if f.endswith(".py"):
        blocks = [("glossaire", s)]
    else:
        marks = [(m.start(), m.group(1)) for m in re.finditer(r'(?:\sid|data-pop)="([^"]*)"', s)]
        marks.append((len(s), None))
        blocks = [(marks[i][1], s[marks[i][0]:marks[i+1][0]]) for i in range(len(marks)-1)]
        if marks and marks[0][0] > 0:
            blocks.insert(0, ("debut", s[:marks[0][0]]))
    for anchor, frag in blocks:
        t = text_of(frag) if not f.endswith(".py") else frag
        frag_head = True
        for m in PAT.finditer(t):
            val = m.group(1); val2 = m.group(2); unit = m.group(3) or ""
            ctx = t[max(0, m.start()-70): m.end()+70].strip()
            # ignorer les numéros de figure/cas/îlot, les codes CIM et les attributs techniques
            pre = t[max(0, m.start()-12): m.start()]
            post = t[m.end(): m.end()+6]
            if (re.search(r"(Figure|fictif|Cas|CIM-|G|I|exon|type|HSAN|N-0|e-|p-|\(|Version|directive allemande|Betta)\s*$", pre)
                    or (re.match(r"^(19|20)\d\d$", val) and not unit)
                    or re.match(r"^(\.\d|-GM|\))", post)
                    or (re.match(r"^\.\s", post) and not unit and not re.search(r"[a-zéèàù,]\s$", pre))
                    or re.match(r"^\s*(e|er|re)\b", post)
                    or (frag_head and t.strip().startswith(val) and m.start() < 3)):
                kind = "repere_non_calculable"
            else:
                kind = "valeur"
            total += 1
            out.append({"id": f"V{total:04d}", "fichier": f, "sha256_fichier": sha, "ancre": anchor,
                        "valeur": val + (("–" + val2) if val2 else ""), "unite": unit, "nature": kind,
                        "contexte": ctx})
json.dump({"source_snapshot_sha": SHA, "total_releves": total,
           "valeurs": sum(1 for o in out if o["nature"] == "valeur"),
           "reperes_non_calculables": sum(1 for o in out if o["nature"] != "valeur"),
           "occurrences": out}, sys.stdout, ensure_ascii=False, indent=1)
