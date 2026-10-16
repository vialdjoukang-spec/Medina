# Audit médical Alpha, tour 1 — G23, « Autres maladies dégénératives des noyaux gris centraux » (S08)

Mission **ALPHA1-CLAUDE-G23-MED** · branche `claude/alpha1/g23-med-g1` · base de mission `d1a488ad` (manifeste) · worktree créé sur `32416a20` · génération 1 · modèle et effort conformes au manifeste · exécuté par un sous-agent Claude Code.

Les empreintes SHA-256 des sept fichiers de la leçon sont **conformes** au manifeste. START exécuté sur le premier main contenant l'approbation de la mission (PR #181). Sources figées identiques : empreintes SHA-256 conformes au manifeste. La lecture a porté sur les sept fichiers en entier, et chaque ancre a été vérifiée par script : elle apparaît une seule fois dans son fichier.

## Synthèse

La leçon est solide sur les critères MDS, la neuropathologie et la pharmacologie suisse, mais elle n’a **pas de sémiologie fondamentale et analytique**. Ses sciences échouent au contrôle `audit_sciences.py`. L’audit relève aussi quatre erreurs décisionnelles sur les critères : le seuil diastolique appliqué à l’AMS, l’impériosité confondue avec l’incontinence par impériosité, des valeurs de sensibilité attribuées au mauvais test et une dose de Madopar® exprimée sans conversion en lévodopa. Il signale enfin trois omissions de sécurité tirées des informations professionnelles suisses : l’agranulocytose sous défériprone, les contre-indications cardiaques de l’amantadine et l’hypertension de décubitus sous l’association midodrine–fludrocortisone.

| BLOQUANT | MAJEUR | MINEUR | ENRICHISSEMENT |
|---|---|---|---|
| 0 | 11 | 11 | 5 |

Aucun constat n’est classé BLOQUANT au sens médical : aucune dose dangereuse n’est prescrite. En revanche, **C01 (sémiologie absente) est MAJEUR, bloquant pour la clôture du cours et du lot (AGENTS.md)**.

Horodatages UTC : début non relevé au démarrage (`null` ; premier horodatage observé 2026-10-16T05:57:35Z) ; fin 2026-10-16T06:28:50Z, relevée juste avant le commit.

## Constats majeurs

**C01** — `G23_c.html` — La leçon ne possède pas de sous-onglet « Sémiologie fondamentale et analytique » : la barre #pS ne contient que les cinq disciplines (anatomie, histologie, physiologie, biochimie, génétique). Les symptômes et signes existent en liste (g23-5, g23-6), sans technique, sans mécanisme par signe, sans normal préalable, sans regroupement syndromique ni raisonnement en cinq étapes. SEM-01, SEM-02, SEM-03 (pour cette discipline) et SEM-13 sont non satisfaits.  
*Preuve :* [S1] Supportive features ; Cardiovascular Autonomic Failure; [S3] Cardiovascular autonomic failure; [S5] Conclusion on diagnostic criteria.  
*Proposition :* Insérer la discipline complète de propositions/G23_c_1.html (bouton en tête de .sci-bar, div.sci g23-s-semio, neuf sections data-semiology g23-sm-1 à g23-sm-9, bouton g23-tab-semio, panneau role=tabpanel, figure 8) ajouter en fin de chapters/G23/G23_pop2.html les 8 fenêtres g23-sm-* de propositions/G23_pop2_1.html (seuls _pop1 et _pop2 sont des fichiers admis) ; insérer dans chapters/G23/G23_a.html (panneau pA, îlot g23-6, avant l’encadré « À retenir ») la section data-semiology-clinical="G23" de propositions/G23_a_semio_clinique.html.

**C02** — `G23_c.html` — tests/audit_sciences.py échoue sur G23 (base 32416a20) : quatre disciplines sur cinq ont moins de 280 mots (histologie 221, physiologie 234, biochimie 229, génétique 205) et neuf encadrés de corrélation exigés manquent (Science → traitement en anatomie, histologie et génétique ; Science → examen en physiologie et biochimie ; À retenir dans les cinq).  
*Preuve :* [S4] Biologisch und neuropathologisch basierte Krankheitsdefinition; [S4] Ätiopathogenese; [S3] Supportive laboratory findings.  
*Proposition :* Ajouter les paragraphes et encadrés de propositions/G23_c_2.html (cinq disciplines) et la clé MAPT au glossaire.

