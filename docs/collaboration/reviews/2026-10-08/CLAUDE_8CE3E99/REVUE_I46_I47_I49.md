# Contrelecture ciblée — Claude 8ce3e99 — I46, I47 et I49

Tête reçue et vérifiée : `8ce3e99a18b96f6e6774d3d00bc709655e7ccb84`. Les **28 sources proposées ont été lues intégralement**, templates compris. La vérification externe est ciblée : cette revue ne certifie ni toutes les assertions, ni la complétude CIM-11 du fragment, ni le fonctionnement de la plateforme après injection. Les nouvelles explications sont examinées avec leur contexte ; les erreurs héritées restent distinguées des ajouts de cette remise.

| Cours | Sources lues | Copies corrigées | Remplacements annotés | Mots lus, templates inclus |
| --- | ---: | ---: | ---: | ---: |
| I46 — Arrêt cardiaque | 9 | 8 | 28 | 30 782 |
| I47 — Tachycardies paroxystiques supraventriculaires et ventriculaires | 10 | 10 | 48 | 41 199 |
| I49 — Extrasystoles et autres arythmies | 9 | 8 | 49 | 35 420 |

Total : **26 copies corrigées**, 125 remplacements, 107 401 mots lus.

Les corrections sont préparées en copies séparées. Aucun original, HTML canonique, glossaire ou runtime du dépôt n’a été modifié par cette contrelecture. Les décisions médicales rectifiées sont répercutées dans les supports répétés concernés, notamment tableaux, fenêtres, Pareto et quiz. Le parent doit conserver ses statuts de révision et réconcilier les éventuelles améliorations de prose postérieures.

## Livrables contrôlés

- Copies : `/workspace/scratch/6eaecafb4b19/latest_claude_8ce/adapted/chapters/I46`, `I47`, `I49`.
- Journal consolidé SHA256 et remplacements littéraux : `/workspace/scratch/6eaecafb4b19/latest_claude_8ce/reviews/REVUE_I46_I47_I49_manifest.json`.
- SHA256 du journal consolidé : `628d6f817343a18984d8e9c5e2eea9911e7e162a181e7dc31742b4c526916d64`.
- Les trois journaux détaillés identifient les sources primaires, les changements nécessaires et les réserves ouvertes. Les SHA256 des originaux et des copies ont été revérifiés avant gel.

La fusion appartient au parent : les copies ne doivent pas écraser une révision canonique postérieure. Identifiants, contrôles interactifs, SVG, scripts et valeurs des réponses correctes sont conservés. Les rares textes de quiz corrigés sont annotés dans le journal. Les tests navigateur et la compilation ne sont pas revendiqués dans cette revue.

## Contrelecture — I46 — Arrêt cardiaque

La lecture des neuf HTML proposés est terminée. Vingt-huit remplacements indispensables sont préparés dans huit copies séparées ; aucun original, fichier canonique ou glossaire n’a été modifié. La réponse correcte des quatre quiz, les identifiants, les boutons, les scripts et les SVG sont conservés.

### Portée vérifiée

Les 30 782 mots extraits incluent les contenus des templates : texte principal, examens, sciences fondamentales, pharmacologie, cinq lots de fenêtres, tableaux, réponses de quiz, Pareto et textes de figures. Le comptage décrit une couverture de lecture, **pas une validation de chaque assertion**. La vérification externe porte sur les décisions signalées dans le journal ; une matrice exhaustive assertion → mécanisme → source primaire → interaction reste à réaliser.

### Corrections proposées

