# Rapport — G23, Autres maladies dégénératives des noyaux gris centraux (N-05-Neurologie)
Cycle Betta 36, leçon 1, agent C36-A1-NEUR (rédaction, Sonnet 5.5), 15.10.2026.
Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers
| Fichier | Taille |
|---|---|
| chapters/G23/G23_a.html | 40943 octets |
| chapters/G23/G23_b.html | 37965 octets |
| chapters/G23/G23_c.html | 41067 octets |
| chapters/G23/G23_d.html | 14003 octets |
| chapters/G23/G23_pop1.html | 38532 octets |
| chapters/G23/G23_pop2.html | 30752 octets |
| glossary/g23.py | 18909 octets |

## Contenu
- Quatre onglets (Pathologie 0 à 12, Examens e-1 à e-5, Sciences : anatomie, neuropathologie, physiologie, biochimie, génétique, Pharmacologie p-1 à p-4) ; dernier îlot de la pathologie = critères formels (alert) puis paramètres clés (key).
- 63 fenêtres (50 explicatives, 13 Pareto), 5 quiz de cas, 7 figures SVG noir et blanc, 68 entrées de glossaire (add_if_absent, sans mutation du glossaire existant).
- Niveaux PSP écrits O-1, P-1, A-1, C-1 (et non O1, P1…) : P1, A1, C1 existent déjà dans le glossaire racine avec d'autres sens (mitral, albuminurie, complément).

## Sources utilisées
Uniquement celles de sources.json (S1 à S23), citées par lien dans le texte et en fin d'onglet 1.

## Lacunes (reprises du dossier de recherche, non comblées)
- L1 : rattachement de la DCB/SCB dans l'index CIM-10-GM non vérifié (affiché comme tel).
- L2 : aucune ligne directrice suisse ou EAN lue ; ligne directrice ERN-RND/EAN/MDS-ES signalée en cours.
- L3 : stridor/apnées et traitement urologique de l'AMS non lus ; le cours ne les décrit pas.
- L4 : Florinef, Xeomin, Ferriprox : indication seulement ; posologie de la toxine botulique non lue.
- L5 : aucune épidémiologie suisse ni européenne primaire de l'AMS ; chiffres cités de seconde main.
- L6 : sources S8, S9, S11, S13, S14, S15 lues en résumé.
- L7 : syndrome de Shy-Drager = terminologie historique.
- Vignette et cas récapitulatif fictifs, étiquetés comme tels. Conduite après un essai négatif de lévodopa non documentée, signalée.
- Développements littéraux des symboles de gènes et de traceurs dans le glossaire : usage d'identification, hors dossier de sources.

## Contrôles
- build_medina (racine temporaire en scratchpad) : « G23 non couvertes: 0 », aucune erreur Pareto.
- Prévisualisation navigateur (test_preview.py adapté en HTTP, car l'import dynamique de lesson-core.js échoue en file:// y compris pour N17) : OK.
- Clés de fenêtres toutes présentes, aucune inutilisée, identifiants uniques préfixés g23-, HTML bien formé.
- Aucun fichier modifié hors de ce dossier ; chapters/, glossary/, chapters.json racine et git non touchés.
