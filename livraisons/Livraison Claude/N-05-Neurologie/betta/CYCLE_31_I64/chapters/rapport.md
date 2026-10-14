# Rapport de rédaction — I64, cycle Betta 31, agent C31-A1-NEUR (Sonnet 5.5)

Leçon : I64 — Accident vasculaire cérébral, non précisé comme étant hémorragique ou par infarctus (N-05-Neurologie). Rédigée le 14.10.2026 à partir du seul dossier `recherche.md` et `sources.json` (20 sources).

## Fichiers (octets)
chapters/I64/I64_a.html 20 210 · I64_b.html 19 999 · I64_c.html 21 627 · I64_d.html 6 629 · I64_pop1.html 12 675 · I64_pop2.html 12 717 · glossary/i64.py (25 abréviations). Environ 9 800 mots.

## Contenu
- Pathologie : 14 îlots (0 à 13), dernier îlot = critères formels (`div.alert`) puis paramètres clés (`div.key`), références datées en fin d'onglet ; 5 Pareto ; 2 figures (fenêtres thérapeutiques, algorithme de résolution du code).
- Examens : 5 îlots, 3 quiz, tableaux de seuils et de situations.
- Sciences : 4 disciplines (physiologie, hémodynamique, biostatistique, hémostase), une figure SVG noir et blanc et une corrélation clinique chacune.
- Pharmacologie : 4 îlots, tableau des doses altéplase/ténectéplase (informations professionnelles suisses), encadré d'interactions, gestes à éviter.
- 31 fenêtres (21 explicatives, 10 Pareto), 6 quiz.

## Sources utilisées
S1 à S20 du dossier (CIM-10-GM 2024 BfArM ; Hänsel 2025 ; ESO 2021 thrombolyse ; ESO–ESMINT 2019 ; ESO 2025 pression artérielle ; ESO/EANS 2025 ; Weir 1994 ; informations professionnelles Actilyse juin 2025 et Metalyse mai 2025 ; Essen 2023, etc.). Aucune donnée extérieure au dossier.

## Divergence et arbitrage
INR sous antivitamine K : ESO 2021 ≤ 1,7 ; informations professionnelles suisses (2025) contre-indication > 1,3. Le texte suisse, plus récent et propre au produit, est retenu pour l'usage autorisé ; l'ESO est présenté en regard (fenêtre `i64-inr`).

## Lacunes (reprises du dossier)
Définition formelle de l'AVC (OMS/ESO) ; critères SFCNS 2021 ; lignes directrices de la Swiss Stroke Society ; physiopathologie de la pénombre (seul l'usage en imagerie est enseigné) ; part suisse infarctus/hémorragie et part d'I64 ; antagonisation des anticoagulants dans l'hémorragie ; grossesse ; recommandation ESO dédiée à la ténectéplase ; données du registre suisse. Anatomie et histologie non rédigées faute de source dans le dossier : les sciences retenues sont celles que le dossier permet d'étayer. Développements lexicaux d'ESMINT, EANS, SFCNS signalés dans le glossaire comme absents du dossier.

## Auto-contrôle
HTML bien formé (aucune balise déséquilibrée), identifiants uniques et préfixés `i64-`, toutes les clés `data-k` ont une fenêtre, aucune fenêtre orpheline, couvertures Pareto valides, abréviations toutes présentes au glossaire. `build_medina.py` et `test_preview.py` non exécutés (interdiction de toucher la racine).

Audit différé — revue IA, distincte d'une validation médicale humaine.
