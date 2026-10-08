# Déploiement vérifié — I83 — Varices des membres inférieurs (C-01-Cardiologie)

Vérification du 8 octobre 2026, terminée à `2026-10-08T10:17:21.863279+00:00`. **GitHub Pages a publié avec succès le commit `72ccab4ea2197f8890d090270d212bb54184e0d0`. L’index, le document global et le fragment cardiologique répondent HTTP 200 et correspondent exactement à l’artefact construit pour ce SHA.** Les preuves détaillées sont conservées dans [DEPLOIEMENT.json](DEPLOIEMENT.json).

## Commit, sources et Actions

- [Commit publié](https://github.com/vialdjoukang-spec/Medina/commit/72ccab4ea2197f8890d090270d212bb54184e0d0) : `72ccab4ea2197f8890d090270d212bb54184e0d0`. La référence `main` lue à la fin du contrôle est `8d6deeeec54a5557fe93dcea6f6c6e6543e09d83`.
- [Injection canonique](https://github.com/vialdjoukang-spec/Medina/commit/bb3214d2f887068e669371b76509693ca63b5606) : `bb3214d2f887068e669371b76509693ca63b5606`, ancêtre du commit publié.
- [Source Claude auditée](https://github.com/vialdjoukang-spec/Medina/commit/6d5797c6a902e430cd9d3e9dd5159ec507a1476a) : `6d5797c6a902e430cd9d3e9dd5159ec507a1476a`. Les huit HTML et les deux modules de glossaire publiés sont identiques octet pour octet à cette remise. L’entrée canonique est I83, titre « Varices des membres inférieurs », `covers: [I83, I87]`.
- Empreinte publiée de `I83_pop4.html` : `dede4bdcf1974bbff6c2b2874410b64ac1e15003371fc9d78b3436c4999174f4`. Elle correspond à la dernière correction Rapidocain inspectée.
- [Workflow Pages 37760666231](https://github.com/vialdjoukang-spec/Medina/actions/runs/37760666231) : `completed / success`, au même SHA. Il a commencé à `2026-10-08T10:01:14Z` et sa mise à jour terminale date de `2026-10-08T10:03:19Z`.
- [Construction](https://github.com/vialdjoukang-spec/Medina/actions/runs/37760666231/job/113255996369) : tests Python, reconstruction du global et des fragments, assemblage, audit des fragments et dépôt de l’artefact terminés avec succès.
- [Déploiement](https://github.com/vialdjoukang-spec/Medina/actions/runs/37760666231/job/113256658173) : terminé avec succès ; [statut GitHub exact](https://api.github.com/repos/vialdjoukang-spec/Medina/deployments/6932642673/statuses/19452765184) enregistré à `2026-10-08T10:03:19Z` pour le déploiement `6932642673`, SHA `72ccab4ea2197f8890d090270d212bb54184e0d0`.

## Site et artefact réellement lus

| Document du site | Réponse | Identique au fichier de l’artefact Pages |
| --- | --- | --- |
| [Index](https://vialdjoukang-spec.github.io/Medina/) | HTTP 200 | Oui |
| [MEDINA global](https://vialdjoukang-spec.github.io/Medina/MEDINA.html) | HTTP 200 | Oui |
| [C-01-Cardiologie](https://vialdjoukang-spec.github.io/Medina/fragments/MEDINA_S01_cardiovasculaire.html) | HTTP 200 | Oui |

L’artefact GitHub Pages `11541837833` appartient au workflow du SHA publié. Le ZIP téléchargé fait `13665064` octets ; son SHA-256 `e349c1f5115de9725d2d41734d8fdf7c3cadf07153b9be810550e52112f54fc6` correspond au digest annoncé par GitHub. L’index, le global et S01 ont été comparés octet pour octet à leurs entrées régulières dans l’archive, sans extraction générale sur le système de fichiers. Empreinte du S01 réellement servi : `63b3ebf99ecad49dd3dd3dc92913fa10646597701f30656c910bdd4a0b97fbb0`. [Métadonnées exactes de l’artefact](https://api.github.com/repos/vialdjoukang-spec/Medina/actions/artifacts/11541837833) ; expiration annoncée : `2026-10-09T10:02:52Z`.

## Routes et limite du navigateur

- [I83 — Varices des membres inférieurs (C-01-Cardiologie)](https://vialdjoukang-spec.github.io/Medina/fragments/MEDINA_S01_cardiovasculaire.html#/entry/I83).
- [I87 — Autres atteintes veineuses (C-01-Cardiologie)](https://vialdjoukang-spec.github.io/Medina/fragments/MEDINA_S01_cardiovasculaire.html#/entry/I87), renvoyant au cours primaire I83.

Chromium `151.0.7922.173` refuse la navigation directe sur l’URL HTTPS avec `ERR_CERT_AUTHORITY_INVALID`. Aucun contrôle de certificat n’a été désactivé et aucun transport alternatif n’a été utilisé pour contourner ce refus. Les lectures HTTPS qui établissent la disponibilité et les empreintes du site ont été effectuées normalement par Python `urllib`.

La vérification interactive distincte a servi les octets S01 téléchargés du site sur HTTP local, avec le helper canonique et les destinations HTTP(S) externes bloquées. Elle a réussi **41 contrôles**, pour **quatre cas** : routes I83 et I87, largeurs 1360 et 390 px. Chaque route affiche un unique cours primaire I83 ; les quatre onglets sont accessibles ; aucun débordement horizontal ni erreur JavaScript détecté. Ce résultat porte sur le document déployé, dont l’identité avec l’artefact est prouvée ; il ne certifie pas l’accès HTTPS direct de Chromium ni les ressources tierces. Les interactions des routes du document global n’ont pas été testées par cette sentinelle.

Cette vérification établit la provenance, la publication et les routes du chapitre examiné. Elle ne constitue pas une nouvelle relecture médicale ni une déclaration de complétude du fragment. Aucune référence Git ni source canonique n’a été modifiée ; seuls ces deux fichiers de rapport ont été écrits dans le dépôt.
