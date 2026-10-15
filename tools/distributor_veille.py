#!/usr/bin/env python3
"""Veille du distributeur d'agents (skill .claude/skills/agent-distributor) : détecte les leçons en retard.

Registre $DISTRIB_ROSTER (JSON) : {"lecons": [{"code": "G40", "dir": "livraisons/…/CYCLE_05_G40",
  "etape": "recherche"|"redaction", "debut": "2026-10-15T12:48:00+00:00", "renforts": 0}]}
Sortie attendue : recherche → preuves/dossier_sources.json ; rédaction → preuves/source_ledger_claude.json.
Seuils (min) : recherche 45/75, rédaction 35/55. Une leçon terminée ou dans les temps ne demande rien.

  python3 tools/distributor_veille.py              # un passage ; code 3 et actions si renfort requis
  python3 tools/distributor_veille.py --boucle 300 # répète jusqu'à une action
"""
import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEUILS = {'recherche': (45, 75, 'preuves/dossier_sources.json'),
          'redaction': (35, 55, 'preuves/source_ledger_claude.json')}


def actions(roster, now):
    out = []
    for lecon in roster['lecons']:
        s1, s2, sortie = SEUILS[lecon['etape']]
        debut = datetime.fromisoformat(lecon['debut'])
        if (ROOT / lecon['dir'] / sortie).exists() and (ROOT / lecon['dir'] / sortie).stat().st_mtime > debut.timestamp():
            continue
        minutes = (now - debut).total_seconds() / 60
        voulu = 2 if minutes >= s2 else 1 if minutes >= s1 else 0
        if voulu > lecon.get('renforts', 0):
            out.append(f"RENFORT {voulu} {lecon['code']} {lecon['etape']} ({minutes:.0f} min sans {sortie})")
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--boucle', type=int, default=0)
    a = p.parse_args()
    path = Path(os.environ.get('DISTRIB_ROSTER', Path.home() / '.distrib_roster.json'))
    while True:
        found = actions(json.loads(path.read_text()), datetime.now(timezone.utc))
        if found:
            print('\n'.join(found))
            return 3
        if not a.boucle:
            print('Distributeur : toutes les leçons sont dans les temps')
            return 0
        time.sleep(a.boucle)


if __name__ == '__main__':
    sys.exit(main())
