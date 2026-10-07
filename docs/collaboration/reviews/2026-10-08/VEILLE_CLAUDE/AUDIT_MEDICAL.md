# Première contrelecture médicale Codex — réception Claude du 8 octobre 2026

**Décision : nouvelle réception repérée et contrelecture ciblée effectuée ; aucune nouvelle remise de chapitre autorisée à l’injection par cette revue.** La proposition comparative la plus complètement examinée est **I44 — Troubles de la conduction et bradycardies (C-01-Cardiologie)**. Elle nécessite une correction de cohérence interne et une vérification indépendante de ses référentiels primaires. Cette décision ne retire pas les intégrations historiques ni leurs preuves.

## Révision examinée et méthode

- Branche reçue : `origin/claude/loving-shannon-spwrhc`.
- Tête examinée : `d8dae520c4d19213d0aa0099f3da34ca974b2c1d`.
- Ancienne réception de comparaison : `8ce3e99a18b96f6e6774d3d00bc709655e7ccb84`.
- Historique et inventaire des différences : `git log 8ce3e99..d8dae520`, `git diff --stat`, `git diff --name-only`, puis lecture d’objets exacts par `git show d8dae520:<chemin>` et `git ls-tree`. Le delta de 779 fichiers contient aussi des intégrations Codex fusionnées dans la branche Claude ; il ne représente pas 779 nouveaux fichiers médicaux produits par Claude.
- Aucun script de la livraison exécuté, aucun changement de branche, aucune injection, aucune modification des sources médicales. Seul ce rapport est ajouté.

L’accusé `livraisons/Livraison Claude/C-01-Cardiologie/ACCUSE_PRISE_EN_CHARGE_2026-10-08.md` est lu intégralement. Il déclare des propositions ESC 2026 en vérification et une production encore en cours. Le manifeste racine `livraisons/Livraison Claude/C-01-Cardiologie/livraison.json` conserve l’identifiant historique `GLOBAL_LOT5_JUSTIFICATION` et la base `75505d8b440a294808147cd1a1c4fb71f4a4c207` ; il ne constitue pas la remise finalisée des nouvelles propositions. Le rapprochement avec la sentinelle de réception confirme l’absence d’un nouveau manifeste de chapitre complet dans cette tête.

## Couverture réelle

Tous les chemins de propositions ci-dessous sont sous `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/`, à la tête exacte indiquée.

| Chapitre | Lecture réellement effectuée | Limite |
| --- | --- | --- |
| I44 — Troubles de la conduction et bradycardies (C-01-Cardiologie) | Fenêtre `I44/out/i44-esc-2026-comparaison__P1.html`, métadonnées `.json`, `.contreverif.json`, job `.json`, les deux fichiers `I44/edits/` et les deux fichiers `I44/verdicts/`. Passage canonique de l’onglet Examens correspondant à l’ancre, consulté au même commit. | Contrelecture ciblée de la proposition comparative ; aucune certification des quatre onglets, de toutes leurs fenêtres ou du glossaire. |
| I30 — Péricardites, épanchement péricardique, tamponnade et constriction (C-01-Cardiologie) | Fenêtre `I30/out/i30-esc-2026-comparaison__P1.html`, contrevérification `.contreverif.json`, ligne canonique de troponine de l’onglet Examens. | Audit ciblé du seuil et de la conséquence clinique ; reste du chapitre non relu. |
| I42 — Cardiomyopathies (C-01-Cardiologie) | Complément `I42/out/i42-esc-2026-comparaison__P1.html`, verdict `I42/verdicts/I42_pop2.json`, passage canonique d’anticoagulation correspondant. | Point de vigilance documenté sur le score ; aucune validation exhaustive des indications thérapeutiques. |
| I35 — Valvulopathies aortiques (C-01-Cardiologie) | Fenêtre `I35/out/i35-esc-2026-comparaison__P1.html` et contrevérification `.contreverif.json`. | Lecture de la proposition et des réserves déclarées ; aucune contrevérification primaire de la posologie. |

Le fichier collectif `travail/esc2026/verification.json` et le relevé `travail/esc2026/RECOMMANDATIONS_2026.md` sont lus. Leurs verdicts restent des déclarations de Claude ; la présente contrelecture n’accorde pas par héritage une validation Codex aux chapitres qui n’ont pas été relus directement.

