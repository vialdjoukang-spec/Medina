# Rapport de rédaction — R27 (cycle Betta 42, leçon 1, N-05-Neurologie)

Agent C42-A3-NEUR (Sonnet 5.5). Seules les données de `recherche.md` et `sources.json` (24 sources, lues le 15.10.2026) ont été utilisées. Porte de vérité franchie avant rédaction : `VÉRITÉ OK · CYCLE_42_R27`.

## Fichiers (chapters/R27/ et glossary/)
| Fichier | Contenu | Octets |
|---|---|---|
| R27_a.html | en-tête, quatre onglets, pA îlots 0 à 6 (question clinique, définitions et classifications, fréquence, physiopathologie, causes, anamnèse, examen clinique) | 29 469 |
| R27_b.html | pA îlots 7 à 13 (démarche et différentiels, urgences et pronostic, prise en charge, suivi, situations particulières, spécificités suisses et lacunes, critères formels `div.alert` puis paramètres clés `div.key`) + références | 27 164 |
| R27_c.html | pE e-1 à e-6 (4 quiz) ; pS : anatomie, physiologie, biochimie et génétique (3 figures SVG légendées, encadrés de corrélation clinique) | 26 216 |
| R27_d.html | pP p-1 à p-4 (stratégie, doses, interactions et surveillance, grossesse et organes ; 1 quiz) | 13 052 |
| R27_pop1.html | 24 fenêtres explicatives (dont l’aide mnémotechnique CPV « aide pédagogique, non critère officiel ») | 28 178 |
| R27_pop2.html | 7 fenêtres explicatives, 7 monographies de médicaments, 12 fenêtres Pareto | 23 682 |
| glossary/r27.py | 42 abréviations nouvelles, entrées conditionnelles (aucun terme existant écrasé) | |

Au total : 50 fenêtres (38 explicatives et monographies, 12 Pareto), 5 quiz de cas, 3 figures SVG, environ 15 400 mots (balises exclues).

## Auto-contrôle (cahier W)
- HTML bien formé : pile de balises vide sur la concaténation a + b + c + d ; chaque fichier de fenêtres bien formé.
- Identifiants uniques et tous préfixés `r27-` ; clés de fenêtres préfixées `r27-` et `pareto-r27-` ; aucune clé `data-k` sans fenêtre, aucune fenêtre orpheline ; identifiants de couverture Pareto tous valides.
- `audit()` de `build_medina.py` (exécuté dans une racine temporaire hors dépôt, avec le glossaire du lot) : `R27 non couvertes: 0`. Construction de la page et `pareto_ratios` sans erreur. `test_preview.py` : seule erreur, le chargement dynamique de `preview/lesson-core.js`, absent de l’environnement et identique sur le chapitre de référence N17 ; aucune fenêtre absente.
- Aucun fichier de `chapters/` ni de `glossary/` racine, ni `chapters.json`, ni git n’a été modifié.

## Sources utilisées
S1 à S24 du dossier : BfArM et OFS (S1, S2) ; ligne directrice DGN/ÖGN/SNG 2024, texte intégral (S3) ; Practical Neurology 2019, texte intégral (S4) ; SARA, revue de prévalence, RFC1, consensus de la marche ataxique, syndrome de déséquilibre aigu (Tarnutzer), série lausannoise, ESO 2021, ataxie pédiatrique, EFNS (S5 à S13, plusieurs au résumé) ; informations professionnelles Swissmedic Benerva (04.2019), Diamox (07.2026), Fampyra (03.2025), Skyclarys (03.2026), Phenhydan (06.2024), Quilonorm (03.2025), Vitarubine (07.2025) (S14 à S17, S19 à S21) ; Swissmedic, Summary report Skyclarys (S18) ; PROFILES 2017 (S22) ; bases légales de l’aptitude à la conduite (S23) ; Vogrig 2019 (S24).

## Lacunes assumées (signalées dans le cours, îlot 12.3, et aux endroits concernés)
L1 épidémiologie suisse ; L2 fréquences des symptômes ; L3 sensibilité et spécificité des signes cérébelleux segmentaires et du Romberg ; L4 délais d’imagerie urgente ; L5 valeurs de référence chiffrées (B1, B12, vitamine E, alpha-fœtoprotéine) ; L6 ataxie et grossesse ; L7 adaptation rénale du lithium ; L8 remboursement LS ; L9 aptitude à la conduite propre à l’ataxie ; L10 infirmités congénitales de l’AI, Suva/LAA, déclaration OFSP ; L11 physiologie cérébelleuse détaillée ; L12 ataxie chronique de l’enfant. Aucun chiffre suisse n’est déduit de données étrangères.

