# Audit linguistique ALPHA1-CLAUDE-G80-LANG — G80 Infirmité motrice cérébrale (paralysie cérébrale)

Mission d’audit IA du fragment S08, tour 1 d’Alpha. Revue de la langue : formulation locale proposée, fond médical inchangé. **Aucune source canonique n’est modifiée** ; les propositions sont à intégrer par une mission d’intégration.

## Synthèse pour Vial

- **74 propositions locales** (chaque « ancien » apparaît exactement une fois dans son fichier, sans chevauchement) ;
- **13 renvois médicaux** : formulations dont la correction changerait le fond, laissées à l’audit médical ;
- empreintes SHA-256 des sept fichiers conformes au manifeste ; abréviations : `build_medina.audit()` renvoie `{}` avant et après application simulée ;
- aucun fait, chiffre, dose ni source n’est ajouté, retiré ou modifié par une proposition.

### Répartition par catégorie

| Catégorie | Propositions |
|---|---|
| syntaxe | 32 |
| registre | 13 |
| ambiguité | 9 |
| grammaire | 6 |
| typographie | 5 |
| répétition | 3 |
| cohérence | 3 |
| ponctuation | 3 |

### Répartition par fichier

| Fichier | Propositions |
|---|---|
| `chapters/G80/G80_a.html` | 16 |
| `chapters/G80/G80_b.html` | 25 |
| `chapters/G80/G80_c.html` | 18 |
| `chapters/G80/G80_d.html` | 8 |
| `chapters/G80/G80_pop1.html` | 4 |
| `chapters/G80/G80_pop2.html` | 2 |
| `glossary/g80.py` | 1 |

## Les défauts les plus nets

- **P-58** — Phrase tronquée en biochimie (« elle traite la spasticité focale et, avec un effet de 3 à 8 mois ») : la coordination n’a pas de second terme.
- **P-31** — « (niveau III) » désigne le niveau de preuve d’une étude de hanche chez des enfants GMFCS IV–V : le lecteur lit un niveau GMFCS III. Le libellé du lien devient « niveau de preuve III ».
- **P-06** — « Plus de subdivision en diplégie, triplégie ou tétraplégie » se lit « davantage de subdivision » : le tableau dit l’inverse de ce que le SCPE a décidé ; la formulation devient « Subdivision … abandonnée ».
- **P-27 / P-47** — Faute d’accord « Aucune ne se reconnaît sans les avoir cherchées » ; comparaison asymétrique « sensibilité moindre que les autres outils ».

## Propositions


### `chapters/G80/G80_a.html`

**P-01** (syntaxe) — « Attendre » avec une durée est ambigu (la confirmation attend-elle ou dure-t-elle ?) ; nombres écrits en chiffres comme dans le reste de la leçon (« 6 mois d’âge corrigé », « 4–5 ans »).

> ancien : Il se pose parfois avant six mois d’âge corrigé, mais sa confirmation définitive attend souvent quatre à cinq ans.
>
> nouveau : Il se pose parfois avant 6 mois d’âge corrigé, mais sa confirmation définitive n’intervient souvent qu’entre 4 et 5 ans.

**P-02** (registre) — L’annonce pédagogique expose le problème médical ; elle ne décrit pas le plan ni la fabrication du cours (STYLE_REDACTION § 3).

> ancien : Ce cours suit ces cinq questions. Il s’appuie sur la classification allemande
>
> nouveau : Les réponses s’appuient sur la classification allemande

**P-03** (syntaxe) — Enchaînement de trois « et » : la coordination est rendue lisible par une virgule et une conjonction qui sépare les deux phénomènes.

> ancien : car le cerveau mûrit et les muscles et les articulations se déforment
>
> nouveau : car le cerveau mûrit, tandis que les muscles et les articulations se déforment

**P-04** (répétition) — Répétition « cérébrale » / « cerveau » dans la même proposition.

> ancien : non une lésion cérébrale fixe survenue dans le cerveau en développement
>
> nouveau : non une lésion fixe survenue dans le cerveau en développement

**P-05** (registre) — « Parler d’atteinte » est oral et sans article ; « décrire » est le verbe du registre professionnel.

> ancien : alors que le réseau SCPE parle d’atteinte unilatérale ou bilatérale
>
> nouveau : alors que le réseau SCPE décrit une atteinte unilatérale ou bilatérale

**P-06** (ambiguité) — « Plus de subdivision » se lit « davantage de subdivision » : l’ambiguïté est levée par une formulation sans équivoque (le contexte — le SCPE a remplacé les anciennes classifications — indique l’abandon).

> ancien : <td>Plus de subdivision en diplégie, triplégie ou tétraplégie</td>
>
> nouveau : <td>Subdivision en diplégie, triplégie ou tétraplégie abandonnée</td>

**P-07** (grammaire) — MACS désigne une seule classification (glossaire : « Manual Ability Classification System ») ; le pluriel « les échelles MACS » est fautif.