Les brouillons **I83 — Varices des membres inférieurs (C-01-Cardiologie)** et **I89 — Autres atteintes non infectieuses des vaisseaux et des ganglions lymphatiques (C-01-Cardiologie)** ne sont pas audités médicalement ici. L’accusé les annonce en production. L’absence de nouvelle remise terminée est constatée, sans transformer leurs sauvegardes en livraisons injectables. Aucun nouveau paquet ESC 2026 spécifique à **I48 — Fibrillation et flutter auriculaires (C-01-Cardiologie)** ou **I50 — Insuffisance cardiaque (C-01-Cardiologie)** n’a été établi dans cette revue.

## Réserves bloquantes

### MED-01 — Référentiels 2026 non contrevérifiés indépendamment

**I44 — Troubles de la conduction et bradycardies (C-01-Cardiologie)** introduit notamment le passage de la resynchronisation de classe I/A à IIa/B1, l’extension de fraction d’éjection à `< 50 %`, et une enveloppe antibiotique IIb/C chez l’hémodialysé ou le greffé rénal. **I42 — Cardiomyopathies (C-01-Cardiologie)** propose des modifications de populations thérapeutiques et du point « C » du score embolique. Ces changements peuvent modifier des décisions cliniques : une référence bibliographique et le verdict du producteur ne remplacent pas la lecture indépendante de la ligne de recommandation et de ses notes.

Claude rapporte une lecture des textes intégraux dans des dossiers `I35/src` et `I44/src`. Ces textes et tableaux n’apparaissent pas dans les objets Git de la tête reçue ; ces chemins sont ignorés par `.gitignore`. Ils ne sont pas disponibles dans le checkout de cette session. Le relevé `RECOMMANDATIONS_2026.md` décrit encore une première étape basée sur des diapositives avec accès OUP bloqué, alors que `verification.json` affirme une lecture ultérieure des textes intégraux. Il manque la preuve accessible permettant au contrelecteur de reproduire cette dernière lecture.

Vérifications indépendantes effectuées avec TLS conservé, sans contournement : requêtes `curl --location --head --max-time 25 --silent --show-error` vers `https://doi.org/10.1093/eurheartj/ehag100`, `https://doi.org/10.1093/eurheartj/ehag098`, la page officielle ESC sur l’insuffisance cardiaque et le jeu de diapositives officiel `https://dam-assets.escardio.org/download/b2e587389baa11f185de06bdfb3e4be9`. Les quatre tentatives échouent avec `CONNECT tunnel failed, response 403`, code de sortie 56. Cette réponse du proxy ne prouve ni l’inexistence des publications ni leur contenu. Les tableaux primaires n’ont donc pas été lus par Codex.

**Pour lever la réserve :** rendre accessibles les sources officielles, ou fournir pour chaque changement les lignes pertinentes du tableau avec titre, DOI, numéro de tableau, population, classe/niveau et notes de bas de tableau, ainsi que la provenance du document consulté. Refaire ensuite la contrelecture indépendante au commit de remise. Les niveaux B1/B2, les nouveaux seuils et les nouvelles populations ne sont pas certifiés par ce rapport.

### MED-02 — Formulations incompatibles dans la proposition comparative

**I44 — Troubles de la conduction et bradycardies (C-01-Cardiologie)** : le job `I44/jobs/i44-esc-2026-comparaison__P1.json`, ancre `I44_c-a1`, propose de conserver :

> « la resynchronisation est alors recommandée (ESC 2021, classe I ; ESC 2026 : classe IIa, fraction &lt; 50 %). »

La fenêtre proposée écrit au contraire « À envisager (IIa, B1) », « option à discuter et non comme obligation ». Le verdict de l’onglet Pathologie précise que le passage à « à envisager » concerne tous les patients de la nouvelle recommandation. Le mot « recommandée » dans l’ancre peut rester compris comme l’indication actuelle, et attribue simultanément deux forces de recommandation à une seule phrase. Cette incohérence est démontrable à l’intérieur du paquet, indépendamment de l’accès au référentiel.

**Pour lever la réserve :** distinguer explicitement la règle historique ESC 2021 de la règle ESC 2026 proposée, puis harmoniser Pathologie, Examens et fenêtre comparative. Conserver les conditions de population et le caractère `< 50 %`, distinct du `≤ 50 %` de BLOCK HF. Refaire la lecture de l’ensemble du chapitre proposé, avec le tableau primaire accessible.

