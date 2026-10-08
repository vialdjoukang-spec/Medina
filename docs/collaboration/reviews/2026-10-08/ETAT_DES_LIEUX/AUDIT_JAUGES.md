# Audit indépendant des jauges — état des lieux du 8 octobre 2026

**Les jauges défendables mesurent une attribution, un renvoi de catalogue ou des étapes documentées. Elles ne mesurent pas le pourcentage de travail médical achevé.** La complétude CIM-11 reste **non établie** ; les fragments certifiés sont **0/11 pour Claude et 0/10 pour Codex**.

Instantané lu : `HEAD` local `e434eac491c14e8c348aeff606d113350df5026b`, avec injection locale supplémentaire de **I83 — Varices des membres inférieurs (C-01-Cardiologie)** depuis Claude `6d5797c6a902e430cd9d3e9dd5159ec507a1476a`. L'injection et les contrôles canoniques sont documentés ; la publication est en cours selon le coordinateur. Le présent contrôle n'établit pas lui-même un push ou un déploiement. Actualiser ces deux états après leurs preuves distantes, sans attribuer rétroactivement cette vérification à cet audit.

## Mesures pour les responsables

| Mesure | Claude | Codex | Sens exact |
| --- | --- | --- | --- |
| Fragments entiers attribués | **11/21 — 52,38 %** | **10/21 — 47,62 %** | Répartition des 21 fragments hors C-01-Cardiologie, pas progression. |
| Fragments certifiés CIM-11 dans la file | **0/11** | **0/10** | Compte de certifications documentées, pas pourcentage de couverture des entités. |
| Complétude des entités CIM-11 | **Non établie** | **Non établie** | Inventaire officiel attendu et matrice de preuves non validés. |
| Chapitre de la file déclaré actif dans le plan | Aucun nouveau chapitre déclaré | **A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie)**, étape `review` | L'absence de déclaration dans la file de Claude ne signifie pas inactivité : son chapitre cardiologique est traité séparément. |
| Activité cardiologique de reprise | I83, remise et corrections | Audit croisé et intégration d'I83 | Backlog distinct des 21 fragments attribués ; cette réception n'ouvre pas une deuxième production Codex. |

**Ne pas répartir à nouveau les catégories entre les IA ni attribuer à leur responsable actuel la paternité des cours historiques.** L'attribution porte sur les fragments entiers. Les totaux du catalogue par fragment décrivent l'existant, indépendamment de l'auteur qui l'a constitué.

Le plan indique **24 missions spécialisées prévues**, organisées en vagues, et **six sous-agents au maximum simultanément**, plus le coordinateur. Ce sont un nombre de missions et une capacité ; aucun de ces nombres ne mesure les agents effectivement actifs à un instant donné ni un taux d'achèvement des missions. Pour montrer une mobilisation réelle, utiliser les rapports de postes et journaux effectivement présents.

## Jauge historique des fragments : renvois du catalogue

Sources recalculées en lecture seule : `organisation/fragments.json`, `fragments.json`, `chapters.json` et le JSON `medora-data` de `shell/medina_front.html`. La règle de rattachement explicite, puis par système, a été confrontée à `tools/build_organisation.py`, sans exécuter cet outil.

**Formule proposée :** nombre de catégories historiques du fragment ayant un code dans le `covers` d'un cours marqué `integrated`, divisé par nombre de catégories historiques rattachées au fragment. Libellé conseillé : **« Catégories avec un renvoi déclaré vers un cours — catalogue historique CIM-10-GM 2024 »**. Cette mesure ne garantit ni le passage spécifique, ni la maîtrise médicale, ni le contrôle de toutes les sous-catégories ; elle ne certifie pas la CIM-11.

