# Vérification du site public — I48 — Fibrillation et flutter auriculaires

**Résultat : conforme.** 54 contrôles navigateur réussis, aucune erreur JavaScript ou console, quatre captures. Vérification achevée le `2026-10-07T21:26:54.961Z` avec Chromium 153.0.8010.0.

Commit publié communiqué pour ce déploiement : `e856ed16893ba5c4ffc3bd4c9ca78a38ce533de6`.

[Ouvrir I48 sur le site public](https://vialdjoukang-spec.github.io/Medina/fragments/MEDINA_S01_cardiovasculaire.html#/entry/I48).

Les quatre onglets s’ouvrent sur PC et à 390 px. Le clic naturel sur le mot vert CHA₂DS₂-VA, puis sur son abréviation imbriquée, ouvre la fenêtre mécanistique complète du score. Le titre et le texte intégral correspondent au template servi. La fermeture rend le focus au mot vert. La fenêtre reste contenue dans le viewport.

## Comparaison de la construction locale et publique

Les empreintes brutes des HTML sont différentes. Le paquet gzip embarqué présente une variation de l’octet d’identification du système de compression : offset 9, valeur 3 dans la construction locale, 255 dans la construction publique. Tous les autres octets de ce paquet sont identiques. Le contenu décompressé et toute la surface HTML hors paquet sont strictement identiques.

| Preuve | Construction locale | Site public |
| --- | --- | --- |
| SHA-256 brut du HTML | `08279a521cb0fa93de132809a526c02c80852e5d7bcc436d1c3b9e011970341a` | `776cb1d1a53bdd31bf53246ed014bfd21970d1c245b3a7b643bdf8930e62332e` |
| SHA-256 du payload décompressé | `9fbd46ba0fad924c6f0e81aeeaa02f92297b69c6f8963446b2ce89a1d5a6171d` | `9fbd46ba0fad924c6f0e81aeeaa02f92297b69c6f8963446b2ce89a1d5a6171d` |
| SHA-256 de la surface hors paquet | `d3301d067a494dbac34baa6ec76fc162d9b7137aaa7b8cc39ec717af8ee0281c` | `d3301d067a494dbac34baa6ec76fc162d9b7137aaa7b8cc39ec717af8ee0281c` |
| Octet OS du gzip | 3 | 255 |

Le rapport [browser_publication_results.json](browser_publication_results.json) conserve les comparaisons intégrales et leurs résultats. [http_poll.json](http_poll.json) conserve le premier téléchargement HTTPS validé par urllib et le constat initial d’empreintes brutes distinctes. [html_difference.json](html_difference.json) localise la variation de base64.

## Environnement de contrôle

Le premier lancement Playwright a rencontré `ERR_CERT_AUTHORITY_INVALID` avec le proxy géré de l’environnement. Le diagnostic figure dans [browser_certificate_probe.json](browser_certificate_probe.json). Le passage final utilise une exception de confiance TLS limitée au contexte navigateur de ce contrôle, consignée dans son rapport. Le téléchargement urllib, qui n’utilise aucune exception TLS, a obtenu HTTP 200 et la même empreinte publique.

Ce contrôle confirme la présence et le fonctionnement de la version intégrée sur le site public. Il complète les contrôles locaux sans étendre la portée de la relecture médicale ciblée.

## Captures

- [Cours sur PC](public_i48_1360.png).
- [Fenêtre du score sur PC](public_i48_score_1360.png).
- [Cours à 390 px](public_i48_390.png).
- [Fenêtre du score à 390 px](public_i48_score_390.png).
