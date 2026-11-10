# Audit linguistique G92 — Encéphalopathie toxique (S08)

Mission ALPHA1-CLAUDE-G92-LANG, tour 4, génération 1. Branche `claude/alpha1/g92-lang-g1`, base de la mission `523832d9` (worktree démarré sur `103745ba`, descendant ; sources figées identiques, empreintes conformes). Audit IA : revue distincte d'une validation médicale humaine ; aucune source canonique modifiée.

## Synthèse

Les sept fichiers de la leçon (quatre onglets, deux fenêtres, glossaire) ont été lus en entier ; leurs empreintes SHA-256 sont conformes au manifeste. Le texte est globalement correct, sourcé et sobre. Les défauts relevés tiennent à trois familles : des phrases nominales ou à l'infinitif injonctif en texte courant, dans les alertes et dans les fenêtres, que le guide de rédaction proscrit ; des anglicismes (« gold standard », « désordres », « investigations », « résolutifs », « ont des preuves ») ; et des constructions fautives ou ambiguës (« jusqu'à 6 à 8 semaines », « ne conduit pas ni ne manipule », « grade 2 et 3 », « ammoniaque » pour l'ammoniac, « présentation de l'enfant par »).

- **104 propositions locales** (`propositions.json`), chacune avec un `ancien` unique dans son fichier, `fond_inchange: true`, sans chevauchement, à balises HTML et chiffres identiques ; application simulée en mémoire suivie de `build_medina.audit()` : aucune abréviation non couverte.
- **26 renvois médicaux** : formulations dont la correction créerait ou retirerait une causalité, une fréquence, une chronologie ou une portée que la source ne porte pas. Ils ne sont pas corrigés ici.
- **2 constats hors périmètre**, transmis à l'audit MED : absence du sous-onglet de sémiologie (MAJEUR, bloquant pour la clôture) et liens vers l'information professionnelle suisse invalides (MINEUR).
- **Choix différés, non appliqués** : espaces insécables globales, séparateur des milliers, style des nombres.

## Propositions par catégorie

| Catégorie | Nombre |
|---|---|
| syntaxe | 51 |
| registre | 16 |
| grammaire | 10 |
| terminologie | 7 |
| ambiguité | 7 |
| cohérence | 5 |
| typographie | 4 |
| ponctuation | 3 |
| répétition | 1 |

## Exemples de propositions

- **P-08** (registre, `G92_a.html`) : « aux désordres toxiques et métaboliques » → « aux troubles toxiques et métaboliques ». Anglicisme (« disorders ») ; le terme français est « troubles ».
- **P-25** (ambiguité, `G92_b.html`) : « pas d’amélioration d’un grade 3 ou 4 après trois jours de fortes doses » → « absence d’amélioration d’un ICANS de grade 3 ou 4 après trois jours de fortes doses ». Un grade ne s’améliore pas ; c’est l’ICANS classé à ce grade qui s’améliore ou non.
- **P-30** (syntaxe, `G92_b.html`) : « avec symptômes neurologiques, investiguer ; carnitine par voie intraveineuse et hémodialyse en cas de surdosage massif. » → « avec des symptômes neurologiques, une exploration complémentaire s’impose ; en cas de surdosage massif, on recourt à la carnitine par voie intraveineuse et à l’hémodialyse. ». Article manquant, anglicisme « investiguer » et segment nominal sans verbe ; la restriction au surdosage massif est conservée.
- **P-40** (typographie, `G92_b.html`) : « faisceau de synthèse = exposition à un neurotoxique + encéphalopathie aiguë ou subaiguë + exclusion d’autres causes + amélioration à l’arrêt » → « faisceau de synthèse : exposition à un neurotoxique, encéphalopathie aiguë ou subaiguë, exclusion d’autres causes et amélioration à l’arrêt ». Symboles « = » et « + » dans le texte courant ; la section 7 formule le même faisceau en énumération.
- **P-47** (grammaire, `G92_c.html`) : « C. Débuter la méthylprednisolone 1000 mg par jour. » → « C. Débuter la méthylprednisolone à 1000 mg par jour. ». Préposition manquante devant la posologie.
- **P-70** (syntaxe, `G92_d.html`) : « <td>Arrêter</td> » → « <td>Arrêt</td> ». Homogénéité de la colonne « Conduite » (formes nominales ailleurs).

