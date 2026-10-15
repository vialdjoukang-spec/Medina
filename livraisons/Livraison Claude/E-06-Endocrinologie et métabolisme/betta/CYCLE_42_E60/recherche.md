# Dossier de recherche — E60 — Carence alimentaire en zinc (E-06-Endocrinologie et métabolisme)

Cycle Betta 42, leçon 2 (c42-E60). Agent de recherche C42-A2-ENDO (Opus 5.5). Consultation : 15.10.2026.
Chaque fait est suivi de sa référence [Sx] (voir `sources.json`). Aucune affirmation de mémoire. Les conversions et calculs faits par l'agent sont signalés « (calcul de l'agent) », toujours avec le facteur de conversion ESPEN : 1 µmol/L = 65,4 µg/L [S2]. Audit différé — revue IA, distincte d'une validation médicale humaine.

## 0. Nosologie (décisif pour le rédacteur)

- Libellé OFS CIM-10-GM 2024 : **E60 — Carence alimentaire en zinc**, bloc E50–E64 (autres carences nutritionnelles), chapitre IV [S1].
- **Pas de sous-code** : E60 est une catégorie terminale (kind="category"), sans subdivision E60.x, sans inclusion ni exclusion propres [S1].
- Métadonnées OFS : utilisable comme diagnostic principal (Para295 = P), sans restriction d'âge ni de sexe, classée **non infectieuse** (Infectious = N) [S1].
- Exclusions héritées du bloc E50–E64 : déshydratation (E86), problèmes alimentaires du nouveau-né (P92.-), séquelles de malnutrition et autres carences nutritionnelles (E64.-), retard de croissance (R62.8) [S1].
- Frontières de codage avec les codes voisins [S1] :
  - **E83.2 — Anomalies du métabolisme du zinc**, inclusion « **Acrodermatitis enteropathica** » : la forme héréditaire par défaut de transport ne se code pas en E60 ;
  - E83 exclut « carence alimentaire en minéraux (E58-E61) » : la carence **d'apport** reste en E60 ;
  - **D53.8 — Autres anémies nutritionnelles précisées** inclut l'« anémie associée à carence en zinc » ;
  - **E61.-** (carences en autres éléments nutritionnels) exclut E64.-, E00-E02 et E83.- ;
  - **E64.8** — Séquelles d'autres carences nutritionnelles ;
  - **R79.0** — Taux anormal de minéraux dans le sang, dont le zinc (valeur biologique isolée sans tableau de carence) ;
  - **T56.5** — Effet toxique du zinc et de ses composés (surdosage).
- Remarque déductive (à présenter comme telle) : une carence **acquise** par malabsorption ou pertes (MICI, bariatrie, nutrition parentérale) n'a pas de libellé distinct dans la CIM-10-GM ; le texte de E83 renvoie la « carence alimentaire » vers E60 [S1].

## 1. Question clinique et enjeu

Un nourrisson allaité, un patient opéré d'un bypass gastrique, un malade de Crohn, un alcoolique cirrhotique ou un patient en nutrition parentérale présente une dermatite périorificielle et acrale qui résiste aux corticoïdes et aux antifongiques, une alopécie, une diarrhée ou des troubles du goût : faut-il penser au zinc, comment interpréter une zincémie basse en présence d'inflammation, et comment corriger la carence avec les produits suisses ?
- La carence acquise est **rare mais sous-diagnostiquée** ; les lésions périorificielles et acrales caractéristiques orientent le diagnostic [S15][S2].
- La supplémentation orale entraîne souvent une **rémission clinique en quelques jours** [S15], avant même la hausse nette du zinc sérique [S14].
- Une revue pédiatrique conclut que l'identification rapide d'une carence en zinc chez le jeune enfant doit être considérée comme une urgence médicale [S14].
- Cas adulte : dermatite étendue traitée à tort comme dermatite de contact et infection herpétique, aggravation jusqu'en soins intensifs avec pneumonie bilatérale ; zincémie basse, amélioration rapide sous zinc [S25].

## 2. Définitions et terminologie

- ESPEN 2022 / exposé suisse (Berger, Lausanne) [S3] :
  - **Déplétion** : perte objectivable d'un micronutriment dans les liquides de l'organisme ou apport inférieur aux recommandations, avec concentration sanguine ou plasmatique sous la valeur de référence.
  - **Carence** : même perte ou apport insuffisant, **associé** à des signes ou symptômes cliniques explicables par le déficit, **ou** à une concentration sous la référence avec effets métaboliques défavorables.
- Carence **marginale** : selon l'OSAV, ses symptômes correspondent à ceux d'une carence importante, en moins prononcés (moindre résistance aux infections, ralentissement de la croissance, troubles du développement cérébral, troubles de l'odorat et du goût) [S5].
- Seuls signes clairement démontrés d'une carence **légère** : ralentissement de la croissance et altération des défenses immunitaires ; le goût et la cicatrisation sont touchés de façon moins constante [S2].
- **Acrodermatite entéropathique (AE)** : malabsorption congénitale du zinc, autosomique récessive, par mutation du gène du transporteur ZIP4 (SLC39A4, chromosome 8q24.3) [S2][S14].
- **Carence néonatale transitoire en zinc (TNZD)** : mutation autosomique dominante de SLC30A2 chez la mère, transfert défectueux du zinc de l'épithélium mammaire au lait ; lait < 25 % des valeurs normales [S14].

## 3. Classifications et stades

Aucune classification en stades officielle n'a été trouvée (lacune). Le dossier permet trois classifications opérationnelles :

**a) Étiologique** (ESPEN [S2], revue pédiatrique [S14], tableau 1) :

| Mécanisme | Exemples | Source |
|---|---|---|
| Apport insuffisant | alimentation riche en phytates, végétarisme et véganisme, anorexie mentale, boulimie, alcoolisme, régimes restrictifs, lait maternel pauvre en zinc (TNZD), NP sans zinc | [S2][S14] |
| Besoins accrus | nourrisson, enfant, adolescent, grossesse, allaitement, prématurité, RCIU, hypercatabolisme | [S2][S14] |
| Malabsorption | grêle court, bariatrie, mucoviscidose, pancréatite chronique, MICI, maladie cœliaque, AE (ZIP4) | [S2][S14] |
| Pertes accrues | entérostomie, fistule entéro-cutanée, diarrhée, brûlures, sepsis, traumatisme, néphropathie, glycosurie, diurétiques, dialyse | [S2][S14] |
| Utilisation altérée / mécanisme incertain | cirrhose alcoolique, diabète, trisomie 21, défauts thymiques | [S2][S14] |

