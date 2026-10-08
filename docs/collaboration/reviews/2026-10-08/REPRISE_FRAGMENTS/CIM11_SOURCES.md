# Sources officielles CIM-11 pour la reprise interne de I-03-Infectiologie

**La version courante est vérifiée comme CIM-11 MMS 2026-01, disponible en français**, au 8 octobre 2026 : la page officielle des versions marque explicitement `2026-01 (latest release)` et offre la langue `fr`. Cette conclusion vient de la page OMS lue, pas d’une version déduite de la date de session. Les fichiers officiels sont téléchargés dans `/workspace/work/cim11-officiel/`. Aucun contenu ni branche du dépôt n’a été modifié.

**Résultat concret :** archive officielle française, fichier TXT/XLSX intégral, PDF imprimable, tables officielles de mapping et de tabulation, documentation d’API ; extraction candidate du chapitre OMS 01 en JSON et CSV avec tous les parents et toutes les catégories résiduelles. Le périmètre pédagogique T1 n’est pas encore établi ni validé.

## Preuve de version et accès

- Versions OMS : https://icd.who.int/browse/releases/mms/en — HTTP 200, lu le 8 octobre 2026 à 16:32 Europe/Zurich ; `2026-01` est la dernière version déclarée, `fr` figure parmi les versions publiées (la pré-publication allemande est distincte).
- Navigateur français versionné : https://icd.who.int/browse/2026-01/mms/fr — HTTP 200 ; indique `2026-01`, la langue française sélectionnée et les liens exacts des archives utilisées.
- Langues/version de l’API : https://icd.who.int/docs/icd-api/SupportedClassifications/ — HTTP 200 ; ligne `2026-01`, MMS français supporté.
- Statut réseau observé pendant cette reprise : configuration cloud actuelle, réseau `unrestricted`, état `enforced`, observations actuelles ; politique locale `/etc/codex/network-policy.json` concordante. Les anciens `CONNECT 403` conservés dans le rapport A41 ne décrivent plus cet accès.
- Toutes les pages et archives ci-dessous sont publiques et obtenues sans inscription, sans connexion et sans en-tête d’authentification. Leurs réponses et empreintes sont enregistrées. L’API de données JSON possède une exigence différente, détaillée plus bas.

## Téléchargements primaires et empreintes

| Source officielle | Fichier local | Taille | SHA-256 |
| --- | --- | ---: | --- |
| https://icdcdn.who.int/static/releasefiles/2026-01/SimpleTabulation-ICD-11-MMS-fr.zip | `SimpleTabulation-ICD-11-MMS-fr-2026-01.zip` | 4979802 | `c5c7c4a07ad007892a642afd1599314f303eac5dcee89c1d1e315fcf64fa2f0f` |
| https://icdcdn.who.int/static/releasefiles/2026-01/mapping.zip | `mapping-2026-01.zip` | 6809366 | `2eb158cf2a0d53690d6e9baf0956f7617e1315e4f2a44dfc3db3be8f49193a1d` |
| https://icdcdn.who.int/static/releasefiles/2026-01/MortalityTabulationList_en.zip | `MortalityTabulationList_en-2026-01.zip` | 151058 | `fed730b06b399e66d476bde74902a12dc19e83d64e2013fec0ef717b936f8f6f` |
| https://icdcdn.who.int/static/releasefiles/2026-01/MorbidityTabulationList_en.zip | `MorbidityTabulationList_en-2026-01.zip` | 192229 | `854a978190b2fc95e93ac71b8bdd9b446855b4ea3eb1c6c5ca4ae1dec023d37d` |
| https://icdcdn.who.int/static/releasefiles/changes/changes_MMS_2026-01_2025-01.zip | `changes-MMS-2026-01-2025-01.zip` | 26662 | `fff8df6e3416a7e72f551c4e0fcb549e70f0fe2ea0c62c1835d53f7bf8921622` |
| https://icdcdn.who.int/static/releasefiles/2026-01/print-ICD-11-MMS-fr.zip | `print-ICD-11-MMS-fr-2026-01.zip` | 11521267 | `917a156fcb28aa3ef861d78812fa3d9a32296d48b478f6497f32e3b9809e2a97` |

Toutes les archives ont répondu HTTP 200. Les liens proviennent directement du menu du navigateur MMS 2026-01 FR, sauf la liste de changements qui provient de la page des versions. Les dates d’accès UTC, URL finales, types MIME et dates `Last-Modified` disponibles figurent dans `provenance.json`, `official-downloads.json` et `official-more-downloads.json`. Les originales ZIP et leurs membres sont conservés séparément sous `extracted/`.

