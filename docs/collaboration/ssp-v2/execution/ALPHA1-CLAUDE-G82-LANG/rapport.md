# Audit linguistique agressif ALPHA77 — G82 (Paraparésie et paraplégie, tétraparésie et tétraplégie)

Mission ALPHA1-CLAUDE-G82-LANG, fragment S08, génération 1. Branche `claude/alpha1/g82-lang-g1`, base `103745baaa38c76f18288758cc7f689e5091ccdb`.

> Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.

## Synthèse

| Indicateur | Valeur |
|---|---|
| Fichiers lus en entier | 7 (empreintes SHA-256 conformes au manifeste) |
| Propositions locales (fond inchangé) | 80 |
| Renvois médicaux (non proposés) | 17 |
| Unicité de chaque `ancien` | 80 sur 80 |
| Abréviations sans clé (`build_medina.audit()`) avant / après | {} / {} |

Répartition par catégorie : syntaxe 22, registre 20, ambiguité 13, cohérence 6, grammaire 6, typographie 5, répétition 3, ponctuation 3, orthographe 2.

Répartition par fichier : G82_b.html 23, G82_a.html 17, G82_d.html 13, G82_c.html 12, G82_pop2.html 11, G82_pop1.html 3, g82.py 1.

## Méthode

Les sept fichiers de la leçon ont été lus intégralement : parties 0 à 13 du premier onglet, examens complémentaires, trois sciences fondamentales, pharmacologie, deux fichiers de fenêtres (dont les fenêtres Pareto) et glossaire. Chaque proposition est locale (`ancien` unique, `nouveau`, `motif`, `fond_inchange: true`). Toute reformulation qui toucherait un fait, un chiffre, un seuil, un critère ou une source a été écartée et consignée en renvoi médical. L’unicité des `ancien`, l’absence de chevauchement, l’équilibre des balises et le résultat `{}` du contrôle des abréviations ont été vérifiés par script sur une application simulée en mémoire.

## Les constats les plus importants

- **Élision omise** (onglet des examens, bilan neuro-urologique) : « La urodynamique invasive » devient « L’urodynamique invasive ».
- **Sujet erroné et accord** : la relative « qui ne répond pas aux antispastiques oraux ou qui les tolère mal » (pharmacologie, baclofène intrathécal) et son pendant dans la fenêtre font tolérer les antispastiques par la spasticité ou par eux-mêmes ; elles sont reconstruites.
- **Renvoi interne erroné** : « (voir la section suivante) » à propos de la spasticité de la moelle, alors que le lien entre siège et tonus se trouve à la section 8.
- **Phrases nominales** dans le corps de texte (urgences 2 et 3 de la section 9), contraires au guide de rédaction : verbes rétablis.
- **Ambiguïté « avant 8 heures »** pour la méthylprednisolone (heure d’horloge) alors que la fenêtre dit « dans les 8 heures ». Proposé dans le tableau, le paramètre clé et le Pareto.

## Propositions locales

### chapters/G82/G82_a.html (17)

