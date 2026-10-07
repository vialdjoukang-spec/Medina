# C-01-Cardiologie — I50 — dossier de relecture et corrections

Version du 7 octobre 2026. Ce dossier réunit les corrections ciblées, le rapport systématique et ses deux annexes. Il peut être lu seul. Les extraits et lignes du rapport correspondent aux sources avant corrections ; les états décrivent les corrections committées ensuite. L’inventaire JSON conserve les chemins, la couverture et les sources.

**NON ACHEVÉ.** 99 groupes de constats sont recensés : 6 corrigés ciblés, 7 partiellement corrigés et 86 à traiter. Leurs concepts ne sont pas tous certifiés. Les sources suisses, les mécanismes, les figures, les posologies et les indications qui restent ouverts doivent encore être repris et justifiés localement.

Corrections de source : `de86fcc1792424e4a0a933ace0e7a5213475f727`. En-tête administratif : `bec9849`, réalisé par l’orchestrateur. Couverture lue : huit HTML, 739 unités HTML avant corrections, 167 définitions candidates de glossaire et les 21 entrées de justification. Les 38 URL de la banque sont inventoriées ; leur contenu n’est pas entièrement vérifié.

Les classements de priorité des annexes sont conservés et définis dans leurs textes ; ils ne constituent pas un score commun. La compilation en mémoire de 21 fenêtres et 21 cibles vérifie leurs ancres, pas la validité de chaque affirmation.



# État des corrections et réserves


Les contradictions ciblées ont été corrigées dans les sources canoniques au commit `de86fcc1792424e4a0a933ace0e7a5213475f727`. Le parcours de tous les fichiers a révélé d’autres lacunes. **La justification médicale de chaque affirmation reste NON ACHEVÉE.** Une compilation réussie ne change pas ce statut.

## Corrections injectées

Les références ci-dessous ont été ouvertes ou vérifiées dans leur publication primaire. L’accès complet aux diapositives ESC 2026 ne signifie pas que l’intégralité de l’article OUP a été lue.

