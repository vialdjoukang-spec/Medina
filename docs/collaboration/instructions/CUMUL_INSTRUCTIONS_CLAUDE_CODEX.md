# MEDINA — Cumul obligatoire des instructions validées pour Claude Code et Codex

Version exhaustive du 8 octobre 2026, établie par Claude Code à la demande du Dr Vial Tato Djoukang, propriétaire de MEDINA. Ce document remplace entièrement la version courte publiée au commit `c04ac54`. Il recense toutes les instructions de Vial et toutes les règles de projet écrites dans le dépôt depuis le début, puis sépare les règles **en vigueur** des règles **remplacées**. Il s’applique à parts égales à Claude Code et à Codex.

## Préambule — caractère OBLIGATOIRE de chaque règle

- **Chaque règle de ce cumul est OBLIGATOIRE.** Aucune règle n’est facultative, indicative ou laissée à l’appréciation de l’IA qui produit, audite ou injecte.
- **Toute dérogation exige l’accord écrit de Vial.** Une IA qui ne peut pas respecter une règle s’arrête sur le point concerné, consigne le blocage avec ses preuves et le signale ; elle ne contourne jamais la règle.
- Une règle formulée « Il est obligatoire de » impose une action. Une règle formulée « Il est interdit de » proscrit une action sans exception.
- Les documents sources restent la référence de détail. Chaque règle cite sa source entre parenthèses, avec sa date. Aucune règle de ce cumul n’a été ajoutée sans source écrite dans le dépôt.
- Une règle remplacée figure uniquement dans l’**annexe A** ; elle ne s’applique plus. Les points dont la portée reste à trancher par Vial figurent dans l’**annexe B** ; dans l’attente, la règle la plus exigeante pour la qualité s’applique.
- Codex confirme sa lecture et son application intégrale en remplissant la liste de contrôle de l’**annexe C**.

## 0. Règles de préséance

- **R-0.1** Il est obligatoire d’appliquer la règle la plus récente lorsque deux instructions se contredisent. (CUMUL v1, COORDINATION.md, 08.10.2026)
- **R-0.2** Il est obligatoire d’appliquer la règle la plus exigeante pour la qualité lorsque deux instructions de même date divergent. (CONSIGNES_VIAL_2026-10-08_CHAINE_CONTINUE, § 2 bis, 08.10.2026)
- **R-0.3** Il est obligatoire de respecter l’ordre de priorité suivant en cas de conflit de fond : exactitude médicale, exhaustivité, pédagogie, interface, économie. (PROMPT_MEDINA, préambule, 25.09.2026)
- **R-0.4** Il est interdit d’appliquer une disposition d’une section marquée « remplacé », « historique » ou « abandonnée » lorsqu’elle est incompatible avec une règle en vigueur ; ses travaux et preuves restent conservés. (bandeaux des documents de collaboration, 08.10.2026)
- **R-0.5** Il est obligatoire d’appliquer les dispositions compatibles des documents portant le bandeau « Protocole remplacé pour les travaux nouveaux », puisque seules leurs dispositions incompatibles sont devenues historiques. (bandeaux de DELIVERY_PROTOCOL, CONSIGNES_INTERACTION, CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES, CODEX_CHAINE_FRAGMENTS, 08.10.2026)
- **R-0.6** Il est obligatoire de lire, à chaque reprise et avant toute production, ce cumul, `CONSIGNES_VIAL_2026-10-08_CHAINE_CONTINUE`, `COORDINATION.md` et `PROTOCOLE_FRAGMENTS_2026-10-08.md`. (CONSIGNES chaîne continue, § 8 ; CLAUDE.md, 08.10.2026)
- **R-0.7** Il est interdit de considérer une mention historique « achevé », « audité » ou « 20/20 » comme une certification au regard des exigences actuelles. (PROMPT_MEDINA, exigences du 07.10.2026)

## 1. Gouvernance et rôles

- **R-1.1** Il est obligatoire de reconnaître le Dr Vial Tato Djoukang comme seul propriétaire de MEDINA et seule autorité qui fixe, modifie ou suspend les règles. (CLAUDE.md ; PROMPT_MEDINA, § 0)
- **R-1.2** Il est obligatoire de traiter Claude Code et Codex comme deux producteurs symétriques : chacun produit ses fragments et audite ceux de l’autre. (Prompt_Codex_2026-10-08 ; PROTOCOLE_FRAGMENTS, 08.10.2026)
- **R-1.3** Il est obligatoire de respecter l’attribution des fragments : Claude produit C-01-Cardiologie (fragment entier remis à Codex), puis P-02, G-04, E-06, H-08, G-10, M-12, R-14, O-17, O-18, M-19 et E-22 ; Codex produit I-03, N-05, N-07, O-09, O-11, I-13, U-15, D-16, D-20 et M-21. (COORDINATION.md ; FRAGMENTS_RESTANTS ; CONSIGNES chaîne continue, § 2 et § 7, 08.10.2026)
- **R-1.4** Il est obligatoire que Codex audite les fragments de Claude et que Claude audite les fragments de Codex. (PROTOCOLE_FRAGMENTS ; production_plan.json, `cross_audit`, 08.10.2026)
- **R-1.5** Il est obligatoire de suivre chaque file dans l’ordre du registre `organisation/production_plan.json`. (FRAGMENTS_RESTANTS ; production_plan.json, 08.10.2026)
- **R-1.6** Il est interdit de redistribuer des catégories entre les IA : chaque fragment est attribué en entier avec toutes ses catégories et sous-catégories. (production_plan.json, `grouping_policy` ; FRAGMENTS_RESTANTS, 08.10.2026)
- **R-1.7** Il est obligatoire de faire produire un cours commun par un producteur unique et de le relier par des renvois contrôlés dans les fragments consommateurs ; ainsi M30 — Périartérite noueuse et affections apparentées (R-14-Rhumatologie et orthopédie) renvoie au cours M31 — Vascularites systémiques (I-13-Immunologie et allergologie), produit par Codex. (CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES, § 2 ; CODEX_CHAINE_FRAGMENTS, 08.10.2026)
- **R-1.8** Il est interdit de doubler le travail de l’autre IA ; avant d’ouvrir un cours, il est obligatoire de consulter la pile, les espaces de remise et les zones de travail. Un cours existant ou déposé est repris, jamais réécrit en parallèle. (message de Vial à Codex ; AGENTS.md ; CLAUDE.md, 08.10.2026)
- **R-1.9** Il est obligatoire de conserver les travaux, commits et contributions antérieurs, y compris ceux de la session GPT « work » et de la branche Alpha. (CLAUDE.md ; FRAGMENTS_RESTANTS, 08.10.2026)
- **R-1.10** Il est obligatoire de désigner, dans chaque IA, un intégrateur unique qui tient les registres de travail, la pile et les reconstructions. (CONSIGNES chaîne continue, § 5, 08.10.2026)

## 2. Communication avec Vial

- **R-2.1** Il est obligatoire de répondre à Vial en français, sur un ton chaleureux, avec des réponses structurées (titres, gras, tableaux), denses et sans remplissage. (CLAUDE.md ; PROMPT_MEDINA, § 0 ; PROMPT_REPRISE_IA, § 6)
- **R-2.2** Il est obligatoire d’interpréter les approximations de transcription, car Vial dicte souvent ses messages. (CLAUDE.md ; PROMPT_MEDINA, § 0)
- **R-2.3** Il est interdit de corriger le texte propre de Vial sans demande de sa part. (CLAUDE.md)
- **R-2.4** Il est obligatoire de livrer sans demander d’accord lorsque les contrôles passent ; il est interdit de solliciter Vial hors d’un échec d’audit ou d’un blocage réel. (CLAUDE.md ; PROMPT_MEDINA, § 0, 26.09.2026)
- **R-2.5** Il est interdit d’écrire des phrases étranges, du bavardage ou des formules creuses dans les messages, rapports et confirmations ; il est obligatoire d’écrire en français professionnel, en phrases complètes et avec un contenu vérifiable. (CUMUL v1, § 0 ; CONSIGNES chaîne continue, § 6 bis, 08.10.2026)
- **R-2.6** Il est obligatoire, pour Codex, de confirmer à Vial la détection de tout le cumul des instructions en remplissant l’annexe C. (message de Vial à Codex, 08.10.2026)
- **R-2.7** Il est obligatoire de fonder chaque annonce à Vial sur des SHAs, des rapports, des contrôles et des liens vérifiables, en distinguant les états attribué, actif, livré, reçu, audité, injecté, contrôlé et publié. (CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES, § 8 ; CODEX_CHAINE_FRAGMENTS, 08.10.2026)
- **R-2.8** Il est obligatoire de nommer chaque remise, audit et injection signalé à Vial par son code, son intitulé complet et son fragment. (FRAGMENTS_RESTANTS ; CODEX_CHAINE_FRAGMENTS, 08.10.2026)

## 3. Processus continu

- **R-3.1** Il est interdit d’attendre que Vial demande de continuer : après chaque livraison, la tâche suivante de la file démarre immédiatement. (CONSIGNES chaîne continue, § 1, 08.10.2026)
- **R-3.2** Il est obligatoire de poursuivre le processus jusqu’à ce que tous les fragments attribués soient rédigés, auto-revus et transférés à l’autre IA pour audit, sauf STOP explicite de Vial. (CONSIGNES chaîne continue, § 1, 08.10.2026)
- **R-3.3** Il est obligatoire de traiter une correction demandée par Vial en priorité absolue, de la livrer, de la signaler, puis de reprendre la production là où elle s’était arrêtée. (CONSIGNES chaîne continue, § 1, 08.10.2026)
- **R-3.4** Il est interdit de traiter une interruption pour correction comme un STOP. (CONSIGNES chaîne continue, § 1, 08.10.2026)
- **R-3.5** Il est obligatoire de laisser les sous-agents de production continuer pendant une correction ; seul le fichier corrigé reste verrouillé jusqu’à sa livraison. (CONSIGNES chaîne continue, § 1, 08.10.2026)
- **R-3.6** Il est obligatoire de traiter en priorité, sur la production en cours, toute correction reçue de l’autre IA et toute erreur médicale démontrée. (CONSIGNES_INTERACTION ; REGLES_VIAL c68d96a, § 1, 08.10.2026)
- **R-3.7** Il est obligatoire, lorsqu’un chapitre est bloqué, de consigner la lacune et de poursuivre les travaux utiles du même fragment. (production_plan.json, `blocked_chapter_policy`, 08.10.2026)
- **R-3.8** Il est obligatoire de limiter la préparation du fragment suivant, pendant l’audit du fragment précédent, à l’inventaire, à la pile et aux recherches ; il est interdit de rouvrir un fragment INJECTÉ à cette occasion. (CONSIGNES chaîne continue, § 5, 08.10.2026)

