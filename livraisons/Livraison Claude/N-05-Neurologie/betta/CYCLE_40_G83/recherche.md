# G83 — Autres syndromes paralytiques (N-05-Neurologie) — dossier de recherche

Cycle Betta 40, leçon 1 · agent C40-A1-NEUR (Opus 5.5) · 15.10.2026
Statut : recherche brute pour l'agent de rédaction. Audit différé — revue IA, distincte d'une validation médicale humaine.
Règle : chaque fait porte sa référence [Sx] (voir `sources.json`). Ce qui n'a pas été lu figure dans « Lacunes ». Aucune donnée de mémoire.
Note de méthode : le quota WebSearch de la session était épuisé dès le départ. Recherche faite par PubMed (MCP et E-utilities : résumés, métadonnées, deux textes intégraux PMC), WebFetch/curl d'URL connues (BfArM, Revue Médicale Suisse, PMC) et `tools/swissmedic_fi.py`. Beaucoup de sources n'ont été lues qu'au niveau du résumé : la rédaction doit s'en tenir aux énoncés ci-dessous.

## 0. Question clinique
G83 est une catégorie « fourre-tout » de syndromes paralytiques qui ne relèvent ni de la paralysie cérébrale (G80), ni de l'hémiplégie (G81), ni de la para-/tétraplégie (G82) [S1]. Elle rassemble des tableaux très différents en gravité : la monoparésie d'un membre, la diplégie brachiale, la paralysie faciale centrale, la paralysie postcritique de Todd, et deux urgences majeures, le **syndrome de la queue de cheval** (G83.4-) et le **locked-in syndrome** (G83.5) [S1][S2]. Pour l'examen, le cœur pratique est : reconnaître et faire imager en urgence un syndrome de la queue de cheval ; reconnaître un locked-in syndrome (et ne pas le confondre avec un trouble de la conscience) ; savoir qu'une paralysie postcritique est un « stroke mimic » ; distinguer paralysie faciale centrale et périphérique pour le codage.

## 1. Définition et périmètre CIM-10-GM
- G83.- « Sonstige Lähmungssyndrome » / « Autres syndromes paralytiques », bloc G80–G83 [S1][S2].
- Note d'usage BfArM : code primaire seulement si l'affection n'est pas précisée davantage, ou si elle est ancienne/de longue date et de cause non précisée ; utilisable aussi en codage multiple, quelle qu'en soit la cause [S1].
- Inclusion générale : paralysie (complète, incomplète) sauf celles listées sous G80–G82 [S1].
- Sous-catégories (libellés OFS français [S2], notes BfArM [S1]) :
  - G83.0 Diparésie et diplégie des membres supérieurs (diplégie supérieure ; paralysie des deux membres supérieurs).
  - G83.1 Monoplégie d'un membre inférieur (paralysie d'une jambe).
  - G83.2 Monoparésie et monoplégie d'un membre supérieur (paralysie d'un bras).
  - G83.3 Monoparésie et monoplégie, sans précision.
  - G83.4- Syndrome de la queue de cheval : G83.40 complet ; G83.41 incomplet ; G83.49 non précisé. Note de codage : pour documenter un trouble vésical neurogène, ajouter un code G95.8- [S1].
  - G83.5 Locked-in syndrome [syndrome de déefférentation motrice] (libellé OFS tel quel, coquille « déefférentation » dans la source [S2]).
  - G83.6 Paralysie faciale centrale : parésie faciale par lésion du premier motoneurone ; **exclut** la paralysie faciale par lésion du deuxième motoneurone, codée G51.0 [S1].
  - G83.8 Autres syndromes paralytiques précisés : inclut la **paralysie de Todd (postcritique)** [S1].
  - G83.9 Syndrome paralytique, sans précision [S1].

## 2. Syndrome de la queue de cheval (G83.4-) — noyau de la leçon

