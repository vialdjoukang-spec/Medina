# I-03-Infectiologie — progression interne du 8 octobre 2026

Le premier des dix fragments Codex reste **I-03-Infectiologie (T1)**. Ce dossier prépare deux cours dans son frontend de travail local : **A41 — Sepsis et choc septique de l’adulte** et **B24 — Infection par le VIH et maladie à VIH de l’adulte**. Les sources canoniques historiques sont conservées. La police est Atkinson Hyperlegible Next, alignée sur celle retenue par Claude ; l’aperçu réutilise le frontend clair de la spécialité.

## Rédaction et revue ciblée

A41 a reçu les précisions de Sepsis-3, des populations Phoenix, du bicarbonate et du qSOFA, ainsi que celles du codage R65, du consensus de choc réfractaire, de la gentamicine et de la mortalité observée à 29,9 %. Les corrections historiques de Claude restent présentes. Les preuves et les limites de ce contrôle ciblé sont dans `preuves/cloture_interne_A41.json` et les rapports associés.

B24 comporte les quatre onglets, six sous-onglets scientifiques, des schémas, des fenêtres explicatives, neuf quiz, cinq synthèses Pareto et son glossaire. Quatre auteurs possèdent chacun un panneau et ses fenêtres ; une relecture indépendante porte sur l’ensemble assemblé. Le cas pédagogique reste borné aux faits explicitement donnés et distingue les exemples hypothétiques des résultats réels du cas.

Les textes distinguent les dates propres des recommandations NIH, EACS et des notices suisses. Ils utilisent la directive OFSP 2025, version 4 du 10 juillet 2026, et les pages NIH effectivement révisées le 24 septembre 2026 lorsqu’elles s’appliquent. Le régime quotidien de prophylaxie PJP NIH reste séparé des trois prises hebdomadaires de la notice suisse. Les notices complètes non accessibles et les interfaces non consultées sont déclarées dans les registres de sources ; elles ne sont pas présentées comme vérifiées.

Les rapports et empreintes sous `preuves/` décrivent une **revue interne ciblée**, sans validation médicale humaine ni audit croisé final. La dérivation des sources communes est répartie entre les panneaux ; les mécanismes s’appuient sur des travaux primaires distincts.

## Accès et contrôles techniques