### Tableur intégral MMS français

Archive : `SimpleTabulation-ICD-11-MMS-fr-2026-01.zip`. Membres exacts : `readme.txt`, `SimpleTabulation-ICD-11-MMS-fr.txt` (13 509 150 octets), `SimpleTabulation-ICD-11-MMS-fr.xlsx` (4 476 452 octets). Le TXT original existe aussi à la racine de ce dossier ; le fichier `readme.txt` explique les champs. Les **37 130 enregistrements** globaux résultent de la lecture CSV/TSV conforme aux cellules citées ; ne pas confondre ce nombre avec le nombre physique de lignes (certains champs contiennent des sauts de ligne).

Champs officiels utiles : `Foundation URI`, `Linearization URI`, `Code`, `BlockId`, `TitleEN`, `Title`, `ClassKind`, `DepthInKind`, `IsResidual`, `ChapterNo`, `BrowserLink`, `isLeaf`, `Primary tabulation`, `Grouping1` à `Grouping5`, `CodingNote`, `Parent`. L’en-tête conserve le timestamp d’export `Version:2026 Jan 17 - 05:30 UTC` ; il ne remplace pas l’identifiant de release `2026-01` vérifié dans l’URL et la page officielle.

### PDF imprimable français

Archive : `print-ICD-11-MMS-fr-2026-01.zip`, membre `ICD-11-MMS-fr.pdf`, 15 119 704 octets, 2 745 pages. Le texte du **chapitre OMS 01** est extrait sous `chapter01-print-fr.txt` à partir des **pages physiques PDF 41 à 172 incluses**, numérotées **39 à 170** dans le document. Les contrôles d’extraction ont vérifié « CHAPITRE 01 » présent et « CHAPITRE 02 » absent, ainsi que le dernier code `1H0Z`. Le PDF original intégral reste la source.

Ce PDF apporte les descriptions, termes inclus/exclus et « codé ailleurs », absents du simple tableur. Il permet des contrôles de rattachement documentaire sans authentification API. Les premiers extraits de navigation qui ont servi à trouver les pages restent des fichiers de travail ; ils ne sont pas un inventaire différent.

### Mapping officiel et listes de tabulation

`mapping-2026-01.zip` conserve les tables OMS CIM-10↔CIM-11 (une catégorie et catégories multiples), ainsi que les tables concernant la Fondation. Son `readme.txt` précise que les concepts CIM-10 peuvent ne plus avoir un code unique dans CIM-11 et changer de chapitre. Aucun mapping automatique n’a été exécuté. Cette archive décrit CIM-10 ; elle n’établit pas une correspondance bijective pour les catégories et variantes nationales CIM-10-GM 2024 du catalogue MEDINA.

`MorbidityTabulationList_en-2026-01.zip` contient une liste de tabulation de **347 ensembles** (348 lignes de feuille dont l’en-tête), et son PDF explicatif. `MortalityTabulationList_en-2026-01.zip` contient **158 ensembles** (159 lignes dont l’en-tête), et son PDF explicatif. Leurs en-têtes indiquent `Export Date:2026-01-29 15:17 Used ICD version:2026-01-17`. Il s’agit de regroupements pour statistiques, en anglais, avec inclusions/exclusions, ensembles et codes développés ; **ces agrégats ne remplacent pas le catalogue complet ni le périmètre d’enseignement T1**.

## Extraction candidate du chapitre OMS 01

Entrée officielle : **Certaines maladies infectieuses ou parasitaires**, identifiant Fondation `http://id.who.int/icd/entity/1435254666`, URL de consultation versionnée https://icd.who.int/browse/2026-01/mms/fr#1435254666. Extraction strictement filtrée sur `ChapterNo == 01`, sans sélection de diagnostic ni exclusion d’une catégorie résiduelle.

| Type de lignes | Nombre |
| --- | ---: |
| Chapitre organisateur | 1 |
| Blocs organisateurs | 43 |
| Catégories et sous-catégories codées | 1025 |
| Total de lignes du chapitre OMS 01 | 1069 |
| Catégories à quatre caractères, profondeur de catégorie 1 | 342 |
| Sous-catégories de profondeur 2 | 531 |
| Sous-catégories de profondeur 3 | 152 |
| Catégories résiduelles, incluses dans les comptes ci-dessus | 323 |
| Catégories feuilles | 876 |