| Id | Catégorie | Ancien | Nouveau | Motif |
|---|---|---|---|---|
| P-01 | registre | elles servent à poser la question du cours : | elles servent à poser le problème clinique : | Registre : l’annonce pédagogique expose le problème médical ; elle ne décrit pas le cours lui-même (STYLE_REDACTION, § 3). |
| P-02 | syntaxe | pour un médecin qui n’est pas spécialiste | pour un médecin non spécialiste | Lourdeur : la proposition relative négative se condense en un adjectif. |
| P-03 | ambiguité | Elle exclut aussi la paralysie cérébrale infantile, codée G80. | La CIM-10-GM exclut aussi la paralysie cérébrale infantile, codée G80. | Ambiguïté du pronom : « Elle » peut renvoyer à la paralysie médullaire traumatique aiguë (« celle-ci ») citée juste avant. |
| P-04 | syntaxe | puis G82 pour l’état chronique ou en code supplémentaire. | puis G82 pour l’état chronique, ou comme code supplémentaire. | Zeugme : « pour l’état chronique » et « en code supplémentaire » n’ont pas la même construction ; virgule et « comme » rétablissent le parallélisme. |
| P-05 | syntaxe | et G82 sert ensuite à l’état chronique ou en code supplémentaire. | et G82 sert ensuite à coder l’état chronique ou s’emploie en code supplémentaire. | Construction fautive : « sert à l’état chronique » n’a pas de complément verbal ; le verbe « coder » est rétabli et les deux emplois sont coordonnés. |
| P-06 | cohérence | peut devenir spastique (voir la section suivante) | peut devenir spastique (voir la section 8) | Renvoi interne erroné : la section suivante (section 2) ne traite pas du tonus ; le lien entre siège et tonus est exposé à la section 8 (« le tonus renseigne sur le siège »). |
| P-07 | registre | L’examen coche trois ensembles de données. | L’examen recueille trois ensembles de données. | Registre : « cocher » relève du formulaire, non de l’examen clinique. |
| P-08 | syntaxe | surtout les personnes âgées et les lésions moins sévères | surtout les personnes âgées et celles dont la lésion est moins sévère | Zeugme : les centres ne « voient » pas des lésions mais des patients. |
| P-09 | ambiguité | les causes sont cardiovasculaires (39,8 %) | les causes de décès sont cardiovasculaires (39,8 %) | Précision : le sujet « les causes » doit être qualifié (causes de décès) pour que la phrase soit complète. |
| P-10 | registre | Un chiffre agrège donc des histoires très différentes. | Un chiffre global agrège donc des évolutions très différentes. | Registre : « histoires » est une métaphore, proscrite par le guide de rédaction ; « global » précise la nature du chiffre. |
| P-11 | syntaxe | à raison d’une médiane de 6 heures par semaine | avec une médiane de 6 heures par semaine | « À raison de » exprime une proportion régulière appliquée à une quantité ; il s’accorde mal avec « médiane ». |
| P-12 | cohérence | que l’abandon cause le décès | que la perte de suivi cause le décès | Cohérence terminologique : le texte parle de patients « perdus de vue » ; « abandon » suppose une décision du patient que la source n’établit pas dans le texte. |
| P-13 | registre | elles ne disent pas ce que ferait un patient donné | elles ne prédisent pas l’évolution d’un patient donné | Contresens lexical : une mortalité « ne fait » rien ; la formule est alignée sur la fenêtre associée (« ne prédisent pas l’évolution d’un patient »). |
| P-14 | répétition | s’installe ensuite dans les heures et les jours qui suivent | s’installe dans les heures et les jours qui suivent | Répétition : « ensuite » et « qui suivent » expriment la même succession. |
| P-15 | syntaxe | Le danger principal est le haut appareil urinaire : | Le danger principal concerne le haut appareil urinaire : | Métonymie fautive : le danger n’« est » pas un organe ; il le menace. |
| P-16 | ponctuation | un érythème au-dessus de la lésion, et une pâleur avec peau froide en dessous. | un érythème au-dessus de la lésion, ainsi qu’une pâleur et une peau froide en dessous. | Ponctuation : pas de virgule devant « et » dans une énumération ; parallélisme des groupes nominaux (« avec peau froide » devient « une peau froide »). |
| P-17 | registre | n’est pas qu’un handicap | n’est pas seulement un handicap | Registre : « ne… que » avec « pas » relève de l’oral. |

### chapters/G82/G82_b.html (23)

