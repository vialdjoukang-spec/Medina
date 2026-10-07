# Lot ESC 2026 — comparaisons dans huit cours de C-01-Cardiologie

Responsable : Claude (orchestrateur). Sous-agents : huit producteurs (un par cours) et un vérificateur indépendant. Date : 8 octobre 2026. Branche `claude/loving-shannon-spwrhc`. Base canonique : `39b7ff0cc585c59ffbb99fb448940daa1950b34d` (convergence cardiologique de Codex, contenu `1fe3846`). Une première version préparée sur `b6e5d18` a été réappliquée sur cette base après la convergence : les huit cours s’appliquent sans échec. Le SHA livré figure dans le message de commit et dans la PR.

## Référentiels lus

Quatre documents ESC du 28.08.2026, lus en **texte intégral** (copies locales non versionnées) : insuffisance cardiaque (doi:10.1093/eurheartj/ehag100), réadaptation cardiaque (ehag099), maladie cardiovasculaire et maladie rénale chronique (ehag098), cinquième définition universelle de l'infarctus (ehag101). Chaque classe et chaque niveau cités viennent d'un tableau de recommandations ; aucune classe n'est déduite d'une formulation.

## Résultat par cours

| Cours | Fenêtre | Verdict | Erreurs corrigées | Réserves |
| --- | --- | --- | --- | --- |
| I30 — Péricardites, épanchement péricardique, tamponnade et constriction (C-01-Cardiologie) | `I30_pop_esc_comparison.html` (ajout) | corrigée | Ligne « Troponine » : « avant 2026, 99e percentile de la méthode » est inexact ; la quatrième définition (2018) recommandait déjà des seuils propres au sexe avec les dosages ultrasensibles (cinquième définition, section 14.1). La cinquième les rend nécessaires à la définition de la lésion. ; Réserve erronée : la cardiomyopathie restrictive n’a pas disparu du texte 2026 ; la note e du tableau de recommandations 4 exige le cathétérisme droit et gauche pour la distinguer de la constriction. | Le texte 2026 ne chiffre pas de seuil par dosage ; seuil féminin de la troponine T ≈ moitié du seuil masculin. ; La phrase de I30_c « seuil commun aux deux sexes » décrit le fabricant ; un complément du texte reste à décider. |
| I40 — Myocardites (C-01-Cardiologie) | `I40_pop_esc_comparison.html` (ajout) | corrigée | Biopsie 2026 décrite comme visant « toute insuffisance cardiaque d’origine incertaine » : surgénéralisation ; le tableau de recommandations 4 vise l’aggravation rapide malgré le traitement ou la suspicion d’inflammation, d’infiltration ou de surcharge non identifiable autrement. ; Arrêt progressif présenté sans sa condition : l’ESC 2026 le réserve à la préférence du patient (« to accommodate patient preference ») et le dit exceptionnel. | Hors ESC 2026, non corrigé : I40_b « FEVG modérément réduite » pour 41–49 %, que l’ESC 2025 nomme « légèrement réduite » (mildly reduced). |
| I42 — Cardiomyopathies (C-01-Cardiologie) | complément de la fenêtre canonique `i42-esc-2026-comparaison` | corrigée | Après fusion, la clé i42-esc-2026-comparaison existe déjà (fenêtre canonique Codex) : l’action « creer » aurait écrasé ou dupliqué la clé ; job converti en « completer » (fichier_cible I42_pop_esc_comparison), rubriques sans redite. ; Indication médicamenteuse à FEVG 45 % présentée sans la note e du tableau 5 (aucun grand essai randomisé limité à 41–49 %). ; Déduction « l’entraînement attend la réduction du gradient » et rappel de l’échocardiographie d’effort ESC 2023 : hors ESC 2026 et redite du cours ; retirés. | La rubrique canonique de Codex « ne suffit pas à attribuer une nouvelle classe ESC 2026 » peut coexister ; les classes sont désormais lues dans le tableau. |
| I33 — Endocardite infectieuse (C-01-Cardiologie) | `I33_pop_esc_comparison.html` (ajout) | corrigée | « La CIM-11 attribue à l’embolie coronaire une extension de code propre » : codes seulement proposés et en cours d’examen dans la cinquième définition ; retiré. ; Classe IIb de l’enveloppe attribuée à des « données observationnelles et modélisations » : l’essai WRAP-IT (population générale, sans modification d’effet selon la fonction rénale) y contribue ; reformulé. | Cinquième définition : document de consensus, non recommandation au sens strict. |
| I34 — Valvulopathies mitrales, tricuspides et pulmonaires (C-01-Cardiologie) | `I34_pop_esc_comparison.html` (ajout) | corrigée | — | Toutes les classes vérifiées : 2026 TEER I, B1 et IIb, C (tableau 17) ; 2025 I, A et IIb, B ; tricuspide 2025 IIa, A ; réadaptation IIa, B2 et IIb, B2 ; ESC 2021 IIa, B (tableau 6 de l’ESC 2026). ; Fiche I34_d : furosémide et spironolactone citent l’ESC 2021 (spironolactone inchangée en 2026). |
| I35 — Valvulopathies aortiques (C-01-Cardiologie) | `I35_pop_esc_comparison.html` (ajout) | corrigée | « Les troubles phosphocalciques accélèrent la calcification » : l’ESC 2026 présente cet effet comme théorique (le cinacalcet n’a pas réduit les événements) ; retiré de la fenêtre. ; Durabilité des bioprothèses généralisée au patient « plus jeune » : le texte la limite au patient jeune atteint de maladie rénale sévère, sans essai pour guider le choix ; reformulé. | Hors ESC 2026, non corrigé : I35_d, furosémide intraveineux « 20–40 mg chez le patient naïf » (ESC 2021) ; l’ESC 2026 (section 7.5.3) indique 40 mg chez le patient naïf et deux fois la dose orale habituelle chez le patient déjà traité. ; DapaTAVI non repris (texte sans recommandation). |
| I44 — Troubles de la conduction et bradycardies (C-01-Cardiologie) | `I44_pop_esc_comparison.html` (ajout) | corrigée | Ancres sans champ « new » et labels hors libellé « ESC 2026 : … » : format non conforme ; réécrites. Ancre I44_b-a2 (rubrique des sources) retirée. ; Comparaison du niveau B1 à « l’ancien niveau B » alors que la classe antérieure était I, A ; corrigé. | Raison de l’abaissement I → IIa non explicitée par l’ESC 2026. ; BLOCK HF : fraction ≤ 50 % ; classification 2026 : < 50 %. |
| Q21 — Cardiopathies congénitales de l’adulte (C-01-Cardiologie) | `Q21_pop_esc_comparison.html` (ajout) | corrigée | Causalité non démontrée : l’hypertension, le diabète et l’obésité étaient présentés comme expliquant le risque d’insuffisance cardiaque multiplié par huit ; ce chiffre est un risque relatif global par rapport à des témoins (section 4.1.4.8). Reformulé. ; Ancres sans champ « new » et labels hors libellé « ESC 2026 : … » : réécrites. | Aucune indication 2026 propre au Fontan, au ventricule droit systémique ni aux cardiopathies cyanogènes. |
| I00 — Rhumatisme articulaire aigu (C-01-Cardiologie) | aucune (bilan seul) | confirmé : aucun changement | — | Les stades A à D du cours sont ceux de la WHF (cardiopathie rhumatismale) ; garder la mention « de la WHF » pour éviter la confusion avec les stades 2026 de l’insuffisance cardiaque. |

