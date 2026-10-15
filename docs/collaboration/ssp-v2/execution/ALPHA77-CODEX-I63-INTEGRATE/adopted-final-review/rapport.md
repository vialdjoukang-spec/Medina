# I63 — revue finale indépendante médicale et sémiologique

Revue Codex, mission déjà acquise `ALPHA1-CODEX-I63-MED`, génération 1. Auteur distinct : `ALPHA77-CODEX-I63-INTEGRATE`. Version effectivement relue : **34838433bd52571ee1c674d97ff28d6f27debbac** ; base de comparaison : `3131a5cbf6cc003ead358e25152073959c53c4d9`. Aucune validation médicale humaine.

**MED : provisional. SEMIO : closed, uniquement pour l’exigence `fundamental_analytical_semiology`.** Les réserves thérapeutiques et les sources primaires héritées incomplètement contrôlées empêchent de clore l’ensemble médical. La clôture sémiologique ne les efface pas. Aucun nouveau problème médical urgent démontré dans les passages effectivement contrôlés.

La réserve réellement visible sous l’en-tête du cours est conservée exactement dans le JSON MED :

> Révision Alpha en cours : certaines réserves thérapeutiques et sources héritées restent à vérifier ; les audits finaux de cette version ne sont pas clos.

## Méthode et version

Les sept fichiers centraux ont été lus intégralement : texte clinique et scientifique des six HTML, tableaux, toutes les fenêtres, questions et réponses commentées, et glossaire Python. L’extraction conserve les contenus des templates ; les nombreuses citations répétées sont regroupées dans l’inventaire des références. Les images encodées sont traitées comme octets et contrôlées visuellement selon le périmètre décrit, pas comme prose. La présence d’une URL dans le cours ne signifie jamais que son texte externe a été lu. `sources-read.json` contient uniquement les sources et passages effectivement relus pour cette revue.

Les huit empreintes finales (sept fichiers et Gray516.png) ont été calculées depuis `git show 34838433:chemin`, comparées aux fichiers gelés et au manifeste candidat : huit concordances. Les sept empreintes `source_files_sha256` des deux rapports sont calculées depuis la base 3131a ; `reviewed_files_sha256` décrit la version finale exacte. Le champ `source_commit` du manifeste auteur précède le gel ; cette différence de métadonnée ne remplace pas le contrôle des octets, qui concordent.

Les rapports MED/LANG antérieurs ont été relus et confrontés aux deltas, sans rejouer un audit inchangé. Les anciens rapports restent intacts. Les lectures externes nouvelles sont des lectures indépendantes ciblées d’originaux conservés dans le cache auteur, avec attribution de ce téléchargement. Le supplément HINTS a été téléchargé indépendamment pendant cette revue. Les empreintes et localisations des passages sont consignées ; aucun PDF, texte complet ou HTML externe n’est recopié dans ce dépôt.

## Anciens constats et réserves

