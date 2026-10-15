# Dossier de recherche — E56 Autres avitaminoses (E-06-Endocrinologie et métabolisme)

Cycle Betta 41, leçon 1. Agent de recherche C41-A2-ENDO (Opus 5.5). Date : 15.10.2026.
Chaque fait renvoie à une source de `sources.json` (Sx), lue pendant cette session : texte intégral, résumé PubMed, page web ou information professionnelle (IP) AmiKo. Rien n'est ajouté de mémoire ; ce qui manque figure en « Lacunes ». Lors du premier passage, la recherche web générale était indisponible (quota épuisé) ; l'accès s'est fait par PubMed et PMC, le PDF ESPEN 2022, le PDF ESPEN-ESPGHAN-ECFS 2016, les pages BfArM et DGE (WebFetch), le PDF SMOB 2023 et `tools/swissmedic_fi.py`. Un complément du même jour (WebSearch/WebFetch rétablis) a relu le ClaML OFS [S28], la liste PROFILES [S29], le statut SL et la catégorie de remise [S30], et revérifié la page DGE vitamine E [S8].

**Convention d'unités (à reprendre dans le cours).** L'extraction du PDF ESPEN remplace le symbole « µ » par « m ». Le contexte fixe la bonne lecture :
- vitamine E : le PDF écrit « 1 mg/dL = 23.22 mmol/L » et « normal 20–30 mmol/L ». Il s'agit de **µmol/L** (2 325 « mmol » correspondent à 1 000 mg ; 1 000 mg / 430 g/mol ≈ 2,3 mmol = 2 325 µmol) [S2, §24.2.1, §24.4] ;
- vitamine K : « AI 1 mg/kg/j », « 120 mg » et « 150 mg » se lisent en **µg**. Les apports de référence DGE se situent à 60–80 µg/j [S9], ce qui confirme cette lecture [S2, §25.1.1].
- Le guide ECFS 2016 écrit « 300 mg/dL » pour le seuil de vitamine E. Ce seuil se lit **300 µg/dL** (3 mg/L ≈ 7 µmol/L) [S3, §3.5.3]. La lecture reste à confirmer sur l'original.

## 0. Sous-codes CIM-10-GM couverts
- **E56.0 Carence en vitamine E** ; **E56.1 Carence en vitamine K** ; **E56.8 Carence en autres vitamines** ; **E56.9 Avitaminose, sans précision** [S1].
- Exclusion de la catégorie E56 : séquelles d'autres avitaminoses (E64.8) [S10].
- Exclusions de **E56.1** : déficit en facteurs de coagulation dû à une carence en vitamine K (**D68.4**) et carence en vitamine K du nouveau-né (**P53**) [S10]. Le cours doit donc dire clairement ce point : la carence en vitamine K se code E56.1 ; la coagulopathie qui en découle se code D68.4 ; la maladie hémorragique néonatale se code P53. Le contenu néonatal reste utile au raisonnement (physiopathologie, prophylaxie suisse), mais il relève d'un autre code.
- Exclusion du bloc E50–E64 : anémies nutritionnelles (D50–D53) [S10].
- Le texte officiel français de l'OFS (ClaML 2024, en vigueur en Suisse depuis le 01.01.2025) confirme mot pour mot ces libellés et ces exclusions : E56 « Autres avitaminoses », exclusion « séquelles d'autres avitaminoses E64.8 » ; E56.1 exclut « carence en facteur de coagulation due à l'avitaminose K D68.4 » et « carence en vitamine K chez le nouveau-né P53 » ; le bloc E50–E64 « Autres carences nutritionnelles » exclut les « anémies nutritionnelles D50–D53 » [S28].
- D68.4 « Carence acquise en facteur de coagulation » inclut la carence en facteur de coagulation due à une avitaminose K ou à une affection du foie, avec un code supplémentaire U69.11! (trouble « durablement acquis ») ou U69.12! (« provisoire ») [S28]. P53 « Maladie hémorragique du fœtus et du nouveau-né » inclut la carence du nouveau-né en vitamine K [S28].
- E56.8 et E56.9 ne portent ni inclusion ni exclusion, ni dans le ClaML OFS [S28] ni sur la page BfArM [S10]. Le périmètre de E56.8 se déduit donc par exclusion des catégories voisines, qui ont leur propre code [S28] : vitamine A (E50), thiamine/B1 (E51), acide nicotinique/pellagre (E52), riboflavine, pyridoxine et autres vitamines B précisées — biotine, cobalamine/B12, folate, acide pantothénique (E53), vitamine C/scorbut (E54), vitamine D (E55). Aucune vitamine n'est nommée sous E56.8 : le cours ne doit pas en inventer la liste.

## 1. Question clinique
- La carence en vitamine E est rare. Elle apparaît dans la malnutrition sévère, la malabsorption des graisses (maladies inflammatoires, mucoviscidose) et dans des maladies génétiques : abêtalipoprotéinémie, déficit en protéine de transfert de l'α-tocophérol (α-TTP) [S2, §24.3].
- Une fois installée, la neuropathie périphérique sévère est difficile, voire impossible, à faire régresser [S5]. Un diagnostic précoce change donc le pronostic : la supplémentation stoppe la progression [S5, S6, S13].
- La carence en vitamine K se manifeste par une hémorragie. Le temps de prothrombine s'allonge, et la correction par la vitamine K confirme le diagnostic [S2, §25.3]. Une hémorragie cliniquement significative s'observe surtout chez le nouveau-né, ainsi qu'en cas d'apport extrêmement bas ou de malabsorption [S2, §25.3].

