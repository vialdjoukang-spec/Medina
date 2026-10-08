# Audit indépendant — Sciences de I83 — Varices des membres inférieurs (C-01-Cardiologie)

Date : **8 octobre 2026**. Auteur : sous-agent Codex chargé de Sciences. Remise examinée : **`0974d854db292ae0311e435b3daea5fbed187e25`**, branche Claude `claude/loving-shannon-spwrhc`, PR #12. Base d'intégration communiquée : **`ea105ace0046c71492cc6a69ff4c61698ef2ce34`**.

**Avis Sciences non bloquant : aucune nouvelle erreur médicale majeure démontrée dans ce périmètre.** Les mécanismes principaux sont cohérents, les deux calculs physiques sont exacts et les limites de plusieurs modèles sont présentes. Trois formulations actuelles méritent une qualification explicite ; elles ne constituent pas les deux erreurs de prescription de l'ancienne remise. Cet avis ne clôt ni l'audit Pharmacologie, ni la décision globale d'injection, ni la couverture CIM-11.

**Actualisation au SHA `20bee19a6329f0a62126e9180bfc909207055e38` :** comparaison indépendante des objets Git effectuée après l'annonce de cette correction. `I83_c.html`, `I83_pop3.html`, `glossary/i83.py`, `I83_pop1.html` et `I83_pop2.html` sont identiques octet pour octet à la remise examinée. Dans `I83_pop4.html`, les fenêtres `i83-d-mpff` et `i83-d-polidocanol` associées à cet audit sont également identiques ; la fenêtre de tumescence modifiée appartient à l'avis Pharmacologie. **L'avis Sciences et ses trois qualifications mineures restent donc applicables à cette nouvelle tête.** Cette concordance ne vaut pas validation de la correction pharmaceutique elle-même.

## Périmètre effectivement lu

- `chapters/I83/I83_c.html`, **entièrement**, en séparant ses deux panneaux : Examens `pE`, puis Sciences `pS`. L'avis présenté ici concerne les cinq sous-onglets Sciences : anatomie `i83-sa`, histologie `i83-sh`, physiologie `i83-sp`, biochimie/inflammation `i83-sb`, génétique `i83-sg`. L'auditeur Pathologie/Examens est chargé de la décision sur `pE`.
- `chapters/I83/I83_pop3.html`, **entièrement**, notamment `i83-laplace`, `i83-saphene`, `i83-gen` et les neuf entrées de `pareto-i83-sci`.
- Les deux figures de Sciences : compartiment saphène/jonction saphéno-fémorale (figure 2) et pression veineuse au pied (figure 3), avec l'intégralité de leurs SVG, légendes et commentaires. **Aucun quiz spécifique n'est présent dans `pS`** ; les quiz de `pE` sont lus mais leur validation relève de l'autre avis.
- Fenêtres associées : `i83-pav` et `i83-microcirc` dans `I83_pop1.html` ; `i83-compression` et `i83-thermique` dans `I83_pop2.html` ; `i83-d-mpff` et `i83-d-polidocanol` dans `I83_pop4.html`, pour la concordance de leurs mécanismes avec Sciences. Cela ne certifie pas toutes leurs prescriptions.
- `glossary/i83.py`, **entièrement en texte**. Aucune importation ni exécution de ce fichier ou d'un code reçu.
- Le rapport `lots/2026-10-08-I83/rapport.md`, ses addenda, les corrections déclarées dans `CORRECTIONS_AUDIT_CODEX.json` et `LIMITES_FERMEES.json`, et l'audit historique `PR12_I83_A41_5BEE2A4/AUDIT_MEDICAL_I83.md` ont été examinés pour distinguer la version actuelle de ses antécédents.

Les trois sources principales de cet avis ne sont **pas encore présentes dans `main` `ea105ace…`**. Leur lecture porte donc sur les objets Git au SHA Claude fixé, et ne prouve aucune injection canonique ou publication.

## Résultats par domaine