- **M01 et M02 résolus** : syndrome vestibulaire aigu avec nystagmus, formation de l’examinateur, limites d’un HIT périphérique dans AICA et attribution des sensibilités 84,0 → 95,7 % au sous-groupe AICA. Source Tarnutzer 2025 effectivement lue, y compris le supplément tableau S1 pour les techniques.
- **M04 résolu** : exception SAPL triple positif avec préférence AVK, et limite de l’extrapolation des données de thrombose hors système nerveux central, concordantes avec la recommandation S2k 2024 lue.
- **M05 résolu après rectification de l’interprétation antérieure** : le PDF bernois comporte deux pages imprimées par page physique. La page physique 31 porte bien le mRS imprimé p. 61 ; la page physique 32 porte le NIHSS détaillé imprimé p. 62–63. Les p. 66/68 sont des versions synthétiques supplémentaires. Le renvoi 61/62–63 n’était donc pas une erreur démontrée.
- **M06 résolu** : 40/40/20 % est attribué à la cardioembolie *isolée*, avec restriction explicite de l’interprétation individuelle. Le passage de Hoyer et son tableau 1 ont été lus.
- **FIG-P1 résolu pour la nouvelle figure** : l’ancien dessin anatomique IA est remplacé par le PNG original Gray516, 116 061 octets, SHA-256 `2db08331119d6817654aa3b3f507835f675e8e10e7f700cf1cf208dd815a61cf`. La page primaire Commons et ses rubriques Summary/Book/Licensing ont été lues : Henry Vandyke Carter, Gray, édition 1918, planche 516, reproduction mécanique d’un original du domaine public. Inspection indépendante : vue inférieure, artères en rouge, basilaire/vertébrales, parties temporale et cérébelleuse réséquées à droite de l’image. Pas de carte individuelle d’occlusion. Les droits de toutes les figures héritées ne sont pas déclarés nouvellement revérifiés.
- **M03 reste ouvert** : la lecture supplémentaire du texte et du tableau 11 ESO pression 2026, de la recommandation DAPT 2021 et de passages des sept FI suisses exactes réduit la réserve, mais ne valide pas toutes les décisions héritées. Le seuil implantable >6 min est retrouvé dans le protocole bernois ; la confrontation complète à ESC 2024 n’a pas été faite. Les textes intégraux ESO IVT 2021 et prévention longue 2022 n’ont pas été relus ici. Ce constat est une limite de couverture, pas une preuve que chaque passage concerné est faux.
- **Lacunes de matrice maintenues** : OFS/BfArM, PROFILES primaire, épidémiologie, références biologiques suisses, sources expérimentales et diverses spécificités suisses restent partiellement ou non contrôlés.

Les corrections LANG ont été confrontées au texte : retrait de l’exclusivité injustifiée de l’installation brutale et négation Actilyse corrigée. Il ne s’agit pas d’un audit LANG final. L’assertion expérimentale Fabry n’est pas nouvellement validée, car sa source primaire n’a pas été relue. Le libellé FLAIR reste lourd malgré son explication contextuelle.

Un renvoi bibliographique reste imprécis, sans modifier les conseils cliniques : le tableau détaillé des erreurs de Tarnutzer est le tableau 2 ; le cours cite plusieurs fois le tableau 1, mais les sections et les passages pertinents sont identifiables. Constat SEMIO non bloquant conservé.

## Couverture des vingt rubriques

« Partielle » signifie que le cours a été lu mais que toutes ses assertions n’ont pas été confrontées à un primaire applicable. La rubrique sémiologique peut être satisfaite sans que l’ensemble de la physiopathologie ou du traitement soit validé.

| Rubrique | Couverture de cette revue et limite |
|---|---|
| 1. Question clinique et enjeu de l’examen fédéral | Reconnaissance et orientation confrontées au triage national suisse ; rattachement fédéral primaire non validé. |
| 2. Définition et périmètre CIM-10-GM | Texte lu ; libellés et inclusions/exclusions OFS/BfArM non relus. Partielle. |
| 3. Classifications et stades | Scores NIHSS/mRS détaillés contrôlés dans le PDF ; catégories étiologiques et classifications administratives non toutes revalidées. |
| 4. Épidémiologie suisse/européenne | Chiffres hérités lus ; primaires épidémiologiques non rouverts. Lacune. |
| 5. Normal → pathologique | Normalité, territoires et mécanismes sémiologiques confrontés à Berne/Hoyer et supplément HINTS ; sources expérimentales de toute la physiopathologie non relues. |
| 6. Étiologies et facteurs de risque | Nuance de cardioembolie isolée et mécanismes postérieurs contrôlés ; fréquences et causes rares partiellement vérifiées. |
| 7. Anamnèse et symptômes | Dernier état habituel, témoin, état antérieur, traitements, temporalité et signes d’alarme vérifiés ; fréquences de chaque symptôme non validées. |
| 8. Examen clinique | Exigence sémiologique vérifiée : normalité, technique NIHSS, HINTS formé/AVS+nystagmus, AICA, audition et stabilité, limites du score. Les performances de tout autre signe ne sont pas exhaustivement revalidées. |
| 9. Drapeaux rouges et urgences | Triage suisse et régression des signes contrôlés ; ensemble des gestes, complications et contre-indications thérapeutiques non couvert exhaustivement. |
| 10. Examens complémentaires | Pièges CT/DWI postérieurs et concordance clinique vérifiés ; toutes normes biologiques locales/Analytica non relues. |
| 11. Diagnostic différentiel | Tableau vestibulaire et distinction déclencheur/aggravation vérifiés ; ensemble des diagnostics concurrents et fréquences restent partiels. |
| 12. Prise en charge suisse et FI | Sept FI exactes relues par passages, doses clés et distinctions notice/protocole contrôlées ; toutes clauses, interactions et décisions cliniques non revérifiées intégralement. M03 ouvert. |
| 13. Complications et pronostic | Présentation lue, risques FI ciblés ; toutes assertions de pronostic et prise en charge des complications non confrontées. |
| 14. Suivi, prévention, dépistage | DAPT 21 jours, population, dose de charge et différence de cadre FI vérifiées ; prévention longue et anticoagulation après épisodes implantables restent partielles. |
| 15. Situations particulières | Exception SAPL/CVT contrôlée ; grossesse, enfant et autres situations vérifiés seulement aux passages FI ciblés. |
| 16. Spécificités suisses | Orientation 144 et distinction protocole bernois/national vérifiées ; OFSP, Suva, conduite, AI, LS/LiMA non contrôlés exhaustivement. |
| 17. Critères formels du diagnostic | Concordance signes/imagerie et absence de valeur d’exclusion d’un NIHSS faible vérifiées ; pas de revalidation normative exhaustive. |
| 18. Paramètres chiffrés | Poids/volumes Metalyse, dose Actilyse, critères de dose apixaban, DAPT et pression ciblés ; ensemble des chiffres hérités non revalidé. |
| 19. Sous-codes CIM-10-GM | Texte lu, primaires OFS/BfArM non consultés dans cette revue. Lacune. |
| 20. PROFILES/SSP | Situations de départ et raisonnement lus ; primaire PROFILES et identifiants non revalidés. Lacune. |

