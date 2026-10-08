# Audit indépendant — Pathologie et Examens

Chapitre : **I83 — Varices des membres inférieurs (C-01-Cardiologie)**. Date : 8 octobre 2026.

Objet Claude examiné : `0974d854db292ae0311e435b3daea5fbed187e25`. Base canonique de comparaison : `ea105ace0046c71492cc6a69ff4c61698ef2ce34`.

**Décision pour ce périmètre : aucun nouveau bloqueur médical démontré ; ancienne réserve bloquante I83-MED-02 corrigée. Avis favorable à l'intégration de ces panneaux, avec les qualifications rédactionnelles ci-dessous. Cet avis ne tranche pas la Pharmacologie ni la décision globale d'injection.** La correction Rapidocain arrivée ensuite relève de la contre-lecture de Pharmacologie ; ce rapport ne la certifie pas.

**Delta de dernière remise :** comparaison effective de `0974d854db292ae0311e435b3daea5fbed187e25` à `20bee19a6329f0a62126e9180bfc909207055e38`. Parmi les HTML du chapitre, seul `I83_pop4.html:50` change, pour retirer l'équivalence directe entre la recette de tumescence et le flacon multidose Rapidocain, en explicitant les conservateurs et la restriction >15 mL. Les six fichiers de notre périmètre, le glossaire et l'entrée du catalogue sont inchangés dans ce delta. **Le présent avis Pathologie/Examens s'applique donc également à cette nouvelle tête exacte.**

La relecture porte sur tous les textes des deux panneaux, leurs exemples, réponses cachées, figure et fenêtres associées. Elle ne signifie pas que chaque référence primaire a pu être consultée de nouveau : les accès externes testés sont bloqués par le proxy. Un échec réseau n'est ni une erreur médicale ni une preuve de conformité.

## Périmètre effectivement lu

- `I83_a.html` et `I83_b.html` : Pathologie entière, sections `i83-1` à `i83-14`, cas fil rouge, quiz CEAP, figure SVG 1 et références finales.
- `I83_c.html` : panneau **pE entier**, sections `i83-e-1` à `i83-e-6`, tableaux, cinq cas d'entraînement et toutes leurs réponses. Ce fichier contient aussi pS ; l'auditeur Sciences a confirmé la prise en charge de ce second panneau.
- `I83_pop1.html` et `I83_pop2.html` : les **30 fenêtres**, dont les trois Pareto de Pathologie.
- `I83_pop3.html` : fenêtres d'Examens `i83-duplex-reflux`, `i83-cartographie`, `i83-ips`, `i83-imagerie-prox` et `pareto-i83-exam`. Cela porte à **35** le nombre de fenêtres relues dans ce périmètre, et à quatre le nombre de Pareto.
- Rapport et addenda du lot `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/`, `CORRECTIONS_AUDIT_CODEX.json`, `LIMITES_FERMEES.json`, preuves suisses et vérifications `verification_ab.json` / `verification_cd.json` ; ancien `AUDIT_MEDICAL_I83.md` du dossier `2026-10-07/PR12_I83_A41_5BEE2A4`.
- Entrée du chapitre dans `chapters.json` pour son titre et son champ `covers`.

Lecture par `git show` de l'objet reçu, sans checkout ni import de code entrant. Aucun HTML canonique, registre ou index n'a été modifié. Aucun build, test navigateur, script du contributeur, déploiement ou publication n'a été exécuté par cet auditeur.

## Anciennes réserves et état actuel

