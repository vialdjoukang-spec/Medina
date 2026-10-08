# Audit technique — I83 — Varices des membres inférieurs (C-01-Cardiologie)

Date : 8 octobre 2026. Sentinelle technique Codex. Inspection en lecture seule des objets Git ; aucun code entrant exécuté, aucun checkout, aucune mutation Git, aucune injection canonique.

- Livraison figée : `0974d854db292ae0311e435b3daea5fbed187e25`.
- Base canonique de comparaison : `ea105ace0046c71492cc6a69ff4c61698ef2ce34`.
- Inventaire vérifiable : [INVENTAIRE_TECHNIQUE.json](INVENTAIRE_TECHNIQUE.json), avec blobs Git, modes, empreintes SHA-256, résultats AST, identifiants, fenêtres et liens.

## Décision de cette inspection

**Conforme pour préparer une copie isolée des dix fichiers ci-dessous et de la seule entrée I83 dans `chapters.json`.** Aucun blocage statique de sécurité ou de contrat technique détecté dans ce périmètre. Cette décision permet au coordinateur de reconstruire et de tester sa proposition sur la base canonique indiquée. Elle ne certifie pas une injection, un rendu navigateur ou l'exactitude médicale.

Les résultats de construction et de navigateur du producteur ne remplacent pas les nouveaux contrôles indépendants du coordinateur. Aucun résultat de build, de navigateur, de mobile ou de publication n'est attribué au présent audit.

## Périmètre exact à reprendre

Les dix fichiers sont des ajouts par rapport à la base canonique, tous en mode Git `100644`. Leur chemin source et leur chemin cible sont identiques. Aucune modification d'un constructeur, d'un moteur JavaScript, d'un outil, d'un autre chapitre ou du glossaire canonique `cardio_1.py` n'est nécessaire.

| Source et cible autorisées pour la copie isolée | SHA-256 du blob entrant |
| --- | --- |
| `chapters/I83/I83_a.html` | `1610615e2f39a888d4ccb46b46b56a4ea0c5195f19dfd8af68cac511f7f0ff76` |
| `chapters/I83/I83_b.html` | `d336d0b4e4977212ffa192fe2c57a535db54f288daa2ce014c022d513ed9da9a` |
| `chapters/I83/I83_c.html` | `ed129bc2d10d36cca74a8a0ab6d3994e9ba101e65ffe3392e84ada8473e48261` |
| `chapters/I83/I83_d.html` | `8f4743ecd4d49746529b5d1ed7a13a5ed2285af33fb14a8795fa8116342244b3` |
| `chapters/I83/I83_pop1.html` | `a790feb6f96e5805da69f398daf23a617813424a44dad8d14d94e1b2348e36cd` |
| `chapters/I83/I83_pop2.html` | `e19683146892162c19e526fda676e558f21d42e894738b6a90ab3475086b1d55` |
| `chapters/I83/I83_pop3.html` | `c0c1dda088686b7abf4f2b38f4f858298a37c46e1d3003f50e06c6b221697c42` |
| `chapters/I83/I83_pop4.html` | `8b5a5d007ff4d789e15199bc19a658cc8a35b5388afb89f2804c6e521ba904d1` |
| `glossary/i83.py` | `b041af30d40c15eb16c0063dc7d83fa0a57c364608d36ccb38003bf2af7636b4` |
| `glossary/fragments_medina.py` | `8d3ecb13d21a3e1e0c53b144e024a564f5aaa0501dc6518b19dff05ebdc0fced` |

Onzième cible : ajouter uniquement cet objet au tableau canonique `chapters.json`, sans reprendre la branche entière :

```json
{
  "code": "I83",
  "covers": ["I83", "I87"],
  "title": "Varices des membres inférieurs",
  "integrated": true,
  "wave": 9,
  "added": "2026-10-08"
}
```

La comparaison JSON des deux SHAs constate exactement un ajout, aucune suppression et aucune modification des entrées préexistantes. Empreinte du `chapters.json` canonique : `087dd33c66da9e5bcfcb7a9ae02e1dab0c42b9e932e54d2c1786de8f49b00c67`. Empreinte du fichier entrant complet : `9458acf43c178c5f3800ca2e70cb60085549fa1f53a77b64439d74f20b882e42`. En cas d'avancée de la base, reprendre cet objet comme delta et conserver les ajouts concurrents.

## Inspection des deux modules de glossaire

