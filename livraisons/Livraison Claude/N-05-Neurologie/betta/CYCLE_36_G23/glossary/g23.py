"""Abréviations G23 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib, sys
_here = Path(__file__).resolve().parent
_dirs = [_here] + [p / 'glossary' for p in _here.parents if (p / 'glossary' / 'cardio_1.py').exists()]
_gdir = next((d for d in _dirs if (d / 'cardio_1.py').exists()), _here)
if str(_gdir) not in sys.path:
    sys.path.insert(0, str(_gdir))
_existing = {}
for _path in sorted(_gdir.glob('*.py')):
    if _path.stem in {'g23', '__init__'}:
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
add_if_absent('AADvac1', [('AADvac1', 'nom de code d’un candidat médicament, non développable lettre à lettre')], 'AADvac1, candidat médicament cité dans la revue de Munich',
              'Candidat thérapeutique en essai dans la paralysie supranucléaire progressive et la dégénérescence corticobasale ; aucune approbation.', 'g23-essais')
add_if_absent('AMS', [('A', 'Atrophie'), ('M', 'Multi'), ('S', 'Systématisée')], 'Atrophie multisystématisée',
              'Maladie neurodégénérative sporadique de l’adulte de plus de 30 ans, caractérisée par des inclusions oligodendrogliales d’α-synucléine, qui associe parkinsonisme, syndrome cérébelleux et dysautonomie.', 'g23-ams')
add_if_absent('AMS-P', [('AMS', 'Atrophie multisystématisée'), ('P', 'forme Parkinson')], 'Atrophie multisystématisée de forme Parkinson (G23.2)',
              'Forme où le parkinsonisme domine ; elle prédomine en Europe.', 'g23-ams')
add_if_absent('AMS-C', [('AMS', 'Atrophie multisystématisée'), ('C', 'forme cérébelleuse')], 'Atrophie multisystématisée de forme cérébelleuse (G23.3)',
              'Forme où le syndrome cérébelleux domine ; elle atteint jusqu’à 73 % des cas en Asie de l’Est.', 'g23-ams')
add_if_absent('AZP2006', [('AZP2006', 'nom de code d’un candidat médicament, non développable lettre à lettre')], 'AZP2006, candidat médicament cité dans la revue de Munich',
              'Molécule en essai dans la paralysie supranucléaire progressive et la dégénérescence corticobasale ; aucune approbation.', 'g23-essais')
add_if_absent('CC1', [('CC1', 'code de l’indice clinique de soutien « résistance à la lévodopa » des critères MDS 2017')], 'Indice clinique de soutien CC1 de la PSP',
              'Résistance à la lévodopa : amélioration de 30 % ou moins du score moteur.', 'g23-psp-criteres')
add_if_absent('CC2', [('CC2', 'code de l’indice clinique de soutien « dysarthrie hypokinétique spastique » des critères MDS 2017')], 'Indice clinique de soutien CC2 de la PSP',
              'Dysarthrie hypokinétique spastique.', 'g23-psp-criteres')
add_if_absent('CC3', [('CC3', 'code de l’indice clinique de soutien « dysphagie » des critères MDS 2017')], 'Indice clinique de soutien CC3 de la PSP',
              'Dysphagie.', 'g23-psp-criteres')
add_if_absent('CC4', [('CC4', 'code de l’indice clinique de soutien « photophobie » des critères MDS 2017')], 'Indice clinique de soutien CC4 de la PSP',
              'Photophobie.', 'g23-psp-criteres')
add_if_absent('CIM', [('C', 'Classification'), ('I', 'Internationale des'), ('M', 'Maladies')], 'Classification internationale des maladies',
              'Classification de l’Organisation mondiale de la santé ; ce chapitre utilise la version CIM-10-GM 2024.', 'g23-cim')
add_if_absent('CMPK2', [('CMPK2', 'symbole de gène : Cytidine/uridine MonoPhosphate Kinase 2')], 'Gène CMPK2',
              'Un des trois gènes récessifs de la calcification cérébrale primaire familiale.', 'g23-pfbc-meca')
add_if_absent('DCB', [('D', 'Dégénérescence'), ('C', 'Cortico'), ('B', 'Basale')], 'Dégénérescence corticobasale',
              'Tauopathie 4R primaire ; terme de diagnostic neuropathologique, dont le tableau clinique est le syndrome corticobasal.', 'g23-dcb')
add_if_absent('DMFP', [('DMFP', 'DesMéthoxyFallyPride, traceur d’imagerie dopaminergique post-synaptique en TEP')], 'Desméthoxyfallypride',
              'Traceur utilisé en TEP pour explorer la voie dopaminergique post-synaptique.', 'g23-imagerie-fonctionnelle')
add_if_absent('EAN', [('E', 'European'), ('A', 'Academy of'), ('N', 'Neurology')], 'European Academy of Neurology (Académie européenne de neurologie)',
              'Société savante européenne de neurologie ; une ligne directrice conjointe est annoncée comme en cours.', None)
add_if_absent('ERN-RND', [('ERN', 'European Reference Network'), ('RND', 'Rare Neurological Diseases')], 'Réseau européen de référence pour les maladies neurologiques rares',
              'Réseau dont une ligne directrice sur le traitement symptomatique de l’AMS et de la PSP est annoncée comme en cours.', None)
add_if_absent('FMR1', [('FMR1', 'symbole de gène : Fragile X Messenger Ribonucleoprotein 1')], 'Gène FMR1',
              'Gène recherché chez certains patients ataxiques.', 'g23-genetique-examens')
add_if_absent('FNP-223', [('FNP-223', 'nom de code d’un candidat médicament, non développable lettre à lettre')], 'FNP-223, candidat médicament cité dans la revue de Munich',
              'Molécule en essai dans la paralysie supranucléaire progressive et la dégénérescence corticobasale ; aucune approbation.', 'g23-essais')
add_if_absent('G23.0', [('G23', 'catégorie CIM-10-GM : autres maladies dégénératives des noyaux gris centraux'), ('.0', 'sous-code : maladie de Hallervorden-Spatz')], 'Code CIM-10-GM G23.0',
              'Neurodégénérescence avec accumulation cérébrale de fer, surtout la PKAN.', 'g23-cim')
add_if_absent('G23.1', [('G23', 'catégorie CIM-10-GM'), ('.1', 'sous-code : ophtalmoplégie supranucléaire progressive')], 'Code CIM-10-GM G23.1',
              'Paralysie supranucléaire progressive.', 'g23-cim')
add_if_absent('G23.2', [('G23', 'catégorie CIM-10-GM'), ('.2', 'sous-code : atrophie multisystématisée de forme Parkinson')], 'Code CIM-10-GM G23.2',
              'Atrophie multisystématisée, forme parkinsonienne.', 'g23-cim')
add_if_absent('G23.3', [('G23', 'catégorie CIM-10-GM'), ('.3', 'sous-code : atrophie multisystématisée de forme cérébelleuse')], 'Code CIM-10-GM G23.3',
              'Atrophie multisystématisée, forme cérébelleuse.', 'g23-cim')
add_if_absent('G23.8', [('G23', 'catégorie CIM-10-GM'), ('.8', 'sous-code : autres maladies dégénératives précisées')], 'Code CIM-10-GM G23.8',
              'Inclut la calcification des noyaux gris centraux et l’hypotension orthostatique neurogène ; rattachement de la dégénérescence corticobasale non vérifié.', 'g23-cim')
add_if_absent('G23.9', [('G23', 'catégorie CIM-10-GM'), ('.9', 'sous-code : sans précision')], 'Code CIM-10-GM G23.9',
              'Maladie dégénérative des noyaux gris centraux, sans précision.', 'g23-cim')
add_if_absent('Hallervorden-Spatz', [('Hallervorden-Spatz', 'noms propres de deux neurologues, éponyme historique')], 'Maladie de Hallervorden-Spatz',
              'Dénomination historique du code G23.0, aujourd’hui regroupée dans les NBIA, surtout la PKAN.', 'g23-nbia')
add_if_absent('IBZM', [('IBZM', 'IodoBenZaMide, traceur d’imagerie dopaminergique post-synaptique en tomographie monophotonique')], 'Iodobenzamide',
              'Traceur utilisé en tomographie par émission monophotonique pour explorer la voie dopaminergique post-synaptique.', 'g23-imagerie-fonctionnelle')
add_if_absent('IF1', [('IF1', 'code de l’indice d’imagerie « atrophie ou hypométabolisme mésencéphalique » des critères MDS 2017')], 'Indice d’imagerie IF1 de la PSP',
              'Atrophie ou hypométabolisme mésencéphalique prédominant par rapport au pont.', 'g23-psp-criteres')
add_if_absent('IF2', [('IF2', 'code de l’indice d’imagerie « dégénérescence dopaminergique striatale post-synaptique » des critères MDS 2017')], 'Indice d’imagerie IF2 de la PSP',
              'Dégénérescence dopaminergique striatale post-synaptique.', 'g23-post-synaptique')
add_if_absent('JAM2', [('JAM2', 'symbole de gène : Junctional Adhesion Molecule 2')], 'Gène JAM2',
              'Un des trois gènes récessifs de la calcification cérébrale primaire familiale.', 'g23-pfbc-meca')
add_if_absent('LIQ', [('LIQ', 'suffixe de nom commercial (forme liquide de Madopar®), non une abréviation')], 'Madopar LIQ',
              'Forme liquide de Madopar®, indiquée en cas de dysphagie.', 'g23-madopar')
add_if_absent('MDS', [('M', 'Movement'), ('D', 'Disorder'), ('S', 'Society')], 'International Parkinson and Movement Disorder Society (Société internationale de la maladie de Parkinson et des troubles du mouvement)',
              'Société savante qui a publié les critères de la PSP (2017) et de l’AMS (2022).', 'g23-ams-criteres')
add_if_absent('MDS-ES', [('MDS', 'Movement Disorder Society'), ('ES', 'European Section')], 'Section européenne de la Movement Disorder Society',
              'Section citée avec l’ERN-RND et l’EAN pour une ligne directrice annoncée comme en cours.', None)
add_if_absent('MDS-UPDRS', [('MDS', 'Movement Disorder Society'), ('U', 'Unified'), ('P', 'Parkinson’s'), ('D', 'Disease'), ('RS', 'Rating Scale')], 'Échelle unifiée d’évaluation de la maladie de Parkinson de la Movement Disorder Society',
              'La partie III mesure le syndrome moteur ; une amélioration inférieure à 30 % sous lévodopa définit un parkinsonisme peu dopa-sensible dans l’AMS.', 'g23-levodopa-reponse')
add_if_absent('MIBG', [('M', 'Méta'), ('I', 'Iodo'), ('B', 'Benzyl'), ('G', 'Guanidine')], 'Méta-iodobenzylguanidine',
              'Traceur de la scintigraphie cardiaque qui explore l’innervation sympathique post-ganglionnaire ; habituellement normale dans l’AMS.', 'g23-preganglionnaire')
add_if_absent('MYORG', [('MYORG', 'symbole de gène : MYOgenesis-Regulating Glycosidase')], 'Gène MYORG',
              'Un des trois gènes récessifs de la calcification cérébrale primaire familiale.', 'g23-pfbc-meca')
add_if_absent('NBIA', [('N', 'Neurodegeneration (neurodégénérescence)'), ('B', 'with Brain'), ('I', 'Iron'), ('A', 'Accumulation')], 'Neurodégénérescence avec accumulation cérébrale de fer',
              'Groupe de maladies génétiques rares avec fer dans les noyaux gris centraux ; la PKAN en est la forme la plus fréquente.', 'g23-nbia')
add_if_absent('NfL', [('N', 'Neuro'), ('f', 'filament'), ('L', 'Light chain (chaîne légère)')], 'Chaîne légère des neurofilaments',
              'Protéine mesurée dans le liquide cérébrospinal ; plus de 1400 pg/mL distinguent l’AMS des maladies à corps de Lewy.', 'g23-biomarqueurs')
add_if_absent('Niemann-Pick', [('Niemann-Pick', 'noms propres de deux médecins, éponyme historique')], 'Maladie de Niemann-Pick de type C',
              'Maladie à rechercher devant un tableau de PSP avant 45 ans.', 'g23-psp-criteres')
add_if_absent('NIO752', [('NIO752', 'nom de code d’un candidat médicament, non développable lettre à lettre')], 'NIO752, candidat médicament cité dans la revue de Munich',
              'Molécule en essai dans la paralysie supranucléaire progressive et la dégénérescence corticobasale ; aucune approbation.', 'g23-essais')
add_if_absent('O-1', [('O', 'Oculomoteur'), ('-1', 'niveau 1 : paralysie supranucléaire verticale')], 'Niveau O-1 des critères MDS 2017',
              'Paralysie supranucléaire verticale.', 'g23-psp-criteres')
add_if_absent('O-2', [('O', 'Oculomoteur'), ('-2', 'niveau 2 : saccades verticales lentes')], 'Niveau O-2 des critères MDS 2017',
              'Saccades verticales lentes.', 'g23-psp-criteres')
add_if_absent('O-3', [('O', 'Oculomoteur'), ('-3', 'niveau 3 : ondes carrées fréquentes ou apraxie d’ouverture des paupières')], 'Niveau O-3 des critères MDS 2017',
              'Ondes carrées fréquentes ou apraxie d’ouverture des paupières.', 'g23-psp-criteres')
add_if_absent('PANK2', [('PANK2', 'symbole de gène : PANtothénate Kinase 2')], 'Gène PANK2',
              'Gène d’une pantothénate kinase mitochondriale, impliqué dans la PKAN.', 'g23-pkan-meca')
add_if_absent('PDGFB', [('PDGFB', 'symbole de gène : Platelet-Derived Growth Factor subunit B')], 'Gène PDGFB',
              'Un des quatre gènes dominants de la calcification cérébrale primaire familiale.', 'g23-pfbc-meca')
add_if_absent('PDGFRB', [('PDGFRB', 'symbole de gène : Platelet-Derived Growth Factor Receptor Beta')], 'Gène PDGFRB',
              'Un des quatre gènes dominants de la calcification cérébrale primaire familiale.', 'g23-pfbc-meca')
add_if_absent('PFBC', [('P', 'Primary'), ('F', 'Familial'), ('B', 'Brain'), ('C', 'Calcification')], 'Calcification cérébrale primaire familiale',
              'Calcifications bilatérales des noyaux gris centraux, ancienne « maladie de Fahr ».', 'g23-pfbc')
add_if_absent('PK-Merz', [('PK-Merz', 'nom commercial du sulfate d’amantadine en Suisse, non une abréviation')], 'PK-Merz® (sulfate d’amantadine)',
              'Spécialité suisse d’amantadine.', 'g23-pkmerz')
add_if_absent('PKAN', [('P', 'Pantothenate'), ('K', 'Kinase-'), ('A', 'Associated'), ('N', 'Neurodegeneration')], 'Neurodégénérescence associée à la pantothénate kinase',
              'Forme la plus fréquente de NBIA, liée au gène PANK2.', 'g23-nbia')
add_if_absent('PMCA', [('P', 'Protein'), ('M', 'Misfolding'), ('C', 'Cyclic'), ('A', 'Amplification')], 'Amplification cyclique des protéines mal repliées',
              'Test d’amplification de l’α-synucléine dont la cinétique est particulière dans l’AMS.', 'g23-biomarqueurs')
add_if_absent('PSP', [('P', 'Paralysie'), ('S', 'Supranucléaire'), ('P', 'Progressive')], 'Paralysie supranucléaire progressive',
              'Tauopathie 4R dont le diagnostic définitif est neuropathologique.', 'g23-psp')
add_if_absent('PSP-CBS', [('PSP', 'Paralysie supranucléaire progressive'), ('CBS', 'Corticobasal Syndrome (syndrome corticobasal)')], 'Phénotype PSP à syndrome corticobasal',
              'Phénotype possible de PSP (O-1 ou O-2 avec C-3).', 'g23-phenotypes-psp')
add_if_absent('PSP-CDS', [('PSP', 'Paralysie supranucléaire progressive'), ('CDS', 'Clinical Deficits Scale (échelle de déficits cliniques)')], 'Échelle de déficits cliniques de la PSP',
              'Échelle de suivi cotée de 0 à 3 par domaine.', 'g23-phenotypes-psp')
add_if_absent('PSP-F', [('PSP', 'Paralysie supranucléaire progressive'), ('F', 'Frontal')], 'Phénotype PSP à présentation frontale',
              'Phénotype probable de PSP (O-1 ou O-2 avec C-2).', 'g23-phenotypes-psp')
add_if_absent('PSP-OM', [('PSP', 'Paralysie supranucléaire progressive'), ('OM', 'Ocular Motor (oculomoteur)')], 'Phénotype PSP à prédominance oculomotrice',
              'Phénotype possible de PSP (O-1 seul).', 'g23-phenotypes-psp')
add_if_absent('PSP-P', [('PSP', 'Paralysie supranucléaire progressive'), ('P', 'Parkinsonisme')], 'Phénotype PSP à prédominance parkinsonienne',
              'Phénotype probable de PSP (O-1 ou O-2 avec A-2 ou A-3).', 'g23-phenotypes-psp')
add_if_absent('PSP-PGF', [('PSP', 'Paralysie supranucléaire progressive'), ('PGF', 'Progressive Gait Freezing (freezing progressif de la marche)')], 'Phénotype PSP à freezing progressif de la marche',
              'Phénotype de PSP (O-1 ou O-2 avec A-1).', 'g23-phenotypes-psp')
add_if_absent('PSP-QoL', [('PSP', 'Paralysie supranucléaire progressive'), ('QoL', 'Quality of Life (qualité de vie)')], 'Échelle de qualité de vie de la PSP',
              'Échelle de suivi de la PSP.', 'g23-phenotypes-psp')
add_if_absent('PSP-RS', [('PSP', 'Paralysie supranucléaire progressive'), ('RS', 'Richardson’s Syndrome (syndrome de Richardson)')], 'Phénotype PSP de Richardson',
              'Chutes en arrière précoces et paralysie verticale du regard.', 'g23-phenotypes-psp')
add_if_absent('PSP-SL', [('PSP', 'Paralysie supranucléaire progressive'), ('SL', 'Speech/Language (parole et langage)')], 'Phénotype PSP à troubles de la parole et du langage',
              'Phénotype possible de PSP (O-1 ou O-2 avec C-1).', 'g23-phenotypes-psp')
add_if_absent('R2', [('R', 'Relaxation'), ('2*', 'transversale apparente')], 'Taux de relaxation transversale apparent R2*',
              'Séquence sensible au fer utilisée pour les NBIA.', 'g23-irm')
add_if_absent('RT-QuIC', [('RT', 'Real-Time (en temps réel)'), ('QuIC', 'Quaking-Induced Conversion (conversion induite par agitation)')], 'Conversion induite par agitation en temps réel',
              'Test d’amplification de l’α-synucléine dont la cinétique est particulière dans l’AMS.', 'g23-biomarqueurs')
add_if_absent('SCB', [('S', 'Syndrome'), ('C', 'Cortico'), ('B', 'Basal')], 'Syndrome corticobasal',
              'Tableau clinique asymétrique associant signes corticaux et sous-corticaux ; il peut relever de plusieurs pathologies.', 'g23-scb-criteres')
add_if_absent('Shy-Drager', [('Shy-Drager', 'noms propres de deux médecins, éponyme historique')], 'Syndrome de Shy-Drager',
              'Dénomination historique de l’hypotension orthostatique neurogène ; assimilé à l’AMS.', 'g23-cim')
add_if_absent('SLC20A2', [('SLC20A2', 'symbole de gène : SoLute Carrier family 20 member A2')], 'Gène SLC20A2',
              'Un des quatre gènes dominants de la calcification cérébrale primaire familiale.', 'g23-pfbc-meca')
add_if_absent('Steele-Richardson-Olszewski', [('Steele-Richardson-Olszewski', 'noms propres de trois médecins, éponyme historique')], 'Syndrome de Steele-Richardson-Olszewski',
              'Dénomination historique de la PSP, présente dans le libellé de G23.1.', 'g23-cim')
add_if_absent('SWI', [('S', 'Susceptibility'), ('W', 'Weighted'), ('I', 'Imaging')], 'Imagerie pondérée en susceptibilité magnétique',
              'Séquence d’IRM sensible au fer.', 'g23-irm')
add_if_absent('TDP-43', [('T', 'TAR'), ('DP', 'DNA-binding Protein'), ('43', '43 kilodaltons')], 'Protéine TDP-43',
              'Pathologie rare qui peut sous-tendre un syndrome corticobasal.', 'g23-dcb')
add_if_absent('TIRCON', [('TIRCON', 'nom d’essai : Treat Iron-Related Childhood-Onset Neurodegeneration')], 'Essai TIRCON',
              'Essai randomisé de la défériprone dans la PKAN.', 'g23-tircon')
add_if_absent('XPR1', [('XPR1', 'symbole de gène : Xenotropic and Polytropic retrovirus Receptor 1')], 'Gène XPR1',
              'Un des quatre gènes dominants de la calcification cérébrale primaire familiale.', 'g23-pfbc-meca')
