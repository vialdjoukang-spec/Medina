# Rapport de rédaction — C85, cycle Betta 33 (C33-A3-HEM, Sonnet 5.5)

Fragment H-08-Hématologie · C85 — Lymphome non hodgkinien, de types autres et non précisés · état au 15.10.2026.
Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers produits (dossier `chapters/C85/` et `glossary/`)
| Fichier | Octets | Contenu |
|---|---|---|
| C85_a.html | 34408 | En-tête, quatre onglets, plan, îlots 0 à 6 (question clinique, définitions, épidémiologie, physiopathologie avec figure 1, causes et diagnostics incomplets, anamnèse, examen) |
| C85_b.html | 43828 | Îlots 7 à 15 (démarche diagnostique avec figure 2, différentiel, urgences, première ligne, lymphome B non précisé, rechute, réponse et suivi, situations particulières, critères formels `alert` puis paramètres clés `key`), fermeture de l'onglet Pathologie |
| C85_c.html | 39291 | Onglet Examens (8 îlots, 5 quiz de cas) et onglet Sciences (anatomie, histologie, immunologie, génétique moléculaire ; figures 3 à 6) |
| C85_d.html | 16502 | Onglet Pharmacologie (5 îlots) ; fermeture du `template` |
| C85_pop1.html | 28774 | 29 fenêtres (définitions, mécanismes, clinique, différentiel) |
| C85_pop2.html | 19214 | 20 fenêtres (examens, schémas, médicaments) dont 7 Pareto |
| glossary/c85.py | — | Abréviations définies, entrées conditionnelles |

Volumes : environ 16 000 mots, 49 fenêtres (dont 7 Pareto), 5 quiz de cas, 6 figures SVG.

## Sources utilisées
Uniquement celles de `sources.json` (23) : CIM-10-GM 2024 (BfArM, OFS), OFS 2021, Onkopedia 12/2025 (SSH, SGMO, DGHO, OeGHO), ESMO 2016, IELSG37, OMS 5e édition, ICC 2022 (résumé), Lugano, Nappi 2025, Chen 2021, Cook 2024, LYSA 2025 (résumé), Juanpere 2013, Villa et Sehn, Sabattini (résumé), Wei, Hoogstra (résumé), informations professionnelles suisses Keytruda, Breyanzi, Yescarta, MabThera, Polivy. Aucune recommandation américaine comme fondement d'une conduite.

## Choix de structure
- Plan monographique classique : aucun îlot ni tableau consacré au code CIM. Les sous-codes C85.1, C85.2, C85.7 et C85.9 sont traités en prose (îlot 1, fenêtre `c85-cim`). C85.2 est développé comme maladie ; C85.1, C85.7 et C85.9 sont traités comme diagnostics à compléter (îlots 4, 7, 11).
- Dernier îlot de la pathologie : critères formels (`div.alert`) puis paramètres clés (`div.key`). Pareto en fin de chaque grande partie (7 Pareto).
- Divergence suisse signalée : Polivy® n'est autorisé en Suisse qu'en rechute, alors que l'EMA l'autorise en première ligne (îlots 11 et p-5).

## Lacunes explicites (reprises du dossier)
Aucun article du Swiss Medical Forum ni incidence suisse propre à C85 ; LYSA 2025 et ICC 2022 lus en résumé ; recommandation ESMO de 2016 ; différentiel tiré d'une revue de 2013 ; aucune source sur la corticothérapie avant biopsie ni sur le risque anesthésique (aucune conduite chiffrée proposée) ; partie finale d'Onkopedia non lue (grossesse détaillée) ; aucune entité rattachée à C85.7 ; doses des composants du CHOP et de l'axicabtagène absentes du dossier (non inventées) ; aucun intervalle de référence suisse de laboratoire fourni.

## Points non issus littéralement du dossier (à signaler à l'audit)
- Lectures anatomiques élémentaires reliant les signes rapportés aux structures comprimées (voies aériennes, tube digestif haut, veine cave supérieure ; îlot 5, fenêtres `c85-vcs`, `c85-compression`, onglet Sciences) : explicitement présentées comme lectures, non comme données de source.
- Développement littéral de sigles standard (CHOP, EPOCH, gènes, marqueurs CD, sociétés) pour le glossaire ; les sigles que le dossier ne développe pas (MAL, MACOP-B, R-V, R-DHAP, R-GDP, R-ICE, BEAM, TRANSFORM) sont déclarés tels dans le glossaire, sans invention.
- Vignettes, quiz et mnémotechnique BSTED : cas pédagogiques fictifs ou aide pédagogique, non critère officiel.

## Auto-contrôle (cahier W)
- `build_medina.audit()` sur chaque fichier, avec glossaire du dépôt plus `glossary/c85.py` : `{}` pour les six fichiers.
- HTML bien formé (pile de balises équilibrée sur a+b+c+d et sur chaque fichier de fenêtres) ; aucun identifiant dupliqué.
- Toute clé `data-k` a son `template data-pop` ; aucune fenêtre orpheline ; toutes les clés préfixées `c85-` ou `pareto-c85-`.
- Pareto : identifiants `data-cover` tous présents ; `pareto_ratios()` s'exécute sans erreur.
- Non exécuté : `test_preview.py` (le chapitre n'est pas injecté dans `chapters/` ni `chapters.json`, conformément à la consigne).
