# G80 — Infirmité motrice cérébrale (N-05-Neurologie) — dossier de recherche

Cycle Betta 39, leçon 2 · agent C39-A3-NEUR (Opus 5.5) · 15.10.2026
Statut : recherche brute pour l'agent de rédaction. Audit différé — revue IA, distincte d'une validation médicale humaine.
Règle : chaque fait porte sa référence [Sx] (voir `sources.json`). Ce qui n'a pas été lu figure dans « Lacunes ». Aucune donnée de mémoire.
Méthode : quota WebSearch épuisé pour la session ; recherche par PubMed (résumés lus), WebFetch d'URL connues (BfArM, PMC) et `tools/swissmedic_fi.py` (AIPS via AmiKo). NICE NG62 inaccessible (HTTP 403) ; page SCPE du JRC introuvable (404).

## 0. Question clinique
Un nourrisson ancien prématuré ou ayant souffert d'une atteinte cérébrale néonatale présente un retard moteur, une asymétrie ou une hypertonie. Comment poser tôt le diagnostic de paralysie cérébrale (PC), la classer (type, topographie, niveau fonctionnel), écarter une maladie progressive ou génétique qui la mime, puis organiser une prise en charge multidisciplinaire (rééducation, spasticité, hanches, épilepsie, nutrition) selon les données suisses et européennes ?