| Domaine et repère | Conclusion et preuve dans le contenu examiné |
| --- | --- |
| Anatomie, `i83-sa`, `i83-saphene`, figure 2 | Le compartiment entre fascia saphène et fascia musculaire est distingué des collatérales sous-cutanées. Les jonctions variables, points de fuite pelviens et rapports avec les nerfs saphène/sural sont reliés au Doppler et au risque d'ablation basse. Le schéma annonce que ses proportions ne sont pas respectées. Les formulations « habituellement rectiligne » dans le développement et les variantes décrites permettent de lire la synthèse comme un schéma anatomique général. Aucune contradiction majeure identifiée. |
| Histologie, `i83-sh`, glossaire MMP | La paroi normale précède le tableau comparatif normal/pathologique : endothélium, valvules, média et matrice. Le texte distingue inflammation, dégradation matricielle et fibrose ; il expose explicitement l'incertitude sur l'ordre dilatation/incompétence valvulaire. Le glossaire ne prétend pas qu'un inhibiteur des métalloprotéinases modifie l'évolution clinique. Les affirmations de remodelage durable concernent la varice constituée ; elles ne doivent pas servir à exclure les options conservatrices décrites ailleurs. |
| Pression/pompe, `i83-sp`, `i83-pav`, figure 3 | Le repos debout, la vidange par contraction, le remplissage et les conséquences du reflux ou de l'obstruction sont reliés logiquement. Les niveaux 80–90 et 20–30 mmHg sont présentés comme mesures citées de l'ESVS ; les courbes sont annoncées qualitatives. L'absence d'axe temporel quantifié n'est donc pas une fausse série expérimentale. L'association entre pression ambulatoire et classe clinique est distinguée d'une prédiction individuelle d'ulcère. Voir SCI-01 pour une phrase de synthèse trop absolue. |
| Filtration/compression, `i83-sp`, `i83-laplace`, `i83-compression` | Le gradient hydrostatique, l'opposition de la pression tissulaire et le drainage lymphatique expliquent l'œdème ; l'effet précapillaire de l'amlodipine est distingué du reflux veineux. La tension du bandage est définie **par unité de largeur**, ce qui rend `P = T/r` dimensionnellement cohérent. Le modèle cylindrique et l'écart avec la jambe réelle sont explicitement signalés. Une précision facultative sur le coefficient de filtration est indiquée plus bas. |
| Inflammation, `i83-sb`, `i83-microcirc` | Un endothélium sous flux régulier est exposé avant le flux anormal. L'activation, les leucocytes, la perméabilité et le remodelage sont articulés à l'œdème et aux lésions cutanées. Le modèle de Bergan est attribué à une revue et à des données surtout expérimentales. Manchons de fibrine et piégeage leucocytaire sont présentés comme hypothèses historiques insuffisantes à elles seules. Le poids propre du fer dans l'ulcère est dit non établi. SCI-03 demande de conserver ces limites dans la synthèse. |
| Génétique, `i83-sg`, `i83-gen`, glossaire FOXC2/PIK3CA | Le cours distingue varices communes polygéniques, syndrome FOXC2, mosaïque somatique PIK3CA et absence de test courant pour les varices communes. L'examen du tissu atteint et la faible fraction de cellules mutées sont reliés au choix du prélèvement. Ascendance surtout européenne, diagnostic par codes/déclarations et faible effet individuel figurent parmi les limites. Les nombres des cohortes sont attribués à leurs publications ; ils n'ont pas été revérifiés en ligne dans cette session. Voir SCI-02 pour la portée de l'inférence causale. |

## Recalcul indépendant des unités et exemples

1. **Colonne hydrostatique :** `120 cm × 1,05 / 1,36 = 92,647… mmHg`, donc **environ 93 mmHg**. Le cours sépare cette estimation, dépendante d'une hauteur approximative de 1,2 m, des 80–90 mmHg mesurés qu'il cite. Il n'y a pas d'erreur arithmétique ou de contradiction démontrée entre une approximation géométrique et ces mesures.
2. **Rapport de pression cheville/mollet à tension identique :** `r_mollet/r_cheville = C_mollet/C_cheville = 36/24 = 1,5`. Le résultat est exact pour les hypothèses annoncées. Ce n'est pas une pression réellement mesurée chez un patient.
3. **Laplace :** une tension par unité de largeur en N/m divisée par un rayon en m donne une pression en N/m². Le nombre de couches multiplie approximativement cette pression ; la fenêtre mentionne le chevauchement et les limites de la géométrie. Aucun calcul de dose médicale n'est validé par ces vérifications physiques.

