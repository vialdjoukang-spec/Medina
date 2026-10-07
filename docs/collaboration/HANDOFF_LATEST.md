# MEDINA — dernière passation disponible

Date : 7 octobre 2026. Cette page constitue le lien stable à remettre à Claude après chaque livraison publiée.

## Livraison à relire

- Branche : [`codex/sciences-cs-fragments-20261007`](https://github.com/vialdjoukang-spec/Medina/tree/codex/sciences-cs-fragments-20261007).
- Base de contenu : [`bb134857e12245f46b4f329c1334ebd57251fcff`](https://github.com/vialdjoukang-spec/Medina/tree/bb134857e12245f46b4f329c1334ebd57251fcff).
- Instructions prioritaires : lire `CLAUDE.md` et ce dossier à la tête actuelle de la branche. La base de contenu précède les nouvelles instructions d'audit global et de complétude CIM-11.
- Branche de contribution : `claude/review-medina-global-20261007`, préparée avec les mêmes consignes de collaboration.
- Retour de Claude : lecture des consignes confirmée le 7 octobre 2026 ; **audit global non commencé**. Relectures I48 ESC 2024 et Sémiologie CS : **rapport reçu, intégré** au commit [`f9efb78`](https://github.com/vialdjoukang-spec/Medina/commit/f9efb78eabdb8142aada6a494143c536bcf765e8) de `claude/review-medina-global-20261007`, proposé par pull request vers `codex/sciences-cs-fragments-20261007`.

Le lot comprend 30 cours dans cinq fragments et la Sémiologie CS cardiovasculaire. Les sciences enrichies comprennent 140 disciplines ; CS comprend dix étapes et quatre modèles 3D en fenêtres. Claude relit tous les textes livrés, y compris les contenus antérieurs aux enrichissements.

| Fragment | Cours concernés |
| --- | --- |
| S01 — Cardiovasculaire | I00, I10, I21, I25, I30, I33, I34, I35, I40, I42, I44, I46, I47, I48, I49, I50, I70, I71, I80, Q21 |
| S02 — Respiratoire | J45, J44, J18, I26 |
| S07 — Immunitaire | D84, M32, M31, T78 |
| S10 — Locomoteur | M06 |
| T1 — Agents et thérapeutique | A41 |

## Documents utiles

| Document | Usage |
| --- | --- |
| [Mission globale](CLAUDE_AUDIT_GLOBAL_2026-10-07.md) | Périmètre intégral, exigences médicales, didactiques et linguistiques. |
| [Manifeste](CLAUDE_REVIEW_SCOPE_2026-10-07.json) | 289 fichiers de contenu, chemins, repères et empreintes de la base. |
| [Relevé de complétude](../../audits/COMPLETUDE_2026-10-07/README.md) | Lacunes du catalogue historique CIM-10 ; absence de certification CIM-11. |
| [Règle CIM-11](../COMPLETUDE_CIM11.md) | Inventaire officiel et preuves nécessaires pour chaque catégorie et sous-catégorie. |
| [Sources communes](SOURCES_CANONIQUES.md) | Sources primaires et trace attendue pour toute correction médicale. |
| [Livraison et contrôles](../../audits/SCIENCES_CS_2026-10-07/README.md) | Rapports techniques, mesures, captures et limites. |
| [Zone de remise](reviews/README.md) | Rapport, journal, branche, PR ou patch. |

La relecture couvre les quatre onglets, toutes les fenêtres, les figures et leurs légendes, les tableaux, quiz et corrections, les glossaires et les textes visibles des modèles CS. La langue doit rester professionnelle, précise et fluide. Supprimer répétitions, métadiscours et remplissage ; conserver les distinctions et les notions utiles.

## Contrôles et limites

Les rapports de livraison consignent 71 contrôles de navigation et 569 contrôles sciences/CS réussis. Ils attestent des contrôles techniques exécutés sur le lot ; ils ne certifient pas une relecture médicale indépendante.

Les cinq fragments sont incomplets. Leur catalogue local provient de la CIM-10-GM 2024. La couverture exhaustive CIM-11 est **non établie** tant que l'inventaire officiel et la matrice de couverture ne sont pas constitués et vérifiés.

## File de relecture

| Lot | Base de contenu | Travail attendu | État |
| --- | --- | --- | --- |
| 30 cours et CS — 2026-10-07 | `bb134857e12245f46b4f329c1334ebd57251fcff` | Audit intégral médical, rédactionnel et didactique selon la mission globale. | Disponible ; premier lot planifié (formules clonées, métadiscours, I40, A41, I48 entier). |
| I48 — sous-tâche ESC 2024 | `c3770739b58c96120c180a4ae0c68d00dde70a51` | Confirmation ECG ; à inclure dans l'audit global sans limiter celui-ci. | **Rapport reçu, intégré** : `f9efb78eabdb8142aada6a494143c536bcf765e8`. [Rapport](reviews/CLAUDE_I48_ESC2024_RAPPORT.md). Réserves R08 et R11 ouvertes. |
| Sémiologie CS — repères et manœuvres | `bb134857e12245f46b4f329c1334ebd57251fcff` | Relecture de `modules/cardiovascular_cs.html` et `.js`. | **Rapport reçu, intégré** : `f9efb78eabdb8142aada6a494143c536bcf765e8`. [Rapport](reviews/CLAUDE_CS_CARDIO_RAPPORT_2026-10-07.md). Lacune C10 ouverte. `verify_sciences_cs.cjs` : 569 contrôles réussis. |

Après chaque nouveau lot, publier les sources et les contrôles, puis ajouter ici sa base exacte, son périmètre et ses limites. La disponibilité est annoncée après le push. Les anciennes bases demeurent identifiables pour intégrer les corrections sans perdre les travaux concurrents.