| Id | Catégorie | Ancien | Nouveau | Motif |
|---|---|---|---|---|
| P-18 | ambiguité | la fonction de la vie quotidienne | le fonctionnement dans la vie quotidienne | Précision : « la fonction de la vie quotidienne » est elliptique et peut se lire comme une fonction d’organe. |
| P-19 | syntaxe | une lésion à ou au-dessus du 6e segment thoracique | une lésion située au 6e segment thoracique ou au-dessus | Construction fautive (« à ou au-dessus du ») ; la formule est alignée sur le reste de la leçon. |
| P-20 | ambiguité | le seul élément isolé qui rassure ou inquiète est celui qui change | le seul élément qui rassure ou inquiète est celui qui change | Contradiction interne : « isolé » s’oppose à l’idée de changement dans le temps qui suit. |
| P-21 | registre | Le diagnostic différentiel utilise d’abord la définition. | Le diagnostic différentiel repose d’abord sur la définition. | Registre : un diagnostic différentiel ne « utilise » pas ; il « repose sur ». |
| P-22 | cohérence | Parmi les lésions des segments les plus bas, trois tableaux se distinguent : | Selon le siège de l’atteinte, trois tableaux se distinguent : | Incohérence avec le tableau : la première ligne décrit la lésion médullaire haute, qui n’est pas une lésion des segments les plus bas. |
| P-23 | grammaire | cône médullaire (distinction, codage)</button> illustre la frontière. | cône médullaire (distinction, codage)</button> illustrent la frontière. | Accord : le sujet (« le syndrome de la queue de cheval et le cône médullaire ») est pluriel. |
| P-24 | registre | leur plein texte n’a pas été lu | leur texte intégral n’a pas été lu | Terminologie : « texte intégral » est l’expression utilisée dans le protocole de lecture des sources. |
| P-25 | ambiguité | 24 heures à dose élevée proposées comme option si l’administration débute avant 8 heures | un schéma de 24 heures à dose élevée proposé comme option si l’administration débute dans les 8 heures | Accord et ambiguïté : le sujet est un schéma (et non « 24 heures proposées ») ; « avant 8 heures » peut se lire comme une heure d’horloge, alors que la fenêtre associée dit « dans les 8 heures ». |
| P-26 | syntaxe | Viser au moins 75–80 mmHg ; ne pas élever activement au-delà de 90–95 mmHg ; pendant 3 à 7 jours ; pas de recommandation sur le vasopresseur | Viser au moins 75–80 mmHg et ne pas élever activement au-delà de 90–95 mmHg, pendant 3 à 7 jours ; pas de recommandation sur le vasopresseur | La durée « pendant 3 à 7 jours » était isolée entre deux points-virgules ; elle est rattachée aux deux bornes, comme dans la fenêtre associée. |
| P-27 | ambiguité | Les bornes de pression ont un rôle | Les bornes de pression ont chacune un rôle | Précision : la phrase suivante distingue les deux bornes. |
| P-28 | syntaxe | Seconde urgence : la <button class="w" data-k="g82-da">dysréflexie autonome</button>, potentiellement vitale. | La <button class="w" data-k="g82-da">dysréflexie autonome</button> constitue la seconde urgence ; elle est potentiellement vitale. | Phrase nominale, proscrite par le guide de rédaction (§ 2) : verbe conjugué rétabli. |
| P-29 | syntaxe | Troisième urgence : le <button class="w" data-k="g82-sevrage">sevrage de baclofène intrathécal</button>, par panne de pompe ou déconnexion du cathéte… | Le <button class="w" data-k="g82-sevrage">sevrage de baclofène intrathécal</button> constitue la troisième urgence ; il résulte d’une panne de pompe … | Phrase nominale, proscrite par le guide de rédaction (§ 2) : verbe conjugué rétabli ; « par panne » devient « d’une panne » (cause). |
| P-30 | ambiguité | des hémorragies cérébrales récidivantes en rapport de cas | des hémorragies cérébrales récidivantes dans un rapport de cas | « En rapport de » est ambigu (« en relation avec ») ; « dans un rapport de cas » désigne la publication. |
| P-31 | ponctuation | une défaillance multiviscérale, et le décès est possible | une défaillance multiviscérale ; le décès est possible | Rupture de construction : la dernière proposition n’appartient pas à l’énumération des signes. |
| P-32 | registre | le Credé et la poussée abdominale | la manœuvre de Credé et la poussée abdominale | Registre : « le Credé » est un raccourci de jargon ; la manœuvre est nommée. |
| P-33 | registre | répond à une hiérarchie de priorités | obéit à une hiérarchie de priorités | Registre : une prise en charge « obéit » à une hiérarchie ; « répondre à » est impropre. |
| P-34 | grammaire | relève d’une décision partagée, avec une instruction approfondie | relèvent d’une décision partagée, avec un enseignement approfondi | Accord : le sujet (« l’auto-sondage intermittent et les traitements de deuxième ligne ») est pluriel ; « instruction » est un anglicisme (instruction = enseignement au patient). |
| P-35 | syntaxe | La raison est que le haut appareil se dégrade | En effet, le haut appareil se dégrade | Lourdeur : « La raison est que » alourdit l’énoncé causal. |
| P-36 | syntaxe | le cours ne les remplace pas | le cours ne peut pas en tenir lieu | Syntaxe : « remplacer » n’a pas ici de sens clair ; « tenir lieu de » exprime la substitution visée. |
| P-37 | répétition | l’étiologie maligne a le pronostic le plus sombre | la cause maligne a le pronostic le plus sombre | Répétition : « étiologie » figure deux fois dans la même phrase. |
| P-38 | registre | Cette section réunit ce qui définit et ce qui chiffre. Les critères viennent de | Les critères et les valeurs chiffrées viennent de | Registre : la phrase décrit la section au lieu de poser son contenu (STYLE_REDACTION, § 3) ; aucun fait n’est retiré. |
| P-39 | cohérence | mortalité standardisée 2,32 (traumatique) et 1,6 fois (non traumatique) | mortalité standardisée 2,32 fois (traumatique) et 1,6 fois (non traumatique) | Parallélisme : « fois » figure pour le second chiffre seulement. |
| P-40 | ambiguité | méthylprednisolone uniquement avant 8 heures et pendant 24 heures | méthylprednisolone uniquement dans les 8 heures et pendant 24 heures | Ambiguïté de « avant 8 heures » (heure d’horloge) ; alignement sur la fenêtre « dans les 8 heures ». |

