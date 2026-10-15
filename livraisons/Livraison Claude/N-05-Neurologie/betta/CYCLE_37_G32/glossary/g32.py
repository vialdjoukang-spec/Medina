"""Abréviations G32 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'g32', '__init__'}:
        continue
    _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
G = {}
def add_if_absent(key, letters, full, definition, window):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full,
                  'def': '<p>' + definition + '</p>', 'ref': window}
add_if_absent('AMM', [('A', 'Acide'), ('M', 'Méthyl'), ('M', 'Malonique')], 'Acide méthylmalonique',
              'Cette molécule s’accumule quand la méthylmalonyl-CoA mutase manque de cobalamine active. Elle est élevée au-delà de 300 nmol/l et prouve un déficit fonctionnel en vitamine B12.', 'g32-amm')
add_if_absent('DCS', [('D', 'Dégénérescence'), ('C', 'Combinée'), ('S', 'Subaiguë')], 'Dégénérescence combinée subaiguë de la moelle',
              'Démyélinisation des cordons postérieurs et latéraux de la moelle, surtout cervicale, par déficit fonctionnel en vitamine B12.', 'g32-dcs')
add_if_absent('IRM', [('I', 'Imagerie'), ('R', 'par Résonance'), ('M', 'Magnétique')], 'Imagerie par résonance magnétique',
              'Elle montre dans la DCS un hypersignal T2 des cordons postérieurs en « V inversé », typiquement de C3 à C5 ; jusqu’à un tiers des cas sont normaux.', 'g32-irm')
add_if_absent('NMDA', [('N', 'N'), ('M', 'Méthyl'), ('D', 'D'), ('A', 'Aspartate')], 'N-méthyl-D-aspartate',
              'Nom d’un récepteur du glutamate dont l’excitotoxicité pourrait contribuer à la lésion induite par le protoxyde d’azote.', 'g32-n2o')
add_if_absent('NNT', [('N', 'Number'), ('N', 'Needed'), ('T', 'to Treat')], 'Nombre de sujets à traiter',
              'Nombre de patients à traiter pour qu’un patient de plus bénéficie de l’intervention ; ici 4 pour un schéma plus intensif chez les non-marchants autonomes.', 'g32-prono')
add_if_absent('VIH', [('V', 'Virus'), ('I', 'de l’Immunodéficience'), ('H', 'Humaine')], 'Virus de l’immunodéficience humaine',
              'Cause de myélopathie vacuolaire à discuter dans le diagnostic différentiel.', 'g32-diffmyelo')
add_if_absent('CIM-10-GM', [('CIM', 'Classification Internationale des Maladies'), ('10', 'dixième révision'), ('GM', 'German Modification')], 'CIM-10-GM 2024',
              'Version allemande de la classification internationale, utilisée par la Suisse pour le catalogue de ce cours.', 'g32-cim')
add_if_absent('CoA', [('Co', 'Coenzyme'), ('A', 'A')], 'Coenzyme A',
              'Cofacteur des acyl-transferts ; il entre dans le nom des substrats méthylmalonyl-CoA et succinyl-CoA.', 'g32-enzymes')
add_if_absent('MTHFR', [('M', 'Méthylène'), ('T', 'Tétra'), ('H', 'Hydro'), ('F', 'Folate'), ('R', 'Réductase')], 'Méthylènetétrahydrofolate réductase',
              'Gène dont le variant C677T figure parmi les causes génétiques rares citées de carence.', 'g32-diffmyelo')
add_if_absent('BfArM', [('Bf', 'Bundesinstitut für'), ('Ar', 'Arzneimittel'), ('M', 'und Medizinprodukte')], 'Institut fédéral allemand des médicaments et dispositifs médicaux',
              'Éditeur de la version allemande de la CIM-10-GM.', 'g32-cim')
add_if_absent('OFS', [('O', 'Office'), ('F', 'Fédéral de la'), ('S', 'Statistique')], 'Office fédéral de la statistique',
              'Éditeur suisse de la version française de la classification.', 'g32-cim')
add_if_absent('CHUV', [('C', 'Centre'), ('H', 'Hospitalier'), ('U', 'Universitaire'), ('V', 'Vaudois')], 'Centre hospitalier universitaire vaudois',
              'Hôpital cité pour l’expérience de cas comparables.', 'g32-epid')
add_if_absent('AIPS', [('A', 'Arzneimittel'), ('I', 'Informations'), ('P', 'Publikationsplattform'), ('S', 'Swissmedic')], 'Plateforme d’information professionnelle de Swissmedic',
              'Base publique des informations professionnelles de médicaments en Suisse.', 'g32-hydroxo')
add_if_absent('BSH', [('B', 'British'), ('S', 'Society for'), ('H', 'Haematology')], 'British Society for Haematology',
              'Société savante dont la ligne directrice n’a pas été trouvée.', 'g32-lacunes')
add_if_absent('NICE', [('N', 'National'), ('I', 'Institute for health and'), ('C', 'Care'), ('E', 'Excellence')], 'National Institute for Health and Care Excellence',
              'Organisme britannique dont la page n’a pas pu être lue.', 'g32-lacunes')
add_if_absent('AG', [('A', 'Aktien'), ('G', 'Gesellschaft')], 'Société anonyme',
              'Forme juridique de l’entreprise titulaire de la Vitarubine®.', 'g32-hydroxo')
add_if_absent('PM R', [('PM', 'Physical Medicine'), ('R', 'and Rehabilitation')], 'Physical Medicine and Rehabilitation',
              'Titre abrégé du périodique de la revue systématique.', 'g32-prono')
add_if_absent('H2', [('H', 'Histamine'), ('2', 'récepteur de type 2')], 'Antagonistes des récepteurs H2 de l’histamine',
              'Médicaments gastriques qui réduisent l’acidité et peuvent s’associer à une carence en vitamine B12.', 'g32-cim')
add_if_absent('T2', [('T', 'Temps de relaxation'), ('2', 'deuxième pondération')], 'Pondération T2',
              'Séquence d’IRM où l’hypersignal des cordons postérieurs est visible.', 'g32-irm')
add_if_absent('C1', [('C', 'Cervical'), ('1', 'première vertèbre')], 'Niveaux cervicaux C1 à C5',
              'Niveaux de la moelle cervicale cités dans les descriptions d’IRM.', 'g32-irm')
add_if_absent('C2', [('C', 'Cervical'), ('2', 'deuxième vertèbre')], 'Niveau cervical C2',
              'Limite supérieure des niveaux documentés dans la série allemande.', 'g32-irm')
add_if_absent('C3', [('C', 'Cervical'), ('3', 'troisième vertèbre')], 'Niveau cervical C3',
              'Début de la zone typique de l’hypersignal.', 'g32-irm')
add_if_absent('C4', [('C', 'Cervical'), ('4', 'quatrième vertèbre')], 'Niveau cervical C4',
              'Niveau intermédiaire de la zone typique.', 'g32-irm')
add_if_absent('C5', [('C', 'Cervical'), ('5', 'cinquième vertèbre')], 'Niveau cervical C5',
              'Fin de la zone typique de l’hypersignal.', 'g32-irm')
add_if_absent('B1', [('B', 'Vitamine B'), ('1', 'thiamine')], 'Vitamine B1',
              'Carence citée dans le diagnostic différentiel des polyneuropathies.', 'g32-diffmyelo')
add_if_absent('B6', [('B', 'Vitamine B'), ('6', 'pyridoxine')], 'Vitamine B6',
              'Sa carence élève l’homocystéine et figure parmi les causes de polyneuropathie.', 'g32-hcy')
add_if_absent('B9', [('B', 'Vitamine B'), ('9', 'folates')], 'Vitamine B9',
              'Carence citée dans le diagnostic différentiel.', 'g32-folates')
add_if_absent('B12', [('B', 'Vitamine B'), ('12', 'cobalamine')], 'Vitamine B12',
              'Cobalamine, cofacteur de la méthylmalonyl-CoA mutase et de la méthionine synthase.', 'g32-enzymes')
add_if_absent('C677T', [('C677T', 'nom d’un variant génétique, non une abréviation')], 'Variant C677T du gène MTHFR',
              'Désigne la substitution en position 677 de la séquence du gène.', 'g32-diffmyelo')
add_if_absent('E53', [('E', 'chapitre des maladies endocriniennes, nutritionnelles et métaboliques'), ('53', 'catégorie des autres carences en vitamines du groupe B')], 'Catégorie E53 de la CIM-10-GM',
              'Sa sous-catégorie E53.8 est le code causal listé sous G32.0.', 'g32-cim')
add_if_absent('G30', [('G', 'chapitre des maladies du système nerveux'), ('30', 'catégorie de la maladie d’Alzheimer')], 'Catégorie G30 de la CIM-10-GM',
              'Début du bloc G30–G32 dans la classification.', 'g32-cim')
add_if_absent('G32', [('G', 'chapitre des maladies du système nerveux'), ('32', 'catégorie des autres affections dégénératives au cours de maladies classées ailleurs')], 'Catégorie G32 de la CIM-10-GM',
              'Catégorie à astérisque, manifestation d’une maladie causale.', 'g32-cim')
add_if_absent('SafeZone', [('SafeZone', 'nom propre d’un service suisse de conseil, non une abréviation')], 'SafeZone.ch',
              'Service de consultation sur les substances, cité pour la prévention.', 'g32-droit')
add_if_absent('AmiKo', [('AmiKo', 'nom propre d’une application de consultation des notices, non une abréviation')], 'AmiKo',
              'Base de consultation de l’information professionnelle suisse.', 'g32-hydroxo')