### 2.1 Anatomie normale → lésion
- La moelle se termine vers L2 ; la queue de cheval comprend toutes les racines nées sous ce niveau, dont les composantes proximales de L3, L4, L5 et S1 [S5].
- L'atteinte de L3–S1 touche surtout les jambes ; le terme « syndrome de la queue de cheval » désigne historiquement le dysfonctionnement des racines **S2 à S5** (vessie, intestin, sensibilité périnéale, fonction sexuelle) [S5].
- Distinction avec le syndrome du cône terminal (trauma) : le syndrome du cône peut résulter d'une lésion des vertèbres T12–L2 et atteint les structures nerveuses du segment médullaire T12 jusqu'à la racine S5 ; le syndrome de la queue de cheval peut résulter d'une lésion des vertèbres L3–L5 et atteint les racines L3–S5 ; l'hypothèse d'un meilleur pronostic fonctionnel du second reste à tester [S14].

### 2.2 Définition
- Définition pratique proposée (revue de 212 articles, 17 définitions recensées) : diagnostic clinique résultant du dysfonctionnement d'une ou plusieurs racines sacrées S2 et en dessous ; au moins un des éléments suivants : dysfonction vésicale et/ou intestinale ; diminution de la sensibilité de la région en selle ; dysfonction sexuelle. Douleur lombaire et des jambes, signes moteurs ou sensitifs des membres inférieurs sont fréquents mais non indispensables. La compression radiculaire est la cause la plus fréquente ; l'IRM est en général nécessaire à la confirmation [S5].
- Définition suisse (Revue Médicale Suisse) : apparition de troubles sphinctériens par compression des racines sacrées, avec rétention urinaire ou incontinence par regorgement, parésie des membres inférieurs de degré divers et anesthésie en selle [S3].
- Hétérogénéité : sur 110 études (52 008 patients), seules 16 (14,5 %) utilisaient une définition établie (Fraser, BASS, Gleave et MacFarlane…) [S13].

### 2.3 Classifications
- **CESI / CESR** (Gleave et MacFarlane 2002, la plus utilisée) [S5] :
  - CESI (incomplet) : troubles urinaires d'origine neurogène (sensation altérée, perte du besoin, jet faible, poussée) mais contrôle volontaire conservé, miction possible même difficile.
  - CESR (avec rétention) : perte du contrôle volontaire, rétention indolore avec regorgement. Le sondage précoce complique ce diagnostic (il empêche distension et regorgement).
  - Valeur pronostique ; selon Gleave et MacFarlane, une fois au stade CESR, le délai opératoire n'influence plus le résultat (contesté) [S5].
- Catégories ajoutées [S5] : CESS (suspicion : symptômes bilatéraux des jambes ou grosse hernie connue, sans symptôme de queue de cheval) ; CESE (précoce, « symptômes seuls » : hypoesthésie périnéale à vessie normale, ou changement mictionnel à sensibilité normale) ; CESC (complet : perte de toutes les fonctions sensitives et motrices de queue de cheval, pire que CESR).
- Classification par mode de présentation (Tandon et Sankaran) : trois types ; le type 2 domine dans les litiges ; type 3 souvent non urgent, plus âgé [S5] (détail des trois types non lisible dans le texte extrait : lacune).
- Fiabilité : sur 100 vignettes réelles, accord inter-observateurs insuffisant pour toutes les catégories ; meilleur accord pour « CES avec rétention vs autres » (kappa 0,34, accord minimal) ; consultants spécialistes kappa 0,17 [S12]. La revue britannique 2025 (parcours GIRFT) mentionne une « déclassification » du CES [S7].
- Lien avec le codage : CIM-10-GM sépare complet (G83.40), incomplet (G83.41), non précisé (G83.49) [S1] ; aucune source lue ne fait la correspondance officielle avec CESI/CESR (lacune).