Routes prévues après publication : [aperçu B24](https://vialdjoukang-spec.github.io/Medina/apercus/infectiologie.html#/entry/B24) et [aperçu A41](https://vialdjoukang-spec.github.io/Medina/apercus/infectiologie.html#/entry/A41). Ces routes sont vérifiées après déploiement ; le paquet B24 est une version de travail interne.

Le constructeur vérifie le manifeste des sources puis compile une copie temporaire. Il conserve strictement les catégories T1, ouvre uniquement les deux cours déclarés, utilise un espace de carnet de travail et n’affiche aucune certification finale. Le glossaire interne est appliqué après les dictionnaires historiques pour conserver les définitions infectiologiques. Les fichiers médicaux canoniques ne sont pas écrits.

Les **168 tests Python** et **223 contrôles de structure** locaux passent. Les 19 sources déclarées concordent avec les empreintes du manifeste. Le navigateur local étant bloqué par les restrictions de sockets du conteneur, le workflow Pages est préparé pour exécuter les contrôles interactifs sur ordinateur et mobile **avant le déploiement**, avec Python 3.12 et Playwright 1.55.0. Il conservera les résultats et captures dans l’artefact `controle-cours-infectiologie`, puis dans [le rapport technique prévu](https://vialdjoukang-spec.github.io/Medina/apercus/controle/browser-proof.json). Un échec empêchera la publication ; les captures ne seront pas une validation clinique.

**État avant le réglage : les contrôles navigateur n’avaient pas été exécutés.** La tentative de publication GitHub du 8 octobre 2026 à 19:55 Europe/Zurich a été refusée avant création de l’arbre : `MCP tool call requires approval, but approval policy is never`. Aucun objet, commit ou déplacement de branche distant n’a été effectué. Le contenu, l’aperçu HTML et les contrôles sont sauvegardés localement ; les liens B24 et les nouvelles captures ne sont pas encore disponibles en ligne. La preuve de ce blocage est conservée dans `preuves/technique/publication-bloquee.json`.

## Couverture et suite

Le catalogue frontend actuel comprend **184 catégories dans 24 blocs**. Ce chiffre est distinct de l’inventaire pédagogique CIM-11 à établir. Le dossier `inventaire/` conserve le catalogue local, le candidat OMS MMS 2026-01 français et une matrice non certifiée. L’équivalence `B24 → 1C62.1` de la table OMS n’est pas appliquée automatiquement au titre pédagogique VIH adulte.

**Le fragment reste EN_PRODUCTION, incomplet, non transmis pour audit final et non injecté.** B24 poursuit son contrôle interne ; la priorité suivante du même fragment sera B18 selon le registre. Le seul audit croisé final par Claude concernera le fragment entier, après sa rédaction et son auto-revue complète.


## Reprise de publication après le réglage

Le 08/10/2026 à 20:21 Europe/Zurich, l’accès complet aux fichiers et au réseau est confirmé. Le navigateur réel passe **2223 contrôles, sans échec**, sur ordinateur et mobile, avec les 161 fenêtres ouvertes aux deux largeurs, les quiz, les quatre panneaux de chaque cours, les sous-onglets scientifiques, les préférences du lecteur et Navigo. Les sources restent inchangées et leurs 19 empreintes concordent. La preuve locale est `preuves/technique/browser-proof-local.json`. Les deux défauts du script de contrôle ont été corrigés : clic sur le rectangle réellement peint d’un mot multiligne et prise en compte du plan Navigo permanent sur grand écran. Le moteur, les polices et le contenu médical ne sont pas modifiés par ces corrections.

La publication reprend par Git depuis le commit local `79d8ece8ed8742da6c753e02080caa7904486d02`. Le refus GitHub initial reste conservé comme événement historique. Le workflow Pages doit encore réussir avant que les nouvelles routes et captures soient annoncées comme disponibles. Cette reprise ne vaut ni complétude du fragment, ni audit croisé final, ni injection canonique.


## Captures directement visibles

La publication `3527a78f3efbd09a95dd22ba036c76f58ff7f750` est vérifiée : workflow Pages 37823748880 réussi, 2 223 contrôles navigateur sans échec, quatre panneaux B24 réellement ouverts sur le site public. Les nouvelles captures sont présentées dans les messages du chat. Sur la demande directe de Vial, le workflow génère aussi une animation réelle des quatre onglets et d’une fenêtre explicative. Les cinq PNG originales sont conservées ; le script `tools/build_preview_capture_animation.py` produit une GIF en boucle, cinq secondes par vue. Cette animation enregistrée est actualisée à chaque publication réussie ; elle ne constitue ni une diffusion vidéo en direct, ni une validation médicale.

Chemin public de l’animation : `apercus/controle/b24-apercu-anime.gif`. Le premier smoke réel comporte cinq vues 1440 × 1000 avec Atkinson et le réglage de lecture à 19 px ; sa provenance est dans `preuves/technique/animation-initiale.json`. Les captures CI possèdent leur propre date et leur propre empreinte dans `apercus/controle/b24-animation.json`.

## Retouche ciblée de B24 après retour du lecteur

Le passage sur les stades CDC/OMS et le codage B24 est reformulé en français clinique direct. Six autres phrases maladroites du même panneau sont clarifiées, dont la priorité de stabilisation d’une urgence. L’onglet Examens reçoit un troisième quiz sur l’interprétation d’un test immunologique négatif en présence d’un déficit immunitaire profond. Les faits de M. L., les liens et les fenêtres explicatives restent inchangés. Le détail des empreintes et des sources figure dans `preuves/retouche-b24-2026-10-08.md` ; les anciennes empreintes de relecture demeurent un instantané historique.

Le nouvel aperçu local compile avec les 19 empreintes exactes. **168 tests Python et 2 229 contrôles navigateur ordinateur/mobile passent, sans échec** ; le contrôle navigateur couvre les 161 fenêtres A41/B24 et les neuf quiz B24. Une nouvelle capture dédiée montre exactement la section révisée et l’animation conserve les cinq vues réelles. Ce sont des contrôles internes d’une version de travail, sans revue médicale humaine ni audit final du fragment.

## Progression de B18 — Hépatite virale chronique (I-03-Infectiologie)

Le contrôle interne ciblé de B24 est consigné dans `preuves/cloture_interne_B24.json`. Il suffit pour avancer dans la file sans déclarer B24 validé cliniquement ni le fragment complet. La catégorie suivante est **B18 — Hépatite virale chronique**, déjà attribuée au frontend I-03. La veille des branches Claude n'a trouvé aucun cours B18 concurrent ; le registre de production réserve maintenant ce seul chapitre actif.

B18 comprend quatre onglets, avec le cas pédagogique de Mme R., 42 ans, dont deux tests Ag HBs positifs sont espacés de plus de six mois. Les ALAT, l'ADN VHB, le statut HBeAg, le VHD, la fibrose et les autres résultats restent inconnus tant qu'aucun résultat n'est donné. Le cours distingue VHB, VHC, VHD et VHE chronique, leurs sous-codes B18, les examens, la science et les choix thérapeutiques conditionnels. Les huit sources HTML et le glossaire sont déclarés par **28 empreintes** au manifeste interne, avec A41/B24 inchangés. Le constructeur ajoute B18 à la seule copie de consultation ; aucune source médicale canonique n'est modifiée.

Le dossier `preuves/B18/SOURCES_VERIFIEES.md` trace BfArM CIM-10-GM 2024, EASL VHB 2025, VHC 2020, VHD 2023, VHE 2018, CHC 2025, la position suisse SASL/SSG/SSI VHC 2021, l'OMS VHB 2024 et l'information professionnelle suisse Hepcludex de juillet 2026. La divergence entre EASL VHC 2020 et EASL CHC 2025 sur la surveillance après guérison avec fibrose F3 sans cirrhose est explicitée ; les situations VHB à haut risque sans cirrhose conservent leur évaluation propre. La revue indépendante `preuves/B18/REVUE_INDEPENDANTE.md` a fait corriger la hiérarchie EASL VHB 2025/SASL 2021 de la prévention d'une réactivation sous AAD. Elle ne relève plus de réserve médicale bloquante dans son périmètre ciblé. L'onglet Examens compte trois quiz ; les **93 interactions B18** ouvrent des fenêtres réelles sans clé orpheline.

La compilation locale affiche A41, B24 et B18 dans le frontend clair isolé d'Infectiologie, avec **254 fenêtres** au total. Les **178 tests Python** passent. Le contrôle Chromium réel sur ordinateur et mobile a validé **3 459 vérifications, sans échec**, dont l'ouverture des 93 fenêtres B18 aux deux largeurs, les quatre onglets, les trois quiz Examens, la police Atkinson et l'absence de modification des 28 sources manifestées pendant la lecture. Sa preuve est `preuves/technique/browser-proof-b18-final.json`. Une animation locale de cinq vues réelles, avec fenêtre ouverte, est documentée dans `preuves/technique/animation-b18-local.json`. La publication Pages et son contrôle distant restent à effectuer. B18 reste une version de travail, sans validation médicale humaine, sans équivalence CIM-11 automatique, sans audit croisé final du fragment ni injection canonique.