Lecture par `ast.parse`, puis contrôle des instructions et extraction par `ast.literal_eval`, sans `import`, `eval` ou exécution du contenu entrant. Chacun des modules contient un unique import autorisé, `from cardio_1 import a, G`, puis exclusivement des appels directs à `a` dont tous les arguments sont des chaînes ou des listes de couples de chaînes littérales.

| Contrôle | `glossary/i83.py` | `glossary/fragments_medina.py` |
| --- | --- | --- |
| Entrées littérales | 33 | 5 |
| Appel ou instruction hors contrat | 0 | 0 |
| Argument calculé, étoilé ou nommé | 0 | 0 |
| Clé dupliquée dans le module | 0 | 0 |
| Clé en collision avec le glossaire canonique | 0 | 0 |
| Balisage actif dans les définitions HTML | 0 | 0 |

Le registre canonique `cardio_1.a` effectue seulement l'enregistrement dans `G` des données fournies. La vérification des collisions a inspecté les AST des 34 modules canoniques, y compris les enveloppes `t` et `b` autour de `a` ; aucune des 38 nouvelles clés n'apparaît comme chaîne littérale exacte dans leurs AST et aucune autre écriture dans `G` hors du registre canonique n'a été trouvée.

Toutes les références de fenêtres fournies par les 33 entrées du glossaire clinique se résolvent. Les cinq clés du glossaire transversal correspondent exactement à des libellés présents dans `organisation/fragments.json` : `C-01-Cardiologie`, `P-02-Pneumologie`, `I-03-Infectiologie`, `D-16-Dermatologie`, `M-21-Médecine de premier recours et santé publique`. Ce module ajoute leurs définitions textuelles ; il n'ajoute aucun chapitre de ces fragments.

## HTML, identifiants et navigation

Analyse par `HTMLParser` de la bibliothèque standard sur les huit blobs, dans leur ordre de construction. Le corps `a+b+c+d` et l'ensemble avec fenêtres ferment tous leurs éléments explicitement ouverts ; aucun décalage de fermeture n'a été détecté par ce contrôle statique.

| Contrôle | Résultat |
| --- | --- |
| Template de cours | Un unique `ch-I83` |
| Panneaux et boutons d'onglet | `pA`, `pE`, `pS`, `pP`, un chacun |
| Visibilité initiale | `pA` visible ; `pE`, `pS`, `pP` avec `hidden` |
| Sélecteurs scientifiques | Cinq, avec cibles `i83-s-anat`, `i83-s-histo`, `i83-s-physio`, `i83-s-bioch`, `i83-s-gen` présentes |
| Sections `ilot` | 31 |
| Fenêtres | 47 définitions uniques |
| Occurrences `data-k` | 85 ; aucune clé manquante |
| ID dupliqué dans la contribution | 0 |
| Nouvelle collision d'ID avec les autres chapitres canoniques | 0 |
| Collision de clé de fenêtre avec les autres chapitres canoniques | 0 |
| Lien interne non résolu | 0 |
| Classes hors du contrat | 0 |
| Pareto | Six ; toutes les sections `data-cover` existent comme `section.ilot` |
| Quiz | Six, dont cinq dans le fichier des examens/sciences |
| SVG | Huit |

Les IDs de contenu et les nouvelles clés de fenêtres portent le préfixe `i83-` ; les six fenêtres de synthèse portent `pareto-i83-`. Les IDs `pA/pE/pS/pP` sont les quatre emplacements communs attendus par le moteur dans chaque template : leur présence dans les autres cours est donc exclue du calcul des collisions nouvelles. Le titre H1 est « Varices des membres inférieurs », conforme à l'entrée du catalogue.

## Code actif et surfaces exécutables

Aucun élément `script`, `iframe`, `object`, `embed`, `base`, `link`, formulaire ou contenu SVG actif détecté. Aucun attribut d'événement `on…`, `srcdoc`, URL à schéma exécutable ou attribut CSS actif détecté. Les noms d'attributs observés sont conservés par fichier dans l'inventaire. Le balisage des définitions du glossaire a subi le même contrôle de contenu actif.

Les huit SVG utilisent des éléments géométriques et textuels ; aucune ressource externe ni événement incorporé n'est présent. Les liens HTML de la contribution sont internes. Les chaînes de sources bibliographiques sont des contenus textuels : ce contrôle ne confirme pas leur validité documentaire.

## Catalogue, couverture et rattachements