### 2.4 Épidémiologie
- Incidence publiée 0,34 à 7 / 100 000 / an [S9].
- Prévalence ≈ 0,04 % parmi les patients lombalgiques (Suisse, citant la littérature) [S3].
- ≈ 2 % des hernies discales lombaires [S4].
- Cause la plus fréquente : hernie discale lombaire massive [S5][S25].

### 2.5 Causes
- Hernie discale lombaire (cause la plus fréquente) [S5][S25].
- Causes iatrogènes documentées en Suisse : injection péridurale de stéroïdes sans guidage par l'imagerie (deux cas Balgrist : un CES avec arachnoïdite, un syndrome du cône après ponction durale ; séquelles vésico-intestinales persistantes à 2 ans) [S15] ; bloc des branches médiales lombaires avec méthylprednisolone particulaire, lésions ischémiques de la queue de cheval à l'IRM (Morges) [S16].
- Tumeurs de la queue de cheval (ex. tumeur fibreuse solitaire mimant un schwannome) : citées en différentiel dans la littérature lue (lacune quantitative). L'IRM est supérieure au CT pour visualiser le sac dural et les tissus mous en cas de tumeur [S3].

### 2.6 Clinique
- Symptôme le plus souvent retrouvé : rétention urinaire, sensibilité ≈ 90 % ; en son absence, probabilité de CES ≈ 1/10 000 [S3].
- Série de 44 hernies discales : tous avaient rétention ou incontinence par regorgement avec anesthésie en selle ; installation en < 24 h chez 89 % [S3].
- L'incontinence est un stade tardif : interroger finement la sensation urinaire, le jet, la fréquence ; examiner la sensibilité périnéale, périanale et génitale ; ne pas se contenter de « êtes-vous incontinent ? » [S5].
- Une hypoesthésie périnéale n'est pas absolument indispensable au CESI [S5].
- Drapeaux rouges retrouvés dans toutes les recommandations internationales revues (9 documents) : troubles sensitifs périanaux/périnéaux/en selle et dysfonction vésicale ou intestinale ; douleur radiculaire dans 8/9 ; faiblesse motrice nouvelle 5/9 ; toucher rectal 4/9 ; résidu post-mictionnel 5/9 [S6].
- Valeur prédictive faible des drapeaux rouges : « sciatique bilatérale » sensibilité 32,4 %, VPP 17,2 %, VPN 88,3 % (260 suspicions, prospectif) [S10].

### 2.7 Examens
- **IRM** : examen de choix ; urgente en cas de drapeaux rouges, consensus de toutes les recommandations revues [S3][S6]. Standard BASS (Royaume-Uni) : IRM immédiate, dans l'heure suivant la présentation aux urgences [S25]. Parcours GIRFT 2025 : capacité IRM 24 h/24 locale, séquences standardisées, imagerie plus proximale si pas de compression de la queue de cheval [S7].
- CT : montre bien l'os, analyse mal la queue de cheval, le sac dural et le LCR [S3].
- **Résidu post-mictionnel (échographie vésicale)** :
  - Prospectif, 260 patients : seuil ≥ 200 ml, sensibilité 94,1 %, spécificité 66,8 %, VPP 29,9 %, VPN 98,7 % ; 13 % classés « bas risque », IRM non urgente sans compression retrouvée [S10].
  - Méta-analyse (7 études, 734 patients analysables, 125 CES confirmés) : 200 ml meilleur seuil, sensibilité 82 % ; spécificité rapportée 65 % (l'intervalle publié 0,70–0,90 est incohérent avec la valeur ponctuelle : ne pas citer l'intervalle) ; à n'utiliser qu'en complément, pas comme outil d'exclusion [S11].
  - GIRFT 2025 : scanner vésical comme outil d'inclusion (« rule-in ») et non d'exclusion [S7].
- CES « à IRM négative » (Hoeritzauer) : symptômes de type CES sans compression, groupe non chirurgical [S5].
- Après CES : bilan neuro-urologique nécessaire pour révéler la dysfonction vésico-intestinale et prévenir les complications secondaires [S15].

