"""Abréviations N27 — Petit rein de cause inconnue ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'n27', '__init__'}:
        continue
    _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
G = {}
def add_if_absent(key, letters, full, definition, window):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full,
                  'def': '<p>' + definition + '</p>', 'ref': window}
add_if_absent('MRC', [('M', 'Maladie'), ('R', 'Rénale'), ('C', 'Chronique')], 'Maladie rénale chronique',
              'Anomalie de structure ou de fonction rénale présente depuis au moins trois mois, avec des implications pour la santé, selon KDIGO 2024.', 'n27-mrc')
add_if_absent('DFGe', [('D', 'Débit'), ('F', 'de Filtration'), ('G', 'Glomérulaire'), ('e', 'estimé')], 'Débit de filtration glomérulaire estimé',
              'Estimation du débit de filtration à partir de la créatinine, de la cystatine C ou des deux ; il classe la maladie rénale chronique en catégories G1 à G5.', 'n27-dfge')
add_if_absent('RAC', [('R', 'Rapport'), ('A', 'Albumine'), ('C', 'Créatinine (urinaires)')], 'Rapport albumine/créatinine urinaire',
              'Mesure de l’albuminurie sur un échantillon d’urine ; il range l’albuminurie en catégories A1 à A3.', 'n27-albuminurie')
add_if_absent('SRA', [('S', 'Système'), ('R', 'Rénine'), ('A', 'Angiotensine')], 'Système rénine-angiotensine',
              'Système hormonal bloqué par les IEC et les ARA ; son blocage fait chuter la filtration quand la perfusion rénale dépend de l’angiotensine II.', 'n27-sras')
add_if_absent('CAKUT', [('C', 'Congenital (congénitales)'), ('A', 'Anomalies'), ('K', 'of the Kidney (du rein)'), ('U', 'and Urinary (et des voies urinaires)'), ('T', 'Tract')], 'Anomalies congénitales du rein et des voies urinaires',
              'Groupe d’anomalies qui comprend l’agénésie, l’hypo ou dysplasie, la dysplasie multikystique, la duplicité et les valves de l’urètre postérieur.', 'n27-cakut')
add_if_absent('CGA', [('C', 'Cause'), ('G', 'catégorie de DFG (GFR)'), ('A', 'catégorie d’Albuminurie')], 'Cause, catégorie de DFG, catégorie d’albuminurie',
              'Nomenclature KDIGO qui classe la maladie rénale chronique.', 'n27-mrc')
add_if_absent('IR', [('I', 'Indice'), ('R', 'de Résistance')], 'Indice de résistance',
              'Paramètre de l’échodoppler rénal ; un IR supérieur à 0,80 annonce un faible bénéfice de revascularisation.', 'n27-echo')
add_if_absent('DMSA', [('D', 'Di'), ('M', 'Mercapto'), ('S', 'Succinique'), ('A', 'Acide')], 'Acide dimercaptosuccinique',
              'Traceur de la scintigraphie qui visualise le cortex rénal ; les cicatrices apparaissent en zones froides.', 'n27-dmsa')
add_if_absent('HNF1B', [('H', 'Hepatocyte (des hépatocytes)'), ('N', 'Nuclear (nucléaire)'), ('F', 'Factor (facteur)'), ('1', '1'), ('B', 'Bêta')], 'Facteur nucléaire des hépatocytes 1 bêta',
              'Gène dont le déficit associe kystes rénaux, diabète et atteinte multisystémique variable.', 'n27-hnf1b')
add_if_absent('UMOD', [('UMOD', 'UroMODuline (gène de l’uromoduline)')], 'Gène de l’uromoduline',
              'Gène cité parmi les huit gènes qui regroupent plus de 60 % des variants monogéniques de la maladie rénale chronique.', 'n27-genetique')
add_if_absent('PKD1', [('P', 'Polycystic (polykystique)'), ('K', 'Kidney (rénale)'), ('D', 'Disease (maladie)'), ('1', 'type 1')], 'Gène de la maladie rénale polykystique de type 1',
              'Gène parmi les huit qui regroupent plus de 60 % des variants monogéniques.', 'n27-genetique')
add_if_absent('PKD2', [('P', 'Polycystic (polykystique)'), ('K', 'Kidney (rénale)'), ('D', 'Disease (maladie)'), ('2', 'type 2')], 'Gène de la maladie rénale polykystique de type 2',
              'Gène parmi les huit qui regroupent plus de 60 % des variants monogéniques.', 'n27-genetique')
add_if_absent('COL4A3', [('COL', 'COLlagène'), ('4', 'de type 4'), ('A3', 'chaîne alpha 3')], 'Gène de la chaîne alpha 3 du collagène de type 4',
              'Gène parmi les huit qui regroupent plus de 60 % des variants monogéniques.', 'n27-genetique')
add_if_absent('COL4A4', [('COL', 'COLlagène'), ('4', 'de type 4'), ('A4', 'chaîne alpha 4')], 'Gène de la chaîne alpha 4 du collagène de type 4',
              'Gène parmi les huit qui regroupent plus de 60 % des variants monogéniques.', 'n27-genetique')
add_if_absent('COL4A5', [('COL', 'COLlagène'), ('4', 'de type 4'), ('A5', 'chaîne alpha 5')], 'Gène de la chaîne alpha 5 du collagène de type 4',
              'Gène parmi les huit qui regroupent plus de 60 % des variants monogéniques.', 'n27-genetique')
add_if_absent('MUC1', [('MUC', 'MUCine'), ('1', 'type 1')], 'Gène de la mucine 1',
              'Gène parmi les huit qui regroupent plus de 60 % des variants monogéniques.', 'n27-genetique')
add_if_absent('NPHS1', [('NPHS', 'NePHrotic Syndrome (syndrome néphrotique)'), ('1', 'type 1')], 'Gène du syndrome néphrotique de type 1',
              'Gène cité par KDIGO 2024 parmi ceux dont le test génétique joue un rôle croissant.', 'n27-genetique')
add_if_absent('SKIPOGH', [('SKIPOGH', 'nom d’une étude familiale suisse ; les sources lues ne donnent pas de développement lettre à lettre')], 'Étude suisse SKIPOGH',
              'Étude familiale suisse (Lausanne, Genève, Berne) qui a mesuré la longueur rénale échographique de 793 adultes d’ascendance européenne.', 'n27-taille')
add_if_absent('AKIN', [('A', 'Acute'), ('K', 'Kidney'), ('I', 'Injury'), ('N', 'Network')], 'Acute Kidney Injury Network',
              'Réseau dont la classification qualifie la gravité d’une hausse de créatinine ; le stade 1 signale une hausse de créatinine sous bloqueur du SRA.', 'n27-signes')
add_if_absent('ASC', [('A', 'Aire'), ('S', 'Sous la'), ('C', 'Courbe')], 'Aire sous la courbe',
              'Mesure de la capacité d’un score à discriminer ; 0,829 pour le score échographique cité.', 'n27-echo')
add_if_absent('CT', [('C', 'Computed (calculée)'), ('T', 'Tomography (tomographie)')], 'Tomodensitométrie',
              'Scanner utilisé pour l’angiographie rénale quand le DFG dépasse 60 ml/min/1,73 m².', 'n27-echo')
add_if_absent('angio-CT', [('angio', 'angiographie'), ('CT', 'Computed Tomography (par scanner)')], 'Angiographie par tomodensitométrie',
              'Technique d’imagerie de l’artère rénale, possible si le DFG dépasse 60.', 'n27-echo')
add_if_absent('Angio-CT', [('Angio', 'angiographie'), ('CT', 'Computed Tomography (par scanner)')], 'Angiographie par tomodensitométrie',
              'Technique d’imagerie de l’artère rénale, possible si le DFG dépasse 60.', 'n27-echo')
add_if_absent('anti-PLA2R', [('anti', 'anticorps dirigés contre'), ('PLA2R', 'Phospholipase A2 Receptor (récepteur de la phospholipase A2)')], 'Anticorps anti-récepteur de la phospholipase A2',
              'Sérologie ciblée selon le contexte glomérulaire.', 'n27-mrc')
add_if_absent('anti-MBG', [('anti', 'anticorps dirigés contre'), ('MBG', 'Membrane Basale Glomérulaire')], 'Anticorps anti-membrane basale glomérulaire',
              'Sérologie ciblée selon le contexte glomérulaire.', 'n27-mrc')
add_if_absent('N27.0', [('N27.0', 'code CIM-10-GM, non une abréviation')], 'Petit rein unilatéral',
              'Code CIM-10-GM 2024 du petit rein unilatéral de cause inconnue.', 'n27-cim')
add_if_absent('N27.1', [('N27.1', 'code CIM-10-GM, non une abréviation')], 'Petit rein bilatéral',
              'Code CIM-10-GM 2024 du petit rein bilatéral de cause inconnue.', 'n27-cim')
add_if_absent('N27.9', [('N27.9', 'code CIM-10-GM, non une abréviation')], 'Petit rein, sans précision',
              'Code CIM-10-GM 2024 du petit rein de cause inconnue sans précision de latéralité.', 'n27-cim')
add_if_absent('Ask-Upmark', [('Ask-Upmark', 'noms propres des auteurs de la description, non une abréviation')], 'Rein d’Ask-Upmark',
              'Hypoplasie segmentaire du rein, décrite comme congénitale ou comme séquelle de reflux, qui provoque une hypertension chez le sujet jeune.', 'n27-askupmark')
add_if_absent('Sanofi-Aventis', [('Sanofi-Aventis', 'nom propre d’entreprise, non une abréviation')], 'Sanofi-Aventis Suisse',
              'Titulaire de l’information professionnelle suisse de Triatec® (ramipril).', 'n27-ramipril')
