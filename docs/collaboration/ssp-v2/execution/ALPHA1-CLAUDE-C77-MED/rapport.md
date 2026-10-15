# Audit médical Alpha, tour 1 — C77 Tumeur maligne des ganglions lymphatiques, secondaire et non précisée (S06 Hématologie)

**Mission** ALPHA1-CLAUDE-C77-MED · **Branche** `claude/alpha1/c77-med-g1` · **Base** `f664dd9e8da71f647dd3dc4da18f509f8517959c` · **Génération** 1 · **Conversation** alpha1-claude-c77-med · **Exécutant** sous-agent Claude Code (voir accusé issue 107) · **Modèle et effort** conformes au manifeste · **Date** 15 octobre 2026.

## 1. Lecture et intégrité

J’ai lu en entier les sept fichiers de la leçon : les onglets `C77_a` à `C77_d`, les fenêtres `C77_pop1` et `C77_pop2` et le glossaire `glossary/c77.py`. Leurs empreintes SHA-256, recalculées au commit de base, sont **identiques** à celles du manifeste (instantané `bfc4576`). Aucune source canonique n’a été modifiée.

La première source lue est l’information professionnelle suisse du **carboplatine (Sandoz®)**, mise à jour en février 2026. Je l’ai obtenue par `tools/swissmedic_fi.py` (GTIN 7680548290014), rubriques « Indications » puis « Posologie ». J’ai ensuite lu en texte intégral la FI du paclitaxel (Accord®, novembre 2023), la revue suisse de Hanzalová et Matter (*Swiss Medical Weekly* 2024) et la ligne directrice Onkopedia CUP de septembre 2025. J’ai lu une section de la CIM-10-GM 2024 (BfArM), de la revue mécanistique de Liu (2023) et des pages de l’OFSP et de l’ONEC sur la loi sur l’enregistrement des maladies oncologiques (LEMO). La ligne directrice ESMO 2023 n’a été lue qu’à travers ses métadonnées et le résumé de Bochtler : son texte intégral reste inaccessible.

## 2. Jugement d’ensemble

La leçon est solide sur la nosologie, la démarche topographique, l’immunohistochimie et la séquence « tissu avant bistouri ». Les chiffres de la revue suisse et d’Onkopedia sont, pour la plupart, repris fidèlement. Je n’ai trouvé **aucune erreur bloquante**. En revanche, une figure anatomique générée pour le cours est non recevable. Les faiblesses se concentrent sur trois terrains : la **pharmacologie**, où les contre-indications et les interactions sont tronquées alors que les FI suisses les donnent ; le **bilan du CUP**, où l’exigence d’une histologie et de l’IRM mammaire manque ; et plusieurs **attributions de sources** inexactes.

## 3. Constats majeurs (9)