**C03** — `G23_a.html` — Erreur factuelle : la revue de Munich, citée par la leçon, présente le syndrome de Richardson comme le phénotype clinique le plus fréquent à ce jour, bien qu’il ne concerne qu’environ 25 % des cas. La leçon affirme l’inverse.  
*Preuve :* [S4] Klinische Manifestationen.  
*Proposition :* Remplacer par le texte de propositions/G23_a_1.html et ajouter PSP-PI à la fenêtre g23-phenotypes-psp.

**C04** — `G23_a.html` — La leçon applique à l’AMS la définition ESC (chute systolique ≥ 20 ou diastolique ≥ 10 ou systolique < 90 mmHg). Les critères MDS 2022 exigent une chute systolique ≥ 20 mmHg, acceptent le critère systolique seul et précisent que la chute diastolique isolée n’est pas spécifique et ne doit pas être utilisée seule. Même formulation en g23-e-2 (G23_c.html), dans le tableau de g23-e-2 et dans la fenêtre g23-ho.  
*Preuve :* [S1] Cardiovascular Autonomic Failure.  
*Proposition :* Remplacer par le texte de propositions/G23_a_2.html aux trois emplacements.

**C05** — `G23_c.html` — Attribution erronée : 91,3 % et 88,4 % (et 79 % en station active) sont la sensibilité et la spécificité du rapport ΔFC/ΔPAS < 0,5 pour distinguer l’hypotension neurogène des causes non neurogènes, et non celles du test d’inclinaison pour l’hypotension orthostatique. Même erreur dans la fenêtre g23-ho (G23_pop1.html : « Le test d’inclinaison a une sensibilité de 91,3 % »).  
*Preuve :* [S3] Cardiovascular autonomic failure.  
*Proposition :* Remplacer par propositions/G23_c_3.html dans g23-e-2 et dans la fenêtre g23-ho.

**C06** — `G23_b.html` — Le critère autonome MDS 2022 est l’incontinence urinaire par impériosité inexpliquée (fuite involontaire), non l’impériosité. Formulé « impériosité » dans l’alerte de g23-12, dans la fenêtre g23-ams-criteres (« ou impériosité urinaire inexpliquée ») et dans g23-retention (« ou une impériosité inexpliquée sont des critères autonomes »). L’exclusion des causes prostatiques et pelviennes n’est pas mentionnée.  
*Preuve :* [S1] Tableau 1 ; tableau 3 (lexique); [S1] Urogenital Failure.  
*Proposition :* Remplacer par propositions/G23_b_1.html aux trois emplacements.

**C07** — `G23_b.html` — Ambiguïté de dose : « 125 mg » est le nom de dosage de Madopar® « 125 » (100 mg de lévodopa + 25 mg de bensérazide), alors que l’essai diagnostique s’exprime en lévodopa (jusqu’à 1000 mg par jour). Juxtaposés sans conversion (9.2 et tableau g23-p-2 : « entretien de Madopar® : 3 à 6 fois 125 mg par jour »), ils laissent croire que l’entretien de 750 mg de Madopar approche l’essai ; 1000 mg de lévodopa correspondent à dix unités « 125 ».  
*Preuve :* [S14] Forme pharmaceutique; [S14] Posologie; [S1] Parkinsonism.  
*Proposition :* Remplacer par propositions/G23_b_2.html (9.2) et adapter la ligne lévodopa de g23-p-2.

**C08** — `G23_d.html` — La surveillance de la défériprone omet le risque majeur de l’information professionnelle suisse : neutropénie et agranulocytose parfois mortelles, avec numération des neutrophiles hebdomadaire la première année, arrêt en cas d’infection, contre-indications (agranulocytose, neutropénies récidivantes, médicaments neutropéniants).  
*Preuve :* [S17] Mises en garde et précautions; [S17] Contre-indications.  
*Proposition :* Remplacer la ligne par propositions/G23_d_1.html et ajouter le bloc Sécurité à la fenêtre g23-ferriprox.

