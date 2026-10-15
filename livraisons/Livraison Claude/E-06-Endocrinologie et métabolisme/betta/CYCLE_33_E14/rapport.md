# Rapport de rédaction — E14 Diabète sucré, sans précision (E-06-Endocrinologie et métabolisme)

Cycle Betta 33, leçon 2. Agent C33-A2-ENDO (rédaction, Sonnet 5.5). Date : 15.10.2026. Sources : uniquement `recherche.md` et `sources.json` (S1 à S20). Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers (chapters/E14/ et glossary/)
| Fichier | Octets |
|---|---|
| E14_a.html (en-tête, onglet 1 sections 0 à 6) | 26 303 |
| E14_b.html (sections 7 à 13, critères formels, paramètres clés, références) | 33 240 |
| E14_c.html (Examens e-1 à e-4 ; Sciences : physiologie, biochimie, génétique et immunologie, complications) | 28 727 |
| E14_d.html (Pharmacologie p-1 à p-4) | 9 749 |
| E14_pop1.html / E14_pop2.html (62 fenêtres) | 23 587 / 37 422 |
| glossary/e14.py (49 abréviations, conditionnelles) | 16 714 |

Volume : environ 15 800 mots, 26 îlots, 24 tableaux, 6 schémas SVG légendés, 5 quiz de cas, 39 fenêtres explicatives et 23 fenêtres Pareto (une par grande partie). Aucune donnée en dehors du dossier de recherche.

## Contrôles (cahier W)
- HTML bien formé (pile de balises vide), identifiants uniques et préfixés `e14-`, toutes les clés `data-k` ont leur fenêtre, aucune clé nouvelle sans préfixe.
- Copie de travail hors dépôt (racine temporaire) : `build_medina.py E14` → « E14 non couvertes: 0 », aucune erreur Pareto.
- Contrôle navigateur : chargement, quatre onglets, ouverture d'une fenêtre. `test_preview.py` échoue pour toute leçon (y compris N17) sur le module `preview/lesson-core.js`, absent du dépôt : défaut préexistant, indépendant de E14.
- Dernier îlot de l'onglet 1 : critères formels (`div.alert`) puis paramètres clés (`div.key`), avec la liste des références.

## Sources utilisées
S1 à S20 (liste complète dans `sources.json`), en priorité OFS (CIM-10-GM 2024, manuels de codage 2024/2025), OMS 2019, SSED 2023/2024/2025, consensus 2024 sur les crises hyperglycémiques, JBDS 2022, Swissmedic (Glucophage®, Baqsimi®).

## Lacunes et attributions
- Équivalence E14 / « diabète non classé » : rapprochement interprétatif, signalé comme tel (aucune source officielle).
- Aucune donnée suisse sur la fréquence du code E14.
- Seuils de l'état hyperosmolaire : JBDS 2022 (figure du consensus 2024 illisible).
- ESC 2023 : principes seulement ; classes et cibles chiffrées non lues ; ESC 2026 non consultée pour ce sujet.
- Pas d'information professionnelle lue pour l'insuline, les inhibiteurs du SGLT2 ou les agonistes du GLP-1 : pas de posologie ni de mécanisme pour ces classes (indiqué dans le cours).
- Anatomie et histologie descriptives non incluses (absentes du dossier) : la barre des sciences contient physiologie, biochimie, génétique et immunologie, complications.
- Le calcul des « HbA1c-années » n'est pas précisé dans le dossier ; la fenêtre le signale comme lecture pédagogique.
- Libellés des codes étoiles (N08.3, H36.0, H28.0, G63.2, G59.0) : libellés usuels de la CIM-10, le dossier ne cite que les codes ; signalé dans la fenêtre.
- Mnémotechniques « A, C, A, P » (typage) et « D, K, A » (acidocétose) : aides pédagogiques, non critères officiels.
- Vignette et cas des quiz : valeurs fictives, signalées comme telles.
