**Politique des sources (8 octobre 2026)** : sources suisses d'abord (sociétés savantes, universités, Swissmedic/OFSP), puis européennes applicables en Suisse ; recherche indexée avec `origine` CH/EU ; toute autre source exige `derogation`. Lire `docs/collaboration/POLITIQUE_SOURCES.md` ; contrôle bloquant `python3 tools/sources_guard.py check` (CI et commit).

**Référence médicamenteuse suisse = `ref/fi/` ; aucune posologie, interaction ou contre-indication sans vérification dans ce corpus.** Corpus : informations professionnelles (FI) AIPS Swissmedic en français, version du 8 octobre 2026, indexées dans `ref/fi/INDEX.md` ; régénération avec `tools/aips_to_fi.py`.

## Alignement avec Claude — police de lecture, 8 octobre 2026

Dernière instruction directe de Vial : « Pas de conflit avec Claude. Aligne toi avec la Police qu’il a trouvé ». **Atkinson Hyperlegible Next** devient la police par défaut du portail, des 22 frontends et des cours, avec les quatre WOFF2 de Claude (`f928674`). Cette consigne remplace la demande antérieure de police Anthropic Serif ; celle-ci reste une option du lecteur. Conserver les contributions de Claude, les contrastes élevés, le thème clair et la séparation des spécialités. Les réglages du lecteur s’appliquent au texte, aux fenêtres et à Navigo. Aucune modification de source médicale ni de statut de fragment n’est requise par cette consigne. Voir `docs/collaboration/FRONTENDS_2026-10-08.md` et son reçu d’alignement.

## Consigne frontend active — 8 octobre 2026

Vial demande un accès visuel aux cours, un accueil clair et agréable et une refonte majeure du frontend. **Chaque fragment possède son HTML et sa navigation propres, limités au contenu de sa spécialité.** Les cartes de catégories sont sobres, sur fond clair, avec un relief 3D discret ; la police par défaut est **Anthropic Serif authentique**, embarquée hors ligne. Le lecteur peut adapter sa police et sa taille. La classification frontend est centralisée dans `fragment_surface.py` ; les anciens rattachements anatomiques ne doivent pas réintroduire un cours étranger. L’aperçu de rédaction A41 est une consultation explicitement marquée « Version de travail » sous `apercus/infectiologie.html`, sans injection canonique, sans certification finale et sans remise pour audit du fragment incomplet. Lire `docs/collaboration/FRONTENDS_2026-10-08.md`.

## Consigne active — reprise et fragments entiers, 8 octobre 2026

Vial demande de prendre connaissance de `Prompt_Codex.pdf` et de continuer. Cette reprise lève le STOP antérieur. Lire [COORDINATION.md](COORDINATION.md) et [le protocole par fragment](docs/collaboration/PROTOCOLE_FRAGMENTS_2026-10-08.md) avant les instructions historiques ci-dessous. **Fragment entier complet et auto-revu avant transmission ; audit croisé unique, correction et injection par l’autre IA ; fragment INJECTÉ immuable ; arrêt après les 22 ; HTML clair exclusivement.** Les règles de remise par chapitre, d’injection autonome avant audit, de renvois successifs et de correction après injection sont remplacées. Les travaux et leurs preuves restent conservés. Le mode multi-agent et un auteur par fichier restent applicables ; les veilles automatiques restent en pause.

# CLAUDE.md — MEDINA (Atlas des cours de médecine par systèmes)

## Consigne la plus récente — STOP Codex, 8 octobre 2026

Vial demande : « injecte ce qu'il faut injecter puis STOP. je vais changer les règles ». La session Codex est arrêtée, y compris sa production, ses sous-agents et sa veille automatique. [Décision et état final](docs/collaboration/ARRET_CODEX_2026-10-08.md). I83 v6 est déjà injecté et publié ; I89, J45 et A41 restent non injectables. La demande A41 sur PR #15 demeure disponible, mais sa présence et les missions historiques ci-dessous ne constituent pas un ordre de reprise Codex. Attendre les nouvelles instructions avant de relancer son travail ou sa veille.