| Sujet | État à l'objet examiné | Preuve et portée |
| --- | --- | --- |
| **I83-MED-02 : EHIT III** | **Corrigé dans les trois endroits concernés.** | `I83_b.html:64`, fenêtre `i83-thermique` et `pareto-i83-tt` de pop2 : III reçoit le curatif et une échographie hebdomadaire jusqu'à rétraction/résolution ; IV est traitée comme une TVP provoquée. Concordance avec les recommandations 3.2–3.5 de Kabnick reproduites dans l'audit indépendant antérieur, dont la lecture primaire est documentée. Pas de nouvelle lecture primaire revendiquée ici. |
| CEAP, coexistence de C4a/C4c | Ancienne hiérarchie erronée retirée ; notation explicitée. Une occurrence non harmonisée subsiste. | `I83_a.html:40,195` et `i83-ceap` : élémentaire C4, complète C2,3,4a,c, indice s/a ; pas de hiérarchie interne a/b/c. `LIMITES_FERMEES.json` contient les citations de Lurie/Eklöf et une transcription du guide AVF. L'ancien accès limité au résumé ne décrit plus la remise actuelle, mais les copies intégrales annoncées ne sont pas fournies dans l'objet. Voir R1. |
| Diamètre des varices | Formulation corrigée et attribution primaire précise. | `I83_a.html:25` et `I83_b.html:129` : sous-cutané, ≥3 mm debout, tronc rectiligne avec reflux inclus ; réticulaires 1 à <3 mm, télangiectasies <1 mm. La citation anglaise d'Eklöf p.1250 est fournie dans `LIMITES_FERMEES.json`. Concordance avec cet extrait, pas nouvelle lecture du PDF. |
| IPS et étiologie de l'ulcère | Ancienne confusion corrigée. | Pathologie, Examens et cas distinguent diagnostic veineux clinique/duplex, artériopathie associée et seuils de compression. L'IPS >0,8 n'est plus donné comme preuve exclusive de l'origine veineuse ; médiacalcose et pression d'orteil sont explicites. |
| Intervention en TVS aiguë | Interdiction absolue retirée et portée ESVS qualifiée. | Section 8, fenêtre `i83-tvs` et Pareto : recommandation III C ; exception d'évacuation d'un thrombus court de collatérale ; ablation du reflux discutée ≥3 mois après, délai reconnu non fondé sur des preuves. La totalité des évolutions SVS/AVF/AVLS 2023 n'a pas été revérifiée en ligne. |
| Mousse et seuil de 6 mm | Ancienne interdiction corrigée. | Tableau et paramètres de Pathologie, tableau d'Examens, `i83-mousse` et Pareto : préférence IIb B pour les petits troncs, aucune interdiction formelle au-delà ; moindre durabilité expliquée et essais distingués. |
| Couverture de la catégorie associée | Limite maintenant visible ; aucune complétude établie. | Le cours **I87 — Autres atteintes veineuses (C-01-Cardiologie)** développe principalement les sous-catégories techniques I87.0, I87.1, I87.2 ; I87.8/I87.9 sont explicitement non développées. Le champ `covers: [I83,I87]` reste un regroupement de catalogue. Il ne prouve pas une couverture intégrale CIM-10-GM, encore moins CIM-11. |
| I83-MED-01 : diabète/polidocanol | Correction déclarée dans le lot ; clôture à confirmer par Pharmacologie. | La conduite réglementaire appartient à d/pop4 et à l'audit correspondant. La présente relecture des indications interventionnelles ne se substitue pas à ce contrôle. |

## Contrôles cliniques de l'ensemble des panneaux

