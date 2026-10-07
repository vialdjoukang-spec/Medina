# MEDINA — complétude des fragments livrés

Relevé du 7 octobre 2026. Base pédagogique : `bb134857e12245f46b4f329c1334ebd57251fcff`.

**Aucun des cinq fragments livrés n’est complet selon l’exigence CIM-11.** Les 30 cours ont été enrichis ; ils ne représentent pas cinq systèmes exhaustifs.

## Référentiel réellement présent

Le fichier primitif `Medina.html` de 78 392 308 octets a été relu après récupération. Son catalogue `medora-data` contient 1 636 entrées et déclare `meta.icd = CIM-10-GM 2024`. Ses entrées sont strictement identiques à celles du frontend actuel et de la passation Alpha. Son empreinte SHA-256 est `b299db900020967e35cdae6d1ee43c2212e36a1427fcb9a54dc64f09d4392207`. Le décompte ancien de 1 635 dans un compte rendu ne correspond pas au tableau actuellement vérifié.

Les entrées ne possèdent aucun champ structurel de correspondance CIM-11. Des mentions ponctuelles dans les cours ne prouvent pas l’exhaustivité du référentiel. La [CIM-11 MMS 2026-01, français](https://icd.who.int/browse/2026-01/mms/fr), consultée le 7 octobre 2026, est la nouvelle cible. Voir [la règle de complétude](../../docs/COMPLETUDE_CIM11.md).

## Couverture déclarée du catalogue local CIM-10

Le tableau compte les catégories à trois caractères déclarées dans `covers`, dans le périmètre exact de chaque fragment. Il ne mesure ni la qualité, ni la profondeur des cours, ni leurs sous-catégories, ni leur complétude CIM-11.

| Fragment | Cours intégrés | Catégories déclarées couvertes / catalogue local | Couverture déclarée | Manquantes | CIM-11 |
| --- | ---: | ---: | ---: | ---: | --- |
| S01 | 20 | 56 / 77 | 72,73 % | 21 | Non établie |
| S02 | 4 | 9 / 64 | 14,06 % | 55 | Non établie |
| S07 | 4 | 8 / 13 | 61,54 % | 5 | Non établie |
| S10 | 1 | 2 / 155 | 1,29 % | 153 | Non établie |
| T1 | 1 | 1 / 155 | 0,65 % | 154 | Non établie |

Les dénominateurs reproduisent `build_front.py`, fonctions `fragment_shell` et `fragment_chapters` : rattachement explicite par code, sinon rattachement par système, avec exclusion des codes attribués explicitement à un autre fragment. Les résultats ont été recoupés avec les données des cinq HTML construits. [Données, codes manquants et empreintes](catalogue-coverage.json).

## Pneumologie : état concret

Les quatre cours sont J45 (asthme), J44 (bronchopneumopathie chronique obstructive), J18 (pneumonies) et I26 (embolie pulmonaire). Ils déclarent couvrir `I26, J13, J14, J15, J18, J43, J44, J45, J46`. Les 55 autres catégories du fragment n’ont pas de couverture déclarée par un cours intégré. Les cours suivants restent notamment absents : grippe, bronchectasies, pneumopathies interstitielles, insuffisance respiratoire, hypertension pulmonaire, pneumothorax, maladies pleurales, pneumoconioses et tumeurs thoraciques.

Le dénominateur de 64 est un périmètre technique local. La tuberculose respiratoire (A15/A16), la sarcoïdose (D86), la mucoviscidose (E84) et les troubles du sommeil (G47) sont classés dans d’autres fragments et ne disposent pas de cours intégré. L’exhaustivité pneumologique exige aussi un accès aux entités pertinentes classées dans d’autres domaines.

## Anomalies et limites de rattachement

- Le cours M31 du fragment S07 déclare aussi couvrir M30. M30 reste dans le catalogue S10 : son alias n’ouvre pas un cours dans les fragments autonomes S07 ou S10. Cette déclaration hors fragment n’est pas comptée comme une catégorie accessible.
- S07 contient les dix catégories immunitaires du catalogue, plus M31, M32 et T78. S10 conserve 155 catégories après le transfert explicite de M31 et M32. Ces regroupements pédagogiques ne correspondent pas à des chapitres exhaustifs de la CIM-11.
- `DONE_SYS={1}` concerne l’ancien groupe « Cœur et hémodynamique » : 49 catégories déclarées par des cours et sept renvois textuels. Il ne certifie ni les 77 catégories du fragment cardiovasculaire S01, ni la CIM-11. Plusieurs renvois désignent des productions futures.
- Les groupes de l’accueil des fragments sont des rubriques pédagogiques. Leur libellé « catégories » a été corrigé en « rubriques » pour éviter leur confusion avec les catégories CIM.
- Les 17 cours historiquement marqués achevés ont reçu des enrichissements qui exigent une nouvelle relecture indépendante. Un statut historique ou un contrôle technique réussi ne valide pas ces ajouts.

## Catégories manquantes par fragment

Ces listes décrivent les absences de déclaration locale. Elles n’établissent pas un inventaire CIM-11 et n’excluent pas une mention partielle dans un cours.

### S01

Cours intégrés : I50, I21, I25, I48, I10, I30, I33, I35, I34, I00, I40, I42, I44, I47, I49, I46, Q21, I71, I80, I70.

Catégories sans couverture déclarée : `A43`, `I51`, `I52`, `I73`, `I77`, `I78`, `I79`, `I83`, `I85`, `I86`, `I87`, `I88`, `I89`, `I95`, `I97`, `I98`, `I99`, `R00`, `R01`, `R02`, `R03`.

### S02

Cours intégrés : J45, J44, J18, I26.

Catégories sans couverture déclarée : `C33`, `C34`, `C37`, `C38`, `C39`, `C45`, `I27`, `I28`, `J09`, `J10`, `J11`, `J12`, `J16`, `J17`, `J20`, `J21`, `J22`, `J40`, `J41`, `J42`, `J47`, `J60`, `J61`, `J62`, `J63`, `J64`, `J65`, `J66`, `J67`, `J68`, `J69`, `J70`, `J80`, `J81`, `J82`, `J84`, `J85`, `J86`, `J90`, `J91`, `J92`, `J93`, `J94`, `J95`, `J96`, `J98`, `J99`, `Q30`, `Q31`, `Q32`, `Q33`, `Q34`, `R04`, `R05`, `R06`.

### S07

Cours intégrés : D84, M32, T78, M31.

Catégories sans couverture déclarée : `D86`, `D89`, `D90`, `U60`, `U61`.

### S10

Cours intégrés : M06.

Catégories sans couverture déclarée : `C40`, `C41`, `D16`, `M00`, `M01`, `M02`, `M03`, `M07`, `M08`, `M09`, `M10`, `M11`, `M12`, `M13`, `M14`, `M15`, `M16`, `M17`, `M18`, `M19`, `M20`, `M21`, `M22`, `M23`, `M24`, `M25`, `M30`, `M33`, `M34`, `M35`, `M36`, `M40`, `M41`, `M42`, `M43`, `M45`, `M46`, `M47`, `M48`, `M49`, `M50`, `M51`, `M53`, `M54`, `M60`, `M61`, `M62`, `M63`, `M65`, `M66`, `M67`, `M68`, `M70`, `M71`, `M72`, `M73`, `M75`, `M76`, `M77`, `M79`, `M80`, `M81`, `M82`, `M83`, `M84`, `M85`, `M86`, `M87`, `M88`, `M89`, `M90`, `M91`, `M92`, `M93`, `M94`, `M95`, `M96`, `M99`, `Q65`, `Q66`, `Q67`, `Q68`, `Q69`, `Q70`, `Q71`, `Q72`, `Q73`, `Q74`, `Q75`, `Q76`, `Q77`, `Q78`, `Q79`, `S40`, `S41`, `S42`, `S43`, `S44`, `S45`, `S46`, `S47`, `S48`, `S49`, `S50`, `S51`, `S52`, `S53`, `S54`, `S55`, `S56`, `S57`, `S58`, `S59`, `S60`, `S61`, `S62`, `S63`, `S64`, `S65`, `S66`, `S67`, `S68`, `S69`, `S70`, `S71`, `S72`, `S73`, `S74`, `S75`, `S76`, `S77`, `S78`, `S79`, `S80`, `S81`, `S82`, `S83`, `S84`, `S85`, `S86`, `S87`, `S88`, `S89`, `S90`, `S91`, `S92`, `S93`, `S94`, `S95`, `S96`, `S97`, `S98`, `S99`.

### T1

Cours intégrés : A41.

Catégories sans couverture déclarée : `A15`, `A16`, `A18`, `A19`, `A20`, `A21`, `A22`, `A23`, `A24`, `A25`, `A26`, `A27`, `A28`, `A30`, `A31`, `A32`, `A33`, `A34`, `A35`, `A36`, `A37`, `A38`, `A40`, `A42`, `A44`, `A46`, `A48`, `A49`, `A50`, `A51`, `A52`, `A53`, `A54`, `A55`, `A56`, `A57`, `A58`, `A59`, `A60`, `A63`, `A64`, `A65`, `A66`, `A67`, `A68`, `A69`, `A70`, `A71`, `A74`, `A75`, `A77`, `A78`, `A79`, `A80`, `A82`, `A92`, `A93`, `A94`, `A95`, `A96`, `A97`, `A98`, `A99`, `B00`, `B01`, `B02`, `B03`, `B04`, `B05`, `B06`, `B07`, `B20`, `B21`, `B22`, `B23`, `B24`, `B25`, `B26`, `B27`, `B30`, `B33`, `B34`, `B35`, `B36`, `B37`, `B38`, `B39`, `B40`, `B41`, `B42`, `B43`, `B44`, `B45`, `B46`, `B47`, `B48`, `B49`, `B50`, `B51`, `B52`, `B53`, `B54`, `B55`, `B56`, `B57`, `B58`, `B60`, `B64`, `B65`, `B66`, `B67`, `B68`, `B69`, `B70`, `B71`, `B72`, `B73`, `B74`, `B75`, `B76`, `B77`, `B78`, `B79`, `B80`, `B81`, `B82`, `B83`, `B85`, `B86`, `B87`, `B89`, `B90`, `B91`, `B92`, `B94`, `B95`, `B96`, `B97`, `B98`, `B99`, `U04`, `U07`, `U08`, `U09`, `U10`, `U11`, `U12`, `U80`, `U81`, `U82`, `U83`, `U84`, `U85`, `U99`.

## Relecture et suite

Vérifications de ce complément : construction des 22 fragments réussie ; `tests/audit_fragments.py` réussi (JavaScript valide et build reproductible) ; `node --check shell/fragment.js`, liens relatifs des documents et cohérence arithmétique du relevé vérifiés. Les contrôles navigateur de la livraison antérieure ne sont pas présentés comme une nouvelle passe : la tentative actuelle n'a pas pu démarrer, faute de Chromium exécutable dans cet environnement.

La [mission globale de Claude](../../docs/collaboration/CLAUDE_AUDIT_GLOBAL_2026-10-07.md) comprend tous les onglets et fenêtres des 30 cours, la Sémiologie CS, les légendes et les textes des modèles. L’inventaire CIM-11 et la rédaction des catégories manquantes sont des travaux de complétude distincts de cette relecture. Claude peut remettre un rapport ou un patch ; aucun retour externe n’a encore été reçu.
