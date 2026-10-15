"""Abréviations G08 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib, sys
_here = Path(__file__).resolve().parent
if (_here / 'cardio_1.py').exists():
    _gdir = _here
else:
    _gdir = next((p / 'glossary' for p in _here.parents if (p / 'glossary' / 'cardio_1.py').exists()), None)
_existing = {}
if _gdir is not None:
    if str(_gdir) not in sys.path:
        sys.path.insert(0, str(_gdir))
    for _path in sorted(_gdir.glob('*.py')):
        if _path.stem in {'g08', '__init__'}:
            continue
        try:
            _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
        except Exception:
            pass
G = {}
def add_if_absent(key, letters, full, definition, window=None):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full,
                  'def': '<p>' + definition + '</p>', 'ref': window}

add_if_absent('TVC', [('T','Thrombose'),('V','Veineuse'),('C','Cérébrale')], 'Thrombose veineuse cérébrale',
              'Obstruction thrombotique d’une ou plusieurs veines cérébrales ou d’un sinus dural. La forme septique, déclenchée par une infection de voisinage, est l’objet de ce cours.', 'g08-tvc')
add_if_absent('ISCVT', [('ISCVT', 'sigle d’une cohorte internationale sur la thrombose des veines cérébrales et des sinus duraux, développement non repris des sources lues')],
              'Cohorte internationale ISCVT (thrombose des veines cérébrales et des sinus duraux)',
              'Cette cohorte de 624 patients décrit le pronostic de la thrombose veineuse cérébrale : mortalité de 8,3 % et facteurs prédictifs de décès ou de dépendance, dont l’infection du système nerveux central (Stroke 2004).', 'g08-coma')
add_if_absent('mRS', [('m','modified'),('R','Rankin'),('S','Scale')], 'Échelle de Rankin modifiée (modified Rankin Scale)',
              'Échelle de handicap de 0 (aucun symptôme) à 6 (décès). Elle sous-estime les séquelles cognitives de la thrombose veineuse cérébrale.', 'g08-pronostic')
add_if_absent('DECOMPRESS2', [('DECOMPRESS2', 'nom d’un essai, non développé lettre à lettre dans les sources lues')],
              'Essai DECOMPRESS2',
              'Cette étude de 118 patients évalue la décompression chirurgicale dans la thrombose veineuse cérébrale : à un an, deux tiers sont en vie et un tiers sont indépendants.', 'g08-decompression')
add_if_absent('DOAC-CVT', [('DOAC', 'Direct Oral AntiCoagulants (anticoagulants oraux directs)'), ('CVT', 'Cerebral Venous Thrombosis (thrombose veineuse cérébrale)')],
              'Cohorte DOAC-CVT',
              'Cette cohorte observationnelle de 619 patients compare anticoagulants oraux directs et antagonistes de la vitamine K : le critère composite est de 3 % dans chaque groupe.', 'g08-aod')
add_if_absent('TO-ACT', [('TO-ACT', 'nom d’un essai, non développé lettre à lettre dans les sources lues')],
              'Essai TO-ACT',
              'Cet essai de thrombectomie endovasculaire a été arrêté prématurément sans bénéfice dans la thrombose veineuse cérébrale.', 'g08-endovasc')
add_if_absent('DIAS3', [('DIAS3', 'sigle d’un score, non développé lettre à lettre dans les sources lues')],
              'Score DIAS3',
              'Score destiné à prédire l’épilepsie après une thrombose veineuse cérébrale.', 'g08-crises')
add_if_absent('VITT', [('VITT', 'sigle anglais désignant la thrombose avec thrombopénie après vaccin à vecteur adénoviral, développement non repris des sources lues')],
              'Thrombose avec thrombopénie après vaccination',
              'Complication rare de certains vaccins à vecteur adénoviral : thrombose veineuse cérébrale avec thrombopénie, dosage des anticorps anti-PF4.', 'g08-vitt')
add_if_absent('DGN', [('D','Deutsche'),('G','Gesellschaft für'),('N','Neurologie')], 'Société allemande de neurologie',
              'Elle a publié, avec des représentants autrichiens et suisses, la ligne directrice de consensus S2k sur la thrombose veineuse cérébrale (mise à jour du 24 octobre 2023).', 'g08-heparine')
add_if_absent('EAN', [('E','European'),('A','Academy of'),('N','Neurology')], 'Académie européenne de neurologie',
              'Elle a endossé avec l’Organisation européenne de l’accident vasculaire cérébral la recommandation de 2017 sur la thrombose veineuse cérébrale.', 'g08-heparine')
add_if_absent('Tolosa-Hunt', [('Tolosa-Hunt', 'noms propres des auteurs qui ont décrit le syndrome, non une abréviation')], 'Syndrome de Tolosa-Hunt',
              'Diagnostic classique du syndrome du sinus caverneux cité ici sans conduite, car sa différenciation n’a pas été lue dans une source européenne.')
add_if_absent('Pays-Bas', [('Pays-Bas', 'nom propre d’un pays, non une abréviation')], 'Pays-Bas', 'Pays où a été mesurée l’incidence de la thrombose veineuse cérébrale citée dans le cours.')
add_if_absent('Papouasie-Nouvelle-Guinée', [('Papouasie-Nouvelle-Guinée', 'nom propre d’un pays, non une abréviation')], 'Papouasie-Nouvelle-Guinée', 'Pays d’une série de complications intracrâniennes otogènes, cité pour sa mortalité dans un contexte de présentation tardive.')