### MED-03 — Seuil de troponine et conséquence clinique insuffisamment conditionnés

**I30 — Péricardites, épanchement péricardique, tamponnade et constriction (C-01-Cardiologie)** : le tableau de la fenêtre exige correctement une hausse/baisse avec une valeur supérieure au 99e percentile propre au sexe. Mais le paragraphe de décision dit seulement qu’une troponine qui monte ou baisse sous 14 ng/L « peut donc signer une atteinte myocardique et faire classer la péricardite en myopéricardite ». La contrevérification de Claude formule une condition plus précise : valeur *entre le seuil féminin et 14 ng/L*. Cette condition manque dans le paragraphe remis.

La phrase « le seuil unique du fabricant, 14 ng/L » n’identifie pas la génération de test ni la valeur validée à utiliser localement. Le rapport de Claude admet que le texte 2026 ne chiffre pas le seuil de chaque méthode ; « environ la moitié » n’est pas un seuil utilisable en pratique. Le canonique consulté contient encore « seuil commun aux deux sexes » ; Claude laisse son complément « à décider ».

**Pour lever la réserve :** préciser que la valeur doit dépasser le 99e percentile validé pour la méthode et le sexe, malgré une valeur éventuellement inférieure au seuil global cité ; ne pas déduire une atteinte d’une simple variation sous ce seuil. Conditionner la qualification de myopéricardite au tableau de péricardite, à l’atteinte myocardique documentée et à l’évaluation ventriculaire, avec la source diagnostique correspondante. Réconcilier la fenêtre et la ligne canonique avant remise. Codex ne fournit pas ici de nouveau seuil numérique, faute de document primaire du dosage effectivement visé.

## Vigilances encore non levées

**I42 — Cardiomyopathies (C-01-Cardiologie)** : le verdict `I42/verdicts/I42_pop2.json` donne désormais un point « C » à une cardiomyopathie avec anomalie structurelle même asymptomatique, par rattachement au stade B. Ce changement pourrait faire passer un score nul à un score de 1 et modifier la discussion d’anticoagulation. Il faut lire le tableau primaire du score, les critères exacts du stade B et leurs exclusions, puis confronter le passage au contexte de fibrillation/flutter et aux seuils de traitement. Il ne faut pas transformer « anomalie structurelle » en règle autonome sans ces conditions. Cette remarque est une demande de preuve et de conditions ; ce rapport ne conclut pas que la nouvelle règle ESC citée est fausse.

**I35 — Valvulopathies aortiques (C-01-Cardiologie)** : Claude déclare une divergence de furosémide intraveineux entre l’ancienne dose de 20–40 mg chez le patient naïf et une dose 2026 de 40 mg. Ni la source primaire ni le paragraphe pharmacologique complet ne sont contrevérifiés ici. La divergence reste ouverte et doit être réconciliée dans une remise de chapitre, en tenant compte de la population, de la situation clinique et du référentiel daté. Ce rapport n’impose aucune modification posologique sur la seule affirmation du producteur.

## Conditions de la prochaine décision d’injection

1. Recevoir un seul chapitre terminé avec commit précis, fichiers proposés, rapport de couverture réelle, base des empreintes et éventuelles adaptations ; une sauvegarde de `travail/` ne suffit pas.
2. Rendre reproductible la lecture des sources primaires et corriger les réserves applicables au chapitre choisi. Conserver les propositions de Claude et tracer les corrections, sans effacer ses rapports.
3. Effectuer une contrelecture indépendante des quatre onglets, des fenêtres, des sources et du glossaire au même commit, puis les contrôles techniques adaptés. Les contrôles historiques du lot 5 ne certifient pas ce paquet ultérieur.
4. Autoriser seulement le chapitre dont les réserves bloquantes sont levées ; injecter, reconstruire, tester et publier avec un reçu distinct. Le chapitre suivant reste fermé jusqu’à la clôture du premier.

**État final de ce poste : audit ciblé enregistré, sources primaires 2026 non accessibles, réserves MED-01 à MED-03 ouvertes, aucune injection effectuée. Aucune revendication de revue exhaustive ni de complétude CIM-11.**

## Réception actualisée — 8 octobre 2026, tête figée `3f90204`

