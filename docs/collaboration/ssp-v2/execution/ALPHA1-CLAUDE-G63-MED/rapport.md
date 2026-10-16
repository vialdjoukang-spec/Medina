# Audit médical Alpha, tour 1 — G63, Polynévrite au cours de maladies classées ailleurs (S08)

Mission `ALPHA1-CLAUDE-G63-MED` · branche `claude/alpha1/g63-med-g1` · base de mission `d1a488ad` (manifeste) · worktree créé sur `32416a20` · génération 1 · du 2026-10-16T05:51:52Z au 2026-10-16T06:18:55Z. Effort et modèle conformes au manifeste.

START exécuté sur le premier main contenant l'approbation de la mission (PR #181). Sources figées identiques : empreintes SHA-256 conformes au manifeste. Horodatages UTC relevés par `date -u` ; la fin est relevée juste avant le commit de traçabilité.

> Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.

## Synthèse

La leçon G63 est solide sur sa charpente : classification clinique, chiffres de Sommer et coll., règles suisses du pied diabétique, doses des informations professionnelles. L’audit relève **0 constat bloquant, 11 majeurs, 12 mineurs et 6 enrichissements**. Aucune dose dangereuse n’a été démontrée. Les défauts majeurs portent sur quatre points.

1. **La sémiologie manque — constat MAJEUR, bloquant pour la clôture du cours et du lot (AGENTS.md)** : aucune discipline « Sémiologie fondamentale et analytique », et l’onglet Sciences ne compte que quatre disciplines réelles (C01, C02).
2. **Le périmètre CIM est faux pour deux causes majeures** : la neuropathie alcoolique se code G62.1 et la neuropathie médicamenteuse, dont celle de la chimiothérapie, G62.0, non G63.4* ni G63.1* (C03).
3. **La douleur neuropathique repose sur une stratégie dépassée et un chiffre incomplet** : NeuPSIG a révisé ses lignes en 2025 (tramadol relégué en troisième ligne) et l’« efficacité comparable » affirmée n’est pas énoncée par les sources ; les NNT poolés contre placebo ne hiérarchisent pas les classes (C04, C05, C11).
4. **La sécurité médicamenteuse est incomplète face au patient type** : contre-indications de la duloxétine (inhibiteurs du CYP1A2, hypertension non équilibrée), prégabaline exclue sous 30 mL/min, mésusage des gabapentinoïdes chez le patient alcoolique, dose et ordre de la thiamine dans l’encéphalopathie de Wernicke (C06 à C09). S’y ajoute un délai de dépistage du type 1 tiré d’une recommandation nord-américaine (C10).

Empreintes SHA-256 des sept fichiers : **conformes** au manifeste. Première source lue : https://doi.org/10.1016/S1474-4422(14)70251-0 (Résumé PubMed 25575710 (NNT et lignes de traitement)).

## Constats bloquants (0)

Aucun.

## Constats majeurs (11)

**C01 — `chapters/G63/G63_c.html` (bloquant pour la clôture).** Sémiologie absente de l’onglet Sciences : aucune discipline « Sémiologie fondamentale et analytique » (bouton data-s="g63-s-semio" en tête de .sci-bar). Les éléments sémiologiques existent seulement de façon descriptive dans g63-5 et g63-6 (tableau des fibres, signe clé, monofilament, diapason) : pas de mécanisme par signe, pas de valeur chiffrée hors prédiction de l’ulcère, pas de tableau des syndromes, pas d’examen systématique en étapes, pas de cas corrigés consacrés aux signes. SEM-01, SEM-02, SEM-13 et SEM-19 à « non ».  
*Preuve :* [S1] tableau 1 (symptômes, signes) ; [S4] notes (5) et (6) ; [S14] résumé.  
*Proposition :* Insérer la discipline complète de propositions/G63_c_1.html (sept îlots g63-sm-1 à g63-sm-7, figure S1, trois cas corrigés) et les fenêtres de propositions/G63_pop3_1.html dans un nouveau G63_pop3.html.

**C02 — `chapters/G63/G63_c.html`.** L’onglet Sciences ne compte que quatre disciplines réelles (Anatomie, Histologie, Physiologie, Biochimie et génétique) ; l’addendum du lot 2 en exige cinq, puis la Sémiologie. La discipline la plus utile manquante est l’immunologie : elle explique G63.1* (anticorps neuronaux, paraprotéines), G63.5* (vasculite) et les trois diagnostics immunitaires à exclure (Guillain-Barré, PIDC, neuropathie motrice multifocale).  
*Preuve :* [S7] texte, phénotypes et anticorps ; [S1] paraprotéines ; [S11] résumé.  
*Proposition :* Ajouter la discipline Immunologie de propositions/G63_c_2.html (≥ 280 mots, figure accessible, quatre libellés).

**C03 — `chapters/G63/G63_a.html`.** Périmètre CIM-10-GM inexact : la leçon range la neuropathie alcoolique sous G63.4* et la neuropathie du traitement anticancéreux sous G63.1* (tableaux de g63-1 et g63-4). La CIM-10-GM 2024 code la polyneuropathie alcoolique en G62.1 et la polyneuropathie médicamenteuse en G62.0 (avec code de substance). La « lacune de codage » déclarée dans le piège de g63-1, dans g63-chimio et dans le glossaire (G62.0) est donc tranchée par la source.  
*Preuve :* [S15] G62.0, G62.1, G62.2 ; [S15] G63.1*.  
*Proposition :* Appliquer propositions/G63_a_1.html (cellules corrigées, paragraphe et tableau G62/G63, piège réécrit) ; reporter dans g63-4, g63-chimio et glossary/g63.py.