## 4. Organisation en 22 fragments et nommage

- **R-4.1** Il est obligatoire de structurer l’atlas en exactement 22 fragments, selon la hiérarchie Fragment → Catégories → Chapitres. (Prompt_Codex_2026-10-08 ; PROTOCOLE_FRAGMENTS, 08.10.2026)
- **R-4.2** Il est obligatoire de nommer un fragment par initiale de la spécialité, rang de production à deux chiffres et nom littéral, selon `organisation/fragments.json` (par exemple `C-01-Cardiologie`). (CLAUDE.md ; AGENTS.md, 07.10.2026)
- **R-4.3** Il est obligatoire de nommer chaque leçon par son code CIM et son intitulé complet, y compris dans les liens, rapports et navigations. (CLAUDE.md ; AGENTS.md, 07.10.2026)
- **R-4.4** Il est obligatoire de citer chaque catégorie ou chapitre sous la forme **code — intitulé (libellé complet du fragment)**, par exemple **J45 — Asthme (P-02-Pneumologie)**. (CLAUDE.md ; production_plan.json, `category_label_format`, 08.10.2026)
- **R-4.5** Il est obligatoire de conserver stables les identifiants techniques S01…T7, les routes et les champs `code`, `title` et `fragment_id`. (AGENTS.md, 07.10.2026 ; CODEX_CHAINE_FRAGMENTS, 08.10.2026)
- **R-4.6** Il est obligatoire d’employer les codes CIM-10-GM 2024 du catalogue local tant que la cartographie CIM-11 n’est pas établie. (CLAUDE.md, 07.10.2026)
- **R-4.7** Il est obligatoire de structurer les plateformes par catégories CIM : numéro de catégorie, chapitres numérotés dans la catégorie, code discret en haut à droite et couleur vive lisible. (CLAUDE.md, 07.10.2026)
- **R-4.8** Il est obligatoire de choisir les chapitres d’un fragment selon les priorités du registre, puis l’ordre du catalogue, en reprenant d’abord un cours existant dont la revue exhaustive reste ouverte. (production_plan.json, `chapter_order` ; FRAGMENTS_RESTANTS, 08.10.2026)
- **R-4.9** Il est obligatoire de fixer le champ `wave` d’un chapitre d’après le champ `system` de ses catégories dans `medora-data`, jamais par supposition. (CLAUDE.md, règle 8 ; PROMPT_MEDINA, § 19.2)
- **R-4.10** Il est obligatoire de tenir le psychisme hors de la carte des 22 fragments, conformément au périmètre demandé. (FRAGMENTS.md)
- **R-4.11** Il est obligatoire, pour un axe transversal encore sans catégories, de définir son inventaire et ses identifiants dans les sources canoniques avant toute réservation ; il est interdit d’inventer un code CIM pour réserver un thème. (FRAGMENTS_RESTANTS, § progression, 08.10.2026)

## 5. Complétude CIM

- **R-5.1** Il est obligatoire de donner un cours fondé sur la CIM à chaque catégorie CIM rattachée au fragment, seul ou regroupé dans un cours déclaré (`covers`) ; il est interdit de laisser une catégorie sans cours. (CONSIGNES chaîne continue, § 2 bis, 08.10.2026)
- **R-5.2** Il est obligatoire de dresser l’inventaire exhaustif des catégories du fragment au démarrage, de le publier dans la pile et de démontrer à la remise que chaque catégorie est couverte. (CONSIGNES chaîne continue, § 2 bis, 08.10.2026)
- **R-5.3** Il est obligatoire de vérifier chaque code dans la CIM-10-GM 2024 du BfArM avant de le déclarer dans `covers`. (PROMPT_MEDINA, § 9.1)
- **R-5.4** Il est obligatoire de viser la complétude CIM-11 : toutes les catégories et sous-catégories pertinentes de chaque système doivent posséder un enseignement spécifique, accessible et relu. (COMPLETUDE_CIM11 ; CLAUDE.md, 07.10.2026)
- **R-5.5** Il est obligatoire d’inventorier la CIM-11 MMS version 2026-01 en français (OMS) avec code, identifiant d’entité, intitulé, parent, version, URL et rattachements pédagogiques. (COMPLETUDE_CIM11, 07.10.2026)
- **R-5.6** Il est obligatoire de tenir la matrice CIM-11 par entité : référence, système MEDINA, enseignement (fichier, cours, onglet, repère stable), couverture, accès vérifié, relecture et état (absent, plan, rédigé, intégré, relu, contrôlé). (COMPLETUDE_CIM11, 07.10.2026)
- **R-5.7** Il est interdit de supposer des correspondances CIM-10 → CIM-11 bijectives ou de les déduire de la ressemblance des intitulés. (COMPLETUDE_CIM11 ; CLAUDE_AUDIT_GLOBAL, 07.10.2026)
- **R-5.8** Il est obligatoire d’afficher « couverture CIM-11 non établie » tant que l’inventaire officiel n’est pas constitué et contrôlé ; il est interdit de calculer un pourcentage CIM-11 à partir du catalogue CIM-10. (COMPLETUDE_CIM11, 07.10.2026)
- **R-5.9** Il est interdit de déclarer un fragment complet sur la seule présence d’un titre, d’un code, d’un compteur, d’un `covers`, d’une valeur `DONE_SYS` ou d’un renvoi vers un cours futur. (COMPLETUDE_CIM11 ; AGENTS.md, 07.10.2026)
- **R-5.10** Il est obligatoire de laisser chaque entité partagée visible dans chacun des systèmes concernés, avec un lien vers le passage qui la traite effectivement, et de la compter dans le dénominateur de chacun. (COMPLETUDE_CIM11, 07.10.2026)
- **R-5.11** Il est interdit d’utiliser un regroupement de maladies pour omettre leurs particularités diagnostiques et thérapeutiques. (COMPLETUDE_CIM11, 07.10.2026)
- **R-5.12** Il est obligatoire de présenter séparément la couverture CIM, le nombre de cours, la qualité linguistique, l’exactitude médicale et la réussite technique. (COMPLETUDE_CIM11, 07.10.2026)

## 6. Production, remise, audit croisé, injection et garde CI

- **R-6.1** Il est obligatoire de produire intégralement le fragment actif avant de le transmettre ; il est interdit de transmettre ou d’injecter un fragment incomplet. (Prompt_Codex ; PROTOCOLE_FRAGMENTS ; production_plan.json, 08.10.2026)
- **R-6.2** Il est obligatoire de conduire une auto-revue rigoureuse du fragment entier (exactitude clinique, cohérence entre surfaces, actualité des recommandations, intégrité et accessibilité des sources) et de corriger avant transmission. (PROTOCOLE_FRAGMENTS, 08.10.2026)
- **R-6.3** Il est interdit de présenter une revue interne de sous-agents comme l’audit externe de l’autre IA ou comme une validation médicale humaine. (PROTOCOLE_FRAGMENTS, 08.10.2026)
- **R-6.4** Il est interdit au producteur d’écrire dans les sources canoniques (`chapters/`, `glossary/`, `chapters.json`) ; ses cours vivent dans `livraisons/Livraison <IA>/<fragment>/travail/sources/`. (CONSIGNES chaîne continue, § 5 ; commit 07a663e, 08.10.2026)
- **R-6.5** Il est obligatoire de remettre le fragment dans `espace_partage/FRAGMENTS_<IA>_A_AUDITER_PAR_<autre IA>/<fragment>/` avec `REMISE.md`, `MANIFESTE.json`, `sources/` et `chapters_additions.json`. (CONSIGNES chaîne continue, § 5 ; commit 0bdb60c, 08.10.2026)
- **R-6.6** Il est obligatoire de transmettre la remise sur un commit exact, avec inventaire de couverture catégorie → cours, fichiers, empreintes SHA-256, rapport interne, sources et contrôles. (PROTOCOLE_FRAGMENTS, 08.10.2026)
- **R-6.7** Il est obligatoire de conduire l’audit croisé en un seul tour : l’auditeur relit le fragment entier, corrige lui-même, injecte la version finale dans les sources canoniques et reconstruit la plateforme HTML. (Prompt_Codex ; PROTOCOLE_FRAGMENTS, 08.10.2026)
- **R-6.8** Il est interdit de renvoyer le fragment au producteur pour un nouveau tour (« ping-pong ») et il est interdit d’injecter un fragment sur la base d’un auto-audit. (Prompt_Codex ; PROTOCOLE_FRAGMENTS, 08.10.2026)
- **R-6.9** Il est obligatoire, si une source ou un contrôle indispensable manque pendant l’audit, de consigner le blocage dans le même tour et de conserver la version non injectée ; il est interdit de déclarer favorable une vérification inachevée. (PROTOCOLE_FRAGMENTS, 08.10.2026)
- **R-6.10** Il est obligatoire de consigner les états et preuves finaux des fragments dans `organisation/fragment_status.json`. (PROTOCOLE_FRAGMENTS ; COORDINATION.md, 08.10.2026)
- **R-6.11** Il est obligatoire de faire passer toute modification canonique par la garde `tools/espace.py garde <avant> <après>`, qui refuse une écriture canonique sans les preuves d’un fragment entier audité. (PROTOCOLE_FRAGMENTS ; CONSIGNES chaîne continue, § 5, 08.10.2026)
- **R-6.12** Il est interdit d’utiliser les anciennes commandes de remise, d’audit ou d’injection par cours, désactivées pour empêcher une injection partielle. (PROTOCOLE_FRAGMENTS, 08.10.2026)
- **R-6.13** Il est obligatoire de traiter le statut INJECTÉ comme terminal : aucun moteur ne rouvre, n’enrichit ni ne corrige un fragment injecté. (Prompt_Codex ; PROTOCOLE_FRAGMENTS ; production_plan.json, 08.10.2026)
- **R-6.14** Il est interdit d’attribuer le statut INJECTÉ à un fragment entier du fait de l’injection historique d’un chapitre isolé. (PROTOCOLE_FRAGMENTS ; COORDINATION.md, 08.10.2026)
- **R-6.15** Il est obligatoire de poursuivre un chapitre achevé dans les sources de travail du fragment, sans remise pour audit final d’un chapitre isolé. (production_plan.json, `next_chapter_gate` ; PROTOCOLE_FRAGMENTS, 08.10.2026)
- **R-6.16** Il est obligatoire, pour l’auditeur, de vérifier les seuils, doses, unités et délais dans les recommandations effectivement consultées, d’identifier chaque anomalie par fichier et repère avec gravité, raison, source et correction, et de laisser en réserve toute affirmation non vérifiée. (CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES, § 6, 08.10.2026)
- **R-6.17** Il est interdit d’injecter un contenu porteur d’une erreur médicale, d’une réserve majeure non résolue, d’une perte de contenu utile ou d’un contrôle requis en échec. (CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES, § 6 ; CODEX_CHAINE_FRAGMENTS, 08.10.2026)
- **R-6.18** Il est obligatoire de motiver explicitement dans le reçu toute observation mineure laissée ouverte ; il est interdit de la masquer par une mention globale « validé ». (CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES, § 6, 08.10.2026)
- **R-6.19** Il est obligatoire, pour l’auditeur, de contrôler la liste « Examen fédéral » du fragment et sa Sémiologie CS. (CONSIGNES chaîne continue, § 3 et § 6 bis, 08.10.2026)
- **R-6.20** Il est obligatoire de conserver les données déjà vérifiées en texte intégral exactement et de consigner toute donnée nouvelle avec sa source primaire, son URL et sa date. (PASSATION_REECRITURE, § 6 ; STYLE_REDACTION, § 7)
- **R-6.21** Il est obligatoire de prendre les remises A41 et J45 antérieures de l’espace partagé comme provenance conservée, et non comme un ordre d’audit final de fragment. (COORDINATION.md ; PROTOCOLE_FRAGMENTS, 08.10.2026)