**Un nouveau lot formel est désormais remis pour audit ; il n’est pas validé pour injection par cette contrelecture.** Le constat antérieur d’absence de nouvelle remise concerne exclusivement la tête `d8dae520c4d19213d0aa0099f3da34ca974b2c1d`. Les preuves de cette première réception sont conservées ci-dessus.

### Révision et évolution de la remise

Lecture seule dans le miroir `/workspace/medina-env/claude-watch-validation-final/git`, par identifiants d’objets Git, sans se fier à une tête mobile :

- Nouvelle tête auditée : `3f90204dc663d6f7dee3e98bbd5819d457b6a586`.
- Delta de réception : `d8dae520c4d19213d0aa0099f3da34ca974b2c1d..3f90204dc663d6f7dee3e98bbd5819d457b6a586`.
- Commit de remise déclaré dans `docs/collaboration/SIGNAUX_CLAUDE.json` : `020e65b721415481298d0cf295ba0ed8966875ea`, état `pret_audit` pour `ESC2026_COMPARAISONS`.
- Base canonique du nouveau manifeste : `b6e5d18c2c2383893819c4c0834d6402bbe30e67`.
- Le nouveau `livraisons/Livraison Claude/C-01-Cardiologie/livraison.json` contient **25 fichiers : 18 remplacements et 7 ajouts**, pour huit chapitres. L’ancien lot 5 est archivé avec son manifeste. Ces nombres concordent avec la sentinelle de réception.
- `git diff --name-only 020e65b..3f90204 -- <manifeste> <sources> <rapport ESC2026>` ne retourne aucune différence : les fichiers de cette remise sont identiques aux objets du commit déclaré, malgré les nouvelles sauvegardes de production.

Le rapport final `archives/2026-10-08-ESC2026_COMPARAISONS/rapport.md`, le manifeste et les deux documents de signal/veille sont lus. Le signal réunit huit comparaisons : **I30 — Péricardites, épanchement péricardique, tamponnade et constriction (C-01-Cardiologie)** ; **I33 — Endocardite infectieuse (C-01-Cardiologie)** ; **I34 — Valvulopathies mitrales, tricuspides et pulmonaires (C-01-Cardiologie)** ; **I35 — Valvulopathies aortiques (C-01-Cardiologie)** ; **I40 — Myocardites (C-01-Cardiologie)** ; **I42 — Cardiomyopathies (C-01-Cardiologie)** ; **I44 — Troubles de la conduction et bradycardies (C-01-Cardiologie)** ; **Q21 — Cardiopathies congénitales de l’adulte (C-01-Cardiologie)**. Cette liste décrit le manifeste ; elle ne signifie pas que Codex a audité médicalement ces huit chapitres en entier.

Les sauvegardes supplémentaires **I83 — Varices des membres inférieurs (C-01-Cardiologie)** et **I89 — Autres atteintes non infectieuses des vaisseaux et des ganglions lymphatiques (C-01-Cardiologie)** restent `en_production` dans le signal et hors de ce manifeste. Elles ne sont pas auditées médicalement par cet ajout.

### Contrôle ciblé des fichiers effectivement remis

Les repères de ligne suivants concernent les objets de `3f90204`, sous `livraisons/Livraison Claude/C-01-Cardiologie/sources/` ; ils ne désignent pas une injection canonique.