### 2.8 Prise en charge
- Suisse : la lombosciatique avec syndrome de la queue de cheval fait partie des trois entités à adresser en urgence en milieu hospitalier (avec la lombosciatique hyperalgique et la lombosciatique paralysante) ; urgence diagnostique et thérapeutique ; chirurgie retardée associée à déficit moteur sévère persistant, douleurs neurogènes, dysfonction sphinctérienne et sexuelle [S3].
- Délai : sur 24 patients opérés après 48 h, retard imputable au patient 4 fois, au médecin 20 fois (absence de diagnostic 7, retard des moyens diagnostiques 8, retard chirurgical 5) [S3].
- Allemagne (Dtsch Arztebl 2024) : urgence chirurgicale absolue, décompression dans les 24–48 h [S4].
- GIRFT 2025 : tout CES établi doit bénéficier d'une décompression urgente (NCEPOD niveau 1/2), en général dans les 24 h [S7].
- Données sur le délai :
  - Ahn 2000 (322 patients) : avantage significatif ≤ 48 h vs > 48 h (sensitif, moteur, urinaire, rectal) ; pas de différence < 24 h vs 24–48 h [S23]. OR rapportés par [S4] : incontinence urinaire 2,5 ; déficit moteur 9,1 ; dysfonction rectale 9,1 ; déficit sensitif 3,5.
  - Kumar 2022 (cité par [S4] : 22 études, 852 CES, suivi ≥ 1 an) : incontinence urinaire résiduelle 24,6 % (≤ 48 h) vs 50,3 % (> 48 h).
  - Méta-analyse 2026 (15 études, 26 627 adultes, CES dégénératif) : ≤ 48 h améliore la récupération urinaire (OR ≈ 2,3), motrice et neurologique ; effet fort dans le CES incomplet, pas de différence significative liée au délai dans le CES avec rétention ; pas d'avantage constant de < 24 h vs 24–48 h ; à ≥ 12 mois les différences s'atténuent et l'état vésical initial domine le pronostic ; bases nationales : mortalité et durée de séjour accrues au-delà de 48 h [S8].
  - DeLong 2008 (CESR) : risque relatif de résultat moyen/mauvais plus élevé avec chirurgie plus tardive (RR 1,77–2,19 selon le seuil) ; CESR et CESI ne doivent pas être analysés ensemble [S24].
  - Revue JBJS 2025 : délai optimal débattu ; décompression chirurgicale = traitement définitif ; litiges surtout pour retard diagnostique [S9].
- Médicaments : aucun traitement médicamenteux spécifique du CES dans les sources lues (lacune). Pour les séquelles spastiques d'autres causes de G83 voir §4.

### 2.9 Pronostic et séquelles
- Séquelles après CES (synthèse [S4]) : incontinence urinaire 43 % ; dysfonction rectale 31 % ; dysfonction sexuelle 40 % (Kumar) ou 70 % des hommes et 60 % des femmes (Sangondimath) ; déficit sensitif 53 % ; déficit moteur 38 %.
- Facteurs pronostiques : délai de décompression, sévérité initiale, atteinte vésicale [S8][S24] ; douleur lombaire chronique préopératoire et dysfonction rectale préopératoire = moins bon résultat urinaire ; âge plus élevé = moins bonne fonction sexuelle [S23].

## 3. Locked-in syndrome (G83.5)

### 3.1 Définition et formes
- Tétraplégie avec mouvements oculaires verticaux et des paupières préservés et capacités cognitives conservées ; décrit par Plum et Posner (1972) [S17].
- Formes (Bauer 1979) [S17] : classique (tétraplégie, anarthrie, seuls mouvements verticaux des yeux et clignement) ; incomplet (davantage de motricité volontaire ; peut être une étape de récupération) ; complet (aucun mouvement volontaire, aucune communication directe : examens complémentaires indispensables) ; « locked-in plus » (troubles de la conscience associés, terme du Salzburg Coma Group).