| Domaine relu | Résultat de la comparaison interne et des preuves disponibles |
| --- | --- |
| Définitions et classifications | CVD/CVI C3–C6 distinguées ; CEAP descriptive séparée du VCSS ; C2r, C4c, C6r, Esi/Ese explicités ; Villalta 5–9, 10–14, ≥15 ou ulcère cohérent entre corps, fenêtre et critères. Le score requiert l'antécédent thrombotique et le délai ≥3 mois dans les critères formels. |
| Épidémiologie, causes et mécanismes | Hétérogénéité et absence de données nationales suisses vérifiées déclarées ; modèles microcirculatoires séparés des hypothèses ; facteurs associés et mécanismes plausibles majoritairement qualifiés. Les chiffres des cohortes et le pronostic de l'ulcère restent attribués aux références fournies, sans recontrôle primaire intégral dans cette session. |
| Symptômes, examen et différentiels | Médicaments, organes, TVP, artériopathie, infection, lymphœdème/lipœdème et ulcères atypiques effectivement traités. Examen veineux debout, pouls insuffisants pour exclure l'artériopathie, signes d'obstruction proximale et biopsie d'un ulcère atypique expliqués. Les différences entre dermite de stase et infection sont des indices cliniques, à ne pas lire comme règles d'exclusion absolues. |
| Duplex et reflux | Mesure provoquée debout et analyse du réseau profond avant ablation ; seuils >0,5 s superficiel et >1 s pour fémorale commune, fémorale et poplitée dans les tableaux et critères ; durée distinguée de gravité. Pour les perforantes, variante >0,35 s explicitée dans le tableau, convention >0,5 s utilisée dans les critères. Cartographie inclut source, longueur, diamètre, profondeur cutanée, séquelles et drainage de contournement. Réserve sur l'abréviation des Pareto : R2. |
| Indications et choix d'intervention | Varices symptomatiques et lésions cutanées distinguées du reflux asymptomatique isolé ; œdème seul multifactoriel ; thermique, mousse, colle, mécanochimique, chirurgie et conservation du tronc avec classes/niveaux séparés. Critère de 6 mm traité comme préférence. Risque nerveux sous le genou et phlébectomie associée explicitent la décision du cas. La formulation sur les perforantes mérite R3. |
| Urgences, TVS et EHIT | Surélévation/pression puis orientation urgente après hémorragie ; duplex de tout le membre en TVS ; classes EHIT I–IV et conduite harmonisées. Le choix d'anticoagulant, sa dose et les schémas consommés du chapitre **I80 — Thrombose veineuse profonde et thromboses veineuses (C-01-Cardiologie)** ne sont pas réaudités ici. |
| Compression et ulcère | Tableau et cas concordent sur IPS <0,6, cheville <60 mmHg, orteil <30 mmHg : pas de compression soutenue ; compression modifiée <40 mmHg et surveillance pour l'ulcère mixte avec perfusion suffisante ; compression complète ≥40 mmHg pour l'ulcère veineux avec bilan artériel approprié. NYHA IV/III sans surveillance, neuropathie et pontage superficiel sont explicités. Les contre-indications ne sont pas réduites au seul IPS. |
| EVRA et ESCHAR | Médianes 56/82 jours, 85,6/76,3 % à 24 semaines, récidive 56/31 % à quatre ans cohérents entre texte, fenêtre et quiz. Ulcères récents, observance et chirurgie historique qualifiés ; écart ESVS/publication EVRA déclaré. Pas de lecture primaire neuve certifiée par ces concordances. |
| Atteinte profonde/pelvienne et suivi | Compression et Villalta, protection d'une saphène de drainage, symptômes nécessaires avant stent, équipe multidisciplinaire et contrôle du stent explicités ; traitement local pelvien sans douleur versus embolisation après exclusion des autres causes. Suivi duplex 1–4 semaines expressément attribué à ESVS 2022 IIa C, pas présenté comme nouvelle comparaison exhaustive des recommandations 2023. |
| Cas et quiz | Six quiz relus avec leur réponse : CEAP, artériopathie sévère, compression après revascularisation, ablation précoce, TVS, télangiectasies. Cas d'IPS 0,55/55 mmHg puis 0,75/85/45 mmHg concordants avec leurs décisions. VCSS 8 puis 4 recalculé sur les postes donnés ; corona incluse à 1 pour l'item varices selon la grille reproduite dans le cours. Données de Mme R. cohérentes entre panneaux ; évolution fictive déclarée. |

Ces contrôles établissent la lecture complète et la cohérence des décisions décrites. Ils n'établissent pas une validation médicale humaine intégrale ni une autorisation indépendante de chaque posologie.

## Réserves actuelles localisées

