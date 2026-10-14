# Rapport de rédaction — N27 Petit rein de cause inconnue (N-07-Néphrologie), cycle Betta 31

Agent C31-A3-NEPH (Sonnet 5.5), d'après `recherche.md` et `sources.json` (S1–S15), consultés le 14.10.2026.

## Fichiers (octets)
| Fichier | Contenu |
|---|---|
| chapters/N27/N27_a.html | 15 588 · en-tête, 4 onglets, plan, îlots 0 à 6 |
| chapters/N27/N27_b.html | 15 231 · îlots 7 à 12 (dernier : div.alert puis div.key), pager |
| chapters/N27/N27_c.html | 17 203 · Examens (e-1 à e-5, 3 quiz) et Sciences (anatomie, histologie, physiologie, biochimie) |
| chapters/N27/N27_d.html | 6 416 · Pharmacologie (p-1 à p-4), fermeture du gabarit |
| chapters/N27/N27_pop1.html | 13 776 · 12 fenêtres |
| chapters/N27/N27_pop2.html | 16 406 · 11 fenêtres + 12 fenêtres Pareto |
| glossary/n27.py | 29 entrées conditionnelles (`add_if_absent`) |

## Auto-contrôle (cahier W)
- HTML bien formé (analyseur de balises : aucune erreur, aucune balise ouverte).
- Identifiants uniques, tous préfixés `n27-` (hors pA, pE, pS, pP, ch-N27).
- Toutes les clés de fenêtre référencées existent (0 manquante, 0 inutilisée) ; ratios Pareto : tous les îlots couverts existent.
- `build_medina.audit()` sur les six fichiers avec le glossaire n27 : `{}` (aucune abréviation hors glossaire).
- Références des entrées de glossaire : toutes vers une fenêtre existante.

## Sources utilisées
S1–S15 du dossier, sans donnée extérieure. Les raisonnements du rédacteur (mécanismes de la sténose sous bloqueur du SRA, critère d'orientation d'un petit rein, raisons de la monographie) sont signalés comme tels dans le texte.

## Lacunes (reprises du dossier)
Aucune recommandation ni épidémiologie suisse propre à N27 ; centiles SKIPOGH non lus ; codes CIM des causes non relus ; aucune source sur la biopsie des petits reins ; ESC/ESH non relues ; une seule FI suisse (ramipril), aucune pour iSGLT2, statine, aspirine ; sémiologie propre au petit rein non documentée ; valeurs pédiatriques non exploitées ; plusieurs sources lues en résumé seul. Pas de `data-evidence` : ce cahier n'en exige pas.

Audit différé — revue IA, distincte d'une validation médicale humaine.
