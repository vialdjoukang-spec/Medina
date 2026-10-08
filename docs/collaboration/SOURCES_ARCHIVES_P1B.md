# MEDINA — sources et inventaires archivés du checkpoint P1B

L’archive [2026-10-08_C426D0_P1B](../../livraisons/Livraison%20Codex/archives/2026-10-08_C426D0_P1B/) conserve **l’intégralité des vingt-deux exports régénérés depuis les sources canoniques publiées à `c426d0b0bdd41f25638a788748e2b3680b8eade3`**. Il s’agit d’une photographie historique, indépendante des exports et travaux ultérieurs.

Chaque sous-dossier `<libellé>/` contient uniquement `README.md`, `livraison.json` et `sources/`. Les noms suivent le registre des fragments, par exemple **C-01-Cardiologie** et **P-02-Pneumologie**. Le SHA source est porté par les manifestes. Les glossaires et éléments de runtime partagés sont consultables au [commit immuable c426d0](https://github.com/vialdjoukang-spec/Medina/tree/c426d0b0bdd41f25638a788748e2b3680b8eade3) et référencés par les manifestes. Cette archive ne contient pas les nouveaux travaux de main ; elle ne certifie pas l’achèvement des fragments.

Les inventaires bruts sont conservés dans [CAMPAGNE_15_15_2026-10-08](archives/CAMPAGNE_15_15_2026-10-08/) :

| Fichier | Contenu historique |
| --- | --- |
| [DELIVERIES_LATEST.json.gz](archives/CAMPAGNE_15_15_2026-10-08/DELIVERIES_LATEST.json.gz) | Index complet produit pour cette campagne, avec routes, reçus et réserves. |
| [SNAPSHOT_DISTANT_2026-10-08_P1B.json.gz](archives/CAMPAGNE_15_15_2026-10-08/SNAPSHOT_DISTANT_2026-10-08_P1B.json.gz) | Données brutes figées de collecte : branches, PR, comparaisons, catalogue et reçus. |
| [ARCHIVES_SHA256.json](archives/CAMPAGNE_15_15_2026-10-08/ARCHIVES_SHA256.json) | Empreintes SHA-256 brutes et comprimées, tailles et datation. |

La compression gzip est **réversible sans perte** : après décompression, chaque JSON conserve exactement les octets de l’original, sans retrait de fichiers, de lignes ou de champs. Les empreintes du fichier comprimé et du fichier brut se contrôlent séparément avec `ARCHIVES_SHA256.json`.

Pour reproduire le scan historique, décompresser le snapshot avant de le fournir à l’option `--snapshot` de `tools/collaboration_sync.py`. Écrire les résultats dans un dossier historique distinct : les données archivées ne constituent pas un scan courant de main. Le [bilan de la campagne 15/15](CODEX_CAMPAGNE_15_15_2026-10-08.md) précise les contrôles datés et les réserves médicales/CIM-11 de cet instantané.