| Id | Fichier | Constat | Proposition |
|---|---|---|---|
| MAJ-01 | C77_d | Contre-indications du carboplatine incomplètes : manquent l’hypersensibilité au platine, l’insuffisance hépatique grave, les troubles auditifs majeurs et l’allaitement (FI, février 2026). | `propositions/C77_d_1.html` |
| MAJ-02 | C77_d | Le cours affirme que les interactions ne figurent pas dans les sources. Les deux FI les détaillent : aminosides, diurétiques de l’anse, vaccins vivants, myélosuppresseurs ; modulateurs du CYP2C8/3A4 ; paclitaxel toujours avant le cisplatine. | `propositions/C77_d_2.html` |
| MAJ-03 | C77_d | Contre-indications du paclitaxel réduites à la neutropénie : manquent l’hypersensibilité sévère, la grossesse et l’allaitement. | `propositions/C77_d_1.html` |
| MAJ-04 | C77_d, pop2 | Le schéma carboplatine AUC 2 et paclitaxel 50 mg/m² hebdomadaire est rattaché à tort au CUP cervical N3. Onkopedia le cite comme exemple de radiochimiothérapie du CUP épidermoïde (§ 5.1.3.2). | `propositions/C77_d_3.html` |
| MAJ-05 | C77_b | Le cours présente la cytoponction comme équivalente au trocart dans le bilan du CUP. Onkopedia exige une **histologie**, et pas seulement une cytologie, avec assez de matériel pour l’immunohistochimie et la biologie moléculaire. | `propositions/C77_b_1.html` |
| MAJ-06 | C77_b | Le cas récapitulatif retient un CUP axillaire « sein-like » **sans IRM mammaire**, que la ligne directrice prévoit (avec une scintigraphie osseuse). | `propositions/C77_b_2.html` |
| MAJ-07 | C77_b, C77_a | Critère post-vaccinal incomplet : la bénignité ne vaut que pour une adénopathie **unilatérale** non suspecte. Une adénopathie controlatérale ou persistante au-delà de 12 semaines relève du bilan standard. Le cours écrit aussi « environ 1 %, axillaire », ce qui déforme la source. | `propositions/C77_b_3.html` |
| MAJ-08 | C77_a | La ligne sus-claviculaire omet le **sein** (environ 30 % selon Onkopedia), ainsi que le PSA et le toucher rectal chez l’homme. | `propositions/C77_a_1.html` |
| MAJ-09 | C77_c | La Figure 1 est un schéma anatomique dessiné pour le cours (silhouette et régions ganglionnaires), sans source iconographique. Elle est **non recevable** selon la règle de Vial du 15.10.2026 (voir section Figures). | `propositions/C77_c_figure1.html` |

## 4. Constats mineurs (12)

- **MIN-01** — Contresens : « 15 à 25 % des CUP localisés sont favorables ». La source dit que 15 à 25 % des CUP sont **localisés** et que 70 à 85 % n’appartiennent à aucun sous-groupe favorable.
- **MIN-02** — Le seuil de soins palliatifs seuls (espérance de vie inférieure à 4 mois) est attribué à Onkopedia. Il provient de la revue suisse, qui cite l’ESMO 2015.
- **MIN-03** — Deux études sont fusionnées dans le chiffre du TEP-CT : 36 % de détection dans une série cervicale, 45,8 % de changement thérapeutique sur l’ensemble des CUP.
- **MIN-04** — L’écart de survie de 57 % contre 82 % a un sens connu : 57 % avec extension extracapsulaire, 82 % sans.
- **MIN-05** — Pour le N2 cervical, l’option de radiothérapie définitive est omise. Les facteurs de risque qui imposent la radiochimiothérapie ne sont pas définis.
- **MIN-06** — Le nadir du carboplatine en association (15 jours) et ses critères de reprise sont absents.
- **MIN-07** — Le cours dit que la prévention n’est pas traitée dans les sources. Onkopedia affirme pourtant qu’aucune mesure spécifique n’existe.
- **MIN-08** — La liste des médicaments responsables d’adénopathie omet les sels d’or.
- **MIN-09** — L’essaimage de 7 % est présenté sans la nuance de la même source : la survie n’est pas aggravée dans deux séries ORL.
- **MIN-10** — La tolérance immunitaire du ganglion colonisé, observée dans un modèle murin, est présentée comme une explication clinique établie.
- **MIN-12** — La Figure 4 et le tableau CK7/CK20 omettent le tractus digestif haut et pancréatobiliaire, ainsi que les glandes salivaires.
- **MIN-11** — Les indications suisses du carboplatine sont résumées de façon imprécise : tumeurs ORL en monothérapie avec radiothérapie ou en association ; vessie en association.

## 5. Enrichissements proposés (11)

Les propositions sont prêtes à intégrer et sourcées `[Sx]` dans `propositions/`.

