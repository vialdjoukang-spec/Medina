# Contrat des preuves — cycle 1

La consigne de lancement est l'autorité. `organisation/production_plan.json` conserve la répartition historique et ajoute une exception explicite limitée aux quatre systèmes et au cycle 1. `organisation/tetrade_cycle_status.json` suit les quatre chapitres sans déclarer les fragments complets. `tools/tetrade_cycle.py` complète la garde existante : aucun registre Claude ne peut autoriser à sa place une modification des quatre chapitres.

## Revue structurée

Chaque référence de preuve porte `path` relatif au dépôt et `sha256`. Le JSON de revue porte `code`, `actor`, `runtime_agent_id` (identité réelle de la mission), `medical_human_validation:false`, `entry`, `exit`, `final_files` et `blocking_reserves`. Chaque porte entrée/sortie porte `actor`, `verdict`, `checked_at` avec fuseau, `prompt_files` (empreintes des deux Prompts, du guide et de l'instruction de lancement), et `checks`.

Les sept vérifications sont `autorisation`, `perimetre_provenance`, `sources_lues`, `contexte_suisse`, `independance`, `contrat_cours`, `honnetete`. Chaque vérification favorable est documentée par des références d'artefacts existants, empreintes et explications précises. L'entrée vérifie l'application à la mission engagée ; la sortie vérifie le résultat livré. Un fait non vérifié n'est jamais marqué conforme pour satisfaire le schéma.

L'auteur ajoute `source_ledger` : référence d'une matrice ayant `code`, `final_files`, `covered_files`, `unverified_claims:[]`, `claims`. Chaque ligne comporte `claim`, `location`, `source_url`, `source_title`, `version_date`, `section`, `source_passage_summary` (reformulation fidèle), `population`, `limits`, `accessed_on`, `download_sha256`. Toutes les surfaces, y compris fenêtres, quiz, Pareto, sciences et glossaire, sont réellement relues. Le schéma contrôle la présence de ces preuves ; les auditeurs jugent leur exhaustivité et leur exactitude.

Les sources intégrales téléchargées restent dans le scratch partagé `/workspace/work/cycle1-sources-<CODE>/` pour les contrelectures. Le dossier publié conserve URL, version, localisation, empreinte et analyse ; il ne republie pas les articles ou informations professionnelles en entier.

## Deux passes de chaque audit

Le JSON de revue croisée ou différée ajoute `passes`, deux références numérotées 1 et 2. Chaque rapport de passe porte `actor`, `code`, `pass`, `started_at`, `finished_at`, `dimensions` (observations réelles : `redaction`, `medecine`, `sources`, `frontend`), `numerical_checks` (au moins dix, avec affirmation, source, section, passage et constat), `verdict`, `final_files`, `blocking_reserves`, `score`. La passe 1 relève les corrections ; la passe 2 relit le résultat corrigé. Une note de 19 à moins de 20 exige `minor_reserve_justification` et une décision motivée. Le contre-audit ajoute `fresh_context:true` et commence après clôture des audits croisés. Auteur, auditeur croisé, contre-auditeur et coordinateur sont distincts.

Toute modification médicale significative pendant le contre-audit impose une nouvelle relecture des versions modifiées par les auditeurs concernés. Les rapports sont liés aux empreintes finales ; aucune preuve périmée ne permet l'injection.

## Contexte suisse et contrôle final

La matrice suisse conserve les exigences historiques du contrat d'audit ; sa portée est ici `scope:"chapter"`, avec `fragment_id`, `chapter_code`, `source_files`, `unresolved_divergences:[]`, et toutes les décisions. Les produits exacts et passages FI restent obligatoires. `international` identifie honnêtement une source telle que l'OMS, avec manque suisse documenté et justification ; aucune recommandation américaine ne devient le fondement final d'une conduite. Ce changement ne modifie pas la portée des matrices historiques par fragment.

Le contrôle final ajoute `swiss_context` (verdict, chemin, empreinte) et `technical_checks` : référence d'un JSON avec empreintes finales, résultat des commandes exécutées, rendu ordinateur et mobile, fenêtres, erreurs JavaScript, abréviations, débordement et les deux PNG vérifiés. La garde ne remplace ni la revue scientifique, ni les contrôles réels de navigateur, ni une validation médicale humaine.

## Injection et publication distinctes

La première activation du registre ne peut modifier aucune source médicale. Les quatre chapitres doivent être prêts avant la première injection. Un commit d'injection ajoute exactement les sources d'un chapitre et une entrée nouvelle dans `chapters.json`, avec `covers` limité à la seule catégorie démontrée, `integrated:true` et `production_cycle:1`. Les sources et audits deviennent immuables après injection.

Un reçu distinct vérifie le SHA de `main`, le succès du déploiement, l'URL publique, la relecture du contenu et les jauges. Le chapitre suivant attend ce reçu. Le cycle 2 n'est pas autorisé ; la clôture du cycle 1 exige les quatre publications vérifiées et toutes les réserves bloquantes closes.
