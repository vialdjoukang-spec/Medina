# Rapport de rédaction — G91 Hydrocéphalie (N-05-Neurologie)

Cycle Betta 40, leçon 1 · agent C40-A3-NEUR (Sonnet 5.5) · 15.10.2026
Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers (octets)
- chapters/G91/G91_a.html 24 539 (en-tête, plan, îlots 0–5)
- chapters/G91/G91_b.html 23 601 (îlots 6–13, dont critères formels `alert` puis paramètres clés `key`)
- chapters/G91/G91_c.html 20 076 (Examens e-1 à e-5 ; Sciences : anatomie, histologie, physiologie, biochimie, 4 schémas SVG)
- chapters/G91/G91_d.html 7 124 (Pharmacologie p-1 à p-4)
- chapters/G91/G91_pop1.html 31 302 (36 fenêtres) ; G91_pop2.html 10 037 (17 fenêtres dont 10 Pareto)
- glossary/g91.py 13 515 (50 entrées lettre à lettre ou noms propres signalés)

## Sources utilisées
S1 à S19 du dossier `sources.json` (aucune donnée extérieure). Les fenêtres citent leurs sources. Les recommandations américaines (AAN 2015) sont mentionnées uniquement comme écartées.

## Auto-contrôle (cahier W)
- HTML bien formé (analyse de balises : aucune erreur) ; identifiants uniques, préfixés `g91-`.
- Les 43 clés de fenêtres référencées existent ; aucune fenêtre inutilisée ; 10 Pareto, couverture des îlots vérifiée ; `pareto_ratios` du moteur passe.
- `build_medina.audit()` renvoie `{}` sur les six fichiers avec le glossaire G91.
- Quatre onglets, quiz de cas (4), tableaux introduits et commentés, mnémotechnique marquée « aide pédagogique, non critère officiel ».

## Lacunes (reprises du dossier, non comblées)
Aucune ligne directrice suisse ni EAN spécifique ; aucun débit ni volume humain de LCS ; recommandations formelles sur le drain ventriculaire externe (image) et sevrage ; G91.3 adulte ; score ETVSS et taux d'échec des dérivations à 1–2 ans ; histoire naturelle non opérée ; sept entités CHiA ; triade de Cushing ; dose adulte d'acétazolamide ; valeurs normales de l'index d'Evans et du périmètre crânien ; conduite et fréquence de surveillance de l'acétazolamide. Sigles d'essais (PENS, BASICS, ULTRA, SINPHONI, HARM, PaVM) non développés faute de source lue.
Chapitre plus court que N17 car limité strictement au dossier ; aucune extrapolation.

## Non touché
chapters/ racine, glossary/ racine, chapters.json, git.