### 3.2 Mécanismes
- Lésion de la base (partie ventrale) du pont : faisceaux corticospinaux (motricité du corps) et corticobulbaires (nerfs crâniens caudaux : parole, langue) qui y cheminent côte à côte [S17].
- Mouvements horizontaux perdus si atteinte de la formation réticulée pontique paramédiane (PPRF) ; mouvements verticaux et releveur de la paupière contrôlés par le mésencéphale (riMLF, noyau interstitiel de Cajal, commissure postérieure, noyaux III et IV), donc préservés dans la forme classique ; leur atteinte donne la forme complète [S17].
- Conscience altérée (locked-in plus) si la lésion s'étend au mésencéphale et au thalamus médian, ou au tegmentum dorsal (système réticulé activateur ascendant) [S17].
- Mouvements involontaires possibles (automatismes oraux, spasmes, bâillements, pleurs) : à distinguer des mouvements volontaires utilisables pour communiquer [S17].

### 3.3 Causes et épidémiologie
- Causes les plus fréquentes : infarctus et hémorragie du territoire vertébrobasilaire (pont ventral), parfois précédés d'un « pontine warning syndrome » (symptômes moteurs/sensitifs récidivants et fluctuants, à haut risque d'infarctus basilaire) [S17].
- Autres causes : dissection, anévrisme, myélinolyse centropontine, traumatisme crânien, tumeur, abcès, sclérose en plaques, hypoglycémie prolongée ; états « locked-in like » : SLA avancée, Guillain-Barré sévère, morsures de serpent ; causes iatrogènes [S17].
- Série de 139 cas (1986) : âge moyen 52 ans, 85 hommes/52 femmes, 89 classiques, 46 incomplets, 3 complets ; 82 infarctus pontiques ; mortalité 60 % (majorité dans les 4 premiers mois) ; étude plus récente : 75 % en phase aiguë ; décès surtout par complications pulmonaires et nouvelle atteinte du tronc [S17].
- Prévalence estimée 0,7/10 000 patients en EMS néerlandais (2013) [S17].
- Occlusion de l'artère basilaire : 1–2 % des AVC, évolution naturelle très défavorable [S18].

### 3.4 Diagnostic et différentiel
- Délai diagnostique moyen > 2 mois ; dans un quart des cas seulement, le médecin est le premier à reconnaître la conscience du patient (étude 2002) [S17].
- Différentiels : syndrome d'éveil non répondant (UWS), état de conscience minimale (MCS), dissociation cognitivo-motrice (CMD), mutisme akinétique ; lésions surtout supratentorielles dans ces derniers, tronc cérébral dans le LiS [S17].
- Examen clinique répété et structuré, IRM ; si aucune communication n'est établie, IRM fonctionnelle ou paradigmes EEG actifs ; la CRS-R est l'étalon pour UWS/MCS mais manque les patients sans sortie comportementale ; l'EAN propose une évaluation multimodale des troubles de la conscience [S17].

### 3.5 Prise en charge aiguë de la cause (occlusion basilaire, ESO/ESMINT 2024)
- Certitude des preuves généralement très faible ; nombreux énoncés par consensus d'experts [S18].
- Thrombolyse intraveineuse jusqu'à 24 h sauf contre-indication (consensus) ; IVT + traitement endovasculaire (EVT) plutôt qu'EVT direct [S18].
- EVT + meilleur traitement médical plutôt que traitement médical seul pour NIHSS ≥ 10 (certitude très faible) ; pour NIHSS < 10, pas de preuve en faveur de l'EVT [S18].

