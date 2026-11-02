# C86 — version à examiner, 2 novembre 2026

La monographie des autres lymphomes T/NK spécifiés a été révisée sur sa branche exclusive. Elle est présentable pour examen utilisateur ; aucune PR vers main et aucune validation médicale humaine ne sont annoncées.

## Livraison

- [Aperçu autonome dans le lecteur Medina](C86-apercu-autonome.html) : images originales intégrées, légendes françaises reliant les lettres et flèches originales à leur interprétation.
- [Couverture des quatorze points](monograph-14.json) et [vingt rubriques](matrix-20.json), distinctes d’une note de qualité.
- [Passages réellement lus](recherche_C86/sources.json), [sources historiques conservées](recherche_C86/inherited-sources.json), [provenance des images](images-provenance.json).
- [Contrôles reproductibles](verify_c86.py), [résultat](verification.json), [navigation réelle](browser-report-autonomous.json), [empreintes finales](source-binding.json).

## Mesures

26,786 mots selon le comptage du texte sans balises template, 52 fenêtres, cinq quiz, quatorze synthèses Pareto, six disciplines scientifiques et neuf sections sémiologiques. La base comparable comptait 17 641 mots, 49 fenêtres, cinq quiz et quatre disciplines ; aucune image médicale originale n’y était intégrée. Le volume ne constitue pas une mesure de qualité.

31 lectures ciblées documentées, dont trois FI suisses exactes. Deux figures originales humaines CC BY 4.0 sont intégrées dans quatre occurrences ; deux diagrammes causaux non anatomiques complètent la biochimie et la génétique. 28 captures générées, 14 inspectées visuellement ; dimensions 1440×900 et390×844, Livre24, toutes les fenêtres et cinq quiz exercés dans chaque viewport. Coût réel et tokens : non exposés, donc non chiffrés.

## Corrections médicales déterminantes

Sept sous-codes ne signifient pas sept maladies : BPDCN est de lignée dendritique ; C86.6 inclut LyP et pcALCL. Les critères ENKTL, TFH et BPDCN sont intégrés au tissu et au contexte. Les risques thiopurines gardent leur population masculine de moins de35ans et ne sont ni annuels ni une instruction d’arrêt automatique après deux ans.

RCD-II, EATL et MEITL sont distingués ; les seuils de cytométrie, la durée du régime et les exclusions sont explicités. Le HLH peut nécessiter traitement des organes, du déclencheur et de l’hyperinflammation en parallèle. Le SPTCL sans HLH peut relever d’une immunosuppression ; son différentiel lupique est documenté.

L’allogreffe peut être précoce dans HSTL/BPDCN ; l’autogreffe EATL ne demande pas de donneur. ENKTL : radiothérapie seule possible dans certaines situations localisées, DeVIC sans asparaginase, doses Oncaspar de LLA distinctes des protocoles ENKTL. Adcetris : indication cutanée exacte, G-CSF, bléomycine contre-indiquée et adaptations neurologiques par schéma. Elzonris : seuil initial d’albumine distinct des seuils sous traitement et dénominateurs de sécurité225/89 séparés.

## Portée et limites

Les quatre dimensions de revue sont déclarées en auto-relecture par le même auteur, conformément au mode autorisé. Elles ne sont pas des audits indépendants. Les séries sélectionnées, le résumé Gayden, les repères HUG2019 et les limites de remboursement2026 sont nommés. La classification et le codage2024 ne certifient pas toutes les règles administratives2026.

Le navigateur a exercé une origine HTTP interceptée, avec réseau externe bloqué. L’ouverture réelle file:// est interdite par la politique administrateur et n’a pas été prétendue testée. Les captures longues peuvent inclure les barres flottantes natives ; les pixels des originaux restent inchangés. Le bandeau historique « Publication provisoire : contre-audit restant » et les compteurs globaux hérités ne sont pas les indicateurs du harness de cette campagne.

## Reproduction

Depuis le worktree, avec les dépendances Medina et Chromium installés : `python3 docs/collaboration/ssp-v2/execution/ALPHA77-CODEX-C86-INTEGRATE/verify_c86.py`. Ce script reconstruit et vérifie ; il ne publie pas et ne réalise aucune revue médicale. Une modification des sources invalide les empreintes et exige de renouveler les preuves affectées.