> ancien : les sources citent les échelles <button class="w" data-k="g80-macs">MACS</button> et une échelle de communication
>
> nouveau : les sources citent l’échelle <button class="w" data-k="g80-macs">MACS</button> et une échelle de communication

**P-08** (registre) — Le « chapitre » désigne le cours entier (G80) ; la physiopathologie est une partie (section 4).

> ancien : décrite dans le chapitre de physiopathologie
>
> nouveau : décrite dans la partie consacrée à la physiopathologie

**P-09** (syntaxe) — Le réseau ne possède pas de prévalence : il la mesure (métonymie ambiguë).

> ancien : la prévalence du réseau SCPE a baissé
>
> nouveau : la prévalence mesurée par le réseau SCPE a baissé

**P-10** (syntaxe) — GMFCS est un système de classification : c’est le niveau qui est plus ou moins élevé (cf. glossaire QI : « niveau GMFCS »).

> ancien : un GMFCS plus élevé s’associait à un quotient intellectuel plus bas
>
> nouveau : un niveau GMFCS plus élevé s’associait à un quotient intellectuel plus bas

**P-11** (registre) — Intitulé obscur : « population des chiffres » ne dit pas à quelle population s’appliquent les données.

> ancien : <span class="k">Population des chiffres</span> Le registre suisse
>
> nouveau : <span class="k">Population concernée</span> Le registre suisse

**P-12** (typographie) — Locution latine en italique, comme dans G80_b et G80_c.

> ancien : variants de novo ponctuels
>
> nouveau : variants <i>de novo</i> ponctuels

**P-13** (ambiguité) — « Par » est ambigu (agent ou moyen) : la phrase suivante précise que les sources ne détaillent pas l’origine de la spasticité.

> ancien : décrivent le mécanisme de la spasticité par l’action des médicaments
>
> nouveau : décrivent le mécanisme de la spasticité à travers l’action des médicaments

**P-14** (cohérence) — Terminologie : « jonction neuromusculaire » est le terme employé partout ailleurs dans la leçon.

> ancien : l’autre à la jonction avec le muscle
>
> nouveau : l’autre à la jonction neuromusculaire

**P-15** (syntaxe) — Même correction que pour la section 3.2 : c’est le niveau qui est élevé.

> ancien : QI plus bas avec un GMFCS plus élevé
>
> nouveau : QI plus bas avec un niveau GMFCS plus élevé

**P-16** (syntaxe) — Phrase nominale proscrite (STYLE_REDACTION § 2) : sujet et verbe conjugué rétablis.

> ancien : <p>Raideur à la mobilisation, réflexes vifs, asymétrie si la forme est unilatérale.
>
> nouveau : <p>Le médecin constate une raideur à la mobilisation, des réflexes vifs et, si la forme est unilatérale, une asymétrie.


### `chapters/G80/G80_b.html`

**P-17** (syntaxe) — Phrase nominale dans l’algorithme (proscrite dans les listes, STYLE_REDACTION § 2).

> ancien : <li>Nourrisson à risque (prématurité, atteinte néonatale) ou inquiétude des parents.</li>
>
> nouveau : <li>Le point de départ est un nourrisson à risque (prématurité, atteinte néonatale) ou l’inquiétude des parents.</li>

**P-18** (syntaxe) — Phrase nominale remplacée par une phrase complète, mêmes éléments.

> ancien : <li>Anamnèse et examen neurologique standardisé (HINE), observation des mouvements généraux avant 5 mois.</li>
>
> nouveau : <li>Le médecin recueille l’anamnèse, réalise un examen neurologique standardisé (HINE) et observe les mouvements généraux avant 5 mois.</li>

**P-19** (syntaxe) — Infinitif injonctif sans sujet (proscrit) ; la formulation « classer le groupe » est impropre : on classe la lésion dans un groupe.

> ancien : <li>IRM : classer le groupe MRICS.</li>
>
> nouveau : <li>L’IRM permet de classer la lésion dans un groupe MRICS.</li>

**P-20** (ambiguité) — « Les trois » sans antécédent explicite ; phrase nominale remplacée par deux propositions conjuguées.

> ancien : <li>Si les trois sont concordants : diagnostic de « haut risque de PC » et orientation immédiate vers une intervention précoce.</li>
>
> nouveau : <li>Si les trois éléments concordent, le diagnostic est celui de « haut risque de PC » et l’enfant est orienté sans délai vers une intervention précoce.</li>

**P-21** (syntaxe) — Phrase nominale : sujet et verbe rétablis.

> ancien : signes neurodéveloppementaux : bilan génétique (
>
> nouveau : signes neurodéveloppementaux, le médecin demande un bilan génétique (

**P-22** (grammaire) — Accord syntaxique avec le verbe « demande » introduit à la proposition précédente (« rechercher » est transitif direct).

> ancien : ) et recherche d’une erreur innée du métabolisme.
>
> nouveau : ) et recherche une erreur innée du métabolisme.

**P-23** (syntaxe) — Phrase nominale remplacée par deux phrases conjuguées.