Ces nombres décrivent l’export du **chapitre de classification OMS**, sans ratio d’enseignement. Les blocs et le chapitre ne sont pas des leçons supplémentaires. Les 342 catégories à quatre caractères sont également annoncées dans le PDF, au début du chapitre. Il n’y a pas d’URI MMS dupliquée dans les 1 069 lignes sélectionnées.

Fichiers de reprise :
- `chapter01_mms_2026-01_fr.json` : champs officiels originaux, champs normalisés distincts, rang d’enregistrement dans le TXT, code, bloc, titres, parent source, URI Fondation, URI MMS, catégories résiduelles, groupements, provenance et limites. Aucun rattachement MEDINA ni passage pédagogique attribué.
- `chapter01_mms_2026-01_fr.csv` : tous les champs officiels du chapitre, avec `SourceRecordNumber` et `ReleaseId` ajoutés ; parents vides et résiduelles conservés.
- `chapter01-print-fr.txt` : descriptions et renvois du PDF pour ce chapitre, extraction documentée.
- `provenance.json` : réponses officielles et digest des fichiers locaux ; une extraction locale reste un dérivé identifié, distinct de l’archive OMS.

### Points de fidélité à préserver

1. **Les 323 catégories résiduelles n’ont pas d’URI Fondation.** Elles possèdent toutefois un code, une URI MMS et un rattachement dans l’export. Aucune n’a été supprimée ni dotée d’un faux ID Fondation. C’est cohérent avec la documentation OMS : la Fondation ne contient pas les catégories résiduelles de la linéarisation.
2. **Les URI MMS de l’export ne portent pas explicitement la release**, par exemple `http://id.who.int/icd/release/11/mms/1435254666`. Conserver la valeur originale et toujours associer la provenance de l’archive `2026-01`, plutôt que prétendre que cette chaîne contient une version.
3. **`BrowserLink` est une formule `hyperlink` vers `latestrelease/mms/en`**, même dans l’export FR. La formule originale est conservée. Le JSON ajoute séparément un lien FR `2026-01` dérivé par substitution explicite, marqué comme non ouvert individuellement ; il ne prétend pas que ce lien est une colonne officielle de l’export.
4. **`Parent` est vide pour 1C1G — Borréliose de Lyme**, constat recoupé sur le TXT et la cellule du XLSX officiel. Le champ `Grouping1` vaut `BlockL1-1C1`, mais il n’a pas été utilisé pour inventer un parent URI. Le parent de la racine chapitre est naturellement vide. Cette anomalie documentaire reste à contrôler dans le navigateur ou l’API authentifiée avant validation d’une hiérarchie pédagogique complète.
5. Les tirets d’indentation des titres et les champs bruts sont conservés. Le titre lisible sans tirets est un champ distinct. Les sous-catégories ne sont pas rabattues sur leur catégorie parente.

### Groupes OMS de niveau supérieur présents

| Bloc | Intitulé officiel français, indentation retirée pour lecture |
| --- | --- |
| BlockL1-1A0 | Gastroentérite ou colite d'origine infectieuse |
| BlockL1-1A6 | MST - [maladie sexuellement transmissible] |
| BlockL1-1B1 | Maladies mycobactériennes |
| BlockL1-1B4 | Certaines maladies à staphylocoques ou à streptocoques |
| BlockL1-1B7 | Infections bactériennes pyogènes de la peau ou des tissus souscutanés |
| BlockL1-1B9 | Certaines anthropozoonoses bactériennes précisées |
| BlockL1-1C1 | Autres maladies bactériennes |
| BlockL1-1C6 | Maladie du virus de l'immunodéficience humaine |
| BlockL1-1C8 | Infections virales du système nerveux central |
| BlockL1-1D0 | Infections non-virales ou non précisées du système nerveux central |
| BlockL1-1D2 | Dengue |
| BlockL1-1D4 | Certaines fièvres virales transmises par des arthropodes |
| BlockL1-1D6 | Certaines maladies zoonotiques virales |
| BlockL1-1D8 | Certaines autres maladies virales |
| BlockL1-1E3 | Grippe |
| BlockL1-1E5 | Hépatite virale |
| BlockL1-1E7 | Infections virales caractérisées par des lésions cutanées ou muqueuses |
| BlockL1-1F2 | Mycoses |
| BlockL1-1F4 | Maladies parasitaires |
| BlockL1-1G4 | Sepsis |
| BlockL1-1G8 | Séquelles de maladies infectieuses |

