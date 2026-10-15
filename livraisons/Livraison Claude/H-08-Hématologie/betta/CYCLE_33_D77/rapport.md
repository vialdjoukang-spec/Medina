# Rapport de rédaction — D77 (cycle Betta 33, leçon 1, agent C33-A3-HEM, Sonnet 5.5)

Fragment H-08-Hématologie. Leçon : D77 — Autres maladies du sang et des organes hématopoïétiques au cours de maladies classées ailleurs (fibrose splénique de la bilharziose, B65.-†). Date : 15.10.2026.

## Fichiers
| Fichier | Octets |
|---|---|
| chapters/D77/D77_a.html (en-tête, onglet Pathologie, îlots 0 à 6) | voir `wc -c` |
| chapters/D77/D77_b.html (îlots 7 à 14, critères formels puis paramètres clés) | |
| chapters/D77/D77_c.html (onglet Examens ; onglet Sciences : physiologie, parasitologie et immunité, hématologie cellulaire) | |
| chapters/D77/D77_d.html (onglet Pharmacologie) | |
| chapters/D77/D77_pop1.html (16 fenêtres) ; D77_pop2.html (14 fenêtres et 9 Pareto) | |
| glossary/d77.py (abréviations et codes, entrées conditionnelles) | |

## Sources utilisées
Les 20 sources de `sources.json` : codage BfArM/OFS ; consensus espagnol 2022 ; série TIPS 2021 ; étude hématologique européenne 2023 ; Suttorp 2021 ; revue radiologique 2026 ; Baveno VII ; revue bêtabloquants 2023 (résumé) ; Swiss TPH 2018 ; protocole CHUV 2024 ; OMS 2022 ; ECDC 2018 ; informations professionnelles suisses du propranolol et du carvédilol. EASL 2026 et BIA 2024 sont citées uniquement comme lacunes.

## Auto-contrôle (cahier W)
- HTML bien formé, balises équilibrées (a à d forment un seul template).
- Identifiants uniques, préfixés `d77` ; fenêtres `d77-…` ; Pareto `pareto-d77-…` ; toute clé `data-k` a sa fenêtre.
- `build_medina.audit()` renvoie `{}` avec le glossaire `d77.py`.
- Dernier îlot de la pathologie : `div.alert` (critères formels) puis `div.key` (paramètres clés).
- Quatre onglets, six Pareto (pathologie, examens, pharmacologie) et trois Pareto de sciences, quiz fictifs signalés.

## Lacunes et réserves (reprises du dossier)
- Aucune information professionnelle Swissmedic pour le praziquantel ; doses issues du consensus espagnol et de l’OMS.
- Aucune recommandation suisse de société savante ; sources suisses cliniques : Swiss TPH 2018 et CHUV 2024.
- EASL 2026, OMS 2022, BIA 2024, revue sur les bêtabloquants et Swiss TPH lus en résumé ou page de synthèse.
- Pas d’histologie propre de la fibrose splénique schistosomienne, pas de seuil chiffré d’hypersplénisme, pas d’indication formelle de splénectomie. Cette lacune est signalée dans le cours.
- CIM-11 non établie. Doses des vasoactifs absentes du dossier : non données.
- Quelques rappels d’anatomie générale (système porte, rate congestive) sont d’ordre classique, signalés dans le cours comme tels ; aucune valeur numérique hors dossier.
- Les cas cliniques sont fictifs et le dit.

Audit différé — revue IA, distincte d’une validation médicale humaine.

## Tailles mesurées (octets)
| Fichier | Octets |
|---|---|
| D77_a.html | 24867 |
| D77_b.html | 24032 |
| D77_c.html | 21797 |
| D77_d.html | 12467 |
| D77_pop1.html | 18710 |
| D77_pop2.html | 18277 |
| glossary/d77.py | 6465 |