| Réserve | Preuve actuelle dans les sources remises | Décision ciblée |
| --- | --- | --- |
| MED-01 — Sources primaires | Le rapport final affirme une lecture des quatre textes intégraux ESC du 28 août 2026 et précise « copies locales non versionnées ». Le delta n’apporte pas les tableaux primaires permettant de reproduire cette lecture. | Non levée. Les requêtes officielles précédentes ont rencontré un refus du proxy ; aucun nouveau contenu primaire n’a été lu ici. Cela établit une limite d’accès, pas une erreur démontrée des publications citées. |
| MED-02 — I44 — Troubles de la conduction et bradycardies (C-01-Cardiologie) | `chapters/I44/I44_a.html:20` applique le verdict reformulé ; `chapters/I44/I44_b.html:113` écrit désormais « pour tous, qu’“à envisager” (classe IIa, niveau B1) ». Mais `chapters/I44/I44_c.html:87` conserve « la resynchronisation est alors recommandée (ESC 2021, classe I ; [bouton ESC 2026 : classe IIa], fraction &lt; 50 %) ». La fenêtre `chapters/I44/I44_pop_esc_comparison.html:5` écrit « À envisager (IIa, B1) », et sa ligne 9 précise « option à discuter ». | Non levée. La correction de l’onglet Pathologie ne corrige pas le passage Examens. L’incohérence de formulation entre fichiers remis est prouvée ; la validité médicale du changement de classe reste à vérifier sur le tableau primaire. |
| MED-03 — I30 — Péricardites, épanchement péricardique, tamponnade et constriction (C-01-Cardiologie) | `chapters/I30/I30_c.html:29` ajoute un bouton « ESC 2026 : seuil propre au sexe » après « 14 ng/L, seuil commun aux deux sexes ». Le paragraphe de décision de `chapters/I30/I30_pop_esc_comparison.html:8` conserve « une troponine qui monte ou baisse sous cette valeur peut donc signer une atteinte myocardique et faire classer la péricardite en myopéricardite ». | Non levée. Le bouton permet de lire la comparaison, mais le paragraphe n’explicite toujours pas le dépassement du 99e percentile validé pour le sexe et le dosage. Cette insuffisance de condition est constatée dans le texte remis ; aucun seuil numérique alternatif n’est validé ici. |

**I42 — Cardiomyopathies (C-01-Cardiologie)** : `chapters/I42/I42_pop2.html:113` applique effectivement la proposition mentionnée dans le premier audit : CHA₂DS₂-VA actuel et point « C » pour le stade B à D, avec la conséquence « anomalie structurelle, même asymptomatique, apporte donc au moins un point ». La vigilance sur le tableau exact du score et les critères de population demeure ; cette évolution n’est pas certifiée indépendamment par la lecture d’un référentiel primaire. Il ne s’agit pas d’une erreur déclarée prouvée.

**I35 — Valvulopathies aortiques (C-01-Cardiologie)** : le rapport final conserve explicitement la divergence de furosémide « non corrigée, à traiter ». **I40 — Myocardites (C-01-Cardiologie)** : il conserve la qualification de fraction d’éjection « modérément réduite » déclarée différente du référentiel 2025. Ces réserves rapportées par Claude ne sont ni supprimées ni transformées en corrections posologiques/terminologiques vérifiées par Codex dans cette revue ciblée.

### Portée et prochaine action

Cette seconde contrelecture concerne les passages finaux cités et les éléments de remise. Elle ne constitue pas un audit de tous les 25 fichiers complets, des quatre onglets de chacun des huit chapitres, du glossaire ou de toutes les fenêtres. Aucun code entrant — y compris le nouveau programme de veille — n’a été exécuté par ce poste ; aucun canonique n’a été modifié.

La nouvelle remise est recevable pour examen, contrairement à l’état documentaire de la première tête. **Les réserves médicales ciblées restent ouvertes.** La prochaine étape est de faire corriger les formulations MED-02 et MED-03, de rendre reproductible la vérification primaire MED-01, puis de relire chaque chapitre séparément au nouveau SHA. Les chapitres en réserve ne doivent pas être injectés par bloc au seul motif que le manifeste comporte des empreintes ou que Claude déclare des contrôles techniques réussis. Le signal `audits_de_codex: []` à la tête reçue ne constitue pas une attestation d’approbation de cette remise.

## Contrôle du delta — 8 octobre 2026, tête figée `482a679`

**Les réserves MED-01, MED-02 et MED-03 ne sont pas levées. Le manifeste reste présent, mais ses 25 fichiers sources sont absents de la nouvelle tête.** Ce contrôle établit une évolution de la remise et l’identité de ses éléments de travail ; il ne constitue pas un nouvel audit médical exhaustif.

Révisions comparées dans le miroir `/workspace/medina-env/claude-watch/git` : `3f90204dc663d6f7dee3e98bbd5819d457b6a586` → `482a6799b3e076bf49e9699b6091c82d54c2d105`. Méthode : `git diff --name-status --no-renames` sur les chemins de remise ; inventaires exacts des objets par `git ls-tree -r -z` des deux commits ; comparaison des identifiants de blobs ; lecture du signal. Aucun programme entrant exécuté, aucune injection ni écriture canonique.

### Éléments rigoureusement identiques