**C04 — `chapters/G63/G63_d.html`.** Affirmation inexacte sur un point décisionnel : la leçon présente les quatre classes de première ligne comme d’efficacité comparable (NNT 6,4 à 7,7) et omet le NNT des antidépresseurs tricycliques. Cette équivalence n’est pas énoncée par les sources lues. Le résumé de 2015 précise que les NNT étaient plus bas pour les tricycliques ; la mise à jour de 2025 donne 4,6 pour les tricycliques, 8,9 pour les ligands α2δ et 7,4 pour les inhibiteurs de la recapture. Même erreur dans g63-9.2 (« Le choix ... non d’un avantage net d’efficacité »), dans la fenêtre g63-nnt, le Pareto g63-pharma, l’encadré key de g63-9 et la figure 5.  
*Preuve :* [S8] résumé ; [S9] résumé.  
*Proposition :* Remplacer l’encadré key de g63-p-1 et insérer le tableau NNT/NNH de propositions/G63_d_1.html ; corriger g63-9.2, g63-nnt, la figure 5 et le Pareto en conséquence.

**C05 — `chapters/G63/G63_b.html`.** Source obsolète sur la stratégie de la douleur neuropathique : NeuPSIG a révisé ses recommandations en 2025 (313 essais). La deuxième ligne devient capsaïcine 8 %, capsaïcine en crème et lidocaïne 5 % (recommandation faible) ; les opioïdes (dont le tramadol, deuxième ligne en 2015) passent en troisième ligne avec la toxine botulique A et la stimulation magnétique transcrânienne répétée. La leçon place encore le tramadol en deuxième ligne (g63-9.2, g63-p-1, g63-douleur).  
*Preuve :* [S9] résumé ; [S8] résumé.  
*Proposition :* Fonder la stratégie sur Soliman et coll. 2025 (propositions/G63_d_1.html) ; mentionner 2015 comme version antérieure dans la fenêtre g63-douleur.

**C06 — `chapters/G63/G63_d.html`.** Contre-indications de la duloxétine incomplètes alors que la FI suisse lue les donne : association aux inhibiteurs du CYP1A2 (fluvoxamine, ciprofloxacine, énoxacine) et instauration en cas d’hypertension artérielle non équilibrée. La phrase « Les sources lues ne listent pas d’autres interactions » est contredite par la source citée. La ciprofloxacine est d’usage courant chez le diabétique (infection du pied, infection urinaire).  
*Preuve :* [S18] Contre-indications ; [S18] Contre-indications.  
*Proposition :* Remplacer l’alert de g63-p-3 par le bloc 1 de propositions/G63_d_2.html ; compléter la fenêtre g63-duloxetine.

**C07 — `chapters/G63/G63_b.html`.** Dans le paragraphe « Insuffisance rénale et dialyse », la leçon laisse entendre que la prégabaline s’adapte chez le dialysé. La FI suisse de Lyrica (juillet 2026) dit que la prégabaline « ne doit pas être utilisée » si la clairance est inférieure à 30 mL/min. Le tableau g63-p-2 et la fenêtre g63-pregabaline adoucissent la formule (« l’information consultée ne prévoit pas l’emploi »). Le cas 5 (clairance 25 mL/min) est cohérent pour la duloxétine mais ne dit pas que la prégabaline est elle aussi exclue.  
*Preuve :* [S16] Posologie, troubles de la fonction rénale ; [S17] Posologie, hémodialyse.  
*Proposition :* Paragraphe 1 de propositions/G63_b_2.html ; remplacer dans g63-p-2 et g63-pregabaline « l’information consultée ne prévoit pas l’emploi » par « ne doit pas être utilisée » ; ajouter dans la correction du cas 5 que la prégabaline est aussi exclue.

**C08 — `chapters/G63/G63_d.html`.** Mises en garde majeures absentes pour les gabapentinoïdes, alors qu’un patient type du cours est dépendant de l’alcool : mésusage et dépendance (y compris aux doses thérapeutiques), évaluation du risque avant prescription, arrêt progressif sur des semaines à des mois, dépression respiratoire et décès en association avec les opioïdes (désormais troisième ligne).  
*Preuve :* [S16] Mises en garde ; [S16] Posologie, arrêt ; [S17] Mises en garde.  
*Proposition :* Insérer le bloc 2 de propositions/G63_d_2.html après « Effets indésirables à surveiller » et l’ajouter aux fenêtres g63-pregabaline et g63-gabapentine.

**C09 — `chapters/G63/G63_b.html`.** L’urgence thiamine est incomplète : ni critères cliniques de l’encéphalopathie de Wernicke chez l’alcoolique (deux signes sur quatre), ni règle « thiamine avant tout glucide », ni dose de la recommandation européenne (200 mg trois fois par jour, de préférence IV). La leçon ne donne que le plafond de la FI Benerva de 2019 (jusqu’à 200 mg par jour). Le contentieux FI/recommandation n’est pas présenté, contrairement à la consigne sur les contentieux.  
*Preuve :* [S10] résumé, recommandations 2 et 5 ; [S22] Posologie.  
*Proposition :* Appliquer propositions/G63_b_1.html (alert reformulée, fenêtre de contentieux).

