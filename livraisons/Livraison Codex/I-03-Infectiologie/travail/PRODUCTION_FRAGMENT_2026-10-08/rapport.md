# I-03-Infectiologie — progression interne du 8 octobre 2026

Le premier des dix fragments Codex reste **I-03-Infectiologie (T1)**. Ce dossier prépare deux cours dans son frontend de travail local : **A41 — Sepsis et choc septique de l’adulte** et **B24 — Infection par le VIH et maladie à VIH de l’adulte**. Les sources canoniques historiques sont conservées. La police est Atkinson Hyperlegible Next, alignée sur celle retenue par Claude ; l’aperçu réutilise le frontend clair de la spécialité.

## Rédaction et revue ciblée

A41 a reçu les précisions de Sepsis-3, des populations Phoenix, du bicarbonate et du qSOFA, ainsi que celles du codage R65, du consensus de choc réfractaire, de la gentamicine et de la mortalité observée à 29,9 %. Les corrections historiques de Claude restent présentes. Les preuves et les limites de ce contrôle ciblé sont dans `preuves/cloture_interne_A41.json` et les rapports associés.

B24 comporte les quatre onglets, six sous-onglets scientifiques, des schémas, des fenêtres explicatives, huit quiz, cinq synthèses Pareto et son glossaire. Quatre auteurs possèdent chacun un panneau et ses fenêtres ; une relecture indépendante porte sur l’ensemble assemblé. Le cas pédagogique reste borné aux faits explicitement donnés et distingue les exemples hypothétiques des résultats réels du cas.

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