### chapters/G82/G82_c.html (12)

| Id | Catégorie | Ancien | Nouveau | Motif |
|---|---|---|---|---|
| P-41 | cohérence | À l’inverse, la recommandation préfère une décompression | Par ailleurs, la recommandation préfère une décompression | Connecteur inexact : la phrase ajoute un second élément d’ordre ; elle ne s’oppose pas à la précédente. |
| P-42 | registre | informer le pronostic neurologique | éclairer le pronostic neurologique | Anglicisme : on éclaire un pronostic ; on ne l’« informe » pas. |
| P-43 | répétition | La formulation « lorsque c’est faisable » signale | Cette formulation signale | Répétition : l’expression vient d’être citée à la phrase précédente. |
| P-44 | orthographe | La <button class="w" data-k="g82-urodynamique">urodynamique invasive</button> est obligatoire | L’<button class="w" data-k="g82-urodynamique">urodynamique invasive</button> est obligatoire | Élision omise : « la urodynamique » devient « l’urodynamique ». |
| P-45 | registre | chez des lésés au 6e segment thoracique ou au-dessus, et la pression diastolique | chez des patients dont la lésion se situe au 6e segment thoracique ou au-dessus, et la pression diastolique | Registre : « des lésés » est un substantif de jargon. |
| P-46 | syntaxe | n’atteint pas le seuil de plus de 20 mmHg | ne dépasse pas le seuil de 20 mmHg | Formulation illogique (« atteindre un seuil de plus de ») ; la définition reste « plus de 20 mmHg ». |
| P-47 | syntaxe | 118 − 100 = 18, ce qui est inférieur. | 118 − 100 = 18, ce qui est inférieur à 20. | Complément manquant : « inférieur » appelle un terme de comparaison. |
| P-48 | syntaxe | Un patient paraplégique chronique, lésion complète, spastique, a son segment moteur intact | Un patient paraplégique spastique, avec une lésion chronique complète, a son segment moteur intact | Phrase asyndétique et nominale : apposition remplacée par un complément construit. |
| P-49 | registre | La moelle se découpe en segments | La moelle se divise en segments | Registre : « se découper » relève de la boucherie ; « se diviser » est le verbe de l’anatomie. |
| P-50 | registre | La moelle lésée est un tissu qui continue de souffrir après l’impact. | Après l’impact, le tissu médullaire lésé continue de s’altérer. | Registre : « souffrir » est une personnification (métaphore proscrite) ; « s’altérer » désigne le processus. |
| P-51 | registre | n’est pas qu’une conséquence à supprimer | n’est pas seulement une conséquence à supprimer | Registre : « ne… pas que » relève de l’oral. |
| P-52 | syntaxe | Surveiller la pression artérielle pendant les gestes invasifs : | La pression artérielle se surveille pendant les gestes invasifs : | Infinitif injonctif, proscrit par le guide de rédaction (§ 2) ; forme pronominale déjà employée dans la leçon. |

### chapters/G82/G82_d.html (13)