**C10 — `chapters/G63/G63_b.html`.** Conduite fondée sur une recommandation nord-américaine : le délai de dépistage dans le diabète de type 1 (cinq ans après le diagnostic) est, dans la revue de Feldman et coll., attribué à l’ADA et à la Canadian Diabetes Association. Aucune source suisse ou européenne lue ne fixe ce délai.  
*Preuve :* [S2] section dépistage ; [S3] § 1.  
*Proposition :* Paragraphe 2 de propositions/G63_b_2.html ; déclarer la lacune pour le type 1 et rechercher une source SSED ou européenne.

**C11 — `chapters/G63/G63_c.html`.** Figure 5 illisible à 390 px et incomplète : viewBox de 640 de large, texte rendu à 7,3 px (mesure Chromium), étiquettes « Recapture sérotonine et noradrénaline » et « Prégabaline » qui se chevauchent ; elle porte des valeurs décisionnelles (NNT) et omet la classe au NNT le plus bas (tricycliques). Les hauteurs ne sont pas exactement proportionnelles (6,4 → 120 ; 7,7 → 134). Données de 2015 dépassées (C05).  
*Preuve :* [S9] résumé ; [S8] résumé.  
*Proposition :* Remplacer la figure par le tableau NNT/NNH de propositions/G63_d_1.html, ou redessiner un SVG de 360 de large à 14 px avec les quatre classes de première et deuxième ligne de 2025, étiquettes sur deux lignes.

## Constats mineurs (12)

**C12 — `chapters/G63/G63_c.html`.** Figures 3 et 4 : viewBox de 640 de large, texte rendu à 7,3 px à 390 px (mesure Chromium). Aucune valeur décisionnelle, mais lecture difficile sur téléphone.  
*Preuve :* contrôle mécanique (mesure Chromium ou script du projet).  
*Proposition :* Redessiner en viewBox 360 de large, font-size 14, textes sur deux lignes (modèle des figures 1, 2 et 6, rendues à 13,2 px).

**C13 — `chapters/G63/G63_a.html`.** Causalité surévaluée : Feldman et coll. écrivent que l’insulinorésistance neuronale « pourrait expliquer en partie » le moindre bénéfice. Même formulation dans g63-diab-meca, g63-contglyc et le key « Science → clinique » de g63-s-bioch.  
*Preuve :* [S2] section mécanismes.  
*Proposition :* « L’insulinorésistance neuronale pourrait expliquer en partie ce moindre bénéfice ; c’est une hypothèse. »

**C14 — `chapters/G63/G63_b.html`.** Attribution erronée : le lien entre monofilament manqué et neuropathie des grosses fibres ne figure pas dans Feldman et coll. ; il vient du document suisse QualiCCare 2016 (note 5).  
*Preuve :* [S4] note (5) ; [S2] section diagnostic.  
*Proposition :* Citer QualiCCare 2016 pour le monofilament et Feldman et coll. pour la neurographie normale des petites fibres.

**C15 — `chapters/G63/G63_a.html`.** Chiffre non attribué : il vient de l’étude de Mygland (Vest-Agder) citée par Julian et coll. 2019. De même, le couple « environ 30 % contre 11 % » (g63-4, g63-5, g63-alcool) vient de Wetterling cité par Julian et coll. (29,6 % continus, 29,9 % fréquents, 11,3 % épisodiques), non de Sommer et coll., qui ne donne pas ces chiffres.  
*Preuve :* [S6] section prévalence ; [S6] section facteurs de risque.  
*Proposition :* Ajouter « (Mygland, cité par Julian et coll., 2019) » et « (Wetterling, cité par Julian et coll., 2019) ».

**C16 — `chapters/G63/G63_pop1.html`.** Attribution erronée (fenêtre g63-neuronopathie ; aussi g63-s-bioch « selon Sommer et coll. » et glossaire CV2) : Sommer et coll. 2018 ne mentionnent ni anti-Hu, ni CV2/CRMP5, ni amphiphysine, ni syndrome paranéoplasique. Les faits sont exacts, mais leur source est Graus et coll. 2021.  
*Preuve :* [S1] recherche plein texte ; [S7] phénotypes.  
*Proposition :* Remplacer « Sommer et coll. citent aussi » par « Graus et coll. citent aussi » dans g63-neuronopathie, g63-s-bioch et glossary/g63.py (CV2).

**C18 — `chapters/G63/G63_d.html`.** Posologie de Qutenza incomplète : la FI suisse précise qu’un renouvellement avant 90 jours ne s’envisage qu’après une évaluation minutieuse, avec un minimum de 60 jours, et une réévaluation après 3 traitements.  
*Preuve :* [S20] Posologie.  
*Proposition :* « Intervalle habituel de 90 jours ; 60 jours au minimum après évaluation minutieuse ; réévaluation après 3 traitements. »