## 2. Définitions et nomenclature
- **Vitamine E** : vitamine liposoluble et antioxydante. L'α-tocophérol est la forme naturelle de plus haute activité biologique. C'est le principal antioxydant liposoluble des membranes biologiques [S2, §24.1].
- La vitamine E se définit comme le 2R-α-tocophérol, définition retenue notamment par l'EFSA [S5]. Les tocophérols autres que l'α-tocophérol et les tocotriénols sont catabolisés et excrétés plus vite ; ils ne devraient pas être appelés vitamine E [S5].
- Équivalences : 1 UI de d-α-tocophérol naturel = 0,67 mg ; 1 UI de dl-α-tocophérol synthétique = 0,9 mg [S2, §24.2.1]. Par poids, l'activité du RRR-α-tocophérol naturel vaut le double de celle du tocophérol synthétique all-rac (rapport 2:1) [S5]. La DGE l'écrit ainsi : 1 mg RRR = 2 mg all-rac [S8].
- **Vitamine K** : groupe de molécules liposolubles, cofacteurs de la carboxylase qui active les protéines vitamine K-dépendantes [S2, §25.1]. Vitamine K1 = phylloquinone (plantes). Vitamine K2 = ménaquinones (MK-n, de MK-2 à MK-14), synthétisées par le microbiote intestinal et présentes dans les aliments fermentés et les produits animaux. Vitamine K3 = ménadione, provitamine synthétique [S2, §25.1].

## 3. Épidémiologie
- Vitamine E : carence rare, liée à la malnutrition sévère ou à la malabsorption [S2, §24.3]. Dans la mucoviscidose, des carences biochimiques s'observent chez 23 % des nourrissons nouvellement diagnostiqués et chez 14 % des enfants plus âgés [S3, §3.5.3]. La DGE qualifie la carence de « très rare » dans la population générale [S8].
- AVED (ataxie avec carence en vitamine E) : maladie autosomique récessive rare [S6]. Elle semble plus fréquente dans les pays d'Afrique du Nord ; des cas existent aussi en Europe du Nord (Norvège) [S14]. Plus de 25 mutations du gène de l'α-TTP sont connues [S5].
- Vitamine K : chez l'adulte sain, 8 à 31 % présentent une carence si l'on se fonde sur les protéines sous-carboxylées [S2, §25.3]. Une coagulopathie clinique reste rare en dehors des situations à risque [S2, §25.3].
- Patients hospitalisés : dans une cohorte de 292 patients évalués pour une coagulopathie (84,2 % hospitalisés, 48,3 % en soins intensifs), 25 à 38 % avaient un profil FII/FIIE évocateur d'une carence en vitamine K [S16]. Aux soins intensifs, la carence est liée à la malnutrition, à la malabsorption, aux antibiotiques et à un renouvellement accru [S17].
- Mucoviscidose : le statut en vitamine K est souvent insuffisant. Il apparaît déficitaire chez tous les patients atteints d'une hépatopathie liée à la mucoviscidose [S3, §3.5.4].
- Hémorragie néonatale par carence en vitamine K (code P53, hors E56) en Suisse : neuf cas pour 505 708 naissances vivantes entre 2018 et 2024, soit 1,78/10⁵ [S11]. Entre 2005 et 2011, l'incidence était de 1,09/10⁵, dont 0,87/10⁵ pour la forme tardive [S12].

## 4. Mécanismes : du normal au pathologique
### 4.1 Vitamine E
- **Normal** : l'α-tocophérol protège de la peroxydation les lipides membranaires, les lipoprotéines et les graisses de réserve. C'est un antioxydant « briseur de chaîne » ; il régule aussi les espèces réactives de l'oxygène et de l'azote et module la transduction du signal [S2, §24.1]. L'IP Ephynal décrit le même rôle : protection des membranes et des lipoprotéines contre les radicaux libres [S19].
- **Absorption** : elle exige la bile et les sécrétions pancréatiques, puis le transport par les chylomicrons [S5]. La bile est nécessaire à la micellisation. Des enfants cholestatiques ont retrouvé une α-tocophérolémie normale après greffe hépatique [S5]. L'absorption ne se fait que si le mécanisme d'absorption des graisses est intact [S20].
- **Rôle du foie et de l'α-TTP** : dans l'hépatocyte, l'α-TTP récupère l'α-tocophérol nouvellement absorbé et le transfère vers les VLDL et les HDL naissantes, qui le distribuent aux tissus [S5]. Le foie renouvelle chaque jour la totalité du pool plasmatique d'α-tocophérol [S5]. L'α-TTP est le principal déterminant de la concentration plasmatique [S7].
- **Transport** : la vitamine E circule surtout dans les LDL, au maximum environ 9 mol par mol de LDL [S2, §24.2]. La concentration plasmatique est régulée par la protéine de liaison du tocophérol. Une valeur plasmatique normale peut donc coexister avec des réserves tissulaires basses [S2, §24.2]. Les concentrations les plus élevées se trouvent dans le tissu adipeux et les surrénales [S20].
- **Pathologique** : en cas de carence, la peroxydation lipidique accumule de la lipofuscine dans les tissus et raccourcit la demi-vie des cellules [S19]. Les érythrocytes deviennent plus sensibles à l'hémolyse [S5]. Le test d'hémolyse in vitro n'est toutefois pas un biomarqueur fiable [S5].
- **Délai** : chez l'adulte, plus de 5 ans s'écoulent avant l'apparition des symptômes. Chez l'enfant, ils apparaissent dès les premiers mois ou les premières années de vie [S5].
- **Prématuré** : l'α-tocophérol fœtal est nettement plus bas que celui de la mère. Les lipoprotéines fœtales sont basses et le passage placentaire est faible. Le très grand prématuré (< 1 500 g) est considéré comme carencé, au vu de sa sensibilité à l'anémie hémolytique, aux atteintes pulmonaires et à la rétinopathie du prématuré [S5].

