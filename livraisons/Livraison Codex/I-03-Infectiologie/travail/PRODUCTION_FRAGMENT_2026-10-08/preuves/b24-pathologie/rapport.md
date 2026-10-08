# B24 — panneau clinique et fenêtres associées

Rédaction du 8 octobre 2026, dans le cadre de la production interne du fragment entier I-03-Infectiologie. Cette livraison contient le panneau pA et ses fenêtres. Elle ne représente ni validation médicale humaine, ni audit final, ni injection, ni déclaration de complétude de T1.

## Fichiers livrés et contrat

Seuls les deux fichiers attribués à cet auteur ont été écrits dans le dépôt : `sources/chapters/B24/B24_a.html` et `B24_pop1.html`, sous `livraisons/Livraison Codex/I-03-Infectiologie/travail/PRODUCTION_FRAGMENT_2026-10-08/`.

`B24_a.html` ouvre exactement le template `ch-B24` et le conteneur `chap`, fournit l’en-tête et les quatre onglets pA/pE/pS/pP, puis le panneau pA entier. Le fichier ferme seulement `chap-body` et pA ; `chap` et `template` restent ouverts pour les trois autres auteurs. Il contient treize sections : question clinique ; définitions/stades/codage ; épidémiologie ; transmission ; anamnèse ; examen ; diagnostic/différentiels ; urgences ; infections opportunistes ; prise en charge ; suivi ; prévention/I=I ; populations et limites.

`B24_pop1.html` contient 25 templates, tous préfixés `b24-pa-`, avec un titre et une source consultée ou un appui explicitement identifié. Les deux quiz ont chacun une seule réponse `data-ok="1"`, des propositions alternatives et une explication masquée `p.fb[hidden]`. Les deux boutons Pareto ouvrent chacun leur fenêtre propre ; aucune proportion de bénéfice n’est inventée pour ces synthèses.

## Cas commun et interprétation

Les seuls faits sont ceux de l’énoncé : M. L., 34 ans, fièvre, amaigrissement, candidose orale, VIH-1 confirmé, ARN 180 000 copies/mL, CD4 86/µL, sans dyspnée ni atteinte initiale du système nerveux central. Aucun traitement antérieur, résultat de résistance, sérologie, antigène cryptococcique, fonction rénale, voie de transmission ou infection profonde n’a été ajouté.

Le cas remplit le critère immunologique CDC de stade 3, sous réserve de l’exception de stade 0 si l’histoire des tests prouve une infection récente : cette histoire n’est pas donnée. La candidose orale n’est pas elle-même une affection définissante CDC du sida. Une candidose orale persistante entre dans le stade clinique OMS 3, mais sa persistance n’étant pas donnée, ce stade clinique n’est pas imposé au cas. La maladie avancée OMS est déjà établie par les CD4 inférieurs à 200/µL.

Le cours distingue le libellé local B24 (« Immunodéficience humaine virale [VIH], sans précision », catalogue CIM-10-GM 2024) du périmètre éditorial adulte plus large. Le bloc officiel BfArM montre que toutes les manifestations connues ne relèvent pas indistinctement de B24. Aucune équivalence avec CIM-11 MMS 1C62.1 n’est affirmée.

## Points de version réellement vérifiés

