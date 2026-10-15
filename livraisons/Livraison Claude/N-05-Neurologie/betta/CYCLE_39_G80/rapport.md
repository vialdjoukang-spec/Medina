# Rapport de rédaction G80 — Infirmité motrice cérébrale (N-05-Neurologie)

Cycle Betta 39, leçon 2 · agent C39-A3-NEUR (rédaction, Sonnet 5.5) · 15.10.2026
Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers
| Fichier | Octets |
|---|---|
| chapters/G80/G80_a.html (onglet 1, îlots 0–6) | 22 612 |
| chapters/G80/G80_b.html (onglet 1, îlots 7–12, références) | 19 218 |
| chapters/G80/G80_c.html (Examens e-1 à e-4 ; Sciences : anatomie, physiologie, génétique, biochimie) | 25 787 |
| chapters/G80/G80_d.html (Pharmacologie p-1 à p-4) | 9 064 |
| chapters/G80/G80_pop1.html, G80_pop2.html (47 fenêtres dont 14 Pareto) | 10 919 + 13 478 |
| glossary/g80.py (31 entrées : sigles, 7 sous-codes G80.x, G11.4) | 8 336 |

Volume : environ 10 900 mots de texte visible (pages + fenêtres), 6 quiz de cas (4 en Examens, 2 en Pharmacologie), 5 schémas SVG légendés, 14 fenêtres de Pareto.

## Sources du dossier effectivement utilisées
S1 (CIM-10-GM), S2 à S11, S13 à S21. S12 (AVC néonatal, titres seuls) n'est pas utilisé ; la fenêtre « Facteurs prénataux » le signale.

## Lacunes conservées dans le cours (fenêtre « Ce que ce cours ne couvre pas »)
Aucune recommandation suisse de société ; NICE NG62 (403) ; page SCPE du JRC (404) ; assurance-invalidité ; niveaux MACS/CFCS ; intervalles de surveillance des hanches ; formule de la migration de Reimers ; informations professionnelles du diazépam, de la tizanidine, du glycopyrronium et des antiépileptiques ; espérance de vie et transition à l'âge adulte ; prévalence suisse populationnelle ; spécificités des tests précoces ; interactions médicamenteuses et contre-indications des trois monographies suisses (non extraites du dossier).

## Choix de rédaction
- Les sciences fondamentales sont limitées à ce que le dossier établit (fenêtres de vulnérabilité MRICS, hanche, tonus et mouvement SCPE, génétique, sites d'action du baclofène et de la toxine) : aucune anatomie des voies motrices n'a été ajoutée de mémoire.
- Les statuts d'examen (indiqué, conditionnel, non systématique) sont ceux du rédacteur, signalés comme tels.
- Le « gold standard » est nommé par question (pas de référence unique pour le diagnostic de PC).
- Aucune recommandation américaine ; la définition de 2006 (atelier de Bethesda) est lue comme consensus international.

## Auto-contrôle (cahier W)
- HTML équilibré (a+b+c+d), identifiants uniques et préfixés `g80-`, clés de fenêtres `g80-…` / `pareto-g80-…`, toutes référencées et existantes (aucune fenêtre orpheline).
- Moteur `build_medina.py` (racine temporaire, sans toucher au dépôt) : `G80 non couvertes: 0`, aucune erreur Pareto.
- `test_preview.py G80` : cours affiché, fenêtres de glossaire et de cours ouvertes, quatre onglets et mode livre parcourus ; seule remontée : l'import dynamique `preview/lesson-core.js` est absent du dépôt, défaut identique sur N17 (non lié à G80).
- Non réalisé (consigne) : audit, injection, `chapters.json`, git.
