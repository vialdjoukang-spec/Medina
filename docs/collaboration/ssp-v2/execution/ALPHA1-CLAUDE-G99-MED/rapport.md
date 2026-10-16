# Audit médical Alpha — G99 — Autres affections du système nerveux au cours de maladies classées ailleurs (N-05-Neurologie)

Mission **ALPHA1-CLAUDE-G99-MED**, fragment S08, branche `claude/alpha1/g99-med-g1`, base `103745ba` (HEAD du worktree ; manifeste `523832d9`). Audit du 16 octobre 2026, conforme au manifeste. Les sept fichiers lus ont des empreintes SHA-256 **conformes** au manifeste. Première source lue : BfArM, ICD-10-GM 2024, bloc G90–G99 (S1).

> Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.

## Synthèse

| Gravité | Nombre |
|---|---|
| BLOQUANT | 0 |
| MAJEUR | 7 |
| MINEUR | 14 |
| ENRICHISSEMENT | 4 |

La leçon est exacte sur la plupart de ses chiffres : 386 des 406 grandeurs calculables sont confirmées par les sources, 8 sont des arrondis acceptables. Ses faiblesses sont ailleurs. Elle range à tort la neuropathie urémique sous G99. Elle présente douze pourcentages d’**accord d’experts** comme s’il s’agissait de fréquences, de performances diagnostiques ou d’efficacités. Elle propose les gabapentinoïdes chez le patient urémique sans la contre-indication suisse de la prégabaline. Elle ignore les trois traitements suisses de la polyneuropathie à transthyrétine. Enfin, elle n’a ni sémiologie dédiée ni sciences conformes au contrat, et deux de ses figures sont des dessins anatomiques produits par IA.

## Constats MAJEURS

1. **C01 — Sémiologie absente.** `#pS` compte quatre disciplines (`g99-s-anat`, `-histo`, `-physio`, `-bioch`) et aucune `g99-s-semio`. L’onglet 1 cite les signes sans technique ni valeur. *Proposition* : `propositions/G99_c_semio.html` (sept îlots, figure de raisonnement non anatomique, trois cas) et six fenêtres dans `propositions/G99_pop1_semio.html` (à verser dans `G99_pop1.html`).
2. **C02 — Périmètre CIM-10-GM.** La CIM-10-GM 2024 classe la neuropathie urémique en **G63.8*** et la polyneuropathie amyloïde en **G63.3*** ; G99.8* ne vise que la *paralysie* urémique, et G99.0* la neuropathie *autonome* amyloïde [S1][S2]. Aucun sous-code (G99.00 gastroparésie, G99.08, G99.1, G99.2 avec M47.0-†, M50.0†, M51.0†, C00–D48†, M47.-†, G99.8) n’est cité. *Proposition* : P01, P02 et `glossary_g99_ajouts.py`.
3. **C03 — Accords pris pour des valeurs.** « Nausées et vomissements (95 %) », « scintigraphie (98 %) et test respiratoire (95 %) valides », « D2 (86 %) », « 5-HT4 (85 %) », « cause (88 %) » : ce sont des taux d’accord du panel UEG/ESNM [S3]. Le lecteur y lit une fréquence ou une performance qui n’existe pas. Douze occurrences ont le verdict FAUX dans `calculs/resultats.json`. *Proposition* : P03 à P08.
4. **C04 — Gabapentinoïdes chez l’urémique.** L’information suisse interdit la prégabaline sous 30 mL/min et réduit sa dose de moitié entre 30 et 60 mL/min [S29]. La gabapentine se réduit à 150–300 mg/j sous 15 mL/min, puis à 200–300 mg après chaque dialyse [S30]. La neuropathie urémique est hors de leurs indications suisses. *Proposition* : P12.
5. **C05 — Traitements suisses de l’ATTRv-PN omis.** Onpattro (300 µg/kg IV toutes les 3 semaines, maximum 30 mg), Amvuttra (25 mg SC tous les 3 mois avec vitamine A) et Wainzua (45 mg SC par mois) sont autorisés pour les stades 1 et 2 [S26][S27][S28]. *Proposition* : P13 à P15 et `G99_pop2_attr.html`.
6. **C06 — Sciences sous le contrat.** `tests/audit_sciences.py` échoue avec 21 erreurs : disciplines de 147 à 176 mots, pas de figure en biochimie, aucun des quatre libellés exigés. *Proposition* : `G99_c_sciences.html` ; une fois appliquée sur copie, le contrôle passe.
7. **C07 — Figures anatomiques IA.** Les figures 3 (« Moelle comprimée ») et 4 (« Fibre nerveuse ») ont été dessinées par l’agent de rédaction (le rapport du cycle 41 le déclare) : classe `ANATOMIQUE_IA`. Elles sont remplacées par des chaînes causales sourcées. Aucun original n’a pu être validé (Commons HTTP 429 ; la figure du BMJ est reproduite avec permission d’un tiers).