**b) Biochimique** (seuils de population suisses et internationaux, détaillés en §10) : valeurs basses selon le moment du prélèvement [S5] ; valeurs sous le percentile 5 de SKIPOGH [S6].

**c) Épidémiologique (santé publique)** : prévalence de zincémies basses < 5 % faible, 5–10 % modérée, 10–20 % moyennement élevée, > 20 % élevée ; au-delà de 20 %, la carence est un problème de santé publique [S5].

**d) Selon la sévérité clinique** : la forme sévère associe alopécie, éruption du visage, des aines, des mains et des pieds, retard de croissance et de maturation sexuelle et osseuse, retard de cicatrisation, déficit immunitaire, diarrhée, émoussement du goût et de l'odorat [S2] ; la forme légère se limite surtout au ralentissement de croissance et au déficit immunitaire [S2].

## 4. Épidémiologie

### Suisse
- **Donneurs de sang (n = 700, 4 centres CRS)** : zinc sérique moyen 814 µg/L chez la femme (n = 334) et 860 µg/L chez l'homme (n = 366) ; médianes 796 et 845 µg/L ; différence entre sexes de 5,5 % ; pas d'influence de l'âge [S5].
- Prévalence de valeurs basses chez les donneurs : **3,4–10,8 %** (femmes) et **3,2–12,1 %** (hommes) selon le seuil (après-midi ou matin postprandial) ; part effective probablement < 10 % ; **pas de carence au niveau de la population** suisse [S5].
- **Végétariens et végétaliens (n = 107)** : moyennes 769 µg/L (femmes) et 788 µg/L (hommes), significativement inférieures à celles des donneurs ; valeurs basses chez **9,9–22,3 %** des femmes et **8,6–28,7 %** des hommes ; risque moyennement élevé ; effectif trop petit pour conclure définitivement [S5].
- Au moins 96,7 % des valeurs mesurées se situent dans l'intervalle clinique de 600–1200 µg/L [S5].
- Apport (menuCH) : adéquat chez la femme ; chez l'homme, 12 mg/j calculés contre 14 mg/j recommandés pour un apport moyen en phytates [S5].
- Compléments : près d'un tiers de la population suisse en consomme au moins un ; 9 % des consommateurs prennent un produit contenant du zinc ; 46 % des végétariens et végétaliens, avec un apport moyen de 7,3 mg/j [S5].
- **Vaud 2023 (hommes)** : médiane 824 ng/mL chez 196 détenus contre 749 ng/mL dans la population générale (n = 189) ; sous la limite SKIPOGH chez 6,12 % vs 9,52 % (NS) ; sous 700 ng/mL chez 17,3 % vs 32,3 % (p < 0,001) [S6].
- Facteurs associés à un zinc plus bas (détenus vaudois) : **âge** (β = −3,30 ng/mL par année, p = 0,002) et établissement à régime strict et surpeuplé (β = −66,9, p = 0,03) [S6].
- Aucune donnée d'incidence de E60 codée en Suisse n'a été trouvée (lacune).

### Europe et monde
- Peu de données existent sur la carence en zinc en Europe ; l'OMS estime que plus d'un milliard d'individus en souffrent [S5].
- La carence en zinc figure, avec celles en iode, fer et vitamine A, parmi les principaux facteurs de risque sanitaires mondiaux [S2].
- Environ 20 % de la population mondiale aurait une carence légère à modérée ; près de la moitié des enfants dans certains pays à revenus faibles ou intermédiaires [S14].
- Étude danoise (n = 357) : moyenne 733 µg/L [S5].
- MICI (méta-analyse, 9 études) : prévalence de carence **54 %** dans la maladie de Crohn (n = 1677) et **41 %** dans la rectocolite (n = 806) ; globale 50 % (hétérogénéité I² = 96 %) [S16].
- AE héréditaire : incidence **1/500 000**, sans prédominance de sexe ni d'origine ; la consanguinité est un indice anamnestique [S14].
- Après chirurgie bariatrique (pratique suisse), le zinc figure parmi les carences fréquentes avec calcium, fer, B12 et vitamine D [S20].

## 5. Normal → pathologique (physiologie, mécanisme causal)

### Normal
- Plus de 300 métalloenzymes à zinc : anhydrase carbonique, **phosphatase alcaline**, ARN et ADN polymérases, alcool déshydrogénase ; les protéines à « doigts de zinc » contrôlent la transcription de l'ADN [S2].
- Trois classes de rôles : structural, catalytique, régulateur ; signalisation endocrine, paracrine, autocrine ; le zinc réduit la sécrétion d'insuline et freine sa clairance hépatique [S2].
- Défense antioxydante : composant de la superoxyde dismutase Cu/Zn cytoplasmique, inhibition de la NADPH oxydase, induction des métallothionéines [S2].
- Fonctions cliniques : complexes avec l'insuline et le glucagon au pancréas ; maturation des gonades, stéroïdogenèse testiculaire et fertilité ; fonction des lymphocytes T, macrophages et granulocytes [S7].
- La carence touche d'abord les **tissus à renouvellement rapide** (spermatozoïdes, embryon, cellules immunocompétentes, tissu de granulation) [S7].
- Répartition : > 85 % du zinc corporel dans le muscle squelettique et l'os ; **0,1 %** seulement dans le plasma, lié à 70 % à l'albumine, concentration étroitement régulée vers 10–17 µmol/L [S2]. Revue pédiatrique : 2–3 g au total ; 80 % lié à l'albumine et 20 % à l'α2-macroglobuline [S14]. Environ 95 % du zinc est intracellulaire [S7].
- **Aucun réservoir spécifique** : l'apport doit être permanent ; l'homéostasie passe par l'adaptation de l'absorption et de l'excrétion intestinale [S7][S5].
- Absorption : surtout jéjunale [S2] (duodénum et grêle proximal selon la FI [S7]) par le transporteur **ZIP4**, sortie vers le sang par les transporteurs **ZnT** [S14] ; 10–40 % du zinc alimentaire [S7], 5–30 % selon une autre FI [S8].
- Excrétion : biliaire importante avec cycle entéro-hépatique, perte digestive nette 2–4 mg/j ; urinaire ≈ 0,5 mg/j ; pertes par la peau et les cheveux [S2]. Fèces 88 %, urine 2 % [S8].
- **Phytates** (céréales complètes, légumineuses, noix) : forment des complexes peu solubles qui empêchent l'absorption ; les aliments d'origine animale (produits laitiers, œufs, poisson, viande) apportent du zinc très biodisponible [S5][S7].
- Lait maternel : > 3 mg/L au début, < 1 mg/L à 6 mois, indépendamment de l'apport maternel ; le nourrisson de 6 mois dépend ensuite de la diversification (viande) [S14].
- Fœtus : l'essentiel du transfert materno-fœtal se fait au cours des **dix dernières semaines** de grossesse [S14].

