#!/usr/bin/env python3
"""Publie l'inventaire des sources des quatre systèmes, sans réécrire les cours."""
import argparse
import base64
import hashlib
import html
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
SYSTEMS = {"S08", "S05", "S04", "S06"}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build(output):
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    catalog = json.loads((ROOT / "chapters.json").read_text())
    fragments = [r for r in json.loads((ROOT / "organisation/fragments.json").read_text()) if r["id"] in SYSTEMS]
    filenames = {r["id"]: "MEDINA_" + r["id"] + "_" + r["slug"] + ".html" for r in json.loads((ROOT / "fragments.json").read_text())}
    groups, known = [], set()
    for fragment in sorted(fragments, key=lambda r: r["order"]):
        courses = []
        for row in sorted(catalog, key=lambda r: r["code"]):
            if row.get("owner") != fragment["id"] or not row.get("integrated"):
                continue
            code = row["code"]
            paths = sorted((ROOT / "chapters" / code).glob("*.html")) + [ROOT / "glossary" / (code.lower() + ".py")]
            missing = [str(p.relative_to(ROOT)) for p in paths if not p.is_file()]
            if missing or not all((ROOT / "chapters" / code / (code + "_" + tab + ".html")).is_file() for tab in "abcd"):
                raise ValueError("Sources déclarées mais absentes : " + code)
            courses.append({"code": code, "title": row["title"], "route": "../fragments/" + filenames[fragment["id"]] + "#/entry/" + code,
                            "publication_mode": row.get("publication_mode"), "declared_audit_status": row.get("audit_status"),
                            "source_files": {p.relative_to(ROOT).as_posix(): digest(p) for p in paths}})
            known.add(code)
        groups.append({"id": fragment["id"], "label": fragment["label"], "courses": courses})
    preparations = {}
    for fragment in fragments:
        folder = ROOT / "livraisons/Livraison Claude" / fragment["label"]
        for path in sorted(folder.rglob("recherche.md")):
            match = re.search(r"CYCLE_\d+_([A-Z]\d{2})(?:/|$)", path.relative_to(folder).as_posix())
            if not match or match[1] in known:
                continue
            code = match[1]
            files = [p for p in path.parent.iterdir() if p.is_file() and p.suffix in {".md", ".json"}]
            preparations.setdefault(code, {"code": code, "fragment_id": fragment["id"], "source_files": {}})["source_files"].update(
                {p.relative_to(ROOT).as_posix(): digest(p) for p in sorted(files)})
    manifest = {"schema_version": 1, "source_commit": revision, "medical_audit_performed_by_this_operation": False,
                "systems": groups, "preparations_without_course": list(preparations.values())}
    output.mkdir(parents=True, exist_ok=True)
    (output / "sources.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    esc = html.escape
    sections = []
    for group in groups:
        items = "".join('<li><a href="' + esc(r["route"], quote=True) + '">' + esc(r["code"] + " — " + r["title"]) + '</a></li>' for r in group["courses"])
        sections.append('<section><h2>' + esc(group["label"]) + '</h2><p>' + str(len(group["courses"])) + ' cours accessibles.</p><ul>' + items + '</ul></section>')
    research = []
    for row in preparations.values():
        links = ['<a href="https://github.com/vialdjoukang-spec/Medina/blob/' + revision + '/' + quote(name, safe='/') + '">' + esc(Path(name).name) + '</a>' for name in row["source_files"]]
        research.append('<li>' + esc(row["code"]) + ' — préparation disponible ; cours non rédigé : ' + ' · '.join(links) + '</li>')
    faces = ''.join("@font-face{font-family:Atkinson;font-style:normal;font-weight:%s;font-display:swap;src:url(data:font/woff2;base64,%s) format('woff2')}" %
                    (weight, base64.b64encode((ROOT / 'shell/fonts' / name).read_bytes()).decode('ascii'))
                    for name, weight in [('ahn-400.woff2', '400'), ('ahn-700.woff2', '700')])
    page = '<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>MEDINA — quatre systèmes</title><style>' + faces + 'body{font:18px/1.6 Atkinson,system-ui,sans-serif;color:#193126;background:#fafbf8;max-width:72rem;margin:auto;padding:2rem}a{color:#17553b}section{background:white;border:1px solid #dce4dc;border-radius:12px;padding:1rem 1.5rem;margin:1.5rem 0}li{margin:.4rem 0}code{overflow-wrap:anywhere}small{color:#48594d}</style><main><a href="../">Accueil MEDINA</a><h1>Les quatre systèmes</h1><p>Publication en l’état des cours disponibles. Les travaux en cours restent des travaux en cours ; cet inventaire ne constitue pas un audit médical.</p>' + ''.join(sections)
    if research:
        page += '<section><h2>Préparations disponibles</h2><ul>' + ''.join(research) + '</ul></section>'
    page += '<p><a href="sources.json">Inventaire et empreintes pour l’audit futur</a> · <a href="../publication.json">Manifeste de construction</a></p><small>Référence des sources : <code>' + revision + '</code></small></main></html>\n'
    (output / "index.html").write_text(page)
    print(json.dumps({"courses": sum(len(g["courses"]) for g in groups), "preparations": len(preparations), "source_commit": revision}))
    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "_site/audit")
    build(parser.parse_args().output)