### 4.2 Vitamine K
- **Normal** : la vitamine K est le cofacteur de la γ-glutamyl-carboxylase [S2, §25.1 ; S15]. La carboxylation crée des résidus Gla qui fixent le calcium, condition de l'activité biologique [S15]. Les protéines vitamine K-dépendantes comprennent les facteurs II (prothrombine), VII, IX et X, les protéines C, S et Z et la protéine M. S'y ajoutent des protéines osseuses et vasculaires : ostéocalcine, Matrix Gla Protein, Gas6, GRP, périostine [S2, §25.1].
- L'IP Konakion décrit le même mécanisme : comme cocarboxylase, la phytoménadione participe à la formation de la prothrombine, des facteurs VII, IX et X et des protéines C et S [S18].
- **Pathologique** : sans vitamine K, des formes inactives sous-carboxylées circulent. C'est le cas de la prothrombine sous-carboxylée, ou PIVKA-II (protéine induite par l'absence ou l'antagonisme de la vitamine K) [S2, §25.2]. Le TP s'allonge et l'hémostase est altérée [S2, §25.3].
- **Faibles réserves** : la phytoménadione s'accumule surtout dans le foie et n'est stockée que brièvement. Sa demi-vie plasmatique est d'environ 70 h [S18]. La faible capacité de stockage justifie une administration quotidienne en cas de supplémentation [S3, §3.5.4].
- Les bactéries intestinales, dont *E. coli*, synthétisent la vitamine K2 mais pas la K1, et contribuent aux besoins [S2, §25.1.1]. Cette donnée éclaire le rôle des antibiotiques.
- **Nouveau-né (P53)** : la vitamine K franchit mal le placenta, l'intestin est stérile à la naissance et le lait maternel en contient peu. Le nourrisson allaité est donc à risque [S9, S18].

