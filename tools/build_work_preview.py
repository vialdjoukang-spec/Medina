#!/usr/bin/env python3
"""Build the internal A41 work copy with the current fragment frontend.

The ten manifest-verified source files are copied into a temporary overlay.
Canonical chapters and the final-audit registry are never changed. The result
is a consultation preview, not a delivery for the fragment's final audit.

Usage: python3 tools/build_work_preview.py --output work/infectiologie.html
"""
import argparse
import base64
import gzip
import hashlib
import html
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile


FRAGMENT = "T1"
CHAPTER = "A41"
WORK_FOLDER = Path("livraisons/Livraison Codex/I-03-Infectiologie/travail/FRAGMENT_COMPLET_2026-10-08")
EXPECTED_FILES = {
    *(f"chapters/A41/A41_{suffix}.html" for suffix in
      ("a", "b", "c", "d", "pop1", "pop2", "pop_pa", "pop_sciences_revision")),
    "chapters/A41/A41_justifications.json",
    "glossary/a41.py",
}
WORK_LABEL = "Version de travail · cours en rédaction"


def json_text(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def read_sources(sources):
    manifest_path = sources.parent / "manifest_interne.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    rows = manifest.get("files", [])
    paths = [row["path"] for row in rows]
    if len(paths) != len(EXPECTED_FILES) or set(paths) != EXPECTED_FILES:
        raise ValueError("Le manifeste doit décrire exactement les dix sources internes A41.")
    actual = {p.relative_to(sources).as_posix() for p in sources.rglob("*") if p.is_file()}
    if actual != EXPECTED_FILES:
        raise ValueError("Le dossier sources ne correspond pas aux dix fichiers du manifeste.")
    verified_files = {}
    for row in rows:
        content = (sources / row["path"]).read_bytes()
        digest = hashlib.sha256(content).hexdigest()
        if digest != row.get("internal_sha256"):
            raise ValueError("Empreinte interne incorrecte : " + row["path"])
        verified_files[row["path"]] = content
    return manifest, verified_files


def create_overlay(root, verified_files, overlay):
    """Link unchanged frontend files; copy the course and shadow build metadata."""
    overlay.mkdir()
    excluded = {".git", "__pycache__", "dist", "work", "chapters", "glossary", "shell", "chapters.json"}
    for item in root.iterdir():
        if item.name not in excluded:
            (overlay / item.name).symlink_to(item, target_is_directory=item.is_dir())
    for name, content in verified_files.items():
        target = overlay / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
    for item in (root / "glossary").iterdir():
        target = overlay / "glossary" / item.name
        if item.name != "__pycache__" and not target.exists():
            target.symlink_to(item, target_is_directory=item.is_dir())
    chapters = json.loads((root / "chapters.json").read_text(encoding="utf-8"))
    if not any(chapter["code"] == CHAPTER for chapter in chapters):
        raise ValueError("A41 manque dans le catalogue de la base.")
    for chapter in chapters:
        chapter["integrated"] = chapter["code"] == CHAPTER
    (overlay / "chapters.json").write_text(json_text(chapters) + "\n", encoding="utf-8")
    # Integrated permits opening the lesson. Completed/audited is a distinct state:
    # historical chapter certification must not certify this new internal copy.
    (overlay / "shell").mkdir()
    for item in (root / "shell").iterdir():
        if item.name not in {"data.py", "__pycache__"}:
            (overlay / "shell" / item.name).symlink_to(item, target_is_directory=item.is_dir())
    build_data = (root / "shell/data.py").read_text(encoding="utf-8")
    build_data += "\n# Consultation of an internal work copy: no final certification.\nDONE_COURSES = set()\nDONE_SYS = set()\n"
    (overlay / "shell/data.py").write_text(build_data, encoding="utf-8")


def mark_preview(source, manifest):
    metadata = {
        "status": "work_in_progress", "fragment_id": FRAGMENT,
        "chapter_codes": [CHAPTER], "final_validation": False,
        "fragment_complete": False, "source_commit": manifest.get("source_commit"),
        "source_files": [{"path": row["path"], "sha256": row["internal_sha256"]}
                         for row in manifest["files"]],
    }
    for identifier in ("medora-data", "medina-category-organisation-data"):
        pattern = re.compile(r'(<script id="' + identifier + r'" type="application/json">)(.*?)(</script>)', re.S)
        match = pattern.search(source)
        if not match:
            raise ValueError("Métadonnées du frontend absentes : " + identifier)
        data = json.loads(match.group(2))
        data["work_preview"] = metadata
        if identifier == "medora-data":
            data["fragment"]["work_preview"] = True
        else:
            for block in data["blocks"]:
                for lesson in block["lessons"]:
                    if lesson["code"] == CHAPTER:
                        lesson["work_in_progress"] = True
        source = source[:match.start()] + match.group(1) + json_text(data) + match.group(3) + source[match.end():]
    head = '<script id="medina-work-preview-data">window.MEDINA_WORK_PREVIEW=' + json_text(metadata) + ';</script>'
    head += ('<script id="medina-work-preview-title">'
             'new MutationObserver(()=>{if(!document.title.endsWith(" · Version de travail"))'
             'document.title+=" · Version de travail";})'
             '.observe(document.querySelector("title"),{childList:true,subtree:true,characterData:true});'
             '</script>')
    head += ('<style id="medina-work-preview-style">'
             'html[data-medina-fragment] .topbar{display:flex;flex-wrap:wrap}'
             '.medina-work-preview{order:-1;flex:0 0 100%;margin:0;padding:10px 14px;border:1px solid #dfcc8a;'
             'border-radius:12px;background:#fff9e8;color:#57451b;font-family:inherit;font-size:1rem;line-height:1.5}'
             '.medina-work-preview strong{display:block;font-size:inherit}'
             '.medina-work-preview p{margin:3px 0 0;font-size:inherit}'
             '.medina-work-preview a{display:inline-block;margin-top:6px;color:inherit;text-decoration:underline;font-size:inherit}'
             '@media(min-width:1100px){.mc-navigo{top:calc(var(--medina-work-header-height,180px) + 4px)!important;transform:none!important}'
             '.mc-navigo-panel{top:0!important;transform:none!important;max-height:calc(100dvh - var(--medina-work-header-height,180px) - 16px)!important}}'
             '@media(max-width:700px){.medina-work-preview{padding:9px 12px}}'
             '</style>')
    source = source.replace("</head>", head + "</head>", 1)
    source, count = re.subn(r"<title>.*?</title>", "<title>Medina · Infectiologie · Version de travail</title>", source, count=1, flags=re.S)
    if count != 1:
        raise ValueError("Le titre de l’aperçu est absent.")
    banner = ('<aside class="medina-work-preview" id="medina-work-preview-banner" role="note">'
              '<strong>' + html.escape(WORK_LABEL) + '</strong>'
              '<p>I-03-Infectiologie · A41 — Sepsis et choc septique de l’adulte. '
              'Contenu en cours de revue interne.</p>'
              '<a href="#/home">Voir les catégories d’infectiologie</a></aside>')
    source, count = re.subn(r'(<header\b[^>]*\bclass="[^"]*\btopbar\b[^"]*"[^>]*>)',
                            lambda match: match.group(1) + banner, source, count=1)
    if count != 1:
        raise ValueError("La barre de navigation du frontend est absente.")
    measure_header = ('<script id="medina-work-preview-header">'
                      'const workHeader=document.querySelector(".topbar");'
                      'new ResizeObserver(()=>document.documentElement.style.setProperty('
                      '"--medina-work-header-height",workHeader.getBoundingClientRect().height+"px"))'
                      '.observe(workHeader);</script>')
    source = source.replace("</body>", measure_header + "</body>", 1)
    # Keep consultation notes separate from the regular fragment's notebook.
    source = source.replace("medina.fragment.T1.atlas", "medina.fragment.T1.work.atlas")
    return source


def verify_output(source):
    complete = re.search(r"window\.MEDINA_COMPLETE=(.*?);</script>", source, re.S)
    if not complete or json.loads(complete.group(1)):
        raise ValueError("Un statut de cours achevé subsiste dans l’aperçu.")
    pack = re.search(r'<script id="mdn-pack" type="application/octet-stream">(.*?)</script>', source, re.S)
    templates = gzip.decompress(base64.b64decode(pack.group(1))).decode("utf-8") if pack else source
    courses = re.findall(r'<template\b[^>]*\bid="ch-([^"]+)"', templates)
    if courses != [CHAPTER]:
        raise ValueError("L’aperçu doit contenir un seul cours, A41 : " + repr(courses))
    for panel in ("pA", "pE", "pS", "pP"):
        if f'id="{panel}"' not in templates:
            raise ValueError("Un des quatre onglets A41 manque : " + panel)
    if 'data-pop="a41-contraste-rein"' not in templates or 'data-pop="a41-j-gazometrie"' not in templates:
        raise ValueError("Une fenêtre de la dernière copie interne manque.")
    return len(re.findall(r'<template\b[^>]*\bdata-pop=', templates))


def main():
    sys.dont_write_bytecode = True
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--output", required=True, type=Path, help="HTML autonome de consultation à écrire")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="Base du frontend")
    parser.add_argument("--sources", type=Path, help="Dix sources internes A41 et manifeste dans leur parent")
    args = parser.parse_args()
    root = args.root.resolve()
    sources = (args.sources or root / WORK_FOLDER / "sources").resolve()
    destination = args.output.resolve()
    if destination.suffix.lower() != ".html":
        parser.error("--output doit désigner un fichier .html")
    protected = [root / name for name in ("chapters", "glossary", "shell", "engine", "tools", "livraisons")]
    if any(destination.is_relative_to(folder.resolve()) for folder in protected):
        parser.error("La sortie doit rester hors des dossiers de sources et de livraisons.")
    try:
        manifest, verified_files = read_sources(sources)
        fragment = next(item for item in json.loads((root / "fragments.json").read_text(encoding="utf-8"))
                        if item["id"] == FRAGMENT)
        destination.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix=".medina-work-preview-", dir=destination.parent) as temporary:
            workspace = Path(temporary)
            overlay, built = workspace / "overlay", workspace / "built"
            create_overlay(root, verified_files, overlay)
            environment = dict(os.environ, MEDINA_ROOT=str(overlay), MEDINA_OUT=str(built),
                               PYTHONDONTWRITEBYTECODE="1", TMPDIR=str(workspace))
            subprocess.run([sys.executable, str(root / "build_front.py"), "--fragment", FRAGMENT],
                           env=environment, cwd=overlay, check=True)
            result = built / "fragments" / f"MEDINA_{FRAGMENT}_{fragment['slug']}.html"
            source = mark_preview(result.read_text(encoding="utf-8"), manifest)
            windows = verify_output(source)
            sys.path.insert(0, str(root))
            from tools.atomic_output import atomic_output
            with atomic_output(destination) as staging:
                Path(staging).write_text(source, encoding="utf-8")
        print(f"Aperçu de travail : {destination} ({len(source.encode('utf-8'))} octets, quatre onglets, {windows} fenêtres)")
        print("Aucune source canonique ni aucun statut d’audit final modifié.")
    except (OSError, ValueError, KeyError, StopIteration, subprocess.CalledProcessError) as error:
        parser.exit(1, "Construction de l’aperçu impossible : " + str(error) + "\n")


if __name__ == "__main__":
    main()