- Distinguer TV avec pouls stable, TV monomorphe instable et TV polymorphe soutenue ; garder le choc prioritaire devant une torsade soutenue ou sans pouls.
- Retirer le délai individuel certain de cinq minutes d’irréversibilité cérébrale dans le cours, la fenêtre et le Pareto.
- Distinguer utilité de l’examen neurologique initial et impossibilité d’une conclusion défavorable sur un signe précoce isolé.
- Rétablir la restriction ERC de la double défibrillation au cadre de la recherche et rendre la décompression dépendante d’une suspicion clinique de pneumothorax sous tension.
- Corriger le raisonnement du quiz neurologique : examens non décrits ≠ examens normaux ; NSE 38 µg/L sous le seuil défavorable ≠ NSE normale. La réponse B reste correcte.
- Ne pas inférer une règle de réchauffement d’un essai de refroidissement ; ne pas présenter l’absence de différence statistique comme une preuve d’équivalence.
- Préciser la discussion d’une dialyse pendant un arrêt hyperkaliémique réfractaire ; corriger le compartiment anatomique du cœur et le contexte du seuil d’hyperoxémie de TTM2.
- Distinguer compensation ventilatoire et traitement de l’acidose métabolique dans la toxicité des anesthésiques locaux ; distinguer transfert intracellulaire et élimination rénale, digestive ou par dialyse du potassium.
- Préserver le statut de révision du canonique, corriger une référence bibliographique et ne pas banaliser les complications des fractures costales.

### Réserves ouvertes

Douze réserves documentées figurent dans `I46_journal.json`, avec leur passage et le travail requis. Elles concernent notamment les règles de codage, certaines hiérarchies et données épidémiologiques, la suspension d’un bolus d’adrénaline sur une hausse isolée de capnographie, le délai observationnel de répétition de l’ECG, la distinction trou osmolal/osmolalité, le mécanisme des ondes T hyperkaliémiques, les textes suisses et les liens directs vers les sources.

Les nouveautés ERC 2025 suivantes ont été confrontées au texte primaire et ne sont pas des erreurs à annuler : dose unique d’adrénaline sous 30 °C en l’absence d’ECPR imminente ; choc en cas de doute FV fine/asystolie ; groupe de trois chocs sous monitorage compté comme le premier choc de l’algorithme médicamenteux ; repère d’asystolie persistante de 20 minutes dans une décision contextualisée, y compris mention des groupes d’âge dans le chapitre Éthique. Le modèle de phases de la FV ne doit pas réintroduire une période imposée de RCP avant le premier choc : la proposition le distingue déjà correctement.

### Sources consultées

