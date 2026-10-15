# E10 — livraison d’auteur et d’intégration Alpha77

Cette livraison intègre les corrections médicales et linguistiques Alpha1, ajoute la sémiologie demandée et fournit les preuves locales. Ce document n’est ni un audit final MED/LANG/SEMIO, ni une clôture Alpha, ni une validation médicale humaine. Les audits finaux distincts restent au coordinateur.

La base de travail transmise est `3131a5cbf6cc003ead358e25152073959c53c4d9`, branche `codex/alpha77/e10-integrate-g1`, mission `ALPHA77-CODEX-E10-INTEGRATE`, génération 1. Le START_OK a été acquis par le coordinateur; aucune réacquisition n’a été effectuée. Les écritures finales se limitent aux sept sources E10, à un original iconographique dans le sous-dossier autorisé et à ce dossier de preuves.

## Corrections appliquées

Les 26 propositions LANG et les sept remplacements MED correspondant à M01–M05 ont été repris sans échec de correspondance. `reprise-propositions.json` contient leur texte exact; les rapports Alpha1 ne sont pas promus en audits de la version finale.

L’artériopathie n’est plus exclue par deux pouls et un index cheville-bras isolé. Le texte associe Doppler, index cheville-bras et index orteil-bras selon les recommandations 2 et 4 IWGDF/ESVS/SVS2023, relues. La présentation des tests neurologiques distingue également la filière suisse de plaie simple d’une exclusion universelle de neuropathie. L’urgence métabolique est recherchée immédiatement, et les formulations absolues sur symptômes digestifs et arrêt de toute cétogenèse ont été corrigées. Les unités de Tresiba ne sont pas converties lors d’un changement de concentration.

La réserve L01 sur l’insuline humaine soluble a été traitée par correction des surfaces actives. Les recherches AmiKo Actrapid et Insuman n’ont pas retourné de produit; la recherche Huminsulin a retourné uniquement la présentation Basal NPH. Aucun débit d’insuline humaine n’est donc prétendu vérifié par une FI suisse. Les débits 0,1/0,05 U/kg/h, l’incrément 1 U/h et la basale générique 0,25 U/kg ont été retirés du corps et de la fenêtre. Le cours conserve la physiologie, les objectifs de réponse biologique et leurs calculs, la surveillance du potassium/glucose, la continuité de couverture et la prescription hospitalière individualisée. La voie intraveineuse et les précautions de NovoRapid viennent de la FI exacte. Les exemples de repas/correction existants restent explicitement fictifs et individualisés. `correction-insuline-iv.json` documente les remplacements.

## Sémiologie et sciences

Le premier bouton local est «Sémiologie fondamentale et analytique», `e10-tab-semio`, sélectionné initialement; son panneau `e10-s-semio` est visible. Les neuf sections normal/signs/mechanisms/examination/interpretation/differentials/urgency/limits/sources relient normalité, mécanismes, symptômes, mesure, interprétation, différentiels et urgence. Le premier h3 reprend exactement l’intitulé imposé. Le marqueur clinique `data-semiology-clinical="E10"` se trouve dans A04, avec une analyse de la temporalité, des symptômes hyperglycémiques/hypoglycémiques et de leur gravité.

Le cours avait quatre sous-onglets scientifiques. Une histologie endocrine distincte complète les six boutons locaux avec la sémiologie. Les six panneaux dépassent 280 mots, possèdent une figure accessible sourcée et les quatre liens explicites Science→clinique/examen/traitement/À retenir. `current-sciences.json` fournit les mesures, sans altérer le test partagé.

## Sources et figures

`claim-mapping.json` contient 22 entrées d’assertions et passages, avec URL, éditeur, version, date, section, population et limites. Les trois FI réellement rouvertes sont NovoRapid 100 U/mL (avril 2026, autorisations 55045/55046/55712/65630), Tresiba (décembre 2024, 62562/62563) et Baqsimi 3 mg nasal (mars 2026, 67465). Leurs voies, doses pertinentes, précautions et populations ne sont pas interchangeables.

Les normes Viollier glucose, peptideC, sodium, potassium, osmolalité et bicarbonates, ainsi que la gazométrie La Source ont été rouvertes. Le peptideC Viollier est une référence à jeun; il ne faut pas la confondre avec le prélèvement non à jeun conditionnel NICE. Les glyphes≥ du PDF diagnostique SSED 2011 ont été inspectés visuellement sur la première page; l’extraction textuelle seule perd leur barre. Le tableau professionnel 3 et la page 13 des recommandations suisses de conduite 2025 ont été relus. La discordance texte/tableau du premier groupe déjà signalée n’a pas été arbitrairement effacée.

Figure 6 : l’original LibreTexts, version 2022, correspond octet pour octet à l’asset existant; licence et crédit de la micrographie 2012 lus, image ouverte. Figure 8 : le nouvel asset est l’original de la publication 2021; son MD5 correspond exactement au MD5 indiqué dans le XML primaire. La licence inclut les figures sauf crédit contraire, absent de la légende de cette figure; l’original a été ouvert. Figure 9 : la publication 2025 et sa licence ont été lues, mais aucune preuve de méthode de création n’a été trouvée. L’image anatomique a été retirée de toutes les surfaces actives et remplacée par un diagramme décisionnel sans anatomie, fondé sur NICE 1.1.4–1.1.6 et 1.1.10. Aucun redessin anatomique n’a été produit. Voir `figures-provenance.json` et `figure8-original-acquisition.json`.