| Sujet | Sources modifiées | Correction et limite conservée | Référence primaire |
|---|---|---|---|
| BNP sous ARNI | `I50_b.html` §7.2 ; `I50_c.html` §e-2, quiz 2 et §sb-i ; `I50_pop4.html` d-arni et Pareto diagnostic, biologie, sciences | Le BNP peut augmenter au début et reste pronostique. Le NT-proBNP n’est pas directement dégradé par la néprilysine ; il peut varier avec la maladie et le rein. Deux dosages ne prouvent pas seuls une amélioration ni la nécessité d’augmenter un diurétique. | [Myhre 2019, analyse PARADIGM-HF](https://doi.org/10.1016/j.jacc.2019.01.018) |
| HFA-PEFF en fibrillation auriculaire | `I50_b.html` §7.2 ; `I50_pop3.html` h2fpef | Le critère mineur NT-proBNP est 375–660 pg/mL. Les seuils e′ propres au score sont adaptés à l’âge de 75 ans. Le score de consensus garde sa population et sa démarche ; il n’est pas assimilé au tableau ASE. | [Consensus HFA-PEFF original](https://doi.org/10.1002/ejhf.1741) ; PDF auteur consulté |
| Échographie et ICFEp | `I50_a.html` §3.1 ; `I50_c.html` §e-3 et quiz 1 ; `I50_pop4.html` Pareto examens | Une FEVG préservée ne garantit pas une fonction systolique normale. Les seuils e′ suivent les groupes d’âge ASE 2025. E/e′ et la taille de l’OG sont des indices indirects ; la FA, les valves et le haut débit peuvent dilater l’OG. | [ASE 2025, tableaux 4 et 6](https://www.asecho.org/wp-content/uploads/2025/07/Left-Ventricular-Diastolic-Function.pdf) |
| FEVG et dispositifs | `I50_c.html` tableau e-3 | Le seuil de phénotype ≥50 % est distingué d’une borne physiologique de normalité. FEVG ≤35 % contribue à des indications sélectionnées ; elle ne les décide pas seule. | [ESC 2026, diapositives officielles](https://dam-assets.escardio.org/download/b2e587389baa11f185de06bdfb3e4be9) |
| CRT, largeur QRS et délais | `I50_b.html` §9.4 ; `I50_c.html` ECG ; `I50_pop3.html` ecg-ic et crt ; `I50_pop4.html` Pareto traitement et examens | Le profil classique conserve symptômes, FEVG ≤35 %, rythme sinusal, BBG et QRS ≥150 ms. La planification simultanée à l’initiation de la TMF est une option sélectionnée IIb. Le délai du DAI primaire n’est pas imposé à toute CRT. QRS <130 ms garde l’exception de stimulation pour BAV de haut degré. Le non-BBG n’annule pas toute indication. | ESC 2026, diapositives 56–57, intégralement disponibles |
| I NEED HELP | `I50_pop3.html` ineedhelp ; `glossary/cardio_2.py` définition effective | FEVG <20 % **ou mauvaise fonction VD**, selon la version 2026. Un signal invite à discuter un recours spécialisé ; il ne confirme pas seul le stade D. | ESC 2026, diapositive 71, texte et figure consultés |
| Créatinine sous traitement | `I50_d.html` §p-4 ; `I50_pop4.html` Pareto pharmacologie | La hausse <50 % et la valeur restant <266 µmol/L sont associées. Le repère alternatif ESC 2021 est une baisse de DFG <10 % avec maintien >25. La trajectoire, le potassium, la pression et la congestion restent à évaluer. Le contexte CKD et la réévaluation KDIGO au-delà de 30 % dans quatre semaines sont précisés. | [ESC 2021 intégral, §13.4](https://www.heartfailurematters.org/wp-content/uploads/2022/05/ESC-Heart-Failure-Guidelines-2021.pdf) ; [KDIGO 2024, points 3.6.2–3.6.5](https://kdigo.org/wp-content/uploads/2024/03/KDIGO-2024-CKD-Guideline.pdf) |
| Hypotension et diurétiques | `I50_d.html` §p-4 ; `I50_pop4.html` Pareto pharmacologie | La réduction du diurétique dépend de l’absence de congestion, notamment d’une hypovolémie. Une hypotension asymptomatique n’est pas une autorisation universelle de maintenir toute dose. Une hypoperfusion exige une évaluation urgente. | ESC 2021 et KDIGO 2024, conduite contextualisée |
| Hyperkaliémie | `I50_d.html` §p-4 ; `I50_pop4.html` Pareto pharmacologie | La réduction universelle de moitié « ARM ou IEC » est retirée. L’adaptation dépend de la molécule, de la dose et de sa notice. ≥6,0 mmol/L appelle une évaluation urgente. La recherche d’hémolyse ne retarde pas le traitement d’un résultat menaçant. | [RCP fabricant Inspra, tableau 1, mars 2026](https://www.medicines.org.uk/emc/product/120/smpc) ; KDIGO 2024. L’exemple britannique ne remplace pas l’information suisse. |
| Dronédarone | `I50_d.html` §p-5 | La contre-indication suisse inclut l’insuffisance cardiaque ou la dysfonction systolique VG ; elle n’est pas limitée à FEVG ≤40 % ou à l’instabilité. | [Multaq, information professionnelle suisse](https://compendium.ch/fr/product/1134151-multaq-cpr-pell-400-mg) |
| Vériciguat et interactions | `I50_pop4.html` d-veri | Les nitrés nécessitent une prudence, surtout prolongés ; ils ne sont pas tous contre-indiqués. PDE5 : association non recommandée. Autre stimulateur sGC, tel riociguat : contre-indication. La dose du tableau ESC 2026 est conservée. | [RCP fabricant Verquvo, §4.3–4.5](https://www.medicines.org.uk/emc/product/12774/smpc) |
| Finérénone | `I50_d.html` tableau p-2 | La ligne explicite FINEARTS-HF, FEVG ≥40 %, et renvoie à la stratégie ICFEp. Elle n’enseigne plus implicitement un remplacement de tous les ARM stéroïdiens dans toute ICFEr. | [FINEARTS-HF original](https://doi.org/10.1056/NEJMoa2407107) ; ESC 2026 |
| Choc cardiogénique | `I50_b.html` §8.1 ; `I50_pop2.html` v-ta ; `I50_pop4.html` choc | Une pression conservée et un lactate normal n’excluent pas tout choc. Le stade E ne se limite pas à un arrêt cardiaque. Le stade décrit gravité et évolution ; il ne prescrit pas seul une assistance. | [Consensus SCAI 2022 intégral](https://www.sts.org/sites/default/files/Expert%20Consensus/SCAI%20SHOCK.pdf) |
| Poids | `I50_a.html` §5.2 ; `I50_pop2.html` poidssec ; `I50_pop4.html` Pareto clinique | +2 kg en trois jours reste une alerte faisant suspecter une rétention. Ce seuil ne prouve pas seul la congestion. Le plan écrit, les symptômes et la tolérance guident la suite. | ESC, éducation et autosurveillance ; inférence clinique explicitée |
| Gs/Gq | `glossary/j45.py` définitions effectives | Gs inclut β1 cardiaque et β2 bronchique, avec voie adénylate cyclase/AMP cyclique. Gq inclut AT1 et M3, phospholipase C et mobilisation du calcium. Les seconds messagers sont développés en toutes lettres. La réponse dépend du tissu. | [IUPHAR/BPS, Concise Guide 2025/26](https://doi.org/10.1111/bph.70230), PDF intégral consulté |

Le dossier du cours est `chapters/I50/`. Les neuf fichiers sources committés sont les sept HTML cités, `glossary/j45.py` et `glossary/cardio_2.py`. `I50_pop1.html` et la banque JSON n’ont pas été modifiés. Les sorties générées et le moteur n’ont pas été modifiés par ce lot.

L’orchestrateur a ensuite retiré l’ancien score automatique dans l’en-tête I50 au commit `bec9849`, en conservant le référentiel et la réserve de revue indépendante. Le constat I50-001 est partiellement corrigé ; les sources suisses et celles de l’examen restent à vérifier.

## Vérification effectuée

- Compilation **en mémoire** : 21 entrées, 21 fenêtres, 21 cibles trouvées. Le champ `exhaustive_review` reste `false`.
- Comparaison avant/après des huit HTML : mêmes IDs, clés `data-pop`, boutons `data-k`, valeurs `data-ok` et SVG identiques.
- Syntaxe Python des deux glossaires et contrôle de leurs définitions après fusion : réussis.
- `git diff --check` : réussi. Aucun build ou contrôle navigateur exécuté par cet agent ; ils sont confiés à l’orchestrateur.
- Instantané original et journal des modifications conservés hors des sources. Les anciennes remises ne sont pas remplacées par ces instantanés.

## Lacunes restantes à reprendre

Le rapport systématique et son annexe popups détaillent les sections. Les corrections ci-dessus n’ajoutent pas encore toutes les fenêtres locales demandées. Une partie des contre-indications, posologies, adaptations rénales, indications et mécanismes reste à justifier avec les sources suisses et les essais originaux.

Les figures de Frank-Starling, pression-volume et fibrose restent à reprendre. Certaines légendes ne décrivent pas correctement la géométrie effectivement dessinée. Les SVG ont été conservés conformément au périmètre de ce lot ; leur conservation technique ne valide pas leur valeur médicale.

Restent notamment ouverts : mécanique Frank-Starling réduite au chevauchement, tamponnade et peptides, récupération après anthracyclines, cardiomyopathie rythmique liée aux ESV, gadolinium et groupes d’agents, viabilité/revascularisation, nuances des essais et critères composites, généralisation de plusieurs traitements au stade B, restrictions hydriques, grossesse et statut suisse du tolvaptan. Les autres définitions globales d’échographie et les résumés d’essais restent à harmoniser.

Les 38 URL de la banque sont recensées ; leur contenu n’a pas été intégralement vérifié dans ce lot. Certains accès ont échoué ou se limitent à un résumé indexé. Une référence générale à un guideline ne suffit pas à documenter chaque mécanisme expérimental.

La couverture réelle est une lecture des huit HTML, des 21 entrées de la banque et des définitions repérées dans le texte complet. Elle n’est ni une certification de chaque phrase ni un inventaire achevé de la CIM-11. **L’état final demeure NON ACHEVÉ.**


# Rapport systématique : 90 constats initiaux


**NON ACHEVÉ.** Cette relecture porte sur les huit fichiers HTML, la banque de 21 justifications et les définitions de glossaire repérées dans le texte complet. Elle décrit des lacunes explicatives, des limites de contexte et des contradictions. Elle ne certifie aucune phrase. Des corrections ciblées ne suffisent pas à déclarer la leçon médicalement achevée.

La lecture préalable et la réécriture de ce rapport ont été effectuées sans modifier le dépôt, les tests, les fichiers dist ou le build. Les 90 identifiants, priorités et références des constats initiaux sont conservés. Leur rédaction et leurs citations ont été clarifiées. Les états de correction ont été actualisés selon les modifications signalées par le responsable de l’audit dans le commit `de86fcc1792424e4a0a933ace0e7a5213475f727`, puis dans le commit `bec9849` pour l’en-tête : **6 corrections ciblées, 7 corrections partielles et 77 constats à traiter**. Les citations, les lignes et les décomptes décrivent toujours l’instantané avant corrections. Une correction ciblée ne certifie jamais tous les concepts du constat.

## Couverture et méthode corrigées

| Source | Lignes | Unités HTML | Lecture |
|---|---:|---:|---|
| `chapters/I50/I50_a.html` | 127 | 132 | Fichier complet |
| `chapters/I50/I50_b.html` | 109 | 104 | Fichier complet |
| `chapters/I50/I50_c.html` | 182 | 168 | Fichier complet |
| `chapters/I50/I50_d.html` | 69 | 63 | Fichier complet |
| `chapters/I50/I50_pop1.html` | 71 | 44 | Fichier complet |
| `chapters/I50/I50_pop2.html` | 78 | 45 | Fichier complet |
| `chapters/I50/I50_pop3.html` | 75 | 50 | Fichier complet |
| `chapters/I50/I50_pop4.html` | 133 | 133 | Fichier complet |
| **Total des huit fichiers** | **844** | **739** | |

Le décompte initial affichait à tort zéro unité pour I50_a et les quatre fichiers de popups : `BeautifulSoup.get_text()` omettait les objets `TemplateString`. Ce défaut d’inventaire a été corrigé. Le recomptage utilise exclusivement le contenu de l’instantané avant corrections ; les huit empreintes SHA-256 et les nombres de lignes sont inchangés.

Une unité est un élément `p`, `li`, `tr`, `figcaption`, `button` ou `text` dont le texte normalisé n’est pas vide. L’extraction inclut `NavigableString` et `TemplateString`. Les boutons sont retenus seulement avec `data-ok` ou `data-k` ; les `p/li` imbriqués dans un autre `p/li` sont exclus. Les lignes proviennent de `html.parser.sourceline`. Les légendes, boutons et textes SVG peuvent recouvrir une autre unité ; une unité peut contenir plusieurs affirmations ou du texte de navigation. Les **739 unités ne sont donc ni 739 assertions cliniques distinctes ni un taux de vérification médicale**.

**Banque :** 21 entrées lues, 38 URL distinctes inventoriées. Le contenu de ces 38 sources n’a pas été intégralement vérifié. **Glossaire : 167 définitions repérées dans le texte complet, lues**, dont 63 ajoutées après correction du défaut d’extraction des templates. Il n’existe pas de `glossary/i50.py` ; les définitions viennent de la fusion effective des modules et de leurs éventuels écrasements. Le repérage par expression régulière peut aussi retenir certains sous-termes d’un sigle composé : 167 n’est pas un comptage exact des liaisons effectuées par le moteur. Les définitions et leurs origines sont conservées dans `glossary_consumed` ; les 63 lectures complémentaires sont documentées dans [I50_GLOSSAIRE_COMPLEMENT_2026-10-07.json](sandbox:/workspace/scratch/6eaecafb4b19/I50_GLOSSAIRE_COMPLEMENT_2026-10-07.json).

Les 90 extraits ci-dessous sont courts, continus et retrouvés dans les sources avant corrections, après retrait du balisage et normalisation des espaces. Ils servent à localiser un passage ; ils ne reproduisent pas toutes les affirmations regroupées dans le constat. La banque et `glossary/cardio_1.py`, confirmés inchangés dans ce lot par le responsable de l’audit, ont été ajoutés à l’instantané depuis leurs contenus canoniques stables. La vérification d’une citation ne valide pas son contenu médical.

Le référentiel ESC 2026 a été retrouvé. Le seuil ICFEr < 50 %, la suppression de la catégorie HFmrEF, la nomenclature DHF et les recommandations récentes sur les ARM et les incrétines ne sont pas des erreurs du seul fait de leur différence avec 2021. Le diaporama officiel a été consulté ; la lecture intégrale de l’article OUP n’est pas attestée. Mécanismes plausibles, résultats composites d’essais et classes de recommandation constituent des preuves de nature différente.

Les neuf constats complémentaires I50-091 à I50-099 sont détaillés dans [I50_GLOSSAIRE_LACUNES_COMPLEMENT_2026-10-07.md](sandbox:/workspace/scratch/6eaecafb4b19/I50_GLOSSAIRE_LACUNES_COMPLEMENT_2026-10-07.md). Tous restent à traiter. L’inventaire JSON rassemble désormais **99 groupes de constats : 6 corrigés ciblés, 7 partiels et 86 à traiter**. Ce nombre mesure des groupes de lacunes identifiées, sans décompter toutes les phrases ni établir un score médical.

## Les 90 constats initiaux

**P0** : contradiction pouvant tromper une décision. **P1** : précision clinique ou actualisation nécessaire. **P2** : justification, contexte ou référence insuffisante. Les états indiqués décrivent la portée des corrections signalées après le commit cité. « Corrigé ciblé » concerne les formulations visées ; « partiellement corrigé » conserve explicitement les éléments ouverts ; « à traiter » signale l’absence de correction dans ce lot. Quand cela aide l’apprentissage, ajouter une fenêtre locale expliquant la chaîne causale, la raison clinique, les limites et les sources, en réutilisant les fenêtres existantes.

### I50-001 — P1

**Source :** `chapters/I50/I50_a.html`, ligne 4 — En-tête et §0–1.

**Extrait :** « Validation interne 20/20 »

**Lacune :** Le score affiché ne décrit pas un contrôle de la justification de chaque affirmation. L’adoption du référentiel en Suisse et la préparation à l’examen fédéral ne sont pas rattachées à des sources précises.

**Correction proposée :** Remplacer le score de validation par une description factuelle du contrôle effectué. Identifier le référentiel, sa date et les sources suisses vérifiées ; signaler explicitement celles qui restent à trouver.

**Références de ce constat :** S01. **État de correction :** partiellement corrigé.

**Portée de la correction :** Le score automatique de l’en-tête a été retiré dans le commit bec9849 et remplacé par « Révision des justifications en cours ». Le référentiel et les réserves sont conservés. Les sources suisses et la préparation à l’examen fédéral restent ouvertes. L’extrait cité reste celui de l’instantané avant correction.

### I50-002 — P2

**Source :** `chapters/I50/I50_a.html`, ligne 27 — §1.1 et table.

**Extrait :** « partagent la physiopathologie et la réponse thérapeutique »

**Lacune :** La nouvelle nomenclature a été vérifiée, mais la justification de la fusion présente les patients comme un groupe trop homogène. Les preuves obtenues initialement pour une FEVG ≤ 40 % ne deviennent pas identiques pour une FEVG de 41 à 49 %.

**Correction proposée :** Ajouter une fenêtre de classification qui explique le continuum de FEVG et la variabilité de sa mesure. Distinguer le seuil du référentiel 2026 des populations effectivement étudiées dans chaque essai.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-003 — P2

**Source :** `chapters/I50/I50_a.html`, ligne 33 — §1.2 quatre stades.

**Extrait :** « Le stade ne régresse pas »

**Lacune :** La formulation est absolue. Les stades B et D sont résumés sans leurs critères ni leur justification ; une élévation isolée des peptides natriurétiques ne permet pas à elle seule de classer toutes les situations.

**Correction proposée :** Décrire le rôle de l’histoire des symptômes, les facteurs qui influencent les biomarqueurs et les critères de l’insuffisance cardiaque avancée. Rattacher ces précisions au référentiel 2026.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-004 — P2

**Source :** `chapters/I50/I50_a.html`, ligne 40 — §1.3–1.4.

**Extrait :** « mesure la gêne fonctionnelle actuelle »

**Lacune :** La classification NYHA est déjà accessible dans une fenêtre, mais ses conditions d’évaluation, sa variabilité entre évaluateurs et le manque de spécificité des symptômes restent à expliquer. Le choix du terme DHF ne justifie pas de considérer tous les tableaux aigus comme équivalents.

**Correction proposée :** Compléter les limites de la classification NYHA. Distinguer l’insuffisance cardiaque de novo, la congestion progressive et l’œdème pulmonaire brutal, avec leur contexte clinique.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-005 — P2

**Source :** `chapters/I50/I50_a.html`, ligne 48 — §2 trois paragraphes.

**Extrait :** « environ la moitié des patients décèdent »

**Lacune :** Les chiffres de prévalence, de répartition selon le sexe, d’incidence et de mortalité à cinq ans ne précisent ni cohorte, ni date, ni dénominateur, ni incertitude. L’âge est présenté comme le premier déterminant sans source précise. Chaque réhospitalisation est décrite comme une aggravation causale, alors qu’elle peut également témoigner de la sévérité de la maladie.

**Correction proposée :** Ajouter, pour chaque chiffre et chaque affirmation pronostique, la population, la période et la source primaire. Distinguer incidence et prévalence, ainsi qu’association pronostique et effet causal. Une cohorte primaire contemporaine reste à vérifier.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-006 — P1

**Source :** `chapters/I50/I50_a.html`, ligne 56 — §3.1.

**Extrait :** « le ventricule se contracte normalement »

**Lacune :** Une FEVG préservée ne signifie pas que toute la fonction systolique est normale. La réserve contractile et le strain longitudinal global (GLS) peuvent être altérés.

**Correction proposée :** Décrire une fraction d’éjection préservée malgré des anomalies possibles de relaxation, de compliance et de fonction systolique. Expliquer ce que la FEVG mesure et ce qu’elle ne suffit pas à exclure.

**Références de ce constat :** S02. **État de correction :** corrigé ciblé.

**Portée de la correction :** La formulation sur une contraction normale malgré une FEVG préservée a été corrigée. Cette correction ciblée ne certifie pas tous les concepts du constat.

### I50-007 — P2

**Source :** `chapters/I50/I50_a.html`, ligne 58 — §3.1–3.2.

**Extrait :** « Le rein perçoit une baisse du débit comme une hypovolémie »

**Lacune :** L’explication réduit l’insuffisance cardiaque au bas débit. La congestion veineuse rénale, la baisse du volume artériel efficace, le baroréflexe sympathique et le signal de sodium à la macula densa restent à expliquer.

**Correction proposée :** Réutiliser la fenêtre consacrée au rein et compléter la séquence capteurs → réponses. Expliquer la congestion veineuse et distinguer une hypovolémie totale d’un sous-remplissage artériel efficace.

**Références de ce constat :** S06. **État de correction :** à traiter.

### I50-008 — P2

**Source :** `chapters/I50/I50_a.html`, ligne 59 — §3.2, corrélation et figure 1.

**Extrait :** « bloquent chacune un maillon de ce cercle vicieux »

**Lacune :** Les inhibiteurs de SGLT2 ne se résument pas au blocage d’un maillon neurohormonal. Certains mécanismes métaboliques restent des hypothèses contributives. Les diurétiques symptomatiques et les traitements de fond ne disposent pas des mêmes preuves cliniques.

**Correction proposée :** Préciser les cibles des médicaments et distinguer les mécanismes établis, les hypothèses et les bénéfices cliniques démontrés. Indiquer dans la légende que les liens sont schématiques et que les mécanismes des inhibiteurs de SGLT2 sont pluriels.

**Références de ce constat :** S01, S07, S08. **État de correction :** à traiter.

### I50-009 — P2

**Source :** `chapters/I50/I50_a.html`, ligne 61 — §3.3.

**Extrait :** « c’est la dyspnée, l’orthopnée et les crépitants »

**Lacune :** Le mécanisme général est introduit, mais la fatigue, les extrémités froides, l’oligurie, la confusion et les manifestations de congestion droite ne disposent pas tous d’une explication locale. Leurs limites et leurs diagnostics différentiels sont insuffisamment précisés.

**Correction proposée :** Relier chaque signe aux pressions, à la perfusion ou au travail respiratoire dans des fenêtres courtes. Indiquer leur caractère non spécifique et réutiliser les fenêtres sur les œdèmes et l’orthopnée lors des répétitions.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-010 — P2

**Source :** `chapters/I50/I50_a.html`, ligne 63 — §3.4.

**Extrait :** « explique l’échec historique des traitements neurohormonaux isolés »

**Lacune :** Le modèle d’inflammation microvasculaire est présenté comme une explication exhaustive de l’échec ou du succès des traitements, sans tenir compte de l’hétérogénéité de l’ICFEp.

**Correction proposée :** Présenter ce modèle comme une contribution physiopathologique. Expliquer les mécanismes distincts et les critères de sélection des essais thérapeutiques. Une source primaire précise reste nécessaire pour la portée attribuée au modèle.

**Références de ce constat :** S01, S02. **État de correction :** à traiter.

### I50-011 — P2

**Source :** `chapters/I50/I50_a.html`, ligne 81 — §4, cartes des causes.

**Extrait :** « bradycardies ; stimulation ventriculaire droite chronique »

**Lacune :** Les listes étiologiques n’expliquent pas les liens causaux des cardiomyopathies, de l’hypertension, des valvulopathies, des toxiques, de la stimulation ventriculaire droite, des bradycardies ou des états de haut débit et de la carence en thiamine. Les fenêtres sur l’amylose et la cardiomyopathie rythmique ne couvrent pas toutes ces causes.

**Correction proposée :** Regrouper les explications selon les mécanismes : surcharge de pression, surcharge de volume, perte de myocytes, infiltration, troubles du rythme et haut débit. Préciser le contexte qui conduit à rechercher chaque cause.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-012 — P1

**Source :** `chapters/I50/I50_a.html`, ligne 84 — §4.1 ischémie.

**Extrait :** « selon l’anatomie, la viabilité et les symptômes »

**Lacune :** La formulation peut laisser croire que la viabilité suffit à sélectionner les patients qui bénéficieront d’une revascularisation sur le pronostic, ou que l’angioplastie et le pontage apportent des preuves équivalentes.

**Correction proposée :** Distinguer le traitement de l’angor ou d’un syndrome coronarien aigu, l’évaluation anatomique par la Heart Team et les preuves du pontage. Ne pas utiliser la viabilité comme critère isolé de bénéfice pronostique de l’angioplastie ou du pontage.

**Références de ce constat :** S09, S10. **État de correction :** à traiter.

### I50-013 — P2

**Source :** `chapters/I50/I50_a.html`, ligne 85 — §4.1 toutes lignes hors ischémie.

**Extrait :** « correction chirurgicale ou percutanée »

**Lacune :** Les traitements étiologiques — biopsie et immunosuppression de certaines myocardites, abstinence, traitement du rythme, traitement ciblant la transthyrétine, saignées ou chélation — sont cités sans mécanisme, limites ni critères de sélection.

**Correction proposée :** Créer une fenêtre par traitement causal pour expliquer la sélection des patients et ses conséquences diagnostiques. Préciser que les saignées ne sont pas universelles dans l’hémochromatose, notamment en cas d’anémie ou d’insuffisance cardiaque sévère. Les références spécifiques restent à rechercher.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-014 — P2

**Source :** `chapters/I50/I50_a.html`, ligne 91 — §4.2.

**Extrait :** « c’est souvent lui qu’il faut traiter en premier »

**Lacune :** Les effets d’un apport salé, de la non-observance, de l’infection, de la fibrillation auriculaire et des glitazones ne sont pas expliqués. La priorité thérapeutique dépend de l’urgence, du besoin de stabilisation et du mécanisme déclenchant.

**Correction proposée :** Expliquer l’augmentation de la demande et les effets inflammatoires de l’infection, les conséquences de la fibrillation auriculaire sur le rythme et le remplissage, l’arrêt des traitements et la rétention liée aux glitazones. Compléter les causes urgentes selon le référentiel 2026, dont l’infection et la tamponnade.

**Références de ce constat :** S01, S08. **État de correction :** à traiter.

### I50-015 — P2

**Source :** `chapters/I50/I50_a.html`, ligne 101 — §5.1 antécédents.

**Extrait :** « Histoire familiale de cardiomyopathie ou de mort subite »

**Lacune :** Le motif des recherches cliniques reste souvent implicite : hérédité, épaisseur des parois, amylose, exposition aux toxiques et terrain cardiovasculaire. Seules les recherches coronariennes et la cardiotoxicité disposent d’une fenêtre explicite.

**Correction proposée :** Ajouter le contexte et la valeur des signes d’alerte qui motivent chaque recherche. Expliquer qu’un signe isolé, tel qu’un canal carpien bilatéral, ne suffit pas à diagnostiquer une amylose.

**Références de ce constat :** S01, S11. **État de correction :** à traiter.

### I50-016 — P2

**Source :** `chapters/I50/I50_a.html`, ligne 102 — §5.2.

**Extrait :** « Symptômes par ordre de fréquence »

**Lacune :** L’ordre de fréquence n’est pas référencé. La nycturie, la toux, l’anorexie, la satiété précoce, les symptômes de l’hypochondre, la fatigue et les variations de poids ne sont pas tous expliqués par leur mécanisme.

**Correction proposée :** Supprimer le classement non vérifié ou lui associer une source primaire appropriée, qui reste à trouver. Expliquer la redistribution rénale nocturne et la congestion abdominale, ainsi que le manque de spécificité de ces symptômes.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-017 — P1

**Source :** `chapters/I50/I50_a.html`, ligne 106 — §5.2 et I50_b, §10.

**Extrait :** « plus de 2 kg en trois jours signe une rétention hydrique »

**Lacune :** Un seuil d’alerte pour l’autosurveillance devient une preuve diagnostique de rétention hydrique. Le poids peut varier pour d’autres raisons.

**Correction proposée :** Indiquer qu’une telle variation fait suspecter une rétention et déclenche un contact selon le plan personnalisé. Préciser les conditions reproductibles de la pesée et rappeler que le poids seul ne prouve pas une congestion.

**Références de ce constat :** S01. **État de correction :** corrigé ciblé.

**Portée de la correction :** Le seuil de variation de poids a été reformulé comme un signal d’alerte, sans preuve diagnostique automatique. Cette correction ciblée ne certifie pas tous les concepts du constat.

### I50-018 — P1

**Source :** `chapters/I50/I50_a.html`, ligne 110 — §5.3 forme atypique.

**Extrait :** « ICFEp méconnue »

**Lacune :** L’exemple associant FEVG à 60 %, fibrillation auriculaire, anomalie de l’oreillette gauche et NT-proBNP à 900 énonce le diagnostic sans démonstration intégrée ni diagnostic différentiel. Le classement NYHA III n’est pas relié à une activité concrètement limitée.

**Correction proposée :** Décrire les symptômes, la limitation fonctionnelle et les éléments qui augmentent la probabilité diagnostique. Examiner les autres causes de fatigue et présenter l’ICFEp comme une conclusion qui nécessite une confirmation appropriée.

**Références de ce constat :** S02, S05. **État de correction :** à traiter.

### I50-019 — P2

**Source :** `chapters/I50/I50_a.html`, ligne 118 — §6.1–6.2 signes.

**Extrait :** « Dyspnée au repos ou à la parole, cyanose, marbrures. »

**Lacune :** La fréquence et la régularité cardiaques, la fréquence respiratoire, la SpO2, la température, le poids et l’anthropométrie ne sont pas reliés à leurs causes ou à la gravité. Le souffle d’insuffisance tricuspide, l’épanchement pleural, le choc de pointe, la pression différentielle, la macroglossie et les ecchymoses restent présentés sous forme de listes.

**Correction proposée :** Regrouper les signes dans des fenêtres qui expliquent leur mécanisme et l’intérêt de les rechercher. Préciser leur spécificité, l’effet de l’âge ou de la position et les limites d’interprétation.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-020 — P2

**Source :** `chapters/I50/I50_a.html`, ligne 125 — §6 piège.

**Extrait :** « le signe de congestion le plus fiable »

**Lacune :** Le superlatif appliqué à la turgescence jugulaire n’est pas contextualisé par la technique d’examen et sa variabilité. L’explication par l’adaptation lymphatique n’est pas rattachée à une étude primaire précise.

**Correction proposée :** Décrire l’estimation de la pression droite, les limites liées à l’obésité, à la position et à la ventilation, ainsi que la confrontation avec les autres données cliniques. Trouver une référence primaire pour l’affirmation sur l’adaptation lymphatique.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-021 — P1

**Source :** `chapters/I50/I50_b.html`, ligne 3 — §7.1–7.2.

**Extrait :** « les inverser gaspille des ressources »

**Lacune :** L’ordre des examens est formulé comme une règle trop impérative. Une forte suspicion, une urgence ou une valvulopathie peuvent justifier une échocardiographie d’emblée ; la figure évoque déjà cette exception.

**Correction proposée :** Adapter le parcours ambulatoire à la probabilité diagnostique, à la disponibilité des examens et à la gravité. Rendre les exceptions explicites dans le texte et les fenêtres.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-022 — P1

**Source :** `chapters/I50/I50_b.html`, ligne 11 — §7.2, ligne 11, et pop3.

**Extrait :** « NT-proBNP > 365 pg/mL »

**Lacune :** Le seuil mineur du score HFA-PEFF en fibrillation auriculaire est erroné. Les seuils d’exclusion usuels sont également insuffisamment distingués des seuils utilisés pour contribuer à la confirmation par ce score.

**Correction proposée :** Remplacer 365 par l’intervalle 375–660 pg/mL pour le critère mineur en fibrillation auriculaire et préciser le seuil > 660 pg/mL pour le critère majeur. Distinguer ces valeurs des seuils d’exclusion de 125 pg/mL en ambulatoire et de 300 pg/mL en situation aiguë.

**Références de ce constat :** S04. **État de correction :** corrigé ciblé.

**Portée de la correction :** Le seuil mineur HFA-PEFF en fibrillation auriculaire a été corrigé. Cette correction ciblée ne certifie pas tous les concepts du constat.

### I50-023 — P0

**Source :** `chapters/I50/I50_b.html`, ligne 12 — §7.2, ligne 12 ; I50_c, §e2, quiz 2 et biochimie.

**Extrait :** « seul le NT-proBNP reste interprétable »

**Lacune :** Cette phrase contredit l’entrée i50-j-neprilysine de la banque : le BNP conserve une valeur pronostique sous sacubitril/valsartan. Le NT-proBNP n’est ni nécessairement inchangé ni un reflet pur de la pression.

**Correction proposée :** Harmoniser les répétitions et les corrigés. Expliquer que le BNP peut augmenter sous l’effet du médicament et que le NT-proBNP est moins directement perturbé. Interpréter les deux avec la clinique et la fonction rénale ; deux concentrations isolées ne permettent pas de conclure automatiquement à une amélioration.

**Références de ce constat :** S03, S07. **État de correction :** corrigé ciblé.

**Portée de la correction :** Les contradictions sur l’interprétation BNP/NT-proBNP sous ARNI ont été corrigées dans les répétitions visées. Les mécanismes plus détaillés du constat I50-077 restent ouverts ; cette correction ne les certifie pas.

### I50-024 — P2

**Source :** `chapters/I50/I50_b.html`, ligne 16 — §7.3–7.5.

**Extrait :** « l’échocardiographie d’effort ou le cathétérisme droit tranchent »

**Lacune :** Les paramètres diagnostiques et les recherches étiologiques ne disposent pas tous d’une explication de leur valeur et de leurs limites. L’échocardiographie d’effort et le cathétérisme ne résolvent l’incertitude que dans un contexte approprié et avec des mesures de qualité.

**Correction proposée :** Ajouter une fenêtre sur l’algorithme multiparamétrique et les tests d’effort. Préciser les indications conditionnelles de l’exploration coronarienne, de l’IRM et du bilan d’amylose, avec des renvois aux sections e3 et e5.

**Références de ce constat :** S02, S05, S11. **État de correction :** à traiter.

### I50-025 — P2

**Source :** `chapters/I50/I50_b.html`, ligne 23 — Figure 2.

**Extrait :** « d’après l’algorithme ESC »

**Lacune :** La légende n’identifie ni version ni page du référentiel. Elle distingue insuffisamment la confirmation du syndrome de sa classification par FEVG : une FEVG seule ne démontre pas une insuffisance cardiaque.

**Correction proposée :** Préciser qu’il s’agit du parcours de l’insuffisance cardiaque chronique et signaler les exceptions en cas de forte suspicion. Identifier la source 2026 et représenter l’association de symptômes et de preuves objectives avant la classification du phénotype.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-026 — P2

**Source :** `chapters/I50/I50_b.html`, ligne 28 — §8, alerte et quatre gestes.

**Extrait :** « lactate élevé, oligurie, confusion »

**Lacune :** Le mécanisme des critères de gravité et des profils de Stevenson reste incomplet. L’oxygène, la ventilation non invasive et les diurétiques ne s’appliquent pas mécaniquement à tous les chocs ni aux patients sans congestion.

**Correction proposée :** Créer une fenêtre de gravité et de triage. Expliquer l’usage de l’oxygène en cas d’hypoxémie, les effets de la pression positive sur le travail respiratoire et les charges cardiaques, ainsi que ses limites en cas d’hypotension ou d’atteinte du ventricule droit.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-027 — P1

**Source :** `chapters/I50/I50_b.html`, ligne 39 — §8.1 choc.

**Extrait :** « noradrénaline en vasopresseur de premier choix »

**Lacune :** Les traitements du choc sont présentés sans objectifs hémodynamiques ni critères de sélection. Un choc peut exister sans pression artérielle systolique < 90 mmHg ; aucun des traitements cités n’est automatiquement indiqué dans tous les cas.

**Correction proposée :** Expliquer l’objectif de restauration de la perfusion selon la pression et le débit, avec les risques rythmiques. Présenter l’assistance comme une décision d’équipe spécialisée, pour des patients sélectionnés, plutôt que comme une étape systématique.

**Références de ce constat :** S01. **État de correction :** partiellement corrigé.

**Portée de la correction :** La possibilité d’un choc normotensif, les limites du lactate et la sélection de l’assistance ont été corrigées dans pop4. Les formulations automatiques de I50_b et les explications restantes sont à reprendre.

### I50-028 — P2

**Source :** `chapters/I50/I50_b.html`, ligne 38 — §8.1 tableaux.

**Extrait :** « Éviter l’excès de vasodilatateurs »

**Lacune :** Le texte n’explique pas suffisamment comment l’hypertension peut redistribuer les volumes, pourquoi certains tableaux du ventricule droit dépendent de la précharge, ni pourquoi les diurétiques nécessitent une congestion ou une surcharge à traiter.

**Correction proposée :** Distinguer l’œdème pulmonaire par redistribution d’une surcharge globale. Expliquer la postcharge du ventricule droit dans l’embolie pulmonaire ou l’infarctus et la prudence nécessaire avec la vasodilatation et la ventilation non invasive.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-029 — P1

**Source :** `chapters/I50/I50_b.html`, ligne 41 — §8.2.

**Extrait :** « impose de doubler la dose »

**Lacune :** La stratégie guidée par la natriurèse est présentée comme une exigence absolue, alors que la recommandation 2026 est optionnelle. Une réponse insuffisante ne justifie pas de doubler la dose sans vérifier la tolérance.

**Correction proposée :** Expliquer la relation dose–réponse et la réévaluation de la diurèse, de la natriurèse, de la pression artérielle, de la fonction rénale et du potassium. Préciser les patients concernés, la durée courte et les risques du blocage séquentiel du néphron.

**Références de ce constat :** S01, S08. **État de correction :** à traiter.

### I50-030 — P2

**Source :** `chapters/I50/I50_b.html`, ligne 43 — §8.3.

**Extrait :** « La morphine n’est pas utilisée en routine. »

**Lacune :** La raison du seuil de pression artérielle systolique de 110 mmHg pour les nitrates n’est pas expliquée. Il manque aussi des explications sur les risques des inotropes, l’absence d’usage systématique de la morphine et la thromboprophylaxie par héparine.

**Correction proposée :** Ajouter des fenêtres sur les critères, les effets attendus et les limites de chaque traitement. Décrire la sélection pour une héparine de bas poids moléculaire selon le risque thromboembolique, le risque hémorragique et une éventuelle anticoagulation déjà prescrite.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-031 — P1

**Source :** `chapters/I50/I50_b.html`, ligne 45 — §8.4.

**Extrait :** « réduit les réhospitalisations précoces »

**Lacune :** L’effet des visites est confondu avec celui du programme complet de STRONG-HF. Les critères de sortie, dont la stabilité rénale pendant 24 heures, restent parfois incomplets.

**Correction proposée :** Décrire la stabilité clinique, la congestion, la tolérance des traitements oraux et le programme de titration avec surveillance. Attribuer le bénéfice au programme de prise en charge étudié, et non à une visite isolée.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-032 — P2

**Source :** `chapters/I50/I50_b.html`, ligne 58 — §9.1.

**Extrait :** « Leurs effets s’additionnent »

**Lacune :** La formulation suggère une démonstration randomisée directe des quatre classes combinées contre chaque traitement isolé. Les bénéfices sur des critères composites ne prouvent pas une réduction de mortalité pour chaque classe et chaque phénotype.

**Correction proposée :** Décrire le niveau de preuve, les populations et les critères de jugement. Distinguer les FEVG ≤ 40 % des FEVG de 41 à 49 % et expliquer que l’addition des bénéfices est estimée à partir d’essais distincts.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-033 — P1

**Source :** `chapters/I50/I50_b.html`, ligne 59 — §9.1–9.2.

**Extrait :** « jusqu’aux doses cibles des essais »

**Lacune :** Les conditions de stabilité, de pression artérielle, de fonction rénale et de kaliémie manquent localement. Certaines classes, dont les inhibiteurs de SGLT2, ne sont pas titrées comme les autres. Une recommandation de classe I n’efface pas les contre-indications.

**Correction proposée :** Relier la présentation aux précautions de la fenêtre pop4 et expliquer leur mécanisme. Réserver la notion de dose cible aux traitements à titrer et identifier les références propres à chaque classe et phénotype.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-034 — P1

**Source :** `chapters/I50/I50_b.html`, ligne 60 — §9.1 diurétiques.

**Extrait :** « sans modifier la mortalité »

**Lacune :** L’absence de démonstration d’un bénéfice de survie est formulée comme la preuve d’un effet nul sur la mortalité.

**Correction proposée :** Indiquer que les diurétiques soulagent la congestion et que leur bénéfice sur la survie n’est pas démontré par des essais appropriés. Expliquer l’objectif de la dose minimale permettant de maintenir l’euvolémie.

**Références de ce constat :** S08. **État de correction :** à traiter.

### I50-035 — P2

**Source :** `chapters/I50/I50_b.html`, ligne 69 — §9.2–9.3.

**Extrait :** « améliore les symptômes et réduit les hospitalisations »

**Lacune :** Les indications des agonistes du GLP-1, du tirzépatide et du fer intraveineux ne précisent pas suffisamment les seuils et profils des patients, les paramètres de surveillance dont le potassium selon le traitement, le phénotype de FEVG, la carence martiale et le type de fer. Les hospitalisations et la mortalité ne sont pas assez distinguées.

**Correction proposée :** Décrire l’indication et la justification de chaque ajout. Ne pas extrapoler les essais à toute ICFEp, à tout taux d’hémoglobine ou à un bénéfice sur les décès. Les essais primaires propres à chaque intervention restent à documenter explicitement.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-036 — P1

**Source :** `chapters/I50/I50_b.html`, ligne 71 — §9.3–9.4.

**Extrait :** « après au moins trois mois de TMF optimisée »

**Lacune :** Les références 2021 sur l’ivabradine et l’hydralazine sont datées. Une attente de trois mois présentée comme universelle pour la resynchronisation contredit l’option 2026 de planification simultanée chez certains patients. La sélection pour une réparation mitrale percutanée bord à bord (TEER) n’est pas expliquée.

**Correction proposée :** Conserver les repères historiques en les confrontant au référentiel 2026. Préciser l’exception pour la resynchronisation, distinguer prévention primaire et secondaire par DAI et expliquer les critères de TEER avec l’évaluation par une équipe valvulaire.

**Références de ce constat :** S01. **État de correction :** partiellement corrigé.

**Portée de la correction :** Les critères et nuances de resynchronisation ont été corrigés. La sélection pour TEER et les autres explications du constat restent ouvertes.

### I50-037 — P1

**Source :** `chapters/I50/I50_b.html`, ligne 75 — §9.5.

**Extrait :** « infection active, cancer récent »

**Lacune :** Les contre-indications à la greffe sont condensées en termes absolus, sans préciser leur nature ni l’évaluation spécialisée. Les informations et dates relatives aux centres suisses ne sont pas référencées.

**Correction proposée :** Distinguer contre-indications relatives et absolues et décrire la décision multidisciplinaire. Relier les seuils au type de cancer, à la cause et au risque de récidive. Les recommandations ISHLT et les sources des centres suisses restent à vérifier.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-038 — P2

**Source :** `chapters/I50/I50_b.html`, ligne 76 — §9.5 assistance/palliatifs.

**Extrait :** « fonction ventriculaire droite suffisante »

**Lacune :** La raison de l’évaluation de la réserve du ventricule droit et des profils INTERMACS reste implicite. Le choix entre pont vers la greffe et traitement définitif, ainsi que les soins palliatifs et la désactivation du DAI, manquent de contexte.

**Correction proposée :** Expliquer le circuit de l’assistance et le risque d’aggravation du ventricule droit. Présenter la sélection selon les objectifs du patient et distinguer bénéfice pronostique, soulagement des symptômes et décisions de fin de vie.

**Références de ce constat :** S01, S12. **État de correction :** à traiter.

### I50-039 — P2

**Source :** `chapters/I50/I50_b.html`, ligne 82 — §10 surveillance.

**Extrait :** « Après chaque titration, on contrôle la créatinine et la kaliémie »

**Lacune :** La surveillance nécessaire diffère selon les classes. La pesée, le plan écrit, l’exercice et les vaccinations restent cités sans toujours expliquer leur raison ni les patients concernés.

**Correction proposée :** Relier la surveillance à la cible et au mécanisme des traitements, avec les fenêtres sur le potassium et le rein. Décrire la réadaptation chez un patient stable et correctement perfusé, le plan d’éducation et le risque infectieux. Les sources précises de l’OFSP en vigueur en 2026 restent à vérifier.

**Références de ce constat :** S01, S06. **État de correction :** à traiter.

### I50-040 — P1

**Source :** `chapters/I50/I50_b.html`, ligne 83 — §10 diététique.

**Extrait :** « restriction sodée modérée »

**Lacune :** La quantité, le contexte et la raison de la restriction sodée ne sont pas précisés ; l’incertitude sur les résultats cliniques n’est pas présentée. L’absence de restriction hydrique systématique n’est pas expliquée.

**Correction proposée :** Expliquer la prévention des excès sans imposer une restriction stricte uniforme. Adapter les apports hydriques à l’hyponatrémie et à la congestion, en précisant les résultats de SODIUM-HF et le référentiel 2026.

**Références de ce constat :** S14. **État de correction :** à traiter.

### I50-041 — P1

**Source :** `chapters/I50/I50_b.html`, ligne 84 — §10, FEVG améliorée, et glossaire cardio_2, TRED-HF.

**Extrait :** « on ne réduit pas le traitement »

**Lacune :** Les données de TRED-HF, obtenues dans des cardiomyopathies dilatées récupérées, sont extrapolées à toutes les situations. Le référentiel 2026 prévoit une option de retrait progressif chez des patients très sélectionnés présentant une cause réversible.

**Correction proposée :** Présenter la poursuite aux doses maximales tolérées comme le principe général. Préciser la population de TRED-HF et les exceptions spécialisées de 2026, sans faire de l’amélioration de la FEVG une autorisation d’arrêt individuel.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-042 — P1

**Source :** `chapters/I50/I50_b.html`, ligne 85 — §10, stade B.

**Extrait :** « un IEC et un bêtabloquant retardent l’apparition des symptômes »

**Lacune :** L’indication après infarctus est trop large sans FEVG, dose ou tolérance. Le mécanisme de prévention du remodelage n’est pas expliqué.

**Correction proposée :** Préciser la FEVG et le stade B concernés. Rattacher au référentiel 2026 les indications d’IEC pour une FEVG ≤ 40 % et de bêtabloquant pour une FEVG < 50 %, puis expliquer les effets sur la charge et le remodelage.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-043 — P1

**Source :** `chapters/I50/I50_b.html`, ligne 85 — §10, hypertension, cardio-oncologie et conduite.

**Extrait :** « inférieure à 130/80 mmHg »

**Lacune :** La cible tensionnelle, la baisse relative du GLS et la protection cardiologique sont présentées sans distinguer leurs contextes. Les directives suisses concernant la conduite ne sont pas citées.

**Correction proposée :** Expliquer l’individualisation selon l’âge, la fragilité et la méthode de mesure de la pression. Pour le GLS, préciser la comparaison avec la valeur initiale, les conditions de mesure et le type de traitement anticancéreux. Trouver les recommandations de cardio-oncologie et une référence suisse datée sur l’aptitude à la conduite.

**Références de ce constat :** S01, S02. **État de correction :** à traiter.

### I50-044 — P2

**Source :** `chapters/I50/I50_b.html`, ligne 92 — §11 rénale/hyperkaliémie.

**Extrait :** « le premier obstacle à la titration des IEC et des ARM »

**Lacune :** Le superlatif n’est pas démontré. La capacité des chélateurs du potassium à maintenir les doses n’est pas suffisamment distinguée d’un bénéfice clinique ou pronostique ; leurs risques et leur contexte d’utilisation restent incomplets.

**Correction proposée :** Réutiliser les fenêtres sur le potassium et le rein. Décrire la recherche des causes, l’évaluation de la gravité et de l’ECG, les indications d’un traitement urgent et le plan d’adaptation des traitements. Ne pas présumer qu’une hyperkaliémie est bénigne.

**Références de ce constat :** S06. **État de correction :** à traiter.

### I50-045 — P1

**Source :** `chapters/I50/I50_b.html`, ligne 93 — §11 grossesse.

**Extrait :** « les dérivés nitrés et les diurétiques de l’anse restent utilisables »

**Lacune :** La liste mélange absence de preuves et fœtotoxicité, sans préciser la molécule, le trimestre ou la surveillance. La définition de la cardiomyopathie du péripartum limitée au dernier mois de grossesse et aux cinq mois suivants reprend un repère ancien comme une frontière stricte.

**Correction proposée :** Créer une fenêtre sur la prise en charge spécialisée, la surveillance fœtale et l’équilibre volémique. Actualiser la définition de la cardiomyopathie du péripartum sans utiliser ce repère temporel comme critère d’exclusion absolu. Une référence récente propre à la grossesse reste à vérifier.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-046 — P2

**Source :** `chapters/I50/I50_b.html`, ligne 95 — §11 FA/hyponatrémie/sommeil/valves.

**Extrait :** « l’ablation améliore le pronostic chez des patients sélectionnés en ICFEr »

**Lacune :** Les raisons et les critères de sélection restent incomplets pour l’ablation de la fibrillation auriculaire, l’ablation du nœud AV associée à la CRT, le traitement de l’hyponatrémie, la CPAP ou l’ASV, ainsi que le choix entre TAVI, chirurgie et TEER. Il manque notamment la distinction entre hyponatrémie de dilution et déplétion.

**Correction proposée :** Ajouter des fenêtres contextuelles expliquant les mécanismes, les critères de sélection, les limites et les classes de recommandation de 2026. Distinguer les résultats des essais randomisés chez des patients sélectionnés de leur application à tout patient.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-047 — P2

**Source :** `chapters/I50/I50_b.html`, ligne 100 — §11 anémie/BPCO/diabète.

**Extrait :** « La BPCO ne contre-indique pas les bêtabloquants β1-sélectifs. »

**Lacune :** Les mécanismes et les risques des agents stimulant l’érythropoïèse, des bêtabloquants en présence de BPCO et de la saxagliptine ne sont pas expliqués. Éviter de généraliser à toute fibrillation auriculaire le bénéfice pronostique des bêtabloquants β1-sélectifs.

**Correction proposée :** Expliquer le risque thromboembolique des agents stimulant l’érythropoïèse, la cardiosélectivité et le risque de bronchospasme. Présenter le signal de l’essai SAVOR et préciser que le bêtabloquant répond à une indication cardiaque, sans proposer de traiter toute BPCO par bêtabloquant.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-048 — P1

**Source :** `chapters/I50/I50_b.html`, ligne 104 — Cas récapitulatif : sept décisions.

**Extrait :** « Bêtabloquant (bisoprolol 1,25 mg) une fois euvolémique : pronostic et contrôle de la fréquence. »

**Lacune :** Dans ce cas de fibrillation auriculaire permanente, le bénéfice pronostique du bêtabloquant est présenté sans nuance. La mention d’une dose d’anticoagulant adaptée au DFG ne précise ni la clairance de Cockcroft-Gault ni les autres critères propres à chaque molécule. L’effet tensionnel des iSGLT2 ne doit pas être assimilé à une absence totale d’effet.

**Correction proposée :** Justifier chaque décision selon la stabilité clinique, la kaliémie et la pression artérielle. Présenter le bêtabloquant comme un outil de contrôle de fréquence, avec un bénéfice pronostique non uniformément démontré en FA. Préciser les règles de dose de chaque AOD et la méthode d’estimation rénale applicable.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-049 — P2

**Source :** `chapters/I50/I50_c.html`, ligne 7 — §e1, tableau des neuf examens.

**Extrait :** « Chaque examen répond à une question précise. »

**Lacune :** Les statuts des neuf examens sont indiqués, mais leurs raisons, leurs mécanismes et leurs exceptions ne sont pas expliqués localement. Les fenêtres existantes ne couvrent pas les neuf questions du tableau.

**Correction proposée :** Ajouter des fenêtres pour ECG, échocardiographie, radiographie, imagerie coronaire, IRM, recherche d’ATTR, cathétérisme et épreuve cardiorespiratoire. Préciser l’objectif, la place dans le parcours, les critères d’utilisation et la décision que le résultat peut modifier.

**Références de ce constat :** S01, S02, S11. **État de correction :** à traiter.

### I50-050 — P1

**Source :** `chapters/I50/I50_c.html`, ligne 22 — §e2, premier paragraphe sur les peptides.

**Extrait :** « Ils répondent donc directement à la question « les pressions intracardiaques sont-elles élevées ? ». »

**Lacune :** Les peptides natriurétiques ne sont pas des manomètres. La contrainte myocardique dépend de la géométrie, de la charge, du rythme et de la fonction rénale ; des élévations existent aussi en dehors de l’IC.

**Correction proposée :** Les présenter comme des biomarqueurs de contrainte myocardique à interpréter dans leur contexte. Expliquer leur bonne valeur prédictive négative et les limites de leur valeur prédictive positive.

**Références de ce constat :** S01, S03. **État de correction :** à traiter.

### I50-051 — P2

**Source :** `chapters/I50/I50_c.html`, ligne 27 — §e2, tableau des variations.

**Extrait :** « Embolie pulmonaire, hypertension pulmonaire, sepsis, syndrome coronarien »

**Lacune :** Les fenêtres consacrées à l’obésité et aux ARNI existent, mais les mécanismes liés à l’âge, à la fonction rénale, à la FA, à la surcharge du ventricule droit, au sepsis et au syndrome coronarien restent peu explicités. L’effet rénal ne se réduit pas à une baisse de clairance.

**Correction proposée :** Ajouter des explications distinctes ou regroupées selon un mécanisme commun : production et clairance rénales, étirement atrial en FA, stress du VD dans l’EP ou l’hypertension pulmonaire, et contexte du sepsis ou du syndrome coronarien. Éviter une explication unique par la clairance rénale.

**Références de ce constat :** S01, S03, S06. **État de correction :** à traiter.

### I50-052 — P1

**Source :** `chapters/I50/I50_c.html`, ligne 34 — §e2 bilan initial.

**Extrait :** « DFG ≥ 60 mL/min/1,73 m² (CKD-EPI) »

**Lacune :** Des seuils diagnostiques peuvent être lus comme des valeurs normales universelles. Un DFG ≥ 60 n’exclut pas une maladie rénale chronique. Le diagnostic fondé sur l’HbA1c nécessite un contexte approprié et, selon la situation, une confirmation ; l’anémie peut affecter son interprétation. Une carence martiale ne conduit pas automatiquement au fer IV.

**Correction proposée :** Séparer les intervalles de laboratoire, les critères diagnostiques, les cibles et les conséquences thérapeutiques conditionnelles. Ajouter les références OMS/KDIGO nécessaires et préciser le phénotype d’IC concerné par le fer IV.

**Références de ce constat :** S06, S01. **État de correction :** à traiter.

### I50-053 — P2

**Source :** `chapters/I50/I50_c.html`, ligne 35 — §e2, bilan : potassium, TSH, troponine et albuminurie.

**Extrait :** « K⁺ 3,5–5,0 mmol/L (cible 4,0–5,0 sous TMF) »

**Lacune :** Les explications de la banque sont utiles, mais elles ne valident pas chaque cible chiffrée : kaliémie, TSH, HbA1c, DFG et indication de la finérénone. La cohérence avec la cinquième définition universelle de l’infarctus, mentionnée pour la troponine, reste à examiner.

**Correction proposée :** Relier chaque cible clinique à une fenêtre explicative ou à une référence explicite. Vérifier le contexte tensionnel, les valeurs de référence et l’indication de chaque molécule ; éviter une décision thérapeutique fondée sur une mesure isolée.

**Références de ce constat :** S06, S01. **État de correction :** à traiter.

### I50-054 — P1

**Source :** `chapters/I50/I50_c.html`, ligne 50 — §e3, tableau de quantification.

**Extrait :** « ≥ 50 % (ESC 2026) »

**Lacune :** Le seuil de classification des phénotypes d’IC n’est pas la borne inférieure de normalité pour toute quantification de la FEVG. Les valeurs de référence dépendent notamment du sexe et de la méthode. Une FEVG ≤ 35 % ne constitue pas, seule, une indication de dispositif.

**Correction proposée :** Distinguer le phénotype selon ESC 2026, les valeurs de référence de quantification et les indications de dispositifs, qui reposent sur plusieurs critères.

**Références de ce constat :** S01, S02. **État de correction :** partiellement corrigé.

**Portée de la correction :** La table de FEVG a été corrigée. La définition correspondante du glossaire cardio_1 et les autres conditions restent ouvertes.

### I50-055 — P1

**Source :** `chapters/I50/I50_c.html`, ligne 53 — §e3, tableau de diastole et source de 2016.

**Extrait :** « e′ septale ≥ 7 cm/s ; latérale ≥ 10 cm/s »

**Lacune :** La référence de 2016 est appliquée uniformément alors que les recommandations ASE 2025 sont déjà citées dans la banque. Les mesures dépendent de l’âge, du rythme et des valvulopathies ; un E/e′ isolé ne suffit pas à établir le diagnostic.

**Correction proposée :** Revoir l’algorithme de 2025 et son tableau 6. Expliquer les variations avec l’âge, les conditions d’acquisition, les patients exclus de certains algorithmes et l’intégration de plusieurs paramètres.

**Références de ce constat :** S02. **État de correction :** partiellement corrigé.

**Portée de la correction :** Les seuils et leur dépendance à l’âge ont été actualisés selon ASE. Les conditions d’acquisition et les mécanismes restent ouverts.

### I50-056 — P2

**Source :** `chapters/I50/I50_c.html`, ligne 58 — §e3, autres lignes du tableau.

**Extrait :** « Veine cave inférieure »

**Lacune :** Les autres paramètres manquent d’explications sur ce qu’ils mesurent, leur acquisition et leurs limites : Simpson, GLS selon fabricant et charge, volume atrial en FA, vitesse tricuspide, TAPSE selon charge, masse indexée et VCI selon ventilation.

**Correction proposée :** Ajouter une fenêtre par paramètre indiquant la mesure, la raison du seuil et les conditions d’interprétation. Éviter de transformer un chiffre isolé en diagnostic univoque.

**Références de ce constat :** S02, S01. **État de correction :** partiellement corrigé.

**Portée de la correction :** Les formulations concernant l’oreillette gauche, E/e′ et le Pareto ont été corrigées. Les autres paramètres, leurs acquisitions et leurs limites restent ouverts.

### I50-057 — P2

**Source :** `chapters/I50/I50_c.html`, ligne 60 — §e3, piège de l’insuffisance mitrale.

**Extrait :** « Dans l’insuffisance mitrale sévère, une FEVG à 55 % traduit déjà une dysfonction »

**Lacune :** L’explication de la FEVG en présence d’une postcharge réduite est amorcée, mais la distinction entre insuffisance mitrale primaire et secondaire, les mesures associées et les critères opératoires selon le risque restent insuffisamment explicités.

**Correction proposée :** Expliquer les volumes d’éjection antérograde et régurgité et l’effet de la postcharge. Relier l’interprétation au parcours valvulaire 2025/2026 et vérifier la portée générale de la phrase sur une FEVG à 55 %.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-058 — P2

**Source :** `chapters/I50/I50_c.html`, ligne 65 — §e4 ECG.

**Extrait :** « ondes Q de nécrose (ischémique) »

**Lacune :** Les anomalies ECG sont associées à des causes sans expliquer leurs mécanismes ni leurs limites : infarctus sans onde Q, ondes Q non spécifiques et bas voltage inconstant dans l’amylose. Les critères de CRT liés au QRS sont incomplets.

**Correction proposée :** Ajouter des fenêtres par anomalie ou par groupe électromécanique. Détailler les conditions d’indication de la CRT et confronter chaque anomalie au contexte clinique et à l’imagerie.

**Références de ce constat :** S01, S11. **État de correction :** à traiter.

### I50-059 — P1

**Source :** `chapters/I50/I50_c.html`, ligne 67 — §e4, radiographie.

**Extrait :** « Les signes apparaissent dans un ordre qui suit l’élévation de la pression capillaire pulmonaire. »

**Lacune :** La séquence radiologique en trois stades n’est ni systématique ni un moyen de dater la décompensation. Le seuil du rapport cardiothoracique dépend d’une acquisition postéro-antérieure debout en inspiration ; une projection antéro-postérieure peut majorer la silhouette cardiaque.

**Correction proposée :** Préciser les conditions de projection, les limites de la séquence et de sa chronologie. Expliquer redistribution vasculaire, lignes de Kerley et œdème alvéolaire.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-060 — P2

**Source :** `chapters/I50/I50_c.html`, ligne 73 — §e4, échographie pulmonaire.

**Extrait :** « est plus sensible que la radiographie pour détecter l’œdème interstitiel au lit du patient. »

**Lacune :** La comparaison doit préciser le contexte de recherche d’un œdème cardiogénique. La phrase n’explique ni la non-spécificité des lignes B, ni leur signification physique, ni la dépendance à l’opérateur.

**Correction proposée :** Ajouter une fenêtre sur l’artefact interstitiel et le diagnostic différentiel avec fibrose, pneumonie et SDRA. Rechercher et citer une étude primaire comparative adaptée au contexte.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-061 — P1

**Source :** `chapters/I50/I50_c.html`, ligne 78 — §e5 IRM.

**Extrait :** « diffus et sous-endocardique global dans l’amylose. »

**Lacune :** Les profils de rehaussement sont utiles mais non spécifiques. Une myocardite ne présente pas toujours de LGE, et l’amylose peut avoir un rehaussement transmural. L’affirmation sur la reproductibilité de l’IRM demande un contexte.

**Correction proposée :** Expliquer les objectifs et les limites des séquences ciné, LGE, T1, ECV et T2, ainsi que les contraintes de contraste, fonction rénale, rythme et dispositifs. Une référence primaire SCMR reste à trouver et à vérifier.

**Références de ce constat :** S02. **État de correction :** à traiter.

### I50-062 — P2

**Source :** `chapters/I50/I50_c.html`, ligne 80 — §e5, ATTR, et quiz 3.

**Extrait :** « permet le diagnostic d’amylose ATTR sans biopsie. »

**Lacune :** L’algorithme est solide, mais il manque les raisons du choix du traceur et du diagnostic sans biopsie, la confirmation myocardique par SPECT, les faux positifs, l’interprétation des chaînes légères en maladie rénale et la place de la génétique après un diagnostic d’ATTR.

**Correction proposée :** Expliquer les conditions du diagnostic d’ATTR, le contexte échocardiographique compatible et la confirmation de la localisation myocardique par SPECT. Distinguer la démarche pour l’AL et son urgence hématologique.

**Références de ce constat :** S11, S01. **État de correction :** à traiter.

### I50-063 — P2

**Source :** `chapters/I50/I50_c.html`, ligne 82 — §e5 coronarographie.

**Extrait :** « Elle est indiquée si l’on suspecte une cause ischémique chez un patient candidat à une revascularisation. »

**Lacune :** Le texte explique peu la probabilité prétest, la place des examens non invasifs, la distinction entre syndrome coronarien aigu et situation chronique, le risque rénal du contraste et la raison de limiter l’examen aux candidats à une revascularisation.

**Correction proposée :** Expliquer comment l’identification de l’anatomie coronaire peut modifier la prise en charge. Préciser les conditions de recours au coroscanner selon la probabilité de maladie et la qualité attendue de l’examen.

**Références de ce constat :** S09, S10, S01. **État de correction :** à traiter.

### I50-064 — P1

**Source :** `chapters/I50/I50_c.html`, ligne 84 — §e5, cathétérisme droit.

**Extrait :** « Le cathétérisme droit mesure directement la pression capillaire pulmonaire et le débit cardiaque. »

**Lacune :** La pression d’occlusion artérielle pulmonaire (PAWP) est un reflet de la pression atriale gauche, avec des limites liées à la technique, à la respiration, au rythme et à la position. Un seuil isolé ne confirme pas le syndrome clinique d’ICFEp ; PAWP et pression télédiastolique VG ne sont pas interchangeables.

**Correction proposée :** Décrire une mesure correcte de la pression bloquée et les conditions d’application des seuils au repos et à l’effort en décubitus. Intégrer symptômes, FEVG et exclusion des causes valvulaires ; éviter d’assimiler PCWP et pression télédiastolique VG.

**Références de ce constat :** S02, S13. **État de correction :** à traiter.

### I50-065 — P1

**Source :** `chapters/I50/I50_c.html`, ligne 84 — §e5, cathétérisme droit, et glossaire cardio_1, PAPi.

**Extrait :** « inférieur à 1,85 évoque une défaillance ventriculaire droite, notamment avant une assistance gauche. »

**Lacune :** La définition de la composante précapillaire n’intègre pas explicitement tous les paramètres, dont la PAWP. Le seuil de PAPi issu du contexte précédant une assistance gauche est extrapolé à la défaillance VD générale.

**Correction proposée :** Présenter pression artérielle pulmonaire moyenne, PAWP et résistances vasculaires pulmonaires ensemble. Décrire le PAPi comme un outil de risque contextuel, notamment avant LVAD, avec des seuils variables plutôt qu’un diagnostic universel.

**Références de ce constat :** S13, S12. **État de correction :** à traiter.

### I50-066 — P2

**Source :** `chapters/I50/I50_c.html`, ligne 84 — §e5, cathétérisme et épreuve cardiorespiratoire.

**Extrait :** « quantifie la limitation et oriente vers les thérapies avancées. »

**Lacune :** Le sens de l’index cardiaque et les limites des mesures par Fick ou thermodilution ne sont pas expliqués. Le choc ne se résume pas à un seuil d’index cardiaque. Le lien entre VO₂, VE/VCO₂, limitation d’effort et orientation vers la greffe reste bref.

**Correction proposée :** Expliquer transport d’oxygène et effort, les limitations pulmonaires ou périphériques, la qualité de l’effort et l’effet du traitement bêtabloquant. Rechercher et vérifier les références primaires ISHLT nécessaires.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-067 — P0

**Source :** `chapters/I50/I50_c.html`, ligne 93 — §e6, retour du quiz 1.

**Extrait :** « sont des preuves directes de pressions de remplissage élevées. »

**Lacune :** La dilatation atriale gauche et E/e′ fournissent des indices indirects. Un score de probabilité intermédiaire ne constitue pas une confirmation d’ICFEp.

**Correction proposée :** Remplacer « preuves directes » par « indices indirects concordants ». Expliquer le score minimal de 4, les composantes non renseignées et la confirmation conditionnelle par des explorations complémentaires.

**Références de ce constat :** S02, S05. **État de correction :** corrigé ciblé.

**Portée de la correction :** Le bouton et la réponse du quiz 1 ont été corrigés. Cette correction ciblée ne certifie pas tous les concepts du constat.

### I50-068 — P2

**Source :** `chapters/I50/I50_c.html`, ligne 93 — §e6, trois quiz.

**Extrait :** « Réponse B. Chez l’obèse, les peptides natriurétiques sont abaissés. »

**Lacune :** Les corrigés expliquent surtout la bonne réponse sans examiner chaque distracteur. L’exigence de justifier chaque affirmation inclut les options fausses.

**Correction proposée :** Expliquer pourquoi chaque autre option proposée est fausse, puis préciser les étapes suivantes et les limites de la réponse. Ne pas introduire de nouvelles affirmations sans source.

**Références de ce constat :** S02, S03, S11. **État de correction :** à traiter.

### I50-069 — P2

**Source :** `chapters/I50/I50_c.html`, ligne 118 — §sa-i anatomie.

**Extrait :** « Ses fibres myocardiques s’organisent en trois couches »

**Lacune :** L’architecture hélicoïdale est un modèle simplifié d’une organisation continue. La vulnérabilité sous-endocardique dépend notamment de la compression et de la perfusion ; la même explication ne doit pas être transposée automatiquement à l’amylose. Des sources anatomiques primaires manquent.

**Correction proposée :** Expliquer le caractère simplifié du modèle, les gradients de perfusion et de contrainte ainsi que la réserve de débit. Ne pas attribuer l’atteinte du GLS dans l’amylose à la seule distance des artères épicardiques. Les sources primaires correspondantes restent à trouver.

**Références de ce constat :** S02. **État de correction :** à traiter.

### I50-070 — P2

**Source :** `chapters/I50/I50_c.html`, ligne 120 — §sa-i, ventricule droit, mitrale et figure guide.

**Extrait :** « l’hypertension pulmonaire post-capillaire finit par le dilater »

**Lacune :** L’évolution vers une dilatation VD n’est pas inéluctable. Les mécanismes d’insuffisance mitrale ventriculaire et atriale diffèrent, et les réponses de la géométrie et de la coaptation au traitement sont variables.

**Correction proposée :** Employer des formulations conditionnelles. Expliquer postcharge VD, remodelage inverse et mécanisme atrial distinct de l’insuffisance mitrale ; référencer la figure originale.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-071 — P2

**Source :** `chapters/I50/I50_c.html`, ligne 125 — §sh-i histologie.

**Extrait :** « Elle rigidifie le ventricule (dysfonction diastolique) et crée un substrat d’arythmie par réentrée. »

**Lacune :** La fenêtre sur la fibrose apporte une chaîne explicative, mais collagènes I/III, connexines, desmosomes, activation fibroblastique par l’aldostérone et retentissement mécanique demandent davantage de liens causaux et de preuves primaires.

**Correction proposée :** Relier collagène et rigidité, connexines et vitesse/anisotropie de conduction, puis désorganisation tissulaire et propagation électrique. Distinguer associations cliniques et démonstrations in vitro ; les preuves primaires restent à compléter.

**Références de ce constat :** S02. **État de correction :** à traiter.

### I50-072 — P1

**Source :** `chapters/I50/I50_c.html`, ligne 126 — §sh-i IRM/amylose.

**Extrait :** « Plus cet espace est grand (fibrose, amylose), plus le rehaussement tardif est intense »

**Lacune :** Le LGE est une imagerie de contraste et non une mesure linéaire de la fibrose diffuse ; T1 et ECV apportent des informations complémentaires. Le bas voltage n’est pas constant dans l’amylose et ne découle pas nécessairement de l’épaississement pariétal.

**Correction proposée :** Distinguer LGE focal, atteinte diffuse et apports de T1/ECV. Expliquer l’épaississement par infiltration amyloïde et préciser qu’un bas voltage peut être présent malgré des parois épaisses, sans en faire une conséquence obligatoire.

**Références de ce constat :** S02, S11. **État de correction :** à traiter.

### I50-073 — P2

**Source :** `chapters/I50/I50_c.html`, ligne 128 — Figure guide de la fibrose.

**Extrait :** « qui se divise en deux branches »

**Lacune :** Le texte et la légende décrivent deux branches, mécanique et électrique, alors que le SVG dispose les étapes en chaîne : rigidité puis conduction. Le schéma montre ainsi une causalité différente de celle annoncée.

**Correction proposée :** Dessiner effectivement deux branches ou adapter le texte pour éviter une causalité implicite entre perte de souplesse et trouble de conduction. Conserver les identifiants et l’accessibilité.

**Références de ce constat :** S02. **État de correction :** à traiter.

### I50-074 — P2

**Source :** `chapters/I50/I50_c.html`, ligne 130 — §sp-i physiologie.

**Extrait :** « est la force intrinsèque, indépendante des conditions de charge. »

**Lacune :** Volume et pression ne sont pas des équivalents de la précharge lorsque la compliance varie. L’élastance est une approximation dépendante des conditions, et la loi de Laplace pour une paroi mince ne décrit pas exactement un ventricule gauche à paroi épaisse.

**Correction proposée :** Ajouter des définitions et des équations expliquées, avec unités de contrainte, relations géométriques et limites des modèles. Une source primaire de physiologie classique reste à retrouver et à vérifier.

**Références de ce constat :** S02. **État de correction :** à traiter.

### I50-075 — P1

**Source :** `chapters/I50/I50_c.html`, ligne 138 — Figure 3, Starling.

**Extrait :** « Un diurétique ramène vers la gauche avec une faible perte de volume d’éjection, car la courbe est plate. »

**Lacune :** Les points A et B sont dessinés à des hauteurs différentes. La réponse au diurétique sur une courbe plate n’est pas universelle, notamment en défaillance VD, bas débit ou dépendance à la précharge. Le seuil de congestion représenté est arbitraire.

**Correction proposée :** Expliciter le caractère qualitatif du schéma et ses hypothèses. Faire correspondre le dessin aux volumes annoncés ou parler de compensation partielle. Expliquer qu’une diurèse excessive peut diminuer la perfusion.

**Références de ce constat :** S08. **État de correction :** à traiter.

### I50-076 — P2

**Source :** `chapters/I50/I50_c.html`, ligne 149 — Figure 4, pression–volume, et paragraphe.

**Extrait :** « sa hauteur à droite indique la pression télédiastolique (PTD). »

**Lacune :** La hauteur entière du côté droit de la boucle ne représente pas la PTD, qui correspond au point télédiastolique inférieur droit. Les relations télésystolique et télédiastolique doivent être lisibles et cohérentes avec les annotations. Les volumes normaux de la boucle ICFEp constituent une simplification.

**Correction proposée :** Identifier les quatre phases, les points télésystolique et télédiastolique, la largeur correspondant au volume d’éjection et la PTD au point télédiastolique. Montrer les relations propres à l’ICFEp et à l’ICFEr si les pentes sont discutées ; éviter de valider ces relations à partir du seul schéma actuel.

**Références de ce constat :** S02. **État de correction :** à traiter.

### I50-077 — P1

**Source :** `chapters/I50/I50_c.html`, ligne 154 — §sb-i, peptides natriurétiques, et glossaire cardio_1, NT-proBNP.

**Extrait :** « en deux fragments sécrétés à parts égales »

**Lacune :** Le modèle idéal de clivage n’implique pas des concentrations mesurées équimolaires. Glycosylation, proBNP immunoréactif et différences de clairance compliquent l’interprétation.

**Correction proposée :** Distinguer le modèle biochimique, les molécules détectées par le dosage et leur pharmacocinétique approximative. Éviter de présenter ces concentrations comme une mesure directe de pression.

**Références de ce constat :** S03, S07. **État de correction :** à traiter.

### I50-078 — P2

**Source :** `chapters/I50/I50_c.html`, ligne 158 — §sb-i SRAA.

**Extrait :** « Cette dernière action explique le risque d’hyperkaliémie quand on la bloque. »

**Lacune :** L’explication est partiellement présente, mais elle ne détaille pas la signalisation intracellulaire de l’aldostérone, ENaC, la Na⁺/K⁺-ATPase, le gradient favorisant la sécrétion de potassium ni le signal de la macula densa. Soif et fibrose font intervenir plusieurs voies.

**Correction proposée :** Réutiliser les fenêtres SRAA et potassium. Préciser les cibles du tube collecteur et expliquer les conditions de maintien des doses selon fonction rénale et kaliémie, avec un mécanisme précis.

**Références de ce constat :** S06. **État de correction :** à traiter.

### I50-079 — P2

**Source :** `chapters/I50/I50_c.html`, ligne 161 — §sb-i, tableau des dix cibles.

**Extrait :** « Couplé à la protéine Gs → AMPc »

**Lacune :** La nature des cibles est listée, mais les voies GPCR/AMPc/PLC, la transcription par le récepteur minéralocorticoïde, le lien glycosides–NCX–calcium, la vasodilatation par sGC et le rôle de If ne sont pas toutes reliées à l’effet clinique et à l’indication.

**Correction proposée :** Pour chaque classe, relier cible, signal, effet, bénéfice démontré et risque. Harmoniser les définitions finales de Gs et Gq.

**Références de ce constat :** S07, S08, S15. **État de correction :** à traiter.

### I50-080 — P1

**Source :** `chapters/I50/I50_c.html`, ligne 172 — §sb-i énergie.

**Extrait :** « à une utilisation accrue du glucose, avec un rendement énergétique réduit. »

**Lacune :** La phrase peut confondre quantité totale d’ATP produite et efficacité par quantité d’oxygène consommée : le glucose est plus économe en oxygène que les acides gras. Le remodelage métabolique est variable. Le statut hypothétique de l’apport cétonique sous iSGLT2 est correctement conservé à la fin du paragraphe.

**Correction proposée :** Expliquer le déficit de réserve énergétique et de flexibilité mitochondriale plutôt qu’un rendement intrinsèquement inférieur du glucose. Une source expérimentale primaire reste à valider.

**Références de ce constat :** S02. **État de correction :** à traiter.

### I50-081 — P1

**Source :** `chapters/I50/I50_c.html`, ligne 176 — §sg-i génétique.

**Extrait :** « est une cause d’hypertrophie ventriculaire curable par enzymothérapie ou chaperon. »

**Lacune :** Un traitement spécifique de Fabry ne signifie pas une guérison. Le regroupement de TTN, FLNC et DSP parmi les variants à risque manque de précisions sur le type de variant et son contexte. Le lien entre cardiomyopathie génétique, notamment LMNA, et décision de défibrillateur reste bref.

**Correction proposée :** Remplacer « curable » par « accessible à un traitement spécifique ». Expliquer phénotype, pénétrance, pathogénicité, critères de sélection du migalastat et évaluation du risque rythmique selon plusieurs critères.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-082 — P2

**Source :** `chapters/I50/I50_c.html`, ligne 178 — §sg-i, génétique et guide.

**Extrait :** « Un diagnostic génétique justifie un dépistage des apparentés au premier degré »

**Lacune :** Le guide consacré aux VUS est utile, mais les familles de gènes ne sont pas suffisamment reliées à la chaîne protéine–atteinte–test–décision : titine, sarcomère, lamines/enveloppe nucléaire, desmosomes et régulation calcique. La référence aux recommandations de cardiomyopathies de 2023 reste à vérifier.

**Correction proposée :** Ajouter des fenêtres par famille génétique, avec conseil génétique, dépistage en cascade et surveillance lorsque le résultat est négatif ou non concluant. Rechercher et vérifier la source ESC 2023 sur les cardiomyopathies.

**Références de ce constat :** S01. **État de correction :** à traiter.

### I50-083 — P2

**Source :** `chapters/I50/I50_justifications.json`, ligne 14 — 21 entrées et couverture des ancres.

**Extrait :** « "anchor": "e-2" »

**Lacune :** Les 21 fenêtres constituent un progrès explicatif, mais le décompte des ancres uniques et des blocs couverts reste à confirmer : 19 ancres et 17 blocs sont évoqués de façon incertaine. L’inventaire signale 13 entrées sur 21 centrées sur le bilan ou l’échocardiographie. La couverture n’est pas achevée et des répétitions contradictoires persistent.

**Correction proposée :** Réutiliser les fenêtres dans les passages répétés en évitant les boutons imbriqués. Cartographier chaque affirmation, son ancre et la fenêtre effectivement visible. Conserver les 21 identifiants et le contexte local. Confirmer les décomptes dans l’état avant correction de la banque.

**Références de ce constat :** S02, S03. **État de correction :** à traiter.

### I50-084 — P2

**Source :** `chapters/I50/I50_justifications.json`, ligne 592 — i50-j-energie-relaxation.

**Extrait :** « "text": "contractilité" »

**Lacune :** Le point d’entrée intitulé « contractilité » ouvre une fenêtre surtout consacrée à la relaxation active. Le lecteur qui cherche l’explication de la force intrinsèque reçoit donc une réponse partielle.

**Correction proposée :** Adapter l’intitulé ou expliquer distinctement contractilité et relaxation, avec le rôle de l’ATP et du calcium. Conserver l’ancre et l’identifiant.

**Références de ce constat :** S02. **État de correction :** à traiter.

### I50-085 — P2

**Source :** `chapters/I50/I50_justifications.json`, ligne 40 — Sources de toutes les entrées.

**Extrait :** « NICE — Insuffisance cardiaque chronique, NG106 : diagnostic et surveillance, mise à jour 2025 »

**Lacune :** Les 38 URL uniques n’ont pas fait l’objet ici d’une vérification exhaustive de leur contenu. L’accès à NICE a renvoyé une erreur 403, le texte OUP intégral n’est pas certifié lu et certaines pages PubMed/PMC sont vides ou bloquées par reCAPTCHA. Des mécanismes formulés prudemment ne suffisent pas à valider les indications et règles suisses applicables.

**Correction proposée :** Ajouter un journal indiquant accès, affirmation soutenue, date et type de preuve. Ne pas présenter toutes les références comme relues ; vérifier PMID, titre et contenu de source lors du prochain lot.

**Références de ce constat :** S17. **État de correction :** à traiter.

### I50-086 — P1

**Source :** `glossary/cardio_1.py`, ligne 8 — FEVG/Ee/GLS/TAPSE/PAPi/QRS/TMF.

**Extrait :** « Normale ≥ 50 % (ESC 2026). »

**Lacune :** Les définitions globales reprennent une FEVG « normale » fondée sur un seuil de classification, une interprétation isolée d’E/e′, un seuil de PAPi généralisé et des indications de CRT/TMF sans conditions. Elles ne disposent pas de références propres.

**Correction proposée :** Harmoniser avec les constats I50-054, I50-055, I50-056, I50-065 et I50-036. Expliquer chaque paramètre et ses limites, avec des références primaires explicites.

**Références de ce constat :** S01, S02, S12. **État de correction :** à traiter.

### I50-087 — P2

**Source :** `glossary/cardio_1.py`, ligne 104 — GMP/ATPase/V2/ARA.

**Extrait :** « Guanosine monophosphate (ici sous sa forme cyclique, GMPc) »

**Lacune :** GMP et GMPc désignent des molécules différentes. Les ATPases forment une classe plus large que les seules pompes de transport. L’action du récepteur V2 sur les aquaporines demande une chaîne de signalisation, et l’usage d’ARA pour ARA II doit être présenté comme une convention contextuelle.

**Correction proposée :** Rédiger des définitions génériques exactes et expliquer V2→Gs/AMPc→AQP2. Utiliser GMPc lorsque le contexte biochimique concerne le messager cyclique.

**Références de ce constat :** S15. **État de correction :** à traiter.

### I50-088 — P1

**Source :** `glossary/j45.py`, ligne 41 — Définitions effectives de Gs/Gq dans le tableau I50.

**Extrait :** « Active l’adénylate cyclase après liaison d’un agoniste bêta-2. »

**Lacune :** Les définitions finales de Gs et Gq restent centrées sur des exemples pulmonaires. Elles sont trop étroites pour les récepteurs β1 et AT1 présentés dans I50.

**Correction proposée :** Définir les protéines G de manière générique, puis donner β1/β2 et AT1/M3 comme exemples, avec les voies AMPc et PLC. Rechercher et citer IUPHAR et coordonner la modification avec les autres chapitres consommateurs.

**Références de ce constat :** S15, S16. **État de correction :** corrigé ciblé.

**Portée de la correction :** Les définitions effectives de Gs/Gq ont été corrigées. Cette correction ciblée ne certifie pas tous les concepts du constat.

### I50-089 — P1

**Source :** `glossary/cardio_2.py`, ligne 62 — I NEED HELP/FINEARTS-HF/TRED-HF/CASTLE/COAPT.

**Extrait :** « réduction des événements d’insuffisance cardiaque et du décès cardiovasculaire. »

**Lacune :** Le seuil de l’aide-mémoire I NEED HELP doit être confronté à la version 2026. La formulation de FINEARTS-HF peut faire croire à une réduction significative de la mortalité cardiovasculaire isolée. Les limites de population et d’application des essais TRED-HF, CASTLE et COAPT manquent.

**Correction proposée :** Présenter précisément le critère composite, le bénéfice observé et les limites de chaque essai, avec une fenêtre méthodologique. Actualiser I NEED HELP selon le repère 2026 : FEVG < 20 % ou mauvaise fonction VD.

**Références de ce constat :** S01. **État de correction :** partiellement corrigé.

**Portée de la correction :** Le repère I NEED HELP a été corrigé dans cardio_2 et dans le popup. Les résumés des essais et leurs limites restent ouverts.

### I50-090 — P2

**Source :** `glossary/cardio_2.py`, ligne 15 — BPCO, HbA1c, CIM-10, OFSP et syndrome d’ADH inappropriée.

**Extrait :** « Nomenclature de codage diagnostique en vigueur en Suisse (version 2024 dans MEDINA). »

**Lacune :** Les énoncés cliniques et réglementaires du glossaire manquent de sources datées. L’interprétation diagnostique de l’HbA1c nécessite conditions et confirmation ; une version CIM de 2024 ne peut être présentée comme actuelle en 2026 sans preuve. Les règles suisses, notamment la mention d’une seule indication, restent à vérifier.

**Correction proposée :** Citer des sources datées et adapter l’actualisation à chaque question. Rechercher les sources primaires Swissmedic, OFSP et SSC nécessaires ; distinguer la version historique du projet de la nomenclature actuellement applicable.

**Références de ce constat :** S06. **État de correction :** à traiter.

## Sources consultées et limites d’accès

Les statuts d’accès ci-dessous sont ceux consignés pendant l’audit ; la présente réécriture ne les transforme pas en lectures intégrales. Une recommandation générale peut soutenir une indication sans établir chaque mécanisme expérimental du texte. Les sources inventoriées dans la banque ne sont pas toutes vérifiées.

- **S01** — [ESC 2026 — page officielle et Official Slide Set (105 pages)](https://dam-assets.escardio.org/download/b2e587389baa11f185de06bdfb3e4be9). Accès consigné : PDF primaire intégral consulté par recherche; article original OUP non certifié intégralement.
- **S02** — [ASE 2025 — fonction diastolique et diagnostic ICFEp, DOI 10.1016/j.echo.2025.03.011](https://www.asecho.org/wp-content/uploads/2025/07/Left-Ventricular-Diastolic-Function.pdf). Accès consigné : PDF primaire intégral, tableaux 4/6 et algorithmes consultés.
- **S03** — [Myhre et coll. 2019 — BNP sous sacubitril/valsartan, analyse PARADIGM-HF](https://www.jacc.org/doi/10.1016/j.jacc.2019.01.018). Accès consigné : Publication primaire identifiée/recherche JACC et dépôt auteurs; PubMed direct renvoie parfois contenu vide et PMC reCAPTCHA.
- **S04** — [Pieske et coll. — HFA-PEFF, consensus primaire 2019/2020](https://orbi.uliege.be/bitstream/2268/290869/1/European%20J%20of%20Heart%20Fail%20-%202020%20-%20Pieske%20-%20How%20to%20diagnose%20heart%20failure%20with%20preserved%20ejection%20fraction%20the%20HFA%20PEFF.pdf). Accès consigné : PDF primaire auteur trouvé; intervalle 375–660 FA vérifié.
- **S05** — [Reddy et coll. 2018 — développement original H2FPEF](https://pubmed.ncbi.nlm.nih.gov/29792299/). Accès consigné : Résumé primaire indexé; accès direct parfois vide.
- **S06** — [KDIGO 2024 — maladie rénale chronique](https://kdigo.org/wp-content/uploads/2024/03/KDIGO-2024-CKD-Guideline.pdf). Accès consigné : PDF primaire intégral accessible (199 pages).
- **S07** — [ENTRESTO — notice réglementaire FDA/DailyMed](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=000dc81d-ab91-450c-8eae-8eb74e72296f). Accès consigné : Notice primaire accessible; ne remplace pas Swissmedic pour statut suisse.
- **S08** — [LASIX — notice réglementaire FDA/DailyMed](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2c9b4d8f-0770-482d-a9e6-9c616a440b1a). Accès consigné : Notice primaire accessible.
- **S09** — [Panza et coll. 2019 — viabilité, STICH](https://pubmed.ncbi.nlm.nih.gov/31433921/). Accès consigné : Résumé primaire lu.
- **S10** — [Perera et coll. 2023 — viabilité, analyse primaire REVIVED-BCIS2](https://jamanetwork.com/journals/jamacardiology/fullarticle/2810727). Accès consigné : Publication primaire et conclusions indexées consultées.
- **S11** — [Gillmore et coll. 2016 — diagnostic ATTR sans biopsie](https://pubmed.ncbi.nlm.nih.gov/27143678/). Accès consigné : Résumé primaire lu.
- **S12** — [Morine et coll. 2016 — PAPi avant assistance gauche](https://pubmed.ncbi.nlm.nih.gov/26564619/). Accès consigné : Résumé primaire indexé; ouverture directe erreur intermittente.
- **S13** — [ESC/ERS 2022 — hypertension pulmonaire](https://academic.oup.com/eurheartj/article/43/38/3618/6673929). Accès consigné : Définitions primaires indexées vérifiées; ouverture directe erreur intermittente.
- **S14** — [Ezekowitz et coll. 2022 — essai primaire SODIUM-HF](https://pubmed.ncbi.nlm.nih.gov/35381194/). Accès consigné : Publication primaire indexée consultée.
- **S15** — [IUPHAR/BPS — Concise Guide 2025/26, récepteurs G](https://air.unimi.it/retrieve/f2a805a6-9cad-47bd-ab43-c7ca8ca4be2c/British%20J%20Pharmacology%20-%202026%20-%20Alexander%20-%20The%20Concise%20Guide%20to%20PHARMACOLOGY%202025%2026%20%20G%20protein%E2%80%90coupled%20receptors.pdf). Accès consigné : PDF primaire 2025/26 intégral vérifié via DOI 10.1111/bph.70230 ; couplages β1–Gs et AT1–Gq vérifiés.
- **S16** — [IUPHAR/BPS — β1 adrenoceptor](https://www.guidetopharmacology.org/GRAC/ObjectDisplayForward?objectId=28). Accès consigné : Page officielle β1 bloquée par un mur de connexion : pas de lecture complète de cette page. Le couplage β1–Gs est vérifié dans le PDF intégral IUPHAR 2025/26, DOI 10.1111/bph.70230 (S15).
- **S17** — [NICE NG106 — insuffisance cardiaque](https://www.nice.org.uk/guidance/ng106/chapter/recommendations). Accès consigné : Ouverture 403; ne pas présenter cette lecture comme vérification complète.

## Vérifications et références encore nécessaires

Les points suivants nécessitent une source propre à l’affirmation, ou un contrôle d’accès et de contenu supplémentaire. Une référence générale à ESC, ASE ou KDIGO ne suffit pas à les clore. Les références repérées dans l’annexe restent à rattacher précisément aux passages correspondants.

| Constats | Source ou vérification attendue |
|---|---|
| I50-001, I50-037, I50-039, I50-043, I50-090 | Sources suisses datées : adoption du référentiel et examen fédéral, centres de transplantation, recommandations vaccinales OFSP, aptitude à la conduite, informations Swissmedic et version CIM applicable. |
| I50-005, I50-016, I50-020 | Cohortes contemporaines avec dénominateurs et périodes, études sur la fréquence des symptômes, performance clinique des jugulaires et mécanisme d’adaptation lymphatique. |
| I50-007 à I50-011, I50-019, I50-051, I50-069 à I50-071, I50-074, I50-078 à I50-080 | Sources primaires ciblées sur la congestion et les signes, le modèle microvasculaire de l’ICFEp, l’anatomie, l’histologie, les modèles de mécanique ventriculaire et le métabolisme. Les travaux repérés en annexe ne couvrent pas automatiquement toute la chaîne affirmée. |
| I50-013, I50-043, I50-045 | Recommandations et travaux propres aux traitements étiologiques, à la cardio-oncologie et à la grossesse ; vérifier leur portée et leur actualité. L’ESC grossesse 2025 est repérée dans l’annexe, sans attestation de lecture intégrale. |
| I50-031, I50-032, I50-035, I50-041, I50-046 à I50-048, I50-089 | Publications originales et populations des essais STRONG-HF, TRED-HF, STEP-HFpEF/SUMMIT, essais de fer, CASTLE, COAPT et essais concernant la FA. Distinguer programmes complets, critères composites et résultats individuels. FINEARTS-HF et FAIR-HF2 sont repérés dans l’annexe ; leurs accès et résultats doivent rester décrits précisément. |
| I50-037, I50-038, I50-066 | Recommandations ISHLT et travaux de sélection pour transplantation ou assistance. La version ISHLT 2024 est repérée en annexe, mais sa lecture intégrale et son application à chaque seuil ne sont pas attestées. |
| I50-052, I50-053, I50-090 | Sources propres aux critères et cibles HbA1c, anémie, TSH, potassium et à la définition de l’infarctus ; distinguer seuil diagnostique, intervalle de laboratoire et cible thérapeutique. |
| I50-057, I50-060, I50-061, I50-064, I50-072 | Références valvulaires, études comparatives d’échographie pulmonaire, recommandations SCMR et méthodes de mesure hémodynamique. Le consensus EACVI 2023 ouvert en annexe ne remplace pas toutes les études comparatives nécessaires. |
| I50-081, I50-082 | ESC 2023 sur les cardiomyopathies et références propres à la pathogénicité, la pénétrance, au risque rythmique et aux traitements génétiques ; références exactes et contenu restant à vérifier. |
| I50-083 à I50-085 | Cartographie des 21 ancres et de leurs blocs, vérification des 38 URL de la banque, correspondance titre–PMID–contenu et journal d’accès par affirmation. Les décomptes incertains des ancres ne doivent pas être utilisés comme mesure d’achèvement. |
| I50-087 ; limites de source de I50-088 | Références propres aux autres définitions et à leurs chaînes de signalisation, notamment V2 et GMPc. Le PDF IUPHAR 2025/26 a été vérifié intégralement pour β1–Gs et AT1–Gq (S15) et les définitions Gs/Gq ont reçu une correction ciblée. La page β1 elle-même reste inaccessible derrière un mur de connexion (S16). |

## Annexe : popups et pharmacologie

Le [rapport détaillé des popups et de la pharmacologie](sandbox:/workspace/scratch/6eaecafb4b19/i50_popups_pharma_assertion_audit.md) porte sur l’intégralité de I50_pop1 à I50_pop4 et I50_d. Il ajoute des repères par ligne, des nuances sur les doses, contre-indications, dispositifs et mécanismes, ainsi que 28 groupes de sources avec leurs limites d’accès. **Ses identifiants S1–S28 sont propres à cette annexe ; ils ne correspondent pas aux S01–S17 du présent rapport.** I50_d ne contient pas de quiz ; les quiz examinés dans les constats initiaux sont dans I50_c.

L’annexe distingue notamment les conditions alternatives de l’ESC 2021 pour l’évolution de créatinine et de DFG. Sa référence S14 a été actualisée depuis le PDF officiel intégral ouvert par le responsable de l’audit : hausse de créatinine < 50 % et valeur < 266 µmol/L, ou baisse du DFG < 10 % et DFG restant > 25 mL/min/1,73 m², avec évaluation clinique. Il ne s’agit pas d’une conjonction globale de toutes ces conditions.

Le [complément des lacunes du glossaire](sandbox:/workspace/scratch/6eaecafb4b19/I50_GLOSSAIRE_LACUNES_COMPLEMENT_2026-10-07.md) présente neuf constats supplémentaires, I50-091 à I50-099, issus des 63 définitions nouvellement repérées. Ils complètent les 90 constats initiaux conservés ici et dans l’inventaire ; leurs sources et leurs statuts sont décrits dans cette annexe. Le complément consigne notamment la source originale STRONG-HF : cette publication est donc repérée, mais la portée du résultat et son rattachement aux passages doivent encore être traités.

## Banque de 21 justifications : apports et portée

Les 21 entrées présentent une explication, un mécanisme, une implication, des limites et des références. Elles développent notamment anémie et transport d’oxygène, eau–sodium et ADH, potassium et conduction, congestion veineuse rénale, fer et mitochondries, thyroïde, diabète, congestion hépatique, troponine, albuminurie, ARNI et peptides natriurétiques, obésité, e′, orthopnée, œdèmes, fibrose et réentrée, énergie et relaxation, diurétiques, bêtabloquants, filtration sous traitement et AINS. Ces explications ne corrigent pas automatiquement les énoncés contradictoires répétés dans les tableaux et les corrigés, et ne couvrent pas tous les autres symptômes, examens, causes, seuils et traitements.

## Travail restant

1. Corriger les contradictions vérifiées et leurs répétitions, avec sources exactes et journal distinct des modifications.
2. Traiter les autres constats en ajoutant les explications et les références propres à chaque affirmation.
3. Relire les contenus corrigés, y compris quiz, dessins, légendes, Pareto et définitions après fusion.
4. Vérifier les 21 ancres et la compilation selon le périmètre autorisé au responsable, sans modifier les identifiants ou le moteur au titre de cet audit.
5. Maintenir le statut **NON ACHEVÉ** tant que les lacunes restantes et leurs corrections n’ont pas été traitées puis relues.


# Neuf constats complémentaires du glossaire


Le dénombrement initial de 104 clés excluait le texte des templates. L’extraction corrigée repère 167 clés candidates dans les huit HTML, soit 63 définitions supplémentaires. Ces 63 définitions ont été lues intégralement. La recherche compte parfois un sous-terme d’un sigle composé ; elle ne prétend donc pas reproduire exactement les boutons créés par le moteur. Le fichier JSON associé conserve les définitions examinées.

Ces constats complètent les groupes I50-086 à I50-090 du rapport principal. **Aucune des corrections ci-dessous n’a été injectée dans ce lot.** Les termes sans définition propre mais reliés à une fenêtre ont aussi été considérés ; l’existence d’un renvoi ne prouve pas que la fenêtre explique toute l’affirmation.

| ID | Source et termes | Extrait exact | Lacune constatée et correction recommandée | Référence et état |
|---|---|---|---|---|
| I50-091 | `glossary/cardio_1.py` : ST, BBG | « ses déplacements traduisent une ischémie ou une lésion myocardique » | Le déplacement ST n’est pas spécifique d’ischémie. La morphologie du BBG est résumée à V1/V6, sans tous les critères ni distinction asynchronisme électrique/mécanique. Décrire les limites, les diagnostics concurrents et les critères ECG complets. | La recommandation ESC ACS 2023 a été identifiée, mais son ouverture OUP a échoué. Les références ECG et recommandations de conduction exactes restent à sélectionner et vérifier. À traiter. |
| I50-092 | `glossary/cardio_1.py` : OG, POD, PAPS, B3 | « intègre la chronicité des pressions de remplissage élevées » | OG et B3 ne doivent pas devenir une preuve universelle de dysfonction. PAPS = gradient VD–OD + POD, avec qualité du jet et absence d’obstruction à considérer. POD ≤8 mmHg et pression jugulaire nécessitent contexte de position, respiration et technique. Ajouter acquisition, limites et conséquences cliniques. | [ASE 2025, fonction diastolique](https://www.asecho.org/wp-content/uploads/2025/07/Left-Ventricular-Diastolic-Function.pdf) et [ASE 2025, cœur droit, DOI 10.1016/j.echo.2025.01.006](https://www.asecho.org/wp-content/uploads/2026/08/ASE-Right-Heart-Guidelines-May-2025.pdf), PDF primaires disponibles, passages pertinents vérifiés : TAPSE §B, PAPS §C et tableau 5. La référence propre au B3 reste à sélectionner. À traiter. |
| I50-093 | `glossary/zz_fusion.py` : définition effective VNI | « Indication clé : acidose respiratoire de l’exacerbation de BPCO » | La définition fusionnée renvoie à la fenêtre J44 alors que le cours I50 utilise la VNI pour l’œdème cardiogénique. Conserver les deux indications et expliquer les critères propres à l’IC, ainsi que les limites en hypotension, défaillance VD ou impossibilité de protéger les voies aériennes. Vérifier le renvoi dans le fragment cardiologique livré. | ESC 2026, prise en charge décompensée ; contrôle du rendu confié à l’orchestrateur. À traiter. |
| I50-094 | `glossary/cardio_1.py` : T1, T2, Ciné-IRM | « le calcul du volume extracellulaire en dérive » | Le volume extracellulaire ne dérive pas du seul T1 natif : il repose sur des mesures avant/après contraste et l’hématocrite. Les plages T1/T2 dépendent du matériel et de la séquence ; elles ne donnent pas seules une étiologie. Distinguer ciné, cartographie native et ECV. | [Consensus SCMR/EACVI 2017, DOI 10.1186/s12968-017-0389-8](https://link.springer.com/article/10.1186/s12968-017-0389-8), texte primaire complet accessible et passage ECV vérifié : mesures natives/après contraste et hématocrite ; ECV synthétique possible si calibration connue. À traiter. |
| I50-095 | `glossary/cardio_2.py` : DELIVER | « réduction des aggravations et du décès cardiovasculaire » | Le résultat principal est composite. Le décès cardiovasculaire isolé n’est pas significativement réduit : HR 0,88, IC95 % 0,74–1,05. Réécrire « réduction du critère composite aggravation de l’IC ou décès cardiovasculaire », puis préciser le rôle des événements d’IC. | [DELIVER original, NEJM 2022](https://doi.org/10.1056/NEJMoa2206286), résumé primaire indexé vérifié ; ouverture du texte NEJM bloquée (403). À traiter. |
| I50-096 | `glossary/cardio_2.py` : STRONG-HF | « réduction des réhospitalisations et des décès à 180 jours » | La phrase peut laisser croire que la mortalité isolée a été démontrée. Nommer le critère composite réhospitalisation pour IC ou décès toutes causes. Le bénéfice appartient à un programme de titration et de suivi intensifs ; il ne se réduit ni au NT-proBNP ni à une consultation. | [STRONG-HF original, Lancet 2022](https://pubmed.ncbi.nlm.nih.gov/36356631/), résumé primaire vérifié. À traiter. |
| I50-097 | `glossary/cardio_2.py` : essais des traitements | « réduction de 30 % de la mortalité » | RALES et les autres essais omettent souvent FEVG, NYHA, rein/potassium, traitement de fond, durée et caractère composite. Les seuils historiques ne changent pas rétroactivement avec la nomenclature ESC 2026. Ajouter des fenêtres méthodologiques liées à chaque essai ; éviter de généraliser un résultat à tout le phénotype actuel. | [PARADIGM-HF original](https://doi.org/10.1056/NEJMoa1409077) : seuil d’inclusion ≤40 %, puis ≤35 % après amendement, vérifié dans le texte primaire indexé. Les autres protocoles doivent être vérifiés individuellement. À traiter. |
| I50-098 | `glossary/cardio_2.py` : DIGIT-HF, VICTORIA, IRONOUT-HF, HELIOS-B | « le fer oral est inefficace » | Un échec d’amélioration de VO₂ dans une population et un protocole précis ne prouve pas l’inefficacité de tout fer oral pour toute anémie. Pour les essais digitoxine, vériciguat et vutrisiran, préciser population, traitement concomitant, critère composite et risques, sans déduire une mortalité isolée d’un composite. | [DIGIT-HF original, NEJM 2025](https://doi.org/10.1056/NEJMoa2415471), population FEVG ≤40 %/NYHA III–IV ou ≤30 %/NYHA II et critère composite vérifiés dans le résumé primaire. [IRONOUT-HF original, JAMA 2017](https://jamanetwork.com/journals/jama/fullarticle/2626574), texte primaire accessible, VO₂ à 16 semaines et population vérifiés. Les autres détails restent à vérifier. À traiter. |
| I50-099 | Définitions sans développement propre : VD, FC, PA, DAI, BB, QCM, AVC ; définitions réglementaires SIADH/CIM | « seule indication suisse autorisée du tolvaptan » | Une expansion littérale ne remplace pas toujours le pourquoi clinique ; les renvois DAI/BB/PA sont utiles mais doivent être relus. La phrase sur le tolvaptan est trop générale : Samsca est indiqué dans l’hyponatrémie secondaire au SIADH ; Jinarc dans la polykystose rénale autosomique dominante. Distinguer les spécialités, puis vérifier leurs notices intégrales avant de discuter un emploi dans l’IC. La version CIM utilisée par le projet est à distinguer de la version nationale en vigueur. | [Compendium, Samsca](https://compendium.ch/fr/product/1409439-samsca-cpr-30-mg) et [Compendium, Jinarc](https://compendium.ch/fr/product/1320733-jinarc-cpr-60-mg-30-mg), pages produit/brevier et indications consultées. Les notices intégrales et la documentation nationale de codage ne sont pas entièrement vérifiées ici. À traiter. |

Les termes ATP, SERCA2a, ECA, RM, sGC, CYP3A4, Na-K-2Cl, TTR et CyBorD ont été lus aussi. Leurs mécanismes ont été examinés avec les fenêtres correspondantes de l’annexe popups. La brièveté de ces définitions laisse notamment à compléter les chaînes signal → réponse → examen ou traitement, la sélection de la population et les risques. Cela ne signifie pas que tous ces termes comportent une erreur factuelle.

HFrEF, HFpEF et HFmrEF ont été lus et confrontés au référentiel ESC 2026. La fusion des catégories n’est pas déclarée erronée par comparaison avec des classifications antérieures. Les résumés d’essais ne certifient pas, à eux seuls, la prescription actuelle suisse.

**NON ACHEVÉ.** Ce complément documente les lacunes constatées après correction de l’extraction. Il n’attribue aucun score automatique de complétude médicale.


# Annexe : pharmacologie et anciennes fenêtres


Date : 7 octobre 2026. Périmètre intégral : `medina/chapters/I50/I50_pop1.html` (71 lignes), `I50_pop2.html` (78), `I50_pop3.html` (75), `I50_pop4.html` (133), `I50_d.html` (69). Aucun quiz dans ces cinq fichiers : `I50_d.html` est l’onglet Pharmacologie. Cette lecture initiale n’a modifié aucun fichier du dépôt et n’a lancé ni build ni test. Les citations et numéros de lignes ci-dessous correspondent aux sources avant corrections.

Les corrections ciblées ont ensuite été injectées au commit `de86fcc1792424e4a0a933ace0e7a5213475f727`. Leur état actuel est détaillé dans [I50_CORRECTIONS_ET_RESERVES_2026-10-07.md](sandbox:/workspace/scratch/6eaecafb4b19/I50_CORRECTIONS_ET_RESERVES_2026-10-07.md) et dans le journal JSON. Sont corrigées les contradictions chiffrées HFA-PEFF, les répétitions BNP/ARNI, I NEED HELP, la contre-indication dronédarone, l’interaction vériciguat/nitrés et les repères créatinine/potassium. Les indications CRT, le choc, l’hypotension et la ligne finérénone ont été contextualisés. Les explications plus larges regroupées avec ces passages restent ouvertes lorsqu’elles ne figurent pas dans le journal. Les autres lacunes de cette annexe restent à traiter.

Les priorités P1/P2/P3 ci-dessous constituent le classement initial propre à cette annexe ; le rapport principal utilise P0/P1/P2. Ces étiquettes ne doivent pas être additionnées ni assimilées à un score de complétude. La lecture de tous les fichiers couverts ne certifie pas chaque affirmation.

Le préfixe de tous les chemins cités ci-dessous est `/workspace/scratch/6eaecafb4b19/medina/chapters/I50/`. Les citations sont des extraits courts des fichiers audités. P1 = erreur de sécurité ou conduite pouvant être mal appliquée ; P2 = erreur factuelle/diagnostique ou généralisation importante ; P3 = explication pédagogique/contextuelle manquante. Les P3 sont des propositions d’amélioration, pas des accusations d’erreur médicale.

## Résultats prioritaires

| Référence | Citation | Constat et recommandation | Vérification |
|---|---|---|---|
| I50_d.html:52 | «50 % (ou jusqu’à 266 µmol/L)» | **P1 — OU au lieu de ET.** L’acceptabilité décrite par ESC 2021 associe une hausse <50 % au maintien de la créatinine <266 µmol/L, avec une limite de DFG. Ne pas présenter 266 comme une permission d’augmentation illimitée depuis une valeur basse. Donner les conditions cumulatives, la trajectoire et la réévaluation clinique. | S14, source primaire, texte indexé confirmé. |
| I50_d.html:52,56 ; I50_pop4.html:80 | «réduire le diurétique avant…» | **P1 — manque l’état volémique.** Réduire un diurétique chez un patient encore congestif peut aggraver l’IC. Cette manœuvre concerne l’absence de congestion/hypovolémie ; rechercher pertes, déshydratation, infection, AINS et autres hypotenseurs. | S1, S14 ; nuance clinique issue des algorithmes. |
| I50_pop4.html:100 | «ne pas associer aux dérivés nitrés» | **P1 — interdiction générale inexacte pour vériciguat.** Les nitrés courts ont été bien tolérés dans l’IC ; l’expérience avec les nitrés longs est limitée. Écrire précaution et surveillance tensionnelle selon RCP, pas contre-indication absolue. Les PDE5 et autres stimulateurs de sGC nécessitent une ligne distincte, dépendante du RCP suisse. | S15, RCP fabricant complet vérifié par l’agent pharmacologie. |
| I50_d.html:64 | «dronédarone (FEVG ≤40 % ou…instable)» | **P1 — contre-indication suisse trop étroite.** Le RCP suisse contre-indique l’insuffisance cardiaque, sans limiter à une FEVG ≤40 % ni à l’instabilité. RCP fabricant UK : IC actuelle ou antérieure/dysfonction systolique VG. Corriger et expliquer les données ANDROMEDA/PALLAS. | S16, information professionnelle suisse et RCP fabricant vérifiés. |
| I50_pop3.html:22 | «mineur 365–660» | **P2 — faute numérique HFA-PEFF.** NT-proBNP mineur en FA = 375–660 pg/mL, pas 365. | S2, texte primaire indexé et validation primaire S2b. |
| I50_pop3.html:20 | «e′ septale <7 ou latérale <10» | **P2 — seuils HFA-PEFF non adaptés à l’âge.** Ces seuils s’appliquent avant 75 ans ; à ≥75 ans : septal <5 ou latéral <7 cm/s. Important dans le phénotype âgé du chapitre. | S2/S2b. |
| I50_pop3.html:70 | «QRS <130 ms : pas d’indication» | **P2 — exception BAV oubliée.** L’absence d’indication concerne les patients sans indication de stimulation pour BAV de haut degré. La phrase absolue contredit la ligne 69 du même popup. | S1, p. 57, lecture complète. |
| I50_pop3.html:5 ; I50_pop4.html:76 | «QRS ≥150 ms → CRT» | **P2 — indication amputée.** Un BBG large seul ne suffit pas ; conserver symptômes, FEVG ≤35 %, rythme, traitement et contexte de stimulation. Ajouter un lien vers la monographie CRT et reformuler «fait rechercher une indication». | S1, pp. 56–57. |
| I50_pop4.html:68 | «Dispositifs après ≥3 mois» | **P2 — délai commun DAI/CRT trop absolu.** Il reste un repère DAI primaire. ESC 2026 permet la planification simultanée TMF/CRT chez certains patients symptomatiques BBG ≥150, FEVG ≤35, avec réévaluation avant implantation (IIb). | S1 p. 57. |
| I50_pop3.html:74 | «Éjection : FEVG ≤25 %» | **P2 — version I NEED HELP non concordante avec 2026.** Les diapos officielles 2026 p. 71 indiquent EF <20 % **ou mauvaise fonction VD**. Ne pas inventer un diagnostic de stade D à partir de ce seul repère ; soit dater la version historique, soit actualiser. | S1 p. 71, extraction + capture lues. |
| I50_pop4.html:118 ; I50_pop2.html:33 | «PAS <90…définit le choc» | **P2 — définition trop rigide.** Le choc cardiogénique peut être normotensif ; un lactate normal n’élimine pas toute hypoperfusion, surtout dans l’IC chronique. L’index cardiaque invasif et les pressions élevées sont des descripteurs classiques, pas des prérequis chez tous, notamment certains chocs VD. Recentrer la définition sur l’hypoperfusion causée par dysfonction cardiaque. | S4, consensus SCAI complet ; S1 p. 60. |
| I50_pop4.html:119 | «E…arrêt circulatoire, réanimation en cours» | **P2 — E réduit à l’arrêt.** Le stade E comprend le choc réfractaire nécessitant plusieurs interventions simultanées ; un arrêt n’est pas obligatoire. | S4/S1. |
| I50_d.html:34 | «Finérénone» sous «Stratégie ICFEr» | **P2 — contexte de prescription trompeur.** La dose est exacte, mais le tableau sous ICFEr peut suggérer que finérénone remplace spironolactone/éplérénone pour toute ICFEr. ESC 2026 distingue ARM stéroïdien dans ICFEr et stéroïdien/non stéroïdien dans ICFEp ; FINEARTS incluait FEVG ≥40. Annoter l’indication/population de chaque traitement ajouté. | S1 pp. 49–50 ; S17. |
| I50_pop1.html:5 | «optimise le chevauchement» | **P2 — mécanisme Frank-Starling simplifié à tort.** La relation physiologique repose surtout sur l’activation dépendante de la longueur, la sensibilité calcique et le recrutement des ponts ; l’étirement n’augmente pas simplement le chevauchement. Garder calcium/titine et remplacer l’explication géométrique exclusive. | S5, expériences de sarcomères/cardiomyocytes. |
| I50_pop1.html:13 | «Pente télésystolique conservée» | **P2 — ICFEp hétérogène.** L’élastance télésystolique peut être augmentée ; FEVG conservée ne veut pas dire contractilité/réserve systolique normales. «Souvent conservée ou augmentée» + couplage ventricule-artères. | S6, études hémodynamiques originales. |
| I50_pop1.html:26 | «tamponnade (le ventricule ne s’étire pas)» | **P2 — généralisation.** Une compression péricardique peut atténuer les peptides, mais des taux élevés existent en tamponnade ; le ventricule «ne s’étire pas» est absolu et trompeur. Le BNP n’est pas un test d’exclusion de tamponnade. | S7, étude originale NT-proBNP/épanchement. |
| I50_pop2.html:8 | «Anthracyclines…souvent irréversible» | **P2 — dichotomie ancienne.** Une récupération partielle ou complète est possible si détection et traitement précoces ; ne pas apprendre «anthracyclines irréversibles, trastuzumab réversible» comme règle. | S8, cohorte originale Cardinale 2015. |
| I50_pop2.html:65–67 | «fréquence…rapide et prolongée» ; «se normalise» | **P2 — cardiomyopathie rythmique.** Les ESV fréquentes ne requièrent pas nécessairement une tachycardie soutenue ; mécanisme aussi par dyssynchronie. Une amélioration confirme la composante rythmique, la normalisation totale n’est pas obligatoire. L’attente avant DAI ne s’applique pas automatiquement à une prévention secondaire. | S9, séries originales d’ablation d’ESV ; S1 pour DAI. |
| I50_pop3.html:30 | «agents linéaires…proscrits» | **P2 — classification gadolinium trop absolue.** Le risque de FSN dépend du groupe d’agent ; tous les linéaires n’ont pas le même risque, certains sont de groupe II. En contexte suisse/européen, préciser l’agent autorisé et le protocole radiologique ; ne pas remplacer cette sélection par une règle mondiale linéaire=interdit. | S10, consensus ACR/NKF primaire ; accès intégral web partiel, texte indexé. |
| I50_pop4.html:9,60,72 | «non le BNP» ; «NT-proBNP sous ARNI» | **P2 — formulation exclusiviste.** Le NT-proBNP est plus simple à interpréter au début d’un ARNI ; le BNP conserve une valeur pronostique et ne devient pas inutilisable. Expliquer hausse pharmacologique possible + diminution de la contrainte sous traitement, plutôt qu’une interdiction de mesure. | S11, analyse originale PARADIGM-HF ; doublon avec audit parent. |
| I50_pop4.html:112 | «Fibrose…bloquée par les ARM» | **P2 — effet absolu injustifié.** ARM atténuent des voies profibrosantes ; ils ne bloquent pas toute fibrose ni n’effacent une cicatrice. Distinguer LGE focal et fibrose diffuse en T1/ECV. | S1/S3 ; inférence pédagogique, pas nouvelle efficacité clinique revendiquée. |

## Relecture des lacunes explicatives dans chaque fichier de popups

### I50_pop1.html — fondamentaux

| Lignes | Citation courte | Lacune et ajout recommandé |
|---|---|---|
| 4–7 | «précharge» ; «courbe s’aplatit» | **P3.** Distinguer précharge mécanique, volume et pression de remplissage, dépendante de la compliance. Dire que la courbe force-débit est déplacée/aplatie surtout en dysfonction systolique et que toute IC ne possède pas une unique courbe plate. La sécurité de la décongestion dépend de congestion préalable, VD et état volémique ; ce n’est pas une garantie contre l’hypotension. |
| 10–11 | «surface…travail cardiaque» | **P3.** La surface donne le travail mécanique externe par battement ; elle ne couvre pas toute dépense énergétique/consommation O₂. Définir les axes, valves et relations Ees/EDPVR pour relier les phrases au cycle. |
| 12–13 | «D’où…flash» | **P3.** Expliquer la poussée hypertensive par hausse brutale de postcharge/redistribution et la FA par perte de systole auriculaire/tachycardie ; l’œdème flash n’est pas spécifique ICFEp ni un effet obligatoire d’un petit gain de volume. |
| 16–19 | «baisse du sodium…macula densa» | **P3.** Dire que la macula densa détecte l’apport NaCl (lié débit tubulaire) et que l’IC peut activer SRAA malgré excès total d’eau/sodium : diminution de volume artériel efficace. Nommer angiotensinogène, surrénale et effets segmentaires. L’ajout ARM se fonde sur des essais pronostiques, pas sur l’échappement seul. |
| 22–24 | «excellente valeur prédictive négative» | **P3/P2.** Distinguer seuil d’exclusion et seuil de forte probabilité, préciser qu’un seuil élevé ne confirme pas seul l’IC. La VPN dépend de la probabilité prétest ; obésité/ICFEp et certains œdèmes très précoces donnent faux négatifs. Donner la zone grise. Le tableau d’âge peut rester historique daté tant qu’algorithme 2026 non vérifié en détail. |
| 25–26 | «Âge, insuffisance rénale, FA…» | **P3.** Liste de facteurs sans pourquoi : clairance et stress cardiaque rénal, parois/rythme/étirement atrial pour FA, moindre NP dans obésité par mécanismes multiples ; ne pas réduire tous les confondants à la clairance rénale. |
| 27 | «1 pmol/L…» | Explication suffisante pour la conversion ; utile de distinguer valeur analytique selon test, sans mécanisme additionnel indispensable. |
| 28 | «une baisse…de bon pronostic» | **P3.** Association pronostique ≠ preuve qu’une titration uniquement guidée par NP réduit les événements. Relier baisse à réduction de contrainte/congestion et préciser rein/FA/ARNI. |
| 31–33 | «E/e′ élevé (pression…)» | **P3/P2.** e′ et E/e′ sont des indices dépendants du contexte, à intégrer avec autres paramètres ; OG dilatée peut être FA/valvulopathie plutôt que seule chronicité d’IC. Décrire onde E (flux) et e′ (relaxation) et pourquoi le ratio augmente. Les deux troubles tachycardie/FA peuvent décompenser, pas toujours «brutalement». S3. |
| 36–39 | «IM secondaire, arythmies…» | **P3.** Chaînes manquantes : déplacement piliers/anneau→défaut coaptation ; fibrose→conduction hétérogène/réentrée ; géométrie→contrainte/inefficacité. Expliquer traitement comme contrôle d’activation neurohormonale et CRT comme correction dyssynchronie. |
| 42–44 | «pression oncotique…retient» | **P3.** C’est le modèle simplifié classique. Mentionner perméabilité/endothélium-glycocalyx et drainage lymphatique ; les seuils 18/25 ne sont pas universels et sont déjà correctement dits indicatifs. Distinguer pression capillaire réelle et pression d’occlusion. |
| 47–49 | «froid et humide…inotropes» | **P2/P3.** L’inotrope n’est pas automatique pour une étiquette froide : objectiver hypoperfusion, rechercher cause/volume, monitorer. Expliquer surmortalité/arythmies des inotropes et pourquoi vasodilatateurs peuvent aider sans hypotension. «Froid» clinique n’est pas à lui seul un choc. S1/S4. |
| 52–54 | «réserve…<80 %» | **P3.** Fournir formule (FCpic−FCrepos)/(FCmaxprédite−FCrepos), méthode FCmax et effort suffisant ; seuil sous BB non spécifié. Ajouter que données de retrait BB concernent surtout ICFEp avec incompétence chronotrope documentée et suivi, pas retrait routinier. S12. |
| 57–58 | «trois à six mois» | **P3.** Le risque culmine tôt mais ne cesse pas à six mois. La liste de causes inclut des facteurs associés, pas une attribution démontrée pour chaque décès. Décrire la fréquence des contacts STRONG-HF (phase intensive initiale) et l’éligibilité clinique. S1 p. 64. |
| 61–62 | «NYHA» | Explication suffisante ; pas de lacune mécanistique pertinente. |
| 65–66 | «σ = P×r/(2×h)» | **P3.** Préciser approximation de paroi mince/sphère ; ventricule épais/non sphérique ≠ application exacte. P diastolique/précharge et P systolique/postcharge ne sont pas interchangeables. |
| 69–71 | «phosphorylation réduite» | **P3.** Dire que l’effet dépend du site/kinase (PKA/PKG sur N2B réduisent rigidité ; certaines phosphorylations PKC la majorent). Variants tronquants TTN : pénétrance variable, pas maladie obligatoire. Troponine chroniquement élevée signifie lésion myocardique ; seule la dynamique/contexte soutient une cause aiguë/ischémique. S5/S13. |

### I50_pop2.html — clinique

| Lignes | Citation courte | Lacune et ajout recommandé |
|---|---|---|
| 5 | «oriente vers une coronarographie» | **P2/P3.** Une cardiopathie ischémique connue ne rend pas coronarographie obligatoire : symptômes, probabilité d’obstruction, possibilité/bénéfice revascularisation comptent. Le DAI dépend FEVG, TMF, délai post-IDM et espérance de vie, pas du seul antécédent. S1 pp. 18, 47, 53. |
| 8 | «trastuzumab…réversible» | **P3.** Expliquer topoisomérase/mitochondries pour anthracyclines, voie HER2 de survie myocytaire pour trastuzumab, inflammation immune pour ICI et lésions vasculaires/fibrose radiation ; préciser hétérogénéité de récupération et urgence si symptômes ICI. S8, cardio-oncologie ESC à compléter pour mécanismes. |
| 13 | «ne peut ni augmenter son débit» | **P2/P3.** Le débit augmente souvent mais insuffisamment à l’effort ; d’autres mécanismes de dyspnée interviennent (réserve chronotrope, périphérie/muscle, ventilation, poumon/VD). Réduire l’absolu et expliquer pression OG→capillaires. |
| 17–19 | «nombre…bon marqueur» | **P3.** Le nombre d’oreillers dépend des habitudes et d’autres causes ; questionner changement/latence/amélioration. Le mécanisme plateau Frank-Starling ne couvre pas tous les phénotypes ; le transfert central augmente les pressions quand réserve de remplissage/éjection limitée. |
| 22–24 | «dépression…centre respiratoire» | **P3.** Le volet mécanistique nocturne est présenté comme certain sans source ; privilégier redistribution/réabsorption et présenter facteurs neurorespiratoires comme contributeurs proposés. Distinguer apnée obstructive/centrale et dyspnée paroxystique nocturne. |
| 27–29 | «compression…retour veineux» | **P3/P2.** L’étude fondatrice établit augmentation des pressions pendant flexion ; hausse du retour veineux n’est pas une explication directement prouvée. Mentionner pression intrathoracique/abdominale et le contexte de petite étude d’IC systolique avancée. S18. |
| 32–34 | «PAS >110…autorise» | **P3.** Le seuil rend envisageable une vasodilatation, ne constitue pas une permission automatique : surveillance PA, hypoperfusion, valvulopathie/VD et autres médicaments. Pression différentielle étroite dépend aussi compliance artérielle ; signal, pas mesure du débit. S1. |
| 37–38 | «>2 kg…signale une rétention» | **P2/P3.** Alerte compatible, pas preuve (variabilité, balance, alimentation) ; une décompensation par redistribution peut survenir sans gain de poids. Décrire qui appeler, symptômes urgents et le plan prescrit d’ajustement, sans systématiser hausse diurétique. |
| 41–43 | «Killip dans l’infarctus» | **P3.** Expliquer le rôle de l’extension des râles/œdème/choc dans Killip et limiter à IDM ; pas score global IC chronique. Mécanisme des crépitants et différences avec fibrose manquants. |
| 47–48 | «décélération…remplissage» | Explication mécanistique déjà présente ; **P3** préciser B3 marque surcharge/dysfonction dans contexte adulte sans attribuer obligatoirement à une FEVG abaissée. |
| 51–54 | «signe…le plus fiable» | **P2/P3.** Jugulaire mesure surtout pression droite, peut être dissociée pression gauche ; difficulté obésité/examinateur. Distance oreillette-sternum 5 cm est approximation, variable position. RHJ n’indique pas exclusivement incapacité du VD : augmentation persistante reflète réserve cardiaque/remplissage élevés. Ne pas fonder toute décongestion sur un signe unique. |
| 57–58 | «alternance…calcium» | **P3.** Distinguer pulsus alternans (force mécanique) d’extrasystoles/bigéminisme et de variation respiratoire ; disponibilité calcique et restitution contractile sont mécanismes proposés, pas seule alternance de remplissage. |
| 61–62 | «CHAMP…causes banales» | **P2/P3.** Compléter explicitement infection et tamponnade (CHAMPIT déjà dans recommandations 2021 et diapos ESC 2025) ; ne pas appeler infection cause «banale» dans le Pareto. Explication d’une ligne par cause : ischémie contractilité, postcharge, débit/diastole arythmie, rupture/valve, surcharge VD EP. S19. |
| 65–67 | «contrôler la fréquence» | **P3.** Selon rythme, suppression/ablation des ESV ou restauration rythme peut être préférable à la seule fréquence. Relier fréquence prolongée à handling calcium, énergie et remodelage ; préciser le diagnostic causal par amélioration et exclusion d’autres étiologies. S9. |
| 70–73 | «parois épaisses et bas voltage» | **P3.** Pourquoi : dépôt extracellulaire épaissit parois mais dysfonction électrique ; dépôt tendon/ligaments précède signes cardiaques. Ce couple n’est ni constant ni spécifique. AL nécessite bilan urgent, ATTR sauvage n’entraîne pas dépistage génétique familial comme ATTR variant. Expliquer exclusion de protéine monoclonale pour éviter d’attribuer fixation AL à ATTR et nécessité SPECT pour distinguer pool sanguin. |
| 77–78 | «bromocriptine…anticoagulation» | **P3.** Le rationnel est correctement «proposé». Expliquer agonisme D2→suppression prolactine, suppression lactation et risque thrombotique justifiant anticoagulation. Distinguer grossesse et allaitement ; la normalisation FEVG n’annule pas le risque de grossesse ultérieure. S20. |

### I50_pop3.html — examens

| Lignes | Citation courte | Lacune et ajout recommandé |
|---|---|---|
| 4–6 | «sensibilité élevée» ; «ondes Q…» | **P3.** Expliquer que beaucoup de maladies provoquent anomalies ECG sans IC et que normalité réduit probabilité surtout ICFEr, pas ICFEp. Q pathologiques ne sont pas automatiquement infarctus ; bas voltage peut être obésité/BPCO ; BBG et douleur nécessitent évaluation SCA sans attendre. |
| 10–14 | «TAPSE» ; «sans risque» | **P3/P2.** Définir mesures et question qu’elles résolvent (systole VD, remplissage, surcharge, valve). Variabilité FEVG ±5–10 points dépend modalité/qualité ; comparer mêmes méthodes et état de charge. TTE standard non irradiant et de très faible risque ; «sans risque» absolu évitable, notamment si contraste/stress. |
| 17–24 | «Outils…non critères officiels» | **P3.** HFA-PEFF est un consensus professionnel diagnostique publié, pas simple moyen mnémotechnique ; H2FPEF est un modèle probabiliste. Donner population dyspnée inexpliquée ambulatoire, étapes/exclusion mimics, relation prétest et limites FA/obésité. La liste numérique brute mérite schéma d’interprétation et définitions OG/GLS/E/e′. Les erreurs chiffrées sont en tableau prioritaire. S2/S3. |
| 23 | «≥5 : ICFEp confirmée» | **P2/P3.** Valide dans l’algorithme avec conditions préalables, pas confirmation autonome chez tout patient ni exclusion universelle par ≤1. En 2025 ASE insiste sur pressions de remplissage et effort si doute. |
| 28–29 | «T2…inflammation aiguë» | **P3.** T2 détecte œdème et n’est pas spécifique inflammation ; LGE est expansion interstitielle/contraste retenu, pas automatiquement fibrose. Une image sous-épicardique n’identifie pas seule myocardite/sarcoïdose ; relier distribution vasculaire/cicatrice et non ischémique. |
| 30 | «dispositifs…non compatibles» | **P3.** De nombreux dispositifs non conditionnels peuvent être examinés sous protocole expert ; ne pas assimiler incompatibilité historique à exclusion de toute IRM. Ajouter contrôle matériel/programming/monitoring. S10 pour contraste. |
| 33–35 | «épaississement des septa» | **P2/P3.** B-lines sont artefacts liés à diminution du rapport air/eau/augmentation densité, pas une visualisation directe des septa dans toutes les maladies. Le diagnostic combine distribution, ligne pleurale et contexte ; seuil «≥3 dans ≥2 zones bilatérales» est bon repère mais dépend protocole. S21. |
| 39–41 | «normale >20» ; «effort maximal» | **P3.** VO₂ attendue dépend âge/sexe/taille/activité ; privilégier % prédit. RER >1,05 avec seuil anaérobie est critère d’effort adéquat transplant, pas preuve absolue de maximalité ; 1,10 est un autre repère. Expliquer VE/VCO₂ comme ventilation nécessaire pour éliminer CO₂, donc inefficacité/hyperventilation. S22. |
| 40 | «≤12 sous BB / ≤14 sans» | **P3.** Critères d’aide à inscription, intégrés à tableau clinique, âge/sexe, % prédit, obésité (masse maigre), VE/VCO₂ si sous-maximal, et préférence patient. Le texte «fait partie» est correctement prudent mais gagnerait à lier la source 2024. S22. |
| 44–46 | «Na urinaire <50–70» | **P3.** Préciser après dose IV, objectif fenêtre précoce et pourquoi un Na urinaire bas signale faible natriurèse malgré parfois urine abondante. Une concentration isolée dépend aussi eau/heure/prélèvement ; surveiller pression/rein/électrolytes en escaladant. Classe IIb 2026 correcte. S1. |
| 49–51 | «acétazolamide…alcalose» | **P3.** Expliquer inhibition anhydrase→moins réabsorption bicarbonate/Na ; thiazide→NCC distal. Acétazolamide peut causer acidose et hypokaliémie ; ne pas prescrire toute combinaison à tout patient. Distinction essais ADVOR/CLOROTIC : stratégies/doses/populations, pas deux molécules interchangeables. |
| 54–58 | «fer oral inefficace» | **P2/P3.** IRONOUT-HF montre absence d’amélioration de capacité d’effort avec formulation/protocole donné dans ICFEr ; «toute voie orale toujours inefficace» serait trop large. Expliquer hepcidine/inflammation et déficit énergétique musculaire/myocardique même sans anémie. Résumer bénéfice IV sans attribuer un succès statistique identique à AFFIRM-AHF et IRONMAN, actualiser bibliographie avec FAIR-HF2/HEART-FID et ESC 2026. Les classes I/IIa sont bien confirmées en 2026 p. 90. S1/S23. |
| 61–64 | «prévention secondaire» | **P3.** Donner notion >48 h post-IDM pour certaines arythmies et cause réversible, espérance de vie/préférence et risque non arythmique. Repères 2021 restent largement vrais, désormais vérifiés en 2026 ; supprimer «dernières…vérifiées ici» comme métadonnée éditoriale visible ou la remplacer par date/source. S1 pp. 53–54. |
| 67–71 | «bénéfice faible…non BBG» | **P2/P3.** Non-BBG ≥150 conserve indication IIa ; «faible ou absent» sans contexte peut nier indication de la ligne 70. Expliquer activation électrique tardive→contraction mal coordonnée ; pacing VD peut créer dyssynchronie, d’où CRT/BAV. La nouveauté 2026 est modification de classe et population, pas découverte de cette indication déjà classe I 2021. |
| 74–75 | «un seul signal» | **P3.** Décrire signaux de recours précoce et gravité cumulative/trajectoire, sans faire d’un seul signal le diagnostic stade D. La classe I 2026 vise IC avancée **ou risque d’IC avancée** chez candidat motivé sans CI absolue. S1 pp. 69–72. |

### I50_pop4.html — monographies et Pareto

| Lignes | Citation courte | Lacune et ajout recommandé |
|---|---|---|
| 4–9 | «prolonge…peptides natriurétiques» | **P3.** Relier NP→récepteur guanylate cyclase/GMPc→natriurèse, vasodilatation et effets antiprolifératifs ; pourquoi valsartan accompagne l’inhibition de la néprilysine (autres substrats dont angiotensine). Relier effets indésirables à baisse du tonus efférent/aldostérone et bradykinine. Préciser indications exactes pour angioœdème selon médicament ; l’intervalle de 36 h sert à éviter le chevauchement de deux enzymes dégradant la bradykinine. |
| 12–16 | «effet…pas de classe» | **P3.** Nébivolol validé chez les personnes âgées sur un composite, preuve de mortalité totale différente des 3 essais cités ; ne pas transférer à toutes les formes/métoprolol tartrate. Pourquoi faible dose/stabilité : effet inotrope négatif initial ; bénéfice chronique via neurohormones/remodelage. Expliquer BAV/bradycardie et sélectivité dose-dépendante/asthme. |
| 19–23 | «natriurèse…antifibrosant» | **P3.** Effet d’épargne K via le néphron distal ; le bénéfice IC ne vient pas d’une diurèse puissante. Préciser seuils DFG/K et différence stéroïdien/finérénone, conduite en cas d’hyperK et gynécomastie/récepteurs hormonaux. «Prudence DFG <30» est trop peu concret pour un ARM stéroïdien : les essais/algorithmes excluent souvent l’initiation à un DFG ≤30. |
| 26–30 | «rétrocontrôle…cétonique» | Mécanisme correctement marqué hypothétique. **P3.** Expliquer baisse initiale du DFG par pression intraglomérulaire et différence avec lésion aiguë ; mécanisme d’acidocétose et risques même sans hyperglycémie ; mycoses par glycosurie. Seuils d’initiation : ceux des essais/labels, à relier au médicament/à l’indication. «Jusqu’à dialyse» = interrompre à son initiation, pas traiter le dialysé ; formulation à clarifier. S24. |
| 27 | «décès CV ou hospitalisation» | **P3.** Le composite ne prouve pas une baisse significative de chacun de ses éléments dans chaque essai, notamment à EF conservée. Mentionner la dominante réduction des événements IC plutôt que suggérer une mortalité démontrée uniforme. |
| 33–36 | «hyperkaliémie…modéré» | **P3/P2.** Le risque persiste et n’est pas forcément «modéré» pour un patient CKD/hyperK. La distribution cœur-rein repose surtout sur pharmacologie/préclinique ; ne pas en déduire une supériorité clinique universelle. Expliquer pourquoi les doses sont liées au DFG et le monitoring K après ajustement ; statut suisse correctement présenté, à vérifier, pas une autorisation déjà acquise. S17. |
| 39–43 | «augmenter…pas fractionner» | **P2/P3.** Chaque dose doit atteindre le seuil, mais une fois celui-ci atteint, le fractionnement peut limiter la rétention postdiurétique ; ne pas apprendre que fractionner est toujours inutile. Donner deux cas seuil/rebond, adaptation au DFG et doses équivalentes. Expliquer pertes K/Mg, volume/pression, ototoxicité en cas d’exposition IV rapide. |
| 48 | «deux phénotypes seulement» | Classification 2026 correcte. **P3.** Ne pas confondre EF clinique et seuils des essais/traitements. Épidémiologie/mortalité : moyennes de cohortes datées, pas pronostic individuel. «Stade ne régresse pas» mérite d’expliquer l’antécédent persistant malgré rémission et le lien avec la classification. |
| 52 | «iSGLT2 (natriurèse, métabolisme)» | **P3.** Le Pareto laisse croire à un mécanisme dominant prouvé, alors que la monographie dit débattu : ajouter «effets multiples proposés». IEC inhibe la formation d’angiotensine II, ARNI = AT1 + néprilysine, pas un simple blocage identique de l’angiotensine II. |
| 56 | «+2 kg…=rétention» | Doublon de généralisation : écrire alerte de possible rétention/contacter selon le plan. La JVP fiable doit rester un examen intégré. |
| 60 | «Toujours bilan…coronaires, IRM, amylose» | **P2/P3.** Bilan étiologique toujours, ces examens selon indices/prétest ; pas coronarographie + IRM + scintigraphie systématiques pour tout patient. Diagnostic HFpEF = syndrome clinique + critères objectifs, pas FEVG + OG/Ee seuls. S1/S3. |
| 64 | «iSGLT2 débuté à l’hôpital» | **P2/P3.** Ajouter après stabilisation initiale, absence de jeûne/acidocétose, fonction rénale/volume. «Poursuivre BB hors choc» trop absolu : une hypoperfusion organique réfractaire en IC avancée peut justifier une réduction même hors choc (nouveauté 2026 IIa). HBPM seulement si non déjà anticoagulé et balance hémorragique adaptée. S1 pp. 66,75. |
| 64 | «VNI, nitrés» ; «assistance temporaire» | **P3.** VNI réduit le travail respiratoire/la précharge mais risque d’hypotension/VD ; nitrés conditionnés par la PA. Assistance en équipe experte et chez des patients sélectionnés, pas tout choc ; nouvelle classe III dans l’infarctus non sélectionné. |
| 68 | «diurétiques : symptômes seulement» | **P2/P3.** Pas de bénéfice de mortalité randomisé robuste, mais ESC 2026 cite aussi la prévention des hospitalisations par une stratégie de dose dynamique ; ne pas enseigner l’absence de tout bénéfice événementiel. Introduire la différence soulagement/congestion, hospitalisation/mortalité. S1 p. 50. |
| 68 | «TEER…IM secondaire» | **P3.** Citer symptômes persistants, IM sévère, TMF/CRT optimales, anatomie et critères, pas un geste dès le diagnostic d’IM. Rationnel : coaptation et seuils vérifiables p. 87. |
| 76 | «E/e′ >14…=pressions élevées» | **P2/P3.** Plusieurs marqueurs concordants/algorithme et rythme requis ; OG : marqueur chronique confondu par FA/valve. TAPSE unidimensionnel/dépendant de la charge ne résume pas toute la fonction VD. Un cathétérisme élevé ne suffit pas à diagnostiquer l’ICFEp sans syndrome/EF/exclusion valve-péricarde. S3. |
| 80 | «doses cibles» | **P3.** Valeurs des essais = objectif selon tolérance, pas obligation uniforme. «K 5,5–6 : réduire de moitié» doit nommer molécule/urgence/contrôle, pas tout traitement. Dose/contrôle de la finérénone diffèrent. |
| 83–87 | «Digoxinémie 0,5–0,9» | Mécanisme NCX/vagal bien expliqué. **P3/P2.** La surveillance manque la concentration de digitoxine spécifique : 8–18 ng/mL ; une seule cible «digoxinémie» après un popup mixte peut être appliquée à tort. Ajouter fenêtre thérapeutique étroite et pourquoi l’hypoK accroît fixation digoxine/arythmies, le rein réduit la clairance, le délai de 6 h permet l’équilibre tissulaire. S25. |
| 90–94 | «sans effet…tensionnel» | **P3.** Dire pas d’effet direct majeur sur contractilité/PA, pas absence d’hypotension possible. If = pente de dépolarisation diastolique du pacemaker, HCN rétine→phosphènes. Distinguer seuil essai 70 vs autorisation 75 : déjà bien fait. Préciser ajustements FC ≤50/symptômes et 2,5 mg après 75 ans selon label. |
| 97–100 | «voie…déficiente» | **P3.** Explication NO–sGC–GMPc correcte ; préciser déficit NO/oxydation et lien avec l’hypotension. VICTORIA : population avec aggravation récente, composite dominé par hospitalisations ; ne pas laisser penser à une large réduction de mortalité isolée. Attention aux nouveaux essais/stabilité et limite du label. Erreur sur les nitrés dans le tableau prioritaire. |
| 103–105 | «ascendance africaine» | **P3.** A-HeFT portait sur des patients s’auto-identifiant noirs, NYHA III–IV, pas une preuve génétique générale ni une prescription pour toute ascendance. Expliquer remplacement RAAS si impossible et bénéfice additionnel du sous-groupe ; grossesse possible mais diurétiques prudents selon congestion/perfusion utérine. S26/S27. |
| 109 | «chélateurs plutôt qu’arrêt» | **P2/P3.** Pas une règle absolue : hyperK sévère exige traitement urgent/parfois arrêt temporaire ; les chélateurs permettent le maintien RAAS chez certains mais le bénéfice pronostique de cette manœuvre est moins établi. La surveillance créat/K doit être liée aux classes, pas à tout ajustement d’iSGLT2. |
| 109 | «grossesse…permis» | **P3.** β1-sélectif avec monitoring mère/fœtus ; diurétiques pour congestion, éviter déplétion ; «permis» n’est pas absence de risque fœtal. IEC allaitement/grossesse correctement distingués dans pop2. S26. |
| 109 | «Stade B…après infarctus» | **P2/P3.** Pas IEC + BB routiniers après tout IDM quelle que soit l’EF. ESC 2026 stade B : ACEI/ARB EF ≤40 ; BB EF <50 ; éplérénone IDM EF ≤40 + signe IC/diabète. Ajouter EF/contextes sans aplatir le rôle des preuves. S1 p. 8. |
| 109 | «GLS…>15 %→protection» | **P3.** Mesurer baisse relative par rapport au baseline (valeur absolue GLS), même fabricant/charge ; confirmer/évaluer FEVG et biomarqueurs, discussion cardio-oncologie/oncologie plutôt que traitement automatique. |
| 109 | «hyponatrémie…restriction» | **P2/P3.** Réserver la stratégie à l’hypervolémie dilutionnelle ; l’hypovolémie sous diurétiques nécessite une conduite différente. Sévérité, chronologie et symptômes déterminent urgence et lenteur de correction. Tolvaptan à l’hôpital/hors label suisse : déjà précisé dans la monographie. |
| 112 | «BNP…↑ sous ARNI» | **P2/P3.** Hausse initiale possible, pas invariable ; NT-proBNP aussi produit/éliminé par plusieurs voies, pas uniquement un marqueur du rein. Expliquer contrainte/test et éviter BNP ↑ = amélioration. S11/S28. |
| 112 | «génétique…→défibrillateur» | **P2/P3.** Risque variant/gène + LGE/EF/rythme/famille, pas DAI automatique si LMNA/FLNC. Dépistage familial pertinent pour ATTR héréditaire, pas TTR sauvage. |
| 116 | «ischémie d’abord ; hypertension d’abord» | **P3.** Cadre de fréquences/cohortes, pas étiologie de tout patient ; ICFEp souvent multifactorielle. Revascularisation : pas de bénéfice pronostique pour toute ischémie (CABG sélectionné vs PCI). Tafamidis ne traite pas AL. |
| 118–120 | «noradrénaline, inotrope» | **P3.** Expliquer objectifs PA/perfusion et contractilité, monitorer lactate/urine/clinique ; phénotype VD/valve/volume/causes guide le traitement. Distinguer assistance temporaire comme pont et assistance durable. |
| 123–124 ; 109 ; I50_d:65 | «pas de servo-ventilation» | SERVE-HF et maintien de classe III en 2026 pour apnée centrale prédominante confirmés ; **P3** distinguer dispositifs/algorithmes, population historique EF ≤45 et HFrEF 2026 <50, et mentionner apnée obstructive (ASV IIb 2026). Hypothèses correctement étiquetées. |
| 126–128 | «8 à 10 mmol/L/24 h» | **P2/P3.** La limite de correction dépend du risque et de la durée : patients à haut risque (alcool, malnutrition, foie, hypoK) exigent ≤8 et souvent un objectif plus bas ; le seuil ne remplace pas monitoring fréquent ni anticipation de surcorrection sous tolvaptan. Préciser absence de perte Na directe et risque de déshydratation/contre-indication en hypovolémie. |
| 130–133 | «PAPi, POD» ; «von Willebrand» | **P3.** Définir PAPi = (PAPsys−PAPdia)/POD et pourquoi la défaillance VD réduit le remplissage de la pompe ; conditions expertes/pronostic/réhabilitation/anticoagulation. Cisaillement de la pompe→perte des multimères vWF→hémorragies, fréquentes sous anticoagulation. Profils 2–4 : repères corrects ; 1 : pont temporaire fréquent, déjà bien contextualisé. S1 pp. 76–78. |

### I50_d.html — pharmacologie

| Lignes | Citation courte | Lacune et ajout recommandé |
|---|---|---|
| 7–15 | «objectif distinct» | **P3.** Bonne distinction pronostic/soulagement, mais les objectifs se chevauchent (les piliers améliorent aussi les symptômes ; la décongestion prévient les décompensations). Ajouter causalité et temps de l’effet. Le tableau entier peut renvoyer aux monographies, chaque classe ayant un bouton visible. |
| 9 | «IEC ou ARNI…IIb dans ICFEp» | **P3.** Préciser réduction des hospitalisations espérée, pas mortalité démontrée dans l’ICFEp, et inclure ARA II comme option IIb 2026. |
| 11–12 | «TMF quelle que soit FEVG» | Validité ESC 2026 confirmée ; **P3** distinguer ARM stéroïdien/non stéroïdien et fonctions rénales/potassium. Initiation iSGLT2 hospitalière après stabilisation. |
| 14–15 | «Sous-groupes» ; «Sémaglutide, tirzépatide» | **P3.** Liste TMA sans explication dans l’onglet : créer liens vers popups disponibles/monographies manquantes fer/incrétines et préciser critères. Nouveau repère 2026 incrétines = HF symptomatique FEVG ≥45, IMC ≥30, avec ou sans diabète ; «ICFEp avec obésité» est trop étroit pour EF 45–49. |
| 19–20 | «tachycarde : BB précocement» | **P1/P3.** Tachycardie de choc/congestion non stabilisée : pas une indication d’introduire BB ; rechercher compensation/FA/causes traitables et mentionner stabilité/proximité de l’euvolémie, déjà dans popup BB. Chaque ordre proposé doit avoir les conditions K/DFG/PA. |
| 21–41 | «dose initiale…dose cible» | Doses ESC 2026 vérifiées, y compris ramipril BID, spiro 50, digitoxine 0,07→0,1 ; **P3** préciser doses des essais adaptées à tolérance/indication et concentrations des digitaliques, pas des protocoles génériques. Finérénone en ICFEr : voir le tableau prioritaire. |
| 42 | «36 heures…angiœdème» | Explication bonne ; **P3** donner bradykinine/simultanéité enzymatique et également l’intervalle au passage ARNI→IEC selon RCP. |
| 46–47 | «finérénone…FEVG ≥40» | **P3.** Faire le lien avec la recommandation ICFEp et les populations 40–49 nouvellement ICFEr. Incrétines : satiété/poids, effets inflammatoires proposés, résultats des essais. Chercher ATTR selon drapeaux rouges/profil, pas à tout prix ; valvulopathie/AL : diagnostics différentiels. |
| 52–59 | «hausse créat» ; «hypotension» | Voir les résultats prioritaires ; **P3** expliquer pourquoi IEC/ARNI/iSGLT2 modifient l’hémodynamique glomérulaire, distinguer effet attendu et lésion avec clinique. Si K >6 : suspendre autres apports/épargnants K/RAS selon contexte, ECG urgence/recontrôles ; ne pas suspendre uniquement l’ARM par automatisme. |
| 55 | «Ne modifier TMF» | **P2/P3.** Formule acceptable dans une hypotension légère, stable, asymptomatique, pas autorisation pour une PA extrêmement basse/progressive ; rechercher hypoperfusion et causes, plutôt qu’une consigne absolue. |
| 57 | «bradycardie symptomatique…réduire» | **P3.** Ajouter ECG/type de bloc/signes de gravité, vérifier autres médicaments et contexte de l’indication ; une fréquence <50 isolée ne crée pas le même risque qu’un nœud pathologique/BAV. |
| 58 | «suspendre…chirurgie» | **P3.** Dire arrêt préopératoire 3 j pour ces molécules, reprise quand stable/alimentation et hydratation rétablies/absence de cétose ; comment reconnaître l’acidocétose euglycémique (nausées, douleur abdominale, tachypnée) malgré glucose modeste. |
| 64–65 | «à éviter…» | **P3.** Plusieurs affirmations sans pourquoi : AINS ↓prostaglandines rénales/rétention Na + IRA ; glitazones : rétention ; classe I : inotropie négative/proarythmie en maladie structurelle ; moxonidine : excès d’inhibition neurohormonale/données de l’essai ; saxagliptine : signal d’hospitalisation et non contre-indication de tous les DPP4 ; triple RAAS : hyperK/IRA ; supplémentation K : risque d’hyperK mais une hypoK documentée peut requérir une correction monitorée. Dronédarone : corriger ci-dessus. |

## Sources médicales primaires et accès

Les sources fournissent les repères de vérification ; les propositions P3 sont des choix pédagogiques issus de cette lecture. Les références de recherche ne doivent pas être citées par le parent sans nouvelle ouverture/recherche, conformément aux règles de citation. Les URLs sont données pour cette réouverture.

| ID | Source primaire | URL et accès dans cet audit |
|---|---|---|
| S1 | ESC HF 2026, officiel, DOI 10.1093/eurheartj/ehag100 | Page officielle ouverte : https://www.escardio.org/guidelines/clinical-practice-guidelines/all-esc-practice-guidelines/heart-failure/ (turn300view0). **Slides officielles intégralement accessibles**, 105 p. : https://dam-assets.escardio.org/download/b2e587389baa11f185de06bdfb3e4be9 (turn302view1 ; recherches turn317view0/1 ; capture p. 71 turn319view1). OUP complet échoue : taille >4 MiB ; ne pas dire que l’article entier a été lu. |
| S2 | Consensus HFA-PEFF 2019, Pieske et al., DOI 10.1093/eurheartj/ehz641 | https://academic.oup.com/eurheartj/article/40/40/3297/5557740 (turn305search6), texte indexé précis ; ouverture complète échoue (turn308view0). Variante EJHF échoue par redirection (turn309view0). |
| S2b | Validation/étude primaire HFA-PEFF | Étude «Prognostic significance…» https://pmc.ncbi.nlm.nih.gov/articles/PMC8120389/ et https://pubmed.ncbi.nlm.nih.gov/33760383/ (turn305search24/33), seuils indexés ≥75/FA 375. Étude originale diagnostique JAMA : https://jamanetwork.com/journals/jamacardiology/fullarticle/2793877 (turn305search19). |
| S3 | ASE 2025 fonction diastolique, DOI 10.1016/j.echo.2025.03.011 | **PDF complet ouvert**, 33 p. : https://www.asecho.org/wp-content/uploads/2025/07/Left-Ventricular-Diastolic-Function.pdf (turn308view1, turn309view1/2). Référence désormais plus récente qu’ASE 2016 pour algorithmes hors score HFA-PEFF. |
| S4 | Consensus SCAI SHOCK 2022, DOI 10.1016/j.jscai.2021.100008 | **PDF primaire complet ouvert**, 11 p. : https://www.ishlt.org/docs/default-source/standards-guidelines/2022_endorsement_scai_shockconsensusupdate.pdf?sfvrsn=3319fed_1 (turn328view0). Copie PMC : reCAPTCHA. |
| S5 | Expériences longueur/activation, titine | https://pubmed.ncbi.nlm.nih.gov/30523116/ ; https://pubmed.ncbi.nlm.nih.gov/31314138/ ; https://pubmed.ncbi.nlm.nih.gov/12963792/ (turn311search2/4/6). Notices et abstracts primaires indexés, pas textes expérimentaux intégraux. |
| S6 | Hémodynamique ICFEp, élastance | https://pubmed.ncbi.nlm.nih.gov/12578874/ (Kawaguchi 2003, turn313search18) ; https://pubmed.ncbi.nlm.nih.gov/17404159/ (cohorte Olmsted, turn313search16) ; https://pubmed.ncbi.nlm.nih.gov/19628115/ (Borlaug 2009, turn313search26). Abstracts primaires indexés. |
| S7 | NT-proBNP/épanchement/tamponnade, étude originale 2009 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2686974/ (turn311search29), texte indexé : valeurs augmentées associées à la tamponnade. À ouvrir avant citation finale. |
| S8 | Cardinale 2015, cohorte anthracyclines, DOI 10.1161/CIRCULATIONAHA.114.013777 | https://pubmed.ncbi.nlm.nih.gov/25948538/ (turn317search0), résumé primaire indexé ; récupérations partielle et complète mesurées. |
| S9 | Récupération après ablation ESV, étude originale | https://pubmed.ncbi.nlm.nih.gov/23099051/ (turn330search8), abstract indexé. |
| S10 | Consensus ACR/NKF gadolinium 2021, DOI 10.1148/radiol.2020202903 | https://pubs.rsna.org/doi/10.1148/radiol.2020202903 (turn321search21/26) ; https://pubmed.ncbi.nlm.nih.gov/33170103/ (turn321search17). Copie PMC : reCAPTCHA à l’ouverture ; **résumé/indexation primaire**, pas article entier lu. Tableau des groupes dans ACR manual : https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Contrast-Manual (turn321search29/36). |
| S11 | Myhre 2019 PARADIGM-HF BNP sous ARNI, PMID 30846338 | https://pubmed.ncbi.nlm.nih.gov/30846338/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC7955687/ ; DOI : https://www.jacc.org/doi/10.1016/j.jacc.2019.01.018 (turn330search0/13/22). Notice/texte indexé ; le parent signale avoir vérifié. |
| S12 | PRESERVE-HR 2021, essai randomisé de retrait BB ICFEp + incompétence chronotrope | https://pubmed.ncbi.nlm.nih.gov/34794685/ ; https://www.jacc.org/doi/10.1016/j.jacc.2021.08.073 (turn313search0/17). Résumé primaire indexé ; effets à court terme/population sélectionnée. |
| S13 | Expériences de phosphorylation de la titine humaine | https://pubmed.ncbi.nlm.nih.gov/16897574/ ; https://pubmed.ncbi.nlm.nih.gov/19023132/ (turn313search8/4). Résumés primaires indexés. |
| S14 | ESC 2021, §13.4, p. 71 — créatinine et DFG | PDF officiel intégral ouvert par le parent : https://www.heartfailurematters.org/wp-content/uploads/2022/05/ESC-Heart-Failure-Guidelines-2021.pdf. Le passage associe une hausse de créatinine <50 % **ET** une valeur restant <266 µmol/L, **OU** une baisse du DFG <10 % **ET** un DFG restant >25 mL/min/1,73 m². Les deux repères sont alternatifs ; ne pas réunir toutes les conditions en une conjonction globale. L’évaluation clinique reste nécessaire. L’article OUP avait auparavant été vérifié par indexation : https://academic.oup.com/eurheartj/article/42/36/3599/6358045. |
| S15 | Bayer vériciguat RCP fabricant et information suisse | https://www.medicines.org.uk/emc/product/12774/smpc (agent drug_verification, turn320view0 L337–338), **RCP complet ouvert**. Information suisse PDE5/grossesse : https://compendium.ch/fr/product/1481946-verquvo-cpr-pell-2-5-mg (turn320search14) ; résumé également ouvert en allemand : https://compendium.ch/de/product/1481946-verquvo-filmtabl-2-5-mg (turn314view0 L95). |
| S16 | Dronédarone information professionnelle suisse + fabricant | https://compendium.ch/fr/product/1134151-multaq-cpr-pell-400-mg (agent drug_verification, turn316view0 L95) ; https://www.medicines.org.uk/emc/product/497/smpc (turn316view1 L237/289). **Textes complets ouverts par l’agent**. |
| S17 | FINEARTS-HF 2024, DOI 10.1056/NEJMoa2407107 | https://www.nejm.org/doi/full/10.1056/NEJMoa2407107 (agent drug_verification, turn325search0) ; https://pubmed.ncbi.nlm.nih.gov/39225278/ (turn325search6). Résumé primaire indexé vérifié : patients avec FEVG ≥40 %, dose maximale 20 ou 40 mg/j. Appuyer par S1 pp. 49–50 pour la place des ARM ; vérifier le label avant publication. Aucun chiffre de risque nouveau inféré ici. |
| S18 | Thibodeau 2014 bendopnea, DOI 10.1016/j.jchf.2013.07.009 | https://pubmed.ncbi.nlm.nih.gov/24622115/ ; https://www.jacc.org/doi/10.1016/j.jchf.2013.07.009 (turn305search2/22). Résumé/article indexé primaire ; pression intrathoracique proposée, débit n’augmente pas. |
| S19 | ESC 2025 myocardite/péricardite, CHAMPIT | https://www.escardio.org/static-file/Escardio/Guidelines/Products/Slide%20sets/2025/2025%20official%20slides_MyoPeri.pdf (turn317search36) ; slide officielle Fig.10 indexée : CHAMPIT. |
| S20 | Hilfiker-Kleiner 2007 prolactine PPCM, DOI 10.1016/j.cell.2006.12.036 | https://pubmed.ncbi.nlm.nih.gov/17289576/ (turn317search1), résumé primaire indexé. |
| S21 | Consensus EACVI 2023 écho pulmonaire, DOI 10.1093/ehjci/jead169 | **Texte primaire complet ouvert** : https://pmc.ncbi.nlm.nih.gov/articles/PMC11032195/ (turn324view0) ; PMID : https://pubmed.ncbi.nlm.nih.gov/37450604/ . |
| S22 | ISHLT 2024 évaluation du candidat à la transplantation, DOI 10.1016/j.healun.2024.05.010 | PDF officiel indexé : https://www.ishlt.org/docs/default-source/standards-guidelines/2024_guideline_careofhtxcandidates.pdf?sfvrsn=b475b421_2 (turn330search36). Page de la société : https://www.ishlt.org/education-and-publications/standards-guidelines-detail/ishlt-guidelines-for-the-evaluation-and-care-of-cardiac-transplant-candidates (turn330search2). Remplace les versions 2006/2016. |
| S23 | FAIR-HF2 essai randomisé 2025, DOI 10.1001/jama.2025.3833 | https://pubmed.ncbi.nlm.nih.gov/40159390/ ; https://jamanetwork.com/journals/jama/fullarticle/2832132 (turn321search3/27). DOI confirmé dans la notice PubMed ouverte (agent drug_verification, turn336view0 L179–182) ; abstract primaire indexé. Ajouter en bibliographie d’actualisation, sans annuler la recommandation 2026 I/IIa. |
| S24 | KDIGO CKD 2024/SGLT2 et RCP empagliflozine | https://kdigo.org/guidelines/ckd-evaluation-and-management/ ; https://doi.org/10.1016/j.kint.2022.06.013 ; https://www.ema.europa.eu/en/documents/rmp-summary/jardiance-epar-risk-management-plan-summary_en.pdf (agent drug_verification, turn320search4/11/36). Source primaire indexée pour continuation à DFG bas et interruption lors de suppléance. |
| S25 | DIGIT-HF protocole, concentration de digitoxine | https://pmc.ncbi.nlm.nih.gov/articles/PMC6607489/ (agent drug_verification, turn325search3), source primaire indexée : cible 8–18 ng/mL ; dose ESC 2026 correcte. |
| S26 | ESC grossesse 2025, §12.6 | https://academic.oup.com/eurheartj/article/46/43/4462/8234487 (agent drug_verification, turn322search0), texte primaire indexé : hydralazine + nitrés et précaution avec les diurétiques ; S1 p. 16 confirme la liste des médicaments pour la grossesse. |
| S27 | A-HeFT, essai randomisé 2004, DOI 10.1056/NEJMoa042934 | https://pubmed.ncbi.nlm.nih.gov/15533851/ (turn338search1), abstract primaire indexé ; https://www.nejm.org/doi/full/10.1056/nejmoa042934 (turn338search11), article indexé : auto-identification Black (définie comme African descent), NYHA III–IV. |
| S28 | Clairance du NT-proBNP, études originales humaines | https://pubmed.ncbi.nlm.nih.gov/19605456/ (turn338search7) ; https://pubmed.ncbi.nlm.nih.gov/19264247/ (turn338search3). Résumés primaires indexés : clairance dans plusieurs tissus, pas uniquement rénale. |

## Éléments vérifiés qu’il ne faut pas transformer en fausses erreurs

- ESC 2026 existe et est publié le 28 août 2026 ; nouvelle nomenclature FEVG <50/≥50, suppression HFmrEF, TMF/TMA, titration 1–2 semaines, ARM quelle que soit la FEVG classe I, SGLT2 hospitalier classe I après stabilisation, glycosides IIa FEVG ≤40, vériciguat IIb FEVG <45, CRT plutôt que VD pour BAV de haut degré IIa et LVAD classe I sont confirmés par les slides officielles.
- Doses ramipril 1,25–2,5 mg BID→5 mg BID, spironolactone 12,5–25→50, digitoxine 0,07→0,1 conformes au tableau ESC 2026. L’objet de l’audit n’est pas de remettre aux doses 2021.
- Finérénone FEVG ≥40 dans FINEARTS, différence du seuil ivabradine 70 essai/recommandation vs 75 autorisation, hydralazine + nitrés possibles en grossesse, arrêt SGLT2 avant chirurgie, intervalle IEC/ARNI 36 h essentiellement corrects ; améliorer contexte/rationnels.
- SERVE-HF n’est pas une contre-indication obsolète pure : ESC 2026 maintient classe III pour HFrEF et apnée centrale prédominante, tout en permettant ASV IIb si obstructive prédominante. Ne pas interpréter ADVENT-HF comme levée automatique du repère enseigné.
- Les popups ont souvent une vraie explication (Mécanisme, Pourquoi) ; le problème pédagogique principal est la réapparition d’absolus/raccourcis dans les Pareto et tableaux, et les effets/CI listés sans chaîne causale, pas une absence générale de mécanismes.
