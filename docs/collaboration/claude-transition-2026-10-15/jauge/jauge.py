#!/usr/bin/env python3
"""Jauge MEDINA Claude : lit l'état écrit par 7_Starter_Claude (aucun appel réseau)."""
import json, sys, time
from pathlib import Path
S = Path('/tmp/claude-0/-home-user-Medina/32d77524-f01f-5b7e-92b4-188dd9e32b87/scratchpad/7_Starter_Claude/etat.json')
LIB = {'APPEL_GOUVERNANCE': 'en attente d’approbation du lot suivant', 'LANCER_LOT': 'lot approuvé, lancement',
       'ATTENDRE': 'lot en cours', 'INTEGRATION_EN_COURS': 'intégration et publication en cours', 'FIN_77': 'terminé (77)', 'CATALOGUE_EPUISE': 'catalogue épuisé'}
def line(short=False):
    try:
        d = json.loads(S.read_text())
    except Exception:
        return 'JAUGE indisponible (7_Starter arrêté ?)'
    j = d['jauge'] if not short else d['jauge'].split(' · tour')[0]
    return f"{j} · lot {d['tour']} : {LIB.get(d['decision'], d['decision'])} · maj {d['maj']}"
if __name__ == '__main__':
    print(line('--court' in sys.argv))
