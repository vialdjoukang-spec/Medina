# Audit linguistique agressif de E11 — Diabète sucré de type 2

Mission ALPHA1-CLAUDE-E11-LANG, génération 1, branche `claude/alpha1/e11-lang-g1`, base `f664dd9e`. Audit de formulation locale : aucun fait, chiffre, dose ou source n’a été changé. *Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.*

## Tableau de bord

| Indicateur | Valeur |
|---|---|
| Fichiers lus en entier | 7 sur 7, empreintes SHA-256 conformes au manifeste |
| Propositions locales (`propositions.json`) | **302** (chacune : extrait « ancien » unique dans son fichier, vérifié par script) |
| Renvois (`renvois.json`) | **19** (dont 13 renvois médicaux, 6 renvois d’intégration) |
| Répartition par fichier | E11_a.html : 13 ; E11_b.html : 19 ; E11_c.html : 21 ; E11_d.html : 11 ; E11_pop1.html : 56 ; E11_pop2.html : 174 ; e11.py : 8 |
| Audit d’abréviations du moteur | `{}` avant et après application simulée |
| Structure HTML après application | nombre de balises identique, `glossary/e11.py` compile |
| Espaces insécables dans la leçon | 0 (voir constat C-03) |

Répartition des propositions par catégorie : phrase_nominale_lien (54), phrase_nominale (34), accord_nombre (25), article_manquant (24), meta_discours (20), syntaxe (19), lexique (18), ambiguite (17), ponctuation (16), grammaire (13), infinitif_injonctif (12), lourdeur (9), repetition (8), unite (8), terminologie (6), typographie (3), registre (3), orthographe (3), intitule (3), accord (2), accord_nombre+phrase_nominale_lien (2), accord_nombre+repetition (1), infinitif_injonctif+phrase_nominale_lien (1), abreviation (1).

## Constats classés par importance

### Importance haute

**C-01 — Intitulés des fenêtres (data-title), E11_pop2.html.** Trois intitulés de fenêtres sont agrammaticaux : « Cholestérol Lipoprotéines de faible densité », « Agonistes du récepteur du Peptide de type glucagon 1 », « Inhibiteurs de la Enzyme de dégradation des incrétines ». Ils résultent d’une substitution mécanique d’un sigle par sa définition de glossaire. Quatre autres titres contredisent le corps de leur fenêtre (Peptide / Polypeptide insulinotrope, apparenté / de type glucagon 1, faible / basse densité, Index / Indice).

**C-02 — Syntaxe : agent ou objet impropre.** Plusieurs phrases attribuent l’action au mauvais sujet ou confondent enzyme et médicament : « la DPP-4 s’arrête avant l’agoniste » (c’est l’inhibiteur qui s’arrête), « la SSED contrôle la glycémie », « la SSED évite ces produits », « la grossesse n’autorise l’usage », « multiplier par dix passe des milligrammes… », « une dose multiplie une quantité », « Quel est l’examen prioritaire ? » suivi d’une réponse à quatre examens. Le lecteur doit deviner le sens.

**C-03 — Toute la leçon (typographie française).** Aucune espace insécable dans les sept fichiers : les espaces avant « ; », « : », « ? », « % », à l’intérieur des « » et entre un nombre et son unité sont des espaces ordinaires (voir le détail chiffré). Une coupure de ligne peut donc isoler « % », « mmol/L » ou « ; » en début de ligne. Les chiffres de cinq signes ou plus (« 10 251 », « 100 000 ») sont aussi séparés par une espace ordinaire. Le même constat vaut pour tout le corpus (vérifié sur les 207 fichiers _a du dépôt : zéro espace insécable).

*Recommandation :* Traitement global et mécanique par le moteur (transformation à l’affichage) ou par un script d’intégration ; non transcrit en propositions locales car il concerne près de 2000 occurrences et n’a pas d’« ancien » unique.

Décompte : 822 « ; » précédés d’une espace ordinaire, 536 « : », 28 « ? », 182 « % », 48 guillemets « » à espaces ordinaires, 400 nombres suivis d’une unité par une espace ordinaire, 5 nombres de cinq chiffres ou plus à espace ordinaire.

