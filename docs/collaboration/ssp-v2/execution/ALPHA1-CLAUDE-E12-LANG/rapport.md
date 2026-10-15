# Audit linguistique agressif — E12 Diabète sucré de malnutrition

Mission ALPHA1-CLAUDE-E12-LANG, génération 1, branche `claude/alpha1/e12-lang-g1`, commit de base `f664dd9e`. Audit IA : revue distincte d’une validation médicale humaine ; aucune source canonique modifiée. Date : 15 octobre 2026.

## Résumé pour Vial

Les sept fichiers de la leçon (quatre onglets, deux fichiers de fenêtres, glossaire) ont été lus en entier ; leurs empreintes SHA-256 sont conformes au manifeste. L’audit propose **102 remplacements locaux** (`propositions.json`), tous à ancre unique vérifiée mécaniquement, sans changement de chiffre, de dose, de seuil ni de source, et **21 renvois médicaux** là où une reformulation risquait de toucher le sens. Quatre observations globales (typographie, HTML, phrases nominales, terminologie) complètent le dispositif.

La leçon est bien écrite dans l’ensemble : phrases courtes, annonces claires, tableaux introduits. Les défauts relevés tiennent surtout à des phrases sans verbe dans les cellules, les encadrés et les fenêtres, à quelques contresens de formulation et à des unités ou abréviations non homogènes.

## Constats les plus graves

- **Cas récapitulatif sans verbe principal** (`E12_b`, section 11) : la première phrase est une suite de huit groupes nominaux. Proposition E12-LANG-b-22.
- **Contresens apparent en biochimie** (`E12_c`) : « Le mécanisme de la cétose s’explique par la sécrétion résiduelle » alors que la sécrétion résiduelle explique l’absence de cétose. Proposition E12-LANG-c-19.
- **Renvoi inexact et verbe impropre** (`E12_a`) : « Le tableau suivant sépare les deux formes » (ce sont deux encadrés) ; « L’absence de douleur ne retire pas la FCPD » (on exclut un diagnostic, on ne le retire pas) ; « La FCPD donne une acidocétose remarquablement inhabituelle » (se lit comme une cause).
- **Calque « discrets »** (`E12_c`, `E12_pop2`) : « gros calculs intracanalaires discrets » contredit « gros » en français ; « distincts » est proposé.
- **Incohérences internes à trancher par l’audit médical** : mnémotechnique SANS présentée comme l’ordre de la démarche (RM-06) ; « pancréas normal » classé tantôt « fréquent », tantôt « occasionnel » (RM-07) ; Vellore décrite comme « étude indienne » alors qu’elle inclut la Corée et la Thaïlande (RM-15).

## Tableau de bord

| Fichier | Propositions | Renvois médicaux |
|---|---:|---:|
| E12_a (Pathologie) | 26 | 6 |
| E12_b (Examens, partie 1) | 24 | 9 |
| E12_c (Examens et Sciences) | 21 | 3 |
| E12_d (Pharmacologie) | 10 | 0 |
| E12_pop1 (fenêtres, 1re partie) | 14 | 1 |
| E12_pop2 (fenêtres, 2e partie) | 7 | 1 |
| glossaire e12.py | 0 | 1 |
| **Total** | **102** | **21** |

| Catégorie | Nombre |
|---|---:|
| phrase nominale | 21 |
| syntaxe | 10 |
| grammaire | 9 |
| répétition | 9 |
| ambiguïté | 9 |
| unités | 8 |
| lexique | 6 |
| lourdeur | 4 |
| typographie | 3 |
| orthographe | 3 |
| anglicisme | 3 |
| cohérence | 3 |
| méta-discours | 2 |
| registre | 2 |
| ponctuation | 2 |
| cohérence terminologique | 2 |
| calque | 2 |
| abréviation | 2 |
| précision | 1 |
| contresens | 1 |

## Contrôles mécaniques

