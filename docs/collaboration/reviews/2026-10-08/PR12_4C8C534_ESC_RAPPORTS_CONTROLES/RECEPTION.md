# Réception Claude — rapports et contrôles ESC 2026

PR #12, tête `4c8c534a6239c0b08ae3b1c2969d6f875549869d`; main de référence `960586ec0f6ddf76911a966f1bbd4a2bdcbc29b1`.

Claude joint aux huit lots **I30, I33, I34, I35, I40, I42, I44 et Q21** un rapport, un manifeste enrichi et un journal de contrôle natif. Les 24 objets sont archivés sans modification sous l’empreinte d’arbre `449bd70da67b3afe7fbcde95baf2e278275d73ee`.

## Contrôles producteurs reçus

| Cours | Contrôles | Échecs | Erreurs |
|---|---:|---:|---:|
| I30 | 2 787 | 0 | 0 |
| I33 | 2 997 | 0 | 0 |
| I34 | 4 075 | 0 | 0 |
| I35 | 3 269 | 0 | 0 |
| I40 | 3 127 | 0 | 0 |
| I42 | 3 039 | 0 | 0 |
| I44 | 3 427 | 0 | 0 |
| Q21 | 3 947 | 0 | 0 |
| **Total** | **26 668** | **0** | **0** |

Les contrôles déclarent tous la base exacte `960586ec0f6ddf76911a966f1bbd4a2bdcbc29b1`. Ils n’ont pas été reproduits indépendamment. Les 26 propositions restent identiques aux contenus ESC déjà inventoriés : 18 remplacements correspondent à leur baseline vérifiée et 8 ajouts étaient absents comme attendu.

## Décision

État : **repéré, reçu et archivé ; non intégré, non contrôlé indépendamment et non publié comme contenu de cours**.

L’injection est différée parce que :

- le signal de chaîne maintient **I83** comme chapitre actif et place ces huit lots après sa clôture ;
- chaque rapport conserve l’état `pending_exhaustive_review` et demande une contre-relecture ;
- la synthèse `LEVEE_RESERVES.json` affichée dans les rapports rend les champs MED-01 à MED-03 à `null`, ce qui rompt la preuve agrégée de levée ;
- I35 conserve hors proposition une indication de furosémide IV 20–40 mg chez le patient naïf, alors que le rapport ESC 2026 retient 40 mg et le double de la dose orale antérieure chez le patient déjà traité ;
- I40 conserve hors proposition « FEVG modérément réduite » pour 41–49 %, tandis que le rapport cite « mildly reduced » ;
- l’inventaire CIM-11 demeure non établi.

Aucune attribution, aucun chapitre actif et aucun fichier canonique n’a été modifié. Cette réception ne constitue ni une validation médicale exhaustive ni une validation technique indépendante.

[Reçu JSON](../../../receipts/CLAUDE_ESC_4C8C534_RECEPTION_2026-10-08.json)
