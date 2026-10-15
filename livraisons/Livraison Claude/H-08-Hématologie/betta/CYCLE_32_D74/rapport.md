# Rapport de rédaction — D74 Méthémoglobinémie (cycle Betta 32, leçon 2, agent C32-A4-HEM, Sonnet 5.5)

Audit différé — revue IA, distincte d'une validation médicale humaine. Date : 14.10.2026.

## Fichiers (chapters/D74/, glossary/)
| Fichier | Octets |
|---|---|
| D74_a.html (en-tête, pathologie îlots 0-7) | 26 311 |
| D74_b.html (pathologie îlots 8-15, critères formels et paramètres clés) | 25 553 |
| D74_c.html (Examens, Sciences : 4 disciplines, 3 schémas SVG) | 30 198 |
| D74_d.html (Pharmacologie) | 14 673 |
| D74_pop1.html (32 fenêtres explicatives) | 42 850 |
| D74_pop2.html (10 fenêtres Pareto) | 8 860 |
| glossary/d74.py (22 entrées conditionnelles) | 6 453 |

Total : environ 10 400 mots de cours et 5 100 mots en fenêtres ; 42 fenêtres, 4 quiz de cas, 4 onglets, 10 boutons Pareto.

## Sources utilisées (toutes issues de sources.json)
EHA/EuroBloodNet 2021 (texte intégral), informations professionnelles suisses Proveblue, Emla, Fasturtec, Swissmedic Vigilance-News juin 2011, cas HFR Fribourg 2025, CIM-10-GM 2024 BfArM/OFS ; résumés seuls : cas Inselspital 2019, revue zurichoise COVID-19 2020, cas Triemli 2026, résumé EHA HemaSphere 2021. Aucune donnée extérieure au dossier. Deux calculs de l'auteur sont signalés comme tels (1,5 g/dl = 10 % à 15 g/dl d'hémoglobine, environ 19 % à 8 g/dl).

## Divergences présentées (fenêtres)
- Seuils de gravité Swissmedic 2011 / EHA 2021 : `d74-seuils` ; l'EHA 2021, source primaire européenne la plus récente, est retenue, la grille 2011 reste consultable.
- Perfusion continue du bleu de méthylène EHA / information professionnelle suisse : `d74-perfusion` ; les deux positions sont exposées, le choix revient au clinicien avec Tox Info Suisse.

## Lacunes (reprises du dossier)
Aucune recommandation d'une société suisse dédiée ; liste des antidotes de Tox Info Suisse inaccessible ; pas d'information professionnelle suisse pour l'acide ascorbique injectable ni la dapsone ; pas d'épidémiologie suisse ; posologie pédiatrique de l'acide ascorbique non trouvée ; raison de la contre-indication du bleu de méthylène après nitrite antidotique du cyanure non détaillée dans les passages lus ; résultats pour le type II et le type IV face au bleu de méthylène « non précisés par les sources lues ».

## Auto-contrôle
- HTML bien formé (analyse des balises : aucune erreur, chapitre et fenêtres).
- Identifiants uniques et préfixés `d74-` ; toute clé `data-k` possède son `template data-pop` (aucune orpheline) ; clés Pareto `pareto-d74-*` ; couvertures Pareto toutes existantes.
- `build_medina.audit()` appliqué au texte complet avec le glossaire racine + `glossary/d74.py` : `{}` (aucune abréviation non couverte).
- Dernier îlot de la pathologie : `div.alert` (critères formels) puis `div.key` (paramètres clés).
- Non exécuté : `test_preview.py` (nécessite l'installation dans chapters/ racine, hors périmètre de cette tâche).
- Aucun fichier modifié hors du dossier de la leçon ; ni git, ni chapters.json.
