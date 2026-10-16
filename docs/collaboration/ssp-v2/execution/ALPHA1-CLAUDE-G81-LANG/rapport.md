# Audit linguistique G81 — Hémiparésie et hémiplégie (S08)

Mission ALPHA1-CLAUDE-G81-LANG, tour 3, génération 1. Branche `claude/alpha1/g81-lang-g1`, base `103745ba` (le manifeste fixe `523832d9`, ancêtre de la base ; les sept fichiers de la leçon sont identiques entre les deux commits). Audit IA : revue distincte d'une validation médicale humaine ; aucune source canonique modifiée.

## Synthèse

Les sept fichiers de la leçon (quatre onglets, deux fenêtres, glossaire) ont été lus en entier ; leurs empreintes SHA-256 sont conformes au manifeste. Le français est globalement soigné et sobre ; les défauts relevés sont de cinq types :

- **des épilogues et des cellules rédigés en mots-clés** (« G81.0 = flasque », « Suivre par échelles, entretenir le mouvement, réinjecter… », « Spasticité = résistance… ») que le guide de rédaction proscrit ; ils sont remplacés par des phrases complètes de même contenu (37 propositions de syntaxe) ;
- **le mot « simulateur »**, qui désigne en français médical le patient qui feint un déficit, employé pour les imitateurs de l'AVC que la leçon appelle « pseudo-AVC » partout ailleurs (P-01, P-02, P-24, P-26, P-27, P-28, P-35) ;
- **des ambiguïtés de rattachement** : pronom « Elle » sans antécédent net, « on s'y oppose », « il ne la rend pas anodine », participe « agissant » rapporté à la tizanidine au lieu des acides aminés, relative « qui inhibe » entre le récepteur et le baclofène, « le test de marche de 6 minutes et le Berg pour l'équilibre » ;
- **des fautes de grammaire et de lexique** : « la dysphagie dépasse 50 % des AVC » (deux occurrences), « ce rapport donne 56 mg » pour un produit, « Sa conséquence est la pneumonie, la dénutrition et… » (sujet singulier pour trois conséquences), « chez l'AVC du réveil », « le patient décrit » pour la patiente de la vignette, « contre-indications hépatique » ;
- **des incohérences internes de forme** : « Réperfusion » pour « reperfusion », « le Babinski » pour « signe de Babinski », « Les trois avaient la même sensibilité » après quatre tests cités, BOTOX et Xeomin sans ® alors que Dysport® en porte un, lecture lettre à lettre erronée de l'abréviation SMNS dans le glossaire.

- **98 propositions locales** (`propositions.json`), chacune avec un `ancien` unique dans son fichier, `fond_inchange: true`, sans chevauchement ; application simulée en mémoire suivie de `build_medina.audit()` : aucune abréviation non couverte, mêmes balises, mêmes clés `data-k`, aucun chiffre perdu.
- **21 renvois médicaux** : formulations dont la correction créerait, retirerait ou nuancerait un fait (causalité, fréquence, chronologie, classification, comparaison implicite). Ils ne sont pas corrigés ici.

## Propositions par catégorie

| Catégorie | Nombre |
|---|---|
| syntaxe | 37 |
| grammaire | 12 |
| registre | 12 |
| ambiguïté | 11 |
| cohérence | 11 |
| terminologie | 5 |
| typographie | 3 |
| répétition | 2 |
| orthographe | 2 |
| précision | 2 |
| ponctuation | 1 |

## Propositions par fichier

| Fichier | Nombre |
|---|---|
| `chapters/G81/G81_a.html` | 25 |
| `chapters/G81/G81_b.html` | 28 |
| `chapters/G81/G81_c.html` | 16 |
| `chapters/G81/G81_d.html` | 20 |
| `chapters/G81/G81_pop1.html` | 2 |
| `chapters/G81/G81_pop2.html` | 5 |
| `glossary/g81.py` | 2 |

## Les trois constats les plus lourds

1. **Le mot « simulateur » désigne un patient qui feint, non un imitateur de l'AVC** (P-01, P-02, P-24, P-26, P-27, P-28, P-35) : sept occurrences dans le corps et les légendes de la leçon, dont la question qui structure tout le cours (« quelle est la part d'un simulateur ? »). Un lecteur d'examen y lira une question de simulation, non de diagnostic différentiel.
2. **« La dysphagie dépasse 50 % des AVC »** (P-21, P-38) et **« ce rapport donne environ 56 mg »** (P-42) : deux énoncés chiffrés dont la grammaire fait dire autre chose que ce qu'ils calculent. La correction touche le sujet de la phrase, jamais le chiffre.
3. **Phrases à lecture ambiguë où un pronom change le sens** : « mais il ne la rend pas anodine pour autant » (P-31, le doute rendrait la thrombolyse anodine) ; « agissant sur les récepteurs NMDA » rapporté à la tizanidine (P-67) ; « le test de marche de 6 minutes et le Berg pour l'équilibre » (P-23). Chaque correction retient la lecture que le reste de la leçon impose.