## 7. Parallélisme

- **R-7.1** Il est obligatoire de travailler en mode multi-agent : plusieurs sous-agents en parallèle, chacun responsable d’une catégorie, ou d’un cours regroupant plusieurs catégories, du fragment actif. (CONSIGNES chaîne continue, § 5, 08.10.2026)
- **R-7.2** Il est obligatoire de respecter un auteur par fichier : un sous-agent n’écrit que les fichiers de son cours ; les autres agents relisent. (CONSIGNES chaîne continue, § 5 ; CONSIGNES_INTERACTION, 08.10.2026)
- **R-7.3** Il est interdit à deux sous-agents d’écrire simultanément dans un même HTML, glossaire, manifeste, banque JSON ou fichier partagé. (CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES, § 3 ; FRAGMENTS_RESTANTS, 08.10.2026)
- **R-7.4** Il est interdit aux sous-agents de lancer une commande Git qui modifie l’état (`checkout`, `reset`, fusion, commit) ; seul le responsable fige les commits et assemble. (PASSATION_REECRITURE, § 6 ; CODEX_CHAINE_FRAGMENTS, 08.10.2026)
- **R-7.5** Il est obligatoire de modifier les fichiers partagés par remplacement exact, jamais par réécriture complète. (PASSATION_REECRITURE, § 6)
- **R-7.6** Il est obligatoire de donner à chaque sous-agent sa désignation `code — intitulé (libellé complet du fragment)`, le SHA de départ, ses chemins modifiables, ses chemins en lecture seule, les notions attendues, les références à vérifier et le format de remise. (CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES, § 3 ; CODEX_CHAINE_FRAGMENTS, 08.10.2026)
- **R-7.7** Il est obligatoire, avant d’ajouter une clé de glossaire, de vérifier qu’un autre rédacteur ne l’a pas déjà créée et de ne garder qu’une définition en cas de doublon. (PROMPT_MEDINA, § 17)
- **R-7.8** Il est obligatoire de relire la tête partagée avant toute réservation, injection ou libération, puisque le plan n’est pas un verrou distant, et de signaler toute concurrence. (FRAGMENTS_RESTANTS ; CODEX_CHAINE_FRAGMENTS, 08.10.2026)
- **R-7.9** Il est interdit d’exposer les procédures internes des agents dans les cours. (CONSIGNES_INTERACTION, 08.10.2026)

## 8. Contrat HTML du chapitre

- **R-8.1** Il est obligatoire de répartir un chapitre en `chapters/<CODE>/<CODE>_a.html` à `_d.html` et en fenêtres `<CODE>_pop*.html`, dans l’espace de travail du producteur jusqu’à l’injection. (CLAUDE.md, règle 2 ; PROMPT_MEDINA, § 4.1)
- **R-8.2** Il est obligatoire d’ouvrir `_a.html` par `<template id="ch-<CODE>"><div class="chap">`, l’en-tête `chap-head` (code, couverture, CIM-10-GM 2024, système ; `h1` ; `span.status`), la barre de quatre onglets `data-p="pA|pE|pS|pP"`, puis le panneau `pA` avec `nav.toc ui` et `div.chap-body`. (PROMPT_MEDINA, § 4.1)
- **R-8.3** Il est obligatoire de fermer `pA` dans `_b.html` par les références `div.src` puis le `pager` (îlot précédent, îlot suivant), de placer `pE` et `pS` dans `_c.html` et `pP` dans `_d.html`, fermé par `</div></template>`. (PROMPT_MEDINA, § 4.1)
- **R-8.4** Il est obligatoire de conserver les quatre onglets : Pathologie et prise en charge, Examens complémentaires, Sciences fondamentales spécialisées, Pharmacologie. (CLAUDE.md, règle 2 ; PROTOCOLE_FRAGMENTS, 08.10.2026)
- **R-8.5** Il est interdit d’utiliser une classe hors de la liste fermée : `alert card chap chap-body chap-head code fb ilot k key lab maj n next pager panel pareto-btn prev quiz ratio sci sci-bar sci-body src ssp status t tabs toc trap two ui w`, plus `small` dans les fenêtres. (PROMPT_MEDINA, § 4.2)
- **R-8.6** Il est interdit d’ajouter un attribut `style` en ligne dans un chapitre. (PASSATION_REECRITURE, § 6 ; STYLE_REDACTION, § 8)
- **R-8.7** Il est obligatoire d’employer le balisage exact des îlots, mots verts, encadrés `key`, pièges `trap`, alertes, deux colonnes, tableaux `table.t`, quiz, boutons et fenêtres Pareto, figures, mises à jour `span.maj` et références `div.src`. (PROMPT_MEDINA, § 4.2)
- **R-8.8** Il est obligatoire de préfixer les identifiants par le code en minuscules : `<code>-0…`, `<code>-e-n`, `<code>-p-n`, `<code>-s-…` ; toute nouvelle clé de fenêtre commence par `<code>-` et toute clé Pareto par `pareto-<code>-`. (CLAUDE.md, règle 2 ; PROMPT_MEDINA, § 4.3)
- **R-8.9** Il est obligatoire que chaque `data-k` possède son `template data-pop`. (CHAPTER_SPEC, § 3 ; MISSION_JUSTIFICATION, 07.10.2026)
- **R-8.10** Il est interdit de modifier une fenêtre d’un autre chapitre ; sa réutilisation n’est permise que si son contenu convient exactement. (PROMPT_MEDINA, § 4.3 ; CHAPTER_SPEC, § 3)
- **R-8.11** Il est interdit de modifier le chapitre modèle `chapters/I50/`. (PROMPT_MEDINA, § 2)
- **R-8.12** Il est obligatoire de dessiner les figures SVG en noir et blanc (trait `#222`), avec légende numérotée, `viewBox` lisible à 380 px, texte d’au moins 10,5 unités, normal avant pathologique et échelle sur les courbes chiffrées. (PROMPT_MEDINA, § 4.4)
- **R-8.13** Il est obligatoire de déclarer chaque cours avec `code`, `covers`, `title`, `integrated`, `wave` et `added`, l’injection dans `chapters.json` revenant à l’auditeur par `chapters_additions.json`. (PROMPT_MEDINA, § 6.1 ; CONSIGNES chaîne continue, § 5, 08.10.2026)
- **R-8.14** Il est obligatoire de conserver les identifiants, routes et fonctions de lecture, ainsi que les fonctions globales de la coque (`pageTitle`, `SM`, `EM`, `route`, `context`, `crumbs`, `url`, `h`, `nextPrevious`, `entryPage`, `render`, `MEDINA_mount`) ; il est interdit de les renommer. (PROMPT_MEDINA, § 3 ; CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES, § 4)
- **R-8.15** Il est obligatoire de préserver les outils de lecture : Navigo, Police Taille, mode livre, fenêtres empilées, quiz et Pareto. (CLAUDE.md, 07.10.2026 ; FRONTENDS_2026-10-08)

## 9. Contenu médical et pédagogique

