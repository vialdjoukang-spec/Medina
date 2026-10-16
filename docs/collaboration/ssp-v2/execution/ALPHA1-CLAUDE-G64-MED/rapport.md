# Audit Alpha tour 1 — ALPHA1-CLAUDE-G64-MED

**Leçon : G64 — Autres affections du système nerveux périphérique (S08, N-05-Neurologie).**
Audit médical agressif avec enrichissement, effort élevé, conforme au manifeste. Branche `claude/alpha1/g64-med-g1`. Base de la mission (manifeste) : `d1a488ad4f0031d7f2a4b47a0721e89a93475d77`. Base du worktree : `32416a2080e67537641040a81252dec0b3e6d137` ; START exécuté sur le premier main contenant l'approbation de la mission (PR #181). Sources figées identiques : empreintes SHA-256 conformes au manifeste.

Horodatages UTC : début non relevé (premier horodatage observé 2026-10-16T05:55:35Z) ; fin 2026-10-16T06:12:10Z.

> Audit IA — revue distincte d'une validation médicale humaine ; aucune source canonique modifiée.

## 1. Lecture et contrôles d’entrée

J’ai lu en entier les sept fichiers de la leçon : `G64_a` à `G64_d`, `G64_pop1`, `G64_pop2` et `glossary/g64.py`. Leurs empreintes SHA-256, recalculées dans le worktree, sont **identiques au manifeste**. `python3 test_v7.py --static G64` affiche **OK** (9106 mots, 34 fenêtres, 5 quiz, 14 Pareto). Un script a vérifié que chaque ancre citée figure telle quelle dans son fichier, une seule fois.

La première source lue est la revue de Sommer et al. (Dtsch Arztebl Int 2018) : d’abord son résumé PubMed, puis son texte intégral sur PMC. Cette revue est la source principale de la leçon. J’ai lu en texte intégral la guideline allemande DGN « Diagnostik bei Polyneuropathien » (AWMF 030/067, 2025). J’ai aussi lu quatre informations professionnelles suisses datées : Lyrica® (juillet 2026), Duloxetin-Mepha® (décembre 2024), Saroten® (octobre 2022) et Neurontin® (avril 2025). Vingt sources figurent dans `sources.json`, avec leur niveau de lecture.

## 2. Synthèse

| Gravité | Nombre |
|---|---|
| BLOQUANT | 0 |
| MAJEUR | 8 |
| MINEUR | 6 |
| ENRICHISSEMENT | 5 |

La leçon est prudente et transparente sur ses limites. Elle n’invente aucun chiffre. Les chiffres vérifiés dans la revue allemande, dans les guidelines EFNS/PNS et PNS, dans la méta-analyse NeuPSIG et dans les informations professionnelles sont exacts (voir § 5). Trois fragilités dominent cependant. Le rattachement de codage de la vignette est faux. Deux critères formels déforment leur source. Enfin, la sécurité des deux médicaments décrits est incomplète pour une patiente âgée. L’onglet Sciences ne remplit pas l’exigence structurelle : il manque une cinquième discipline et la sémiologie.

## 3. Constats classés par gravité

### MAJEUR

**C01 — La vignette relève de G62.9, non de G64** (`G64_a.html`, g64-0 et g64-1). La patiente présente une polyneuropathie distale symétrique, ce que la leçon reconnaît elle-même. La CIM-10-GM 2024 prévoit pour ce cas G62.9, « polyneuropathie, sans précision ». G64 couvre seulement une « affection du système nerveux périphérique sans autre indication » [S1]. Le tableau du bloc omet aussi G62.9 et G62.80. La correction se trouve dans `propositions/G64_a_1.html`.

**C02 — La vascularite « probable » est surévaluée** (`G64_b.html` g64-12, `G64_c.html` g64-e-5, fenêtre g64-vasc-criteres). La leçon exige que les cinq prédicteurs histologiques soient « réunis ». Le résumé PNS 2010 dit seulement que les critères « incluent » cinq prédicteurs [S3]. La leçon omet aussi la définition clinique sans biopsie. Ce seuil inventé peut faire écarter une neuropathie traitable. Le texte intégral était inaccessible (LACUNE L01). La correction se trouve dans `G64_b_1.html`.

**C03 — Le syndrome de Guillain-Barré n’a pas de conduite hospitalière** (`G64_b.html` g64-8, fenêtre g64-sgb). La leçon affirme que sa source ne donne pas le traitement. Or la revue de 2018 demande une hospitalisation rapide, souvent en soins intensifs, et cite les immunoglobulines intraveineuses et les échanges plasmatiques [S2]. La guideline EAN/PNS 2023 donne la dose de 0,4 g/kg par jour pendant cinq jours, chez le patient incapable de marcher sans aide [S15]. La correction se trouve dans `G64_b_2.html`.

