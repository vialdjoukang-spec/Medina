# G01 — intégration du 15 octobre 2026

Livraison d’auteur/intégrateur, provisoire et réservée. Ce rapport n’est ni un audit final MED/LANG/SEMIO indépendant, ni une validation médicale humaine, ni une clôture Alpha. L’avis visible demandé par le coordinateur est présent sous l’en-tête : « Révision Alpha en cours : certaines réserves thérapeutiques et sources héritées restent à vérifier ; les audits finaux de cette version ne sont pas clos. »

Mission : `ALPHA77-CODEX-G01-INTEGRATE`, génération 1. Branche : `codex/alpha77/g01-integrate-g1`. Base effective propre : `3131a5cbf6cc003ead358e25152073959c53c4d9`. START_OK transmis par le coordinateur après acquire/start ; réservation distante `caa932507a8046f036e77adc1f7055f3c4203276`. Le transport n’a pas sauvegardé le JSON start local : aucun reçu original local n’est revendiqué. L’attestation transmise et le reçu central de lancement de la PR146 sont les références du coordinateur.

## Travail intégré

Les audits `ALPHA1-CODEX-G01-MED` et `ALPHA1-CODEX-G01-LANG` sont adoptés avec attribution. Les six copies médicales proposées ont servi de point de départ et les 21 substitutions linguistiques ont été appliquées. Les rapports historiques ne sont pas promus en audits finaux de cette version.

- Ponction : séparation des critères d’imagerie et des autres contre-indications, dont coagulation/anticoagulation ; aucun retard du traitement pour l’imagerie.
- Listériose : suppression de l’arrêt automatique et de la contre-indication de dexaméthasone déduits d’une seule cohorte ; présentation des données observationnelles contradictoires de MONALISA et de la cohorte néerlandaise de 2023. Le rapport HR 0,54, dont le comparateur n’a pas été recontrôlé, est retiré sans invention d’un comparateur.
- Neuroborréliose : conjonction des anomalies inflammatoires, prérequis complets avant confirmation, index persistant distingué d’une infection active. Doxycycline : recommandation pédiatrique distincte des restrictions de la FI suisse. Dexaméthasone : schémas pondéraux de la FI attribués aux enfants/adolescents.
- Vignette immunodéprimée : distinction du schéma communautaire sans immunosuppression. FI exactes de Vancomycine Sandoz et Meronem : doses, perfusions, rein, surveillance, valproate et expérience adulte très limitée de Meronem.
- Tuberculose : lecture réussie du guide suisse auparavant inaccessible. FI de Rifater et Myambutol : limites des doses fixes dans l’atteinte du système nerveux central et surveillance hépatique, rénale et visuelle. La FI de l’aciclovir injectable est également lue.
- Prophylaxie : distinction entre la fiche cantonale et l’indication du produit. La prophylaxie méningococcique n’est pas retrouvée dans la FI Ciproxine consultée. La règle de grossesse est attribuée à la fiche cantonale. La vaccination B post-exposition automatique non établie par une source suisse directement lue n’est plus enseignée.
- Seuils : unité mg/L rétablie pour la concentration minimale inhibitrice. Le tableau 1 du référentiel indique des protéines virales inférieures à 100 mg/dL : la fausse mention « non précisé » est corrigée. La contradiction interne entre la prose et le tableau de la source sur les protéines bactériennes est tracée ; le tableau explicite est retenu, sans inventer d’erratum.

## Sémiologie et figures

Le premier bouton de pS est « Sémiologie fondamentale et analytique », sélectionné et visible initialement. Ses identifiants et attributs ARIA concordent. Les neuf sections contiennent 1 382 mots, un schéma causal non anatomique et des références reliées aux observations et décisions. La clinique de pA comporte un enrichissement sourcé : état habituel, gêne cervicale, antipyrétiques, peau, conjonctives et signes qui changent la séquence des examens.