**C-10 — Renvois.** 19 points ne sont pas reformulés parce que la formulation actuelle masque une ambiguïté médicale ou parce que l’intervention dépasse une phrase (voir renvois.json) : 13 renvois médicaux, 6 renvois d’intégration.

### Importance moyenne

**C-04 — Phrases nominales (STYLE_REDACTION § 2).** 54 paragraphes sont réduits à un lien nominal (« Valeurs de référence suisses, conditions… ») et 34 autres passages sont des fragments sans verbe (résultats d’essais, consignes de dose, listes de conditions). Les propositions rétablissent un sujet et un verbe sans changer un chiffre.

**C-05 — Articles manquants et infinitifs injonctifs.** 24 énumérations sans articles (« Devant nausées, vomissements, douleur… ») et 12 infinitifs injonctifs (étapes de calcul, consignes de lecture) contreviennent à STYLE_REDACTION § 2.

**C-06 — Méta-discours.** 20 passages parlent de la fabrication du cours (« ce cours ne donne ni… », « le cours retient », « dans ce cours »), tournure proscrite par STYLE_REDACTION § 3 pour les annonces. Les trois bandeaux « Les vignettes et cas de ce cours sont fictifs » ont été laissés en l’état : ils remplissent une fonction d’avertissement.

**C-07 — Barres obliques et unités.** 16 barres obliques entre deux mots (« grossesse/allaitement », « modérée/sévère », « traiter/adresser »…) et 8 unités manquantes (« > 300 » sans mOsm/kg, « entre 30 et 59 » sans mL/min/1,73 m²).

### Importance basse

**C-08 — Accord en nombre.** « Références : » est employé pour une seule référence dans 28 paragraphes (les paragraphes à deux liens ou plus restent au pluriel).

**C-09 — Cohérence terminologique et orthographique.** « co-signé » (3) contre « cosigné » (1) ; « rénine-angiotensine » (1) contre « rénine–angiotensine » (huit) ; « faible densité » contre « basse densité » ; « Fédération internationale de chimie clinique » sans majuscule ; « index » contre « indice » de pression systolique ; « Piège » contre « Erreur fréquente » (renvoi d’intégration R-17).

## Exemples représentatifs

- **L-128** (`E11_pop2.html`) : « data-title="Cholestérol Lipoprotéines de faible densité : cibles selon le risque" » devient « data-title="Cholestérol des lipoprotéines de basse densité : cibles selon le risque" ». *Intitulé agrammatical (« Cholestérol Lipoprotéines », majuscule interne) ; « basse densité » aligné sur la lettre à lettre du glossaire (Low = basse).*
- **L-175** (`E11_pop2.html`) : « data-title="Agonistes du récepteur du Peptide de type glucagon 1 (sémaglutide, dulaglutide)" » devient « data-title="Agonistes du récepteur du peptide de type glucagon 1 (sémaglutide, dulaglutide)" ». *Majuscule interne injustifiée (résidu d’une substitution de sigle).*
- **L-185** (`E11_pop2.html`) : « data-title="Inhibiteurs de la Enzyme de dégradation des incrétines (sitagliptine, linagliptine)" » devient « data-title="Inhibiteurs de la dipeptidyl-peptidase 4 (sitagliptine, linagliptine)" ». *Intitulé agrammatical (« de la Enzyme ») ; le développement exact du sigle DPP-4 est donné par le glossaire (« Dipeptidyl-peptidase 4 »).*
- **L-062** (`E11_d.html`) : « la DPP-4 s’arrête avant l’agoniste » devient « l’inhibiteur de la DPP-4 s’arrête avant l’agoniste ». *La DPP-4 est une enzyme : c’est son inhibiteur qui s’arrête (confusion enzyme / médicament).*
- **L-161** (`E11_pop2.html`) : « Sous glucocorticoïdes, la SSED contrôle la glycémie après » devient « Sous glucocorticoïdes, la SSED recommande de contrôler la glycémie après ». *Agent erroné : une société savante ne contrôle pas la glycémie, elle recommande de la contrôler.*
- **L-044** (`E11_c.html`) : « Quel est l’examen prioritaire ? » devient « Quel est le bilan prioritaire ? ». *La réponse correcte énumère quatre examens : le singulier « l’examen » est inexact.*
- **L-111** (`E11_pop1.html`) : « entre l’épaississement isolé de la membrane basale (classe I) ou l’expansion mésangiale (classe II) et la sclérose globale de plus de la moitié des glomérules (classe IV) » devient « entre, d’une part, l’épaississement isolé de la membrane basale (classe I) et l’expansion mésangiale (classe II) et, d’autre part, la sclérose globale de plus de la moitié des glomérules (classe IV) ». *« Entre A ou B et C » est incorrect : « entre » exige deux termes coordonnés (d’une part / d’autre part).*
- **L-293** (`E11_pop2.html`) : « alors que 2 litres n’en sont pas une. » devient « alors que 2 litres ne le dépassent pas. ». *Tournure elliptique obscure (« n’en sont pas une ») : le pronom « en » et « une » sans antécédent net ; formulation directe.*
- **L-050** (`E11_c.html`) : « >Signal de type glucagon 1 » devient « >Peptide de type glucagon 1 ». *Étiquette de figure erronée : GLP-1 est un « peptide » de type glucagon 1, non un « signal » ; cohérence avec le glossaire (Peptide de type glucagon 1).*
- **L-021** (`E11_b.html`) : « Notre patient, obèse et albuminurique, relève » devient « Le patient de l’îlot 0, obèse et albuminurique, relève ». *Cohérence de désignation : le même patient est appelé « le patient de l’îlot 0 » ailleurs ; « notre » introduit un nous d’auteur absent du reste du cours.*
- **L-124** (`E11_pop2.html`) : « système rénine-angiotensine et aspirine » devient « système rénine–angiotensine et aspirine ». *Tiret : le reste du cours écrit « rénine–angiotensine » (huit occurrences).*
- **L-273** (`E11_pop2.html`) : « La fédération internationale de chimie clinique a établi » devient « La Fédération internationale de chimie clinique a établi ». *Majuscule du nom d’institution.*