Tous les chemins de cette table sont relatifs à `livraisons/Livraison Claude/C-01-Cardiologie/`. L’identifiant donné est le même blob Git dans les deux têtes : il prouve une identité de contenu, sans répéter artificiellement la contrelecture.

| Élément | Blob identique à `3f90204` et `482a679` |
| --- | --- |
| `livraison.json` | `f97e7e568332fabede091663a311b4d40b69e498` |
| `archives/2026-10-08-ESC2026_COMPARAISONS/rapport.md` | `285d4f54f7e551e45b057697bc5a899e9a4c2b96` |
| Job de l’ancre CRT — I44 — Troubles de la conduction et bradycardies (C-01-Cardiologie), `travail/esc2026/I44/jobs/i44-esc-2026-comparaison__P1.json` | `af26ee7c3cd88980b8c7958cd255de64d1f46a16` |
| Sortie comparative — I44 — Troubles de la conduction et bradycardies (C-01-Cardiologie), `travail/esc2026/I44/out/i44-esc-2026-comparaison__P1.html` | `48b8bbca41109b0bbfdee44bd3258e87fe2746df` |
| Sortie comparative — I30 — Péricardites, épanchement péricardique, tamponnade et constriction (C-01-Cardiologie), `travail/esc2026/I30/out/i30-esc-2026-comparaison__P1.html` | `9262e9ab47c676ec6bc55acbf60527c9a9b3c044` |
| `travail/esc2026/verification.json` | `c902b5c87e7d8d4432fa0aa00dcb7ef6e3466c25` |

Le signal `docs/collaboration/SIGNAUX_CLAUDE.json` annonce encore le commit `020e65b721415481298d0cf295ba0ed8966875ea`, état `pret_audit`, et `audits_de_codex: []`. Il n’annonce pas une correction des réserves.

### Sources finales absentes, et non simplement identiques

Le manifeste inchangé référence 25 `source_path`. La comparaison avec l’arbre exact de `482a679` constate **25 absences sur 25** dans le dossier racine de remise. Pour les deux chapitres ciblés, les anciens blobs finaux ci-dessous ont aussi été recherchés dans l’ensemble de la nouvelle arborescence : aucun chemin de cette tête ne porte ces mêmes blobs. Le déplacement apparent de certains fichiers dans des archives historiques ne préserve donc pas ces six versions finales à l’identique dans la tête courante.

| Chapitre | Ancien chemin sous `sources/` | Blob final de `3f90204` | État à `482a679` |
| --- | --- | --- | --- |
| I44 — Troubles de la conduction et bradycardies (C-01-Cardiologie) | `chapters/I44/I44_a.html` | `8fa3aff363658a2ea556cfc90b9dce8eb6145b32` | Absent ; aucun même blob ailleurs dans l’arbre. |
| I44 — Troubles de la conduction et bradycardies (C-01-Cardiologie) | `chapters/I44/I44_b.html` | `e059d922a523387f544c658cc32d4b92a401ea75` | Absent ; aucun même blob ailleurs dans l’arbre. |
| I44 — Troubles de la conduction et bradycardies (C-01-Cardiologie) | `chapters/I44/I44_c.html` | `e486d4cb00b862d72f89cdc1d5abc31e10804e9d` | Absent ; aucun même blob ailleurs dans l’arbre. |
| I44 — Troubles de la conduction et bradycardies (C-01-Cardiologie) | `chapters/I44/I44_pop_esc_comparison.html` | `372f05d873e4cf2ab653da32da713e06996ffeda` | Absent ; aucun même blob ailleurs dans l’arbre. |
| I30 — Péricardites, épanchement péricardique, tamponnade et constriction (C-01-Cardiologie) | `chapters/I30/I30_c.html` | `d3958e434a347f02d3afe048598aa0b4fae8d1ce` | Absent ; aucun même blob ailleurs dans l’arbre. |
| I30 — Péricardites, épanchement péricardique, tamponnade et constriction (C-01-Cardiologie) | `chapters/I30/I30_pop_esc_comparison.html` | `617df074924cc2bfe3639cfc53360aa5d0122b6a` | Absent ; aucun même blob ailleurs dans l’arbre. |

Les anciens objets restent récupérables au commit de remise déclaré ; leur absence dans cette nouvelle tête ne signifie pas qu’ils ont disparu de l’historique. En revanche, on ne peut pas contrôler ou injecter le dossier courant selon ce manifeste comme si ses sources existaient encore.

