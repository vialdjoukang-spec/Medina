# C-01-Cardiologie — injection des livraisons Claude, lot 5

Les **128 sources HTML de quatorze cours** sont injectées dans `chapters/`, après réception figée à `67c01cb4`, puis complément final à `2947ba8639ddb56f884bf09ab0658ab70f17e035`. Les quatre fichiers de fenêtres I48 corrigés bibliographiquement sont fusionnés à trois voies ; le résultat conserve les adaptations médicales et égale la proposition finale de Claude. Le glossaire Q21 reçoit la correction TBX1. Les nouveautés ESC 2026 sont distinguées dans les fenêtres comparatives I48, I50 et I42.

Cette réception complète le lot 4 I48. **15 des 20 cours présents ont reçu ces livraisons de justification étendue : 75 %.** Ce pourcentage mesure la réception et l’injection, pas l’achèvement du Fragment 01. Aucun cours n’est déclaré clos par une contrelecture médicale indépendante exhaustive. Le Fragment 02 attend la clôture vérifiée du Fragment 01.

## Réception, empreintes et conservation

- Premier paquet : 95 sources, dix cours, empreintes de base et propositions conformes ; copies reçues égales aux blobs GitHub figés. Deux lectures par chemin divergentes ont été reprises par SHA de blob, sans modification du manifeste original.
- Complément final : 33 sources, quatre cours, mêmes contrôles conformes ; glossaire Q21 et quatre rapports de vérification égaux à leurs blobs GitHub.
- Les 95 propositions du premier paquet sont inchangées dans le lot 5 final. Les corrections bibliographiques I48 sont également identiques au résultat de la fusion Codex. Le manifeste final comporte 132 sources : 128 des quatorze cours et quatre I48.
- Les originaux, manifestes et rapports restent sous `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/`, `2026-10-07-LOT5_FINAL/` et `2026-10-07-I48_BIBLIOGRAPHY/`. Les adaptations canoniques sont consignées séparément.
- Les preuves du déploiement I48 publiées concurremment au commit `d6718ba5` sont conservées. Elles documentent la version publique antérieure ; elles ne prouvent pas le déploiement du nouveau lot 5.

## Cours injectés et fenêtres natives

| Cours | Fenêtres natives actuelles |
| --- | ---: |
| I00 — Rhumatisme articulaire aigu | 70 |
| I30 — Péricardites, épanchement péricardique, tamponnade et constriction | 78 |
| I33 — Endocardite infectieuse | 85 |
| I34 — Valvulopathies mitrales, tricuspides et pulmonaires | 106 |
| I35 — Valvulopathies aortiques | 101 |
| I40 — Myocardites | 76 |
| I42 — Cardiomyopathies | 89 |
| I44 — Troubles de la conduction et bradycardies | 113 |
| I46 — Arrêt cardiaque | 91 |
| I47 — Tachycardies paroxystiques supraventriculaires et ventriculaires | 97 |
| I49 — Extrasystoles et autres arythmies | 87 |
| I71 — Anévrismes et dissections artérielles | 18 |
| I80 — Thrombose veineuse profonde et thromboses veineuses | 20 |
| Q21 — Cardiopathies congénitales de l’adulte | 125 |
| **Quatorze cours du lot 5** | **1 156** |
| I48 — Fibrillation et flutter auriculaires, lot 4 et complément bibliographique | **101** |

Les fenêtres natives ne sont pas les 204 entrées des banques de justifications, lesquelles concernent quinze cours et 205 cibles explicites. Ces mesures ne comptent ni les clics ni des affirmations médicales certifiées.

## Adaptations Codex

Les mentions de validation interne 20/20 ont été retirées des en-têtes des quatorze cours reçus. Les références utiles restent dans les passages concernés. I42 n’attribue plus à l’ESC 2026 des classes non vérifiées et ne déduit plus une classe de la formulation narrative. Sa comparaison sépare le référentiel des cardiomyopathies de celui de l’insuffisance cardiaque. La correction bibliographique I48 ne touche aucune proposition médicale.

La mention générale d’I80 attribuant les doses à une information professionnelle suisse non relue a été remplacée par l’attribution ESVS 2021/résumés européens réellement décrite dans le rapport reçu, avec vérification du produit suisse à faire. La correction TBX1 distingue son expression pharyngée et son influence indirecte sur la crête neurale ; contrelecture ciblée de la recherche primaire : Vitelli et al., *Development* 2005, https://journals.biologists.com/dev/article/132/23/5307/43163/Tbx1-expression-in-pharyngeal-epithelia-is .

La fréquence de fièvre EURO-ENDO d’I33 était déjà corrigée à 78 % dans la remise reçue. La vérification primaire confirme 77,7 % dans l’ESC 2023 ; elle n’est pas présentée comme une nouvelle correction Codex. Voir `I33_CONFIRMATION.json`.

## Contrôles et portée exacte