## Renvois (non reformulés)

| N° | Type | Fichier | Extrait | Problème | Orientation |
|---|---|---|---|---|---|
| R-01 | medical | `E11_a.html` | « la SSED 2023 cite une forte fréquence d’obésité, variable selon les populations » | Affirmation sans valeur : « forte fréquence » et « variable selon les populations » ne disent aucun chiffre ; la phrase ne peut pas être contrôlée. | Mission MED : relire la section de la SSED 2023 et remplacer par la fréquence citée, ou retirer la proposition. |
| R-02 | medical | `E11_b.html` | « Trois mois plus tard, le patient de l’îlot 0 a un rapport albumine/créatinine de 5 mg/mmol » | Le cas de l’îlot 0 est chiffré à 6 mg/mmol et l’îlot 9 annonce « un rapport de 6 mg/mmol confirmé à trois mois » ; l’îlot 12 donne 5 mg/mmol (même catégorie A2, mais le chiffre change). | Mission MED ou rédaction : harmoniser à 6 mg/mmol (ou expliciter « légèrement variable à 5 »). |
| R-03 | medical | `E11_pop1.html` | « 45–59 avec A2, A3, ou atteinte microvasculaire de trois territoires » | La liste « DFG 45–59 avec A2, A3, ou atteinte… » ne dit pas si A3 s’associe à un DFG 45–59 ou vaut seul ; l’énumération est syntaxiquement ambiguë. | Mission MED : relire le tableau 7 de l’ESC 2023, puis réécrire la liste avec des articles (« un DFG < 45…, un DFG de 45–59 avec A2, une albuminurie A3 ou… »). |
| R-04 | medical | `E11_pop1.html` | « Une plaie noire évoque une nécrose ; une atteinte osseuse ou articulaire de grade 3 impose » | « Cette discussion » n’a pas d’antécédent dans la fenêtre (le paragraphe précédent parle d’« orientation urgente »). | Mission MED : vérifier la grille QualiCCare 2023 et nommer explicitement l’action. |
| R-05 | medical | `E11_pop1.html` | « ces seuils ne sont pas des intervalles normaux du sang » | L’indice cheville/bras et les pressions d’orteil ne sont pas des paramètres « du sang » ; la précision visée (« valeurs de perfusion, non valeurs biologiques normales ») n’est pas dite. | Mission MED : remplacer par « ne sont pas des intervalles de référence » après relecture. |
| R-06 | medical | `E11_pop1.html` | « Une insuffisance rénale terminale ou une dialyse augmente le risque de ce parcours. » | « Le risque de ce parcours » est énigmatique (risque de quoi ? d’amputation, de complication ?). | Mission MED : compléter d’après QualiCCare 2023. |
| R-07 | medical | `E11_pop1.html` | « Les seuils de dépistage asymptomatique sont un consensus « Swiss C », avec une frontière d » | Sigle « Swiss C » non défini et inconnu du glossaire ; phrase difficile à comprendre. | Mission MED : retrouver la signification dans SSED–Société suisse de cardiologie 2024 ou supprimer. |
| R-08 | medical | `E11_pop1.html` | « après 70 ans, elle s’élève d’environ 0,4 % » | Une HbA1c s’exprime en %, donc un écart de « 0,4 % » est ambigu (points de pourcentage ou valeur relative). | Mission MED : remplacer par « 0,4 point de pourcentage » si confirmé. |
| R-09 | medical | `E11_pop2.html` | « Le médecin évite les formes sévères de gastroparésie selon le produit » | Lu littéralement, le médecin « évite » une maladie ; le sens voulu (éviter de prescrire en cas de gastroparésie sévère ?) n’est pas certain, et la tirzépatide est traitée par « prudence particulière » dans la fenêtre voisine. | Mission MED : relire les FI Ozempic® et Trulicity® et réécrire. |
| R-10 | medical | `E11_pop2.html` | « sous DFG 45 mL/min/1,73 m², la dose est 2,5 mg » | « Sous DFG 45 » ne dit pas si 45 est inclus (< 45 ou ≤ 45). | Mission MED : confirmer dans la FI Onglyza® (septembre 2023) et écrire « ≤ 45 » ou « < 45 ». |
| R-11 | medical | `E11_pop2.html` | « aucune classe ESC 2026 non sourcée n’est ajoutée ici » | « ESC 2026 » alors que le cours cite partout l’ESC 2023 pour le diabète (le glossaire de ce fichier contient la même mention, ligne 68 de glossary/e11.py). | Mission MED : vérifier ; corriger l’année dans la fenêtre et dans le glossaire si c’est une coquille. |
| R-12 | medical | `E11_pop2.html` | « indépendamment de la présence de nausées » | Le membre de phrase « 1000 mg par jour, indépendamment de la présence de nausées » ne se comprend pas dans le contexte de l’insuffisance rénale. | Mission MED : relire la FI ; supprimer ou expliquer. |
| R-13 | integration | `E11_pop2.html` | « Metformine et croissance fœtale. » | Le même encadré (« Metformine et croissance fœtale » / « Restriction de grossesse ») figure à l’identique dans les fenêtres e11-grossesse et e11-d-metformine : répétition d’un bloc entier. | Intégration : garder l’encadré dans la fenêtre Grossesse et renvoyer depuis la fenêtre Metformine. |
| R-14 | integration | `E11_pop2.html` | « Le terme est expliqué ici dans le contexte du diabète ; les décisions, populations, chiffr » | Phrase passe-partout répétée à l’identique dans dix fenêtres (ZnT8, DPP-4, GIP, LDL, FLOW, SOUL, KDIGO, CKD-EPI, EAS, FEVG) : l’extrait n’est pas unique et ne peut donc pas être corrigé localement ; elle ne dit rien de propre à chaque notion. | Mission de rédaction : remplacer par une définition en une phrase pour chaque terme. |
| R-15 | integration | `E11_pop1.html` | « Très élevé, 3 ; traiter/adresser » | Cellules identiques répétées (six occurrences de « traiter/adresser » dans le tableau de risque) : « ancien » non unique ; barre oblique à remplacer par « traiter ou adresser ». | Intégration : remplacement global dans cette fenêtre (e11-mrc). |
| R-16 | integration | `E11_a.html` | « Figure 7 — Acanthosis nigricans axillaire » | Numérotation des figures non croissante dans l’ordre de lecture : 1 (îlot 3), 7 (îlot 6), 8 (îlot 9), 6 (Examens), 2 à 5 (Sciences), puis 9 et 10 (fenêtres). Le renvoi « figure 8 de l’îlot 9 » est exact, mais la suite 1-7-8-6-2-5 déroute. | Intégration : renuméroter dans l’ordre de lecture (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) et mettre à jour le renvoi croisé de E11_pop1. |
| R-17 | integration | `E11_b.html` | « Le patient de l’îlot 0 remplit les critères » | Les étiquettes de mise en garde alternent entre « Piège » (span.k, îlots 8, E-2, fenêtre acanthosis) et « Erreur fréquente » (îlots 5 et 10) pour des encadrés de même fonction. | Intégration : retenir « Erreur fréquente » (plus explicite) partout, ou conserver les deux avec un sens distinct. |
| R-18 | integration | `e11.py` | « acidose si < 7,3 » | Dans les chaînes HTML du glossaire, le signe « < » n’est pas écrit « &lt; » (lignes 62, 75, 76, 82) alors que les fenêtres emploient « &lt; » : risque d’affichage tronqué si le texte est inséré tel quel. | Intégration : remplacer « < » par « &lt; » dans ces quatre chaînes. |
| R-19 | medical | `E11_c.html` | « une baisse du DFG de plus de 5 mL/min par an » | La pente de DFG est donnée en « mL/min par an » alors que le DFG est partout en mL/min/1,73 m² ; la fenêtre néphrologie dit « > 5 mL/min/an ». | Mission MED : relire la brochure SSED–néphrologie 2024 et compléter l’unité. |