## 1. Définition et périmètre CIM-10-GM
- Définition internationale (rapport d'avril 2006) : groupe de troubles permanents du développement du mouvement et de la posture, entraînant une limitation d'activité, attribués à des perturbations non progressives survenues dans le cerveau fœtal ou du nourrisson en développement ; les troubles moteurs s'accompagnent souvent de troubles sensoriels, cognitifs, de communication, de comportement, d'épilepsie et de problèmes musculosquelettiques secondaires [S2 (résumé), S4]. Les personnes sans limitation d'activité ne doivent pas être incluses [S2].
- « Permanents mais non immuables » : la lésion est non progressive, mais le tableau change avec l'âge (maturation, plasticité, complications orthopédiques) [S4].
- Registres : diagnostic définitif rarement possible avant quelques années ; âge de 5 ans souvent retenu par les registres, au moins 4 ans recommandé avant confirmation [S4].
- CIM-10-GM 2024, catégorie G80.- Infantile Zerebralparese (bloc G80–G83) [S1] :
  - G80.0 spastique tétraplégique (inclut quadriplégique) ;
  - G80.1 spastique diplégique (inclut paralysie spastique congénitale cérébrale ; PC spastique SAI) ;
  - G80.2 hémiplégique infantile ;
  - G80.3 dyskinétique (inclut athétosique et dystonique) ;
  - G80.4 ataxique ;
  - G80.8 autres (inclut syndromes mixtes) ;
  - G80.9 sans précision (PC SAI).
  - Exclusion : paraplégie spastique héréditaire → G11.4 [S1].
- Intitulés français OFS : nosologie du dépôt `nosology/fragments/S08.json` (G80.0–G80.9).

## 2. Classifications
- SCPE (Surveillance of Cerebral Palsy in Europe), système actuel ayant remplacé Ingram (1955) et Hagberg (1976) [S4] :
  - spastique : unilatérale ou bilatérale (sans subdivision en diplégie, triplégie, tétraplégie) ;
  - dyskinétique : dystonique (hypertonique-hypokinétique) ou choréo-athétosique (hypotonique-hyperkinétique) ; si le sous-type est difficile, « dyskinétique » ;
  - ataxique (tonus surtout diminué) ;
  - tableaux mixtes classés selon la composante prédominante [S4].
- Remarque pour la rédaction : la CIM-10-GM garde la topographie (tétra-, di-, hémiplégie) alors que la SCPE parle d'uni-/bilatéral [S1, S4].
- Fonction motrice globale : GMFCS (Gross Motor Function Classification System), 5 niveaux, par tranches d'âge (< 2, 2–4, 4–6, 6–12, 12–18 ans) [S4] :
  - I marche sans restriction ; II marche avec limitations ; III marche avec aide technique ; IV mobilité limitée, fauteuil électrique possible ; V déplacé en fauteuil par un tiers [S4].
  - GMFCS valide et fiable dès 2 ans [S9].
- Fonction manuelle : MACS et BFMF cités [S4, S8] ; niveaux MACS non lus (lacune).
- IRM : MRICS de la SCPE, 5 groupes : A malformations ; B lésion prédominante de la substance blanche ; C lésion prédominante de la substance grise ; D divers ; E normale [S4, S8]. IRM anormale chez > 80 % [S4]. Les lésions bilatérales s'associent à une atteinte motrice et à des déficiences associées plus sévères que les unilatérales (3818 enfants, 20 registres) [S8].

## 3. Épidémiologie
- Europe : 2,08/1000 naissances vivantes (SCPE 1980–1990) ; fréquence > 70 fois plus élevée sous 1500 g qu'à ≥ 2500 g [S4, résumé S4].
- Selon l'âge gestationnel (méta-analyse citée) : 146/1000 avant 28 SA ; 62/1000 à 28–31 SA ; 7/1000 à 32–36 SA ; 1,13/1000 à terme [S4].
- Tendance SCPE 1980–2003 : 1,90 → 1,77/1000 ; baisse surtout à 1000–1499 g (70,9 → 35,9/1000) [S4]. Chez les < 1500 g, 60,6 → 39,5/1000 de 1980 à 1996, baisse liée à la PC spastique bilatérale ; 94 % spastiques, dont 24 % unilatérales [S10].
- Suisse (Swiss-CP-Reg, fondé 2017) : 546 participants (08.2017–08.2021) ; 55 % garçons ; 56 % nés à terme ; 73 % diagnostiqués avant 2 ans (médiane 18 mois) ; 76 % spastiques ; GMFCS I–II 59 %, III 12 %, IV–V 29 % ; QI plus bas avec un GMFCS plus élevé (sous-groupe de 170) [S3].
- Suisse, cohorte nationale < 30 SA nés en 2006 : PC chez 14/235 (6 %) à 5 ans [S11].
- PC ataxique : 3,8 % des PC dans 20 registres SCPE (679 enfants) ; 79 % nés à terme ; ~70 % marchent ; 40 % déficience intellectuelle sévère ; IRM normale 29 %, malformations 28,5 % ; syndromes génétiques 9 % ; bilan génétique complet particulièrement recommandé [S7].
- Pronostic global (pays à hauts revenus) : 2 sur 3 marcheront, 3 sur 4 parleront, 1 sur 2 aura une intelligence normale [S5].

## 4. Mécanismes (normal → pathologique)
- Cerveau en développement : la nature de la lésion dépend de la période de vulnérabilité (malformation précoce, substance blanche périventriculaire chez le prématuré, substance grise profonde/cortex à terme) — principe du MRICS [S8].
- Facteurs prénataux ≈ 75 % des cas ; néonatals/nourrisson 10–18 % ; la part périnatale est moindre que ce que l'on croyait [S4].
- Prématurité et faible poids : facteur majeur ; plus la grossesse est courte, plus l'atteinte est sévère [S4].
- AVC néonatal : topographie et volume de l'infarctus prédisent la PC (hémiplégie) [résumés PubMed listés S12, lecture limitée au titre — à ne pas utiliser sans relecture].
- Génétique : variants de novo (SNV, CNV), mitochondriaux, rarement expansions de répétitions ; rendement maximal si IRM normale, évolution atypique ou signes neurodéveloppementaux supplémentaires ; exome en trio en première intention, puis puce ADN ou génome [S6].
- Spasticité : le baclofène stimule les récepteurs GABA-B médullaires et inhibe les réflexes mono- et polysynaptiques en réduisant la libération de glutamate et d'aspartate [S14] ; la toxine botulique A bloque la libération d'acétylcholine à la jonction neuromusculaire → dénervation chimique et paralysie flasque locale [S13].

## 5. Clinique, comorbidités
- Signes moteurs apparaissant et évoluant avant 2 ans [S5].
- Comorbidités [S3, S4] :
  - épilepsie 15–60 % (tétraplégie 50–94 % ; hémiplégie 33–50 % ; diplégie/ataxique 16–27 %), surtout la 1re année ; risque de SUDEP 1,1–3,4/1000 enfants/an [S4] ;
  - déficience intellectuelle 40–65 % [S4] ;
  - dysphagie oropharyngée ≈ 2 enfants sur 3 ; troubles digestifs fréquents [S4] ;
  - trouble de la parole > 50 % ; 97 % des PC dyskinétiques avec parole sévèrement atteinte ou absente vs 90 % de parole compréhensible en spastique unilatérale [S4] ;
  - vision, audition, douleur, sommeil, alimentation, cognition [S3] ;
- Hanches : déplacement (migration de Reimers > 40 %) chez 18 % de 212 enfants ; dès 2–3 ans ; risque 0 % en GMFCS I à 64 % en GMFCS V ; 0 % en ataxie pure à 79 % en tétraplégie spastique ; l'amplitude articulaire est un mauvais indicateur → surveillance radiographique selon âge et GMFCS [S9].

## 6. Diagnostic (précoce) et examens
- Diagnostic possible avant 6 mois d'âge corrigé (historiquement 12–24 mois) [S5].
- Avant 5 mois d'âge corrigé : IRM à terme (sensibilité 86–89 %), General Movements de Prechtl (98 %), Hammersmith Infant Neurological Examination HINE (90 %) [S5].
- Après 5 mois : IRM (86–89 %), HINE (90 %), DAYC (indice C 83 %) [S5].
- Combinaison anamnèse + imagerie + examen neurologique standardisé + évaluation motrice concordants ; orientation rapide vers une intervention précoce [S5].
- IRM préférée ; échographie transfontanellaire chez le nourrisson ; EEG (vidéo-EEG), bilans psychologique, visuel, audiométrique [S4].
- Génétique : voir § 4 ; particulièrement en cas de PC ataxique, IRM normale, évolution atypique [S6, S7].

## 7. Diagnostic différentiel
- Mimes de PC : erreurs innées du métabolisme traitables et maladies génétiques ; régression ou progression = signal d'alarme [S4, S6].
- Paraplégie spastique héréditaire (exclue de G80, codée G11.4) [S1].
- Détails des drapeaux rouges (NICE NG62) non lus → lacune.

## 8. Prévention (anténatale et néonatale)
- Sulfate de magnésium aux femmes à risque d'accouchement < 34 SA : réduit la PC à 2 ans d'âge corrigé (RR 0,71 ; IC 95 % 0,57–0,89 ; 6 ECR, 6107 enfants ; NNT 60) et décès ou PC (RR 0,87) ; pas de différence démontrée à l'âge scolaire (preuve faible) ; plus d'effets indésirables maternels imposant l'arrêt (RR 3,21) [S15].
- Préventions efficaces (synthèse GRADE) : corticoïdes anténatals, sulfate de magnésium, caféine, hypothermie néonatale [S16].

## 9. Prise en charge
- Principe : rééducation intensive fondée sur la neuroplasticité, multidisciplinaire [S4, S5].
- Interventions efficaces (feu vert, revue systématique 2019) : thérapie par contrainte induite, entraînement bimanuel, entraînement orienté vers des objectifs, entraînement spécifique à la tâche, plâtres, renforcement, tapis roulant, programmes à domicile ; médical/chirurgical : antiépileptiques, bisphosphonates, toxine botulique (± ergothérapie, ± plâtre), diazépam, soins dentaires, surveillance des hanches, baclofène intrathécal, correction de scoliose, rhizotomie dorsale sélective [S16]. Feu rouge cité : thérapie crânio-sacrée, attelle de hanche, oxygène hyperbare, NDT, intégration sensorielle [S4 citant Novak 2013].
- Toxine botulique A : spasticité focale ; effet ≈ 3–8 mois ; doit être couplée à la rééducation [S4] ; consensus européen 2009 : approche intégrée multidisciplinaire, buts réalistes, courbes GMFCS/GMFM (36 institutions, 9 pays, > 10 000 patients) [S17].
- Dysport® (FI Swissmedic, mai 2026) [S13] :
  - indications : spasticité focale des membres supérieurs et inférieurs (pied équin dynamique) dès 2 ans ;
  - membre supérieur enfant : max 16 U/kg ou 640 U (unilatéral), 21 U/kg ou 840 U (bilatéral), la plus faible ;
  - membre inférieur enfant : max 15 U/kg unilatéral, 30 U/kg bilatéral, ≤ 500 U par jambe, ≤ 1000 U ou 30 U/kg par séance ; ≤ 0,5 ml par site ;
  - unités non interchangeables entre préparations ; mises en garde : propagation à distance, dysphagie, troubles respiratoires, risque accru si troubles de déglutition préexistants ; effet maximal vers 2 semaines.
- Baclofène oral, Liorésal® (FI, janvier 2025) [S14] : enfant dès 12 mois ; début 0,3 mg/kg/j en 4 prises, paliers de 1–2 semaines, entretien 0,75–2 mg/kg/j ; max 40 mg/j < 8 ans, 60 mg/j > 8 ans ; effets indésirables plus fréquents en spasticité d'origine cérébrale ; arrêt progressif sur ~3 semaines (sevrage : confusion, hallucinations, convulsions, hyperthermie, rebond) ; prudence si la spasticité sert la station debout ; insuffisance rénale.
- Baclofène intrathécal, Liorésal intrathécal® (FI, avril 2024) [S18] : test en bolus (enfant 25 µg) ; non-répondeur à 100 µg exclu ; spasticité cérébrale : augmentation de 5–20 % au plus ; entretien 22–1400 µg/j (moyenne 276 µg/j à 12 mois) ; < 12 ans : 24–1199 µg/j ; sécurité < 4 ans non démontrée ; arrêt brutal → tableau hypermétabolique, rhabdomyolyse [S14, S18]. En Europe, 3,4 % des enfants PC traités (surtout GMFCS IV–V, spastique bilatéral) ; accès variable selon le PIB [S19].
- Rhizotomie dorsale sélective : section de 50–75 % des fibres afférentes L1–S1, irréversible, membres inférieurs [S4].
- Chirurgie de hanche (GMFCS IV–V, Genève/Clermont-Ferrand) : ostéotomie pelvienne percutanée + ostéotomie fémorale de varisation : migration 66,8 % → 8,1 % [S20].
- Épilepsie pharmacorésistante : chirurgie, stimulation vagale, régime cétogène après échec de 2 antiépileptiques [S4].
- Cannabinoïdes : prescrits malgré l'absence de preuves (enquête Swiss-CP-Reg, 70 médecins) — épilepsie 69 %, spasticité 64 %, douleur 63 % ; somnolence fréquente ; ECR nécessaires [S21].

## 10. Suivi et situations particulières
- Surveillance des hanches par radiographie selon âge et GMFCS [S9, S16].
- Suivi des comorbidités (épilepsie, nutrition, parole, cognition) ; registre national Swiss-CP-Reg pour standardiser la prise en charge [S3].
- Prématurés suisses < 30 SA : suivi neurodéveloppemental au-delà de l'âge scolaire, surtout en milieu socio-économique défavorable [S11].

## 11. Critères formels (pour l'îlot final)
- Définition 2006 : trouble permanent du mouvement et de la posture + limitation d'activité + lésion non progressive du cerveau en développement [S2, S4].
- SCPE : type (spastique uni-/bilatéral, dyskinétique, ataxique) ; confirmation après 4–5 ans dans les registres [S4].
- Diagnostic précoce « à haut risque de PC » : IRM + GMA/HINE concordants avec l'anamnèse [S5].

## 12. Paramètres clés
- Prévalence ≈ 2/1000 naissances vivantes [S4] ; 146/1000 avant 28 SA [S4].
- GMFCS I–V ; Suisse : 59 % GMFCS I–II, 29 % IV–V [S3, S4].
- GMA 98 %, HINE 90 %, IRM 86–89 % de sensibilité [S5].
- MgSO4 < 34 SA : NNT 60 pour éviter une PC [S15].
- Hanche : migration > 40 % = déplacement ; 64 % en GMFCS V [S9].
- Dysport enfant MI : ≤ 30 U/kg ou 1000 U ; baclofène oral max 40/60 mg/j [S13, S14].

## Sous-codes couverts
G80.0, G80.1, G80.2, G80.3, G80.4, G80.8, G80.9 (définitions et type SCPE correspondant).

## Lacunes explicites
- Aucune recommandation suisse de société (SSNP/SGNP, SMF) lue : WebSearch épuisé ; seules sources suisses = Swiss-CP-Reg [S3], cohorte nationale prématurés [S11], enquête cannabinoïdes [S21], FI Swissmedic.
- Assurance-invalidité (infirmité congénitale, OIC) non lue.
- NICE NG62 inaccessible (403) : drapeaux rouges, gestion de la sialorrhée, densité osseuse non sourcés.
- Niveaux MACS, CFCS non lus ; texte intégral du rapport Rosenbaum 2007 non lu (résumé seulement).
- Protocole européen de surveillance des hanches (intervalles précis) non lu.
- Pas de FI lue pour diazépam, tizanidine, glycopyrronium, antiépileptiques spécifiques.
- Espérance de vie et transition à l'âge adulte non sourcées.
- Prévalence suisse populationnelle non disponible (Swiss-CP-Reg = registre non exhaustif).