**C19 — `chapters/G63/G63_d.html`.** Emplois hors indication non signalés (addendum § 5) : la toxine botulique A n’a pas d’indication suisse de douleur neuropathique ; aucune spécialité de lidocaïne 5 % en emplâtre n’a été trouvée dans AmiKo ; la gabapentine n’est autorisée que pour la douleur de la neuropathie diabétique et de la névralgie postherpétique (pas pour les neuropathies alcoolique, urémique ou chimio-induites).  
*Preuve :* [S25] champ indication ; [S17] Indications.  
*Proposition :* Ajouter la colonne « Statut en Suisse » du tableau de propositions/G63_d_1.html et la mention « hors indication » partout où ces produits sont cités.

**C20 — `chapters/G63/G63_c.html`.** Contrat des sciences non satisfait : tests/audit_sciences.py échoue sur les quatre disciplines (« lien absent : À retenir. »). Aucune discipline ne se ferme par un encadré « À retenir. ».  
*Preuve :* contrôle mécanique (mesure Chromium ou script du projet).  
*Proposition :* Ajouter un encadré <div class="key"><b>À retenir.</b> …</div> à la fin de chaque discipline (g63-s-anat, -histo, -physio, -bioch).

**C21 — `chapters/G63/G63_a.html`.** Formulation trop affirmative : selon Sommer et coll., une paraprotéine trouvée chez un patient atteint de polyneuropathie est le plus souvent une coïncidence sans conséquence thérapeutique ; seuls un taux élevé ou un phénotype évocateur (IgM anti-MAG, POEMS) orientent vers une hémopathie.  
*Preuve :* [S1] paraprotéines.  
*Proposition :* « Une paraprotéine est souvent une coïncidence ; un taux élevé ou un phénotype évocateur (neuropathie démyélinisante distale à IgM anti-MAG, POEMS) oriente vers une hémopathie. »

**C22 — `chapters/G63/G63_b.html`.** Ambiguïté : dans le guide QualiCCare 2023, le suivi au moins hebdomadaire concerne le pied diabétique aigu (ulcère, Charcot), non tout pied à risque. Placée après les drapeaux rouges sans ce contexte, la phrase peut contredire les fréquences annuelles à trimestrielles de g63-9.3.  
*Preuve :* [S5] stratification.  
*Proposition :* « Pour un ulcère ou un pied aigu, le suivi est au moins hebdomadaire, quel que soit le niveau de soins. »

**C23 — `chapters/G63/G63_b.html`.** Hiérarchie des sources : la règle sur la metformine est attribuée à une revue nord-américaine (Feldman et coll.) alors que la FI suisse de Glucophage (octobre 2025) la fonde : contrôle régulier, par exemple annuel, surtout en cas d’anémie ou de neuropathie périphérique ; risque croissant avec la dose et la durée.  
*Preuve :* [S23] Mises en garde.  
*Proposition :* « La deuxième porte sur la metformine : son information professionnelle suisse recommande de contrôler la vitamine B12 régulièrement, par exemple chaque année, surtout en cas de neuropathie, car le risque de carence croît avec la dose et la durée. »

**C24 — `chapters/G63/G63_b.html`.** Nuance omise : l’entretien de 18 à 24 mois concerne les patients en rémission après une association, et se fait par azathioprine ou méthotrexate ; le cyclophosphamide est réservé aux formes sévères, de préférence en bolus intraveineux.  
*Preuve :* [S11] résumé, recommandations 4 et 5.  
*Proposition :* « … ; après rémission sous association, entretien de 18 à 24 mois par azathioprine ou méthotrexate ; cyclophosphamide pour les formes sévères, en bolus intraveineux. »

## Enrichissements (6)

**C25 — `chapters/G63/G63_b.html`.** Le diagnostic différentiel du Guillain-Barré ne donne ni le traitement européen (IgIV, échanges plasmatiques), ni l’outil de risque respiratoire, ni la requalification en PIDC à début aigu au-delà de 8 semaines.  
*Preuve :* [S12] résumé ; [S12] résumé.  
*Proposition :* Paragraphe 3 de propositions/G63_b_2.html ; phrase sur A-CIDP dans g63-pidc.

**C26 — `chapters/G63/G63_d.html`.** Surveillance de la substitution en vitamine B12 incomplète : la FI de Vitarubine Dépôt demande de contrôler régulièrement la kaliémie (érythropoïèse relancée) et de traiter une carence en folates associée ; elle signale aussi un risque thromboembolique transitoire chez les patients prédisposés.  
*Preuve :* [S21] Mises en garde ; [S21] Indications.  
*Proposition :* Bloc 3 de propositions/G63_d_2.html dans g63-hydroxocobalamine.

**C27 — `chapters/G63/G63_b.html`.** Valeur sémiologique des pouls et de l’index de pression systolique absente de l’examen du pied : pouls pédieux absent chez jusqu’à 8 % des sujets sains, tibial postérieur chez jusqu’à 3 % ; IPS < 0,9 hautement suspect ; IPS > 1,3 (médiacalcose) chez 30 % des patients avec ulcère.  
*Preuve :* [S4] notes (3) et (4).  
*Proposition :* Fenêtre g63-sm-pouls de propositions/G63_pop3_1.html, reliée depuis g63-6.

