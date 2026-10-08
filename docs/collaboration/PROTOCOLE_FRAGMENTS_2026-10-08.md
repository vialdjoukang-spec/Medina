# Production par fragment et audit croisé unique

Le 8 octobre 2026, Vial demande de prendre connaissance de `Prompt_Codex.pdf` et de continuer le travail. La demande de reprise lève l'arrêt Codex consigné plus tôt ; les règles du document joint deviennent les nouvelles consignes de production. Elles remplacent les dispositions incompatibles des règles administratives, des anciennes remises par chapitre et de l'injection autonome avant audit. Les preuves et les travaux antérieurs restent conservés.

## Périmètre et production

L'atlas comprend exactement **22 fragments**, organisés **Fragment → Catégories → Chapitres**. Les attributions déjà établies sont conservées dans [COORDINATION.md](../../COORDINATION.md) : dix fragments Codex, onze Claude, plus la cardiologie historiquement partagée. Aucun fragment n'est déclaré achevé du seul fait de son attribution, de son HTML distribué ou de la présence d'un cours.

Chaque responsable produit intégralement son fragment actif avant de le transmettre. La rédaction se poursuit chapitre par chapitre au sein de ce fragment, avec plusieurs sous-agents spécialisés et un auteur par fichier. Un chapitre achevé reste dans les sources de travail du fragment ; sa publication documentaire éventuelle ne constitue pas une demande d'audit final. Les anciens dépôts A41 et J45 sont conservés pour leur provenance, mais ne constituent pas une remise de fragment complet sous cette règle.

La complétude conserve la cible CIM-11 précédemment demandée. L'inventaire officiel versionné et la matrice d'enseignements spécifiques doivent être rapprochés des sources et des liens accessibles. Tant que cette preuve manque, la couverture reste **non établie** et le fragment poursuit sa production interne. Un catalogue historique CIM-10-GM ou un regroupement `covers` ne remplace pas cet inventaire.

## Rédaction et auto-revue

Rédiger en français clinique expert, dense, avec phrases complètes, mécanismes précis et limites d'application. Toute recommandation, donnée chiffrée ou posologie doit être appuyée sur une source vérifiable effectivement consultée, datée et adaptée à la population. Les mots interactifs ouvrent des explications contextualisées et leurs références. Conserver les quatre onglets, les classifications pertinentes, les quiz, les Pareto et le glossaire.

Lorsque **tout le fragment** est rédigé, son producteur conduit une auto-revue rigoureuse : exactitude clinique, cohérence entre surfaces, actualité des recommandations, intégrité et accessibilité des sources. Il corrige avant transmission et contrôle les HTML sur ordinateur et mobile. Les revues internes de sous-agents aident à cette étape ; elles ne constituent ni l'audit externe de Claude Code ni une validation médicale humaine.

## Audit croisé et injection

Un fragment complet et auto-revu est transmis sur un commit exact, avec inventaire de couverture, fichiers et empreintes, rapport interne, sources et contrôles. **Selon l'instruction Claude Leader plus récente, Codex remet ses cours à Claude, qui les corrige et les injecte ; Codex n'audite aucun cours Claude et n'injecte plus lui-même.** Le mécanisme d'audit croisé antérieur de ce protocole est remplacé sur ces points. Aucun fragment incomplet ni auto-audit ne vaut certification de complétude.

**Contexte suisse bloquant.** Appliquer le [contrat d'audit du contexte suisse](CONTRAT_AUDIT_CONTEXTE_SUISSE_2026-10-08.md) à toutes les décisions cliniques. Une prescription ou posologie doit être confrontée à la société savante suisse applicable et à la FI Swissmedic/Compendium du produit exact ; les textes européens et américains gardent leurs dates, leur population et leurs divergences, mais aucune recommandation américaine ne fonde la conduite finale. Claude refuse la remise Codex si la provenance ou la résolution clinique manque. La garde de `tools/espace.py` contrôle la preuve structurée liée aux empreintes lorsque la voie d'audit croisé passe par elle ; la chaîne interne Claude vérifie médicalement ses propres leçons avant injection.

L'audit et les corrections portent sur l'ensemble du fragment et la version finale effectivement injectée. Si une source ou un contrôle indispensable manque, l'auditeur consigne le blocage dans ce même tour et conserve la version non injectée ; il ne déclare pas favorable une vérification inachevée. Les anciens audits ciblés restent des preuves historiques, sans consommer le tour final d'un fragment qui n'a pas encore été remis complet.

Les états et preuves sont conservés dans [fragment_status.json](../../organisation/fragment_status.json). La garde `tools/espace.py garde <avant> <après>` protège les modifications canoniques et le registre. Les anciennes commandes de remise/audit/injection **par cours** sont désactivées sous ce protocole pour empêcher une injection partielle. La préparation de la remise finale devra utiliser un dossier de fragment entier et les preuves attendues par la garde ; aucun outil ne produit un verdict médical à la place de l'auditeur.

## Verrou et arrêt

Le statut **INJECTE (INJECTÉ à l'affichage)** est terminal. Les empreintes de toutes les sources du fragment et les preuves finales sont gelées : aucun moteur ne rouvre, n'enrichit ni ne corrige ce fragment après injection. Les demandes historiques de peaufinage et de nouveau dépôt après injection ne s'appliquent plus. Une injection historique d'un chapitre isolé ne suffit pas à attribuer ce statut au fragment entier.

Lorsque les **22 fragments** sont rédigés, auto-revus, audités et injectés avec leurs preuves, arrêter toute production et toute boucle de peaufinage ; publier uniquement le rapport de complétion. Le statut d'arrêt global ne peut être déduit d'un compteur de cours.

## Sortie

**HTML en thème clair exclusivement.** Aucun bouton, préférence enregistrée ou adaptation système ne doit activer un mode sombre. Les contrôles incluent un navigateur configuré avec une préférence système sombre et un ancien réglage sombre sauvegardé.
