from cardio_1 import a, G
# C96 — Tumeurs malignes des tissus lymphoïde, hématopoïétique et apparentés, autres et non précisées (H-08-Hématologie). Entrées conditionnelles : aucun terme existant dans G n’est écrasé.
def d(k, lit, full, df, ref=None):
    if k not in G:
        a(k, lit, full, '<p>' + df + '</p>', ref)

def code(k, full, df, ref='c96-categorie'):
    d(k, [(k, 'code de la CIM-10-GM 2024 ; ce code n’est pas développable lettre à lettre')], full, df, ref)

def nom(k, full, df, ref=None):
    d(k, [(k, 'nom propre ou nom de marqueur ; non développable lettre à lettre')], full, df, ref)

code('C96.0', 'Histiocytose à cellules de Langerhans multifocale et multisystémique (C96.0)', 'Sous-catégorie de C96 pour l’histiocytose à cellules de Langerhans atteignant plusieurs systèmes ; inclut la maladie d’Abt-Letterer-Siwe.')
code('C96.1', 'Code C96.1, inexistant dans la CIM-10-GM 2024', 'Ce code n’existe pas dans la version 2024.')
code('C96.2', 'Tumeur maligne à mastocytes (C96.2)', 'Sous-catégorie de C96 pour la mastocytose systémique agressive et le sarcome mastocytaire. La forme indolente (D47.0) et la leucémie à mastocytes (C94.3-) en sont exclues.')
code('C96.3', 'Code C96.3, inexistant dans la CIM-10-GM 2024', 'Ce code n’existe pas dans la version 2024.')
code('C96.4', 'Sarcome à cellules dendritiques (C96.4)', 'Sous-catégorie de C96 pour les sarcomes à cellules de Langerhans, dendritiques folliculaires et dendritiques interdigitées.')
code('C96.5', 'Histiocytose à cellules de Langerhans multifocale et unisystémique (C96.5)', 'Sous-catégorie de C96 pour plusieurs lésions dans un seul système ; inclut la maladie de Hand-Schüller-Christian.')
code('C96.6', 'Histiocytose à cellules de Langerhans unifocale (C96.6)', 'Sous-catégorie de C96 pour une lésion unique ; inclut le granulome éosinophile.')
code('C96.7', 'Autres tumeurs malignes précisées des tissus lymphoïde, hématopoïétique et apparentés (C96.7)', 'Sous-catégorie résiduelle de C96 sans entité clinique décrite dans les sources lues.')
code('C96.8', 'Sarcome histiocytaire (C96.8)', 'Sous-catégorie de C96 pour le sarcome histiocytaire, qui inclut l’histiocytose maligne.')
code('C96.9', 'Tumeur maligne des tissus lymphoïde, hématopoïétique et apparentés, sans précision (C96.9)', 'Sous-catégorie résiduelle de C96 sans entité clinique décrite dans les sources lues.')
code('D47.0', 'Tumeurs histiocytaires et mastocytaires d’évolution imprévisible ou inconnue (D47.0)', 'Code où se range la mastocytose systémique indolente, exclue de C96.2.')
code('C94.3', 'Leucémie à mastocytes (C94.3-)', 'Code de la leucémie à mastocytes, exclue de C96.2.')
code('Q82.2', 'Mastocytose cutanée congénitale (Q82.2)', 'Code de la mastocytose cutanée congénitale, exclue de C96.2.')

