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
    total = 0
    for fragment in fragments:
        filename = f"MEDINA_{fragment['id']}_{fragment['slug']}.html"
        path = args.fragments_dir / filename
        if not path.is_file():
            raise SystemExit(f"fragment manquant : {path}")
        count = chapter_count(path)
        total += count
        label = "cours disponible" if count == 1 else "cours disponibles"
        accent = ("coral", "azure", "lime", "violet", "amber", "teal")[len(cards) % 6]
        cards.append((fragment["id"], f'''<li class="fragment {accent}" data-search="{html.escape((fragment['id'] + ' ' + fragment['nom']).casefold(), quote=True)}">
          <a href="fragments/{html.escape(filename, quote=True)}" aria-label="{html.escape(fragment['nom'], quote=True)}, {count} {label}">
            <span class="symbol" aria-hidden="true">{html.escape(fragment['id'][0])}<small>{html.escape(fragment['id'][1:])}</small></span>
            <span class="copy"><strong>{html.escape(fragment['nom'])}</strong><small>{html.escape(fragment['id'])} · {count} {label}</small></span><span class="arrow" aria-hidden="true">↗</span>
          </a></li>'''))

    systems = "\n".join(card for ident, card in cards if ident.startswith("S"))
    transversal = "\n".join(card for ident, card in cards if ident.startswith("T"))
    page = (ROOT / "site/index_template.html").read_text(encoding="utf-8")
    page = (page.replace("<!-- SYSTEMS -->", systems)
                .replace("<!-- CROSS -->", transversal)
                .replace("__FRAGMENTS__", str(len(fragments)))
                .replace("__COURSES__", str(total)))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(page, encoding="utf-8")
    print(f"index {args.output} ({len(fragments)} fragments)")


if __name__ == "__main__":
    main()
