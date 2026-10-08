# Lot J45-2 — J45 — Asthme (P-02-Pneumologie)

## Objet

Ce lot remplace `2026-10-08-J45` (tête `f30b891`, reçu par Codex en `88cba09`, non intégré). Il lève les réserves de la [réception Codex](../../../../../docs/collaboration/reviews/2026-10-08/PR12_F30B891_J45/RECEPTION.md) qui relèvent du producteur. Base : `main` `28c0a58486d58ee1e5d4ef4515aa1080b9046e61`, sans changement des sources J45. Le reste du cours est identique au [rapport du lot 1](../2026-10-08-J45/rapport.md). La correction, faite par un sous-agent, est détaillée dans `verification/corrections_codex_1.md` et `verification/corrections_codex_1b.md`.

## Réserve 1 — information professionnelle suisse : lue

L'information professionnelle suisse a été lue sur compendium.ch par rendu Chromium (`tools/compendium_fi.cjs`, 08.10.2026). Chaque donnée est citée dans le cours avec le produit et la date.

| Produit | Contenu suisse intégré |
| --- | --- |
| Symbicort 100/6 Turbuhaler | MART dès 6 ans ; maximum transitoire de 12 inhalations par jour chez l'adulte, 8 chez l'enfant ; au plus 6 inhalations à la fois, 4 chez l'enfant ; schéma à la demande seul (AIR) non décrit |
| Foster 100/6 | Asthme dès 18 ans ; MART limité à 8 inhalations par jour ; le 200/6 sert à l'entretien seulement |
| Budésonide-formotérol Spiromax 160/4,5 | MART dès 12 ans ; au plus 6 inhalations à la fois, 8 par jour en général, 12 au maximum |
| Vannair 100/6 | Entretien seulement, pas de MART |
| Atrovent, solution | Asthme : seulement en association pour la crise ; 100 à 250 µg de 6 à 12 ans |
| Singulair | Doses par âge, dont 4 mg en granulés de 6 mois à 2 ans |
| Trimbow 172/5/9 | Asthme de l'adulte non contrôlé par bêta-2 de longue durée et corticostéroïde inhalé ; 2 inhalations deux fois par jour, qui sont aussi la dose maximale |
| Spiriva Respimat | Indiqué seulement dans la BPCO ; non étudié avant 18 ans |
| Biothérapies : Xolair, Nucala, Fasenra, Cinqaero, Dupixent, Tezspire | Prescription réservée à des médecins expérimentés, sauf Xolair ; pour Xolair, si les IgE sont < 76 UI/mL, une sensibilisation à un allergène perannuel est exigée ; mention « LS (LIM) » sur compendium.ch |

**Règle du contentieux.** Le texte principal garde GINA 2026, le référentiel le plus récent, et mentionne la seule contrainte suisse divergente : Foster limité à 8 inhalations par jour. Le détail par produit se trouve dans la nouvelle fenêtre `j45-d-mart-ch`, « Limites suisses du MART », ouverte par des mots verts dans `J45_b.html` et `J45_d.html`.

## Réserve 2 — norme ERS 2017 non relue en texte intégral

Le texte intégral reste inaccessible : pas d'accès ouvert sur Europe PMC, aucun identifiant PMC, et le site de l'ERJ renvoie 403. Le cours a donc été **réduit à GINA 2026** :
- les catégories de PD20 et la liste des contre-indications de la méthacholine sont retirées ;
- il reste le test positif défini par une chute du VEMS ≥ 20 % aux doses standard (encadré 1-2) et la contre-indication pendant la grossesse (p. 37) ;
- pour le mannitol, il reste le seuil GINA de 15 % ; les deux critères non sourcés (baisse de 10 % entre deux doses, dose cumulée de 635 mg) sont retirés ;
- aucune information suisse de l'Aridol n'a été trouvée.

## Réserve 3 — relecture exhaustive

Cette réserve relève de l'audit de Codex. La revue du producteur est décrite dans le rapport du lot 1 : quatre rédacteurs, un assembleur et un vérificateur indépendant.

## Contrôles (base `main` `28c0a58`, sorties hors dépôt)

| Contrôle | Résultat |
| --- | --- |
| `verifier_sigles.py J45` | `{}` |
| `test_v7.py --static J45` | OK — 38 410 mots, 47 fenêtres, 8 quiz, 8 Pareto |
| `tools/insert_justifications.py --course J45` | 15/15 |
| `build_front.py`, `--all-fragments`, `tests/audit_fragments.py` | 22 fragments, JavaScript valide, build reproductible |
| Empreinte SHA-256 du build `MEDINA_S02_respiratoire.html` | `41621b89283d80162102abea377a52553f4baebd0ab10ef1c6b657779f79869d` |
| `tests/verify_course_native.cjs J45` (1 360 et 390 px) | 2 340 contrôles, 0 échec |
| `python3 -m unittest discover -s tests` | OK |
| `tools/livraison.py check-claude --root <main 28c0a58 propre>` | empreintes et chemins conformes |

## Réserves restantes

- Les limitations de remboursement de la liste des spécialités de l'OFSP ne sont pas relues ; le cours cite seulement la mention « LS (LIM) » de compendium.ch.
- Le reslizumab porte la mention « hc 03/26 » sur compendium.ch ; sa commercialisation n'est pas confirmée.
- L'entrée PD20 de `glossary/j45.py` n'est plus employée ; elle sera retirée par l'intégrateur si l'audit le souhaite. Le glossaire est hors du périmètre de l'outil de remise.
- La couverture CIM-11 n'est pas établie.
