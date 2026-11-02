"""Abréviations D77 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'d77', '__init__'}:
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

add_if_absent('HSS',[('H', 'Hepato- (hépato-)'), ('S', 'Splenic (splénique)'), ('S', 'Schistosomiasis (schistosomiase)')],'Schistosomiase hépatosplénique','Forme associant notamment fibrose périportale, hypertension portale présinusoïdale et splénomégalie. Une fonction hépatique relativement préservée n’exclut pas des varices graves. Source : revue HSS 2021.','d77-exp-3')
add_if_absent('PSVD',[('P', 'Porto-'), ('S', 'Sinusoidal (sinusoïdale)'), ('V', 'Vascular (vasculaire)'), ('D', 'Disease (maladie)')],'Maladie vasculaire porto-sinusoïdale','La définition EASL 2026 exclut explicitement la schistosomiase. Une hypertension portale non cirrhotique ne suffit donc pas à attribuer cette étiquette.','d77-exp-10')
add_if_absent('PALS',[('P', 'PeriArteriolar (périartériolaire)'), ('L', 'Lymphoid (lymphoïde)'), ('S', 'Sheath (gaine)')],'Gaine lymphoïde périartériolaire','Structure de la pulpe blanche indiquée dans la légende de la photographie humaine de Gleiberg. L’image normale n’est pas un cas de fibrose D77.',None)
add_if_absent('GTIN',[('G', 'Global'), ('T', 'Trade'), ('I', 'Item'), ('N', 'Number')],'Numéro international d’identification d’un article','Identifiant utilisé pour préciser la présentation dont la FI suisse a été consultée, sans prouver sa disponibilité actuelle.',None)
add_if_absent('H&E',[('H', 'Hématoxyline'), ('&', 'et'), ('E', 'Éosine')],'Coloration hématoxyline-éosine','Coloration de l’original histologique humain de rate. L’organisation observée ne mesure pas la pression portale ou l’immunité individuelle.',None)
add_if_absent('OAMéd',[('OA', 'Ordonnance sur les autorisations'), ('Méd', 'dans le domaine des médicaments')],'Ordonnance sur les autorisations dans le domaine des médicaments','L’article 49 encadre certaines importations professionnelles. Vérifier conditions Swissmedic et produit réel ; aucune autorisation individuelle n’est accordée ici.','d77-cas-3')
add_if_absent('AmiKo',[('AmiKo', 'Nom de la base documentaire')],'Base d’information sur les médicaments','Base consultée pour les FI exactes et la recherche datée praziquantel/Biltricide. Une recherche sans résultat ne prouve pas une indisponibilité définitive.','d77-cas-3')
add_if_absent('D77',[('D77', 'Catégorie de manifestation, usage astérisque')],'Autres maladies du sang et des organes hématopoïétiques au cours de maladies classées ailleurs','Inclusion : fibrose splénique due à la schistosomiase B65.-†, CIM-10-GM suisse 2024. Aucun sous-code D77.x ; diagnostic et cause précèdent le codage.','d77-exp-1')
