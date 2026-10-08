# Réception PR #12 — J45-2 — J45 — Asthme (P-02-Pneumologie)

Date : 8 octobre 2026

## Décision

La remise Claude `2026-10-08-J45-2` à la tête `c3dd8cd0791fef551089bf6240f2adf45f0586fe` est **reçue et archivée**, mais **non injectée**.

Elle remplace le lot J45 initial à `f30b891`, reçu au commit `88cba09` et jamais injecté. Sept des neuf propositions changent réellement ; `J45_a.html` et `J45_justifications.json` sont identiques au premier lot et ne sont pas réappliqués séparément.

## Provenance et périmètre

- PR : https://github.com/vialdjoukang-spec/Medina/pull/12
- branche : `claude/loving-shannon-spwrhc`
- tête : `c3dd8cd0791fef551089bf6240f2adf45f0586fe`
- base déclarée : `28c0a58486d58ee1e5d4ef4515aa1080b9046e61`
- main contrôlé : `883869c780f8dff0704014e7125c9dca23710542`
- fragment : S02 — P-02-Pneumologie
- chapitre : J45 — Asthme ; catégories couvertes J45/J46
- campagne : 21 fragments restants, 11 Claude / 10 Codex
- campagnes distinctes conservées : historique 30 cours, 15/15 ; backlog cardiologique 20 cours, 10/10
- attribution et chapitre actif : aucune modification

## Empreintes et réconciliation

Les neuf SHA-256 de proposition sont exacts. Les neuf SHA-256 de baseline sont exacts sur la base déclarée et restent exacts sur le main contrôlé. Aucun conflit de contenu ni de chemin n'est détecté sur les cibles `chapters/J45/`.

Delta réel depuis le lot J45 initial :

- inchangés : `J45_a.html`, `J45_justifications.json` ;
- modifiés : `J45_b.html`, `J45_c.html`, `J45_d.html`, `J45_pop1.html`, `J45_pop2.html`, `J45_pop3.html`, `J45_pop4.html`.

Les 15 fichiers originaux du lot sont archivés sans modification avec leurs blobs Git, leur provenance et l'arbre immuable de l'archive.

## Contrôles indépendants exécutés

- inventaire distant paginé : 16 branches puis page vide ; 13 PR puis page vide ;
- comparaison `c68d96a…c3dd8cd` : un commit, 16 fichiers ;
- 9/9 SHA-256 de proposition et 9/9 SHA-256 de baseline ;
- 47 identifiants uniques, aucun doublon ;
- 47 modèles de fenêtre uniques et 47 clés de déclencheur uniques, correspondance complète ;
- aucune référence `aria-controls`, `data-p` ou `data-cover` orpheline ;
- aucun script embarqué dans les huit HTML ;
- JSON des justifications valide : 15 entrées et 15 identifiants uniques ; cibles et ancres présentes ;
- contrelecture médicale ciblée des sept fichiers modifiés.

Les résultats producteurs sont archivés mais n'ont pas été reproduits : sigles `{}`, statique 38 410 mots/47 fenêtres/8 quiz/8 Pareto, 15/15 justifications, 22 fragments reproductibles, 2 340 contrôles natifs sans échec aux largeurs 1 360 et 390 px, 118 tests.

## Contrelecture médicale ciblée

### J45-MED-01 — substantiellement levée

Les informations professionnelles suisses ciblées concordent avec la remise pour Symbicort, Foster, Atrovent et Spiriva. Les données Trimbow concordent également avec la page Compendium indexée.

- Symbicort : https://compendium.ch/fr/product/93068/mpro
- Foster : https://compendium.ch/fr/product/1384292/mpro
- Atrovent : https://compendium.ch/fr/product/2600/mpro
- Spiriva Respimat : https://compendium.ch/fr/product/1413224/mpro
- Trimbow 172/5/9 : https://compendium.ch/de/product/index/1514226-trimbow-aeros-doseur-172-g-5-g-9-g

Réserves non bloquantes conservées : critères détaillés de limitation OFSP non relus ; commercialisation actuelle du reslizumab non confirmée.

### J45-MED-02 — encore bloquante

Les catégories PD20, la liste détaillée de contre-indications de la méthacholine et les critères mannitol non relus ont été retirés. Les seuils conservés et la contre-indication pendant la grossesse correspondent à GINA 2026 : https://ginasthma.org/2026-gina-strategy-report/

Cependant, `J45_c.html`, `J45_pop2.html` et `J45_pop4.html` gardent des affirmations catégoriques selon lesquelles les tests indirects seraient plus spécifiques, refléteraient l'inflammation active, serviraient à confirmer et que le mannitol prédirait la réponse aux corticostéroïdes. GINA 2026 ne suffit pas à étayer l'ensemble de ces formulations. Il faut relire et citer le standard primaire Hallstrand 2018 (DOI 10.1183/13993003.01033-2018), ou atténuer/supprimer ces passages.

### J45-MED-03 — non levée

La contrelecture reste ciblée. Elle ne certifie pas exhaustivement les 38 410 mots, les 47 fenêtres, les huit quiz, les huit Pareto et toutes les études primaires du cours.

## Contrôles non exécutés

Le dépôt, `tools/livraison.py`, le runtime complet et le navigateur local ne sont pas disponibles dans cet espace. L'injection, la reconstruction, les tests unitaires et les vérifications interactives ordinateur/mobile n'ont donc pas été reproduits. Aucun statut de validation technique complète ni de publication du site n'est attribué.

## État

- repéré : oui ;
- reçu : oui ;
- intégré : non ;
- contrôlé techniquement : contrôles statiques et empreintes seulement, contrôles producteurs non reproduits ;
- publié : documentation de réception uniquement.