**C09** — `G23_d.html` — L’alerte « Interactions et contre-indications dangereuses » donne une liste incomplète des contre-indications de PK-Merz® sans le signaler : manquent l’insuffisance cardiaque NYHA IV, la cardiomyopathie ou myocardite, les ondes U et le QT long congénital familial, les arythmies ventriculaires graves, l’association à un médicament allongeant le QT et les antécédents de délire ; l’exclusion sous traitement (allongement > 60 ms ou QTc > 480 ms) manque aussi. L’indication suisse des comprimés (« Morbus Parkinson verschiedener Genese ») n’est pas qualifiée pour la PSP et la DCB.  
*Preuve :* [S13] Contre-indications; [S13] Posologie.  
*Proposition :* Remplacer la phrase par propositions/G23_d_2.html et préciser dans g23-pkmerz que l’indication suisse vise la maladie de Parkinson « quelle que soit son origine » ; son extension aux tauopathies 4R reste à documenter comme usage hors indication probable.

**C10** — `G23_b.html` — La séquence thérapeutique propose midodrine et fludrocortisone sans signaler que la FI de Gutron® décrit une hypertension de décubitus fréquente aux fortes doses, surtout en association avec la fludrocortisone, ni que la moitié des patients AMS avec hypotension neurogène ont une hypertension de décubitus ou nocturne. L’arrêt en cas de hausse excessive de la pression couchée n’est pas mentionné.  
*Preuve :* [S12] Effets indésirables; [S12] Posologie; [S3] Cardiovascular autonomic failure.  
*Proposition :* Ajouter l’encadré trap de propositions/G23_b_3.html après la séquence ESC (9.5) et le rappeler dans g23-p-3.

**C11** — `G23_b.html` — La toxine botulique est proposée dans la PSP et la DCB, dont la dysphagie est la cause principale de mortalité, sans mentionner l’aggravation possible de la dysphagie (revue de Munich) ni la mise en garde de la FI Xeomin® (dysphagie pendant 2 à 3 semaines, diffusion à distance parfois mortelle, prudence en cas d’antécédent d’aspiration).  
*Preuve :* [S4] Tableau des traitements symptomatiques; [S15] Mises en garde.  
*Proposition :* Ajouter le paragraphe de propositions/G23_b_4.html en 9.3 et dans la fenêtre g23-xeomin (mettre à jour la date de la FI : mars 2026).

## Constats mineurs

**C12** — `G23_d.html` — La liste des contre-indications de Gutron® omet les arythmies, la maladie rénale aiguë, les maladies vasculaires oblitérantes sévères, la rétinopathie diabétique proliférante, la réaction hypertonique au test de station debout et l’allaitement ; l’indication suisse comprend aussi les formes fonctionnelles et iatrogènes. Un générique suisse (Midodrin Substipharm, mai 2024) existe.  
*Preuve :* [S12] Contre-indications; [S18] Indications.  
*Proposition :* Compléter l’alerte de g23-p-3 et la fenêtre g23-gutron avec la liste intégrale de la FI (mars 2021) et mentionner le générique.

**C13** — `G23_b.html` — Avant 45 ans, les critères MDS 2017 font aussi chercher une hypoparathyroïdie, une neuroacanthocytose et une neurosyphilis. Le seuil d’exclusion de la dysautonomie dans la PSP (30/15 mmHg en 3 minutes) n’est donné nulle part (« dysautonomie prédominante » seulement).  
*Preuve :* [S2] Tableau 1, exclusions dépendant du contexte et obligatoires.  
*Proposition :* Compléter la ligne du tableau 7.5 et la fenêtre g23-psp-criteres : « avant 45 ans : maladie de Wilson, Niemann-Pick C, hypoparathyroïdie, neuroacanthocytose, neurosyphilis » ; « dysautonomie : hypotension orthostatique d’au moins 30/15 mmHg en 3 minutes ».