## Constats MINEURS

| Id | Point | Proposition |
|---|---|---|
| C08 | « Mécanisme principal » de l’hyperkaliémie : la source parle de corrélation forte et demande des essais [S17] | P16–P19 |
| C09 | La discectomie antérieure avec cage vaut pour la hernie discale, pas pour toute MCD (88,5 % de voies postérieures dans une série) [S9][S11] | P20 |
| C10 | Tableau de conduite : « sinon au moins 12 mois » est ambigu ; la ligne « vasovagale unique hors conduite : apte » manque [S18] | P21–P22 |
| C11 | Midodrine : plafond de la FI (30 mg/j) omis à côté de « jusqu’à 15 mg/j » [S21] | P23–P24 |
| C12 | Fludrocortisone : 0,3 mg/j (ESC) > 0,2 mg/j (FI) ; limite de 0,05 mg/j en cas d’hypertension ; trois contre-indications manquantes [S22] | P26–P27 |
| C13 | Toronto : il faut deux tests **cardiovagaux** et l’exclusion des autres causes [S6] | P28–P30 |
| C14 | La rétention > 20 % à 4 h s’associe à une **moindre** intensité des symptômes à 48 semaines [S3] | P09–P11 |
| C15 | Les dates des FI sont extractibles (Gutron 03/2021, Florinef 03/2026, Motilium 06/2026, Paspertin 01/2020, Vyndaqel 04/2026) | P25 |
| C16 | Dompéridone : érythromycine et clarithromycine contre-indiquées, ainsi que l’occlusion et le phéochromocytome ; la midodrine inhibe le CYP2D6 et peut augmenter l’exposition au métoclopramide [S23][S21] | P31–P32 |
| C17 | « Au plus 10 battements » (Physiologie) contre « habituellement » (ESC) | P33 |
| C18 | Plan du cours : l’entrée de g99-12 est mal intitulée et g99-13 manque | P34 |
| C19 | PND et NIS sont développés par la source | P35–P36 |
| C20 | Trois figures ont pour seul nom accessible « Schéma » | P37–P39 |
| C21 | Cas récapitulatif : le critère diastolique (10 mmHg) est aussi atteint ; la fréquence debout manque | P40 |

## Enrichissements

E01 : histoire naturelle de la compression asymptomatique (8 % à un an, 22 % sur 44 mois) [S8]. E02 : pharmacodynamie tirée des FI (desglymidodrine ; dompéridone périphérique) [S21][S3]. E03 : groupement de Cook (≥ 3/5 → spécificité 99 %, RV+ 30,9) [S31]. E04 : définition de Toronto et prévalence jusqu’à 65 % [S6].

## Calculs

Script : `calculs/inventaire.py` → `calculs/inventaire.json` ; `calculs/verifier.py` → `calculs/resultats.json`.

| Relevés | Références bibliographiques exclues | Calculables | Recalculés | Corrects | Arrondis | Faux | Non vérifiables |
|---|---|---|---|---|---|---|---|
| 689 | 52 | 406 | 406 | 386 | 8 | 12 | 0 |

