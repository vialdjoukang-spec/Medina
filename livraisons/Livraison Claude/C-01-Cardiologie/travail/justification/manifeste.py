#!/usr/bin/env python3
"""Met à jour livraison.json pour les cours dont une copie corrigée existe.

Usage : python3 manifeste.py <CODE> [...]
Pour chaque fichier copié sous sources/chapters/<CODE>/, enregistre l'empreinte de la source
canonique (sha256) et celle de la copie (proposed_sha256), puis annonce le cours.
"""
import hashlib
import json
import pathlib
import sys

ICI = pathlib.Path(__file__).resolve().parent
LIVR = ICI.parents[1]
DEPOT = LIVR.parents[2]


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


m = json.loads((LIVR / "livraison.json").read_text())
sys.path.insert(0, str(DEPOT / "tools"))
import livraison  # noqa: E402
cat = {c["code"]: c for c in livraison.catalog(DEPOT)["S01"]["chapters"]}
fichiers = {r["target_path"]: r for r in m["files"]}
annonces = {c["code"] for c in m["chapters"]}
for code in sys.argv[1:]:
    for copie in sorted((LIVR / "sources" / "chapters" / code).glob("*.html")):
        cible = f"chapters/{code}/{copie.name}"
        r = fichiers.setdefault(cible, {"target_path": cible, "source_path": "sources/" + cible})
        if (DEPOT / cible).exists():
            r.pop("operation", None)
            r["sha256"] = sha(DEPOT / cible)
        else:
            r["operation"] = "add"
            r["sha256"] = None
        r["proposed_sha256"] = sha(copie)
    if code not in annonces:
        titre = cat.get(code, {}).get("title")
        if not titre:
            sys.exit(f"Titre de {code} introuvable dans le catalogue")
        m["chapters"].append({"code": code, "title": titre, "covers": cat[code].get("covers", [code]),
                              "owner_fragment": "S01"})
        annonces.add(code)
m["files"] = sorted(fichiers.values(), key=lambda r: r["target_path"])
(LIVR / "livraison.json").write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n")
print(len(m["files"]), "fichiers ;", sorted(annonces))
