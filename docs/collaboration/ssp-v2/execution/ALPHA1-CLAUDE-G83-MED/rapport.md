# Audit médical ALPHA77 — G83 Autres syndromes paralytiques (S08, Neurologie)

**Mission** ALPHA1-CLAUDE-G83-MED · branche `claude/alpha1/g83-med-g1` · base `103745baaa38c76f18288758cc7f689e5091ccdb` (sources figées à `523832d9`) · audit du 16 octobre 2026.
Lecture intégrale des sept fichiers ; **empreintes SHA-256 conformes au manifeste** (7/7). Première source lue : S10, Katzouraki et coll., *Bone Joint J* 2020, résumé.

## Synthèse

La leçon est honnête : elle déclare ses lacunes au lieu de les combler de mémoire, et **aucun de ses 417 nombres calculables n’est faux**. Ses faiblesses sont ailleurs. Elle enseigne une thrombolyse « jusqu’à 24 heures » sans dire qu’elle sort de l’autorisation suisse, elle omet le plafond de 100 µg du test au baclofène intrathécal et elle présente le toucher rectal comme un complément utile alors que sa sensibilité est faible. Le sous-onglet de sémiologie exigé est absent, les sciences fondamentales échouent au contrôle automatique et deux figures anatomiques ont été dessinées par une intelligence artificielle.

| Gravité | Nombre |
|---|---|
| BLOQUANT | 0 |
| MAJEUR | 7 |
| MINEUR | 11 |
| ENRICHISSEMENT | 5 |

## Constats MAJEURS

1. **C01 — Sémiologie fondamentale et analytique absente.** Le panneau pS compte trois disciplines, sans `g83-s-semio`. Proposition complète en neuf sections (`propositions/G83_c_semio.html`), bloc clinique dans pA et huit fenêtres. Appliquée sur une copie, elle passe `test_v7.py --static` (OK).
2. **C02 — Thrombolyse « jusqu’à 24 heures » sans l’autorisation suisse.** La suggestion ESO/ESMINT (consensus) est exacte. Pourtant, l’information professionnelle d’Actilyse® (06/2025) et celle de Metalyse® 5000 U (05/2025) limitent l’AVC ischémique à 4,5 heures. La proposition confronte les deux et donne les doses recalculées : altéplase 0,9 mg/kg, au plus 90 mg (63,0 mg à 70 kg, dont 6,3 mg en bolus) ; ténectéplase par paliers de poids, au plus 25 mg.
3. **C03 — Baclofène intrathécal : la FI suisse est incomplètement reprise.** Il manque le plafond de 100 µg du test, le coma possible après 25 µg, la titration après implantation (double de la dose test sur 24 heures), les signes du sevrage et les interactions.
4. **C04 — Le toucher rectal est présenté comme un complément de l’évaluation.** Pourtant, la sensibilité du tonus anal va de 0,23 à 0,53 ; le tonus est diminué chez 35 % des patients avec compression et chez 31 % de ceux qui n’en ont pas ; le parcours britannique actuel ne le requiert plus pour ce seul but.
5. **C05 — Sciences fondamentales insuffisantes.** Il y a trois disciplines et 865 mots ; `audit_sciences.py` échoue (5 erreurs) ; la physiologie de la miction, mécanisme du signe décisif, n’est pas traitée.
6. **C06 et C07 — Figures 1 et 3 : anatomie dessinée par une IA.** Ces SVG sans source viennent du commit 71fdb467. Aucun original n’a pu être proposé, car Commons répondait HTTP 429.

## Constats MINEURS

| Id | Objet | Proposition |
|---|---|---|
| C08 | Le texte écrit que l’ESO « recommande » ; la source dit « suggère », par consensus. L’énoncé contre la reperfusion en cas de lésions ischémiques étendues est omis | G83_b_1, G83_d_1 |
| C09 | IRM « dans l’heure » (BASS) ; le parcours GIRFT de 2026 fixe 4 heures au plus après la demande ; la RMS parle d’« urgence immédiate » | G83_b_1 |
| C10 | « Au plus tard 48 heures » : l’épilogue contredit le piège du même îlot | G83_b_1 |
| C11 | Attributions fusionnées : 17 définitions (Fraser) et 212 articles (Lavy) ; séquelles tirées de Kumar via Kögl | G83_mineurs |
| C12 | Interprétations non sourcées : κ 0,34 « proche du hasard », 0,17 placé hors contexte, AUC « moyenne » | G83_mineurs |
| C13 | Série de 1986 : 85 + 52 = 137 et 89 + 46 + 3 = 138, alors que la série compte 139 cas (énoncé incomplet) | G83_b_1 |
| C14 | Le terme a été introduit par Plum et Posner en 1966, non en 1972 | G83_b_1 |
| C15 | La « série suisse » de 24 patients n’est pas suisse | G83_mineurs |
| C16 | Bloc médial (Morges) : la source déconseille les stéroïdes particulaires | G83_mineurs |
| C17 | « Scanner vésical » se confond avec la tomodensitométrie | G83_mineurs |
| C18 | Répartition des fichiers hors contrat (pA dans `_b`, pE et pS dans `_c`) | G83_mineurs |

## Enrichissements