Les documents scientifiques complets téléchargés restent hors dépôt dans `/workspace/scratch/E10-integrate-sources`; le dépôt ne reçoit que les passages nécessaires et leurs empreintes. Les pages PMC de challenge ne sont pas présentées comme lues; les XML EuropePMC ont servi de source intégrale alternative. Le catalogue de recherche Alpha1 a été conservé avec attribution historique explicite.

## Matrice de complétude et réserves

«Couvert» décrit les éléments vérifiés ou corrigés, pas une certification exhaustive de chaque phrase héritée.

| Rubrique | État de cette intégration | Surface ou preuve |
|---|---|---|
|1 Question clinique et enjeu fédéral|Couvert, mapping éditorial non officiel|pA A01/A04; pS sémiologie|
|2 Définition et périmètre CIM|LACUNE : édition OFS applicable et détail des modificateurs non révalidés|A02; annexe Alpha1 attribuée|
|3 Classifications et stades|Aigu couvert; LACUNE sur stades présymptomatiques|A02/A06; e10-semio-interpretation|
|4 Épidémiologie|LACUNE : chiffre suisse spécifique type 1 non établi; tous-types non assimilé au type 1|A02|
|5 Normal→pathologique|Noyau sémiologique renforcé; pas revalidation ligne par ligne de toute biochimie/immunologie héritée|pS six panneaux|
|6 Étiologies et risques|Classification révisable et diagnostics alternatifs|A02/A03; e10-semio-differentials|
|7 Anamnèse et symptômes|Couvert sans fréquence inventée|A04; e10-semio-signs|
|8 Examen|Couvert; limites des tests pied corrigées|A04/A09/A10; e10-semio-examination|
|9 Urgences|Couvert pour passages consultés, cadres adulte nommés|A06/A07; e10-semio-urgency|
|10 Examens|Normes citées rouvertes; matrices et questions distinguées|E01/E02; claim-mapping NORM-*|
|11 Différentiels|Renforcé et discriminants explicités|A04; e10-semio-differentials|
|12 Prise en charge|Trois FI exactes; débits insuline humaine non étayés retirés|A06; pP P01/P02; correction-insuline-iv.json|
|13 Complications|Corrections vasculaires/neurologiques/digestives appliquées|A09/A10; S01; fenêtres concernées|
|14 Suivi et dépistage|LACUNE : ancien cadre suisse 2017 et échéancier complet non révalidés ici|A09/A11; E03|
|15 Situations particulières|FI et limites adulte/enfant/grossesse/rein explicites|A08; P01/P02; e10-semio-limits|
|16 Spécificités suisses|Conduite professionnelle relue; LACUNE remboursement 2026 et discordance premier groupe conservée|A11; e10-a11-conduite|
|17 Diagnostic formel|Glyphes du PDF 2011 résolus; LACUNE confirmation asymptomatique par directive suisse actuelle|A04/A12; e10-semio-interpretation|
|18 Paramètres clés|Normes et objectifs distincts; calculs biologiques conservés|E02/E03; A12; fenêtres|
|19 Sous-codes CIM|LACUNE administrative, pas de tableau CIM ajouté au cours|Annexe Alpha1, sans prétendre couverture OFS 2026|
|20 Examen fédéral|Trois quiz existants préservés; LACUNE enrichissement autonome SSP162/lipides|E03; A01/A04; graphe éditorial hérité|

Un avis visible sous le titre indique exactement : « Révision Alpha en cours : certaines réserves thérapeutiques et sources héritées restent à vérifier ; les audits finaux de cette version ne sont pas clos. » Les réserves substantielles restantes sont celles explicitement marquées LACUNE dans cette matrice. La revalidation indépendante de toutes les assertions et images historiques inchangées n’est pas revendiquée. Aucune note 20/20, conformité suisse finale ou validation humaine n’est attribuée.

## Vérifications et remise

La porte `betta_verite.py` a affiché VÉRITÉ OK avant la rédaction des nouveaux contenus, puis en sortie. Les33remplacements hérités avaient été adoptés avant cette porte; cette chronologie est conservée et n’est pas présentée comme un contrôle préalable rétroactif de ces remplacements. Le build S05 et `test_v7.py` ont été exécutés sur les sources de ce worktree. Le test partagé `audit_sciences.py` échoue avant tout examen courant parce que E10 n’existe pas à sa base historique fixe; `audit-sciences.log` conserve cet échec. Aucun test partagé n’a été modifié. Les mêmes prédicats portant sur la source courante sont appliqués par `make-evidence.py` et passent.

Les contrôles navigateur et leurs captures réelles portent sur 1360×950 et 390×844, les six sélections, la sélection initiale, Entrée/Espace, police 24 px, mode Livre et une fenêtre explicative. Ils ne revendiquent pas une navigation par flèches/Home/End. Les résultats définitifs se trouvent dans `test-v7.log` et `browser-check.json`. `source-verification.json` contrôle identifiants uniques, neuf marqueurs, six panneaux, disparition de l’ancienne image 9 et des débits non étayés. `source-files.json` associe les sources et leurs copies de remise sous `delivery/`, sans auto-référence d’empreinte.

Audit différé — revue IA, distincte d’une validation médicale humaine. Cette livraison d’auteur reste destinée aux audits finaux distincts et à une publication Alpha provisoire si le coordinateur retient ce statut; elle ne clôture pas le cours.

Résultats de sortie sur les sources finales : build S05 réussi; `test_v7.py` navigateur **OK**; prédicats sciences courants **passed**; vérification source/snapshots **8/8 identiques**; `git diff --check` sans erreur. Le cours contient 35210 mots selon le compteur du test; 106 fenêtres, 3 quiz et 21 Pareto; ses six fichiers HTML occupent 362251 octets. Ces nombres décrivent le contenu et ne constituent pas une note médicale.