### 3.6 Réadaptation, suivi, éthique
- Réadaptation précoce et intensive (début en moyenne 1 mois après) : améliore le devenir fonctionnel et réduit la mortalité ; prise en charge de la douleur, spasticité, incontinence, nutrition, trachéotomie, vision, communication [S17].
- Prévention des complications pulmonaires (première cause de décès) : kinésithérapie respiratoire, changements de position, drainage, aspiration [S17].
- Spasticité : baclofène intrathécal fréquemment utilisé [S17] (voir FI suisse §4).
- Ulcère cornéen par fermeture palpébrale insuffisante : tarsorraphie latérale ou toxine botulique [S17].
- Communication : interfaces cerveau-ordinateur (EEG surtout) ; 63 % des patients d'une enquête utilisent des aides techniques avancées [S17].
- Récupération possible sur des années : 72 % de récupération de mouvements fonctionnels dans une enquête chez des patients chroniques ; récupération distale plus probable [S17].
- Qualité de vie : 72 % se déclarent heureux ; souhait d'euthanasie 7 % ; les soignants sous-estiment le bien-être ; une enquête européenne : 9 % des professionnels pensent que ces patients ne ressentent pas la douleur ; la moitié des patients d'une enquête française rapportent des douleurs [S17].

## 4. Pharmacologie utile — baclofène intrathécal (Liorésal intrathécal®, FI suisse, mise à jour avril 2024) [S22]
- Indication : spasticité chronique grave d'origine médullaire (traumatisme, SEP, autres atteintes médullaires) ou cérébrale ne répondant pas aux antispastiques oraux (dont baclofène oral) ou avec effets indésirables inacceptables aux doses orales efficaces.
- Mécanisme : antispastique à point d'impact médullaire ; ralentit la transmission réflexe mono- et polysynaptique par stimulation des récepteurs GABA-B ; transmission neuromusculaire non modifiée.
- Phase de test obligatoire : bolus intrathécal (ponction lombaire ou cathéter), dose initiale adulte 25 ou 50 µg, paliers de 25 µg à au moins 24 h d'intervalle jusqu'à effet de 4 à 8 h ; enfant 25 µg ; dans un centre équipé, matériel de réanimation prêt (risque de dépression du SNC, collapsus, insuffisance respiratoire). Pompe implantée seulement après évaluation de la réponse.
- Après traumatisme crânien : traitement au long cours seulement quand la spasticité est stabilisée, au plus tôt 1 an après la lésion.
- Contre-indications : hypersensibilité ; voies IM, IV, péridurale, sous-cutanée ; épilepsie résistante au traitement.
- Arrêt : toujours progressif (hors surdosage urgent) ; ne jamais interrompre soudainement (sevrage pouvant mettre la vie en danger).
- Surdosage : hypotonie excessive, somnolence, vertiges, sédation, crises, hypothermie, ptyalisme, nausées ; dépression respiratoire, apnée, coma si fort surdosage.
- Prudence si une part de spasticité est nécessaire à la station debout, à l'équilibre ou à la marche.

## 5. Paralysie de Todd (postcritique, G83.8)
- Incluse dans G83.8 [S1].
- Revue systématique des manifestations postcritiques (78 articles, 45 en méta-analyse) : 31 manifestations ; durée habituellement < 24 h, jusqu'à 2 mois pour certains symptômes physiques et cognitivo-comportementaux [S19] (fréquence et durée spécifiques de la parésie de Todd non extraites du résumé : lacune).
- Diagnostic différentiel avec l'AVC ischémique (« stroke mimic ») :
  - Aux urgences d'un hôpital universitaire (Italie, 6 998 patients rétrospectifs), 46,7 % des suspicions d'AVC étaient des mimics ; score de triage à 10 variables (SMS), AUROC 0,777 et 0,774 en validation [S20].
  - Parmi des patients thrombolysés sans signe ischémique précoce ni occlusion (Lituanie, 330), 11,2 % étaient des mimics ; prédicteurs : âge plus jeune, symptômes sensitifs, antécédent de migraine ou d'épilepsie, absence de fibrillation auriculaire ; aucune hémorragie intracrânienne chez les mimics thrombolysés [S21].
- Prise en charge propre de la paralysie de Todd : non documentée dans les sources lues (lacune).