## Incohérences repérées hors du périmètre ESC 2026 (non corrigées, à traiter)

- I40_b, tableau de risque : « FEVG modérément réduite » au lieu de « légèrement réduite » (ESC 2025, « mildly reduced », 41–49 %).
- I35_d : furosémide intraveineux 20–40 mg chez le patient naïf (ESC 2021) contre 40 mg en 2026 (deux fois la dose orale habituelle chez le patient déjà traité, section 7.5.3).
- I30_c : troponine T ultrasensible 14 ng/L « seuil commun aux deux sexes » ; la cinquième définition exige un seuil propre au sexe (complément du texte à décider).

## Fichiers remis (`livraison.json`)

| Cible | Opération | SHA-256 d'origine | SHA-256 proposé |
| --- | --- | --- | --- |
| `chapters/I30/I30_c.html` | replace | `5dfeb9e062d5` | `d2af1a9fe40e` |
| `chapters/I30/I30_pop_esc_comparison.html` | add | `—` | `c3a0b1a5aa71` |
| `chapters/I33/I33_b.html` | replace | `a9c65f458619` | `d794ef67448c` |
| `chapters/I33/I33_pop2.html` | replace | `d56b33dbb981` | `f04bea3a6ff6` |
| `chapters/I33/I33_pop_esc_comparison.html` | add | `—` | `e4f66102035a` |
| `chapters/I34/I34_b.html` | replace | `dd9918c4f1a3` | `51d09c66b13d` |
| `chapters/I34/I34_pop_esc_comparison.html` | add | `—` | `433086d28496` |
| `chapters/I35/I35_b.html` | replace | `fb3e260404db` | `a8aa392f9087` |
| `chapters/I35/I35_pop_esc_comparison.html` | add | `—` | `064b0b86fea7` |
| `chapters/I40/I40_b.html` | replace | `7a5ab7c9a875` | `2dae7b62d3f8` |
| `chapters/I40/I40_pop_esc_comparison.html` | add | `—` | `ca84f5b02d36` |
| `chapters/I42/I42_a.html` | replace | `74eed9c83f1b` | `08aa19271173` |
| `chapters/I42/I42_b.html` | replace | `22b4ec162f5d` | `264bc87bd53e` |
| `chapters/I42/I42_d.html` | replace | `f96f42ccf223` | `6051d21e7eb6` |
| `chapters/I42/I42_pop2.html` | replace | `e3913844c5c2` | `8fc74c92f09c` |
| `chapters/I42/I42_pop5.html` | replace | `60fa151f6db2` | `e20d967904e0` |
| `chapters/I42/I42_pop6.html` | replace | `84ece3298f6e` | `d4e6402a105c` |
| `chapters/I42/I42_pop_esc_comparison.html` | replace | `cba5e2c3ba31` | `23460f78b1be` |
| `chapters/I44/I44_a.html` | replace | `59fca80ea61c` | `3572613ac5ca` |
| `chapters/I44/I44_b.html` | replace | `53be3609df86` | `c29e5b0c3864` |
| `chapters/I44/I44_c.html` | replace | `f7499e2e6a5f` | `4e387c5f207a` |
| `chapters/I44/I44_pop_esc_comparison.html` | add | `—` | `9af445722cce` |
| `chapters/Q21/Q21_a.html` | replace | `6a0fbe86a8b9` | `42882f9dfda7` |
| `chapters/Q21/Q21_b.html` | replace | `7949c1806ace` | `86151c32498d` |
| `chapters/Q21/Q21_pop_esc_comparison.html` | add | `—` | `ebd5b1448b76` |