**C04 — Les mises en garde de la prégabaline sont incomplètes** (`G64_d.html` g64-p-3). Manquent l’étourdissement et la somnolence, avec le risque de chute chez la personne âgée, et l’abstention de conduite. Manquent aussi la dépression respiratoire, l’association aux opiacés (odds ratio ajusté 1,68 de décès lié aux opioïdes) ainsi que le mésusage et la dépendance [S10]. La correction se trouve dans `G64_d_1.html`.

**C05 — Les contre-indications de la duloxétine sont incomplètes** (`G64_d.html` g64-p-4). Manquent les inhibiteurs irréversibles de la monoamine oxydase, l’insuffisance hépatique, les inhibiteurs du CYP1A2 et l’hypertension non équilibrée. Le seuil rénal (moins de 30 ml/min), l’hyponatrémie du sujet âgé et l’évaluation à deux mois manquent aussi [S11]. La correction se trouve dans `G64_d_2.html`.

**C06 — L’onglet Sciences compte quatre disciplines réelles au lieu de cinq** : anatomie, histologie, physiologie et biochimie. Je propose la **génétique**, qui répond aux deux questions ouvertes de la leçon. La première est la polyneuropathie restée sans cause (environ 25 %). La seconde est la neuropathie douloureuse des petites fibres. La génétique a en outre des conséquences thérapeutiques : maladie de Fabry et amylose à transthyrétine [S14]. La discipline complète se trouve dans `G64_c_2.html`.

**C07 — La sémiologie fondamentale et analytique est absente. MAJEUR, bloquant pour la clôture du cours et du lot (AGENTS.md).** Voir la rubrique 21 ci-dessous. La proposition se trouve dans `G64_c_1.html` et `G64_pop3_1.html`.

**C08 — Le critère formel de la neuropathie des petites fibres ne comporte pas la clinique** (`G64_b.html` g64-12). Les sources suisses et européennes posent d’abord le diagnostic sur des signes thermoalgiques ou dysautonomiques, avec une électroneurographie normale. La biopsie ou les QST confirment ensuite [S16][S14][S6]. La correction se trouve dans `G64_b_3.html`.

### MINEUR

- **C09** — Le NNH de la méta-analyse NeuPSIG compte les arrêts pour effet indésirable, non tous les événements. Plusieurs chiffres présentés comme « non cités » figurent dans le résumé : capsaïcine crème, lidocaïne. La troisième ligne regroupe la toxine botulique A, la stimulation magnétique transcrânienne répétitive et les opioïdes [S5]. Correction dans `G64_d_4.html`.
- **C10** — Pour la PIDC et la neuropathie motrice multifocale, les chiffres de la source sont des prévalences [S2]. La leçon les classe parmi des « incidences ».
- **C11** — Le seuil d’alcool de 100 g par jour doit être nuancé : la guideline de 2025 ne retient aucun seuil net [S14]. Correction dans `G64_b_4.html`.
- **C12** — Sous une clairance de la créatinine de 30 ml/min, la prégabaline « ne doit pas être utilisée » selon l’information professionnelle. La leçon écrit seulement « non recommandée » [S10].
- **C13** — La ligne « IgG avec amylose → amylose » est circulaire. Une gammapathie IgG ou IgA est en général fortuite, sauf dans le POEMS [S14][S2].
- **C14** — Dix mots verts sont imbriqués (un bouton dans un bouton) : le HTML est invalide, défaut technique sans effet sur le fond.

### ENRICHISSEMENT

- **E01** — Amitriptyline : elle est indiquée en Suisse dans les douleurs neuropathiques de l’adulte, à 10 à 25 mg le soir puis 25 à 75 mg par jour. Ses contre-indications sont cardiaques et hépatiques [S12]. Proposition dans `G64_d_3.html`.
- **E02** — Gabapentine : son indication suisse se limite à la neuropathie diabétique et à la névralgie postherpétique [S13]. Proposition dans `G64_d_3.html`.
- **E03** — Calendrier de suivi : contrôle après six mois à un an. La forme idiopathique chronique, qui représente environ 25 % des cas, a un bon pronostic [S14]. Proposition dans `G64_b_4.html`.
- **E04** — Drapeau rouge de l’amylose à transthyrétine après 60 ans [S14], pertinent pour la patiente de 67 ans de la vignette.
- **E05** — POEMS : maladie de Castleman, facteur de croissance de l’endothélium vasculaire, autogreffe de cellules souches en première ligne [S2].

