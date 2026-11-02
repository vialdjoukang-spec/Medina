"""Abréviations E40 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib

_existing = {}
_here = Path(__file__).resolve().parent
_dirs = [_here] + [p / 'glossary' for p in _here.parents if (p / 'glossary' / 'cardio_1.py').exists()]
import sys
for _d in _dirs:
    if str(_d) not in sys.path:
        sys.path.append(str(_d))
    for _path in sorted(_d.glob('*.py')):
        if _path.stem in {'e40', '__init__'}:
            continue
        try:
            _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
        except Exception:
            pass

G = {}


def add_if_absent(key, letters, full, definition, window=None):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full,
                  'def': '<p>' + definition + '</p>', 'ref': window}

add_if_absent('GLIM', [('G', 'Global'), ('L', 'Leadership'), ('I', 'Initiative on'), ('M', 'Malnutrition')], 'Global Leadership Initiative on Malnutrition', 'Consensus mondial de diagnostic adulte : après dépistage, au moins un critère phénotypique et un étiologique. Ni albumine seule ni critère pédiatrique OMS.', 'e40-glim')
add_if_absent('PB', [('P', 'Périmètre'), ('B', 'Brachial')], 'Périmètre brachial', 'Mesure anthropométrique dont les seuils et la portée dépendent de l’âge ; ne pas transposer le seuil des six à cinquante-neuf mois aux nourrissons ou adultes.', 'e40-muac')
add_if_absent('RUTF', [('R', 'Ready-to-'), ('U', 'Use'), ('T', 'Therapeutic'), ('F', 'Food')], 'Aliment thérapeutique prêt à l’emploi', 'Aliment standardisé utilisé dans des phases de prise en charge de malnutrition pédiatrique ; pas une prescription universelle de tout âge.', 'e40-rutf')
add_if_absent('MAS', [('M', 'Malnutrition'), ('A', 'Aiguë'), ('S', 'Sévère')], 'Malnutrition aiguë sévère', 'Cadre OMS pédiatrique, avec critères distincts selon âge. Un œdème nutritionnel peut suffire ; le PB du jeune nourrisson n’a pas la même portée que celui des plus grands.', 'e40-nutritional-edema')
add_if_absent('F75', [('F', 'Formule thérapeutique'), ('75', '75 kcal pour 100 mL')], 'Lait thérapeutique F75', 'Lait thérapeutique de stabilisation dans le guide OMS/UNICEF 2026 des six à cinquante-neuf mois ; les quantités se prescrivent selon phase et tolérance.', 'e40-stabilization')
add_if_absent('F100', [('F', 'Formule thérapeutique'), ('100', '100 kcal pour 100 mL')], 'Lait thérapeutique F100', 'Lait thérapeutique utilisé notamment dans la transition, selon le guide pédiatrique ; pas une dose de renutrition adulte.', 'e40-transition')
add_if_absent('ClCr', [('Cl', 'Clairance'), ('Cr', 'Créatinine')], 'Clairance de la créatinine', 'Paramètre de fonction rénale utilisé dans certaines tables de FI ; population, méthode et unité doivent être conservées.', 'e40-amoxicillin')
add_if_absent('IMCI', [('I', 'Integrated'), ('M', 'Management of'), ('C', 'Childhood'), ('I', 'Illness')], 'Prise en charge intégrée des maladies de l’enfant', 'Sigle anglais du cadre pédiatrique OMS utilisé pour les signes de danger. Un signe de danger modifie le triage ; les critères dépendent du circuit et de l’âge.', 'e40-admission')
add_if_absent('FELANPE', [('FELANPE', 'Federación Latinoamericana de Terapia Nutricional, Nutrición Clínica y Metabolismo')], 'Fédération latino-américaine de thérapie nutritionnelle, nutrition clinique et métabolisme', 'Une des quatre sociétés participantes au consensus mondial GLIM ; ce sigle identifie la provenance, sans créer une recommandation nationale suisse.', 'e40-glim')
add_if_absent('PENSA', [('P', 'Parenteral and'), ('E', 'Enteral'), ('N', 'Nutrition'), ('S', 'Society of'), ('A', 'Asia')], 'Parenteral and Enteral Nutrition Society of Asia', 'Société asiatique participante au consensus mondial GLIM aux côtés des trois autres organisations citées.', 'e40-glim')
add_if_absent('JPEN', [('J', 'Journal of'), ('P', 'Parenteral and'), ('E', 'Enteral'), ('N', 'Nutrition')], 'Journal of Parenteral and Enteral Nutrition', 'Revue où paraît la mise à jour GLIM2025 ; le lieu de publication et le caractère mondial conjoint du consensus sont explicitement distingués.', 'e40-glim')
