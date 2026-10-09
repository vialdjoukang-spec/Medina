# Rapport de relecture — R06 — Dyspnée et anomalies de la respiration (P-02-Pneumologie)

Relecteur : agent distinct de l’auteur (chaîne P-02, 09.10.2026). **Revue par IA : ne vaut pas validation médicale humaine.**

## Portée de cette relecture
Relecture **ciblée, une passe** : posologies et repères suisses du tableau de pharmacologie, contrôles techniques et intégration. La seconde passe complète sur les quatre dimensions reste à faire.

## Vérifications contre l’information professionnelle suisse (AmiKo, 09.10.2026)
- Palladon : 1,3 mg d’hydromorphone orale ≈ 10 mg de morphine orale. Conforme.
- Paspertin : 30 mg par jour au plus, 5 jours au plus ; réduction de 50 % si clairance 15–60 mL/min (75 % si ≤ 15 mL/min). Conforme.
- Aucune correction de contenu nécessaire sur les points vérifiés.

## Intégration
- Copie dans `chapters/R06/` et `glossary/r06.py` ; entrées `chapters.json` et `organisation/course_groups.json` ; R06 ajouté à la liste des nouvelles productions de `tests/audit_sciences.py`.
- Pas de planche morphologique : cours de symptôme, sans lésion élémentaire propre.

## Contrôles
- `python3 build_medina.py R06` : 0 abréviation non couverte.
- `test_preview.py R06` : seule erreur `preview/lesson-core.js` absent, identique sur J45 (environnement).

## Réserves maintenues
Celles du rapport d’auteur restent ouvertes (traitements symptomatiques hors indication suisse, recommandation ERS 2024 lue en résumé, lacunes nommées).
