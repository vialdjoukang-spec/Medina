# Application des consignes — A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie)

État du 2026-10-08T15:02:58.374844+02:00 (Europe/Zurich). **État actualisé : tableau et liens propres contrevalidés indépendamment, deltaP2 contrevalidé, monographie Compendium après rendu effectivement lue.** Les sections de relevé initial plus bas conservent les constats avant adaptation. Aucun canonique ni Git modifié. Ce rapport ne renouvelle pas un audit médical exhaustif ni le contrôle réseau de toutes les URL.

## Ce qui est rempli

Les huit HTML comportent maintenant25 tableaux et70 fenêtres natives. Les tableaux rapprochent des colonnes cohérentes : diagnostic/critère, agent/code, organe/mécanisme/signe, norme/matrice, médicament/dose/limite. Le tableau de gaz et les biomarqueurs gardent la méthode et la population de référence. Aucun objectif arbitraire de longueur n’a été utilisé.

À la demande du coordonnateur, le §1.5 de A41_a.html est passé d’une énumération en deux paragraphes à un tableau code/agent, avec A41.5 explicitement groupe. L’exemple Mme R./A41.51+R57.2, les exclusions et le choc toxique sont inchangés, hors tableau. Le lien BfArM indique2024 sans certifier une facturation suisse2026. Empreinte proposée : `34a54b45c140cfb352add0adf9feed32c39fc34359f03fff0f58221256e650d1`.

Les huit fenêtres de A41_pop1.html reçues en attribution ont17 liens supplémentaires : sepsis3/sofa/ssc/cultures/sign-focal/source/lactate/atcd-immune. Les phrases cliniques restent identiques. Les captions distinguent la définition2016, ESE2024, la prise en charge2026, CHUVV13 et le protocoleIDSA2009. L’EAU est le texte actuel consulté08.10.2026, sans millésime annuel inventé. Le contrôle du foyer est bien l’énoncé24 dans les129 cartes officielles. Empreinte proposée : `cdb1671a68f9f87d78b468c57b958cf894ada46439cd05b29d2b3e2db2645cce`. Traces exactes avant/après et reconstruction d’identité dans PATHOLOGIE1.

Les quatre fenêtres scientifiques — PCT, CRP, gaz, lecture scientifique — ont déjà leurs liens vers les sources et leurs limites. La banque de justifications ajoute des fenêtres complémentaires à ses seules cibles ; elle ne fournit pas automatiquement les références des fenêtres natives.

## Ajustements transmis aux auteurs — relevé initial avant leurs deltas

| Fichier / fenêtre | Ajustement ciblé | Texte déjà lu et version |
| --- | --- | --- |
| A41_pop_pa / a41-pam | Ajouter accès aux cibles actuelles, conserver essais historiques | Surviving Sepsis Campaign2026,13/14 |
| A41_pop_pa / a41-remplissage | Ajouter accès au texte applicable | Même texte,10,43–47,49 |
| A41_pop_pa / a41-delai-atb | Ajouter liens aux énoncés d’initiation | Même texte,16–20 |
| A41_pop_pa / a41-desescalade | Ajouter liens de réévaluation/désescalade/durée | Même texte,35–37,39/40 |
| A41_pop_pa / a41-refractaire | Ajouter le lien au consensus cité, niveau résumé | Leone2026,PMID41874620 |
| A41_b, tableau support d’organes ligne108 | Libellés verts vers oxygene/sdra/mesures | Fenêtres existantes ; conserver les seuils et grades utiles |
| A41_d, tableaux lignes19/28/37 | Noms de médicaments verts vers les monographies existantes | Fenêtres existantes, sources de produit déjà identifiées |
| A41_pop2 / norad,hydro | Ajouter accès aux décisions2026 en conservant le texte de produit daté | Surviving Sepsis Campaign2026,53/79 |

Cette liste décrit le relevé au moment du rapport ; les auteurs seuls modifient leurs fichiers. Les plages numériques sont des cartes réellement lues, et non des substitutions des informations professionnelles. Aucune donnée Aldomet n’entre dans le chapitre. Pour les inotropes, la carte60 est pertinente ; la59 concerne le bleu de méthylène.

## Compendium : constat statique historique avant preuve du rendu

L’URL fournie `https://compendium.ch/product/931-aldomet-cpr-250-mg/mpro` retourne HTTP200 et une fiche produit allemande dans le HTML effectivement lu. Le lien FR correspondant retourne aussi HTTP200 (162450octets, SHA-256 `2a38d60d14b1fd6701cb6d7d9a35e90a5dc63ba417cf409d4ce70ec2329b873c`), avec une fiche française mais sans les sections Indications/Posologie/Contre-indications ni une date d’information professionnelle. La notice lue dit :

> Il n’existe à l’heure actuelle aucun contrat de collaboration rédactionnelle avec HCI Solutions SA pour ce produit. Nous vous renvoyons donc aux pages officielles de swissmedicinfo.ch et à la liste des spécialités de l’OFSP.

Le pied de site « v2.38.0.9 -10.09.2026 » n’est pas une date de monographie. Le coordonnateur rapporte une observation de Claude de la monographie après renduJS ; notre contrôle Playwright/Chromium du lien FR a réellement échoué sur `net::ERR_CERT_AUTHORITY_INVALID`, avec `ignore_https_errors=False`. Aucun contournement TLS ni code Claude exécuté. Les preuves se trouvent dans `/tmp/a41-compendium-rendered-result.json`, `/tmp/a41-compendium-fr-static.html` et `/tmp/a41-compendium-fr-static.txt`.

