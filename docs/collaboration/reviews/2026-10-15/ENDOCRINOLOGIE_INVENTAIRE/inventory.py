#!/usr/bin/env python3
"""Inventaire documentaire S05 des têtes distantes présentes, sans écriture médicale.

Exécuter depuis la racine du dépôt. Les refs distantes doivent être actualisées
par le coordinateur avant l'exécution. Aucune vérification clinique n'est faite.
"""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path.cwd()
sys.path.insert(0, str(ROOT))
from fragment_surface import frontend_catalog

OUT = Path(__file__).resolve().parent
SNAPSHOT = "bc3a56fa8ef7abdc048e9bb0b4e94dd850b1c373"


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def write(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def tree(sha):
    rows = {}
    for row in git("ls-tree", "-r", "-z", sha).decode().split("\0"):
        if row:
            metadata, path = row.split("\t", 1)
            rows[path] = metadata.split()[2]
    return rows


full, owners, _ = frontend_catalog(ROOT)
entries = {item["code"]: item for item in full["entries"]
           if owners.get(item["code"]) == "S05"}
snapshot_courses = {item["code"]: item for item in json.loads(git("show", SNAPSHOT + ":chapters.json"))
                    if item.get("integrated") and item.get("owner") == "S05"}
refs = [line.split() for line in git("for-each-ref", "--format=%(refname) %(objectname)",
                                   "refs/remotes/origin").decode().splitlines()]
commits = {}
for ref, sha in refs:
    commits.setdefault(sha, []).append(ref)

variants = {}
research = {}
for sha, names in commits.items():
    for path, blob in tree(sha).items():
        match = re.search(r"(?:^|/)chapters/([A-Z][0-9]{2})/[^/]+\.html$", path)
        if match and match[1] in entries:
            key = (path, blob)
            record = variants.setdefault(key, {"code": match[1], "path": path,
                                               "git_blob": blob, "refs": []})
            record["refs"].extend(names)
        if "E-06-Endocrinologie et métabolisme/" in path and path.endswith(("recherche.md", "sources.json")):
            match = re.search(r"CYCLE_\d+_(E\d{2})/", path)
            if match and match[1] in entries:
                key = (path, blob)
                research.setdefault(key, {"code": match[1], "path": path,
                                          "git_blob": blob, "refs": []})["refs"].extend(names)

blob_cache = {}
for record in [*variants.values(), *research.values()]:
    blob = record["git_blob"]
    if blob not in blob_cache:
        body = git("cat-file", "blob", blob)
        blob_cache[blob] = {"bytes": len(body), "sha256": hashlib.sha256(body).hexdigest()}
    record.update(blob_cache[blob])
    record["refs"].sort()

snapshot_tree = tree(SNAPSHOT)
published = json.loads((OUT / "publication-before.json").read_text())
rows = []
for code, entry in sorted(entries.items()):
    sources = [record for record in variants.values() if record["code"] == code]
    source_research = [record for record in research.values() if record["code"] == code]
    canonical = {path: blob for path, blob in snapshot_tree.items()
                 if path.startswith("chapters/" + code + "/") and path.endswith(".html")}
    candidate_roots = sorted({str(Path(record["path"]).parent) for record in sources
                              if not record["path"].startswith("chapters/")})
    state = ("publie_avant_mission" if code in published["course_templates"] else
             "candidat_html_non_publie" if sources else
             "recherche_seule" if source_research else "aucun_contenu_repere")
    rows.append({"code": code, "title": snapshot_courses.get(code, {}).get("title", entry["title"]),
                 "state_at_snapshot": state, "canonical_metadata": snapshot_courses.get(code),
                 "canonical_html_count": len(canonical), "candidate_roots": candidate_roots,
                 "html_variant_count": len(sources), "research_variant_count": len(source_research)})

result = {"scope": "E-06-Endocrinologie et métabolisme (S05)", "snapshot_main": SNAPSHOT,
          "remote_refs_count": len(refs), "unique_remote_heads": len(commits),
          "categories": rows, "medical_audit_performed": False,
          "limits": ["Les états décrivent le snapshot et la lecture publique avant publication de cette mission.",
                     "Les références de branches sont celles actualisées par le coordinateur ; ce script ne contacte pas GitHub.",
                     "Les empreintes et contrôles techniques ne valident pas le contenu médical ni la complétude CIM-11."]}
write("inventory.json", result)
write("remote-heads.json", [{"ref": ref, "commit": sha} for ref, sha in refs])
write("html-variants.json", sorted(variants.values(), key=lambda x: (x["code"], x["path"], x["git_blob"])))
write("research-variants.json", sorted(research.values(), key=lambda x: (x["code"], x["path"], x["git_blob"])))
counts = {state: sum(item["state_at_snapshot"] == state for item in rows)
          for state in sorted({item["state_at_snapshot"] for item in rows})}
print(json.dumps({"categories": len(rows), "states": counts,
                  "remote_refs": len(refs), "html_variants": len(variants)}, ensure_ascii=False))
