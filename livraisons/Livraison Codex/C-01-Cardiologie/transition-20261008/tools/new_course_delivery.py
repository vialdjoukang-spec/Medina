#!/usr/bin/env python3
"""Paqueter, vérifier et enregistrer un nouveau cours sans écraser une source.

Les contrôles sont techniques. La reconstruction et la validation médicale
restent distinctes de l'enregistrement transactionnel.
"""
from __future__ import annotations

import argparse
import ast
import collections
from datetime import datetime, timezone
from html.parser import HTMLParser
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

_spec = importlib.util.spec_from_file_location("medina_delivery", Path(__file__).with_name("livraison.py"))
delivery = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(delivery)
DeliveryError = delivery.DeliveryError
digest, json_bytes, safe_child, no_symlinks, load_json = (
    delivery.digest, delivery.json_bytes, delivery.safe_child,
    delivery.no_symlinks, delivery.load_json)
DEFAULT_ROOT = Path(__file__).resolve().parents[1]
LABEL = "C-01-Cardiologie"


class References(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids, self.pops = [], []
        self.keys, self.targets, self.routes = set(), set(), set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for name, collection in (("id", self.ids), ("data-pop", self.pops)):
            if attrs.get(name):
                collection.append(attrs[name])
        if attrs.get("data-k"):
            self.keys.add(attrs["data-k"])
        for name in ("aria-controls", "aria-labelledby", "data-p", "data-s"):
            if attrs.get(name):
                self.targets.update(attrs[name].split())
        href = attrs.get("href", "")
        if href.startswith("#/entry/"):
            self.routes.add(href[len("#/entry/"):].split("/")[0])
        elif href.startswith("#") and len(href) > 1 and not href.startswith("#/"):
            self.targets.add(href[1:])

    handle_startendtag = handle_starttag


def text_file(path):
    no_symlinks(path)
    try:
        return Path(path).read_bytes().decode("utf-8")
    except (OSError, UnicodeError) as error:
        raise DeliveryError(f"Source UTF-8 illisible : {path}") from error


def metadata(course):
    if not isinstance(course, dict):
        raise DeliveryError("Métadonnées course absentes.")
    code = course.get("code", "")
    if not re.fullmatch(r"[A-Z][0-9]{2}", code):
        raise DeliveryError("Code CIM invalide.")
    if not isinstance(course.get("title"), str) or not course["title"].strip():
        raise DeliveryError("Intitulé complet obligatoire.")
    covers = course.get("covers")
    if (not isinstance(covers, list) or code not in covers
            or any(not isinstance(c, str) or not re.fullmatch(r"[A-Z][0-9]{2}", c) for c in covers)
            or len(set(covers)) != len(covers)):
        raise DeliveryError("covers doit contenir le code et des catégories CIM distinctes.")
    if course.get("fragment") != "S01" or course.get("category") not in ("vaisseaux", "pression"):
        raise DeliveryError("Fragment S01 et catégorie vaisseaux ou pression obligatoires.")
    return code


def references(texts):
    parsed = References()
    for value in texts:
        parsed.feed(value)
    return parsed


def fragment_courses(root):
    """Reproduire la sélection de build_front.py pour la surface S01."""
    chapters = load_json(root / "chapters.json")
    fragments = load_json(root / "fragments.json")
    fragment = next((f for f in fragments if f.get("id") == "S01"), None)
    if fragment is None:
        raise DeliveryError("Fragment S01 absent.")
    attached = set(fragment.get("rattachements", []))
    explicit = {c for f in fragments for c in f.get("rattachements", [])
                if re.fullmatch(r"[A-Z][0-9]{2}", c)}
    front = safe_child(root, "shell/medina_front.html")
    shell = text_file(front) if front.is_file() else ""
    match = re.search(r'<script id="medora-data" type="application/json">(.*?)</script>', shell, re.S)
    try:
        systems = {e["code"]: e.get("system") for e in json.loads(match.group(1))["entries"]} if match else {}
    except (json.JSONDecodeError, KeyError, TypeError) as error:
        raise DeliveryError("Catalogue de la coque invalide.") from error
    return [c for c in chapters if c.get("integrated") and
            (c["code"] in attached or (c["code"] not in explicit and systems.get(c["code"]) in attached))], shell


def shared_references(root, exclude):
    registered, shell = fragment_courses(root)
    texts = [shell]
    for chapter in registered:
        if chapter["code"] == exclude:
            continue
        folder = safe_child(root, f"chapters/{chapter['code']}")
        if folder.is_dir():
            texts.extend(text_file(path) for path in sorted(folder.glob("*.html")))
    shared = references(texts)
    # Les ID des gabarits d'autres cours ne sont pas présents dans le cours actif.
    # Les fenêtres natives de ces cours restent accessibles via leurs templates.
    shared.ids = references([shell]).ids
    return shared


def inspect_sources(root, course, contents):
    code = metadata(course)
    required = {f"chapters/{code}/{code}_{part}.html" for part in "abcd"}
    glossary_path = f"glossary/{code.lower()}.py"
    if not required <= contents.keys() or glossary_path not in contents:
        raise DeliveryError("Les quatre sources a/b/c/d et le glossaire sont obligatoires.")
    html = [data.decode("utf-8") for name, data in contents.items() if name.endswith(".html")]
    local, shared = references(html), shared_references(root, code)
    for name, values in (("ID", local.ids), ("fenêtre", local.pops)):
        duplicates = [v for v, count in collections.Counter(values).items() if count > 1]
        if duplicates:
            raise DeliveryError(f"{name} natif en double : {duplicates}")
    if not {f"ch-{code}", "pA", "pE", "pS", "pP"} <= set(local.ids):
        raise DeliveryError("Gabarit ch-CODE et quatre panneaux pA/pE/pS/pP obligatoires.")
    if any(not (key.startswith(code.lower() + "-") or key.startswith("pareto-" + code.lower()))
           for key in local.pops):
        raise DeliveryError("Les fenêtres locales doivent porter le préfixe du cours.")
    missing = local.keys - set(local.pops) - set(shared.pops)
    missing_ids = local.targets - set(local.ids) - set(shared.ids)
    chapters, _ = fragment_courses(root)
    routes = {alias for c in chapters for alias in c.get("covers", [c["code"]])} | {c["code"] for c in chapters}
    missing_routes = local.routes - routes - set(course["covers"])
    try:
        tree = ast.parse(contents[glossary_path].decode("utf-8"), filename=glossary_path)
    except SyntaxError as error:
        raise DeliveryError(f"Glossaire Python invalide : {error}") from error
    # Lire les références littérales sans exécuter le Python remis.
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "a":
            candidate = node.args[4] if len(node.args) >= 5 else next(
                (k.value for k in node.keywords if k.arg == "ref"), None)
            if isinstance(candidate, ast.Constant) and isinstance(candidate.value, str):
                if candidate.value not in set(local.pops) | set(shared.pops):
                    missing.add(candidate.value)
    if missing or missing_ids or missing_routes:
        raise DeliveryError(f"Références absentes : fenêtres={sorted(missing)}, "
                            f"ID={sorted(missing_ids)}, cours={sorted(missing_routes)}")
    return {"native_ids": len(local.ids), "native_popups": len(local.pops),
            "shared_popup_references": sorted(local.keys - set(local.pops))}


def package(root, code, title, covers, category, report, source_commit=None, author="Claude"):
    root = no_symlinks(root)
    course = {"code": code, "title": title, "covers": covers,
              "fragment": "S01", "category": category}
    metadata(course)
    if author not in ("Claude", "Codex"):
        raise DeliveryError("Auteur Claude ou Codex attendu.")
    if source_commit is None:
        source_commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    delivery.valid_sha(source_commit, 40)
    source = safe_child(root, f"chapters/{code}")
    if not source.is_dir():
        raise DeliveryError(f"Sources du nouveau cours absentes : {source}")
    contents = {}
    for path in sorted(source.iterdir()):
        if not path.is_file() or not re.fullmatch(re.escape(code) + r"_[\w-]+\.(html|json)", path.name):
            raise DeliveryError(f"Source hors format : {path}")
        value = text_file(path)
        if path.suffix == ".json":
            load_json(path)
        contents[path.relative_to(root).as_posix()] = value.encode("utf-8")
    glossary_path = f"glossary/{code.lower()}.py"
    contents[glossary_path] = text_file(safe_child(root, glossary_path)).encode("utf-8")
    checks = inspect_sources(root, course, contents)
    report_path = safe_child(root, report)
    report_data = text_file(report_path).encode("utf-8")
    if not report_data.strip():
        raise DeliveryError("Rapport vide.")
    directory = safe_child(root, f"livraisons/Livraison {author}/{LABEL}/production/{code}")
    if directory.exists():
        raise DeliveryError(f"Paquet déjà présent : {directory}")
    manifest = {"schema_version": 1, "kind": "new_course_delivery", "author": author,
                "status": "livré ; contrôles techniques seulement", "course": course,
                "source_parent_commit": source_commit,
                "report": {"path": "rapport.md", "original_path": report,
                           "sha256": digest(report_data)},
                "files": [{"target_path": name, "source_path": "sources/" + name,
                           "sha256": digest(value)} for name, value in contents.items()],
                "checks": checks, "limits": ["Validation médicale et complétude CIM-11 non certifiées."]}
    directory.parent.mkdir(parents=True, exist_ok=True)
    # Un dossier incomplet n'est jamais présenté comme une remise terminée.
    with tempfile.TemporaryDirectory(prefix=".new-course-", dir=directory.parent) as temp:
        stage = Path(temp) / code
        stage.mkdir()
        for name, data in contents.items():
            destination = safe_child(stage, "sources/" + name)
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)
        (stage / "rapport.md").write_bytes(report_data)
        (stage / "livraison.json").write_bytes(json_bytes(manifest))
        os.rename(stage, directory)
    return directory


