# Audit technique de réception — I83 — Varices des membres inférieurs (C-01-Cardiologie)

État : **reçu pour examen ; audit statique partiel ; aucune injection, reconstruction ou publication**.

Version examinée : `8dfa6ba453fc872591b79e5720c914ce47964470`. La tête `5bee2a48ef1804a0e3452d64a1041e0bd1b50691` annoncée ensuite par le coordinateur conserve les huit blobs HTML et le rapport. Les deux blobs glossaire calculés correspondent aux valeurs distantes communiquées : `d3d7d7e784340d6b0b5d0178c6ccaf0fa15fe964` et `68632417b2e0fa406bace348373cfed33155a1f2`.

## Instructions et périmètre

AGENTS.md, DELIVERY_PROTOCOL.md, tools/livraison.py (lecture intégrale) et rapport original de la remise lus. Seuls les huit fichiers `chapters/I83/`, les deux glossaires et le catalogue récupérés ont été analysés. Aucune attribution ni source de cours n’a été modifiée. I89 — Autres affections non infectieuses des vaisseaux et des ganglions lymphatiques n’a pas été intégré.

La création de cours se reçoit par revue de branche et PR, conformément au protocole. `apply-claude` est limité aux cours déjà intégrés et ne couvre ni ajout du registre de chapitre, ni glossaires communs : il n’a donc pas été exécuté pour cette création.

## Contrôles réellement exécutés

Les contrôles utilisent Python 3, hashlib, json, ast, html.parser et BeautifulSoup ; aucune dépendance du code de production n’a été importée ou exécutée.

| Contrôle | Résultat |
| --- | --- |
| Lecture brute, UTF-8 et SHA-256 des dix sources annoncées | 10/10 correspondent exactement au rapport ; aucune normalisation de fin de ligne nécessaire. |
| Empreintes Git blob | Calculées sur les octets bruts des dix sources, du catalogue et du rapport ; valeurs complètes dans INVENTAIRE_TECHNIQUE_I83.json. |
| Noms et contenu du catalogue | Une entrée I83 — Varices des membres inférieurs, `covers` I83/I87 ; gabarit `ch-I83` conservé. |
| Emboîtement explicite des balises | Concaténation a/b/c/d sans fermeture orpheline ni balise restante ; quatre fichiers pop vérifiés séparément, sans erreur. Ce contrôle statique ne certifie pas le rendu HTML. |
| Identifiants HTML | 41 identifiants, aucun doublon. |
| Fenêtres et mots cliquables | 47 fenêtres uniques, 83 boutons `data-k`, 47 clés distinctes ; aucune référence locale non résolue. |
| Ancres de plan | Aucune cible `href="#…"` absente. |
| Onglets | Quatre onglets principaux pA/pE/pS/pP, cinq onglets Sciences ; cibles locales présentes. |
| Quiz et Pareto | Six quiz et six boutons Pareto présents. Leur comportement JavaScript n’a pas été exécuté. |
| Figures | Trois figures SVG légendées et cinq SVG d’icônes ; le total huit SVG ne contredit pas les trois figures annoncées. |
| Glossaire I83 | AST Python valide, 33 entrées, aucun terme dupliqué ; toutes les références aux fenêtres se résolvent. PIK3CA est déjà fusionné dans le glossaire livré. |
| Glossaire fragments partagé | AST Python valide, cinq entrées, aucun doublon interne. |
| Scripts locaux | Aucun élément script dans les huit sources ; le comportement dépend du moteur externe non récupéré. |

Le h1 porte le nom complet, avec le code I83 placé dans le bloc de code voisin. Cela conserve l’association code et nom dans l’en-tête et le catalogue. Les libellés partagés suivent la nomenclature de fragment demandée. La position visuelle du code, les contrastes, catégories et routes du site restent à vérifier dans la coque réelle.

## Réserves et limites

**TECH-I83-01 — bloquante avant injection :** checkout du dépôt incomplet. La coque et le moteur, `build_front.py`, les tests, les registres `fragments.json`/`organisation/fragments.json` et `glossary/cardio_1.py` ne sont pas présents dans le périmètre local fourni. La reconstruction et la navigation du vrai site n’ont pas été exécutées. Les 1 887 contrôles natifs et les autres résultats du rapport sont des déclarations de Claude, non des contrôles réexécutés par Codex.

**TECH-I83-02 — avant intégration :** rapprocher la proposition de la vraie tête main, contrôler la différence exacte de chapters.json et les imports globaux du glossaire. Le champ `integrated: true` dans le catalogue de la branche est un état proposé ; il ne prouve pas l’intégration sur main.

**MED-I83 — transmis à la contre-lecture médicale :** le quiz de `I83_a.html` propose « Classe la plus élevée C4a, avec C4c », alors que le domaine C décrit aussi une corona phlebectatica C4c. Le feedback et le cas reprennent cette hiérarchie. Il faut vérifier la règle CEAP 2020 sur une source primaire et harmoniser les mentions avant décision ; cet audit technique ne tranche pas le point médical.

La liste de réserves médicales du rapport reste à examiner indépendamment. Un contrôle statique réussi ne lève aucune réserve médicale, ne certifie pas la relecture exhaustive des 30 cours et ne démontre aucune complétude CIM-11. Le référentiel livré reste déclaré CIM-10-GM 2024.

## Décision proposée

Recevoir et archiver les originaux avec leurs empreintes, puis conserver l’injection bloquée jusqu’à l’audit médical et à la reconstruction/navigation de la version réconciliée. Les empreintes et liaisons HTML locales ne présentent pas de défaut constaté.