**C14** — `G23_pop1.html` — La liste des phénotypes MDS 2017 omet la PSP à prédominance d’instabilité posturale (PSP-PI), présente dans les critères et dans la revue de Munich.  
*Preuve :* [S2] Predominance Types.  
*Proposition :* Voir propositions/G23_a_1.html (ajout PSP-PI et clé de glossaire).

**C15** — `G23_b.html` — Formulation plus précise que le passage lu de l’ESC 2018, qui dit seulement que les preuves sont insuffisantes pour confirmer l’efficacité à long terme. Le statut suisse de la droxidopa n’a pas été vérifié.  
*Preuve :* [S8] § 5.3.10.  
*Proposition :* Écrire : « Les preuves sont insuffisantes pour confirmer l’efficacité de la droxidopa à long terme (lignes directrices ESC sur la syncope, 2018) ; aucune autorisation suisse n’a été vérifiée. »

**C16** — `G23_b.html` — La source dit « aucune recommandation » pour la chirurgie des muscles oculomoteurs, et non qu’elle n’est pas indiquée.  
*Preuve :* [S4] Tableau des traitements symptomatiques.  
*Proposition :* Écrire : « la revue de Munich ne recommande pas de chirurgie des muscles oculomoteurs ».

**C17** — `G23_a.html` — Relation causale étendue à l’AMS sans source lue (addendum, point 3) : les sources citées établissent la dégénérescence dopaminergique post-synaptique comme indice d’imagerie de la PSP (IF2) ; aucune source lue ne l’établit comme mécanisme de la mauvaise réponse dans l’AMS.  
*Preuve :* [S2] Tableau 3; [S3] Parkinsonism.  
*Proposition :* Écrire : « Dans la PSP, la dégénérescence dopaminergique striatale post-synaptique est un indice d’imagerie (IF2) ; elle est cohérente avec la faible réponse à la lévodopa. Dans l’AMS, la faible réponse est constatée ; son mécanisme n’est pas détaillé dans les sources lues. »

**C18** — `G23_a.html` — Jugement comparatif non sourcé (« le geste le plus rentable »).  
*Preuve :* [S1] Cardiovascular Autonomic Failure.  
*Proposition :* Écrire : « La pression artérielle couchée puis debout, avec le pouls, objective le critère autonome cardiovasculaire des critères MDS. »

**C19** — `G23_pop2.html` — Les FI suisses de Florinef® et de Xeomin® portent la date de mise à jour mars 2026 ; la leçon écrit « date non relevée » (g23-florinef, g23-xeomin : « Posologie et date de mise à jour non relevées. »). L’indication suisse de Florinef® comprend aussi le syndrome de perte de sel du syndrome adrénogénital.  
*Preuve :* [S16] Indications ; mise à jour; [S15] Mise à jour.  
*Proposition :* Inscrire « information professionnelle suisse Florinef®, mars 2026 » et « Xeomin®, mars 2026 » ; compléter l’indication de Florinef®.

**C20** — `G23_a.html` — Figure 1 : texte en font-size 11 dans une viewBox de 420 de large ; rendu à environ 9,4 px dans une colonne de 358 px (écran de 390 px avec gouttières de 16 px), sous le seuil d’environ 10 px. Aucune valeur chiffrée décisionnelle n’y figure.  
*Preuve :* mesure directe du fichier.  
*Proposition :* Porter le texte à font-size 13 au minimum, ou réduire la viewBox à 360 de large en scindant les libellés sur deux lignes.

**C21** — `G23_b.html` — La spécificité de la rétention vaut contre la maladie de Parkinson ; elle est moins discriminante contre la PSP, où une vessie neurogène peut aussi apparaître. La précision est donnée en 5.2 mais pas en 8.3 ni dans l’alerte de 9.5.  
*Preuve :* [S3] Disorders presenting with autonomic failure; [S1] Urogenital Failure.  
*Proposition :* Ajouter « par rapport à la maladie de Parkinson, mais non par rapport à la PSP » en 8.3 et 9.5.

