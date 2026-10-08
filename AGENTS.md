## Consigne la plus récente — chaîne continue, 8 octobre 2026

Lire d’abord [CONSIGNES_VIAL_2026-10-08_CHAINE_CONTINUE.pdf](docs/collaboration/instructions/CONSIGNES_VIAL_2026-10-08_CHAINE_CONTINUE.pdf) (source `.md` au même endroit) : il s’applique à Claude et à Codex. **Processus continu sans attendre de relance ; arrêt seulement après remise de tous ses fragments ou sur STOP de Vial ; une correction demandée passe en priorité puis la production reprend.** Claude achève toutes les catégories CIM de C-01-Cardiologie puis remet le fragment à Codex. **Chaque fragment, Claude ou Codex : toutes les catégories CIM reçoivent un cours, aucune lacune.** Sous-agents parallèles par catégorie, un auteur par fichier. Bouton « Isolate Federal – CH Exam » : `organisation/federal_exam.json`, `engine/federal_exam.*`. Pile visible : `organisation/PILE_FRAGMENTS.html` (`tools/pile_fragments.py`).

## Captures visibles dans le chat — 8 octobre 2026

Vial demande explicitement de voir les captures du travail sur les cours **ici, de manière dynamique**. Afficher les captures dans les messages et réponses avec une image visible, accompagnée du lien direct du cours ; les sorties techniques et les seuls liens de téléchargement ne suffisent pas. Pour présenter une navigation, produire une capture animée issue du navigateur réel et l’afficher directement. Garder le statut de version de travail et dater/versionner les captures ; ne pas inventer un rendu ni annoncer un flux en direct pour une animation enregistrée. Le workflow Pages publie les captures et l’animation sous `apercus/controle/` après les contrôles.

## Alignement avec Claude — police de lecture, 8 octobre 2026

Dernière instruction directe de Vial : « Pas de conflit avec Claude. Aligne toi avec la Police qu’il a trouvé ». **Atkinson Hyperlegible Next** devient la police par défaut du portail, des 22 frontends et des cours, avec les quatre WOFF2 de Claude (`f928674`). Cette consigne remplace la demande antérieure de police Anthropic Serif ; celle-ci reste une option du lecteur. Conserver les contributions de Claude, les contrastes élevés, le thème clair et la séparation des spécialités. Les réglages du lecteur s’appliquent au texte, aux fenêtres et à Navigo. Aucune modification de source médicale ni de statut de fragment n’est requise par cette consigne. Voir `docs/collaboration/FRONTENDS_2026-10-08.md` et son reçu d’alignement.

## Consigne frontend active — 8 octobre 2026

Vial demande un accès visuel aux cours, un accueil clair et agréable et une refonte majeure du frontend. **Chaque fragment possède son HTML et sa navigation propres, limités au contenu de sa spécialité.** Les cartes de catégories sont sobres, sur fond clair, avec un relief 3D discret ; la police par défaut est **Anthropic Serif authentique**, embarquée hors ligne. Le lecteur peut adapter sa police et sa taille. La classification frontend est centralisée dans `fragment_surface.py` ; les anciens rattachements anatomiques ne doivent pas réintroduire un cours étranger. L’aperçu de rédaction A41 est une consultation explicitement marquée « Version de travail » sous `apercus/infectiologie.html`, sans injection canonique, sans certification finale et sans remise pour audit du fragment incomplet. Lire `docs/collaboration/FRONTENDS_2026-10-08.md`.

## Consigne active — reprise et fragments entiers, 8 octobre 2026

Vial demande de prendre connaissance de `Prompt_Codex.pdf` et de continuer. Cette reprise lève le STOP antérieur. Lire [COORDINATION.md](COORDINATION.md) et [le protocole par fragment](docs/collaboration/PROTOCOLE_FRAGMENTS_2026-10-08.md) avant les instructions historiques ci-dessous. **Fragment entier complet et auto-revu avant transmission ; audit croisé unique, correction et injection par l’autre IA ; fragment INJECTÉ immuable ; arrêt après les 22 ; HTML clair exclusivement.** Les règles de remise par chapitre, d’injection autonome avant audit, de renvois successifs et de correction après injection sont remplacées. Les travaux et leurs preuves restent conservés. Le mode multi-agent et un auteur par fichier restent applicables ; les veilles automatiques restent en pause.

