#!/usr/bin/env python3
"""Mesurer l'origine des sources citées dans chaque cours MEDINA.

Compte, dans le texte visible des fichiers d'un cours, les mentions de sources
suisses, européennes ou internationales reconnues en Europe, et américaines.
Taux d'américanisation = américaines / (suisses + européennes + américaines).
Les textes conjoints co-signés par une société européenne (ATS/ERS…) ne sont pas
comptés comme américains. Indicateur de tri, pas une preuve de conformité.

  python3 tools/americanisation.py [--json sortie.json] [--md sortie.md] [DOSSIER…]
"""

from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

US = r"\b(CDC|IDSA|ACCP|CHEST|AHA|ACC/AHA|AHA/ACC|ACC|ATLS|FDA|SCCM|ACOG|ACP|USPSTF|AASLD|NCCN|ACR|AAP|NIH|NHLBI|ASCO|AUA|ACG|AGA|AAAAI|ACAAI|DailyMed|GeneReviews|Endocrine Society|ASE|ASRA|ACMG|AASM|AAFP|StatPearls|Medscape|UpToDate|Jeffrey Modell|DHHS|IAS-USA|NEJM Journal Watch|SVS|SHEA|HRS|ASH|ASHP|JNC ?\d?|American (College|Heart|Thoracic|Diabetes|Academy|Society|Association)\w*|Centers for Disease|U\.?S\.? Preventive)\b"
JOINT_US = r"\b(ATS|IDSA|ACCP|AHA|ACC|HRS|ASH)\s*/\s*(ERS|ESC|ESCMID|EULAR|EASD|ESH|EHRA|EACTS|JRS|ALAT)|\b(ERS|ESC|ESCMID|EULAR|EASD|ESH|EHRA|EACTS)\s*/\s*(ATS|IDSA|ACCP|AHA|ACC|HRS|ASH)"
ATS_ALONE = r"\bATS\b"
CH = r"\b(OFSP|BAG|Swissmedic|compendium(\.ch)?|swissmedicinfo|AIPS|Information professionnelle suisse|SSI|SGInf|Soci[ée]t[ée] suisse[\w ’'-]*|Ligue (pulmonaire|suisse)[\w ’'-]*|Plan de vaccination suisse|mediX|SGAIM|SSMIG|Swiss Society|Swiss \w+ Society|EKIF|CFV|Suva|Unisant[ée]|Swissnoso|Anresis|Guidelines Schweiz|SGP|SSP|SSC|SGK|PROFILES)\b"
EU = r"\b(ESC|ERS|ESICM|ESCMID|ECDC|EMA|EASL|EAU|ESMO|EULAR|KDIGO|NICE|BTS|ESH|EAN|ESGE|ERC|GINA|GOLD|OMS|WHO|ESPGHAN|EACTS|ESTS|EASD|EHRA|EAACI|ESPID|ESCRS|EAS|ESO|ECCO|UEG|EAPC|ESHRE|EBMT|EHA|ELN|AWMF|DGP|HAS|SPILF|SPLF|JRS|ALAT|ISHLT|ESVS)\b"


def text_of(files):
    raw = "\n".join(f.read_text(encoding="utf-8", errors="replace") for f in files)
    raw = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", raw, flags=re.S)
    return html.unescape(re.sub(r"<[^>]+>", " ", raw))


def measure(text):
    joint = len(re.findall(JOINT_US, text))
    cleaned = re.sub(JOINT_US, " ", text)
    us = len(re.findall(US, cleaned)) + len(re.findall(ATS_ALONE, cleaned))
    ch = len(re.findall(CH, text, flags=re.I))
    eu = len(re.findall(EU, cleaned)) + joint
    total = us + ch + eu
    return {"suisse": ch, "europeen": eu, "americain": us,
            "taux_americanisation": round(100 * us / total, 1) if total else 0.0,
            "taux_suisse": round(100 * ch / total, 1) if total else 0.0}


def courses(dirs):
    found = {}
    for base in dirs:
        for d in sorted(Path(base).glob("*/")):
            files = sorted(d.glob("*.html"))
            if files:
                key = d.name if d.name not in found else d.name + " (travail Codex)"
                found[key] = (d, files)
    return found


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("dirs", nargs="*", default=[str(ROOT / "chapters")])
    ap.add_argument("--json")
    ap.add_argument("--md")
    a = ap.parse_args()
    titles = {c["code"]: c["title"] for c in json.loads((ROOT / "chapters.json").read_text())}
    rows = []
    for code, (d, files) in courses(a.dirs).items():
        m = measure(text_of(files))
        rows.append({"code": code, "titre": titles.get(code.split()[0], ""), "dossier": str(d), **m})
    rows.sort(key=lambda r: -r["taux_americanisation"])
    tot = {k: sum(r[k] for r in rows) for k in ("suisse", "europeen", "americain")}
    s = sum(tot.values()) or 1
    summary = {"cours": len(rows), **tot, "taux_americanisation": round(100 * tot["americain"] / s, 1),
               "taux_suisse": round(100 * tot["suisse"] / s, 1)}
    if a.json:
        Path(a.json).write_text(json.dumps({"synthese": summary, "cours": rows}, ensure_ascii=False, indent=1) + "\n")
    lines = ["| Code | Cours | Suisse | Europe/intern. | Américain | Taux américain | Taux suisse |", "|---|---|---|---|---|---|---|"]
    lines += [f"| {r['code']} | {r['titre']} | {r['suisse']} | {r['europeen']} | {r['americain']} | {r['taux_americanisation']} % | {r['taux_suisse']} % |" for r in rows]
    lines.append(f"| **Total** | {summary['cours']} cours | {tot['suisse']} | {tot['europeen']} | {tot['americain']} | **{summary['taux_americanisation']} %** | **{summary['taux_suisse']} %** |")
    out = "\n".join(lines)
    if a.md:
        Path(a.md).write_text(out + "\n")
    print(out)


if __name__ == "__main__":
    main()
