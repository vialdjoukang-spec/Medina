#!/usr/bin/env python3
"""Images médicales réelles sous licence ouverte : recherche, contrôle de licence, import tracé.

Aucun outil tiers : API publiques Wikimedia Commons et Openverse (voir
docs/collaboration/OUTILS_GITHUB_IMAGES_2026-10-14.md). Licences admises : CC0, PD, CC BY, CC BY-SA.
NC et ND sont refusées. L'outil ne juge pas le contenu : ouvrir l'image et vérifier la légende reste obligatoire.

  python3 tools/images_ouvertes.py chercher "iron deficiency anemia blood smear" [--source openverse] [-n 8]
  python3 tools/images_ouvertes.py importer "File:Hypochromic anemia.jpg" assets/img/cycle1/d50 \
      --legende "…" --alt "…" --emplacement "chapters/D50/D50_b.html#d50-…"
"""
import argparse, hashlib, html, io, json, re, sys, time, urllib.parse, urllib.request
from datetime import datetime, timezone
from pathlib import Path

UA = "MEDINA-cours-medicaux/1.0 (https://github.com/vialdjoukang-spec/Medina; vial.djoukang@gmail.com)"
COMMONS = "https://commons.wikimedia.org/w/api.php"
OPENVERSE = "https://api.openverse.org/v1/images/"
ALLOWED = re.compile(r"^(cc0|public domain|pd|cc[- ]by(-sa)?)([- ]\d(\.\d)?)?", re.I)
REFUSED = re.compile(r"\b(nc|nd)\b|non[- ]?commercial|no[- ]?deriv", re.I)


def get(url, params=None, raw=False):
    if params:
        url += "?" + urllib.parse.urlencode(params)
    for attempt in range(6):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=60) as r:
                data = r.read()
            return data if raw else json.loads(data)
        except urllib.error.HTTPError as e:
            if e.code != 429 or attempt == 5:
                raise
            # Commons limite les IP partagées : respecter Retry-After, sinon attente croissante.
            wait = e.headers.get("Retry-After", "")
            time.sleep(min(int(wait), 60) if wait.isdigit() else 3 * 2 ** attempt)


def text(v):
    return html.unescape(re.sub(r"<[^>]+>", "", v or "")).strip()


def licence_ok(name):
    name = (name or "").strip()
    return bool(ALLOWED.match(name)) and not REFUSED.search(name)


def commons_info(titles):
    d = get(COMMONS, {"action": "query", "format": "json", "prop": "imageinfo", "titles": "|".join(titles),
                      "iiprop": "url|extmetadata|size|mime", "iiurlwidth": 1200})
    out = []
    for p in d.get("query", {}).get("pages", {}).values():
        if "imageinfo" not in p or not p["imageinfo"][0].get("mime", "").startswith("image/"):
            continue
        i = p["imageinfo"][0]; m = i.get("extmetadata", {})
        lic = text(m.get("LicenseShortName", {}).get("value"))
        out.append({"title": p["title"], "page": i.get("descriptionurl"), "file": i.get("url"),
                    "thumb": i.get("thumburl"), "mime": i.get("mime"), "size": [i.get("width"), i.get("height")],
                    "author": text(m.get("Artist", {}).get("value")), "credit": text(m.get("Credit", {}).get("value")),
                    "licence": lic, "licence_url": m.get("LicenseUrl", {}).get("value"),
                    "description": text(m.get("ImageDescription", {}).get("value"))[:300],
                    "admissible": licence_ok(lic)})
    return out