def check(root, directory):
    root = no_symlinks(root)
    directory = Path(directory)
    directory = no_symlinks(directory if directory.is_absolute() else safe_child(root, directory.as_posix()))
    manifest = load_json(safe_child(directory, "livraison.json"))
    if manifest.get("schema_version") != 1 or manifest.get("kind") != "new_course_delivery":
        raise DeliveryError("Format de paquet inconnu.")
    code = metadata(manifest.get("course"))
    delivery.valid_sha(manifest.get("source_parent_commit"), 40)
    if not isinstance(manifest.get("files"), list) or not manifest["files"]:
        raise DeliveryError("Liste de fichiers obligatoire.")
    contents = {}
    for item in manifest["files"]:
        if not isinstance(item, dict):
            raise DeliveryError("Entrée de fichier invalide.")
        target, source = item.get("target_path", ""), item.get("source_path", "")
        safe_child(root, target)
        allowed = (re.fullmatch(rf"chapters/{code}/{code}_[\w-]+\.(html|json)", target)
                   or target == f"glossary/{code.lower()}.py")
        if not allowed or source != "sources/" + target or target in contents:
            raise DeliveryError(f"Chemin de source interdit ou répété : {target}")
        data = text_file(safe_child(directory, source)).encode("utf-8")
        delivery.valid_sha(item.get("sha256"))
        if digest(data) != item["sha256"]:
            raise DeliveryError(f"Empreinte incorrecte : {source}")
        if target.endswith(".json"):
            load_json(safe_child(directory, source))
        contents[target] = data
    report = manifest.get("report", {})
    if report.get("path") != "rapport.md":
        raise DeliveryError("Rapport rapport.md obligatoire.")
    safe_child(root, report.get("original_path", ""))
    data = text_file(safe_child(directory, report["path"])).encode("utf-8")
    if not data.strip() or digest(data) != report.get("sha256"):
        raise DeliveryError("Rapport vide ou empreinte incorrecte.")
    checks = inspect_sources(root, manifest["course"], contents)
    return manifest, contents, checks


