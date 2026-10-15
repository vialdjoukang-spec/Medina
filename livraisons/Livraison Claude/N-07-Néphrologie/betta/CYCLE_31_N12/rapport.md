# Rapport de rédaction — N12 — Néphrite tubulo-interstitielle, non précisée comme aiguë ou chronique

Cycle Betta 31, leçon 1, agent C31-A3-NEPH (rédaction Sonnet 5.5). Consultation des sources : 14.10.2026. Fragment N-07-Néphrologie.

## Fichiers (octets)
- chapters/N12/N12_a.html : 18783
- chapters/N12/N12_b.html : 27224
- chapters/N12/N12_c.html : 22787
- chapters/N12/N12_d.html : 9326
- chapters/N12/N12_pop1.html : 19856
- chapters/N12/N12_pop2.html : 20935
- glossary/n12.py : 3713

## Volume
- Environ 12416 mots (texte hors balises), 33 fenêtres explicatives, 7 fenêtres Pareto, 5 quiz de cas cliniques, 4 schémas SVG (sciences), 4 onglets.

## Sources utilisées
Uniquement celles du dossier recherche.md / sources.json (S1 à S19) : revue médicale suisse HUG 2022 (S3), directive SSI 2025 (S4), EAU 2026 (S7), KDIGO 2012 (S10), consensus pédiatrique suisse (S9), Praga et González (S5, S6), González 2008 (S8), ADQI 2026 (S12), informations professionnelles Swissmedic de la ciprofloxacine, de la ceftriaxone, de la prednisone et du pantoprazole (S15 à S18). Aucune donnée extérieure au dossier n'a été ajoutée.

## Lacunes (reprises du dossier et choix de rédaction)
- Aucune recommandation de la Société suisse de néphrologie ni de l'ERA sur la NIA ; aucune dose standard de corticoïdes validée : le cours le dit explicitement (encadré d'alerte, fenêtre « cortico »).
- Homme hors directive SSI ; articles mediX et Primary and Hospital Care 2021 illisibles ; EAU lu partiellement (niveaux de preuve 3.7 non lus).
- Plusieurs articles lus en résumé seul (S5, S6, S8, S11 à S14, S19).
- Aucun critère diagnostique formel validé de la NIA : l'encadré de critères est présenté comme cadre pédagogique, avec cette réserve.
- Les sciences fondamentales sont limitées aux notions définitionnelles et aux mécanismes présents dans la revue suisse ; aucune donnée de physiologie ou d'histologie générale extérieure au dossier n'a été ajoutée. La mention de TINU = « Tubulointerstitial Nephritis and Uveitis » (développement littéral du glossaire) est un usage standard de la sigle, non tiré d'une source du dossier.
- Les informations professionnelles ne détaillent pas, dans le dossier, la mise en garde sur les précipités calcium-ceftriaxone ni les adaptations rénales de la gentamicine : indiqué comme non précisé.

## Auto-contrôle (cahier W)
- build_medina.py N12 (racine temporaire) : « N12 non couvertes: 0 », aucune erreur Pareto.
- Toute clé data-k possède son template data-pop ; aucune fenêtre orpheline ; identifiants uniques et tous préfixés n12- ; HTML a+b+c+d bien formé (pile vide).
- test_preview.py N12 : seule défaillance, une importation dynamique de preview/lesson-core.js absente de l'environnement (artefact de l'environnement de test, non lié au contenu) ; fenêtres, onglets et mode livre n'ont produit aucune autre erreur.
- Aucun fichier hors du dossier de la leçon n'a été modifié (ni chapters/, ni glossary/, ni chapters.json, ni git).

Audit différé — revue IA, distincte d'une validation médicale humaine.
