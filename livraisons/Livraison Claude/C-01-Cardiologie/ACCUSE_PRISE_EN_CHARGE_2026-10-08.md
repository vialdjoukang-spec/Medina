# Accusé de prise en charge de Claude — cahier des charges du 8 octobre 2026

## Documents lus

- [CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES.md](../../../docs/collaboration/CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES.md), blob `1db235437134965b62afeccc8a5316749453261a`, lu au commit d'intégration `b6e5d18c2c2383893819c4c0834d6402bbe30e67`.
- `AGENTS.md`, `CLAUDE.md`, `FRAGMENTS_RESTANTS.md`, `organisation/production_plan.json`, `HANDOFF_LATEST.md`, `DELIVERY_PROTOCOL.md`, `FRAGMENT_01_PRIORITE.md`, `MECHANISMS_CLAUDE.md`, `MECHANISMS_PLAN.json` et le reçu `CLAUDE_LOT5_FINAL_20261007.json`, à la même tête.

## Têtes Git consultées le 8 octobre 2026

| Référence | SHA complet |
| --- | --- |
| `main` | `20915d9a36f0ebc65a79ec6428357727dd5afe6c` |
| `codex/sciences-cs-fragments-20261007` (intégration) | `b6e5d18c2c2383893819c4c0834d6402bbe30e67` |
| `claude/loving-shannon-spwrhc` après fusion de l'intégration | `c7cfe4f26907c2614f2ecac2960f063344023158` |

Inventaire : `python3 tools/collaboration_sync.py --out <hors dépôt>`. Seize têtes ont été repérées. Le scanner déclare la collecte **partielle** : les métadonnées de PR passent par l'API GitHub, dont l'accès n'est pas garanti dans cette session. Aucune remise de chapitre Codex n'a été repérée sur les 21 fragments restants. L'audit croisé de **A41 — Sepsis et choc septique de l'adulte (I-03-Infectiologie)** commencera dès sa publication.

## Livraisons antérieures examinées

- Lot 4 : **I48 — Fibrillation et flutter auriculaires (C-01-Cardiologie)**. Reçu, injecté et publié par Codex.
- Lot 5 : quatorze cours. La comparaison montre 115 copies identiques au canonique et 17 adaptées par Codex. Ces adaptations retirent les badges de validation interne ainsi que les classes ESC 2026 déduites d'une formulation narrative, et ajoutent une fenêtre comparative dans **I42 — Cardiomyopathies (C-01-Cardiologie)**. Ces adaptations sont acceptées et servent désormais de base.

## État prouvé de la priorité cardiologie (C-01-Cardiologie)

**Elle n'est pas close.** Les dix cours attribués à Claude sont injectés et techniquement contrôlés. `MECHANISMS_PLAN.json` les maintient tous en `pending_exhaustive_review` jusqu'à l'audit croisé de Codex. Travaux de Claude encore ouverts :

1. **I83 — Varices des membres inférieurs (C-01-Cardiologie)** : production en cours (architecte, puis quatre rédacteurs d'onglet).
2. **I89 — Autres atteintes non infectieuses des vaisseaux et des ganglions lymphatiques (C-01-Cardiologie)** : production en cours (même organisation).
3. Comparaisons **ESC 2026** dans I30, I33, I34, I35, I40, I42, I44 et Q21 : propositions écrites, vérification indépendante en cours. Pour I00, l'examen n'a trouvé aucune recommandation 2026 pertinente (bilan seul).
4. Corrections consécutives à l'audit Codex des dix cours, dès réception de ses observations.

## Chapitre réservé

Aucun dans `production_plan.json`. La file de Claude ne commence qu'après la clôture de la priorité cardiologie. Son premier chapitre sera **J45 — Asthme (P-02-Pneumologie)**, que Claude n'a pas commencé et ne réserve pas ici. I83 et I89 relèvent du fragment C-01-Cardiologie, hors des 21 files ; ils ne figurent donc pas dans `active_chapter`.

Écart déclaré : I83 et I89 sont produits en parallèle, car tous deux sont attribués à Claude par `FRAGMENT_01_PRIORITE.md` et étaient déjà commencés avant le cahier du 8 octobre. Chacun sera remis dans **son propre lot**, avec rapport, manifeste et audit distincts. Claude ne peut pousser que sur `claude/loving-shannon-spwrhc` ; les lots partageront donc la PR existante, et Codex pourra les recevoir chapitre par chapitre.

## Sous-agents et chemins possédés

| Rôle | Nombre | Chemins en écriture |
| --- | --- | --- |
| Rédacteurs I83 (Pathologie, Examens, Sciences, Pharmacologie) | 4 | `travail/production/I83/brouillon/` (un fichier, un auteur) |
| Rédacteurs I89 | 4 | `travail/production/I89/brouillon/` |
| Vérificateur ESC 2026 | 1 | `travail/esc2026/<CODE>/` |
| Vérificateurs indépendants I83 et I89 (à lancer) | 2 | corrections en place dans le brouillon, `verification.json` |
| Assemblage, Git, manifeste, contrôles | Claude responsable | `chapters/I83`, `chapters/I89`, `glossary/i83.py`, `glossary/i89.py`, `chapters.json`, `livraisons/Livraison Claude/C-01-Cardiologie/` |

Seul le responsable effectue les opérations Git ; une sauvegarde automatique du dossier `travail/` protège les brouillons.

## Contrôles prévus par chapitre

`python3 tools/production_plan.py` ; `verifier_sigles.py` (résultat `{}`) ; `python3 test_v7.py --static <CODE>` ; `MEDINA_OUT="$PWD/dist" python3 build_front.py` puis `--fragment S01` ; `python3 test_v7.py <CODE>` ; contrôle navigateur sur ordinateur et mobile ; `python3 tools/livraison.py check-claude` sur le dossier du lot.

## Blocages

- Aucun accès de publication autre que la branche Claude.
- Métadonnées de PR peut-être partielles (voir l'inventaire).
- Couverture CIM-11 non établie.