## Répartition des 21 fragments restants — 8 octobre 2026

Lire [FRAGMENTS_RESTANTS.md](docs/collaboration/FRAGMENTS_RESTANTS.md) et [production_plan.json](organisation/production_plan.json) : **11 fragments entiers Claude, 10 fragments entiers Codex**, hors cardiologie. Toutes les catégories restent regroupées sous leur fragment. Chaque catégorie ou chapitre cité porte **code — intitulé (libellé complet du fragment)**, par exemple **J45 — Asthme (P-02-Pneumologie)**. Un seul fragment et **un seul chapitre en production par agent**, un chapitre par remise. Produire le chapitre complet et le remettre à l’autre IA pour audit avant de commencer le suivant ; les corrections reçues restent prioritaires. Les audits, injections et publications des chapitres déjà remis sont suivis séparément et conservent leurs contrôles. Les files respectent les rangs du registre. La nouvelle consigne active la chaîne Codex sur I-03-Infectiologie ; la cardiologie et ses réserves restent conservées dans le backlog. Lire [CODEX_CHAINE_FRAGMENTS.md](docs/collaboration/CODEX_CHAINE_FRAGMENTS.md) pour les vagues de sous-agents et les sentinelles. Aucun fragment n’est déclaré complet par cette attribution. Cette règle de progression prime sur les anciennes consignes de production par lots ou cycles pour les travaux nouveaux.

La session Codex actuelle prend le relais de GPT « work » comme coordinateur prioritaire ; conserver les travaux et commits antérieurs. **Mode multi-agent obligatoire** : Claude et Codex progressent en parallèle, avec plusieurs sous-agents spécialisés dans le seul chapitre actif de chacun et un auteur par fichier. **Claude audite les chapitres Codex avant leur injection. Claude peut injecter ses propres chapitres après revue interne et contrôles complets ; Codex les audite ensuite dans l’ordre de [FILE_AUDIT_CODEX.json](docs/collaboration/FILE_AUDIT_CODEX.json)**. Appliquer [REGLES_INJECTION_CLAUDE.md](docs/collaboration/REGLES_INJECTION_CLAUDE.md) : aucune réserve bloquante ouverte, toutes les conditions obligatoires vérifiées ; une erreur médicale démontrée reste prioritaire. Les chapitres Claude attendent l’audit sous la mention « en audit croisé » ; les désaccords non bloquants de leurs chapitres sont tranchés par Claude. La mission précise de Claude est [CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES.md](docs/collaboration/CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES.md).



## Précisions durables de Vial — 8 octobre 2026

Lire [les consignes communes d’interaction, densité et sources](docs/collaboration/CONSIGNES_INTERACTION_DENSITE_SOURCES.md). Le parallélisme répartit les catégories et sujets du **même chapitre** entre sous-agents, avec un auteur par fichier. Les explications sont accessibles après clic sur le mot interactif ; les tableaux servent les classifications et énumérations quand ils clarifient le contenu, avec des cellules courtes et cohérentes. Aucun plafond de mots arbitraire. Pour un contentieux clinique, **la source primaire applicable la plus récente l’emporte** ; présenter le choix dans une fenêtre liée à un mot vert, avec accès au texte actuellement en vigueur même s’il est ancien. Compendium est un accès utile aux monographies suisses, à lire et dater réellement. Ne pas assimiler revue IA, tests et validation par un médecin.

## Mission cardiologie conservée : Fragment 01 à 50/50

Lire [FRAGMENT_01_PRIORITE.md](docs/collaboration/FRAGMENT_01_PRIORITE.md) : vingt cours présents en cardiologie répartis 10 Codex / 10 Claude, plus quatre productions prioritaires réparties 2/2. Les listes historiques 15/15 ci-dessous sont remplacées pour cette reprise. Fenêtres contextualisées, volume sans multiplicateur imposé et ESC 2026 comparatif. La nouvelle chaîne Codex du 8 octobre ouvre I-03-Infectiologie ; les réserves cardiologiques demeurent ouvertes et Claude conserve sa mission actuelle.


