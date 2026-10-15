"""Abréviations I65 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'i65', '__init__'}:
        continue
    _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
G = {}
def add_if_absent(key, letters, full, definition, window):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full,
                  'def': '<p>' + definition + '</p>', 'ref': window}

add_if_absent('NASCET', [('N','North (nord)'),('A','American (américain)'),('S','Symptomatic (symptomatique)'),('C','Carotid (carotidienne)'),('E','Endarterectomy (endartériectomie)'),('T','Trial (essai)')],
              'Essai nord-américain sur l’endartériectomie carotidienne symptomatique',
              'Le nom de cet essai désigne la méthode de référence des degrés de sténose carotidienne dans la ligne directrice de l’European Stroke Organisation : légère (moins de 50 %), modérée (50 à 69 %), serrée (70 à 99 %) et quasi-occlusion.', 'i65-nascet')
add_if_absent('ACST-2', [('A','Asymptomatic (asymptomatique)'),('C','Carotid (carotidienne)'),('S','Surgery (chirurgie)'),('T','Trial (essai)'),('2','numéro 2')],
              'Essai de chirurgie carotidienne asymptomatique, numéro 2',
              'Cet essai a comparé le stenting à l’endartériectomie chez 3625 patients avec une sténose carotidienne asymptomatique ; décès ou AVC à 30 jours : 3,7 % contre 2,7 %.', 'i65-ecst2')
add_if_absent('ACT-1', [('A','Asymptomatic (asymptomatique)'),('C','Carotid (carotidienne)'),('T','Trial (essai)'),('1','numéro 1')],
              'Essai carotidien asymptomatique, numéro 1',
              'Cet essai a comparé le stenting à l’endartériectomie dans la sténose carotidienne asymptomatique : 3,2 % contre 2,5 % d’AVC, de décès ou d’infarctus du myocarde à 30 jours, différence non significative.', 'i65-ecst2')
add_if_absent('CREST', [('C','Carotid (carotidienne)'),('R','Revascularization (revascularisation)'),('E','Endarterectomy (endartériectomie)'),('S','versuS (contre)'),('T','Stenting Trial (essai de stenting)')],
              'Essai de revascularisation carotidienne : endartériectomie contre stenting',
              'Cet essai a comparé le stenting et l’endartériectomie ; le critère composé à 30 jours était de 3,7 % pour le stenting et de 3,6 % pour l’endartériectomie dans la sténose asymptomatique.', 'i65-ecst2')
add_if_absent('SPACE-2', [('S','Stent'),('P','Protected (protégée)'),('A','Angioplasty (angioplastie)'),('C','versus Carotid (contre carotidienne)'),('E','Endarterectomy (endartériectomie)'),('2','numéro 2')],
              'Essai d’angioplastie avec stent contre endartériectomie carotidienne, numéro 2',
              'Cet essai, arrêté prématurément (513 patients), n’a pas montré de différence entre traitement médical seul et revascularisation à un an ni à cinq ans.', 'i65-ecst2')
add_if_absent('ECST-2', [('E','European (européen)'),('C','Carotid (carotidien)'),('S','Surgery (chirurgie)'),('T','Trial (essai)'),('2','numéro 2')],
              'Second essai européen de chirurgie carotidienne',
              'Cet essai a comparé le traitement médical optimisé seul à ce traitement associé à la revascularisation chez 429 patients à risque faible ou intermédiaire ; il n’a pas montré de bénéfice de la revascularisation à deux ans.', 'i65-ecst2')
add_if_absent('ICSS', [('I','International (international)'),('C','Carotid (carotidienne)'),('S','Stenting'),('S','Study (étude)')],
              'Étude internationale sur le stenting carotidien',
              'Cette étude est citée pour l’IRM de diffusion après revascularisation : 50 % de nouvelles lésions après stenting contre 17 % après endartériectomie.', 'i65-dwi')
add_if_absent('EVA-3S', [('E','Endarterectomy (endartériectomie)'),('V','Versus (contre)'),('A','Angioplasty (angioplastie)'),('3S','in patients with Symptomatic Severe carotid Stenosis (chez les patients atteints de sténose carotidienne symptomatique et serrée)')],
              'Endartériectomie contre angioplastie chez les patients avec sténose carotidienne symptomatique serrée',
              'Cet essai est cité par la ligne directrice de l’European Stroke Organisation dans le contexte de la comparaison entre stenting et endartériectomie ; son texte n’a pas été lu dans ce cours.', 'i65-age-technique')
add_if_absent('SAMMPRIS', [('S','Stenting and (et)'),('A','Aggressive (agressive)'),('M','Medical (médicale)'),('M','Management (prise en charge) for (pour)'),('P','Preventing (prévenir)'),('R','Recurrent stroke (AVC récidivant)'),('I','in Intracranial (intracrânienne)'),('S','Stenosis (sténose)')],
              'Stenting et prise en charge médicale agressive pour prévenir l’AVC récidivant dans la sténose intracrânienne',
              'Cet essai est cité pour 20,8 % d’AVC ischémique périprocédural lors du stenting de la sténose basilaire.', 'i65-cochrane-vert')
add_if_absent('VIST', [('V','Vertebral (vertébrale)'),('I','Ischaemia (ischémie)'),('S','Stenting'),('T','Trial (essai)')],
              'Essai de stenting dans l’ischémie vertébrale',
              'Cet essai est cité dans une méta-analyse de données individuelles ; le rapport de risque d’AVC est de 0,40 (0,14 à 1,13), non significatif.', 'i65-cochrane-vert')
add_if_absent('VAST', [('V','Vertebral (vertébrale)'),('A','Artery (artère)'),('S','Stenting'),('T','Trial (essai)')],
              'Essai de stenting de l’artère vertébrale',
              'Cet essai est cité, avec VIST et SAMMPRIS, dans la méta-analyse de données individuelles : risque périprocédural de 16 % en intracrânien contre 1 % en extracrânien.', 'i65-cochrane-vert')
