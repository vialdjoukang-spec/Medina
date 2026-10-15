"""Abréviations C77 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'c77', '__init__'}:
        continue
    _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
G = {}
def add_if_absent(key, letters, full, definition, window):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full, 'def': '<p>' + definition + '</p>', 'ref': window}

_CODE = 'code de la classification CIM-10-GM 2024, non développable lettre à lettre'
for _k, _d in [
    ('C77.0', 'Ganglions lymphatiques de la tête, de la face et du cou, y compris sus-claviculaires.'),
    ('C77.1', 'Ganglions lymphatiques intrathoraciques.'),
    ('C77.2', 'Ganglions lymphatiques intra-abdominaux.'),
    ('C77.3', 'Ganglions lymphatiques de l’aisselle et du membre supérieur.'),
    ('C77.4', 'Ganglions lymphatiques inguinaux et du membre inférieur.'),
    ('C77.5', 'Ganglions lymphatiques intrapelviens.'),
    ('C77.8', 'Ganglions lymphatiques de sièges multiples.'),
    ('C77.9', 'Ganglion lymphatique sans précision.'),
    ('C80.0', 'Tumeur maligne de localisation primitive inconnue, ainsi désignée.'),
    ('C80.9', 'Tumeur maligne sans précision.')]:
    add_if_absent(_k, [(_k, _CODE)], 'Code ' + _k, _d, 'c77-codage')

add_if_absent('CUP', [('C', 'Cancer'), ('U', 'of Unknown'), ('P', 'Primary (primitif)')], 'Cancer of unknown primary (tumeur de primitif inconnu)', 'Tumeur maligne confirmée par l’histologie ou la cytologie dont l’origine reste inconnue après un bilan de base standardisé et un bilan étendu (Onkopedia 2025).', 'c77-cup')
add_if_absent('CT', [('C', 'Computed (assistée par ordinateur)'), ('T', 'Tomography (tomographie)')], 'Tomodensitométrie (scanner)', 'Examen d’imagerie en coupes par rayons X. Dans « TEP-CT », il est couplé à la tomographie par émission de positons.', 'c77-tep')
add_if_absent('NGS', [('N', 'Next'), ('G', 'Generation (nouvelle génération)'), ('S', 'Sequencing (séquençage)')], 'Séquençage de nouvelle génération', 'Analyse simultanée de plusieurs gènes de la tumeur. L’ESMO la propose en routine pour le CUP ; le résultat est discuté en comité moléculaire.', 'c77-ngs')
add_if_absent('TMB', [('T', 'Tumor (tumorale)'), ('M', 'Mutational (mutationnelle)'), ('B', 'Burden (charge)')], 'Charge mutationnelle tumorale', 'Nombre de mutations de la tumeur. Une charge élevée ou un statut MSI/dMMR fait discuter une immunothérapie dans les formes défavorables du CUP.', 'c77-immuno')
add_if_absent('FNA', [('F', 'Fine (fine)'), ('N', 'Needle (aiguille)'), ('A', 'Aspiration (aspiration)')], 'Cytoponction à l’aiguille fine', 'Prélèvement de cellules par aiguille fine. Sensibilité de 56 % et valeur prédictive négative de 72 % dans la revue suisse de 2024.', 'c77-fna')
add_if_absent('CNB', [('C', 'Core (carotte)'), ('N', 'Needle (aiguille)'), ('B', 'Biopsy (biopsie)')], 'Biopsie à l’aiguille tranchante (au trocart)', 'Prélèvement d’une carotte de tissu de 16 à 18 G qui conserve l’architecture du ganglion.', 'c77-cnb')
add_if_absent('HPV', [('H', 'Human (humain)'), ('P', 'Papilloma (du papillome)'), ('V', 'Virus')], 'Virus du papillome humain', 'Sa présence, avec une positivité de p16, oriente vers l’oropharynx dans le CUP cervical et indique un meilleur pronostic.', 'c77-hpv')
add_if_absent('EBV', [('E', 'Epstein'), ('B', 'Barr'), ('V', 'Virus')], 'Virus d’Epstein-Barr', 'Un carcinome lié à ce virus oriente vers le nasopharynx dans le CUP cervical.', 'c77-hpv')
add_if_absent('EHNS', [('E', 'European'), ('H', 'Head and'), ('N', 'Neck'), ('S', 'Society (société européenne de la tête et du cou)')], 'European Head and Neck Society', 'Société savante coauteure de la ligne directrice EHNS-ESMO-ESTRO 2020, identifiée mais non lue en texte intégral.', 'c77-sources')
add_if_absent('GTIN', [('G', 'Global'), ('T', 'Trade'), ('I', 'Item'), ('N', 'Number (numéro d’article commercial)')], 'Global Trade Item Number', 'Identifiant commercial qui désigne l’emballage d’un médicament dans les bases de données d’informations professionnelles.', 'c77-carboplatine')
add_if_absent('ICD-10-GM', [('ICD', 'International Classification of Diseases (classification internationale des maladies)'), ('10', 'dixième révision'), ('GM', 'German Modification (modification allemande)')], 'Classification internationale des maladies, 10e révision, modification allemande', 'Version allemande de la classification internationale des maladies, dont l’Office fédéral de la statistique publie la version française (CIM-10-GM).', 'c77-codage')
add_if_absent('ER', [('E', 'Estrogen (des œstrogènes)'), ('R', 'Receptor (récepteur)')], 'Récepteur des œstrogènes', 'Marqueur d’immunohistochimie du sein dans le profil CK7 positif et CK20 négatif.', 'c77-ihc')
add_if_absent('hCG', [('h', 'human (humaine)'), ('CG', 'Chorionic Gonadotropin (gonadotrophine chorionique)')], 'Gonadotrophine chorionique humaine', 'Marqueur sérique dosé, dans sa sous-unité bêta, avec l’AFP et le PSA chez l’homme dans le bilan du CUP.', 'c77-diffdx')
add_if_absent('PSA', [('P', 'Prostate'), ('S', 'Specific (spécifique)'), ('A', 'Antigen (antigène)')], 'Antigène spécifique de la prostate', 'Protéine dosée dans le sang chez l’homme dans le bilan du CUP, et recherchée par immunohistochimie.', 'c77-diffdx')
add_if_absent('PSMA', [('P', 'Prostate'), ('S', 'Specific (spécifique)'), ('M', 'Membrane (de membrane)'), ('A', 'Antigen (antigène)')], 'Antigène membranaire spécifique de la prostate', 'Marqueur d’immunohistochimie du cancer de la prostate.', 'c77-ihc')
add_if_absent('CK7', [('CK', 'Cytokératine'), ('7', 'numéro 7')], 'Cytokératine 7', 'Marqueur d’immunohistochimie dont l’association à la cytokératine 20 oriente l’organe d’origine d’un carcinome.', 'c77-ihc')
add_if_absent('CK20', [('CK', 'Cytokératine'), ('20', 'numéro 20')], 'Cytokératine 20', 'Marqueur d’immunohistochimie, lu avec la cytokératine 7 pour orienter l’organe d’origine d’un carcinome.', 'c77-ihc')
add_if_absent('AE1', [('AE1', 'nom d’un clone d’anticorps, non développable lettre à lettre')], 'Anticorps AE1', 'Associé à l’anticorps AE3 sous la forme AE1/AE3, il détecte les cytokératines et signe un carcinome.', 'c77-ihc')
add_if_absent('AE3', [('AE3', 'nom d’un clone d’anticorps, non développable lettre à lettre')], 'Anticorps AE3', 'Associé à l’anticorps AE1 sous la forme AE1/AE3 : pan-cytokératine, marqueur de carcinome.', 'c77-ihc')
add_if_absent('CD10', [('CD', 'Cluster of Differentiation (groupe de différenciation)'), ('10', 'numéro 10')], 'Antigène CD10', 'Marqueur d’immunohistochimie retenu avec PAX8 et PAX2 pour l’origine rénale.', 'c77-ihc')
add_if_absent('CD79a', [('CD', 'Cluster of Differentiation (groupe de différenciation)'), ('79a', 'numéro 79a')], 'Antigène CD79a', 'Marqueur de la lignée B, cité avec CD3, CD20 et CD30 dans l’exploration d’une hémopathie.', 'c77-ihc')
add_if_absent('CDX2', [('CDX2', 'Caudal-type homeobox 2 (gène homéotique de type caudal 2)')], 'Facteur de transcription CDX2', 'Marqueur d’immunohistochimie, avec SATB2, d’une origine colorectale.', 'c77-ihc')
add_if_absent('SATB2', [('SATB2', 'Special AT-rich sequence-Binding protein 2 (protéine 2 de liaison aux séquences riches en AT)')], 'Protéine SATB2', 'Marqueur d’immunohistochimie, avec CDX2, d’une origine colorectale.', 'c77-ihc')
add_if_absent('GATA3', [('GATA', 'séquence d’ADN reconnue (G, A, T, A)'), ('3', 'membre 3 de la famille')], 'Facteur de transcription GATA3', 'Marqueur d’immunohistochimie du sein et de la vessie.', 'c77-ihc')
add_if_absent('TTF1', [('T', 'Thyroid (thyroïdien)'), ('T', 'Transcription'), ('F', 'Factor (facteur)'), ('1', 'numéro 1')], 'Facteur de transcription thyroïdien 1', 'Marqueur d’immunohistochimie du poumon et de la thyroïde.', 'c77-ihc')
add_if_absent('PAX8', [('PAX', 'Paired box (boîte appariée)'), ('8', 'numéro 8')], 'Facteur de transcription PAX8', 'Marqueur d’immunohistochimie des voies müllériennes, de la thyroïde et du rein.', 'c77-ihc')
add_if_absent('PAX2', [('PAX', 'Paired box (boîte appariée)'), ('2', 'numéro 2')], 'Facteur de transcription PAX2', 'Marqueur d’immunohistochimie du rein.', 'c77-ihc')
add_if_absent('WT1', [('W', 'Wilms'), ('T', 'Tumor (tumeur)'), ('1', 'numéro 1')], 'Protéine WT1 de la tumeur de Wilms', 'Marqueur d’immunohistochimie des voies müllériennes, avec PAX8.', 'c77-ihc')
add_if_absent('NKX3.1', [('NKX3.1', 'NK3 homeobox 1 (gène homéotique NK3, numéro 1)')], 'Facteur de transcription NKX3.1', 'Marqueur d’immunohistochimie de la prostate.', 'c77-ihc')
add_if_absent('SOX10', [('SOX', 'SRY-related HMG-box (boîte HMG apparentée à SRY)'), ('10', 'numéro 10')], 'Facteur de transcription SOX10', 'Marqueur d’immunohistochimie du mélanome.', 'c77-ihc')
add_if_absent('S100', [('S100', 'protéine S100, nom lié à sa solubilité ; non développable lettre à lettre')], 'Protéine S100', 'Marqueur d’immunohistochimie du mélanome.', 'c77-ihc')
add_if_absent('Melan-A', [('Melan-A', 'antigène des mélanocytes, nom propre non développable lettre à lettre')], 'Antigène Melan-A', 'Marqueur d’immunohistochimie du mélanome.', 'c77-ihc')
add_if_absent('HMB45', [('HMB45', 'nom d’un anticorps antimélanome, non développable lettre à lettre')], 'Anticorps HMB45', 'Marqueur d’immunohistochimie du mélanome.', 'c77-ihc')
add_if_absent('SALL4', [('SALL', 'Spalt-Like (apparenté à Spalt)'), ('4', 'numéro 4')], 'Facteur de transcription SALL4', 'Marqueur d’immunohistochimie des tumeurs germinales.', 'c77-ihc')
add_if_absent('OCT3', [('OCT', 'Octamer-binding Transcription factor (facteur de transcription se liant à l’octamère)'), ('3', 'numéro 3, dans la forme OCT3/4')], 'Facteur de transcription OCT3/4', 'Marqueur d’immunohistochimie des tumeurs germinales.', 'c77-ihc')
add_if_absent('INSM1', [('INSM', 'INSulinoMa-associated (associé à l’insulinome)'), ('1', 'numéro 1')], 'Protéine INSM1', 'Marqueur d’immunohistochimie des tumeurs neuroendocrines, avec la synaptophysine.', 'c77-ihc')
add_if_absent('CCL21', [('CC', 'chimiokine à motif C-C'), ('L', 'Ligand'), ('21', 'numéro 21')], 'Chimiokine CCL21', 'Produite par l’endothélium lymphatique, elle attire les cellules tumorales qui portent CCR7.', 'c77-ccl21')
add_if_absent('CCR7', [('CC', 'chimiokine à motif C-C'), ('R', 'Receptor (récepteur)'), ('7', 'numéro 7')], 'Récepteur CCR7', 'Récepteur des cellules tumorales qui répond à CCL21.', 'c77-ccl21')
add_if_absent('NCI', [('N', 'National (national)'), ('C', 'Cancer (du cancer)'), ('I', 'Institute (institut)')], 'National Cancer Institute', 'Institut national du cancer des États-Unis ; son programme SEER a produit le schéma original des régions ganglionnaires utilisé en figure 1 des Sciences.', 'c77-drainage')
add_if_absent('FGFR2', [('F', 'Fibroblast (des fibroblastes)'), ('G', 'Growth (croissance)'), ('F', 'Factor (facteur)'), ('R', 'Receptor (récepteur)'), ('2', 'numéro 2')], 'Récepteur 2 du facteur de croissance des fibroblastes', 'Récepteur à activité tyrosine kinase ; une fusion du gène FGFR2 est une altération ciblable citée parmi les CUP les plus favorables à une thérapie guidée (Onkopedia 2025).', 'c77-ngs')
add_if_absent('p.G12C', [('p.', 'protéine (notation de la variation au niveau protéique)'), ('G', 'Glycine (acide aminé d’origine)'), ('12', 'position 12 de la protéine'), ('C', 'Cystéine (acide aminé de remplacement)')], 'Variant KRAS p.G12C', 'Mutation du gène KRAS qui remplace la glycine en position 12 par une cystéine ; Onkopedia 2025 la range parmi les altérations ciblables plus rares du CUP.', 'c77-ngs')