| Fragment entier | Responsable de la file | Cours présents localement | Renvois déclarés / catégories historiques | Pourcentage de renvois |
| --- | --- | ---: | ---: | ---: |
| C-01-Cardiologie | Backlog hors répartition | 21 | 58/77 | 75,32 % |
| P-02-Pneumologie | Claude | 5 | 13/64 | 20,31 % |
| I-03-Infectiologie | Codex | 1 | 1/155 | 0,65 % |
| G-04-Gastroentérologie et hépatologie | Claude | 0 | 0/102 | 0 % |
| N-05-Neurologie | Codex | 0 | 0/120 | 0 % |
| E-06-Endocrinologie et métabolisme | Claude | 0 | 0/77 | 0 % |
| N-07-Néphrologie | Codex | 0 | 0/27 | 0 % |
| H-08-Hématologie | Claude | 0 | 0/44 | 0 % |
| O-09-Oncologie, génétique médicale et soins palliatifs | Codex | 0 | 0/54 | 0 % |
| G-10-Gynécologie et sénologie | Claude | 0 | 0/50 | 0 % |
| O-11-Obstétrique et néonatologie | Codex | 0 | 0/134 | 0 % |
| M-12-Médecine des âges de la vie | Claude | 0 | 0/0 | **N/D** |
| I-13-Immunologie et allergologie | Codex | 4 | 8/13 | 61,54 % |
| R-14-Rhumatologie et orthopédie | Claude | 1 | 3/155 | 1,94 % |
| U-15-Urologie et andrologie | Codex | 0 | 0/52 | 0 % |
| D-16-Dermatologie | Codex | 0 | 0/89 | 0 % |
| O-17-Oto-rhino-laryngologie et médecine bucco-dentaire | Claude | 0 | 0/80 | 0 % |
| O-18-Ophtalmologie | Claude | 0 | 0/56 | 0 % |
| M-19-Médecine d’urgence, traumatologie et toxicologie | Claude | 0 | 0/152 | 0 % |
| D-20-Diagnostic clinique et examens complémentaires | Codex | 0 | 0/0 | **N/D** |
| M-21-Médecine de premier recours et santé publique | Codex | 0 | 0/135 | 0 % |
| E-22-Éthique médicale, droit et communication | Claude | 0 | 0/0 | **N/D** |

**N/D** signifie « aucune catégorie propre dans ce catalogue historique ». Ce n'est ni 0 %, ni 100 %, ni une dispense d'enseignement : ces axes conservent leur périmètre pédagogique transversal à inventorier. Ne pas leur fabriquer un dénominateur CIM-11.

Les cours partagés restent attachés à leur fragment canonique. Par exemple, le renvoi de **M30 — Périartérite noueuse et affections apparentées (R-14-Rhumatologie et orthopédie)** vers **M31 — Autres vasculopathies nécrosantes (I-13-Immunologie et allergologie)** ne déplace pas la catégorie : le numérateur compte le renvoi dans le fragment de la catégorie, et le compteur des cours compte une seule source primaire dans son fragment.

### Totaux locaux et instantané antérieur

| État du catalogue | Cours marqués intégrés | Catégories avec renvoi déclaré | Jauge historique globale |
| --- | ---: | ---: | ---: |
| Sources au commit `e434eac` avant injection | 31 | 81/1 636 | 4,95 % |
| Sources locales après injection I83 | 32 | 83/1 636 | 5,07 % |

L'ajout apporte **un cours et deux codes de renvoi déclarés**. La catégorie associée **I87 — Autres atteintes veineuses (C-01-Cardiologie)** demeure partiellement traitée ; `covers` ne transforme pas ses sous-catégories non développées en enseignements certifiés. Les deux lignes sont des instantanés de sources ; ne pas appeler la seconde « site publié » avant vérification distante.

## Cycle majeur documenté : I83

La liste suivante contient huit **jalons de suivi** définis pour ce rapport. Ils ne sont pas de même durée ni de même effort. Une frise à cases est préférable à une jauge « X % du chapitre terminé ».

