# Publication I83 v6 vérifiée

I83 — Varices des membres inférieurs (C-01-Cardiologie). Constat figé au 2026-10-08T15:12:02.792846+02:00 ; source Claude `8a6dc7f28bbdaa5251f9a4b75031875073bf7ccb`, intégrée par `eb276b90465edcd238fd122b4bd178015a5cb8c0`.

Le [run Pages 37781328939](https://github.com/vialdjoukang-spec/Medina/actions/runs/37781328939) est terminé avec succès pour `c545b79cb604347c7c1f38c5c8fe03126daafbc9`. Le déploiement `6936287487` est en état `success` depuis `2026-10-08T13:05:09Z`. Les trois téléchargements HTTPS ont répondu 200 après ce déploiement ; leur contenu correspond exactement aux mêmes fichiers de l’artefact GitHub Pages `11552161370`. Le digest ZIP annoncé et mesuré est `ee3961ddc561d4a3f65cd8126b997e8107528d3a562d371a43a27861d33f7091`.

| Fichier réellement servi | SHA256 observé |
| --- | --- |
| [Accueil](https://vialdjoukang-spec.github.io/Medina/index.html) | `2ba636c84028cc4abdb3e82c361113c36efaf087ee2bcec5f2caa6a8f0fb042b` |
| [Global](https://vialdjoukang-spec.github.io/Medina/MEDINA.html) | `d2c122e99448188f52d902093536bf8b598d26605ed60ecc59c457586b6bed41` |
| [S01](https://vialdjoukang-spec.github.io/Medina/fragments/MEDINA_S01_cardiovasculaire.html) | `50ab98bad3705354046b5aee76bd4f33898174166d0ac92359647ee29995bb7f` |

Les empreintes HTML global/S01 diffèrent de la reconstruction locale v6 attendue. La comparaison démontre un seul octet différent dans leur flux gzip : le champ OS à l’offset 9 (`03` local, `ff` publié). Tous les autres octets comprimés, les charges décodées et le HTML hors paquet sont identiques. Les empreintes locales ne sont donc pas revendiquées comme celles du site public. Preuve : [DECODED_COMPARISON.json](publication_pages/DECODED_COMPARISON.json).

Les neuf objets I83 ont été vérifiés à `66f1bd9`. Les changements ultérieurs jusqu’au SHA déployé concernent des documents, le plan d’organisation et des archives de livraison ; aucun chapitre, glossaire ou moteur canonique n’a changé. L’artefact actuel a été vérifié séparément, sans attribuer une injection aux archives.

Les 41 assertions de routes I83/I87 ont passé sur les octets S01 réellement téléchargés : PC 1360 et mobile 390, quatre onglets, aucun débordement horizontal ni erreur JavaScript. Ces octets sont identiques après le dernier déploiement ; le même contrôle n’est pas recompté. Le navigateur public HTTPS a rencontré `ERR_CERT_AUTHORITY_INVALID` dans cet environnement. Aucun contrôle TLS n’a été désactivé : urllib a téléchargé en HTTPS vérifié, puis ces fichiers exacts ont été servis en HTTP local, avec les assertions conservées. Les résultats natifs 1 923 / S01 72 de v5 restent une preuve historique distincte.

[PUBLICATION_PAGES.json](PUBLICATION_PAGES.json) contient les URLs, heures, empreintes et inventaire des preuves. [Artefact actuel](publication_pages/ARTIFACT_COMPARISON_C545.json), [HTTP actuel](publication_pages/LIVE_HTTP_FINAL.json), [routes](publication_pages/routes_live/routes-i83-i87.json). Le constat initial `28c0a58` et l’artefact intermédiaire `66f1bd9` sont conservés. Aucun Git ni fichier canonique modifié.
