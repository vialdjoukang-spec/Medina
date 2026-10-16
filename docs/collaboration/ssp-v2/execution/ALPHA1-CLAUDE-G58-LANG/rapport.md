# Audit linguistique agressif — G58, « Autres mononévrites » (S08)

Mission ALPHA1-CLAUDE-G58-LANG · génération 1 · branche `claude/alpha1/g58-lang-g1` · base 32416a20.

> Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.

## Synthèse

Les sept fichiers de la leçon ont été lus en entier ; leurs empreintes SHA-256 correspondent au manifeste. L’audit propose **78 reformulations locales** qui ne changent ni un fait, ni un chiffre, ni une dose, ni une source, et signale **36 renvois médicaux** : des formulations qui créent une causalité, une fréquence ou une chronologie que les fichiers ne démontrent pas par eux-mêmes. Rien n’a été appliqué dans `chapters/` ni dans `glossary/`.

| Catégorie | Propositions |
|---|---|
| style_nominal | 17 |
| ambiguite | 12 |
| registre | 9 |
| style_infinitif | 9 |
| coherence_terminologique | 8 |
| grammaire | 6 |
| syntaxe | 4 |
| lourdeur | 3 |
| orthographe | 3 |
| lexique | 2 |
| style_passif | 2 |
| style_meta | 1 |
| accord | 1 |
| typographie_nombres | 1 |

| Fichier | Propositions |
|---|---|
| G58_b.html | 23 |
| G58_pop2.html | 20 |
| G58_c.html | 16 |
| G58_pop1.html | 7 |
| G58_a.html | 6 |
| G58_d.html | 5 |
| g58.py | 1 |

## Erreurs franches (orthographe et grammaire)

- **G58-LANG-P15** (G58_b.html) : « Cette liste découle de Blaes (2015) et de Ruffer et coll. (2024), complétées par des cas et séries » → « Cette liste s’appuie sur Blaes (2015) et sur Ruffer et coll. (2024), complétée par des cas et des séries ». Accord : le participe « complétée » se rapporte à « liste » ; « découler » remplacé par « s’appuyer sur ».
- **G58-LANG-P27** (G58_b.html) : « débuter prégabaline, gabapentine, duloxétine ou amitriptyline » → « débuter la prégabaline, la gabapentine, la duloxétine ou l’amitriptyline ». Articles manquants devant les noms de médicaments.
- **G58-LANG-P29** (G58_b.html) : « surveillance des médicaments reconnus comme inducteurs, traitement des infections virales, et prévention de la » → « la surveillance des médicaments reconnus comme inducteurs, le traitement des infections virales et la préventi ». Articles manquants dans une énumération ; virgule superflue devant « et ».
- **G58-LANG-P30** (G58_c.html) : « <th>Ce qu’il oriente</th> » → « <th>Orientation diagnostique</th> ». « Orienter » est transitif indirect ; « ce qu’il oriente » est incorrect.
- **G58-LANG-P31** (G58_c.html) : « décrivent ce que chaque résultat oriente. » → « décrivent l’orientation que donne chaque résultat. ». « Orienter » est transitif indirect (orienter vers).
- **G58-LANG-P32** (G58_c.html) : « ANCA</button> oriennent le diagnostic » → « ANCA</button> orientent le diagnostic ». Faute d’orthographe : « orientent ».
- **G58-LANG-P55** (G58_pop1.html) : « Une perte de jusqu’à 40 % du volume herniaire » → « Une perte de volume herniaire pouvant atteindre 40 % ». « Une perte de jusqu’à » est incorrect.
- **G58-LANG-P58** (G58_pop2.html) : « data-title="Aide mémoire des arguments contre la NSVN" » → « data-title="Aide-mémoire des arguments contre la NSVN" ». Orthographe : « aide-mémoire » prend un trait d’union.
- **G58-LANG-P60** (G58_pop2.html) : « La cible EULAR 2022 est 5 mg/j en 4 à 5 mois. » → « La cible EULAR 2022 est de 5 mg/j en 4 à 5 mois. ». Préposition manquante.
- **G58-LANG-P78** (g58.py) : « 'Aide mémoire O-A-C-V' » → « 'Aide-mémoire O-A-C-V' ». Orthographe : « aide-mémoire » prend un trait d’union.

