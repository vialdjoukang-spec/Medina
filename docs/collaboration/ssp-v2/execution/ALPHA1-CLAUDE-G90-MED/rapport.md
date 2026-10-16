# Audit Alpha tour 1 — G90 — Affections du système nerveux autonome (N-05-Neurologie, S08)

Mission `ALPHA1-CLAUDE-G90-MED` · audit médical agressif avec enrichissement · branche `claude/alpha1/g90-med-g1` · base `103745ba` · instantané des sources `523832d9` · 16 octobre 2026.
Exécutant : sous-agent Claude Code (voir accusé issue 107), modèle et effort conformes au manifeste.

## Lecture

- Les sept fichiers ont été lus en entier : `G90_a.html`, `G90_b.html`, `G90_c.html` (onglets Examens et Sciences), `G90_d.html`, `G90_pop1.html`, `G90_pop2.html` et `glossary/g90.py`.
- Les empreintes SHA-256 ont été recalculées sur l’instantané `523832d9` : elles sont **conformes** au manifeste pour les sept fichiers.
- Lectures d’entrée : consigne de l’auditeur, protocole Alpha (section A), EXIGENCE_CALCULS, EXIGENCE_SEMIOLOGIE, contrat `SEMIOLOGIE_FONDAMENTALE_ANALYTIQUE_2026-10-15.yaml`, règle des figures anatomiques, instruction « Clarté, bases et calculs », PROMPT_VERITE et STYLE_REDACTION.
- Première source lue : information professionnelle suisse de MIDODRIN SUBSTIPHARM (mise à jour de mai 2024), rubriques « Posologie » et « Contre-indications », via `tools/swissmedic_fi.py`.
- Contrôles automatiques :
  - `test_v7.py --static G90` : **OK** (14 019 mots, 52 fenêtres, 8 quiz, 16 Pareto) ;
  - `tests/audit_sciences.py` : **en échec**, « À retenir. » absent des trois disciplines (C08).

## Verdict d’ensemble

La leçon est **solide sur ses définitions chiffrées**. Les seuils de l’hypotension orthostatique, les grades de l’hypertension de décubitus, les tests pharmacologiques du Horner, les critères de Budapest et la posologie suisse de la midodrine et de Florinef sont exacts et ont été recalculés. Le calcul principal de la vignette d’ouverture est juste (148 − 112 = 36 mmHg ; accélération de 3 par minute).

Six faiblesses restent **décisionnelles** :

- la **sémiologie fondamentale et analytique** est absente comme sous-onglet ;
- l’urgence de la **dysréflexie** omet la contre-indication des inhibiteurs de la phosphodiestérase de type 5 aux dérivés nitrés ;
- la même urgence fait de la bradycardie un critère, alors que la tachycardie est aussi fréquente ;
- les **contre-indications de la midodrine** sont incomplètes : grossesse, allaitement, phéochromocytome, hyperthyroïdie et glaucome à angle fermé manquent ;
- la **tachycardie posturale** n’a aucun critère chiffré ;
- le **massage sinocarotidien** est indiqué sans aucune précaution.

Aucun constat n’est bloquant au sens d’une dose fausse. Les deux omissions de sécurité (C02, C03) doivent cependant être corrigées avant toute clôture.

## Calculs (EXIGENCE_CALCULS)

L’inventaire est scripté (`calculs/inventaire.py`, puis `calculs/inventaire.json`). Le recalcul est scripté et conservé (`calculs/verifier.py`, puis `calculs/resultats.json`).

| Indicateur | Valeur |
|---|---|
| Occurrences numériques relevées (7 fichiers) | 755 |
| Repères non calculables (numéros d’îlot, années, codes, ordinaux anatomiques) | 353 |
| Valeurs médicales | 402, toutes rattachées à un contrôle (387) ou classées non calculables avec motif (15) |
| Contrôles | 65 |
| Contrôles calculables (recalcul numérique ou logique) | 39 |
| Recalculés | **39 / 39** |
| Contrôles contre la source (seuils, fréquences, posologies) | 26 |
| Corrects | 59 |
| Arrondis | 2 (K20 : 18/88 = 20,5 % pour « 20 % » ; K39 : 7 gouttes de Gutron = 2,33 mg pour 2,5 mg) |
| **Faux** | **3** (K43 → C02 ; K55 → M01 ; K56 → M02) |
| Non vérifiables | 1 (K13 : cas 4 sans pression de base → M08) |

Les recalculs principaux portent sur trois groupes.

