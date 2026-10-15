"""Abréviations R26 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'r26', '__init__'}:
        continue
    _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
G = {}
def add_if_absent(key, letters, full, definition, window=None):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full,
                  'def': '<p>' + definition + '</p>', 'ref': window}

def _np(key, nature, full, definition, window=None):
    """Nom propre ou nom commercial : aucune lettre à développer."""
    add_if_absent(key, [(key, nature)], full, definition, window)

add_if_absent('SSP', [('S','Situations'),('S','(as) Starting'),('P','Points')],
              'Situations as Starting Points, situations de départ du référentiel PROFILES',
              'Le référentiel PROFILES 2017 numérote les situations cliniques de départ de l’examen fédéral. Ce cours relie le symptôme R26 aux situations 96, 97, 98 et 103 par une correspondance pédagogique du dépôt.', 'r26-ssp')
add_if_absent('WFG', [('W','World'),('F','Falls'),('G','Guidelines')],
              'World Falls Guidelines, recommandations mondiales de prévention des chutes',
              'Ces recommandations internationales de 2022 définissent les catégories de risque de chute (faible, intermédiaire, élevé) et l’intervention correspondante.', 'r26-wfg')
add_if_absent('TUG', [('T','Timed'),('U','Up'),('G','and Go')],
              'Timed Up and Go',
              'Test chronométré : se lever d’une chaise à accoudoirs, marcher 3 m, se retourner, revenir et s’asseoir. Un temps supérieur à 15 secondes est un seuil de risque de chute.', 'r26-tug')
add_if_absent('SPPB', [('S','Short'),('P','Physical'),('P','Performance'),('B','Battery')],
              'Short Physical Performance Battery',
              'Batterie de tests de la fonction physique citée parmi les outils de mesure de la marche et de l’équilibre des recommandations mondiales.')
add_if_absent('EMS', [('E','Établissement'),('M','Médico'),('S','Social')],
              'Établissement médico-social',
              'Structure d’hébergement et de soins pour personnes âgées en Suisse. Tous ses résidents sont considérés à haut risque de chute.', 'r26-ems')
add_if_absent('CHF', [('CH','Confoederatio Helvetica'),('F','franc')],
              'Franc suisse',
              'Code international de la monnaie suisse, utilisé pour le coût matériel annuel des chutes estimé par le BFU.')
add_if_absent('BFU', [('B','Beratungsstelle'),('F','für'),('U','Unfallverhütung')],
              'Beratungsstelle für Unfallverhütung, Bureau suisse de prévention des accidents',
              'Ce bureau, à Berne, publie les données suisses sur les chutes des personnes de 65 ans et plus et les programmes de prévention.', 'r26-bfu')
_np('StoppSturz', 'nom propre du programme de prévention du BFU, non une abréviation', 'StoppSturz, programme suisse de prévention des chutes',
    'Ce programme du BFU, dont le nom allemand signifie « arrêter la chute », propose des supports de formation pour les professionnels et les personnes âgées.', 'r26-bfu')
_np('STOPPFall', 'nom propre du consensus européen, non une abréviation à développer ici', 'STOPPFall, consensus européen sur les médicaments qui augmentent le risque de chute',
    'Ce consensus Delphi de 2021 identifie 14 classes de médicaments à risque et précise les différences à l’intérieur de chaque classe.', 'r26-stoppfall')
_np('DO-HEALTH', 'nom propre de l’essai, dont le résumé lu ne développe pas les lettres', 'DO-HEALTH, essai européen sur le vieillissement en bonne santé',
    'Cet essai coordonné à Zurich a inclus 2157 Européens de 70 ans et plus, selon un plan factoriel 2×2×2 (vitamine D, oméga-3, exercice).', 'r26-vitd')
_np('VITAL', 'nom propre d’un essai américain, lettres non développées dans le résumé lu', 'VITAL, essai sur la vitamine D chez 25 871 adultes',
    'Cet essai américain est cité comme donnée probante avec DO-HEALTH, non comme recommandation.', 'r26-vitd')
_np('Vi-De', 'nom commercial, non une abréviation', 'Vi-De 3, cholécalciférol en gouttes (information professionnelle suisse)',
    'Spécialité de la société VERFORA dont l’information professionnelle est mise à jour en octobre 2021.', 'r26-vide3')
_np('VERFORA', 'nom propre de société, non une abréviation', 'VERFORA, titulaire de l’autorisation de Vi-De 3', 'Société suisse titulaire de l’autorisation de la spécialité Vi-De 3.', 'r26-vide3')
_np('Sanofi-Aventis', 'nom propre de société, non une abréviation', 'Sanofi-Aventis (Suisse), titulaire de l’autorisation de Clexane', 'Société titulaire de l’autorisation de la spécialité Clexane.', 'r26-clexane')
add_if_absent('SA', [('S','Société'),('A','Anonyme')], 'Société anonyme', 'Forme juridique d’une société, citée dans le nom du titulaire d’une autorisation.')
_np('Montero-Odasso', 'nom propre du premier auteur, non une abréviation', 'Montero-Odasso, premier auteur des World Falls Guidelines', 'Auteur principal des recommandations mondiales de prévention des chutes de 2022.', 'r26-wfg')
_np('LeBoff', 'nom propre d’une autrice, non une abréviation', 'LeBoff, première autrice d’une synthèse des essais VITAL et DO-HEALTH', 'Autrice de la synthèse de 2023 sur la vitamine D et la santé musculosquelettique.', 'r26-vitd')
_np('Bischoff-Ferrari', 'nom propre d’une autrice, non une abréviation', 'Bischoff-Ferrari, coordinatrice de l’essai DO-HEALTH', 'Autrice de l’Université de Zurich qui coordonne l’essai DO-HEALTH.', 'r26-vitd')
add_if_absent('ISFM', [('I','Institut'),('S','Suisse pour la'),('F','Formation'),('M','Médicale postgraduée et continue')],
              'Institut suisse pour la formation médicale postgraduée et continue',
              'Cet institut publie, avec les facultés de médecine, le référentiel PROFILES de l’examen fédéral.', 'r26-ssp')
add_if_absent('CIM', [('C','Classification'),('I','Internationale des'),('M','Maladies')],
              'Classification internationale des maladies',
              'Classification statistique des diagnostics ; le catalogue de ce projet suit la dixième révision, modification allemande 2024.')
add_if_absent('BD-FIC', [('B','Blessure'),('D','Deux chutes ou plus en douze mois'),('F','Fragilité'),('I','Incapacité à se relever pendant une heure ou plus'),('C','Connaissance perdue, perte de connaissance suspectée')],
              'Moyen mnémotechnique des critères de risque élevé de chute',
              'Aide pédagogique, non critère officiel : un acronyme propre à ce cours pour retenir les cinq éléments qui, associés à une chute, classent le patient à risque élevé.', 'r26-mnemo')

# Codes CIM-10-GM 2024 cités dans le cours (libellés de l’Office fédéral de la statistique, inclusions et exclusions du BfArM).
for _code, _lib, _def in [
    ('R26', 'Anomalies de la démarche et de la motilité', 'Catégorie de symptômes qui cède la place au diagnostic étiologique dès qu’il est posé.'),
    ('R26.0', 'Démarche ataxique', 'Inclut la démarche titubante ; l’ataxie qui ne se limite pas à la marche se code R27.0.'),
    ('R26.1', 'Démarche paralytique', 'Inclut la démarche spastique.'),
    ('R26.2', 'Difficulté à la marche, non classée ailleurs', 'Accueille les marches prudente, antalgique, frontale ou parkinsonienne non rattachées à un diagnostic.'),
    ('R26.3', 'Immobilité', 'Inclut la dépendance au fauteuil roulant et l’alitement ; exclut le syndrome d’immobilité paraplégique (M62.3-).'),
    ('R26.8', 'Anomalies de la démarche et de la motilité, autres et non précisées', 'Inclut l’instabilité debout sans autre précision.'),
    ('R27.0', 'Ataxie, sans précision', 'Ataxie qui ne se limite pas à la marche ; exclue de R26.'),
    ('A52.1', 'Tabès (ataxie locomotrice syphilitique)', 'Exclu de R26.'),
    ('M62.3', 'Syndrome d’immobilité (paraplégique)', 'Exclu de R26 ; la rubrique est notée M62.3- dans la classification.'),
    ('G11', 'Ataxie héréditaire', 'Les codes G11.- sont exclus de R26.'),
]:
    add_if_absent(_code, [(_code, 'code de la CIM-10-GM 2024 : ' + _lib)], _lib, _def, 'r26-exclusions')