### État des réserves et décision

- **MED-01 : non levée.** Aucun document primaire sous `travail/esc2026/**/src/` ni PDF de ce périmètre n’est présent dans l’arbre reçu. Le rapport et la contrevérification restent identiques et renvoient aux copies locales non versionnées. Aucune nouvelle lecture indépendante de tableau n’est établie. La limite d’accès primaire reste distincte d’une erreur médicale démontrée.
- **MED-02 : non levée.** Pour **I44 — Troubles de la conduction et bradycardies (C-01-Cardiologie)**, le job qui conserve « recommandée » avec la classe IIa et la fenêtre « à envisager » n’ont pas changé. Les fichiers finaux courants sont absents ; aucune nouvelle version finale corrigée n’est livrée au chemin annoncé. La contradiction constatée au commit précédent demeure dans la proposition conservée, sans préjuger de la validité primaire du changement de classe.
- **MED-03 : non levée.** Pour **I30 — Péricardites, épanchement péricardique, tamponnade et constriction (C-01-Cardiologie)**, la sortie contenant le paragraphe insuffisamment conditionné est le même blob que précédemment. Aucun fichier final corrigé n’est remis dans la tête courante.

**Injection du lot courant suspendue :** restaurer ou remettre explicitement les sources du chapitre choisi avec un manifeste cohérent, corriger les réserves et rendre accessible leur preuve primaire, puis faire vérifier la version exacte. Ce contrôle n’a pas audité toutes les autres modifications importées dans la nouvelle tête, ni les nouveaux brouillons de production ; leurs différences ne sont pas assimilées à une résolution de ces réserves.

## Restauration et rapprochement de base — 8 octobre 2026, tête figée `f2e9934`

**Les 25 sources finales sont restaurées ; le blocage documentaire « sources absentes » est levé à cette tête. Les réserves médicales MED-01, MED-02 et MED-03 restent ouvertes.** Aucun nouvel audit exhaustif n’est revendiqué pour les fichiers dont les blobs sont identiques à la remise précédemment relue.

Contrôle en lecture seule dans `/workspace/medina-env/claude-watch/git`, au commit exact `f2e9934c7c372bde5cc1d116f9b24fe3bb621a2f`. Comparaisons : delta depuis `482a6799b3e076bf49e9699b6091c82d54c2d105`, identité des sources avec la remise `020e65b721415481298d0cf295ba0ed8966875ea`, et différences entre les bases canoniques. Aucun programme entrant exécuté, aucun canonique modifié, aucune injection.

### Restauration réelle, correction médicale non confondue

Le manifeste contient toujours 25 fichiers : chaque `source_path` existe désormais dans l’arbre reçu. La base passe de `b6e5d18c2c2383893819c4c0834d6402bbe30e67` à `39b7ff0cc585c59ffbb99fb448940daa1950b34d`. Le rapport final décrit une réapplication après convergence sur cette nouvelle base et actualise la taille construite du fragment ; il n’annonce pas une correction des réserves MED-01 à MED-03.

Comparaison de tous les identifiants de blobs du manifeste avec `020e65b` : **18 fichiers identiques, 7 fichiers différents**. Les quatre fichiers décisifs pour les réserves ciblées ont retrouvé exactement leurs anciens blobs :

| Chapitre | Chemin relatif sous `sources/` | Blob identique à `020e65b` et `f2e9934` |
| --- | --- | --- |
| I44 — Troubles de la conduction et bradycardies (C-01-Cardiologie) | `chapters/I44/I44_c.html` | `e486d4cb00b862d72f89cdc1d5abc31e10804e9d` |
| I44 — Troubles de la conduction et bradycardies (C-01-Cardiologie) | `chapters/I44/I44_pop_esc_comparison.html` | `372f05d873e4cf2ab653da32da713e06996ffeda` |
| I30 — Péricardites, épanchement péricardique, tamponnade et constriction (C-01-Cardiologie) | `chapters/I30/I30_c.html` | `d3958e434a347f02d3afe048598aa0b4fae8d1ce` |
| I30 — Péricardites, épanchement péricardique, tamponnade et constriction (C-01-Cardiologie) | `chapters/I30/I30_pop_esc_comparison.html` | `617df074924cc2bfe3639cfc53360aa5d0122b6a` |