## Commandes exécutées (application temporaire aux sources canoniques, puis restauration)

```
python3 travail/justification/appliquer_justifications.py <CODE> travail/esc2026/<CODE> --ecrire   # 8 cours, aucun échec
cp sources/chapters/<CODE>/*.html chapters/<CODE>/ ; python3 test_v7.py --static I30 I33 I34 I35 I40 I42 I44 Q21   # OK
verifier_sigles.py <CODE> chapters/<CODE>/*.html   # {} pour les 8 cours
MEDINA_OUT=../dist_esc python3 build_front.py ; build_front.py --fragment S01   # 16,2 Mo → 9,7 Mo ; S01 9,1 Mo → 4,4 Mo
MEDINA_OUT=../dist_esc python3 test_v7.py I30 I33 I34 I35 I40 I42 I44 Q21   # OK (navigateur)
git checkout -- chapters/ ; git clean -f chapters/   # sources canoniques restaurées
python3 tools/livraison.py check-claude 'livraisons/Livraison Claude/C-01-Cardiologie'   # empreintes et chemins conformes
```

Contrôles non exécutés : affichage mobile et fragment autonome ouvert à la main ; ils sont à refaire après injection.

## Réserves générales

- Une comparaison ESC 2026 vérifiée ne valide pas le reste du cours. Les huit cours restent en `pending_exhaustive_review` jusqu'à l'audit croisé de Codex.
- Couverture CIM-11 non établie.

## Demande à Codex

Audit croisé de ce lot au commit indiqué dans la PR, puis `python3 tools/livraison.py apply-claude 'livraisons/Livraison Claude/C-01-Cardiologie'`. Le lot 5 précédent (manifeste et copies) est archivé sous `archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/`, conformément au reçu `CLAUDE_LOT5_FINAL_20261007.json`.