## API officielle : documentée, données sans auth refusées

Documentation : https://icd.who.int/docs/icd-api/APIDoc-Version2/ et https://icd.who.int/docs/icd-api/API-Authentication/ (HTTP 200). L’API cloud utilise OAuth2 `client credentials`, obtenus après inscription/connexion ; aucune inscription, connexion ou demande de clé effectuée. Version de protocole `API-Version: v2`, langue via `Accept-Language: fr`, ressources MMS sous https://id.who.int/.

Vérification faite sans identité : `GET https://id.who.int/icd/release/11/2026-01/mms/1435254666`, avec les seuls en-têtes `API-Version: v2`, `Accept: application/json`, `Accept-Language: fr`, a retourné **HTTP 401**. La réponse est enregistrée dans `api-chapter01-noauth-response.json`. Les archives publiques permettent d’obtenir la classification sans clé API.

La documentation distingue la **Fondation**, multidimensionnelle et pouvant avoir plusieurs parents, de la **linéarisation MMS**, qui comporte les codes, les catégories résiduelles et un seul parent par entité. Les endpoints MMS sont à utiliser pour la liste de codes. Les possibilités de déploiement local sont documentées dans `ICDAPI-LocalDeployment.html`, sans installation lancée durant cette tâche.

## Ce qui manque encore pour le système pédagogique I-03-Infectiologie

Le chapitre OMS 01 ne peut pas devenir automatiquement le dénominateur T1. Le début du PDF donne déjà des contre-exemples concrets : infection liée à un dispositif/implant/greffe non classée ailleurs **NE83.1** exclue ; infections du fœtus/nouveau-né **KA60–KA6Z**, maladies humaines à prions **8E00–8E0Z**, pneumonie **CA40** codées ailleurs. Ces références doivent faire l’objet d’une décision de rattachement pédagogique argumentée, pas d’une suppression du périmètre infectieux.

Réciproquement, l’export comprend des infections intestinales et hépatites que le catalogue MEDINA historique attache S03. Une classification MMS, la Fondation OMS et une organisation d’enseignement peuvent avoir des topologies différentes. Le choix final nécessite un inventaire global des entités pertinentes de l’export complet, la lecture des descriptions/inclusions/exclusions, leurs rattachements transversaux, puis les preuves d’un enseignement spécifique accessible et relu.

Suite interne faisable : conserver cette extraction comme **inventaire officiel candidat**, puis constituer la matrice définie dans `docs/COMPLETUDE_CIM11.md` : entité officielle/version/parent/source ; tous systèmes MEDINA justifiés ; passage spécifique (cours/onglet/ancre) ; particularités et sous-catégories ; lien réellement ouvert dans le fragment distribué ; rapport de relecture et SHA ; état distinct. Le nombre total d’entités attendues et tout pourcentage T1 restent `null`/non établis jusqu’à ce contrôle.

## État concurrent A41, sans confusion avec la clôture T1

Pendant la tâche, le coordinateur a signalé main `a5563238887df2a72da7a9f663bdae9ab01f4bc8`. Les blobs ont été lus : `ETAT.json` A41 est `injecte`, avec audit Claude `ba6a80fbbe901b52085f3b8f992e2e49fe592e4d`, verdict « favorable sous réserves mineures ». Les dix empreintes de l’état, des fichiers partagés et des sources canoniques concordent. Cette injection porte sur le **chapitre A41 selon l’ancien protocole**, et ne constitue pas le statut INJECTÉ du fragment entier imposé par le nouveau PDF. Aucun audit médical ni déploiement reproduit par ce relevé.

Les cinq fichiers de périmètre historique (registre des fragments, structure, chapitres, catalogue natif, règle CIM-11) restent identiques entre a6f82b6 et a556323. L’inventaire historique 155 catégories demeure une donnée CIM-10-GM, distincte des 1 025 catégories/sous-catégories du chapitre OMS. L’état concurrent est conservé sous `latest-a41-state-observation.json` et ajouté aux deux rapports historiques `/workspace/work/inventaire-i03.md` et `.json`.

## Limites du relevé

Téléchargement et provenance OMS vérifiés, parsing et conservation des lignes contrôlés ; pas de certification de périmètre MEDINA, pas de mapping automatique, pas de validation médicale, pas de mesure de couverture d’enseignement ni de publication.