## 4. Matrice des 20 rubriques

| N° | Rubrique | Statut | Ancre |
|---|---|---|---|
| 1 | Question clinique et enjeu | couvert | g64-0 (codage à corriger, C01) |
| 2 | Définition et périmètre CIM-10-GM | partiel | g64-1 (C01) |
| 3 | Classifications et stades | couvert | g64-2 |
| 4 | Épidémiologie | partiel | g64-2, g64-3 (C10) ; aucune donnée suisse |
| 5 | Normal → pathologique | partiel | g64-4, g64-s-physio |
| 6 | Étiologies et facteurs de risque | couvert | g64-3 (C11) |
| 7 | Anamnèse et symptômes | partiel | g64-5 (C07) |
| 8 | Examen clinique | partiel | g64-6 (C07) |
| 9 | Drapeaux rouges | partiel | g64-8 (C03, E04) |
| 10 | Examens complémentaires | couvert | g64-7, g64-e-1 à e-5 |
| 11 | Diagnostic différentiel | partiel | g64-6, g64-8 (C07) |
| 12 | Prise en charge suisse | partiel | g64-9, g64-p-1 à p-5 (C04, C05, E01, E02) |
| 13 | Complications et pronostic | partiel | g64-10 |
| 14 | Suivi, prévention | partiel | g64-10, g64-11 (E03) |
| 15 | Situations particulières | partiel | g64-11 |
| 16 | Spécificités suisses | absent | aptitude à la conduite seulement dans la proposition C04 |
| 17 | Critères formels (div.alert) | partiel | g64-12 (C02, C08) |
| 18 | Paramètres clés (div.key) | couvert | g64-12 |
| 19 | Sous-codes CIM-10-GM | sans objet | G64 n’a pas de sous-code [S1] |
| 20 | Points d’examen fédéral | partiel | g64-e-6, g64-p-6 |

## 21. Sémiologie fondamentale et analytique

**Statut : absente — constat C07, MAJEUR, bloquant pour la clôture du cours et du lot (AGENTS.md).** La barre `.sci-bar` ne contient aucun bouton `g64-s-semio` et il n’existe aucun `div.sci` homonyme. La sémiologie existante se réduit à deux îlots. L’îlot g64-5 présente l’anamnèse comme une liste de causes. L’îlot g64-6 contient un seul signe qualifié de « sensible et spécifique », sans chiffre [S2], et un tableau d’interprétation. On n’y trouve ni technique des gestes, ni mécanisme par signe, ni valeur chiffrée, ni examen systématique, ni raisonnement en cinq étapes.

| Critère | Résultat | Preuve |
|---|---|---|
| SEM-01 | non | aucun `data-s="g64-s-semio"` |
| SEM-02 | non | absent |
| SEM-03 | non | absent |
| SEM-04 | non | discipline absente (la leçon actuelle passe `--static`) |
| SEM-05 | non | pas de tableau des symptômes |
| SEM-06 | non | aucune technique |
| SEM-07 | non | mécanismes généraux en g64-4 seulement |
| SEM-08 | non | aucune valeur ni LACUNE déclarée pour les signes |
| SEM-09 | non | normal non décrit |
| SEM-10 | oui | pièges g64-6, g64-11 |
| SEM-11 | non | profils sans mécanisme commun |
| SEM-12 | non | pas de raisonnement ordonné |
| SEM-13 | oui | `div.alert` g64-8 (seuil de gravité à préciser, C03) |
| SEM-14 | non | différentiels sans discriminant |
| SEM-15 | non | pas d’examen numéroté |
| SEM-16 | non | pas de synthèse présentée |
| SEM-17 | non | quiz sans valeur d’un signe |
| SEM-18 | non | sans objet ; mots verts imbriqués (C14) |
| SEM-19 | oui | sources suisses, européennes et revues ; aucune recommandation américaine |
| SEM-20 | oui | chiffres cohérents |
| SEM-21 | non | sans objet |
| SEM-22 | non | non vérifiable |
| SEM-23 | non | aucune capture possible |
| SEM-24 | oui | statut « aucune validation médicale humaine » |

Les critères bloquants SEM-01 à SEM-04 et SEM-08 ne sont pas remplis. Les critères SEM-13 et SEM-19 sont remplis.