- Empreintes SHA-256 des 7 fichiers : conformes au manifeste.
- Unicité : 102 sur 102 `ancien` apparaissent exactement une fois dans leur fichier (`verification_unicite.py`, exécutable depuis la racine du worktree).
- Application séquentielle simulée : aucun chevauchement ; les nombres du texte visible sont identiques avant et après ; les balises sont inchangées, sauf l’ordre de deux boutons dans la proposition E12-LANG-a-02.
- Abréviations : toutes les abréviations de la leçon ont une clé de glossaire (dans e12.py ou dans un glossaire voisin), sauf « Ph. Eur. » (développée dans le texte par E12-LANG-d-03 et E12-LANG-pop2-07).

## Renvois médicaux (aucune reformulation proposée)

**RM-01** — `E12_a.html` — abréviation / précision. Ancre : « les anticorps anti-GAD sont négatifs ». La vignette écrit « anti-GAD » alors que tout le reste de la leçon et la clé de glossaire utilisent « anti-GAD65 ». « anti-GAD » seul n’a pas de clé de glossaire. Corriger en « anti-GAD65 » précise l’isoforme testée : c’est une précision d’examen, donc à décider par l’audit médical.

**RM-02** — `E12_a.html` — ambiguïté de référent. Ancre : « la proportion parmi les diabétiques varie de 6 à 21 % ». « La proportion » ne dit pas de quoi (cas de diabète de malnutrition ? FCPD ?). Le texte source n’ayant pas été relu pour cet audit linguistique, le référent n’est pas reformulé.

**RM-03** — `E12_a.html` — assertion non sourcée. Ancre : « en Suisse, l’entité se rencontrerait d’abord comme diagnostic d’exclusion ». La phrase précédente déclare une lacune et affirme ne pas extrapoler ; la suite énonce pourtant, au conditionnel, une prédiction sur la Suisse sans source. Contradiction interne à trancher sur le fond (supprimer, ou sourcer).

**RM-04** — `E12_a.html` — explication absente. Ancre : « Pourquoi les besoins en insuline paraissaient élevés. ». L’intertitre promet une explication ; le paragraphe indique seulement que l’impression venait d’observations anciennes et que les études récentes la contredisent. Le « pourquoi » (mécanisme causal) manque : enrichissement médical à demander à l’audit médical.

**RM-05** — `E12_b.html` — libellé de critère elliptique. Ancre : « (1) un pays tropical ». Le critère (1) de la FCPD est écrit « un pays tropical » : on ne sait pas s’il s’agit de la résidence, de l’origine ou de la survenue. Le libellé exact d’Endotext doit être vérifié avant toute reformulation.

**RM-06** — `E12_b.html` — incohérence interne. Ancre : « moyen mnémotechnique SANS, aide pédagogique ». L’encadré « À retenir » présente SANS comme moyen de retenir l’ordre de la démarche (glycémie, anticorps et C-peptide, imagerie, contexte nutritionnel), alors que SANS (Sécrétion, Anticorps, Non-cétosique, Sensibilité) décrit le profil et non cet ordre. Le lien affirmé est faux ou à reformuler ; l’intention pédagogique relève du fond.

**RM-07** — `E12_b.html` — incohérence interne. Ancre : « pancréas normal en imagerie pour écarter la FCPD ». Dans l’alerte « Critères formels », « pancréas normal en imagerie » figure parmi les caractéristiques « fréquentes » ; dans la démarche diagnostique (section 7) et la fenêtre e12-type5, il est classé parmi les « occasionnelles ». Une des deux listes doit être corrigée d’après le consensus.

**RM-08** — `E12_b.html` — ambiguïté de portée. Ancre : « il n’existe pas non plus d’essai thérapeutique fondé sur les preuves (grade 1C) ». Un grade de recommandation (1C) est attaché à l’absence d’essai ; il s’agit probablement du niveau de recommandation de HaPanEU, non d’un grade de l’absence d’essai. À vérifier dans la source avant reformulation.

**RM-09** — `E12_b.html` — parenthèse elliptique. Ancre : « des vitamines liposolubles et la vitamine D (ostéodystrophie) ». La parenthèse « (ostéodystrophie) » ne dit pas si la vitamine D la prévient ou la traite. Choisir le verbe suppose de relire Endotext.

