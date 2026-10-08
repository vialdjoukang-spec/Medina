#!/usr/bin/env python3
"""Garde-fou des sources MEDINA : impose la politique `organisation/sources_policy.json`.

  check [--base REF] [--strict]  contrôle les *_justifications.json ; échec si une NOUVELLE source hors politique
                                 apparaît (les écarts historiques sont tolérés via organisation/sources_baseline.json)
  baseline                       fige les écarts actuels comme tolérés (à n'utiliser que pour l'héritage)
  scaffold [--quiet]             dépose le pointeur SOURCES_POLITIQUE.md dans chaque chapitre / remise (idempotent)
  reminder                       rappelle la règle (utilisé par les crochets Claude Code)
  install                        active les crochets git (core.hooksPath=tools/githooks)
"""
import argparse, glob, json, re, subprocess, sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
POLICY = ROOT / 'organisation' / 'sources_policy.json'
BASELINE = ROOT / 'organisation' / 'sources_baseline.json'
STUB = ("# Sources — politique obligatoire\n\n"
        "Toute affirmation de ce dossier s'appuie sur des sources suisses (A), puis européennes applicables en Suisse (B).\n"
        "Source indexée (J) : déclarer `origine` (CH/EU). Autre source (X) : `derogation` motivée.\n"
        "Médicaments : vérifier dans `ref/fi/`. Règle complète : `docs/collaboration/POLITIQUE_SOURCES.md` ; "
        "liste : `organisation/sources_policy.json` ; contrôle : `python3 tools/sources_guard.py check`.\n")


def load_policy():
    p = json.loads(POLICY.read_text(encoding='utf-8'))
    a = [d for v in p['A_suisse'].values() for d in v]
    return {'A': a, 'B': p['B_europe'], 'J': p['J_index']}


def tier(url, pol):
    host = (urlparse(url).hostname or '').lower()
    for t in ('A', 'B', 'J'):
        if any(host == d or host.endswith('.' + d) for d in pol[t]):
            return t
    return 'X'


def violations(files, pol):
    out = {}
    for f in files:
        try:
            entries = json.loads(Path(f).read_text(encoding='utf-8')).get('entries', [])
        except Exception as e:
            out[(str(f), 'JSON')] = f'illisible : {e}'; continue
        for en in entries:
            if not en.get('sources'):
                out[(str(f), en.get('id', '?'))] = 'entrée sans aucune source'
            for s in en.get('sources', []):
                url = s.get('url', '') if isinstance(s, dict) else ''
                if not url:
                    out[(str(f), en.get('id', '?'))] = 'source sans URL'; continue
                t, der = tier(url, pol), bool(isinstance(s, dict) and s.get('derogation'))
                org = s.get('origine') if isinstance(s, dict) else None
                if t == 'X' and not der:
                    out[(str(f), url)] = 'source hors politique (X) sans dérogation'
                elif t == 'J' and org not in ('CH', 'EU') and not der:
                    out[(str(f), url)] = 'source indexée (J) sans origine CH/EU déclarée'
                elif org == 'INT' and not der:
                    out[(str(f), url)] = 'origine INT sans dérogation'
    return out


def rel(p):
    return str(Path(p).resolve().relative_to(ROOT))


def justification_files():
    pats = ['chapters/*/*_justifications.json', 'livraisons/**/*_justifications.json']
    return sorted({rel(f) for p in pats for f in glob.glob(str(ROOT / p), recursive=True)})


def targets():
    d = [p for p in (ROOT / 'chapters').iterdir() if p.is_dir()]
    for p in (ROOT / 'livraisons').glob('*/*'):
        if p.is_dir(): d.append(p)
    return d


def scaffold(quiet=False, dry=False):
    made = []
    for d in targets():
        s = d / 'SOURCES_POLITIQUE.md'
        if not s.exists():
            made.append(rel(s))
            if not dry: s.write_text(STUB, encoding='utf-8')
    if made and not quiet: print(f'{len(made)} pointeur(s) {"manquant(s)" if dry else "créé(s)"}')
    return made


def changed(base):
    r = subprocess.run(['git', 'diff', '--name-only', f'{base}...HEAD'], cwd=ROOT, capture_output=True, text=True)
    return set(r.stdout.split())


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('cmd', choices=['check', 'baseline', 'scaffold', 'reminder', 'install'])
    ap.add_argument('--base'); ap.add_argument('--strict', action='store_true'); ap.add_argument('--quiet', action='store_true')
    a = ap.parse_args()
    if a.cmd == 'scaffold': scaffold(a.quiet); return 0
    if a.cmd == 'reminder':
        print("RÈGLE MEDINA — sources : suisses d'abord (sociétés savantes, universités, Swissmedic/OFSP), puis européennes "
              "applicables en Suisse. Toute source hors liste exige `derogation`. Médicaments : ref/fi/. "
              "Contrôle : python3 tools/sources_guard.py check. Voir docs/collaboration/POLITIQUE_SOURCES.md"); return 0
    if a.cmd == 'install':
        subprocess.run(['git', 'config', 'core.hooksPath', 'tools/githooks'], cwd=ROOT, check=True); print('crochets git activés'); return 0
    pol = load_policy(); files = justification_files()
    v = violations(files, pol)
    if a.cmd == 'baseline':
        BASELINE.write_text(json.dumps(sorted([list(k) for k in v]), ensure_ascii=False, indent=0) + '\n', encoding='utf-8')
        print(f'{len(v)} écart(s) historique(s) figé(s)'); return 0
    base = {tuple(x) for x in json.loads(BASELINE.read_text(encoding='utf-8'))} if BASELINE.exists() else set()
    new = {k: m for k, m in v.items() if a.strict or k not in base}
    ch = changed(a.base) if a.base else None
    if ch is not None:
        new = {k: m for k, m in new.items() if k[0] in ch}
    miss = [m for m in scaffold(dry=True) if ch is None or str(Path(m).parent) in {str(Path(c).parent) for c in ch}]
    for (f, k), m in sorted(new.items()): print(f'ÉCART {f} — {k} : {m}')
    for m in miss: print(f'POINTEUR MANQUANT {m} (python3 tools/sources_guard.py scaffold)')
    print(f'{len(files)} fichier(s) ; {len(v)} écart(s) au total dont {len(v) - len(new) if not a.strict else 0} historique(s) toléré(s) ; {len(new)} nouveau(x)')
    return 1 if new or miss else 0


if __name__ == '__main__':
    sys.exit(main())