- **R-9.1** Il est obligatoire d’écrire en professeur omnipraticien, enseignant de médecins assistants, et de traiter chaque pathologie comme une notion nouvelle, des généralités au point pointu, avec l’obsession de faire comprendre. (CLAUDE.md ; PROMPT_MEDINA, § 0)
- **R-9.2** Il est obligatoire de suivre, dans l’onglet Pathologie, l’ordre des îlots : cas fil rouge et objectifs, définitions et classifications, épidémiologie datée, physiopathologie avec figure, étiologies, anamnèse, examen clinique, diagnostic avec algorithme, urgences et complications, prise en charge, suivi, situations particulières, puis références datées ; un îlot non applicable est supprimé et un îlot propre à la pathologie est ajouté. (PROMPT_MEDINA, § 10 ; CHAPTER_SPEC, § 4)
- **R-9.3** Il est obligatoire de clore l’onglet Pathologie par un dernier îlot qui énonce les critères formels du diagnostic (société savante, version, nombre de critères) dans un `div.alert`, puis les paramètres clés (seuils, signes de gravité, valeurs à surveiller, pièges) dans un `div.key`. (CLAUDE.md, règle 4 ; PROMPT_MEDINA, § 13)
- **R-9.4** Il est obligatoire de placer un Pareto « perfectit » à la fin de chaque grande partie, avec une fraction calculée par le moteur et visant habituellement 5 à 20 % du texte pour 100 % des notions utiles. (CLAUDE.md, règle 5 ; PROMPT_MEDINA, § 14)
- **R-9.5** Il est obligatoire, dans l’onglet Examens, de fournir le tableau question → examen → statut, l’examen de référence nommé, des fiches d’interprétation (valeurs normales avec unités et population, seuils, pièges, erreur fréquente) et au moins trois quiz de cas cliniques au format de l’examen. (PROMPT_MEDINA, § 10 ; CHAPTER_SPEC, § 4)
- **R-9.6** Il est obligatoire, dans l’onglet Sciences, de proposer une barre par discipline, un îlot par science, au moins un schéma légendé par science utile et des corrélations science → clinique, examen et traitement dans des encadrés `key`, au niveau universitaire. (PROMPT_MEDINA, § 10 ; STYLE_REDACTION, § 6)
- **R-9.7** Il est obligatoire, dans l’onglet Pharmacologie, de donner la classification, la place selon le stade et le phénotype, le tableau des doses (initiale, cible, maximale, formes suisses), les interactions dangereuses dans un `alert`, la surveillance, les médicaments à éviter et des monographies en fenêtres. (PROMPT_MEDINA, § 10 ; CHAPTER_SPEC, § 4)
- **R-9.8** Il est obligatoire de préciser pour chaque médicament la molécule, la forme, la dose, la voie, la fréquence, la durée, la dose maximale, l’adaptation rénale et hépatique, la grossesse et l’allaitement, conformément à l’information professionnelle suisse. (PROMPT_MEDINA, § 11)
- **R-9.9** Il est obligatoire de présenter le normal avant le pathologique, du simple au complexe, avec un exemple chiffré ou un patient pour chaque notion nouvelle et un cas fil rouge qui ouvre et ferme le chapitre. (CLAUDE.md, règle 7 ; PROMPT_MEDINA, § 11)
- **R-9.10** Il est obligatoire de donner à chaque chiffre son unité, sa population, son contexte et sa source datée, et de distinguer recommandation (classe, niveau de preuve), option, consensus et incertitude. (PROMPT_MEDINA, § 11)
- **R-9.11** Il est obligatoire de garder la même valeur d’un seuil dans les quatre onglets, les fenêtres, les tableaux, les quiz, le glossaire et le Pareto. (PROMPT_MEDINA, § 11 ; CLAUDE_AUDIT_GLOBAL, 07.10.2026)
- **R-9.12** Il est interdit de généraliser un essai hors de sa population ou d’affirmer une causalité sans mécanisme ou preuve. (PROMPT_MEDINA, § 11)
- **R-9.13** Il est obligatoire de signaler les pièges et erreurs fréquentes partout où ils existent et de placer les moyens mnémotechniques en fenêtre avec la mention « aide pédagogique, non critère officiel ». (PROMPT_MEDINA, § 11 ; CHAPTER_SPEC, § 4)
- **R-9.14** Il est obligatoire de produire les figures, courbes et tracés propres à chaque spécialité (par exemple spirométrie et gaz du sang en pneumologie, partogramme en obstétrique, cinétique sérologique en infectiologie) et de relier les cours concernés à l’atlas ECG. (PROMPT_MEDINA, § 15)
- **R-9.15** Il est obligatoire de traiter J40 — Bronchite (P-02-Pneumologie) comme un cours unique couvrant J20, J40, J41 et J42, en distinguant bronchite chronique et BPCO. (CLAUDE.md, 07.10.2026)
- **R-9.16** Il est obligatoire de présenter les nouveautés ESC 2026 de manière comparative, dans des fenêtres contextualisées, sans multiplicateur de volume. (CLAUDE.md, mission cardiologie, 08.10.2026)
- **R-9.17** Il est obligatoire de citer le tableau 18 ESC 2026 dans I42 — Cardiomyopathies (C-01-Cardiologie) dans une fenêtre ouverte par un mot vert, où « C » désigne l’insuffisance cardiaque chronique des stades B à D. (CONSIGNES_INTERACTION ; REGLES_VIAL c68d96a, § 3, 08.10.2026)
- **R-9.18** Il est obligatoire de présenter l’ordre de rendement des systèmes comme une estimation MEDINA, puisque les pondérations officielles du blueprint ne sont pas publiées. (PROMPT_MEDINA, § 9.2)
- **R-9.19** Il est interdit de condenser ou d’appauvrir un cours pour économiser des ressources ; toutes les notions utiles sont conservées. (PROMPT_MEDINA, § 19.4 et § 20 ; CLAUDE.md)

## 10. Justification des affirmations

- **R-10.1** Il est obligatoire de justifier chaque affirmation médicale, dans tous les onglets, tableaux, figures, quiz, fenêtres, Pareto et glossaires, par son mécanisme causal précis, sa conséquence clinique, ses limites et sa source primaire. (CLAUDE.md ; MISSION_JUSTIFICATION, 07.10.2026)
- **R-10.2** Il est obligatoire d’expliquer, pour « anémie : facteur aggravant », la baisse du transport artériel d’oxygène, les compensations cardiovasculaires et la réserve limitée, en tenant compte du contexte. (CLAUDE.md ; MECHANISMS_CLAUDE, 07.10.2026)
- **R-10.3** Il est obligatoire, pour un examen biologique comme le sodium ou le potassium, de justifier séparément pourquoi le doser, comment interpréter le résultat et comment agir. (CLAUDE.md ; CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES, § 4, 07–08.10.2026)
- **R-10.4** Il est interdit de confondre association pronostique et causalité, ou preuve et consensus ; une association est présentée comme telle avec sa source. (CLAUDE.md ; MECHANISMS_CLAUDE, 07.10.2026)
- **R-10.5** Il est obligatoire, pour un traitement, de distinguer mécanisme, bénéfice clinique démontré, indications et risques. (MECHANISMS_CLAUDE, 07.10.2026)
- **R-10.6** Il est interdit d’écrire une cellule de tableau laconique qui énonce un fait sans cause ni conséquence : elle forme une phrase complète ou porte un mot vert qui ouvre l’explication. (MISSION_JUSTIFICATION, 07.10.2026)
- **R-10.7** Il est obligatoire, dans une liste d’examens, de dire pour chacun pourquoi il est demandé et quelle valeur change quelle décision. (MISSION_JUSTIFICATION, 07.10.2026)
- **R-10.8** Il est obligatoire de privilégier la fenêtre interactive ouverte par un mot vert pour les explications longues ou réutilisées, et d’écrire dans le texte une explication courte de deux ou trois phrases. (MISSION_JUSTIFICATION ; CONSIGNES_INTERACTION, 07–08.10.2026)
- **R-10.9** Il est obligatoire de structurer une fenêtre de justification par une explication synthétique, puis le mécanisme précis, la conséquence clinique, les limites et les sources, dans l’ordre normal → perturbation → conséquence → décision. (MECHANISMS_CLAUDE ; MISSION_JUSTIFICATION, 07.10.2026)
- **R-10.10** Il est obligatoire de garder dans le texte principal toute mise en garde qui change une décision ; il est interdit de cacher une réserve nécessaire dans une fenêtre. (MECHANISMS_CLAUDE ; CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES, § 4, 07–08.10.2026)
- **R-10.11** Il est obligatoire de présenter un mécanisme incertain comme incertain. (MISSION_JUSTIFICATION, 07.10.2026)
- **R-10.12** Il est interdit de retirer une notion utile ou de recopier une explication déjà présente ailleurs ; il est obligatoire de renvoyer à la fenêtre existante. (MISSION_JUSTIFICATION, 07.10.2026)
- **R-10.13** Il est interdit de présenter une banque de fenêtres ciblées comme une relecture exhaustive ou de marquer un cours validé pour sa seule compilation ; toute affirmation non revue demeure à contrôler. (CLAUDE.md ; MECHANISMS_CLAUDE, 07.10.2026)
- **R-10.14** Il est obligatoire, lorsqu’une banque `chapters/<CODE>/<CODE>_justifications.json` est utilisée, de respecter le format strict du compilateur `tools/insert_justifications.py` (identifiants `<code>-j-<nom>`, cibles natives sous ancre existante, occurrence explicite si le texte se répète, sources HTTPS). (MECHANISMS_CLAUDE, 07.10.2026)

## 11. Sources et Compendium

- **R-11.1** Il est obligatoire de rechercher d’abord les sources suisses (sociétés savantes suisses, OFSP, Plan de vaccination suisse, Swissmedic, compendium.ch, mediX, Suva, Ligues, PROFILES), puis les recommandations européennes et internationales acceptées en Suisse. (CLAUDE.md ; PROMPT_MEDINA, § 12)
- **R-11.2** Il est obligatoire de vérifier la version en vigueur à la date de rédaction, par une dizaine de recherches ciblées, et de dater chaque recommandation. (PROMPT_MEDINA, § 12 ; CHAPTER_SPEC, § 4)
- **R-11.3** Il est interdit d’inventer un chiffre, un seuil, une posologie ou une classe de recommandation ; une donnée non vérifiable est attribuée explicitement à la dernière version vérifiée, sans formule de chantier « à vérifier ». (PROMPT_MEDINA, § 12 ; CHAPTER_SPEC, § 4)
- **R-11.4** Il est obligatoire de citer pour chaque affirmation nouvelle l’organisme, le titre, la version, l’URL ou le DOI, la section, le tableau ou la page, et la date de consultation. (SOURCES_CANONIQUES ; MISSION_JUSTIFICATION, 07.10.2026)
- **R-11.5** Il est obligatoire de distinguer accès impossible, résumé et texte intégral ; un seuil, une manœuvre ou une posologie exige la lecture du passage dans le texte intégral. (SOURCES_CANONIQUES, 07.10.2026 ; CONSIGNES_INTERACTION, 08.10.2026)
- **R-11.6** Il est interdit de combiner silencieusement deux sources divergentes ; le rédacteur décrit leur population, leur situation et leur portée. (SOURCES_CANONIQUES, 07.10.2026)
- **R-11.7** Il est interdit de remplacer une source primaire par une synthèse d’IA ou un résumé commercial, ou une recommandation clinique par un manuel pour une décision thérapeutique. (SOURCES_CANONIQUES, 07.10.2026)
- **R-11.8** Il est obligatoire de faire primer, en cas de contentieux clinique, la source primaire applicable la plus récente dans le texte principal. (CLAUDE.md ; CONSIGNES_INTERACTION ; REGLES_VIAL c68d96a, 08.10.2026)
- **R-11.9** Il est obligatoire de présenter ce choix dans une fenêtre liée à un mot vert, avec le périmètre, la date, le niveau de preuve et les limites de la recommandation retenue, et avec l’accès au texte actuellement en vigueur même s’il est plus ancien. (CLAUDE.md ; CONSIGNES_INTERACTION, 08.10.2026)
- **R-11.10** Il est interdit de tenir une date plus récente pour applicable sans avoir lu son contenu et vérifié sa population, son indication et son contexte suisse. (CONSIGNES_INTERACTION, 08.10.2026)
- **R-11.11** Il est obligatoire de lire et dater réellement la monographie suisse en vigueur sur compendium.ch (page `…/product/<id>-<nom>/mpro`), de confirmer le produit, la date et les conditions, et il est interdit d’importer une dose ou une indication d’un produit hors sujet. (CLAUDE.md ; CONSIGNES_INTERACTION, 08.10.2026)
- **R-11.12** Il est obligatoire de citer l’information professionnelle sous la forme « Information professionnelle suisse, compendium.ch, <produit>, consultée le <date> » ; l’outil `tools/compendium_fi.cjs` peut en extraire les sections après vérification locale. (REGLES_VIAL c68d96a, § 4 ; CONSIGNES_INTERACTION, 08.10.2026)
- **R-11.13** Il est obligatoire d’insérer toute mise à jour de veille dans un `span.maj` daté et sourcé. (PROMPT_MEDINA, § 12)
- **R-11.14** Il est obligatoire d’ajouter au registre `SOURCES_CANONIQUES.md` la référence suisse ou européenne pertinente, sa version et son accès avant de rédiger dans un fragment encore sans cours intégré. (SOURCES_CANONIQUES, 07.10.2026)
- **R-11.15** Il est obligatoire de documenter le choix de source dans le rapport d’audit et de laisser visible toute réserve non résolue. (CONSIGNES_INTERACTION, 08.10.2026)