> ancien : <li>Évaluation du type SCPE et du niveau GMFCS à partir de 2 ans ; confirmation vers 4–5 ans.</li>
>
> nouveau : <li>Le type SCPE et le niveau GMFCS s’évaluent à partir de 2 ans ; la confirmation intervient vers 4–5 ans.</li>

**P-24** (syntaxe) — Épilogue en phrases complètes (STYLE_REDACTION § 3) ; mêmes éléments.

> ancien : Diagnostic clinique, posé précocement par la concordance de l’anamnèse, de l’imagerie et d’un examen standardisé ; toute régression ou toute imagerie normale ouvre la recherche d’une autre maladie.
>
> nouveau : Le diagnostic est clinique : il peut être posé précocement lorsque l’anamnèse, l’imagerie et un examen standardisé concordent. Toute régression ou toute imagerie normale ouvre la recherche d’une autre maladie.

**P-25** (syntaxe) — Place de l’adverbe : « surtout » porte sur la période (« la première année »), non sur l’adjectif.

> ancien : est surtout fréquente la première année
>
> nouveau : est fréquente surtout la première année

**P-26** (ambiguité) — La PC est un trouble (définition de la section 1) ; c’est la lésion qui est non progressive.

> ancien : La PC est une lésion non progressive : une aggravation brusque
>
> nouveau : La lésion à l’origine de la PC est non progressive : une aggravation brusque

**P-27** (grammaire) — Faute d’accord (« aucune » singulier, « les … cherchées » pluriel) et sujet de l’infinitif non rattaché.

> ancien : Aucune ne se reconnaît sans les avoir cherchées.
>
> nouveau : Aucune ne se reconnaît sans avoir été recherchée.

**P-28** (ponctuation) — Deux-points interdits entre le verbe « être » et son attribut.

> ancien : Les interventions <button class="w" data-k="g80-feux">« feu vert »</button> sont : la thérapie par contrainte induite
>
> nouveau : Les interventions <button class="w" data-k="g80-feux">« feu vert »</button> sont la thérapie par contrainte induite

**P-29** (syntaxe) — Fragment sans verbe : proposition rétablie.

> ancien : Sur le plan médical et chirurgical : les antiépileptiques
>
> nouveau : Sur le plan médical et chirurgical, ce sont les antiépileptiques

**P-30** (répétition) — Redondance « lombaires et sacrées » / « de la première racine lombaire à la première racine sacrée » et absence de virgule (la fourchette se lit comme complément de « sacrées »).

> ancien : sectionne 50 à 75 % des fibres afférentes des racines lombaires et sacrées de la première racine lombaire à la première racine sacrée
>
> nouveau : sectionne 50 à 75 % des fibres afférentes des racines nerveuses, de la première racine lombaire à la première racine sacrée

**P-31** (ambiguité) — Ambiguïté avec le niveau GMFCS III, employé partout ailleurs dans la leçon (le contexte immédiat parle de GMFCS IV–V).

> ancien : data-k="g80-chir-hanche">niveau III</button>
>
> nouveau : data-k="g80-chir-hanche">niveau de preuve III</button>

**P-32** (syntaxe) — On ne réduit pas la PC mais son risque (le risque relatif 0,71 qui suit est un risque).

