# G45 — audit croisé, passe 1

**Avis défavorable : 14/20.** Revue IA, sans validation médicale humaine.

Entrée réelle : 2026-10-14T00:24:32.412938+00:00. Clôture : 2026-10-14T00:44:57.341500+00:00.

21 parties, 126 sous-parties, 69 fenêtres, glossaire, tableaux et 21 quiz relus ; 30 contrôles numériques ; neuf figures inspectées. Les fichiers auteur sont restés gelés.

## Corrections bloquantes

- **R1 — majeure_medicale** : Les exclusions d’Aspirine Cardio omettent les maladies inflammatoires intestinales et l’insuffisance cardiaque sévère. Elles restent absentes de toutes les surfaces, malgré une monographie censée guider la sécurité du produit.
  Correction attendue : Enseigner ces contre-indications du produit exact avec définitions/liens utiles, vérifier cohérence monographie/corps/tableau et renouveler ledger. Ne pas les transformer en contre-indication universelle de toute forme/dose d’aspirine.
  Localisation : `chapters/G45/G45_pop2.html::template[data-pop="g45-aspirine"]; chapters/G45/G45_d.html#g45-p02-partie-2`.

- **R2 — majeure_medicale** : Sortis : cholestase et association glécaprévir/pibrentasvir sont absentes des exclusions. Les douleurs/faiblesses musculaires appellent une évaluation dans le texte, mais l’arrêt immédiat en cas de myopathie suspectée/diagnostiquée ou d’élévation significative des CPK n’est pas enseigné.
  Correction attendue : Ajouter les exclusions pertinentes exactes et la conduite d’arrêt immédiat dans les conditions de la FI ; distinguer simple myalgie à évaluer de myopathie suspectée. Définir cholestase/CPK et documenter l’association contre-indiquée, sans nouveau seuil arbitraire.
  Localisation : `chapters/G45/G45_pop2.html::template[data-pop="g45-sortis"]; chapters/G45/G45_d.html#g45-p02-partie-2; #g45-p02-partie-3`.

- **R3 — majeure_medicale** : La monographie ne traite pas le syndrome des antiphospholipides avec antécédent thrombotique, pour lequel la FI déconseille les anticoagulants oraux directs, surtout en triple positivité. La conduite devant hémorragie majeure reste une décision générique d’interruption, sans indiquer l’arrêt prévu par la FI.
  Correction attendue : Ajouter la non-recommandation dans cette population et l’arrêt en cas d’hémorragie majeure, avec évaluation urgente et renvoi aux mesures spécialisées sans improviser une réversion. Garder distinctes contre-indication formelle et emploi non recommandé.
  Localisation : `chapters/G45/G45_pop2.html::template[data-pop="g45-eliquis"]; chapters/G45/G45_d.html#g45-p02-partie-3`.

- **R4 — moderee_scientifique** : La fenêtre dit « TXA2 le thromboxane A2 et ses récepteurs », confondant ligand et récepteur. Le dessin porte TBXA2 et TBXA2R distincts, ainsi que TBXAS1,F2/F2R,ADCY3,GNAS,IP3,P2RY1/P2RX1 non expliqués ; la légende promet pourtant les abréviations explicitées.
  Correction attendue : Distinguer explicitement molécule, récepteur et enzyme ; compléter une lecture guidée sourcée des symboles utiles et les correspondances exactes du dessin, ou choisir une figure publiée moins complexe. Ne pas développer les symboles de mémoire ; garder l’image publiée intacte.
  Localisation : `chapters/G45/G45_pop2.html::template[data-pop="g45-plaquette"]; chapters/G45/G45_c.html#g45-s03-partie-3; glossary/g45.py`.

- **R5 — moderee_pedagogique** : La relation débit=gradient/résistance est donnée sans unité de résistance ni exemple chiffré refaisable. L’explication des limites est bonne mais le calcul demandé depuis les bases reste incomplet.
  Correction attendue : Ajouter variables et unités cohérentes, un exemple explicitement fictif ou adimensionnel, étapes et effet d’un changement de résistance, sans valeur prétendue normale ni cible de soin. Fournir le passage exact qui étaye la relation.
  Localisation : `chapters/G45/G45_pop1.html::template[data-pop="g45-perfusion"]; chapters/G45/G45_c.html#g45-s02-partie-1`.

- **R6 — moderee_completude** : La discussion des sténoses reste générale : le seuil≥50% de la fenêtre concerne surtout l’imputabilité, sans enseigner la branche d’intervention >50% du tableau bernois ni le délai « within a few days ». Le cahier demande critères,bénéfices et risques, pas seulement renvoi spécialisé.
  Correction attendue : Compléter la conduite attribuée à Berne, différence imputabilité/indication, temporalité et principaux éléments arbitrant chirurgie/stenting. Conserver décision multidisciplinaire et exceptions ; ne pas importer un seuil ou délai d’une autre recommandation sans lecture.
  Localisation : `chapters/G45/G45_b.html#g45-a10-partie-3; chapters/G45/G45_pop1.html::template[data-pop="g45-carotide"]`.

## Observations complémentaires

M1 : crédit du traducteur Petit B. M2 : lien reperfusion/perfusion. M3 : arrondi EXPRESS (8,19 points avec fractions non arrondies).

La matrice suisse indépendante est réservée. A09 remplit le parcours AIT par son texte ; l’algorithme AVC aigu est un complément de transport explicitement limité. Les neuf agrandissements fonctionnent dans l’aperçu sous forme d’images cliquables.

Le détail des sources, passages, calculs, images et empreintes se trouve dans `pass1.json` et les inventaires adjacents. Attente du signal de correction, puis passe 2 indépendante.