I83 — Varices des membres inférieurs (C-01-Cardiologie) et I87 — Autres atteintes veineuses (C-01-Cardiologie) n'ont aucun propriétaire de `covers` dans le catalogue canonique de la base inspectée. L'objet entrant ne provoque donc pas de collision d'alias entre cours.

Les entrées I83/I87 existent déjà dans les données canoniques de `shell/medina_front.html`, toutes deux sous « Vaisseaux et microcirculation ». L'application statique de la règle de rattachement de `build_front.py` les affecte exclusivement à `S01`, dont le libellé public est `C-01-Cardiologie`. Aucun autre fragment ne reçoit ces codes par cette règle. `fragments.json` et `organisation/fragments.json` sont identiques entre les deux SHAs ; aucun changement de rattachement n'est requis pour que le nouveau cours soit sélectionné dans le fragment.

`covers` décrit ici une correspondance technique de navigation. Il ne constitue pas une preuve de couverture médicale exhaustive de I87 ni de complétude du fragment.

## Contrôles restant au coordinateur

1. Reconstituer les dix blobs et le delta de catalogue sur une copie isolée de la base canonique ; vérifier leurs empreintes avant construction.
2. Exécuter les constructeurs et outils canoniques de confiance, puis les contrôles des fenêtres, des abréviations et des Pareto sur cette proposition.
3. Tester dans le navigateur les quatre onglets, les cinq sections scientifiques, les fenêtres, les quiz, les synthèses et la navigation I83/I87 dans `C-01-Cardiologie`, avec rendu étroit et absence d'erreur console.
4. Conserver séparément la décision médicale et ses éventuelles adaptations ; toute modification des blobs inspectés demande de nouvelles empreintes et un contrôle du delta concerné.

La présente sentinelle n'a écrit que ce rapport et son inventaire dans le répertoire d'audit assigné. Les sources canoniques et les références Git restent sous la responsabilité du coordinateur.

## Appendice — correction `20bee19a`, inspection du delta seulement

Livraison figée : `20bee19a6329f0a62126e9180bfc909207055e38`, comparée à `0974d854db292ae0311e435b3daea5fbed187e25`. Base canonique de référence conservée : `ea105ace0046c71492cc6a69ff4c61698ef2ce34`. L'inventaire historique `INVENTAIRE_TECHNIQUE.json` est conservé octet pour octet ; le nouvel état est décrit séparément dans [DELTA_20BEE19_TECHNIQUE.json](DELTA_20BEE19_TECHNIQUE.json).

**Delta techniquement conforme pour la prochaine copie isolée.** Parmi les dix sources autorisées, seul `chapters/I83/I83_pop4.html` change. Les sept autres HTML, les deux modules de glossaire et `chapters.json` sont identiques au SHA précédemment inspecté. Le mode Git reste `100644` et le nouveau blob est `685d2f9a869c4d11b2e69ec039fe77904eddbfda`.

L'empreinte calculée du nouveau fichier est `79ca90654e97fe00619ed3d76ad1847734b41c8f9019af32146b47d18f3d58d9`, exactement celle annoncée par le producteur. Cette empreinte remplace celle de `I83_pop4.html` pour la copie proposée au SHA `20bee19a` ; les neuf autres empreintes de l'inventaire historique restent applicables.

Le changement se limite à un paragraphe de la fenêtre `i83-d-tumescence`, ligne 50. Il précise les conservateurs du flacon multidose Rapidocain, les restrictions pour les volumes supérieurs à 15 mL, les contre-indications liées à certaines allergies et l'absence d'équivalence directe avec la recette de tumescence demandant 50 mL. Le contrôle présent décrit ce delta textuel ; sa validité clinique et documentaire appartient à l'audit médical.

La séquence complète des balises, attributs et commentaires analysés par `HTMLParser` est identique avant et après correction. Les huit clés `data-pop` de ce fichier, les trois occurrences `data-k`, les titres des fenêtres et les attributs de couverture Pareto restent identiques. Aucun ID ajouté, aucun contenu actif, événement, URL exécutable ou fermeture incorrecte détecté. Puisque les autres sources sont identiques, les 47 fenêtres et les 85 références du chapitre conservent leurs correspondances précédemment inspectées. Aucun code entrant n'a été exécuté.

Le commit accompagne cette source de trois pièces du producteur : modification de `rapport.md`, ajout de `controles/i83_native_main_ea105ac.json` et de `controles/simulation_main_ea105ac_JOURNAL.txt` dans le lot `2026-10-08-I83`. Elles ne sont pas reprises comme preuves de tests indépendants par cette sentinelle. Les contrôles du coordinateur sur la nouvelle copie doivent identifier le SHA `20bee19a` et la nouvelle empreinte ci-dessus ; des contrôles sur la copie `0974d854` ne valident pas ce texte corrigé.

