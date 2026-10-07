# Justifications et organisation MEDINA — 7 octobre 2026

## Livré

- **31 cours intégrés**, dont le nouveau **J40 — Bronchite**, couvrant J20, J40, J41 et J42 en conservant leurs aspects propres.
- **197 fenêtres supplémentaires**, reliées à 197 passages explicites dans les quinze cours attribués à Codex. Chaque fenêtre contient un mécanisme causal, sa conséquence clinique et des références ; une rubrique de limites apparaît lorsqu’un contexte supplémentaire est nécessaire.
- Dans **I50 — Insuffisance cardiaque**, le tableau du bilan biologique ouvre directement les explications sur l’anémie, le sodium et le potassium. Les explications distinguent mécanisme, interprétation et conséquence pratique.
- L’audit systématique de **I50 — Insuffisance cardiaque** a conduit à 54 corrections ciblées dans neuf sources, notamment sur les biomarqueurs, l’échographie et les critères cliniques. Son dossier partagé recense 99 groupes de constats : six corrigés sur le point ciblé, sept partiellement traités et 86 ouverts. Ces groupes ne représentent pas un décompte exhaustif de toutes les affirmations du cours.
- Organisation injectée dans les **22 plateformes originales** : catégories et chapitres numérotés, couleurs contrastées, code discret dans le coin supérieur droit, regroupements et renvois. Les **1 636 catégories CIM-10-GM 2024** sont conservées dans 265 blocs.
- Instruction transmise au véritable Claude dans la [PR #10](https://github.com/vialdjoukang-spec/Medina/pull/10#issuecomment-6041361558). Répartition définitive : quinze cours chacun, détaillée dans `docs/collaboration/MECHANISMS_PLAN.json` et `MISSION_JUSTIFICATION_2026-10-07.md`.
- Livraison Claude reçue sur la tête **be6a909059200711493064bd9c96a7437d71c019** : 27 sources injectées après vérification des empreintes, puis corrections médicales ciblées documentées. Sa proposition de mission, PR #11, est conservée intégralement dans les archives ; la mission commune reprend la répartition définitive.
- Nouvelle livraison réelle de Claude, **PR #12, tête b1f19c3510c1a828650867da033ebe2fbf30142e** : huit sources de **I48 — Fibrillation et flutter auriculaires**, glossaire et rapports reçus. Les copies originales restent intactes ; les canoniques ont été contre-corrigés sur le rythme, l’anticoagulation, la portée des études et certains mécanismes. Les 100 fenêtres natives sont accessibles.
- Au point **b6db50cb2911fcbe0b09e64b79df03aab294e3df**, le paquet Claude contient 85 propositions dont **77 nouvelles sources de huit cours** : I00 — Rhumatisme articulaire aigu ; I30 — Péricardites, épanchement péricardique, tamponnade et constriction ; I33 — Endocardite infectieuse ; I34 — Valvulopathies mitrales, tricuspides et pulmonaires ; I35 — Valvulopathies aortiques ; I40 — Myocardites ; I42 — Cardiomyopathies ; I44 — Troubles de la conduction et bradycardies. Ces 77 sources sont injectées après contrelecture ciblée : 17 HTML ont reçu des corrections médicales et huit en-têtes ont conservé le statut de révision. Les quatre propositions de fenêtres I48 — Fibrillation et flutter auriculaires apportent uniquement des corrections bibliographiques, fusionnées sans remplacer les arbitrages médicaux. Le snapshot original des 85 sources est conservé séparément.
- **Neuf des quinze cours attribués à Claude ont une remise reçue et intégrée dans le premier checkpoint publié f149128**, I48 — Fibrillation et flutter auriculaires compris. Au checkpoint suivant **8ce3e99**, les six autres cours ont une nouvelle proposition : I47 — Tachycardies paroxystiques supraventriculaires et ventriculaires ; I49 — Extrasystoles et autres arythmies ; I46 — Arrêt cardiaque ; Q21 — Cardiopathies congénitales de l’adulte ; I71 — Anévrismes et dissections artérielles ; I80 — Thrombose veineuse profonde et thromboses veineuses. Leur réception et leur contrelecture contrôlées sont distinctes du premier checkpoint. Une remise ne certifie pas la justification exhaustive de chaque affirmation.
- **Les quinze remises Claude sont désormais reçues et intégrées après contrelecture ciblée.** Le snapshot 8ce conserve 132 propositions exactes : 79 identiques au point b6, 51 sources des six cours supplémentaires et deux nouvelles versions de fenêtres I48. L'injection de 53 HTML préserve les statuts et la prose locale. Les deux rapports de contrelecture consignent **159 substitutions médicales ou bibliographiques** dans 41 copies adaptées. Deux harmonisations cliniques I48, trois ajustements de libellés et le seul paragraphe TBX1 du glossaire sont traités séparément. Les anciens manifestes et tous les originaux restent conservés ; aucun fichier de travail brut n'est assimilé à une livraison.
- Le complément d’outillage Claude à la tête **0755710** est archivé sans exécution. Les chemins de travail bruts restent des brouillons ; ils ne sont pas injectés comme cours achevés. L'intégration des propositions déclarées au point b6 est distincte de ces fichiers de travail.
- L’injection accepte désormais les nouveaux HTML/JSON explicitement déclarés, dont les banques `CODE_justifications.json`. Absence et empreintes sont recontrôlées ; aucune collision n’est écrasée. Les banques des cours touchés compilent avant le reçu ; un échec provoque le retour arrière.

## Contrôles réalisés

| Contrôle | Résultat | Portée |
|---|---:|---|
| Tests unitaires | 83 réussis | Compilation, empreintes, chemins, créations et retour arrière, construction atomique, routage et frontières des termes du glossaire |
| Audit statique des sigles | 31 cours réussis | Les termes connus restent reconnus dans les mots verts ; les composants inconnus restent signalés. Le rendu S01 est identique avant/après cette correction de l'auditeur |
| Fenêtres interactives | 2 310 contrôles réussis, aucune erreur JavaScript | Les 197 ajouts sur ordinateur ; les 21 fenêtres I50 sur mobile ; les 40 fenêtres et six synthèses Pareto de J40 sur les deux écrans ; liens de références, Escape, focus et retour imbriqué |
| Fenêtres natives I48 | 5 951 contrôles réussis, aucune erreur JavaScript | À chaque viewport : 206 mots verts, 15 synthèses Pareto, 35 boutons imbriqués, 100 fenêtres ; citations, Escape, focus, Retour et largeur mobile |
| Huit nouveaux cours Claude | 24 582 contrôles réussis, aucune erreur JavaScript | 717 gabarits canoniques, tous ouverts sur ordinateur et mobile ; liens, fermeture, focus, retour imbriqué et largeur |
| Six derniers cours Claude | 15 470 contrôles réussis, aucune erreur JavaScript | Tous les déclencheurs et toutes les fenêtres canoniques sur ordinateur et mobile ; texte complet, liens de sources, fermeture, focus, retours imbriqués et largeur |
| Fenêtres natives I50 | 2 894 contrôles réussis, aucune erreur JavaScript | 114 déclencheurs par écran, 88 fenêtres dont 21 ajouts ; 130 navigations de références, Escape, focus et retour du glossaire imbriqué |
| Catégories originales | 656 contrôles réussis | Les 22 fragments, conservation du catalogue, contrastes et navigation |
| Vérification pulmonaire | 55 contrôles réussis | Bronchite et renvois respiratoires |
| Sciences et sémiologie CS | 609 contrôles réussis | 31 cours, onglets, figures et interfaces CS dans cinq fragments |
| Tableau d’organisation | 740 contrôles réussis | 22 fragments, 265 blocs, 1 636 catégories et 31 cours |
| Construction des fragments | 22 réussis | Validité JavaScript et reproductibilité |

Ces résultats sont des contrôles techniques. Ils ne constituent pas une validation médicale indépendante de toutes les affirmations. Les URL des premières références des banques ont été réellement ouvertes sous observation ; les pages distantes n’ont pas été téléchargées par le test navigateur. Les preuves détaillées sont dans les sous-dossiers `browser_recovery`, `categories`, `sciences_cs` et dans `organisation`.

Après l'injection 8ce, une seconde campagne de **22 686 contrôles navigateur** réussit : les six derniers cours, les 100 fenêtres I48, l'interface des sciences et l'organisation des 22 plateformes. Les 83 tests unitaires, l'audit statique explicite des 31 cours et la reconstruction reproductible passent aussi. Les preuves de cette campagne sont dans `audits/MECANISMES_2026-10-08`. Ces nombres incluent des vérifications répétées entre campagnes ; ils ne comptent pas des assertions médicales indépendantes.

La protection des mots verts empêche désormais un sigle interne de détourner le clic vers le glossaire. Les liens de références sont également protégés : leur libellé ouvre la source. L’audit de construction vérifie la présence de l’organisation et de sa navigation dans chacun des 22 fragments.

## Travail restant explicitement ouvert

**La relecture exhaustive de toutes les affirmations des trente cours antérieurs n’est pas terminée.** Les quatre onglets, tableaux, fenêtres anciennes, figures, légendes, quiz, Pareto et glossaires restent inclus dans cette mission. Aucune leçon ancienne n’est déclarée achevée au seul motif qu’une banque de nouvelles fenêtres existe. Les trente statuts restent `pending_exhaustive_review` dans le plan.

**La complétude CIM-11 n’est pas établie.** Le catalogue réellement présent utilise CIM-10-GM 2024. Il faut retrouver le fichier primitif de Medina, choisir une version CIM-11 précise et rapprocher toutes ses catégories avant de certifier une couverture internationale complète. Une conservation exhaustive du catalogue local ne remplace pas cette comparaison.

Les corrections I48, I10, I42, M31 et T78 sont ciblées et sourcées dans les rapports associés. Les réserves pédagogiques sur certaines figures héritées restent ouvertes ; elles ne sont pas masquées par les tests réussis.

Le dossier I50 est disponible dans `livraisons/Livraison Codex/C-01-Cardiologie/audits/2026-10-07/I50-Insuffisance-cardiaque`. Les anciens scores automatiques et les anciens indicateurs d’achèvement ont été remplacés par le statut actuel de révision dans les 17 en-têtes concernés.
