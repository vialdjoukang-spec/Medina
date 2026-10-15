# G63 — Polynévrite au cours de maladies classées ailleurs (N-05-Neurologie) — dossier de recherche

Cycle Betta 38, leçon 1 · agent C38-A4-NEUR (Opus 5.5) · 15.10.2026
Statut : recherche brute pour l'agent de rédaction. Audit différé — revue IA, distincte d'une validation médicale humaine.
Règle : chaque fait porte sa référence [Sx] (voir `sources.json`). Ce qui n'a pas été lu figure dans « Lacunes ». Aucune donnée de mémoire.

## 0. Question clinique
Un patient diabétique, alcoolique, dialysé, sous chimiothérapie ou porteur d'une maladie systémique décrit des fourmillements et des brûlures des pieds qui remontent lentement. La polyneuropathie est-elle réellement due à la maladie connue, ou faut-il chercher une autre cause, plus grave ou traitable (carence en B12, paraprotéine, vasculite, syndrome paranéoplasique, PIDC) ? Comment la confirmer au cabinet, protéger le pied et soulager la douleur selon les règles suisses ?

## 1. Définition et périmètre CIM-10-GM
- G63.-* est une catégorie « astérisque » : elle code la manifestation neurologique (polyneuropathie) d'une maladie de base codée ailleurs par un code primaire « croix » (†) [S1][S2].
- Sous-codes [S1][S2] :
| Code | Libellé (OFS) | Codes primaires † (BfArM) |
|---|---|---|
| G63.0* | Polynévrite au cours de maladies infectieuses et parasitaires classées ailleurs | ex. diphtérie, mononucléose infectieuse, lèpre, maladie de Lyme, oreillons, état après zona, syphilis tardive (y compris congénitale), formes tuberculeuses |
| G63.1* | Polynévrite au cours de maladies tumorales | C00–D48† |
| G63.2* | Polynévrite diabétique | E10–E14†, quatrième position .4 |
| G63.3* | Polynévrite au cours d'autres maladies endocriniennes et métaboliques | E00–E07†, E15–E16†, E20–E34†, E70–E89† |
| G63.4* | Polynévrite par carence nutritionnelle | E40–E64† |
| G63.5* | Polynévrite au cours d'affections disséminées du tissu conjonctif | M30–M35† |
| G63.6* | Polynévrite au cours d'autres affections ostéo-articulaires et des muscles | M00–M25†, M40–M96† |
| G63.8* | Polynévrite au cours d'autres maladies classées ailleurs | dont neuropathie urémique (N18.-†) |
- Exclusions au niveau du bloc G60–G64 (pas de la catégorie G63) : névralgie, névrite et radiculite SAI, névrite périphérique de la grossesse [S1].
- Sous-codes couverts par ce dossier : G63.0 (Lyme seulement, partiellement), G63.1 (paranéoplasique et, par extension clinique, neuropathie liée au traitement anticancéreux — voir lacune de codage), G63.2, G63.3 (amylose à transthyrétine), G63.4 (B12, thiamine, alcool-carence), G63.5 (vasculite, Sjögren), G63.8 (urémie). G63.6 sans contenu spécifique dans les sources lues.

## 2. Classifications cliniques
- Distribution [S4] : polyneuropathie distale symétrique sensitivo-motrice (forme la plus fréquente) ; polyradiculonévrite (atteinte proximale et distale, parfois tronc et nerfs crâniens) ; mononévrite multiple asymétrique (nerfs touchés simultanément ou successivement).
- Type de fibres [S4] : prédominance sensitive, motrice ou autonomique selon les fibres atteintes ; neuropathie des petites fibres = conduction nerveuse normale [S5].
- Évolution [S4] : aiguë (ex. Guillain-Barré), subaiguë (ex. vasculite), chronique (ex. diabète), très chronique (ex. formes héréditaires).
- Formes diabétiques [S4][S5] : polyneuropathie distale symétrique (forme typique) ; parésie oculomotrice ; amyotrophie ou plexopathie diabétique ; neuropathie aiguë douloureuse ou autonomique au début d'une insulinothérapie intensive (neuropathie induite par le traitement).
- Neuropathie diabétique aiguë douloureuse (série suisse CHUV/HUG) : deux sous-types, neuropathie induite par le traitement et cachexie neuropathique diabétique ; atteinte des petites fibres, survenue paradoxale après correction rapide de la glycémie, douleur intense, récupération éventuelle ; 4 patients, HbA1c moyenne 14,2 % → 7,0 % en 4,5 mois en moyenne, résolution en 12,7 mois en moyenne chez 3 patients [S27].

