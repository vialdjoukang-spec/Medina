# Rapport C31-A1-NEUR — I62, Autres hémorragies intracrâniennes non traumatiques (N-05-Neurologie)

Audit différé — revue IA, distincte d’une validation médicale humaine.

## Fichiers livrés (cycle Betta 31, leçon 1)

| Fichier | Octets | Empreinte SHA-256 (16 premiers caractères) |
|---|---|---|
| chapters/I62/I62_a.html | 24495 | 5e210ff3bdb8a630 |
| chapters/I62/I62_b.html | 41105 | be7d177217862e6c |
| chapters/I62/I62_c.html | 30381 | 329d12525ef8d4e8 |
| chapters/I62/I62_d.html | 11816 | c3ebe8c3ddc9d0fd |
| chapters/I62/I62_pop1.html | 31781 | e8d37de87b0b2866 |
| chapters/I62/I62_pop2.html | 22403 | 522b306bf00e254f |
| glossary/i62.py | 4717 | 220d5c4cc7a78349 |
| recherche.md, sources.json | fournis (entrée) | — |

Total rédigé : 166698 octets.

## Contenu
- Monographie en quatre onglets : Pathologie (îlots 0 à 12, références, dernier îlot = critères formels `alert` puis paramètres clés `key`), Examens (e-1 à e-5), Sciences (Anatomie, Histologie, Physiologie, Biochimie), Pharmacologie (p-1 à p-4).
- 50 fenêtres (36 explicatives, 14 Pareto), 4 quiz de cas, 6 figures SVG noir et blanc légendées, environ 11 900 mots de corps et 5 200 mots de fenêtres.
- Glossaire `glossary/i62.py` : 12 entrées (HSDC, GCS, mRS, Dex-CSDH et noms d’essais honnêtement non développés).

## Sources utilisées
Uniquement celles de `sources.json` (S1 à S41), citées dans les fenêtres et la section de références. Les informations professionnelles suisses (S27, S28, S29, S34, S37, S41) sont reliées au portail Swissmedic Info, faute d’URL de fiche dans le dossier.

## Lacunes reprises du dossier et traitées honnêtement
- Aucune recommandation suisse ou européenne propre à l’hématome sous-dural chronique ; guide britannique ICENI lu en résumé seulement (non détaillé).
- Antidotes : libellé et force des recommandations européennes non lisibles ; application à l’espace sous-dural signalée comme extrapolation ; dose du concentré donnée selon la monographie suisse et le consensus, sans trancher.
- Résultats de TORCH non trouvés ; posologie adulte de la vitamine K et information professionnelle de la dexaméthasone non lues ; effets indésirables et contre-indications de plusieurs produits signalés « non détaillés ».
- I62.9 : aucune source spécifique (rubrique décrite uniquement par son intitulé) ; diagnostics différentiels hygroma, pachyméningite, lymphome dural mentionnés sans critère ; sémiologie de l’hypotension intracrânienne non détaillée ; pas de donnée sur la grossesse ni l’insuffisance rénale ou hépatique.
- Valeurs de référence biologiques non présentes dans le dossier : renvoi au laboratoire de l’établissement.
- Écart d’arrondi signalé : 23 ÷ 435 = 5,3 % alors que la source indique 5,2 %.

## Auto-contrôle (cahier W)
- `build_medina.audit()` sur une copie isolée de la racine : `I62 non couvertes: 0`, aucune erreur Pareto.
- HTML bien formé (pile vide), identifiants uniques et préfixés `i62-`, toutes les clés `data-k` ont leur `template data-pop`, aucune fenêtre orpheline, aucun résidu de macro.
- Contrôle navigateur `test_preview.py` non exécuté : Chromium de Playwright non installé dans l’environnement.
- Aucun fichier modifié hors du dossier du cycle ; ni `chapters/` racine, ni `glossary/` racine, ni `chapters.json`, ni git.