d('HCL', [('H','Histiocytose'),('C','à Cellules'),('L','de Langerhans')], 'Histiocytose à cellules de Langerhans', 'Néoplasie clonale de cellules dendritiques, classée dans le groupe L des histiocytoses ; son code dépend de l’extension (C96.0, C96.5, C96.6).', 'c96-clonal')
d('HαT', [('H','Hérédo-'),('α','alpha-'),('T','Tryptasémie')], 'Alpha-tryptasémie héréditaire', 'Trait génétique présent chez environ 5 % de la population, qui élève la tryptase de base ; la valeur se corrige en divisant par (1 + nombre de copies alpha supplémentaires).', 'c96-hat')
d('ECNM', [('E','European'),('C','Competence'),('N','Network'),('M','on Mastocytosis')], 'Réseau européen de compétence sur la mastocytose', 'Réseau qui a publié en 2021 les critères diagnostiques et la classification des maladies mastocytaires, et qui tient un registre européen.', 'c96-sources-guides')
d('Euro-Histio-Net', [('Euro','européen'),('Histio','des histiocytoses'),('Net','Network (réseau)')], 'Réseau européen des histiocytoses', 'Réseau dont les recommandations de 2013 pour l’adulte et pour l’enfant sont des références européennes de l’histiocytose à cellules de Langerhans.', 'c96-sources-guides')
d('SGH/SSH', [('SGH','Schweizerische Gesellschaft für Hämatologie'),('SSH','Société suisse d’hématologie')], 'Société suisse d’hématologie', 'Société savante suisse, cosignataire du guide Onkopedia sur la mastocytose systémique.', 'c96-sources-guides')
for k,full,df in [
 ('CD1a','Cluster de différenciation 1a','Protéine de surface des cellules de Langerhans, marqueur de l’histiocytose à cellules de Langerhans.'),
 ('CD163','Cluster de différenciation 163','Marqueur des macrophages et histiocytes matures ; positif dans le sarcome histiocytaire et dans les maladies de Rosai-Dorfman et d’Erdheim-Chester.'),
 ('CD207','Cluster de différenciation 207 (langerine)','Nom du marqueur de la langerine, protéine des cellules de Langerhans.'),
 ('CD21','Cluster de différenciation 21','Marqueur des cellules dendritiques folliculaires.'),
 ('CD23','Cluster de différenciation 23','Marqueur des cellules dendritiques folliculaires.'),
 ('CD35','Cluster de différenciation 35','Marqueur des cellules dendritiques folliculaires.'),
 ('CD13','Cluster de différenciation 13','Marqueur myéloïde cité pour le sarcome myéloïde.'),
 ('CD33','Cluster de différenciation 33','Marqueur myéloïde cité pour le sarcome myéloïde.')]:
    d(k, [('CD','Cluster of Differentiation (groupe de différenciation)'),(k[2:],'numéro du marqueur')], full, df)