**RM-10** — `E12_b.html` — énumération ambiguë. Ancre : « rénales, oculaires, neurologiques, vasculaires périphériques, multiples, avec le pied diabétique ». On ne sait pas si le pied diabétique est une sous-rubrique à part ou un cas des complications multiples (« avec »). La structure de la rubrique CIM-10-GM doit être relue avant de choisir « et » ou « ainsi que ».

**RM-11** — `E12_b.html` — ambiguïté terminologique. Ancre : « atteinte rénale précoce de type 1 ». « De type 1 » peut se lire comme « de type diabète de type 1 » ou comme un type de lésion rénale. La même phrase indique « une atteinte macrovasculaire généralement non associée » (à quoi ?). Les deux points demandent la source HaPanEU.

**RM-12** — `E12_b.html` — référent manquant. Ancre : « le risque de décès est disproportionné, surtout chez la femme ». « Disproportionné » par rapport à quoi (le risque de cancer, la taille de la tumeur, la population générale) ? Le texte ne le dit pas ; la précision relève de la source (Endotext).

**RM-13** — `E12_b.html` — confusion classification / soins. Ancre : « la prise en charge relève de la rubrique obstétricale ». Une rubrique est un code de classification ; elle ne régit pas la prise en charge. La phrase confond codage (O24.-) et conduite. Reformuler en « se code sous O24.- » changerait l’énoncé, donc proposition réservée.

**RM-14** — `E12_c.html` — affirmation contredite par le contexte. Ancre : « Cette histologie fonde deux phénotypes différents ». Le paragraphe précédent dit que les données histologiques sont indirectes, et la dernière phrase que l’on n’a aucune biopsie humaine du « type 5 ». Écrire que cette histologie « fonde » deux phénotypes est donc excessif ; le verbe (suggère ? est compatible avec ?) dépend de la force de la source.

**RM-15** — `E12_pop1.html` — incohérence interne. Ancre : « Petit effectif, hommes seulement, pas de suivi, étude indienne. ». La fenêtre qualifie Vellore d’« étude indienne » alors que l’onglet 1 (section 2) dit que la Corée et la Thaïlande s’ajoutent dans l’étude de Vellore. Une des deux informations est inexacte ou à nuancer.

**RM-16** — `e12.py` — définition de glossaire hors sujet. Ancre : « La metformine est contre-indiquée en dessous de 30 mL/min et limitée à 1 000 mg par jour entre 30 et 59 mL/min. ». La définition de la clé DFGe ne définit pas le DFGe : elle énonce une règle posologique. Une définition correcte (« mesure estimée de la filtration rénale par le rein… ») introduirait un énoncé nouveau, que le protocole interdit d’ajouter dans un audit linguistique.

**RM-17** — `E12_pop2.html` — rubrique inadaptée. Ancre : « Jusqu’à 25 % de diabètes instables. ». Cette donnée figure sous « Facteurs aggravants » alors qu’elle décrit une fréquence, non un facteur. Un déplacement dans une autre rubrique est un choix de structure à valider.

**RM-18** — `E12_c.html` — force du verbe. Ancre : « Les sources européennes exigent de confirmer par la glycémie à jeun. ». « Exigent » dit plus qu’une recommandation graduée. Le verbe exact dépend de la formulation de HaPanEU, non lue ici.

**RM-19** — `E12_c.html` — enrichissement médical. Ancre : « aucun facteur de conversion n’est fourni par les sources lues ». La leçon compare des ng/mL (Vellore) et des pmol/L (SGED) en disant qu’aucun facteur de conversion n’est fourni. Un facteur de conversion existe dans la littérature biochimique ; l’ajouter revient à ajouter un fait sourcé, donc à confier à l’audit médical (rubrique ENRICHISSEMENT).

**RM-20** — `E12_a.html` — attribution ambiguë. Ancre : « La version allemande modifiée (CIM-10-GM 2024) de l’Office fédéral de la statistique reprend le libellé ». « La version allemande modifiée … de l’Office fédéral de la statistique » : la CIM-10-GM est publiée en Allemagne ; l’OFS la reprend pour la Suisse. L’attribution précise relève des sources.

