# Rapport de relecture — J69 — Pneumopathies d’inhalation et atteintes respiratoires toxiques (P-02-Pneumologie)

Relecteur : agent distinct de l’auteur (chaîne P-02, 09.10.2026). **Revue par IA : ne vaut pas validation médicale humaine.**

## Portée de cette relecture
Relecture **ciblée, une passe** : priorité aux affirmations à risque (posologies, adaptations rénales, antidotes), contrôles techniques et intégration. La seconde passe complète sur les quatre dimensions reste à faire.

## Vérifications contre l’information professionnelle suisse (AmiKo, 09.10.2026)
- Co-Amoxi-Mepha i.v. : 2200 mg 3 à 4 fois par jour ; clairance 10–30 mL/min : 1,2 g puis 600 mg toutes les 12 heures ; < 10 mL/min : 1,2 g puis 600 mg toutes les 24 heures ; pas de perfusion de 2200 mg sous 30 mL/min. **Correction** : la ligne « inférieure à 10 » omettait la dose initiale de 1,2 g (J69_d.html, îlot j69-p-2).
- Cyanokit : 5 g en 15 minutes chez l’adulte ; 70 mg/kg (5 g au plus) chez l’enfant ; seconde dose possible ; maximum 10 g (adulte), 140 mg/kg (enfant, 10 g au plus). Conforme.

## Intégration
- Copie dans `chapters/J69/` et `glossary/j69.py` ; entrées `chapters.json` (covers J68, J69, J70) et `organisation/course_groups.json` ; J69 ajouté à la liste des nouvelles productions de `tests/audit_sciences.py`.
- Planche ajoutée : `J69_pop_planche.html` (fragment végétal inhalé, Yale Rosen, Wikimedia Commons, CC BY-SA 2.0), mot vert dans l’unité Histologie et radiobiologie.

## Contrôles
- `python3 build_medina.py J69` : 0 abréviation non couverte, Pareto calculés.
- `test_preview.py J69` : seule erreur `preview/lesson-core.js` absent, identique sur J45 (environnement de prévisualisation, non propre au cours).

## Réserves maintenues
Celles du rapport d’auteur (hors indication des corticoïdes, résumés seuls pour plusieurs sources, lacunes nommées) restent ouvertes.