**C22** — `G23_c.html` — Pour l’AMS cérébelleuse établie, MDS 2022 retient l’atrophie ou la diffusivité accrue du putamen, l’atrophie du pont ou du pédoncule cérébelleux moyen, ou le signe de la croix ; « infratentorielle » englobe à tort l’atrophie cérébelleuse, que la ligne exclut ensuite.  
*Preuve :* [S1] Brain MRI markers.  
*Proposition :* Écrire : « Atrophie ou diffusivité accrue du putamen, atrophie du pont ou du pédoncule cérébelleux moyen, signe de la croix ».

## Enrichissements

**E01** — `G23_a.html` — Rubrique 4 : des estimations suisses existent (fiches Parkinson Suisse rédigées par des neurologues suisses) ; la leçon déclare l’absence de toute donnée suisse.  
*Preuve :* [S10] Fiche entière; [S11] Fiche entière.  
*Proposition :* Texte de propositions/G23_a_3.html.

**E02** — `G23_b.html` — Lacune déclarée par la leçon (stridor) comblée par un consensus européen en texte intégral : définition, examens, ventilation en pression positive continue, trachéotomie, incertitude sur la survie.  
*Preuve :* [S5] Treatment of stridor.  
*Proposition :* Texte de propositions/G23_b_5.html.

**E03** — `G23_c.html` — Le bilan urinaire initial recommandé par MDS 2022 (calendrier de 3 jours, toucher rectal, échographie prostatique, résidu échographique) et le piège de la chirurgie prostatique inutile (43 % des hommes) manquent.  
*Preuve :* [S1] Urogenital Failure; [S3] Disorders presenting with autonomic failure.  
*Proposition :* Texte de propositions/G23_c_4.html.

**E04** — `G23_b.html` — Critères européens d’adressage au spécialiste (ERN-RND 2020) absents ; statut de la ligne directrice ERN-RND/EAN/MDS-ES non daté.  
*Preuve :* [S6] Section 1; [S7] Project timeline.  
*Proposition :* Texte de propositions/G23_b_6.html.

**E05** — `G23_a.html` — Le piège des chutes précoces dans l’AMS (28 % la première année ; latence médiane 24 mois contre 118 mois dans la maladie de Parkinson) n’est pas donné ; les chutes seules ne distinguent pas PSP et AMS.  
*Preuve :* [S3] Disorders presenting with parkinsonism; [S1] Supportive features.  
*Proposition :* Ajouter à la carte : « Dans l’AMS, 28 % des patients tombent aussi dès la première année ; la chute précoce isolée ne tranche pas (revue d’Innsbruck, 2023). » Repris dans la fenêtre g23-sm-chutes (propositions/G23_pop2_1.html).

## 21 — Sémiologie fondamentale et analytique

**Statut : absente (constat C01, MAJEUR, bloquant pour la clôture du cours et du lot, AGENTS.md).** Ce n’est pas une simple lacune. L’onglet 1 cite les symptômes (g23-5) et les signes (g23-6) sous forme de listes et de fenêtres. Il ne décrit pas la technique d’examen, ni l’état normal, ni le mécanisme de chaque signe, ni sa valeur chiffrée. Il ne regroupe pas les signes en syndromes, ne propose pas de raisonnement en cinq étapes et ne donne aucun cas corrigé. La proposition `propositions/G23_c_1.html` ajoute la discipline complète selon le contrat `SEMIOLOGIE_FONDAMENTALE_ANALYTIQUE_2026-10-15.yaml` et le modèle D50 : bouton `g23-tab-semio`, panneau `g23-s-semio` (`role="tabpanel"`), neuf sections `data-semiology` (normal à sources), une figure lisible à 390 px et trois cas corrigés. Elle compte environ 3 700 mots. La proposition `propositions/G23_pop2_1.html` ajoute huit fenêtres à `chapters/G23/G23_pop2.html`, fichier admis existant. La proposition `propositions/G23_a_semio_clinique.html` ajoute le marqueur clinique `data-semiology-clinical="G23"` dans le panneau pA (`G23_a.html`, îlot g23-6). Toutes les valeurs proviennent de MDS 2022, de MDS 2017, de la revue d’Innsbruck, de la revue de Munich, du consensus de Bologne, de l’ERN-RND et de Parkinson Suisse.

