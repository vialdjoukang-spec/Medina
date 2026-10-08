# Réception PR #12 — I83-HARMONISATION-5

Date : 8 octobre 2026  
Dépôt : `vialdjoukang-spec/Medina`  
PR : [#12](https://github.com/vialdjoukang-spec/Medina/pull/12)  
Branche Claude : `claude/loving-shannon-spwrhc`  
Tête reçue : `d5b46aa2502c91517f7f80c8ac158f42605257e8`  
Baseline annoncée et vérifiée : `3dac92808b055e235ee6f57cfec8e283455a85ca`

## Décision

| Niveau | État |
|---|---|
| Repéré | Oui — cinquième remise complète distincte |
| Reçu | Oui — 14 originaux archivés sans modification |
| Intégré | Non |
| Contrôlé techniquement | Empreintes, structure et baseline vérifiées ; contrôles producteurs non reproduits |
| Publié | Archive, reçu et rapport seulement |

Le paquet remplace `I83-HARMONISATION-4`, reçu mais non injecté. Les huit couples baseline/proposition du manifeste donnent **16 valeurs SHA-256 sur 16 exactes**. La comparaison porte sur les contenus : seul `I83_b.html` change réellement depuis la v4 ; les six autres HTML et `glossary/i83.py` sont identiques. La v4 n'a pas été réappliquée.

Empreinte agrégée de l'archive : `bce002e2c8a654b0ba6aee10d0cd68e56f67b977`.

## Contenu archivé

Les 14 objets d'origine sont conservés sous :

`livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_PR12_D5B46AA_I83_HARMONISATION_5/originals/`

Le signal Claude, le manifeste, le rapport, le diff, deux rapports de contrôle, sept propositions HTML et le complément de glossaire conservent leurs blobs Git d'origine.

## Relecture médicale ciblée

La réserve v4 est levée. Le nouveau passage distingue désormais :

- l'ARTE anticoagulée, traitée jusqu'à rétraction du thrombus, ce qui implique un contrôle échographique ;
- la TVP, dont la conduite dépend de son siège, de ses symptômes et du risque d'extension, avec renvoi au cours I80 — Thrombose veineuse profonde et thromboses veineuses (C-01-Cardiologie) ;
- le symptôme nouveau et le traitement en plusieurs temps, qui restent des indications explicites d'écho-Doppler.

L'encadré « À retenir » suit la même distinction et ne généralise plus une surveillance jusqu'à résolution à toute TVP.

Sources primaires relues :

- [SVS/AVF/AVLS 2023, recommandations 11.3.1–11.3.4 et 11.4.2](https://pmc.ncbi.nlm.nih.gov/articles/PMC11523430/)
- [ESVS 2022, §4.1.7 et recommandation 27](https://esvs.org/wp-content/uploads/2023/03/ESVS-2022-CVD-Guidelines.pdf)

Aucune nouvelle réserve bloquante n'est relevée dans le delta v4→v5. Cette contre-relecture ciblée ne certifie pas exhaustivement I83, le glossaire ni les 30 cours ; les limites déjà consignées restent applicables.

## Contrôle technique

Le producteur annonce :

- contrôle natif : 1 923 vérifications, 0 échec/erreur, vues 1360×900 et 390×844, 47 gabarits ;
- contrôle S01 : 72 vérifications, 0 erreur, Chromium 141.

Ces rapports sont archivés mais n'ont pas été reproduits indépendamment. Le workspace de cette itération ne contient ni le dépôt, ni `tools/livraison.py`, ni le runtime/navigateur nécessaires. Les opérations suivantes n'ont donc pas été exécutées :

- `tools/livraison.py check-claude` et `apply-claude` ;
- adaptation contrôlée du glossaire hors manifeste ;
- tests unitaires et audit statique après injection ;
- reconstruction des plateformes ;
- contrôle interactif ordinateur/mobile des fenêtres ARTE/EHIT, de la navigation, des débordements et de la console JavaScript.

Le lot est techniquement structuré pour une injection sélective des sept HTML ; le glossaire exige une adaptation manuelle séparée. La branche PR est fortement divergente et ne doit pas être fusionnée entière.

## Organisation préservée

- campagne historique : 30 cours, 15 Claude / 15 Codex ;
- backlog cardiologique : 20 cours, 10 Claude / 10 Codex ;
- fragments restants : 21, dont 11 Claude / 10 Codex ;
- aucune attribution ni aucun chapitre actif modifié ;
- aucune route, source canonique ou sortie générée modifiée ;
- catalogue maintenu en CIM-10, sans revendication de complétude CIM-11.

## Suite requise

Depuis un checkout propre de la tête distante de `main`, exécuter la réception via `tools/livraison.py`, l'injection sélective des sept HTML, l'adaptation séparée du glossaire, la reconstruction et tous les contrôles navigateur prescrits. Recontrôler `main` immédiatement avant toute publication.
