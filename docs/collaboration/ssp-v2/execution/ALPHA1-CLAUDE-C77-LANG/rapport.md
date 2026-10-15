# Audit linguistique agressif — C77, Tumeur maligne des ganglions lymphatiques, secondaire et non précisée

Mission ALPHA1-CLAUDE-C77-LANG · génération 1 · branche `claude/alpha1/c77-lang-g1` · base `f664dd9e8da71f647dd3dc4da18f509f8517959c` · conversation `alpha1-claude-c77-lang`.
Exécutant : sous-agent Claude Code (voir accusé issue 107), modèle et effort conformes au manifeste.

> Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée. Seul le dossier `docs/collaboration/ssp-v2/execution/ALPHA1-CLAUDE-C77-LANG/` est écrit.

## 1. Lecture et contrôles d’entrée

- Les sept fichiers de la leçon (onglets A à D, fenêtres 1 et 2, glossaire) ont été lus en entier, ainsi que `PROMPT_VERITE.md` et `STYLE_REDACTION.md`.
- Les sept empreintes SHA-256 recalculées sont conformes au manifeste (`lecture.empreintes_conformes = true`).
- Le moteur d’audit des abréviations (`build_medina.audit`) renvoie `{}` avant et après application de toutes les propositions : aucune abréviation sans clé de glossaire.

## 2. Tableau de bord

| Indicateur | Valeur |
|---|---|
| Propositions locales (`propositions.json`) | 523 |
| dont typographie (espaces insécables) | 390 |
| dont reformulations de fond constant | 133 |
| Renvois médicaux (rien n’est proposé) | 13 |
| Fichiers touchés | 7 sur 7 |
| `ancien` unique dans son fichier | 523 sur 523 (script) |
| Chevauchements entre propositions | 0 |
| Application dans trois ordres | résultat identique |
| Balises HTML après application | identiques ; glossaire Python compilable |

Répartition des 133 reformulations : phrases nominales ou télégraphiques 84, registre 8, répétitions 6, ambiguïtés 6, infinitifs injonctifs 5, ponctuation 5, lourdeurs 5, syntaxe 4, parallélisme 2, cohérence terminologique 2, grammaire 2, accords 2, intitulés 2.

| Fichier | Propositions | dont hors typographie |
|---|---|---|
| `C77_a.html` (Pathologie) | 80 | 16 |
| `C77_b.html` (Pathologie, suite) | 74 | 12 |
| `C77_c.html` (Examens, Sciences) | 104 | 12 |
| `C77_d.html` (Pharmacologie) | 42 | 5 |
| `C77_pop1.html` | 88 | 11 |
| `C77_pop2.html` | 127 | 76 |
| `glossary/c77.py` | 8 | 1 |

## 3. Constats par gravité

Le cours est globalement correct sur le plan grammatical : aucune faute d’orthographe lexicale, aucun mot répété par inadvertance et aucune apostrophe droite n’ont été détectés. Les défauts se concentrent en trois familles.

### 3.1 Typographie française : espaces insécables absentes (390 occurrences)

Aucune espace insécable n’existe dans les sept fichiers. Les espaces avant « ; : ! ? », entre un nombre et « % » ou une unité, à l’intérieur des guillemets « » et dans « 100 000 » peuvent donc se détacher en fin de ligne. Chaque occurrence est corrigée par une proposition de catégorie `typographie` (U+00A0 partout, par prudence sur le glyphe de l’espace fine dans la police du portail). Les caractères sont insérés littéralement dans `propositions.json` : ils s’affichent comme des espaces ordinaires. Source : Lexique des règles typographiques en usage à l’Imprimerie nationale, via l’article « Espace insécable » (section Usage, France).

### 3.2 Phrases nominales, infinitifs injonctifs, énumérations sans verbe (89 propositions)

`STYLE_REDACTION.md` § 2 les proscrit partout, y compris dans les fenêtres. Elles dominent dans les fenêtres du deuxième fichier (cytoponction, trocart, exérèse, immunothérapie, schémas par stade N, pronostic, carboplatine, paclitaxel) et dans les 46 puces des fenêtres « Pareto ». Exemples : « Ne pas coder en lymphome… » devient « Le médecin ne code pas en lymphome… » (C77-LANG-0010) ; « Faire le TEP-CT après la panendoscopie… » devient « L’erreur consiste à faire le TEP-CT… » (C77-LANG-0192) ; la suite de phrases nominales des paramètres clés est réécrite à chiffres constants (onglet B).

