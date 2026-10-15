"""Abréviations G97 (cycle Betta 41) ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib, sys
_existing = {}
def _root():
    for p in [Path(__file__).resolve().parent] + list(Path(__file__).resolve().parents):
        if (p / 'glossary' / 'cardio_1.py').exists():
            return p / 'glossary'
    return None
_g = _root()
if _g is not None:
    sys.path.insert(0, str(_g))
    for _path in sorted(_g.glob('*.py')):
        if _path.stem in {'g97', '__init__'}:
            continue
        try:
            _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
        except Exception:
            pass
G = {}
def a(key, letters, full, definition, window=None):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full, 'def': '<p>' + definition + '</p>', 'ref': window}

a('LCR', [('L','Liquide'),('C','Céphalo-'),('R','Rachidien')], 'Liquide céphalorachidien',
  'Liquide qui baigne le système nerveux central ; sa fuite par une brèche durale peut abaisser sa pression et provoquer une céphalée.', 'g97-lcr')
a('ICHD-3', [('I','International'),('C','Classification of'),('H','Headache'),('D','Disorders,'),('3','troisième édition')], 'Classification internationale des céphalées, troisième édition',
  'Classification de la International Headache Society ; sa rubrique 7.2 décrit les céphalées attribuées à une basse pression du LCR.', 'g97-ichd')
a('BPE', [('B','Blood'),('P','Patch'),('E','Épidural')], 'Blood patch épidural',
  'Injection de sang autologue dans l’espace épidural pour obturer une fuite de LCR ; traitement de référence de la céphalée post-ponction invalidante ou réfractaire.', 'g97-bpe')
a('POSI', [('PO','Post-Operative'),('S','Speech'),('I','Impairment')], 'Postoperative speech impairment, trouble de la parole postopératoire',
  'Terme de la cohorte européenne : mutisme ou parole sévèrement réduite après chirurgie de la fosse postérieure.', 'g97-mutisme-def')
a('OR', [('O','Odds'),('R','Ratio')], 'Rapport de cotes (odds ratio)',
  'Mesure d’association comparant des cotes entre deux groupes ; une valeur de 1 signale l’absence d’association, et la mesure ne donne pas une fréquence.', 'g97-or')
a('ESRA', [('E','European'),('S','Society of'),('R','Regional'),('A','Anaesthesia and Pain Therapy')], 'European Society of Regional Anaesthesia and Pain Therapy',
  'Société européenne d’anesthésie régionale et de traitement de la douleur ; cosignataire du consensus de 2023 et coauteure de la recommandation sur les antithrombotiques.', 'g97-consensus-origine')
a('ESAIC', [('E','European'),('S','Society of'),('A','Anaesthesiology and'),('I','Intensive'),('C','Care')], 'Société européenne d’anesthésiologie et de soins intensifs',
  'Coauteure, avec la société européenne d’anesthésie régionale, de la recommandation 2022 sur l’anesthésie régionale sous antithrombotiques.', 'g97-antithrombotiques')
a('AINS', [('A','Anti-'),('I','Inflammatoires'),('N','Non'),('S','Stéroïdiens')], 'Anti-inflammatoires non stéroïdiens',
  'Classe dont l’ibuprofène fait partie ; proposée par le consensus de 2023 dans la céphalée post-ponction, sauf contre-indication.', 'g97-ibuprofene')
a('IRM', [('I','Imagerie par'),('R','Résonance'),('M','Magnétique')], 'Imagerie par résonance magnétique',
  'Examen de référence retenu pour l’hématome épidural rachidien compressif, à réaliser en urgence.', 'g97-irm')
a('GRADE', [('GRADE','nom d’un système de cotation de la certitude de la preuve')], 'GRADE, système de cotation de la preuve',
  'Système qui qualifie la certitude d’une preuve ; la méta-analyse sur l’aiguille atraumatique est de haute qualité.', 'g97-grade-pop')
a('ACTH', [('A','Adreno'),('C','Cortico'),('T','Trophic'),('H','Hormone')], 'Hormone adrénocorticotrope',
  'Hormone citée parmi les traitements de la céphalée post-ponction sans soutien (grade I).', 'g97-nonsoutenus')
a('CIM-10-GM', [('CIM','Classification internationale des maladies'),('10','dixième révision'),('GM','German Modification, modification allemande')], 'CIM-10-GM',
  'Classification des maladies, révision allemande ; version 2024 utilisée pour situer la catégorie.', 'g97-cim')
a('BfArM', [('B','Bundesinstitut'),('f','für'),('Ar','Arzneimittel'),('M','und Medizinprodukte')], 'Institut fédéral allemand des médicaments et dispositifs médicaux',
  'Éditeur de la version allemande 2024 de la classification des maladies.', 'g97-cim')
a('AIPS', [('AIPS','sigle de la base suisse des informations professionnelles ; son développement lettre à lettre n’est pas établi dans les sources lues')], 'Base suisse des informations professionnelles',
  'Source des informations professionnelles suisses du paracétamol et de l’ibuprofène, lues le 15 octobre 2026.', 'g97-paracetamol')
a('Ibuprofen-Mepha', [('Ibuprofen-Mepha','nom commercial d’une spécialité suisse, non une abréviation')], 'Ibuprofen-Mepha Teva®, spécialité suisse',
  'Comprimés pelliculés dont l’information professionnelle suisse a été lue pour l’ibuprofène.', 'g97-ibuprofene')

a('EPiMAP', [('EPiMAP','nom d’une étude européenne sur l’échec du blood patch épidural après brèche durale obstétricale ; son développement lettre à lettre n’est pas établi dans les sources lues')], 'EPiMAP, étude européenne de cohorte',
  'Cohorte prospective multicentrique de 643 parturientes traitées par blood patch, qui identifie les facteurs associés à l’échec.', 'g97-bpe-echec')
for _code, _full, _w in (
    ('G97.0', 'Écoulement de liquide céphalorachidien après rachicentèse', 'g97-cim'),
    ('G97.1', 'Autre réaction secondaire à une rachicentèse', 'g97-cim'),
    ('G97.2', 'Hypotension intracrânienne suite à un pontage ventriculaire', 'g97-cim'),
    ('G97.80', 'Fistule de liquide céphalorachidien postopératoire', 'g97-cim'),
    ('G97.81', 'Mutisme (cérébelleux) postopératoire', 'g97-cim'),
    ('G97.82', 'Hémorragie rachidienne épidurale postopératoire', 'g97-cim'),
    ('G97.83', 'Hémorragie rachidienne sous-durale postopératoire', 'g97-cim'),
    ('G97.84', 'Hémorragie rachidienne sous-arachnoïdienne postopératoire', 'g97-cim'),
    ('G97.88', 'Autres maladies du système nerveux après des actes médicaux', 'g97-cim'),
    ('G97.9', 'Affection du système nerveux après un acte à visée diagnostique et thérapeutique, sans précision', 'g97-cim')):
    a(_code, [('G97', 'catégorie G97 de la CIM-10-GM 2024'), (_code[3:], 'subdivision de la catégorie')], _full,
      'Code de la CIM-10-GM 2024, libellé français de l’Office fédéral de la statistique.', _w)
