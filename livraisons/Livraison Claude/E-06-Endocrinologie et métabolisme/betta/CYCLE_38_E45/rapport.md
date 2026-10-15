# Rapport de rédaction — E45 (cycle Betta 38, C38-A2-ENDO)

Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers (octets)
- chapters/E45/E45_a.html 27107 (îlots 0 à 6 de la pathologie)
- chapters/E45/E45_b.html 23474 (îlots 7 à 14, critères formels `alert` puis paramètres clés `key`)
- chapters/E45/E45_c.html 25741 (onglet Examens : 5 îlots, 4 quiz ; onglet Sciences : physiologie, biochimie, histologie, génétique, 3 schémas SVG noir et blanc)
- chapters/E45/E45_d.html 9881 (onglet Pharmacologie : 5 îlots)
- chapters/E45/E45_pop1.html 14748 et E45_pop2.html 13772 : 37 fenêtres (dont 8 Pareto)
- glossary/e45.py 12029 : 49 entrées conditionnelles (`if k not in G`)

## Auto-contrôle
- HTML équilibré (aucune balise orpheline), identifiants uniques et préfixés `e45-`.
- 29 clés de fenêtres référencées, toutes définies, aucune fenêtre orpheline ; chaque Pareto couvre des îlots existants.
- `build_medina.audit()` sur le chapitre et ses fenêtres avec le glossaire : `{}`.

## Sources utilisées (dossier recherche.md / sources.json)
S1 à S24 ; rattachement par lien dans chaque paragraphe `src`. Aucune donnée hors dossier. Aucune dose pédiatrique inventée : les doses (thiamine, zinc, renutrition) sont étiquetées adulte ou essai.

## Choix de prudence
- Cellules « Non précisé » dans le tableau des configurations (absence de donnée dans les sources).
- Zones histologiques de la plaque non décrites (hors dossier) ; le rattrapage par sénescence est dit extrapolé de modèles glucocorticoïdes.
- Mnémotechnique PAMIR forgée pour le cours, signalée « aide pédagogique, non critère officiel ».

## Lacunes
Pas de recommandation suisse ni européenne (SSP, ESPGHAN, ESPE) sur le stunting nutritionnel ; courbes suisses 2011 non nommées ; renutrition pédiatrique absente ; indication de la GH dans E45 absente ; frontière E45 / E64.0 non précisée ; pas de posologie pédiatrique suisse (zinc, thiamine) ; pas de prévalence suisse ; plusieurs sources lues en résumé seulement.
