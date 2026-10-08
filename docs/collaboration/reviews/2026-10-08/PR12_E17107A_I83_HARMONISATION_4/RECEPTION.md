# Réception PR #12 — I83-HARMONISATION-4

Date : 8 octobre 2026  
Dépôt : `vialdjoukang-spec/Medina`  
PR : [#12](https://github.com/vialdjoukang-spec/Medina/pull/12)  
Branche Claude : `claude/loving-shannon-spwrhc`  
Tête reçue : `e17107aaafff29ac94abf9197a1eef6fb0d6c817`  
Baseline annoncée et vérifiée : `0dc7aa93f8a8cea42b6aa556c38505a66b8919d5`

## Décision

| Niveau | État |
|---|---|
| Repéré | Oui — quatrième remise complète distincte |
| Reçu | Oui — 14 originaux archivés sans modification |
| Intégré | Non |
| Contrôlé techniquement | Empreintes et structure vérifiées ; contrôles producteurs non reproduits |
| Publié | Archive, reçu et rapport seulement |

Le paquet remplace `I83-HARMONISATION-3`. Les sept couples baseline/proposition et le complément de glossaire donnent **15 empreintes attendues sur 15 exactes**. La comparaison de contenu montre que seul `I83_b.html` change réellement ; les six autres propositions et le glossaire sont identiques à la v3. La v3 n'est pas réappliquée.

Empreinte agrégée de l'archive : `3b7ed1c72814841e399921fcecf52efb59934d37`.

## Contenu archivé

Les 14 objets d'origine sont conservés sous :

`livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_PR12_E17107A_I83_HARMONISATION_4/originals/`

Le signal Claude, le manifeste, le rapport, le diff, deux rapports de contrôle, sept propositions de chapitre et le complément de glossaire sont conservés avec leurs blobs Git d'origine.

## Relecture médicale ciblée

La réserve de la v3 est bien corrigée dans les deux passages visés :

- `I83_b` §13.1 prévoit désormais les exceptions pour ARTE/TVP détectée, symptôme nouveau et traitement séquentiel ;
- l'encadré « À retenir » reprend ces exceptions ;
- aucune autre formule restrictive équivalente n'est retrouvée dans les sept sources ou le glossaire.

Sources primaires relues :

- [SVS/AVF/AVLS 2023, partie II — §11](https://pmc.ncbi.nlm.nih.gov/articles/PMC11523430/)
- [ESVS 2022 — maladie veineuse chronique, §4.1.7](https://esvs.org/wp-content/uploads/2023/03/ESVS-2022-CVD-Guidelines.pdf)

### Réserve médicale bloquante nouvelle

La phrase détaillée de `I83_b` prévoit qu'une « thrombose profonde découverte » serait surveillée jusqu'à sa « résolution ». Cette formulation généralise à toute TVP un suivi échographique sérié jusqu'à disparition.

Les recommandations SVS/AVF/AVLS 2023 ne posent pas cette règle universelle :

- 11.3.1 réserve l'imagerie sériée pendant deux semaines à certaines TVP distales aiguës sans symptômes graves ni facteur d'extension ;
- 11.3.2–11.3.3 déterminent surtout l'anticoagulation selon le siège et le risque, sans exiger une résolution échographique pour toute TVP ;
- 11.4.2 poursuit l'anticoagulation d'une ARTE jusqu'à rétraction du thrombus.

La correction doit dissocier :

- **ARTE** : contrôle jusqu'à rétraction lorsque le traitement est indiqué ;
- **TVP** : surveillance selon le siège, les symptômes, le risque d'extension et le protocole du cours I80, sans imposer une résolution échographique universelle.

L'encadré court « TVP en cours de surveillance » demeure acceptable. Cette relecture porte sur le delta v4 ; elle ne certifie ni l'ensemble d'I83 ni les 30 cours.

## Contrôle technique

Le producteur annonce :

- contrôle natif : 1 923 vérifications, 0 échec/erreur, vues 1360×900 et 390×844, 47 gabarits ;
- contrôle S01 : 72 vérifications, 0 erreur, Chromium 141 ;
- build reproductible et `tools/livraison.py check-claude` réussi.

Ces résultats ont été archivés, mais non reproduits dans l'environnement de réception. Le dépôt et le runtime nécessaires à `tools/livraison.py`, aux reconstructions et aux contrôles navigateur ne sont pas présents. Le glossaire reste hors manifeste et exige une adaptation séparée. La branche entière est fortement divergente : elle ne doit pas être fusionnée à l'aveugle.

## Suite attendue

1. Corriger la généralisation du suivi échographique de toute TVP dans `I83_b.html`.
2. Réémettre le paquet complet avec ses empreintes exactes.
3. Reproduire indépendamment `check-claude`, l'injection, la reconstruction, les tests et les contrôles navigateur ARTE/EHIT sur ordinateur et mobile.

Aucune source canonique, route, attribution ni chapitre actif n'a été modifié.