**RM-21** — `E12_a.html` — figure. Ancre : « Figure 1 — Production hépatique de glucose et captation périphérique ». Les hauteurs de barres de la figure 1 ne sont pas proportionnelles aux valeurs (0,50/0,84 → 57/84 px ; 10,1/4,2 → 140/47 px) et les deux paires n’ont pas d’échelle commune. La légende annonce « schéma non calibré » ; une échelle ou un axe gradué relève d’une correction de figure, non de formulation.

## Observations globales

**OG-01** — typographie — espaces insécables (tous les fichiers). Aucun espace insécable (U+00A0 ou U+202F) n’est employé : chaque « ; », « : », « ? », « ! » est précédé d’une espace simple et les guillemets « » sont suivis/précédés d’une espace simple (E12_a : 54 signes ponctués, 34 guillemets ; E12_b : 101, 42 ; E12_c : 70, 46 ; E12_d : 39, 10 ; E12_pop1 : 52, 26 ; E12_pop2 : 59, 12 ; glossaire : 4, 1). Le même constat est vrai de E10, E11, I63 et N17 (0 espace insécable) : il s’agit d’une convention de la chaîne de production, non d’un défaut propre à E12. Non traité ligne à ligne ; une correction mécanique globale (remplacement par U+202F avant ; ? ! et U+00A0 après « / avant ») relève d’une mission d’intégration sur fichier partagé.

**OG-02** — HTML — signe < non échappé (E12_b (7), E12_c (1), E12_d (2), E12_pop1 (9), E12_pop2 (2)). Le signe « < » apparaît brut dans le texte (« IMC < 18,5 kg/m² », « DFGe < 30 mL/min »). Le navigateur le tolère parce qu’il est suivi d’une espace, mais l’entité &lt; serait plus sûre. Non traité (21 occurrences, aucune erreur de rendu constatée sans test navigateur).

**OG-03** — phrases nominales dans les fenêtres et les Pareto (E12_pop1 (Pareto et fenêtres), E12_pop2). Les puces de Pareto et de nombreux paragraphes de fenêtres sont des énumérations de groupes nominaux (« Pancréas normal en imagerie : « type 5 ». Calculs intracanalaires : FCPD. »). STYLE_REDACTION § 2 les proscrit, mais l’espace disponible dans les Pareto est volontairement réduit. Seuls les cas où la phrase est ambiguë ou sans verbe sur plusieurs lignes ont été proposés ; les autres sont laissés à l’arbitrage éditorial.

**OG-04** — cohérence terminologique (tous les fichiers). « CT » et « scanner » coexistent (deux occurrences de « scanner » dans E12_b, traitées par les propositions E12-LANG-b-22 et b-23) ; « déviations standard » est conservé (usage helvétique). « Vigilance oncologique » et « surveillance du cancer » alternent : non modifié, les deux termes étant compréhensibles.

## Propositions par fichier

Le détail complet (ancien, nouveau, motif) est dans `propositions.json`. Le tableau ci-dessous en donne l’inventaire.

### E12_a (Pathologie)

