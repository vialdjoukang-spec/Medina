"""Abréviations G81 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'g81', '__init__'}:
        continue
    _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
G = {}
def add_if_absent(key, letters, full, definition, window=None):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full,
                  'def': '<p>' + definition + '</p>', 'ref': window}

# Codes de la CIM-10-GM 2024 (bloc G80–G83) cités dans le cours
_CODES = (
    ('G81.0', 'Hémiparésie et hémiplégie flasques', 'Libellé traduit du texte allemand du BfArM (« schlaffe Hemiparese und Hemiplegie ») ; la version française de l’Office fédéral de la statistique n’a pas été lue. Ce sous-code correspond à la phase où dominent hypotonie et faiblesse.', 'g81-cim'),
    ('G81.1', 'Hémiparésie et hémiplégie spastiques', 'Libellé traduit du texte allemand du BfArM (« spastische Hemiparese und Hemiplegie ») ; la version française de l’Office fédéral de la statistique n’a pas été lue. Ce sous-code correspond à la phase où s’installe la spasticité.', 'g81-cim'),
    ('G81.9', 'Hémiparésie et hémiplégie, sans précision', 'Libellé traduit du texte allemand du BfArM (« nicht näher bezeichnet ») ; il s’emploie lorsque le caractère flasque ou spastique n’est pas documenté.', 'g81-cim'),
    ('G83.1', 'Monoparésie et monoplégie d’un membre inférieur', 'Code voisin de G81 : un seul membre est atteint, non l’hémicorps.', 'g81-cim'),
    ('G83.2', 'Monoparésie et monoplégie d’un membre supérieur', 'Code voisin de G81 : un seul membre est atteint, non l’hémicorps.', 'g81-cim'),
    ('G83.5', 'Syndrome de verrouillage (locked-in)', 'Code voisin de G81 dans le même bloc de la classification.', 'g81-cim'),
    ('G83.6', 'Parésie faciale centrale', 'Code voisin de G81 ; il exclut G51.0, la paralysie faciale périphérique.', 'g81-cim'),
    ('G83.8', 'Autres syndromes paralytiques précisés', 'Ce code inclut la paralysie postcritique de Todd selon le texte du BfArM.', 'g81-todd'),
    ('G51.0', 'Paralysie faciale (périphérique)', 'Code exclu de G83.6 : la paralysie faciale périphérique se distingue de la parésie faciale centrale.', 'g81-cim'),
    ('G11.4', 'Paraplégie spastique héréditaire', 'Code exclu de G80 selon le texte du BfArM.', 'g81-cim'),
)
for _k, _full, _d, _w in _CODES:
    add_if_absent(_k, [(_k, 'code de la CIM-10-GM 2024, non une abréviation développable lettre à lettre')], _full, _d, _w)

add_if_absent('SNAP-25', [('SNAP', 'Synaptosomal-Associated Protein (protéine associée aux synaptosomes)'), ('25', 'masse d’environ 25 kilodaltons')],
              'Protéine associée aux synaptosomes de 25 kDa',
              'La toxine botulique A clive cette protéine présynaptique, ce qui bloque la libération d’acétylcholine, selon l’information professionnelle suisse de BOTOX®.', 'g81-botox')
add_if_absent('OR', [('O', 'Odds (cotes)'), ('R', 'Ratio (rapport)')], 'Rapport de cotes',
              'Mesure d’association qui compare les cotes d’un événement entre un groupe exposé et un groupe de référence. Un rapport de cotes de 6,57 n’est ni un risque absolu ni une preuve de causalité.', 'g81-prevalence')
add_if_absent('Fugl-Meyer', [('Fugl-Meyer', 'nom propre de l’échelle, d’après ses auteurs, non une abréviation')],
              'Échelle de Fugl-Meyer',
              'Échelle d’évaluation motrice après AVC ; sa version du membre supérieur est citée par l’ESO 2025 (FMA-UE).', 'g81-echelles')
add_if_absent('PICO', [('P', 'Population'), ('I', 'Intervention'), ('C', 'Comparaison'), ('O', 'Outcome (critère de jugement)')],
              'Population, Intervention, Comparaison, Outcome',
              'Cadre qui structure une question de recommandation en population, intervention, comparaison et critère de jugement. La recommandation ESO 2025 est organisée en questions PICO numérotées.', 'g81-intensite')
add_if_absent('SMNS', [('S', 'Syndrome'), ('M', 'du Motoneurone'), ('N', 'supérieur (Neurone)'), ('S', 'Supérieur')],
              'Syndrome du motoneurone supérieur',
              'Ensemble de signes négatifs (faiblesse, hypotonie) et positifs (spasticité, hyperréflexie, clonus, signe de Babinski). La spasticité n’en est qu’une composante.', 'g81-smns')
add_if_absent('EMG', [('E', 'Électro'), ('M', 'Myo'), ('G', 'Graphie')], 'Électromyographie',
              'Enregistrement de l’activité électrique d’un muscle. En spasticité, l’activité enregistrée croît avec la vitesse d’étirement ; l’information professionnelle de BOTOX® mentionne aussi le guidage par électromyographie.', 'g81-vitesse')
add_if_absent('MAS', [('M', 'Modified'), ('A', 'Ashworth'), ('S', 'Scale')], 'Échelle d’Ashworth modifiée',
              'Échelle de cotation de la spasticité ; un score de 3 ou plus définit la spasticité invalidante dans la méta-analyse citée.', 'g81-mas')
add_if_absent('ESSD', [('E', 'European'), ('S', 'Society for'), ('S', 'Swallowing'), ('D', 'Disorders')],
              'Société européenne des troubles de la déglutition',
              'Elle a élaboré avec l’European Stroke Organisation la recommandation de 2021 sur le diagnostic et le traitement de la dysphagie post-AVC.', 'g81-dysphagie')
add_if_absent('FMA-UE', [('F', 'Fugl-'), ('M', 'Meyer'), ('A', 'Assessment'), ('U', 'Upper'), ('E', 'Extremity')],
              'Fugl-Meyer Assessment, membre supérieur',
              'Échelle d’évaluation de la fonction motrice du membre supérieur citée par l’ESO 2025.', 'g81-echelles')
add_if_absent('ARAT', [('A', 'Action'), ('R', 'Research'), ('A', 'Arm'), ('T', 'Test')], 'Action Research Arm Test',
              'Test de la fonction du membre supérieur cité par l’ESO 2025.', 'g81-echelles')
add_if_absent('WMFT', [('W', 'Wolf'), ('M', 'Motor'), ('F', 'Function'), ('T', 'Test')], 'Wolf Motor Function Test',
              'Test de la fonction motrice du membre supérieur cité par l’ESO 2025.', 'g81-echelles')
add_if_absent('MAL', [('M', 'Motor'), ('A', 'Activity'), ('L', 'Log')], 'Motor Activity Log',
              'Questionnaire sur l’usage du membre supérieur dans la vie quotidienne, cité par l’ESO 2025.', 'g81-echelles')
add_if_absent('FAC', [('F', 'Functional'), ('A', 'Ambulation'), ('C', 'Categories')], 'Functional Ambulation Categories',
              'Échelle de catégories de marche citée par l’ESO 2025.', 'g81-echelles')
add_if_absent('FGA', [('F', 'Functional'), ('G', 'Gait'), ('A', 'Assessment')], 'Functional Gait Assessment',
              'Évaluation fonctionnelle de la marche citée par l’ESO 2025.', 'g81-echelles')
add_if_absent('CIM', [('C', 'Classification'), ('I', 'Internationale des'), ('M', 'Maladies')], 'Classification internationale des maladies',
              'Classification statistique des diagnostics. Ce cours cite la CIM-10-GM 2024 ; la correspondance avec la CIM-11 n’est pas établie.', 'g81-cim')
add_if_absent('Swiss-CP-Reg', [('Swiss-CP-Reg', 'Swiss Cerebral Palsy Registry, nom d’un registre')],
              'Registre suisse de la paralysie cérébrale',
              'Registre cité uniquement par son titre pour renvoyer vers G80 ; son contenu n’a pas été lu.', 'g81-cim')
add_if_absent('ATC', [('A', 'Anatomical'), ('T', 'Therapeutic'), ('C', 'Chemical')], 'Classification anatomique, thérapeutique et chimique',
              'Système de classification des médicaments cité dans la fiche de recherche AIPS du baclofène intrathécal.', 'g81-intrathecal')