## Formulations actuelles à qualifier

Les observations ci-dessous sont **mineures, sans nouveau blocage de sécurité identifié**. Elles sont localisées sur le contenu actuel, pas reprises d'un ancien rapport comme si celui-ci décrivait encore la remise.

| ID | Localisation et passage actuel | Motif démontrable | Correction proposée |
| --- | --- | --- | --- |
| SCI-01 | `I83_c.html`, `i83-sp`, « Science → examen » : **« Le reflux n'apparaît que debout et après provocation. »** | La phrase transforme un protocole de recherche diagnostique en condition exclusive d'existence du phénomène. Les passages `i83-e-2` et `i83-duplex-reflux` parlent correctement de recherche du reflux, de provocation et de risque de le sous-estimer selon la position. | « Le reflux se recherche de préférence debout, avec une manœuvre de provocation adaptée au segment ; un examen couché peut le sous-estimer. » Conserver l'attribution au protocole ESVS § 2.3.1 et les limites cliniques. |
| SCI-02 | `I83_pop3.html`, `i83-gen`, « Association ou cause » : **« comme une répartition au hasard, à l'abri des facteurs de confusion »**. | La même fenêtre parle ensuite d'un rôle causal **soutenu**, et d'un mécanisme hypothétique. « À l'abri » affirme une garantie sans conditions. La randomisation mendélienne exige notamment des instruments pertinents, indépendants des facteurs de confusion et sans voie d'action sur l'issue autre que l'exposition étudiée ; ces conditions ne découlent pas du seul fait d'utiliser des variants. | « La randomisation mendélienne utilise des variants associés à la taille comme instruments ; sous ses hypothèses de validité, elle réduit certains biais de confusion et soutient un rôle causal. Une pléiotropie ou une structure de population peuvent notamment limiter cette interprétation. » Ne pas inventer un test de sensibilité réalisé dans l'étude sans le relire. |
| SCI-03 | `I83_c.html`, `i83-sb`, « À retenir », et `I83_pop3.html`, `pareto-i83-sci` : **fer/TGF-β présentés comme conduisant à la fibrose et à l'ulcère**. | Le développement dit que le poids propre du fer dans l'ulcère n'est pas établi et que certaines étapes du modèle sont expérimentales. La synthèse retire ces limites et paraît établir une chaîne causale clinique complète. | « Selon le modèle inflammatoire, endothélium, leucocytes et remodelage participent aux lésions cutanées ; le rôle propre de certains médiateurs, notamment du fer, reste imparfaitement établi. Les manchons de fibrine sont une hypothèse discutée. » Garder cette distinction aussi dans le Pareto. |

**Précision pédagogique facultative :** dans `i83-sp`, `Kf` est le coefficient de filtration, associant conductivité hydraulique et surface d'échange, plutôt que la seule « perméabilité ». L'équation de Starling est ici une présentation classique simplifiée ; elle explique le sens des variations de filtration sans quantifier à elle seule l'œdème individuel. La prise en compte du drainage lymphatique est déjà présente. Cette simplification ne démontre pas une erreur de conduite clinique.

## Réserves historiques : ne pas les réouvrir artificiellement

- La préférence pour la mousse dans un tronc inférieur à 6 mm est **explicitement séparée d'une interdiction au-delà** dans le tableau actuel d'Examens et son Pareto. L'ancienne formulation restrictive de la remise initiale n'est plus celle de `I83_pop3.html` examiné.
- La fenêtre actuelle `i83-thermique` prescrit bien le **curatif pour la classe III**, avec échographie hebdomadaire, et expose la classe IV. Le glossaire EHIT dit que la classe IV relève du curatif ; il ne dit pas que **seule** cette classe y relève. L'ancien blocage d'omission de la classe III ne peut donc pas être reporté automatiquement à ce SHA.
- La fenêtre actuelle `i83-d-polidocanol` conserve le **diabète dans les contre-indications suisses**, distingue le silence européen et qualifie le mécanisme proposé comme hypothèse. L'ancienne rétrogradation en contre-indication relative n'y subsiste pas.
- Les addenda postérieurs du rapport déclarent des vérifications CEAP, Rapidocain et remboursement qui rendent historiques certaines réserves de ses premiers paragraphes. Leur présence ancienne n'établit pas une erreur actuelle. Leur contrôle primaire détaillé et la formulation Rapidocain relèvent des autres avis ; **aucune clôture Pharmacologie n'est apportée ici**.
- Une actualisation ESC sans rapport direct avec ce cours n'est pas imposée par cet audit. La référence générale des varices dans ce corpus est ESVS 2022, avec les références spécifiques citées pour les autres questions.