| Contrôle | Résultat |
| --- | --- |
| Tests unitaires | 80 réussis |
| Dix premiers cours, navigateur 1360/390 px | 8 637 vérifications, 20 vues, aucune erreur |
| Quatre cours complémentaires, navigateur 1360/390 px | 2 421 vérifications, 8 vues, aucune erreur |
| **Total des quatorze cours** | **11 058 vérifications ; les 1 156 fenêtres natives sont ouvertes aux deux largeurs** |
| I48 après fusion bibliographique et comparaisons I48/I50 | 931 vérifications, toutes les 101 fenêtres I48 ouvertes aux deux largeurs |
| Banques de justifications | 2 400 vérifications, 204 entrées et quinze cours, aucune erreur |
| Navigation S01 | 71 vérifications réussies |
| Sciences des 31 cours intégrés | Contrats réussis, aucune erreur |
| Construction et audit final | 22 fragments, syntaxe JavaScript et reproductibilité conformes |

Les parcours ouvrent les fenêtres depuis les quatre onglets, les quiz après réponse et les Pareto, suivent leurs renvois, vérifient les retours, la restitution du focus, les largeurs et le texte à 24 px. Les titres affichés sont comparés aux templates construits. Les rapports complets locaux et leurs empreintes sont référencés dans `VALIDATION_SUMMARY.json`. Les scripts reproductibles sont joints.

Les dix premiers cours ont été contrôlés avant le complément final : leurs 96 sources HTML canoniques, comparaison I42 comprise, sont strictement inchangées depuis ce contrôle. Les quatre cours supplémentaires et I48 disposent de leurs contrôles propres après reconstruction. Les tests de compilation, de Sciences et des banques sont exécutés sur le contenu final. On ne cumule pas ces séries comme une certification médicale.

## Réserves et suite

Les rapports Claude contrôlent ses propositions, avec des réserves explicites ; ils ne certifient pas la relecture de toute affirmation héritée. Restent notamment des informations professionnelles suisses non relues, des tableaux de doses/classes non recoupés, des seuils et chiffres historiques, et des divergences de référentiels à résoudre. Les originaux des réserves sont conservés ; ne pas convertir un succès technique en clôture médicale.

La répartition active reste **10 cours présents Codex / 10 Claude**, plus deux productions prioritaires chacun. I47, I46, I49, I71 et I80, rédigés par Claude avant leur transfert à Codex, sont acceptés et conservés. Codex poursuit ses dix cours et les productions I73 — Autres maladies vasculaires périphériques / I95 — Hypotension. Claude ferme les réserves de ses dix cours et produit I83 — Varices des membres inférieurs / I89 — Autres atteintes non infectieuses des vaisseaux et des ganglions lymphatiques.

Les cinq cours sans cette livraison étendue sont I50 — Insuffisance cardiaque ; I21 — Syndromes coronariens aigus et infarctus du myocarde ; I25 — Syndromes coronariens chroniques et angor ; I10 — Hypertension artérielle ; I70 — Athérosclérose périphérique, artériopathie des membres inférieurs et ischémie aiguë. Ils disposent déjà de banques ciblées, qui ne remplacent pas la justification et la revue intégrales.

Le Fragment 01 contient toujours 20 cours uniques. Son catalogue historique compte 77 catégories CIM-10-GM réparties en onze rubriques ; les entrées restantes, leurs regroupements et le rattachement incohérent d’A43 — Nocardiose doivent être arbitrés. La complétude CIM-11 n’est pas établie. Anthropic Serif est absente du dépôt et des polices installées ; la préférence est conservée sans prétendre l’avoir appliquée.


## Convergence avec la publication médicale et l’organisation du 8 octobre

Contenu contrôlé : `1fe38461d8502fb7984d66b0fe223afecd759889` (arbre `3976a77f33f86fb5d4db5f7de5a1594662313884`). Le main médical `f149128` et la répartition des fragments `20915d9` sont conservés. Les 36 fichiers en conflit sont résolus et documentés dans [CONVERGENCE_MAIN.json](CONVERGENCE_MAIN.json). Les 11 arbitrages I48 et les 15 adaptations complémentaires sont préservés ; quatre formulations ont été harmonisées après contrôle indépendant ciblé. Le comparateur I42 conserve le référentiel ESC 2023 lu, sans ajouter une classe ESC 2026 non consultée.

97 tests unitaires, 31 cours Sciences, 22 fragments avec JavaScript valide et compilation reproductible. Contrôles navigateur : 11 118 sur 14 cours, 931 sur I48 final, 2 400 sur les 204 banques/15 cours, 71 sur S01, 748 sur le tableau des 22 fragments. Aucune erreur JavaScript ; toutes les fenêtres attendues des cours contrôlés sont ouvertes à 1360 et 390 px. Voir [la synthèse de validation](convergence_main/VALIDATION_SUMMARY.json). Les rapports distinguent leurs empreintes d’entrée ; les 14 sources sont inchangées après leur contrôle, puis I48 a été recontrôlé après ses harmonisations.

Les 22 remises Codex contiennent 274 sources vérifiées contre cet arbre, dont 187 pour C-01-Cardiologie : [preuve](convergence_main/EXPORT_PROOF.json). Le lot figé reçu est `2947ba8` ; les travaux plus récents de Claude sont repérés séparément.

Le Fragment 01 reste ouvert : 15/20 cours présents ont reçu l’enrichissement étendu. La relecture exhaustive de toutes les affirmations et l’inventaire CIM-11 restent à terminer. La priorité cardiologie et la répartition 10/10 sont conservées. Les 21 fragments suivants sont attribués 11 à Claude/10 à Codex, avec un seul chapitre actif par agent et audit croisé avant injection ; cette attribution ne les déclare pas commencés.