| Id | Catégorie | Motif |
|---|---|---|
| a-01 | précision | Le déterminant possessif lève l’ambiguïté sur la grossesse concernée. |
| a-02 | méta-discours | L’annonce décrit le cours (« Ce cours décrit… Il expose… ») au lieu d’exposer le problème médical, ce que proscrit STYLE_REDACTION § 3. La reformulation énonce directement le contenu, sans rien ajouter ni retirer. |
| a-03 | lourdeur | « version 10 de l’OMS » est une tournure elliptique ; le participe rend la relation explicite. |
| a-04 | méta-discours | Le discours sur le cours lui-même est remplacé par une tournure impersonnelle centrée sur la notion. |
| a-05 | grammaire | Articles omis dans une coordination : registre télégraphique, contraire à la phrase complète exigée par le guide. |
| a-06 | syntaxe | « diabètes de la maladie » est incorrect (article défini singulier, relation non exprimée). |
| a-07 | registre | « dériver de » évoque un écart ; « découler de » exprime la déduction voulue. |
| a-08 | typographie | Unité d’insuline notée tantôt UI, tantôt U dans la même phrase, et abréviation « /j » non conforme ; harmonisation sans changer les valeurs. |
| a-09 | unités | Symbole du litre en majuscule (dL) ; même unité, graphie SI correcte. |
| a-10 | syntaxe | Syntaxe fautive : les patients ne « possèdent » pas un rapport hommes/femmes. Unité répétée pour la seconde valeur. Les chiffres sont inchangés. |
| a-11 | répétition | Redondance « FCPD / la maladie » et métonymie « touche l’Inde du Sud ». |
| a-12 | syntaxe | Une pancréatite n’a pas d’IMC : le complément se rapporte aux patients, ce que la tournure rend explicite. |
| a-13 | grammaire | « ni » employé sans corrélatif ; la structure ni… ni… est rétablie. |
| a-14 | ambiguïté | « couple » est ambigu (foie et muscle ? insuline et glucose ?) ; « double action » reprend exactement les deux effets décrits. |
| a-15 | grammaire | « avant » employé sans complément ; « auparavant » est l’adverbe correct. |
| a-16 | orthographe | Orthographe usuelle : « postprandial » sans trait d’union. |
| a-17 | anglicisme | Anglicisme mis entre guillemets (« sous-performer ») remplacé par une formulation française. |
| a-18 | grammaire | Articles omis dans une énumération de compléments : phrase complète exigée. |
| a-19 | orthographe | Orthographe : « prédiabétique » sans trait d’union. |
| a-20 | ponctuation | Énumération sans articles ni ponctuation : trois exemples distincts sont séparés pour qu’on ne rattache pas « avec moins d’îlots » aux rongeurs. |
| a-21 | syntaxe | On n’« exclut » pas des antécédents : on écarte leur existence ; la construction est rétablie. |
| a-22 | cohérence | Il n’y a pas de tableau mais deux encadrés (div.two/card) : renvoi inexact. |
| a-23 | phrase nominale | Phrase nominale proscrite par STYLE_REDACTION § 2. |
| a-24 | phrase nominale | Phrase nominale sans verbe ; préposition « en » omise devant « décubitus ventral ». |
| a-25 | lexique | Verbe impropre : on exclut un diagnostic, on ne le « retire » pas. |
| a-26 | lourdeur | La formule « calibré à l’échelle d’un patient » est obscure. |

### E12_b (Examens, partie 1)

| Id | Catégorie | Motif |
|---|---|---|
| b-01 | syntaxe | Ce sont les examens qui mesurent, non la masse qui « se mesure basse » ; sujet et verbe rétablis, contenu identique. |
| b-02 | phrase nominale | Phrase nominale proscrite par STYLE_REDACTION § 2. |
| b-03 | phrase nominale | Phrase nominale ; antécédent de « qui » rendu non ambigu. |
| b-04 | unités | Symbole du litre en majuscule (dL). |
| b-05 | unités | Symbole du litre en majuscule (dL). |
| b-06 | ambiguïté | Adjectif substantivé sans antécédent : le nom « caractéristiques » est rétabli. |
| b-07 | ambiguïté | Même cas que ci-dessus. |
| b-08 | lourdeur | Répétition du verbe « avoir » (« pouvoir avoir ») : lourdeur. |
| b-09 | syntaxe | Corrélation « sans… ni », registre (« regardé » → « examiné ») et ordre « diagnostic validé de la classification » (la formulation initiale se lisait « diagnostic de la classification validé »). |
| b-10 | phrase nominale | Phrase nominale : le verbe est rétabli. |
| b-11 | ambiguïté | « donne une acidocétose » se lit comme une cause de la complication alors que la phrase dit son extrême rareté. |
| b-12 | lourdeur | « non-perception » n’a pas de complément ; la tournure verbale explicite l’objet. |
| b-13 | cohérence terminologique | La lentille est une légumineuse : l’énumération la présentait comme une catégorie distincte. |
| b-14 | lexique | Le coût n’est pas un « risque » au même titre que l’hypoglycémie ; préposition manquante. |
| b-15 | syntaxe | « chez IMC » est incorrect ; unité manquante. |
| b-16 | ponctuation | Virgule après « que » devant un complément circonstanciel détaché. |
| b-17 | phrase nominale | Formule télégraphique (« insuline oui si ») remplacée par une phrase complète. |
| b-18 | syntaxe | « à éviter » dépendait d’un sujet absent : la connexion « mais reste » est rétablie. |
| b-19 | lexique | « vivent » est ambigu (durée de vie ou simple existence) ; « survivent » exprime la survie voulue. |
| b-20 | répétition | Redondance « annuel… par an ». |
| b-21 | phrase nominale | Liste de mots-clés remplacée par une phrase complète (STYLE_REDACTION § 2). Le contenu des mesures reste identique. |
| b-22 | phrase nominale | Premier énoncé sans verbe conjugué (phrase nominale de huit propositions) ; virgules ajoutées autour de l’inciso. « scanner » est remplacé par « CT », terme utilisé partout ailleurs dans la leçon et défini au glossaire. |
| b-23 | cohérence terminologique | Cohérence terminologique avec « CT » (clé du glossaire) utilisée dans les autres onglets. |
| b-24 | typographie | Ordinal en toutes lettres comme dans le corps du texte (« troisième décennie »). |