| Critère | Résultat |
|---|---|
| SEM-01 | non |
| SEM-02 | non |
| SEM-03 | non (discipline absente ; audit_sciences.py en échec sur les cinq disciplines existantes) |
| SEM-04 | oui pour l’état actuel (test_v7.py --static G23 : OK) ; non applicable à la discipline absente |
| SEM-05 | non (tableau g23-5.2 sans mécanisme ni piège) |
| SEM-06 | non |
| SEM-07 | non |
| SEM-08 | partiel (valeurs g23-5.2 sourcées, population indiquée ; attribution erronée C05) |
| SEM-09 | non |
| SEM-10 | partiel (div.trap de g23-5, g23-6) |
| SEM-11 | non |
| SEM-12 | non |
| SEM-13 | non pour la discipline ; div.alert de g23-8 présente |
| SEM-14 | partiel (tableau g23-7.5) |
| SEM-15 | non |
| SEM-16 | non |
| SEM-17 | non (quiz existants hors sémiologie) |
| SEM-18 | non vérifiable (aucun mot vert sémiologique) |
| SEM-19 | oui pour l’existant (sources européennes ; cohorte américaine signalée) |
| SEM-20 | non (C04, C05, C06 : seuils divergents de MDS 2022) |
| SEM-21 | sans objet |
| SEM-22 | non vérifié (aucune capture réelle prise par l’audit) |
| SEM-23 | non (aucune capture réelle prise par l’audit) |
| SEM-24 | oui (bandeau « Aucune validation médicale humaine ») |

Les critères bloquants SEM-01, SEM-02, SEM-03 et SEM-13 sont à « non » pour la discipline : la leçon ne peut pas être déclarée conforme à l’exigence de Vial du 15.10.2026 avant l’intégration de la discipline.

## Matrice des 20 rubriques

| N° | Rubrique | Statut | Ancre |
|---|---|---|---|
| 1 | Question clinique et enjeu pour l’examen fédéral | couvert | g23-0 |
| 2 | Définition et périmètre CIM-10-GM | partiel | g23-1, fenêtre g23-cim ; rattachement de la DCB à G23.8 non vérifié (index alphabétique non lu, ni par la leçon ni par l’audit) |
| 3 | Classifications et stades | couvert | g23-7.1 à 7.3, fenêtres g23-ams-criteres, g23-psp-criteres, g23-scb-criteres ; erreurs C04, C06, C14 |
| 4 | Épidémiologie suisse puis européenne | partiel | g23-2 ; estimations suisses absentes (E01) ; AMS chiffrée par une cohorte américaine de seconde main |
| 5 | Normal → pathologique | partiel | g23-3, g23-s-physio ; disciplines trop brèves (C02) ; normal peu décrit pour les signes (C01) |
| 6 | Étiologies et facteurs de risque | couvert | g23-4, g23-s-gene ; haplotype MAPT H1 absent (proposé en C02) |
| 7 | Anamnèse et symptômes (fréquences) | partiel | g23-5 (cohorte de 30 patients) ; valeurs MDS 2022 et Innsbruck absentes (C01) |
| 8 | Examen clinique (signes, Se/Sp) | partiel | g23-6 et fenêtres ; techniques et sensibilités absentes, attribution erronée C05 |
| 9 | Drapeaux rouges et urgences | partiel | div.alert de g23-8 ; critères d’adressage (E04) et stridor (E02) absents |
| 10 | Examens complémentaires | couvert | g23-e-1 à g23-e-5 ; corrections C05, C22, E03 |
| 11 | Diagnostic différentiel | couvert | g23-7.5 ; liste avant 45 ans incomplète (C13) |
| 12 | Prise en charge suisse (FI datées) | partiel | g23-9, g23-p-1 à g23-p-4 ; sécurité incomplète C08 à C12 ; urologie non sourcée |
| 13 | Complications et pronostic | couvert | g23-8, g23-10 |
| 14 | Suivi, prévention, dépistage | couvert | g23-10 |
| 15 | Situations particulières | partiel | g23-11 ; sujet âgé sans recommandation |
| 16 | Spécificités suisses (AI, conduite, remboursement) | absent | aucune ancre ; seules les ressources de Parkinson Suisse (g23-9.1) ; lacune non comblée par l’audit |
| 17 | Critères formels du diagnostic (div.alert) | couvert | div.alert de g23-12 ; corrections C04 et C06 |
| 18 | Paramètres clés (div.key) | couvert | div.key de g23-12 |
| 19 | Sous-codes CIM-10-GM couverts | couvert | tableau de g23-1 (G23.0 à G23.9) |
| 20 | Points d’examen fédéral | partiel | vignette g23-0, cas g23-11, quiz ; aucune correspondance PROFILES vérifiée |

