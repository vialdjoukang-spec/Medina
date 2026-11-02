# N29 — Autres affections du rein et de l’uretère au cours de maladies classées ailleurs

Reprise du cours existant, branche `codex/alpha77/n29-integrate-g1`, base `8a512893acbab9caa0dcfdd0e8682a44ea72fda6`. Travail limité aux chemins de la mission N29 ; aucune PR, fusion main ou modification du moteur partagé.

Ouvrir [l’aperçu natif autonome](N29-apercu-autonome.html). Les octets des quatre images originales sont incorporés sans modification, pour huit occurrences. Les autres cours présents dans la navigation héritée ne font pas partie de cette livraison.

Le cours conserve les développements existants et corrige les affirmations identifiées : performances urinaires de tuberculose, chirurgie individualisée, interprétation des cohortes de schistosomiase, distinction syphilis tardive/tertiaire, bénéfice très précoce de la cystéamine, doses et précautions des produits suisses. Les six disciplines scientifiques comprennent une sémiologie de neuf sections. Le plan clinique précède l’annexe administrative.

- [Plan de 14 points et matrice de 20 rubriques](lesson-manifest.json), avec ancres et sources précises.
- [Registre des sources](source-ledger.json) : 31 lectures ciblées ; neuf FI suisses exactes, un RCP français explicitement étranger ; références héritées conservées par pointeur, avec attribution à Claude.
- [Provenance, droits et annotations des figures](figures-rights.json).
- [Constats initiaux](findings-initial.json) et [corrections relues](findings-final.json).
- [Tests statiques](test-static.txt), [audit des sciences](audit-sciences.json), [contrôle navigateur](browser-report.json), [liaison aux sources finales](source-binding.json).
- [Auto-relecture médicale](reviews/medical.json), [linguistique](reviews/language.json), [ordinateur](reviews/visual_desktop.json), [mobile](reviews/visual_mobile.json).
- Captures : [ouverture ordinateur](captures/N29-1440-opening.png), [fenêtre mobile](captures/N29-390-popup.png), [anatomie rénale annotée](captures/N29-1440-original-kidney.png), [néphron mobile](captures/N29-390-original-nephron.png), [histologie réelle annotée](captures/N29-1440-original-schisto.png), [pelvis féminin annoté](captures/N29-390-original-bladder.png).

Le navigateur utilise une origine HTTP interceptée servant la copie native ; toutes les autres requêtes sont bloquées. Les images sont mesurées après défilement et décodage. Le test vérifie aussi la position absolue des annotations dans l’image, six onglets scientifiques, neuf sections sémiologiques, les fenêtres, Livre 24 px et l’absence de débordement horizontal. Aucun déploiement public n’est revendiqué. Un premier passage fonctionnel avait laissé passer une altération du CSS ; l’inspection visuelle l’a révélée, la correction et le contrôle géométrique ont précédé le reçu final.

Les revues sont des **auto-relectures IA**, pas des audits indépendants ni une validation clinique humaine. Les limites demeurent : absence de données rénales suisses déductibles des statistiques générales ; sémiologie spécifique de la gomme rénale tertiaire non documentée dans les recommandations consultées ; accès suisse au praziquantel à confirmer ; indométacine pédiatrique internationale non assimilable à la capsule retard suisse ; divergences de recommandations et FI explicitement conservées. Les passages hérités ne sont pas présentés comme intégralement relus dans leurs sources primaires.

Le bandeau natif peut ajouter « contre-audit restant » et afficher des compteurs hérités du système partagé. Ces éléments ne sont pas recalculés par cette livraison et ne remplacent pas les statuts de revue du manifeste. La correspondance PROFILES utilise explicitement l’édition 2017 ; ni la classification CIM ni les exercices originaux ne sont déclarés questions fédérales officielles.

Les scripts du dossier conservent les étapes de travail. Les sources canoniques finales et leurs empreintes font foi ; les anciens scripts de reprise depuis la base ne doivent pas être relancés isolément sur une version finalisée. Les sources intégrales et extraits de travail restent dans le cache externe. Mesures réelles de tokens et coût : non disponibles, laissées nulles.