**C28 — `chapters/G63/G63_b.html`.** La limite du réflexe achilléen isolé n’est pas chiffrée : dans une cohorte autrichienne de 2022 diabétiques, il manquait chez 24,8 % des patients à vibration normale (68,6 % si vibration anormale).  
*Preuve :* [S14] résumé.  
*Proposition :* Fenêtre g63-sm-achille de propositions/G63_pop3_1.html ; une phrase dans g63-signes.

**C29 — `chapters/G63/G63_c.html`.** L’onglet des examens ne présente pas la place des anticorps antigangliosides dans le Guillain-Barré : valeur limitée dans la forme typique, anti-GQ1b seulement si un syndrome de Miller Fisher est suspecté ; anticorps nodaux et paranodaux si une nodopathie auto-immune est suspectée.  
*Preuve :* [S12] résumé.  
*Proposition :* Une ligne dans le tableau de g63-e-1 (« Une forme aiguë immunitaire est-elle suspectée ? ») et la discipline Immunologie (propositions/G63_c_2.html).

**C30 — `chapters/G63/G63_d.html`.** Mises en garde utiles de la duloxétine absentes : hausse moyenne de la pression artérielle de 1 à 2 mmHg, crises hypertensives rapportées, hyponatrémie (surtout chez le sujet âgé).  
*Preuve :* [S18] Mises en garde ; [S18] Mises en garde.  
*Proposition :* Ajouter dans g63-duloxetine : « Surveillance : pression artérielle (hausse moyenne de 1 à 2 mmHg, crises hypertensives rapportées) et natrémie chez le sujet âgé. »

## Matrice des 20 rubriques

| Rang | Rubrique | Statut | Onglet ou ancre |
|---|---|---|---|
| 1 | Question clinique et enjeu pour l’examen fédéral | couvert | g63-0 (trois vignettes) |
| 2 | Définition et périmètre CIM-10-GM | partiel | g63-1 ; rattachements G62.1 (alcool) et G62.0 (médicaments) erronés (C03) |
| 3 | Classifications et stades | couvert | g63-1 (distribution, fibres, évolution ; quatre formes du diabète) |
| 4 | Épidémiologie suisse puis européenne | partiel | g63-2 ; aucune donnée suisse (lacune déclarée par la leçon) |
| 5 | Normal → pathologique | partiel | g63-3, g63-s-anat, g63-s-histo ; structure normale du nerf non décrite (déclaré) |
| 6 | Étiologies et facteurs de risque | couvert | g63-4 ; G63.0 hors Lyme, G63.3 hors amylose et G63.6 sans source (déclaré) |
| 7 | Anamnèse et symptômes (fréquences) | partiel | g63-5 ; seules les fréquences de la douleur sont chiffrées |
| 8 | Examen clinique (sensibilité/spécificité) | partiel | g63-6, g63-e-2 ; valeurs seulement pour la prédiction de l’ulcère (C27, C28) |
| 9 | Drapeaux rouges et urgences | partiel | g63-8 ; Wernicke incomplet (C09), traitement du Guillain-Barré absent (C25) |
| 10 | Examens complémentaires | couvert | g63-e-1 à g63-e-4 ; valeurs de référence de laboratoire non données (déclaré) |
| 11 | Diagnostic différentiel | couvert | g63-7 (tableau avec éléments discriminants) |
| 12 | Prise en charge suisse (FI datées) | partiel | g63-9, g63-p-1 à g63-p-4 ; C04 à C08, C18, C19 |
| 13 | Complications et pronostic | couvert | g63-10, g63-pronostic-pied |
| 14 | Suivi, prévention, dépistage | partiel | g63-10 ; délai type 1 d’origine nord-américaine (C10) |
| 15 | Situations particulières | partiel | g63-11 (grossesse, âgé, rein, protoxyde d’azote) ; enfant absent |
| 16 | Spécificités suisses | partiel | g63-9.3 (AI, QualiCCare) ; règle d’âge AI non vérifiée (lacune) ; Suva, aptitude à la conduite et remboursement absents |
| 17 | Critères formels du diagnostic | couvert | g63-12 div.alert |
| 18 | Paramètres clés chiffrés | couvert | g63-12 div.key (NNT à corriger, C04) |
| 19 | Sous-codes CIM-10-GM couverts | partiel | tableau de g63-1 ; G63.6 sans contenu ; frontière G62 non traitée (C03) |
| 20 | Points d’examen fédéral | partiel | pièges et cas présents (g63-7, g63-e-5) ; aucune correspondance PROFILES explicite |

## 21 — Sémiologie fondamentale et analytique

**Statut : absente** (constat C01, MAJEUR, bloquant pour la clôture du cours et du lot, AGENTS.md). La sémiologie fondamentale est **partielle** : elle se limite à g63-5 (tableau des familles de fibres), g63-6 (signe clé, monofilament, diapason), g63-signes, g63-mono, g63-diapason. Il manque : mécanisme causal par signe, valeur chiffrée hors prédiction de l’ulcère, réflexe achilléen isolé et sa limite, réflexes vifs et signes pyramidaux de la myéloneuropathie, pouls du pied et leur valeur. La sémiologie analytique est **absente** ; il manque : tableau des syndromes, raisonnement en cinq étapes, examen systématique numéroté, synthèse présentée, trois cas corrigés sur les signes.