## Propositions qui exigent une relecture attentive avant intégration

Elles lèvent une ambiguïté en retenant la lecture que le contexte impose ; elles ne changent pas le fond selon cet audit, mais l'audit médical doit les confirmer : P-05 (« Cette lecture »), P-20 (énoncé du quiz), P-23 (domaine « marche »), P-25 (« quatre tests »), P-31 (thrombolyse non anodine), P-41 (« on s'oppose alors à la thrombolyse »), P-67 (NMDA entre parenthèses), P-68 (baclofène sujet de « inhibe »), P-92 (« les recommandations s'opposent »).

## Renvois médicaux (hors correction linguistique)

- **R-01** (classification, `G81_a.html`) : « Entité distincte du bloc. ». Le tableau place G83.5 (syndrome de verrouillage) parmi les codes « à ne pas confondre » avec le critère « Entité distincte du bloc », alors que la même section situe G83 dans le bloc G80–G83 et que le glossaire (g81.py) écrit « Code voisin de G81 dans le même bloc de la classification ». Le critère de distinction est donc contradictoire ou mal formulé. Le corriger suppose de choisir le fait de classification exact (par exemple une entité distincte de G81 au sein du bloc) : à trancher par l’audit médical.
- **R-02** (chronologie, `G81_a.html`) : « Le Babinski apparaît tôt ; la spasticité plus tard. ». La phrase précédente range le signe de Babinski parmi les signes positifs qui « viennent ensuite » (après les signes négatifs) ; la phrase ci-dessus le dit précoce, et la figure 1 l’oppose à une spasticité « plus tardive ». Le Babinski est donc à la fois « ensuite » et « tôt ». Reformuler la chronologie des signes positifs change le fond : à trancher par l’audit médical (P-10 ne corrige que la forme « le Babinski » → « le signe de Babinski »).
- **R-03** (précision, `G81_a.html`) : « Lésion‹/text›‹text x="68" y="52"›du neurone ». Dans la figure 1, la première boîte porte l’étiquette « Lésion du neurone », sans « moteur supérieur » : le neurone lésé n’est pas identifié, alors que le titre de la figure parle du « motoneurone supérieur ». Compléter l’étiquette précise la lésion en cause (lésion du motoneurone supérieur ou de la voie descendante) et modifie le schéma : à trancher par l’audit médical (contrainte de largeur de la boîte à vérifier au rendu).
- **R-04** (statistique/causalité, `G81_a.html`) : « multiplie le risque de spasticité (rapport de cotes, ». Un rapport de cotes de 6,57 n’est pas un multiplicateur du risque ; le glossaire (clé « OR ») et la fenêtre g81-prevalence le précisent (« ce n’est pas un risque absolu »). « Multiplie le risque » présente donc l’OR comme un risque relatif. La reformulation correcte (« multiplie les cotes ») ou l’abandon du verbe change l’énoncé statistique : à trancher par l’audit médical.
- **R-05** (causalité/définition, `G81_a.html`) : « La spasticité traduit un déséquilibre facilitation/inhibition, une plasticité de la moelle et une part mécanique du muscle qui se raccourcit. ». L’épilogue de la section 3 range la « part mécanique du muscle » parmi ce que « traduit » la spasticité. Or la sous-section 3.4 et la fenêtre g81-intrinseque présentent cette part comme une hypertonie non réflexe, distincte de la spasticité (qui est réflexe et dépendante de la vitesse). L’épilogue omet par ailleurs la plasticité cérébrale citée en 3.3 (« plasticité spinale et cérébrale »). Toute correction modifie l’énoncé physiopathologique : à trancher par l’audit médical.
- **R-06** (cohérence chiffrée, `G81_a.html`) : « Parésie sévère et AVC hémorragique : facteurs de risque de spasticité. ». L’épilogue de la section 4 parle de « parésie sévère », alors que le corps du texte (OR 6,57) et la fenêtre g81-prevalence parlent de « parésie modérée à sévère ». P-15 conserve volontairement « sévère » ; l’alignement sur « modérée à sévère » est une correction de fond (graduation de la parésie) : à trancher par l’audit médical.
- **R-07** (logique/conduite, `G81_a.html`) : « Un patient qui tousse en mangeant ou qui s’étouffe est un patient à dépister avant toute alimentation orale. ». La phrase est inexacte dans sa logique : un patient qui tousse en mangeant a déjà mangé ; le dépistage de la dysphagie est recommandé chez tous les patients avant toute alimentation orale (voir 8.2 et 9.2), non seulement chez ceux qui toussent. En outre « L’hémiparésie … masque parfois un trouble de la déglutition » attribue à l’hémiparésie un masquage dont le sujet réel est l’apparence « seulement faible » du patient. Reformuler change la conduite énoncée : à trancher par l’audit médical.
- **R-08** (comparaison implicite, `G81_a.html`) : « Les patients sont plus jeunes, plus souvent des femmes, avec moins de facteurs de risque vasculaire et des symptômes moins sévères. ». Les comparatifs (« plus jeunes », « moins sévères ») n’ont pas de terme de comparaison dans la phrase. Le terme est vraisemblablement « les patients ayant un AVC » (voir la fenêtre g81-mimics), mais l’expliciter revient à ajouter un fait de comparaison que la phrase ne porte pas : à confirmer par l’audit médical avant ajout.
- **R-09** (codage, `G81_a.html`) : « sans précision, ancienne ou de longue date avec une cause non précisée ». La règle d’usage du code primaire/supplémentaire est formulée de trois manières : ici « sans précision, ancienne ou de longue date avec une cause non précisée » (portée de « avec une cause non précisée » ambiguë : concerne-t-elle les trois cas ou le seul cas de longue date ?), dans l’épilogue de la section 1 (« la cause est inconnue ou ancienne »), et dans l’encadré de la section 12 (« la cause est non précisée ou ancienne »). Les trois énoncés ne sont pas équivalents (« inconnue » ≠ « non précisée »). Les harmoniser suppose de relire le texte du BfArM : à trancher par l’audit médical.
- **R-10** (registre/portée, `G81_a.html`) : « Le dossier de recherche ne distingue pas hémiparésie et hémiplégie ». Le mot « dossier » (36 occurrences dans les sept fichiers, dont « le dossier ne contient pas… », « ce dossier ») désigne la base de sources de fabrication du cours, vocabulaire interne que la règle d’annonce pédagogique proscrit (« aucune formule de chantier »). Le remplacer par « la classification » ou « la source » change l’objet de l’assertion (limite des sources lues versus propriété de la classification) : à trancher par l’audit médical, au cas par cas.
- **R-11** (absolu, `G81_b.html`) : « Ils agissent sur la part mécanique du muscle, que les médicaments n’atteignent pas. ». « Que les médicaments n’atteignent pas » est un énoncé absolu. La sous-section 3.4 dit que les médicaments agissent « surtout » sur la part réflexe, ce qui laisse une action partielle possible sur la part intrinsèque. Nuancer ou conserver l’absolu change le fond : à trancher par l’audit médical.
- **R-12** (contradiction chiffrée, `G81_b.html`) : « expliquent mal l’échec dans la majorité des situations ; l’immunogénicité n’est pas la cause la plus fréquente de non-réponse ». Le paragraphe affirme que les anticorps neutralisants « expliquent mal l’échec dans la majorité des situations » et ne sont « pas la cause la plus fréquente », alors que la section e-4 et la fenêtre g81-immuno donnent une sensibilité de 56 % pour expliquer une non-réponse secondaire (ils l’expliqueraient donc dans plus de la moitié des cas où elle survient). Les deux énoncés ne sont pas conciliables sans précision sur la population (1 % de tous les patients versus non-répondeurs secondaires). La phrase ne peut pas être réécrite sans trancher cette incohérence : à trancher par l’audit médical. Les deux propositions de la phrase sont en outre redondantes.
- **R-13** (fréquence, `G81_b.html`) : « sont les complications fréquentes. ». L’encadré d’urgence qualifie le risque de chute et la douleur de « complications fréquentes », alors que la section 5.2 précise que « le dossier ne donne aucune fréquence » des symptômes séquellaires ; le déterminant « les » suppose en outre une liste exhaustive. Remplacer « les complications fréquentes » par « des complications possibles » change le fond : à trancher par l’audit médical.
- **R-14** (fréquence, `G81_b.html`) : « traiter l’une soulage souvent l’autre ». « Souvent » quantifie un effet que la fenêtre g81-douleur énonce au mode du possible (« Traiter l’une peut soulager l’autre »). Remplacer par « peut soulager » est une correction de fréquence : à trancher par l’audit médical.
- **R-15** (comparaison implicite, `G81_b.html`) : « Thérapie de groupe spécifique non inférieure (équilibre, vitesse, endurance) ». « Non inférieure » n’a pas de terme de comparaison dans la cellule ; le libellé de la ligne (« Groupe ou individuel ») suggère « à la thérapie individuelle ». Expliciter ajoute un fait de comparaison : à confirmer par l’audit médical avant ajout.
- **R-16** (définition, `G81_b.html`) : « augmentation du tonus dépendante de la vitesse d’étirement ». L’encadré des critères formels résume la définition de Lance par « augmentation du tonus dépendante de la vitesse d’étirement », alors que la fenêtre g81-lance (reprise du texte de Trompetto 2014) la formule : « augmentation, dépendante de la vitesse, des réflexes toniques d’étirement ». « Tonus » et « réflexes toniques d’étirement » ne sont pas synonymes (voir 3.4 : le tonus comporte une part non réflexe). Harmoniser change la définition : à trancher par l’audit médical.
- **R-17** (omission, `G81_c.html`) : « la biologie vient ensuite ». Le paragraphe de lecture du tableau e-1 range « la biologie » entre l’imagerie et les échelles, alors que le tableau ne contient aucun examen biologique et que le dossier n’en documente aucun. L’affirmation est donc non sourcée ; la supprimer ou la sourcer change le fond : à trancher par l’audit médical.
- **R-18** (causalité, `G81_c.html`) : « d’où une amélioration en deux semaines et un effet maximal en quatre à six semaines ». Le connecteur « d’où » fait du relâchement local du muscle la cause du délai d’apparition de l’effet (2 semaines, puis 4 à 6 semaines). Cette causalité n’est pas portée par l’information professionnelle citée, qui donne seulement les délais. Le remplacer par « avec » est une correction de causalité : à trancher par l’audit médical.
- **R-19** (précaution, `G81_d.html`) : « rétention urinaire en cas d’hypertonie sphinctérienne ». La précaution « rétention urinaire en cas d’hypertonie sphinctérienne » est ambiguë : s’agit-il d’une rétention urinaire existante (par hypertonie du sphincter) qui impose la prudence, ou d’un risque de rétention en cas d’hypertonie ? La fenêtre g81-baclofene la réduit à « rétention urinaire ». Seule l’information professionnelle (Liorésal) permet de trancher : à trancher par l’audit médical.
- **R-20** (cohérence, `G81_d.html`) : « n’ont pas été lues en entier ». La section p-5 dit que les informations professionnelles de Dysport®, Xeomin et Liorésal intrathécal® « n’ont pas été lues en entier », alors que p-1, p-2 et les fenêtres g81-botox et g81-intrathecal disent « textes non lus » et « n’a pas été lu ». Lu partiellement ou non lu : état de lecture à consigner par l’audit médical, car il détermine la prudence du cours.
- **R-21** (cohérence, `G81_pop1.html`) : « niveau de preuve très faible ». La fenêtre g81-todd juge le niveau de preuve de la paralysie de Todd « très faible », la section 4 (G81_a) dit « faible » pour le même rapport de cas. Une seule graduation doit être retenue : à trancher par l’audit médical.

## Choix différés, non appliqués

- Espaces insécables globales (avant ; : ! ?, dans les guillemets « », dans les nombres) : non appliquées, ni proposées. Les sept fichiers ne contiennent aucun U+00A0 ni U+202F (442 occurrences d’une espace ordinaire avant ; : ! ? dans le texte des six fichiers HTML) ; la correction relève d’une passe mécanique unique, non d’un choix local.
- Harmonisation des plages de valeurs : tiret « - » (2018-2019, 2014-2022), demi-cadratin « – » (50–200 U, 4,5–9 h) et « à » / « et » coexistent ; choix éditorial différé.
- Écriture « Liorésal » avec ou sans ® (quiz et feedback de 9.4 sans ®, sections p-1 et p-4 avec ®) : harmonisation limitée à BOTOX® et Xeomin® (P-46, P-50, P-52, P-76, P-78, P-88, P-95 ; Dysport® et Liorésal intrathécal® portent déjà ®) ; le reste est différé.

## Observations

- Annonce pédagogique : « Ce cours poursuit cinq objectifs » (section 0) décrit le cours lui-même, ce que STYLE_REDACTION § 3 proscrit ; la remplacer exige de réécrire le paragraphe entier (changement de structure), non une formulation locale. Même remarque pour « Ce cours ne chiffre donc pas… », « Ce cours ne les détaille pas », « Ce cours retient la version… » et « Ce cours ne donne ni indication précise… » (fenêtre g81-intrathecal).
- Vocabulaire de fabrication : « le dossier » (36 occurrences), « sources lues », « lacune assumée », « résumé seul lu ». Ces tours portent un fait sur l’état de lecture des sources ; ils sont conservés (voir R-10).
- Anglicismes conservés : thumb rolling test, forearm rolling, index finger rolling, pronator drift (noms d’épreuves sans équivalent français établi dans la leçon), abstract (« l’abstract et la question PICO 3 »), « paquet de transfert » (calque de transfer package, section 9.3), Swiss Medical Forum. Leur remplacement exige un choix terminologique de l’audit médical.
- Listes « Pareto » et encadrés « Paramètres clés » : puces nominales et valeurs symboliques (≤, ×, +) conservées car elles résument des valeurs ; seules les phrases rédigées ont été reprises.
- Intervalle de réinjection exprimé en mois pour le membre supérieur (« 2 mois ») et en semaines pour le membre inférieur (« 12 semaines ») : unités différentes pour une comparaison immédiate ; fond non modifié.
- Libellé « Piège » (balise trap) employé pour des limites de sources (section 4, e-2, p-5) : intitulé de classe, non modifié.
- Le tableau du différentiel (7.1) répète le rang « 1 » pour deux hypothèses et classe « par gravité » une paralysie de Todd avant les pseudo-AVC sans critère de gravité explicite : choix de présentation à confirmer.

## Figures

Le contrôle a porté sur le texte des figures, pas sur leur provenance. Les deux figures de la leçon sont des schémas SVG non anatomiques. L'étiquette « Lésion du neurone » de la figure 1 est incomplète (R-03) ; la légende de la figure 2 est corrigée par P-27.

## Vérifications réalisées

- Empreintes SHA-256 des sept fichiers : conformes au manifeste.
- Unicité : `ancien.count(fichier) == 1` pour les 98 propositions, par script ; aucune paire de propositions ne se chevauche.
- Application simulée en mémoire sur une copie temporaire du dépôt : `build_medina.audit()` renvoie `{}` sur les six fichiers HTML avant et après ; le glossaire `g81.py` se charge après modification (lecture SMNS : S(yndrome du) M(oto)N(eurone) S(upérieur)).
- Mêmes comptes de balises et mêmes clés `data-k` avant et après ; aucun chiffre du texte n'est perdu.

## Lacunes

- Aucune vérification médicale n’a été faite : les renvois_medicaux signalent des formulations dont la correction changerait le fond ; ils ne sont ni confirmés ni infirmés.
- Aucune lecture des sources primaires citées : les écarts avec les sources sont établis seulement par comparaison interne entre les sept fichiers de la leçon.
- Aucun contrôle de rendu navigateur des propositions : l’application simulée a été faite en mémoire sur une copie temporaire ; aucun fichier canonique n’est modifié.
- Le choix « simulateur » → « pseudo-AVC » (P-01, P-02, P-24, P-26, P-27, P-28, P-35) repose sur le sens usuel de « simulateur » en français médical (patient qui feint) et sur le glossaire interne de la leçon (« pseudo-AVC (imitateurs de l’AVC) ») ; aucune ressource terminologique externe n’a été consultée.
- Les 98 propositions sont jugées « fond inchangé » par comparaison avec le reste de la leçon ; quelques-unes aident à lever une ambiguïté en retenant la lecture que le contexte impose (P-05, P-20, P-23, P-25, P-31, P-41, P-67, P-68, P-92) : l’auditeur médical doit les relire avant intégration.

## Tableau de bord

| Indicateur | Valeur |
|---|---|
| Fichiers lus en entier | 7 / 7 |
| Empreintes conformes au manifeste | oui |
| Propositions locales | 98 |
| Renvois médicaux | 21 |
| Propositions à relecture attentive | 9 |
| Abréviations non couvertes après application | 0 |
| Faits, chiffres, doses ou sources modifiés | 0 (selon cet audit) |
| Fichiers canoniques modifiés | 0 |

Audit IA — revue distincte d'une validation médicale humaine ; aucune source canonique modifiée.
