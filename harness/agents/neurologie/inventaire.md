## État courant distinct du cliché préparatoire

Mise à jour du 2 novembre 2026 : G02 est acquise et active dans `/workspace/Medina-neurologie`, branche `codex/alpha77/g02-integrate-g1`. La préparation ci-dessous reste historique. Le premier paquet a été poussé au commit `a35d56e70fe8b1739816a6b65c97753327bd130d` ; [aperçu autonome de cette version](https://github.com/vialdjoukang-spec/Medina/blob/a35d56e70fe8b1739816a6b65c97753327bd130d/docs/collaboration/ssp-v2/execution/ALPHA77-CODEX-G02-INTEGRATE/G02-apercu-autonome.html). La révision WHO et produit exact fexinidazole ajoute deux lectures (23 au total), avec reconstruction/captures passées et push au commit `3a7c7aa23d769e00f2e4d1e8beba6050d9a8dc6b` ; [aperçu de cette version](https://github.com/vialdjoukang-spec/Medina/blob/3a7c7aa23d769e00f2e4d1e8beba6050d9a8dc6b/docs/collaboration/ssp-v2/execution/ALPHA77-CODEX-G02-INTEGRATE/G02-apercu-autonome.html). Le chemin local courant est `docs/collaboration/ssp-v2/execution/ALPHA77-CODEX-G02-INTEGRATE/G02-apercu-autonome.html` dans ce worktree.

Les réserves substantielles restent dans le README du paquet et `brief.json`. L’auto-relecture explicite est autorisée par le contrat ; elle ne doit pas être appelée indépendante. G05 demeure un candidat ultérieur, aucun passage automatique. Voir aussi `orchestration.md` pour la coordination des quatre filières.

# Préparation Neurologie — aucun cours produit

Base inspectée : `8a512893acbab9caa0dcfdd0e8682a44ea72fda6`. Modèle demandé par le parent : GPT-6 Astra, réflexion élevée. Les tokens consommés ne sont pas mesurables ici ; aucun chiffre n’est estimé. Le présent dossier contient uniquement une préparation, sans rédaction médicale, acquisition de réservation ni changement des sources.

## Choix et ordre

**G02 — Méningite au cours d’autres maladies infectieuses et parasitaires classées ailleurs (N-05-Neurologie)** est le premier cours existant Codex libre dans la file de campagne, au rang global 8. Le registre distant collecté par le parent ne contient aucune réservation G02. I63 et G01 restent réservés en génération 1, avec MED/LANG et intégration ; leurs reçus `organisation/alpha-publications/Codex/{I63,G01}/0001.json` sont `provisional`. Ils ne doivent pas être repris implicitement.

Le balayage rétrospectif de `PROMPT_CONTINUITE_AUTEURS.md` demande de corriger les existants avant les nouveaux. L’ordre utilisateur courant remplace le fonctionnement historique incompatible en lots, tout en préservant réservations et preuves. Le plan ci-dessous est une file de travail proposée ; chaque démarrage exige la garde actuelle et un worktree exclusif annoncé par le parent.

La mission `ALPHA77-CODEX-G02-INTEGRATE` est approuvée dans `.medina/missions/ALPHA77-CODEX-G02-INTEGRATE.json`. Branche prévue : `codex/alpha77/g02-integrate-g1`. Chemins : `chapters/G02`, `glossary/g02.py`, `assets/img/g02/alpha/codex`, `organisation/alpha-publications/Codex/G02`, `docs/collaboration/ssp-v2/execution/ALPHA77-CODEX-G02-INTEGRATE`. Le catalogue partagé ne fait pas partie de cette mission.

## Inventaire et file complète

Le plan V2 actuel compte 57 cours existants S08 (29 Codex, 28 Claude), 50 cibles nouvelles (25/25) et 9 réserves distinctes. Ces chiffres décrivent un plan éditorial conservatoire, pas une complétude fédérale officiellement validée. La campagne Codex77 ne comprend que 7 nouvelles cibles S08 parmi ses 25 nouvelles cibles globales ; les 18 autres cibles Neurologie Codex restent hors campagne historique et exigent leurs missions avant exécution.

| Ordre | Code — intitulé | État |
|---|---|---|
| 1 | G02 — Méningite au cours d’autres maladies infectieuses et parasitaires classées ailleurs | Existant libre, à reprendre |
| 2 | G05 — Encéphalite, myélite et encéphalomyélite au cours d’affections classées ailleurs | Existant libre, à reprendre |
| 3 | I64 — Accident vasculaire cérébral, non précisé comme étant hémorragique ou par infarctus | Existant libre, à reprendre |
| 4 | C70 — Tumeur maligne des méninges | Existant libre, à reprendre |
| 5 | G03 — Méningite due à des causes autres et non précisées | Existant libre, à reprendre |
| 6 | G06 — Abcès et granulome intracrâniens et intrarachidiens | Existant libre, à reprendre |
| 7 | G07 — Abcès et granulome intracrâniens et intrarachidiens au cours d’affections classées ailleurs | Existant libre, à reprendre |
| 8 | G08 — Phlébite et thrombophlébite intracrâniennes et intrarachidiennes | Existant libre, à reprendre |
| 9 | G09 — Séquelles d’affections inflammatoires du système nerveux central | Existant libre, à reprendre |
| 10 | G21 — Syndrome parkinsonien secondaire | Existant libre, à reprendre |
| 11 | G22 — Syndrome parkinsonien au cours de maladies classées ailleurs | Existant libre, à reprendre |
| 12 | G24 — Dystonie | Existant libre, à reprendre |
| 13 | G25 — Autres syndromes extrapyramidaux et troubles de la motricité | Existant libre, à reprendre |
| 14 | G26 — Syndromes extrapyramidaux et troubles de la motricité au cours d’affections classées ailleurs | Existant libre, à reprendre |
| 15 | G32 — Autres affections dégénératives du système nerveux au cours d’affections classées ailleurs | Existant libre, à reprendre |
| 16 | G36 — Autres affections démyélinisantes aiguës disséminées | Existant libre, à reprendre |
| 17 | G37 — Autres affections démyélinisantes du système nerveux central | Existant libre, à reprendre |
| 18 | G52 — Affections des autres nerfs crâniens | Existant libre, à reprendre |
| 19 | G53 — Affections des nerfs crâniens au cours de maladies classées ailleurs | Existant libre, à reprendre |
| 20 | G55 — Compression des racines et des plexus nerveux au cours de maladies classées ailleurs | Existant libre, à reprendre |
| 21 | G57 — Mononévrite du membre inférieur | Existant libre, à reprendre |
| 22 | G59 — Mononévrite au cours de maladies classées ailleurs | Existant libre, à reprendre |
| 23 | G60 — Neuropathie héréditaire et idiopathique | Existant libre, à reprendre |
| 24 | I66 — Occlusion et sténose des artères cérébrales, n’entraînant pas un infarctus cérébral | Existant libre, à reprendre |
| 25 | I68 — Troubles cérébrovasculaires au cours de maladies classées ailleurs | Existant libre, à reprendre |
| 26 | R25 — Mouvements involontaires anormaux | Existant libre, à reprendre |
| 27 | R47 — Troubles du langage, non classés ailleurs | Existant libre, à reprendre |
| 28 | G00 — Méningite bactérienne, non classée ailleurs | Nouveau, campagne77 |
| 29 | G04 — Encéphalite, myélite et encéphalomyélite | Nouveau, campagne77 |
| 30 | G41 — État de mal épileptique | Nouveau, campagne77 |
| 31 | I60 — Hémorragie sous-arachnoïdienne | Nouveau, campagne77 |
| 32 | R40 — Somnolence, stupeur et coma | Nouveau, campagne77 |
| 33 | G30 — Maladie d’Alzheimer | Nouveau, campagne77 |
| 34 | G40 — Épilepsie | Nouveau, campagne77 |
| 35 | C71 — Tumeur maligne de l’encéphale | Nouveau, mission future requise |
| 36 | G31 — Autres affections dégénératives du système nerveux, non classées ailleurs | Nouveau, mission future requise |
| 37 | G35 — Sclérose en plaques | Nouveau, mission future requise |
| 38 | G43 — Migraine | Nouveau, mission future requise |
| 39 | G44 — Autres syndromes d’algies céphaliques | Nouveau, mission future requise |
| 40 | G50 — Affections du nerf trijumeau [nerf crânien V] | Nouveau, mission future requise |
| 41 | Q01 — Encéphalocèle | Nouveau, mission future requise |
| 42 | Q02 — Microcéphalie | Nouveau, mission future requise |
| 43 | Q03 — Hydrocéphalie congénitale | Nouveau, mission future requise |
| 44 | Q04 — Autres malformations congénitales de l’encéphale | Nouveau, mission future requise |
| 45 | R41 — Autres symptômes et signes relatifs aux fonctions cognitives et à la conscience | Nouveau, mission future requise |
| 46 | R42 — Étourdissements et éblouissements | Nouveau, mission future requise |
| 47 | S04 — Lésion traumatique des nerfs crâniens | Nouveau, mission future requise |
| 48 | S14 — Lésion traumatique des nerfs et de la moelle épinière au niveau du cou | Nouveau, mission future requise |
| 49 | S24 — Lésion traumatique des nerfs et de la moelle épinière au niveau du thorax | Nouveau, mission future requise |
| 50 | S44 — Lésion traumatique de nerfs au niveau de l’épaule et du bras | Nouveau, mission future requise |
| 51 | S54 — Lésion traumatique de nerfs au niveau de l’avant-bras | Nouveau, mission future requise |
| 52 | S64 — Lésion traumatique de nerfs au niveau du poignet et de la main | Nouveau, mission future requise |

Réservés, conservés hors file active : I63 et G01. La présence historique d’un dossier rédigé par Claude ne change pas l’attribution actuelle : le dossier G02 est conservé dans `livraisons/Livraison Claude/N-05-Neurologie/betta/CYCLE_33_G02/`. Le parent a collecté toutes les branches et PR dans `/tmp/medina-harness-discovery/` ; aucune branche G02 ni PR G02 n’a été relevée dans ce cliché. Recontrôle obligatoire avant acquisition.

## État initial G02

Les six HTML et `glossary/g02.py` existent. Les empreintes exactes sont dans `brief.json`. Quatre sous-onglets scientifiques seulement : Physiologie, Immunologie, Virologie diagnostique, Mycologie et parasitologie. Aucun marqueur `data-semiology-clinical` ni `data-semiology` ; six SVG et aucune balise `<img>`. L’absence de sémiologie établit l’incomplétude structurelle. La seule présence d’un SVG ne prouve pas une anatomie générée : inspecter le contenu et la provenance avant de qualifier le défaut.

Le dossier auteur comporte `sources.json`, `recherche.md` et `rapport.md`. Il doit être attribué et comparé aux octets courants, jamais présenté comme une nouvelle lecture primaire. Le rapport déclare notamment des limites de couverture suisse, des parties parasitologiques non lues et des FI manquantes ou partielles. Ce sont des pistes d’audit héritées, non des conclusions médicales revalidées par cet agent.

## Prompt et références de qualité

Le dernier fichier portant un prompt dans l’historique de main est `docs/collaboration/claude-transition-2026-10-15/PROMPT_TRANSITION.md`, commit `a6f51eba`, 15 octobre 2026 à 22:24:46 UTC. C’est une transition Claude ; ses ordres locaux ne s’appliquent pas automatiquement à Codex. Le dernier contrat opérationnel commun est `docs/collaboration/ssp-v2/2026-10-15/prompt-commun-ia.yaml`, `d40aaf7c`, 15 octobre 2026 à 17:37:19 UTC. Le socle médical est `docs/collaboration/betta/PROMPT_VERITE.md`, `60bb2100`, 15 octobre 2026 à 10:03:50 UTC. Les modifications les plus récentes de gouvernance ne sont pas nécessairement des modifications de ces prompts ; AGENTS.md et l’ordre humain courant restent prioritaires.

`PROMPT_MEDINA.md` désigne `chapters/I50/` comme modèle de forme. `PROMPT_TRANSITION.md` désigne `chapters/J81/` comme niveau de rendu et `livraisons/Livraison Claude/P-02-Pneumologie/travail/J81/rapport_relecture.md` comme modèle de rapport. La règle sémiologique désigne I50/I21/I48/I10 et les moteurs de cardiologie comme références en lecture seule. Leur contenu n’est jamais une source clinique primaire.

Le plan monographique exigé par `docs/collaboration/LEADERSHIP_CLAUDE_2026-10-08.md`, section 11, couvre question clinique, définition/classifications, épidémiologie/pronostic, physiopathologie, causes/risques, anamnèse, examen, diagnostic, urgences/complications, traitement, suivi/prévention, situations particulières et critères finaux. Le code administratif reste discret. Le cours doit relier normal → mécanisme → signe → examen → interprétation → décision, en français complet et fluide.

`docs/collaboration/instructions/SEMIOLOGIE_FONDAMENTALE_ANALYTIQUE_2026-10-15.yaml` exige le sous-onglet initial de sémiologie en pS, ses neuf sections substantielles, un bloc clinique pA et des preuves MED/LANG/SEMIO finales. Les six sous-onglets incluent cinq disciplines scientifiques et la sémiologie ; les quatre références cardiologiques historiques ne suffisent pas seules à cette exigence.

## Sources à relire avant toute affirmation

Les 18 références héritées sont détaillées individuellement dans `brief.json`, avec sections et limites. Priorité aux sources suisses applicables à rechercher ou rouvrir, puis DGN/EAN/ECMM européennes selon leur portée. S12–S13 : pages OFSP ; S8–S9 : travaux CHUV/HUG, dont la lecture historique est limitée au résumé. S14–S17 : FI exactes Aciclovir Labatec i.v., Valaciclovir-Mepha, AmBisome et Fluconazole Sandoz eco ; retrouver l’original Swissmedic/Compendium, la version et les rubriques pertinentes. Les URL génériques amiko du dossier ne suffisent pas à une preuve produit.

S3 : directive DGN 2025 ; S10 : recommandation cryptococcose 2024 ; S11 : traitement trypanosomiase OMS, historiquement simple page de présentation ; S18 : ESCMID 2012, historiquement résumé. Les passages concernant seuils, délais, posologies, adaptations, contre-indications, interactions et populations particulières doivent être réellement lus. La version en vigueur doit être contrôlée ; une directive ancienne reste applicable seulement si sa validité est établie. Le cache hérité doit préciser lecteur, contenu, section, date et population ; ne jamais dater sa réutilisation comme une nouvelle lecture.

## Contrôles et conception du harness

1. Avant rédaction : tests du harness et démonstration de la veille ; SHA de base figé, chemins exclusifs et réservation distante ; sources effectivement consultées, matrice des 20 rubriques, puis `tools/betta_verite.py`.
2. Pendant la leçon : correspondance assertion/passages/IDs HTML, couverture suisse et FI produit ; inventaire figures, origine humaine anatomique, droits propres à la figure, attribution et inspection visuelle. Une image originale libre ne certifie pas sa pertinence médicale.
3. Avant livraison : `tests/audit_sciences.py --base <SHA40> --codes G02`, garde Alpha et mission sur candidat final, reconstruction S08, liens et fenêtres, six sous-onglets, bureau/mobile390, Livre24 et captures réelles. Ne pas ajouter de SVG factice pour satisfaire un test.
4. Rapports finaux séparés MED, LANG, SEMIO liés aux empreintes finales ; aucune clôture favorable avec réserve clinique bloquante ; aucune revue auteur présentée comme indépendante. PR/publication seulement par le parent et selon son mandat.

Le harness proposé est cohérent s’il lie le SHA-cache au contenu et au passage, à la population et à la décision. Une lecture tronquée reste explicitement partielle. Le bail unique par spécialité doit s’ajouter aux verrous de leçon et de chemins, avec transaction atomique. L’expiration d’un heartbeat gèle la mutation concernée mais n’efface pas une réservation distante concurrente. Le heartbeat atteste un processus vivant, pas une lecture ni une consommation mesurée de tokens.

Les tests négatifs doivent couvrir acquisition concurrente, génération et base périmées, doublons, échappement de chemins et symlinks, cache changé, source non lue, résumé seul insuffisant, sémiologie cachée/incomplète et preuve médicale absente malgré HTML valide. Les portes techniques et médicales restent distinctes : un JSON complet ne prouve pas la vérité clinique.

La veille locale600s et le dépôt GitHub privé cron10min doivent observer sans écrire dans main Medina. Leur disponibilité ne garantit ni agent permanent ni livraison ponctuelle à la seconde. À08h Europe/Zurich, produire un instantané horodaté ; il ne s’agit pas d’un ordre d’arrêt de production. Journaux limités, droits minimaux, aucun secret exposé.

## Orchestration des quatre filières

Trois Astra spécialisés (Neurologie, Endocrinologie, Néphrologie) et parent Codex pour Hématologie/outillage : une seule leçon active par spécialité, intégration des fichiers partagés séquentielle par le parent. Chaque filière reprend un existant libre avant d’ouvrir un nouveau. Une réserve bloque la leçon concernée, pas les trois autres. Les avis de revue peuvent être relus par un autre agent seulement après son point de sauvegarde, sans lancer de cinquième agent ni prétendre à une validation humaine. Avant 08h Europe/Zurich, ne démarrer que ce qui peut être sauvegardé proprement ; conserver les travaux incomplets et leurs réserves.

Jalon suivant poussé : `4f92780d038dcb73cba79d24766659656c5ad27f`, flucytosine produit exact et statut suisse, 26 lectures ; [aperçu autonome de cette version](https://github.com/vialdjoukang-spec/Medina/blob/4f92780d038dcb73cba79d24766659656c5ad27f/docs/collaboration/ssp-v2/execution/ALPHA77-CODEX-G02-INTEGRATE/G02-apercu-autonome.html). La passe suivante traite les causes rares et la concordance des tableaux pharmacologiques. Chaque version reste un paquet de revue, pas une clôture médicale.


Actualisation 2026-11-02T03:11:23.408712+00:00 : G02 achevé dans le harness à03:10:39 UTC, après39lectures et revue auteur des14points/20rubriques. Version publiée sur branche `37a113894d55e7e0d5d3a1952d731fa689f641fb` ; [aperçu autonome](https://github.com/vialdjoukang-spec/Medina/blob/37a113894d55e7e0d5d3a1952d731fa689f641fb/docs/collaboration/ssp-v2/execution/ALPHA77-CODEX-G02-INTEGRATE/G02-apercu-autonome.html). SHA256 `76c59b4fba209a09fb186f6a5554541e81397722633547ce89a3b61ecda435db`. Limites L1–L6 maintenues ; aucune certification clinique, publication main ni audit indépendant revendiqués. Le reçu et sa représentation explicite de la matrice20 sont en cours de push séparé.


2026-11-02T03:12:01.786896+00:00 — Reçu final G02 poussé et vérifié : `a402352904ace3854e886740d97759a7de907db6`. [Aperçu autonome final](https://github.com/vialdjoukang-spec/Medina/blob/a402352904ace3854e886740d97759a7de907db6/docs/collaboration/ssp-v2/execution/ALPHA77-CODEX-G02-INTEGRATE/G02-apercu-autonome.html), SHA256 `76c59b4fba209a09fb186f6a5554541e81397722633547ce89a3b61ecda435db`. Contrôle de mission réussi sur ce commit exact ; achèvement projet enregistré à 03:10:39 UTC. Contenu et captures inchangés depuis la version précédente. Libération G02 puis acquisition G05 autorisées par le parent, sous réserve du registre réel.


G05 acquis réellement après libération G02 : registre `94514a6d560b60dcf9932d7ed3f7f904f179b541`, branche `codex/alpha77/g05-integrate-g1`, worktree `/workspace/Medina-neurologie-G05`. Start et claim réussis ; recherche seule au départ, aucune source héritée prétendue relue. Paquet final G02 conservé dans `completed_lessons`.


## G05 — achèvement réel 2026-11-02T04:17:49+00:00

Contenu poussé et vérifié : `07e2dc4b5a157e11060ba53f4f266ceb6aa282c8`. [Aperçu autonome actuel](/workspace/Medina-neurologie-G05/docs/collaboration/ssp-v2/execution/ALPHA77-CODEX-G05-INTEGRATE/G05-apercu-autonome.html), SHA `42d8f942ddaaba5709f87a88720e57cb5448d991785ea6a34ac4b4879b5bf8d0`. 47 lectures ciblées, 14/20 couverts, six sciences, neuf sections sémiologiques, deux originaux humains. [Reçu](/workspace/Medina-neurologie-G05/docs/collaboration/ssp-v2/execution/ALPHA77-CODEX-G05-INTEGRATE/harness-completion.json), [limites](/workspace/Medina-neurologie-G05/docs/collaboration/ssp-v2/execution/ALPHA77-CODEX-G05-INTEGRATE/lesson-manifest.json). Aucun audit indépendant ou médical humain revendiqué ; aucune PR/main. Le reçu final de branche sera ajouté après push.


## État courant — 2026-11-02T04:21:53.551738+00:00

G05 achevé à 04:17:49 UTC, poussé au commit `89113a86c9bc354c081cf0e1e6fbab4b1a91da24`, puis libéré au registre `9ae08824f8047a7a76a2a527813a6e83c525ded4`. [Aperçu de cette version](https://github.com/vialdjoukang-spec/Medina/blob/89113a86c9bc354c081cf0e1e6fbab4b1a91da24/docs/collaboration/ssp-v2/execution/ALPHA77-CODEX-G05-INTEGRATE/G05-apercu-autonome.html). 47 lectures ciblées, 14 points et 20 rubriques couverts ; auto-relecture, aucune certification clinique. I64 reste le prochain candidat existant Codex, sous réserve d’acquisition et de start/claim réels. Les inventaires initiaux ci-dessus sont historiques.


## I64 — livraison finale du 2 novembre 2026, 05:07 UTC

Achèvement réel, branche finale `b85aae199347d50025576f5155b7fe810546adb2` poussée et vérifiée ; réservation libérée. [Aperçu autonome](https://github.com/vialdjoukang-spec/Medina/blob/b85aae199347d50025576f5155b7fe810546adb2/docs/collaboration/ssp-v2/execution/ALPHA77-CODEX-I64-INTEGRATE/I64-apercu-autonome.html), SHA `3bd2f292131c8a1f9a94b5e76c97e37ca61e50d810af7a3e2eeef1b7c3b656a9`. 34 lectures ciblées, 14/20 couverts, 15 346 mots, 39 fenêtres, 5 quiz, six sciences, neuf sections. Deux originaux humains, trois occurrences ; 10 captures finales inspectées sur 20. Tests 1440/390/Livre 24 et source-binding exact réussis. Auto-relecture sans certification médicale. Huit limites explicites jugées non bloquantes, dont différences FI/protocoles et recouvrement temporaire du bouton Plan mobile. Aucun moteur/catalogue/main modifié.