## 3. Épidémiologie
- Polyneuropathie : affection la plus fréquente du système nerveux périphérique de l'adulte, prévalence estimée 5–8 % selon l'âge [S4] ; études de population 1–4 %, dont 40–55 % attribuées au diabète [S5].
- Diabète = première cause en Europe [S4]. Prévalence de la neuropathie : 8–54 % (type 1) et 13–46 % (type 2) [S4] ; jusqu'à 50 % des diabétiques au cours du temps [S5]. Incidence ≈ 6100/100 000 années-personnes (type 2) et 2800/100 000 (type 1) [S5].
- Alcool : 22–66 % des alcooliques chroniques [S4] ; méta-analyse 44,2 % (IC 95 % 35,9–53 %) à l'examen clinique et 46,3 % (35,7–57,3 %) en neurographie [S9] ; ≈ 10 % des polyneuropathies dans une étude de population norvégienne [S9].
- Neuropathie induite par la chimiothérapie : prévalence souvent citée 30–40 %, très variable selon le produit [S4].
- Idiopathique : cause non trouvée jusque dans 30 % des cas [S4] ; dans une cohorte de 921 neuropathies des petites fibres (Maastricht), 53 % sans cause, 47 % avec au moins une affection associée [S10].
- Urémie : ≈ 90 % des dialysés ; jusqu'à 70 % des patients non encore dialysés dans les cohortes récentes [S19].
- Douleur : environ la moitié des polyneuropathies [S4] ; 30–50 % des neuropathies diabétiques [S5] ; 42 % (IC 29–56 %) des neuropathies alcooliques [S9].

## 4. Mécanismes — du normal au pathologique
- Axonopathie dépendante de la longueur (« dying back ») : les axones sensitifs les plus longs dégénèrent d'abord à leur extrémité ; d'où la distribution en chaussettes puis en gants [S5].
- Diabète [S5] : hyperglycémie → voies des polyols et des hexosamines → espèces réactives de l'oxygène et inflammation ; produits de glycation avancée via RAGE ; surcharge de substrats → défaillance mitochondriale, baisse d'ATP, acylcarnitines toxiques pour les cellules de Schwann et les neurones ; microangiopathie (épaississement de la membrane basale, vasodilatation épineurale altérée) ; perte de soutien neurotrophique ; insulinorésistance neuronale, hypothèse expliquant le moindre bénéfice du contrôle glycémique dans le type 2.
- Séquence clinique diabétique [S5] : petites fibres d'abord (brûlure distale nocturne, perte piqûre/froid), grosses fibres ensuite (vibration, proprioception) ; réflexes achilléens perdus tôt ; faiblesse des pieds tardive.
- Alcool [S4][S9] : malnutrition (vitamines B), toxicité directe de l'éthanol, acétaldéhyde (variant ALDH2*2), stress oxydatif ; mécanisme non résolu [S9]. Distinction de Koike [S9] : neuropathie alcoolique lente, sensitive, petites fibres ; neuropathie par carence en thiamine souvent rapide (< 1 mois dans 56 %), motrice, grosses fibres.
- Urémie [S19] : ralentissement diffus sensitif et moteur → effet toxique systémique ; aucune toxine urémique formellement causale ; l'hyperkaliémie altère la fonction nerveuse de façon dose-dépendante et réversible.
- Thiamine : 0,4 mg de thiamine nécessaire en moyenne pour produire ≈ 4200 kJ par le métabolisme glucidique → le besoin croît avec l'apport glucidique [S26].
- Vitamine B12 : besoin journalier ≈ 1–2 µg, réserve totale 2–5 mg dont ≈ 1 mg hépatique [S25] ; une exposition prolongée au protoxyde d'azote peut induire une carence fonctionnelle avec atteinte neurologique grave malgré des réserves normales [S25].
- Paranéoplasique [S11] : neuronopathie sensitive = atteinte des neurones des ganglions rachidiens dorsaux (déficit sensitif non dépendant de la longueur) ; anticorps « à haut risque » (> 70 % de cancer associé), p. ex. anti-Hu (> 85 % de cancer bronchique à petites cellules).

