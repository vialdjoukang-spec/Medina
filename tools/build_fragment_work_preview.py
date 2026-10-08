#!/usr/bin/env python3
"""Compile a manifest-verified, multi-chapter T1 consultation preview.

Sources stay in the internal production folder. A temporary overlay makes only
the declared chapters readable, without changing canonical medical sources or
certification. The current fragment frontend and its fonts are reused as-is.
"""
import argparse
import base64
import gzip
import hashlib
import html
from html.parser import HTMLParser
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import tempfile


FRAGMENT = "T1"
WORK_FOLDER = Path("livraisons/Livraison Codex/I-03-Infectiologie/travail/PRODUCTION_FRAGMENT_2026-10-08")
REQUIRED_SUFFIXES = ("a", "b", "c", "d", "pop1", "pop2", "pop_pa")
PANELS = {"pA", "pE", "pS", "pP"}


def json_text(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def frontend_owners(root):
    """Read the same ownership rules as the frontend being compiled."""
    spec = importlib.util.spec_from_file_location("preview_fragment_surface", root / "fragment_surface.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.frontend_catalog(root)[1]


def validate_manifest(manifest, owners):
    if type(manifest.get("schema_version")) is not int or manifest["schema_version"] != 1:
        raise ValueError("Version de manifeste interne non reconnue.")
    if manifest.get("kind") != "internal_fragment_work" or manifest.get("fragment_id") != FRAGMENT:
        raise ValueError("Le manifeste doit décrire le travail interne du fragment T1.")
    for flag in ("fragment_complete", "external_audit", "canonical_injection"):
        if manifest.get(flag) is not False:
            raise ValueError("L’aperçu exige un statut non final : " + flag)
    if not isinstance(manifest.get("source_commit"), str) or not manifest["source_commit"].strip():
        raise ValueError("Le commit source manque dans le manifeste.")
    codes, chapters = manifest.get("chapter_codes"), manifest.get("chapters")
    if (not isinstance(codes, list) or not codes or
            any(not isinstance(code, str) or not re.fullmatch(r"[A-Z][0-9]{2}", code) for code in codes) or
            len(set(codes)) != len(codes)):
        raise ValueError("Les codes de chapitres doivent être uniques et explicites.")
    if not isinstance(chapters, list) or any(not isinstance(row, dict) for row in chapters):
        raise ValueError("Les chapitres du manifeste sont absents.")
    if [row.get("code") for row in chapters] != codes:
        raise ValueError("Les chapitres doivent correspondre à chapter_codes, dans le même ordre.")
    covered = set()
    for chapter in chapters:
        code, title, covers = chapter["code"], chapter.get("title"), chapter.get("covers")
        if not isinstance(title, str) or not title.strip():
            raise ValueError("L’intitulé complet manque : " + code)
        if (not isinstance(covers, list) or not covers or
                any(not isinstance(item, str) or not re.fullmatch(r"[A-Z][0-9]{2}", item) for item in covers) or
                len(set(covers)) != len(covers) or code not in covers):
            raise ValueError("La couverture du chapitre est incorrecte : " + code)
        if any(owners.get(item) != FRAGMENT for item in covers):
            raise ValueError("Un code est étranger à l’infectiologie : " + code)
        if covered.intersection(covers):
            raise ValueError("Deux chapitres couvrent le même code.")
        covered.update(covers)
    required = {name for code in codes for name in (
        *(f"chapters/{code}/{code}_{suffix}.html" for suffix in REQUIRED_SUFFIXES),
        f"glossary/{code.lower()}.py",
    )}
    allowed = set(required)
    allowed.update(f"chapters/{code}/{code}_pop_sciences_revision.html" for code in codes)
    allowed.update(f"chapters/{code}/{code}_pop3.html" for code in codes)
    if "A41" in codes:
        allowed.add("chapters/A41/A41_justifications.json")
    return required, allowed


def read_sources(sources, root):
    """Reject undeclared files, path escapes and symlinks before reading bytes."""
    sources, root = Path(sources).absolute(), Path(root)
    if any(path.is_symlink() for path in (sources, *sources.parents)) or not sources.is_dir():
        raise ValueError("Le dossier sources doit être un dossier réel.")
    manifest_path = sources.parent / "manifest_interne.json"
    if manifest_path.is_symlink():
        raise ValueError("Le manifeste ne peut pas être un lien symbolique.")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not isinstance(manifest, dict):
        raise ValueError("Le manifeste interne doit être un objet JSON.")
    required, allowed = validate_manifest(manifest, frontend_owners(root))
    rows = manifest.get("files")
    if not isinstance(rows, list) or not rows:
        raise ValueError("Le manifeste ne contient aucun fichier.")
    paths = []
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get("path"), str):
            raise ValueError("Chaque fichier doit porter un chemin relatif explicite.")
        path = row["path"]
        relative = PurePosixPath(path)
        if (relative.is_absolute() or "\\" in path or any(part in (".", "..", "") for part in path.split("/")) or
                path not in allowed):
            raise ValueError("Chemin source non autorisé : " + path)
        if not isinstance(row.get("internal_sha256"), str) or not re.fullmatch(r"[0-9a-f]{64}", row["internal_sha256"]):
            raise ValueError("Empreinte SHA-256 absente ou incorrecte : " + path)
        paths.append(path)
    if len(paths) != len(set(paths)) or not required.issubset(paths):
        raise ValueError("Le manifeste contient des doublons ou omet des sources de chapitre.")
    actual = set()
    for item in sources.rglob("*"):
        if item.is_symlink():
            raise ValueError("Lien symbolique interdit dans les sources : " + str(item))
        if item.is_file():
            actual.add(item.relative_to(sources).as_posix())
        elif not item.is_dir():
            raise ValueError("Type de fichier source non autorisé : " + str(item))
    if actual != set(paths):
        raise ValueError("Le dossier sources ne correspond pas exactement au manifeste.")
    verified = {}
    for row in rows:
        content = (sources / row["path"]).read_bytes()
        if hashlib.sha256(content).hexdigest() != row["internal_sha256"]:
            raise ValueError("Empreinte interne incorrecte : " + row["path"])
        verified[row["path"]] = content
    return manifest, verified


def create_overlay(root, verified_files, manifest, overlay):
    """Copy work sources and shadow build metadata; keep the frontend unchanged."""
    root, overlay = Path(root), Path(overlay)
    overlay.mkdir()
    excluded = {".git", "__pycache__", "dist", "work", "chapters", "glossary", "shell", "chapters.json", "organisation"}
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
    # Historical modules share cardio_1.G and can overwrite a draft definition
    # long after a41/b24 were loaded. Replay the verified internal sources last;
    # plain imports would return already-mutated dictionaries from sys.modules.
    final_name = max(item.name for item in (overlay / "glossary").glob("*.py"))[:-3] + "_internal_work.py"
    glossary_sources = [(f"glossary/{code.lower()}.py", verified_files[f"glossary/{code.lower()}.py"].decode("utf-8"))
                        for code in manifest["chapter_codes"]]
    replay = ("# Generated only in the consultation overlay.\n"
              "_internal_glossary = {}\n"
              "for _path, _source in " + repr(glossary_sources) + ":\n"
              "    _scope = {'__name__': __name__, '__file__': _path, '__package__': None}\n"
              "    exec(compile(_source, _path, 'exec'), _scope)\n"
              "    _internal_glossary.update(_scope.get('G', {}))\n"
              "G = _internal_glossary\n")
    (overlay / "glossary" / final_name).write_text(replay, encoding="utf-8")
    chapters = json.loads((root / "chapters.json").read_text(encoding="utf-8"))
    work = {chapter["code"]: chapter for chapter in manifest["chapters"]}
    existing = {chapter["code"] for chapter in chapters}
    for chapter in chapters:
        chapter["integrated"] = chapter["code"] in work
        if chapter["code"] in work:
            chapter.update(work[chapter["code"]], owner=FRAGMENT, work_in_progress=True)
    for code in manifest["chapter_codes"]:
        if code not in existing:
            chapters.append(dict(work[code], integrated=True, owner=FRAGMENT, work_in_progress=True))
    (overlay / "chapters.json").write_text(json_text(chapters) + "\n", encoding="utf-8")
    # A historical group must not replace the declared work title/coverage.
    (overlay / "organisation").mkdir()
    for item in (root / "organisation").iterdir():
        if item.name != "course_groups.json":
            (overlay / "organisation" / item.name).symlink_to(item, target_is_directory=item.is_dir())
    groups_path = root / "organisation/course_groups.json"
    if groups_path.exists():
        groups = json.loads(groups_path.read_text(encoding="utf-8"))
        group_rows = groups if isinstance(groups, list) else groups.get("groups", groups.get("courses", []))
        for group in group_rows:
            if group["code"] in work:
                group.update(work[group["code"]], owner=FRAGMENT)
        (overlay / "organisation/course_groups.json").write_text(json_text(groups) + "\n", encoding="utf-8")
    (overlay / "shell").mkdir()
    for item in (root / "shell").iterdir():
        if item.name not in {"data.py", "__pycache__"}:
            (overlay / "shell" / item.name).symlink_to(item, target_is_directory=item.is_dir())
    build_data = (root / "shell/data.py").read_text(encoding="utf-8")
    build_data += "\n# Internal fragment consultation: no final certification.\nDONE_COURSES = set()\nDONE_SYS = set()\n"
    (overlay / "shell/data.py").write_text(build_data, encoding="utf-8")


def mark_preview(source, manifest):
    """Reuse the existing work-preview banner and reader-safe mobile styling."""
    from tools import build_work_preview as legacy
    source = legacy.mark_preview(source, manifest)
    metadata = {
        "status": "work_in_progress", "fragment_id": FRAGMENT,
        "chapter_codes": manifest["chapter_codes"], "final_validation": False,
        "fragment_complete": False, "external_audit": False, "canonical_injection": False,
        "source_commit": manifest["source_commit"],
        "source_files": [{"path": row["path"], "sha256": row["internal_sha256"]} for row in manifest["files"]],
    }
    codes = set(manifest["chapter_codes"])
    for identifier in ("medora-data", "medina-category-organisation-data"):
        pattern = re.compile(r'(<script id="' + identifier + r'" type="application/json">)(.*?)(</script>)', re.S)
        match = pattern.search(source)
        data = json.loads(match.group(2))
        data["work_preview"] = metadata
        if identifier == "medora-data":
            for course in data["fragment"].get("courses", []):
                if course["code"] in codes:
                    course.update(work_in_progress=True, complete=False)
        else:
            for course in data.get("courses", []):
                if course["code"] in codes:
                    course["work_in_progress"] = True
            for block in data["blocks"]:
                for lesson in block["lessons"]:
                    if lesson["code"] in codes:
                        lesson["work_in_progress"] = True
        source = source[:match.start()] + match.group(1) + json_text(data) + match.group(3) + source[match.end():]
    source = re.sub(r'(window\.MEDINA_WORK_PREVIEW=).*?(;</script>)',
                    lambda match: match.group(1) + json_text(metadata) + match.group(2), source, count=1, flags=re.S)
    labels = "; ".join(chapter["code"] + " — " + chapter["title"] for chapter in manifest["chapters"])
    course_count = len(manifest["chapters"])
    banner = ('<aside class="medina-work-preview" id="medina-work-preview-banner" role="note">'
              '<strong>Version de travail · Infectiologie <span>' + str(course_count) +
              ' cours</span></strong><details><summary>Chapitres visibles</summary><p>' +
              html.escape(labels) + '</p></details>'
              '<a id="medina-work-categories-link" href="#/home">Voir les catégories</a></aside>')
    source, count = re.subn(r'<aside class="medina-work-preview".*?</aside>', lambda _: banner, source, count=1, flags=re.S)
    if count != 1:
        raise ValueError("Le bandeau de consultation est absent.")
    runtime = re.compile(r'(<script id="medina-category-organisation-runtime">)(.*?)(</script>)', re.S)
    match = runtime.search(source)
    if not match or match.group(2).count('available.slice(0,3)') != 1:
        raise ValueError("La liste des cours en accueil a changé ; contrôle manuel nécessaire.")
    home_runtime = match.group(2).replace('available.slice(0,3)', 'available').replace('↗', '→')
    source = source[:match.start()] + match.group(1) + home_runtime + match.group(3) + source[match.end():]
    home_style = '''<style id="medina-t1-work-home-style">
html[data-medina-fragment="T1"] .medina-work-preview{display:flex;align-items:center;flex-wrap:wrap;gap:6px 18px;padding:8px 14px;background:#fbf9f2;border-color:#e5dbbd;box-shadow:0 2px 8px #372b1410}
html[data-medina-fragment="T1"] .medina-work-preview strong{font-weight:600}
html[data-medina-fragment="T1"] .medina-work-preview strong span{margin-left:8px;font-size:.82em;font-weight:500;color:#6c6042}
html[data-medina-fragment="T1"] .medina-work-preview details{font-size:.82em}
html[data-medina-fragment="T1"] .medina-work-preview summary{cursor:pointer;list-style:revert}
html[data-medina-fragment="T1"] .medina-work-preview details p{max-width:80ch;margin:7px 0}
html[data-medina-fragment="T1"] .medina-work-preview a{margin:0 0 0 auto;font-size:.82em}
html[data-medina-fragment="T1"] .mcg-home{--atlas-font:'Atkinson Hyperlegible Next','Atkinson Hyperlegible',system-ui,sans-serif}
html[data-medina-fragment="T1"] .mcg-cover{padding:20px 0 26px;margin-bottom:25px}
html[data-medina-fragment="T1"] .mcg-cover h1{margin:12px 0!important;font-size:clamp(34px,4vw,58px)!important}
html[data-medina-fragment="T1"] .mcg-counts{margin-top:16px}
html[data-medina-fragment="T1"] #mcg-categories-title{scroll-margin-top:calc(var(--medina-work-header-height,140px) + 14px)}
html[data-medina-fragment="T1"][data-medina-fragment] body .mcg-featured-grid{grid-template-columns:repeat(auto-fit,minmax(190px,1fr))!important}
html[data-medina-fragment="T1"][data-medina-fragment] body .mcg-featured-lesson{border:1px solid #dde5dd!important;box-shadow:0 3px 12px #14301f0c!important}
html[data-medina-fragment="T1"][data-medina-fragment] body .mcg-featured-lesson:hover{background:#f7faf7!important;box-shadow:0 6px 18px #14301f14!important}
html[data-medina-fragment="T1"][data-medina-fragment] body .mcg-draft-access{display:none!important}
html[data-medina-fragment="T1"][data-medina-fragment] body .mcg-category-grid{grid-template-columns:repeat(auto-fit,minmax(250px,1fr))!important}
html[data-medina-fragment="T1"][data-medina-fragment] body .mcg-category-card{min-height:145px!important;padding:16px 18px!important;overflow:hidden;background:#fff!important;color:#21352a!important;border:1px solid #e2e8e1!important;box-shadow:0 2px 5px #14301f0a,0 6px 17px #14301f10!important;transform:none}
html[data-medina-fragment="T1"][data-medina-fragment] body .mcg-category-card::before{content:"";position:absolute;left:0;top:0;bottom:0;width:4px;background:var(--cat);border-radius:14px 0 0 14px}
html[data-medina-fragment="T1"][data-medina-fragment] body .mcg-category-card *{color:#21352a!important}
html[data-medina-fragment="T1"][data-medina-fragment] body .mcg-category-card:hover{transform:translateY(-2px);box-shadow:0 4px 10px #14301f12,0 9px 20px #14301f16!important}
html[data-medina-fragment="T1"][data-medina-fragment] body .mcg-category-card h2{font:600 18px/1.32 var(--atlas-font)!important;color:#21352a!important;letter-spacing:-.012em;margin:12px 0!important}
html[data-medina-fragment="T1"][data-medina-fragment] body .mcg-category-card .mcg-category-foot,html[data-medina-fragment="T1"][data-medina-fragment] body .mcg-category-card .mcg-category-foot *{color:#5e6d63!important}
html[data-medina-fragment="T1"][data-medina-fragment] body .mcg-category-card .mcg-category-number{background:#f1f5f0!important;color:#476149!important;font-weight:600!important}
html[data-medina-fragment="T1"][data-medina-fragment] body .mcg-category-card .mcg-code{background:#f6f8f5!important;color:#435547!important;border-color:#dce6db!important}
html[data-medina-fragment="T1"][data-medina-fragment] body .mcg-category-foot .mcg-available-dot{background:#218253!important}
@media(max-width:650px){html[data-medina-fragment="T1"] .medina-work-preview{gap:4px 12px;padding:7px 10px}html[data-medina-fragment="T1"] .medina-work-preview a{margin-left:0}html[data-medina-fragment="T1"][data-medina-fragment] body .mcg-featured-grid{grid-template-columns:repeat(2,minmax(0,1fr))!important}html[data-medina-fragment="T1"][data-medina-fragment] body .mcg-category-grid{grid-template-columns:1fr!important}html[data-medina-fragment="T1"][data-medina-fragment] body .mcg-category-card{min-height:130px!important}}
@media(prefers-reduced-motion:reduce){html[data-medina-fragment="T1"] .mcg-category-card{transition:none!important}}
</style>'''
    source = source.replace('</head>', home_style + '</head>', 1)
    category_jump = '''<script id="medina-t1-category-jump">
document.getElementById('medina-work-categories-link').addEventListener('click',()=>{
  let tries=0;
  const show=()=>{const heading=document.getElementById('mcg-categories-title');
    if(heading){heading.scrollIntoView({block:'start',behavior:'instant'});return;}
    if(++tries<30)requestAnimationFrame(show);
  };
  requestAnimationFrame(show);
});
</script>'''
    entry_scroll = '''<script id="medina-t1-entry-scroll">
(()=>{
  let lastCode='';
  const routeCode=()=>location.hash.match(/^#\\/entry\\/([A-Z][0-9]{2})(?:$|[/?#])/)?.[1]||'';
  const alignEntry=()=>{
    const code=routeCode();
    if(!code){lastCode='';return;}
    if(code===lastCode)return;
    lastCode=code;
    let tries=0;
    const whenMounted=()=>{
      if(routeCode()!==code)return;
      if(document.querySelector('.mc[data-code="'+code+'"]')){
        requestAnimationFrame(()=>{if(routeCode()===code)window.scrollTo(0,0)});
        return;
      }
      if(++tries<120)requestAnimationFrame(whenMounted);
    };
    requestAnimationFrame(whenMounted);
  };
  addEventListener('hashchange',alignEntry);
  addEventListener('load',alignEntry);
  alignEntry();
})();
</script>'''
    source = source.replace('</body>', category_jump + entry_scroll + '</body>', 1)
    return source


class PackParser(HTMLParser):
    """Track course templates separately from their nested popup templates."""
    def __init__(self):
        super().__init__()
        self.depth = 0
        self.current = None
        self.courses = []
        self.panels = {}
        self.windows = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "template":
            self.depth += 1
            identifier = attrs.get("id", "")
            if identifier.startswith("ch-"):
                if self.current is not None:
                    raise ValueError("Deux cours sont imbriqués dans le pack.")
                self.current = (identifier[3:], self.depth)
                self.courses.append(identifier[3:])
                self.panels[identifier[3:]] = []
            if "data-pop" in attrs:
                self.windows += 1
        if self.current and attrs.get("id") in PANELS and {"panel", "mc-panel"}.intersection(attrs.get("class", "").split()):
            self.panels[self.current[0]].append(attrs["id"])

    def handle_endtag(self, tag):
        if tag == "template":
            if self.current and self.current[1] == self.depth:
                self.current = None
            self.depth -= 1
            if self.depth < 0:
                raise ValueError("Une fermeture de template est sans ouverture.")


def verify_output(source, manifest):
    complete = re.search(r"window\.MEDINA_COMPLETE=(.*?);</script>", source, re.S)
    if not complete or json.loads(complete.group(1)):
        raise ValueError("Un statut de cours achevé subsiste dans l’aperçu.")
    pack = re.search(r'<script id="mdn-pack" type="application/octet-stream">(.*?)</script>', source, re.S)
    if not pack:
        raise ValueError("Le pack de cours compilé est absent.")
    templates = gzip.decompress(base64.b64decode(pack.group(1), validate=True)).decode("utf-8")
    parsed = PackParser()
    parsed.feed(templates)
    if parsed.depth or parsed.current:
        raise ValueError("Un template du pack n’est pas fermé.")
    expected = manifest["chapter_codes"]
    if len(parsed.courses) != len(expected) or set(parsed.courses) != set(expected):
        raise ValueError("L’aperçu contient des cours manquants, étrangers ou doublés : " + repr(parsed.courses))
    for code in expected:
        if len(parsed.panels[code]) != 4 or set(parsed.panels[code]) != PANELS:
            raise ValueError("Le cours doit contenir exactement quatre onglets : " + code)
    return parsed.windows


def check_destination(root, destination):
    root, destination = Path(root).resolve(), Path(destination).resolve()
    if destination.suffix.lower() != ".html":
        raise ValueError("--output doit désigner un fichier .html")
    protected = [root / name for name in ("chapters", "glossary", "shell", "engine", "tools", "livraisons", "tests", "organisation", "docs", ".git", "fragments")]
    if any(destination.is_relative_to(folder.resolve()) for folder in protected):
        raise ValueError("La sortie doit rester hors des sources, livraisons et frontends canoniques.")
    if destination.parent == root and destination.name in {"MEDINA.html", "index.html", "organisation.html"}:
        raise ValueError("La sortie ne peut pas remplacer un frontend canonique.")
    return destination


def build_preview(root, sources, destination):
    root = Path(root).resolve()
    destination = check_destination(root, destination)
    manifest, verified = read_sources(Path(sources), root)
    fragment = next(item for item in json.loads((root / "fragments.json").read_text(encoding="utf-8")) if item["id"] == FRAGMENT)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".medina-fragment-preview-", dir=destination.parent) as temporary:
        workspace = Path(temporary)
        overlay, built = workspace / "overlay", workspace / "built"
        create_overlay(root, verified, manifest, overlay)
        environment = dict(os.environ, MEDINA_ROOT=str(overlay), MEDINA_OUT=str(built),
                           PYTHONDONTWRITEBYTECODE="1", TMPDIR=str(workspace))
        subprocess.run([sys.executable, str(root / "build_front.py"), "--fragment", FRAGMENT],
                       env=environment, cwd=overlay, check=True)
        result = built / "fragments" / f"MEDINA_{FRAGMENT}_{fragment['slug']}.html"
        sys.path.insert(0, str(root))
        source = mark_preview(result.read_text(encoding="utf-8"), manifest)
        windows = verify_output(source, manifest)
        from tools.atomic_output import atomic_output
        with atomic_output(destination) as staging:
            Path(staging).write_text(source, encoding="utf-8")
    return {"output": str(destination), "bytes": len(source.encode("utf-8")), "chapter_codes": manifest["chapter_codes"], "windows": windows}


def main():
    sys.dont_write_bytecode = True
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--sources", type=Path, help="Sources internes ; manifest_interne.json dans leur parent")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        result = build_preview(root, args.sources or root / WORK_FOLDER / "sources", args.output)
    except (OSError, ValueError, KeyError, TypeError, StopIteration, subprocess.CalledProcessError) as error:
        parser.exit(1, "Construction de l’aperçu impossible : " + str(error) + "\n")
    print(json_text(result))
    print("Version de travail : aucune injection canonique ni validation finale.")


if __name__ == "__main__":
    main()
