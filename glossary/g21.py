"""Abréviations G21 (Alpha77 ; auto-relecture Sol-Neurologie-G21) ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'g21', '__init__'}:
        continue
    try:
        _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
    except Exception:
        pass
G = {}
def add_if_absent(key, letters, full, definition, window=None):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full, 'def': '<p>' + definition + '</p>', 'ref': window}
add_if_absent('DAT', [('DA', 'dopamine'), ('T', 'transporter : transporteur')], 'Transporteur de la dopamine', 'Protéine présynaptique explorée par imagerie ; distincte du récepteur D2. Une préservation peut soutenir une forme surtout postsynaptique, sans résoudre seule toutes les causes.', 'g21-dat')
add_if_absent('SMN', [('S', 'syndrome'), ('M', 'malin'), ('N', 'des neuroleptiques')], 'Syndrome malin des neuroleptiques', 'Urgence médicamenteuse potentiellement grave ; présentation variable et absence de test unique spécifique.', 'g21-nms')
add_if_absent('CK', [('C', 'créatine'), ('K', 'kinase')], 'Créatine kinase', 'Enzyme pouvant augmenter lors de lésion musculaire ; ni confirmation ni exclusion isolée du syndrome malin.', 'g21-ck')
add_if_absent('GPi', [('GP', 'globus pallidus'), ('i', 'interne')], 'Segment interne du globus pallidus', 'Noyau de sortie dans le modèle de boucle motrice ; différent du segment externe GPe.', 'g21-network')
add_if_absent('GPe', [('GP', 'globus pallidus'), ('e', 'externe')], 'Segment externe du globus pallidus', 'Structure pallidale impliquée dans les boucles de régulation motrice.', 'g21-network')
add_if_absent('STN', [('ST', 'subthalamic : sous-thalamique'), ('N', 'nucleus : noyau')], 'Noyau sous-thalamique', 'Structure nommée sur la planche humaine de référence, distincte de la substance noire.', 'g21-network')
add_if_absent('SN', [('S', 'substantia : substance'), ('N', 'nigra : noire')], 'Substance noire', 'Structure mésencéphalique de la boucle ; une image pigmentée ne mesure pas la dopamine.', 'g21-dopamine')
add_if_absent('LIQ', [('LIQ', 'désignation de forme dispersible du produit')], 'Madopar LIQ', 'Comprimé dispersible avec quantité propre de lévodopa et de bensérazide ; ne pas assimiler la dispersion à une solution à concentration fixe.', 'g21-calculation')
add_if_absent('CYP3A4', [('CYP', 'cytochrome P450'), ('3A4', 'désignation de famille, sous-famille et isoforme')], 'Cytochrome P450 3A4', 'Enzyme impliquée dans le métabolisme de bromocriptine ; inhibiteurs puissants ou modérés contre-indiqués avec Parlodel selon FI mai 2020.', 'g21-bromocriptine')