La proposition `propositions/G63_c_1.html` rédige la discipline complète en sept îlots, selon la structure du § 4 b : priorité clinique (Guillain-Barré, Wernicke, pied urgent), tableau des symptômes avec mécanisme et valeur, signes physiques (monofilament, diapason, achilléen, pouls, signes pyramidaux), tableau de sept syndromes, raisonnement en cinq étapes, examen systématique en onze étapes avec présentation type, trois cas corrigés. Les fenêtres des nouveaux mots verts sont dans `propositions/G63_pop3_1.html`. Chaque valeur absente des sources est écrite comme telle.

| Critère | Résultat |
|---|---|
| SEM-01 | non |
| SEM-02 | non |
| SEM-03 | non (audit_sciences.py échoue déjà sur les quatre disciplines, C20) |
| SEM-04 | oui pour l’existant (test_v7.py --static G63 : OK) ; sans objet pour la discipline absente |
| SEM-05 | non (tableau de g63-5 sans colonnes mécanisme, valeur et piège) |
| SEM-06 | partiel : technique du monofilament et du diapason seulement (g63-mono, g63-diapason) |
| SEM-07 | non |
| SEM-08 | partiel : valeurs du monofilament sourcées (S4) ; absences non déclarées pour les autres signes |
| SEM-09 | partiel (normes du monofilament et du diapason) |
| SEM-10 | partiel (pièges du monofilament, de la callosité, des petites fibres) |
| SEM-11 | non |
| SEM-12 | non (g63-7 donne quatre questions, pas les cinq étapes) |
| SEM-13 | non dans les Sciences ; alert présent dans g63-8 |
| SEM-14 | oui dans g63-7 (tableau du différentiel) |
| SEM-15 | non |
| SEM-16 | non |
| SEM-17 | non (aucun cas consacré à la valeur d’un signe) |
| SEM-18 | sans objet (vérification navigateur non réalisée) |
| SEM-19 | non pour la discipline absente ; non pour l’existant (C10, C23) |
| SEM-20 | sans objet |
| SEM-21 | sans objet |
| SEM-22 | non réalisé (capture non prise par ce rôle d’audit) |
| SEM-23 | non réalisé |
| SEM-24 | oui (bandeau : revue par intelligence artificielle, aucune validation médicale humaine) |

Lacunes propres à la sémiologie :

- Aucune source universitaire suisse de sémiologie neurologique périphérique n’a pu être lue (diapositives Unisanté 2023 de J.-B. Epiney : redirection 301, contenu non lu).
- Technique du réflexe achilléen et du testing de la force non décrites dans les sources lues.
- Seuil de l’hypotension orthostatique : consensus de 2011 (Freeman et coll.) sans résumé accessible ; seuil non écrit.
- Sensibilité et spécificité des symptômes (brûlure, engourdissement, ataxie) non chiffrées dans les sources lues.

## Figures

L’inventaire `tools/image_clo_finder.py inventory G63` trouve six figures, toutes des **schémas non anatomiques** (aucune image anatomique, aucune origine IA à démontrer), et quatre icônes de boutons. Mesure dans Chromium à 390 px de large :

| Figure | Fichier | viewBox | Texte rendu | Constat |
|---|---|---|---|---|
| Figure 1 | G63_a.html | 380 | 13.2 px | — |
| Figure 2 | G63_b.html | 380 | 13.2 px | — |
| Figure 3 | G63_c.html | 640 | 7.3 px | C12 |
| Figure 4 | G63_c.html | 640 | 7.3 px | C12 |
| Figure 5 | G63_c.html | 640 | 7.3 px + chevauchement | C11 |
| Figure 6 | G63_c.html | 380 | 13.2 px | — |

## Contrôles exécutés

- `python3 test_v7.py --static G63` : OK (G63 mots 16667 fenêtres 49 quiz 7 pareto 14).
- `python3 tests/audit_sciences.py --base 32416a20… --codes G63` : échec : « lien absent : À retenir. » sur g63-s-anat, -histo, -physio, -bioch (C20).
- Ancres des 30 constats : une occurrence exacte chacune (script).
- `python3 -m json.tool` sur `rapport.json` et `sources.json`.

## Vérifications conformes (échantillon)