## 6. Monoparésie, diplégie brachiale, paralysie faciale centrale (G83.0–G83.3, G83.6)
- Définitions et inclusions : voir §1 [S1][S2].
- Paralysie faciale centrale : lésion du premier motoneurone ; la forme par lésion du deuxième motoneurone (périphérique) relève de G51.0 [S1]. Les fibres corticobulbaires cheminent avec les faisceaux corticospinaux dans le pont ventral [S17].
- Aucune source lue ne détaille la sémiologie distinctive (épargne du front), l'étiologie ou la prise en charge des monoparésies et de la paralysie faciale centrale : lacune explicite ; l'agent de rédaction ne doit pas compléter de mémoire.

## 7. Critères formels (à reprendre dans `div.alert`)
- CIM-10-GM : G83 = paralysie hors G80–G82 ; code primaire seulement si non précisée ou ancienne de cause non précisée [S1].
- CES (définition pratique) : ≥ 1 parmi dysfonction vésicale/intestinale, hypoesthésie en selle, dysfonction sexuelle, par atteinte des racines S2 et en dessous ; confirmation par IRM [S5].
- CESI vs CESR : contrôle mictionnel volontaire conservé vs rétention indolore avec regorgement [S5].
- LiS classique : tétraplégie + anarthrie + mouvements verticaux des yeux/clignement préservés + cognition conservée [S17].

## 8. Paramètres clés (à reprendre dans `div.key`)
- CES : ≈ 2 % des hernies discales [S4] ; 0,04 % des lombalgiques [S3] ; incidence 0,34–7/100 000/an [S9].
- Rétention urinaire : sensibilité ≈ 90 % ; sans elle, probabilité ≈ 1/10 000 [S3].
- Installation < 24 h chez 89 % [S3].
- Résidu post-mictionnel ≥ 200 ml : sensibilité 94,1 %, VPN 98,7 % [S10].
- Décompression ≤ 48 h : incontinence résiduelle 24,6 % vs 50,3 % [S4] ; OR récupération urinaire ≈ 2,3 [S8].
- Occlusion basilaire : 1–2 % des AVC [S18] ; IVT jusqu'à 24 h (consensus) [S18].
- Baclofène IT test : 25–50 µg, paliers de 25 µg / ≥ 24 h [S22].

## 9. Sous-codes couverts
G83.0, G83.1, G83.2, G83.3 (définitions seulement) ; G83.4, G83.40, G83.41, G83.49 (complet) ; G83.5 (complet) ; G83.6 (définition et exclusion) ; G83.8 (Todd, partiel) ; G83.9 (définition).

## 10. Lacunes
1. WebSearch indisponible (quota épuisé) : aucune recommandation suisse dédiée au CES, au LiS ou à la paralysie de Todd n'a pu être recherchée ; Swiss Medical Forum non consulté. Source suisse unique pour le CES : Amaudruz et al., Rev Med Suisse 2010 [S3] (datée), et deux cas suisses [S15][S16].
2. Pas de ligne directrice européenne (EAN, EANS, EuroSpine) spécifique au CES trouvée ; les standards cités (BASS, GIRFT) sont britanniques et lus au niveau des résumés de revues [S7][S25].
3. Paralysie faciale centrale : sémiologie (épargne frontale), causes, conduite non sourcées.
4. Monoparésies et diplégie brachiale : étiologies et démarche non sourcées.
5. Paralysie de Todd : fréquence, durée typique, physiopathologie et conduite non extraites.
6. Correspondance CESI/CESR ↔ G83.40/G83.41 non documentée.
7. Neuro-urologie après CES (EAU) non relue pour cette leçon ; le dossier G82 (cycle 39) en contient une partie.
8. Classification Tandon–Sankaran : les trois types ne sont pas détaillés dans le texte extrait.
9. Méta-analyse PVR [S11] : intervalle de confiance de la spécificité incohérent dans le résumé.