## 12. Rédaction et style

- **R-12.1** Il est obligatoire d’appliquer `docs/STYLE_REDACTION.md` à chaque phrase : le lecteur comprend, il ne devine pas. (CLAUDE.md, règle 0 ; STYLE_REDACTION, 26.09.2026)
- **R-12.2** Il est obligatoire d’écrire des phrases courtes et complètes, avec sujet et verbe conjugué, une idée par phrase, une vingtaine de mots au plus. (STYLE_REDACTION, § 2)
- **R-12.3** Il est interdit d’écrire une phrase nominale, un infinitif injonctif, une énumération de mots-clés à la place d’une explication ou une parenthèse qui remplace une phrase ; les titres restent des groupes nominaux courts. (STYLE_REDACTION, § 2)
- **R-12.4** Il est obligatoire de faire suivre à chaque îlot, sous-partie et discipline le mouvement annonce, développement et épilogue « À retenir » dans un `div.key`. (STYLE_REDACTION, § 3)
- **R-12.5** Il est interdit qu’une annonce décrive le plan ou la fabrication du cours (« cet îlot présente », « cette section explique », « le lecteur apprend ») ; elle expose directement le problème médical. (STYLE_REDACTION, § 3 ; CLAUDE.md, 07.10.2026)
- **R-12.6** Il est obligatoire de dire, pour chaque affirmation, quoi, pourquoi, puis ce que cela change pour le patient, et de supprimer toute phrase qui n’explique, ne prouve ou ne sert rien. (STYLE_REDACTION, § 1)
- **R-12.7** Il est obligatoire d’introduire chaque tableau par la question clinique, de lui donner des en-têtes explicites et de le faire suivre d’une lecture sur un exemple de patient ; la même règle vaut pour les figures. (STYLE_REDACTION, § 4)
- **R-12.8** Il est obligatoire d’employer un tableau lorsqu’il clarifie une classification, une comparaison ou une énumération, avec des cellules courtes et cohérentes, des unités et conditions indiquées et une lisibilité vérifiée sur ordinateur et mobile ; il est interdit de convertir systématiquement la prose causale en tableau. (CONSIGNES_INTERACTION ; REGLES_VIAL c68d96a, § 2, 08.10.2026)
- **R-12.9** Il est obligatoire de faire de chaque antécédent, symptôme, signe, examen, score, critère, médicament et essai important un mot vert ouvrant une fenêtre réelle rédigée selon le même guide. (STYLE_REDACTION, § 5)
- **R-12.10** Il est obligatoire de tout évoquer sans bavardage : chaque phrase apporte une information, un mécanisme ou une décision ; il est interdit d’écrire remplissage, transition creuse ou répétition. (CONSIGNES chaîne continue, § 6 bis, 08.10.2026)
- **R-12.11** Il est interdit de fixer ou de poursuivre un objectif ou un plafond de mots ; la longueur se justifie par le contenu. (CLAUDE.md ; CONSIGNES_INTERACTION, 07–08.10.2026)
- **R-12.12** Il est interdit d’écrire métaphores, comparaisons imagées, jeux de mots, plaisanteries, termes vains, formules de chantier et compliments au cours. (CLAUDE.md, règle 7 ; PROMPT_MEDINA, § 11 ; CLAUDE_AUDIT_GLOBAL)
- **R-12.13** Il est interdit de cloner une phrase d’un autre chapitre. (PROMPT_MEDINA, § 11 ; CHAPTER_SPEC, § 1)
- **R-12.14** Il est obligatoire d’employer une terminologie exacte et constante, des définitions opérationnelles (seuil, durée, nombre de critères) et une fréquence en chiffres plutôt qu’un adverbe. (PROMPT_MEDINA, § 11)
- **R-12.15** Il est obligatoire d’écrire des paragraphes courts de trois à six phrases et de laisser la mise en forme au moteur. (STYLE_REDACTION, § 8)
- **R-12.16** Il est obligatoire de distinguer constatation, interprétation et degré de certitude, et de situer une précaution dans son contexte sans la répéter mécaniquement. (CLAUDE_AUDIT_GLOBAL, 07.10.2026)

## 13. Glossaire et abréviations

- **R-13.1** Il est interdit d’employer une abréviation sans clé dans le glossaire (`glossary/<code>.py`, fonction `a(*x)`), avec définition littérale lettre par lettre. (CLAUDE.md, règle 3 ; PROMPT_MEDINA, § 5)
- **R-13.2** Il est obligatoire que `build_medina.audit()` renvoie `{}` pour chaque cours. (CLAUDE.md, règle 3 ; CONSIGNES chaîne continue, § 6)
- **R-13.3** Il est obligatoire de lister les clés existantes avant d’écrire et de vérifier le sens d’une clé existante avant de l’employer. (PROMPT_MEDINA, § 5)
- **R-13.4** Il est interdit d’ajouter une clé qui existe déjà, puisque la dernière définition chargée l’emporte dans tout l’atlas ; les arbitrages se font dans `glossary/zz_fusion.py`. (PASSATION_REECRITURE, § 6 ; PROMPT_MEDINA, § 2)
- **R-13.5** Il est interdit d’employer une clé dans un autre sens que celui du glossaire (par exemple « IC » pour un intervalle de confiance, « C4 » pour un leucotriène, « T2 » pour l’inflammation de type 2, « RR », « FC », « PA », « AL », « V1 »). (PROMPT_MEDINA, § 5)
- **R-13.6** Il est obligatoire de déclarer dans le glossaire les codes CIM à décimale hors « I », les unités à casse mixte et les noms propres composés absents de la liste blanche. (PROMPT_MEDINA, § 5)
- **R-13.7** Il est obligatoire d’écrire honnêtement un nom d’essai non développable lettre à lettre, selon le modèle de `glossary/cardio_2.py`. (PROMPT_MEDINA, § 5 ; CHAPTER_SPEC, § 5)
- **R-13.8** Il est obligatoire d’écrire en toutes lettres ce qui n’exige pas d’abréviation (« par voie intraveineuse », « par jour », « aérosol-doseur », « angiotensine II »). (PROMPT_MEDINA, § 5 ; CHAPTER_SPEC, § 5)
- **R-13.9** Il est interdit de traiter les symboles d’unités (mg, mL, mmHg, µg, mmol/L) comme des abréviations à définir. (PROMPT_MEDINA, § 5 ; CHAPTER_SPEC, § 5)
- **R-13.10** Il est interdit de placer une abréviation dans les libellés des onglets, des boutons Pareto et de la barre des sciences. (PROMPT_MEDINA, § 5)
- **R-13.11** Il est obligatoire de signaler les collisions d’un sigle global et les conséquences d’une définition modifiée sur les autres cours. (CLAUDE_AUDIT_GLOBAL, 07.10.2026)
- **R-13.12** Il est obligatoire, en cas de conflit de définition d’une même clé, de retenir une seule définition, la plus littérale et la plus exacte. (PROMPT_MEDINA, § 2 ; REPRISE_CLAUDE_CODE, phase 1, 26.09.2026)

## 14. Typographie et frontend

- **R-14.1** Il est obligatoire d’employer **Atkinson Hyperlegible Next** comme police par défaut du portail, des 22 frontends et des cours, avec les quatre WOFF2 originaux embarqués hors ligne (romain 400, italique 400, romain 600, romain 700). (AGENTS.md ; CLAUDE.md ; FRONTENDS_2026-10-08, 08.10.2026)
- **R-14.2** Il est obligatoire de conserver Anthropic Serif comme simple option du lecteur. (FRONTENDS_2026-10-08 ; CLAUDE.md, 08.10.2026)
- **R-14.3** Il est obligatoire de permettre au lecteur d’adapter police et taille, et d’appliquer ces réglages au texte, aux fenêtres et à Navigo. (CLAUDE.md ; FRONTENDS_2026-10-08, 08.10.2026)
- **R-14.4** Il est obligatoire de produire un HTML en thème clair exclusivement ; il est interdit qu’un bouton, une préférence enregistrée ou une adaptation système active un mode sombre. (Prompt_Codex ; PROTOCOLE_FRAGMENTS, 08.10.2026)
- **R-14.5** Il est obligatoire de contrôler le thème clair dans un navigateur configuré avec une préférence système sombre et un ancien réglage sombre sauvegardé. (PROTOCOLE_FRAGMENTS, 08.10.2026)
- **R-14.6** Il est obligatoire de garantir des contrastes élevés, un texte principal presque noir sur surfaces claires et un contraste d’au moins 4,5:1 pour le texte blanc des cartes colorées. (FRONTENDS_2026-10-08, 08.10.2026)
- **R-14.7** Il est obligatoire d’attribuer une couleur vive distincte à chaque spécialité et à chaque catégorie, sur des cartes sobres à fond clair et relief discret. (CLAUDE.md ; FRONTENDS_2026-10-08 ; CONSIGNES chaîne continue, § 6, 08.10.2026)
- **R-14.8** Il est obligatoire de donner à chaque fragment son HTML et sa navigation propres, limités au contenu de sa spécialité, avec une classification centralisée dans `fragment_surface.py`. (CLAUDE.md ; FRONTENDS_2026-10-08, 08.10.2026)
- **R-14.9** Il est interdit que d’anciens rattachements anatomiques réintroduisent un cours étranger dans un fragment ; les glossaires embarqués ne contiennent que les termes des cours présents et leurs dépendances. (CLAUDE.md ; FRONTENDS_2026-10-08, 08.10.2026)
- **R-14.10** Il est obligatoire de maintenir le portail des 22 spécialités avec recherche, un carnet local distinct par fragment, un rendu responsive et le respect de `prefers-reduced-motion`. (FRONTENDS_2026-10-08, 08.10.2026)
- **R-14.11** Il est interdit de revendiquer un « standard universel de lecture » ou un bénéfice clinique non mesuré de la police. (FRONTENDS_2026-10-08, 08.10.2026)
- **R-14.12** Il est obligatoire de marquer tout aperçu de rédaction « Version de travail », sans injection canonique, sans certification finale et avec des indicateurs de validation et de complétude vides. (CLAUDE.md ; FRONTENDS_2026-10-08, 08.10.2026)
- **R-14.13** Il est obligatoire de réserver l’Atlas ECG au fragment C-01-Cardiologie. (FRAGMENTS.md)
- **R-14.14** Il est interdit d’intégrer un état des lieux d’avancement dans le produit ; il vit dans un fichier séparé. (PROMPT_MEDINA, § 7 ; CLAUDE.md)
- **R-14.15** Il est interdit d’afficher l’insigne « 100 % rédigé » pour un cours ou un système qui n’est pas achevé selon les critères en vigueur. (PROMPT_MEDINA, § 7 ; COMPLETUDE_CIM11, 07.10.2026)
- **R-14.16** Il est interdit d’employer l’ocre de la branche Alpha pour les titres. (REPRISE_CLAUDE_CODE, phase 1, 26.09.2026)

