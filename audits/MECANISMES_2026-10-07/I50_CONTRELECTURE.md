# I50 — Insuffisance cardiaque : contrelecture des justifications

Date : 7 octobre 2026. Objet : `chapters/I50/I50_justifications.json`.

Les 21 fenêtres ont été relues indépendamment. Les chaînes explicatives relient le constat local à un mécanisme et à sa conséquence clinique. Les identifiants, les cibles et les occurrences ont été conservés. La compilation donne **21 fenêtres et 21 liens valides**.

Cette contrelecture concerne ces fenêtres. Elle ne certifie ni la justification de chaque phrase des fichiers HTML du cours, ni l'exactitude de tous leurs seuils et schémas thérapeutiques, ni la complétude de la classification CIM-11.

## Corrections appliquées

- Les six références vers une recherche DailyMed sont remplacées par les notices précises de **ENTRESTO** et de **LASIX**, toutes deux destinées à l'usage humain. Les pages de recherche ne constituent plus les sources affichées.
- Les deux références ASE initiales pointent désormais vers le PDF officiel de 2025. Le PDF KDIGO 2024 remplace sa page de présentation.
- Les entrées anémie, sodium, potassium, fer, foie, thyroïde, diabète, fibrose, œdèmes, orthopnée et énergie disposent de publications originales pertinentes ; une recommandation de réaliser un examen n'est plus utilisée seule pour justifier sa physiopathologie.
- La natrémie est décrite comme une concentration liée à l'équilibre entre eau et électrolytes échangeables. Elle est distinguée de la quantité totale de sodium retenue.
- Le potassium est relié à la repolarisation, à la pompe sodium-potassium, au calcium intracellulaire et à la conduction. L'absence de signes électriques typiques n'est pas présentée comme rassurante.
- Le rôle de l'hepcidine et de la ferroportine est explicité ; la ferritine est distinguée de la disponibilité du fer. L'activation de cette voie reste une possibilité liée au contexte inflammatoire.
- Le BNP conserve une valeur pronostique sous sacubitril/valsartan. La préférence pour le NT-proBNP lors de l'introduction du traitement est contextualisée ; une hausse de BNP ne doit pas être attribuée automatiquement au médicament.
- L'effet rénal des inhibiteurs du cotransporteur sodium-glucose de type 2 n'est pas réduit à une vasoconstriction afférente universelle. L'essai RED montre l'importance du terrain dans l'interprétation des effets glomérulaires.
- Le paragraphe sur les bêtabloquants limite l'indication aux phénotypes où le bénéfice est établi ; un mécanisme physiologique ne suffit pas à prescrire dans chaque forme d'insuffisance cardiaque.
- Les études humaines observationnelles, les expériences cellulaires et les modèles numériques sont distingués des preuves de bénéfice thérapeutique.

Aucun nouveau seuil, aucune dose et aucune indication thérapeutique chiffrée n'ont été introduits.

## Lecture des 21 entrées