| Id | Catégorie | Ancien | Nouveau | Motif |
|---|---|---|---|---|
| P-53 | ambiguité | Aucun médicament ne rend la fonction perdue. | Aucun médicament ne restitue la fonction perdue. | Ambiguïté : « rendre perdue » peut se lire comme « faire perdre » ; « restituer » lève le doute. |
| P-54 | ambiguité | avec une limite que le cours documente quand elle a été lue | avec une limite que le cours documente lorsque la source en a été lue | Ambiguïté : « elle » (la limite) ne peut pas être « lue » ; c’est la source qui est lue. |
| P-55 | syntaxe | indique le baclofène aussi dans la spasticité médullaire | indique aussi le baclofène dans la spasticité médullaire | Place de l’adverbe : « aussi » porte sur le verbe, non sur le complément éloigné. |
| P-56 | syntaxe | et 100 à 120 mg par jour sous surveillance hospitalière | et de 100 à 120 mg par jour sous surveillance hospitalière | Parallélisme : « est de 30 à 80 mg, et de 100 à 120 mg ». |
| P-57 | cohérence | l’arrêt est progressif sur environ trois semaines | l’arrêt doit être progressif sur environ trois semaines | Une consigne se formule à l’obligatif ; la fenêtre du quiz le dit déjà (« L’arrêt doit être progressif »). |
| P-58 | grammaire | qui ne répond pas aux antispastiques oraux ou qui les tolère mal | qui ne répond pas aux antispastiques oraux ou pour laquelle ceux-ci sont mal tolérés | Sujet erroné : c’est le patient, non la spasticité, qui tolère mal les antispastiques ; la relative est reconstruite sans nommer d’autre sujet. |
| P-59 | registre | un patient porteur d’une pompe qui présente cette séquence est une urgence | un patient porteur d’une pompe qui présente cette séquence constitue une urgence | Registre : « est une urgence » identifie une personne à une situation. |
| P-60 | ambiguité | le tableau commence par des signes banals | le tableau clinique commence par des signes banals | Ambiguïté : « le tableau » désigne ailleurs dans la leçon un tableau de données. |
| P-61 | registre | Ces contre-indications se déduisent du mécanisme antimuscarinique | Ces contre-indications s’expliquent par le mécanisme antimuscarinique | Registre : une contre-indication de l’information professionnelle est un fait lu ; elle s’explique, elle ne se déduit pas. |
| P-62 | grammaire | se plaint d’une fatigue | se plaint de fatigue | Grammaire : « fatigue » est ici indénombrable. |
| P-63 | grammaire | Quel risque l’information professionnelle décrit-elle ? | Quels risques l’information professionnelle décrit-elle ? | Accord avec les réponses, qui énumèrent plusieurs effets. |
| P-64 | typographie | <button class="w" data-k="g82-lioresal-it">Liorésal intrathécal®</button></td> | <button class="w" data-k="g82-lioresal-it">Liorésal® intrathécal</button></td> | Typographie : le symbole ® suit le nom de marque. |
| P-65 | typographie | <p><button class="w" data-k="g82-lioresal-it">Liorésal intrathécal®</button> est réservé | <p><button class="w" data-k="g82-lioresal-it">Liorésal® intrathécal</button> est réservé | Typographie : le symbole ® suit le nom de marque. |

### chapters/G82/G82_pop1.html (3)

| Id | Catégorie | Ancien | Nouveau | Motif |
|---|---|---|---|---|
| P-66 | syntaxe | surtout les personnes âgées et les lésions moins sévères. | surtout les personnes âgées et celles dont la lésion est moins sévère. | Zeugme : les centres ne « voient » pas des lésions mais des patients. |
| P-67 | registre | ne distinguent pas toujours une vraie lésion médullaire d’une codification large | ne distinguent pas toujours une lésion médullaire avérée d’un codage large | Registre : « vraie » et « codification » sont remplacés par « avérée » et « codage », terme employé dans le reste de la leçon. |
| P-68 | ambiguité | Les deux nombres peuvent différer chez un même patient : l’apprenant note l’un pour la clinique, l’autre pour le codage. | Les deux niveaux peuvent différer chez un même patient : le médecin note l’un pour la clinique, l’autre pour le codage. | Précision : il s’agit de niveaux, non de nombres ; c’est le médecin (et non « l’apprenant ») qui note. |

### chapters/G82/G82_pop2.html (11)

