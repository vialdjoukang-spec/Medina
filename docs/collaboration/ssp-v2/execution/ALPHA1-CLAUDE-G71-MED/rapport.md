# Audit Alpha tour 1 — G71 — Affections musculaires primitives (N-05-Neurologie, S08)

**Mission** ALPHA1-CLAUDE-G71-MED · audit médical agressif avec enrichissement · génération 1 · branche `claude/alpha1/g71-med-g1`.
**Base de la mission** (manifeste) : `d1a488ad4f0031d7f2a4b47a0721e89a93475d77`. **Base du worktree** : `32416a2080e67537641040a81252dec0b3e6d137` ; START exécuté sur le premier main contenant l’approbation de la mission (PR #181). Sources figées identiques : empreintes SHA-256 conformes au manifeste.
**Exécutant** : sous-agent Claude Code (voir accusé issue 107) ; modèle et effort conformes au manifeste. **Début** : 16.10.2026, 05:55:18 UTC (relevé par `date -u`) ; **fin** : 2026-10-16T06:18:58Z (relevée par `date -u` juste avant le commit).

## Lecture
Les sept fichiers ont été lus en entier : `G71_a`, `G71_b`, `G71_c`, `G71_d`, `G71_pop1`, `G71_pop2` et `glossary/g71.py`. Leurs empreintes SHA-256 sont **conformes au manifeste**. Chaque ancre citée a été vérifiée par script : elle apparaît une seule fois dans son fichier.

La **première source lue** est suisse : le protocole Care-NMD-CH (Waldboth et coll., JMIR Res Protoc 2026), section « Setting and Participants », qui décrit les sept centres neuromusculaires de référence du pays.

Contrôles exécutés : `test_v7.py --static G71` affiche OK ; `tests/audit_sciences.py` **échoue** (C02) ; l’inventaire des figures trouve six figures, rendues ensuite dans Chromium à 390 px.

## Verdict d’ensemble
La leçon est riche et, sur ce que l’audit a pu confronter, **exacte**. Quinze groupes de faits sont conformes au texte intégral des consensus Duchenne et DM1, de la recommandation EFNS, de la CIM-10-GM et de la FI suisse d’AGAMREE®. Ils sont listés dans `rapport.json`, clé `verifications_conformes`.

Ses défauts tiennent à trois manques. Le premier est structurel : il n’existe **ni sixième sous-onglet de sémiologie** ni encadrés de corrélation conformes. Le deuxième est pharmacologique : la FI suisse impose des gestes que la leçon n’écrit pas, et deux statuts européens ont changé. Le troisième touche les figures : une anatomie dessinée par IA et deux schémas illisibles sur téléphone. L’audit ne relève **aucune erreur bloquante** au sens du protocole, c’est-à-dire aucune affirmation fausse et dangereuse.

## Constats par gravité

| Gravité | Nombre |
|---|---|
| BLOQUANT | 0 |
| MAJEUR | 9, dont C01, bloquant pour la clôture |
| MINEUR | 10 |
| ENRICHISSEMENT | 6 |

### MAJEUR
- **C01 — Sémiologie absente : MAJEUR, bloquant pour la clôture du cours et du lot (AGENTS.md).** `G71_c.html` compte **5 `data-s`** : `g71-s-anat`, `g71-s-histo`, `g71-s-physio`, `g71-s-bioch` et `g71-s-gen`. Les cinq disciplines réelles sont donc présentes, mais `g71-s-semio` manque. La discipline à ajouter, en première position, est « Sémiologie fondamentale et analytique ». La proposition se trouve dans `G71_c_semio.html`, `G71_a_semio_clinique.html`, `G71_pop1_semio.html` (à ajouter à `G71_pop1.html`) et `glossary_g71_ajouts.py`.
- **C02 — Sciences non conformes.** `audit_sciences.py` échoue. Quatre disciplines sur cinq comptent moins de 280 mots, et aucune ne porte les libellés « Science → clinique / examen / traitement » ni « À retenir ». La proposition est `G71_c_2.html`.
- **C03 — Vamorolone et stress.** La FI suisse exige d’**ajouter de l’hydrocortisone systémique** en phase de stress, car le vamorolone seul est déconseillé : il est antagoniste minéralocorticoïde. Elle exige aussi une décroissance par paliers d’environ 20 % [S6]. La proposition est `G71_b_1.html`.
- **C04 — Suxaméthonium.** La FI suisse le **contre-indique** dans les maladies myotoniques, y compris la myotonie congénitale. Elle le contre-indique aussi dans les myopathies comme la Duchenne et en cas d’antécédent d’hyperthermie maligne, et le déconseille avant 12 ans [S7]. La proposition est `G71_b_2.html`.
- **C05 — Épisode pseudo-vasculaire du MELAS.** Antiplaquettaires et thrombolyse **ne sont pas indiqués**, et des corticoïdes intraveineux se discutent au cas par cas. Le consensus est en outre lisible en texte intégral [S10]. La proposition est `G71_b_3.html`.
- **C06 — Ataluren.** L’autorisation européenne a **expiré le 28.03.2025** sans renouvellement, faute d’efficacité confirmée [S11]. La leçon le présente encore comme une option thérapeutique. La proposition est `G71_d_1.html`.
- **C07 — Emplois hors indication non signalés.** Le modafinil n’est autorisé en Suisse que dans la narcolepsie [S8]. La lamotrigine est un antiépileptique [S25]. L’indication européenne de la mexilétine se limite à la myotonie **non dystrophique** de l’adulte [S13]. La proposition est `G71_d_1.html`.
- **C08 — Figure 2 `ANATOMIQUE_IA`.** C’est une silhouette humaine en SVG, introduite par le commit `71fdb467` (auteur Claude, injection Betta), sans aucune source iconographique. Son texte est rendu à 7,3 px à 390 px. La proposition `G71_c_figures.html` retire la figure et la remplace provisoirement par un tableau.
- **C09 — Figure 6 illisible.** À 390 px, les seuils CTG 35 et 50 sont rendus à 7,3 px. La figure recomposée se trouve dans `G71_c_figures.html`.

### MINEUR
- **C10** : dès 40 kg, la FI indique 240 mg (6 ml) une fois par jour, alors que la leçon écrit « dose maximale tolérée » [S6].
- **C11** : l’association du vamorolone avec la spironolactone ou l’éplérénone impose un contrôle du potassium à un mois. Les inducteurs du CYP3A4 réduisent son efficacité [S6].
- **C12** : la figure 5 est illisible à 7,3 px, sans valeur décisionnelle.
- **C13** : le glossaire développe ENMC en « Neuromuscular Muscle Centre » ; le sigle signifie *European Neuromuscular Centre* [S24].
- **C19** : la CIM-10-GM écrit « Duchenne- oder Becker-ähnlich », non « de type » [S9].
- **C20** : l’EFNS dit que la biopsie « peut » être faite, non qu’elle « est justifiée » [S5].
- **C21** : « bisannuel » est ambigu ; la source dit *annual or biennial* [S4].
- **C22** : la CVF prédite se calcule d’après l’envergure ou l’ulna [S2].
- **C24** : la limite « seul l’abstract a été lu » est caduque pour le MELAS [S10].
- **C25** : le seuil CK > 1000 U/L, les mollets et la GGT normale sont absents du texte intégral de Birnkrant partie 1, à laquelle la leçon les attribue.

### ENRICHISSEMENTS (propositions prêtes à intégrer)

| Id | Fichier | Apport | Proposition |
|---|---|---|---|
| C14 | G71_b | Sept centres suisses de référence, Swiss-Reg-NMD, filière CHUV-HUG | G71_b_4.html |
| C15 | G71_d | Givinostat : autorisation conditionnelle de l’UE du 06.06.2025 | G71_d_1.html |
| C16 | G71_a | Suisse : LAMA2 ≥ 0,8/100 000 ; dysferlinopathie fondatrice | G71_a_1.html |
| C17 | G71_a | Définition ENMC 2026 des myopathies congénitales, écart avec G71.2 | G71_a_2.html |
| C18 | G71_a | Définition ENMC 2025 des myopathies mitochondriales primaires | G71_a_2.html |
| C23 | G71_b | Losmapimod : essai de phase 3 REACH négatif | G71_mineurs.html |

## Figures (règle de Vial du 15.10.2026 ; addendum lot 2, point 2)

| Figure | Classe | Preuve | Lisibilité à 390 px |
|---|---|---|---|
| 1 (G71_a) | SCHEMA_NON_ANATOMIQUE | Chaîne causale en boîtes | 11,1 px, lisible |
| 2 (G71_c, anatomie) | **ANATOMIQUE_IA** | SVG sans source ; commit 71fdb467 (auteur Claude) | 7,3 px (C08) |
| 3 (G71_c, histologie) | SCHEMA_NON_ANATOMIQUE | Histogramme | 11,1 px |
| 4 (G71_c, physiologie) | SCHEMA_NON_ANATOMIQUE | Courbe qualitative | 11,1 px |
| 5 (G71_c, biochimie) | SCHEMA_NON_ANATOMIQUE | Boîtes | 7,3 px (C12) |
| 6 (G71_c, génétique) | SCHEMA_NON_ANATOMIQUE | Axe de seuils | 7,3 px, seuils décisionnels (C09) |

Aucun candidat de remplacement n’est proposé pour la figure 2. Commons a répondu HTTP 429 et aucun nouvel essai n’a été tenté. Europe PMC n’a fourni aucune figure exploitable vérifiée. Aucune image n’a été générée.

## 21 — Sémiologie fondamentale et analytique

**Statut : absente comme discipline.** Le constat **C01** est **MAJEUR et bloquant pour la clôture**. Décompte des `data-s` : 5 ; `g71-s-semio` est absent.

- **Sémiologie fondamentale** : elle est partielle et dispersée dans l’onglet 1 (îlots `g71-5` et `g71-6`, fenêtres `g71-gowers` et `g71-fshd`). Il lui manque la définition, le normal, la technique, le mécanisme, la valeur et le piège de chaque signe.
- **Sémiologie analytique** : elle est absente. Il n’y a ni regroupement syndromique, ni raisonnement en cinq étapes, ni examen systématique, ni cas corrigés.
- **LACUNE** : aucune sensibilité, spécificité ni rapport de vraisemblance n’a été trouvé dans les sources lues pour le signe de Gowers, la myotonie de préhension, la cotation MRC ou les symptômes d’hypoventilation. La proposition l’écrit explicitement et n’invente aucun chiffre.

| N° | Critère | Résultat (leçon actuelle) |
|---|---|---|
| SEM-01 | Bouton `g71-s-semio` en première position et `div.sci` | **non** (bloquant) |
| SEM-02 | Premier `h2` avec la formule exigée | **non** (bloquant) |
| SEM-03 | `audit_sciences.py` satisfait | **non** (bloquant ; voir aussi C02) |
| SEM-04 | `test_v7.py --static G71` OK | oui |
| SEM-05 | Tableau des symptômes | non |
| SEM-06 | Technique de chaque signe | non |
| SEM-07 | Mécanisme de chaque signe | non |
| SEM-08 | Valeurs chiffrées sourcées ou LACUNE | **non** (bloquant) |
| SEM-09 | Normal avant pathologique | non |
| SEM-10 | Piège par signe majeur | non |
| SEM-11 | Tableau des syndromes | non |
| SEM-12 | Raisonnement en cinq étapes | non |
| SEM-13 | `alert` sémiologique cohérente avec l’onglet 1 | **non** (bloquant) |
| SEM-14 | Discriminant sourcé par différentiel | non |
| SEM-15 | Examen systématique numéroté | non |
| SEM-16 | Synthèse en `div.card` | non |
| SEM-17 | Trois cas corrigés | non |
| SEM-18 | Fenêtres réelles des mots verts | non |
| SEM-19 | Sources suisses puis européennes | non évaluable (**bloquant** tant que la discipline manque) |
| SEM-20 | Cohérence des chiffres | non évaluable |
| SEM-21 | Pas de redite de l’onglet 1 | non évaluable |
| SEM-22 | Libellé lisible à 390 px | non |
| SEM-23 | Deux captures réelles | non |
| SEM-24 | Statut « revue IA » | oui |

La proposition `G71_c_semio.html` respecte le contrat `SEMIOLOGIE_FONDAMENTALE_ANALYTIQUE_2026-10-15.yaml` : un bouton `g71-tab-semio` en première position (`aria-selected="true"`, les cinq autres à `false`), un panneau `g71-s-semio` (`role="tabpanel"`, `aria-labelledby`, visible) et neuf sections `data-semiology`, de `g71-sm-1` à `g71-sm-9`, dans l’ordre normal, signs, mechanisms, examination, interpretation, differentials, urgency, limits, sources, toutes titrées en `h3`. L’`alert` reste cohérente avec l’îlot `g71-8`. Elle comprend une figure non anatomique dont le texte est rendu à 11,9 px à 390 px et trois quiz, dont un sur la formulation honnête d’une limite. La section `sources` relie chaque affirmation au passage lu, avec un lien `https` par source. Le marqueur clinique `data-semiology-clinical="G71"` est proposé dans `G71_a_semio_clinique.html` (pA, îlot `g71-6`). Elle n’utilise que des classes de la liste fermée, sans style en ligne, et chaque affirmation porte une source lue. Elle n’affaiblit aucune obligation clinique de la leçon.

## Matrice des 20 rubriques (leçon actuelle)

| # | Rubrique | Statut | Ancre |
|---|---|---|---|
| 1 | Question clinique | couvert | g71-0 |
| 2 | Définition, CIM-10-GM | couvert | g71-1, g71-sousgroupes (C17, C19) |
| 3 | Classifications | partiel | g71-1 (C17, C18) |
| 4 | Épidémiologie suisse puis européenne | partiel | g71-2 (C16) |
| 5 | Normal → pathologique | couvert | g71-3, g71-s-* |
| 6 | Étiologies et facteurs de risque | couvert | g71-4 |
| 7 | Anamnèse et symptômes | partiel | g71-5 |
| 8 | Examen clinique | partiel | g71-6 (C01) |
| 9 | Drapeaux rouges | partiel | g71-8 (C03, C04, C05) |
| 10 | Examens complémentaires | couvert | e-1 à e-7 |
| 11 | Diagnostic différentiel | partiel | g71-7.1 |
| 12 | Prise en charge suisse | partiel | g71-9, G71_d (C06, C07, C14) |
| 13 | Complications et pronostic | couvert | g71-8, g71-10 |
| 14 | Suivi, prévention, dépistage | couvert | g71-10, g71-11 |
| 15 | Situations particulières | partiel | g71-11 |
| 16 | Spécificités suisses | absent | — (lacune) |
| 17 | Critères formels | couvert | g71-12 alert |
| 18 | Paramètres clés | couvert | g71-12 key |
| 19 | Sous-codes CIM-10-GM | couvert | g71-sousgroupes |
| 20 | Points d’examen fédéral | partiel | quiz ; aucun objectif SSP cité |

## Lacunes principales
- Aucune recommandation clinique suisse spécifique n’a été trouvée. Le texte intégral de la *Revue Médicale Suisse* 2022 n’était pas accessible ; seul son résumé a été lu.
- Plusieurs ateliers ENMC restent inaccessibles : le 229e (LGMD), le 259e (anesthésie), le 263e (conductrices) et le 268e (FSHD). L’ESC 2022 n’a été lue qu’en partie, et l’ESC 2021 sur la stimulation n’a pas été lue.
- Le statut suisse de la mexilétine, du givinostat, du déflazacort et de l’ataluren n’a pas été trouvé. Les FI de la lamotrigine, du dantrolène et de l’hydrocortisone n’ont pas été lues en texte.
- Aucune source n’a été lue sur la transmission de la DM2 et de la FSHD, ni sur les spécificités suisses (AI, conduite, remboursement).
- Aucune valeur chiffrée n’a été trouvée pour les signes sémiologiques.

## Correctifs de contrat (revue Codex)

- Sémiologie : `G71_c_semio.html` restructurée selon le validateur (`id`, `role`, `aria-*`, neuf `data-semiology`, aucun `h2`) ; fond inchangé, l’affirmation sur la CK sous statine, sans passage consigné, est retirée.
- Marqueur clinique : nouvelle proposition `G71_a_semio_clinique.html` (`data-semiology-clinical="G71"`, pA).
- Fichiers admis : `G71_pop3.html` renommée `G71_pop1_semio.html`, cible `G71_pop1.html` ; aucune clé orpheline.
- `sources.json` : version, section ou page, passage paraphrasé, population, limites et niveau de lecture pour les 26 sources ; inconnues déclarées.
- Constats C01 à C09 conservés tels quels ; seule la référence de fichier de C01 change.

## Tableau de bord

| Élément | Valeur |
|---|---|
| Cours | G71 — Affections musculaires primitives (N-05-Neurologie, S08) |
| Sous-catégories | G71.0, G71.1, G71.2, G71.3, G71.8, G71.9 |
| Système | Neurologie (S08) |
| Empreintes | 7/7 conformes au manifeste |
| Constats | 0 bloquant · 9 majeurs (C01 bloquant pour la clôture) · 10 mineurs · 6 enrichissements |
| Sources lues | 26 (`sources.json`) : 9 suisses (4 fiches AIPS, Revue Médicale Suisse, Care-NMD-CH, Swiss-Reg-NMD ×2, centres de Bâle, Lausanne et Zurich), 13 européennes, 4 internationales |
| Propositions | 14 fichiers dans `propositions/` |
| Figures | 6 : 1 ANATOMIQUE_IA, 5 schémas non anatomiques (3 illisibles à 390 px) |
| Alertes | Sémiologie absente (bloquante) ; `audit_sciences` en échec ; FI suisse incomplètement reprise (vamorolone, suxaméthonium) ; ataluren expiré |

*Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.*