Pour les sept fichiers différents, lecture des changements ligne par ligne et rapprochement avec la différence canonique `b6e5d18..39b7ff0` : toutes les lignes ajoutées/retirées correspondent aux mêmes modifications présentes dans cette différence de base, sans ligne de changement proposée supplémentaire dans ces sept fichiers. Il s’agit de la reprise de modifications déjà contenues dans la nouvelle base, dont certaines améliorent le contenu médical ; elles ne corrigent pas les passages faisant l’objet des réserves ciblées.

| Chapitre et fichier repris | Évolution observée depuis la première remise |
| --- | --- |
| I44 — Troubles de la conduction et bradycardies (C-01-Cardiologie), `chapters/I44/I44_a.html` | Statut de relecture repris ; disparition de la déduction automatique « cinq demi-vies = cause médicamenteuse exclue », remplacée par une surveillance selon médicament, métabolites et fonctions d’élimination. |
| I44 — Troubles de la conduction et bradycardies (C-01-Cardiologie), `chapters/I44/I44_b.html` | Correction préexistante du traitement de l’hyperkaliémie : élimination selon contexte et soutien circulatoire/stimulation en parallèle si nécessaire. Le passage CRT concerné par MED-02 ne change pas. |
| I33 — Endocardite infectieuse (C-01-Cardiologie), `chapters/I33/I33_b.html` | Correction préexistante de l’interprétation d’une seule paire d’hémocultures positive selon le germe et le contexte, notamment pour *S. aureus*. |
| I34 — Valvulopathies mitrales, tricuspides et pulmonaires (C-01-Cardiologie), `chapters/I34/I34_b.html` | Prudence préexistante sur le choix de l’anticoagulant dans le rétrécissement mitral dégénératif serré et la portée d’INVICTUS. |
| I35 — Valvulopathies aortiques (C-01-Cardiologie), `chapters/I35/I35_b.html` | Corrections préexistantes des conditions de chirurgie précoce dans l’insuffisance aortique, de l’accès transfémoral du TAVI et des limites d’interprétation de la durabilité. |
| I42 — Cardiomyopathies (C-01-Cardiologie), `chapters/I42/I42_a.html` | Statut de relecture repris. |
| Q21 — Cardiopathies congénitales de l’adulte (C-01-Cardiologie), `chapters/Q21/Q21_a.html` | Statut de relecture et liste des référentiels repris. |

Cette lecture de changements ne certifie pas médicalement tous ces chapitres ni les référentiels cités ; elle identifie la provenance des différences dans la base de convergence.

### État des trois réserves

- **MED-01 : non levée.** Aucun document primaire ESC 2026 n’est ajouté au périmètre `travail/esc2026/**/src/` ni comme PDF dans ce dossier. La section « Référentiels lus » du rapport conserve la mention « copies locales non versionnées ». Le changement de base et les contrôles techniques déclarés ne rendent pas reproductible la lecture indépendante des classes/niveaux et populations. Aucune nouvelle vérification primaire n’est établie ; l’inaccessibilité précédente reste une limite de preuve, sans conclusion sur l’existence ou l’exactitude des textes cités.
- **MED-02 : non levée.** **I44 — Troubles de la conduction et bradycardies (C-01-Cardiologie)** retrouve, dans l’onglet Examens et sa fenêtre, les mêmes blobs que ceux portant l’incohérence « recommandée » avec IIa versus « à envisager ». Les changements des onglets Pathologie et prise en charge proviennent de la nouvelle base et concernent d’autres passages. La restauration ne constitue pas une correction de cette incohérence.
- **MED-03 : non levée.** **I30 — Péricardites, épanchement péricardique, tamponnade et constriction (C-01-Cardiologie)** retrouve ses mêmes blobs d’onglet Examens et de fenêtre. Le paragraphe de décision conserve donc l’insuffisance de condition du seuil propre au sexe et au dosage constatée précédemment.

**Décision actuelle : sources de remise de nouveau disponibles, réserves médicales ciblées ouvertes, aucune injection autorisée par ce contrôle.** Fournir les corrections et les preuves primaires au SHA de la prochaine remise, puis refaire uniquement les contrelectures affectées avant la décision d’intégration du chapitre concerné. Les nouveaux fichiers de vérification des brouillons de production restent hors du périmètre médical de ce contrôle.
