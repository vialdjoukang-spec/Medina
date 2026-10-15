# Rapport de rédaction — N29 (N-07-Néphrologie), cycle Betta 32, leçon 1

Agent C32-A3-NEPH (Sonnet 5.5), 14.10.2026. Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers (sous `livraisons/Livraison Claude/N-07-Néphrologie/betta/CYCLE_32_N29/`)
| Fichier | Taille (octets) |
|---|---|
| chapters/N29/N29_a.html (pathologie, îlots 0 à 6) | 25 243 |
| chapters/N29/N29_b.html (pathologie, îlots 7 à 12 et références) | 25 290 |
| chapters/N29/N29_c.html (examens, sciences) | 28 992 |
| chapters/N29/N29_d.html (pharmacologie) | 8 896 |
| chapters/N29/N29_pop1.html (fenêtres de contenu) | 40 132 |
| chapters/N29/N29_pop2.html (monographies, calculs, Pareto) | 12 548 |
| glossary/n29.py | 3 980 |

Environ 13 800 mots visibles ; 61 fenêtres (47 de contenu, 14 Pareto) ; 4 quiz de cas ; 5 figures SVG noir et blanc légendées ; 4 sciences (anatomie, histologie, physiologie, biochimie).

## Sources utilisées
S1 à S25 du dossier `sources.json` ; aucune donnée absente du dossier. Informations professionnelles suisses : Procysbi®, Cystadrops®, Rifater®, Myambutol®, Pyrazinamide Labatec® (octobre 2022), Extencilline®.
Le contentieux du pyrazinamide en insuffisance rénale (guide suisse 2024 contre information professionnelle 2022) est présenté dans la fenêtre `n29-tb-ir` : la source la plus récente guide la conduite, le texte d'autorisation reste exposé.

## Lacunes explicites (reprises dans le cours)
1. Aucune recommandation suisse ou européenne propre à la tuberculose urogénitale ; données urinaires issues d'une revue non systématique.
2. Fréquence suisse de la forme urogénitale inconnue.
3. Praziquantel : aucune information professionnelle suisse trouvée ; schéma suisse ou européen non lu.
4. Aucune source sur la gomme rénale ni l'atteinte rénale de la syphilis tertiaire proprement dite ; seule la glomérulopathie de la syphilis précoce est documentée (codée N08.0*). Tests sérologiques de la syphilis non détaillés dans le dossier.
5. Recommandations cystinose 2026 lues en résumé seulement.
6. Aucun article du Swiss Medical Forum ni position de la Société suisse de néphrologie trouvé.
7. Règle d'arbitrage N16.3*/N29.8* non lue.

## Auto-contrôle du cahier W
- HTML bien formé (analyse de balises : pile vide, aucune erreur) pour les fichiers de pages et de fenêtres.
- Identifiants uniques, tous préfixés `n29` ; classes de la liste fermée uniquement.
- Toutes les clés `data-k` ont leur `template data-pop` (aucune manquante, aucune orpheline) ; clés préfixées `n29-` ou `pareto-n29-`.
- Couvertures Pareto : tous les identifiants d'îlots existent.
- Dernier îlot de la pathologie : `div.alert` (critères formels) puis tableau puis `div.key` (paramètres clés).
- Audit des abréviations (`build_medina.audit`) : `{}` ; construction `build_medina.py N29` dans une copie de travail : « N29 non couvertes: 0 », sans erreur Pareto. Le test navigateur `test_preview.py` n'a pu être mené à terme : `lesson-core.js` est absent de l'environnement (défaut d'environnement, non lié au chapitre).
- Aucune modification de `chapters/` racine, `glossary/` racine, `chapters.json` ni du dépôt git.