## Verdict sémiologique et contrôle réel du frontend

Les neuf rubriques du premier sous-onglet scientifique sont substantielles : normalité, signes et temporalité, mécanismes, examen, interprétation, différentiels, urgence, limites suisses, sources. La clinique pA et les fenêtres ne sont pas remplacées par des titres. Les fonctions normales et gestes NIHSS sont contrôlés dans Berne imprimé p. 4 et 62–63 ; les associations topographiques dans Hoyer tableau 1 ; la technique VOR/HIT, nystagmus, skew et audition dans Tarnutzer supplément tableau S1 ; l’urgence dans le texte national suisse p. 323. Les limites sont explicites et aucune prescription n’est déduite de ce seul onglet.

Build neuf exécuté en scratch depuis la source gelée, puis Chromium réel : desktop 1440 et mobile 390, premier onglet actif, six boutons scientifiques, neuf rubriques, activation native Enter/Space et visibilité exclusive, fenêtre HINTS réellement ouverte, mode livre à 24 px, aucun identifiant dupliqué, aucune erreur JavaScript, aucune largeur excédant le viewport. Défilement mobile vérifié jusqu’aux dernières sources : 17426 + 760 = 18186 px. Captures réellement obtenues, dont desktop sémiologie et mobile livre 24, inspectées visuellement. La mise en page mobile reste dense au grand corps, mais le texte est accessible par défilement.

L’essai de lecture de `window.MC_GLOSS` renvoie `null` pour HINTS et aucun global GLOSS : il ne prouve donc pas la définition effectivement consommée par tous les raccourcis du glossaire partagé. Le glossaire local a été lu ; la fenêtre HINTS propre au cours a été ouverte et son texte vérifié dans le navigateur. Aucune couverture du moteur global n’est déduite de cet essai.

## Livrables et contrôles de périmètre

`audit-final-medical.json` et `audit-final-semiologie.json` portent chacun les empreintes de base et de sortie exactes. Les preuves propres de cette revue sont sous `final-review-34838433/` : sources et passages lus, méthode, inventaire des renvois, résultats navigateur/défilement et captures. Les deux JSON sont aussi copiés dans `/workspace/scratch/i63-final-audits/` pour l’intégrateur. Aucun fichier source I63, métadonnée du cours, fichier partagé, rapport antérieur, reçu de publication ou branche source n’est modifié. Ce commit est un livrable d’audit ; il ne publie ni ne fusionne le cours.
