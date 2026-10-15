"""Abréviations G03 — Méningite due à des causes autres et non précisées ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'g03', '__init__'}:
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

add_if_absent('DGN', [('D', 'Deutsche'), ('G', 'Gesellschaft'), ('N', 'für Neurologie')],
              'Deutsche Gesellschaft für Neurologie (Société allemande de neurologie)',
              'Cette société savante allemande publie, avec l’AWMF, les recommandations 030/100 (méningo-encéphalite virale, 2025) et 030/089 (méningo-encéphalite bactérienne de l’adulte, 2023) sur lesquelles repose ce cours. Ce sont des recommandations allemandes, non suisses.', 'g03-sources-guides')
add_if_absent('HSV', [('H', 'Herpes'), ('S', 'Simplex'), ('V', 'Virus')],
              'Virus de l’herpès simplex',
              'Deux types existent : HSV-1 et HSV-2. HSV-2 est l’agent le plus étroitement lié à la méningite récurrente de Mollaret ; l’encéphalite herpétique est l’indication de l’aciclovir par voie intraveineuse.', 'g03-hsv2')
add_if_absent('JC', [('JC', 'nom d’usage du virus JC, non développé lettre à lettre dans les sources lues')],
              'Virus JC',
              'La recommandation allemande de 2025 le liste parmi les cibles de la PCR sur liquide céphalo-rachidien non centrifugé, avec les herpèsvirus, les flavivirus et les entérovirus.', 'g03-pcr')
add_if_absent('NMDAR', [('N', 'N-méthyl-'), ('M', ''), ('D', 'D-'), ('A', 'aspartate'), ('R', 'Récepteur')],
              'Récepteur du N-méthyl-D-aspartate',
              'Des anticorps dirigés contre ce récepteur caractérisent une forme d’encéphalite auto-immune, à rechercher selon la recommandation virale lorsqu’aucun agent n’est identifié.', 'g03-sources-guides')
add_if_absent('CASPR2', [('CASPR2', 'Contactin-Associated Protein-like 2 : nom d’usage, non développé lettre à lettre')],
              'Contactin-associated protein-like 2',
              'Des anticorps dirigés contre cette protéine caractérisent une forme d’encéphalite auto-immune, à rechercher lorsqu’aucun agent n’est identifié.', 'g03-sources-guides')
add_if_absent('LGI1', [('LGI1', 'Leucine-rich Glioma-Inactivated 1 : nom d’usage, non développé lettre à lettre')],
              'Leucine-rich glioma-inactivated 1',
              'Des anticorps dirigés contre cette protéine caractérisent une forme d’encéphalite auto-immune, à rechercher lorsqu’aucun agent n’est identifié.', 'g03-sources-guides')
for _k, _t, _w in [
    ('G03.0', 'Méningite à liquide clair (inclut la méningite abactérienne)', 'g03-codage'),
    ('G03.1', 'Méningite chronique', 'g03-codage'),
    ('G03.2', 'Méningite récurrente bénigne [Mollaret]', 'g03-codage'),
    ('G03.8', 'Méningite due à d’autres causes précisées', 'g03-codage'),
    ('G03.9', 'Méningite, sans précision (inclut l’arachnoïdite spinale sans précision)', 'g03-codage'),
    ('B00.4', 'Encéphalite herpétique', 'g03-encephalite'),
]:
    add_if_absent(_k, [(_k, 'code de la CIM-10-GM 2024, non une abréviation')], _t,
                  'Code de la CIM-10-GM 2024 : ' + _t + '.', _w)
for _k, _t, _w in [
    ('Yelehe-Okouma', 'Yelehe-Okouma et collaborateurs, revue sur la méningite aseptique médicamenteuse, Fundam Clin Pharmacol 2018', 'g03-medic'),
    ('Martínez-Girón', 'Martínez-Girón et Pantanowitz, cytologie du liquide céphalo-rachidien dans les atteintes méningées aseptiques non malignes, Diagn Cytopathol 2017', 'g03-cell-mollaret'),
    ('Ibuprofen-Mepha', 'Ibuprofen-Mepha Teva, comprimés pelliculés : information professionnelle suisse, mise à jour de décembre 2024', 'g03-d-ibuprofene'),
    ('Valaciclovir-Mepha', 'Valaciclovir-Mepha 500/1000 Lactab® : information professionnelle suisse, mise à jour de décembre 2025', 'g03-d-valaciclovir'),
]:
    add_if_absent(_k, [(_k, 'nom propre d’un auteur ou d’un produit, non une abréviation')], _t,
                  'Référence citée dans ce cours : ' + _t + '.', _w)