- [ERC 2025 — Réanimation avancée adulte](https://www.erc.edu/media/vedoa2ga/gl2025-05-als-e.pdf), en particulier recommandations cliniques, défibrillation, monitorage et arrêt sous surveillance.
- [ERC-ESICM 2025 — Soins post-réanimation](https://www.erc.edu/media/atqopqm4/gl2025-07-post-resus-e.pdf) et [résumé officiel RCUK](https://www.resus.org.uk/professional-library/2025-resuscitation-guidelines/post-resuscitation-care-guidelines).
- [ERC 2025 — Circonstances particulières](https://www.erc.edu/media/wwufbysp/gl2025-06-spec-circ-e.pdf).
- [AHA 2025 — Réanimation avancée adulte, section 16](https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-advanced-life-support), pour la TV polymorphe soutenue.
- [AHA 2025 — Circonstances particulières, toxicité des anesthésiques locaux](https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-and-pediatric-special-circumstances-of-resuscitation).
- [TTM2 — Essai primaire](https://doi.org/10.1056/NEJMoa2100591).
- [ERC 2025 — Éthique](https://www.sciencedirect.com/science/article/pii/S0300957225002461).
- [Paradis 1990 — Étude de perfusion coronaire](https://jamanetwork.com/data/journals/JAMA/9235/jama_263_8_029.pdf) : la fenêtre qui distingue seuil observé et condition suffisante est cohérente avec l’étude.
- [OFSP — Consentement au don](https://www.bag.admin.ch/fr/don-dorganes-principe-du-consentement-explicite-ou-presume), pour la réserve sur le droit actuellement applicable.

### Contrôles effectués

Chaque remplacement est unique et consigné littéralement avec SHA256 avant/après. Les attributs de contrôle (`id`, `data-k`, `data-pop`, `data-p`, `data-ok`, `aria-controls`), les scripts et les SVG sont identiques avant/après. Aucun test navigateur ou compilation globale n’a été exécuté par cet agent : ils doivent suivre l’arbitrage et l’injection du parent.

Aucune addition au glossaire n’est imposée. Une future fenêtre sur le **trou osmolal** serait utile, avec mécanisme, phase de l’intoxication, limites et source EXTRIP, une fois le tableau correspondant corrigé.

## Contrelecture — I47 — Tachycardies paroxystiques supraventriculaires et ventriculaires

Les dix HTML proposés ont été lus intégralement, y compris les six lots de fenêtres, les tableaux, les réponses des cinq cas, les Pareto et les textes des figures. Les 41 199 mots extraits décrivent la couverture de lecture. Ils ne constituent pas une certification médicale de chaque assertion. La vérification externe est ciblée sur les décisions et chaînes causales ci-dessous.

Quatorze groupes de corrections, soit 48 remplacements dans dix copies, sont consignés littéralement dans `I47_corrections.json`. Aucun original ni fichier canonique n’a été modifié. Les anciennes notes de validation ne sont pas validées par cette revue ; le parent doit conserver les statuts ouverts au moment de sa fusion.

### Corrections établies

| Groupe | Point corrigé | Supports concernés |
| --- | --- | --- |
| I47-01 | TV soutenue : au moins 30 secondes ou intervention nécessaire à son interruption. | a, pop6 |
| I47-02 | Monomorphe décrit une morphologie stable ; ce n’est pas une preuve de réentrée sur cicatrice. | a, pop6 |
| I47-03 | Limiter la dépendance nodale de la TRAV antidromique à la forme classique ; reconnaître les deux voies accessoires. Un arrêt sous adénosine ne prouve pas toujours un circuit nodal, et un QRS fin n’exclut pas toutes les TV. | a, pop1, pop3, pop6 |
| I47-04 | Retirer « sans danger » du traitement supposé d’une TV et préciser les exceptions de l’amiodarone intraveineuse. | b |
| I47-05 | Distinguer tachyarythmie responsable d’instabilité, tachycardie sinusale compensatrice et TV polymorphe soutenue. Cette dernière nécessite un choc non synchronisé. Ne pas administrer automatiquement l’amiodarone après tout échec de choc. | b, pop2, pop4, pop6 |
| I47-06 | Réserver l’isoprénaline aux torsades récidivantes du QT long acquis dépendantes des pauses, après correction des facteurs favorisants, sans ischémie. Rappeler le choc immédiat des torsades soutenues, même avec pouls. | a, b, c, d, pop1, pop4, pop6 |
| I47-07 | Un QRS identique à un ancien tracé est un argument pour une aberration, pas une preuve suffisante pour donner le traitement d’une TSV. | b |
| I47-08 | Après RACS, distinguer coronarographie immédiate prioritaire en cas de ST net ou forte suspicion d’occlusion et examen différable chez un patient stable sans ces critères. | b |
| I47-09 | Corriger IIb en IIa pour la classe Ic au long cours dans la tachycardie atriale focale sans cardiopathie ischémique ou structurelle ; garder la distinction avec la TRAV. | d, pop6 |
| I47-10 | L’élargissement diffus du QRS sous hyperkaliémie peut imiter une TV ; il n’exclut pas la survenue d’une véritable arythmie ventriculaire. | pop5, pop6 |
| I47-11 | Corriger les déficits en magnésium et potassium en parallèle ; la fuite rénale rend la correction du potassium difficile tant que le magnésium reste bas. | pop5 |
| I47-12 | Grossesse : amiodarone à éviter, avec exception spécialisée pour une arythmie réfractaire ou menaçant la vie, non contrôlable autrement. | pop4, pop6 |
| I47-13 | La contre-indication aiguë des bêtabloquants intraveineux en insuffisance cardiaque décompensée n’impose pas l’arrêt automatique d’un traitement oral déjà prescrit. | pop6 |
| I47-14 | Limiter l’association bêtabloquant–amiodarone de l’orage au contexte de cardiopathie structurelle ; préciser TV monomorphe bien tolérée et arrêt choquable dans les indications de l’amiodarone. | b, d, pop4, pop6 |

La comparaison avec la base exacte distingue les erreurs héritées des nouvelles formulations. Le journal indique cette origine pour chaque remplacement : cette livraison n’est pas présentée comme la cause de toutes les erreurs corrigées. Deux chaînes nouvelles étaient particulièrement trompeuses : l’exclusion de toute TV par le mécanisme de l’hyperkaliémie et l’extension de la contre-indication des bêtabloquants intraveineux à tout traitement d’une décompensation.

### Réserves ouvertes

- Il n’existe pas ici de matrice complète reliant chaque assertion, son mécanisme, sa source primaire et son point d’accès interactif. Les listes d’indications, fréquences, rendements génétiques, chiffres historiques, risques et doses comportent encore des vérifications distinctes à réaliser.
- Les références des nouvelles fenêtres sont souvent bibliographiques. Leur ajout n’établit pas à lui seul que chaque proposition est soutenue par le passage cité ; plusieurs références physiologiques sont des synthèses ou manuels. L’audit externe n’a pas reproduit la totalité des calculs ni vérifié chaque donnée des essais.
- Les restrictions suisses de conduite, le cadre génétique légal, les conditions de remboursement et les disponibilités/importations de médicaments sont repris avec leurs dates mais n’ont pas été recertifiés ici auprès de leurs autorités primaires.
- La présentation de Brugada affirme encore, dans plusieurs supports, qu’un type 1 induit exige toujours un critère clinique ou familial. Le cadre ESC 2022 comprend aussi une possibilité diagnostique faible dans certains types 1 pharmacologiquement induits isolés, discutée dans le consensus EHRA 2025. Une révision spécialisée de l’ensemble de ces formulations reste à faire ; cela ne change pas l’absence d’indication immédiate de DAI dans le cas asymptomatique proposé.
- La mise à jour des passages grossesse au regard de l’ESC 2025 ne porte ici que sur l’exception de l’amiodarone. La totalité de la stratégie, des posologies et de la surveillance obstétricale n’est pas recertifiée.
- Les mécanismes de Brugada, des torsades et de l’action de la flécaïnide dans la TVPC ne sont pas tous établis chez l’homme. Le texte conserve les hypothèses explicitement qualifiées ; cette revue ne les transforme pas en certitudes.
- La complétude CIM-11 du fragment n’est pas démontrée par la présence de ces dix fichiers I47. Elle demande la matrice de correspondance dédiée du parent, distincte de la contrelecture médicale.

### Sources primaires confrontées

- [ESC 2019 — TSV](https://academic.oup.com/eurheartj/article/41/5/655/5556821), sections 9.2.1, 10.1.1, 11.1.2 et 11.3.10 ; tableau de traitement de la tachycardie atriale focale et figure 9. Le [PDF du même texte signé](https://www.techmed.sk/svt/svt-2019.pdf) a permis de lire la table, dont le rendu web omet certaines cellules.
- [ESC 2022 — Arythmies ventriculaires](https://academic.oup.com/eurheartj/article/43/40/3997/6675633), définitions, traitement aigu et QT long acquis.
- [ERC 2025 — ALS](https://www.erc.edu/media/vedoa2ga/gl2025-05-als-e.pdf), tachyarythmies, synchronisation et énergies ; [AHA 2025 — ALS, section 16](https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-advanced-life-support), TV polymorphe soutenue.
- [ERC–ESICM 2025 — Post-réanimation](https://www.erc.edu/media/atqopqm4/gl2025-07-post-resus-e.pdf), stratégie coronaire ; [ERC 2025 — Circonstances particulières](https://www.erc.edu/media/wwufbysp/gl2025-06-spec-circ-e.pdf), algorithme hyperkaliémie mentionnant expressément la TV.
- [ESC 2025 — Grossesse](https://academic.oup.com/eurheartj/article/46/43/4462/8234487), exception de l’amiodarone.
- [NICE CG187 — Recommandation 1.5.1](https://www.nice.org.uk/guidance/cg187/chapter/Recommendations), traitement bêtabloquant déjà prescrit lors d’une insuffisance cardiaque aiguë.
- [HRS/EHRA 2019 — Ablation des arythmies ventriculaires](https://academic.oup.com/europace/article/21/8/1143/5487880), TV fasciculaire septale haute à QRS fins.
- [EHRA 2024 — Orage rythmique](https://academic.oup.com/europace/article/26/4/euae049/7607771), section 8.2.5.1 : cardiopathie structurelle et sélection du traitement selon l’arythmie, l’étiologie et les contre-indications.

Les explications physiologiques conservées et précisées ont également été confrontées aux textes signés de [Weiss et coll. 2017](https://doi.org/10.1161/CIRCEP.116.004667) et [Huang et Kuo 2007](https://pubmed.ncbi.nlm.nih.gov/17804670/) ; ce sont des synthèses mécanistiques, pas de nouveaux essais thérapeutiques. La réserve Brugada s’appuie sur le [consensus EHRA 2025 de provocation pharmacologique](https://academic.oup.com/europace/article/27/4/euaf067/8100200).

### Contrôles

Chaque remplacement est unique. Les SHA256 sont consignés avant et après pour chaque copie. Identifiants, `data-k`, `data-pop`, titres des fenêtres, réponses `data-ok`, références `aria-controls`, SVG, scripts et questions sont conservés. Les cinq cas ont été relus ; aucune réponse correcte n’a été changée. Aucun ajout de glossaire n’est nécessaire à ces corrections. Compilation et tests dans la plateforme restent à exécuter par le parent après fusion contrôlée.

## Contrelecture — I49 — Extrasystoles et autres arythmies

La lecture des neuf HTML proposés est terminée : 35 420 mots, contenus des templates inclus. Quarante-neuf remplacements sont préparés dans huit copies séparées. Aucun original, fichier canonique ou glossaire n’a été modifié ; `I49_pop4.html` est conservé sans adaptation. Les identifiants, contrôles, scripts, SVG et réponses correctes des cinq quiz restent identiques.

### Portée vérifiée

Tous les textes principaux, fenêtres, tableaux, réponses et explications de quiz, Pareto et textes de figures ont été lus. Les vérifications externes ciblent les décisions de réanimation, les erreurs de définition, les contradictions et quelques chaînes causales. Cette couverture de lecture ne certifie ni chaque assertion ni la complétude des justifications. Une matrice assertion → mécanisme → source primaire → interaction reste nécessaire.

### Corrections proposées

- Distinguer une salve ventriculaire, une TV et une TV non soutenue selon fréquence, durée et terminaison ; présenter la largeur du QRS et la monomorphie comme des caractères descriptifs, sans preuve absolue d’origine.
- Retirer l’exclusion de toute TV soutenue en l’absence de cicatrice apparente, ainsi que le « seulement sur substrat » du résumé R sur T.
- Distinguer cardiomyopathie induite et aggravée par les ESV : le rehaussement tardif n’exclut pas toute amélioration après suppression. L’attente de récupération de FEVG ne doit pas différer une autre indication de défibrillateur.
- Corriger le comptage du quiz sur le déficit de pouls : 76 complexes ventriculaires comprennent ici 38 battements sinusaux et 38 ESV. La réponse B est préservée.
- Harmoniser l’énergie de choc avec les formes d’onde pulsées, le décompte médicamenteux des trois chocs initiaux sous monitorage et le calendrier de la lidocaïne. Le tableau d’adrénaline distingue désormais les rythmes non choquables.
- Retirer l’ancienne conduite de simple réanalyse devant un doute FV fine/asystolie ; préciser les conditions du changement de vecteur et la restriction de la double défibrillation à la recherche.
- Actualiser le contrôle de température post-RACS et préciser la population de COACT. Retirer l’attente d’un seuil fixe de quatre minutes avant la préparation et la réalisation d’une hystérotomie de réanimation.
- Distinguer les programmes d’entraînement adaptés du POTS de la gestion de l’activité et du repos en présence de malaise post-effort ; ne pas inciter à poursuivre malgré une exacerbation retardée. Ne pas déclarer une supériorité universelle à long terme de l’exercice. Ajouter la réserve rénale à l’expansion hydrosodée.
- Distinguer la neuropathie sympathique périphérique partielle et la réponse adrénergique du POTS. Préciser les conditions de prévention secondaire du prolapsus mitral arythmogène.
- Préserver le statut ouvert de révision des justifications, sans réintroduire de note automatique.

### Réserves ouvertes

Dix-sept réserves sont consignées avec passage et travail attendu dans `I49_journal.json`. Elles concernent notamment la portée des données pronostiques, SWISSRECA, le raisonnement sur l’anxiété, les règles probabilistes de localisation ECG, les exceptions de prescription de flécaïnide, l’hétérogénéité du POTS, les SVG conservés, les règles de conduite suisses, le panel biologique systématique, les protocoles d’imagerie, les critères de cardiomyopathie arythmogène, la portée du quiz POTS et les informations professionnelles suisses. Les données de PARAMEDIC2 ne permettent pas de déduire une cause du handicap neurologique ; les références bibliographiques ne constituent pas encore une matrice sourcée de tous les chiffres et mécanismes.

Le repère de trente secondes pour l’ECG connecté exige aussi une formulation contextualisée : l’ESC 2024 le décrit comme convention et recommande une confirmation ECG après dépistage, tout en laissant la durée minimale ambulatoire dépendre du contexte. Aucun changement automatique d’anticoagulation n’est introduit.

L’attribution de la FEVG réduite à moins de 50 % à l’ESC 2026 n’a pas été supprimée : la publication et la nouvelle classification ont été vérifiées sur le site officiel de l’ESC. Il ne faut pas revenir automatiquement à l’ancienne division en trois phénotypes.

### Sources primaires consultées

- [ESC 2022 — Arythmies ventriculaires et prévention de la mort subite](https://academic.oup.com/eurheartj/article/43/40/3997/6675633), définitions et sections 7.1.2.1–7.1.2.2 ; passages pertinents obtenus par recherche du texte primaire, l’ouverture directe ayant échoué.
- [ERC 2025 — Réanimation avancée adulte](https://www.erc.edu/media/vedoa2ga/gl2025-05-als-e.pdf), défibrillation, médicaments, VF fine et réfractaire.
- [ERC-ESICM 2025 — Soins post-réanimation](https://www.erc.edu/media/atqopqm4/gl2025-07-post-resus-e.pdf), cible de température, durée clinique et coronarographie.
- [ERC 2025 — Circonstances particulières](https://www.erc.edu/media/wwufbysp/gl2025-06-spec-circ-e.pdf), arrêt pendant la grossesse et hystérotomie.
- [HRS 2015 — POTS, tachycardie sinusale inappropriée et syncope réflexe](https://pmc.ncbi.nlm.nih.gov/articles/PMC5267948/), mécanismes et traitements ; extraits primaires retrouvés par recherche, l’ouverture PMC étant bloquée par un contrôle navigateur.
- [OMS — État post-COVID, réadaptation](https://www.who.int/teams/health-care-readiness/post-covid-19-condition), gestion du malaise post-effort et entraînement en l’absence de PESE ; [CDC — Activité et intolérance orthostatique dans le ME/CFS](https://www.cdc.gov/me-cfs/hcp/clinical-care/treating-the-most-disruptive-symptoms-first-and-preventing-worsening-of-symptoms.html).
- [EHRA 2022 — Prolapsus mitral arythmogène](https://academic.oup.com/europace/article/24/12/1981/6661340), conditions de prévention secondaire.
- [ESC 2024 — Fibrillation auriculaire](https://academic.oup.com/eurheartj/article/45/36/3314/7738779), pour la réserve sur la durée ECG.
- [ESC — Publication et classification de l’insuffisance cardiaque en 2026](https://www.escardio.org/news/press/press-releases/major-changes-made-to-the-esc-guidelines-on-heart-failure/), source officielle du maintien du seuil de FEVG indiqué.

### Contrôles effectués

Chaque remplacement est unique et journalisé littéralement avec SHA256 avant/après et ligne d’origine. Les attributs de contrôle, `data-ok`, scripts et SVG sont identiques. Aucun test navigateur ou compilation globale n’a été exécuté par cet agent ; ils doivent suivre l’arbitrage et l’injection du parent.

Aucune addition au glossaire n’est imposée. Une fenêtre dédiée au **malaise post-effort** pourrait être utile ultérieurement, en distinguant aggravation retardée, intolérance immédiate, gestion de l’activité et reprise individualisée ; elle doit rester distincte des fenêtres déjà présentes et faire l’objet d’une validation propre.