## Justifier chaque affirmation — priorité actuelle

La consigne de Vial du 7 octobre 2026 s’applique à **toutes les affirmations médicales**, dans tous les onglets, tableaux, figures, quiz, fenêtres, Pareto et glossaires. Expliquer pourquoi le fait est vrai ou la décision utile : mécanisme causal précis, conséquence clinique, limites et source primaire. Pour « anémie : facteur aggravant », détailler la diminution du transport artériel d’oxygène et les compensations cardiovasculaires, en tenant compte du contexte. Pour le sodium ou le potassium, justifier séparément le dosage, l’interprétation et la conduite ; ne pas confondre association pronostique et causalité.

La priorité actuelle répartit les **20 cours présents du Fragment 01 : 10 Codex, 10 Claude**, selon `docs/collaboration/MECHANISMS_PLAN.json` et `MECHANISMS_CLAUDE.md`. Une banque de fenêtres ciblées n’est pas une relecture exhaustive. Toute affirmation non revue demeure à contrôler ; ne pas marquer le cours validé pour sa seule compilation. Cette instruction prime sur les anciennes missions.

Les catégories CIM structurent désormais les plateformes originales : numéro de catégorie, chapitres numérotés dans cette catégorie, code discret en haut à droite, couleur vive lisible. **J40 — Bronchite** est un cours unique couvrant J20, J40, J41 et J42 ; distinguer bronchite chronique et BPCO. Préserver les quatre onglets et les outils de lecture.

Lire la passation, reprendre depuis la branche d’intégration `codex/sciences-cs-fragments-20261007` et utiliser le protocole de livraison : les sources corrigées de PR #10 sont reçues et leur injection/contrelecture est tracée dans les reçus. Ne pas recopier une ancienne version au-dessus de corrections nouvelles. Les accès GitHub restent ceux de la connexion effective ; aucun secret ni jeton ne doit être transmis dans les fichiers.

## Organisation des fragments et des remises — 7 octobre 2026

Nomme toujours une leçon par son **code CIM et son intitulé complet**. Nomme toujours un fragment par **initiale de spécialité - ordre de production - nom littéral**, suivant `organisation/fragments.json` : `C-01-Cardiologie`, par exemple. Les codes du catalogue sont ceux de la CIM-10-GM 2024 ; la cartographie CIM-11 demeure à établir.

Le tableau de bord commun est `organisation/MEDINA_Organisation.html`, publié à https://vialdjoukang-spec.github.io/Medina/organisation.html. Chaque fragment dispose de sources complètes pour ses cours existants dans `livraisons/Livraison Codex/<libellé>/`. Dépose tes sources corrigées et ton rapport dans `livraisons/Livraison Claude/<libellé>/`, sur ta branche, puis ouvre une PR. Lis `docs/collaboration/DELIVERY_PROTOCOL.md` pour la remise, les contrôles et l'injection. Le dépôt entier reste accessible ; aucune nouvelle confirmation de publication n'est demandée au propriétaire.

## Consigne prioritaire de Vial — 7 octobre 2026

**Réception des livraisons.** Lire aussi `AGENTS.md` et `docs/collaboration/DELIVERIES_LATEST.md`. À chaque reprise et avant publication, recenser toutes les branches et PR avec `tools/collaboration_sync.py`. Les anciens rapports et les branches sans PR sont recevables. Toute livraison reçoit un accusé sous `docs/collaboration/receipts/`, avec les sources, les fragments, le commit d'intégration et les réserves. Ne pas conclure « aucun rapport reçu » depuis la seule passation ou depuis les références du clone local.