# Collaboration MEDINA

## Consigne la plus récente — STOP Codex, 8 octobre 2026

Vial demande : « injecte ce qu'il faut injecter puis STOP. je vais changer les règles ». Codex a terminé le contrôle des dernières remises et s’arrête : aucune nouvelle production, correction, injection, veille ou relance de ses sous-agents avant les nouvelles instructions. Les sources I83 v6 sont déjà injectées et leur publication vérifiée. I89, J45 et A41 restent non injectables pour les motifs consignés dans [ARRET_CODEX_2026-10-08.md](docs/collaboration/ARRET_CODEX_2026-10-08.md). La veille locale Codex est arrêtée et la veille GitHub automatique mise en pause ; ne pas les relancer au démarrage. Les répartitions et travaux ci-dessous sont conservés, sans valoir ordre de reprise.

## Répartition des 21 fragments restants — 8 octobre 2026

Lire [FRAGMENTS_RESTANTS.md](docs/collaboration/FRAGMENTS_RESTANTS.md) et [production_plan.json](organisation/production_plan.json) : **11 fragments entiers Claude, 10 fragments entiers Codex**, hors cardiologie. Toutes les catégories restent regroupées sous leur fragment. Chaque catégorie ou chapitre cité porte **code — intitulé (libellé complet du fragment)**, par exemple **J45 — Asthme (P-02-Pneumologie)**. Un seul fragment et **un seul chapitre en production par agent**, un chapitre par remise. Produire le chapitre complet et le remettre à l’autre IA pour audit avant de commencer le suivant ; les corrections reçues restent prioritaires. Les audits, injections et publications des chapitres déjà remis sont suivis séparément et conservent leurs contrôles. Les files respectent les rangs du registre. La nouvelle consigne active la chaîne Codex sur I-03-Infectiologie ; la cardiologie et ses réserves restent conservées dans le backlog. Lire [CODEX_CHAINE_FRAGMENTS.md](docs/collaboration/CODEX_CHAINE_FRAGMENTS.md) pour les vagues de sous-agents et les sentinelles. Aucun fragment n’est déclaré complet par cette attribution. Cette règle de progression prime sur les anciennes consignes de production par lots ou cycles pour les travaux nouveaux.

La session Codex actuelle prend le relais de GPT « work » comme coordinateur prioritaire ; conserver les travaux et commits antérieurs. **Mode multi-agent obligatoire** : Claude et Codex progressent en parallèle, avec plusieurs sous-agents spécialisés dans le seul chapitre actif de chacun et un auteur par fichier. **Claude audite les chapitres Codex avant leur injection. Claude peut injecter ses propres chapitres après revue interne et contrôles complets ; Codex les audite ensuite dans l’ordre de [FILE_AUDIT_CODEX.json](docs/collaboration/FILE_AUDIT_CODEX.json)**. Appliquer [REGLES_INJECTION_CLAUDE.md](docs/collaboration/REGLES_INJECTION_CLAUDE.md) : aucune réserve bloquante ouverte, toutes les conditions obligatoires vérifiées ; une erreur médicale démontrée reste prioritaire. Les chapitres Claude attendent l’audit sous la mention « en audit croisé » ; les désaccords non bloquants de leurs chapitres sont tranchés par Claude. La mission précise de Claude est [CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES.md](docs/collaboration/CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES.md).


Vial autorise en permanence les publications et intégrations GitHub du projet. Lire `CLAUDE.md`, `docs/collaboration/README.md` et les instructions actuelles avant de modifier le contenu.


## Précisions durables de Vial — 8 octobre 2026

