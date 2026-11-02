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
              'Cohorte historique de thrombose veineuse cérébrale citée dans le dossier antérieur. Ses résultats chiffrés non relus ne constituent pas une estimation individuelle de G08 dans la présente version.', 'g08-coma')
add_if_absent('mRS', [('m','modified'),('R','Rankin'),('S','Scale')], 'Échelle de Rankin modifiée (modified Rankin Scale)',
              'Échelle fonctionnelle utilisée dans les études après thrombose veineuse cérébrale ; elle ne constitue pas un critère de G08 et ne résume pas toutes les séquelles cognitives.', 'g08-pronostic')
add_if_absent('DECOMPRESS2', [('DECOMPRESS2', 'nom d’une cohorte observationnelle, non un sigle à développer artificiellement')],
              'Cohorte observationnelle DECOMPRESS2',
              'Cohorte prospective observationnelle de décompression, décrite par la revue2025, et non essai randomisé. Elle concerne des thromboses graves de toutes causes, pas exclusivement septiques.', 'g08-decompression')
add_if_absent('DOAC-CVT', [('DOAC', 'Direct Oral AntiCoagulants (anticoagulants oraux directs)'), ('CVT', 'Cerebral Venous Thrombosis (thrombose veineuse cérébrale)')],
              'Cohorte DOAC-CVT',
              'Cohorte observationnelle internationale de thrombose veineuse cérébrale ; ses chiffres non relus dans la source originale ne sont pas présentés comme preuve spécifique de G08 septique.', 'g08-aod')
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
              'Cause inflammatoire de syndrome caverneux discutée dans le différentiel de la série européenne2018 effectivement lue ; aucun traitement immunosuppresseur ne se décide sur le seul nom sans rechercher infection.')
add_if_absent('Pays-Bas', [('Pays-Bas', 'nom propre d’un pays, non une abréviation')], 'Pays-Bas', 'Pays des équipes de la série clinique2018effectivement lue ; ses données ne deviennent pas une incidence suisse.')
add_if_absent('Papouasie-Nouvelle-Guinée', [('Papouasie-Nouvelle-Guinée', 'nom propre d’un pays, non une abréviation')], 'Papouasie-Nouvelle-Guinée', 'Nom de pays conservé comme clé de glossaire ; aucun chiffre de série historique de ce pays n’est généralisé à G08 dans cette version.')

# Codes et noms propres de la version G08 relue en novembre2026 ; clés antérieures conservées.
for _code, _text in [('G95.18', 'Code de la classification française2024des autres myélopathies vasculaires ; exclusion des formes intrarachidiennes non purulentes dans les notes G08.'), ('O08.7', 'Autres complications veineuses consécutives à un avortement, une grossesse extra-utérine ou molaire ; exclusion causale de G08.'), ('O22.5', 'Thrombose veineuse cérébrale au cours de la grossesse ; codage obstétrical distinct de G08.'), ('O87.3', 'Thrombose veineuse cérébrale au cours de la puerpéralité ; codage obstétrical distinct de G08.')]:
    add_if_absent(_code, [(_code, 'code de classification, non une abréviation médicale')], 'Code ' + _code, _text, 'g08-codage')
add_if_absent('SINT', [('SINT', 'élément d’un nom commercial, non une abréviation médicale à développer')], 'Metronidazole SINT i.v.', 'Spécialité suisse exacte de métronidazole ; sa dose générale de FI ne constitue pas un protocole universel de G08.', 'g08-metronidazole')
add_if_absent('Oto-Rhino-Laryngology', [('Oto-Rhino-Laryngology', 'élément anglais du titre propre d’une revue')], 'European Archives of Oto-Rhino-Laryngology', 'Revue de la série néerlandaise2018de thrombose septique du sinus caverneux ; le titre est conservé pour une attribution exacte.', 'g08-r5')
