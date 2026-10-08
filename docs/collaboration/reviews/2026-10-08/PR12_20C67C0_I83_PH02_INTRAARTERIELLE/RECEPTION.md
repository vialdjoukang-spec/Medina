# Réception Claude — I83, causalité médicamenteuse et injection intra-artérielle

## État

- **Repéré :** PR #12, branche `claude/loving-shannon-spwrhc`, tête `20c67c011e57eccd25b105b15f465becf7df7f2e`.
- **Reçu et archivé :** six objets originaux conservés sans modification sous `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_PR12_20C67C0_I83_PH02_INTRAARTERIELLE/`.
- **Empreinte agrégée :** arbre Git `f65ad81c54a97bf68fad6d9bb4e2df1fef0a6763`.
- **Intégré :** non.
- **Contrôlé techniquement par Codex :** non.
- **Publié :** réception documentaire uniquement.

## Comparaison de contenu

Le delta depuis la dernière tête reçue `20bee19a6329f0a62126e9180bfc909207055e38` comporte un commit et six fichiers nouveaux ou modifiés.

### PH-02 — chronologie et causalité

`I83_d.html` remplace « attribué au médicament jusqu’à preuve du contraire » par une formulation conditionnelle : la chronologie fait suspecter une origine médicamenteuse, puis elle est confrontée à l’examen, aux causes cardiaques, rénales, hépatiques ou thrombotiques et à l’évolution après adaptation. Le texte précise qu’une chronologie seule ne justifie pas l’arrêt automatique.

Cette correction est cliniquement plus sûre : la temporalité augmente la plausibilité, mais ne démontre pas la causalité. Elle évite aussi un arrêt médicamenteux automatique sans évaluation du rapport bénéfice-risque.

### Injection intra-artérielle accidentelle

`I83_d.html` et le Pareto de `I83_pop4.html` ajoutent la mépivacaïne comme alternative à la lidocaïne. La nouvelle preuve recopie deux informations professionnelles suisses :

- Aethoxysklerol, novembre 2022, Swissmedic 33273 ;
- Sclerovein, mai 2022.

Les deux extraits livrés décrivent 5 à 10 mL de lidocaïne ou mépivacaïne à 1–2 %, 500 UI d’héparine par la même aiguille, membre en position basse et hospitalisation en chirurgie vasculaire. Le cours attribue explicitement cette conduite aux informations professionnelles suisses.

La concordance interne entre preuve et proposition est établie. Elle ne vaut pas vérification indépendante des documents officiels : le portail AIPS officiel demande désormais une authentification. De plus, cette conduite doit rester présentée comme une instruction spécifique des informations professionnelles du produit et non comme une recommandation universelle fondée sur des essais ; l’urgence vasculaire et les protocoles locaux priment.

## Contrôles producteurs

Le nouveau JSON annonce :

- base `main` exacte : `e5bde2b5f94852851a6b2542b48e541ce6a72ef5` ;
- 1 923 contrôles, zéro défaillance et zéro erreur ;
- navigateur 1360 × 900 et mobile 390 × 844 ;
- 47 fenêtres canoniques, sept parcours imbriqués et aucune cible inaccessible ;
- 72 contrôles S01 réussis ;
- reconstruction de 22 fragments déclarée reproductible.

Les empreintes du journal concordent avec les deux propositions courantes : `I83_d.html` `d6a339fe…` et `I83_pop4.html` `04ef2f3e…`. Ces contrôles n’ont pas été reproduits indépendamment.

## Décision

**Réception et archivage sans injection.** Le `main` courant ne contient pas encore I83 ; appliquer deux fichiers isolés contournerait l’intégration complète du cours. I83 reste le chapitre Claude actif. Aucun chapitre, attribution, route ou fichier canonique de cours n’est modifié.

Les campagnes sont préservées : historique 30 cours / 15-15, cardiologie 20 cours / 10-10, fragments restants 21 / 11 Claude-10 Codex.

## Contrôles réellement exécutés

- lecture de la PR, de la branche, de la tête et de `main` ;
- inventaire distant paginé : 15 branches et 13 PR, pages suivantes vides ;
- comparaison `20bee19…20c67c0` : un commit, six fichiers ;
- comparaison sémantique des deux modifications médicales ;
- lecture intégrale des extraits Aethoxysklerol/Sclerovein fournis ;
- validation structurelle du JSON natif : `passed`, 1 923 contrôles, zéro échec, zéro erreur ;
- vérification des empreintes du journal et de la baseline ;
- tentative de consultation de la source officielle suisse, bloquée par l’authentification AIPS.

## Réserves

- copies Aethoxysklerol/Sclerovein non confrontées indépendamment aux documents officiels ;
- conduite intra-artérielle non contre-lue comme protocole universel : elle doit rester attribuée aux libellés produits et aux protocoles locaux ;
- `tools/livraison.py`, reconstruction, tests et navigateur non exécutés par Codex ;
- audit médical exhaustif de I83 inachevé ;
- aucune complétude CIM-11 certifiée.
