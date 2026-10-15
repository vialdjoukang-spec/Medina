"""Abréviations G36 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib, sys
_here = Path(__file__).resolve().parent
_gdir = _here
if not (_gdir / 'cardio_1.py').exists():
    for _p in _here.parents:
        if (_p / 'glossary' / 'cardio_1.py').exists():
            _gdir = _p / 'glossary'
            break
if str(_gdir) not in sys.path:
    sys.path.insert(0, str(_gdir))
_existing = {}
for _path in sorted(_gdir.glob('*.py')):
    if _path.stem in {'g36', '__init__'}:
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

add_if_absent('NMOSD', [('N','Neuromyelitis'),('O','Optica'),('S','Spectrum'),('D','Disorders')],
              'Troubles du spectre de la neuromyélite optique',
              'Terme parapluie qui couvre la neuromyélite optique avec anticorps anti-aquaporine 4, ses formes frustes et des syndromes apparentés. Les patients sans anticorps anti-aquaporine 4 qui remplissent les critères de la MOGAD ne doivent plus recevoir ce diagnostic (recommandations européennes de 2023).', 'g36-nmosd')
add_if_absent('MOG', [('M','Myelin'),('O','Oligodendrocyte'),('G','Glycoprotein')],
              'Glycoprotéine oligodendrocytaire de la myéline',
              'Protéine cible des anticorps dans la MOGAD. Les anticorps anti-MOG se recherchent dans le sérum par un test cellulaire.', 'g36-mogad')
add_if_absent('MOGAD', [('MOG','Myelin Oligodendrocyte Glycoprotein'),('A','Antibody-'),('D','associated Disease')],
              'Maladie associée aux anticorps anti-glycoprotéine oligodendrocytaire de la myéline',
              'Entité distincte de la sclérose en plaques et de la NMOSD avec anticorps anti-aquaporine 4. Ses critères diagnostiques datent de 2023 (panel international).', 'g36-mogad')
add_if_absent('ADEM', [('A','Acute'),('D','Disseminated'),('E','Encephalo'),('M','Myelitis')],
              'Encéphalomyélite aiguë disséminée',
              'Encéphalomyélite démyélinisante aiguë, classée G37.8 dans la CIM-10-GM 2024. La leucoencéphalite hémorragique aiguë en est la forme la plus sévère.', 'g36-adem')
add_if_absent('LCS', [('L','Liquide'),('C','Cérébro-'),('S','Spinal')], 'Liquide cérébro-spinal',
              'Liquide recueilli par ponction lombaire ; son profil (bandes oligoclonales, quotient d’albumine, réaction MRZ) aide à distinguer la NMOSD, la MOGAD et la sclérose en plaques.', 'g36-lcs')
add_if_absent('LETM', [('L','Longitudinally'),('E','Extensive'),('T','Transverse'),('M','Myelitis')],
              'Myélite transverse longitudinalement étendue',
              'Lésion médullaire s’étendant sur trois segments vertébraux contigus ou plus, typique de la NMOSD.', 'g36-myelite')
add_if_absent('SEP', [('S','Sclérose'),('E','En'),('P','Plaques')], 'Sclérose en plaques',
              'Maladie inflammatoire démyélinisante du système nerveux central, classée G35 ; principal diagnostic différentiel de la NMOSD sans anticorps.', 'g36-nmosd')
add_if_absent('MRZ', [('M','Masern (rougeole)'),('R','Röteln (rubéole)'),('Z','Zoster (zona)')],
              'Réaction MRZ',
              'Réaction mesurée dans le liquide cérébro-spinal, positive dans environ 67 % des cas de sclérose en plaques et quasi absente en NMOSD et MOGAD (recommandations européennes de 2023).', 'g36-lcs')
add_if_absent('EDSS', [('E','Expanded'),('D','Disability'),('S','Status'),('S','Scale')], 'Échelle étendue du statut d’incapacité',
              'Échelle d’évaluation du handicap neurologique, recommandée avec les scores des systèmes fonctionnels tous les 6 à 12 mois.', 'g36-nmosd')
add_if_absent('FSS', [('F','Functional'),('S','System'),('S','Scores')], 'Scores des systèmes fonctionnels',
              'Scores fonctionnels associés à l’échelle EDSS pour le suivi du handicap.', 'g36-nmosd')
add_if_absent('NEMOS', [('NEMOS', 'nom du groupe allemand d’étude de la neuromyélite optique (Neuromyelitis Optica Study Group), non développable lettre à lettre')],
              'Neuromyelitis Optica Study Group',
              'Ce groupe a publié en 2023 et 2024 les recommandations européennes sur le diagnostic et le traitement de la NMOSD, sources principales de ce cours.', 'g36-nmosd')
add_if_absent('NMATDC', [('N','Nerf'),('M','Moelle'),('A','Area postrema'),('T','Tronc'),('D','Diencéphale'),('C','Cerveau')],
              'Nerf, Moelle, Area postrema, Tronc, Diencéphale, Cerveau',
              'Aide pédagogique pour retenir les six caractéristiques cardinales de la NMOSD, non critère officiel.', 'g36-mnemo')
add_if_absent('BN40898', [('BN40898', 'numéro d’étude, sans développement de lettres')], 'Étude BN40898',
              'Étude citée dans l’information professionnelle suisse d’Enspryng® pour l’efficacité chez les patients avec anticorps anti-aquaporine 4.', 'g36-enspryng')
add_if_absent('W135', [('W135', 'désignation d’un sérogroupe de méningocoque, sans développement de lettres')], 'Sérogroupe W135 du méningocoque',
              'Sérogroupe inclus dans la vaccination antiméningococcique préalable aux anti-C5 (A, C, Y, W135 ; B si disponible).', 'g36-complement')
add_if_absent('G36.0', [('G36.0', 'code de la CIM-10-GM 2024, intitulé : Neuromyélite optique [Devic]')], 'Neuromyélite optique [Devic]',
              'Sous-code de G36 ; inclut la démyélinisation au cours d’une névrite optique ; exclut la névrite optique sans précision (H46).', 'g36-adem')
add_if_absent('G36.1', [('G36.1', 'code de la CIM-10-GM 2024, intitulé : Leucoencéphalite hémorragique aiguë et subaiguë [Hurst]')], 'Leucoencéphalite hémorragique aiguë et subaiguë [Hurst]',
              'Sous-code de G36, sans note d’inclusion ni d’exclusion.', 'g36-adem')
add_if_absent('G36.8', [('G36.8', 'code de la CIM-10-GM 2024, intitulé : Autres affections démyélinisantes aiguës disséminées précisées')], 'Autres affections démyélinisantes aiguës disséminées précisées',
              'Sous-code de G36 ; le rattachement de la MOGAD à G36.8 ou à G37.8 n’est pas fixé par les sources lues.', 'g36-adem')
add_if_absent('G36.9', [('G36.9', 'code de la CIM-10-GM 2024, intitulé : Affection démyélinisante aiguë disséminée, sans précision')], 'Affection démyélinisante aiguë disséminée, sans précision',
              'Sous-code de G36.', 'g36-adem')
add_if_absent('G04.0', [('G04.0', 'code de la CIM-10-GM 2024, intitulé : Encéphalite aiguë disséminée')], 'Encéphalite aiguë disséminée',
              'Inclut l’encéphalite et l’encéphalomyélite post-vaccinales ; le code du vaccin s’ajoute.', 'g36-adem')
add_if_absent('G04.8', [('G04.8', 'code de la CIM-10-GM 2024, intitulé : Encéphalite et encéphalomyélite postinfectieuses sans précision')], 'Encéphalite et encéphalomyélite postinfectieuses sans précision',
              'Exclue de G36.', 'g36-adem')
add_if_absent('G37.3', [('G37.3', 'code de la CIM-10-GM 2024, intitulé : Myélite transverse aiguë dans les maladies démyélinisantes du système nerveux central')], 'Myélite transverse aiguë dans les maladies démyélinisantes du système nerveux central',
              'Code voisin de G36 dans la CIM-10-GM 2024.', 'g36-adem')
add_if_absent('G37.8', [('G37.8', 'code de la CIM-10-GM 2024, intitulé : Autres maladies démyélinisantes précisées du système nerveux central')], 'Autres maladies démyélinisantes précisées du système nerveux central',
              'Inclut l’encéphalomyélite démyélinisante aiguë (ADEM) dans la CIM-10-GM 2024.', 'g36-adem')
add_if_absent('anti-GFAP', [('anti', 'dirigé contre'), ('GFAP', 'Glial Fibrillary Acidic Protein (protéine acide fibrillaire gliale)')], 'Anticorps anti-protéine acide fibrillaire gliale',
              'Astrocytopathie auto-immune citée parmi les diagnostics différentiels de la NMOSD.', 'g36-nmosd')
add_if_absent('GFAP', [('G','Glial'),('F','Fibrillary'),('A','Acidic'),('P','Protein')], 'Protéine acide fibrillaire gliale',
              'Protéine des astrocytes ; cible des anticorps dans l’astrocytopathie auto-immune, diagnostic différentiel de la NMOSD.', 'g36-nmosd')