Les 12 FAUX correspondent tous à C03. Les recalculs clés sont les suivants. Le cas récapitulatif donne ΔPAS 25 et ΔPAD 10 mmHg ; le quiz 1 donne ΔPAS 22 et ΔPAD 5. Le rapport 108/183 vaut 59,02 %, la somme 32,4 + 15,8 vaut 48,2 % et le rapport 15/18 vaut 83,3 %. La midodrine passe de 7,5 à 30 mg/j au plus. Le métoclopramide est plafonné à min(30 mg ; 0,5 mg/kg) ; ce plafond donne 15 mg/j ou 7,5 mg/j après réduction rénale. Le QTc passe de 415,1 à 444,9 ms, soit +29,8 ms. Les enrichissements sont aussi recalculés : patisiran 21 mg pour 70 kg, probabilité post-test de Cook 94,4 %, hauteurs des barres de la figure 6.

## Rubrique 21 — Sémiologie fondamentale et analytique

Statut : **absente**, donc MAJEUR (C01). Sur la leçon actuelle, SEM-04 et SEM-24 sont « oui ». Tous les autres critères sont « non » ou « non évaluables » ; le détail figure dans `rapport.json`, clé `semiologie.grille_SEM`. Avec la proposition appliquée sur copie, `test_v7.py --static G99` affiche OK et `audit_sciences.py` affiche `passed`. Deux critères restent ouverts : SEM-22 et SEM-23, faute de captures réelles.

## Matrice des 20 rubriques

| # | Rubrique | Statut |
|---|---|---|
| 1 | Question clinique | couvert |
| 2 | Périmètre CIM-10-GM | partiel (C02) |
| 3 | Classifications | couvert |
| 4 | Épidémiologie | partiel |
| 5 | Normal → pathologique | partiel (C06) |
| 6 | Étiologies | couvert |
| 7 | Anamnèse | partiel (C03) |
| 8 | Examen clinique | partiel (C01) |
| 9 | Urgences | couvert |
| 10 | Examens complémentaires | partiel |
| 11 | Différentiel | partiel |
| 12 | Prise en charge suisse | partiel (C04, C05, C15) |
| 13 | Pronostic | couvert |
| 14 | Suivi, dépistage | partiel |
| 15 | Situations particulières | partiel |
| 16 | Spécificités suisses | partiel (C10) |
| 17 | Critères formels | couvert |
| 18 | Paramètres clés | couvert |
| 19 | Sous-codes | absent (C02) |
| 20 | Examen fédéral | couvert |

## Lacunes

Plusieurs points n’ont pas pu être vérifiés :

- aucune recommandation suisse propre au sujet n’a été trouvée ;
- l’ESC 2018 a été lu partiellement : instructions pratiques web et tableau de conduite non lus ;
- les valeurs de coupure des tests réflexes n’ont pas été lues ;
- les seuils scintigraphiques européens n’ont pas été trouvés ;
- la posologie des corticoïdes dans la compression médullaire métastatique n’a pas été sourcée ;
- aucun original anatomique n’a été validé, et aucune capture réelle n’a été prise ;
- l’inotersen n’a pas d’information professionnelle suisse trouvée ;
- l’AI et la Liste des spécialités n’ont pas été recherchées.

Plusieurs sources n’ont été lues qu’au résumé ou par sections (voir `sources.json`).

## Tableau de bord

| Élément | Valeur |
|---|---|
| Leçon | G99 — Autres affections du système nerveux au cours de maladies classées ailleurs (N-05-Neurologie) |
| Fichiers | 7 lus, empreintes conformes |
| Sources | 32 (`sources.json`), dont 10 informations professionnelles suisses datées |
| Contrôles de la leçon actuelle | `test_v7 --static` OK ; `audit_sciences` en échec (21 erreurs) |
| Propositions | 43 remplacements locaux à ancre unique, 1 discipline, 9 fenêtres, 12 clés de glossaire |
| Contrôles après application (copie) | `test_v7 --static` OK (15 896 mots, 46 fenêtres, 7 quiz) ; `audit_sciences` passed |
| Alertes | C02, C03, C04 et C05 touchent le codage, la lecture des preuves et la prescription |
