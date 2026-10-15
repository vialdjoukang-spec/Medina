from cardio_1 import a, G
# G90 — Affections du système nerveux autonome (N-05-Neurologie). Entrées conditionnelles : aucun terme existant n’est écrasé.
from pathlib import Path
import importlib
_ex = set(G)
for _p in sorted(Path(__file__).parent.glob('*.py')):
    if _p.stem in {'g90', '__init__', 'cardio_1'}:
        continue
    try:
        _ex |= set(getattr(importlib.import_module(_p.stem), 'G', {}))
    except Exception:
        pass
def ac(k, lit, full, d, ref=None):
    if k not in _ex:
        a(k, lit, full, d, ref)

ac('HO', [('H','Hypotension'),('O','Orthostatique')], 'Hypotension orthostatique', '<p>Baisse progressive et soutenue de la pression systolique d’au moins 20 mmHg ou de la pression diastolique d’au moins 10 mmHg, ou pression systolique inférieure à 90 mmHg, après le passage à la position debout (ESC 2018).</p>', 'g90-criteres-ho')
ac('HOn', [('HO','Hypotension Orthostatique'),('n','neurogène')], 'Hypotension orthostatique neurogène', '<p>Hypotension orthostatique due à une atteinte du réflexe de régulation de la pression : l’accélération cardiaque est émoussée ou absente, habituellement de 10 battements par minute ou moins (consensus AAS/EFAS 2018).</p>', 'g90-hon')
ac('HDn', [('HD','Hypertension de Décubitus'),('n','neurogène')], 'Hypertension de décubitus neurogène', '<p>Chez un patient dont l’hypotension orthostatique neurogène est prouvée, pression systolique d’au moins 140 mmHg et/ou diastolique d’au moins 90 mmHg après au moins 5 minutes couché.</p>', 'g90-hdn')
ac('SDRC', [('S','Syndrome'),('D','Douloureux'),('R','Régional'),('C','Complexe')], 'Syndrome douloureux régional complexe', '<p>Douleur post-traumatique primaire et invalidante des parties distales des membres, anciennement algodystrophie ou maladie de Sudeck ; le diagnostic est clinique, selon les critères de Budapest.</p>', 'g90-budapest')
ac('PoTS', [('Po','Postural'),('T','Tachycardia'),('S','Syndrome')], 'Syndrome de tachycardie posturale (nom anglais : Postural Tachycardia Syndrome)', '<p>Accélération cardiaque excessive au lever avec intolérance orthostatique, sans la chute de pression de l’hypotension orthostatique.</p>', 'g90-pots')
ac('EFAS', [('E','European'),('F','Federation of'),('A','Autonomic'),('S','Societies')], 'European Federation of Autonomic Societies (Fédération européenne des sociétés du système nerveux autonome)', '<p>Fédération qui a publié, avec l’American Autonomic Society, le consensus de 2018 sur l’hypertension de décubitus neurogène.</p>', 'g90-hdn')
ac('ELP1', [('ELP','Elongator complex'),('1','protein 1')], 'Gène ELP1 (Elongator complex protein 1)', '<p>Gène dont la mutation fondatrice provoque la dysautonomie familiale par saut de l’exon 20 et perte de la protéine Elongator-1.</p>', 'g90-elp1')
ac('HSAN', [('H','Hereditary'),('S','Sensory and'),('A','Autonomic'),('N','Neuropathy')], 'Neuropathie sensitive et autonome héréditaire (Hereditary Sensory and Autonomic Neuropathy)', '<p>Groupe de neuropathies héréditaires ; la dysautonomie familiale est le type 3.</p>', 'g90-fd')
ac('gAChR', [('g','ganglionic'),('A','Acetyl'),('Ch','Choline'),('R','Receptor')], 'Récepteur nicotinique ganglionnaire de l’acétylcholine', '<p>Cible des anticorps pathogènes de la ganglionopathie autonome auto-immune.</p>', 'g90-ganglionopathie')
ac('CGRP', [('C','Calcitonin'),('G','Gene-'),('R','Related'),('P','Peptide')], 'Peptide lié au gène de la calcitonine', '<p>Neuropeptide des fibres afférentes C, impliqué dans l’inflammation neurogène du syndrome douloureux régional complexe et dans le bourgeonnement afférent de la dysréflexie autonome.</p>', 'g90-cgrp')

ac('CIM', [('C','Classification'),('I','Internationale des'),('M','Maladies')], 'Classification internationale des maladies', '<p>Classification de l’Organisation mondiale de la santé dont la version allemande modifiée, CIM-10-GM 2024, sert de catalogue à ce cours.</p>', 'g90-codage')
_codes = {
 'G90.0': 'Neuropathie autonome périphérique idiopathique (sous-codes G90.00, G90.08, G90.09)',
 'G90.00': 'Syndrome du sinus carotidien (syncope)',
 'G90.1': 'Dysautonomie familiale [Riley-Day]',
 'G90.2': 'Syndrome de Claude Bernard-Horner',
 'G90.3': 'Code inexistant en CIM-10-GM 2024 : l’atrophie multisystématisée est codée G23.2 et G23.3',
 'G90.4': 'Dysréflexie autonome (sous-codes G90.40 à G90.49)',
 'G90.40': 'Dysréflexie autonome avec crises hypertensives',
 'G90.41': 'Dysréflexie autonome avec crises de transpiration',
 'G90.5': 'Syndrome douloureux régional complexe de type I (sous-codes G90.50 à G90.59)',
 'G90.6': 'Syndrome douloureux régional complexe de type II (sous-codes G90.60 à G90.69)',
 'G90.7': 'Syndrome douloureux régional complexe, autre type et type non précisé',
 'G90.8': 'Autres affections du système nerveux autonome (G90.80 et G90.88)',
 'G90.80': 'Syndrome de tachycardie posturale',
 'G90.9': 'Affection du système nerveux autonome, sans précision',
 'G23.2': 'Atrophie multisystématisée de type parkinsonien',
 'G23.3': 'Atrophie multisystématisée de type cérébelleux',
 'G23.8': 'Autres affections dégénératives des noyaux gris centraux, dont l’hypotension orthostatique neurogène [Shy-Drager]',
 'G31.2': 'Dysfonction du système nerveux autonome due à l’alcool',
}
for _k, _v in _codes.items():
    ac(_k, [(_k, 'code de la CIM-10-GM 2024, non une abréviation à développer lettre à lettre')], 'Code ' + _k + ' de la CIM-10-GM 2024', '<p>' + _v + '.</p>', 'g90-codage')
for _k, _v, _d in [
 ('González-Duarte', 'González-Duarte, auteur d’une revue', 'Premier auteur de la revue sur la dysautonomie familiale citée dans ce cours.'),
 ('Budge-Waller', 'Budge-Waller, noms propres des auteurs', 'Le centre cilio-spinal de Budge-Waller, situé du 8e segment cervical au 2e segment thoracique, abrite le premier neurone de la voie oculosympathique.'),
 ('Shy-Drager', 'Shy-Drager, noms propres des auteurs', 'Nom de l’hypotension orthostatique neurogène associée à l’atrophie multisystématisée.'),
 ('Riley-Day', 'Riley-Day, noms propres des auteurs', 'Autre nom de la dysautonomie familiale.')]:
    ac(_k, [(_k, 'noms propres, non une abréviation')], _v, '<p>' + _d + '</p>', 'g90-fd')
