from cardio_1 import a, G
# E46 — Malnutrition protéino-énergétique, sans précision (E-06-Endocrinologie et métabolisme). Entrées conditionnelles : aucun terme existant n’est écrasé.
from pathlib import Path
import importlib
_ex = set(G)
for _p in sorted(Path(__file__).parent.glob('*.py')):
    if _p.stem in {'e46', '__init__', 'cardio_1'}:
        continue
    try:
        _ex |= set(getattr(importlib.import_module(_p.stem), 'G', {}))
    except Exception:
        pass
def ac(k, lit, full, d, ref=None):
    if k not in _ex:
        a(k, lit, full, d, ref)
ac('GLIM', [('G','Global'),('L','Leadership'),('I','Initiative on'),('M','Malnutrition')], 'Initiative mondiale de leadership sur la malnutrition', '<p>Consensus des sociétés de nutrition clinique du monde entier qui définit le diagnostic de malnutrition de l’adulte : au moins un critère phénotypique et un critère étiologique après un dépistage positif.</p>', 'e46-glim')
ac('ESPEN', [('E','European'),('S','Society for'),('P','Parenteral and'),('E','Enteral'),('N','Nutrition')], 'Société européenne de nutrition clinique et métabolisme (sigle historique : nutrition parentérale et entérale)', '<p>Société savante européenne dont les recommandations de 2018 sur les patients polymorbides de médecine interne fournissent les repères énergétiques et protéiques de la leçon.</p>', 'e46-cachexie')
ac('EFFORT', [('E','Effect of early nutritional support on'),('F','Frailty,'),('F','Functional outcomes'),('O','and'),('R','Recovery of malnourished medical inpatients'),('T','Trial')], 'Essai suisse sur le soutien nutritionnel précoce individualisé des patients hospitalisés dénutris', '<p>Essai randomisé mené dans huit hôpitaux suisses : un soutien individualisé débuté en 48 heures réduit les événements défavorables et la mortalité à 30 jours.</p>', 'e46-effort')
ac('NRS', [('N','Nutritional'),('R','Risk'),('S','Screening')], 'Dépistage du risque nutritionnel', '<p>Outil de dépistage dont la version 2002 cote l’état nutritionnel et la sévérité de la maladie de 0 à 3, avec un point à partir de 70 ans ; un score d’au moins 3 indique un risque.</p>', 'e46-nrs')
ac('MNA-SF', [('MNA','Mini Nutritional Assessment'),('SF','Short Form (forme courte)')], 'Évaluation nutritionnelle mini, forme courte', '<p>Outil de dépistage nutritionnel validé, cité par le consensus GLIM parmi les outils de première étape.</p>', 'e46-glim')
ac('MUST', [('M','Malnutrition'),('U','Universal'),('S','Screening'),('T','Tool')], 'Outil universel de dépistage de la malnutrition', '<p>Outil de dépistage nutritionnel validé, cité par le consensus GLIM parmi les outils de première étape.</p>', 'e46-glim')
ac('ET', [('É','Écart'),('T','Type (écart-type)')], 'Écart-type', '<p>Mesure de la distance d’une valeur à la moyenne de la population de référence. La note du bloc E40–E46 classe la gravité en écarts-types du poids sous la moyenne.</p>', 'e46-bloc')
ac('CIM', [('C','Classification'),('I','Internationale des'),('M','Maladies')], 'Classification internationale des maladies', '<p>Classification de l’Organisation mondiale de la Santé. La leçon utilise sa version allemande modifiée CIM-10-GM 2024.</p>', 'e46-codage')
ac('E44.0', [('E','Chapitre des maladies endocriniennes, nutritionnelles et métaboliques'),('44.0','Malnutrition protéino-énergétique modérée')], 'Code CIM-10-GM : malnutrition protéino-énergétique modérée', '<p>Poids de 2 à moins de 3 écarts-types sous la moyenne de la population de référence.</p>', 'e46-codage')
ac('E44.1', [('E','Chapitre des maladies endocriniennes, nutritionnelles et métaboliques'),('44.1','Malnutrition protéino-énergétique légère')], 'Code CIM-10-GM : malnutrition protéino-énergétique légère', '<p>Poids de 1 à moins de 2 écarts-types sous la moyenne de la population de référence.</p>', 'e46-codage')
ac('E64.0', [('E','Chapitre des maladies endocriniennes, nutritionnelles et métaboliques'),('64.0','Séquelles de malnutrition protéino-énergétique')], 'Code CIM-10-GM : séquelles de malnutrition protéino-énergétique', '<p>Exclu du bloc E40–E46 par la classification.</p>', 'e46-bloc')
ac('DXA', [('D','Dual-energy'),('X','X-ray'),('A','Absorptiometry')], 'Absorptiométrie à rayons X en double énergie', '<p>Technique qui distingue la masse maigre de la masse grasse ; recommandée par la guidance GLIM de 2022 pour apprécier la masse musculaire lorsqu’elle est disponible.</p>', 'e46-musc')
ac('BIA', [('B','Bioelectrical'),('I','Impedance'),('A','Analysis')], 'Analyse d’impédance bioélectrique', '<p>Technique d’estimation de la masse maigre par la conduction d’un courant faible ; recommandée par la guidance GLIM de 2022 lorsqu’elle est disponible.</p>', 'e46-musc')
ac('CT', [('C','Computed'),('T','Tomography')], 'Tomodensitométrie', '<p>Imagerie en coupes qui permet de mesurer la masse musculaire ; recommandée par la guidance GLIM de 2022 lorsqu’elle est disponible.</p>', 'e46-musc')
ac('FFMI', [('F','Fat'),('F','Free'),('M','Mass'),('I','Index')], 'Indice de masse maigre sans graisse', '<p>Masse maigre rapportée au carré de la taille, en kg/m². Exemples de seuils GLIM : moins de 17 chez l’homme, moins de 15 chez la femme.</p>', 'e46-musc')
ac('ASMI', [('A','Appendicular'),('S','Skeletal'),('M','Muscle'),('I','Index')], 'Indice de masse musculaire squelettique appendiculaire', '<p>Masse musculaire des membres rapportée au carré de la taille ; seuils EWGSOP : moins de 7,26 kg/m² chez l’homme, moins de 5,25 chez la femme.</p>', 'e46-musc')
ac('ALM', [('A','Appendicular'),('L','Lean'),('M','Mass')], 'Masse maigre appendiculaire', '<p>Masse maigre des membres ; exemples de seuils : moins de 21,4 kg chez l’homme, moins de 14,1 kg chez la femme.</p>', 'e46-musc')
ac('EWGSOP', [('E','European'),('W','Working'),('G','Group on'),('S','Sarcopenia in'),('O','Older'),('P','People')], 'Groupe de travail européen sur la sarcopénie chez les personnes âgées', '<p>Groupe dont les seuils de masse musculaire servent d’exemple dans le tableau 2 du consensus GLIM.</p>', 'e46-musc')
ac('FAO', [('F','Food and'),('A','Agriculture'),('O','Organization')], 'Organisation des Nations unies pour l’alimentation et l’agriculture', '<p>Co-auteur, avec l’Organisation mondiale de la Santé et l’Université des Nations unies, d’équations de dépense énergétique citées par la revue suisse.</p>', 'e46-besoins')
ac('UNU', [('U','United'),('N','Nations'),('U','University')], 'Université des Nations unies', '<p>Co-auteur, avec la FAO et l’OMS, d’équations de dépense énergétique citées par la revue suisse.</p>', 'e46-besoins')
ac('GESKES', [('GESKES','sigle de la société suisse de nutrition clinique (Société suisse de nutrition clinique, SSN) ; non développé lettre à lettre dans le dossier de recherche')], 'Société suisse de nutrition clinique', '<p>Aucune recommandation de cette société n’a été trouvée ni lue pour la leçon ; la source suisse principale est la revue de Baumgartner et collaborateurs (2020).</p>', 'e46-bilan')
ac('Marques-Vidal', [('Marques-Vidal','nom d’auteur, non une abréviation')], 'Marques-Vidal, auteur', '<p>Coauteur de l’analyse de la base suisse des sorties hospitalières 2012–2022.</p>', 'e46-tanweer')
ac('Kaegi-Braun', [('Kaegi-Braun','nom d’auteur, non une abréviation')], 'Kaegi-Braun, auteur', '<p>Auteur de l’analyse GLIM d’EFFORT et de la méta-analyse du soutien après la sortie.</p>', 'e46-effort-glim')
ac('kJ', [('k','kilo (mille)'),('J','Joule')], 'Kilojoule', '<p>Unité d’énergie. 4,2 kJ équivalent environ à 1 kcal.</p>', 'e46-thiamine-bioch')
