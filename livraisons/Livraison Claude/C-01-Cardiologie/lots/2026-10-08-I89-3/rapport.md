# Lot I89-3 — I89 — Autres atteintes non infectieuses des vaisseaux et des ganglions lymphatiques (C-01-Cardiologie)

## Objet

Ce lot remplace `2026-10-08-I89-2` (tête `de67651`, reçu par Codex en `f204b06`, non intégré). Il lève les deux réserves de la [réception I89-2](../../../../../docs/collaboration/reviews/2026-10-08/PR12_DE67651_I89_2/RECEPTION.md). Base : `main` `f204b06ac174d41632b742ec6b82097b1532b2c8`, sans changement des chemins I89. Les corrections antérieures sont dans les [rapports v1](../2026-10-08-I89/rapport.md) et [v2](../2026-10-08-I89-2/rapport.md).

La correction est minimale et faite par un sous-agent. Chaque mécanisme s'appuie désormais sur l'**information officielle du produit**, source primaire réglementaire, lue en entier le 08.10.2026 dans la base de données des notices de la Bibliothèque nationale de médecine des États-Unis. Le détail, avec les identifiants et les versions, figure dans `CORRECTIONS_AUDIT_CODEX_2.md`.

## Réserves levées

| Réserve Codex | Correction | Source primaire |
| --- | --- | --- |
| 1. Mécanisme rénal du minoxidil extrapolé d'une source sur l'hydralazine | Le mécanisme commun « baisse de la perfusion rénale » est **retiré**. Pour le minoxidil, la baisse de pression active les mécanismes rénaux, dont la rénine ; la rétention atteint plusieurs centaines de milliéquivalents de sel sans diurétique, et un diurétique de l'anse est presque toujours nécessaire. Pour l'hydralazine, la voie passe par la rénine, l'angiotensine II et l'aldostérone. **Son étiquetage indique un débit sanguin rénal maintenu ou augmenté, ce qui contredisait l'ancienne phrase.** | Étiquetages du minoxidil (25.08.2026) et de l'hydralazine (14.09.2026) |
| 2a. Anti-inflammatoires non stéroïdiens | Le texte se limite à rétention hydrique et œdème, et à la baisse de l'effet natriurétique du furosémide et des thiazides. | Étiquetage de l'ibuprofène sur ordonnance (29.07.2026) |
| 2b. Corticoïdes | Rétention sodée avec œdème et perte de potassium. L'hydrocortisone et la cortisone retiennent davantage le sel ; les dérivés de synthèse moins, sauf à forte dose. Le terme « minéralocorticoïde » est retiré. | Étiquetage de la prednisone (15.09.2026) |
| 2c. Pénicilline et peptidoglycane | Inhibition de la biosynthèse du mucopeptide de la paroi (peptidoglycane), effet bactéricide en phase de multiplication active, streptocoques A, C et G « très sensibles ». La revue de Kong est retirée. | Étiquetage de la pénicilline V potassique (29.09.2026) |
| 2d. Myxœdème et glycosaminoglycanes | Une source primaire remplace la revue de Safer : dans la peau de dix patients atteints de myxœdème non traité, l'acide hyaluronique est augmenté et baisse sous thyroxine. Le texte dit que les auteurs « proposent » ce rôle dans l'œdème qui ne garde pas le godet. | Lund et al., Acta Endocrinologica 1986 (PMID 3094309), résumé |

## Contrôles (base `main` `f204b06`, sorties hors dépôt)

| Contrôle | Résultat |
| --- | --- |
| `verifier_sigles.py I89` | `{}` |
| `test_v7.py --static I89` | OK — 36 953 mots, 43 fenêtres, 8 quiz, 5 Pareto |
| `build_front.py`, `--all-fragments`, `tests/audit_fragments.py` | 22 fragments, JavaScript valide, build reproductible |
| Empreinte SHA-256 du build `MEDINA_S01_cardiovasculaire.html` utilisé pour les contrôles | `612c493a8a93e41f50320be523cb34e86ed085182a4cc554324f233bfc49eace` |
| `tests/verify_course_native.cjs I89` (1 360 et 390 px) | 2 595 contrôles, 0 échec |
| `tests/verify_s01_browser.cjs` (22 cours) | 73 réussis |
| `test_v7.py I89` | OK |
| `python3 -m unittest discover -s tests` | 118 tests OK |

## Réserves restantes

- **Étiquetages** : ils sont américains ; l'information professionnelle suisse est inaccessible depuis cet environnement.
- **Anti-inflammatoires non stéroïdiens** : le rôle des prostaglandines n'est appuyé que par l'interaction avec les diurétiques décrite dans l'étiquetage.
- **Myxœdème** : Lund 1986 est une petite étude, lue en résumé ; le mécanisme reste une hypothèse.
- **Hors de ce lot** : les glitazones (canal sodique épithélial) et le docétaxel n'ont pas été relus.
- **Toujours valables** : les limites des versions 1 et 2, à savoir Verdye en Suisse, I88 non couverte et CIM-11 non établie.
