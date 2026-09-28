#!/usr/bin/env python3
"""Génère la page d'accueil statique des fragments MEDINA."""
import argparse
import base64
import gzip
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def chapter_count(path):
    source = path.read_text(encoding="utf-8")
    packed = re.search(r'<script id="mdn-pack"[^>]*>([^<]+)</script>', source)
    if packed:
        source += gzip.decompress(base64.b64decode(packed.group(1))).decode("utf-8")
    return len(set(re.findall(r'id=["\']ch-([^"\']+)["\']', source)))


def human_size(size):
    if size < 1000:
        return f"{size} o"
    if size < 1_000_000:
        return f"{size / 1000:.1f} ko".replace(".0 ", " ")
    return f"{size / 1_000_000:.1f} Mo".replace(".0 ", " ")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fragments-dir", type=Path, default=ROOT / "dist/fragments")
    parser.add_argument("--output", type=Path, default=ROOT / "_site/index.html")
    args = parser.parse_args()
    fragments = json.loads((ROOT / "fragments.json").read_text(encoding="utf-8"))

    cards = []
    for fragment in fragments:
        filename = f"MEDINA_{fragment['id']}_{fragment['slug']}.html"
        path = args.fragments_dir / filename
        if not path.is_file():
            raise SystemExit(f"fragment manquant : {path}")
        count = chapter_count(path)
        label = "chapitre rédigé" if count == 1 else "chapitres rédigés"
        cards.append((fragment["id"], f'''<li><a href="fragments/{filename}">
          <strong>{html.escape(fragment['nom'])}</strong>
          <span>{count} {label} · {human_size(path.stat().st_size)}</span>
        </a></li>'''))

    systems = "\n".join(card for ident, card in cards if ident.startswith("S"))
    transversal = "\n".join(card for ident, card in cards if ident.startswith("T"))
    page = f'''<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>MEDINA — Atlas par systèmes</title>
<style>
:root{{color-scheme:light dark;--bg:#f5f6f8;--card:#fff;--text:#18202a;--muted:#637083;--line:#a8afb9;--link:#1257a6}}
@media(prefers-color-scheme:dark){{:root{{--bg:#11151b;--card:#1c222c;--text:#edf1f7;--muted:#aeb8c7;--line:#697382;--link:#8fc5ff}}}}
*{{box-sizing:border-box}} body{{margin:0;background:var(--bg);color:var(--text);font:16px/1.5 system-ui,sans-serif}}
main{{width:min(54rem,100%);margin:auto;padding:2rem 1rem 4rem}} h1{{font-size:clamp(1.7rem,5vw,2.5rem);line-height:1.15}}
.complete{{display:inline-block;margin:.25rem 0 1.5rem;color:var(--link);font-weight:650}} ul{{list-style:none;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(15rem,1fr));gap:.7rem}}
li a{{display:flex;flex-direction:column;height:100%;padding:1rem;border-radius:.6rem;background:var(--card);color:inherit;text-decoration:none;box-shadow:0 1px 4px #0002}}
li a:hover,li a:focus-visible{{outline:2px solid var(--link)}} li span{{margin-top:.35rem;color:var(--muted);font-size:.9rem}}
h2{{display:flex;align-items:center;gap:.8rem;margin-top:2rem;color:var(--muted);font-size:1rem;font-weight:600}}
h2::before,h2::after{{content:"";height:1px;background:var(--line);flex:1}}
</style></head><body><main>
<h1>MEDINA — Atlas par systèmes</h1>
<a class="complete" href="MEDINA.html">Consulter le MEDINA complet</a>
<ul>{systems}</ul>
<h2>Axes transversaux</h2>
<ul>{transversal}</ul>
</main></body></html>
'''
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(page, encoding="utf-8")
    print(f"index {args.output} ({len(fragments)} fragments)")


if __name__ == "__main__":
    main()