## 5. Causes à rechercher (par sous-code)
- G63.2 diabète ; facteurs de risque [S4][S5] : durée du diabète, HbA1c, rétinopathie, néphropathie, HTA, artériopathie, obésité, dyslipidémie (hypertriglycéridémie, HDL bas), alcool, tabac, âge, grande taille, sédentarité.
- G63.4 carences [S4] : B12 (paresthésies subaiguës des pieds, ataxie sensitive ; parésie rare ; myélo-neuropathie combinée avec réflexes vifs et signes pyramidaux ; ≈ 50 % sans anémie macrocytaire) ; B6 (carence : neuropathie subaiguë, p. ex. pompe Duodopa, perte de poids rapide ; surdosage : neuropathie aussi). Metformine : contrôler la B12 [S5].
- Alcool [S4][S9] : risque lié à la dose cumulée vie entière ; > 100 g/j pendant plusieurs années considéré comme probablement pathogène [S4] ; consommation continue ≈ 30 % de neuropathie contre 11 % pour les buveurs épisodiques [S9].
- G63.1 tumeurs [S4][S11] : neuronopathie sensitive et polyradiculonévrite paranéoplasiques (anti-Hu, CV2/CRMP5, amphiphysine ; CBPC, sein) ; paraprotéines : IgM anti-MAG (démyélinisante distale), POEMS, IgM élevée → Waldenström, IgG élevée → amylose AL [S4]. Un Guillain-Barré ou une PIDC chez un cancéreux n'est pas paranéoplasique sans anticorps à haut risque [S11].
- Neuropathie liée au traitement anticancéreux [S4] : platines, vinca-alcaloïdes, taxanes, inhibiteurs du protéasome (bortézomib : surtout petites fibres), anticorps ; inhibiteurs de points de contrôle : neuropathie immunitaire aiguë ou chronique ; début sensitif dans les 2 premiers mois ; oxaliplatine : neurotoxicité aiguë réversible en 2–3 jours dans 60–80 %, atteinte persistante chez 73 % après traitement prolongé ; phénomène de « coasting » (aggravation après l'arrêt) avec les platines, rarement la vincristine ; ≈ 40 % de douleur chronique ; toxicité selon dose unitaire, dose cumulée et durée.
- G63.3 [S18] : amylose héréditaire à transthyrétine — polyneuropathie axonale progressive dépendante de la longueur touchant d'abord thermo-algésie ; drapeaux rouges : dysautonomie sans diabète (hypotension orthostatique, diarrhée/constipation, dysfonction érectile), perte de poids importante, syndrome du canal carpien, troubles conductifs cardiaques, syncope ; antécédent familial absent dans > 50 % des formes tardives non endémiques.
- G63.5 [S14][S10] : neuropathie vasculitique — atteinte sensitive ou sensitivo-motrice, asymétrique/multifocale, prédominant aux membres inférieurs et en distal, douloureuse, évolution aiguë par poussées, neurophysiologie non démyélinisante ; orientent vers une vasculite systémique : atteinte d'autres organes, ANCA, cryoglobulines, VS ≥ 100 mm/h [S14]. Sjögren 1,3 %, sarcoïdose 3,0 %, maladie cœliaque 0,5 % dans la cohorte petites fibres [S10].
- G63.0 [S1][S17] : Lyme — neuroborréliose définie par symptômes neurologiques + pléiocytose du LCR + anticorps intrathécaux anti-Borrelia [S17]. Autres infections listées par la CIM sans contenu clinique lu.
- G63.8 urémie [S19].

## 6. Anamnèse et examen
- Anamnèse : personnelle, systématique, professionnelle, sociale, familiale [S4] ; médicaments et toxiques (métronidazole, nitrofurantoïne, quinolones, thalidomide, tacrolimus, colchicine, amiodarone, lithium, disulfirame, pyridoxine, phénytoïne ; arsenic, plomb, mercure, thallium, solvants, acrylamide, sulfure de carbone) [S4].
- Symptômes et signes (tableau 1 de [S4]) : sensitifs (engourdissement, fourmillements, brûlure, paresthésies au froid, décharges, instabilité, chutes / hypoesthésie, hypoalgésie, allodynie, ataxie sensitive) ; moteurs (faiblesse, amyotrophie, crampes, fasciculations / parésie, aréflexie) ; autonomiques (peau sèche, troubles trophiques, vessie, diarrhée, tachycardie, gastroparésie, dysfonction érectile / anhidrose, tachycardie de repos).
- Signe clé : aréflexie distale + baisse de la pallesthésie ou de la piqûre = sensible et spécifique de polyneuropathie [S4].
- Dépistage suisse au cabinet chez le diabétique de type 2 [S6] : dès le diagnostic, au moins 1×/an, pieds nus des deux côtés + chaussures habituelles ; monofilament 10 g sur 4 sites prédéfinis non calleux (normal = identifiés clairement) et/ou diapason gradué de Rydel-Seiffer 128/64 Hz (normal dépendant de l'âge, au moins ≥ 5/8) ; anamnèse ciblée (brûlures, piqûres, dysesthésies, engourdissement) ; peau (callosités, lésions, sudation, sécheresse, température) ; déformations ; pouls pédieux et tibial postérieur ; chaussures.
- Technique [S7] : monofilament démontré d'abord sur l'avant-bras, yeux fermés, pression jusqu'à flexion, ≈ 1 s ; sensibilité protectrice suffisante = 4 sites sur 4 correctement identifiés ; l'incapacité à sentir le filament en ≥ 1 site est associée à une neuropathie des grosses fibres ; sensibilité 65–90 % et spécificité 35–85 % pour le risque d'ulcère. Diapason 128 Hz sur l'articulation métatarso-phalangienne médiale de l'hallux, démontré au poignet ; pathologique ≤ 4/8 ; moins prédictif d'ulcère que le monofilament.
- Le guide suisse 2023 définit « pas de neuropathie » par monofilament 4/4 et pallesthésie > 4/8 [S8].

## 7. Diagnostic, examens et différentiel
- Le diagnostic de neuropathie diabétique exige des symptômes ou signes de dysfonction nerveuse périphérique après exclusion d'autres causes ; l'anamnèse et l'examen suffisent dans la plupart des cas [S5].
- Laboratoire de base [S4] : CRP, formule sanguine, électrolytes, fonctions hépatique et rénale, électrophorèse et immunofixation des protéines, protéinurie de Bence Jones, TSH, HbA1c, CDT, vitamine B12.
- Laboratoire étendu [S4] : holotranscobalamine ; vitamines B1, B6, E ; AAN ; p- et c-ANCA ; cryoglobulines ; sérologies hépatites, VIH, Borrelia ; anti-GM1 IgM, anti-GQ1b, anti-MAG ; LCR avec sérologies.
- Neurophysiologie [S4][S5] : neurographie, EMG, potentiels évoqués ; diabète : amplitudes et vitesses réduites, membres inférieurs avant supérieurs (valeurs normales du nerf sural citées en exemple : > 6 µV et > 39 m/s) [S5] ; petites fibres : neurographie normale, biopsie cutanée (densité des fibres intra-épidermiques) étalon, tests quantitatifs sensitifs [S4][S5].
- Imagerie : échographie nerveuse, neurographie IRM [S4].
- LCR : si cause inflammatoire suspectée [S4]. Biopsie nerveuse : seulement si neuropathie modérée à sévère progressive non élucidée par des méthodes moins invasives ; distingue démyélinisation et axonopathie, montre inflammation ou amylose [S4]. Vasculite : biopsie combinée nerf-muscle-peau augmente le rendement [S4].
- Génétique : PMP22, GJB1, MPZ, MFN2, panel, exome/génome [S4] ; amylose TTR : biopsie (graisse abdominale, rectum, sural, glandes salivaires labiales ; rouge Congo, biréfringence vert pomme, immunohistochimie) + génotypage TTR, les deux requis [S18].
- Signes atypiques chez un diabétique imposant un avis neurologique et un bilan étendu [S5] : début aigu, distribution non dépendante de la longueur, prédominance motrice, asymétrie (bilan : B12, thyroïde, immunofixation, LCR, IRM, génétique, rarement biopsie).
- Différentiel immunitaire [S4][S13] : Guillain-Barré (incidence 1–2/100 000/an ; maximum en ≤ 4 semaines) ; PIDC (prévalence 2–3/100 000 ; évolution ≥ 8 semaines ; faiblesse proximale et distale symétrique, aréflexie ; démyélinisation électrophysiologique ; LCR < 10 leucocytes/µL avec protéines élevées) [S4] ; la révision EAN/PNS 2021 distingue PIDC typique et variantes (multifocale, focale, distale, motrice, sensitive) et ne garde que deux niveaux de certitude (PIDC, PIDC possible) [S13]. Neuropathie motrice multifocale : 0,6–2/100 000, faiblesse distale asymétrique, blocs de conduction, anti-GM1 IgM ≈ 50 % [S4].
- Paranéoplasique [S11] : score PNS-Care ; « définitif » ≥ 8 (phénotype + anticorps à haut ou moyen risque + cancer) ; dépistage tumoral rapide, répété tous les 4–6 mois pendant 2 ans si phénotype à haut risque + anticorps à haut risque et premier bilan négatif.

## 8. Urgences et drapeaux rouges
- Paralysie ascendante après infection digestive ou respiratoire → Guillain-Barré : hospitalisation rapide ; risque de troubles conductifs cardiaques et d'insuffisance respiratoire [S4].
- Atteinte multifocale progressive ou neuropathie distale symétrique subaiguë → suspecter une vasculite [S4].
- Neuropathie sévère sans cause → centre spécialisé [S4].
- Pied diabétique (Suisse 2023) [S8] : niveau 3 « urgence » = cellulite, gangrène, infection systémique, ischémie aiguë, pied de Charcot aigu ; drapeaux rouges = infection locale avec signes systémiques ou progression rapide (fièvre, IDSA 4), ischémie critique (IPS < 0,5, tcPO2 < 25 mmHg, pression d'orteil < 30 mmHg), nécrose, suspicion de Charcot, neuropathie aiguë douloureuse, insuffisance rénale terminale (dialyse) ; suivi au moins hebdomadaire à tous les niveaux.

## 9. Prise en charge suisse
### 9.1 Traiter la cause
- Diabète : facteurs de risque, mode de vie avec entraînement physique, soins symptomatiques (douleur, dysautonomie, pied) [S4]. Contrôle glycémique : efficace dans le type 1 (différence de risque annualisée −1,84 ; IC −2,56 à −1,11), non significatif dans le type 2 (−0,58 ; IC −1,17 à 0,01) ; un objectif HbA1c < 6 % a accru la mortalité dans le type 2 ; un contrôle trop agressif peut provoquer une neuropathie induite par le traitement [S5].
- Alcool : abstinence et correction nutritionnelle ; régression possible sur des mois à des années [S4] ; vitamines B (dont thiamine) : meilleure preuve disponible mais rare [S9] ; amélioration sensitive en jours, motrice en semaines à mois, jusqu'à 2 ans dans les formes sévères ; séquelles possibles [S9].
- Thiamine (Benerva®) [S26] : 100 mg/2 j (symptômes légers), 100 mg/j (modérés), 200–300 mg/j per os (graves) ; voie i.m. ou i.v. lente jusqu'à 200 mg/j dans l'avitaminose sévère (béribéri, Wernicke, cardiomyopathie alcoolique).
- Vitamine B12 : substituer rapidement [S4]. Vitarubine® Dépôt (hydroxocobalamine) [S25] : i.m. ; cas aigus 1000 µg 2–3×/semaine ; entretien de l'anémie pernicieuse 1000 µg tous les 2–3 mois, à vie ; troubles de la marche depuis > 2 ans pas toujours réversibles ; réponse insuffisante → penser à une carence associée en fer ou en folates.
- Toxiques : éviction et élimination ; métaux lourds : chélateurs, diurèse forcée [S4].
- Urémie : la transplantation rénale est considérée comme le traitement le plus efficace ; l'hémodiafiltration pourrait améliorer la fonction nerveuse ; la restriction potassique est une piste [S19].
- Vasculite non systémique [S14] : corticoïdes en monothérapie ≥ 6 mois en première ligne ; association (cyclophosphamide, azathioprine, méthotrexate) si progression rapide ; entretien 18–24 mois.
- Amylose TTR (consensus 2016) [S18] : tafamidis au stade I ; transplantation hépatique historique ; suivi multidisciplinaire (neurologue, cardiologue, ophtalmologue), génétique familiale.
- Chimiothérapie : surveillance avec échelles ; adaptation selon dose et durée [S4]. Recommandations ESMO-EONS-EANO 2020 non lues [S12].
### 9.2 Douleur neuropathique
- Première ligne (NeuPSIG/GRADE) : antidépresseurs tricycliques, IRSN (duloxétine), prégabaline, gabapentine ; deuxième ligne : lidocaïne topique, capsaïcine haute concentration, tramadol ; troisième ligne : opioïdes forts, toxine botulique A ; NNT : IRSN 6,4 ; prégabaline 7,7 ; gabapentine 7,2 ; capsaïcine 8 % 10,6 [S16]. EFNS 2010 : preuves de niveau A pour tricycliques, prégabaline, gabapentine, tramadol, opioïdes, duloxétine, venlafaxine ; association tricyclique-gabapentine et gabapentine-opioïde utile [S15]. Revue allemande : gabapentinoïdes, tricycliques, duloxétine en premier choix ; capsaïcine 8 %, lidocaïne, tramadol en deuxième ; opioïdes forts en troisième [S4].
- Prégabaline (Lyrica®) [S20] : indiquée pour douleurs neuropathiques périphériques et centrales de l'adulte ; début 150 mg/j en 2–3 prises, 300 mg/j après 3–7 jours, max 600 mg/j après 7 jours de plus ; ClCr 30–60 mL/min : 75–300 mg/j ; ClCr < 30 : ne pas utiliser (FI) ; répondeurs 50 % : 33–46 % (300 mg) et 39–48 % (600 mg) contre 15–30 % placebo ; prise de poids ≥ 7 % chez 5,2 % des diabétiques ; insuffisance cardiaque rapportée chez des âgés ; éviter pendant la grossesse sauf bénéfice net, contraception efficace.
- Gabapentine (Neurontin®) [S22] : douleur neuropathique diabétique ou post-zostérienne ; J1 300 mg, J2 600 mg, J3 900 mg/j en 3 prises ; entretien 900–3600 mg/j ; ClCr 50–79 : 600–1200 ; 30–49 : 300–900 ; 15–29 : 150–600 ; < 15 : 150–300 mg/j.
- Duloxétine (Duloxetin-Mepha®) [S21] : douleur neuropathique diabétique ; 60 mg 1×/j ; pas de bénéfice supplémentaire > 60 mg ; évaluer après 2 mois, puis au moins tous les 3 mois ; contre-indiquée en cas d'insuffisance hépatique, de ClCr < 30 mL/min et avec IMAO irréversibles ; HbA1c +0,3 % à 52 semaines contre placebo.
- Amitriptyline (Saroten®) [S23] : douleurs neuropathiques de l'adulte ; début 10–25 mg le soir, + 10–25 mg tous les 3–7 jours ; 25–75 mg/j ; > 100 mg avec prudence ; effet en 2–4 semaines ; contre-indiquée : infarctus récent, bloc ou trouble du rythme, insuffisance coronarienne, IMAO, hépatopathie sévère ; effet analgésique indépendant de l'effet antidépresseur (blocage sodique, potassique, NMDA).
- Capsaïcine 8 % (Qutenza®) [S24] : douleurs neuropathiques périphériques ; jusqu'à 4 patchs ; 30 min sur les pieds, 60 min ailleurs ; intervalle minimal 60 jours ; inspection minutieuse des pieds avant chaque application chez le diabétique ; gants nitrile.
- Insuffisance rénale : tricycliques mal tolérés chez l'âgé, à éviter en cas d'arythmie, d'insuffisance cardiaque, d'hypotension orthostatique, de rétention urinaire ; gabapentinoïdes à adapter à la clairance [S19][S20][S22].
### 9.3 Non médicamenteux
- Physiothérapie : équilibre, coordination, proprioception, renforcement, prévention des déformations ; ergothérapie, aides techniques ; activité physique encouragée [S4].
- Pied diabétique (SGED) [S6] : catégorie IWGDF 0 (sans PNP, sans artériopathie, sans déformation) → contrôle 1×/an ; 1 (PNP sans artériopathie ni déformation) et 2a (PNP + déformation) → au moins 2×/an, soins protecteurs, chaussures adaptées ; 2b (PNP + artériopathie) → au moins 4×/an, bilan de revascularisation ; 3a/3b (après ulcère / amputation) → au moins 4×/an ; ulcère aigu, Charcot ou nécrose → centre de niveau 3, en urgence pour la gangrène. Inscription AI pour chaussures adaptées au diabète si < 65 ans (H) / < 64 ans (F) [S6].
- Pronostic du pied [S7] : après un ulcère, risque de récidive jusqu'à 36 fois plus élevé, récidive jusqu'à 40 % à 1–2 ans ; réamputation cumulée 27 % à 1 an, 48 % à 3 ans, 61 % à 5 ans ; mortalité cumulée à 5 ans 46 % après amputation.

## 10. Suivi
- Dépistage de la neuropathie : au diagnostic puis annuellement dans le type 2 ; 5 ans après le diagnostic puis annuellement dans le type 1 [S5] ; Suisse : au moins 1×/an dès le diagnostic du type 2 [S6].
- Duloxétine : réévaluation à 2 mois puis ≥ tous les 3 mois [S21] ; amitriptyline : réévaluation régulière [S23].
- Paranéoplasique : surveillance tumorale 2 ans [S11]. Amylose TTR : contrôle à 3 mois, bilan pluridisciplinaire à 6 et 12 mois, puis ≥ 2×/an [S18].

## 11. Situations particulières
- Grossesse : prégabaline à éviter au premier trimestre sauf bénéfice net (malformations majeures signalées ; une étude nordique de > 2700 expositions n'a pas montré de risque significatif) [S20].
- Sujet âgé : pas de réduction de la prégabaline sauf insuffisance rénale [S20] ; amitriptyline 10–25 mg le soir au départ [S23].
- Dialyse : neuropathie ≈ 90 %, dysautonomie > 50 % des hémodialysés [S19].
- Protoxyde d'azote : carence fonctionnelle en B12 possible malgré des réserves normales [S25].

## 12. Critères formels (pour le div.alert)
- Diagnostic de polyneuropathie diabétique : symptômes et/ou signes de dysfonction nerveuse périphérique chez un diabétique, après exclusion des autres causes [S5].
- Perte de sensibilité protectrice (Suisse) : monofilament 10 g < 4/4 sites et/ou pallesthésie ≤ 4/8 au diapason de Rydel-Seiffer [S7][S8].
- Neuroborréliose définie : 3 critères (symptômes neurologiques, pléiocytose du LCR, anticorps intrathécaux) ; possible : 2 sur 3 [S17].
- Syndrome paranéoplasique définitif : score PNS-Care ≥ 8 [S11].
- Neuropathie vasculitique cliniquement probable : atteinte sensitive ou sensitivo-motrice, asymétrique/multifocale, distale, prédominant aux membres inférieurs, douloureuse, évolution aiguë par poussées, neurophysiologie non démyélinisante [S14].

## 13. Paramètres clés (pour le div.key)
- Prévalence de la polyneuropathie : 5–8 % selon l'âge [S4] ; diabète = 1re cause ; idiopathique ≤ 30 % [S4].
- Monofilament 10 g, 4 sites/pied ; diapason 128 Hz, pathologique ≤ 4/8 [S7].
- Contrôle du pied diabétique : 1×/an (cat. 0), ≥ 2×/an (1, 2a), ≥ 4×/an (2b, 3) [S6].
- Prégabaline 150 → 300 → 600 mg/j ; gabapentine 900–3600 mg/j ; duloxétine 60 mg/j ; amitriptyline 25–75 mg/j [S20][S21][S22][S23].
- Hydroxocobalamine 1000 µg i.m. 2–3×/semaine en phase aiguë, puis tous les 2–3 mois [S25].
- PIDC ≥ 8 semaines ; Guillain-Barré maximum ≤ 4 semaines [S4].

## Lacunes explicites
1. Aucune recommandation de la Société suisse de neurologie ni article du Swiss Medical Forum sur la polyneuropathie n'a pu être lu (domaine medicalforum.ch injoignable ; recherche web épuisée). La revue suisse Blanquet & Humm 2025 [S3] n'est connue que par son résumé.
2. Ligne directrice allemande DGN « Diagnostik bei Polyneuropathien » (AWMF 030-067) non lue (page vide) ; ses éléments ne sont repris qu'à travers [S4].
3. ESMO-EONS-EANO 2020 [S12] non lue : aucune recommandation de prévention ou de traitement de la neuropathie induite par la chimiothérapie (duloxétine, cryothérapie, etc.) ne doit être rédigée sur cette base. Le rattachement CIM de la neuropathie médicamenteuse (G62.0 vs G63.1) n'a pas été vérifié.
4. Lignes directrices EAN/PNS PIDC 2021 [S13], PNS vasculite 2010 [S14], EFNS douleur 2010 [S15], NeuPSIG 2015 [S16] et EFNS Lyme [S17] : résumés seulement. NICE CG173 inaccessible (403).
5. G63.0 : lèpre, VIH, diphtérie, syphilis, zona — aucune source clinique lue. G63.3 : hypothyroïdie, acromégalie, porphyrie — non documentées ; amylose TTR seulement selon un consensus de 2016 (thérapies géniques actuelles et statut suisse non vérifiés). G63.6 : aucun contenu.
6. Recommandation suisse récente sur le dépistage de la neuropathie diabétique au-delà des documents SGED 2013/2016/2023 non trouvée ; IWGDF 2023 prévention non lue.
7. Données suisses d'épidémiologie de la polyneuropathie absentes.
8. Neuropathie diabétique aiguë douloureuse : seule la série suisse [S27] (4 cas) lue en résumé.