| Id | Catégorie | Ancien | Nouveau | Motif |
|---|---|---|---|---|
| P-69 | syntaxe | est l’aggravation du tissu nerveux qui suit | est l’aggravation de l’atteinte du tissu nerveux qui suit | Syntaxe : un tissu ne s’aggrave pas ; son atteinte, si. |
| P-70 | syntaxe | peuvent soutenir la posture, la circulation et la prévention de la thrombose | peuvent soutenir la posture et la circulation, et contribuer à prévenir la thrombose | Zeugme : « soutenir la prévention » ; formulation alignée sur le texte principal de la leçon. |
| P-71 | registre | La décision est partagée et l’instruction approfondie. | La décision est partagée et l’enseignement approfondi. | Anglicisme : « instruction » signifie ici enseignement au patient. |
| P-72 | syntaxe | Premièrement protéger le haut appareil urinaire, deuxièmement la continence, troisièmement restaurer la fonction, quatrièmement la qualité de vie. | Premièrement protéger le haut appareil urinaire, deuxièmement assurer la continence, troisièmement restaurer la fonction, quatrièmement améliorer la … | Parallélisme : deux objectifs sont des noms, deux sont des infinitifs ; les verbes sont ceux employés dans le texte principal. |
| P-73 | registre | Le Credé et la poussée abdominale créent | La manœuvre de Credé et la poussée abdominale créent | Registre : « le Credé » est un raccourci de jargon. |
| P-74 | grammaire | ne répondant pas aux antispastiques oraux ou mal tolérés par ceux-ci. | ne répondant pas aux antispastiques oraux ou pour laquelle ceux-ci sont mal tolérés. | Accord et sens : « mal tolérés par ceux-ci » fait tolérer les antispastiques par eux-mêmes ; la relative est reconstruite. |
| P-75 | ponctuation | Ensuite 15 mg × 3 = 45 mg | Ensuite, 15 mg × 3 = 45 mg | Ponctuation : virgule après l’adverbe de liaison. |
| P-76 | ambiguité | Méthylprednisolone seulement avant 8 heures | Méthylprednisolone seulement dans les 8 heures | Ambiguïté de « avant 8 heures » (heure d’horloge) ; alignement sur la fenêtre « dans les 8 heures ». |
| P-77 | typographie | <template data-pop="g82-lioresal-it" data-title="Liorésal intrathécal® : information professionnelle suisse"> | <template data-pop="g82-lioresal-it" data-title="Liorésal® intrathécal : information professionnelle suisse"> | Typographie : le symbole ® suit le nom de marque. |
| P-78 | typographie | Liorésal intrathécal®</a>, consultée le 15 octobre 2026. | Liorésal® intrathécal</a>, consultée le 15 octobre 2026. | Typographie : le symbole ® suit le nom de marque. |
| P-79 | typographie | Liorésal intrathécal®, mise à jour d’avril 2024 | Liorésal® intrathécal, mise à jour d’avril 2024 | Typographie : le symbole ® suit le nom de marque. |

### glossary/g82.py (1)