> ancien : avant 34 SA réduit la PC à 2 ans d’âge corrigé (
>
> nouveau : avant 34 SA réduit le risque de PC à 2 ans d’âge corrigé (

**P-33** (syntaxe) — Coordination fautive : le sulfate ne réduit pas « le critère composite » ; il réduit le risque mesuré par ce critère.

> ancien : et le critère composite décès ou PC (risque relatif 0,87)
>
> nouveau : et celui du critère composite « décès ou PC » (risque relatif 0,87)

**P-34** (registre) — Intitulé obscur (voir P-11).

> ancien : <span class="k">Population des chiffres</span> Le pronostic
>
> nouveau : <span class="k">Population concernée</span> Le pronostic

**P-35** (syntaxe) — Même correction que pour la section 10.1 ; seconde proposition nominale remplacée par une phrase conjuguée.

> ancien : avant 34 SA réduit la PC à 2 ans ; 60 femmes à traiter pour éviter un cas.
>
> nouveau : avant 34 SA réduit le risque de PC à 2 ans ; il faut traiter 60 femmes pour éviter un cas.

**P-36** (registre) — « Sulfate de magnésium maternel » est une expression elliptique et trompeuse (le médicament n’est pas maternel).

> ancien : relève du sulfate de magnésium maternel
>
> nouveau : justifie l’administration de sulfate de magnésium à la mère

**P-37** (ambiguité) — « Signaler une prudence » est impropre ; « les posologies ne sont pas ajustées » se lit comme un fait clinique alors que la phrase décrit une lacune des sources.

> ancien : signale une prudence en cas d’insuffisance rénale. Les posologies ne sont pas ajustées dans les sources lues.
>
> nouveau : recommande la prudence en cas d’insuffisance rénale. Les sources lues ne précisent aucun ajustement posologique.

**P-38** (syntaxe) — Énumération sans articles et virgule devant le dernier « et » ; articles rétablis, ponctuation corrigée.

> ancien : Le plan associe rééducation orientée vers des buts, surveillance radiographique de ses hanches (risque croissant avec le niveau GMFCS), évaluation de la parole et de la déglutition, recherche de l’épilepsie, et discussion d’une injection
>
> nouveau : Le plan associe une rééducation orientée vers des buts, la surveillance radiographique de ses hanches (risque croissant avec le niveau GMFCS), l’évaluation de la parole et de la déglutition, la recherche de l’épilepsie et la discussion d’une injection

**P-39** (ponctuation) — Deux-points interdits entre le verbe « être » et son attribut ; énumération coordonnée.

> ancien : Les limites d’âge des médicaments sont : 12 mois (baclofène oral), 2 ans (toxine), 4 ans (sécurité du baclofène intrathécal).
>
> nouveau : Les limites d’âge des médicaments sont de 12 mois (baclofène oral), de 2 ans (toxine) et de 4 ans (sécurité du baclofène intrathécal).

**P-40** (syntaxe) — Épilogue nominal remplacé par une phrase complète (STYLE_REDACTION § 3).

> ancien : Rééducation intensive centrée sur des buts, toxine botulique pour la spasticité focale, baclofène ou rhizotomie pour les formes sévères, surveillance de hanche, traitement de l’épilepsie : le tout réuni par une équipe.
>
> nouveau : La prise en charge associe une rééducation intensive centrée sur des buts, la toxine botulique pour la spasticité focale, le baclofène ou la rhizotomie pour les formes sévères, la surveillance de la hanche et le traitement de l’épilepsie, le tout réuni par une équipe.

**P-41** (typographie) — Le signe « = » est proscrit dans le texte courant.

> ancien : Hanche : migration supérieure à 40 % = déplacement ;
>
> nouveau : Hanche : migration supérieure à 40 % signant un déplacement ;


### `chapters/G80/G80_c.html`

**P-42** (registre) — Anglicisme ; « examen de référence » est la locution employée dans la phrase suivante.

> ancien : Le « gold standard » doit être nommé avec précision.
>
> nouveau : L’examen de référence doit être nommé avec précision.

**P-43** (syntaxe) — Épilogue nominal remplacé par des phrases conjuguées ; même contenu.

> ancien : Une question, un examen, un statut : mouvements généraux et HINE pour le risque, IRM pour la lésion, radiographie pour la hanche, génétique en cascade pour les cas atypiques.
>
> nouveau : À chaque question correspondent un examen et un statut : les mouvements généraux et l’HINE évaluent le risque, l’IRM la lésion, la radiographie la hanche et la génétique en cascade les cas atypiques.

**P-44** (répétition) — Répétition « donnent … donnent » dans la même phrase.

> ancien : Les sources lues donnent les <b>sensibilités</b> ; elles ne donnent pas les seuils de cotation détaillés, qui n’ont pas été lus.
>
> nouveau : Les sources lues fournissent les <b>sensibilités</b>, mais non les seuils de cotation détaillés, qui n’ont pas été lus.

**P-45** (grammaire) — Pronom au singulier alors que le sujet (« mouvements généraux ») est au pluriel ; « seul » et « sans imagerie » disent la même chose.

> ancien : l’utiliser seul sans imagerie.
>
> nouveau : les utiliser sans imagerie.

**P-46** (ambiguité) — L’adjectif « anormale » se rattache grammaticalement à « sensibilité » (féminin) ; le sujet réel est l’IRM.

> ancien : sensibilité 86 à 89 % ; anormale chez plus de 80 % des enfants atteints.
>
> nouveau : sensibilité 86 à 89 % ; l’IRM est anormale chez plus de 80 % des enfants atteints.

**P-47** (syntaxe) — Comparaison asymétrique (une sensibilité n’est pas moindre que des outils) ; phrase nominale.

> ancien : <b>Piège :</b> sensibilité moindre que les autres outils.
>
> nouveau : <b>Piège :</b> sa sensibilité est moindre que celle des autres outils.

**P-48** (registre) — Lourdeur de la locution « c’est la raison pour laquelle ».

> ancien : une anomalie isolée ne suffit donc pas, et c’est la raison pour laquelle le diagnostic exige la concordance.
>
> nouveau : une anomalie isolée ne suffit donc pas, ce qui explique que le diagnostic exige la concordance.

**P-49** (typographie) — Le signe « = » est proscrit dans le texte courant ; phrase complète.

> ancien : <b>Valeur :</b> migration de Reimers supérieure à 40 % = hanche déplacée.
>
> nouveau : <b>Valeur :</b> une migration de Reimers supérieure à 40 % définit une hanche déplacée.

**P-50** (registre) — Intitulé inexact : le tableau ne présente pas des diagnostics mais l’imagerie, les comorbidités et la hanche selon le type ; « associations » est vague.

> ancien : e-3.3 Diagnostics selon le type moteur et les associations
>
> nouveau : e-3.3 Imagerie et comorbidités selon le type moteur

**P-51** (syntaxe) — Phrase nominale proscrite (STYLE_REDACTION § 2).

> ancien : <p>Quatre cas fictifs d’entraînement. Ils reposent uniquement sur les données du cours.</p>
>
> nouveau : <p>Ces quatre cas fictifs servent à l’entraînement. Ils reposent uniquement sur les données du cours.</p>

**P-52** (syntaxe) — Articles absents ; « si concordant » sans sujet.

> ancien : Compléter par HINE et IRM ; si concordant, poser le diagnostic
>
> nouveau : Compléter par l’HINE et l’IRM ; si les résultats concordent, poser le diagnostic

**P-53** (grammaire) — Articles absents dans l’énoncé du cas.

> ancien : présente confusion, hallucinations et hyperthermie 2 jours après
>
> nouveau : présente une confusion, des hallucinations et une hyperthermie 2 jours après

**P-54** (registre) — « Chercher la génétique » est familier et imprécis : on recherche une cause génétique.

> ancien : chercher la génétique si l’imagerie est normale
>
> nouveau : chercher une cause génétique si l’imagerie est normale

**P-55** (syntaxe) — Épilogue nominal remplacé par des phrases conjuguées ; mêmes conditions.

> ancien : Génétique en cascade (exome en trio) si imagerie normale ou évolution atypique ; radiographie de hanche pour toute PC, avec un seuil de migration de 40 %.
>
> nouveau : Le bilan génétique en cascade (exome en trio) se justifie si l’imagerie est normale ou l’évolution atypique ; la radiographie de hanche concerne toute PC, avec un seuil de migration de 40 %.

**P-56** (syntaxe) — « Prévenir de » signifie avertir : une lésion n’avertit pas ; elle annonce (prédit) une atteinte.

> ancien : Une lésion bilatérale prévient d’une atteinte plus sévère
>
> nouveau : Une lésion bilatérale annonce une atteinte plus sévère

**P-57** (cohérence) — Confusion terminologique : « dyskinétique » est le type ; les sous-types sont dystonique et choréo-athétosique (section 2.1).

> ancien : lorsque le sous-type dyskinétique est difficile à reconnaître
>
> nouveau : lorsque le sous-type, dystonique ou choréo-athétosique, est difficile à reconnaître

**P-58** (syntaxe) — Phrase tronquée (« et, avec … ») : coordination sans second terme.

> ancien : elle traite la spasticité focale et, avec un effet de 3 à 8 mois.
>
> nouveau : elle traite la spasticité focale, avec un effet de 3 à 8 mois.

**P-59** (syntaxe) — Épilogue nominal remplacé par des phrases conjuguées (le renvoi R-06 signale la nuance intrathécale).

> ancien : Baclofène : action générale sur la moelle ; toxine : action locale au muscle.
>
> nouveau : Le baclofène agit de façon générale sur la moelle ; la toxine agit localement sur le muscle.


### `chapters/G80/G80_d.html`

**P-60** (registre) — Une discipline ne traite pas un patient ; personnification évitée.

> ancien : la pharmacologie traite la spasticité, l’épilepsie et les complications
>
> nouveau : le traitement médicamenteux porte sur la spasticité, l’épilepsie et les complications

**P-61** (ambiguité) — « Elle » peut renvoyer à la spasticité focale ou à la toxine.

> ancien : relève de la toxine botulique, car elle agit au muscle injecté
>
> nouveau : relève de la toxine botulique, car cette dernière agit au muscle injecté

**P-62** (registre) — « Situation du baclofène » est impropre ; on parle d’indication.

> ancien : est la situation du baclofène intrathécal
>
> nouveau : est l’indication du baclofène intrathécal

**P-63** (syntaxe) — Épilogue nominal avec adjectifs substantivés ; phrase complète, mêmes correspondances.

> ancien : Toxine pour le focal, baclofène oral pour le diffus, baclofène intrathécal pour le sévère ;
>
> nouveau : La toxine convient à la spasticité focale, le baclofène oral à la spasticité diffuse et le baclofène intrathécal à la spasticité sévère ;

**P-64** (syntaxe) — « La plus faible » sans nom ni verbe ; formulation alignée sur le cas 1 du quiz (« la plus faible des deux limites »).

> ancien : 21 U/kg ou 840 U (bilatéral) ; la plus faible</td>
>
> nouveau : 21 U/kg ou 840 U (bilatéral) ; la plus faible des deux limites s’applique</td>

**P-65** (ambiguité) — Sujet de la sécurité non nommé : la phrase suit deux médicaments différents.

> ancien : La sécurité avant 4 ans n’est pas démontrée.
>
> nouveau : La sécurité du baclofène intrathécal avant 4 ans n’est pas démontrée.

**P-66** (syntaxe) — Épilogue nominal remplacé par des phrases conjuguées ; mêmes doses.

> ancien : Dysport®, unités non interchangeables ; baclofène oral progressif de 0,3 mg/kg/jour à 0,75–2 mg/kg/jour ; baclofène intrathécal : bolus test, puis entretien individualisé.
>
> nouveau : Les unités du Dysport® ne sont pas interchangeables. Le baclofène oral augmente progressivement de 0,3 mg/kg/jour à 0,75–2 mg/kg/jour. Le baclofène intrathécal commence par un bolus test, puis passe à un entretien individualisé.

**P-67** (syntaxe) — Épilogue nominal remplacé par une phrase complète ; énumération coordonnée.

> ancien : À éviter : les interventions « feu rouge », les cannabinoïdes sans preuve, la transposition des unités de toxine, l’arrêt brutal du baclofène.
>
> nouveau : Il faut éviter les interventions « feu rouge », les cannabinoïdes sans preuve, la transposition des unités de toxine et l’arrêt brutal du baclofène.


### `chapters/G80/G80_pop1.html`

**P-68** (typographie) — Titre étranger non identifié comme tel ; langue précisée et italique.

> ancien : La catégorie G80 « Infantile Zerebralparese » est dans le bloc G80–G83.
>
> nouveau : La catégorie G80, intitulée en allemand « <i>Infantile Zerebralparese</i> », appartient au bloc G80–G83.

**P-69** (grammaire) — Même correction que P-07 : MACS désigne une seule classification.

> ancien : Les sources citent les échelles MACS (fonction manuelle) et une échelle de communication
>
> nouveau : Les sources citent l’échelle MACS (fonction manuelle) et une échelle de communication

**P-70** (typographie) — Locution latine en italique.

> ancien : Variants de novo (variants ponctuels, SNV ;
>
> nouveau : Variants <i>de novo</i> (variants ponctuels, SNV ;

**P-71** (syntaxe) — La dysphagie n’est pas un risque : elle y expose.

> ancien : La dysphagie est un risque respiratoire et nutritionnel
>
> nouveau : La dysphagie expose à un risque respiratoire et nutritionnel


### `chapters/G80/G80_pop2.html`

**P-72** (ponctuation) — « Non » seul entre deux groupes nominaux sans conjonction : la coordination est rétablie.

> ancien : synthèse de preuves, non recommandation nationale suisse
>
> nouveau : synthèse de preuves et non recommandation nationale suisse

**P-73** (registre) — Participe « basé sur » sans sujet et sans verbe (anglicisme) ; espace insécable fine dans le nombre à cinq chiffres.

> ancien : Basé sur 36 institutions de 9 pays et plus de 10 000 patients.
>
> nouveau : Il repose sur 36 institutions de 9 pays et plus de 10 000 patients.


### `glossary/g80.py`

**P-74** (cohérence) — Il n’existe pas de « classification suisse » dans la leçon : la catégorie est celle de la CIM-10-GM employée en Suisse (section 1).

> ancien : de la classification suisse.</p>
>
> nouveau : de la CIM-10-GM utilisée en Suisse.</p>


## Renvois médicaux (non traités, à l’audit médical)

**R-01** — `chapters/G80/G80_a.html` — référence à un schéma inexistant

> Le schéma de la fenêtre <button class="w" data-k="g80-vulnerabilite">Fenêtres de vulnérabilité</button> résume cette correspondance.

La phrase annonce un « schéma » dans la fenêtre « Fenêtres de vulnérabilité » ; la fenêtre G80_pop1 (g80-vulnerabilite) ne contient que du texte. Deux corrections sont possibles (supprimer « schéma » ou produire la figure) ; la seconde modifie le contenu. L’expression « la fenêtre Fenêtres de vulnérabilité » est en outre redondante. À trancher par l’audit médical / l’intégration.

**R-02** — `chapters/G80/G80_c.html` — logique du critère de classement

> La classification <button class="w" data-k="g80-mrics">MRICS</button> répartit les images en cinq groupes selon le moment du développement où l’atteinte est survenue

La phrase dit que les cinq groupes sont répartis selon le moment de l’atteinte, mais seuls trois (A, B, C) correspondent à un moment ; D (divers) et E (normale) n’en ont pas. La même formulation figure dans la légende de la figure 1 (« Cinq groupes d’imagerie selon le moment de l’atteinte »). Toute reformulation précise un fait de classification : à trancher par l’audit médical.

**R-03** — `chapters/G80/G80_b.html` — niveaux radiculaires de la rhizotomie

> sectionne 50 à 75 % des fibres afférentes des racines lombaires et sacrées de la première racine lombaire à la première racine sacrée

La fourchette « de la première racine lombaire à la première racine sacrée » (également dans G80_pop2, g80-rhizotomie) est un fait chiffré anatomique que ce rôle n’a pas vérifié ; la reformulation locale proposée (P-30) ne la modifie pas. À vérifier dans la source primaire par l’audit médical.

**R-04** — `chapters/G80/G80_b.html` — portée de « réserve au nourrisson »

> Une <button class="w" data-k="g80-irm">IRM</button> est préférée à l’échographie transfontanellaire, que l’on réserve au nourrisson.

L’IRM étant aussi pratiquée chez le nourrisson (tableau 7.1 : « IRM à terme »), la proposition relative « que l’on réserve au nourrisson » ne dit pas ce qui distingue l’échographie ; la fenêtre G80_pop1 (g80-irm) écrit « peut être utilisée chez le nourrisson ». Toute précision (âge, situation) est un fait médical.

**R-05** — `chapters/G80/G80_b.html` — cohérence des dates de sources

> Consensus européen sur la toxine botulique : Heinen F et al., 2010 (résumé).

Le consensus est daté de 2009 dans le texte (section 9.2 ; G80_pop2 g80-consensus : « Consensus européen de 2009 », « Ancien (2009) ») et de 2010 dans les références. De même, la « synthèse de preuves de 2019 » (section 9.1, fenêtre « Synthèse feux tricolores de 2019 ») est référencée « Novak I et al., 2020 ». Il peut s’agir d’année de consensus et d’année de publication, mais le lecteur ne le sait pas : harmonisation à décider par l’audit médical après lecture des sources.

**R-06** — `chapters/G80/G80_c.html` — cohérence logique du « donc »

> Le baclofène agit sur la moelle et touche donc l’ensemble du corps

La phrase déduit une action sur « l’ensemble du corps » de l’action médullaire du baclofène, alors que la même phrase indique ensuite la voie intrathécale (doses en microgrammes), voie locale. La déduction est contestable ; toute reformulation modifie l’énoncé pharmacologique.

**R-07** — `chapters/G80/G80_c.html` — référent non introduit

> Les intervalles de surveillance du programme européen n’ont pas été lus.

« Le programme européen » n’a été défini nulle part dans la leçon (la fenêtre G80_pop1 g80-hanche écrit seulement « Les intervalles précis n’ont pas été lus »). Nommer le programme exige la source.

**R-08** — `chapters/G80/G80_d.html` — contenu d’une colonne intitulée « Maximum »

> Moyenne 276 µg/jour à 12 mois ; avant 12 ans : 24–1199 µg/jour

Dans le tableau des doses, la colonne « Maximum » du Liorésal intrathécal® contient une moyenne (276 µg/jour) et une plage (24–1199 µg/jour) qui ne sont pas des maxima ; la ligne du Dysport® membre supérieur laisse « Selon la fiche » en dose initiale et cible. Toute correction modifie des données posologiques.

**R-09** — `chapters/G80/G80_d.html` — cohérence de la séquence de bolus

> Pour le baclofène intrathécal, le patient non répondeur à un bolus de 100 µg est exclu du traitement.

Le tableau donne un bolus test de 25 µg chez l’enfant, la phrase suivante exclut le non-répondeur à 100 µg : la séquence d’escalade entre 25 et 100 µg n’est pas écrite. L’expliciter est un ajout de fond.

**R-10** — `chapters/G80/G80_c.html` — figure 3 : placement de la forme spastique

> <text x="480" y="115" font-size="16" font-weight="bold">Spastique</text>

Dans la figure 3, « Spastique » (tonus augmenté) est placé au-dessus de l’axe horizontal, donc dans la zone « Mouvement augmenté (hyperkinétique) », alors que le texte précédent dit seulement que le tonus est augmenté. Le placement relève de la figure, non de la rédaction ; à signaler à l’audit médical.

**R-11** — `chapters/G80/G80_pop1.html` — formulation de la politique des sources

> il est lu ici comme définition et non comme recommandation de conduite américaine

La proposition peut se lire « conduite américaine » (le rapport serait américain) ou « recommandation de conduite, [d’origine] américaine ». La phrase énonce une règle de sources du projet, non un fait médical ; la reformuler exige de connaître l’intention (le rapport de 2006 est présenté comme issu d’un atelier international).

**R-12** — `chapters/G80/G80_b.html` — cohérence des âges de confirmation

> (4) confirmation après 4 à 5 ans dans les registres.

Le cours donne tour à tour « souvent 4–5 ans » (section 0, P-01), « 5 ans » pour les registres avec « au moins 4 ans recommandés » (section 7.1) et « après 4 à 5 ans » (critères formels). Les formulations ne sont pas équivalentes (âge de la confirmation, durée d’observation) ; harmonisation à décider par l’audit médical.

**R-13** — `chapters/G80/G80_pop2.html` — graphie du nom commercial

> <div class="lab">Source</div><p>Informations professionnelles suisses du Liorésal® (janvier 2025) et du Liorésal intrathécal® (avril 2024).</p>

Le nom « Liorésal® » (avec accent) est employé dans toute la leçon. La graphie du nom commercial dans l’information professionnelle suisse n’a pas été vérifiée par ce rôle ; à contrôler dans le texte de la fiche (Swissmedic / compendium.ch).


## Observations

- Espaces insécables : les sept fichiers ne contiennent aucun U+00A0 ni U+202F (0 occurrence). On dénombre, avant tout traitement automatique, environ 20 occurrences d’espace simple avant « ; » dans G80_a, 28 dans G80_b, 32 dans G80_c, 21 dans G80_d, 36 dans G80_pop1, 46 dans G80_pop2 et 8 dans g80.py, ainsi que des espaces simples avant « : » ; la typographie française exige une espace insécable (fine avant « ; », « ! », « ? » ; forte avant « : ») et à l’intérieur des guillemets « » : non proposé en propositions locales (traitement global à décider par l’intégration ou par le moteur). Une seule proposition (P-73) applique l’espace fine insécable à un nombre de cinq chiffres.
- Nombres : « 3818 », « 6107 », « 1500 g », « 1400 µg » s’écrivent sans séparateur ; « 10 000 » (pop2) avec espace simple. Choix à harmoniser globalement (cf. observation ci-dessus).
- Phrases nominales et infinitifs dans les encadrés « Piège » et « Erreur fréquente » : douze encadrés (G80_a 2.3, 4.4, 6 ; G80_b 7.3 (deux), 8.1, 9.3 (deux) ; G80_c e-1 ; G80_d p-1, p-2, p-4) commencent par un infinitif sans sujet (« Réduire la PC… », « Chercher une cause unique… ») ; la règle STYLE_REDACTION § 2 les proscrit, mais la forme est homogène dans le corpus et son remplacement uniforme relève de l’intégration : non proposé cas par cas.
- Terminologie : « quadriplégique » (intitulé G80.0, titre officiel OFS) alterne avec « tétraplégie » / « tétra- » dans le texte courant ; « Paralysie cérébrale » (G80.0, G80.1, G80.3, G80.4, G80.9) alterne avec « Infirmité motrice cérébrale » (G80.2, G80.8, titre de la leçon) : les intitulés CIM sont ceux de l’OFS et ne sont pas modifiés.
- Emploi de « GMFCS IV–V », « en GMFCS V » sans « niveau » dans de nombreuses occurrences (G80_a, G80_b, G80_c, G80_d, pop) : raccourci cohérent dans la leçon, non proposé ; seules les occurrences où « GMFCS plus élevé » prête à confusion ont été corrigées (P-10, P-15).
- Pareto : le bouton « Loi de Pareto — Anamnèse et manifestations » (G80_a 5) ouvre la fenêtre intitulée « Pareto — Anamnèse et examen » (G80_pop2, couvrant g80-5 et g80-6) : les deux intitulés diffèrent ; l’harmonisation relève de l’intégration.
- Abréviations : build_medina.audit() renvoie {} sur les six fichiers HTML avant et après application simulée des propositions. Aucune proposition n’introduit de sigle nouveau.
- Graphie « l’HINE » (élision devant un sigle commençant par H) : employée dans toute la leçon, cohérente, non modifiée.

## Figures

Le contrôle a porté sur le texte des figures (légendes, étiquettes), pas sur leur provenance. La vérification de la provenance est transmise à l'audit MED.

- Figure 2 (G80_c.html, hanche centrée et hanche déplacée) : ORIGINE_INCONNUE (réserve). Seule figure anatomique dessinée (SVG, cercles et arcs) ; sa légende la dit « schéma didactique non à l’échelle ». Provenance et justesse anatomique à vérifier par l'audit MED ; remplacement par une image réelle sourcée (image-clo-finder) à envisager.
- Figures 1, 3, 4, 5 (SVG) : non évaluée par ce rôle (schémas non anatomiques d'après leur légende) (transmis à l'audit MED). Aucune provenance vérifiée ; le placement de « Spastique » dans la figure 3 est signalé en R-09.

## Lacunes

- Aucune vérification médicale n’a été faite : les renvois_medicaux signalent des formulations dont la correction changerait le fond ; ils ne sont ni confirmés ni infirmés.
- Aucun contrôle de rendu navigateur des propositions : l’application simulée a été faite en mémoire (alignement des balises, audit des abréviations), aucun fichier canonique n’est modifié.
- Aucune lecture des sources primaires citées dans la leçon : les écarts signalés sont établis par comparaison interne entre les sept fichiers.
- Aucun correcteur orthographique automatique (aspell, hunspell ou pyenchant) n’est disponible dans l’environnement : l’orthographe a été relue manuellement sur les sept fichiers ; une faute isolée a pu passer.
- Le manifeste fixe la base d’exécution à un SHA antérieur d’un merge ; la branche de travail repose sur la base indiquée dans la consigne ; les sept fichiers sont identiques aux empreintes du manifeste.

## Tableau de bord

| Indicateur | Valeur |
|---|---|
| Fichiers lus en entier | 7 / 7 |
| Empreintes conformes | oui |
| Propositions | 74 |
| Renvois médicaux | 13 |
| Unicité des « ancien » | 74 / 74 |
| Chevauchements | 0 |
| Abréviations non couvertes avant / après | 0 / 0 |
| Sources canoniques modifiées | 0 |

*Audit IA — revue distincte d'une validation médicale humaine ; aucune source canonique modifiée*
