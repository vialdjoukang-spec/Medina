"""Abréviations G63 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'g63', '__init__'}:
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

for _code, _lib, _txt in [
    ('G63.0', 'infectieuses et parasitaires classées ailleurs', 'maladie de Lyme, diphtérie, lèpre, syphilis tardive, zona'),
    ('G63.1', 'tumorales', 'syndromes paranéoplasiques, paraprotéines, traitement anticancéreux'),
    ('G63.2', 'diabétique', 'diabète sucré, quatrième position .4'),
    ('G63.3', 'd’autres maladies endocriniennes et métaboliques', 'amylose à transthyrétine dans ce cours'),
    ('G63.4', 'par carence nutritionnelle', 'vitamine B12, thiamine, alcool'),
    ('G63.5', 'd’affections disséminées du tissu conjonctif', 'vasculite, syndrome de Sjögren'),
    ('G63.6', 'd’autres affections ostéo-articulaires et des muscles', 'aucun contenu dans les sources lues'),
    ('G63.8', 'd’autres maladies classées ailleurs', 'neuropathie urémique'),
]:
    add_if_absent(_code, [(_code[:3], 'catégorie de la classification internationale des maladies'), (_code[3:], 'sous-rubrique')],
                  'Polynévrite ' + _lib + ' (' + _code + '*)',
                  'Sous-rubrique astérisque de la catégorie G63 dans la CIM-10-GM 2024. Maladies de base citées : ' + _txt + '. Elle ne s’emploie qu’avec le code primaire de la maladie de base.', 'g63-croix')
add_if_absent('G62.0', [('G62', 'autres polyneuropathies'), ('.0', 'polynévrite médicamenteuse')],
              'Polynévrite médicamenteuse (G62.0)',
              'Code envisagé pour la neuropathie causée par un médicament. Son rattachement, par rapport à G63.1 pour le traitement anticancéreux, n’a pas été vérifié dans les sources lues.', 'g63-chimio')
add_if_absent('ALDH2', [('ALDH', 'Aldehyde Dehydrogenase (acétaldéhyde déshydrogénase)'), ('2', 'isoforme 2')],
              'Aldéhyde déshydrogénase 2',
              'Enzyme dont le variant ALDH2*2 est cité par la revue de Julian et coll. parmi les éléments qui font intervenir l’acétaldéhyde dans la neuropathie alcoolique.', 'g63-alcool')
add_if_absent('AG', [('A', 'Aktien'), ('G', 'gesellschaft (société anonyme)')],
              'Société anonyme de droit suisse ou allemand (Aktiengesellschaft)',
              'Forme juridique de l’entreprise titulaire de l’autorisation citée pour l’information professionnelle (Mepha Pharma AG, Streuli Pharma AG, Lundbeck (Schweiz) AG, Grünenthal Pharma AG).', 'g63-duloxetine')
add_if_absent('SA', [('S', 'Société'), ('A', 'Anonyme')],
              'Société anonyme',
              'Forme juridique de l’entreprise titulaire de l’autorisation citée pour Benerva (Teofarma Suisse SA).', 'g63-thiamine')
add_if_absent('GmbH', [('G', 'Gesellschaft'), ('mb', 'mit beschränkter'), ('H', 'Haftung (responsabilité limitée)')],
              'Société à responsabilité limitée de droit allemand (Gesellschaft mit beschränkter Haftung)',
              'Forme juridique de l’entreprise titulaire de l’autorisation citée pour Lyrica et Neurontin (Viatris Pharma GmbH).', 'g63-pregabaline')
add_if_absent('ATTReuNET', [('ATTR', 'Amylose à Transthyrétine'), ('euNET', 'réseau européen (nom de réseau)')],
              'Réseau européen sur l’amylose à transthyrétine (nom de réseau)',
              'Groupe européen d’experts auteur du premier consensus de 2016 sur le diagnostic, la prise en charge et le traitement de la polyneuropathie amyloïde familiale à transthyrétine.', 'g63-ttr')
add_if_absent('Anti-Hu', [('Anti', 'dirigé contre'), ('Hu', 'antigène neuronal Hu (nom conventionnel)')],
              'Anticorps dirigé contre l’antigène neuronal Hu',
              'Anticorps à haut risque de cancer : il s’associe à plus de 85 % de cancers bronchiques à petites cellules (Graus et coll., 2021).', 'g63-neuronopathie')
add_if_absent('CV2', [('CV2', 'nom conventionnel d’un anticorps, non développé dans les sources lues')],
              'Anticorps CV2/CRMP5',
              'Anticorps cité par Sommer et coll. avec l’anti-Hu et l’amphiphysine parmi les anticorps des neuronopathies sensitives paranéoplasiques.', 'g63-neuronopathie')
add_if_absent('CRMP5', [('C', 'Collapsin'), ('R', 'Response'), ('M', 'Mediator'), ('P', 'Protein'), ('5', 'numéro 5')],
              'Protéine médiatrice de la réponse à la collapsine 5',
              'Cible de l’anticorps CV2/CRMP5, associé aux neuronopathies sensitives paranéoplasiques.', 'g63-neuronopathie')
add_if_absent('anti-GM1', [('anti', 'dirigé contre'), ('GM1', 'ganglioside GM1')],
              'Anticorps dirigé contre le ganglioside GM1',
              'Anticorps présent d’environ 50 % des neuropathies motrices multifocales (IgM).', 'g63-pidc')
add_if_absent('anti-GQ1b', [('anti', 'dirigé contre'), ('GQ1b', 'ganglioside GQ1b')],
              'Anticorps dirigé contre le ganglioside GQ1b',
              'Anticorps inscrit au bilan étendu de la revue de Sommer et coll.', 'g63-labo')
add_if_absent('anti-MAG', [('anti', 'dirigé contre'), ('MAG', 'Myelin-Associated Glycoprotein (glycoprotéine associée à la myéline)')],
              'Anticorps dirigé contre la glycoprotéine associée à la myéline',
              'Anticorps des neuropathies démyélinisantes distales à IgM.', 'g63-labo')
add_if_absent('MAG', [('M', 'Myelin'), ('A', 'Associated'), ('G', 'Glycoprotein')],
              'Glycoprotéine associée à la myéline (Myelin-Associated Glycoprotein)',
              'Cible des anticorps de la neuropathie démyélinisante distale à IgM.', 'g63-labo')
add_if_absent('POEMS', [('P', 'Polyneuropathy'), ('O', 'Organomegaly'), ('E', 'Endocrinopathy'), ('M', 'Monoclonal gammopathy'), ('S', 'Skin changes')],
              'Syndrome POEMS',
              'Syndrome cité par la revue de Sommer et coll. parmi les neuropathies à paraprotéine.', 'g63-labo')
add_if_absent('PMP22', [('PMP', 'Peripheral Myelin Protein'), ('22', 'masse de 22 kilodaltons')],
              'Protéine périphérique de la myéline 22',
              'Gène cité parmi les gènes testés dans les neuropathies héréditaires.', 'g63-labo')
add_if_absent('GJB1', [('GJB', 'Gap Junction Beta'), ('1', 'numéro 1')],
              'Gène de la jonction communicante bêta 1',
              'Gène cité parmi les gènes testés dans les neuropathies héréditaires.', 'g63-labo')
add_if_absent('MPZ', [('M', 'Myelin'), ('P', 'Protein'), ('Z', 'Zero')],
              'Protéine zéro de la myéline',
              'Gène cité parmi les gènes testés dans les neuropathies héréditaires.', 'g63-labo')
add_if_absent('MFN2', [('MFN', 'Mitofusin'), ('2', 'numéro 2')],
              'Mitofusine 2',
              'Gène cité parmi les gènes testés dans les neuropathies héréditaires.', 'g63-labo')
add_if_absent('RAGE', [('R', 'Receptor for'), ('A', 'Advanced'), ('G', 'Glycation'), ('E', 'End products')],
              'Récepteur des produits de glycation avancée',
              'Récepteur par lequel agissent les produits de glycation avancée dans la neuropathie diabétique (Feldman et coll., 2019).', 'g63-diab-meca')
add_if_absent('NNT', [('N', 'Nombre'), ('N', 'de patients'), ('T', 'à Traiter')],
              'Nombre de patients à traiter',
              'Nombre de patients à traiter pour obtenir un répondeur de plus qu’avec le placebo ; plus il est bas, plus le traitement est efficace en moyenne.', 'g63-nnt')
add_if_absent('PNS', [('P', 'Peripheral'), ('N', 'Nerve'), ('S', 'Society')],
              'Peripheral Nerve Society (société du nerf périphérique)',
              'Société savante coauteure de la recommandation européenne de la polyradiculoneuropathie chronique et auteure de la recommandation sur la neuropathie vasculitique.', 'g63-pidc')
add_if_absent('PNS-Care', [('PNS', 'Paraneoplastic Neurological Syndromes'), ('Care', 'nom du score, non développé dans les sources lues')],
              'Score PNS-Care (syndromes neurologiques paranéoplasiques)',
              'Score de la publication de Graus et coll. (2021) : un syndrome paranéoplasique est définitif à partir de 8 points.', 'g63-pnscare')
add_if_absent('PIDC', [('P', 'Polyradiculoneuropathie'), ('I', 'Inflammatoire'), ('D', 'Démyélinisante'), ('C', 'Chronique')],
              'Polyradiculoneuropathie inflammatoire démyélinisante chronique',
              'Neuropathie dysimmune d’évolution d’au moins 8 semaines, avec démyélinisation électrophysiologique.', 'g63-pidc')
add_if_absent('EAN', [('E', 'European'), ('A', 'Academy of'), ('N', 'Neurology')],
              'Académie européenne de neurologie (European Academy of Neurology)',
              'Société savante coauteure de la recommandation de 2021 sur la polyradiculoneuropathie chronique.', 'g63-pidc')
add_if_absent('EFNS', [('E', 'European'), ('F', 'Federation of'), ('N', 'Neurological'), ('S', 'Societies')],
              'Fédération européenne des sociétés de neurologie',
              'Auteure des recommandations de 2010 sur la douleur neuropathique et sur la neuroborréliose européenne.', 'g63-douleur')
add_if_absent('EONS-EANO', [('EONS', 'European Oncology Nursing Society'), ('EANO', 'European Association of Neuro-Oncology')],
              'Société européenne des soins infirmiers en oncologie et Association européenne de neuro-oncologie',
              'Coauteures, avec la Société européenne d’oncologie médicale, de la recommandation de 2020 sur la neurotoxicité des traitements anticancéreux, non lue.', 'g63-chimio')
add_if_absent('NeuPSIG', [('Neu', 'Neuropathic'), ('P', 'Pain'), ('S', 'Special'), ('I', 'Interest'), ('G', 'Group')],
              'Groupe d’intérêt spécialisé sur la douleur neuropathique',
              'Groupe de l’Association internationale pour l’étude de la douleur, auteur de la méta-analyse de 2015 sur la pharmacothérapie de la douleur neuropathique.', 'g63-douleur')
add_if_absent('JRSM', [('J', 'Journal'), ('R', 'of the Royal'), ('S', 'Society of'), ('M', 'Medicine')],
              'Journal of the Royal Society of Medicine',
              'Famille de revues dont JRSM Cardiovascular Disease, qui a publié la revue sur les complications neurologiques de la maladie rénale chronique.', 'g63-uremie')
add_if_absent('Rydel-Seiffer', [('Rydel-Seiffer', 'noms de deux auteurs, non une abréviation')],
              'Diapason gradué de Rydel et Seiffer',
              'Diapason dont la graduation donne une valeur sur 8 ; la valeur normale dépend de l’âge.', 'g63-diapason')
add_if_absent('Duloxetin-Mepha', [('Duloxetin', 'duloxétine'), ('Mepha', 'nom du fabricant, non une abréviation')],
              'Duloxetin-Mepha, nom commercial de la duloxétine',
              'Générique de la duloxétine dont l’information professionnelle suisse a été lue.', 'g63-duloxetine')
add_if_absent('kJ', [('k', 'kilo'), ('J', 'joule')],
              'Kilojoule',
              'Unité d’énergie : l’information professionnelle de Benerva rapporte 0,4 mg de thiamine nécessaire pour environ 4200 kJ de métabolisme glucidique.', 'g63-thiamine')