| Jalon | État à l'instantané | Preuve consultée |
| --- | --- | --- |
| 1. Remise source repérée et reçue | Documenté | Reçus successifs de PR #12, inventaire du dossier `I83_DECISION_0974D85` ; source finale `6d5797c`. |
| 2. Périmètre, provenance et empreintes établis | Documenté | `INVENTAIRE_TECHNIQUE.json`, inventaires et deltas techniques des têtes effectivement lues. |
| 3. Audit croisé des quatre onglets et contenus associés | Documenté avec limites de sources | `AUDIT_PATHOLOGIE_EXAMENS.md`, `AUDIT_SCIENCES.md`, `AUDIT_PHARMACOLOGIE.md` et deltas. Lecture déclarée de tous les panneaux/fenêtres dans leurs périmètres ; certaines sources externes restent non téléchargées. |
| 4. Réserves de prescription ciblées corrigées et contrevérifiées | Documenté | Anciennes contre-indication polidocanol et EHIT III corrigées ; PH-01/PH-02 et procédure intra-artérielle closes par les rapports Pharmacologie, dont `DELTA_6D5797C_PHARMACOLOGIE.md`. Les remarques mineures restent visibles. |
| 5. Injection sélective dans les sources canoniques locales | Documenté | `INJECTION_LOCALE_6D5797C.json` : dix fichiers et entrée du catalogue, `local_injection_only: true`, `published: false` à cet instantané. |
| 6. Reconstruction et contrôles du canonique injecté | Documenté, réussis | `CONTROLES_CANONIQUES_6D5797C.md`, commandes et résultats `6D5797C_*_CANONIQUES.json` ; 118 tests unitaires, 1 923 assertions natives, 72 contrôles S01, 41 assertions des routes. |
| 7. Publication Git et reçu d'intégration distant vérifiés | En cours / preuve finale à ajouter | Les preuves locales ne donnent pas encore le SHA d'intégration publié et vérifié. Mettre à jour après lecture du commit distant et du reçu. |
| 8. Déploiement du site et accès aux routes publiées vérifiés | En attente de preuve | Succès CI Pages au SHA publié et ouverture de l'artefact/site de ce SHA, puis routes du chapitre. La réussite locale ou un push ne suffisent pas. |

On peut afficher **« 6 jalons documentés, 2 vérifications de publication restantes »** pour cet instantané. **Ne pas afficher « 75 % terminé »** : cela transformerait une checklist choisie en estimation de travail ou de qualité. Une mise à jour distante peut modifier les deux dernières cases sans modifier les conclusions médicales déjà bornées à leur SHA.

L'ancien `DECISION.md` à `20bee19` conserve légitimement un blocage historique. Pour l'état actuel, lire les contrelectures ultérieures à `20c67c0` et `6d5797c`, puis la preuve d'injection. Le dernier reçu de réception seul n'est pas le reçu final d'intégration ; aucune réserve d'autres chapitres ESC n'est réputée fermée par l'injection de ce chapitre.

## Cycle actif Codex : A41 et ses réserves

Chapitre : **A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie)**. Audit Claude de la base `39b7ff0cc585c59ffbb99fb448940daa1950b34d` reçu et archivé dans `livraisons/Livraison Claude/I-03-Infectiologie/archives/AUDIT_A41_39B7FF0_RECU_20261007_5BEE2A4/`. Lecture des trois JSON et recomptage de leurs observations, sans nouvelle certification de leur contenu médical :

| Périmètre | Majeures | Mineures | Rédactionnelles | Total d'observations |
| --- | ---: | ---: | ---: | ---: |
| Pathologie 1 | 0 | 18 | 9 | 27 |
| Pathologie 2 | 2 | 10 | 4 | 16 |
| Examens, Sciences, Pharmacologie | 8 | 18 | 6 | 32 |
| **Total** | **10** | **46** | **19** | **75** |