Seuls cet appendice et le fichier de delta ont été écrits pour cette vérification. Aucune mutation Git ni canonique, aucune reconstruction et aucun test navigateur n'ont été exécutés par la sentinelle technique.

## Appendice — correction `20c67c0`, copie et reconstruction possibles

Livraison figée : `20c67c011e57eccd25b105b15f465becf7df7f2e`, comparée à `20bee19a6329f0a62126e9180bfc909207055e38`. **Avis technique favorable à la copie sélective et à la reconstruction isolée de cette nouvelle version.** Résultats détaillés : [DELTA_20C67C0_TECHNIQUE.json](DELTA_20C67C0_TECHNIQUE.json). Les inventaires antérieurs sont conservés.

| Source modifiée | SHA-256 réel à `20c67c0` |
| --- | --- |
| `chapters/I83/I83_d.html` | `d6a339fea23ae2ffb8aa16268972ec0e9708b997fbd44403b3a2478387bbc88f` |
| `chapters/I83/I83_pop4.html` | `04ef2f3e5d1985dc9a338f60c4a921a908b9d16c630b28cbb52fec3b05f18574` |

Seules ces deux sources changent : deux paragraphes du fichier de pharmacologie et une ligne de sa synthèse Pareto. Le texte ajoute la mépivacaïne à la conduite décrite pour une injection intra-artérielle et ses attributions documentaires ; il remplace également l'attribution automatique d'un œdème à un médicament par une démarche de suspicion, de comparaison clinique et de réévaluation. La conformité clinique de ces changements relève de l'audit médical.

Pour chacun des deux fichiers, la séquence des balises, attributs et commentaires est identique à la version précédente. IDs, clés `data-pop` et `data-k`, titres et couvertures Pareto restent identiques ; aucun contenu actif ni nouvelle anomalie de fermeture détecté. Tous deux restent en mode `100644`. Les huit autres sources, les deux modules de glossaire inclus, et `chapters.json` sont inchangés. Aucun nouvel audit AST ni test des objets identiques n'a été relancé.

Les pièces ajoutées dans le lot sont des preuves et contrôles du producteur : `preuves/injection_intra_arterielle_extraits.md`, `controles/i83_native_main_e5bde2b.json`, `controles/simulation_main_e5bde2b_JOURNAL.txt`, avec actualisation de `rapport.md`. Ce contrôle statique ne les transforme pas en preuves indépendantes de construction. Les prochains contrôles doivent porter sur la copie proposée à `20c67c0`, en conservant les modifications concurrentes de la base canonique choisie par le coordinateur. Aucune source canonique ou référence Git n'a été modifiée, aucun code entrant exécuté par cette sentinelle.

## Appendice — précision Rapidocain `6d5797c`

Livraison figée : `6d5797c6a902e430cd9d3e9dd5159ec507a1476a`, comparée à `20c67c011e57eccd25b105b15f465becf7df7f2e`. Le seul objet modifié dans le périmètre autorisé est `chapters/I83/I83_pop4.html`, ligne 50. Son **SHA-256 réel est `dede4bdcf1974bbff6c2b2874410b64ac1e15003371fc9d78b3436c4999174f4`**. Les neuf autres sources et `chapters.json`, soit les dix autres objets du périmètre, sont identiques.

Le paragraphe précise les présentations sans conservateur de Rapidocain, leur absence d'adrénaline et les règles de préparation locale de la solution de tumescence. Seul le texte change : la séquence de balises, attributs et commentaires, les huit clés de fenêtres, les trois références `data-k`, les titres et les couvertures Pareto restent identiques. Aucun ID ajouté, contenu actif ni nouvelle anomalie de fermeture détecté ; mode `100644` conservé.

**Avis technique favorable pour copier cette empreinte exacte et poursuivre les contrôles du coordinateur après validation médicale.** [DELTA_6D5797C_TECHNIQUE.json](DELTA_6D5797C_TECHNIQUE.json) conserve les empreintes, le texte du delta et les comparaisons. Les inventaires antérieurs sont préservés. Aucun code entrant, build ou test navigateur exécuté par cette sentinelle ; aucune mutation canonique ou Git. Les tests précédents ne clôturent pas cette version : la publication clinique reste conditionnée à la clôture des contrôles sur les sources effectivement injectées.