## Sources et limites réelles de cet avis

L'avis repose sur la lecture indépendante du **contenu pédagogique à son SHA**, les recalculs et les contradictions de formulation repérables dans ce contenu. Les références citées sont identifiées dans le cours : De Maeseneer et al., ESVS 2022 (§§ 1.2–1.3, 2.3.1, 3.2, 4.1.3, 6.3) ; Raffetto et Khalil 2008 ; Bergan et al. 2006 ; Fukaya 2018 ; Ahmed 2022 ; Mellor 2007 ; Luks 2015 ; Browse 1982 et Coleridge Smith 1988. **Leur citation par le rédacteur ne vaut pas consultation primaire indépendante de toutes ces publications par cet auditeur.**

Les tentatives de lecture indépendante effectuées le 8 octobre vers EuropePMC/EBI, PubMed, PMC, ORBi et ESVS ont échoué avec **`Tunnel connection failed: 403 Forbidden`**. Une exécution autorisée hors du sandbox a rencontré le même refus du proxy. Aucune copie primaire complète ESVS/génétique locale n'a été trouvée. Les URL consultées pour diagnostiquer l'accès comprennent [ORBi — ESVS 2022](https://orbi.uliege.be/handle/2268/288479), [EuropePMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search), [PubMed](https://pubmed.ncbi.nlm.nih.gov/), [PMC — EHIT](https://pmc.ncbi.nlm.nih.gov/articles/PMC7820569/) et [ESVS](https://esvs.org/clinical-practice-guidelines/).

Cette limite **n'est pas transformée en blocage médical nouveau**. Elle empêche seulement de déclarer revérifiés les chiffres génétiques, toutes les données histologiques expérimentales et la totalité des affirmations primaires. Aucun résumé inaccessible n'a été inventé et aucune information provenant d'une autre édition n'a été substituée silencieusement.

## Provenance et contrôles réellement effectués

| Source au SHA Claude fixé | SHA-256 |
| --- | --- |
| `chapters/I83/I83_c.html` | `ed129bc2d10d36cca74a8a0ab6d3994e9ba101e65ffe3392e84ada8473e48261` |
| `chapters/I83/I83_pop3.html` | `c0c1dda088686b7abf4f2b38f4f858298a37c46e1d3003f50e06c6b221697c42` |
| `glossary/i83.py` | `b041af30d40c15eb16c0063dc7d83fa0a57c364608d36ccb38003bf2af7636b4` |
| `chapters/I83/I83_pop1.html` — fenêtres associées | `a790feb6f96e5805da69f398daf23a617813424a44dad8d14d94e1b2348e36cd` |
| `chapters/I83/I83_pop2.html` — fenêtres associées | `e19683146892162c19e526fda676e558f21d42e894738b6a90ab3475086b1d55` |
| `chapters/I83/I83_pop4.html` — fenêtres associées | `8b5a5d007ff4d789e15199bc19a658cc8a35b5388afb89f2804c6e521ba904d1` |

Commandes réellement exécutées : lecture `git show 0974d854…:<chemin>` ; inventaire `git ls-tree` des pièces du lot ; calcul SHA-256 des octets avec `hashlib` ; comptage des cinq titres, des deux figures, de l'absence de quiz `pS` et des neuf entrées du Pareto ; recalculs arithmétiques avec Python standard ; comparaison d'existence avec `main` `ea105ace…` ; requêtes HTTPS publiques décrites ci-dessus. **Aucun build, test navigateur, import de glossaire, code entrant, injection, commit, push ou déploiement exécuté par cet auditeur.**

La décision générale appartient au coordinateur après rapprochement des avis Sciences, Pathologie/Examens, Pharmacologie et contrôles techniques. Les éventuelles corrections sont remises par Claude sur sa branche et contre-vérifiées au nouveau SHA. La certification de complétude CIM-11 reste **non établie**.