**Proposition** (`propositions/G64_c_1.html`, sept îlots `g64-sm-1` à `g64-sm-7`, huit fenêtres dans `G64_pop3_1.html`). Elle suit la structure du § 4 b. L’îlot 1 ouvre sur une priorité clinique : le syndrome de Guillain-Barré face à l’atteinte médullaire. L’îlot 2 présente un tableau des six symptômes, avec leur mécanisme et leur valeur. L’îlot 3 décrit quatre gestes : réflexe achilléen, diapason de Rydel-Seiffer, sensibilité thermoalgique, Romberg et marche. Il contient une figure non anatomique, lisible à 390 px (texte rendu à 12,9 px). L’îlot 4 regroupe les signes en cinq syndromes. L’îlot 5 conduit le raisonnement en cinq étapes, avec des discriminants sourcés. L’îlot 6 détaille l’examen systématique en onze étapes et donne un exemple de présentation. Il comporte les quatre encadrés exigés. L’îlot 7 propose trois cas corrigés : la valeur d’un signe, la localisation et la formulation honnête d’une limite.

Une seule valeur chiffrée de signe a été trouvée. L’abolition achilléenne a un rapport de vraisemblance positif de 7,6 et négatif de 0,3 [S19]. Ce chiffre vient d’une étude australienne lue en résumé : il est signalé comme tel et ne fixe aucune conduite. Toutes les autres valeurs sont écrites « non chiffrées dans les sources lues » (LACUNE L04). Les liens causaux que les sources n’énoncent pas sont marqués « déduction ».

## 5. Vérifications conformes

Plusieurs données ont été vérifiées dans leur source et sont conformes. Dans la revue de 2018 [S2] : prévalence de 5 à 8 % ; parts du diabète, de l’alcool et de la chimiothérapie ; carence en B12 sans macrocytose ; cause indéterminée jusqu’à 30 %. On y trouve aussi les délais du syndrome de Guillain-Barré et de la PIDC, le liquide céphalorachidien de la PIDC, les chiffres de l’oxaliplatine et les indications de biopsie. La guideline EFNS/PNS de 2010 sur la biopsie cutanée confirme les niveaux de preuve et le chiffre de 0,19 % [S4]. Les critères de vascularite systémique et les recommandations thérapeutiques PNS sont exacts [S3]. Les NNT et NNH des trois classes de première ligne sont exacts [S5]. Les posologies de la prégabaline et de la duloxétine sont conformes [S10][S11]. Les chiffres des deux revues romandes sont conformes [S8][S9].

## 6. Lacunes

| N° | Objet | Conséquence |
|---|---|---|
| L01 | Texte intégral PNS 2010 (HTTP 403) | nombre de prédicteurs exigé non lu |
| L02 | eTableau d’immunosuppression de Sommer 2018 illisible | évidences par indication non vérifiées |
| L03 | Seuils du diapason gradué et du test de Schellong | déclarés non lus |
| L04 | Valeurs suisses ou européennes des signes | un seul signe chiffré, source australienne |
| L05 | Revues suisses en accès payant | lues en résumé |
| L06 | Spécificités suisses (AI, Suva, remboursement) | rubrique 16 non enrichie |
| L07 | Quelques affirmations de la leçon non relues | ni confirmées ni infirmées |
| L08 | Captures SEM-22 et SEM-23 | à faire à l’intégration |

## 7. Figures

L’outil `tools/image_clo_finder.py inventory G64` recense cinq SVG, tous de type `SCHEMA_NON_ANATOMIQUE`. Le premier est l’organigramme de la démarche, figure 1 de `G64_b.html`. Mesuré à 390 px, son texte est rendu à 13,2 px, sans débordement. Les quatre autres sont les pictogrammes de la barre des sciences. La leçon ne contient aucune figure anatomique produite par une IA.

## 8. Tableau de bord

| Élément | Valeur |
|---|---|
| Cours | G64 — Autres affections du système nerveux périphérique |
| Fragment | S08 (N-05-Neurologie) |
| Empreintes | 7/7 conformes |
| Contrôle statique | OK |
| Constats | 0 bloquant, 8 majeurs, 6 mineurs, 5 enrichissements |
| Sémiologie | absente (MAJEUR, bloquant pour la clôture du cours et du lot), proposition complète en 7 îlots |
| Disciplines Sciences | 4/5, génétique proposée |
| Sources | 20 (2 en texte intégral, 4 informations professionnelles par section, 14 en résumé) |
| Propositions | 13 fichiers dans `propositions/` |
| Alertes | Codage de la vignette (C01) ; sécurité médicamenteuse chez la personne âgée (C04, C05) ; critères formels (C02, C08) |

*Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.*