### E12_c (Examens et Sciences)

| Id | Catégorie | Motif |
|---|---|---|
| c-01 | répétition | Paraphrase des en-têtes du tableau, déconseillée par STYLE_REDACTION § 4 ; la définition des statuts, seule utile, est conservée. |
| c-02 | anglicisme | Anglicisme remplacé par le terme français, l’anglais étant conservé entre guillemets pour l’examen. |
| c-03 | cohérence | La colonne « Question » contient des questions ; cette cellule était un simple groupe nominal. |
| c-04 | lexique | On ne « demande » pas une composition corporelle, on demande sa mesure. |
| c-05 | unités | Symbole du litre en majuscule (dL). |
| c-06 | unités | Symbole du litre en majuscule (dL). |
| c-07 | unités | Symbole du litre en majuscule (dL). |
| c-08 | répétition | « En cas de doute » figure deux fois à une phrase d’intervalle ; « supérieure au seuil » est inexact pour un seuil défini par ≥ 11,1 mmol/L. |
| c-09 | grammaire | « avant » employé sans complément ; « auparavant » est l’adverbe correct. |
| c-10 | syntaxe | « demande les anticorps / la fonction exocrine » : les objets sont des examens, non des choses que l’on demande ; l’action est explicitée. |
| c-11 | cohérence | Aucune case n’est vide : elles contiennent « — ». La formulation initiale décrit mal le tableau. |
| c-12 | ambiguïté | Citation isolée dans une cellule : le sujet de l’adjectif n’était pas nommé. |
| c-13 | répétition | Redondance « À retenir… le profil à retenir ». |
| c-14 | répétition | Répétition « diagnostic… diagnostic ». |
| c-15 | grammaire | Articles omis dans l’énumération. |
| c-16 | calque | « est de gros calculs » est syntaxiquement incorrect ; « discrets » signifie en français « peu visibles », donc contredit « gros » ; l’adjectif attendu est « distincts » (calque de l’anglais discrete). |
| c-17 | répétition | Répétition « réduite… réduit » à quatre mots d’intervalle. |
| c-18 | ambiguïté | « ménager l’insuline » est ambigu (épargner la sécrétion endogène ou limiter la dose exogène ?) ; le contexte thérapeutique impose le second sens. |
| c-19 | contresens | Contresens apparent : la sécrétion résiduelle explique l’absence de cétose, non la cétose. |
| c-20 | registre | « en médiane » est elliptique. |
| c-21 | lexique | La génétique n’est pas un diagnostic ; c’est un outil. |

### E12_d (Pharmacologie)

| Id | Catégorie | Motif |
|---|---|---|
| d-01 | syntaxe | « le moins hypoglycémiant » n’a pas de nom ; l’infinitif « de » est répété pour le parallélisme. |
| d-02 | grammaire | Préposition manquante. |
| d-03 | abréviation | Abréviation « Ph. Eur. » sans clé de glossaire : développée dans le texte. |
| d-04 | typographie | Signe « + » employé comme verbe dans une phrase de tableau. |
| d-05 | ambiguïté | « moitié » sans complément ambigu ; le complément est explicité. |
| d-06 | phrase nominale | Phrase nominale proscrite par STYLE_REDACTION § 2. |
| d-07 | phrase nominale | Phrase nominale proscrite par STYLE_REDACTION § 2. |
| d-08 | phrase nominale | Phrase nominale proscrite par STYLE_REDACTION § 2. |
| d-09 | phrase nominale | Construction nominale remplacée par une phrase à sujet explicite. |
| d-10 | phrase nominale | Phrase nominale ; « l’insulinodéficient » substantivé sans nom. |