## Syntaxe, ambiguïtés et lourdeurs

- **G58-LANG-P02** (G58_a.html) : Construction impropre : on prouve l’atteinte d’un nerf, non « le nerf atteint ».
- **G58-LANG-P03** (G58_a.html) : Formule passive et lourde ; la lecture du tableau est annoncée directement (guide § 4).
- **G58-LANG-P04** (G58_a.html) : « Découler » exprime une conséquence logique ; un tableau s’appuie sur des sources. Même formulation que dans l’onglet Examens.
- **G58-LANG-P05** (G58_a.html) : Ambiguïté : « tableau » désigne ici l’ensemble des données cliniques, non le tableau de la page.
- **G58-LANG-P06** (G58_a.html) : Pronom « Il » ambigu (société ou degré de certitude) ; sujet explicité.
- **G58-LANG-P07** (G58_b.html) : Construction « ne… que aux » lourde ; « que dans les troncs » est plus naturel.
- **G58-LANG-P10** (G58_b.html) : « Soutenue » est ambigu (la neuropathie ? le syndrome ?) ; l’onglet Examens écrit que le test « aide à reconnaître » le piégeage.
- **G58-LANG-P11** (G58_b.html) : « Ton » est impropre pour qualifier une douleur ; « caractère » est le terme sémiologique.
- **G58-LANG-P12** (G58_b.html) : Registre : une électrophysiologie ne « dit » pas ; elle ne permet pas d’affirmer.
- **G58-LANG-P13** (G58_b.html) : « Cacher un traitement » est incorrect : c’est une cause qui se cache derrière la présentation.
- **G58-LANG-P14** (G58_b.html) : Dénominateur du pourcentage ambigu ; formulation alignée sur la fenêtre « Cryoglobulinémie et hépatite C », qui donne la même information.
- **G58-LANG-P16** (G58_b.html) : Coordination fautive de « ce que » et de « dont » ; deux propositions distinctes.
- **G58-LANG-P17** (G58_b.html) : Ambiguïté de « rare, surtout dans » (rare surtout dans la GPA ?). Le sens médical reste celui de la phrase d’origine.
- **G58-LANG-P18** (G58_b.html) : Trois pourcentages mal articulés dans une même phrase ; parenthèse et conjonction. Chiffres inchangés.
- **G58-LANG-P21** (G58_b.html) : Adjectif substantivé familier ; terme complet.
- **G58-LANG-P23** (G58_b.html) : Énumération ambiguë (cystite et stérilité rattachées à la corticothérapie ?) ; « du cyclophosphamide » précisé en « dues au ».
- **G58-LANG-P25** (G58_b.html) : Registre : « sauver » est figuré ; le guide proscrit les images.
- **G58-LANG-P26** (G58_b.html) : Coordination ambiguë : « pour réduire… les échanges plasmatiques » se lit comme si l’avacopan réduisait les échanges plasmatiques.
- **G58-LANG-P33** (G58_c.html) : Expression imprécise : « preuve de routine ».
- **G58-LANG-P34** (G58_c.html) : « Découler » exprime une conséquence logique, non une source.
- **G58-LANG-P35** (G58_c.html) : « Y » ambigu et « liés » vague ; l’antécédent est explicité.
- **G58-LANG-P38** (G58_c.html) : Antécédent de « qui » ambigu (voussure, douleur, radiculopathie) ; l’onglet Pathologie attribue la résolution à la radiculopathie.
- **G58-LANG-P39** (G58_c.html) : « Dose prolongée » est impropre : c’est la durée de traitement qui est prolongée.
- **G58-LANG-P46** (G58_d.html) : Registre : « éteindre » est une image ; le guide proscrit les métaphores.
- **G58-LANG-P47** (G58_d.html) : « Plus » seul est ambigu ; la fenêtre sur la prednisone écrit « davantage à court terme ».
- **G58-LANG-P49** (G58_d.html) : « Vidanges » seul est ambigu ; précision de l’organe.
- **G58-LANG-P52** (G58_pop1.html) : Tournure « est un imitateur » lourde.
- **G58-LANG-P54** (G58_pop1.html) : Verbe pronominal impropre (« se présentent comme »).
- **G58-LANG-P56** (G58_pop1.html) : « Sous traitement » est vague et se répète avec « un traitement rapide » ; l’agent est celui de la fenêtre.
- **G58-LANG-P59** (G58_pop2.html) : Tournure « est une alternative » lourde.

