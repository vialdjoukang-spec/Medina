# Audit linguistique agressif — G45 Accidents ischémiques cérébraux transitoires et syndromes apparentés

Mission ALPHA1-CLAUDE-G45-LANG · tour 1 · génération 1 · branche `claude/alpha1/g45-lang-g1` · base `f664dd9e8da71f647dd3dc4da18f509f8517959c` · 15 octobre 2026.

*Audit IA — revue distincte d'une validation médicale humaine ; aucune source canonique modifiée.*

## 1. Périmètre et méthode

Les sept fichiers de la leçon ont été lus en entier : quatre onglets (`G45_a` à `G45_d`), deux fichiers de fenêtres (`G45_pop1`, `G45_pop2`) et le glossaire `glossary/g45.py`. Leurs empreintes SHA-256 ont été recalculées avant toute analyse et comparées au manifeste : **7 sur 7 conformes**. Le manifeste fige le snapshot `bfc4576b` ; le worktree est sur `f664dd9e` ; `git diff` entre les deux est vide pour ces fichiers.

L'audit porte sur la langue, jamais sur le fond : orthographe, grammaire, accords, ponctuation, typographie française, nombres, lourdeurs, ambiguïtés, registre, cohérence terminologique, sigles sans clé de glossaire. Aucun chiffre, aucune dose, aucune source n'est ajouté, retiré ou modifié. Lorsqu'une reformulation exigerait de trancher un point médical, la proposition est remplacée par un **renvoi** (section 5).

## 2. Résultat en chiffres

| Indicateur | Valeur |
|---|---|
| Propositions locales (`propositions.json`) | **96**, toutes `fond_inchange: true` |
| Renvois médicaux | **9** |
| Observations de structure (sans proposition) | 5 |
| Règles systémiques (typographie, nombres, terminologie, sigles) | 5 |
| Unicité de chaque `ancien` dans son fichier | 96 sur 96 (script `verifier_propositions.py`) |
| Chevauchements entre propositions | 0 |
| Suite des balises HTML après application simulée | identique |
| Glossaire modifié | compile |

Répartition par fichier : G45_b 32 · G45_c 19 · G45_pop2 16 · G45_pop1 11 · G45_a 10 · G45_d 5 · glossaire 3.
Répartition par catégorie : terminologie 17 · grammaire 17 · registre 15 · ambiguïté 13 · lexique 8 · nombres 5 · orthographe 4 · ordre des mots 3 · accord 3 · lourdeur 3 · annonce méta 2 · typographie 2 · connecteur, phrase nominale, clarté de calcul, abréviation 1 chacune.

## 3. Le constat le plus lourd : une typographie française absente

Aucun des six fichiers HTML ne contient une seule espace insécable (U+00A0, U+202F, `&nbsp;`). Aucune passe automatique n'en insère à la construction : la recherche dans `shell/`, `build_*.py` et `tools/*.py` ne donne rien. Dans le texte visible, on dénombre :

| Élément | Occurrences (espace simple sécable) |
|---|---|
| Espace avant « ; » | 1 101 |
| Espace avant « : » | 330 |
| Espace avant « ? » | 28 |
| Guillemets « … » | 31 paires |
| Nombre + « % » | 43 |
| Nombre + unité (mmHg, mL, mg, µmol/L, U/L, kg, °C, g) | 134 |
| Séparateur de milliers (100 000, 4 731, 19 185, 18 201, 1 000, 1 200) | 7 |
| Heures « 09 h 10 » | 18 |

Une coupure de ligne peut donc séparer « 152/86 » de « mmHg », ou « 10,3 » de « % ». La recette de normalisation (expressions régulières, nœuds de texte uniquement, hors balises, URL et attributs) figure dans `regles_systemiques.json`. Elle est destinée au moteur de construction, non à 1 500 retouches manuelles ; elle n'est pas appliquée ici, car le moteur est un fichier partagé.

Second défaut systémique : les **apostrophes** sont mêlées (628 droites contre 654 courbes). Le corps des onglets 1 à 4 emploie la forme droite, les titres, boutons et fenêtres la forme courbe ; `G45_pop2` est entièrement courbe.

## 4. Les corrections locales les plus utiles

Les propositions complètes, avec motif, sont dans `propositions.json`. Les familles principales :