| Id | Catégorie | Ancien | Nouveau | Motif |
|---|---|---|---|---|
| P-80 | orthographe | ac('DAP', [('D','Pression anale'),('A','profonde, en anglais'),('P','Deep Anal Pressure')] | ac('DAP', [('D','Deep (profonde)'),('A','Anal (anale)'),('P','Pressure (pression)')] | Abréviation sans développement lettre à lettre : D, A et P étaient associés à des segments de phrase au lieu des mots Deep, Anal, Pressure. La clé (Pression anale profonde) est inchangée. |

Les extraits complets figurent dans `propositions.json`.

## Renvois médicaux (aucune reformulation proposée)

- **R-01** (G82_a.html) — ancre : « La <button class="w" data-k="g82-zpp">zone de préservation partielle</button> complète la description des lésions où la… ». La formule « lésions où la fonction s’arrête de façon incomplète sous le niveau » est obscure et ne coïncide pas avec la fenêtre associée (la zone de préservation partielle concerne l’absence de fonction sacrée). Toute reformulation fixe un champ d’application clinique : à trancher par l’audit médical.
- **R-02** (G82_a.html) — ancre : « ce qui rappelle que la vessie neurogène est une cause directe de décès évitable ». « Cause directe de décès évitable » est une inférence causale que les rapports standardisés de mortalité n’établissent pas ; la phrase suivante du piège d’interprétation affirme d’ailleurs qu’il s’agit d’associations. Atténuer ou retirer relève de l’audit médical.
- **R-03** (G82_a.html) — ancre : « (démontrée dans des données précliniques) ». L’incise s’accroche grammaticalement à « l’atteinte secondaire », alors que, selon la fenêtre associée, ce sont les données précliniques qui justifient la décompression. Corriger le rattachement précise ce qui est démontré : décision médicale.
- **R-04** (G82_a.html) — ancre : « <td>Sensitif incomplet</td> ». Dans la ligne AIS B, « sans motricité » ne précise pas le territoire (segments sacrés S4-S5 ou ensemble sous le niveau). Préciser modifie un critère de classification : à trancher par l’audit médical.
- **R-05** (G82_b.html) — ancre : « Les racines forment un nerf périphérique ». Les racines ne « forment » pas un nerf périphérique ; elles font partie du système nerveux périphérique et donnent naissance aux nerfs. Toute reformulation engage un énoncé anatomique : à trancher par l’audit médical.
- **R-06** (G82_b.html) — ancre : « la borne haute évite une surcharge sans bénéfice démontré ». « Surcharge » (de quoi : volume, pression, risque hémorragique ?) n’est pas défini ; le mot choisi engage un mécanisme. À trancher par l’audit médical.
- **R-07** (G82_b.html) — ancre : « Le détail de la grossesse et de la dysréflexie qui l’accompagne n’a pas été lu. ». « La dysréflexie qui l’accompagne » présente la dysréflexie comme un accompagnement systématique de la grossesse chez la femme lésée ; la formulation conditionnelle (« qui peut l’accompagner ») modifie le fond. À trancher par l’audit médical.
- **R-08** (G82_c.html) — ancre : « des extenseurs du coude cotés 2 et des muscles inférieurs cotés 0 ». La vignette ne cite que trois muscles pour le côté droit, puis des « muscles inférieurs » cotés 0, alors que le calcul qui suit (5 + 4 + 2 + 0 + 0 = 11) additionne cinq muscles du membre supérieur (les deux derniers, C8 et T1, ne sont pas nommés) ; la fenêtre du calcul parle de « membres inférieurs, cotés 0 » à part. Corriger la description modifie les données de la vignette : à trancher par l’audit médical.
- **R-09** (G82_c.html) — ancre : « Ce délai montre que le diagnostic repose d’abord sur la suspicion clinique d’une lésion médullaire lente. ». Non-sequitur : un délai de 12,5 mois jusqu’à l’IRM montre un retard diagnostique, non que le diagnostic « repose d’abord sur la suspicion clinique ». De même, « plus tard qu’elle ne devrait » énonce une norme non sourcée. Toute reformulation change l’énoncé : à trancher par l’audit médical.
- **R-10** (G82_c.html) — ancre : « structurent le bilan en deux niveaux ». Deux niveaux sont annoncés, mais seul le « bilan initial » est nommé ; le second niveau n’est pas identifié (l’urodynamique invasive, qui suit, n’est pas explicitement rattachée au second niveau). Nommer le second niveau ajoute un fait : à trancher par l’audit médical.
- **R-11** (G82_d.html) — ancre : « <td>Alpha-bloquants</td><td>Information professionnelle non relue</td> ». La leçon alterne « non lue » et « non relue » (tableau de la stratégie pharmacologique, fenêtres du codage, de la toxine botulique, de l’auto-sondage, de la spasticité). « Relue » suppose une première lecture. Choisir le bon terme revient à établir si l’information professionnelle a été lue : à trancher par l’audit médical.
- **R-12** (G82_d.html) — ancre : « le médicament freine la contraction des muscles lisses, ce qui est utile pour la vessie, mais dangereux là où un tonus … ». L’explication évoque les muscles lisses, alors que deux des contre-indications citées (myasthénie, glaucome à angle étroit) ne relèvent pas de ce mécanisme. Reformuler engage la justification pharmacologique : à trancher par l’audit médical.
- **R-13** (G82_pop1.html) — ancre : « Un tiers des patients sont à haut risque cardiovasculaire à la sortie de réadaptation ». La fenêtre dit « risque cardiovasculaire », le texte principal (section 4) dit « risque cardiométabolique » pour le même chiffre (« un tiers »). Aligner suppose de savoir lequel des deux a été mesuré : à trancher par l’audit médical.
- **R-14** (G82_pop1.html) — ancre : « 2 : mouvement sans pesanteur ». « Mouvement sans pesanteur » peut se lire comme un mouvement en apesanteur ; la cotation ISNCSCI parle de mouvement actif avec pesanteur éliminée. Reformuler précise une échelle de cotation : à trancher par l’audit médical.
- **R-15** (G82_pop2.html) — ancre : « chez 43,3 % des patients lésés au 6e segment thoracique ou au-dessus dans une étude ». Le texte principal, l’onglet des examens et la fenêtre de la dysréflexie disent « dans 43,3 % des urodynamiques (examens) » ; cette fenêtre dit « chez 43,3 % des patients ». L’unité (examens ou patients) ne se choisit que par la source : à trancher par l’audit médical.
- **R-16** (G82_pop2.html) — ancre : « Le score moteur gagne 4,50 points de plus. ». « De plus » appelle un comparateur (que la chirurgie tardive ?) qui n’est pas nommé. Ajouter le comparateur ajoute un fait : à trancher par l’audit médical.
- **R-17** (G82_pop2.html) — ancre : « Les hommes dont la lésion se situe au 6e segment thoracique ou au-dessus et les centres de fertilité sont informés du r… ». La phrase est à l’indicatif (« sont informés ») ; l’intention de la recommandation est probablement obligative (« doivent être informés »). Le changement de mode modifie la nature de l’énoncé : à trancher par l’audit médical.

## Observations et choix différés

- Espaces insécables : les sept fichiers ne contiennent aucun U+00A0 ni U+202F. Environ 477 espaces ordinaires précèdent « ; : ? ! » dans le texte visible, 13 paires de guillemets « » et environ 51 pourcentages sont écrits avec une espace ordinaire. La correction est mécanique et globale (remplacement par U+00A0 ou U+202F) ; elle n’est pas répartie en propositions locales mais constitue une règle d’intégration unique, à décider avec les autres leçons (la décision est différée dans les audits de référence G71).
- Registre méta : le mot « dossier » apparaît 25 fois dans le texte visible (« le dossier ne détaille pas », « n’a pas été documenté dans le dossier »), ainsi que « lecture du cours » (4 fois). Ces formules décrivent la fabrication du cours (STYLE_REDACTION, § 3) mais portent aussi la déclaration des lacunes de sources, exigée par le prompt de vérité. Leur reformulation relève d’une décision éditoriale commune avec l’audit médical (par exemple « aucune source lue ne précise… »). Aucune proposition locale n’est faite.
- Phrases nominales et infinitifs injonctifs : plusieurs cellules de tableau (section 9, « Viser au moins… »), les rubriques « Signes », « Séquence », « Priorités », « Choix selon le type » des fenêtres et les encadrés « Critères formels » et « Paramètres clés » sont nominaux ou à l’infinitif. Le guide de rédaction (§ 2) les proscrit hors titres et cellules brèves introduites ; leur réécriture complète dépasse la formulation locale et n’a pas été proposée, à l’exception des deux phrases nominales du corps de texte (sections 9, urgences 2 et 3) et de l’encadré « Science → examen » de la physiologie autonome.
- Libellés des mots verts : plusieurs libellés incorporent des parenthèses explicatives longues (par exemple « incidence des lésions médullaires traumatiques (chiffres hospitaliers et sous-couverture) ») qui entrent dans la phrase comme sujet ou complément ; la convention du moteur impose ces destinations annoncées, aucune proposition n’a été faite.
- Terminologie : « lorsque c’est faisable » (onglet des examens, fenêtre de l’IRM) et « lorsqu’elle est réalisable » (partie 8) désignent la même condition ; les guillemets de l’onglet des examens signalent une citation, ils n’ont pas été modifiés.
- Intitulé d’encadré : la rubrique « Science → traitement » de la neuroanatomie classificatoire porte sur le codage du niveau fonctionnel et non sur un traitement ; le gabarit à trois encadrés est conservé, l’intitulé relève d’un choix de structure.
- Hors périmètre linguistique (transmis à l’audit MED) : les figures 1 à 4 sont accompagnées d’une légende mais pas d’un paragraphe de lecture distinct (guide de rédaction, § 4).
- Base : le manifeste porte la base 523832d9ef6097607d3443f4398deee9cd0add11 ; la branche a été créée sur 103745baaa38c76f18288758cc7f689e5091ccdb. Aucun fichier de la leçon ne diffère entre ces deux commits (git diff vide sur chapters/G82 et glossary/g82.py).

## Lacunes

- Aucune vérification médicale n’a été faite : les renvois_medicaux signalent des formulations dont la correction changerait le fond ; ils ne sont ni confirmés ni infirmés.
- Aucun contrôle de rendu navigateur des propositions : l’application simulée a été faite en mémoire, aucun fichier canonique n’est modifié.
- Aucune lecture des sources primaires citées : les écarts avec les sources sont établis seulement par comparaison interne entre les sept fichiers de la leçon.
- Le contrôle de l’accord des libellés de mots verts avec la phrase qui les contient repose sur la lecture ; il n’a pas été exhaustif pour les 73 mots verts des quatre onglets.

## Tableau de bord final

| Rubrique | Résultat |
|---|---|
| Leçon | G82, fragment S08 (Neurologie, moelle épinière et paralysies) |
| Propositions / renvois | 80 / 17 |
| Fichiers canoniques modifiés | 0 |
| Contrôle des abréviations | {} avant et après application simulée |
| Poids des livrables | rapport.json, rapport.md, propositions.json |
| Alertes | espaces insécables globales différées ; registre « dossier » à décider ; un doute sur la vignette de cotation (R-08) |
