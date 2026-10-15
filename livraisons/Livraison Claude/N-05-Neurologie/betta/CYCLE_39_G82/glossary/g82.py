from cardio_1 import a, G
# G82 — Paraparésie et paraplégie, tétraparésie et tétraplégie (N-05-Neurologie). Entrées conditionnelles : aucun terme existant n’est écrasé.
from pathlib import Path
import importlib
_ex = set(G)
for _p in sorted(Path(__file__).parent.glob('*.py')):
    if _p.stem in {'g82', '__init__', 'cardio_1'}:
        continue
    try:
        _ex |= set(getattr(importlib.import_module(_p.stem), 'G', {}))
    except Exception:
        pass
def ac(k, lit, full, d, ref=None):
    if k not in _ex:
        a(k, lit, full, d, ref)

ac('ISNCSCI', [('IS','International Standards'),('N','for Neurological'),('C','Classification'),('SCI','of Spinal Cord Injury')], 'Normes internationales de classification neurologique des lésions médullaires', '<p>Examen standardisé qui note la force de dix muscles clés et la sensibilité en 28 points par côté, puis les fonctions des segments sacrés les plus bas. Il fournit le niveau neurologique lésionnel, la complétude et le grade AIS. La révision de 2019 est celle citée dans la leçon.</p>', 'g82-isncsci')
ac('AIS', [('A','ASIA'),('I','Impairment'),('S','Scale')], 'Échelle de déficience de l’ASIA (association américaine des lésions médullaires)', '<p>Échelle à cinq grades, A (complet) à E (normal), qui classe la gravité neurologique d’une lésion médullaire à partir de l’épargne sacrée et de la motricité sous le niveau lésionnel.</p>', 'g82-ais')
ac('ASIA', [('A','American'),('S','Spinal'),('I','Injury'),('A','Association')], 'Association américaine des lésions médullaires', '<p>Société qui a donné son nom à l’échelle de déficience AIS utilisée dans la classification internationale.</p>', 'g82-ais')
ac('ZPP', [('Z','Zone de'),('P','Préservation'),('P','Partielle')], 'Zone de préservation partielle', '<p>Segment le plus caudal qui conserve une fonction, rapporté pour quatre catégories, lorsque la contraction anale volontaire ou les fonctions sensitives sacrées sont absentes.</p>', 'g82-zpp')
ac('DAP', [('D','Pression anale'),('A','profonde, en anglais'),('P','Deep Anal Pressure')], 'Pression anale profonde', '<p>Perception d’une pression exercée dans l’anus lors du toucher rectal. Avec le tact et la piqûre aux segments sacrés 4 et 5 et la contraction anale volontaire, elle définit l’épargne sacrée.</p>', 'g82-sacre')
ac('SwiSCI', [('Swi','Swiss'),('S','Spinal'),('C','Cord'),('I','Injury cohort')], 'Cohorte suisse des lésions médullaires', '<p>Étude de cohorte nationale qui suit les personnes avec lésion médullaire dans les centres spécialisés suisses et en communauté. Ses publications fournissent les chiffres suisses de mortalité, de comorbidité et de recours aux soins cités dans la leçon.</p>', 'g82-incidence')
ac('SMR', [('S','Standardized'),('M','Mortality'),('R','Ratio')], 'Rapport standardisé de mortalité', '<p>Rapport entre les décès observés dans un groupe et ceux attendus dans la population de référence, à âge et sexe égaux. Une valeur de 2,32 signifie une mortalité 2,32 fois supérieure.</p>', 'g82-mortalite')
ac('EMSCI', [('EM','European Multicenter'),('S','Study about'),('C','Spinal Cord'),('I','Injury')], 'Étude européenne multicentrique sur les lésions médullaires', '<p>Cohorte dans laquelle l’applicabilité de la zone de préservation partielle révisée en 2019 a été évaluée.</p>', 'g82-zpp')
ac('BfArM', [('BfArM','nom allemand de l’institut éditeur de la CIM-10-GM ; développement lettre à lettre non fourni par le dossier de lecture')], 'Institut allemand éditeur de la CIM-10-GM', '<p>Éditeur de la classification CIM-10-GM 2024 dont les catégories G82 et G83.4 sont citées dans la leçon.</p>', 'g82-codage')
ac('CIM-10-GM', [('CIM','Classification Internationale des Maladies'),('10','dixième révision'),('GM','German Modification, modification allemande')], 'Classification internationale des maladies, 10e révision, modification allemande', '<p>Version de la classification utilisée par le catalogue de MEDINA (édition 2024). La correspondance avec la CIM-11 n’est pas vérifiée.</p>', 'g82-codage')
ac('CIM', [('C','Classification'),('I','Internationale des'),('M','Maladies')], 'Classification internationale des maladies', '<p>Système de codage des diagnostics ; la leçon utilise la version 10 modifiée pour l’Allemagne.</p>', 'g82-codage')
ac('AO', [('AO Spine','nom de la fondation, tel que cité par les lignes directrices ; développement lettre à lettre non fourni par le dossier de lecture')], 'Fondation AO Spine (Davos)', '<p>Fondation internationale qui, avec le réseau Praxis, a publié les lignes directrices sur la lésion médullaire aiguë citées dans la leçon. Ces lignes directrices ne sont pas européennes.</p>', 'g82-decompression')
ac('BMJ', [('BMJ','nom de revue, non développé lettre à lettre dans le dossier de lecture')], 'Revue BMJ Open', '<p>Revue médicale dans laquelle ont paru deux études citées dans la leçon.</p>')
ac('BMC', [('BMC','nom de revue, non développé lettre à lettre dans le dossier de lecture')], 'Revue BMC Health Services Research', '<p>Revue dans laquelle a paru l’étude suisse sur l’aide à domicile.</p>')
ac('PAD', [('P','Pression'),('A','Artérielle'),('D','Diastolique')], 'Pression artérielle diastolique', '<p>Pression minimale dans les artères entre deux battements ; elle monte de plus de 10 mmHg dans les trois quarts des épisodes de dysréflexie d’une étude observationnelle.</p>', 'g82-da')
ac('AWMF', [('AWMF','nom allemand de la fédération des sociétés savantes ; développement non fourni par le dossier')], 'Fédération allemande des sociétés médicales savantes', '<p>Éditrice de guides de pratique clinique allemands.</p>')
# Codes CIM décimaux (déclaration exigée par l’audit)
_codes = {
 'G82.0':'Paraparésie et paraplégie flasques','G82.1':'Paraparésie et paraplégie spastiques','G82.2':'Paraparésie et paraplégie, sans précision',
 'G82.3':'Tétraparésie et tétraplégie flasques','G82.4':'Tétraparésie et tétraplégie spastiques','G82.5':'Tétraparésie et tétraplégie, sans précision',
 'G82.6':'Niveau fonctionnel de la lésion médullaire (code supplémentaire)','G82.12':'Paraplégie spastique chronique complète',
 'G82.60':'Niveau fonctionnel : 1er au 3e cervical','G82.61':'Niveau fonctionnel : 4e et 5e cervicaux','G82.62':'Niveau fonctionnel : 6e au 8e cervical',
 'G82.63':'Niveau fonctionnel : 1er au 6e thoracique','G82.64':'Niveau fonctionnel : 7e au 10e thoracique','G82.65':'Niveau fonctionnel : 11e thoracique au 1er lombaire',
 'G82.66':'Niveau fonctionnel : 2e lombaire au 1er sacré','G82.67':'Niveau fonctionnel : 2e au 5e sacré','G82.69':'Niveau fonctionnel non précisé',
 'G83.4':'Syndrome de la queue de cheval','G83.40':'Syndrome de la queue de cheval, complet','G83.41':'Syndrome de la queue de cheval, incomplet','G83.49':'Syndrome de la queue de cheval, sans précision',
 'G95.8':'Code associé à G83.4 pour la vessie neurogène','Z99.1':'Dépendance de longue durée à la ventilation',
}
for _k, _v in _codes.items():
    ac(_k, [(_k, 'code CIM-10-GM 2024 — ' + _v)], _v, '<p>Code de la CIM-10-GM 2024 cité dans la leçon : ' + _v + '.</p>', 'g82-codage')
ac('Brown-Séquard', [('Brown-Séquard','nom propre de deux médecins éponymes ; non développable lettre à lettre')], 'Syndrome de Brown-Séquard', '<p>Syndrome médullaire qui associe un déficit moteur et proprioceptif du côté de la lésion à un déficit thermo-algique du côté opposé ; la forme pure est rare.</p>', 'g82-syndromes')
