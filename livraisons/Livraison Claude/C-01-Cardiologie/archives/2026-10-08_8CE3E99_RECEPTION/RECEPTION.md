# Réception immuable — Claude, PR 12, 8 octobre 2026

Ce dossier conserve exactement le manifeste et les 132 propositions de la tête `8ce3e99a18b96f6e6774d3d00bc709655e7ccb84`. Les octets du manifeste et de chaque proposition ont été comparés aux Git blobs de l’arbre distant non tronqué. Chaque SHA256 proposé, et chaque SHA256 de la source originale au point de départ `75505d8b440a294808147cd1a1c4fb71f4a4c207`, est vérifié dans `RECEPTION.json`.

| Périmètre | Fichiers |
|---|---:|
| Six nouveaux cours : I46 — Arrêt cardiaque ; I47 — Tachycardies paroxystiques supraventriculaires et ventriculaires ; I49 — Extrasystoles et autres arythmies ; I71 — Anévrismes et dissections artérielles ; I80 — Thrombose veineuse profonde et thromboses veineuses ; Q21 — Cardiopathies congénitales de l’adulte | 51 |
| Propositions antérieures exactement identiques à l’archive B6 | 79 |
| Nouvelles versions de I48 — Fibrillation et flutter auriculaires, fenêtres 3 et 4 | 2 |
| Total du paquet de quinze cours | 132 |

Cette réception n’injecte aucun cours. Les 51 nouveaux fichiers sont soumis à contrelecture médicale et aux contrôles d’intégration. Quatre en-têtes et `I80_c.html` divergent du canonique actuel : leur fusion doit conserver les corrections déjà effectuées. Les 81 propositions antérieures sont des originaux historiques ; elles ne doivent pas remplacer automatiquement les sources canoniques contre-corrigées.

Les deux nouvelles versions I48 doivent être comparées séparément aux fenêtres canoniques. Le manifeste annonce quinze cours ; sa mention « 14 cours » dans le statut est conservée à l’identique, sans être reprise comme un résultat de vérification. La complétude CIM-11 et la justification exhaustive de toutes les affirmations restent à établir.

`livraison.json` est le manifeste original, inchangé. `sources/` contient les propositions originales, inchangées. `RECEPTION.json` contient les preuves d’empreinte, le point de départ distant et l’état du canonique au moment de la réception. Le commit local indiqué dans le reçu sert à la traçabilité de la copie de travail ; il ne constitue pas un lien vers un commit GitHub.