- **Seuils de taille** de l’adénopathie : plus de 1 cm de petit axe ; 1,5 cm pour le ganglion jugulo-digastrique ; 5 mm pour le ganglion épitrochléen (ENR-01).
- **Facteurs pronostiques** du CUP : état général, CRP, neutrophiles, albumine, LDH, métastases hépatiques (ENR-02).
- **Facteurs de risque** du CUP : tabac, avec un rapport de risque de 1,7 à 3,7 (ENR-03).
- **Compression médullaire**, urgence oncologique du CUP métastatique (ENR-04).
- **LEMO** : déclaration obligatoire du diagnostic confirmé au registre cantonal sous quatre semaines, information du patient et droit d’opposition (ENR-05). C’est la seule spécificité suisse ; elle était absente.
- **CUP cervical** : 3 à 5 % des tumeurs ORL ; HPV positif, avec un primitif oropharyngé dans 80 à plus de 90 % des cas (ENR-06).
- **TMB élevée** à partir de 10 mutations par mégabase ; essai CUPISCO (ENR-07).
- **Doses et seuils** issus des FI : paclitaxel 175 mg/m² toutes les 3 semaines, plaquettes, foie ; carboplatine : rein, mécanisme, ototoxicité (ENR-08).
- **Bilan inguinal** (ENR-09), **bilan biologique de base** (ENR-10) et inutilité de l’**antibiothérapie empirique** (ENR-11).

## 6. Figures

L’inventaire porte sur les sept fichiers. Il ne trouve aucune balise `img` ni `canvas` et aucun dessin CSS. On compte 4 figures SVG et 4 icônes d’interface, toutes dans `C77_c.html`.

| Figure | Ancre | Classe | Vérification | Constat |
|---|---|---|---|---|
| Figure 1 — Drainage ganglionnaire par région | `aria-label="Schéma du drainage ganglionnaire par région"` | **ANATOMIQUE_IA** | Silhouette et territoires dessinés pour le cours ; la légende cite la source du texte, pas une source iconographique. Le sein manque à la région sus-claviculaire. | MAJ-09 : non recevable, à remplacer |
| Figure 2 — Trajet de la lymphe | `aria-label="Trajet de la lymphe"` | SCHEMA_NON_ANATOMIQUE | Boîtes et flèches, sans forme anatomique dessinée. Les quatre étapes concordent avec Liu 2023. | Recevable |
| Figure 3 — Chaîne de la dissémination | `aria-label="Chaîne de la dissémination lymphatique"` | SCHEMA_NON_ANATOMIQUE | Conforme à Liu 2023 ; la tolérance immunitaire provient d’un modèle murin. | Recevable, voir MIN-10 |
| Figure 4 — Quadrants CK7/CK20 | `aria-label="Quadrants CK7 et CK20"` | SCHEMA_NON_ANATOMIQUE | Placement des quadrants exact (Onkopedia, Tabelle 2) ; contenu incomplet. | Recevable, voir MIN-12 |
| Icônes de la barre des sciences (×4) | `svg viewBox="0 0 24 24"` | SCHEMA_NON_ANATOMIQUE (interface) | Il s’agit d’icônes de boutons, sans contenu médical. | Hors périmètre |

**Candidats réels pour remplacer la Figure 1.** Je les ai identifiés avant la consigne d’usage exclusif du moteur commun Image_Clo_finder. J’ai lu leurs métadonnées par environ neuf requêtes unitaires à l’API officielle de Wikimedia Commons, sans boucle, après deux refus HTTP 429 par curl. Aucune image n’a été téléchargée, générée ni redessinée. Ces candidats **restent à revalider par Image_Clo_finder** lorsque Commons sera rétabli. Les recherches suivantes sont passées uniquement par le moteur commun : « lymph node regions » (Commons était suspendu par le disjoncteur ; Europe PMC n’a renvoyé que des courbes de survie hors sujet), puis « neck lymph node levels anatomy diagram » et « cervical lymph node levels » (Europe PMC et Open-i : aucun candidat retenu, 23 résultats exclus pour suspicion d’IA ou licence). **Lacune** : aucun candidat Europe PMC ou Open-i n’a été validé.

