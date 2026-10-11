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

add_if_absent('PHEL', [('P', 'Pharmacie'), ('H', 'Hôpitaux'), ('E', 'Est'), ('L', 'Lémanique')],
              'Pharmacie des Hôpitaux de l’Est Lémanique',
              'Cette pharmacie publie les documents institutionnels du calcium pour ses établissements partenaires. Son bulletin documente le gluconate allemand importé.', 'n17-calcium')
add_if_absent('Mini-Plasco', [('Mini-Plasco', 'nom commercial de récipient, non une abréviation')],
              'Mini-Plasco, récipient B. Braun',
              'Le catalogue allemand identifie Mini-Plasco connect de 10 mL pour Calciumgluconat B. Braun 10 %. Le récipient ne définit pas à lui seul une dose.', 'n17-calcium')
add_if_absent('Fachinfo-Service', [('Fachinfo-Service', 'nom propre d’un service documentaire, non une abréviation')],
              'Fachinfo-Service, informations professionnelles allemandes',
              'Le service héberge la Fachinformation allemande du calcium gluconate B. Braun consultée. Sa version imprimée reste juillet 2014 ; elle ne devient pas une autorisation suisse.', 'n17-calcium')
add_if_absent('PHEL.FP.217', [('PHEL', 'Pharmacie des Hôpitaux de l’Est Lémanique'), ('FP.217', 'identifiant documentaire, sans développement de lettres établi dans le document lu')],
              'Identifiant PHEL du document Médicaments contenant du calcium',
              'La fiche PHEL.FP.217 V09 est datée du 9 décembre 2025. Son identifiant et le nom du fichier ne remplacent pas la date de version imprimée.', 'n17-calcium')
add_if_absent('PHELinfos', [('PHEL', 'Pharmacie des Hôpitaux de l’Est Lémanique'), ('infos', 'partie du titre du bulletin, non une abréviation clinique')],
              'PHELinfos, bulletin de la pharmacie hospitalière',
              'Le numéro 89 de mai 2025 documente le remplacement d’anciens produits de calcium par le gluconate allemand importé. Ses observations concernent ses établissements partenaires.', 'n17-calcium')
add_if_absent('mOsm', [('m', 'milli'), ('Osm', 'osmole')], 'Milliosmole',
              'La monographie HUG exprime l’osmolarité en milliosmoles par litre. Une osmolarité compte les particules par litre de solution ; une osmolalité les rapporte à un kilogramme d’eau. Les valeurs d’une préparation ne se confondent pas avec la référence sanguine.', 'n17-calcium')

add_if_absent('FENa', [('F','Fraction'),('E','Excrétée'),('Na','Sodium')], 'Fraction excrétée du sodium', 'Ce calcul compare sodium et créatinine dans le sang et l’urine. Les unités, les conditions et les limites sous diurétiques sont détaillées dans la fenêtre N17.', 'n17-fen')
add_if_absent('pCO₂', [('p','pression partielle'),('CO₂','dioxyde de carbone')], 'Pression partielle du dioxyde de carbone', 'La valeur dépend du prélèvement artériel ou veineux et de la ventilation. Les références suisses et la compensation d’une acidose métabolique sont expliquées dans la fenêtre N17.', 'n17-acidobase')
add_if_absent('StatPearls', [('StatPearls','nom propre de collection pédagogique, non une abréviation')], 'StatPearls, collection de synthèses médicales', 'Les chapitres de physiologie et d’histologie rénales complètent les bases anatomiques ; ils ne constituent pas une recommandation suisse de traitement.', 'n17-criteres')