d('V600E', [('V','Valine'),('600','position 600 de la protéine'),('E','remplacée par un acide glutamique (Glutamate)')], 'Mutation BRAF V600E', 'Substitution d’un acide aminé qui rend la kinase BRAF active en permanence ; présente dans environ 50 % des histiocytoses à cellules de Langerhans.', 'c96-mapk')
d('V600', [('V','Valine'),('600','position 600 de la protéine')], 'Valine en position 600 de BRAF', 'Position mutée de BRAF ; le mélanome BRAF V600 est l’indication suisse du vémurafénib.', 'c96-mapk')
d('MAPK', [('M','Mitogen-'),('A','Activated'),('P','Protein'),('K','Kinase')], 'Kinase activée par les mitogènes', 'Voie de signalisation RAS-RAF-MEK-ERK qui transmet un signal de prolifération au noyau ; altérée dans l’histiocytose à cellules de Langerhans et le sarcome histiocytaire.', 'c96-mapk')
d('RAS-RAF-MEK-ERK', [('RAS','Rat Sarcoma'),('RAF','Rapidly Accelerated Fibrosarcoma'),('MEK','MAPK/ERK Kinase'),('ERK','Extracellular signal-Regulated Kinase')], 'Chaîne de kinases de la voie MAPK', 'Succession de protéines transmettant le signal de prolifération de la membrane au noyau.', 'c96-mapk')
d('RAS', [('R','Rat'),('AS','Sarcoma (sarcome du rat, virus d’origine)')], 'Protéine RAS', 'Protéine de la voie MAPK en amont de BRAF.', 'c96-mapk')
d('MEK', [('M','Mitogen-activated protein kinase /'),('E','Extracellular signal-regulated'),('K','Kinase kinase')], 'Kinase de la voie MAPK', 'Kinase située entre BRAF et ERK, cible des inhibiteurs de MEK.', 'c96-mapk')
d('ERK', [('E','Extracellular signal-'),('R','Regulated'),('K','Kinase')], 'Kinase régulée par les signaux extracellulaires', 'Dernière kinase de la chaîne MAPK avant le noyau.', 'c96-mapk')
d('SCF', [('S','Stem'),('C','Cell'),('F','Factor')], 'Facteur de cellules souches', 'Ligand du récepteur KIT ; la mutation D816V active le récepteur sans lui.', 'c96-kit')
d('S100', [('S','Soluble'),('100','dans le sulfate d’ammonium saturé à 100 %')], 'Protéine S100', 'Marqueur immunohistochimique positif dans l’histiocytose à cellules de Langerhans et variable dans le sarcome histiocytaire.')
nom('PU.1', 'PU.1, facteur de transcription des cellules myéloïdes', 'Marqueur immunohistochimique du sarcome histiocytaire.')
nom('VE1', 'VE1, clone d’anticorps dirigé contre BRAF V600E', 'Anticorps d’immunohistochimie dont un résultat négatif ou équivoque se confirme par méthode moléculaire.', 'c96-braf-test')
nom('ZBTB46', 'ZBTB46, facteur de transcription', 'Marqueur du phénotype des cellules de Langerhans tumorales.')
nom('PATHFINDER', 'PATHFINDER, étude de l’avapritinib', 'Étude rapportant une rémission complète de 19 % sous avapritinib dans la mastocytose avancée.')
nom('LCH-IV', 'LCH-IV, essai international de l’histiocytose', 'Essai dont les résultats ne sont pas disponibles dans les sources lues ; il a retiré le poumon des organes à risque.')
for k,full in [('Erdheim-Chester','maladie d’Erdheim-Chester'),('Rosai-Dorfman','maladie de Rosai-Dorfman'),('Abt-Letterer-Siwe','maladie d’Abt-Letterer-Siwe'),('Hand-Schüller-Christian','maladie de Hand-Schüller-Christian')]:
    nom(k, full, 'Nom propre d’une histiocytose, désignée par les auteurs qui l’ont décrite.')
