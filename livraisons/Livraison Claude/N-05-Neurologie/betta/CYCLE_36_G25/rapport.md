# Rapport de rédaction — G25 Autres syndromes extrapyramidaux et troubles de la motricité (N-05-Neurologie)
Cycle Betta 36, leçon 1 — agent C36-A4-NEUR (rédaction, Sonnet 5.5), 15.10.2026.
**Audit différé — revue IA, distincte d'une validation médicale humaine.**

## Fichiers livrés (chapters/G25/ et glossary/)
| Fichier | Octets | Contenu |
|---|---|---|
| G25_a.html | 32 903 | En-tête, 4 onglets, plan, îlots 0 à 6 de la Pathologie |
| G25_b.html | 35 731 | Îlots 7 à 12 (critères formels `alert` puis paramètres `key` en dernier îlot), références |
| G25_c.html | 38 396 | Examens (e-1 à e-10, 4 quiz de cas) et Sciences (anatomie, physiologie, biochimie, génétique, 4 schémas SVG) |
| G25_d.html | 20 843 | Pharmacologie (p-1 à p-6, 3 quiz), fermeture du gabarit |
| G25_pop1.html, G25_pop2.html | 34 823 ; 24 183 | 51 fenêtres : 42 explicatives, dont 3 divergences de sources, et 9 Pareto |
| glossary/g25.py | — | 52 entrées conditionnelles (codes CIM, sigles, noms de gènes et de produits) |

Total : 7 quiz, 6 figures SVG noir et blanc légendées, 19 tableaux, 9 Pareto (bases, clinique, prise en charge, examens, 4 sciences, pharmacologie).

## Sources utilisées (dossier sources.json)
S1 à S24, toutes citées : classifications (S1, S2), consensus tremblement MDS 2018 (S3), lignes directrices S2k tremblement 2022 (S4), jambes sans repos 2024 (S5), chorée 2022 (S12), revues (S6 à S11, S13 à S15, S24) et huit informations professionnelles suisses (S16 à S23). Aucune donnée extérieure au dossier n'a été introduite ; les liens physiopathologiques ajoutés sont des mises en relation de faits du dossier.

## Divergences présentées en mot vert
1. Polysomnographie : page HUG 2026 contre ligne directrice 2024 (fenêtre g25-div-psg).
2. Lévodopa : fiche Madopar (usage prolongé) contre ligne directrice (100 mg, intermittent) (fenêtre g25-div-levodopa).
3. Ropinirole et tétrabénazine : statut suisse et discordance AmiKo, signalés dans p-5 et les fenêtres de monographie.

## Lacunes conservées (non comblées)
L1 rattachement des tremblements rares à G25.2 ; L2 physiopathologie du tremblement essentiel ; L3 informations suisses non lues (topiramate, clonazépam, gabapentine, prégabaline, Ferinject) ; L4 pharmacothérapie de la chorée non huntingtonienne et chorée médicamenteuse ; L5 discordance Xenazine ; L6 causes des tics organiques ; L7 épidémiologie suisse ; L8 ropinirole ; L9 trouble isolé des mouvements périodiques ; L10 critères formels de l'homme raide ; L11 lien akathisie-suicidalité. Les pronostics chiffrés et les valeurs de référence de laboratoire (ferritine, saturation) ne figurent pas non plus dans le dossier.

## Auto-contrôle du cahier W
- HTML bien formé (équilibre des balises vérifié sur a+b+c+d et sur les fenêtres).
- Identifiants uniques et préfixés `g25-` ; clés de fenêtres `g25-…` et `pareto-g25-…` ; aucune clé appelée sans fenêtre, aucune fenêtre orpheline ; ids de couverture Pareto tous existants.
- Classes limitées à la liste fermée ; quatre onglets pA, pE, pS, pP ; Pareto en fin de grandes parties.
- Audit des abréviations de `build_medina.audit()` avec le glossaire racine et `g25.py` : résultat `{}`.
- Non effectué (hors périmètre) : construction du front, injection dans `chapters/`, `chapters.json`, git.
