#!/usr/bin/env python3
"""Lire l'information professionnelle suisse (approuvée par Swissmedic) d'un médicament.

Source : AmiKo (amiko.oddb.org), qui republie les textes AIPS de Swissmedic.
Exemples :
  python3 tools/swissmedic_fi.py chercher tamiflu
  python3 tools/swissmedic_fi.py texte 7680551960010 > /tmp/tamiflu.txt
Citer la référence sous la forme : « Information professionnelle suisse <Nom>®,
Swissmedic (AIPS via AmiKo), consultée le JJ.MM.AAAA ».
"""

from __future__ import annotations

import html
import json
import re
import sys
import urllib.parse
import urllib.request

BASE = "https://amiko.oddb.org"


def get(url: str) -> str:
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "MEDINA"}), timeout=60) as r:
        return r.read().decode("utf-8", "replace")


def chercher(nom: str, lang: str = "fr") -> list[dict]:
    data = json.loads(get(f"{BASE}/name?lang={lang}&name={urllib.parse.quote(nom)}"))
    return [{"titre": d["title"], "titulaire": d["author"], "atc": d["atccode"],
             "indication": re.sub(r"<[^>]+>", "", d.get("therapy", "")),
             "gtin": [p["gtin"] for p in d.get("packinfos", [])][:3]} for d in data]


def texte(gtin: str, lang: str = "fr") -> str:
    page = get(f"{BASE}/{lang}/fi?gtin={urllib.parse.quote(gtin)}")
    page = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", page, flags=re.S)
    page = re.sub(r"</(p|div|h\d|li|tr)>", "\n", page)
    page = html.unescape(re.sub(r"<[^>]+>", " ", page))
    return re.sub(r"[ \t]+", " ", re.sub(r"\n\s*\n+", "\n\n", page)).strip()


def main() -> int:
    if len(sys.argv) < 3 or sys.argv[1] not in {"chercher", "texte"}:
        print(__doc__)
        return 2
    if sys.argv[1] == "chercher":
        print(json.dumps(chercher(" ".join(sys.argv[2:])), ensure_ascii=False, indent=1))
    else:
        print(texte(sys.argv[2]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