| Entrée | Point contrôlé | Appui et limite conservée |
|---|---|---|
| `i50-j-anemie` | Hémoglobine → transport d'oxygène → compensation circulatoire → travail accru | Weiskopf 1998 : expérience humaine ; Anand 1993 : anémie sévère et rétention hydrosodée. Leur population ne fixe pas une stratégie de correction pour l'insuffisance cardiaque. |
| `i50-j-sodium` | Perfusion artérielle efficace → vasopressine → rétention d'eau → dilution | Étude humaine après charge hydrique ; recommandations européennes d'hyponatrémie. Pertes de sodium et médicaments restent à distinguer. |
| `i50-j-potassium` | Hypokaliémie : repolarisation et calcium ; hyperkaliémie : dépolarisation et conduction | Étude expérimentale Tazmini 2020, conférence KDIGO 2020 et notices exactes. Aucun seuil de traitement ajouté. |
| `i50-j-rein` | Hypoperfusion et congestion veineuse → variation de filtration | Mullens 2009 observe une association de la congestion avec la dégradation rénale. KDIGO justifie l'adaptation et la surveillance ; une créatinine isolée ne désigne pas la cause. |
| `i50-j-fer` | Chaîne respiratoire → ATP ; hepcidine → ferroportine → fer circulant | Hoes 2018 en cardiomyocytes humains ; Nemeth 2004 pour les deux étapes de la voie inflammatoire ; NICE pour ferritine et saturation de transferrine. Un mécanisme cellulaire ne prédit pas seul un bénéfice clinique. |
| `i50-j-thyroide` | Tachycardie et perte de contraction atriale ; résistances vasculaires et relaxation | Études humaines de dysthyroïdie et NICE NG145. Les tests peuvent être perturbés par une maladie aiguë ou des médicaments. |
| `i50-j-diabete` | Atteintes coronaire, rénale et myocardique | Ng 2012 et Diamant 2003 observent des anomalies myocardiques. Le diabète ne doit pas être désigné comme cause unique de toute dysfonction. |
| `i50-j-foie` | Pression droite → veines hépatiques → sinusoïdes ; hypoperfusion associée | Myers 2003 : mesures hémodynamiques et histologie. Une anomalie des tests hépatiques ne prouve pas sa cause cardiaque. |
| `i50-j-troponine` | Lésion myocardique, cinétique et arguments d'ischémie | Cinquième définition universelle, 2026. Lésion et infarctus sont distingués ; pas de nouveau seuil. |
| `i50-j-albuminurie` | Barrière glomérulaire et récupération tubulaire ; correction de la dilution | KDIGO 2024, partie 1.3. La persistance d'une élévation doit être confirmée et le rapport n'est pas une décision thérapeutique autonome. |
| `i50-j-neprilysine` | Inhibition enzymatique → interprétation différente du BNP et du NT-proBNP | ENTRESTO section 12.2 ; analyse Myhre 2019 de PARADIGM-HF. Les deux marqueurs conservent une valeur pronostique. |
| `i50-j-obesite` | Concentrations souvent plus faibles ; dépendance à la production et à l'élimination | Wang 2004 : association humaine ; ASE/ESC pour l'évaluation diagnostique. Le mécanisme complet reste discuté et n'est pas attribué à un récepteur unique. |
| `i50-j-echo-relaxation` | Relaxation et recul élastique → déplacement annulaire précoce | ASE 2025, tableau 4 et section 10. Âge, charge, maladie annulaire et contexte clinique modifient l'interprétation. |
| `i50-j-orthopnee` | Position couchée → volume central et mécanique respiratoire | Études humaines de posture, effort inspiratoire et débit expiratoire. La congestion n'est pas l'unique mécanisme possible. |
| `i50-j-oedemes` | Pression hydrostatique, filtration et capacité de drainage lymphatique | Rossitto 2020 et étude humaine des pressions interstitielles de 1984. L'œdème seul n'est pas spécifique de l'insuffisance cardiaque. |
| `i50-j-fibrose` | Obstacles fibreux → propagation hétérogène → circuit de réentrée possible | Modèles de conduction de 2020 et modèles construits à partir de cicatrices humaines de 2022. Pas de prédiction individuelle ni d'indication de dispositif déduite du mécanisme seul. |
| `i50-j-energie-relaxation` | ATP → détachement des ponts ; pompe SERCA → retrait du calcium | Expériences de libération d'ATP et de transport calcique ; Hoes 2018. Le texte ne réduit pas toute insuffisance cardiaque à un déficit énergétique. |
| `i50-j-diuretique` | Transport tubulaire de sodium → excrétion hydrosodée → décongestion | Notice humaine LASIX. Le soulagement symptomatique ne constitue pas à lui seul une preuve de réduction de mortalité. |
| `i50-j-betabloquant` | Stimulation adrénergique prolongée, ralentissement et remodelage | Essais de carvédilol et recommandations ESC. Titration conditionnée par stabilité clinique et phénotype. |
| `i50-j-rein-traitement` | Tonus glomérulaire, pression de filtration et baisse fonctionnelle possible | KDIGO 2024, ENTRESTO et essai RED. Une hausse de créatinine reste à interpréter avec volume, tension, potassium et médicaments. |
| `i50-j-antiinflammatoire` | Inhibition des prostaglandines → filtration et réponse natriurétique | KDIGO 2024, tableau 31 ; interaction indométacine–furosémide dans la notice LASIX. Le risque dépend du contexte et des associations. |

## Traçabilité des vérifications

Les liens précis, titres et populations sont enregistrés dans chaque entrée JSON. Les PDF officiels ASE 2025, KDIGO 2024 et KDIGO hyperkaliémie 2020 ainsi que les notices ENTRESTO et LASIX ont été consultés. Les résultats et résumés des études originales ont été confrontés aux formulations des fenêtres.

La publication **ESC 2026 sur l'insuffisance cardiaque existe** : publication du 28 août 2026, DOI `10.1093/eurheartj/ehag100`, PMID `42661420`. Le texte intégral de l'éditeur dépasse la limite de récupération de l'outil utilisé. Les fenêtres ne doivent donc pas être considérées comme une vérification intégrale de cette recommandation. NICE NG106 a une mise à jour de septembre 2025 ; certaines pages ont refusé la récupération directe, alors que leur contenu reste indexé. Les sources originales mécanistiques ajoutées évitent de faire dépendre les explications de la seule disponibilité de ces pages.

## Vérification technique et portée

- 21 identifiants uniques et 21 ancrages d'origine conservés.
- JSON valide ; chaque fenêtre contient explication, mécanisme, implication, limites et sources.
- Compilation par `load_course_justifications` : **21 fenêtres / 21 liens** ; les textes cibles sont trouvés dans les ancrages prévus.
- **0 URL de recherche DailyMed** dans la banque finale.
- Aucun fichier HTML canonique du cours modifié par cette contrelecture.
- Les 21 fenêtres sont réparties entre les onglets A, C et D. Elles ne constituent pas un inventaire exhaustif des assertions des quatre onglets.

Une correction ponctuelle demandée à côté de cette contrelecture a aussi été appliquée à **I10 — Hypertension artérielle** : le nom non défini « WNK-SPAK » est remplacé par une explication des enzymes de signalisation intracellulaire. La compilation conserve **14 fenêtres / 14 liens**.