## Figures

L’outil `tools/image_clo_finder.py inventory G23` recense sept schémas vectoriels pédagogiques non anatomiques (classe SCHEMA_NON_ANATOMIQUE). Il ne trouve aucune image anatomique d’origine IA et aucune image d’origine inconnue. Les cinq pictogrammes de la barre des sciences sont exclus de l’inventaire. Toutes les viewBox mesurent 480 de large au plus. Seule la figure 1 descend sous 10 px de texte à 390 px (constat C20, mineur).

## Contrôles exécutés

- `python3 test_v7.py --static G23` : **OK** (17 842 mots, 63 fenêtres, 5 quiz, 13 Pareto).
- `python3 tests/audit_sciences.py --base 32416a20… --codes G23` : **échec**. Quatre disciplines ont moins de 280 mots, et neuf encadrés de corrélation manquent (C02).
- Toutes les propositions n’utilisent que les classes de la liste fermée de `test_v7.py`, sans style en ligne.

## Lacunes

- Aucune recommandation suisse ni européenne publiée de traitement de l’AMS, de la PSP ou de la DCB : la ligne directrice ERN-RND/EAN/MDS-ES restait en préparation en 2025 [S7] ; recherche PubMed (guideline AND MSA/PSP AND EAN/MDS-ES/ERN-RND, depuis 2023) : 0 résultat pertinent.
- Protocole national français de l’AMS (HAS 2015) non lu : téléchargement refusé (certificat puis HTTP 503).
- Aucune source de sémiologie universitaire suisse (RMS, facultés) trouvée ; recherche web « Revue Médicale Suisse syndromes parkinsoniens atypiques » sans résultat RMS ; fiches Parkinson Suisse utilisées à la place.
- Fréquences de la dysarthrie, de la dysphagie et de la photophobie : non chiffrées dans les sources lues.
- Prise en charge urologique (autosondage, traitement de l’hyperactivité vésicale) : aucune source suisse ou européenne lue.
- Statut suisse de la droxidopa non vérifié.
- Spécificités suisses (aptitude à la conduite, AI, remboursement LS) : non recherchées dans des sources officielles, rubrique 16 absente.
- Rattachement de la DCB à G23.8 dans l’index alphabétique de la CIM-10-GM : non vérifié.
- Fiches Parkinson Suisse n° 129 et 130 : date de publication non relevée.
- Tableaux de MDS 2017 lus par extraction résumée de la page PMC, non verbatim.
- Captures réelles (SEM-22, SEM-23) non prises : discipline absente.
- Essai TIRCON, Lancet Neurology 2024, Nature Reviews Disease Primers 2022, Armstrong 2013 : non relus par l’audit (résumés du dossier de la leçon).

## Sources lues

