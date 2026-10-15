"""Abréviations G37 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'g37', '__init__'}:
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

add_if_absent('ADEM', [('A','Acute'),('D','Disseminated'),('EM','EncephaloMyelitis')],
              'Encéphalomyélite aiguë disséminée (Acute Disseminated EncephaloMyelitis)',
              'Premier événement polyfocal, présumé inflammatoire et démyélinisant, avec encéphalopathie. La classification CIM-10-GM 2024 la place sous G 37.8.', 'g37-adem')
add_if_absent('IPMSSG', [('I','International'),('P','Pediatric'),('MS','Multiple Sclerosis'),('S','Study'),('G','Group')],
              'International Pediatric Multiple Sclerosis Study Group',
              'Ce groupe d’étude a publié en 2013 la révision de critères des maladies démyélinisantes du système nerveux central, dont l’encéphalomyélite aiguë disséminée.', 'g37-adem')
add_if_absent('TMCWG', [('T','Transverse'),('M','Myelitis'),('C','Consortium'),('W','Working'),('G','Group')],
              'Transverse Myelitis Consortium Working Group',
              'Ce groupe de travail a proposé en 2002 des critères diagnostiques de la myélite transverse aiguë. Le texte intégral n’a pas été lu pour ce cours.', 'g37-atm')
add_if_absent('NEMOS', [('NE','NEuro'),('M','Myelitis'),('O','Optica'),('S','Studiengruppe')],
              'Neuromyelitis Optica Studiengruppe (groupe d’étude allemand)',
              'Ce groupe allemand a publié en 2023 et 2024 des recommandations révisées sur la neuromyélite optique. Leur transposition à la myélite du G 37.3 est une extrapolation.', 'g37-aph')
add_if_absent('EFNS', [('E','European'),('F','Federation'),('N','of Neurological'),('S','Societies')],
              'European Federation of Neurological Societies',
              'Cette fédération, aujourd’hui Académie européenne de neurologie, a publié en 2010 la recommandation sur l’encéphalopathie de Wernicke.', 'g37-thiamine')
add_if_absent('DGN', [('D','Deutsche'),('G','Gesellschaft'),('N','für Neurologie')],
              'Société allemande de neurologie (Deutsche Gesellschaft für Neurologie)',
              'Sa directive 030-050 n’a pas pu être consultée pour ce cours.', 'g37-lacunes')
add_if_absent('OR', [('O','Odds'),('R','Ratio')], 'Rapport de cotes (odds ratio)',
              'Mesure d’association entre une exposition et un événement. Une valeur supérieure à 1 indique une association positive ; elle ne prouve pas la causalité.', 'g37-foix')
add_if_absent('Marchiafava-Bignami', [('Marchiafava-Bignami', 'noms propres des auteurs de la description, non une abréviation')],
              'Maladie de Marchiafava-Bignami',
              'Démyélinisation et nécrose du corps calleux, surtout chez l’alcoolique dénutri.', 'g37-mbd')
add_if_absent('Foix-Alajouanine', [('Foix-Alajouanine', 'noms propres des auteurs de la description, non une abréviation')],
              'Syndrome de Foix-Alajouanine',
              'Myélopathie progressive liée à une malformation artério-veineuse spinale, le plus souvent une fistule durale.', 'g37-foix')
add_if_absent('anti-MOG', [('anti','dirigé contre'),('MOG','Myelin Oligodendrocyte Glycoprotein')],
              'Anticorps dirigés contre la glycoprotéine de la myéline des oligodendrocytes',
              'Leur présence, détectée par test sur cellules, est le critère central de la maladie associée à ces anticorps.', 'g37-mogad')
add_if_absent('anti-NMDAR', [('anti','dirigé contre'),('N','N-'),('M','Méthyl-'),('D','D-'),('A','Aspartate'),('R','Récepteur')],
              'Anticorps dirigés contre le récepteur N-méthyl-D-aspartate',
              'Cette encéphalite auto-immune figure dans le diagnostic différentiel de l’encéphalomyélite aiguë disséminée.', 'g37-adem')
add_if_absent('anti-CRMP5', [('anti','dirigé contre'),('CRMP','Collapsin Response Mediator Protein'),('5','numéro 5')],
              'Anticorps dirigés contre la protéine 5 médiatrice de la réponse de collapsine',
              'Anticorps associé aux myélites paranéoplasiques, avec les anticorps anti-Hu.', 'g37-irm-myelite')