La liste complète figure dans `propositions.json`.

## Renvois médicaux (hors correction linguistique)

Classés par type de risque pour le fond. Chaque renvoi cite l'extrait exact de la leçon.

- **R-01** (ambiguïté médicale, G92_a.html) : « Le médicament le plus récemment introduit ou dosé ». « Dosé » peut signifier « dont la dose vient d’être modifiée » ou « dont la concentration a été mesurée » ; les deux lectures conduisent à des conduites différentes. À trancher par l’audit médical avant toute reformulation.
- **R-02** (attribution des sources, G92_a.html) : « ainsi que le méthotrexate ». La phrase range le méthotrexate à la suite des encéphalopathies « décrites par l’information professionnelle suisse », alors que la source citée pour le méthotrexate est une revue de 2025 (section 4, références, et fenêtre g92-methotrexate : « Source : résumé d’une revue de 2025 »). Reformuler l’attribution revient à trancher un fait de sourcing.
- **R-03** (unité de la proportion, G92_a.html) : « Soixante-quinze pour cent surviennent dans les sept premiers jours ». Le nombre est écrit en toutes lettres (début de phrase) et son sujet implicite est ambigu : 75 % des effets neurologiques ou 75 % des patients. La reformulation « Dans 75 % des cas, ils surviennent… » ou « 75 % des patients… » fixerait l’unité statistique, ce qui relève de la source (information professionnelle de Yescarta).
- **R-04** (cohérence chiffrée, G92_a.html) : « Le délai moyen d’apparition est d’environ 5 jours après la perfusion. ». Cette phrase donne un délai moyen d’environ 5 jours ; la section 2 cite un délai médian de 6 jours pour Yescarta et le bloc « Paramètres clés » (section 12) un délai médian de 6 à 7 jours avec un début « vers le jour 5 ». Moyenne, médiane et début typique sont des grandeurs différentes : l’audit médical doit dire laquelle chaque source donne.
- **R-05** (raisonnement, G92_a.html) : « indiquent une élimination rénale ». La phrase déduit une élimination rénale de deux données : l’adaptation à la clairance de la créatinine (pertinente) et l’épuration par hémodialyse (68 % en trois heures), qui prouve que le produit est dialysable, non qu’il est éliminé par le rein. La phrase signale elle-même qu’il s’agit d’une déduction ; toute correction est un choix de fond.
- **R-06** (sémantique médicale (spécificité ou fréquence), G92_a.html) : « est très spécifique : elle a été observée chez 19 des 22 patients ». « Très spécifique » est appuyé par une fréquence observée (19 des 22 patients atteints de neurotoxicité sévère), c’est-à-dire une sensibilité parmi les cas sévères, non une spécificité. Le choix du mot dépend de la source primaire, que cet audit n’a pas lue. La fenêtre g92-ecriture et la synthèse Pareto reprennent « très spécifique ».
- **R-07** (généralisation, G92_a.html) : « Le point commun de nombreuses encéphalopathies médicamenteuses est la ». « Nombreuses » généralise à partir de deux agents (céfépime, ifosfamide) pour lesquels le tableau cite l’insuffisance rénale comme facteur de risque ; le valproate, le métronidazole et le méthotrexate n’ont pas le même facteur. Reformulation = changement de portée à décider par l’audit médical.
- **R-08** (chronologie / causalité, G92_a.html) : « L’inflammation cytokinique explique le calendrier de l’ICANS (début vers le jour 5, pic des cytokines aux jours 7 à 14) ». Le début de l’ICANS (jour 5) précède le pic des cytokines (jours 7 à 14) : le pic ne peut donc expliquer à lui seul le début. La même phrase de l’onglet Sciences (« Cette chronologie explique le calendrier clinique ») pose le même problème. Toute correction modifie le lien causal affirmé.
- **R-09** (intitulé / critère de classement, G92_b.html) : « Diagnostic différentiel</b>, du plus dangereux au moins urgent ». L’intitulé associe deux critères différents (dangerosité puis urgence) ; la liste suivante n’est classée explicitement selon aucun des deux. Choisir « du plus urgent au moins urgent » ou « du plus dangereux au moins dangereux », ou retirer la promesse de classement, est une décision de fond.
- **R-10** (sens de « corriger l’agent », G92_b.html) : « d’arrêter ou de corriger l’agent ». On corrige une dose, une exposition ou un trouble, non un agent. La reformulation (« adapter la dose », « supprimer l’exposition », « corriger l’accumulation ») dépend de l’agent considéré (antibiotique, chimiothérapie, toxique) et change la conduite énoncée.
- **R-11** (portée du pronom, G92_b.html) : « Ils imposent les soins intensifs, l’avis d’un neurologue et un traitement immédiat ». Le pronom « Ils » suit une phrase qui énumère des situations de grade 4 puis un score ICE de 0 à 2 (grade 3). On ne sait pas si les soins intensifs s’appliquent aux deux grades ou au seul grade 4 ; la table de la section 9.1 ne les mentionne qu’à partir du grade 3. Clarifier la portée est une décision de fond.
- **R-12** (portée de la durée, G92_b.html) : « pendant deux semaines au moins ou jusqu’à disparition des effets neurologiques ». La phrase ne dit pas si l’interdit de conduite dure « le plus long » des deux délais (deux semaines ou disparition des effets) ou « le premier atteint ». La formulation de l’information professionnelle de Yescarta, non relue ici, tranche ce point.
- **R-13** (rattachement de la négation, G92_b.html) : « persistent jusqu’au décès, sans lien avec le traitement ». « Sans lien avec le traitement » peut qualifier la persistance des effets ou le décès. Les deux lectures ont un sens médical et réglementaire différent ; la correction suppose de relire l’information professionnelle de Yescarta.
- **R-14** (données comparatives incomplètes, G92_b.html) : « n’a pas réduit l’ICANS (35 % contre 25 %, p = 0,464) ». Les deux proportions ne sont pas rattachées à leurs groupes (anakinra ou témoin) ; le lecteur ne sait pas lequel des deux groupes a présenté 35 % d’ICANS. Compléter l’énoncé ajoute un fait de la source primaire (Schmid et coll.). Même énoncé dans la fenêtre g92-anakinra.
- **R-15** (critère composite non défini, G92_b.html) : « a été associé à moins de complications composites (p = 0,039) ». « Complications composites » est un calque de « composite endpoint » ; le contenu du critère n’est pas défini dans le chapitre. La fenêtre g92-tocilizumab dit seulement « moins de complications ». La reformulation exige de lire la source primaire (Stolz et coll.).
- **R-16** (objet de la prévention, G92_b.html) : « Méthotrexate</b> : hydratation, acide folinique (leucovorine) et glucarpidase en prévention ou atténuation. ». La phrase ne précise pas ce que ces mesures préviennent ou atténuent (toxicité générale du méthotrexate ou seule neurotoxicité). La section 9.3 et la fenêtre g92-methotrexate (« Prévention ») ne tranchent pas. Une reformulation en phrase complète imposerait de choisir.
- **R-17** (cohérence interne, G92_b.html) : « Le diagnostic d’ICANS est d’exclusion. ». La section 7 dit « Le diagnostic d’ICANS est clinique » ; ce piège dit « d’exclusion » ; la synthèse Pareto « clinique et d’exclusion » et le bloc des critères (section 12) « diagnostic d’exclusion clinique ». Les deux qualificatifs ne sont pas exclusifs mais la hiérarchie entre eux n’est pas posée. À harmoniser par l’audit médical.
- **R-18** (cohérence chiffrée, G92_b.html) : « Début de l’ICANS vers le jour 5 (délai médian 6 à 7 jours), 75 % dans les 7 jours. ». Le délai médian donné ici (6 à 7 jours) diffère de celui de la section 2 (médian de 6 jours, extrêmes 1 à 133) et de la phrase « délai moyen … environ 5 jours ». À sourcer et harmoniser.
- **R-19** (fréquence / chronologie, G92_b.html) : « Les crises surviennent souvent après l’aphasie globale. ». « Souvent » et la succession « après l’aphasie globale » sont des affirmations de fréquence et de chronologie dont la source n’est pas indiquée dans la phrase. Même énoncé dans l’onglet Sciences (neurophysiologie) et, sous une forme plus forte, dans la synthèse Pareto (« L’aphasie précède les crises et l’œdème »).
- **R-20** (portée d’un examen négatif, G92_c.html) : « Sa PCR (HSV, CMV, EBV, HHV-6, VZV) exclut une infection. ». Une PCR négative pour cinq virus ne peut exclure « une infection » en général (bactérienne, fongique, autres virus, LEMP). Le glossaire (CMV : « dont la PCR … exclut une infection du système nerveux central ») reprend la même formule. La portée exacte relève de l’audit médical.
- **R-21** (chronologie / causalité, G92_c.html) : « Cette chronologie explique le calendrier clinique ». Même difficulté que dans l’onglet Pathologie (section 3.3, bloc de corrélation) : les symptômes débutent vers le jour 5, avant le pic des cytokines (jours 7 à 14), de sorte que le pic n’explique pas le début.
- **R-22** (généralisation, G92_pop2.html) : « L’aphasie précède les crises et l’œdème. ». La synthèse Pareto généralise en « précède » une relation que le texte principal exprime par « surviennent souvent après l’aphasie globale ». Retirer « souvent » changerait la portée ; à décider par l’audit médical.
- **R-23** (données comparatives incomplètes, G92_pop2.html) : « (35 % contre 25 %, p = 0,464) ». Voir le renvoi de la section 10 de l’onglet Pathologie : groupes non nommés.
- **R-24** (critère composite non défini, G92_pop2.html) : « a été associé à moins de complications (p = 0,039) ». Cette fenêtre dit « moins de complications » alors que la section 10 dit « moins de complications composites » : la nature du critère est à établir par la source primaire (Stolz et coll.).
- **R-25** (portée d’un examen négatif, g92.py) : « Virus dont la PCR dans le liquide cérébrospinal exclut une infection du système nerveux central en cas de doute. ». Le CMV est défini par la portée de sa PCR (« exclut une infection ») ; les définitions voisines (EBV, HSV, VZV) disent seulement « virus recherché par PCR ». Même difficulté que dans l’onglet Examens (fiche Liquide cérébrospinal).
- **R-26** (fréquence, g92.py) : « Maladie dont la forme grave en réanimation s’accompagne souvent d’une encéphalopathie aiguë. ». « Souvent » n’est pas repris dans le texte principal (section 3.3 : « est associée à l’hypoxémie… »), qui n’indique aucune fréquence. À sourcer ou à retirer par l’audit médical.