## Cohérence terminologique et nombres

- **G58-LANG-P08** (G58_b.html) : « au tiers proximal-moyen du nerf : c’est là » → « au tiers proximo-moyen du nerf : c’est là ».
- **G58-LANG-P09** (G58_b.html) : « produisent une mononeuropathie multiple ischémique » → « produisent une mononévrite multiple ischémique ».
- **G58-LANG-P22** (G58_b.html) : « parce que les déficits finissent par se rejoindre » → « parce que les déficits finissent par se chevaucher ».
- **G58-LANG-P36** (G58_c.html) : « se concentrent au tiers proximal-moyen du nerf » → « se concentrent au tiers proximo-moyen du nerf ».
- **G58-LANG-P37** (G58_c.html) : « Tiers proximal-moyen : zone frontière » → « Tiers proximo-moyen : zone frontière ».
- **G58-LANG-P48** (G58_d.html) : « la tension, le poids et le potassium » → « la tension, le poids et la kaliémie ».
- **G58-LANG-P51** (G58_pop1.html) : « peut causer une mononeuropathie multiple ischémique » → « peut causer une mononévrite multiple ischémique ».
- **G58-LANG-P53** (G58_pop1.html) : « au tiers proximal-moyen du nerf, où survient » → « au tiers proximo-moyen du nerf, où survient ».
- **G58-LANG-P57** (G58_pop1.html) : « (environ 1 patient sur 5 réussit sous radiofréquence pulsée, environ 2 sur 3 après neurect » → « (environ un patient sur cinq réussit sous radiofréquence pulsée, environ deux sur trois ap ».

## Style imposé par le guide de rédaction (phrases nominales, infinitifs, passifs, méta-discours)

Le guide (§ 2) proscrit la phrase nominale et l’infinitif injonctif partout, y compris dans les encadrés, les fenêtres et les Pareto. Les propositions de cette catégorie (29) réécrivent en phrases complètes sans ajouter d’information ; les doses et les chiffres sont recopiés tels quels.


## Renvois médicaux (non reformulés)

Chaque renvoi cite un extrait exact et explique pourquoi une reformulation locale risquerait de changer le sens médical.

- **G58-LANG-RM01** [ambiguite_de_sens] (G58_a.html) : « sans attendre un schéma complet » — « Schéma complet » peut désigner un tableau clinique, un bilan ou un protocole thérapeutique ; la reformulation exige de savoir lequel. Aucune modification proposée.
- **G58-LANG-RM02** [frequence] (G58_a.html) : « soulager une douleur neuropathique souvent longue » — « Souvent longue » est une fréquence/durée que la section Fréquence ne chiffre pas pour la névralgie intercostale (seule la douleur chronique postopératoire est chiffrée).
- **G58-LANG-RM03** [causalite] (G58_a.html) : « parce qu’un retard de traitement expose à des déficits permanents et au décès » — Relation causale retard → déficits permanents et décès, reprise dans l’encadré d’urgence ; aucune source citée à cet endroit ne la chiffre ni ne l’établit pour la mononévrite multiple.
- **G58-LANG-RM04** [ambiguite_de_sens] (G58_a.html) : « jusqu’à 80 % des fractures de côtes traumatiques sont concernées » — Le complément de « concernées » (par une atteinte nerveuse ? une douleur ?) manque ; la reformulation changerait la nature du fait rapporté.
- **G58-LANG-RM05** [frequence] (G58_a.html) : « le retard est la règle » — Généralisation tirée d’une moyenne de « environ cinq médecins avant le diagnostic » ; « la règle » affirme une fréquence que la source ne donne pas.
- **G58-LANG-RM06** [portee_source] (G58_a.html) : « la sensibilité de la paroi inflammatoire est faible » — Formulation imprécise (sensibilité de quoi : de la biopsie ? de la détection d’une inflammation de paroi ?), reprise dans les onglets Examens et dans la fenêtre « Biopsie nerf et muscle ». Une reformulation locale choisirait un sens médical.
- **G58-LANG-RM07** [causalite] (G58_b.html) : « le déficit observé à l’examen reflète donc une lésion localisée » — Inférence « donc » : de la zone frontière de perte axonale au déficit segmentaire ; la source (autopsie de huit cas) ne la formule pas telle quelle.
- **G58-LANG-RM08** [chronologie] (G58_b.html) : « le tableau évolue vers une polyneuropathie sensitivomotrice axonale » — Évolution temporelle (« quand les territoires se chevauchent, le tableau évolue vers ») attribuée à un résumé ; reprise dans la fenêtre « Mononévrite multiple » et dans la Physiologie (« À mesure que… le tableau devient »).
- **G58-LANG-RM09** [causalite] (G58_b.html) : « relève d’une microvascularite sans lien avec la sévérité du diabète » — Mécanisme (microvascularite) et absence de lien avec la sévérité énoncés sans citation à cet endroit.
- **G58-LANG-RM10** [causalite] (G58_b.html) : « explique son ton (brûlure, éclair), sa persistance après la cicatrisation et la réponse aux molécules ciblant la douleur » — Triple relation causale (nature neuropathique → caractère, persistance, réponse thérapeutique) sans source dédiée.
- **G58-LANG-RM11** [frequence] (G58_b.html) : « Anticorps anti-Hu (plus de 90 % avec un cancer bronchique à petites cellules) » — Dénominateur ambigu (90 % des patients anti-Hu ? des cancers ?) ; la lecture correcte relève du médical.
- **G58-LANG-RM12** [frequence] (G58_b.html) : « Viennent ensuite la fracture de côte » — L’ordre de fréquence des causes après la thoracotomie et le zona (« viennent ensuite ») n’est pas donné par la fenêtre « Névralgie intercostale », qui ne hiérarchise que les deux premières.
- **G58-LANG-RM13** [chronologie] (G58_b.html) : « puis s’étend par paliers à d’autres nerfs » — Chronologie « débute de façon aiguë à subaiguë… puis s’étend par paliers » ; la source de cette séquence n’est pas citée à cet endroit.
- **G58-LANG-RM14** [causalite] (G58_b.html) : « Le mécanisme est mécanique : tout mouvement qui étire ou comprime le nerf réveille la douleur. » — Tautologie de forme (« mécanisme mécanique ») et affirmation causale universelle (« tout mouvement ») ; la reformulation toucherait au mécanisme.
- **G58-LANG-RM15** [terminologie_medicale] (G58_b.html) : « (signe de Tinel) » — Le signe de Tinel est cité pour une douleur reproduite « par la palpation » ; l’emploi du terme et son geste (percussion ou palpation) relèvent de l’audit médical.
- **G58-LANG-RM16** [coherence_medicale] (G58_b.html) : « une douleur à l’inclinaison latérale du côté atteint évoque une atteinte pariétale » — « Du côté atteint » (onglet Pathologie) et « du côté de l’inclinaison » (fenêtre) ne désignent pas la même chose ; le quiz parle de Schepelmann « homolatéral ». Le sens du signe doit être tranché sur source avant toute reformulation.
- **G58-LANG-RM17** [causalite] (G58_b.html) : « car un traitement rapide est nécessaire » — Recommandation d’urgence tirée d’un cas rapporté (résumé) ; reprise dans la fenêtre « Neuropathie sous inhibiteur de point de contrôle ».
- **G58-LANG-RM18** [causalite] (G58_b.html) : « peut rendre la preuve histologique plus difficile » — Effet de la corticothérapie préalable sur le rendement de la biopsie : relation non sourcée dans le texte.
- **G58-LANG-RM19** [portee_source] (G58_b.html) : « (diverses conditions) » — La parenthèse peut se rapporter au seul groupe « tramadol et opioïdes » ou à tous les médicaments cités ; le niveau A d’EFNS dépend des conditions. Reformulation impossible sans la source.
- **G58-LANG-RM20** [portee_source] (G58_b.html) : « à long terme, environ un patient sur cinq réussit sous radiofréquence pulsée » — « Réussit » n’est pas défini (soulagement ? durée ? seuil ?) ; reprise dans la fenêtre « ACNES ». Un verbe plus précis choisirait un critère de succès.
- **G58-LANG-RM21** [chronologie] (G58_b.html) : « la radiculopathie diabétique thoracique se résout complètement en 3 à 12 mois » — Durée de résolution complète présentée comme une règle ; reprise dans la Physiologie. De même « amélioration spontanée fréquente » pour les hernies discales thoraciques (fenêtre « Hernie discale thoracique »).
- **G58-LANG-RM22** [causalite] (G58_b.html) : « justifie une information préopératoire » — Recommandation de prévention déduite d’une fréquence (38 % à 12 mois) ; la source ne formule pas cette recommandation.
- **G58-LANG-RM23** [causalite] (G58_c.html) : « ce qui explique les séries où la vascularite n’est que probable ou possible » — Relation causale entre la faible sensibilité de la biopsie et les séries à certitude limitée ; non établie par une source citée.
- **G58-LANG-RM24** [portee_source] (G58_c.html) : « La corrélation avec les neurofilaments est à lire avec prudence » — « Corrélation » introduit un terme statistique que le texte n’a pas défini ; les neurofilaments sont ailleurs décrits comme « marqueur possible d’activité ».
- **G58-LANG-RM25** [coherence_medicale] (G58_c.html) : « La biopsie transforme la suspicion en preuve. » — Formule en tension avec la limite de sensibilité et avec les niveaux « probable » et « possible » ; atténuer la phrase relève du médical.
- **G58-LANG-RM26** [causalite] (G58_c.html) : « La localisation d’une atteinte explique pourquoi le déficit suit un territoire nerveux précis et pourquoi la cause se ch » — Deux relations « explique pourquoi » dont la seconde (cause cherchée dans la vascularisation) n’est pas évidente pour toutes les causes du chapitre (infection, médicament, compression).
- **G58-LANG-RM27** [causalite] (G58_c.html) : « <b>Anatomie → clinique.</b> Vasa nervorum de 50–300 µm et zone frontière expliquent les déficits asymétriques par nerf. » — Lien causal entre calibre des vaisseaux, zone frontière et asymétrie des déficits ; « les nerfs… que l’on teste d’abord » est aussi une chronologie d’examen non sourcée.
- **G58-LANG-RM28** [causalite] (G58_c.html) : « vient de la lésion des fibres sensitives elles-mêmes » — Origine de la douleur neuropathique affirmée sans source ; reprise pour l’effet déclenchant de l’inspiration, de la toux et de la rotation (« ce qui explique leur effet déclenchant »).
- **G58-LANG-RM29** [portee_source] (G58_c.html) : « suppriment l’axe surrénalien » — Intensité (« suppriment » plutôt que « freinent ») dépendante de la notice suisse de la prednisone, non reprise ici.
- **G58-LANG-RM30** [coherence_medicale] (G58_d.html) : « interdits chez l’enfant » — « Interdits » contredit « non recommandés avant 18 ans » (Pathologie et fenêtres) ; le statut réglementaire exact exige l’information professionnelle.
- **G58-LANG-RM31** [indication] (G58_pop2.html) : « l’usage dans la mononévrite vasculitique relève des lignes directrices EFNS et de revues » — Le texte ne dit pas que cet usage est hors des indications autorisées par l’information professionnelle (neuropathie diabétique, névralgie postherpétique) ; la mention « hors indication » relève de l’audit médical.
- **G58-LANG-RM32** [structure] (G58_pop2.html) : « <p>Syndrome DRESS signalé ; non recommandée avant 18 ans.</p> » — Dans la rubrique « Effets indésirables », la mention « non recommandée avant 18 ans » n’est pas un effet indésirable ; son déplacement dépasse la formulation locale.
- **G58-LANG-RM33** [causalite] (G58_pop1.html) : « Cette notion explique qu’une atteinte vasculaire touche des nerfs un à un et laisse d’autres nerfs indemnes » — Relation causale zone frontière/vasa nervorum → atteinte nerf par nerf ; non établie par une source citée.
- **G58-LANG-RM34** [chronologie] (G58_pop1.html) : « arrête ou remplace l’agent suspect avant d’attribuer la neuropathie à une maladie systémique » — Séquence de conduite (arrêt avant attribution) sans source ; la reformulation changerait l’ordre des actes.
- **G58-LANG-RM35** [frequence] (G58_pop2.html) : « Dans la neuropathie des vascularites à ANCA, les protéines et les cellules sont habituellement normales. » — « Habituellement » est une fréquence que la source (revue) ne chiffre pas ; l’onglet Examens écrit « généralement ».
- **G58-LANG-RM36** [portee_source] (g58.py) : « Mesure de l’inflammation. » — La VS est un marqueur indirect de l’inflammation ; la définition « mesure de l’inflammation » est imprécise, mais sa correction relève du médical.

## Choix différés (non appliqués)

- Espaces insécables globales avant « ; : ! ? » et dans « 50 % » : Choix différé par le coordinateur ; non appliqué, non compté dans les propositions.
- « fibrillation atriale » / « fibrillation auriculaire » : Choix différé par le coordinateur ; non appliqué. Aucune occurrence de ce couple n’a été relevée dans G58.

## Lacunes

- Sixième sous-onglet (Sémiologie) : l’onglet Sciences compte quatre disciplines (Anatomie, Histologie, Physiologie, Biochimie) et aucun bouton Sémiologie ; constat relevant de l’audit médical, non traité en mission linguistique.
- Abréviations sans clé de glossaire repérées par balayage automatique des fichiers : « MPO-ANCA » (composé, utilisé avant toute définition ; la clé « MPO » existe ailleurs) et « E10–E14 » (code CIM de la fenêtre g58-cim). Aucune modification de glossaire proposée au-delà de l’orthographe (« aide-mémoire »). Le balayage est automatique : un oubli reste possible.
- Listes nominales des cartes (onglet Pathologie, « Symptômes », « Antécédents », « Examen neurologique », « Signes extra-neurologiques ») et énumérations de causes dans la fenêtre « Névralgie intercostale » : non réécrites ; la réécriture en phrases complètes dépasse une reformulation locale. Les paragraphes télégraphiques des fenêtres médicament ont été traités pour la prégabaline, la gabapentine, la prednisone et le cyclophosphamide ; ceux du rituximab, du mépolizumab, de l’EULAR et des fenêtres Pareto d’anatomie, d’histologie, de physiologie, de biochimie et d’examens restent en l’état.
- Lisibilité des figures 1 à 6 (viewBox de 380 de large, police de 14) : non mesurée par rendu. Plusieurs libellés dépassent 50 caractères (par exemple « Électrophysiologie : amplitude réduite, vitesse conservée ») et pourraient déborder des cadres de 356 unités ; à vérifier au rendu.
- Aucune vérification médicale n’a été faite ; aucune source externe n’a été consultée. Les renvois médicaux signalent seulement ce que les fichiers ne démontrent pas par eux-mêmes.
- Divergence de base : la consigne cite la base 32416a20, le manifeste indique la base d1a488ad. Le worktree est bien sur 32416a20 et les sept empreintes SHA-256 correspondent au manifeste.

## Tableau de bord

| Indicateur | Valeur |
|---|---|
| Fichiers lus | 7 sur 7 |
| Empreintes conformes au manifeste | oui |
| Propositions | 78 |
| Renvois médicaux | 36 |
| Extraits « ancien » uniques dans leur fichier | 78 sur 78 |
| Écritures hors du dossier réservé | 0 |