Lire [les consignes communes d’interaction, densité et sources](docs/collaboration/CONSIGNES_INTERACTION_DENSITE_SOURCES.md). Le parallélisme répartit les catégories et sujets du **même chapitre** entre sous-agents, avec un auteur par fichier. Les explications sont accessibles après clic sur le mot interactif ; les tableaux servent les classifications et énumérations quand ils clarifient le contenu, avec des cellules courtes et cohérentes. Aucun plafond de mots arbitraire. Pour un contentieux clinique, **la source primaire applicable la plus récente l’emporte** ; présenter le choix dans une fenêtre liée à un mot vert, avec accès au texte actuellement en vigueur même s’il est ancien. Compendium est un accès utile aux monographies suisses, à lire et dater réellement. Ne pas assimiler revue IA, tests et validation par un médecin.

## Nomenclature et livraisons — exigence du 7 octobre 2026

Toute leçon doit être nommée **code CIM + intitulé complet**, y compris dans les liens, rapports et navigations. Tout fragment doit porter **initiale de la spécialité - rang de production à deux chiffres - nom littéral**, par exemple `C-01-Cardiologie`. Le registre partagé est `organisation/fragments.json` ; les identifiants techniques S01…T7 et les routes restent stables.

Consulter `organisation/MEDINA_Organisation.html` et `docs/collaboration/DELIVERY_PROTOCOL.md`. Remettre les sources sous `livraisons/Livraison Codex/<libellé>/` ; Claude dépose ses corrections sous `livraisons/Livraison Claude/<libellé>/`. Relire et vérifier l'injection dans les sources canoniques avant reconstruction et publication. Ne jamais déclarer un fragment achevé sur la seule présence d'un cours ou d'un regroupement `covers` : l'objectif de complétude porte sur la CIM-11, dont l'inventaire validé manque encore.

## À chaque reprise et avant une livraison

1. Vérifier les têtes GitHub de `main`, de la branche d'intégration et de **toutes les branches et PR**, avec leurs pages suivantes. Le clone local et la seule branche `claude/review-…` ne constituent pas un inventaire distant.
2. Exécuter `python3 tools/collaboration_sync.py --out docs/collaboration`. Si l'accès shell GitHub est bloqué, collecter les mêmes données par le connecteur puis utiliser `--snapshot <fichier.json>`. Lire `DELIVERIES_LATEST.md` et les contributions en attente avant de commencer un nouveau lot.
3. Accepter aussi les anciens rapports à plat, branches sans PR et patchs remis. Un manifeste ou un nouvel emplacement facilite le suivi ; son absence ne justifie pas d'ignorer une livraison.
4. Ouvrir rapport et diff ; enregistrer la réception. Rattacher chaque modification à ses sources et aux fragments réellement consommateurs. Reconstruire les HTML ; modifier uniquement une sortie générée ne constitue pas une intégration.
5. Conserver les commits et rapports du contributeur. Documenter les adaptations, conflits et réserves. Ne pas déplacer sa branche pour la remettre artificiellement au niveau de la nôtre.
6. Après contrôle, publier le commit d'intégration et un reçu sous `docs/collaboration/receipts/`, puis actualiser l'index et `HANDOFF_LATEST.md`. Citer le SHA exact, les chemins, les contrôles exécutés et les réserves. Vérifier la disponibilité distante avant d'annoncer le résultat.

« Repéré », « reçu », « intégré » et « contrôlé techniquement » désignent des preuves différentes. La fusion d'une relecture ciblée ne certifie ni les 30 cours ni la complétude CIM-11. Une branche publiée ne prouve pas que le site utilisant `main` a été reconstruit : vérifier séparément le déploiement.

## Mécanismes — nouvelle priorité

Chaque affirmation médicale doit comporter une justification causale ou clinique précise, ses limites et sa source. Préférer les mots cliquables et fenêtres contextualisées. Cette règle couvre les quatre onglets et tous les contenus associés. Priorité actuelle : les 20 cours présents du Fragment 01 sont répartis 10 Codex / 10 Claude, dans `docs/collaboration/MECHANISMS_PLAN.json` ; consigne opérationnelle `MECHANISMS_CLAUDE.md`. Ne jamais confondre enrichissement ciblé et relecture exhaustive. J40 — Bronchite est ajouté comme production distincte couvrant J20/J40/J41/J42. La complétude CIM-11 reste à établir.
