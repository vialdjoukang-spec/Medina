"""Abréviations N17 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'n17', '__init__'}:
        continue
    _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
G = {}
def add_if_absent(key, letters, full, definition, window):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full,
                  'def': '<p>' + definition + '</p>', 'ref': window}
add_if_absent('IRA', [('I','Insuffisance'),('R','Rénale'),('A','Aiguë')],
              'Insuffisance rénale aiguë',
              'Une baisse récente de fonction rénale est identifiée par la variation de créatinine ou par une oligurie qualifiée, selon KDIGO 2012.', 'n17-criteres')
add_if_absent('ERBP', [('E','European'),('R','Renal'),('B','Best'),('P','Practice')],
              'European Renal Best Practice',
              'Ce groupe européen a publié en 2012 une position sur les recommandations KDIGO concernant l’insuffisance rénale aiguë. Ses adaptations sont attribuées séparément.', 'n17-suivi')
add_if_absent('UKKA', [('U','United'),('K','Kingdom'),('K','Kidney'),('A','Association')],
              'United Kingdom Kidney Association',
              'Cette association britannique a publié en 2023 une recommandation finale pour l’hyperkaliémie chez l’adulte. Elle fonde les repères d’urgence explicitement attribués.', 'n17-hyperk')

add_if_absent('HM', [('H','Humaine'),('M','Monocomposée')], 'Insuline humaine monocomposée', 'La notice suisse commune décrit Actrapid HM, une solution soluble, et Insulatard HM, une suspension retard. Leurs voies ne sont pas interchangeables.', 'n17-insuline')
