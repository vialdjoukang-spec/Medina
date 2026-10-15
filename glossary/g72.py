"""Abréviations G72 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'g72', '__init__'}:
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

for _code, _lib, _win in [
    ('G72.0', 'médicamenteuse', 'g72-toxique'),
    ('G72.1', 'alcoolique', 'g72-alcool'),
    ('G72.2', 'due à d’autres agents toxiques', 'g72-toxique'),
    ('G72.3', 'paralysie périodique', 'g72-canaux'),
    ('G72.4', 'inflammatoire non classée ailleurs', 'g72-ibm'),
    ('G72.80', 'de réanimation (critical illness myopathy)', 'g72-rea-criteres'),
    ('G72.88', 'autre myopathie précisée', 'g72-cim'),
    ('G72.9', 'sans précision', 'g72-cim'),
]:
    add_if_absent(_code, [(_code[:3], 'catégorie de la classification internationale des maladies'), (_code[3:], 'sous-rubrique')],
                  'Myopathie ' + _lib + ' (' + _code + ')',
                  'Sous-rubrique de la catégorie G72 (autres myopathies) dans la CIM-10-GM 2024 de l’Institut fédéral allemand des médicaments.', _win)
for _code, _txt in [
    ('G70', 'Bloc G70–G73 de la CIM-10-GM : maladies musculaires et de la jonction neuromusculaire.'),
    ('G73', 'Fin du bloc G70–G73 de la CIM-10-GM.'),
    ('M33', 'Catégorie de la dermatomyosite-polymyosite, exclue de G72.'),
    ('M33.2', 'Polymyosite, exclue de G72.'),
    ('M60', 'Catégorie de la myosite, exclue de G72.'),
    ('M62.2', 'Infarctus musculaire ischémique, exclu de G72.'),
    ('Q74.3', 'Arthrogrypose multiple congénitale, exclue de G72.'),
]:
    add_if_absent(_code, [(_code, 'code de la CIM-10-GM, non une abréviation développable')], 'Code ' + _code + ' de la CIM-10-GM 2024', _txt, 'g72-cim')
add_if_absent('ABCDEF', [('ABCDEF', 'sigle d’un ensemble de mesures de réanimation ; les lettres ne sont pas développées dans les passages lus')],
              'Approche ABCDEF de réanimation', 'Ensemble de mesures citées par Latronico et coll. (2023) pour la prévention de la faiblesse acquise en réanimation (mobilisation précoce, sédation légère).', 'g72-rea-criteres')
add_if_absent('B6', [('B', 'vitamine du groupe B'), ('6', 'numéro 6')], 'Vitamine B6', 'Vitamine citée parmi les carences qui contribuent à la myopathie alcoolique.', 'g72-alcool')
add_if_absent('CACNA1S', [('CACN', 'Calcium Channel (canal calcique dépendant du voltage)'), ('A1', 'sous-unité alpha 1'), ('S', 'isoforme du muscle squelettique')],
              'Gène de la sous-unité alpha 1S du canal calcique', 'Gène muté dans environ 60 % des familles de paralysie périodique hypokaliémique (Statland et coll., 2018). La réponse à l’acétazolamide y atteint 56 %.', 'g72-canaux')
add_if_absent('SCN4A', [('SCN', 'Sodium Channel (canal sodique dépendant du voltage)'), ('4', 'type IV'), ('A', 'sous-unité alpha')],
              'Gène de la sous-unité alpha du canal sodique de type IV', 'Gène muté dans environ 20 % des familles de paralysie périodique hypokaliémique et, par gain de fonction, dans la forme hyperkaliémique.', 'g72-canaux')
add_if_absent('KCNJ2', [('K', 'Potassium'), ('CN', 'Channel (canal)'), ('J', 'sous-famille J'), ('2', 'membre 2')],
              'Gène du canal potassique Kir2.1', 'Gène muté dans le syndrome d’Andersen-Tawil.', 'g72-canaux')
add_if_absent('KCNJ18', [('K', 'Potassium'), ('CN', 'Channel (canal)'), ('J', 'sous-famille J'), ('18', 'membre 18')],
              'Gène du canal potassique Kir2.6', 'Gène retrouvé dans jusqu’à 3 % des formes thyrotoxiques de paralysie périodique (Statland et coll., 2018).', 'g72-canaux')
add_if_absent('Nav1.4', [('Na', 'sodium'), ('v', 'voltage-dépendant'), ('1.4', 'sous-type 1.4')], 'Canal sodique voltage-dépendant du muscle squelettique',
              'Canal dont la perte de disponibilité contribue à l’inexcitabilité de la fibre dans la myopathie de réanimation (modèles animaux et in vitro).', 'g72-canaux')
add_if_absent('SLCO1B1', [('SLCO', 'Solute Carrier Organic anion transporter'), ('1B1', 'famille 1, membre B1')], 'Gène du transporteur OATP1B1',
              'Variants associés à un risque plus élevé de myopathie sous simvastatine à forte dose.', 'g72-slco1b1')
add_if_absent('OATP1B1', [('O', 'Organic'), ('A', 'Anion'), ('T', 'Transporting'), ('P', 'Polypeptide'), ('1B1', 'famille 1, membre B1')], 'Polypeptide transporteur d’anions organiques 1B1',
              'Transporteur codé par SLCO1B1 qui module l’exposition aux statines.', 'g72-slco1b1')
add_if_absent('rs4149056', [('rs4149056', 'identifiant d’un variant génétique, non une abréviation')], 'Variant rs4149056 de SLCO1B1',
              'Variant associé à un risque de myopathie de 18 % chez les homozygotes sous simvastatine à forte dose (étude SEARCH).', 'g72-slco1b1')
add_if_absent('SEARCH', [('S', 'Study'), ('E', 'of the Effectiveness'), ('A', 'of Additional'), ('R', 'Reductions in'), ('C', 'Cholesterol and'), ('H', 'Homocysteine')], 'Étude SEARCH',
              'Essai cité par le consensus européen pour le risque de myopathie selon le génotype SLCO1B1.', 'g72-slco1b1')
add_if_absent('STOMP', [('ST', 'Statins (Effect of Statins)'), ('O', 'On skeletal'), ('M', 'Muscle'), ('P', 'Performance')], 'Essai STOMP',
              'Essai cité pour les myalgies sous atorvastatine 80 mg (9,4 %) contre placebo (4,6 %).', 'g72-eas')
add_if_absent('NICE-SUGAR', [('NICE', 'Normoglycaemia in Intensive Care Evaluation'), ('SUGAR', 'Survival Using Glucose Algorithm Regulation')], 'Essai NICE-SUGAR',
              'Essai cité pour la hausse des hypoglycémies et de la mortalité à 90 jours sous contrôle glycémique intensif en réanimation.', 'g72-rea-criteres')
add_if_absent('HMGCR', [('H', 'Hydroxy'), ('M', 'Méthyl'), ('G', 'Glutaryl-coenzyme A'), ('CR', 'Réductase')], '3-hydroxy-3-méthylglutaryl-coenzyme A réductase',
              'Enzyme de la voie du cholestérol, cible des statines et d’un auto-anticorps de la myopathie nécrosante à médiation immune.', 'g72-imnm')
add_if_absent('HMG-CoA', [('HMG', 'Hydroxy-Méthyl-Glutaryl'), ('CoA', 'coenzyme A')], '3-hydroxy-3-méthylglutaryl-coenzyme A',
              'Substrat de l’enzyme HMG-CoA réductase.', 'g72-imnm')
add_if_absent('SRP', [('S', 'Signal'), ('R', 'Recognition'), ('P', 'Particle')], 'Particule de reconnaissance du signal',
              'Cible d’un auto-anticorps de la myopathie nécrosante à médiation immune.', 'g72-imnm')
add_if_absent('IGF-1', [('I', 'Insulin-like'), ('G', 'Growth'), ('F', 'Factor'), ('1', 'numéro 1')], 'Facteur de croissance analogue à l’insuline 1',
              'Médiateur dont la baisse s’associe à la baisse de la synthèse protéique dans les myopathies cortisonique et alcoolique.', 'g72-cortico')
add_if_absent('FOXO', [('FOXO', 'Forkhead box O, nom de famille de facteurs de transcription')], 'Facteurs de transcription Forkhead box O',
              'Facteurs qui activent les atrogènes dans la myopathie cortisonique.', 'g72-cortico')
add_if_absent('MuRF-1', [('Mu', 'Muscle'), ('RF', 'RING-Finger'), ('1', 'protéine 1')], 'Protéine à doigt RING du muscle 1',
              'Atrogène (ligase de l’ubiquitine) activé par les glucocorticoïdes.', 'g72-cortico')
add_if_absent('mTORC1', [('mTOR', 'mechanistic Target Of Rapamycin'), ('C1', 'complexe 1')], 'Complexe 1 de la cible mécanistique de la rapamycine',
              'Voie de synthèse protéique freinée dans la myopathie alcoolique.', 'g72-alcool')
add_if_absent('mTOR', [('m', 'mechanistic'), ('TOR', 'Target Of Rapamycin')], 'Cible mécanistique de la rapamycine',
              'Voie de synthèse protéique freinée dans la myopathie cortisonique.', 'g72-cortico')
add_if_absent('ENMC', [('E', 'European'), ('N', 'NeuroMuscular'), ('C', 'Centre')], 'Centre neuromusculaire européen',
              'Organisation dont les ateliers ont proposé la classification des myopathies nécrosantes (2016) et les critères de la myosite à inclusions (2024).', 'g72-imnm')
add_if_absent('Q10', [('Q', 'quinone'), ('10', 'dix unités isoprène')], 'Coenzyme Q10',
              'Composé dont la déplétion est un mécanisme proposé de la toxicité des statines ; sa supplémentation n’est pas recommandée.', 'g72-alternatives')
add_if_absent('hypoPP', [('hypo', 'hypokaliémique'), ('PP', 'Paralysie Périodique')], 'Paralysie périodique hypokaliémique',
              'Forme avec potassium bas pendant l’accès.', 'g72-hypopp')
add_if_absent('hyperPP', [('hyper', 'hyperkaliémique'), ('PP', 'Paralysie Périodique')], 'Paralysie périodique hyperkaliémique',
              'Forme avec potassium élevé ou normal pendant l’accès.', 'g72-canaux')
add_if_absent('anti-cN1A', [('anti', 'dirigé contre'), ('cN1A', 'nucléotidase cytosolique 1A')], 'Anticorps dirigé contre la 5’-nucléotidase cytosolique 1A',
              'Anticorps cité parmi les éléments des critères révisés de la myosite à inclusions (ENMC 2024), dont le contenu n’a pas été lu.', 'g72-ibm')
add_if_absent('F1000Research', [('F1000Research', 'nom de revue, non une abréviation')], 'F1000Research', 'Revue qui a publié la mise au point sur la faiblesse acquise en réanimation.', 'g72-rea-criteres')
add_if_absent('Andersen-Tawil', [('Andersen-Tawil', 'noms de deux auteurs, non une abréviation')], 'Syndrome d’Andersen-Tawil',
              'Paralysie périodique due à des mutations de KCNJ2, associant paralysie, anomalie cardiaque et dysmorphie (58 à 78 % des porteurs) ; début entre 2 et 18 ans, accès de 1 à 36 heures.', 'g72-canaux')
add_if_absent('Atorvastatin-Mepha', [('Atorvastatin', 'atorvastatine'), ('Mepha', 'nom du fabricant, non une abréviation')], 'Atorvastatin-Mepha, nom commercial de l’atorvastatine',
              'Générique de l’atorvastatine dont l’information professionnelle suisse (avril 2025) a été lue.', 'g72-atorva')
add_if_absent('Acétyl-CoA', [('Acétyl', 'groupe acétyle'), ('CoA', 'coenzyme A')], 'Acétyl-coenzyme A',
              'Précurseur de la voie du mévalonate, point de départ de la synthèse du cholestérol.', 'g72-atorva')