- Prévalence 5–8 %, cause non trouvée ≤ 30 %, diabète type 1 8–54 %, type 2 13–46 %, alcoolisme 22–66 %, chimiothérapie 30–40 % [S1]
- Signe clé aréflexie + pallesthésie ou piqûre [S1]
- Alcool > 100 g/j pendant des années [S1] ; méta-analyse 44,2 % et 46,3 %, douleur 42 %, Koike < 1 mois dans 56 %, récupération [S6]
- B12 : ~50 % sans anémie macrocytaire ; myéloneuropathie [S1] ; besoin, réserve, N2O, posologie Vitarubine [S21]
- Oxaliplatine 60–80 % réversible en 2–3 j, 73 % persistant, coasting, 40 % douleur chronique [S1]
- Guillain-Barré 1–2/100 000/an, nadir ≤ 4 semaines ; PIDC LCR < 10/µL et protéines élevées ; anti-GM1 50 % [S1]
- Vasculite à suspecter dans la PNP distale symétrique subaiguë [S1] ; critères et traitement PNS 2010 [S11]
- Anticorps à haut risque > 70 %, anti-Hu > 85 % CBPC, dépistage 4–6 mois pendant 2 ans, PNS-Care ≥ 8, GBS/PIDC non paranéoplasiques sans anticorps [S7]
- Feldman : 6100 et 2800/100 000 années-personnes, 1–4 % dont 40–55 % diabète, douleur 30–50 %, sural > 6 µV et > 39 m/s, différences de risque −1,84 et −0,58, HbA1c < 6 % [S2]
- QualiCCare : catégories IWGDF et fréquences, monofilament (technique, Se 65–90 %, Sp 35–85 %), diapason ≤ 4/8, ≥ 5/8, récidive ×36 et 40 %, réamputation 27/48/61 %, mortalité 46 %, drapeaux rouges et seuils IPS/tcPO2/orteil [S3 ; S4 ; S5]
- Lyrica : posologie 150/300/600, tableau rénal 30–60, poids 5,2 %, grossesse 2700 expositions [S16]
- Neurontin : titration, 900–3600 mg, tableau rénal exact [S17]
- Duloxétine : 60 mg, pas de bénéfice > 60 mg, évaluation 2 mois puis 3 mois, HbA1c + 0,3 % à 52 semaines [S18]
- Saroten : indication douleurs neuropathiques, 10–25 mg, 25–75 mg, > 100 mg précaution, 2–4 semaines, contre-indications, mécanisme analgésique indépendant [S19]
- Qutenza : 4 patchs, 30/60 min, gants nitrile, examen des pieds [S20]
- Benerva : 100 mg/2 j, 100 mg/j, 200–300 mg/j, parentéral ≤ 200 mg/j, 0,4 mg pour 4200 kJ [S22]
- CIM-10-GM : G63.0*–G63.8* et codes primaires, exclusions du bloc [S15]

## Lacunes

- Sommer et coll. 2018 : lu par outil de lecture de la page PMC (passages ciblés), non par téléchargement intégral (le serveur PMC renvoie une page reCAPTCHA à curl).
- Feldman et coll. 2019, Julian et coll. 2019 et Graus et coll. 2021 : seuls les 100 000 premiers caractères ont été lus ; les tableaux en image de Graus (1, 5) non lus.
- Recommandation ESMO-EONS-EANO 2020 sur la neurotoxicité des traitements anticancéreux : non relue (inaccessible lors du cycle Betta) ; aucune conduite de prévention vérifiable.
- Seuil d’hypotension orthostatique : aucune source lue (consensus 2011 sans résumé).
- Délai de dépistage dans le diabète de type 1 : aucune source suisse ou européenne lue (requête PubMed et documents SSED).
- Lidocaïne 5 % en emplâtre : aucune spécialité trouvée par la recherche AmiKo (« lidocain », « emplâtre », « Pflaster », « versatis ») ; statut suisse à confirmer.
- Règle d’âge AI pour les chaussures adaptées au diabète (g63-9.3, g63-pied : « moins de 65 ans (homme) ou 64 ans (femme) », d’après QualiCCare 2013) : non vérifiée, car la circulaire AI en vigueur n’a pas été lue. L’âge de référence AVS 21 a été lu [S24], mais son application à cette prestation n’est pas démontrée ; aucune correction n’est proposée.
- Source universitaire suisse de sémiologie (Unisanté, Epiney 2023) : redirection 301, non lue.
- Aucune donnée épidémiologique suisse ; aucune source sur Suva (neuropathies toxiques professionnelles), aptitude à la conduite ni remboursement LS.
- Recommandations actuelles de l’amylose à transthyrétine (silenceurs de gène) non lues ; consensus 2016 seul.
- Vérification navigateur des fenêtres, captures à 390 px avec police 24 px : non réalisées par ce rôle d’audit (SEM-18, SEM-22, SEM-23).

## Sources lues