- **C19** : distinguer la paralysie faciale centrale de la périphérique par le front épargné (Heckmann 2019, RMS 2023 et 2025).
- **C20** : décrire les types 1 à 3 de Tandon et Sankaran et la déclassification par GIRFT.
- **C21** : parésie de Todd (13,4 %, médiane de 173,5 s) et conduite ESO 2021, PICO 14.2.
- **C22** : spécificités suisses (LACUNE).
- **C23** : situations particulières (pédiatrie et insuffisance rénale d’après la FI du baclofène).

## Calculs (EXIGENCE_CALCULS)

| Relevés | Calculables | Recalculés | Corrects | Arrondis | Faux | Non vérifiables |
|---|---|---|---|---|---|---|
| 783 | 417 | 417 | 405 | 5 | 0 | 7 |

Les relevés se répartissent ainsi : 370 valeurs chiffrées, 62 quantités en lettres, 165 années, 37 dates, 70 rangs, 56 numérotations et 23 codes. Les scripts sont `calculs/inventaire.py` et `calculs/verifier.py` ; les sorties sont dans `inventaire.json` et `resultats.json`. Points saillants :

- Le tableau 2 × 2 de l’étude prospective a été reconstruit en nombres entiers (32, 2, 75, 151) : la prévalence vaut 13,08 % et la valeur prédictive négative recalculée 98,69 %. La cohérence affirmée par la leçon est confirmée.
- Le calcul confirme deux incohérences des sources : une spécificité de 65 % hors de l’intervalle publié (0,70–0,90) et un κ de 0,34 hors de son intervalle publié (0,27–0,31).
- Pour le baclofène, la série 25-50-75 µg compte 3 doses et 2 intervalles, soit au moins 48 heures ; elle reste sous le plafond de 100 µg.
- Les 7 occurrences non vérifiables viennent de la série de 1986 (C13). Les 5 arrondis sont acceptables : 14,5 %, « un malade sur cinq », « trois paliers » et κ.

## Matrice des 21 rubriques

| N° | Rubrique | Statut |
|---|---|---|
| 1 | Question clinique | couvert (g83-0) |
| 2 | Définition et CIM-10-GM | couvert (g83-1) |
| 3 | Classifications | partiel (C20) |
| 4 | Épidémiologie | partiel |
| 5 | Normal → pathologique | partiel (C05) |
| 6 | Étiologies | partiel |
| 7 | Anamnèse et symptômes | partiel |
| 8 | Examen clinique | partiel (C04, C01) |
| 9 | Drapeaux rouges | couvert (g83-5, g83-7) |
| 10 | Examens complémentaires | couvert (g83-e-1 à e-4) |
| 11 | Diagnostic différentiel | partiel (C19) |
| 12 | Prise en charge suisse | partiel (C02, C03) |
| 13 | Complications et pronostic | couvert |
| 14 | Suivi et prévention | partiel |
| 15 | Situations particulières | absent (C23) |
| 16 | Spécificités suisses | partiel (C15, C22) |
| 17 | Critères formels | couvert (g83-13) |
| 18 | Paramètres clés | couvert (à corriger : C02, C03, C09) |
| 19 | Sous-codes | couvert |
| 20 | Points d’examen fédéral | partiel (C19) |
| **21** | **Sémiologie fondamentale et analytique** | **absent (C01, MAJEUR)** |

### Rubrique 21 — grille SEM

Les critères SEM-01 à SEM-03 et SEM-05 à SEM-23 reçoivent « non » ou « non évaluable », faute de discipline. SEM-04 reçoit « oui », car `test_v7.py --static G83` est OK. SEM-24 reçoit « oui » : le statut affiche « revue IA, aucune validation médicale humaine ». Le détail figure dans `rapport.json`, clé `semiologie`.

## Figures

Sur 5 figures, 2 sont `ANATOMIQUE_IA` (C06, C07) et 3 `SCHEMA_NON_ANATOMIQUE`, recevables. Aucune n’est `IMAGE_SOURCEE`.

## Lacunes principales

- Aucune recommandation suisse ou européenne propre au syndrome de la queue de cheval n’existe dans les sources trouvées. La plupart des sources n’ont été lues qu’en résumé. Les encadrés de force de l’ESO/ESMINT n’ont pas été lus.
- Aucune source neuro-urologique n’a été lue. La sémiologie des monoparésies et de la diplégie brachiale n’a pas été trouvée.
- Les spécificités suisses n’ont pas été recherchées. Aucun original de figure n’a été obtenu. Les captures à 390 px n’ont pas été faites.

## Tableau de bord

| Élément | Valeur |
|---|---|
| Leçon | G83 — Autres syndromes paralytiques (S08 · N-05-Neurologie) |
| Fichiers lus | 7/7, empreintes conformes |
| Sources lues | 36 (`sources.json`), dont 7 suisses (S2, S3, S22, S27, S28, S35, S36) et 2 séries de cas suisses (S15, S16) |
| Constats | 0 bloquant, 7 majeurs, 11 mineurs, 5 enrichissements |
| Calculs | 417/417 recalculés, 0 faux |
| Propositions | 9 fichiers HTML, un script et sa sortie ; 30/30 ancres uniques ; application sur copie : test_v7 OK |
| Alertes | C02 (thrombolyse hors autorisation), C03 (plafond de 100 µg), C04 (toucher rectal), C01 (sémiologie) |

*Audit IA — revue distincte d'une validation médicale humaine ; aucune source canonique modifiée.*
