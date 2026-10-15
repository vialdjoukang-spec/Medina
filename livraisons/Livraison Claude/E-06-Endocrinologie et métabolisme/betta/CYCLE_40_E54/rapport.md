# Rapport de rédaction — E54 Carence en acide ascorbique (E-06-Endocrinologie et métabolisme)

Cycle Betta 40, leçon 2. Agent C40-A2-ENDO (Sonnet 5.5), 15.10.2026. Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers livrés (sous `chapters/E54/` et `glossary/`)
| Fichier | Contenu | Taille (octets) |
|---|---|---|
| E54_a.html | en-tête, quatre onglets, Pathologie : îlots 0 à 6 | 27 960 |
| E54_b.html | Pathologie : îlots 7 à 12 (critères formels `alert`, tableau, paramètres clés `key`) | 25 496 |
| E54_c.html | Examens (e-1 à e-5) et Sciences (anatomie, histologie, physiologie, biochimie) | 24 884 |
| E54_d.html | Pharmacologie (p-1 à p-4), fermeture du `template` | 8 783 |
| E54_pop1.html | 29 fenêtres (cas, mécanismes, clinique) | 30 628 |
| E54_pop2.html | 47 fenêtres (diagnostic, traitement, examens, sciences, 15 Pareto) | 43 878 |
| glossary/e54.py | 10 entrées conditionnelles (ESPEN, D-A-CH, DGE, ÖGE, SGE, HIF-1, HPLC, LOVIT, Möller-Barlow, Raynaud-Simon) | 4 433 |

Total HTML : environ 161 Ko. Fenêtres : 76 (61 explicatives, 15 Pareto). Quiz : 6. Figures : 2 (séquence causale, séquence diagnostique).

## Sources utilisées (dossier `sources.json`, S1 à S17)
Toutes les sources du dossier sont mobilisées : S1 (CIM-10-GM 2024), S2 (ESPEN 2022, seuils, recommandations 23.1 à 23.7), S3 et S4 (informations professionnelles suisses Streuli et Burgerstein), S5 (D-A-CH), S6 et S7 (cas suisses Zurich et Genève), S8 à S17 (revues et séries européennes). Aucune donnée absente du dossier n'a été ajoutée ; les inférences pédagogiques (par exemple coagulation normale donc fragilité de paroi) sont rattachées à leur source et les mécanismes non démontrés sont présentés comme hypothèses.

## Auto-contrôle (cahier W)
- HTML bien formé (analyse des balises, aucune balise non fermée) : OK.
- Identifiants uniques et préfixés `e54-` : OK ; identifiants `data-evidence` uniques : OK.
- 76 clés de fenêtres référencées, 76 définies, aucune orpheline, toutes préfixées `e54-` ou `pareto-e54-` : OK.
- Couvertures Pareto : tous les îlots cités existent : OK.
- Audit des abréviations (`build_medina.audit`, glossaire racine plus `e54.py`) : `{}` sur le corps et sur les fenêtres.

## Lacunes (héritées du dossier de recherche, non comblées)
1. Aucune recommandation suisse ou européenne propre au scorbut (SSED, ESE) ; ESPEN 2022 est la référence retenue.
2. Aucun critère diagnostique formel validé ; l'îlot final présente une définition opérationnelle d'étude.
3. Aucune prévalence suisse ou européenne représentative.
4. Sept sources lues en résumé seulement (S6, S8, S11, S13 à S17) ; fréquence des signes dans les 280 cas adultes non disponible.
5. Information professionnelle de Redoxon non lue ; seules les deux informations Streuli et Burgerstein fondent la posologie suisse.
6. Aucun calendrier de contrôle biologique ni seuil d'hémoglobine d'urgence dans les sources.
7. Notes d'inclusion et d'exclusion du PDF OFS non relues.
8. LOVIT et valeurs américaines exclus (source secondaire américaine).
9. Divergence ESPEN 23.6 (200 à 500 mg/j) et tableau 14 (500 mg/j) signalée dans le cours ; divergence des seuils d'hémolyse G6PD (4 g/j suisse, 60 g ESPEN) tranchée en faveur du texte suisse.