def write_new(path, data):
    """Création exclusive : un fichier apparu entre contrôle et écriture est protégé."""
    no_symlinks(path)
    with open(path, "xb") as stream:
        try:
            os.fchmod(stream.fileno(), 0o644)
            stream.write(data)
        except BaseException:
            path.unlink(missing_ok=True)
            raise


def replace_catalog(path, data, expected):
    no_symlinks(path)
    if path.read_bytes() != expected:
        raise DeliveryError(f"Catalogue modifié simultanément : {path}")
    descriptor, temporary = tempfile.mkstemp(prefix=".new-course-", dir=path.parent)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            os.fchmod(stream.fileno(), 0o644)
            stream.write(data)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def apply(root, directory):
    root = no_symlinks(root)
    manifest, contents, checks = check(root, directory)
    course, code = manifest["course"], manifest["course"]["code"]
    chapter_path, fragment_path = safe_child(root, "chapters.json"), safe_child(root, "fragments.json")
    originals = {path: path.read_bytes() for path in (chapter_path, fragment_path)}
    chapters, fragments = load_json(chapter_path), load_json(fragment_path)
    if any(c.get("code") == code for c in chapters):
        raise DeliveryError(f"Cours déjà enregistré : {code}")
    existing_aliases = {alias for c in chapters if c.get("integrated")
                        for alias in c.get("covers", [c["code"]])} | {c["code"] for c in chapters}
    overlap = existing_aliases & set(course["covers"])
    if overlap:
        raise DeliveryError(f"Catégories déjà couvertes par un cours existant : {sorted(overlap)}")
    fragment = next((f for f in fragments if f.get("id") == "S01"), None)
    category = next((c for c in (fragment or {}).get("categories", [])
                     if c.get("id") == course["category"]), None)
    if category is None:
        raise DeliveryError("Fragment ou catégorie cible absents.")
    if any(code in f.get("rattachements", []) or any(code in c.get("chapters", [])
            for c in f.get("categories", [])) for f in fragments):
        raise DeliveryError(f"Rattachement existant : {code}")
    chapter_dir = safe_child(root, f"chapters/{code}")
    if chapter_dir.exists() or any(safe_child(root, target).exists() for target in contents):
        raise DeliveryError(f"Collision de sources : {code}")
    chapters.append({"code": code, "title": course["title"], "covers": course["covers"], "integrated": True})
    fragment["rattachements"].append(code)
    category["chapters"].append(code)
    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    receipt_path = safe_child(root, f"docs/collaboration/receipts/NEW_COURSE_{code}_{now}.json")
    receipt = {"schema_version": 1, "kind": "new_course_injection", "course": course,
               "source_parent_commit": manifest["source_parent_commit"],
               "manifest_sha256": digest(json_bytes(manifest)),
               "status": "injecté, reconstruction/contrôles à faire",
               "files": manifest["files"], "checks": checks,
               "report": manifest["report"], "limits": manifest.get("limits", [])}
    created, changed = [], []
    chapter_dir.mkdir()
    try:
        for target, data in contents.items():
            path = safe_child(root, target)
            path.parent.mkdir(parents=True, exist_ok=True)
            write_new(path, data)
            created.append(path)
        for path, value in ((chapter_path, chapters), (fragment_path, fragments)):
            replace_catalog(path, json_bytes(value), originals[path])
            changed.append(path)
        receipt_path.parent.mkdir(parents=True, exist_ok=True)
        write_new(receipt_path, json_bytes(receipt))
        created.append(receipt_path)
    except BaseException:
        for path in reversed(changed):
            replace_catalog(path, originals[path], path.read_bytes())
        for path in reversed(created):
            path.unlink(missing_ok=True)
        try:
            chapter_dir.rmdir()
        except OSError:
            pass
        raise
    return receipt_path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    sub = parser.add_subparsers(dest="command", required=True)
    packing = sub.add_parser("package")
    packing.add_argument("code")
    packing.add_argument("--title", required=True)
    packing.add_argument("--covers", nargs="+")
    packing.add_argument("--category", choices=("vaisseaux", "pression"))
    packing.add_argument("--report", required=True)
    packing.add_argument("--source-commit")
    packing.add_argument("--author", choices=("Claude", "Codex"), default="Claude")
    for command in ("check", "apply"):
        sub.add_parser(command).add_argument("directory", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "package":
            result = package(args.root, args.code, args.title, args.covers or [args.code],
                             args.category or ("pression" if args.code == "I95" else "vaisseaux"),
                             args.report, args.source_commit, args.author)
        elif args.command == "check":
            result = check(args.root, args.directory)[2]
        else:
            result = apply(args.root, args.directory)
        print(json.dumps(result, ensure_ascii=False) if isinstance(result, dict) else result)
    except (DeliveryError, OSError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"Échec : {error}\n")


if __name__ == "__main__":
    main()