## 5. Causes et facteurs de risque
| Vitamine | Causes documentées | Source |
|---|---|---|
| E | Malnutrition sévère ; malabsorption des graisses (maladies inflammatoires, mucoviscidose) | S2 §24.3 |
| E | Abêtalipoprotéinémie (défaut de MTTP), hypobêtalipoprotéinémie (apoB), maladie de rétention des chylomicrons (SAR1B) | S2 §24.3 ; S5 |
| E | AVED : mutation du gène *TTPA* (α-TTP), autosomique récessive | S5 ; S6 ; S7 |
| E | Cholestase (atrésie des voies biliaires), insuffisance pancréatique exocrine, syndrome de l'intestin court | S19 ; S5 |
| E | Régime pauvre en graisses (apport en vitamine E réduit de 50 %), chirurgie bariatrique, médicaments limitant l'absorption des graisses | S2 §24.3 ; S5 |
| E | Grande prématurité | S5 |
| K | Malabsorption des graisses (maladie cœliaque, mucoviscidose, intestin court), malnutrition, antibiotiques, anticoagulants (warfarine) | S2 §25.3 |
| K | Hépatopathie, antibiothérapie prolongée (mucoviscidose) | S3 §3.5.4 |
| K | Antibiotiques à large spectre au long cours, stéatorrhée, maladie rénale chronique : groupes où le dosage est utile | S2 Rec. 26.1 |
| K | Cachexie cancéreuse (cas : TP 105,8 s, TCA 58,2 s, corrigés par vitamine K IV) | S21 |
| K | Pseudo-obstruction intestinale avec ciprofloxacine (cas d'hémopéricarde spontané, déficit en facteurs II, VII et X) | S22 |
| K (nouveau-né, P53) | Refus parental de la prophylaxie, cholestase méconnue, allaitement exclusif | S11 ; S12 |

## 6. Anamnèse et examen clinique
### Vitamine E
- Chez l'adulte malabsorbant, la carence débutante est en général asymptomatique [S2, §24.3].
- Signes neurologiques : troubles de l'équilibre et de la coordination, neuropathie périphérique, faiblesse musculaire [S2, §24.3]. L'atteinte se décrit au mieux comme une neuropathie sensitive progressive : ataxie spinocérébelleuse, perte du contrôle moteur, lésions musculaires et nerveuses périphériques [S5].
- AVED : tableau très proche de l'ataxie de Friedreich. On y trouve ataxie, dysarthrie, hyporéflexie et baisse de la sensibilité vibratoire, parfois une cardiomyopathie et une rétinite pigmentaire [S6]. Une dystonie cervicale a été décrite chez des patients non supplémentés [S5].
- Atteinte oculaire : rétinite pigmentaire et dégénérescence maculaire, dans l'AVED et l'abêtalipoprotéinémie [S5].
- Anémie hémolytique [S5 ; S3 §3.5.3]. Le guide ECFS cite aussi une atteinte rétinienne et des déficits cognitifs [S3, §3.5.3].
- Cas norvégien d'AVED : ataxie progressive dès 5 ans, steppage bilatéral, signe de Babinski, dysarthrie, épilepsie précoce. Le traitement, débuté 25 ans après le début, a stabilisé l'état sans récupération [S14].

### Vitamine K
- Tendance hémorragique, avec TP allongé [S2, §25.3]. Chez le nourrisson atteint de mucoviscidose, on a décrit une hémorragie intracrânienne [S3, §3.5.4].
- Hémorragies graves chez l'adulte : hémopéricarde avec tamponnade [S22] ; coagulopathie sévère dans la cachexie [S21].
- Effets extra-hémostatiques associés : mauvais développement osseux, ostéoporose, risque cardiovasculaire accru [S2, §25.3]. Il s'agit d'associations, pas d'une causalité démontrée [S2, §25.3 ; S15].

## 7. Examens complémentaires
### Vitamine E
- Dosage de l'α-tocophérol plasmatique ou sérique par HPLC (détection UV ou fluorescence) [S2, §24.2]. Le prélèvement est réfrigéré à 4 °C pendant le transport [S2, §24.2].
- L'α-tocophérol varie avec les lipides. On l'exprime donc en rapport aux lipides (cholestérol et triglycérides) [S2, §24.2].
- Seuils ESPEN : < 12 µmol/L = apport insuffisant chez l'adulte sain. La valeur normale isolée est d'environ 20–30 µmol/L. Un rapport α-tocophérol/lipides totaux < 0,8 mg/g est l'indicateur le plus précis d'insuffisance chez l'adulte malabsorbant [S2, §24.2]. Conversion : 1 mg/dL = 23,22 µmol/L [S2, §24.2.1].
- Piège : si les lipides et l'α-tocophérol sont tous deux bas (malnutrition), le rapport paraît normal. Pourtant, le statut n'est pas adéquat, car les transporteurs eux-mêmes manquent [S2, §24.2].
- Inflammation : effet faible, mais l'interprétation devient difficile si la CRP dépasse 80 mg/L [S2, §24.2.2].
- Mucoviscidose (ECFS) : rapport α-tocophérol/cholestérol ; limite basse 2,47 mg/g chez le sujet sain ; cible > 5,4 mg/g dans la mucoviscidose. Contrôle au moins annuel, puis 3 à 6 mois après tout changement de dose [S3, §3.5.3].
- ESPEN Rec. 25.1 (grade B) : doser la vitamine E en cas de suspicion clinique, par exemple mucoviscidose, abêtalipoprotéinémie ou purpura thrombotique thrombocytopénique (PTT). Sans signe de carence, il n'y a pas d'indication à la doser pendant une nutrition parentérale [S2]. Rec. 25.2 (grade B) : mesurer l'α-tocophérol plasmatique [S2].
- AVED : α-tocophérol plasmatique effondré, < 1–2 µmol/L [S5]. Confirmation par l'analyse du gène *TTPA* [S6]. Pour les ataxies récessives, l'IRM, l'électrophysiologie et l'analyse moléculaire complètent le diagnostic clinique [S13].

### Vitamine K
- Aucun biomarqueur unique n'est établi [S2, §25.2].
- La phylloquinone plasmatique est le marqueur le plus utilisé, mais elle reflète surtout l'apport récent. Une valeur < 0,15 µg/L indique une déplétion ou une carence [S2, §25.2].
- **PIVKA-II** (prothrombine sous-carboxylée) : marqueur homéostatique sensible de la carence hépatique infraclinique. Un immunodosage automatisé existe [S2, §25.2]. Il est plus sensible et plus spécifique que les tests de coagulation [S15].
- TP, TCA et dosage des facteurs : utilisés, mais peu sensibles et peu spécifiques [S2, §25.2]. Le TP ne s'allonge qu'en cas de carence sévère [S3, §3.5.4].
- Rapport FII/FIIE (FII mesuré par réactif TP et FII mesuré par écarine) : un rapport < 0,86 évoque une carence (sensibilité 47,7 %, spécificité 90,2 %) et prédit la réponse à la vitamine K [S16].
- Préanalytique : protéger l'échantillon de la lumière, des conditions alcalines et de la chaleur [S2, §25.2].
- ESPEN Rec. 26.2 (grade A) : associer plusieurs biomarqueurs et l'apport alimentaire, faute de standard [S2]. Rec. 26.1 (GPP) : doser chez les patients à risque (stéatorrhée, antibiotiques à large spectre prolongés, maladie rénale chronique) [S2].
- **Test thérapeutique** : la carence se confirme par la correction du TP sous vitamine K [S2, §25.3]. Dans la cohorte S16, la carence était définie par une baisse de l'INR d'au moins 0,5 après vitamine K [S16].
- Après chirurgie bariatrique (SMOB) : bilan annuel comprenant la coagulation (INR) et le statut vitaminique [S23].

## 8. Diagnostic différentiel
- Ataxie avec aréflexie et atteinte proprioceptive : ataxie de Friedreich, avec laquelle l'AVED a une « ressemblance souvent frappante » [S6]. Autres ataxies cérébelleuses autosomiques récessives : ataxie-télangiectasie, ataxie avec apraxie oculomotrice. Pour la plupart d'entre elles, il n'existe pas de traitement spécifique, sauf le déficit en coenzyme Q10 et l'abêtalipoprotéinémie [S13].
- Prévalences de référence en population caucasienne : Friedreich 2–4/100 000 ; ataxie-télangiectasie 1–2,5/100 000 [S13].
- TP allongé : la carence en vitamine K se distingue d'une hépatopathie (FIIE bas, souvent associé à une hépatopathie active) [S16] et d'un traitement par antivitamine K [S2, §25.3]. Un rapport FII/FIIE < 0,86 s'observe aussi chez 16 % des patients qui ont un déficit en facteurs non vitamine K-dépendants [S16].
- Avant de conclure à une carence en vitamine E isolée, il faut rechercher une malabsorption ou un trouble des lipoprotéines [S5].

## 9. Urgences
- Hémorragie grave sur carence en vitamine K : la vitamine K IV agit au maximum en 6 à 12 h, et la voie orale en environ 24 h [S2, §25.4.1]. L'IP Konakion pédiatrique précise qu'une transfusion de sang ou de facteurs de coagulation peut devoir être associée pour une action plus immédiate [S18].
- Les concentrés de complexe prothrombinique à 4 facteurs (II, VII, IX, X) sont autorisés dans le déficit acquis en facteurs vitamine K-dépendants [S24].
- Vitamine K IV : rares réactions anaphylactoïdes avec bronchospasme et arrêt cardiaque [S2, §25.4]. L'IP Konakion mentionne des réactions de type anaphylactique après injection IV [S18].

## 10. Prise en charge (Suisse puis Europe)
### Vitamine E
- **ESPEN Rec. 25.5 (GPP)** : supplémenter si l'α-tocophérol plasmatique est < 12 µmol/L, en commençant par 100 mg/j selon la cause [S2].
- Malabsorption ancienne des graisses (intestin court) : 200 mg/j améliorent les symptômes neurologiques en quelques mois, après normalisation du statut. La voie IV est rarement nécessaire [S2, §24.3].
- **AVED** : environ 1 000 mg/j d'α-tocophérol préviennent ou stoppent la progression neurologique, tant que l'α-tocophérolémie reste normalisée [S5]. Les formes naturelle et synthétique ont été utilisées avec succès [S5, S4].
- **Abêtalipoprotéinémie** : doses orales très élevées au long cours, > 100 mg/kg/j [S5].
- **Cholestase** : il faut une forme hydrosoluble qui forme elle-même ses micelles, le TPGS (succinate de tocophérol-polyéthylène glycol) [S5 ; S3 §3.5.3].
- **Mucoviscidose (ECFS)** : 100–400 UI/j ; 50 UI/j avant 12 mois (1 mg = 1,49 UI) ; cible α-tocophérol/cholestérol > 5,4 mg/g [S3, Table 11].
- Nutrition entérale : au moins 15 mg/j d'α-tocophérol pour 1 500 kcal (Rec. 25.3, grade A). Nutrition parentérale : au moins 9 mg/j (Rec. 25.4, grade B) [S2].
- **Médicaments suisses (IP Swissmedic)** :
  - **Ephynal®** (acétate d'int-rac-α-tocophéryle, capsules à 300 mg = 300 UI ; ATC A11HA03) : prévention de la carence par malabsorption (insuffisance pancréatique exocrine, cholestase, atrésie des voies biliaires, intestin court), abêtalipoprotéinémie, neuropathie par carence. Malabsorption : 1 capsule/j. Abêtalipoprotéinémie et neuropathie : 1–2 capsules/j. À prendre avec un repas gras. Sécurité non étudiée chez l'enfant. IP mise à jour en octobre 2022 [S19].
  - **Burgerstein Vitamine E®** (RRR-α-tocophérol, 100 UI = 67,1 mg ; 400 UI = 268,4 mg) : prévention de la carence par trouble de l'absorption. Contre-indiqué en cas d'allergie au soja ou à l'arachide. IP mise à jour en mai 2023 [S20].
  - Précautions communes : à fortes doses, la vitamine E renforce l'effet des anticoagulants, d'où une surveillance de la coagulation. Le fer oral réduit son absorption ; prendre les deux à environ 4 h d'intervalle. Chez l'animal, de très fortes doses limitent l'absorption des vitamines A et K [S19, S20].
- Sécurité : jusqu'à 800 mg/j, pas d'effet indésirable en règle générale. À partir de l'ordre du gramme, troubles digestifs passagers ; CK et créatinurie augmentées [S19, S20]. Limite supérieure de sécurité (UL) chez l'adulte : 1 000 mg/j [S2, §24.4]. À 1 000 UI/j pendant 12 semaines, la γ-carboxylation de la prothrombine diminue. Les patients sous warfarine ou carencés en vitamine K ne doivent pas prendre de vitamine E sans surveillance [S2, §24.4].

### Vitamine K
- **Médicament suisse** : **Konakion® MM** et **Konakion® MM paediatric** (phytoménadione en micelles mixtes ; ATC B02BA01 ; autorisation 48112). Indications Swissmedic : hypoprothrombinémie, antidote des anticoagulants de type dicoumarol, maladie hémorragique du nouveau-né [S18].
  - Konakion MM paediatric : 2 mg/0,2 ml, voie orale, IV ou IM. Traitement du nouveau-né : 1 mg IV, puis selon la clinique et la coagulation. Biodisponibilité orale d'environ 50 %. La voie orale ne convient pas en cas de cholestase ou de malabsorption. Interactions : les dicoumariniques s'opposent à son effet et les anticonvulsivants peuvent l'entraver. Risque d'ictère nucléaire chez le prématuré < 2,5 kg en IV rapide. IP de janvier 2022 [S18].
- **Mucoviscidose (ECFS)** : vitamine K1 0,3–1 mg/j chez le nourrisson ; 1–10 mg/j chez l'enfant plus âgé et l'adulte ; doses plus élevées si le taux est bas ou sous antibiothérapie prolongée. Administration quotidienne. La vitamine K1 est préférée aux sels de ménadione [S3, §3.5.4].
- Nutrition entérale de l'adulte : au moins 120 µg/j pour 1 500 kcal (Rec. 26.3, grade B). Nutrition parentérale : 150 µg/j de vitamine K1 (Rec. 26.4, grade 0) [S2]. Les émulsions lipidiques apportent elles aussi de la phylloquinone. Il faut en tenir compte, car plus de 150 µg peuvent créer une résistance aux antivitamines K [S2, §25.1.1].
- Patients sous AVK : éviter les changements brusques de l'apport en vitamine K et surveiller la coagulation. En nutrition entérale continue, l'interrompre 1 h avant et 1 h après l'AVK [S2, §25.4.1].
- Toxicité : K1 et K2 ne sont pas toxiques [S2, §25.4]. Aucune hypervitaminose K1 n'est connue [S18]. La **ménadione (K3)** est très toxique (ictère, hémolyse, ictère nucléaire du nourrisson) ; elle n'est plus disponible [S2, §25.4].

### Prophylaxie néonatale suisse (P53, cité pour la compréhension)
- Schéma suisse depuis 2003 : 2 mg de Konakion MM par voie orale à la 4ᵉ heure, au 4ᵉ jour et à la 4ᵉ semaine [S11, S12]. La troisième dose a été ajoutée parce que deux doses n'abolissaient pas les formes tardives [S12]. Il reste valide en 2018–2024 [S11].
- IP : 2 mg PO à la naissance, puis 2 mg à J4–J7, puis 2 mg à 4–6 semaines si allaitement. Sinon, 1 mg IM ou IV. Prématuré < 36 SA et < 2,5 kg : 0,4 mg/kg IM ou IV, sans dépasser cette dose. Les erreurs de dose d'un facteur 10 sont fréquentes [S18].
- ESPGHAN : prophylaxie pour tout nouveau-né ; voie IM préférée pour son efficacité et sa fiabilité ; consigner tout refus parental [S27].

## 11. Suivi
- Vitamine E dans la mucoviscidose : contrôle au moins annuel, puis 3 à 6 mois après un changement de dose [S3].
- AVED : l'amélioration ou la stabilisation dépend du maintien d'une α-tocophérolémie normalisée [S5]. Le traitement est donc à vie (lecture de S5 ; aucune durée n'y est explicitée).
- Après chirurgie bariatrique : multivitamines à long terme, à vie après une chirurgie malabsorptive ; contrôle annuel de l'INR et du statut vitaminique ; vérifier le succès du traitement de toute carence avérée [S23].
- Sous AVK : surveiller la coagulation lors de toute modification de l'apport en vitamine K, qu'il soit alimentaire, entéral ou parentéral [S2, §25.4.1].

## 12. Situations particulières
- **Grossesse** : la vitamine E peut être prise à hauteur des besoins quotidiens. Au-delà, elle n'est utilisée que si le bénéfice l'emporte [S19, S20]. La vitamine K1 franchit peu le placenta [S18]. Chez le nouveau-né dont la mère a pris des anticoagulants ou des anticonvulsivants, il faut 1 mg IM ou IV d'emblée [S18].
- **Nutrition parentérale** : apports E et K ci-dessus [S2].
- **Patient sous AVK prenant de la vitamine E** : risque hémorragique accru [S2, §24.4 ; S19].
- **Soins intensifs** : carence fréquente, PIVKA-II élevée. La supplémentation améliore le statut sans le normaliser complètement [S17].
- **Maladie rénale chronique / dialyse** : association entre bas statut en vitamine K et déclin rénal ; aucun effet démontré de la supplémentation sur la fonction rénale [S25]. Chez le dialysé, la ménaquinone-7 (MK-7, 360 µg/j pendant un an) a abaissé la PIVKA-II sans activer la coagulation [S26].

## 12 bis. Spécificités suisses
- **Codage hospitalier** : la CIM-10-GM 2024 en français est obligatoire en Suisse depuis le 01.01.2025 pour le relevé des séjours stationnaires (SpiGes) [S28].
- **Statut des médicaments (données AmiKo, republication Swissmedic/OFSP)** [S30] :
  - Konakion® MM (5 ampoules) et Konakion® MM paediatric : catégorie de remise **B** (ordonnance), **sur la Liste des spécialités (SL)**, quote-part 10 % ; prix public 14.95 CHF (MM) et 26.85 CHF (paediatric).
  - Ephynal® 300 mg (100 capsules) et Burgerstein Vitamine E® 100 UI / 400 UI : catégorie de remise **D** (conseil spécialisé, pharmacie ou droguerie) ; aucune mention SL dans la fiche, donc non remboursés par l'assurance de base selon cette source (à confirmer sur la SL officielle).
- **Prophylaxie néonatale** : schéma suisse oral 3 × 2 mg (voir §10) [S11, S12].
- **Chirurgie bariatrique** : suivi selon les directives suisses SMOB 2023 (multivitamines, INR et statut vitaminique annuels) [S23].
- Déclaration OFSP, Suva/LAA, aptitude à la conduite, AI : aucune source lue ne traite de E56 sous ces angles ; aucun élément propre à E56 n'a été trouvé (voir Lacunes).

## 12 ter. Points d'examen fédéral
- **Objectifs PROFILES** rattachés à E56 : SSP 16 « weight loss, malnutrition, loss of appetite » ; SSP 138 « cachexia and malnutrition » ; SSP 170 « nutritional deficiencies » [S29].
- Pièges documentés par les sources du dossier :
  1. Carence en vitamine K = E56.1, mais la coagulopathie qui en résulte = D68.4 et la forme néonatale = P53 [S28].
  2. Un TP allongé ne suffit pas : il ne s'allonge qu'en carence sévère ; la correction du TP après vitamine K confirme le diagnostic [S2, §25.3 ; S3, §3.5.4].
  3. Une α-tocophérolémie « normale » chez un malnutri peut masquer une carence, car les lipoprotéines de transport manquent aussi ; il faut raisonner en rapport aux lipides [S2, §24.2].
  4. AVED : tableau proche de l'ataxie de Friedreich, mais traitable ; doser la vitamine E devant toute ataxie récessive [S6, S13].
  5. Vitamine E à forte dose + AVK = risque hémorragique [S2, §24.4 ; S19].
  6. Voie orale de vitamine K inadaptée en cas de cholestase ou de malabsorption [S18].

## 13. Critères formels (pour l'îlot `div.alert`)
Aucun critère diagnostique formel publié n'a été trouvé pour E56. Le cours doit présenter des **critères opérationnels sourcés**, pas une définition officielle :
- **Carence en vitamine E** : α-tocophérol plasmatique < 12 µmol/L chez l'adulte (ESPEN), avec correction lipidique (α-tocophérol/lipides totaux < 0,8 mg/g en cas de malabsorption) [S2]. Dans la mucoviscidose, α-tocophérol/cholestérol < 5,4 mg/g [S3]. Dans l'AVED, effondrement < 1–2 µmol/L et mutation *TTPA* [S5, S6].
- **Carence en vitamine K** : TP allongé corrigé par la vitamine K [S2, §25.3], PIVKA-II élevée [S2, §25.2] ou phylloquinone < 0,15 µg/L [S2, §25.2]. Comme aucun standard n'existe, il faut combiner les biomarqueurs [S2, Rec. 26.2].

## 14. Paramètres clés (pour l'îlot `div.key`)
- α-tocophérol : normal ≈ 20–30 µmol/L ; insuffisance < 12 µmol/L ; conversion 1 mg/dL = 23,22 µmol/L [S2].
- Apport de référence DGE/ÖGE : vitamine E 8 mg/j (RRR-α-tocophérol, adulte, dérivation 2024) [S8] ; vitamine K 60–80 µg/j selon le sexe et l'âge [S9]. EFSA : AI vitamine E 13 mg/j chez l'homme et 11 mg/j chez la femme ; AI vitamine K 1 µg/kg/j [S2].
- UL vitamine E : 1 000 mg/j [S2].
- Phylloquinone < 0,15 µg/L = déplétion [S2] ; demi-vie de la phylloquinone ≈ 70 h [S18].
- Délai d'action de la vitamine K : 6–12 h en IV, environ 24 h par voie orale [S2].
- Prophylaxie suisse : 3 × 2 mg PO (H4, J4, S4) [S11].

## Lacunes explicites
1. **E56.8** : ni le ClaML OFS [S28] ni la page BfArM [S10] ne nomment de vitamine sous ce code ; seul le raisonnement par exclusion des catégories E50–E55 est sourcé. Le cours ne doit pas en inventer la liste.
2. **IP Konakion MM adulte (10 mg/ml)** : texte non accessible par AmiKo (même autorisation 48112, renvoi au texte pédiatrique) ; ch.oddb.org bloqué par un anti-robot ; requête WebSearch « Konakion MM 10 mg/ml Fachinformation Erwachsene Dosierung » sans texte suisse. La posologie adulte de la carence, la vitesse de perfusion IV et la dilution ne sont pas sourcées.
3. Aucune recommandation suisse spécifique (SSED, Swiss Medical Forum, SSN) sur la carence en vitamine E ou en vitamine K de l'adulte n'a été trouvée (WebSearch « Swiss Medical Forum Vitamin-K-Mangel Erwachsene … » : aucun résultat SMF).
4. Texte intégral de la mise à jour ESPEN-ESPGHAN-ECFS 2024 sur la mucoviscidose non lu ; les doses viennent de la version 2016.
5. GeneReviews AVED inaccessible (vérification de navigateur). Les doses en mg/kg et les seuils pédiatriques de l'AVED ne sont pas sourcés au-delà de S5 et S6.
6. Valeur DGE vitamine E (8 mg/j RRR-α-tocophérol, adultes 19–65 ans, dérivation 2024) revérifiée par un second WebFetch le 15.10.2026 [S8] ; extraction automatisée, sans PDF original.
7. Lecture des unités du PDF ESPEN (« m » mis pour « µ ») déduite du contexte ; voir la convention en tête.
8. Prévalence de la carence en vitamine E et de l'AVED en Suisse : non trouvée.
9. Aucun critère diagnostique officiel ; les critères du §13 sont opérationnels.
10. **Statut SL** : lu dans AmiKo [S30] ; le site officiel sl.bag.admin.ch n'a pas pu être lu (application JavaScript). WebSearch « Spezialitätenliste BAG Konakion MM Ephynal » sans résultat OFSP.
11. **Déclaration OFSP, Suva/LAA, aptitude à la conduite, AI** pour E56 : aucune source trouvée ; aucune requête dédiée n'a donné de texte applicable.
12. **Classification en stades** : aucune classification officielle de gravité de la carence en vitamine E ou K n'a été trouvée ; seuls des seuils biologiques et des formes étiologiques sont sourcés.

## Matrice de complétude
| rubrique | statut | sources |
|---|---|---|
| 1. Question clinique et enjeu pour l'examen fédéral | ✔ §1, §12 ter | S2, S5, S6, S13, S29 |
| 2. Définition et périmètre CIM-10-GM (libellés OFS, inclusions, exclusions, notes BfArM) | ✔ §0, §2 | S1, S10, S28, S2, S5 |
| 3. Classifications et stades | ✔ partiel §0, §5 (formes étiologiques : carentielle, malabsorptive, génétique AVED/abêtalipoprotéinémie) ; LACUNE stades (lacune 12) | S2, S5, S28 |
| 4. Épidémiologie suisse puis européenne | ✔ §3 (Suisse : P53 seulement ; carence E/K adulte suisse = lacune 8) | S2, S3, S8, S11, S12, S14, S16, S17 |
| 5. Normal → pathologique | ✔ §4 | S2, S5, S7, S9, S15, S18, S19, S20 |
| 6. Étiologies et facteurs de risque | ✔ §5 | S2, S3, S5, S6, S7, S11, S12, S19, S21, S22 |
| 7. Anamnèse et symptômes (fréquences) | ✔ §6 (fréquences non chiffrées dans les sources) | S2, S3, S5, S6, S14 |
| 8. Examen clinique | ✔ §6 (sensibilité/spécificité non disponibles) | S5, S6, S14, S21, S22 |
| 9. Drapeaux rouges et urgences | ✔ §9 | S2, S18, S24 |
| 10. Examens complémentaires | ✔ §7 | S2, S3, S5, S6, S13, S15, S16, S23 |
| 11. Diagnostic différentiel | ✔ §8 | S2, S5, S6, S13, S16 |
| 12. Prise en charge suisse (FI datées) | ✔ §10 ; posologie adulte Konakion 10 mg = LACUNE 2 | S2, S3, S5, S18, S19, S20, S11, S27 |
| 13. Complications et pronostic | ✔ §1, §6, §9 | S2, S5, S14, S22 |
| 14. Suivi, prévention, dépistage | ✔ §10, §11 | S2, S3, S5, S11, S23 |
| 15. Situations particulières | ✔ §12 | S2, S5, S17, S18, S19, S20, S25, S26 |
| 16. Spécificités suisses | ✔ §12 bis (SL, codage, prophylaxie, SMOB) ; déclaration/Suva/conduite/AI = LACUNE 11 | S11, S23, S28, S30 |
| 17. Critères formels du diagnostic | ✔ §13 (critères opérationnels, aucun critère officiel : lacune 9) | S2, S3, S5, S6 |
| 18. Paramètres clés chiffrés | ✔ §14 | S2, S8, S9, S11, S18 |
| 19. Sous-codes CIM-10-GM couverts (E56.0, E56.1, E56.8, E56.9) | ✔ §0 | S1, S10, S28 |
| 20. Points d'examen fédéral | ✔ §12 ter | S29, S2, S3, S6, S13, S18, S28 |
