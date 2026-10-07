#!/usr/bin/env python3
"""Export partagé des cours et injection contrôlée d'une remise Claude.

Cet outil ne construit pas MEDINA et ne réalise aucun audit médical ou navigateur.
Les dossiers copiés sont des sources de travail ; ils ne certifient pas CIM-11.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from urllib.parse import quote


DEFAULT_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "https://github.com/vialdjoukang-spec/Medina"
PAGES = "https://vialdjoukang-spec.github.io/Medina"
PARTIAL = "partiel ; complétude CIM-11 non établie"
INJECTED = "injecté, reconstruction/contrôles à faire"


class DeliveryError(ValueError):
    pass


def digest(data):
    return hashlib.sha256(data).hexdigest()


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def no_symlinks(path):
    """Inspecter les composants avant resolve(), qui masquerait les liens."""
    path = Path(os.path.abspath(path))
    cursor = Path(path.anchor)
    for part in path.parts[1:]:
        cursor /= part
        if cursor.is_symlink():
            raise DeliveryError(f"Lien symbolique interdit : {cursor}")
    return path


def safe_child(directory, relative):
    if not isinstance(relative, str) or not relative or "\\" in relative:
        raise DeliveryError(f"Chemin relatif invalide : {relative!r}")
    parts = PurePosixPath(relative)
    if parts.is_absolute() or any(p in (".", "..") for p in parts.parts):
        raise DeliveryError(f"Chemin absolu ou traversée interdite : {relative}")
    if str(parts) != relative or re.match(r"^[A-Za-z]:", relative):
        raise DeliveryError(f"Chemin non normalisé : {relative}")
    result = no_symlinks(Path(directory) / relative)
    if not result.is_relative_to(no_symlinks(directory)):
        raise DeliveryError(f"Chemin hors du dossier : {relative}")
    return result


def load_json(path):
    no_symlinks(path)
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise DeliveryError(f"JSON illisible : {path} ({error})") from error


def valid_sha(value, length=64):
    if not isinstance(value, str) or not re.fullmatch(rf"[0-9a-f]{{{length}}}", value):
        raise DeliveryError(f"Empreinte SHA invalide : {value!r}")
    return value


def catalog(root):
    """Reproduire le filtre de build_front.py sans importer son exécution."""
    fragments = load_json(root / "fragments.json")
    names = load_json(root / "organisation/fragments.json")
    chapters = load_json(root / "chapters.json")
    if not all(isinstance(x, list) for x in (fragments, names, chapters)):
        raise DeliveryError("Les trois catalogues doivent être des listes JSON.")
    public = {f["id"]: f for f in names}
    if len(public) != len(names):
        raise DeliveryError("Identifiant de fragment en double dans organisation/fragments.json.")
    html = safe_child(root, "shell/medina_front.html").read_text(encoding="utf-8")
    match = re.search(r'<script id="medora-data" type="application/json">(.*?)</script>', html, re.S)
    if not match:
        raise DeliveryError("Catalogue medora-data introuvable dans la coque.")
    entries = json.loads(match.group(1))["entries"]
    systems = {e["code"]: e.get("system") for e in entries}
    explicit = {code for f in fragments for code in f["rattachements"]
                if re.fullmatch(r"[A-Z][0-9]{2}", code)}
    result = {}
    for f in fragments:
        if f["id"] not in public:
            raise DeliveryError(f"Nom public absent pour {f['id']}.")
        name = public[f["id"]]
        label = name["label"]
        if not isinstance(label, str) or not label.strip() or any(x in label for x in ("/", "\\", "\n", "\r")) or label in (".", ".."):
            raise DeliveryError(f"Nom de dossier invalide pour {f['id']} : {label!r}")
        attached = set(f["rattachements"])
        owned = [c for c in chapters if c.get("integrated") and
                 (c["code"] in attached or
                  (c["code"] not in explicit and systems.get(c["code"]) in attached))]
        for c in owned:
            if not re.fullmatch(r"[A-Z][0-9]{2}", c["code"]) or not c.get("title"):
                raise DeliveryError(f"Code ou titre invalide : {c!r}")
        result[f["id"]] = {**f, **name, "chapters": owned}
    return result


def selection(data, fragment):
    if fragment.upper() == "ALL":
        return sorted(data.values(), key=lambda f: (f.get("order", 999), f["id"]))
    ident = fragment.upper()
    if ident not in data:
        raise DeliveryError(f"Fragment inconnu : {fragment}")
    return [data[ident]]


def primary_sources(root, fragment):
    files = {}
    for chapter in fragment["chapters"]:
        directory = safe_child(root, f"chapters/{chapter['code']}")
        if not directory.is_dir():
            raise DeliveryError(f"Dossier de cours absent : {directory}")
        found = sorted(p for p in directory.iterdir() if p.suffix in (".html", ".json"))
        if not any(p.suffix == ".html" for p in found):
            raise DeliveryError(f"Aucun HTML source pour {chapter['code']}.")
        for path in found:
            no_symlinks(path)
            if not path.is_file():
                raise DeliveryError(f"Une source doit être un fichier : {path}")
            files[path.relative_to(root).as_posix()] = path.read_bytes()
    return files


def chapter_records(fragment):
    return [{"code": c["code"], "title": c["title"], "covers": c.get("covers", []),
             "owner_fragment": fragment["id"]} for c in fragment["chapters"]]


def packet_manifest(fragment, source_commit, files, author="Codex", template=False):
    return {
        "schema_version": 1,
        "kind": "claude_contribution" if author == "Claude" else "codex_source_packet",
        "author": author,
        "status": "aucune contribution déposée" if template else PARTIAL,
        "fragment": {k: fragment.get(k, "") for k in ("id", "label", "specialty")},
        "source_commit": valid_sha(source_commit, 40),
        "code_reference": "CIM-10-GM 2024 ; inventaire CIM-11 non établi",
        "chapters": chapter_records(fragment),
        "files": [{"target_path": path, "source_path": "sources/" + path, "sha256": digest(content)}
                  for path, content in files.items()] if not template else [],
        "checks": [],
        "limits": ["La copie de sources ne valide ni la médecine ni la complétude CIM-11.",
                   "Les fichiers communs restent accessibles dans le dépôt canonique."],
    }


def packet_directory(root, author, fragment):
    return safe_child(root, f"livraisons/Livraison {author}/{fragment['label']}")


def readme(fragment, author, source_commit):
    common = ["chapters.json", "fragments.json", "glossary", "modules", "engine", "shell",
              "build_front.py", "tests", "organisation/fragments.json"]
    links = " · ".join(
        f"[{p}]({REPOSITORY}/{'blob' if '.' in Path(p).name else 'tree'}/"
        f"{'main' if p == 'organisation/fragments.json' else source_commit}/{quote(p)})"
        for p in common
    )
    course_lines = "\n".join("| {} | {} |".format(c["code"], c["title"].replace("|", "\\|"))
                            for c in fragment["chapters"])
    if not course_lines:
        course_lines = "| — | Aucun cours intégré dans ce fragment ; production à poursuivre. |"
    route = f"{PAGES}/fragments/MEDINA_{fragment['id']}_{fragment['slug']}.html"
    if author == "Claude":
        mode = ("Ce dossier reçoit les corrections de Claude. Une copie préparée par l'outil est un espace de travail ; "
                "elle ne constitue pas une livraison relue.\n\n"
                "Copier ou préparer `livraison.json`, conserver les empreintes `sha256` des fichiers originaux, "
                "puis modifier les fichiers sous `sources/chapters/`. Décrire les corrections et les sources médicales "
                "dans un rapport. Les fichiers communs et CS sont corrigés directement sur une branche avec PR.\n")
    else:
        mode = ("Les fichiers sous `sources/chapters/` reproduisent intégralement les HTML et JSON des cours intégrés. "
                "Ils conservent les fenêtres et leurs repères. Le manifeste `livraison.json` donne les chemins canoniques "
                "et les empreintes originales.\n")
    return (f"# {fragment['label']} — Livraison {author}\n\n"
            f"Fragment : **{fragment['id']}**. Base de contenu : `{source_commit}`. État : **{PARTIAL}**.\n\n"
            f"{mode}\n"
            f"[Lire le fragment HTML]({route}) · [Organisation]({PAGES}/organisation.html) · "
            f"[Toutes les sources]({REPOSITORY}/tree/{source_commit})\n\n"
            f"Sources communes : {links}.\n\n"
            f"| Code | Cours |\n| --- | --- |\n{course_lines}\n\n"
            "L'existence d'un cours ou de catégories CIM-10 ne certifie pas une couverture CIM-11 complète. "
            "Les textes sont intégrés dans les dossiers canoniques, puis les fragments sont reconstruits et contrôlés.\n").encode("utf-8")


def existing_baseline(directory):
    manifest = safe_child(directory, "livraison.json")
    if not manifest.exists():
        return {}
    data = load_json(manifest)
    if not isinstance(data, dict) or not isinstance(data.get("files"), list):
        raise DeliveryError(f"Manifeste existant invalide : {manifest}")
    return {f["target_path"]: valid_sha(f["sha256"]) for f in data["files"]}


def plan_packet(root, fragment, source_commit, files, author="Codex"):
    directory = packet_directory(root, author, fragment)
    baseline = existing_baseline(directory)
    plans = []
    for target, content in files.items():
        destination = safe_child(directory, "sources/" + target)
        if destination.exists():
            if not destination.is_file():
                raise DeliveryError(f"Source de livraison invalide : {destination}")
            previous = destination.read_bytes()
            if previous != content and digest(previous) != baseline.get(target):
                raise DeliveryError(f"Copie modifiée : export interrompu pour préserver {destination}")
        plans.append((destination, content))
    manifest = packet_manifest(fragment, source_commit, files, author)
    if author == "Claude":
        manifest["status"] = "copie de travail ; aucune correction livrée"
    plans.append((safe_child(directory, "livraison.json"), json_bytes(manifest)))
    source_readme = (
        f"# Sources de {fragment['label']}\n\n"
        f"Ce dossier réunit les sources complètes de {len(fragment['chapters'])} cours intégrés. "
        "Les codes et titres figurent dans le README du fragment et dans `../livraison.json`.\n\n"
        + ("Aucun cours n'est encore intégré dans ce fragment. La présence de catégories dans le catalogue "
           "ne constitue pas une livraison de leçons.\n\n" if not fragment["chapters"] else "")
        + f"[Sources communes et catalogue]({REPOSITORY}/tree/{source_commit}) · "
        f"[Organisation de MEDINA]({PAGES}/organisation.html).\n\n"
        f"État : **{PARTIAL}**. "
        "Une copie préparée pour Claude reste un espace de travail jusqu'à la remise de corrections et d'un rapport.\n"
    ).encode("utf-8")
    plans.append((safe_child(directory, "sources/README.md"), source_readme))
    destination = safe_child(directory, "README.md")
    if destination.exists() and not destination.is_file():
        raise DeliveryError(f"Le README doit être un fichier : {destination}")
    if author == "Codex" or not destination.exists():
        plans.append((destination, readme(fragment, author, source_commit)))
    return plans


def write_plans(plans):
    # Contrôler aussi les README et les ancêtres bloqués, avant toute écriture.
    for path, _ in plans:
        no_symlinks(path)
        if path.exists() and not path.is_file():
            raise DeliveryError(f"Destination occupée par autre chose qu'un fichier : {path}")
        for ancestor in path.parents:
            if ancestor.exists() and not ancestor.is_dir():
                raise DeliveryError(f"Dossier parent occupé par un fichier : {ancestor}")
    for path, data in plans:
        no_symlinks(path)
        if path.exists() and path.read_bytes() == data:
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)


def export_codex(root, fragment_id, source_commit):
    valid_sha(source_commit, 40)
    selected = selection(catalog(root), fragment_id)
    plans, count = [], 0
    for fragment in selected:
        files = primary_sources(root, fragment)
        count += len(files)
        plans += plan_packet(root, fragment, source_commit, files)
        claude = packet_directory(root, "Claude", fragment)
        for name, content in (
            ("README.md", readme(fragment, "Claude", source_commit)),
            ("livraison.template.json", json_bytes(packet_manifest(fragment, source_commit, {}, "Claude", True))),
        ):
            path = safe_child(claude, name)
            if path.exists() and not path.is_file():
                raise DeliveryError(f"Destination Claude invalide : {path}")
            elif not path.exists():
                plans.append((path, content))
    # Tout le lot est examiné avant d'écrire la première copie.
    write_plans(plans)
    return {"action": "export-codex", "fragments": [f["id"] for f in selected],
            "source_files": count, "source_commit": source_commit, "status": PARTIAL}


def prepare_claude(root, fragment_id):
    plans, selected = [], selection(catalog(root), fragment_id)
    for fragment in selected:
        source_dir = packet_directory(root, "Codex", fragment)
        manifest = load_json(safe_child(source_dir, "livraison.json"))
        if manifest.get("fragment", {}).get("id") != fragment["id"]:
            raise DeliveryError(f"Fragment incohérent dans {source_dir}")
        allowed = primary_sources(root, fragment)
        files = {}
        for record in manifest.get("files", []):
            target = record["target_path"]
            if target not in allowed:
                raise DeliveryError(f"Source Codex hors périmètre : {target}")
            path = safe_child(source_dir, "sources/" + target)
            data = path.read_bytes()
            if digest(data) != valid_sha(record["sha256"]):
                raise DeliveryError(f"Copie Codex modifiée : {target}")
            if data != allowed[target]:
                raise DeliveryError(f"Base Codex périmée pour {target} ; réexporter les sources actuelles.")
            files[target] = data
        if set(files) != set(allowed):
            raise DeliveryError(f"Paquet Codex incomplet pour {fragment['id']}.")
        plans += plan_packet(root, fragment, manifest["source_commit"], files, "Claude")
    write_plans(plans)
    return {"action": "prepare-claude", "fragments": [f["id"] for f in selected],
            "status": "copie de travail ; aucune correction livrée"}


def inspect_claude(root, directory):
    directory = no_symlinks(directory)
    manifest = load_json(safe_child(directory, "livraison.json"))
    if not isinstance(manifest, dict) or manifest.get("schema_version") != 1:
        raise DeliveryError("Version de manifeste Claude non reconnue.")
    if manifest.get("author") != "Claude" or manifest.get("kind") != "claude_contribution":
        raise DeliveryError("Le manifeste doit identifier une contribution Claude.")
    valid_sha(manifest.get("source_commit"), 40)
    fragments = catalog(root)
    if not isinstance(manifest.get("fragment"), dict):
        raise DeliveryError("Le champ fragment doit être un objet JSON.")
    ident = manifest["fragment"].get("id")
    if ident not in fragments:
        raise DeliveryError(f"Fragment Claude inconnu : {ident!r}")
    fragment = fragments[ident]
    if manifest["fragment"].get("label") != fragment["label"]:
        raise DeliveryError("Le nom du fragment diffère du catalogue actuel.")
    chapters = {c["code"]: c["title"] for c in fragment["chapters"]}
    announced = manifest.get("chapters")
    if not isinstance(announced, list):
        raise DeliveryError("La liste des cours est obligatoire.")
    for chapter in announced:
        if not isinstance(chapter, dict):
            raise DeliveryError("Chaque cours annoncé doit être un objet JSON.")
        if chapters.get(chapter.get("code")) != chapter.get("title"):
            raise DeliveryError(f"Code ou titre de cours incohérent : {chapter!r}")
    records = manifest.get("files")
    if not isinstance(records, list) or not records:
        raise DeliveryError("Aucun fichier livré ; un modèle vide n'est pas une contribution.")
    sources = safe_child(directory, "sources")
    if not sources.is_dir():
        raise DeliveryError("Dossier sources absent de la livraison Claude.")
    for entry in sources.rglob("*"):
        if entry.is_symlink():
            raise DeliveryError(f"Lien symbolique dans les sources livrées : {entry}")
    allowed, seen, changed = primary_sources(root, fragment), set(), []
    announced_codes = {c["code"] for c in announced}
    for record in records:
        if not isinstance(record, dict):
            raise DeliveryError("Une entrée files doit être un objet JSON.")
        target = record.get("target_path")
        canonical = safe_child(root, target)
        if target not in allowed or PurePosixPath(target).parts[1] not in announced_codes:
            raise DeliveryError(f"Fichier hors des cours autorisés du fragment {ident} : {target}")
        if target in seen:
            raise DeliveryError(f"Fichier déclaré deux fois : {target}")
        seen.add(target)
        if record.get("source_path", "sources/" + target) != "sources/" + target:
            raise DeliveryError(f"Le fichier livré doit conserver son chemin canonique : {target}")
        original = valid_sha(record.get("sha256"))
        if digest(allowed[target]) != original:
            raise DeliveryError(f"Source canonique modifiée depuis la remise : {target}. Réconcilier les versions avant injection.")
        payload = safe_child(directory, "sources/" + target)
        if not payload.is_file():
            raise DeliveryError(f"Fichier livré absent : {payload}")
        proposed = payload.read_bytes()
        if not proposed:
            raise DeliveryError(f"Fichier livré vide : {target}")
        try:
            decoded = proposed.decode("utf-8")
            if payload.suffix == ".json":
                json.loads(decoded)
        except (UnicodeError, json.JSONDecodeError) as error:
            raise DeliveryError(f"Source livrée invalide : {target} ({error})") from error
        if record.get("proposed_sha256") is not None and digest(proposed) != valid_sha(record["proposed_sha256"]):
            raise DeliveryError(f"Empreinte du fichier corrigé incohérente : {target}")
        if proposed != allowed[target]:
            changed.append({"target_path": target, "path": canonical, "original": allowed[target],
                            "proposed": proposed, "original_sha256": original, "proposed_sha256": digest(proposed)})
    if not changed:
        raise DeliveryError("Aucune source corrigée ; cette copie de travail ne constitue pas une livraison.")
    return manifest, fragment, changed, len(records)


def check_claude(root, directory):
    manifest, fragment, changed, count = inspect_claude(root, directory)
    return {"action": "check-claude", "fragment": fragment["id"], "label": fragment["label"],
            "source_commit": manifest["source_commit"], "verified_files": count,
            "changed_files": [c["target_path"] for c in changed],
            "status": "empreintes et chemins conformes ; sources corrigées à examiner ; aucune injection"}


def apply_claude(root, directory):
    manifest, fragment, changed, count = inspect_claude(root, directory)
    # Les fichiers sont tous validés avant préparation puis remplacement.
    staged, replaced = [], []
    now = datetime.now(timezone.utc)
    receipt_name = f"CLAUDE_PACKET_{fragment['id']}_{now.strftime('%Y%m%dT%H%M%S%fZ')}.json"
    receipt_path = safe_child(root, "docs/collaboration/receipts/" + receipt_name)
    if receipt_path.exists():
        raise DeliveryError("Un reçu existe déjà sous ce nom ; aucun fichier n'a été injecté.")
    try:
        for change in changed:
            with tempfile.NamedTemporaryFile(dir=change["path"].parent, prefix=".livraison-", delete=False) as output:
                output.write(change["proposed"])
                staged.append((Path(output.name), change))
            os.chmod(output.name, change["path"].stat().st_mode & 0o777)
        for change in changed:
            no_symlinks(change["path"])
            if digest(change["path"].read_bytes()) != change["original_sha256"]:
                raise DeliveryError(f"Modification concurrente détectée : {change['target_path']}")
        for temporary, change in staged:
            os.replace(temporary, change["path"])
            replaced.append(change)
        receipt = {"schema_version": 1, "producer": "Claude", "received_by": "tools/livraison.py",
                   "received_at": now.isoformat(), "source_commit": manifest["source_commit"],
                   "fragment": {"id": fragment["id"], "label": fragment["label"]},
                   "status": INJECTED, "verification_scope": "chemins, empreintes originales et présence des corrections",
                   "checks": [], "integration_commit": None, "publication": "non effectuée par cet outil",
                   "files": [{k: c[k] for k in ("target_path", "original_sha256", "proposed_sha256")} for c in changed],
                   "limits": ["Reconstruction et contrôles du projet à exécuter.", "Validation médicale et complétude CIM-11 non établies par cet outil."]}
        receipt_path.parent.mkdir(parents=True, exist_ok=True)
        receipt_path.write_bytes(json_bytes(receipt))
    except Exception:
        for change in reversed(replaced):
            change["path"].write_bytes(change["original"])
        raise
    finally:
        for temporary, _ in staged:
            temporary.unlink(missing_ok=True)
    return {"action": "apply-claude", "fragment": fragment["id"], "verified_files": count,
            "changed_files": [c["target_path"] for c in changed],
            "receipt": receipt_path.relative_to(root).as_posix(), "status": INJECTED}


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    aliases = {"--export-codex": "export-codex", "--prepare-claude": "prepare-claude",
               "--check-claude": "check-claude", "--apply-claude": "apply-claude"}
    if argv and argv[0] in aliases:
        argv[0] = aliases[argv[0]]
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("export-codex", "prepare-claude", "check-claude", "apply-claude"):
        sub = commands.add_parser(name)
        sub.add_argument("--root", type=Path, default=DEFAULT_ROOT, help="Racine du dépôt MEDINA.")
        if name in ("export-codex", "prepare-claude"):
            sub.add_argument("--fragment", default="ALL", help="Identifiant du fragment, ou ALL.")
        else:
            sub.add_argument("directory", type=Path, help="Dossier contenant livraison.json et sources/.")
        if name == "export-codex":
            sub.add_argument("--source-commit", required=True, help="SHA complet du contenu exporté.")
    args = parser.parse_args(argv)
    try:
        root = no_symlinks(args.root)
        if args.command == "export-codex":
            result = export_codex(root, args.fragment, args.source_commit)
        elif args.command == "prepare-claude":
            result = prepare_claude(root, args.fragment)
        elif args.command == "check-claude":
            result = check_claude(root, args.directory)
        else:
            result = apply_claude(root, args.directory)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (DeliveryError, OSError, KeyError, TypeError, UnicodeError, json.JSONDecodeError) as error:
        print(f"Livraison interrompue : {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
