# Infrastructure MEDINA — 15 octobre 2026

Référence contrôlée : `bc3a56fa8ef7abdc048e9bb0b4e94dd850b1c373`.
Ce relevé porte sur la construction et le chargement technique. Il ne constitue
pas une validation médicale. Les six préparations intégrées ensuite par le
coordinateur sont hors du périmètre de ces résultats navigateur.

## Corrections livrées

- `0fbd5d1d` : le chargeur reconnaît strictement le schéma AST historique de R27
  qui recherche `glossary` depuis une racine parente. La découverte récursive est
  remplacée en mémoire par les clés déjà chargées. Aucun glossaire médical n'est
  réécrit ; une boucle avec un effet supplémentaire est toujours refusée.
- `67f4ac7e` : l'inventaire compare les livraisons à `main`, au lieu de l'ancienne
  branche d'intégration du 7 octobre. La cible est explicite dans la CI.
- `1cb720c0` : Pages assemble l'index demandé sous `audit/` ; le veto déclaratif
  est vérifié avant construction et sur une lecture fraîche de `main` avant
  déploiement. L'artefact conserve son SHA de construction dans `publication.json`.
  Ce raccord dépend des outils livrés par les missions coordination/gouvernance.

## Contrôles réellement exécutés

| Contrôle | Résultat |
| --- | --- |
| Suite Python complète | 467 tests réussis en 128 secondes |
| Sous-ensemble chargeur | 23 tests réussis, dont refus des effets ajoutés |
| Sous-ensemble scanner | 22 tests réussis |
| Glossaire canonique avec copie réelle R27 | 4 539 clés ; source R27 inchangée |
| Construction atlas, fragments et portail | 23 fragments ; 201 cours intégrés dans le portail |
| Ressources locales des sources intégrées | 144 chemins distincts présents ; aucune absence |
| Bootstrap froid avec scripts et décompression retardés | 28 routes réussies dans les quatre systèmes |
| Parcours navigateur des quatre systèmes | 98 cours, 392 onglets et 64 occurrences d'images ; aucune erreur JS ni requête échouée |
| Affichage mobile | Une capture réelle par système à 390 × 844 ; aucun débordement horizontal |
| Configuration Pages | YAML analysé ; ordre checkout `main` → veto → déploiement vérifié |
| Audit fragments | JavaScript valide pour 23 fragments ; deux reconstructions de l'atlas identiques |
| Diff technique | `git diff --check` réussi ; aucune source médicale modifiée par cette mission |

Les 98 cours du contrôle navigateur se répartissent en 53 Neurologie,
25 Endocrinologie, 6 Néphrologie et 14 Hématologie. Les sorties détaillées sont
[cours-ressources.json](cours-ressources.json) et [bootstrap.json](bootstrap.json).
Les empreintes des 25 sorties HTML sont dans
[constructions-sha256.json](constructions-sha256.json).
Les sous-ensembles Python font partie des 467 tests, ils ne s'y ajoutent pas.
L'empreinte du glossaire R27 réel contrôlé est
`9bab084fa47420381de33cabe4682a7917798c1f6e197fb4daa1ceb15cec43ef`.

L'exécution complète de `tests/audit_fragments.py` a réussi : 23 fragments,
JavaScript valide et construction reproductible. Les contrôles navigateur
existants ont été lancés avec `MEDINA_QA_FRAGMENTS=S04,S05,S06,S08` pour le
bootstrap ; un parcours technique temporaire a ouvert les quatre onglets de
chaque cours intégré pour vérifier les ressources.

## Branches et échecs CI constatés

L'instantané des références distantes contient 79 branches hors références de PR :
54 ancêtres de `main`, 2 références alignées (`main` et la branche Claude active),
23 divergentes. Les 23 simulations `git merge-tree` ont terminé normalement ;
14 produisent des conflits. Aucune fusion ni suppression de branche n'a été faite
par cette mission. L'instantané détaillé a été transmis au coordinateur.

Cinq branches divergentes ne possèdent plus aucun patch distinct de `main`
selon `git cherry` : `codex/cycle1-publication-fix-20261012`,
`codex/jauges-controle-20261012`, `codex/jauges-espacement-20261012`,
`codex/jauges-fiables-20261012`, `codex/liens-cartes-20261012`.
Les branches historiques conservant des changements médicaux doivent garder
leurs sources : une fusion globale réintroduirait des versions antérieures.

- [Garde Claude 38751255186](https://github.com/vialdjoukang-spec/Medina/actions/runs/38751255186) :
  échec réel sur l'agrégat `a5b81ffa` → `bc3a56fa` (« ordre de publication ou
  quatre cours prêts non respecté »). La même tête a passé la garde sur `main`.
  La mission gouvernance traite le rejeu des transitions unitaires ; cette mission
  n'a pas modifié les gardes.
- [Inventaire PR98 38735048315](https://github.com/vialdjoukang-spec/Medina/actions/runs/38735048315) :
  échec réel `GitHub HTTP 403 sur /branches`, après 22 tests scanner réussis.
  Cette erreur d'accès ne démontre pas un échec de construction. Aucun succès
  n'a été substitué à cette erreur et aucune permission GitHub n'a été modifiée.
- À la tête de référence `bc3a56fa`, l'[inventaire 38751247851](https://github.com/vialdjoukang-spec/Medina/actions/runs/38751247851)
  et la [garde main 38751247975](https://github.com/vialdjoukang-spec/Medina/actions/runs/38751247975)
  ont réussi. Le HTTP 403 historique ne se reproduit donc pas sur ce dernier
  inventaire observé.
- À 14 h 45 UTC, [Pages 38750900215](https://github.com/vialdjoukang-spec/Medina/actions/runs/38750900215)
  sur `3e5f6f3a` était encore en cours dans l'audit final ;
  [Pages 38751247881](https://github.com/vialdjoukang-spec/Medina/actions/runs/38751247881)
  sur `bc3a56fa` était en attente. Aucun déploiement de ces têtes n'est certifié ici.

## Limites

Les contrôles Pages ajoutés ont été vérifiés localement au niveau de leur
configuration ; leur exécution distante appartient à la publication finale du
coordinateur. Le veto est un journal déclaratif consulté à un instant donné :
il ne fournit ni authentification matérielle des signataires ni atomicité avec
l'action de déploiement GitHub. Les contrôles techniques n'établissent pas
l'exactitude médicale, la complétude des cours ou l'achèvement d'un audit différé.
