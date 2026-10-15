# Rapport de rédaction : E32, Maladies du thymus (E-06-Endocrinologie et métabolisme)

Cycle Betta 35, leçon 1. Agent C35-A2-ENDO (rédaction, Sonnet 5.5). Date : 15.10.2026.
Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers
- `chapters/E32/E32_a.html` : 27107 octets
- `chapters/E32/E32_b.html` : 23606 octets
- `chapters/E32/E32_c.html` : 32693 octets
- `chapters/E32/E32_d.html` : 7308 octets
- `chapters/E32/E32_pop1.html` : 16039 octets
- `chapters/E32/E32_pop2.html` : 14764 octets
- `glossary/e32.py` : 5391 octets
- Fenêtres : 49 templates (dont 10 Pareto et 1 moyen mnémotechnique « aide pédagogique, non critère officiel »). Quiz : 5 (4 dans Examens, 1 dans la pathologie). Environ 13 000 mots. Figures SVG : 3 (migration embryonnaire, trois profils histologiques, poids du thymus selon l’âge d’après Porubsky 2025).
- Glossaire `glossary/e32.py` : 17 entrées conditionnelles (NVALT, EuroNet-PHL-C1, CD4, CD8, CD10, CD23, Bcl2, Bcl6, LMO2, hCG, UH, CA-125, RyR, MuSK, noms propres d'auteurs et de spécialité).

## Structure
Quatre onglets : Pathologie (îlots 0 à 12 ; dernier îlot = critères formels `div.alert` puis paramètres clés `div.key`), Examens (5 îlots : hiérarchie question-examen-statut, fiches d'interprétation, tableau diagnostics × contexte/imagerie/biologie/histologie, biologie et histologie, 4 quiz de cas), Sciences (Anatomie et embryologie, Histologie, Physiologie, Immunologie ; schéma SVG et bloc « Science → clinique » par science), Pharmacologie (4 îlots : classes, doses sourcées, mises en garde, monographies en fenêtres). Plan monographique ; le périmètre CIM n'est traité que dans une fenêtre et une phrase.

## Sources utilisées
S1 à S25 selon `sources.json` (citations sous forme « (auteur, année) »). S26 (ESMO 2015) non utilisée, non lue. Aucune donnée extérieure au dossier. Les sources non européennes (S4, S11, S12, S14 à S18, S20, S24) servent à des données descriptives ; S20 : résumé seul, algorithme non reproduit.

## Auto-contrôle (cahier W)
HTML bien formé sur les six fichiers concaténés (aucune balise non fermée) ; identifiants uniques, tous préfixés `e32` ; chaque `data-k` possède sa fenêtre, aucune fenêtre orpheline, toutes préfixées `e32-` ou `pareto-e32-` ; les attributs `data-cover`, `data-s` et les renvois du sommaire pointent vers des identifiants existants ; audit des abréviations (`build_medina.audit`) = `{}` avec `glossary/e32.py` ajouté ; transformation et enveloppement `build_medina` exécutés sans erreur. Contrôles exécutés hors racine, sans modifier `chapters/`, `glossary/` ni `chapters.json`. Test navigateur (`test_preview.py`) non exécuté, car il exige le chapitre dans la racine.

## Lacunes (reprises du dossier, non comblées)
Aucune recommandation suisse (SSED, Swiss Medical Forum) ; texte ESMO 2015 inaccessible ; rattachement des kystes (E32.8 présumé) et codes des thymomes non vérifiés ; aucune incidence suisse ou européenne ; indications de thymectomie dans la myasthénie non lues ; abcès thymique : cas isolés, aucun protocole antibiotique ni dose ; mécanisme du carbimazole, interactions médicamenteuses et voie cellulaire du rebond non documentés dans le dossier, donc non exposés. Les vignettes et le cas récapitulatif sont fictifs et signalés.