Les JSON ne classent aucune observation comme « erreur médicale bloquante », mais leur conclusion indique que **les dix majeures empêchent l'injection des corrections tant qu'elles ne sont pas traitées et contrevérifiées**. Ne pas transformer le compteur nul d'une classe de gravité en feu vert. Présenter « 10 réserves majeures à traiter » et les deux autres compteurs séparément, sans pourcentages d'effort.

Les **dix fichiers canoniques** de `chapters/A41/` et `glossary/a41.py` ont été comparés octet pour octet à cette base ; **aucun n'a changé** à l'instantané de cette relecture. Aucune clôture par correction n'est donc déduite de la présence de nouvelles métadonnées ou des contrôles logiciels. Un point majeur est clos uniquement avec correction localisée, nouveau SHA et contrelecture concernée ; un examen argumenté peut aussi documenter un autre arbitrage, sans effacer l'observation initiale.

Le plan conserve `claude_a41_request.status: posted_acknowledgement_pending`, alors que l'audit de base reçu est déjà archivé. Pour le tableau utilisateur, présenter **« inventaire effectué ; audit de base reçu ; corrections et réaudit à conduire »**, et conserver séparément l'état d'un éventuel nouvel accusé. Ce contrôle n'autorise pas une nouvelle injection d'A41.

## Contrôles de cohérence réalisés et recommandations au tableau

1. **Répartition :** 21 identifiants distincts, file Claude de 11 et file Codex de 10, disjointes, union égale aux 22 fragments du registre moins S01. Tous les fragments, y compris les trois axes sans catégorie historique propre, sont attribués une seule fois.
2. **Rattachements :** 1 636 codes historiques distincts, tous rattachés une fois ; aucune catégorie perdue ou déplacée par les renvois. Aucun conflit entre sources primaires de `covers`, aucun code déclaré hors catalogue dans cet instantané.
3. **Sommes :** 21 + 5 + 1 + 4 + 1 = 32 cours présents dans les cinq fragments concernés ; 58 + 13 + 1 + 8 + 3 = 83 renvois déclarés. Les dénominateurs des 22 fragments totalisent 1 636. L'ajout d'I83 explique seul le passage 31→32 et 81→83.
4. **Divisions nulles :** les axes T2, T5, T7 ont un dénominateur historique nul. Afficher N/D et un texte explicatif ; ne pas convertir le résultat en 0 % ou 100 %.
5. **A41 :** les trois JSON donnent exactement 10 majeures, 46 mineures et 19 rédactionnelles ; même SHA examiné dans les trois rapports ; somme égale au rapport Markdown et à `INVENTAIRE_AUDIT_A41.json`.
6. **I83 :** source finale, injection locale et contrôles canoniques portent `6d5797c` ; les six commandes consignées de contrôle ont un code de sortie zéro. Les anciennes copies de simulation et leurs compteurs restent attribués à leur SHA propre.
7. **Publication :** afficher les états local / dépôt publié / site déployé séparément, avec un SHA complet et un lien de preuve pour chacun. Recalculer les compteurs après publication, sans interpréter une sortie HTML locale comme disponibilité distante.
8. **Complétude :** appliquer `docs/COMPLETUDE_CIM11.md` : couverture CIM-11 « non établie » tant que l'inventaire n'est pas validé. Le nombre de certifications 0/11 ou 0/10 peut être affiché, mais pas une jauge de couverture CIM-11 à 0 % qui suggérerait un dénominateur connu d'entités.
9. **Lisibilité :** titres séparés « Attribution des fragments », « Renvois du catalogue historique », « Jalons de livraison », « Réserves ouvertes ». Aucune fusion en un score global d'IA ; une même couleur de succès logiciel ne doit pas suggérer la clôture médicale.

Seul ce rapport a été écrit par ce poste. Aucun code, plan, catalogue, source canonique ou objet Git n'a été modifié ; aucune nouvelle publication ou exécution de tests du projet n'a été effectuée dans cet audit.