- **Vignettes et cas** :
  - vignette g90-0 : 36 mmHg et + 3 par minute ; rapport fréquence/pression 0,083, inférieur à 0,5 ;
  - cas 1 : 40 mmHg, + 4 par minute, rapport 0,10 ;
  - cas 2 : 168/104 mmHg, grade modéré, chaque valeur prise séparément selon la règle « ou » du consensus ;
  - cas 5 : symptômes dans 2 catégories sur 3 requises, critères non remplis ;
  - cas 6 : pause de 4 s, supérieure à 3 s ;
  - cas 7 : 22 h − 21 h = 1 h, inférieur à 4 h ; 3 × 2,5 = 7,5 mg ;
  - cas 8 : 88 mmHg, inférieur à 90 mmHg.
- **Proportions** :
  - 21/8 720 = 0,24 % ;
  - 7/88 et 6/7 ;
  - 1 − 0,68 = 0,32. Ce dernier chiffre est la proportion de sujets **sans** la maladie qui remplissent les critères ; ce n’est pas une valeur prédictive.
- **Posologies** : 3 × 10 mg = 30 mg ; 0,1 mg 3 fois par semaine = 0,043 mg/j ; 10 g de NaCl ≈ 171 mmol de sodium ; un lit de 2 m incliné de 12° ≈ 41,6 cm.

Les sept contrôles P01 à P07 recalculent les exemples nouveaux introduits par les propositions.

## Constats par gravité

### MAJEUR (6)

1. **C01 — Sémiologie fondamentale et analytique absente.** `G90_c.html`, ancre `data-s="g90-s-anat"` : 3 sous-onglets au décompte, aucun `g90-s-semio` et aucun `data-semiology-clinical`.
   - Propositions : `propositions/G90_c_semio.html`, avec 9 sections `data-semiology`, une figure de raisonnement non anatomique et 3 cas corrigés ; `propositions/G90_pop_semio.html`, avec 6 fenêtres ; le marqueur sur `g90-6`.
2. **C02 — Dysréflexie : dérivé nitré sans la contre-indication des inhibiteurs de la PDE5, dans une forme sans information suisse.**
   - L’information suisse de Nitroderm TTS (septembre 2026) contre-indique l’association et tout nitré dans les 24 h qui suivent la prise [S14].
   - Aucune pâte de nitroglycérine à 2 % n’a d’information professionnelle suisse [S21].
   - Trois remplacements sont prévus (g90-8, g90-da-urgence, g90-pharma-da).
3. **C03 — Midodrine : contre-indications incomplètes.**
   - La FI suisse ajoute la grossesse, l’allaitement, le phéochromocytome, l’hyperthyroïdie et le glaucome à angle fermé, et exclut l’enfant et l’adolescent [S11].
   - La phrase « aucune source lue ne traite la grossesse » (g90-12) est démentie par cette FI.
   - L’antagonisme par la prazosine n’est pas signalé.
4. **C04 — Tachycardie posturale sans critère chiffré.** Thijs 2021 (déjà cité par la leçon) donne les critères : plus de 30 par minute, ou au-delà de 120 par minute, dans les 10 minutes ; plus de 40 par minute de 12 à 19 ans ; sans hypotension orthostatique ; avec symptômes [S3].
5. **C06 — Massage sinocarotidien sans précautions.**
   - Les complications restent inférieures à 0,5 %, mais des AVC et un décès ont été rapportés.
   - L’ESC demande la prudence après un AVC ou un AIT et en cas de sténose de plus de 70 % [S3 ; S1].
6. **C07 — Dysréflexie définie par la bradycardie.** La tachycardie est aussi fréquente, voire plus fréquente selon les séries [S5]. L’encadré « Science → clinique » de g90-s-physio peut faire méconnaître une crise.

### MINEUR (15)

- **C08** : `audit_sciences` est en échec (trois « À retenir. » manquent).
- **M01** : « 15 % non améliorés à 2 ans » n’est pas retrouvé dans les sources ; elles donnent 15 à 20 % de syndromes non résolus.
- **M02** : la figure 3 écrit « dans 25 % » au lieu de « jusqu’à 25 % ».
- **M03** : le seuil de 90 mmHg est attribué au « consensus de 2018 » au lieu de l’ESC 2018.
- **M04** : l’écriture « 180/110 » doit devenir « systolique ≥ 180 ou diastolique ≥ 110 ».
- **M05** : la cible de 140 mmHg vient de la section sur la syncope réflexe.
- **M06** : l’ESC donne jusqu’à 0,3 mg/j de fludrocortisone, au-delà du maximum usuel suisse de 0,2 mg/j.
- **M07** : G90.48, G90.49 et les sous-codes de localisation manquent.
- **M08** : le cas 4 n’a pas de pression de base.
- **M09** : le cas 6 pratique un massage hors indication, sans explication.
- **M10** : la prazosine est citée sans FI suisse trouvée et sans son interaction avec la midodrine.
- **M11** : « jusqu’à 40 % » mélange deux populations.
- **M12** : le seuil de 30 mmHg appartient à la définition de 2011.
- **M13** : quatre caractères « < » ne sont pas échappés.
- **M14** : la règle du patient hospitalisé est imprécise ; il faut mesurer debout si la différence dépasse 10 mmHg.

