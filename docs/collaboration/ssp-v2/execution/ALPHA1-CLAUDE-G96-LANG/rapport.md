# Audit linguistique G96 — Autres affections du système nerveux central : fuites de liquide céphalorachidien (S08)

Mission ALPHA1-CLAUDE-G96-LANG, tour 4, génération 1. Branche `claude/alpha1/g96-lang-g1`, base de la mission `523832d9` (worktree démarré sur `103745ba`, qui contient la même base ; sources figées identiques, empreintes conformes). Audit IA : revue distincte d'une validation médicale humaine ; aucune source canonique modifiée.

## Synthèse

Les sept fichiers de la leçon (quatre onglets, deux fenêtres, glossaire) ont été lus en entier ; leurs empreintes SHA-256 sont conformes au manifeste. Le texte est globalement correct et sobre, avec des phrases généralement complètes. Les défauts relevés tiennent à des constructions fautives (« jusqu'à 10 à 15 % », « à 4 à 8 semaines », « sur des mois à des années », « tous les un à deux ans »), à des zeugmes et verbes impropres (« touche… l'obésité », « on obtient… une chirurgie bariatrique », « la lésion de la fuite »), à des pronoms ambigus (« Elle est inférieure à 60 mm… » après « La pression d'ouverture normale »), à des infinitifs injonctifs et phrases nominales que le guide de rédaction proscrit, à des anglicismes (« mimes », « gérer », « patch-sealing ») et à des unités omises (« 30 par minute », « moins de 10 »).

- **114 propositions locales** (`propositions.json`), chacune avec un `ancien` unique dans son fichier, `fond_inchange: true`, sans chevauchement ; application simulée en mémoire suivie de `build_medina.audit()` : aucune abréviation non couverte, glossaire Python valide.
- **25 renvois médicaux** : formulations où une correction créerait ou retirerait une causalité, une fréquence, une chronologie ou une précision anatomique que la leçon ne porte pas. Ils ne sont pas corrigés ici.
- **Choix différés, non appliqués** : espaces insécables globales (aucun U+00A0 ni U+202F dans les sept fichiers) ; harmonisation « scanner » / « tomodensitométrie ».

## Propositions par catégorie

| Catégorie | Nombre |
|---|---|
| syntaxe | 42 |
| registre | 21 |
| ambiguïté | 17 |
| répétition | 8 |
| typographie | 8 |
| grammaire | 7 |
| cohérence | 6 |
| ponctuation | 5 |

## Propositions par fichier

| Fichier | Nombre |
|---|---|
| `chapters/G96/G96_a.html` | 33 |
| `chapters/G96/G96_b.html` | 30 |
| `chapters/G96/G96_c.html` | 15 |
| `chapters/G96/G96_d.html` | 6 |
| `chapters/G96/G96_pop1.html` | 19 |
| `chapters/G96/G96_pop2.html` | 10 |
| `glossary/g96.py` | 1 |

## Les trois constats les plus graves (renvois)

1. **R-22 — figure 2 contredit sa légende.** Le schéma SVG des volumes intracrâniens dessine le rectangle « Sang » de hauteur 80 (normal) puis 40 (perte), alors que la légende annonce que le volume sanguin augmente en compensation (Monro-Kellie). La figure de la physiologie affirme donc le contraire du texte (contrôle sur les coordonnées du SVG, sans rendu navigateur).
2. **R-18 / R-19 — deux formulations de conduite à sens opposés possibles.** « L'évitement des efforts et des laxatifs » (rhinorrhée traumatique) peut se lire éviter les laxatifs ou les prescrire ; « un drain lombaire peut raccourcir la fuite » est une métonymie ambiguë. Seule la source tranche.
3. **R-10 — contradiction chiffrée interne.** La démence frontotemporale de variante comportementale est donnée à 2,5 % (section 5) alors que le tableau des complications (section 8) range « Coma, démence frontotemporale » parmi les formes « rares (moins de 1 %) ». La douleur interscapulaire à 10,9 % est en outre classée parmi les « formes rares ».

## Renvois médicaux (hors correction linguistique)

- **R-01** (terminologie anatomique, `G96_a.html`) : « fistule entre l’espace du liquide et une veine ». L’expression « espace du liquide » (aussi G96_a section 3 « met l’espace du liquide en communication », G96_c section anatomie et légende de la figure 1, fenêtre g96-flv de G96_pop1) n’est pas un terme anatomique. L’arachnoïdite est décrite dans le même cours avec « l’espace sous-arachnoïdien ». Remplacer l’expression revient à désigner un compartiment anatomique précis : à trancher par l’audit médical.
- **R-02** (ambiguïté de source, `G96_a.html`) : « La série du centre de Fribourg classe les fuites spinales en trois types ». « Fribourg » désigne ici (et dans « revue de Fribourg », « série de Fribourg ») un centre dont le pays n’est précisé dans aucun des sept fichiers. Un lecteur suisse comprend le canton de Fribourg ; or les références citées en fin de section 12 (Deutsches Ärzteblatt International, Neuroradiology) ne tranchent pas. L’identité du centre et la graphie correcte (Fribourg, Fribourg-en-Brisgau) relèvent de la lecture de la source.
- **R-03** (causalité, `G96_a.html`) : « Cette divergence reflète l’essor de la myélographie dynamique, qui détecte désormais davantage de fistules. ». La phrase donne une explication causale (essor de la myélographie dynamique) à la différence de fréquences entre deux séries de dates différentes ; ni la section ni les fenêtres ne contiennent d’élément qui l’établisse. À sourcer ou à retirer par l’audit médical.
- **R-04** (cohérence chiffrée, `G96_a.html`) : « Dans chaque série les pourcentages totalisent plus de 100 % ». Après traumatisme, 46 + 44 + 15 + 11 = 116 %. Sans traumatisme, les trois pourcentages cités (30, 17, 16) totalisent 63 % : l’énoncé « dans chaque série » ne se vérifie pas dans le texte pour la seconde série (liste peut-être partielle). La précision ou la correction suppose de relire la source.
- **R-05** (modalité / fréquence, `G96_a.html`) : « le fait qu’un quart des hématomes sous-duraux du sujet de moins de 60 ans a cette origine ». Le corps de la section dit « seraient dus » (conditionnel) ; l’encadré « À retenir » l’affirme à l’indicatif. Aligner le mode revient à fixer le niveau de certitude d’un chiffre épidémiologique : décision médicale.
- **R-06** (causalité, `G96_a.html`) : « Une étude bernoise apporte une preuve causale. ». « Preuve causale » est tirée d’une comparaison avant/après de volumes ventriculaires ; la fenêtre g96-monro (G96_pop1) qualifie l’étude de « petit effectif, résumé seul lu ». Le degré de preuve annoncé est plus fort que celui de la fenêtre. Voir aussi R-23 (G96_c).
- **R-07** (chronologie / chiffres, `G96_a.html`) : « dès environ quatre jours ». Le délai est écrit « dès environ quatre jours » (G96_a), « en environ quatre jours » (G96_c, section de physiologie) et « en quatre jours » (G96_pop1, g96-monro) : trois sens différents (au plus tôt, en moyenne, exactement). De plus, de 15,3 à 18,0 mL la hausse arithmétique est de 17,6 % alors que le texte cite 18,8 % « selon les auteurs, calculée sur les variations individuelles » : à vérifier dans la source.
- **R-08** (unités / cohérence, `G96_a.html`) : « inférieure à 6 cm d’eau ou, le plus souvent, normale, mais non négative ». Le cours exprime la pression d’ouverture en « mm de liquide » (60 mm) ailleurs ; ici l’hypothèse bernoise est donnée en « cm d’eau » (6 cm d’eau, soit 60 mm d’eau). Harmoniser les unités et préciser « non négative » exige de relire la source.
- **R-09** (ambiguïté anatomique, `G96_a.html`) : « Plusieurs lésions rachidiennes sont retrouvées sous la fuite ». « Sous la fuite » (reprise dans le tableau de la section 4 : « Retrouvés sous la fuite ») peut signifier en regard, en dessous (caudal) ou sous-jacent à la fuite. Le sens retenu modifie l’énoncé anatomique.
- **R-10** (fréquence / cohérence chiffrée, `G96_a.html`) : « Les formes rares sont à connaître car elles changent la gravité ». Les « formes rares » incluent la douleur interscapulaire à 10,9 % et la démence frontotemporale de variante comportementale à 2,5 %. Dans G96_b (tableau de la section 8), « Coma, démence frontotemporale » est dit « rares (moins de 1 %) », ce qui contredit le 2,5 % de la section 5. Corriger un des deux chiffres ou le qualificatif « rares » est une décision médicale.
- **R-11** (omission, `G96_a.html`) : « consiste à se pencher en avant, assis, après un temps en décubitus ». La phrase décrit la manœuvre (se pencher en avant, assis, après un temps en décubitus) sans dire ce qui est observé ; la fenêtre g96-reservoir précise « laisse s’écouler le liquide par le nez ». Ajouter le résultat est un ajout de fait.
- **R-12** (causalité / affirmation, `G96_b.html`) : « l’avis neuroradiologique tranche ». La phrase vient d’annoncer que les sources lues ne détaillent aucun critère distinctif pour la malformation de Chiari et les céphalées cervicogènes ; elle affirme ensuite que l’avis neuroradiologique « tranche ». Cette affirmation n’a pas de source lue dans le cours : à sourcer ou à retirer.
- **R-13** (terminologie, `G96_b.html`) : « Pneumocéphalie, crise, abcès épidural, hydrocéphalie (rhinorrhée) ». « Crise » sans qualificatif est ambigu (crise épileptique, comitiale, autre). Préciser le type de crise ajoute un fait que la section ne porte pas.
- **R-14** (ambiguïté chiffrée, `G96_b.html`) : « (139 et 169 minutes selon le groupe) ». La phrase donne deux valeurs « selon le groupe » pour la céphalée résolue (89 % et 94 %) et pour la durée (139 et 169 minutes) sans dire quel groupe correspond à quelle valeur, ni lequel est le « sealing ». L’appariement est un fait de la source. « Résultats équivalents » avec 89 % et 94 % est en outre une qualification statistique à vérifier.
- **R-15** (ambiguïté de conduite, `G96_b.html`) : « relève d’un traitement endovasculaire envisageable en première ligne, avec patch ciblé et chirurgie ». « Avec patch ciblé et chirurgie » peut signifier une association (traitement endovasculaire plus patch ciblé plus chirurgie) ou une liste d’options. Les deux lectures définissent des conduites différentes ; le choix suppose la source.
- **R-16** (référent manquant, `G96_b.html`) : « Le risque est plus élevé quand le délai dépasse 10 semaines ». « Le délai » n’est pas défini (délai depuis le début des symptômes, avant le diagnostic, avant le traitement ?). La fenêtre g96-rebond (G96_pop1) répète « Délai de plus de 10 semaines » sans plus. Préciser le point de départ est un ajout de fait.
- **R-17** (ambiguïté chronologique, `G96_b.html`) : « on réévalue si elle est sévère après une à deux semaines ». Deux lectures sont possibles : réévaluer après une à deux semaines si l’hypertension est sévère ; ou réévaluer si elle est encore sévère après une à deux semaines. La seconde implique une persistance. La fenêtre g96-rebond reprend la même formulation. Le choix de la lecture est clinique.
- **R-18** (ambiguïté de sens, `G96_b.html`) : « l’évitement des efforts et des laxatifs ». La phrase se lit « on prescrit le repos, la tête surélevée à 30°, l’évitement des efforts et des laxatifs », ce qui peut signifier éviter les efforts et éviter les laxatifs, ou éviter les efforts et prescrire des laxatifs (pour prévenir l’effort de poussée). Les deux lectures sont opposées pour les laxatifs ; seule la source tranche.
- **R-19** (sens du verbe, `G96_b.html`) : « Un drain lombaire peut raccourcir la fuite. ». « Raccourcir la fuite » est une métonymie ambiguë : raccourcir la durée de la fuite, la tarir, ou en réduire le débit. Chaque lecture est un énoncé différent sur l’effet du drain.
- **R-20** (référent manquant, `G96_b.html`) : « avec un contrôle à trois mois après l’opération ». La relation entre « récupération plus lente » et « un contrôle à trois mois » n’est pas dite (récupération évaluée à trois mois ? effet mesuré lors d’un contrôle ?). La fenêtre et le tableau de références ne la précisent pas.
- **R-21** (précision anatomique, `G96_c.html`) : « Le liquide céphalorachidien est contenu dans les méninges ». Le liquide est contenu dans l’espace sous-arachnoïdien (et les ventricules), c’est-à-dire entre deux des méninges ; la phrase suivante parle de la dure-mère comme « enveloppe externe ». Remplacer « dans les méninges » par un espace précis est une précision anatomique à valider.
- **R-22** (figure / légende, `G96_c.html`) : « à droite, le volume sanguin intracrânien augmente en compensation ». Dans le schéma SVG de la figure 2, la paire de droite (« Sang ») est dessinée avec un rectangle intérieur de hauteur 80 à l’état « Normal » puis de hauteur 40 à l’état « Perte » : la hauteur de la grandeur dessinée diminue, alors que la légende dit que le volume sanguin augmente. La légende et le dessin se contredisent (contrôle fait sur les coordonnées du SVG, sans rendu navigateur). À corriger par l’audit médical et la production.
- **R-23** (cohérence / degré de preuve, `G96_c.html`) : « apporte la preuve causale ». G96_a écrit « une preuve causale » ; G96_c écrit « la preuve causale » (article défini, sens plus fort). Voir R-06 ; l’alignement des deux formulations dépend du degré de preuve retenu.
- **R-24** (mention de fabrication, `G96_pop1.html`) : « Extraits repris du dossier consacré à un autre cours du même cycle ». La mention décrit la provenance des extraits (dossier d’un autre cours du même cycle) et non un contenu médical. Elle est utile à la traçabilité mais déplacée dans une fenêtre destinée au lecteur du cours ; la retirer ou la déplacer vers les sources relève de la gouvernance, non d’une correction linguistique.
- **R-25** (chronologie / fréquence, `G96_pop2.html`) : « Un éperon, une hernie discale ou une hypermobilité précèdent souvent la déchirure. ». Le Pareto affirme une antériorité (« précèdent ») et une fréquence (« souvent ») que la section 4 ne porte pas : le corps du cours dit que ces lésions sont « retrouvées » et qu’un trouble conjonctif « peut prédisposer ». Le Pareto change donc le niveau de certitude.

## Figures

Le contrôle a porté sur le texte des figures et, pour la figure 2, sur les coordonnées du SVG ; la provenance est transmise à l'audit médical.

| Figure | Classe | Statut |
|---|---|---|
| Figure 1, types de fuite spinale (G96_c) | ORIGINE_INCONNUE | réserve : schéma dessiné en SVG, « non calibré » selon sa légende |
| Figure 2, volumes intracrâniens (G96_c) | ORIGINE_INCONNUE | réserve : incohérence avec la légende (R-22) |
| Trois icônes de la barre des sciences | non anatomique | sans objet |

## Choix différés et observations

- Espaces insécables (avant ; : ! ? et %, dans les guillemets « », dans les nombres) : non appliquées, non proposées. Les sept fichiers ne contiennent aucun U+00A0 ni U+202F ; le choix est global au projet.
- Nombres : « 100 000 » est écrit avec une espace ordinaire, « 2000 », « 3000 » et « 4000 » sans espace ; relève du même choix différé.
- Libellés de liens interactifs : la parenthèse explicative incorporée au mot vert (« signe du halo (portée et limites) sur papier filtre », « acte ou le traumatisme qui précède (critères et codage) ») coupe la phrase ; convention d’interface du projet, non modifiée.
- Phrases nominales : les cellules de tableau, les listes « Pareto » et l’encadré « Paramètres clés » restent en style télégraphique (toléré pour les cellules par STYLE_REDACTION § 2) ; seules les phrases nominales ou infinitives hors cellules ont fait l’objet de propositions. Plusieurs puces Pareto nominales subsistent (par exemple « Trois types de fuite, trois lieux : face ventrale, gaine, veine. »).
- Acronyme SLEC : l’expansion française de l’article (« collection extradurale longitudinale spinale ») n’a pas les initiales S-L-E-C ; le glossaire donne l’expansion anglaise (Spinal Longitudinal Extradural CSF collection). Une mention « (de l’anglais … ) » ou l’emploi du terme anglais serait plus clair ; non proposé pour ne pas modifier le glossaire au-delà de la formulation.
- Anglicisme « compliant » (G96_a, section 3 : « un compartiment spinal trop compliant ») : « distensible » est possible mais relève du vocabulaire de la physiologie ; non proposé.
- Alternance « scanner » (G96_b, G96_c) et « tomodensitométrie » : usage tolérable en clinique suisse, non harmonisé.
- Mentions du cours dans le cours (« le cours ne propose pas de conduite », « le cours n’y ajoute rien », « Dans ce cours » dans le glossaire) : elles énoncent des limites de sources et sont conservées ; elles relèvent de la politique de rédaction, non de la correction linguistique.
- Glossaire : la définition de CIM-10-GM (« catalogue de ce projet ») décrit la fabrication du cours ; non modifiée pour ne pas retirer d’information de provenance.
- Statut en tête de leçon (« Cycle Betta 41 · Revue par intelligence artificielle · Audit différé · Aucune validation médicale humaine ») : mention de gouvernance conservée.

## Lacunes

- Aucune vérification médicale n’a été faite : les renvois_medicaux signalent des formulations dont la correction changerait le fond ; ils ne sont ni confirmés ni infirmés.
- Aucun contrôle de rendu navigateur des propositions : l’application simulée a été faite en mémoire, aucun fichier canonique n’est modifié ; le contrôle de la figure 2 (R-22) porte sur les coordonnées du SVG, sans rendu (aucun navigateur disponible dans l’environnement).
- Aucune lecture des sources primaires citées : les écarts avec les sources sont établis seulement par comparaison interne entre les sept fichiers de la leçon.
- Les propositions sur les unités (« battements par minute », « mL/min ») reprennent l’unité usuelle du même paramètre dans le même texte ; elles n’ont pas été confrontées à l’information professionnelle.

## Tableau de bord final

| Indicateur | Valeur |
|---|---|
| Fichiers lus en entier | 7 / 7 |
| Empreintes SHA-256 conformes au manifeste | oui |
| Propositions locales | 114 |
| Propositions à ancien unique | 114 / 114 |
| Chevauchements entre propositions | aucun |
| Renvois médicaux | 25 |
| Abréviations non couvertes après application simulée | 0 |
| Source canonique modifiée | non |

Audit IA — revue distincte d'une validation médicale humaine ; aucune source canonique modifiée.
