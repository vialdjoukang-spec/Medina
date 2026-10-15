# Rapport de rédaction G09 — cycle Betta 35, leçon 2 (agent C35-A1-NEUR, Sonnet 5.5)

Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers (sous `livraisons/Livraison Claude/N-05-Neurologie/betta/CYCLE_35_G09/`)
| Fichier | Contenu |
|---|---|
| chapters/G09/G09_a.html | En-tête, onglet Pathologie, îlots 0–6 |
| chapters/G09/G09_b.html | Îlots 7–12 (critères formels, paramètres clés, références) |
| chapters/G09/G09_c.html | Examens e-1 à e-6 (3 quiz) ; Sciences : anatomie, physiologie, immunologie, biochimie (4 figures SVG) |
| chapters/G09/G09_d.html | Pharmacologie p-1 à p-5 |
| chapters/G09/G09_pop1.html, G09_pop2.html | 50 fenêtres (dont 14 Pareto) |
| glossary/g09.py | 24 entrées conditionnelles, aucune entrée existante écrasée |

Volume : environ 7 250 mots (onglets) et 4 040 mots (fenêtres), 3 quiz, 5 figures SVG, 4 onglets. Les tailles exactes en octets sont celles des fichiers livrés (`wc -c`).

## Sources utilisées
Les 27 entrées du dossier (S1–S26, S1b) : classification (S1, S1b, S2, S3), lignes directrices OMS 2025 (S4), revues et cohortes (S5–S12, S14–S16, S18, S19, S21, S22, S24, S26), OFSP et Revue médicale suisse sur la FSME (S13, S17), informations professionnelles suisses (S23 lévétiracétam, S25 FSME-Immun CC). S20 (titre seul) n'est pas utilisée au-delà de la mention en fenêtre `g09-lacunes`. Chaque paragraphe porte l'attribut `data-src`.

## Contrôles (auto-contrôle du cahier W)
- HTML bien formé (pile de balises vide pour le chapitre et les fenêtres) ; identifiants uniques et préfixés `g09-` ; classes limitées à la liste fermée.
- 35 clés `data-k` distinctes, toutes résolues par un `template data-pop` ; aucune fenêtre orpheline ; clés préfixées `g09-` / `pareto-g09-` ; `data-cover` tous valides.
- Build dans une racine temporaire (`MEDINA_ROOT`) : `G09 non couvertes: 0`. Contrôle navigateur (`test_preview.py` sur copie) : seul message, l'erreur d'environnement `lesson-core.js` identique à celle de N17 et G01 ; aucun autre échec (affichage, fenêtres, onglets, mode livre).
- Aucun fichier modifié hors du dossier de livraison (ni chapters/ racine, ni glossary/ racine, ni chapters.json, ni git).

## Lacunes et limites (héritées du dossier de recherche)
1. ESCMID 2016 non lu ; aucune recommandation suisse ni de l'EAN sur le suivi des séquelles ni sur l'encéphalite auto-immune.
2. Codage de la FSME (A84) et note B94.1 en CIM-10-GM 2024 non relus : le rattachement des séquelles FSME à B94.1 est présenté comme déduction.
3. Physiopathologie cellulaire, épileptogenèse, mécanisme de la fatigue, résorption du liquide cérébro-spinal : non rédigés.
4. Prise en charge de l'hydrocéphalie séquellaire, immunothérapie de l'encéphalite auto-immune, assurance-invalidité, médicaments de la fatigue ou de la cognition : absents, signalés comme lacunes dans le texte.
5. Valeurs normales d'audiométrie et seuils des tests neuropsychologiques : absents du dossier, non rapportés.
6. Contentieux FSME : rappel tous les 10 ans (OFSP, état juillet 2024) contre 3 à 5 ans (FI FSME-Immun CC) ; la recommandation fédérale prime, fenêtres `g09-vaccin-fsme` et `g09-fi-fsme`.
7. Éléments non issus du dossier, marqués dans le texte : vignette fictive, classement pédagogique des séquelles, rattachement de la perte de transmission à l'oreille moyenne (rappel didactique), mnémotechnique, déductions signalées comme telles. La FI du lévétiracétam est celle d'un générique ; la plupart des articles ont été lus au résumé.