**Conclusion historique avant l’essai suivant :** fiche statique accessible, rendu de notre tentative bloqué par le magasin de confiance. Aucune monographie professionnelle ni date n’a été lue par cette tentative ; cela ne prouve pas l’inaccessibilité dans un profil correctement configuré. Le produit reste hors du chapitre, sans importation de dose, de norme ou de référence.

## Compendium : preuve actuelle après rendu — 2026-10-08T15:09:00.052938+02:00

**Monographie professionnelle effectivement accessible après rendu du lien FR correspondant.** Le contrôle Playwright reproduit par `route.fulfill` les réponses HTTPS obtenues par `urllib.urlopen` avec `ssl.create_default_context`, vérification du nom d’hôte et `CERT_REQUIRED`. Aucun certificat n’a été ignoré et aucun code entrant de Claude exécuté ; son helper a été lu entièrement avant cette vérification par un script propre.

Le texte rendu affiche « Information professionnelle approuvée par Swissmedic », les sections Composition, Indications/Possibilités d’emploi, Posologie/Mode d’emploi, Contre-indications et Mises en garde avec un contenu distinct de la table des matières. La section « Mise à jour de l’information » indique **Février2023**. La ligne séparée22091/20.04.2023 et le pied de site ne remplacent pas cette date de monographie.

- URL rendue : `https://compendium.ch/fr/product/931-aldomet-cpr-250-mg/mpro`.
- Corps professionnel chargé par le site : `https://compendium.ch/fr/product/monographie/22091`, HTTP200,61563octets, SHA-256 `4736ce9d00dc0bc1d69bd70386025a7ed3415452c2a1304e1e7314c674cd79dc`.
- Texte rendu :22827octets, SHA-256 `33d18c27e0df883ac66fe3a5402ed13b24778b5adc15a51260fa25cb5fc70da3`.
- Preuves et réponses primaires empreintées : `/tmp/a41-compendium-tls-verified-render/result.json`, `rendered_text.txt`, `rendered_html.html` et corps identifiés par leur SHA.

Deux ressources hors hôte Compendium (fédération externe et GoogleTagManager) ont été bloquées dans ce périmètre limité ; aucune erreur JavaScript de page n’a été reçue et les sections professionnelles se sont réellement affichées. Cela ne certifie pas toutes les fonctions du portail ni les autres produits. Aucun champ clinique, aucune dose ni aucune référence Aldomet ne sont importés dans le chapitre.

## Adaptations reçues et contrevalidées après le relevé initial

Les trois boutons du tableau support de A41_b et les cinq blocs de liens de A41_pop_pa ont été réellement contrelus. La suppression ciblée de ces seuls ajouts restitue tous les octets des fichiers médicalement déjà relus ; les cartes applicables2026 et les captions ont été vérifiées. Avis favorable au delta, aux empreintes :

- A41_b.html : `b3955084555b603f56f905cdaf54407f1c06603bde38dc80930776e5860c1ace`.
- A41_pop_pa.html : `6e80bc70610be83c8e17927fec8b9b885ca59867e5336da0c85b1b5e6116623f`.

La contrelecture indépendante de l’autre auteur confirme également notre tableauA et les17 lienspop1, aux empreintes34a54b45… et cdb1671a…. Ces avis ne valent pas clôture de la contrelecture Claude. Les demandes adressées aux autres auteurs restent suivies par leurs postes de revue ; leur évolution est relevée dans l’inventaireJSON, sans certification médicale nouvelle par cette passe.

## Limites et suite

Les primaires applicables ont été réellement lues aux niveaux et versions documentés dans le JSON : consensus Sepsis-3 et SOFA2016, recommandations officielles2026, ESE2024, fiche CHUV adulteV13, IDSA2009 et EAU actuelle. La classification BfArM est expressément2024. Une source ancienne applicable reste accessible ; son âge seul n’est pas une erreur. Aucun défaut médical nouveau n’est démontré par cette passe de présentation.

Les deux deltas propres et le deltaP2 ont reçu leur contrelecture indépendante. Les adaptations des autres auteurs demandent leur propre relecture, puis le gel des dix empreintes et le contrôle technique/navigateur. Les empreintes de justifications et pop2 ont évolué par d’autres auteurs pendant cette passe et sont relevées dans le JSON, sans nouvelle certification médicale de ces deltas.

## État final du périmètre éditorial ciblé — 2026-10-08T15:16:54.357408+02:00

Les trois derniers liens de A41_pop_pa (oxygène66–68, SDRA71/73/76, insuline92) ont reçu leur contrelecture indépendante. Aucune phrase clinique ou dose ne change ; suppression des seuls blocs ajoutés restitue la version déjà contrevalidée. Nouvelle empreinte : `f383ad214398215420af0474e35d53478a6688bbfea14721ff3c8c9bba1e560d`. Le lien2026carte56 est maintenant présent dans la fenêtre vasopressine de A41_pop2, à l’empreinte `e7093e7453ac0fbe9d63aee17094a8a25893e899ebdd8d5936b70ddc10fbedc0` ; la présence/caption est vérifiée statiquement, les autres contenus pharmacologiques restent au poste compétent. Les quatre demandes d’accès complémentaires sont donc appliquées.

La preuve Compendium et le script propre sont archivés durablement dans `/workspace/medina-env/reprise-a41/compendium`. Le manifeste `/workspace/medina-env/reprise-a41/compendium/ARCHIVAGE.json` conserve les empreintes, l’identité des copies et le lien entre caches historiques et chemins durables. Il distingue le script Python propre réellement exécuté et le JavaScript du site rendu par Chromium du helperClaude c68d96a, lu entièrement et jamais exécuté. TLS reste vérifié ; les historiques d’échec ou de fiche statique sont conservés distincts du rendu réussi. Aucun enrichissement clinique ni autre source du chapitre modifié.
