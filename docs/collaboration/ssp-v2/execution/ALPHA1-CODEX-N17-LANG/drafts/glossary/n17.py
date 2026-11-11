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
              'Une baisse récente de fonction rénale est identifiée par la variation de créatinine ou par une oligurie qualifiée, selon Kidney Disease: Improving Global Outcomes, recommandation 2012.', 'n17-criteres')
add_if_absent('ERBP', [('E','European'),('R','Renal'),('B','Best'),('P','Practice')],
              'European Renal Best Practice',
              'Ce groupe européen a publié en 2012 une position sur les recommandations Kidney Disease: Improving Global Outcomes concernant l’insuffisance rénale aiguë. Ses adaptations sont attribuées séparément.', 'n17-suivi')
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

add_if_absent('FENa', [('F','Fraction'),('E','Excrétée'),('Na','Sodium')], 'Fraction excrétée du sodium', 'Ce calcul compare le sodium et la créatinine dans le sang et l’urine. Les unités, les conditions et les limites sous diurétiques sont détaillées dans la fenêtre N17.', 'n17-fen')
add_if_absent('pCO₂', [('p','pression partielle'),('C','carbone'),('O','oxygène'),('₂','deux atomes d’oxygène')], 'Pression partielle du dioxyde de carbone', 'La valeur dépend du prélèvement artériel ou veineux et de la ventilation. Les références suisses et la compensation d’une acidose métabolique sont expliquées dans la fenêtre N17.', 'n17-acidobase')
add_if_absent('StatPearls', [('StatPearls','nom propre de collection pédagogique, non une abréviation')], 'StatPearls, collection de synthèses médicales', 'Les chapitres Physiology, Renal et Histology, Nephron complètent les bases anatomiques ; ils ne constituent pas une recommandation suisse de traitement.', 'n17-pompe')

# Ajouts Claude, audit Cycle 1 du 14 octobre 2026 : noms propres signalés par l'audit des abréviations.
add_if_absent('PROFILES', [('PROFILES', 'nom propre du référentiel suisse, acronyme anglais non développé dans ce cours')],
              'PROFILES, référentiel des objectifs de formation médicale en Suisse',
              'Ce référentiel définit les situations cliniques de départ de l’examen fédéral suisse de médecine humaine. Le cours relie ici l’insuffisance rénale aiguë à ses situations 63, 161, 164 et 173.', 'n17-criteres')
add_if_absent('Tamm-Horsfall', [('Tamm-Horsfall', 'noms propres des auteurs qui ont décrit la protéine, non une abréviation')],
              'Protéine de Tamm-Horsfall, ou uromoduline',
              'Cette protéine tubulaire précipite dans la lumière et forme la matrice des cylindres urinaires. Sa précipitation dépend du pH et de la densité de l’urine.', 'n17-sediment')
add_if_absent('Michael-Joseph', [('Michael-Joseph', 'prénom composé d’un auteur, non une abréviation')],
              'Michael-Joseph F. Agbayani, auteur d’une image',
              'Ce médecin est coauteur de l’électrocardiogramme d’hyperkaliémie publié sous licence CC BY 4.0 sur Wikimedia Commons.', 'n17-hyperk')
add_if_absent('Chávez-Iñiguez', [('Chávez-Iñiguez', 'nom de famille composé d’un auteur, non une abréviation')],
              'Chávez-Iñiguez, premier auteur d’un cas publié',
              'Ce néphrologue est le premier auteur du cas publié en 2018 dans BMC Nephrology, dont la figure histologique est reproduite sous licence CC BY 4.0.', 'n17-tubule')