d('R0', [('R','Résidu tumoral'),('0','aucun')], 'Exérèse sans résidu tumoral', 'Qualité d’une résection chirurgicale sans tumeur résiduelle microscopique ; objectif du traitement d’un sarcome histiocytaire localisé.')
d('CHOP', [('C','Cyclophosphamide'),('H','Hydroxydaunorubicine (doxorubicine)'),('O','Oncovin (vincristine)'),('P','Prednisone')], 'Cyclophosphamide, doxorubicine, vincristine, prednisone', 'Schéma de chimiothérapie utilisé en première ligne dans le sarcome histiocytaire disséminé.')
d('ICE', [('I','Ifosfamide'),('C','Carboplatine'),('E','Étoposide')], 'Ifosfamide, carboplatine, étoposide', 'Schéma de rattrapage cité pour le sarcome histiocytaire.')
d('ABVD', [('A','Adriamycine (doxorubicine)'),('B','Bléomycine'),('V','Vinblastine'),('D','Dacarbazine')], 'Adriamycine, bléomycine, vinblastine, dacarbazine', 'Schéma de rattrapage cité pour le sarcome histiocytaire.')
d('CLAG-M', [('CL','Cladribine'),('A','Aracytine (cytarabine)'),('G','G-CSF (facteur stimulant les granulocytes)'),('M','Mitoxantrone')], 'Cladribine, cytarabine, G-CSF, mitoxantrone', 'Schéma de rattrapage cité pour le sarcome histiocytaire.')
d('IPSM', [('I','International'),('P','Prognostic'),('S','Scoring'),('M','Mastocytosis (système pour la mastocytose)')], 'Système international de score pronostique de la mastocytose', 'Score pronostique clinique de la mastocytose systémique.')
d('MARS', [('M','Mutation-'),('A','Adjusted'),('R','Risk'),('S','Score')], 'Score de risque ajusté aux mutations', 'Score pronostique moléculaire de la mastocytose avancée.')
for k,full,lit in [
 ('MAP2K1','Gène de la kinase 1 de la kinase activée par les mitogènes',[('MAP2K1','Mitogen-Activated Protein Kinase Kinase 1')]),
 ('KRAS','Gène KRAS (Kirsten rat sarcoma)',[('K','Kirsten'),('RAS','Rat Sarcoma')]),
 ('NRAS','Gène NRAS (neuroblastoma RAS)',[('N','Neuroblastoma'),('RAS','Rat Sarcoma')]),
 ('TP53','Gène de la protéine tumorale 53',[('TP','Tumor Protein'),('53','poids moléculaire de 53 kilodaltons')]),
 ('PDGFRA','Gène du récepteur alpha du facteur de croissance dérivé des plaquettes',[('P','Platelet-'),('D','Derived'),('G','Growth'),('F','Factor'),('R','Receptor'),('A','Alpha')]),
 ('FIP1L1','Gène FIP1L1, partenaire de fusion de PDGFRA',[('FIP1L1','FIP1-Like 1')]),
 ('SRSF2','Gène du facteur d’épissage riche en sérine et en arginine 2',[('S','Serine/arginine-'),('R','Rich'),('S','Splicing'),('F','Factor'),('2','numéro 2')]),
 ('ASXL1','Gène ASXL1',[('A','Additional'),('S','Sex'),('X','combs'),('L','Like'),('1','numéro 1')]),
 ('RUNX1','Gène RUNX1',[('R','Runt-'),('U','related'),('N','transcription'),('X','factor'),('1','numéro 1')]),
 ('DNMT3A','Gène de l’ADN méthyltransférase 3 alpha',[('DN','DNA (ADN)'),('MT','MéthylTransférase'),('3A','3 alpha')]),
 ('FLT3','Gène FLT3',[('F','Fms-'),('L','Like'),('T','Tyrosine kinase'),('3','numéro 3')]),
 ('VEGFR2','Récepteur 2 du facteur de croissance de l’endothélium vasculaire',[('V','Vascular'),('E','Endothelial'),('G','Growth'),('F','Factor'),('R','Receptor'),('2','numéro 2')]),
 ('PKC','Protéine kinase C',[('P','Protein'),('K','Kinase'),('C','C')]),
 ('SOX10','Facteur de transcription SOX10 (marqueur de mélanome)',[('SOX','SRY-related HMG-box'),('10','numéro 10')]),
 ('HMB45','Anticorps HMB45 (marqueur de mélanome)',[('H','Human'),('M','Melanoma'),('B','Black'),('45','numéro 45')]),
 ('SMARCB1','Gène SMARCB1',[('SMARC','SWI/SNF-related, Matrix-associated, Actin-dependent Regulator of Chromatin'),('B','sous-famille B'),('1','membre 1')])]:
    d(k, lit, full, 'Gène ou marqueur cité à titre de repère génétique ou immunohistochimique dans ce chapitre.' )
d('PAL', [('P','Phosphatases'),('AL','ALcalines')], 'Phosphatases alcalines', 'Enzymes hépatiques et osseuses dosées dans le bilan initial de l’adulte atteint d’histiocytose.')
d('VS', [('V','Vitesse de'),('S','Sédimentation')], 'Vitesse de sédimentation', 'Marqueur inflammatoire dosé dans le bilan initial de l’adulte atteint d’histiocytose.')
d('FSC', [('F','Formule'),('S','Sanguine'),('C','Complète')], 'Formule sanguine complète', 'Numération des cellules du sang, première ligne du bilan initial.')
d('GH', [('G','Growth'),('H','Hormone')], 'Hormone de croissance', 'Hormone antéhypophysaire dont le déficit est le plus fréquent après atteinte de l’axe hypothalamo-hypophysaire dans l’histiocytose.', 'c96-di')