## 15. Bouton « Isolate Federal – CH Exam »

- **R-15.1** Il est obligatoire de placer dans chaque frontend de fragment un bouton nommé exactement **« Isolate Federal – CH Exam »**. (CONSIGNES chaîne continue, § 3, 08.10.2026)
- **R-15.2** Il est obligatoire qu’un appui laisse les catégories affichées et passe en surbrillance « poudre d’or » (fond doré, scintillement discret, contraste conservé) les chapitres des situations cliniques communes de la pratique quotidienne et de l’examen fédéral. (CONSIGNES chaîne continue, § 3, 08.10.2026)
- **R-15.3** Il est obligatoire qu’un second appui rétablisse l’affichage normal et que le choix soit mémorisé localement. (CONSIGNES chaîne continue, § 3, 08.10.2026)
- **R-15.4** Il est obligatoire de centraliser la liste par fragment dans `organisation/federal_exam.json`, sur la base des Exigences MED 2026 (OFSP) et des situations PROFILES, avec le moteur `engine/federal_exam.*`. (CONSIGNES chaîne continue, § 3 ; AGENTS.md, 08.10.2026)
- **R-15.5** Il est obligatoire de présenter cette liste comme une sélection éditoriale, et il est interdit de la présenter comme une pondération officielle. (CONSIGNES chaîne continue, § 3, 08.10.2026)
- **R-15.6** Il est obligatoire que chaque producteur complète la liste de ses fragments lors de leur production et que l’auditeur la contrôle. (CONSIGNES chaîne continue, § 3, 08.10.2026)
- **R-15.7** Il est obligatoire que le bouton respecte le thème clair exclusif, la police Atkinson Hyperlegible Next et les contrastes élevés. (CONSIGNES chaîne continue, § 3, 08.10.2026)

## 16. Sémiologie CS

- **R-16.1** Il est obligatoire de produire un module « Sémiologie CS » (compétences cliniques d’examen et d’interrogatoire) pour chaque fragment où l’examen clinique s’applique (pneumologie, gastroentérologie, neurologie, endocrinologie, néphrologie, hématologie, gynécologie, obstétrique, rhumatologie et orthopédie, urologie, dermatologie, ORL, ophtalmologie, urgences, médecine des âges de la vie, etc.). (CONSIGNES chaîne continue, § 6 bis, 08.10.2026)
- **R-16.2** Il est obligatoire d’intégrer ce module à la complétude du fragment et à sa navigation, sur le modèle `modules/cardiovascular_cs.*`, sous la forme `modules/<nom>_cs.{html,css,js}` déclarée dans `modules/cs_registry.json`. (CONSIGNES chaîne continue, § 6 bis ; commit 15caf87, 08.10.2026)
- **R-16.3** Il est obligatoire de justifier par écrit la dispense d’un fragment sans examen clinique propre (par exemple éthique et droit). (CONSIGNES chaîne continue, § 6 bis, 08.10.2026)
- **R-16.4** Il est obligatoire de rapprocher chaque repère et chaque manœuvre d’un passage précis d’une source d’enseignement institutionnelle, et de vérifier termes anatomiques, techniques et interprétation de chaque signe. (SOURCES_CANONIQUES ; CLAUDE_AUDIT_GLOBAL, 07.10.2026)
- **R-16.5** Il est interdit de présenter les modèles 3D stylisés comme une représentation anatomique exacte ou une imagerie de patient. (CLAUDE_AUDIT_GLOBAL ; MEDINA_S01, 07.10.2026)

## 17. Outils, construction et tests

- **R-17.1** Il est obligatoire de construire avec `python3 build_front.py` et `python3 build_front.py --all-fragments` (ou `--fragment <ID>`), la sortie étant fixée par `MEDINA_OUT`. (CLAUDE.md ; CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES, § 7)
- **R-17.2** Il est obligatoire d’obtenir OK à `python3 test_v7.py --static <CODES>` et à `python3 test_v7.py <CODES>` sur ordinateur et mobile (glossaire, fenêtres, préfixes, classes, styles, zéro erreur JavaScript, aucun débordement mobile). (PROMPT_MEDINA, § 16 ; PROMPT_REPRISE_IA, § 5)
- **R-17.3** Il est obligatoire d’exécuter les contrôles adaptés avant remise et après injection : `tests/audit_fragments.py`, `tests/audit_sciences.py`, `verify_course_native.cjs` sans échec, tests navigateur et tests unitaires. (REGLES_INJECTION_CLAUDE, conditions techniques ; CLAUDE_AUDIT_GLOBAL)
- **R-17.4** Il est obligatoire de contrôler aussi le fragment autonome sur ordinateur et mobile (quatre onglets, fenêtres, quiz, Pareto, navigation, taille de police, mode livre, liens internes), puisque `test_v7.py` cible seulement `MEDINA.html` global. (CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES, § 7)
- **R-17.5** Il est obligatoire de tester les copies de travail dans un répertoire de validation isolé, sans écraser le checkout ni les travaux d’une autre session, et de consigner la méthode et le SHA. (CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES, § 7 ; CODEX_CHAINE_FRAGMENTS)
- **R-17.6** Il est obligatoire de consigner les commandes réellement exécutées et leurs résultats, y compris les échecs ; il est interdit de présenter un contrôle non exécuté comme réussi. (CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES, § 7 ; REVIEW_TEMPLATE)
- **R-17.7** Il est interdit de présenter un test technique réussi comme une validation médicale ou une preuve de complétude. (REVIEW_TEMPLATE ; COMPLETUDE_CIM11, 07.10.2026)
- **R-17.8** Il est obligatoire de reconstruire les HTML après toute intégration ; il est interdit de modifier seulement une sortie générée (`dist/`) en guise d’intégration. (AGENTS.md ; collaboration README, 07.10.2026)
- **R-17.9** Il est obligatoire de régénérer la pile par `tools/pile_fragments.py` et de valider le plan par `python3 tools/production_plan.py` à chaque livraison. (CONSIGNES chaîne continue, § 4 ; FRAGMENTS_RESTANTS, 08.10.2026)
- **R-17.10** Il est obligatoire de livrer selon la séquence : `modules/ecg.py` si les tracés changent, `build_front.py`, `test_v7.py`, `chantier.py`, `pack_v7.py`. (PROMPT_MEDINA, § 18 ; commande /livrer)
- **R-17.11** Il est interdit d’utiliser la coque V7 (`build_v7.py`, `shell/shell.html`) et les anciens outils `test_preview.py`, `test_medina.py` et `pack.py`. (CLAUDE.md, règle 1 ; PROMPT_MEDINA, § 2)
- **R-17.12** Il est interdit de tronquer un chapitre pour tenir une limite de taille de fichier ; il est obligatoire de scinder la livraison si nécessaire. (PROMPT_MEDINA, § 8)

## 18. GitHub, branches, PR et accusés

- **R-18.1** Il est obligatoire d’appliquer l’accord permanent de Vial pour les branches, commits, pushes, rapports et pull requests MEDINA, sans redemander de confirmation. (CLAUDE.md ; AGENTS.md ; collaboration README, 07.10.2026)
- **R-18.2** Il est obligatoire de respecter les contrôles du projet et les protections GitHub ; l’accord ne crée aucune connexion technique manquante. (CLAUDE.md ; DELIVERY_PROTOCOL, 07.10.2026)
- **R-18.3** Il est obligatoire de recenser, à chaque reprise et avant toute publication, toutes les branches et PR avec pagination par `python3 tools/collaboration_sync.py --out docs/collaboration`, ou par `--snapshot` si seul le connecteur fonctionne. (CLAUDE.md ; AGENTS.md, 07.10.2026)
- **R-18.4** Il est interdit de conclure « aucun rapport reçu » d’après la seule passation ou les références du clone local ; les anciens rapports, branches sans PR et patchs restent recevables. (CLAUDE.md ; AGENTS.md, 07.10.2026)
- **R-18.5** Il est obligatoire de lire `HANDOFF_LATEST.md`, `DELIVERIES_LATEST.md` et les reçus avant tout nouveau lot. (AGENTS.md ; CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES, § 1)
- **R-18.6** Il est obligatoire de délivrer un accusé dans `docs/collaboration/receipts/` pour toute remise, tout audit et toute injection, avec commit exact, empreintes, fragments, contrôles et réserves. (CLAUDE.md ; CONSIGNES chaîne continue, § 7, 08.10.2026)
- **R-18.7** Il est obligatoire d’actualiser la passation, l’inventaire et le tableau de bord après chaque lot. (CLAUDE.md ; AGENTS.md, 07.10.2026)
- **R-18.8** Il est obligatoire de conserver les commits et rapports du contributeur ; il est interdit de déplacer, réécrire ou remettre artificiellement à niveau la branche de l’autre IA. (AGENTS.md ; CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES, § 3)
- **R-18.9** Il est interdit de recopier une ancienne version au-dessus de corrections nouvelles ; les sources canoniques, reçus et commits contrôlés les plus récents priment. (CLAUDE.md ; FRAGMENTS_RESTANTS, 07–08.10.2026)
- **R-18.10** Il est obligatoire de distinguer « repéré », « reçu », « intégré », « contrôlé techniquement », « vérifié médicalement » et « publié ». (AGENTS.md ; DELIVERY_PROTOCOL, 07.10.2026)
- **R-18.11** Il est obligatoire de vérifier séparément la disponibilité distante, le déploiement Pages et le contenu réellement servi ; un push sur une branche n’en est pas la preuve. (AGENTS.md ; CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES, § 7)
- **R-18.12** Il est obligatoire, sans accès en écriture, de remettre rapport et patch complet ; il est interdit de présenter l’absence de push comme une publication. (DELIVERY_PROTOCOL ; reviews/README, 07.10.2026)