def chercher(q, source, n):
    if source == "openverse":
        d = get(OPENVERSE, {"q": q, "page_size": n, "license": "cc0,pdm,by,by-sa"})
        return [{"title": r.get("title"), "page": r.get("foreign_landing_url"), "file": r.get("url"),
                 "author": r.get("creator"), "licence": f"{r.get('license')} {r.get('license_version') or ''}".strip(),
                 "licence_url": r.get("license_url"), "provider": r.get("provider"),
                 "admissible": r.get("license") in ("cc0", "pdm", "by", "by-sa")} for r in d.get("results", [])]
    d = get(COMMONS, {"action": "query", "format": "json", "list": "search", "srsearch": q,
                      "srnamespace": 6, "srlimit": n})
    titles = [r["title"] for r in d.get("query", {}).get("search", [])]
    return commons_info(titles) if titles else []


def importer(title, dest, legende, alt, emplacement):
    info = commons_info([title])
    if not info:
        sys.exit("Fichier Commons introuvable : " + title)
    i = info[0]
    if not i["admissible"]:
        sys.exit(f"Licence refusée : {i['licence']!r} ({title})")
    data = get(i["thumb"] or i["file"], raw=True)
    from PIL import Image
    im = Image.open(io.BytesIO(data))
    im.thumbnail((1200, 1200))
    dest = Path(dest); dest.mkdir(parents=True, exist_ok=True)
    stem = re.sub(r"[^a-z0-9]+", "_", Path(title.split(":", 1)[-1]).stem.lower()).strip("_")[:60]
    if im.mode in ("RGBA", "LA", "P") and "transparency" in im.info or im.mode in ("RGBA", "LA"):
        path = dest / (stem + ".png"); im.save(path, optimize=True)
    else:
        path = dest / (stem + ".jpg"); im.convert("RGB").save(path, quality=84, optimize=True, progressive=True)
    sha = hashlib.sha256(path.read_bytes()).hexdigest()
    man_path = dest / "ATTRIBUTIONS.json"
    # Format lu par tools/night_cycle.py : {"code": …, "images": [...]} ; une liste nue reste acceptée.
    doc = json.loads(man_path.read_text()) if man_path.exists() else {"code": dest.name.upper(), "images": []}
    man = doc["images"] if isinstance(doc, dict) else doc
    man[:] = [m for m in man if m.get("fichier") != path.name]
    man.append({"fichier": path.name, "page_source": i["page"], "url_fichier": i["file"], "auteur": i["author"],
                "credit": i["credit"], "licence": i["licence"], "licence_url": i["licence_url"],
                "attribution": f"{i['author']}, {i['licence']}, via Wikimedia Commons",
                "consulte_le": datetime.now(timezone.utc).date().isoformat(), "sha256": sha,
                "octets": path.stat().st_size, "legende": legende, "alt": alt, "emplacement": emplacement,
                "verification_visuelle": "à faire par l'auteur : ouvrir l'image et confirmer la légende"})
    man_path.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n")
    src = path.as_posix()
    src = src[src.index("assets/img/"):] if "assets/img/" in src else src
    print(f'<figure><img src="{src}" alt="{html.escape(alt)}" loading="lazy"><figcaption>{legende} '
          f'Source : {html.escape(i["author"])}, {i["licence"]}, Wikimedia Commons.</figcaption></figure>')


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    s = p.add_subparsers(dest="cmd", required=True)
    c = s.add_parser("chercher"); c.add_argument("q"); c.add_argument("--source", choices=["commons", "openverse"], default="commons"); c.add_argument("-n", type=int, default=8)
    i = s.add_parser("importer"); i.add_argument("title"); i.add_argument("dest")
    i.add_argument("--legende", required=True); i.add_argument("--alt", required=True); i.add_argument("--emplacement", required=True)
    a = p.parse_args()
    if a.cmd == "chercher":
        try:
            res = chercher(a.q, a.source, a.n)
        except urllib.error.HTTPError as e:
            if e.code != 429 or a.source != "commons":
                raise
            print("Commons saturé (429) : repli sur Openverse.", file=sys.stderr)
            res = chercher(a.q, "openverse", a.n)
        print(json.dumps(res, ensure_ascii=False, indent=1))
    else:
        importer(a.title, a.dest, a.legende, a.alt, a.emplacement)


if __name__ == "__main__":
    main()
