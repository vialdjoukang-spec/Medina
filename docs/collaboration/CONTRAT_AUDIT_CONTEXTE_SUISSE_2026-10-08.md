# Contexte suisse : condition bloquante de l'audit final

Instruction directe de Vial du 8 octobre 2026. Le tableau de **tout MEDINA**, son taux initial d'utilisation de ressources américaines et sa mesure après correction sont confiés à Claude Code. Chaque producteur reste responsable de son fragment. La règle médicale suisse concerne les **22 fragments**. Depuis l'instruction Claude Leader plus récente, la matrice ci-dessous et la garde s'appliquent à la voie d'audit croisé structurée ; la chaîne interne Claude applique le même fond médical avec son propre contrôle et injecte sans audit Codex.

## Décision médicale attendue

L'auditeur refuse un verdict favorable lorsque la conduite enseignée diverge d'une recommandation suisse applicable sans explication, lorsqu'une posologie ou une prescription n'a pas été vérifiée dans la FI Swissmedic/Compendium du **produit exact**, ou lorsqu'une affirmation décisive n'est pas rattachée à un passage réellement lu. La source suisse spécialisée est examinée en premier ; IUSTI/BASHH ou une autre société européenne publiée documente les lacunes ou désaccords. Une ressource CDC/NIH/FDA peut rester tracée comme provenance initiale ou comparaison historique, mais aucune recommandation américaine ne fonde la conduite finale du cours. Une lacune suisse appelle une source européenne publiée ou, à défaut, l’OMS ; sinon la décision demeure bloquée. L'information professionnelle du produit et la recommandation clinique ont des rôles différents ; l'auditeur indique leur éventuelle tension.

L'auditeur ne note `conforme` qu'après lecture des passages, vérification des dates et de la population, de la formulation du cours et de la résolution des écarts. Un document introuvable, un simple résumé ou une directive en projet ne valent pas passage vérifié. S'il n'existe pas de recommandation suisse applicable, la recherche infructueuse est tracée et l'option européenne est examinée ; une origine américaine finale est refusée, même si une lacune suisse et européenne est documentée. L'absence de source applicable non démontrée reste bloquante.

## Matrice obligatoire sur les sources finales

La preuve `cross_audit.swiss_context` du registre `organisation/fragment_status.json` porte `verdict: "conforme"`, `matrix_path` et `matrix_sha256`. La matrice JSON doit être un fichier régulier du dépôt et contenir :

- `schema_version: 1`, `fragment_id`, `scope: "fragment_complet"` ;
- `source_files` : exactement les empreintes des fichiers **finaux après corrections** de l'auditeur ;
- `unresolved_divergences: []` ;
- `decisions` : une ligne pour chaque décision clinique décisive, notamment les tests, traitements, doses, voies, contre-indications et suivi. Chaque cours du fragment doit apparaître ; tout cours avec un onglet `_d.html` doit avoir au moins une ligne `medication`.

Chaque ligne porte `id`, `chapter_code`, `kind` (`diagnostic`, `treatment`, `medication`, `follow_up`), `claim` tel qu'enseigné, `initial_primary_origin` et `final_primary_origin` (`swiss`, `european`, `american`), `divergence_status` (`none` ou `resolved`) et `auditor_verdict: "conforme"`. Une divergence résolue ou une source finale non suisse exige `resolution`. La valeur finale `american` est interdite, même si un manque suisse/européen a été documenté ; elle reste dans le schéma pour représenter la provenance initiale.

`swiss_guideline` porte soit `status: "applicable"` avec `organization`, `title`, `url`, `version_date`, `section`, `passage`, soit `status: "documented_gap"` avec `searched_on`, `search_scope`, `searched_sources`, `gap_reason`. Le second état ne permet pas de déclarer l'origine finale `swiss`.

`foreign_sources` liste les recommandations européennes/américaines réellement consultées qui fondent les origines initiale ou finale non suisses. Chaque entrée porte `origin`, `organization`, `title`, `url`, `version_date`, `section`, `passage`. Pour `kind: "medication"`, `swissmedic_product` porte `product_name`, `authorization_number`, `url`, `accessed_on`, `section`, `passage` de la FI suisse du produit exact. Une simple DCI ou une fiche d'un autre produit ne satisfait pas la vérification clinique.

Le taux descriptif par matrice se calcule sur les **mêmes lignes** avant/après : nombre de lignes `initial_primary_origin == "american"` puis `final_primary_origin == "american"`, divisé dans les deux cas par le nombre de décisions recensées. Claude définit et publie séparément le périmètre, le dénominateur et les deux tableaux de **tout le projet** pour éviter de confondre présence d'une citation américaine et dépendance principale d'une décision.

## Portée de la garde

`tools/espace.py` refuse l'audit final ou l'injection si la preuve manque, si la matrice ne correspond pas aux fichiers finaux, si un chapitre manque, si un produit exact n'est pas documenté ou si une divergence reste ouverte. Ce verrou vérifie la **présence et la cohérence structurelle des preuves** ; il ne juge pas la vérité médicale d'une citation, l'applicabilité d'une FI ni la qualité d'un arbitrage. Ces vérifications relèvent de l'auditeur croisé et demeurent bloquantes même si le JSON passe. Les chapitres en version de travail peuvent être publiés comme aperçus sans prétendre avoir franchi cet audit.