## Constats hors périmètre linguistique

- **H-01** (MAJEUR) : Hors périmètre linguistique, MAJEUR, transmis à l'audit MED. Décompte réel de la barre .sci-bar de G92_c.html : quatre disciplines (g92-s-immuno, g92-s-neuro, g92-s-bioch, g92-s-imagerie : Immunologie, Neurophysiologie, Biochimie, Imagerie). Le sous-onglet « Sémiologie fondamentale et analytique » (6e sous-onglet de Sciences selon l'exigence Vial) est absent : aucune occurrence de « sémiologie » dans les sept fichiers.
- **H-02** (MINEUR) : Les liens vers l'information professionnelle suisse sont de la forme href="https://amiko.oddb.org (GTIN …)" : l'URL contient une espace et des parenthèses, donc n'est pas une adresse valide et ne renvoie pas à la monographie. 49 occurrences dans les six fichiers HTML (GTIN Yescarta 7680669860011, Actemra 7680588680011, Cefepim Leman 7680700080019, Holoxan 7680412170817, Depakine 7680347340125, MetronidazoleSINT i.v. 7680708870018). Correction à confier à une mission d'intégration ; non proposée ici car elle modifie une référence.

## Choix différés

- Espaces insécables globales (avant ; : ! ?, dans les guillemets « », dans les nombres et devant %, mg, mL) : non appliquées, ni proposées une à une. Les sept fichiers ne contiennent aucun U+00A0 ni U+202F.
- Séparateur des milliers : « 1000 mg » est écrit sans espace dans les six fichiers (tableaux de dosage, quiz, fenêtres) ; relève du choix différé sur les espaces insécables et les nombres.
- Style des nombres : « deux fois par jour » (lettres) voisine avec « 3 à 4 fois par jour » (chiffres) dans le tableau 9.1 ; harmonisation non proposée pour ne toucher à aucun chiffre.

