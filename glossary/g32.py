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
add_if_absent('AMM', [('A', 'Acide'), ('M', 'Méthyl'), ('M', 'Malonique')], 'Acide méthylmalonique', 'Métabolite pouvant augmenter dans un déficit fonctionnel en B12, mais aussi notamment en insuffisance rénale. Il ne prouve pas seul la cause ; références du laboratoire et contexte nécessaires.', 'g32-b12-fonction')
add_if_absent('DCS', [('D', 'Dégénérescence'), ('C', 'Combinée'), ('S', 'Subaiguë')], 'Dégénérescence combinée subaiguë de la moelle', 'Démyélinisation des cordons postérieurs et latéraux de la moelle, surtout cervicale, par déficit fonctionnel en vitamine B12.', 'g32-dcs')
add_if_absent('IRM', [('I', 'Imagerie'), ('R', 'par Résonance'), ('M', 'Magnétique')], 'Imagerie par résonance magnétique', 'Examen aidant à localiser et rechercher une autre cause ; un signal postérieur en V peut être compatible sans être spécifique, et une image normale ne suffit pas toujours à exclure.', 'g32-imagerie')
add_if_absent('NMDA', [('N', 'N'), ('M', 'Méthyl'), ('D', 'D'), ('A', 'Aspartate')], 'N-méthyl-D-aspartate', 'Nom d’un récepteur du glutamate dont l’excitotoxicité pourrait contribuer à la lésion induite par le protoxyde d’azote.', 'g32-exposition')
add_if_absent('NNT', [('N', 'Number'), ('N', 'Needed'), ('T', 'to Treat')], 'Nombre de sujets à traiter', 'Nombre de personnes à traiter pour obtenir un bénéfice supplémentaire selon un essai et son contexte ; aucun chiffre de cet indicateur non relu n’est appliqué à G32 ici.', 'g32-pronostic')
add_if_absent('VIH', [('V', 'Virus'), ('I', 'de l’Immunodéficience'), ('H', 'Humaine')], 'Virus de l’immunodéficience humaine', 'Cause de myélopathie vacuolaire à discuter dans le diagnostic différentiel.', 'g32-etiologies')
add_if_absent('CIM-10-GM', [('CIM', 'Classification Internationale des Maladies'), ('10', 'dixième révision'), ('GM', 'German Modification')], 'CIM-10-GM 2024', 'Version allemande de la classification internationale, utilisée par la Suisse pour le catalogue de ce cours.', 'g32-codage')
add_if_absent('CoA', [('Co', 'Coenzyme'), ('A', 'A')], 'Coenzyme A', 'Cofacteur des acyl-transferts ; il entre dans le nom des substrats méthylmalonyl-CoA et succinyl-CoA.', 'g32-b12-fonction')
add_if_absent('MTHFR', [('M', 'Méthylène'), ('T', 'Tétra'), ('H', 'Hydro'), ('F', 'Folate'), ('R', 'Réductase')], 'Méthylènetétrahydrofolate réductase', 'Gène du métabolisme des folates cité dans la revue ; une association génétique ne constitue pas un diagnostic de carence ni une indication systématique de test.', 'g32-etiologies')
add_if_absent('BfArM', [('Bf', 'Bundesinstitut für'), ('Ar', 'Arzneimittel'), ('M', 'und Medizinprodukte')], 'Institut fédéral allemand des médicaments et dispositifs médicaux', 'Éditeur de la version allemande de la CIM-10-GM.', 'g32-codage')
add_if_absent('OFS', [('O', 'Office'), ('F', 'Fédéral de la'), ('S', 'Statistique')], 'Office fédéral de la statistique', 'Éditeur suisse de la version française de la classification.', 'g32-codage')
add_if_absent('CHUV', [('C', 'Centre'), ('H', 'Hospitalier'), ('U', 'Universitaire'), ('V', 'Vaudois')], 'Centre hospitalier universitaire vaudois', 'Centre hospitalier cité dans le contexte d’une observation suisse ; pas de fréquence nationale G32 déduite de cette mention.', 'g32-serie')
add_if_absent('AIPS', [('A', 'Arzneimittel'), ('I', 'Informations'), ('P', 'Publikationsplattform'), ('S', 'Swissmedic')], 'Plateforme d’information professionnelle de Swissmedic', 'Base publique des informations professionnelles de médicaments en Suisse.', 'g32-vitarubine')
add_if_absent('BSH', [('B', 'British'), ('S', 'Society for'), ('H', 'Haematology')], 'British Society for Haematology', 'Société britannique d’hématologie ; cette version s’appuie sur le guide NICE et le texte spécialisé britannique effectivement lus, sans attribuer une recommandation non consultée à cette société.', 'g32-r7')
add_if_absent('NICE', [('N', 'National'), ('I', 'Institute for health and'), ('C', 'Care'), ('E', 'Excellence')], 'National Institute for Health and Care Excellence', 'Organisme britannique dont le guide NG239 de 2024 a été réellement lu par sections pour cette version ; le champ concerne les personnes de 16 ans et plus.', 'g32-r5')
add_if_absent('AG', [('A', 'Aktien'), ('G', 'Gesellschaft')], 'Société anonyme', 'Forme juridique de l’entreprise titulaire de la Vitarubine®.', 'g32-vitarubine')
add_if_absent('PM R', [('PM', 'Physical Medicine'), ('R', 'and Rehabilitation')], 'Physical Medicine and Rehabilitation', 'Titre abrégé du périodique de la revue systématique.', 'g32-pronostic')
add_if_absent('H2', [('H', 'Histamine'), ('2', 'récepteur de type 2')], 'Antagonistes des récepteurs H2 de l’histamine', 'Médicaments gastriques qui réduisent l’acidité et peuvent s’associer à une carence en vitamine B12.', 'g32-codage')
add_if_absent('T2', [('T', 'Temps de relaxation'), ('2', 'deuxième pondération')], 'Pondération T2', 'Séquence d’IRM où l’hypersignal des cordons postérieurs est visible.', 'g32-imagerie')
add_if_absent('C1', [('C', 'Cervical'), ('1', 'première vertèbre')], 'Niveaux cervicaux C1 à C5', 'Repère cervical d’imagerie. Le niveau et l’étendue sont décrits selon l’examen et la légende, sans localisation obligatoire dans chaque cas.', 'g32-imagerie')
add_if_absent('C2', [('C', 'Cervical'), ('2', 'deuxième vertèbre')], 'Niveau cervical C2', 'Repère cervical d’imagerie. Le niveau et l’étendue sont décrits selon l’examen et la légende, sans localisation obligatoire dans chaque cas.', 'g32-imagerie')
add_if_absent('C3', [('C', 'Cervical'), ('3', 'troisième vertèbre')], 'Niveau cervical C3', 'Repère cervical d’imagerie. Le niveau et l’étendue sont décrits selon l’examen et la légende, sans localisation obligatoire dans chaque cas.', 'g32-imagerie')
add_if_absent('C4', [('C', 'Cervical'), ('4', 'quatrième vertèbre')], 'Niveau cervical C4', 'Repère cervical d’imagerie. Le niveau et l’étendue sont décrits selon l’examen et la légende, sans localisation obligatoire dans chaque cas.', 'g32-imagerie')
add_if_absent('C5', [('C', 'Cervical'), ('5', 'cinquième vertèbre')], 'Niveau cervical C5', 'Repère cervical d’imagerie. Le niveau et l’étendue sont décrits selon l’examen et la légende, sans localisation obligatoire dans chaque cas.', 'g32-imagerie')
add_if_absent('B1', [('B', 'Vitamine B'), ('1', 'thiamine')], 'Vitamine B1', 'Carence citée dans le diagnostic différentiel des polyneuropathies.', 'g32-etiologies')
add_if_absent('B6', [('B', 'Vitamine B'), ('6', 'pyridoxine')], 'Vitamine B6', 'Sa carence élève l’homocystéine et figure parmi les causes de polyneuropathie.', 'g32-seuils')
add_if_absent('B9', [('B', 'Vitamine B'), ('9', 'folates')], 'Vitamine B9', 'Carence citée dans le diagnostic différentiel.', 'g32-folates')
add_if_absent('B12', [('B', 'Vitamine B'), ('12', 'cobalamine')], 'Vitamine B12', 'Cobalamine, cofacteur de la méthylmalonyl-CoA mutase et de la méthionine synthase.', 'g32-b12-fonction')
add_if_absent('C677T', [('C677T', 'nom d’un variant génétique, non une abréviation')], 'Variant C677T du gène MTHFR', 'Nom de variant cité dans la revue ; aucune recherche génétique systématique ni causalité certaine de G32 n’en est déduite.', 'g32-etiologies')
add_if_absent('E53', [('E', 'chapitre des maladies endocriniennes, nutritionnelles et métaboliques'), ('53', 'catégorie des autres carences en vitamines du groupe B')], 'Catégorie E53 de la CIM-10-GM', 'Sa sous-catégorie E53.8 est le code causal listé sous G32.0.', 'g32-codage')
add_if_absent('G30', [('G', 'chapitre des maladies du système nerveux'), ('30', 'catégorie de la maladie d’Alzheimer')], 'Catégorie G30 de la CIM-10-GM', 'Début du bloc G30–G32 dans la classification.', 'g32-codage')
add_if_absent('G32', [('G', 'chapitre des maladies du système nerveux'), ('32', 'catégorie des autres affections dégénératives au cours de maladies classées ailleurs')], 'Catégorie G32 de la CIM-10-GM', 'Catégorie à astérisque, manifestation d’une maladie causale.', 'g32-codage')
add_if_absent('SafeZone', [('SafeZone', 'nom propre d’un service suisse de conseil, non une abréviation')], 'SafeZone.ch', 'Service de consultation sur les substances, cité pour la prévention.', 'g32-aide')
add_if_absent('AmiKo', [('AmiKo', 'nom propre d’une application de consultation des notices, non une abréviation')], 'AmiKo', 'Base de consultation de l’information professionnelle suisse.', 'g32-vitarubine')
add_if_absent('RöFo', [('Rö', 'Röntgen-'), ('Fo', 'Fortschritte')], 'Fortschritte auf dem Gebiet der Röntgenstrahlen und der bildgebenden Verfahren', 'Titre de revue radiologique rencontré dans le dossier antérieur ; aucune preuve clinique de cette référence non lue n’est utilisée ici.', 'g32-imagerie')
add_if_absent('NG239', [('NG239', 'Guide NICE numéro NG239')], 'Guide NICE numéro NG239', 'Identifiant du guide britannique 2024 sur la carence en vitamine B12 chez les personnes de 16 ans et plus.', 'g32-r5')
add_if_absent('Riviera-Chablais', [('Riviera-Chablais', 'Hôpital Riviera-Chablais')], 'Hôpital Riviera-Chablais', 'Établissement suisse de Rennaz dont les auteurs ont publié l’observation clinique de 2026.', 'g32-r4')
add_if_absent('MMA', [('MMA', 'Acide méthylmalonique, sigle anglais')], 'Acide méthylmalonique, sigle anglais', 'Même métabolite que AMM ; sa mesure se lit avec méthode, rein et contexte.', 'g32-b12-fonction')
add_if_absent('D03m', [('D03m', 'Règle suisse des codes dague et étoile')], 'Règle suisse des codes dague et étoile', 'Règle du manuel 2026 : code étiologique avant la manifestation selon les conditions applicables ; étoile jamais seule.', 'g32-codage')
add_if_absent('CEN', [('CEN', 'Collège des enseignants de neurologie')], 'Collège des enseignants de neurologie', 'Institution française dont le chapitre de sensibilité fonde les manœuvres pédagogiques de cette leçon.', 'g32-r13')
add_if_absent('BioRender', [('BioRender', 'Outil de production d’illustrations')], 'Outil de production d’illustrations', 'La figure 5 du cas suisse porte des droits spécifiques réservés ; elle n’est pas reproduite ici.', 'g32-r4')
