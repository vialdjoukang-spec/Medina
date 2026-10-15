"""Abréviations G06 (cycle Betta 34) ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'g06', '__init__'}:
        continue
    try:
        _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
    except Exception:
        pass
G = {}
def add_if_absent(key, letters, full, definition, window=None):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full, 'def': '<p>' + definition + '</p>', 'ref': window}
add_if_absent('DGN', [('D','Deutsche (allemande)'),('G','Gesellschaft (société)'),('N','für Neurologie (de neurologie)')],
              'Société allemande de neurologie',
              'La Deutsche Gesellschaft für Neurologie a publié en 2021 la ligne directrice S1 sur l’abcès cérébral (AWMF 030/108), co-signée par la Société suisse de neurologie. Sa validité est échue depuis le 31.12.2025.', 'g06-sources')
add_if_absent('SNG', [('S','Schweizerische (suisse)'),('N','Neurologische (de neurologie)'),('G','Gesellschaft (société)')],
              'Société suisse de neurologie',
              'La Schweizerische Neurologische Gesellschaft a co-signé la ligne directrice allemande de 2021 sur l’abcès cérébral, par W. Z’Graggen (Inselspital Berne).', 'g06-sources')
add_if_absent('QJM', [('Q','Quarterly (trimestriel)'),('J','Journal (revue)'),('M','of Medicine (de médecine)')],
              'Quarterly Journal of Medicine',
              'Revue médicale dans laquelle Sendi, Bregenzer et Zimmerli (Liestal) ont publié en 2008 une revue de pratique sur l’abcès épidural spinal.')
add_if_absent('G06.0', [('G06','catégorie CIM-10-GM de l’abcès et du granulome intracrâniens et intrarachidiens'),('.0','abcès et granulome intracrâniens')],
              'Code CIM-10-GM 2024 : abcès et granulome intracrâniens',
              'Il inclut l’abcès embolique du cerveau (otogène, cérébelleux, cérébral) et l’abcès ou le granulome intracrânien épidural, extradural ou sous-dural.', 'g06-codage')
add_if_absent('G06.1', [('G06','catégorie CIM-10-GM de l’abcès et du granulome intracrâniens et intrarachidiens'),('.1','abcès et granulome intrarachidiens')],
              'Code CIM-10-GM 2024 : abcès et granulome intrarachidiens',
              'Il inclut l’abcès embolique de la moelle et l’abcès ou le granulome intrarachidien épidural, extradural ou sous-dural.', 'g06-codage')
add_if_absent('G06.2', [('G06','catégorie CIM-10-GM de l’abcès et du granulome intracrâniens et intrarachidiens'),('.2','abcès extradural et sous-dural, sans précision')],
              'Code CIM-10-GM 2024 : abcès extradural et sous-dural, sans précision',
              'Il s’emploie lorsque la localisation précise de la collection extradurale ou sous-durale n’est pas indiquée.', 'g06-codage')
add_if_absent('A06.6', [('A06','amibiase'),('.6','abcès amibien du cerveau')], 'Code CIM-10-GM 2024 : abcès amibien du cerveau (A06.6†)',
              'Cet abcès relève de la catégorie G07* et n’est pas codé en G06.', 'g06-codage')
add_if_absent('A54.8', [('A54','infection gonococcique'),('.8','autres infections gonococciques, dont l’abcès cérébral')], 'Code CIM-10-GM 2024 : abcès cérébral gonococcique (A54.8†)',
              'Cet abcès relève de la catégorie G07* et n’est pas codé en G06.', 'g06-codage')
add_if_absent('A17.8', [('A17','tuberculose du système nerveux'),('.8','autres formes, dont le tuberculome cérébral')], 'Code CIM-10-GM 2024 : tuberculome cérébral (A17.8†)',
              'Cette lésion relève de la catégorie G07* et n’est pas codée en G06.', 'g06-codage')
add_if_absent('A17.1', [('A17','tuberculose du système nerveux'),('.1','tuberculome méningé')], 'Code CIM-10-GM 2024 : tuberculome méningé (A17.1†)',
              'Cette lésion relève de la catégorie G07* et n’est pas codée en G06.', 'g06-codage')