### ENRICHISSEMENT (6)

- **C05** : les formes initiale et retardée n’ont pas de critères chiffrés, et le rapport ΔFC/ΔPAS < 0,5 manque. Proposition : tableau des quatre formes dans `propositions/G90_c_examens_formes.html`.
- **E02** : la conduite devant une dissection n’est pas décrite. Proposition : intégrer l’ESO 2021 (antiplaquettaire ou anticoagulant ; thrombolyse et thrombectomie).
- **E03** : il manque les spécificités suisses du médicament : Gutron en gouttes (10 mg/mL, 30 gouttes/mL, sur la liste des spécialités), Midodrin Substipharm sans mention de la liste, Florinef sur la liste.
- **E04** : le protocole du Valsalva (15 s, 40 mmHg) et de la respiration profonde (6 cycles par minute) manque.
- **E05** : il manque deux données sur le Horner : sa présence dans jusqu’à 58 % des dissections carotidiennes, et la répartition des niveaux.
- **E06** : l’apraclonidine est hors étiquette en Suisse (Iopidine est autorisée pour le glaucome).

Toutes les propositions locales sont dans `propositions/remplacements.json` : 36 couples « ancien → nouveau ». Le script `remplacements.py` vérifie que chaque « ancien » est présent **exactement une fois** dans l’instantané.

## Figures (règle de Vial du 15.10.2026)

Les six figures sont des **schémas non anatomiques** : boîtes, flèches et texte, sans structure dessinée. L’inventaire a été fait par `image_clo_finder.py inventory G90` et par un décompte des balises. Aucune figure n’est classée ANATOMIQUE_IA ni ORIGINE_INCONNUE. Deux d’entre elles portent une inexactitude de contenu : la figure 3 (M02) et la figure 5 (bradycardie, C07). Une planche anatomique réelle de la voie oculosympathique serait un enrichissement ; elle n’a pas été recherchée.

## 21 — Sémiologie fondamentale et analytique

**Statut : absente**, ce qui fait de C01 un MAJEUR bloquant la clôture.

- **Sémiologie fondamentale : partielle**, et seulement dans l’onglet 1 (g90-5, g90-6, g90-horner, g90-stand). Le normal n’est pas décrit pour chaque geste ni le mécanisme pour chaque signe. Les fréquences des symptômes de l’hypotension orthostatique ne sont **pas chiffrées dans les sources lues** (LACUNE).
- **Sémiologie analytique : absente.** Il manque le regroupement en syndromes, le raisonnement en cinq étapes, l’examen numéroté, la synthèse présentée et les cas consacrés au signe.

| Critère | Résultat | Preuve |
|---|---|---|
| SEM-01 | non | aucun `data-s="g90-s-semio"` |
| SEM-02 | non | — |
| SEM-03 | non | audit_sciences en échec (C08) |
| SEM-04 | oui | test_v7 --static : OK |
| SEM-05 | non | pas de tableau des symptômes |
| SEM-06 | non | technique pour la mesure couchée-debout seulement |
| SEM-07 | non | mécanismes regroupés en g90-3, non par signe |
| SEM-08 | non | valeurs éparses ; absences non déclarées par signe |
| SEM-09 | non | normal non explicite par geste |
| SEM-10 | oui | pièges g90-6, g90-e-2, g90-e-5 |
| SEM-11 | non | aucun tableau des syndromes |
| SEM-12 | non | aucune séquence en cinq étapes |
| SEM-13 | oui | alert g90-8, à compléter (C02, C07) |
| SEM-14 | non | SDRC : différentiel sans discriminant |
| SEM-15 | non | examen non numéroté |
| SEM-16 | non | pas de synthèse présentée |
| SEM-17 | non | aucun cas sur la valeur d’un signe ni sur une limite |
| SEM-18 | non | non vérifié au navigateur |
| SEM-19 | non | conduite de la dysréflexie d’origine américaine (signalée par le cours) |
| SEM-20 | non | attribution du seuil de 90 mmHg incohérente (M03) |
| SEM-21 | oui | sans objet |
| SEM-22 | non | non mesuré |
| SEM-23 | non | aucune capture |
| SEM-24 | oui | statut « revue IA, aucune validation médicale humaine » |

