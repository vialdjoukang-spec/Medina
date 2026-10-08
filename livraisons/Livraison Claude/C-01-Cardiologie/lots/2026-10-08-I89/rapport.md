# Lot I89 — I89 — Autres atteintes non infectieuses des vaisseaux et des ganglions lymphatiques (C-01-Cardiologie)

## Identité et provenance

- **Responsable :** Claude (assemblage, contrôles, Git), branche `claude/loving-shannon-spwrhc`, PR #12.
- **Base :** `main` `918ef69a8526bf0be38ffdf4f88438ad61d9a8a7`.
- **Remise :** création de cours par la voie branche (hors `apply-claude`), comme I83.
- **Ordre :** la v5 de l'harmonisation **I83 — Varices des membres inférieurs (C-01-Cardiologie)** est médicalement acceptée par Codex (reçu `918ef69`, aucune réserve bloquante). Selon la consigne du propriétaire, le chapitre suivant s'enchaîne après la remise à Codex pour audit.
- **Sous-agents :**
  - architecte (`verification/PLAN.md`) ;
  - quatre rédacteurs, un par onglet, chacun propriétaire de ses fichiers ;
  - deux vérificateurs indépendants : A + B (`verification_ab.json`) et C + D (`verification_cd.json`) ;
  - assemblage par Claude.

## Catégories traitées, regroupées sous le fragment propriétaire C-01-Cardiologie

| Catégorie | Traitement |
| --- | --- |
| I89.0- — Lymphœdème, non classé ailleurs (I89.00 à I89.09) | Traité en entier, centre du cours, y compris la lymphangiectasie |
| I89.1 — Lymphangite chronique | Traité ; la lymphangite aiguë (L03.-) est exclue, car infectieuse |
| I89.8 — Autres atteintes précisées (chylocèle non filarienne, réticulose lipomélanique, fistule, lymphocèle, reflux chyleux) | Traité (îlots 12 et 13) |
| I89.9 — Sans précision | Mentionné (îlot 1) |
| I97.2- — Lymphœdème après mastectomie | Traité (cas fil rouge, piège de codage) |
| I88.- — Lymphadénite non spécifique | **Articulée seulement** (îlot 13), non couverte |

Les renvois nomment **A46 — Érysipèle (I-03-Infectiologie)**, **I50 — Insuffisance cardiaque (C-01-Cardiologie)** et **P-02-Pneumologie**, ce dernier pour l'épanchement chyleux.

## Fichiers livrés (`sources/`, diff : `controles/diff_main.diff`)

| Fichier | Opération |
| --- | --- |
| `chapters/I89/I89_{a,b,c,d}.html`, `I89_pop{1..4}.html` | ajout, 8 fichiers |
| `glossary/i89.py` | ajout, 45 entrées |
| `chapters.json` | une entrée I89 insérée après I83 (couvre I89, I97 ; vague 9) |
| `tests/verify_s01_browser.cjs` | compte S01 de 21 à 22 cours, seule modification |

## Vérification médicale

Deux vérificateurs indépendants ont relu les quatre onglets et leurs fenêtres. Ils ont corrigé **57 erreurs**, détaillées avec avant, après et source dans `verification/` (29 erreurs en A + B, 28 en C + D). Par exemple :
- Stemmer, Vasa 1976 (PubMed 969857), et non 1979 ;
- syndrome de Noonan retiré de la ligne des anomalies chromosomiques (ISL 2023, III.B) ;
- essai de Dayes : bras expérimental exact (PubMed 24043733) ;
- essai de Ridner 2022 : proportions rapportées au sous-groupe ayant déclenché l'intervention.

Les écarts au plan sont consignés dans `verification/reserves_*.txt`. La patiente du cas s'appelle Mme L. ; Mme R. reste réservée à I83. La question racine de la figure 2 n'utilise pas de seuil de 72 heures, absent des sources. Le dasatinib est rangé parmi les mécanismes inconnus (Chen 2020).

**ESC 2026 :** aucune recommandation ne porte sur le système lymphatique. La seule comparaison utile concerne l'œdème cardiaque (fenêtre `i89-oed-systemique`).

## Contrôles (base `918ef69`, sorties hors dépôt)

| Contrôle | Résultat |
| --- | --- |
| `verifier_sigles.py I89` | `{}` |
| `test_v7.py --static I89` | OK — 36 357 mots, 43 fenêtres, 8 quiz, 5 Pareto |
| `test_v7.py --static I83` (non-régression) | OK |
| `build_front.py`, `--all-fragments`, `tests/audit_fragments.py` | 22 fragments, JavaScript valide, build reproductible ; sortie globale 9 996 896 octets compressés |
| `tests/verify_course_native.cjs I89` (1 360 et 390 px) | 2 595 contrôles, 0 échec (`controles/i89_native_results.json`) |
| `tests/verify_s01_browser.cjs` (22 cours) | 73 contrôles réussis |
| `test_v7.py I89` | OK |
| `python3 -m unittest discover -s tests` | 118 tests OK |

## Réserves

- **Médicales :** les doses du sirolimus, de l'octréotide, de la pénicilline V et de la prégabaline ont été lues par le rédacteur dans les informations des produits (EMA, étiquetage américain), mais pas relues par le vérificateur dans une source primaire locale. Elles sont attribuées à leur source dans le texte. Aucune posologie de l'érysipèle aigu n'est donnée ; le cours renvoie à A46.
- **Extrapolation signalée :** l'essai de Thomas 2013 porte sur la jambe ; son application au bras est signalée dans le texte, la fenêtre et le quiz.
- **Rédactionnelles :** le volume dépasse les repères du plan (texte A + B ≈ 11 440 mots) ; les tableaux 10.2 et 14.3 peuvent encore être resserrés.
- **CIM-11 :** couverture non établie. I88 n'est pas couverte.

## Demande de contrelecture

Audit croisé Codex du commit livré (voir PR #12), fichiers `sources/` de ce lot.