**R1 — Harmonisation de la notation CEAP, mineure.** `I83_a.html:179` conserve `C2,3,4a,4c S`, alors que la règle corrigée, le quiz et `i83-ceap` donnent `C2,3,4a,c (s)`. Les lésions décrites sont les mêmes ; il ne s'agit plus de l'ancienne erreur de hiérarchie. Harmoniser cette occurrence selon la convention nouvellement documentée. L'affirmation de l'addendum « Mme R. s'écrit maintenant… » n'est donc pas exacte pour toutes les occurrences.

**R2 — Résumés du seuil de reflux profond trop généraux, mineure.** `pareto-i83-bases` (pop1), `pareto-i83-crit` (pop2) et `pareto-i83-exam` (pop3:62) abrègent >1 s à « profond » ou « veines profondes ». Le texte développé et le tableau d'Examens limitent cette valeur aux **veines fémorale commune, fémorale et poplitée**. Reprendre ces trois noms dans les résumés évite d'étendre la convention à tous les segments profonds. Le constat est une différence de périmètre interne ; aucun nouveau seuil n'est inventé dans cet audit.

**R3 — Justification du non-traitement de la perforante à préciser, non bloquante pour le cas donné.** `I83_c.html:43` déduit de l'étiquette générale C4 de Mme R. qu'elle n'est pas une cible, après une définition « pathologique » liée à C5/C6. `I83_b.html:66` écrit toutefois que la recommandation 50 concerne C4b–C6. La patiente est **C4a/c, sans C4b ni ulcère** : sa décision clinique reste cohérente. Préciser ces sous-classes et éviter de faire de « C4 » une exclusion générale ; séparer convention descriptive d'une perforante dite pathologique et indication thérapeutique. Le texte primaire complet de la recommandation 50 n'a pas pu être relu pour une nouvelle certification de son exact libellé.

**R4 — Formulations absolues à qualifier, éditoriales.** Dans `i83-ulcere-local`, pop2:82,85 affirme qu'aucun pansement n'a démontré de supériorité ; la rubrique Infection du même texte cite ensuite des méta-analyses favorables à l'iode cadexomère/argent pour la **proportion** cicatrisée, sans effet établi sur le **délai**. Expliciter endpoint et niveau de certitude résout cette tension, sans affirmer de nouvelle efficacité. L'exemple hémorragique `I83_b.html:12` distingue à juste titre le geste hémostatique immédiat de l'arrêt de l'apixaban ; la règle périopératoire de non-interruption en ablation élective ne doit pas être comprise comme une règle générale pour toute hémorragie persistante. Aucune erreur primaire nouvelle sur ce cas n'est démontrée ici.

**Nomenclature.** L'en-tête fournit le code et h1 l'intitulé complet ; l'entrée du catalogue garde code, titre et catégories associées. Une référence reste écrite `(cours I50 — Insuffisance cardiaque, C-01-Cardiologie)` dans pop1:96 : harmoniser vers **I50 — Insuffisance cardiaque (C-01-Cardiologie)**. Les passages sur **I86 — Varices d'autres localisations (C-01-Cardiologie)** ne deviennent pas une déclaration de couverture de cette catégorie. Aucun fragment n'est déclaré achevé.

## Sources et réalité de leur accès

1. **Kabnick AVF/SVS, DOI 10.1177/0268355520953759.** Les recommandations 3.2–3.5 sont documentées dans l'audit indépendant du 7 octobre, qui indique la lecture du primaire PMC7820569. Les passages corrigés ont été confrontés à cette preuve conservée. Notre nouvelle ouverture de `https://pmc.ncbi.nlm.nih.gov/articles/PMC7820569/` échoue au proxy CONNECT avec HTTP 403 ; ne pas annoncer une nouvelle lecture du primaire.
2. **Eklöf 2004 / Lurie 2020 / guide AVF.** Citations fournies dans `LIMITES_FERMEES.json` : définition « 3 mm in diameter or larger, measured in upright position », préservation des définitions de 2004, règle basic/advanced et ordre non assimilable à la gravité. Comparaison possible avec ces extraits ; copies intégrales et image AVF annoncées dans des chemins `src/` absents de l'objet reçu, non relues indépendamment.
3. **ESVS 2022 / ESVS 2021.** Sections, classes/niveaux, quelques citations et journal de corrections fournis par l'auteur. Aucun PDF/texte complet local n'a été retrouvé pour cette contre-lecture. Les nouveaux accès externes testés ont échoué. Les classes/niveaux ont été contrôlés en cohérence interne et contre les passages fournis ; l'intégralité des tableaux originaux n'a pas été nouvellement validée.
4. **Sources suisses.** Preuves suisses lues comme documents reçus, avec auteur, date et empreintes annoncées. Elles ne réouvrent pas automatiquement la Pharmacologie. Aucune nouvelle vérification intégrale de LiMA, OPAS, tarif, CIM-10-GM ou Swissmedic n'est revendiquée ici.