## 19. Visibilité, captures, pile et tableau de bord

- **R-19.1** Il est obligatoire d’accompagner toute livraison montrée à Vial de captures réelles du rendu, sur ordinateur et sur mobile, produites dans un navigateur et affichées directement dans la conversation avec le lien du cours. (AGENTS.md ; CONSIGNES chaîne continue, § 6 bis, 08.10.2026)
- **R-19.2** Il est interdit de remplacer ces images visibles par des sorties techniques ou de simples liens de téléchargement. (AGENTS.md, 08.10.2026)
- **R-19.3** Il est obligatoire de présenter une navigation par une capture animée issue du navigateur réel. (AGENTS.md, 08.10.2026)
- **R-19.4** Il est obligatoire de dater et versionner les captures et de garder le statut de version de travail ; il est interdit d’inventer un rendu ou d’annoncer un flux en direct pour une animation enregistrée. (AGENTS.md, 08.10.2026)
- **R-19.5** Il est obligatoire de tenir visible en permanence `organisation/PILE_FRAGMENTS.html` et sa source JSON, avec au minimum le fragment suivant de chaque IA, toutes ses catégories et toutes ses leçons (rédigées, à venir, groupements prévus). (CONSIGNES chaîne continue, § 4, 08.10.2026)
- **R-19.6** Il est obligatoire de terminer chaque livraison par un tableau de bord : cours, catégories traitées, fragment ou système, poids du fichier et alertes. (CLAUDE.md ; PROMPT_MEDINA, § 19.6)
- **R-19.7** Il est obligatoire de tenir à jour le tableau commun `organisation/MEDINA_Organisation.html` et sa version publiée. (CLAUDE.md, 07.10.2026)
- **R-19.8** *(levée par R-19.10)* Il était obligatoire, pour **chaque chapitre développé**, de produire et d’afficher directement dans la conversation avec Vial **au moins 3 captures dans chacun des 4 environnements du chapitre** (onglets Pathologie et prise en charge, Examens complémentaires, Sciences fondamentales spécialisées, Pharmacologie), soit au moins 12 captures, plus une vue mobile ; ces petites fenêtres de captures accompagnent le travail naturellement, sans attendre de demande. Il est interdit de livrer, remettre ou annoncer un chapitre sans elles. Outil : `python3 tools/captures_chapitre.py <fragment.html> <CODE> <dossier>`. Cette règle s’applique à Claude Code et à Codex, sans exception. (Vial, 08.10.2026, « pour la toute et ultime dernière fois »)
- **R-19.9** *(levée par R-19.10)* Il était obligatoire que chaque capture provienne du rendu réel du chapitre dans un navigateur (thème clair, police Atkinson Hyperlegible Next) et que l’ensemble couvre le début, le milieu et une fenêtre explicative ouverte de chaque onglet ; une capture manquante est un défaut bloquant de la livraison. (Vial, 08.10.2026)
- **R-19.10** Les règles R-19.8 et R-19.9 sont **levées** : Vial a écrit le 8 octobre 2026 « plus besoin de Capture ; continue la production de cours comme à l’accoutumé, terme interactif cliquable et respect des instructions ». Il est désormais interdit de ralentir la production par des captures systématiques ; les captures restent possibles ponctuellement, à la demande de Vial. (Vial, 08.10.2026)

## 20. Sécurité et secrets

- **R-20.1** Il est interdit de transmettre un secret ou un jeton dans les fichiers du dépôt. (CLAUDE.md, 07.10.2026)
- **R-20.2** Il est interdit d’afficher `GH_TOKEN` dans une sortie, un journal ou un rapport. (collaboration README, 07.10.2026)
- **R-20.3** Il est interdit de transférer un identifiant ou un jeton entre les agents ; chaque agent utilise sa propre connexion GitHub effective. (DELIVERY_PROTOCOL ; collaboration README, 07.10.2026)
- **R-20.4** Il est interdit d’écrire dans le dossier Drive « Medina Alpha » sans demande de Vial. (REPRISE_CLAUDE_CODE ; commande /fusion-alpha, 26.09.2026)
- **R-20.5** Il est interdit d’écraser `Medina.html` (MEDINA_0, 79 Mo, avec les SSP). (REPRISE_CLAUDE_CODE, 26.09.2026)

## 21. Arrêt

- **R-21.1** Il est obligatoire d’arrêter immédiatement toute production sur un « STOP » explicite de Vial et d’attendre ses nouvelles instructions. (CONSIGNES chaîne continue, § 1 ; ARRET_CODEX, 08.10.2026)
- **R-21.2** Il est obligatoire, lorsque les 22 fragments sont rédigés, auto-revus, audités et injectés avec leurs preuves, d’arrêter toute production et de publier uniquement le rapport de complétion. (Prompt_Codex ; PROTOCOLE_FRAGMENTS, 08.10.2026)
- **R-21.3** Il est interdit d’engager une boucle de peaufinage au-delà de cet arrêt et de déduire l’arrêt global d’un simple compteur de cours. (Prompt_Codex ; PROTOCOLE_FRAGMENTS, 08.10.2026)
- **R-21.4** Il est interdit de relancer au démarrage les veilles automatiques (veille locale et workflow `claude_watch`), qui restent en pause. (COORDINATION.md ; PROTOCOLE ; AGENTS.md, 08.10.2026)

## Annexe A — Règles remplacées : ne plus appliquer

Les règles ci-dessous ne s’appliquent plus. Leurs travaux et preuves restent conservés. La date indique le remplacement.

| Ancienne règle (source) | Date | Remplacée par |
| --- | --- | --- |
| Coque V7 `build_v7.py` / `shell/shell.html` (PROMPT_MEDINA, § 2) | 26.09.2026 | Abandonnée par le propriétaire ; R-17.11. |
| Police Georgia partout, par défaut dans les cours (CLAUDE.md, règle 6 ; PROMPT_MEDINA, § 7) | 08.10.2026 | Atkinson Hyperlegible Next par défaut ; R-14.1. |
| Anthropic Serif authentique comme police par défaut (CLAUDE.md, consigne frontend du 08.10.2026) | 08.10.2026 | Atkinson Hyperlegible Next ; Anthropic Serif reste une option ; R-14.1 et R-14.2. |
| Mode sombre facultatif ; captures en mode sombre (PROMPT_MEDINA, § 7 ; REPRISE_CLAUDE_CODE, phase 2) | 08.10.2026 | Thème clair exclusif ; R-14.4 et R-14.5. |
| Objectifs de longueur : 10 000 à 15 000 mots, « niveau de J45 » en volume (PROMPT_MEDINA, § 19.4 ; REPRISE_CLAUDE_CODE, phase 4 ; /chapitre) | 07.10.2026 | Aucun quota de mots ; qualité et densité ; R-12.10 et R-12.11. |
| Cycles de deux systèmes, ordre des vagues et vague 9 (REPRISE_CLAUDE_CODE, phase 4 ; /cycle ; PROMPT_MEDINA, § 9.3 et § 19.3 ; PROMPT_REPRISE_IA, § 4) | 08.10.2026 | Files de fragments entiers 11 Claude / 10 Codex ; R-1.3 et R-1.5. |
| Projet de réécriture J44, J18, I26 et A41 en priorité absolue (PROMPT_REPRISE_IA ; PASSATION_REECRITURE ; CLAUDE.md, reprise du 26.09) | 07–08.10.2026 | Répartitions successives puis fragments entiers ; ces cours relèvent de leur fragment. |
| Fusion Alpha, modernisation phase 2 et livraison `MEDINA_final.html` (REPRISE_CLAUDE_CODE, phases 1 à 3 ; /fusion-alpha) | 26.09.2026 | Réalisées ; mission historique close. |
| Mission d’audit global des 30 cours par Claude seul (CLAUDE_AUDIT_GLOBAL) | 07.10.2026 | Partage 15/15, puis 10/10 du Fragment 01, puis fragments entiers ; ses critères de qualité restent en vigueur (R-12.16, R-13.10, R-16.4). |
| Partages 15/15 et 10/10 des cours cardiologiques (MISSION_JUSTIFICATION ; MECHANISMS_CLAUDE ; CLAUDE.md, Fragment 01) | 08.10.2026 | C-01-Cardiologie achevé par Claude et remis entier à Codex ; R-1.3. |
| Fragment 02 en attente de l’achèvement du Fragment 01 ; chaîne Codex en attente de la cardiologie (HANDOFF ; cahier Claude) | 08.10.2026 | Chaîne Codex activée sur I-03 ; préparation du fragment suivant pendant l’audit ; R-3.8. |
| Un chapitre par remise, rapport et PR ; audit avant le chapitre suivant (FRAGMENTS_RESTANTS ; DELIVERY_PROTOCOL ; CONSIGNES_INTERACTION) | 08.10.2026, 14:36 UTC | Fragment entier auto-revu ; R-6.1 et R-6.15. |
| Un seul chapitre actif par agent ; sous-agents dans le seul chapitre actif (FRAGMENTS_RESTANTS ; cahier Claude ; production_plan.json) | 08.10.2026, 18:07 UTC | Sous-agents parallèles par catégorie ; R-7.1. |
| Injection autonome de Claude, file `FILE_AUDIT_CODEX.json`, mention « en audit croisé », arbitrage des désaccords par Claude (REGLES_INJECTION_CLAUDE, 12:50 UTC) | 08.10.2026, 14:36 UTC | Audit croisé unique, injection par l’auditeur ; R-6.7. |
| Espace partagé par cours, dépôt puis passage immédiat au chapitre suivant, « niveau de base » à deux quiz enrichi plus tard (REGLE_ADMIN ; REGLE_ADMIN_ESPACE_PARTAGE, 14:09–14:15 UTC) | 08.10.2026, 14:36 UTC | Fragment entier complet ; au moins trois quiz ; R-6.1, R-6.12 et R-9.5. |
| Audits en deuxième et troisième passe jusqu’à 20/20 ; chaîne produit → audit → correction → contre-vérification → injection (PROMPT_MEDINA, § 16 ; cahier Claude, § 6 ; CODEX_CHAINE, C3–C4) | 08.10.2026 | Un seul tour d’audit, l’auditeur corrige et injecte ; R-6.7 et R-6.8. |
| Correction ou nouveau dépôt après injection (REGLE_ADMIN, § 2 ; REGLES_INJECTION_CLAUDE) | 08.10.2026 | Statut INJECTÉ immuable ; R-6.13. |
| Rédacteur écrivant dans `chapters/<CODE>/` et `glossary/<code>.py` (PROMPT_MEDINA, § 17 ; CHAPTER_SPEC, § 7 ; /chapitre, étapes 4 à 6) | 08.10.2026 | Producteur hors canonique ; injection par l’auditeur ; R-6.4. |
| Codex coordinateur de l’injection et de la publication des chapitres des deux IA (CLAUDE.md ; FRAGMENTS_RESTANTS ; cahier Claude) | 08.10.2026 | Chaque auditeur injecte le fragment de l’autre ; R-6.7. |
| Outils `check-claude` / `apply-claude` et commandes d’injection par cours (DELIVERY_PROTOCOL ; tools/espace.py) | 08.10.2026 | Désactivés ; garde `tools/espace.py garde` ; R-6.11 et R-6.12. |
| STOP Codex « injecte ce qu’il faut injecter puis STOP » (ARRET_CODEX, 13:55 UTC) | 08.10.2026, 14:36 UTC | Levé par la reprise et le protocole par fragment. |
| Veille Codex automatique toutes les 5 et 15 minutes (CODEX_CHAINE_FRAGMENTS ; HANDOFF) | 08.10.2026 | Veilles en pause ; R-21.4. |
| « Aucune PR sans accord explicite » ; accord de publication par lot (PROMPT_REPRISE_IA ; anciennes mentions) | 07.10.2026 | Accord permanent de Vial ; R-18.1. |
| `DONE_COURSES` / `DONE_SYS` et audit ≥ 20/20 comme définition de « terminé » ; renvois documentés tenant lieu de cours (PROMPT_MEDINA, § 6.2, § 9.1 et § 17) | 07–08.10.2026 | Listes rouvertes ; complétude CIM-11 ; cours pour chaque catégorie ; R-5.1 et R-5.9. |
| Regroupements prévus I73 (I73, I77–I79), I83 (I83, I86, I87), I89 (I88, I89, I97), I95 (I95, I98, I99) ; renvois A43, I51, I52, R00–R03 (PROMPT_MEDINA, § 9.3 et § 19.3) | 08.10.2026 | Regroupements de la chaîne continue : I77 (I77–I79), I85 (I85, I86), I89 (I88, I89), I95 (I95, R03), I97 (I97–I99), I51, R00, R02. |
| Cours J20 « bronchite aiguë et bronchiolite (J20–J22) » (PROMPT_MEDINA, § 9.3) | 07.10.2026 | J40 — Bronchite couvre J20, J40, J41 et J42 ; R-9.15. |
| Atlas ECG présent dans tout l’atlas (PROMPT_MEDINA, § 7) | Carte des fragments | Réservé à C-01-Cardiologie ; R-14.13. |
| Branche de travail `claude/medina-alpha-integration-7dul4i` (PROMPT_REPRISE_IA ; PASSATION_REECRITURE) | 07.10.2026 | Branche propre à chaque session et PR vers la branche d’intégration ; R-18.8. |