- **Calcul affiché de façon fausse.** La section 3.5 de l'onglet 1 écrit « 10,32 − 2,14 ≈ 8,19 » ; or 10,32 − 2,14 = 8,18. La fenêtre `g45-risque` explique déjà l'écart (arrondi intermédiaire : 0,103226 − 0,021352 = 0,081874). La proposition LANG-G45-005 met le texte en accord avec la fenêtre, sans donnée nouvelle.
- **Terminologie flottante.** « Fibrillation atriale » (9 occurrences) et « fibrillation auriculaire » (12, dont le libellé d'indication des FI suisses) coexistent ; « Stroke Unit » côtoie « unité AVC » ; « embol » côtoie « embole » ; « vertébrobasilaire » côtoie « vertébro-basilaire » ; le cholestérol des lipoprotéines de basse densité est écrit de trois façons. Chaque famille est unifiée.
- **Métonymies et collocations fautives.** « Citée par l'Europe », « l'Europe ne démontre pas » (trois occurrences), « le réseau bernois recherche », « le protocole n'administre », « n'empêche pas une lésion » (pour « n'exclut pas »), « la traçabilité du témoin », « renommés valeurs normales ».
- **Grammaire.** Articles omis dans les énumérations (« symptômes, territoire proposé, chronologie »), « il n'existe pas un examen » pour « d'examen », « aucun … ni » mal coordonné, pronom « elle » ambigu dans une option de quiz (la fièvre ou l'endocardite ?), « Elle constitue un modèle » dont le sujet réel est la relation débit = pression ÷ résistance.
- **Formules de chantier proscrites par le guide.** « Cette lacune est conservée », « inventé » (quatre occurrences), « escalade antithrombotique irréfléchie ».
- **Sigles sans clé de glossaire.** ISRS et CHUV (règle n°3 de `CLAUDE.md`) : deux clés proposées avec développement littéral officiel et aucun fait médical.

## 5. Renvois médicaux (aucune reformulation proposée)

| Renvoi | Fichier | Point |
|---|---|---|
| 01 | G45_a | « L'absence de lésion visible renforce un raisonnement » : l'objet du verbe n'est pas nommé. |
| 02 | G45_b | « plus de trois à cinq par an » : seuil de lecture ambiguë (amnésie épileptique). |
| 03 | G45_b | « au-dessous de 140/100 mmHg » : diastolique inhabituelle, répétée dans la fenêtre `g45-carotide`. |
| 04 | G45_b | Le texte dit que l'athérosclérose intracrânienne « exclut » les autres permis ; le tableau dit « Déconseillée ». |
| 05 | G45_b | « la réduction dépend de critères combinés précis » : réduction de quoi ? |
| 06 | G45_d, G45_pop2 | « 7 jours après la dernière dose » / « sa dernière dose » : antécédent ambigu (statine ou acide fusidique), le possessif « sa » s'accordant grammaticalement avec « la statine ». |
| 07 | G45_pop2 | « moins d'événements hémorragiques » dans le critère composite ARISTOTLE. |
| 08 | glossaire | Traduction littérale de LPGH (« dernière preuve de bon état »). |
| 09 | G45_pop1 | « risque compris entre 8 % et 49 % » : les bornes 0,08–0,49 sont celles d'un rapport de risques instantanés. |

## 6. Observations de structure

L'épilogue local s'intitule « Corrélation clinique. » (21 occurrences) alors que le guide prescrit « À retenir. ». Le paragraphe 3.6 de l'onglet 2 décrit ses propres quiz (annonce méta). La section 4.6 de l'onglet 1 annonce trois vignettes et en présente deux. Une carte de l'onglet 1 (section 8) répète presque mot pour mot la section 8.4. « Mécanistique » est un anglicisme (4 occurrences). Ces points relèvent de l'intégrateur.

## 7. Lacunes

- Aucune source médicale (réseau AVC bernois, ESO 2021, recommandation allemande/autrichienne/suisse, FI Swissmedic) n'a été relue ; les renvois en dépendent.
- Aucun build ni rendu navigateur n'a été exécuté : l'effet des espaces insécables sur la justification et la résolution des deux nouvelles clés de glossaire ne sont pas testés.
- Recherche d'une passe typographique limitée à `shell/`, `build_*.py`, `tools/*.py`.
- Les neuf figures n'ont pas été lues, seulement leurs textes alternatifs et légendes.
- Les ratios Pareto, calculés par le moteur, ne sont pas rendus.

## 8. Tableau de bord final

| Mesure | Valeur |
|---|---|
| Fichiers lus / empreintes conformes | 7 / 7 |
| Propositions locales | 96 |
| Renvois médicaux | 9 |
| Règles systémiques | 5 |
| Sources modifiées | 0 |
| Livrables | `rapport.json`, `rapport.md`, `propositions.json`, `regles_systemiques.json`, `verifier_propositions.py` |