| Id | Source | Niveau | Date |
|---|---|---|---|
| S1 | Polyneuropathies (Sommer C, Geber C, Young P, Forst R, Birklein F, Schoser B), Dtsch Arztebl Int 2018;115:83–90 — Deutsches Ärzteblatt International (revue fondée sur la recommandation DGN) | section | 2018-02 |
| S2 | Diabetic neuropathy (Feldman EL et al.), Nature Reviews Disease Primers 2019;5:42 — Nature Reviews Disease Primers | section | 2019-06 |
| S3 | Eckwerte des Fuss-Managements bei Typ-2-Diabetes mellitus in der Grundversorgung (QualiCCare) — Société suisse d’endocrinologie et de diabétologie (SSED/SGED) | texte_integral | 2013-08-15 (état septembre 2014) |
| S4 | Zusatzinformationen zu Risiko-Test (finale Version, 02.06.2016) — SSED/SGED – QualiCCare | texte_integral | 2016-06-02 |
| S5 | Praxisleitfaden zur optimalen Behandlung eines akuten diabetischen Fusssyndroms und Fussulkus (DFS/DFU), version 2023 — QualiCCare / SSED | section | 2023-08 |
| S6 | Alcohol-related peripheral neuropathy: a systematic review and meta-analysis (Julian T et al.), J Neurol 2019;266:2907–2919 — Journal of Neurology | section | 2019 |
| S7 | Updated Diagnostic Criteria for Paraneoplastic Neurologic Syndromes (Graus F et al.), Neurol Neuroimmunol Neuroinflamm 2021;8:e1014 — Neurology Neuroimmunology & Neuroinflammation | section | 2021-05 |
| S8 | Pharmacotherapy for neuropathic pain in adults: a systematic review and meta-analysis (Finnerup NB et al.), Lancet Neurol 2015;14:162–173 — NeuPSIG / IASP | resume | 2015-01-07 |
| S9 | Pharmacotherapy and non-invasive neuromodulation for neuropathic pain: a systematic review and meta-analysis (Soliman N et al.), Lancet Neurol 2025;24:413–428 — NeuPSIG et ERA-NET Neuron | resume | 2025-05 |
| S10 | EFNS guidelines for diagnosis, therapy and prevention of Wernicke encephalopathy (Galvin R et al.), Eur J Neurol 2010;17:1408–1418 — European Federation of Neurological Societies | resume | 2010-12 |
| S11 | PNS Guideline on non-systemic vasculitic neuropathy: executive summary (Collins MP et al.), J Peripher Nerv Syst 2010;15:176–184 — Peripheral Nerve Society | resume | 2010-09 |
| S12 | European Academy of Neurology/Peripheral Nerve Society Guideline on diagnosis and treatment of Guillain-Barré syndrome (van Doorn PA et al.), Eur J Neurol 2023;30:3646–3674 — EAN / PNS | resume | 2023-10-10 |
| S13 | EAN/PNS guideline on diagnosis and treatment of CIDP – second revision (Van den Bergh PYK et al.), Eur J Neurol 2021;28:3556–3583 — EAN / PNS | resume | 2021-07-30 |
| S14 | The value of the Rydel-Seiffer tuning fork as a predictor of diabetic polyneuropathy compared with a neurothesiometer (Kästenbauer T et al.), Diabet Med 2004;21:563–567 — Institut Ludwig-Boltzmann, Vienne | resume | 2004-06 |
| S15 | CIM-10-GM 2024, bloc G60–G64 (G61.0, G62.0, G62.1, G62.2, G63.0*–G63.8*) — BfArM (Institut fédéral allemand des médicaments et dispositifs médicaux) | section | 2023 (version 2024) |
| S16 | Information professionnelle suisse Lyrica® gélules (prégabaline), Viatris Pharma GmbH — Swissmedic (AIPS via AmiKo, GTIN 7680570570016) | texte_integral | 2026-07 (mise à jour de l’information, version 110 F) |
| S17 | Information professionnelle suisse Neurontin® (gabapentine), Viatris Pharma GmbH — Swissmedic (AIPS via AmiKo, GTIN 7680525200104) | texte_integral | 2025-04 (version 107 F) |
| S18 | Information professionnelle suisse Duloxetin-Mepha® gélules gastrorésistantes (duloxétine), Mepha Pharma AG — Swissmedic (AIPS via AmiKo, GTIN 7680660980053) | texte_integral | 2024-12 |
| S19 | Information professionnelle suisse Saroten® (amitriptyline), Lundbeck (Schweiz) AG — Swissmedic (AIPS via AmiKo, GTIN 7680669780012) | texte_integral | 2022-10 |
| S20 | Information professionnelle suisse Qutenza® patch cutané (capsaïcine 8 %), Grünenthal Pharma AG — Swissmedic (AIPS via AmiKo, GTIN 7680614310011) | texte_integral | 2024-03 |
| S21 | Information professionnelle suisse Vitarubine® Dépôt (hydroxocobalamine), Streuli Pharma AG — Swissmedic (AIPS via AmiKo, GTIN 7680335840026) | texte_integral | 2025-07 |
| S22 | Information professionnelle suisse Benerva® (thiamine), Farmaceutica Teofarma Suisse SA — Swissmedic (AIPS via AmiKo, GTIN 7680256360580) | texte_integral | 2019-04 |
| S23 | Information professionnelle suisse Glucophage® comprimés pelliculés (metformine), Merck (Schweiz) AG — Swissmedic (AIPS via AmiKo, GTIN 7680260610169) | section | 2025-10 |
| S24 | AVS 21 : âge de référence des femmes — Office fédéral des assurances sociales (OFAS) | section | consultée 2026-10-16 |
| S25 | Recherche AmiKo de l’indication suisse de BOTOX® (champ indication de la liste des spécialités) — Swissmedic (AIPS via AmiKo) | section | consultée 2026-10-16 |

## Tableau de bord

| Élément | Valeur |
|---|---|
| Leçon | G63 — Polynévrite au cours de maladies classées ailleurs (S08, N-05-Neurologie) |
| Catégories traitées | G63.0* à G63.8* ; frontière G62.0, G62.1, G62.2 |
| Fichiers audités | 7, empreintes conformes |
| Constats | 0 bloquant · 11 majeurs · 12 mineurs · 6 enrichissements |
| Sémiologie (rubrique 21) | absente : MAJEUR bloquant la clôture du cours et du lot ; proposition complète en 7 îlots |
| Disciplines des sciences | 4 réelles → proposition Immunologie (5e) |
| Figures | 6 schémas non anatomiques ; 3 illisibles à 390 px |
| Sources lues | 25 (8 FI suisses datées et 1 liste AmiKo, 4 documents suisses, 12 européens ou internationaux) |
| Propositions | 8 fichiers dans propositions/ |
| Alertes | Sources canoniques non modifiées ; aucune validation médicale humaine |