1. **« Lymph node regions.svg »** — programme SEER du National Cancer Institute, œuvre dérivée de Fred the Oyster, **domaine public**. Page : https://commons.wikimedia.org/wiki/File:Lymph_node_regions.svg ; fichier : https://upload.wikimedia.org/wikipedia/commons/c/cb/Lymph_node_regions.svg. C’est le candidat principal, intégré dans `propositions/C77_c_figure1.html`.
2. **« Blausen 0623 LymphaticSystem Female.png »** — BruceBlaus (Blausen Medical), **CC BY 3.0**. Attribution : Blausen.com staff (2014), WikiJournal of Medicine, DOI 10.15347/wjm/2014.010. Page : https://commons.wikimedia.org/wiki/File:Blausen_0623_LymphaticSystem_Female.png.
3. **« Diagram showing the areas of lymph nodes in the head and neck CRUK 292.svg »** — Cancer Research UK, **CC BY-SA 4.0**. Ce candidat couvre la région cervicale seulement. Page : https://commons.wikimedia.org/wiki/File:Diagram_showing_the_areas_of_lymph_nodes_in_the_head_and_neck_CRUK_292.svg.

## 7. Matrice des 20 rubriques (leçon telle qu’elle est)

| Rubrique | Statut | Localisation ou manque |
|---|---|---|
| 1 Question clinique | couvert | c77-0 |
| 2 Définition et CIM-10-GM | couvert | c77-1, c77-codage (conforme au BfArM 2024) |
| 3 Classifications et stades | partiel | sous-groupes, N1–N3 ; facteurs de risque N3 absents |
| 4 Épidémiologie | partiel | aucune donnée suisse (lacune confirmée) |
| 5 Normal → pathologique | couvert | c77-3, sciences |
| 6 Étiologies et facteurs de risque | partiel | facteurs de risque du CUP absents |
| 7 Anamnèse | couvert | c77-5 |
| 8 Examen clinique | partiel | seuils de taille, examen gynécologique |
| 9 Drapeaux rouges et urgences | partiel | compression médullaire |
| 10 Examens complémentaires | partiel | histologie obligatoire, IRM mammaire |
| 11 Diagnostic différentiel | couvert | c77-7, c77-diffdx |
| 12 Prise en charge suisse | partiel | FI incomplètes, attribution N3 |
| 13 Complications et pronostic | partiel | facteurs pronostiques |
| 14 Suivi, prévention | partiel | prévention déclarée à tort non traitée |
| 15 Situations particulières | partiel | grossesse/allaitement du paclitaxel, foie |
| 16 Spécificités suisses | **absent** | LEMO, remboursement du TEP |
| 17 Critères formels | couvert | c77-12 `div.alert` |
| 18 Paramètres clés | couvert | c77-12 `div.key` |
| 19 Sous-codes | couvert | c77-codage, glossaire |
| 20 Points d’examen fédéral | partiel | quiz présents ; PROFILES non vérifié |

## 8. Lacunes de l’audit

- Le texte intégral de l’ESMO 2023 est inaccessible : HTTP 403 et aucun texte PMC.
- Aucune incidence suisse du CUP ni de C77 n’a été trouvée.
- Le remboursement du TEP-CT selon l’OPAS n’a pas été vérifié.
- Les FI du cisplatine, de la gemcitabine, de l’atézolizumab et du pembrolizumab n’ont pas été lues.
- La règle suisse de codage C77.x avec C80.0 n’a pas été vérifiée. La fenêtre c77-codage laisse entendre que C80.0 remplace C77.
- La ligne directrice EHNS-ESMO-ESTRO 2020 et les objectifs PROFILES n’ont pas été lus.

## 9. Tableau de bord

| Élément | Valeur |
|---|---|
| Leçon | C77 — Tumeur maligne des ganglions lymphatiques, secondaire et non précisée (S06-Hématologie) |
| Fichiers audités | 7, empreintes conformes |
| Sources lues | 11 (4 en texte intégral, 5 par section, 2 par résumé) |
| BLOQUANT | 0 |
| MAJEUR | 9 |
| MINEUR | 12 |
| ENRICHISSEMENT | 11 |
| Propositions rédigées | 15 fichiers HTML |
| Figures inventoriées | 4 figures et 4 icônes : 1 ANATOMIQUE_IA (non recevable), 3 schémas recevables, 0 image sourcée |
| Rubriques couvertes, partielles, absentes | 8 / 11 / 1 |
| Ancres vérifiées mécaniquement | 32 constats et 5 figures, toutes présentes dans les fichiers |

*Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.*