### Pathologique
- Apport ou absorption insuffisants → baisse de l'activité des enzymes zinc-dépendantes → défaut de synthèse protéique et nucléique → **retard de croissance et de cicatrisation** [S2].
- Immunité : la carence altère la survie, la prolifération et la maturation des monocytes, polynucléaires, cellules NK, lymphocytes T et B ; la carence aiguë diminue l'immunité innée et adaptative, la carence chronique **augmente l'inflammation** [S2].
- Peau : hypothèse d'un excès local d'ATP dans les kératinocytes et les cellules de Langerhans (le zinc est cofacteur de l'hydrolyse ATP → AMP), d'où inflammation et apoptose ; le zinc favorise aussi la ré-épithélialisation via les métalloprotéinases [S14].
- AE : perte de fonction de ZIP4 → défaut d'absorption intestinale → carence systémique ; lait de vache : ligand de haut poids moléculaire qui gêne l'absorption, d'où début après le sevrage [S14].
- Prématuré : réserves réduites, balance négative jusqu'au 60e jour, besoins de croissance élevés [S14].
- Nutrition parentérale : apport insuffisant ; la cystéine ajoutée augmente les pertes urinaires de zinc [S14].
- Inflammation : redistribution du zinc de l'albumine plasmatique vers le foie (métallothionéine), corrélée à l'IL-6, l'IL-8 et le TNF-α ; la zincémie chute dès que la CRP dépasse 20 mg/L [S2].
- Hépatopathie : zinc tissulaire réduit dans la cirrhose ; association avec l'encéphalopathie hépatique décrite dans des cas [S19][S18].

## 6. Étiologies et facteurs de risque

- Cause principale : **apport insuffisant en zinc biodisponible** [S5][S2].
- Groupes à besoins accrus : nourrisson, enfant, adolescent, femme enceinte et allaitante [S2].
- Régimes : végétarisme, véganisme, alimentation riche en phytates, troubles alimentaires (anorexie mentale, boulimie) [S2][S5] ; régime cétogène détourné pour maigrir [S14].
- Malabsorption : grêle court, **chirurgie bariatrique** (sleeve, bypass Roux-en-Y, dérivation bilio-pancréatique), mucoviscidose, pancréatite chronique, MICI [S2][S14] ; maladie cœliaque (zinc normalisé par le régime sans gluten) [S14] ; duodéno-pancréatectomie [S14].
- Pertes : entérostomie, fistule, chylorrhée ; pertes urinaires en hypercatabolisme (brûlures, traumatisme, sepsis), néphropathie, alcoolisme, dialysat, nombreux médicaments ; épuration extrarénale prolongée [S2]. Syndrome néphrotique et glycosurie (diurèse osmotique, plus de zinc libre filtré par hypoalbuminémie) [S14].
- Nutrition parentérale prolongée sans ou avec peu de zinc ; nutrition entérale complète prolongée ; jeûne ; cirrhose alcoolique ; diabète [S2].
- Médicaments et chélateurs : pénicillamine, EDTA, DMPS [S7] ; diurétiques, valproate [S14] ; apports simultanés de fer, cuivre ou calcium [S7].
- Facteurs sociaux suisses : âge plus élevé, conditions de détention défavorables (association) [S6].

## 7. Anamnèse et symptômes (fréquences)

- Peau : dermatite **périorificielle et acrale symétrique** (plaques érythémato-squameuses, vésicules, bulles, croûtes), alopécie, retard de cicatrisation ; paronychie, onychodystrophie, onycholyse [S14][S15].
- Muqueuses et organes des sens : glossite, chéilite, stomatite, **dysgueusie/hypogueusie**, dysosmie, conjonctivite, blépharite avec photophobie [S14][S2].
- Digestif : diarrhée, anorexie [S14][S2].
- Infections : récidivantes ; l'enfant peut consulter pour fièvre plutôt que pour les lésions cutanées [S14].
- Croissance et puberté : retard de croissance, retard pubertaire, hypogonadisme [S14][S2].
- Neurologie : retard de développement, troubles du comportement, tremblement intentionnel, troubles de concentration, héméralopie, anosmie [S14].
- Musculo-squelettique : baisse de la masse maigre, risque fracturaire accru [S14].
- Grossesse : retard de croissance fœtale, petit poids de naissance, accouchement prématuré [S14].
- Fréquence : la **triade** dermatite acrale + alopécie + diarrhée est observée dans **moins de 20 %** des AE [S14].
- Indices anamnestiques : âge de début (AE : 4–10 semaines chez le nourrisson nourri au biberon ou peu après le sevrage ; TNZD : plus tôt chez l'enfant exclusivement allaité, guérison après le sevrage), consanguinité, frère ou sœur atteint pendant l'allaitement, régime, chirurgie digestive, NP [S14].
- Les fréquences des autres symptômes dans la carence acquise de l'adulte n'ont pas été trouvées (lacune).

## 8. Examen clinique

- Lésions érythémateuses, érosives, croûteuses, nettement limitées, symétriques, aux joues, oreilles, cou, périnée, doigts et orteils ; bulles interdigitales ; plaque périnéale érosive chez le nouveau-né [S14].
- Surinfection fréquente des lésions : *Staphylococcus aureus* (dont SARM), *Pseudomonas aeruginosa*, *Klebsiella pneumoniae*, *Candida* ; risque d'infection invasive et de sepsis [S14].
- Signes associés : alopécie (jusqu'à universelle), paronychie, cassure de la courbe staturo-pondérale [S14].
- Signes de la cause : enfant en mauvaise croissance malgré des apports caloriques suffisants (prématuré, mucoviscidose) [S14][S17].
- Sensibilité et spécificité des signes cliniques : non trouvées (lacune).

## 9. Drapeaux rouges et urgences

- **Nourrisson** avec dermatite périorificielle/acrale, irritabilité, diarrhée chronique ou alopécie : doser la zincémie, même en présence de fièvre ou de facteurs confondants [S14].
- **Surinfection et sepsis** sur peau lésée (SARM, *Pseudomonas*, *Klebsiella*, *Candida*) : présentation fréquente aux urgences pédiatriques par la fièvre [S14].
- AE non traitée : défaillance multiviscérale et décès possibles ; historiquement souvent mortelle avant la supplémentation [S14].
- Adulte à risque avec dermatite grave résistante au traitement : la carence peut évoluer jusqu'en soins intensifs [S25].
- **Brûlures > 20 % de surface corporelle** : pertes exsudatives majeures, apport IV 30–35 mg/j pendant 2–3 semaines [S2].
- Intoxication aiguë (> 1–2 g de zinc ingérés) : symptômes digestifs caustiques dont hématémèse, néphrite interstitielle ou nécrose tubulaire aiguë, SDRA, nécrose hépatique [S2].
- Délais d'action chiffrés : non trouvés (lacune).

## 10. Examens complémentaires

### Zinc plasmatique ou sérique (examen de référence)
- **Indication** : confirmer une carence clinique et surveiller l'apport (ESPEN recommandation 13.2, grade A) ; **CRP et albumine simultanées obligatoires** pour l'interprétation [S2].
- Méthode : ICP-MS de préférence, ou absorption atomique ; sang total, plasma, sérum, urine ou cheveux [S2]. Le sérum évite les anticoagulants, source de contamination [S5].
- Valeurs de référence :
  - ESPEN : concentration plasmatique régulée vers **10–17 µmol/L** [S2].
  - Intervalle clinique de laboratoire : **600–1200 µg/L** (≈ 9,2–18,3 µmol/L, calcul de l'agent) [S5].
  - SKIPOGH (Suisse, hommes adultes, P5–P95) : **620–999 ng/mL** (≈ 9,5–15,3 µmol/L, calcul de l'agent) [S6].
  - FI suisse : 55–150 µg/100 mL (environ 8–22 µmol/L) chez l'adulte [S8].
  - Revue pédiatrique : 68–107 µg/dL [S14].
- Seuils de population (percentile 2,5, IZiNCG/OMS/AIEA/UNICEF) : **matin après un repas 660 µg/L (femme) et 700 µg/L (homme)** ; **après-midi 590 et 610 µg/L** [S5] ; seuil 700 ng/mL utilisé en recherche [S6].
- **Pièges** :
  - Variation de 20 % sur 24 h liée aux repas [S2] ; baisse postprandiale jusqu'à ≈ 19 % [S6] ; le jeûne nocturne fait remonter la zincémie, rythme circadien [S5].
  - **Inflammation** : zincémie basse dès CRP > 20 mg/L [S2] ; au-delà de 80 mg/L, pratiquement plus de valeurs normales [S3]. Correction BRINDA possible avec CRP ou AGP [S2].
  - **Hypoalbuminémie** : peut mimer une carence ; interpréter avec la clinique [S14][S2].
  - Contamination par la peau ou le matériel ; **hémolyse** → fausse élévation ; prélever le matin à jeun, aiguille en acier inoxydable, tube sans oligo-éléments [S14].
  - La zincémie reste dans la norme lors d'une carence récente (homéostasie) et ne baisse nettement qu'en carence durable ou sévère [S5] ; souvent normale dans la carence primaire légère [S14] ; pas de biomarqueur fiable du zinc corporel total [S6].
- Conversion : 1 mg/L = 15,3 µmol/L ; 1 µmol/L = 65,4 µg/L [S2].

### Autres examens
- **Phosphatase alcaline basse** (métalloenzyme à zinc) : marqueur d'appoint du diagnostic et indice indirect de la réponse au traitement [S14][S15] ; exemples : 42 et 68 U/L (référence 122–469) [S14].
- Zinc des leucocytes et plaquettes : baisse plus rapide mais technique difficile à l'hôpital ; zinc érythrocytaire peu modifié ; zinc des cheveux non utilisé en pratique hospitalière [S2].
- Albumine et CRP : obligatoires [S2] ; CRP lors de toute analyse de micronutriment (recommandation 3, grade B) [S2].
- **Biopsie cutanée** : non spécifique, indiscernable d'autres dermatites carentielles ; parakératose alternant avec orthokératose, amincissement de la granuleuse, acanthose, puis ballonisation et pâleur des kératinocytes ; aspect psoriasiforme chronique ; sert surtout à exclure d'autres diagnostics [S14].
- **Génétique** : SLC39A4 (AE) ; SLC30A2 chez la mère (TNZD) [S14].
- Bilan de cause : cuivre, fer, vitamines A et D [S14] ; malabsorption, maladie cœliaque [S14] ; bilan bariatrique annuel [S21].
- Zinc et vitamine A : le rétinol sérique peut être faussé par la carence en zinc [S2].
- Indications de dosage (ESPEN recommandation 13.1, GPP) : pertes digestives ou cutanées accrues ; début d'une NP prolongée ; tous les **6–12 mois** en NP de longue durée [S2].

## 11. Diagnostic différentiel

| Diagnostic | Élément discriminant | Source |
|---|---|---|
| Acrodermatite entéropathique héréditaire (E83.2) | début néonatal (biberon 4–10 semaines ou sevrage), consanguinité, rechute à l'arrêt du zinc, SLC39A4 ; dose 3 mg/kg/j à vie | [S1][S14][S2] |
| Carence néonatale transitoire (TNZD) | enfant exclusivement allaité, frère/sœur atteint, réponse à 0,5–1 mg/kg/j, guérison après sevrage ; SLC30A2 maternel | [S14] |
| Pellagre (carence en niacine) | **photosensibilité**, absente des autres dermatoses carentielles | [S14] |
| Carence en biotine (dont biotinidase) | lésions de type AE ; zinc et PAL normaux | [S14] |
| Aciduries organiques et autres erreurs innées (acidurie méthylmalonique, propionique, leucinose, citrullinémie, PCU…) | retard de développement, acidose céto-lactique, hyperammoniémie ; zinc et PAL **normaux** (« acrodermatitis dysmetabolica ») | [S14] |
| Déficit en entérokinase | diarrhée sévère, hypoprotidémie, œdèmes ; zinc normal | [S14] |
| Érythème nécrolytique migrateur (glucagonome) | régresse après exérèse tumorale ; carence en acides aminés | [S14] |
| Psoriasis, dermatite atopique sévère, lichen plan buccal, Behçet, dermatoses bulleuses auto-immunes ou héréditaires (épidermolyse bulleuse), alopécie universelle | zincémie et PAL normales, histologie spécifique ; la zincémie peut toutefois être basse dans ces maladies | [S14] |
| Dermatite de contact, infection herpétique | échec du traitement spécifique, terrain à risque, zincémie basse | [S25] |
| Mucoviscidose | dermatite acrale + malabsorption (anémie, hypoalbuminémie), retard de croissance | [S14][S17] |
| Kwashiorkor, carence en acides gras essentiels | autres causes de dermatite périorificielle ou acrale carentielle | [S14] |
| Zincémie basse d'inflammation (pas de carence) | CRP > 20 mg/L, normalisation avec la guérison | [S2] |
| Taux anormal isolé (R79.0) | valeur biologique sans tableau clinique | [S1] |

## 12. Prise en charge suisse

### Principes (ESPEN 2022)
- Voies orale, entérale ou parentérale selon la fonction digestive ; supplémentation combinée au support nutritionnel ou séparée (recommandation 13.9, GPP) [S2].
- **Carence acquise** : **0,5–1 mg/kg/j de zinc élémentaire per os pendant 3–4 mois** ; les sels organiques (histidinate, gluconate, orotate) sont mieux tolérés que le sulfate et le chlorure (recommandation 13.7, GPP) [S2].
- **Acrodermatite entéropathique** : **3 mg/kg/j à vie**, adaptés à la zincémie (recommandation 13.8, grade 0) [S2] ; zincémie tous les 3–6 mois [S14].
- TNZD : 0,5–1 mg/kg/j, arrêt après 3–4 mois ou après la diversification [S14].
- Nutrition entérale : au moins 10 mg/j pour 1500 kcal (13.3, grade A) [S2].
- Nutrition parentérale : 3–5 mg/j IV sans pertes anormales (13.4, grade B) ; jusqu'à 12 mg/j IV en cas de fistules, stomies, diarrhée, tant que persistent les pertes (13.5, grade 0) ; brûlures > 20 % SC : 30–35 mg/j IV pendant 2–3 semaines (13.6, grade B) [S2]. Équilibre positif obtenu avec 3 mg/j IV sans diarrhée ; 6 mg/j suffisent chez presque tous ; jusqu'à 12 mg/j en cas de pertes digestives [S2].
- Épuration extrarénale continue : pertes accrues mais bilan proche de zéro par contamination des solutions [S2].
- Mucoviscidose à risque : < 2 ans 1 mg/kg/j (max 15 mg), 2–18 ans 15 mg/j, adultes 25 mg/j, pendant 6 mois ; prises fractionnées mieux tolérées [S17]. Enzymes pancréatiques : améliorent l'absorption du zinc [S17].
- Hépatite alcoolique sévère : multivitamines et zinc par voie orale raisonnables, carence fréquente [S18]. Cirrhose : zinc et vitamine A peuvent améliorer la dysgueusie ; pas d'effet thérapeutique démontré du zinc oral sur l'encéphalopathie hépatique [S18] ; micronutriments en cas de carence confirmée ou suspectée (EASL) [S19].
- Après bypass gastrique (pratique suisse) : **zinc 20–40 mg/j**, à jeun, pas avec le fer ni le calcium ; troubles digestifs fréquents, prise irrégulière → fluctuations [S20] ; multivitamines avec oligo-éléments au long cours, à vie après chirurgie malabsorptive ; contrôles annuels et vérification du succès du traitement d'une carence [S21].
- Peau : penser à la surinfection bactérienne ou fongique [S14].
- Réponse : amélioration clinique en quelques jours, avant la hausse nette de la zincémie [S14][S15].

### Médicaments suisses (FI Swissmedic, datées)

**Zink Biomed® 20 / 10** (D-gluconate de zinc ; 140 mg = 20 mg Zn) — FI avril 2023 [S7]
- Indications : carence alimentaire en zinc ; pertes accrues ou malabsorption (pénicillamine et chélateurs, sprue, Crohn, cirrhose) ; besoins accrus (chirurgie, traumatisme, brûlures, grossesse, allaitement) ; maladie de Wilson ; acrodermatite entéropathique.
- Posologie adulte : carence/besoins accrus 1–2 cp/j (20–40 mg) ; chélateurs 1 cp/j ; AE jusqu'à 5 cp/j ; Wilson 80–180 mg/j, jamais < 80 mg/j, seulement après déplétion par chélateurs.
- Prise au moins 1 h avant ou 2 h après un repas, avec du liquide.
- Enfant et adolescent : sécurité et efficacité non étudiées.
- Contre-indications : insuffisance rénale sévère, défaillance rénale aiguë, hypersensibilité ; dans la maladie de Wilson, association avec pénicillamine, EDTA ou trientine.
- Précautions : au-delà de 6 mois, contrôler aussi le **cuivre** (carence en cuivre, anémie).
- Interactions : acide phytique ; chélateurs ; sels de fer, cuivre, calcium (réduisent l'absorption du zinc) ; le zinc réduit l'absorption des quinolones (ciprofloxacine), tétracyclines, calcium, fer, cuivre → **intervalle ≥ 2 h**.
- Grossesse : études contrôlées sans risque fœtal.
- Effets indésirables : rares nausées, vomissements ; diarrhée au-delà de 50 mg/j.
- Surdosage : céphalées, vertiges, ataxie, goût métallique, troubles digestifs, léthargie, fièvre, troubles électrolytiques, hausse de l'amylase, de la lipase et de la PAL ; arrêt, éventuellement D-pénicillamine.
- Catégorie de remise : 20 mg [B], 10 mg [D] [S23].

**Burgerstein Zinc 15 mg / 30 mg** (gluconate de zinc) — FI juillet 2025 [S8]
- Indication : carence en zinc liée à l'alimentation, pouvant s'accompagner d'infections plus fréquentes, de problèmes cutanés ou d'un retard de cicatrisation.
- Posologie : 15 mg/j, 1 h avant ou 2 h après le repas ; non établi chez l'enfant et l'adolescent.
- Contre-indications : insuffisance rénale aiguë, troubles sévères de la fonction rénale ; prudence si insuffisance rénale modérée.
- Usage prolongé : déficit en cuivre et anémie.
- Interactions : cuivre, fer ; tétracyclines (absorption réduite jusqu'à 50 %) et pénicillamine (chélates) → espacer d'au moins 5 h ; quinolones ; phosphore, calcium, café, farine complète, histidine.
- Grossesse et allaitement : possible à la dose correspondant aux besoins journaliers.
- Conduite : aucune influence.
- Effets indésirables : rares brûlures d'estomac, vomissements, diarrhée, nausées ; à > 300 mg/j : hausse amylase, lipase, PAL, anémie sidéroblastique réversible avec granulocytopénie.
- Surdosage : arrêt immédiat, D-pénicillamine.
- Catégorie de remise : 30 mg [B], 15 mg [D] [S23].

**Oligo-éléments parentéraux (adultes)**
- **Addaven** (10 mL/j) : zinc 77 µmol sous forme de chlorure (≈ 5,0 mg Zn, calcul de l'agent) ; prudence en insuffisance biliaire ou rénale ; surveillance régulière des oligo-éléments en NP prolongée ; FI janvier 2021 [S9].
- **NUTRYELT** (10 mL/j) : zinc 10 mg (153 µmol) ; contre-indiqué en cholestase prononcée (bilirubine > 140 µmol/L), maladie de Wilson, hémochromatose ; en NP de moyenne ou longue durée, carences plus fréquentes en fer, zinc et sélénium → apport supplémentaire sélectif ; FI novembre 2019 [S10].
- **Tracutil** (10 mL/j ; 20–30 mL/j en besoins accrus) : zinc 3,27 mg (50 µmol) ; contre-indiqué jusqu'à 11 ans ; FI mars 2026 [S13].

**Oligo-éléments parentéraux (pédiatrie)**
- **NUTRYELT JUNIOR** : 100 µg de zinc/mL ; 1 mL/kg/j jusqu'à 20 mL ; chez le prématuré, ajouter du zinc pour atteindre **450–500 µg/kg/j** ; prudence en insuffisance rénale (accumulation de zinc) ; FI décembre 2018 [S11].
- **Peditrace** : zinc 3,82 µmol/mL (≈ 250 µg/mL, calcul de l'agent) ; 1 mL/kg/j jusqu'à 15 kg, 15 mL/j au-delà ; contrôle des oligo-éléments après 4 semaines ; FI novembre 2025 [S12].
- Aucune solution suisse de zinc injectable seul n'a été trouvée par `tools/swissmedic_fi.py` (requêtes « zinc », « zink ») (lacune).

### Toxicité et traitement du surdosage
- Toxicité au-delà de 1–2 g ingérés ; voies digestive, cutanée, respiratoire (inhalation professionnelle de chlorure de zinc), parentérale (NP mal préparée) [S2].
- Toxicité chronique : surtout **carence en cuivre** (anémie sidéroblastique, granulocytopénie, myélodysplasie, polyneuropathie sensitivomotrice ascendante) ; mécanisme : induction de métallothionéine, qui fixe préférentiellement le cuivre — principe utilisé dans la maladie de Wilson [S2].
- Traitement : intoxication aiguë → antiémétiques, liquides, IPP ou anti-H2, éventuellement irrigation intestinale ; chélation CaNa2EDTA ou DTPA ; intoxication chronique → sulfate de cuivre [S2].
- Hémodialyse : des doses > 45 mg/j peuvent être nécessaires pour élever la zincémie, avec risque de carence en cuivre et de pancytopénie (revue japonaise, contexte seulement) [S22].

## 13. Complications et pronostic

- AE non traitée : défaillance multiviscérale et décès ; souvent mortelle avant la supplémentation [S14].
- Infections cutanées et invasives, sepsis [S14].
- Retard de croissance, retard pubertaire, troubles neurodéveloppementaux [S14][S2].
- Grossesse : RCIU, petit poids de naissance, prématurité [S14].
- Anémie associée à la carence en zinc (code D53.8) [S1] ; hémodialyse : carence associée à une moindre réponse aux agents stimulant l'érythropoïèse [S22].
- Pronostic sous traitement : rémission en quelques jours [S15] ; guérison des lésions en 2 semaines (TNZD) à 3 mois (alopécie, cas d'AE) dans les cas rapportés [S14].
- Rechute à l'arrêt : évoque une forme héréditaire, y compris chez l'adolescent ou l'adulte [S14].
- Complications du traitement prolongé : carence en cuivre, anémie [S7][S8][S2].
- Séquelles codées en E64.8 [S1].

## 14. Suivi, prévention, dépistage

- Pas de dépistage populationnel : la carence n'est pas un problème de santé publique en Suisse (prévalence de valeurs basses < 10 %) [S5].
- Apports de référence suisses (OSAV 2022) [S4] :

| Groupe | Zinc (mg/j) |
|---|---|
| Nourrisson 7–11 mois | 2,9 |
| 1–3 ans | 4,3 |
| 4–6 ans | 5,5 |
| 7–10 ans | 7,4 |
| 11–14 ans | 10,7 |
| 15–17 ans, fille / garçon | 11,9 / 14,2 |
| Femme 18–65 ans | 7,5 / 9,3 / 11,0 / 12,7 selon l'apport en phytates |
| Homme 18–65 ans | 9,4 / 11,7 / 14 / 16,3 selon l'apport en phytates |
| > 65 ans, femme / homme | 7,0–10,0 / 11,0–16,0 selon les phytates |
| Grossesse (3 trimestres) | 9,1 / 10,9 / 12,6 / 14,3 selon les phytates |
| Allaitement | 10,4 / 12,2 / 13,9 / 15,6 selon les phytates |

- ESPEN simplifie l'apport de référence adulte à 8–15 mg/j [S2].
- Prévention alimentaire : privilégier les sources animales riches en zinc biodisponible ; attention aux phytates des régimes végétariens [S5].
- Dosages de suivi : zinc + CRP + albumine ; début et tous les 6–12 mois en NP prolongée [S2] ; zincémie tous les 3–6 mois dans l'AE [S14] ; cuivre au-delà de 6 mois de zinc [S7] ; cuivre, fer, vitamines A et D en cas de traitement [S14].
- Prématuré allaité après la sortie : envisager une supplémentation en zinc [S14].
- Bariatrie : suivi à vie, multivitamines avec oligo-éléments, bilans annuels [S21] ; zinc souvent à supplémenter [S20].

## 15. Situations particulières

- **Grossesse et allaitement** : besoins accrus (tableau OSAV) [S4][S2] ; zinc utilisable à dose correspondant aux besoins [S8] ; pas de risque fœtal dans les études contrôlées [S7] ; Addaven : pas d'effet attendu à dose adéquate, éliminé dans le lait, utilisation en allaitement seulement si nécessaire [S9].
- **Nourrisson et enfant** : AE, TNZD, prématuré, RCIU [S14] ; FI orales suisses sans posologie pédiatrique établie [S7][S8] ; doses pédiatriques fondées sur ESPEN (0,5–1 mg/kg/j ; AE 3 mg/kg/j) [S2] et la mucoviscidose [S17] ; NP : Nutryelt Junior, Peditrace [S11][S12].
- **Sujet âgé** : zinc plus bas avec l'âge chez les hommes vaudois [S6] ; pas d'effet de l'âge chez les donneurs de sang [S5].
- **Insuffisance rénale** : zinc oral contre-indiqué en insuffisance rénale sévère ou aiguë [S7][S8] ; NP : accumulation possible, prudence [S9][S10][S11] ; épuration extrarénale prolongée et dialysat = pertes [S2] ; hémodialyse : carence fréquente (revue japonaise) [S22].
- **Insuffisance hépatique et cholestase** : cholestase prononcée = contre-indication de Nutryelt [S10] ; élimination biliaire réduite → accumulation de zinc, cuivre, manganèse [S10][S11] ; cirrhose : dysgueusie, encéphalopathie [S18][S19].
- **Maladie de Wilson** : le zinc est un traitement (induction de métallothionéine, baisse de l'absorption du cuivre) [S2][S7].
- **Végétariens et végétaliens** : groupe à risque en Suisse [S5].

## 16. Spécificités suisses

- Codage : E60 non infectieuse (méta OFS) [S1] ; aucune obligation de déclaration OFSP n'a été trouvée pour la carence en zinc (lacune : liste OFSP non consultée pour ce point).
- Médicaments : Zink Biomed (Biomed AG, Dübendorf) et Burgerstein Zinc (Antistress SA) autorisés ; catégories B ou D selon le dosage [S7][S8][S23] ; aucune mention de la Liste des spécialités (SL) dans AmiKo (à confirmer sur la SL officielle) [S23].
- Remboursement après bariatrie : selon la pratique suisse décrite, les caisses ne paient que la supplémentation **en cas de carence**, pas les multivitamines préventives [S20].
- Aptitude à la conduite : le zinc oral n'a aucune influence [S8] ; pas de donnée sur la maladie elle-même (lacune).
- Toxicité professionnelle (inhalation de chlorure de zinc) codée T56.5 [S2][S1] ; règles Suva non trouvées (lacune).
- AI, LiMA : non trouvés (lacune).
- Position de l'Analysenliste (OFSP) pour le zinc sérique : non lue (lacune).
- OSAV : statut en zinc de la population, apports de référence, consommation de compléments [S4][S5].

## 17. Critères formels du diagnostic (→ `div.alert`)

Aucun critère consensuel publié n'a été trouvé (lacune). Conjonction opérationnelle fondée sur les définitions ESPEN :
1. **Situation à risque** : apport insuffisant ou riche en phytates, besoins accrus, malabsorption, pertes, NP [S2][S14].
2. **Signes cliniques compatibles** : dermatite périorificielle et acrale, alopécie, diarrhée, retard de croissance ou de cicatrisation, infections, dysgueusie [S2][S14].
3. **Zinc plasmatique ou sérique bas**, interprété avec **CRP et albumine** (non interprétable si CRP > 20 mg/L) et l'heure du prélèvement [S2][S5].
4. Arguments d'appoint : **phosphatase alcaline basse** [S14][S15] ; **réponse rapide au zinc** [S14][S15].
- Carence = 1 + (2 ou 3 avec effets métaboliques) ; déplétion = valeur basse ou pertes sans signes [S3].
- **Codage** : E60 si carence d'apport ; **E83.2** si acrodermatite entéropathique héréditaire ; D53.8 si anémie liée ; R79.0 si taux anormal isolé [S1].

## 18. Paramètres clés chiffrés (→ `div.key`)

- Zinc plasmatique : **10–17 µmol/L** (ESPEN) [S2] ; intervalle clinique **600–1200 µg/L** [S5] ; SKIPOGH hommes suisses **620–999 ng/mL** [S6].
- Seuils de population : **660 µg/L (F) / 700 µg/L (H)** le matin après un repas ; **590 / 610 µg/L** l'après-midi [S5].
- Conversion : **1 µmol/L = 65,4 µg/L** [S2].
- Inflammation : zincémie abaissée dès **CRP > 20 mg/L** [S2] ; presque plus de valeurs normales si **CRP > 80 mg/L** [S3].
- Variation circadienne et prandiale : **≈ 20 %** [S2][S6].
- Plasma = **0,1 %** du zinc corporel, **70 %** lié à l'albumine [S2] ; > 85 % dans muscle et os [S2].
- Pertes : digestives nettes **2–4 mg/j**, urinaires **0,5 mg/j** [S2].
- Apport adulte : **8–15 mg/j** (ESPEN) [S2] ; OSAV femme 7,5–12,7, homme 9,4–16,3 mg/j selon les phytates [S4].
- Traitement carence acquise : **0,5–1 mg/kg/j pendant 3–4 mois** ; AE **3 mg/kg/j à vie** [S2].
- NP : **3–5 mg/j** IV ; pertes digestives **jusqu'à 12 mg/j** ; brûlures > 20 % : **30–35 mg/j pendant 2–3 semaines** [S2] ; prématuré **450–500 µg/kg/j** [S11].
- Nutrition entérale : **≥ 10 mg/1500 kcal** [S2].
- Bariatrie (bypass) : **20–40 mg/j** [S20].
- Toxicité aiguë : **> 1–2 g** [S2] ; anémie sidéroblastique à **> 300 mg/j** [S8] ; diarrhée **> 50 mg/j** [S7].
- MICI : prévalence **54 % (Crohn), 41 % (RCH)** [S16] ; AE : **1/500 000** [S14] ; triade complète **< 20 %** des AE [S14].
- Suisse : donneurs de sang **838 µg/L** en moyenne ; valeurs basses **3–12 %** ; végétariens **9–29 %** [S5].

## 19. Sous-codes CIM-10-GM couverts

- **E60** : catégorie terminale, **pas de sous-code** E60.x dans la CIM-10-GM 2024 [S1].
- Codes voisins traités comme frontières ou différentiels, non comme contenu de E60 : E83.2 (acrodermatitis enteropathica), D53.8 (anémie par carence en zinc), E61.-, E64.8, R79.0, T56.5 [S1].

## 20. Points d'examen fédéral

- PROFILES (correspondance pédagogique du dépôt) : SSP **16** perte de poids/malnutrition, **138** cachexie et malnutrition, **170** carences nutritionnelles [S24] ; situations utiles : **59** diarrhée, **90** retard de cicatrisation, **92** perte de cheveux, **94** troubles unguéaux, **95** rougeur cutanée ou muqueuse, **184** retard de croissance et de puberté, **198** malnutrition et sarcopénie [S24].
- Pièges classiques tirés du dossier :
  1. Interpréter une zincémie basse **sans CRP ni albumine** : l'inflammation et l'hypoalbuminémie la font baisser sans carence [S2][S14].
  2. Ignorer l'**heure du prélèvement** et le repas (−20 %) [S2][S5].
  3. Une zincémie normale n'exclut pas une carence récente ou légère [S5][S14].
  4. Confondre **E60** (carence d'apport) et **E83.2** (AE héréditaire, traitement à vie) [S1][S2].
  5. Traiter une dermatite acrale et périorificielle comme une mycose ou un eczéma de contact [S14][S25].
  6. Oublier la **phosphatase alcaline basse** comme indice [S14][S15].
  7. Supplémenter longtemps sans contrôler le **cuivre** (anémie, neutropénie, polyneuropathie) [S2][S7].
  8. Prendre le zinc avec fer, calcium, quinolones ou tétracyclines (espacer ≥ 2 h, 5 h selon la FI Burgerstein) [S7][S8].
  9. Pellagre : la **photosensibilité** distingue cette dermatose carentielle [S14].
  10. Végétariens et patients bariatriques : groupes à risque en Suisse [S5][S20].

## Lacunes (requêtes tentées)

1. Orphanet (fiche acrodermatite entéropathique, ORPHA 37) : page bloquée par une vérification anti-robot (WebFetch).
2. ESPGHAN/ESPEN/ESPR/CSPEN 2018 « pediatric parenteral nutrition: iron and trace minerals » (doi:10.1016/j.clnu.2018.06.949) : PDF indisponible (dépôt ORBi fermé, résumé PubMed absent) ; la dose du prématuré provient de la FI Nutryelt Junior [S11].
3. Glutsch 2019 (JDDG) : texte intégral Wiley refusé (HTTP 403) ; résumé seul [S15].
4. ESPGHAN/ESPID 2014 gastro-entérite aiguë : le résumé ne mentionne pas le zinc ; texte intégral non lu.
5. Analysenliste OFSP (position et tarif du zinc sérique) : recherche web sans résultat ; catalogues Viollier/Risch rendus par JavaScript.
6. Liste des spécialités (SL) officielle pour Zink Biomed et Burgerstein Zinc : non lue (seulement AmiKo [S23]).
7. Limite supérieure de sécurité (UL) EFSA pour le zinc : non lue.
8. Incidence suisse de E60 codé (statistique hospitalière OFS) : non trouvée.
9. Fréquences des symptômes chez l'adulte, sensibilité et spécificité des signes, délais d'action chiffrés : non trouvés.
10. Déclaration OFSP, règles Suva, AI, LiMA, aptitude à la conduite propre à la maladie : non trouvés.
11. Solution suisse de zinc injectable seul : non trouvée dans AmiKo.
12. Directives SMOB sur le zinc (renvoi au site SMOB, § 13.2.2) : page non lue.

## Matrice de complétude

| rubrique | statut | sources |
|---|---|---|
| 1. Question clinique et enjeu pour l'examen fédéral | ✔ | S14, S15, S25, S2 |
| 2. Définition et périmètre CIM-10-GM (libellés OFS, inclusions, exclusions, notes BfArM) | ✔ | S1, S2, S3, S5, S14 |
| 3. Classifications et stades | ✔ (étiologique, biochimique, santé publique ; pas de stades officiels) | S2, S5, S6, S14 |
| 4. Épidémiologie suisse puis européenne | ✔ (incidence E60 suisse : lacune) | S5, S6, S16, S14, S2, S20 |
| 5. Normal → pathologique | ✔ | S2, S5, S7, S8, S14, S18, S19 |
| 6. Étiologies et facteurs de risque | ✔ | S2, S5, S6, S7, S14 |
| 7. Anamnèse et symptômes (fréquences) | ✔ (fréquences adultes : lacune) | S2, S14, S15 |
| 8. Examen clinique | ✔ (Se/Sp : lacune) | S14, S17 |
| 9. Drapeaux rouges et urgences | ✔ (délais : lacune) | S14, S25, S2 |
| 10. Examens complémentaires | ✔ | S2, S3, S5, S6, S8, S14, S15 |
| 11. Diagnostic différentiel | ✔ | S1, S2, S14, S17, S25 |
| 12. Prise en charge suisse (FI datées) | ✔ | S2, S7, S8, S9, S10, S11, S12, S13, S17, S18, S19, S20, S21 |
| 13. Complications et pronostic | ✔ | S1, S2, S7, S8, S14, S15, S22 |
| 14. Suivi, prévention, dépistage | ✔ | S2, S4, S5, S7, S14, S20, S21 |
| 15. Situations particulières | ✔ | S2, S4, S5, S6, S7, S8, S9, S10, S11, S12, S17, S18, S19, S22 |
| 16. Spécificités suisses | ✔ (OFSP, Suva, AI, LiMA, Analysenliste, SL officielle : lacunes) | S1, S4, S5, S7, S8, S20, S23 |
| 17. Critères formels du diagnostic | ✔ (conjonction opérationnelle, pas de critères consensuels) | S1, S2, S3, S5, S14, S15 |
| 18. Paramètres clés chiffrés | ✔ | S2, S3, S4, S5, S6, S7, S8, S11, S14, S16, S20 |
| 19. Sous-codes CIM-10-GM couverts | ✔ (pas de sous-code) | S1 |
| 20. Points d'examen fédéral | ✔ | S24, S1, S2, S5, S7, S8, S14, S20 |