Destinations testées dans cette session, toutes avec `URLError: Tunnel connection failed: 403 Forbidden` :

```text
https://www.venousforum.org/resources/guidelines/
https://pmc.ncbi.nlm.nih.gov/articles/PMC7820569/
https://pmc.ncbi.nlm.nih.gov/articles/PMC11523430/
https://orbi.uliege.be/handle/2268/288479
https://www.venousforum.org/wp-content/uploads/2022/02/3740-AVF-Venous-Workbook_notation.jpg
https://web.archive.org/web/20250702121606/https://www.jvsvenous.org/article/S2213-333X(20)30063-9/fulltext
https://esvs.org/wp-content/uploads/2022/09/2022-CVD-Guidelines.pdf
```

La dernière adresse est un emplacement de PDF essayé ; son existence n'a pas été confirmée. Le refus intervient au tunnel du proxy, avant lecture du site : il ne prouve ni que l'éditeur refuse le document ni qu'il est absent.

Restent seulement **non revérifiés en ligne**, et non démontrés faux : évolution précise des recommandations SVS/AVF/AVLS 2023 face au cadre ESVS annoncé, chiffres épidémiologiques/prognostiques — dont la récidive d'ulcère « jusqu'à 70 % dans les trois mois » — et détails des examens pelviens. Le chiffre de récidive est attribué à ESVS §6.1 dans la vérification auteur ; le passage primaire correspondant n'est pas fourni pour contre-lecture. Cette liste ne constitue pas un nouveau diagnostic d'erreur ni un veto automatique.

Les réserves MED ESC concernant d'autres chapitres restent dans leur dossier propre. Aucun élément de ce contrôle ne les transforme en bloqueur automatique de ce nouveau chapitre ni ne les déclare levées.

## Empreintes des fichiers lus dans l'objet reçu

Le tableau original du rapport conserve des empreintes historiques. L'addendum courant donne les empreintes suivantes, recalculées ici sur les objets Git et concordantes :

```text
1610615e2f39a888d4ccb46b46b56a4ea0c5195f19dfd8af68cac511f7f0ff76  chapters/I83/I83_a.html
d336d0b4e4977212ffa192fe2c57a535db54f288daa2ce014c022d513ed9da9a  chapters/I83/I83_b.html
ed129bc2d10d36cca74a8a0ab6d3994e9ba101e65ffe3392e84ada8473e48261  chapters/I83/I83_c.html
a790feb6f96e5805da69f398daf23a617813424a44dad8d14d94e1b2348e36cd  chapters/I83/I83_pop1.html
e19683146892162c19e526fda676e558f21d42e894738b6a90ab3475086b1d55  chapters/I83/I83_pop2.html
c0c1dda088686b7abf4f2b38f4f858298a37c46e1d3003f50e06c6b221697c42  chapters/I83/I83_pop3.html
```

Avis limité à ces contenus exacts, conservés sans modification à la tête `20bee19a6329f0a62126e9180bfc909207055e38`. Si le coordinateur corrige une réserve ou reçoit un nouveau delta, consigner le nouveau SHA et relire les fichiers et fenêtres consommatrices concernés avant la décision globale d'injection.
