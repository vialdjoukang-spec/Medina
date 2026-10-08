#!/usr/bin/env python3
"""Audit bloquant des fragments et de la reproductibilité du build MEDINA."""
import base64
import gzip
import hashlib
import html
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from fragment_surface import frontend_entries, fragment_chapters, isolated_glossary, presentation, SPECIALTY_BY_FRAGMENT
FRAGMENT_DIR = Path(os.environ.get("MEDINA_FRAGMENTS", ROOT / "dist/fragments"))


def expanded_html(path):
    source = path.read_text(encoding="utf-8")
    packed = re.search(r'<script id="mdn-pack"[^>]*>([^<]+)</script>', source)
    if packed:
        source += gzip.decompress(base64.b64decode(packed.group(1))).decode("utf-8")
    return source


def expected_chapters(fragment, entries):
    return {chapter['code'] for chapter in fragment_chapters(fragment, entries, ROOT)}


def check_javascript(path, source):
    scripts = re.findall(r'<script(?P<attrs>[^>]*)>(?P<body>[\s\S]*?)</script>', source, re.I)
    for number, match in enumerate(scripts, 1):
        attrs, body = match
        kind = re.search(r'\btype=["\']([^"\']+)', attrs, re.I)
        if kind and kind.group(1).lower() not in ("text/javascript", "application/javascript", "module"):
            continue
        with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", dir=ROOT) as js:
            js.write(body)
            js.flush()
            result = subprocess.run(["node", "--check", js.name], capture_output=True, text=True)
        if result.returncode:
            raise AssertionError(f"JavaScript invalide dans {path.name}, bloc {number}:\n{result.stderr}")


def reproducibility():
    hashes = []
    with tempfile.TemporaryDirectory(prefix=".audit-build-", dir=ROOT) as temporary:
        for run in ("a", "b"):
            output = Path(temporary) / run
            env = os.environ.copy()
            env["MEDINA_ROOT"] = str(ROOT)
            env["MEDINA_OUT"] = str(output)
            subprocess.run([sys.executable, str(ROOT / "build_front.py")], check=True, env=env,
                           stdout=subprocess.DEVNULL)
            hashes.append(hashlib.sha256((output / "MEDINA.html").read_bytes()).hexdigest())
    if hashes[0] != hashes[1]:
        raise AssertionError(f"build non reproductible : {hashes[0]} != {hashes[1]}")