## Annexe B — Points à arbitrer par Vial

Ces points ne créent aucune règle. Dans l’attente de l’arbitrage, la règle la plus exigeante pour la qualité s’applique (R-0.2).

- **B-1. Seuil CIM de la remise.** `production_plan.json` (`delivery_gate`) exige un fragment complet selon l’inventaire versionné CIM-11 avant transmission ; la chaîne continue admet une remise couvrant toutes les catégories CIM-10-GM 2024, le rapprochement CIM-11 restant exigé avant certification. La remise C-01-Cardiologie suit la seconde lecture.
- **B-2. Registre et validateur.** `production_plan.json` limite encore chaque IA à un chapitre actif (`max_active_chapters_per_agent: 1`), alors que la chaîne continue autorise plusieurs sous-agents sur plusieurs catégories du fragment.
- **B-3. Branche de destination des PR.** Les documents désignent `codex/sciences-cs-fragments-20261007` comme branche d’intégration, tandis que les publications récentes passent par `main` ; le protocole par fragment ne fixe pas la destination.
- **B-4. Portée de la « structure intouchable ».** La règle du front-end d’origine (`shell/medina_front.html`, embellissement par `polish` seulement) coexiste avec la refonte majeure des 22 frontends ; sa portée exacte (build global seul ou tous les rendus) n’est pas écrite.
- **B-5. Titres rouges soulignés et texte justifié.** Ces exigences typographiques de 2026-09 ne sont pas explicitement révoquées par l’adoption d’Atkinson ; leur maintien dans les nouveaux frontends n’est pas tranché.
- **B-6. Grille d’audit /20.** La grille /20 et le rapport `audits/<CODE>.md` ne sont pas cités par le protocole d’audit unique ; leur caractère obligatoire dans l’audit de fragment n’est pas tranché.
- **B-7. Coordination commune.** Le rôle de Codex comme « coordinateur prioritaire » pour les registres communs (`fragment_status.json`, `production_plan.json`) n’est pas précisé depuis le protocole symétrique.
- **B-8. Zones Compendium.** La vérification `tools/compendium_zones.py verifier <CODE>` et le fichier `<CODE>_compendium.json` figurent seulement dans `REGLE_ADMIN.md`, remplacé ; leur maintien n’est pas tranché.
- **B-9. Psychiatrie.** `FRAGMENTS.md` exclut le psychisme des 22 fragments ; `PROMPT_MEDINA` annonce un volet propre ; aucun calendrier n’est fixé.
- **B-10. Livrable global.** Les livrables `MEDINA_final.html`, `MEDINA_SOURCES.json` et la copie Drive `MEDINA_Claude.html` coexistent avec la publication Pages par fragment ; leur obligation à chaque livraison n’est pas tranchée.
- **B-11. Auditeur final de C-01-Cardiologie.** `COORDINATION.md` indique encore « à fixer » ; la chaîne continue, plus récente, désigne Codex. Le tableau de `COORDINATION.md` reste à aligner.

## Annexe C — Liste de contrôle d’alignement de Codex

Codex crée `docs/collaboration/receipts/CODEX_ALIGNEMENT_CUMUL_2026-10-08.md`. Pour chaque case, il écrit « lu et appliqué », le SHA complet du commit de ce cumul effectivement lu et, le cas échéant, l’écart constaté. Une case non cochée bloque la déclaration d’alignement.

- [ ] **Section 0** — Préséance : récence, exigence, ordre exactitude > exhaustivité > pédagogie > interface > économie. Commit lu : `<SHA complet>` ; mention : « lu et appliqué ».
- [ ] **Section 1** — Gouvernance : files 12 Claude / 10 Codex, audit croisé réciproque, aucune duplication. Commit lu : `<SHA complet>` ; mention : « lu et appliqué ».
- [ ] **Section 2** — Communication : français professionnel, livraison autonome, sans bavardage, annonces vérifiables. Commit lu : `<SHA complet>` ; mention : « lu et appliqué ».
- [ ] **Section 3** — Processus continu, corrections prioritaires, interruption distincte du STOP. Commit lu : `<SHA complet>` ; mention : « lu et appliqué ».
- [ ] **Section 4** — 22 fragments, nommage `code — intitulé (fragment)`, identifiants stables. Commit lu : `<SHA complet>` ; mention : « lu et appliqué ».
- [ ] **Section 5** — Complétude CIM : un cours par catégorie, cible CIM-11, mention « non établie ». Commit lu : `<SHA complet>` ; mention : « lu et appliqué ».
- [ ] **Section 6** — Fragment entier, producteur hors canonique, audit unique, injection par l’auditeur, garde CI, INJECTÉ immuable. Commit lu : `<SHA complet>` ; mention : « lu et appliqué ».
- [ ] **Section 7** — Sous-agents par catégorie, un auteur par fichier, Git réservé au responsable. Commit lu : `<SHA complet>` ; mention : « lu et appliqué ».
- [ ] **Section 8** — Contrat HTML : fichiers, classes fermées, préfixes, quatre onglets, aucun style en ligne. Commit lu : `<SHA complet>` ; mention : « lu et appliqué ».
- [ ] **Section 9** — Contenu : îlots, dernier îlot, Pareto, trois quiz, doses suisses, normal avant pathologique. Commit lu : `<SHA complet>` ; mention : « lu et appliqué ».
- [ ] **Section 10** — Justification de chaque affirmation, fenêtres, association distincte de causalité. Commit lu : `<SHA complet>` ; mention : « lu et appliqué ».
- [ ] **Section 11** — Sources suisses datées, texte intégral, contentieux par mot vert, Compendium. Commit lu : `<SHA complet>` ; mention : « lu et appliqué ».
- [ ] **Section 12** — Style : phrases complètes, annonce-développement-épilogue, aucun quota de mots. Commit lu : `<SHA complet>` ; mention : « lu et appliqué ».
- [ ] **Section 13** — Glossaire : définitions lettre à lettre, `audit()` = `{}`, aucune collision. Commit lu : `<SHA complet>` ; mention : « lu et appliqué ».
- [ ] **Section 14** — Frontend : Atkinson, thème clair exclusif, contrastes, isolement des spécialités. Commit lu : `<SHA complet>` ; mention : « lu et appliqué ».
- [ ] **Section 15** — Bouton « Isolate Federal – CH Exam » et `federal_exam.json`. Commit lu : `<SHA complet>` ; mention : « lu et appliqué ».
- [ ] **Section 16** — Sémiologie CS dans chaque fragment concerné, `cs_registry.json`. Commit lu : `<SHA complet>` ; mention : « lu et appliqué ».
- [ ] **Section 17** — Outils, constructions et tests réellement exécutés, global et fragment autonome. Commit lu : `<SHA complet>` ; mention : « lu et appliqué ».
- [ ] **Section 18** — GitHub : accord permanent, recensement des PR, accusés, branches préservées. Commit lu : `<SHA complet>` ; mention : « lu et appliqué ».
- [ ] **Section 19** — Captures réelles dans la conversation, pile visible, tableau de bord. Commit lu : `<SHA complet>` ; mention : « lu et appliqué ».
- [ ] **Section 20** — Sécurité : aucun secret, aucun jeton, dossiers protégés. Commit lu : `<SHA complet>` ; mention : « lu et appliqué ».
- [ ] **Section 21** — Arrêt : STOP explicite, arrêt après les 22 fragments, veilles en pause. Commit lu : `<SHA complet>` ; mention : « lu et appliqué ».
- [ ] **Annexe A** — Règles remplacées identifiées et abandonnées. Commit lu : `<SHA complet>` ; mention : « lu et appliqué ».
- [ ] **Annexe B** — Points à arbitrer lus ; règle la plus exigeante appliquée dans l’attente. Commit lu : `<SHA complet>` ; mention : « lu et appliqué ».