Points de vigilance pour l’audit différé : la divergence de dose de la thiamine dans l’encéphalopathie de Wernicke (EFNS 2010 : 200 mg 3 fois par jour ; information professionnelle suisse : jusqu’à 200 mg/jour par voie parentérale) est exposée sans être tranchée (fenêtre `r27-wernicke`, pP p-2) ; la répartition de R27.0 et R27.8 est un choix pédagogique du cours, car les notes du BfArM n’en précisent pas le contenu ; les doses de l’acétazolamide, de la 4-aminopyridine et des causes métaboliques rares viennent de la ligne directrice (usage hors étiquette en Suisse). Aucun mécanisme d’action médicamenteux n’est développé : le dossier n’en contient pas.

## Matrice de complétude → onglet et identifiant HTML
Onglets : pA Pathologie et prise en charge, pE Examens complémentaires, pS Sciences fondamentales, pP Pharmacologie.
| # | rubrique | statut | onglet | identifiant |
|---|---|---|---|---|
| 1 | Question clinique et enjeu pour l’examen fédéral | ✔ | pA | r27-0 (enjeu) ; r27-12 (SSP 96, 97, 98, 100, 103) |
| 2 | Définition et périmètre CIM-10-GM | ✔ | pA | r27-1 (1.1 définition, 1.2 périmètre R27, exclusions) ; fenêtres r27-ataxie, r27-cim |
| 3 | Classifications et stades | ✔ | pA / pE | r27-1 (1.3 cause, 1.4 tempo et âge, 1.5 SARA et GTI) ; r27-e-6 |
| 4 | Épidémiologie suisse puis européenne | ✔ (Suisse : LACUNE L1) | pA | r27-2 ; lacunes r27-12 (12.3) |
| 5 | Normal → pathologique | ✔ (détail : LACUNE L11) | pA / pS | r27-3 ; r27-s-anat-cours, r27-s-physio-cours, r27-s-bioch-cours |
| 6 | Étiologies et facteurs de risque | ✔ | pA | r27-4 |
| 7 | Anamnèse et symptômes (fréquences : LACUNE L2) | ✔ | pA | r27-5 |
| 8 | Examen clinique (segmentaires : LACUNE L3) | ✔ | pA / pE | r27-6 ; r27-e-6 (HINTS, GTI, SARA) |
| 9 | Drapeaux rouges et urgences (délais : LACUNE L4) | ✔ | pA | r27-8 (`div.alert` et tableau) |
| 10 | Examens complémentaires (valeurs normales : LACUNE L5) | ✔ | pE | r27-e-1 à r27-e-6 ; quiz des cas 1 à 4 |
| 11 | Diagnostic différentiel | ✔ | pA | r27-7 (tableau classé par gravité) |
| 12 | Prise en charge suisse (FI datées ; LS : LACUNE L8) | ✔ | pA / pP | r27-9 ; r27-p-1 à r27-p-4 ; monographies r27-thiamine, r27-b12, r27-skyclarys, r27-acetazolamide, r27-fampridine, r27-phenytoine, r27-lithium |
| 13 | Complications et pronostic | ✔ | pA | r27-8 (8.1, 8.2) |
| 14 | Suivi, prévention, dépistage | ✔ | pA | r27-10 |
| 15 | Situations particulières (L6, L7, L12) | ✔ | pA / pP | r27-11 ; r27-p-4 |
| 16 | Spécificités suisses (L9, L10) | ✔ | pA | r27-12 (12.1, 12.3) |
| 17 | Critères formels du diagnostic (`div.alert`) | ✔ | pA | r27-13 |
| 18 | Paramètres clés chiffrés (`div.key`) | ✔ | pA | r27-13 |
| 19 | Sous-codes R27, R27.0, R27.8 | ✔ | pA | r27-1 (1.2) ; glossaire R27.0, R27.8, R26.0, G23.3, G31.2 |
| 20 | Points d’examen fédéral | ✔ | pA | r27-12 (12.2 : situations de départ et pièges) |

Correspondance des îlots de pA : r27-0 Question clinique ; 1 Définitions, périmètre, classifications ; 2 Fréquence ; 3 Physiopathologie ; 4 Causes ; 5 Anamnèse ; 6 Examen clinique ; 7 Démarche et différentiels ; 8 Urgences, complications, pronostic ; 9 Prise en charge ; 10 Suivi et prévention ; 11 Situations particulières ; 12 Spécificités suisses, examen fédéral, lacunes ; 13 Critères formels et paramètres clés.

Audit différé — revue IA, distincte d’une validation médicale humaine.