### E12_pop1 (fenêtres, 1re partie)

| Id | Catégorie | Motif |
|---|---|---|
| pop1-01 | anglicisme | Anglicisme remplacé ; cohérence avec la modification de l’onglet Examens. |
| pop1-02 | ambiguïté | Le participe « reconnu » pouvait se rapporter au consensus ou au terme ; la phrase est scindée pour lever l’ambiguïté, en cohérence avec la chronologie de l’onglet 1 et l’entrée de glossaire IDF. |
| pop1-03 | grammaire | Articles omis dans une coordination. |
| pop1-04 | phrase nominale | Infinitif injonctif et énumération de mots-clés proscrits par STYLE_REDACTION § 2. |
| pop1-05 | orthographe | Orthographe usuelle : « postprandial ». |
| pop1-06 | grammaire | « avant » employé sans complément. |
| pop1-07 | phrase nominale | Mot isolé tenant lieu de phrase. |
| pop1-08 | phrase nominale | Définition sans verbe ; article partitif devant « jeunes adultes » ; orthographe « prédiabétique ». |
| pop1-09 | phrase nominale | Succession de groupes nominaux ; le point de départ des « 10 à 20 ans », imprécis, est celui indiqué dans le corps du cours (début des douleurs). |
| pop1-10 | phrase nominale | Phrase nominale. |
| pop1-11 | phrase nominale | Définition sans verbe. |
| pop1-12 | phrase nominale | Infinitif injonctif proscrit par STYLE_REDACTION § 2. |
| pop1-13 | unités | Symbole du litre en majuscule (dL). |
| pop1-14 | unités | Symbole du litre en majuscule (dL). |

### E12_pop2 (fenêtres, 2e partie)

| Id | Catégorie | Motif |
|---|---|---|
| pop2-01 | calque | « discrets » contredit « gros » en français ; calque de l’anglais discrete. |
| pop2-02 | lexique | Verbe et articles : on distingue une entité d’une autre. |
| pop2-03 | phrase nominale | Infinitif injonctif proscrit par STYLE_REDACTION § 2. |
| pop2-04 | ambiguïté | « Le moyen » est sans antécédent immédiat. |
| pop2-05 | répétition | Répétition « suisse… Suisse » et ponctuation en cascade. |
| pop2-06 | répétition | Répétition « suisse… Suisse ». |
| pop2-07 | abréviation | Abréviation « Ph. Eur. » développée ; « collation moitié » sans ponctuation ni complément. |

## Lacunes

- Aucune source médicale n’a été relue : un audit linguistique ne vérifie pas les faits. Les citations (Lancet Global Health 2025, Diabetes Care 2022, Endotext 2024, HaPanEU 2017, RMS 2022, SGED 2023, informations professionnelles Creon, Glucophage, Lantus) ne sont ni confirmées ni infirmées ici.
- Les formulations qui touchent à un sens médical possible sont renvoyées (21 renvois) et non reformulées.
- Aucun test en navigateur : l’effet des propositions sur l’affichage (largeur des tableaux, justification) n’a pas été mesuré.
- Le glossaire n’a fait l’objet d’aucune proposition : une seule anomalie (DFGe, E12-LANG-RM-16) a été renvoyée.
- Les espaces insécables n’ont pas été traités fichier par fichier (convention de la chaîne de production, voir E12-LANG-OG-01).
- Pas d’audit de l’orthographe par un correcteur externe (Antidote, LanguageTool) : la relecture a été faite par lecture intégrale, avec des contrôles mécaniques sur la ponctuation, les unités et les abréviations.

*Audit IA — revue distincte d'une validation médicale humaine ; aucune source canonique modifiée*