### 3.3 Erreurs de langue locales (44 propositions)

- Accords : « CK7 et CK20 négative » → « négatives » (C77-LANG-0233) ; « Le critère de modification est… la fonction rénale » → « Les critères… sont » (C77-LANG-0282) ; deux sujets coordonnés et verbe au singulier « simule » (C77-LANG-0068).
- Syntaxe : « un prélèvement obtient un tissu » (C77-LANG-0003) ; « oriente l’organe d’origine » → « oriente vers » (C77-LANG-0218) ; « une cause qui explique des adénopathies inexpliquées » (C77-LANG-0049).
- Répétitions et tautologies : « dans la radiochimiothérapie » (C77-LANG-0268), « Médicaments à éviter : aucun autre médicament à éviter » (C77-LANG-0294), « est normal, … est normal » (C77-LANG-0142), « déclarés… OFSP (déclarations 2021)… en 2021 » (C77-LANG-0045).
- Parallélisme : « les cellules tumorales, immunitaires et fibroblastes » (C77-LANG-0032 et 0253).
- Ponctuation : virgule absente devant « car » (C77-LANG-0227, 0298), virgule superflue devant « et » (C77-LANG-0029), deux parenthèses consécutives (C77-LANG-0068).
- Intitulés incohérents entre bouton et fenêtre : deux titres de Pareto (C77-LANG-0476 et 0497).
- Registre : « se fait à l’hémogramme », « viennent du médiastin », « le reste du corps », « fermer une option » (image écartée par STYLE § 7).

## 4. Renvois médicaux (aucune proposition)

La forme touche ici le fond ; le détail est dans `rapport.json` (constats R1 à R13).

| Id | Point |
|---|---|
| R1 | « 5 pour 100 000 » sans période pour l’incidence de la tuberculose |
| R2 | « plus de 10 à 15 mm » : seuil ou fourchette ? |
| R3 | « Plusieurs lésions palpables ne sont pas des adénopathies », puis « une adénopathie après vaccin » : contradiction logique |
| R4 | « chacun est daté » alors qu’une seule ligne du tableau porte des années |
| R5 | « ethnie caucasienne » : terme de la source |
| R6 | « Cette observation explique… » : causalité tirée d’un modèle animal |
| R7 | neutrophiles « trop bas » sans chiffre pour le carboplatine |
| R8 | « formule sanguine » et « hémogramme » dans la même phrase |
| R9 | seuils de neutrophiles 500 et 1 500/mm³ sans distinction sous traitement et avant cure |
| R10 | Onkopedia qualifiée de « recommandation européenne » |
| R11 | « ce délai » : 12 semaines ou 3 semaines ? |
| R12 | « 57 % contre 82 % » selon la rupture capsulaire, sens non précisé |
| R13 | « du col » seul (col de l’utérus ?) |

## 5. Recommandations globales (sans proposition)

- Italique des titres de périodiques et de sources dans le corps du texte (plus de soixante-dix occurrences) : à traiter par le moteur.
- Anglicismes « sein-like », « côlon-like », « rein-like », « tête-et-cou-like » : graphies hétérogènes, décision éditoriale.
- Options de quiz à l’infinitif : conservées par convention, malgré STYLE § 2.
- Nombres à quatre chiffres (1500, 7093) laissés sans séparateur.

## 6. Lacunes

- Aucun correcteur automatique (Antidote, LanguageTool) n’a été exécuté : des fautes isolées peuvent subsister.
- Le Lexique de l’Imprimerie nationale n’a pas été lu directement (niveau « section » d’un article qui le cite).
- La compatibilité de U+00A0 avec le moteur et la police du portail n’a pas été testée dans un navigateur.
- Le manifeste porte `source_snapshot_sha = bfc4576b…` alors que le worktree est sur `f664dd9e…` ; les sept empreintes sont conformes dans les deux cas.
- Aucune vérification médicale n’a été faite : mission strictement linguistique.

## 7. Livrables

`rapport.json`, `rapport.md`, `propositions.json` dans `docs/collaboration/ssp-v2/execution/ALPHA1-CLAUDE-C77-LANG/`.