## Méthode et vérifications

1. Empreintes : les sept fichiers du manifeste ont été recalculés et correspondent.
2. Lecture intégrale de la leçon, surface par surface : onglets Pathologie (`E11_a`, `E11_b`), Examens et Sciences (`E11_c`), Pharmacologie (`E11_d`), fenêtres (`E11_pop1`, `E11_pop2`, soit 91 gabarits) et glossaire.
3. Contrôles mécaniques : ponctuation, doublons, espaces, barres obliques, renvois de figures, méta-discours, singuliers et pluriels de « Références », comparaison du vocabulaire de la leçon à celui des autres chapitres du dépôt.
4. Chaque proposition a été testée : l’extrait « ancien » apparaît **exactement une fois** dans son fichier ; aucune proposition ne chevauche une autre (les propositions voisines qui partageaient du contexte ont été fusionnées) ; l’application simulée conserve le nombre de balises de chaque fichier.
5. Les propositions sont à appliquer sur les fichiers figés ; les groupes LIENS et REFERENCES_SINGULIER sont indépendants des autres et peuvent être intégrés ou écartés séparément.

## Limites déclarées

- Audit de forme uniquement : aucun fait, chiffre, dose, seuil ni source n’a été vérifié ni modifié ; les points où la forme masque le fond sont dans renvois.json (13 renvois médicaux).
- Aucun correcteur orthographique ou grammatical automatique n’était disponible dans l’environnement (aspell, hunspell, LanguageTool absents). Contrôle orthographique par relecture intégrale et par comparaison du vocabulaire de la leçon au vocabulaire des autres chapitres du dépôt : 116 formes inconnues examinées une à une, aucune coquille manifeste. Une faute isolée peut subsister.
- Les espaces insécables (constat C-03) ne sont pas transcrites en propositions locales : près de 2000 occurrences, aucune n’a d’extrait unique ; traitement mécanique à confier au moteur ou à une mission d’intégration.
- Les phrases passe-partout répétées à l’identique (dix fenêtres de sigles) et les cellules de tableau identiques ne peuvent pas être corrigées localement : voir R-14 et R-15.
- Propositions par groupes (LIENS, REFERENCES_SINGULIER) : leur intégration est indépendante des autres ; une reformulation globale du type « Ce point est approfondi dans la fenêtre « … » » reste à valider par Vial (choix éditorial).
- La base du dépôt est f664dd9e (consigne) ; le manifeste mentionne bfc4576b (source_snapshot_sha) : les sept fichiers ont des empreintes identiques à celles du manifeste, donc les propositions s’appliquent à l’état figé.

## Livrables

- `propositions.json` : 302 propositions `{id, fichier, ancien, nouveau, motif, categorie, fond_inchange}` (champs facultatifs : `groupe`, `fusion_de`, `verification_a_l_integration`).
- `renvois.json` : 19 renvois avec extrait exact, problème, raison du renvoi et orientation.
- `rapport.json` : synthèse structurée, lecture, vérifications, constats, limites.