- OMS : fiche du 27 juillet 2026, estimations mondiales de 2025 (41,0 millions de personnes vivant avec le VIH ; 1,2 million d’acquisitions ; 570 000 décès). Les chiffres 2024 de pages antérieures ne sont pas mélangés.
- OFSP : bulletin 44/2025 du 27 octobre 2025, 318 cas déclarés en 2024 en Suisse/Liechtenstein et 3,5/100 000 ; données arrêtées au 17 février 2025. Cas déclarés et acquisition dans l’année sont distingués.
- Diagnostic suisse : directive OFSP 2025 **version 4 du 10 juillet 2026**, effectivement lue en PDF. Diagnostic sur au moins deux techniques et vérification médicale ultérieure sur second échantillon sont distingués ; la confirmation initiale ne doit pas être présentée comme attendant nécessairement le second prélèvement. Le périmètre >18 mois et les exclusions périnatales/piqûres d’aiguille sont indiqués.
- NIH : Baseline Evaluation porte le 24 septembre 2026 ; Initiation of ART et Treatment as Prevention portent le 25 septembre 2025. Le millésime d’un recueil ne remplace pas la date de chaque section.
- Pneumocystose NIH : section revue le 27 mai 2026. À l’initiation/non traité, la prophylaxie est indiquée pour CD4 <200/µL (AI). La règle distincte de reprise chez une personne déjà sous ARV n’a pas été appliquée abusivement à l’initiation.
- I=I : la prévention sexuelle concerne la suppression maintenue <200 copies/mL, y compris une valeur mesurable inférieure au seuil. La recommandation NIH de prévention supplémentaire pendant les six premiers mois **et** jusqu’à documentation de suppression est identifiée comme telle ; elle n’est pas transformée en délai universel EACS.
- EACS : version 13.0, édition 2025, confirmée sur la page officielle. Les détails du site interactif ne sont pas présentés comme consultés par cet auteur.

La pharmacie conserve les choix de régime, doses et conditions précises des bithérapies. Le panneau pA n’utilise pas un seuil ARN 500 000 universel pour DTG/3TC et ne présume ni VHB négatif ni absence de résistance.

## Sources et limites d’accès

`sources_lues.json` documente 25 URL effectivement ouvertes et leurs passages, versions, usages et limites. Les fenêtres et le cours proposent des liens consultables ; les paraphrases sont originales, sans longues citations copiées. Les applications au cas sont distinguées des recommandations.

Le site interactif EACS a échoué à l’ouverture par l’outil. Pour les recommandations OMS de maladie VIH avancée du 18 décembre 2025, la page de publication et son résumé ont été lus, mais le PDF n’a pas été obtenu : aucune lecture intégrale ni recommandation détaillée de ce PDF n’est prétendue. L’URL de base NIH candidose ayant échoué, la variante officielle `?view=full`, effectivement accessible, a été utilisée. Le réseau shell a refusé l’archivage des pages ; aucune copie complète locale de ces nouvelles sources n’est annoncée.

Le CDC fournit certains principes dans un cadre américain. Le cours signale les limites pour les calendriers, le dépistage cryptococcique, la PEP et la vaccination ; il n’invente pas de recommandation suisse universelle à partir de ces pages. L’ancienneté réelle des textes de surveillance CDC et des stades OMS est explicitée.

## Contrôles internes et suite

Contrôles de connectivité et de contrat passés : 25 clés d’ouverture pour 25 fenêtres, aucune manquante ou orpheline, aucun doublon de fenêtre/ID dans ces deux fichiers, tous les liens locaux résolus, quatre onglets attendus, pA seul présent, deux quiz correctement balisés, liens externes avec `noopener`, ouverture et fermeture conformes. Une vérification stricte des balises confirme les deux éléments laissés ouverts à dessein dans a et aucune balise ouverte dans pop1. Les résultats et empreintes sont dans `controles.json`.

Ces contrôles portent sur les deux fichiers attribués, pas sur la navigation finale ni sur la cohérence complète des quatre panneaux assemblés. L’assemblage doit intégrer une seule fois ce jeu de fenêtres, vérifier les interactions de l’engine et les renvois des autres auteurs, puis confronter les panneaux sur les seuils, versions et faits du cas. Cela constitue un contrôle interne de chapitre ; l’unique audit croisé final reste au niveau du fragment entier selon le protocole actif.

La retouche interne finale a supprimé, dans la fenêtre candidose, la promesse de doses antifongiques dans l’onglet pharmacologique : elle renvoie désormais à une prescription contextualisée avec l’infectiologue. Aucune dose ni nouvelle source n’a été ajoutée. Les fenêtres stades et suivi ont aussi été resserrées pour limiter les répétitions des textes institutionnels, en conservant le raisonnement et les limites du cas.

Les deux fichiers sont figés pour l’assemblage interne après cette retouche. Leurs empreintes finales figurent dans `controles.json`. Ce gel de travail n’est pas un statut INJECTÉ.

Aucun fichier canonique, statut, audit final, commit ou branche n’a été modifié par cet auteur.