La proposition `G90_c_semio.html` suit la structure exigée par le contrat :

- bouton `g90-tab-semio` en tête de la barre et panneau `g90-s-semio` (`role="tabpanel"`) ;
- neuf sections dans l’ordre normal, signs, mechanisms, examination, interpretation, differentials, urgency, limits, sources ;
- quatre libellés de corrélation, une figure de raisonnement et trois cas corrigés ;
- 3 195 mots, classes de la liste fermée, aucun style en ligne, aucune collision de clé.

Les cas couvrent la valeur d’un signe (cas A, rapport 0,25), le seuil lié à l’âge (cas B, 36 par minute à 22 ans contre 16 ans) et la formulation d’une limite (cas C, anhidrose absente).

## Matrice des 20 rubriques (leçon actuelle)

| N° | Rubrique | Statut | Ancre |
|---|---|---|---|
| 1 | Question clinique | couvert | g90-0 |
| 2 | Définition et CIM-10-GM | couvert | g90-1, g90-codage (M07) |
| 3 | Classifications et stades | partiel | g90-1 (C05) |
| 4 | Épidémiologie suisse puis européenne | partiel | g90-2 ; aucune donnée suisse |
| 5 | Normal → pathologique | couvert | g90-3, g90-s-* |
| 6 | Étiologies | couvert | g90-4 |
| 7 | Anamnèse et fréquences | partiel | g90-5 |
| 8 | Examen clinique et Se/Sp | partiel | g90-6 (C01, C06) |
| 9 | Drapeaux rouges | partiel | g90-8 (C02, C07) |
| 10 | Examens complémentaires | partiel | pE (C04, C05) |
| 11 | Diagnostic différentiel | partiel | g90-7 |
| 12 | Prise en charge suisse | partiel | g90-9, g90-10, pP (C03) |
| 13 | Complications et pronostic | partiel | g90-11 (M01) |
| 14 | Suivi et prévention | couvert | g90-11 |
| 15 | Situations particulières | partiel | g90-12 (C03) |
| 16 | Spécificités suisses | partiel | hors étiquette signalé ; liste des spécialités et conduite automobile absentes (E03) |
| 17 | Critères formels (alert) | partiel | g90-13 (C04) |
| 18 | Paramètres clés (key) | couvert | g90-13 (M01, M04) |
| 19 | Sous-codes | partiel | g90-codage (M07) |
| 20 | Points d’examen fédéral | partiel | g90-0 ; aucun objectif PROFILES |

## Lacunes principales

- **Aucune recommandation suisse ni européenne** sur la conduite aiguë de la dysréflexie. La requête WebSearch « autonome Dysreflexie Leitlinie DMGP Notfall… » est restée sans résultat de ce type.
- **Aucune donnée épidémiologique suisse.** La Revue médicale suisse 2025 (sujet âgé) n’a été lue qu’en résumé ; le texte intégral était inaccessible (délai dépassé).
- **ESC 2018** : les tableaux de classes de recommandation sont publiés en images et n’ont pas été lus.
- **Sources lues en résumé seulement** : Fedorowski, González-Duarte, Krivoborodov, ESO 2021.
- **Recherches dans AmiKo** : aucune prazosine, et seulement des formes retard de nifédipine. Une absence de résultat n’est pas une preuve absolue.
- **Rubrique 16 incomplète** : conduite automobile après syncope, Suva/LAA et AI n’ont pas été recherchées.
- **Contrôles non réalisés** : navigateur (SEM-18, 22, 23) et captures.

## Tableau de bord

| Élément | Valeur |
|---|---|
| Leçon | G90 — Affections du système nerveux autonome (N-05-Neurologie) |
| Fichiers audités | 7 (empreintes conformes) |
| Constats | BLOQUANT 0 · MAJEUR 6 · MINEUR 15 · ENRICHISSEMENT 6 |
| Calculs | 755 relevés · 39 calculables · 39 recalculés · 3 faux · 1 non vérifiable |
| Sémiologie (rubrique 21) | absente (C01, MAJEUR) ; proposition complète |
| Figures | 6 schémas non anatomiques ; 0 anatomique IA |
| Sources | 21 (dont 4 FI suisses datées), voir `sources.json` |
| Propositions | `G90_c_semio.html`, `G90_pop_semio.html`, `G90_c_examens_formes.html`, `remplacements.json` (36 remplacements vérifiés) |
| Fichiers canoniques modifiés | aucun |

*Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.*
