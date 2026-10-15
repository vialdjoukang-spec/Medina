# Rapport de rédaction — G99 (cycle Betta 41, leçon 2, N-05-Neurologie)

Agent C41-A3-NEUR (Sonnet 5.5). Consultation des sources : 15.10.2026. Seules les données de `recherche.md` et `sources.json` ont été utilisées.

## Fichiers (chapters/G99/)
G99_a.html (pA, îlots 0-6), G99_b.html (pA, îlots 7-13 + références), G99_c.html (pE e-1 à e-6 dont 4 quiz ; pS : anatomie, histologie, physiologie, biochimie/génétique, 5 figures SVG au total dans le chapitre), G99_d.html (pP, p-1 à p-4), G99_pop1.html et G99_pop2.html (37 fenêtres : 24 explicatives dont une aide mnémotechnique « aide pédagogique, non critère officiel », 13 Pareto), glossary/g99.py (13 abréviations nouvelles, entrées conditionnelles).

## Auto-contrôle (cahier W)
HTML bien formé (pile de balises vide), identifiants uniques et préfixés `g99-`, toutes les clés `data-k` ont leur fenêtre (aucune manquante, aucune orpheline), clés de fenêtres préfixées, ids de couverture Pareto valides, abréviations majuscules du texte toutes présentes au glossaire (existant ou g99.py). `build_medina.py` non exécuté : interdiction de toucher chapters/ et glossary/ racine.

## Lacunes assumées
Aucune source suisse sur la neuropathie autonome diabétique, la gastroparésie, la neuropathie urémique ; pas de seuils scintigraphiques ni de valeurs de coupure des tests réflexes ; pas de posologie de corticoïde pour la compression métastatique (NICE inaccessible) ; pas d'information suisse lue pour les traitements de la polyneuropathie à transthyrétine (tafamidis suisse = cardiomyopathie) ; fludrocortisone hors indication pour l'hypotension orthostatique ; dates de mise à jour des informations professionnelles non extraites ; plusieurs sources lues au résumé. Sciences fondamentales limitées à ce que le dossier documente. Quelques développements de sigles (AO, NIS, PND, FINESSE) sont signalés comme non fournis par la source.

## Mise à jour après complément de recherche (15.10.2026)
Ajouts : îlot 12 « Spécificités suisses et points d'examen fédéral » (S26 SSC/SSML 2024, S28 PROFILES), phrase RMS 2024 sur la gastroparésie (S27, résumé seul) dans pA îlot 3 ; ancien îlot 12 devenu 13 (critères et paramètres) ; lacunes élargies ; sigle OAC ajouté au glossaire (LCR évité : conflit avec liquide céphalo-rachidien). Tailles : G99_a.html 25321, G99_b.html 27137, G99_c.html 19781, G99_d.html 7682, G99_pop1.html 17476, G99_pop2.html 10341.

## Matrice de complétude → onglet et identifiant HTML
| # | rubrique | statut | onglet | identifiant |
|---|---|---|---|---|
| 1 | Question clinique, enjeu examen | ✔ | Pathologie | g99-0 |
| 2 | Définition, périmètre CIM-10-GM (astérisque, aucune exclusion) | ✔ | Pathologie | g99-0, g99-12 |
| 3 | Classifications et stades | ✔ | Pathologie / Examens | g99-1 (définitions, Toronto, mJOA, stades ATTR), g99-e-1 |
| 4 | Épidémiologie (aucune donnée suisse : lacune) | ✔ | Pathologie | g99-2 |
| 5 | Normal → pathologique | ✔ | Pathologie / Sciences | g99-s-anat, g99-s-physio, g99-s-histo, g99-s-bioch |
| 6 | Étiologies et facteurs de risque | ✔ | Pathologie | g99-4 |
| 7 | Anamnèse et symptômes | ✔ | Pathologie | g99-5 |
| 8 | Examen clinique | ✔ | Pathologie / Examens | g99-6, g99-e-1 |
| 9 | Drapeaux rouges, urgences | ✔ | Pathologie | g99-8 (urgences et complications : MSCC, myélopathie) |
| 10 | Examens complémentaires (seuils scintigraphiques : lacune) | ✔ | Examens | g99-7, g99-e-1 à g99-e-6 |
| 11 | Diagnostic différentiel | ✔ | Pathologie / Examens | g99-7 (démarche diagnostique), g99-e-5 |
| 12 | Prise en charge suisse (FI) | ✔ | Pathologie / Pharmacologie | g99-9, g99-p-1 à g99-p-4 |
| 13 | Complications et pronostic | ✔ | Pathologie | g99-8, g99-9 |
| 14 | Suivi, prévention, dépistage (délai NAC : lacune) | ✔ | Pathologie | g99-10 |
| 15 | Situations particulières | ✔ | Pathologie | g99-11 |
| 16 | Spécificités suisses (conduite SSC/SSML ; OFSP/Suva sans objet ; AI, LS : lacune) | ✔ | Pathologie | g99-12 |
| 17 | Critères formels (div.alert) | ✔ | Pathologie | g99-13 |
| 18 | Paramètres clés (div.key) | ✔ | Pathologie | g99-13 |
| 19 | Sous-codes G99.0, G99.00, G99.08, G99.1, G99.2, G99.8 | ✔ | Pathologie | g99-0, g99-12 |
| 20 | Points d'examen fédéral (PROFILES SSP 103/104 et pièges) | ✔ | Pathologie | g99-12 |

Les identifiants g99-N sont ceux des îlots de la partie Pathologie (G99_a/_b) ; g99-0 Question clinique, 1 Définitions, 2 Fréquence et pronostic, 3 Physiopathologie, 4 Causes, 5 Anamnèse, 6 Examen clinique, 7 Démarche diagnostique, 8 Urgences et complications, 9 Prise en charge, 10 Suivi, 11 Situations particulières, 12 Spécificités suisses, 13 Critères et paramètres.

Audit différé — revue IA, distincte d'une validation médicale humaine.