| Id | Source | Niveau |
|---|---|---|
| S1 | The Movement Disorder Society criteria for the diagnosis of multiple system atrophy (Wenning et al., Mov Disord 2022;37:1131-1148) (2022) | texte_integral |
| S2 | Clinical diagnosis of progressive supranuclear palsy: the Movement Disorder Society criteria (Höglinger et al., Mov Disord 2017;32:853-864) (2017) | texte_integral |
| S3 | A review on the clinical diagnosis of multiple system atrophy (Stankovic, Fanciulli, Sidoroff, Wenning; Cerebellum 2023;22:825-839) (2023) | texte_integral |
| S4 | 4-Repeat Tauopathien – Progressive Supranukleäre Blickparese und kortikobasale Degeneration (Palleis, Bernhardt, Höglinger; Fortschr Neurol Psychiatr 2026;94:389-399) (2026) | texte_integral |
| S5 | Stridor in multiple system atrophy: consensus statement on diagnosis, prognosis, and treatment (Cortelli et al., Neurology 2019;93:630-639) (2019) | texte_integral |
| S6 | Información breve y específica sobre el diagnóstico del parkinsonismo atípico para neurólogos generales/médicos generales (Machetanz, Gasser, Meissner) (30.06.2020) | texte_integral |
| S7 | ERN-RND/EAN/MDS-ES Guidelines on the symptomatic treatment of Atypical Parkinsonian Syndromes (poster, assemblée annuelle 2025) (2025) | texte_integral |
| S8 | 2018 ESC Guidelines for the diagnosis and management of syncope (2018) | section |
| S9 | Syndromes parkinsoniens atypiques (Prof. D. Benninger, Reha Rheinfelden) (2025) | texte_integral |
| S10 | L’atrophie multisystématisée (AMS), série « Les syndromes parkinsoniens atypiques », partie 1 (Prof. M. Sturzenegger), magazine Parkinson n° 129 (date non relevée (magazine n° 129)) | texte_integral |
| S11 | La paralysie supranucléaire progressive (PSP), série « Les syndromes parkinsoniens atypiques », partie 2 (Prof. J.-A. Ghika, Hôpital du Valais), magazine Parkinson n° 130 (date non relevée (magazine n° 130)) | texte_integral |
| S12 | Information professionnelle suisse Gutron® (chlorhydrate de midodrine), GTIN 7680449770288 (Mise à jour mars 2021) | texte_integral |
| S13 | Information professionnelle suisse PK-Merz® (sulfate d’amantadine), GTIN 7680441350273 (Mise à jour février 2025) | texte_integral |
| S14 | Information professionnelle suisse Madopar® (lévodopa/bensérazide), GTIN 7680380960953 (Mise à jour juin 2023) | section |
| S15 | Information professionnelle suisse Xeomin® (incobotulinumtoxine A), GTIN 7680620800018 (Mise à jour mars 2026) | section |
| S16 | Information professionnelle suisse Florinef® (fludrocortisone), GTIN 7680310950184 (Mise à jour mars 2026) | section |
| S17 | Information professionnelle suisse Ferriprox® (défériprone), GTIN 7680556790025 (Mise à jour mars 2022) | section |
| S18 | Information professionnelle suisse Midodrin Substipharm (chlorhydrate de midodrine), GTIN 7680693840058 (Mise à jour mai 2024) | section |

La première source lue est le poster ERN-RND/EAN/MDS-ES de 2025 [S7], lu en entier. Les autres affirmations vérifiées reposent sur le texte intégral, sauf l’ESC 2018 et les FI de Madopar®, de Xeomin®, de Florinef®, de Ferriprox® et de Midodrin, lues par section.

## Tableau de bord

| Élément | Valeur |
|---|---|
| Leçon | G23 — Autres maladies dégénératives des noyaux gris centraux (N-05-Neurologie, chantier S08) |
| Catégories traitées | G23.0, G23.1, G23.2, G23.3, G23.8, G23.9 |
| Fichiers audités | 7 (222 171 octets), empreintes conformes |
| Constats | 11 majeurs, 11 mineurs, 5 enrichissements, 0 bloquant |
| Propositions | 16 fichiers HTML, dont la discipline Sémiologie (≈ 3 700 mots) et 8 fenêtres |
| Sources | 18, dont 7 informations professionnelles suisses datées |
| Alertes | Sémiologie absente (MAJEUR bloquant la clôture) ; audit_sciences en échec ; quatre erreurs de critères (C04 à C07) ; trois omissions de sécurité tirées des FI (C08 à C10) |

*Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.*
