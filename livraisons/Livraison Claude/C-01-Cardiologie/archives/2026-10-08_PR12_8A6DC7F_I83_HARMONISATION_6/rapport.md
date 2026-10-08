# Lot I83-HARMONISATION-6 — I83 — Varices des membres inférieurs (C-01-Cardiologie)

## Objet

Ce lot remplace `2026-10-08-I83-HARMONISATION-5` (tête `d5b46aa`). Le contre-audit médical Codex de la v5 est **favorable : aucune réserve majeure ou bloquante, deux réserves mineures** (commentaire PR #12 du 08.10.2026, 13 h 53). Ce lot applique ces deux réserves en une seule remise, avec le texte proposé par Codex. Base : `main` `1c39691289c49cb701345026b5ab9334f5330225`, dont les sources I83 sont identiques à `8d6deee`. Il ne contient aucun autre changement.

## Réserves appliquées

| Réserve | Fichier | Correction |
| --- | --- | --- |
| I83-V5-MIN-01 | `I83_c.html` (îlot écho-Doppler, perforante de Mme R.) | « L'ESVS réserve l'appellation de perforante pathologique à une perforante située sous un ulcère… » devient « L'ESVS décrit notamment comme « perforantes pathologiques » celles situées près d'un ulcère actif ou cicatrisé (§ 4.6.6) ; il emploie aussi ce terme pour des perforantes répondant aux critères hémodynamiques et de calibre, en particulier dans une zone d'altérations cutanées (§ 2.3.1.1). Cette qualification ne suffit pas à poser une indication thérapeutique. » Aucune autre occurrence n'existe dans le chapitre. |
| I83-V5-MIN-02 | `I83_pop2.html` (Complications, Pareto) et `glossary/i83.py` (entrée ARTE) | Les trois fréquences de 1,4 % et 1,7 % sont rattachées aux **ablations thermiques** de la grande saphène, avec le texte exact de Codex. |

## Contrôles (base `main` `1c39691`, sorties hors dépôt)

| Contrôle | Résultat |
| --- | --- |
| `verifier_sigles.py I83` | `{}` |
| `test_v7.py --static I83` | OK — 41 876 mots, 47 fenêtres, 6 quiz, 6 Pareto |
| `build_front.py`, `--all-fragments`, `tests/audit_fragments.py` | 22 fragments, JavaScript valide, build reproductible |
| `tests/verify_course_native.cjs I83` (1 360 et 390 px) | 1 923 contrôles, 0 échec |
| `tests/verify_s01_browser.cjs` | 72 réussis |
| `test_v7.py I83` | OK |
| `tools/livraison.py check-claude --root <main 1c39691 propre>` | empreintes et chemins conformes |

## Limites

Les limites des versions précédentes sont inchangées : donnée cadexomère (212 participants), recommandation ESVS sur l'occlusion de la veine fémorale commune, affirmations négatives de l'OFSP, couverture CIM-11.
