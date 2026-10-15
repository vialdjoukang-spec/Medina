# Relecture réelle des cours — chaîne du 14 octobre

Ce document précise le format des preuves. Il ne produit aucun verdict et ne remplace ni les lectures ni les corrections. L’autorité reste `docs/collaboration/instructions/CHAINE_CYCLES_2026-10-14_EXECUTEUR.md`.

## Séquence et périmètre

- Une mission de relecture porte sur un seul cours. Le relecteur écrit uniquement dans son dossier de revue désigné ; il ne corrige pas les fichiers de l’auteur, le registre ou les sources canoniques.
- Avant la première lecture, consigner l’heure réelle, le rôle, l’identifiant runtime et les empreintes des sept sources, des images et des rapports reçus. Conserver ce relevé d’entrée immuable. Les horodatages sont des observations réelles, jamais une estimation rétroactive.
- Relire les instructions actuelles, le contrat suisse, le cahier et le Prompt de vérité. Appliquer les exigences à l’entrée et à la sortie ; distinguer les anciennes preuves de lecture et une revalidation plus récente.
- Passe 1 : lire le cours entier, ses fenêtres et glossaire, les passages originaux locaux et les sources primaires nécessaires ; relever les écarts précis. Terminer le rapport et attendre. Aucune deuxième passe dans la même phase sans signal du coordinateur après corrections auteur.
- L’auteur corrige sa propre remise, renouvelle son registre et ses empreintes. Le relecteur effectue ensuite une vraie passe 2 sur ces fichiers, contrôle les corrections et les conséquences dans toutes les surfaces concernées.
- Les quatre audits croisés doivent être clos avant la création des quatre contre-auditeurs à contexte neuf. Les contre-auditeurs ne sont aucun des quatre auteurs. Pendant les corrections, les auditeurs attendent.
- Toute réserve bloquante reste bloquante jusqu’à résolution vérifiée. Une note de 20/20 est un objectif à démontrer, jamais un résultat de gabarit. Une revue IA ne constitue pas une validation médicale humaine.

## Matière à vérifier

Lire les 21 parties et 126 sous-parties, les quatre onglets, les fenêtres, les tableaux, les calculs, les quiz, les définitions et la couverture des sous-codes. Vérifier la clarté en français, les connaissances de base, les unités, populations, limites et distinctions entre exemple fictif et observation publiée.

Les décisions diagnostiques, thérapeutiques et de suivi doivent être reliées au passage réellement consulté. Sources suisses prioritaires, recours européen motivé si lacune suisse, FI Swissmedic du produit exact pour les médicaments. Ne pas transformer une recommandation internationale, un essai ou une figure étrangère en règle suisse sans justification. Examiner aussi contre-indications, surveillance et exceptions, et pas seulement les doses.

Le registre des sources est un index à vérifier, pas une preuve suffisante par lui-même. Contrôler les correspondances affirmation/passage et les archives indiquées ; distinguer données fictives, calculs dérivés et faits issus de la source. Un produit cartésien de références n’est pas un appariement pertinent. Les sources intégrales restent locales sauf droit de redistribution établi ; publier des synthèses originales, des locateurs, empreintes, liens et courts extraits nécessaires.

Inspecter réellement chaque figure finale. Vérifier provenance, auteur, licence du fichier exact, attribution, éventuelles modifications, légende française, texte alternatif, lien d’agrandissement, identité de la zone et pertinence clinique. Un dessin publié ne doit pas être présenté comme une photographie, un graphique publié comme les données d’un patient fictif, ni un algorithme étranger comme une recommandation suisse. Les adaptations au cahier doivent être explicites et justifiées ; elles peuvent constituer une réserve si elles ne remplissent pas l’objectif pédagogique.

Ouvrir le rendu isolé et vérifier les interactions utiles. Les rapports UI du superviseur peuvent compléter la revue si les empreintes correspondent ; ne pas se les attribuer comme observations personnelles. Le contrôle final du coordinateur restera postérieur aux quatre contre-audits.

## Rapports de passes

Chaque `pass1.json` ou `pass2.json` contient au minimum :

- `code`, `actor`, `runtime_agent_id`, `pass` (1 ou 2), `started_at`, `finished_at` ;
- `dimensions` avec quatre observations substantielles : `redaction`, `medecine`, `sources`, `frontend` ;
- `numerical_checks` : au moins dix données numériques distinctes réellement vérifiées, chacune avec `claim`, `source`, `section`, `passage`, `finding` ;
- `blocking_reserves` : liste explicite, avec localisation, problème, source, correction attendue et degré de gravité ;
- `verdict`, `score` et justification de l’évaluation ;
- `final_files` : les sept sources exactes (chemins canoniques relatifs → SHA-256) ; `image_files` séparé ;
- un inventaire des passages et images réellement consultés, plus la version d’aperçu examinée.

La passe 1 peut être défavorable. La seconde ne peut être favorable et notée 20 que si les vérifications le démontrent et que les réserves bloquantes sont vides. Une erreur découverte pendant la passe 2 impose encore une correction et sa vérification, avec traces successives préservées.

## Reçu final d’audit

Après les deux passes réelles, `cross_audit.json` ou `counter_audit.json` suit `tools/tetrade_cycle.py::review`, avec les `PROMPTS` de `tools/night_cycle.py` :

- identité du cours, rôle exact, `runtime_agent_id`, `medical_human_validation: false` ;
- `entry` et `exit`, chacun avec rôle, date réelle, empreintes exactes des cinq Prompt files, verdict étayé et sept contrôles : `autorisation`, `perimetre_provenance`, `sources_lues`, `contexte_suisse`, `independance`, `contrat_cours`, `honnetete` ;
- chaque contrôle cite au moins une preuve relative au dépôt, avec SHA-256 et explication concrète ; les preuves d’entrée doivent rester immuables pendant les corrections ;
- `passes` avec les références `{path, sha256}` des deux rapports ;
- `final_files`, `image_files`, `blocking_reserves` ;
- `fresh_context: true` uniquement pour le contre-auditeur effectivement créé à contexte neuf.

La matrice suisse auteur peut contenir `auditor_verdict: pending_independent_review`. Ne la transformer en conformité qu’après vérification ligne par ligne. Conserver la matrice relue dans le dossier d’audit, sans réécrire celle de l’auteur à sa place, et documenter toute divergence.

## Corrections après clôture croisée

Le coordinateur archive les quatre reçus croisés initiaux, leurs passes et toutes leurs sources/images avant l’entrée des contre-auditeurs. Cette clôture initiale est immuable.

Si le contre-audit impose une correction, les empreintes initiales ne sont pas remplacées rétroactivement. L’auteur renouvelle sa remise ; le relecteur croisé examine les changements réels et rédige une preuve supplémentaire liée à la clôture initiale et aux nouveaux fichiers. Les nouvelles passes et revues portent de nouveaux noms, dates et empreintes. `tools/night_cycle.py::cross_boundary` précise les champs de `corrections_recheck`. Le contre-auditeur réalise ensuite sa deuxième passe sur les sources effectivement corrigées.

Les quatre dossiers doivent être prêts avant la première injection ; publication séquentielle avec lecture publique vérifiée à chaque fois. Le coordinateur tient seul les registres, commits, canoniques et reçus de publication.