Vial a donné son **accord permanent pour les publications et contributions GitHub dans MEDINA** : branches, commits, pushes, rapports et pull requests. Les actions courantes de collaboration ne nécessitent pas une nouvelle confirmation. Lire [le point d'entrée commun](docs/collaboration/README.md) et [la dernière passation](docs/collaboration/HANDOFF_LATEST.md). Claude peut lire tout le dépôt et proposer des modifications sur sa branche ; cette autorisation ne remplace pas sa connexion GitHub effective. Après chaque lot terminé, publier sources, contrôles et rapport, puis actualiser la passation pour rendre le travail immédiatement accessible à l'autre IA. Les fusions suivent les contrôles du projet et les protections GitHub.

La complétude demandée porte désormais sur **toutes les catégories et sous-catégories pertinentes de la CIM-11**, dans chaque système. Le catalogue historique de ce dépôt reste en CIM-10-GM 2024 ; il ne prouve pas cette complétude. Lire [la règle de complétude](docs/COMPLETUDE_CIM11.md) et [le relevé actuel](audits/COMPLETUDE_2026-10-07/README.md). Aucun fragment livré n'est certifié complet en CIM-11.

La relecture intégrale donne priorité aux **20 cours présents du Fragment 01**, répartis **10 Codex et 10 Claude**, selon `docs/collaboration/MECHANISMS_PLAN.json`. Elle porte sur la médecine, les mécanismes, la pédagogie et le français professionnel ; la Sémiologie CS reste aussi à contrôler. La [mission globale historique](docs/collaboration/CLAUDE_AUDIT_GLOBAL_2026-10-07.md) conserve ses critères de qualité, avec ce partage actualisé. La relecture ciblée I48 ne certifie pas les autres contenus. Une annonce pédagogique expose directement le problème médical ; elle ne décrit pas « cet îlot » ou la fabrication du cours. Supprimer les répétitions et le remplissage sans retirer une information utile. Ces instructions actuelles priment sur les anciens objectifs de longueur et sur toute mention historique de système achevé.

> Fichier lu automatiquement par Claude Code à chaque session. **Lire ensuite `PROMPT_MEDINA.md` en entier** (prompt maître, source de vérité) et `CHAPTER_SPEC.md` (contrat HTML historique).

## Propriétaire et mission
- **Dr Vial Tato Djoukang**, Neuchâtel, prépare l’**examen fédéral suisse de médecine humaine**. MEDINA (ancien nom : MEDORA) est son atlas de cours, pathologie par pathologie, système par système (CIM-10-GM 2024).
- Rôle : professeur omnipraticien et enseignant de médecins assistants. Chaque pathologie est traitée comme une notion nouvelle, des généralités au point pointu, avec l’obsession de faire comprendre. Sources suisses d’abord, puis européennes et internationales acceptées en Suisse.
- Communication : français, ton chaleureux, réponses structurées (titres, gras, tableaux), denses, sans remplissage. Il dicte souvent (approximations de transcription). Ne pas corriger son propre texte sans demande.
- **Autonomie de livraison** : quand les contrôles passent, intégrer et livrer sans demander d’accord ; ne le solliciter qu’en cas d’échec d’audit ou de blocage réel.
- **Profondeur et rédaction** : préserver toutes les notions utiles ; supprimer les répétitions et le remplissage. Aucun objectif de longueur ne remplace la qualité.
- Terminer chaque livraison par un **tableau de bord** (cours, catégories traitées, systèmes, poids du fichier, alertes).

## Démarrage rapide
```bash
python3 build_front.py          # construit MEDINA.html (cours compressés, ~8,3 Mo)
python3 test_v7.py I70 I71 I80  # contrôle navigateur : doit afficher OK
python3 chantier.py             # état des lieux (fichier séparé, jamais dans le produit)
python3 pack_v7.py              # empaquette les sources dans MEDINA_SOURCES.json
```
Sortie : variable `MEDINA_OUT` (par défaut `/mnt/user-data/outputs` s’il existe, sinon `./dist`). Dépendances : Python 3.10+, `playwright` + Chromium (`pip install playwright && playwright install chromium`).

## Règles non négociables (détail dans PROMPT_MEDINA.md)
0. **Rédaction** : suivre `docs/STYLE_REDACTION.md` (le lecteur comprend, il ne devine pas ; phrases courtes et complètes, jamais nominales ; annonce, développement, épilogue ; tableaux introduits et commentés).
1. **Front-end d’origine de Medina** (`shell/medina_front.html`, vert `#1f3428`, Georgia) : structure intouchable ; embellissement seulement par `shell/polish.css` / `shell/polish.js`. La coque V7 (`shell/shell.html`, `build_v7.py`) est **abandonnée**.
2. **Contrat HTML** d’un chapitre : `chapters/<CODE>/<CODE>_a.html` … `_d.html` + `_pop*.html` ; 4 onglets (Pathologie, Examens, Sciences, Pharmacologie) ; classes de la liste fermée ; identifiants préfixés par le code en minuscules.
3. **Abréviations** : aucune sans clé dans le glossaire (`glossary/<code>.py`, `a(*x)`), définition littérale lettre à lettre ; `build_medina.audit()` doit renvoyer `{}`.
4. **Dernier îlot de chaque cours** : critères formels du diagnostic (`div.alert`) puis paramètres clés (`div.key`).
5. **Pareto « perfectit »** à la fin de chaque grande partie ; fraction calculée par le moteur.
6. **Typographie** : Georgia partout, titres et numéros rouges soulignés, texte justifié (moteur).
7. Pas de métaphores, jeux de mots ni plaisanteries ; exemples chiffrés ; normal avant pathologique.
8. **Vague d’un chapitre** = système de ses catégories dans `medora-data` (champ `system`), jamais par supposition.

## ⚠️ REPRISE IMMÉDIATE (26.09.2026) : lire `PROMPT_REPRISE_IA.md` puis `PASSATION_REECRITURE_2026-09-26.md`
Réécriture pédagogique de J44, J18, I26 et A41 selon `docs/STYLE_REDACTION.md` : l’onglet 1 est fait ; les onglets 2 à 4, la contre-lecture et la livraison restent à faire.

## ⚠️ MISSION ACTUELLE : lire `REPRISE_CLAUDE_CODE.md` et l’exécuter phase par phase
1. Fusionner la branche **Alpha** (ChatGPT, fichiers dans `_alpha_in/`) dans ce projet : tous les chapitres, audits, glossaire et fonctions d’interface (Navigo, Police Taille, mode livre).
2. Moderniser et styliser le front-end partout, sans changer l’architecture.
3. Livrer `MEDINA_final.html`.
4. Produire par cycles de deux systèmes, qualité extrême.

## Priorités de fond (voir PROMPT_MEDINA.md § 19)
1. **Achever la vague 9** (Vaisseaux et microcirculation + Immunité) : I73, I83, I89, I95, D86, D90, B24 ; puis ajouter 9 à `DONE_SYS`.
2. **Réécrire au niveau de J45** les chapitres condensés : J44, D84, M06, M32.
3. **Poursuivre** l’ordre du § 9 à partir de J18 Pneumonies (vague 2), puis vagues 7, 5, 6, 4, 3, 8, 11, 12.
4. Audit indépendant des chapitres non audités (grille /20, `audits/<CODE>.md`).
5. Réintégrer le volet Examen fédéral (GLOBALITY) comme module chargé à la demande.

## Commandes personnalisées
- `/chapitre <CODE> <catégories> <titre>` : rédiger et intégrer un chapitre complet.
- `/livrer` : construire, tester, empaqueter, copier vers Drive, tableau de bord.
- `/audit <CODE>` : audit indépendant /20 avec rapport.
- `/fusion-alpha` : phase 1 de REPRISE_CLAUDE_CODE.md.
- `/cycle` : un cycle de deux systèmes (phase 4).
