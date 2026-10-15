"""Abréviations N12 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'n12', '__init__'}:
        continue
    try:
        _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
    except Exception:
        pass
G = {}
def add_if_absent(key, letters, full, definition, window):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full,
                  'def': '<p>' + definition + '</p>', 'ref': window}

add_if_absent('NIA', [('N','Néphrite'),('I','Interstitielle'),('A','Aiguë')], 'Néphrite interstitielle aiguë',
              'Inflammation du tissu situé entre les tubules rénaux, avec œdème, le plus souvent immuno-allergique et médicamenteuse ; sa conséquence principale est l’insuffisance rénale aiguë (Revue médicale suisse, 2022).', 'n12-hypersens')
add_if_absent('IPCI', [('I','Inhibiteurs'),('P','de Points'),('C','de Contrôle'),('I','Immunitaire')], 'Inhibiteurs de points de contrôle immunitaire',
              'Médicaments qui lèvent la tolérance immunitaire contre une tumeur ; ils peuvent provoquer une néphrite interstitielle aiguë après des semaines à des mois.', 'n12-ipci')
add_if_absent('TINU', [('T','Tubulo'),('I','Interstitial'),('N','Nephritis and'),('U','Uveitis')], 'Néphrite tubulo-interstitielle avec uvéite (Tubulointerstitial Nephritis and Uveitis)',
              'Syndrome associant une néphrite tubulo-interstitielle à une atteinte oculaire ; il rechute fréquemment pendant la décroissance des corticoïdes (série britannique de 10 patients).', 'n12-systemique')
add_if_absent('UFC', [('U','Unités'),('F','Formant'),('C','Colonies')], 'Unités formant colonies',
              'Nombre de bactéries viables par millilitre d’urine en culture. Seuils de la pyélonéphrite : 10³ UFC/mL chez la femme adulte (Société suisse d’infectiologie) ; chez l’enfant 10⁴ sur sondage, 10⁵ sur mi-jet.', 'n12-pyelo')
add_if_absent('ADQI', [('A','Acute'),('D','Disease'),('Q','Quality'),('I','Initiative')], 'Acute Disease Quality Initiative',
              'Groupe international de consensus en soins aigus néphrologiques ; sa 34e conférence (2026) a traité l’insuffisance rénale aiguë associée aux inhibiteurs de points de contrôle immunitaire.', 'n12-ipci')
add_if_absent('BK', [('BK','nom propre du virus (polyomavirus BK), non développé lettre à lettre')], 'Polyomavirus BK',
              'Virus responsable de néphrite chez le transplanté rénal ; la revue suisse le cite parmi les causes virales de néphrite interstitielle.', 'n12-infect')
add_if_absent('CXCL9', [('CXCL9','chimiokine à motif C-X-C, ligand 9 ; nom de protéine, non développé lettre à lettre')], 'Chimiokine C-X-C ligand 9',
              'Chimiokine urinaire proposée comme biomarqueur de la néphrite tubulo-interstitielle aiguë ; non validée en pratique.', 'n12-biomarqueurs')
add_if_absent('El-Feghi', [('El-Feghi','nom propre d’auteur, non une abréviation')], 'El-Feghi (auteur)',
              'Premier auteur d’une revue 2026 sur la maladie rénale liée aux IgG4, citée pour le diagnostic différentiel.', 'n12-systemique')
for _c, _t in (('N11.0','avec reflux'),('N11.1','obstructive'),('N11.8','autres formes précisées'),('N11.9','sans précision')):
    add_if_absent(_c, [(_c, 'code CIM-10-GM de la néphrite tubulo-interstitielle chronique ' + _t)], 'CIM-10-GM ' + _c + ' : néphrite tubulo-interstitielle chronique ' + _t,
                  'Sous-code du groupe N11 de la classification CIM-10-GM 2024.', 'n12-codes')