def main():
    fragments = json.loads((ROOT / "fragments.json").read_text(encoding="utf-8"))
    required_ids = {f"S{number:02d}" for number in range(1, 17)} - {"S09"}
    required_ids |= {f"T{number}" for number in range(1, 8)}
    manifest_ids = {fragment["id"] for fragment in fragments}
    if manifest_ids != required_ids:
        missing = ", ".join(sorted(required_ids - manifest_ids)) or "aucun"
        extra = ", ".join(sorted(manifest_ids - required_ids)) or "aucun"
        raise SystemExit(f"fragments.json incomplet (manquants : {missing} ; inattendus : {extra})")
    shell = (ROOT / "shell/medina_front.html").read_text(encoding="utf-8")
    payload = re.search(r'<script id="medora-data" type="application/json">(.*?)</script>', shell, re.S)
    entries = json.loads(payload.group(1))["entries"]

    errors = []
    for fragment in fragments:
        path = FRAGMENT_DIR / f"MEDINA_{fragment['id']}_{fragment['slug']}.html"
        if not path.is_file():
            errors.append(f"fragment manquant : {path}")
            continue
        source = expanded_html(path)
        payload = re.search(r'<script id="medora-data" type="application/json">(.*?)</script>', source, re.S)
        data = json.loads(payload.group(1))
        allowed_entries = {entry['code'] for entry in frontend_entries(fragment, entries, ROOT)}
        expected = expected_chapters(fragment, entries)
        embedded_entries = {entry["code"] for entry in data["entries"]}
        if embedded_entries != allowed_entries:
            errors.append(f"{fragment['id']} périmètre CIM incorrect")
        organisation_payload = re.search(r'<script id="medina-category-organisation-data" type="application/json">(.*?)</script>', source, re.S)
        if not organisation_payload:
            errors.append(f"{fragment['id']} organisation des catégories absente")
        else:
            try:
                organisation = json.loads(organisation_payload.group(1))
                if organisation.get('fragment', {}).get('id') != fragment['id']:
                    errors.append(f"{fragment['id']} données de catégories d'un autre fragment")
                organised_codes = [variant["code"] for block in organisation["blocks"]
                                   for lesson in block["lessons"] for variant in lesson["variants"]]
                if set(organised_codes) != embedded_entries or len(organised_codes) != len(set(organised_codes)):
                    errors.append(f"{fragment['id']} organisation CIM incomplète ou dupliquée")
                lessons = [lesson for block in organisation['blocks'] for lesson in block['lessons']]
                if any(lesson['source_fragment_id'] != fragment['id'] or
                       lesson['url'] != '#/entry/' + lesson['code'] for lesson in lessons):
                    errors.append(f"{fragment['id']} conserve un cours ou renvoi étranger")
                available = {lesson['code'] for lesson in lessons if lesson['integrated']}
                if available != expected or organisation['integrated_count'] != len(expected):
                    errors.append(f"{fragment['id']} compteur de cours propres incorrect")
                if organisation['fragment'] != presentation(fragment, ROOT):
                    errors.append(f"{fragment['id']} identité frontend incorrecte")
            except (ValueError, AttributeError, KeyError, TypeError):
                errors.append(f"{fragment['id']} données de catégories invalides")
        if 'id="medina-category-organisation-runtime"' not in source:
            errors.append(f"{fragment['id']} navigation des catégories absente")
        allowed_systems = {presentation(fragment, ROOT)['display_name']} if allowed_entries else set()
        if set(data["fragment"]["systems"]) != allowed_systems:
            errors.append(f"{fragment['id']} contient un système étranger")
        specialty_ids = {specialty["id"] for specialty in data["specialties"]}
        expected_specialties = {fragment.get('specialty') or SPECIALTY_BY_FRAGMENT[fragment['id']]}
        if specialty_ids != expected_specialties:
            errors.append(f"{fragment['id']} contient une spécialité étrangère")
        if any(entry.get('primary') not in expected_specialties or entry.get('specialties') != list(expected_specialties) for entry in data['entries']):
            errors.append(f"{fragment['id']} contient une affectation primaire étrangère")
        grouped = [code for group in data['fragment']['categories'] for code in group['chapters']]
        if len(grouped) != len(set(grouped)) or set(grouped) != expected:
            errors.append(f"{fragment['id']} classement des cours incomplet ou dupliqué")
        if 'id="medina-fragment-runtime"' not in source or 'id="medina-fragment-css"' not in source:
            errors.append(f"{fragment['id']} accueil des cours absent")
        if 'id="medina-portable-resources"' in source or 'id="medora-v7-federal-integration"' in source:
            errors.append(f"{fragment['id']} conserve un catalogue global hors périmètre")
        if data['ssps'] or data['profiles'] or data['focus'] or any(data['legacy'][key] for key in ('specialties', 'families', 'references', 'learningTopics', 'profilesGroups', 'systemSchema', 'coverageAudit')):
            errors.append(f"{fragment['id']} conserve un ancien catalogue médical hors frontend")
        if data["meta"]["entries"] != len(data["entries"]) or data["meta"]["sspVisible"] != len(data["ssps"]):
            errors.append(f"{fragment['id']} contient un compteur de données incorrect")
        present = set(re.findall(r'id=["\']ch-([^"\']+)["\']', source))
        foreign = present - expected
        missing = expected - present
        if foreign:
            errors.append(f"{fragment['id']} contient des chapitres étrangers : {', '.join(sorted(foreign))}")
        if missing:
            errors.append(f"{fragment['id']} manque des cours : {', '.join(sorted(missing))}")
        popup_keys = re.findall(r'<template\b[^>]*\bdata-pop=["\']([^"\']+)', source)
        if any(re.match(r'[a-z]\d{2}[-_]', key) and key[:3].upper() not in expected for key in popup_keys):
            errors.append(f"{fragment['id']} contient une fenêtre de cours étranger")
        glossary_match = re.search(r'<script id="medina-glossary"[^>]*>(.*?)</script>', source, re.S)
        glossary = json.loads(glossary_match.group(1))
        templates = ''.join(re.findall(r'<template\b[^>]*>.*?</template>', source, re.S))
        used = {html.unescape(key) for key in re.findall(r'\bdata-ab=["\']([^"\']+)["\']', templates)}
        if not used.issubset(glossary):
            errors.append(f"{fragment['id']} définitions de fenêtres manquantes : {', '.join(sorted(used - glossary.keys()))}")
        if glossary != isolated_glossary(source, glossary):
            errors.append(f"{fragment['id']} conserve des définitions sans lien avec ses cours")
        sidebar_payload = re.search(r'window\.MEDINA_FRAGMENT_SIDEBAR=(.*?);</script>', source, re.S)
        sidebar = {item["code"] for group in json.loads(sidebar_payload.group(1))
                   for item in group.get("items", []) if item["written"]}
        if sidebar != expected:
            errors.append(f"{fragment['id']} bandeau incorrect : {', '.join(sorted(sidebar ^ expected))}")
        note = re.search(r'<div class="sidebar-note">([\s\S]*?)</div>', source)
        counts = [int(x.replace(' ', '')) for x in re.findall(r'([0-9][0-9 ]*) (?:catégories CIM intégrées|cours rédigés)', note.group(1))]
        if counts != [len(data["entries"]), len(expected)]:
            errors.append(f"{fragment['id']} compteurs du bandeau incorrects")
        try:
            check_javascript(path, source)
        except AssertionError as error:
            errors.append(str(error))
    if errors:
        raise SystemExit("\n".join(errors))
    reproducibility()
    print(f"audit réussi : {len(fragments)} fragments, JavaScript valide, build reproductible")


if __name__ == "__main__":
    main()