## Observations

- Description du plan ou de la fabrication du cours dans le texte (guide de rédaction § 3, non local donc non proposé) : section 0 (« Le chapitre commence donc par ce socle commun, puis développe… », « Objectifs. À la fin du chapitre, le lecteur sait… »), mentions « sources lues » (11), « source lue » (3), « n'a pas été lu » et variantes (5), « le dossier » (3). Ces formules relèvent de la méthode et non de la médecine ; leur retrait demande une réécriture de paragraphes.
- Introduction de tableau (guide § 4) : « Le tableau suivant relie les agents aux examens qui orientent le diagnostic. » (onglet Examens) paraphrase les en-têtes du tableau ; non reformulé car sans faute et non local.
- Cartes et listes nominales (guide § 2) : les cartes « Forme typique » et « Formes atypiques », ainsi que certaines cellules de tableau, restent télégraphiques ; seules les listes en texte courant, les alertes et les fenêtres ont fait l'objet de propositions.
- Termes étrangers non balisés : « Toxische Enzephalopathie », « Cornell Assessment of Pediatric Delirium », « Immune effector Cell-associated Encephalopathy », « Swiss Medical Forum » sont écrits sans italique ni attribut de langue ; convention typographique à décider globalement.
- Figures : six schémas SVG (figures 1 à 6), tous des diagrammes de processus à cases et flèches, aucune anatomie dessinée ; le contrôle a porté sur le texte des étiquettes. Étiquette de la figure 2 « leptoméninges » conservée : une forme plus complète (« atteinte leptoméningée ») dépasserait la largeur de la case du schéma.
- Cohérence terminologique résiduelle : « syndrome de neurotoxicité associé aux cellules effectrices immunitaires » (glossaire ICANS) ; « neurotoxicité des cellules effectrices immunitaires » corrigé en P-01 et dans le glossaire ASTCT.

## Lacunes

- Aucune vérification médicale n'a été faite : les renvois_medicaux signalent des formulations dont la correction changerait le fond ; ils ne sont ni confirmés ni infirmés.
- Aucun contrôle de rendu navigateur des propositions : l'application simulée a été faite en mémoire, aucun fichier canonique n'est modifié.
- Aucune lecture des sources primaires citées : les écarts avec les sources sont établis seulement par comparaison interne entre les sept fichiers de la leçon.
- Aucun contrôle de l'exactitude des liens (les adresses ne sont pas consultées).

## Tableau de bord

| Indicateur | Valeur |
|---|---|
| Fichiers lus | 7 sur 7 |
| Empreintes conformes | oui |
| Propositions | 104 |
| Propositions à ancien unique | 104 sur 104 |
| Renvois médicaux | 26 |
| Constats hors périmètre | 2 |
| Choix différés | 3 |
| Abréviations non couvertes après application | 0 |
| Source canonique modifiée | non |

Horodatage : date_debut non relevé (null) ; date_fin relevée par date -u avant le commit.