Les six disciplines scientifiques dépassent chacune 280 mots, possèdent une figure accessible et les quatre liens pédagogiques exigés. Leurs mesures exactes figurent dans `sciences-local.json`.

La figure 3 anatomique d’origine IA est remplacée par l’original intégral de la planche 1196 de Carter/Gray, édition 1918. `figure3-provenance.json` documente page propre à cette figure, original, droits, dates, attribution et inspection visuelle. Le PNG reste inchangé ; légendes anglaises conservées, termes utiles traduits dans la légende française. Le dossier assets contient uniquement le PNG, utilisé à travers une image SVG accessible. La copie d’assets du workflow existant dessert ce chemin relatif ; aucun moteur ni workflow partagé n’est modifié.

L’inventaire final comporte huit figures : un original anatomique et sept représentations causales ou comparatives non anatomiques. L’inspection par intelligence artificielle ne vaut pas validation médicale humaine.

## Preuves et contrôles

`sources.json` distingue lectures nouvelles et références historiques seulement adoptées. `retrieval.json` donne consultations et empreintes. `claim-mapping.json` relie les enrichissements aux passages ciblés. `passages-med-adoptes.json` conserve les extraits de la mission précédente. Aucun document médical intégral n’est copié dans le dépôt.

La porte Betta passe à l’entrée puis à la sortie avec une matrice conservatoire de vingt rubriques et les lacunes explicites. Elle contrôle une structure de traçabilité, sans certifier la médecine.

Le test partagé `tests/audit_sciences.py --codes G01` échoue avant ses assertions : G01 n’existait pas à sa base historique `c50a28…`. Sortie originale conservée. `check-sciences.py` importe ce test inchangé et remplace seulement BASE par la base effective `3131a…` ; toutes ses assertions sont conservées et passent. Ce résultat n’est pas présenté comme la réussite du test original.

Le frontend S08 est construit avec les sources finales et servi localement. Les contrôles statique, natif `test_v7.py` et spécifique des six sous-onglets passent. `browser-semiology.json` documente ordinateur 1360 × 960 et mobile 390 × 844 : sélection exclusive, neuf sections, Entrée/Espace natifs, Navigo, identifiants uniques, décodage du PNG, fenêtres, police 24 px et mode Livre. Les captures sont réelles. Un premier essai avait recherché une chaîne interrompue par les césures conditionnelles du moteur ; sa sortie est conservée. Le test final identifie le contenu médical sans dépendre de ces césures.

## Réserves pour les audits finaux

1. Le texte de neurosyphilis 2020 indique une validité jusqu’au 30 avril 2025. La limite est explicite ; aucune nouvelle recommandation 2026 n’est revendiquée. La stratégie actualisée demande encore une évaluation indépendante.
2. Agents rares, certaines données épidémiologiques et références historiques lues seulement au résumé ne sont pas exhaustivement revalidés ici. Le texte complet de physiopathologie 2011 n’a pas pu être rouvert. Les mécanismes nouveaux reposent sur la revue européenne accessible de 2024, sans transposition de traitements expérimentaux.
3. PDF OFSP post-exposition et page de déclaration : HTTP 503. Fiche cantonale et page générale OFSP lues ; délais légaux et éventuelle règle nationale B post-exposition non confirmée restent réservés. Aucun intervalle normal suisse du liquide n’est inventé.
4. Les FI consultées et leurs restrictions principales ne constituent pas une revue exhaustive de toutes les contre-indications, interactions, adaptations et options rares du cours historique. La divergence recommandation/FI reste à examiner produit par produit.
5. Le test sciences original reste bloqué par sa base ; une correction du test partagé exige une mission distincte. Aucune garde n’est modifiée.

Les audits finaux indépendants, la décision de publication, le contrôle public et le reçu Alpha restent au coordinateur. Aucun reçu `completed`, aucun audit final fictif et aucune clôture de cours ou de lot ne sont créés. `final-manifest.json` associe les preuves aux empreintes des sources finales.
