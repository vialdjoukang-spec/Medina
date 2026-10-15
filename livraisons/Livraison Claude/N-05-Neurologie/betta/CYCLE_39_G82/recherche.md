# G82 — Paraparésie et paraplégie, tétraparésie et tétraplégie (N-05-Neurologie) — dossier de recherche

Cycle Betta 39, leçon 2 · agent C39-A4-NEUR (Opus 5.5) · 15.10.2026
Statut : recherche brute pour l'agent de rédaction. Audit différé — revue IA, distincte d'une validation médicale humaine.
Règle : chaque fait porte sa référence [Sx] (voir `sources.json`). Ce qui n'a pas été lu figure dans « Lacunes ». Aucune donnée de mémoire.
Note de méthode : le quota WebSearch de la session était épuisé ; recherche faite par PubMed (résumés et métadonnées), WebFetch d'URL connues (BfArM, PMC, uroweb), téléchargement des PDF EAU 2026 et `tools/swissmedic_fi.py`. Plusieurs lignes directrices (AO Spine) n'ont été lues qu'au niveau du résumé : la rédaction doit s'en tenir aux énoncés ci-dessous.

## 0. Question clinique
Un patient ne bouge plus les deux jambes (paraplégie) ou les quatre membres (tétraplégie). En aigu, il faut reconnaître une lésion médullaire, protéger la moelle (perfusion, décompression précoce) et dépister les complications vitales. En chronique, la lésion devient une maladie de toute la vie : vessie et intestin neurogènes, dysréflexie autonome, spasticité, escarres, risque cardiométabolique, espérance de vie réduite. Comment nommer, classer (ISNCSCI/AIS), coder (G82 vs S14/S24/S34) et suivre ces patients en Suisse ?

## 1. Définition et périmètre CIM-10-GM
- G82.- Paraparese und Paraplegie, Tetraparese und Tetraplegie, bloc G80–G83 [S1].
- Usage : paralysies par lésion médullaire ou affection cérébrale lorsqu'aucun autre code n'existe ; peut aussi servir en codage multiple pour signaler ces états quelle qu'en soit la cause [S1].
- Inclut paraplégie, quadriplégie, tétraplégie, forme chronique. Exclut la paralysie médullaire traumatique aiguë (S14.-, S24.-, S34.-) et la paralysie cérébrale infantile (G80.-) [S1].
- Code supplémentaire G82.6-! pour le niveau fonctionnel ; Z99.1 si dépendance (de longue durée) à la ventilation [S1].
- 5e caractère pour G82.0–G82.5 : 0 = aiguë complète non traumatique ; 1 = aiguë incomplète non traumatique ; 2 = chronique complète ; 3 = chronique incomplète ; 9 = non précisée (y compris d'origine cérébrale) [S1].
- Sous-catégories [S1] : G82.0- paraparésie/paraplégie flasque ; G82.1- spastique ; G82.2- non précisée (paralysie des deux jambes SAI) ; G82.3- tétraparésie/tétraplégie flasque ; G82.4- spastique ; G82.5- non précisée (quadriplégie SAI).
- G82.6-! niveau fonctionnel = segment médullaire le plus bas moteur intact : G82.60! C1–C3 ; G82.61! C4–C5 ; G82.62! C6–C8 ; G82.63! T1–T6 ; G82.64! T7–T10 ; G82.65! T11–L1 ; G82.66! L2–S1 ; G82.67! S2–S5 ; G82.69! non précisé [S1].
- Voisin : G83.4- syndrome de la queue de cheval (G83.40 complet, G83.41 incomplet, G83.49 SAI), avec code G95.8- pour la vessie neurogène [S1].
- Note didactique : la CIM-10-GM définit le « niveau fonctionnel » par le segment moteur intact le plus bas ; l'ISNCSCI définit le niveau neurologique (NLI) par sensibilité et motricité bilatérales (§3) [S1][S2]. À signaler à l'apprenant sans confondre les deux.

## 2. Classification clinique de référence : ISNCSCI 2019 [S2]
- Tétraplégie : atteinte motrice et/ou sensitive des segments cervicaux de la moelle par lésion d'éléments nerveux dans le canal ; exclut plexus brachial et nerfs périphériques.
- Paraplégie : atteinte des segments thoraciques, lombaires ou sacrés (pas cervicaux) ; fonction des membres supérieurs épargnée ; exclut plexus lombosacré et nerfs périphériques.
- Muscles clés (bilatéraux) : C5 fléchisseurs du coude ; C6 extenseurs du poignet ; C7 extenseurs du coude ; C8 fléchisseurs des doigts (majeur) ; T1 abducteur du 5e doigt ; L2 fléchisseurs de hanche ; L3 extenseurs du genou ; L4 releveurs du pied ; L5 extenseur long des orteils ; S1 fléchisseurs plantaires.
- Cotation motrice 0–5 (0 paralysie ; 1 contraction palpable/visible ; 2 mouvement sans pesanteur ; 3 contre pesanteur ; 4 contre résistance modérée ; 5 normal) ; NT non testable. Score moteur max. 50 membres supérieurs + 50 membres inférieurs.
- Sensibilité : tact léger et piqûre, 28 points clés par côté (C2 à S4–5), 0 absent / 1 altéré / 2 normal ; max. 56 par modalité et par côté.
- Niveau sensitif : dermatome le plus caudal normal (2) au tact et à la piqûre, tous ceux au-dessus normaux. Niveau moteur : muscle clé le plus bas ≥3, ceux au-dessus à 5. NLI : segment le plus caudal à sensibilité intacte et motricité antigravitaire des deux côtés ; c'est le plus rostral des quatre niveaux.
- Épargne sacrée : tact ou piqûre en S4–5, pression anale profonde (DAP) ou contraction anale volontaire (VAC). Lésion complète = aucune épargne sacrée.
- Grades AIS : A complet (rien en S4–5) ; B sensitif incomplet (sensibilité sacrée sans motricité, et pas de motricité > 3 niveaux sous le niveau moteur) ; C moteur incomplet, moins de la moitié des muscles clés sous le NLI ≥3 ; D moteur incomplet, au moins la moitié ≥3 ; E normal chez un patient ayant eu des déficits (sans lésion médullaire : pas de grade AIS).
- Zone de préservation partielle (ZPP) : utilisée si VAC absente (ZPP motrice) ou si DAP, tact et piqûre S4–5 absents (ZPP sensitive) ; segment le plus caudal avec fonction, pour 4 catégories [S2]. En 2019 étendue à certaines lésions incomplètes ; dans une cohorte EMSCI, ZPP motrices applicables dans 35,2 % des examens de lésions incomplètes, dans tous les AIS B [S3].
- Syndromes cliniques (qualitatifs, hors AIS) [S2] : centromédullaire (souvent hyperextension sur canal cervical spondylotique ; membres supérieurs plus faibles que les inférieurs) ; Brown-Séquard (déficit moteur et proprioceptif homolatéral, thermo-algique controlatéral ; forme pure rare) ; antérieur (perte motrice et thermo-algique, tact et position préservés) ; cône médullaire (vers L1–L2, signes centraux et périphériques mêlés, réflexes sacrés parfois conservés) ; queue de cheval (atteinte périphérique des racines : paralysie flasque, vessie et intestin aréflexiques).
- Lien codage : flasque (G82.0/G82.3) vs spastique (G82.1/G82.4) [S1] ; le syndrome de la queue de cheval se code G83.4 [S1].

## 3. Épidémiologie (Suisse d'abord)
- Incidence des lésions médullaires traumatiques en Suisse (données hospitalières OFS 2012–2013) : 19,9 à 49,7 par million d'habitants et par an selon les critères ; plus élevée chez l'homme, les âges élevés et la paraplégie ; 621 cas administratifs contre 213 dans SwiSCI → sous-couverture des centres spécialisés, surtout chez les âgés et les lésions moins sévères [S4].
- Cohorte SwiSCI : volet communautaire et cohorte d'incidence ; 174 publications ; thèmes : complications secondaires, santé mentale, recours aux soins, participation [S28].
- Profil des nouveaux cas en réadaptation suisse : âge médian 53,5 ans, 69,6 % d'hommes, 53,3 % de paraplégies, 53,7 % de lésions motrices incomplètes, séjour médian 5,2 mois [S5] ; autre échantillon : 77,7 % d'hommes, 73,7 % traumatiques, 59,8 % paraplégies, âge médian 51 ans [S6].
- Lésions non traumatiques : la myélopathie cervicale dégénérative est présentée comme la cause la plus fréquente de lésion médullaire non traumatique de l'adulte [S24] ; délai diagnostique long (adressage à 6,4 mois, IRM à 12,5 mois, avis chirurgical à 15,8 mois du début, cohorte britannique) [S23].
- Prévalence des lésions médullaires traumatiques dans les pays développés : 280 à 906 par million [S18].

## 4. Pronostic vital et morbidité à long terme (Suisse)
- Lésion traumatique : mortalité 2,32 fois celle de la population suisse (SMR 2,32 ; IC 95 % 2,10–2,56) ; tétraplégie associée à davantage de décès respiratoires, cardiovasculaires, infectieux et accidentels ; SMR élevés pour infections urinaires et septicémies [S7].
- Espérance de vie à 30 ans : 80,6 % (hommes) et 76,9 % (femmes) de celle de la population suisse ; paraplégie incomplète 45,1 années restantes contre 28,7 pour la tétraplégie complète [S8].
- Lésion non traumatique : mortalité 1,6 fois la population générale ; causes : cardiovasculaires 39,8 %, néoplasies 22 %, infections 9,9 % [S9] ; étiologie maligne HR 10 contre traumatique, infectieuse 2,6, vasculaire 2,5 [S10].
- Patients « perdus de vue » des centres : risque de décès ×3,62 (lésions traumatiques) [S32].
- Recours à l'aide à domicile professionnelle : 22 % (médiane 6 h/semaine), plus fréquent si indépendance fonctionnelle faible (SCIM) [S29]. Troubles du sommeil : 58,8 %, dont 69,4 % non traités [S30].
- Risque cardiométabolique : un tiers à haut risque à la sortie de réadaptation ; syndrome cardiométabolique ~40 % ; hypertension, diabète et obésité plus fréquents dans les lésions non traumatiques [S5][S34].
- Homme âgé avec lésion médullaire : risque de cancer de vessie multiplié par 16 à 28 ; passage fréquent aux sondes à demeure [S31].

## 5. Mécanismes (normal → pathologique)
- Lésion primaire puis secondaire : la décompression précoce vise à limiter la lésion secondaire du tissu nerveux (données précliniques) [S11].
- Perfusion : augmenter la PAM vise à améliorer la perfusion et l'oxygénation de la moelle lésée pour limiter la lésion ischémique secondaire [S12].
- Choc neurogène : perte brutale du tonus sympathique → vasodilatation, hypotension, bradycardie (lésions cervicales) [S35, étude observationnelle, niveau faible].
- Vessie selon le niveau [S18] : lésion spinale infrapontique–suprasacrée → hyperactivité détrusorienne et dyssynergie vésico-sphinctérienne, résidu post-mictionnel souvent augmenté ; lésion sacrée/infrasacrée → détrusor hypo- ou acontractile, résidu augmenté. Hyperactivité et dyssynergie jusqu'à 95 %, hypoactivité jusqu'à 83 % selon le niveau [S18]. Le danger principal est l'atteinte du haut appareil urinaire par pressions vésicales élevées [S18].
- Dysréflexie autonome (DA) [S18] : réponse autonome brutale et exagérée à un stimulus, en général si lésion à ou au-dessus de T6 ; définie par une hausse de la PAS > 20 mmHg par rapport à la valeur de base ; céphalée sévère, vision floue, anxiété, variation de fréquence cardiaque, sudation, piloérection, flush au-dessus de la lésion, pâleur et peau froide en dessous. Déclencheurs : vessie ou intestin distendus (y compris cystoscopie, urodynamique), sonde à demeure, ongle incarné infecté, escarre, stimulation sexuelle [S18].
- La DA a été observée dans 43,3 % des urodynamiques chez des lésés ≥ T6 ; la PAD monte > 10 mmHg dans 76,2 % des épisodes [S19, observationnel]. Complications graves rapportées : décès (2/18 cas), atteintes du SNC (83 %) ; déclencheurs vésicaux et intestinaux dans 89 % des cas [S33] ; cas d'hémorragies cérébrales récidivantes [S36, rapport de cas].
- Mécanisme neuronal : une architecture neuronale spinale se réorganise après la lésion et produit la DA ; une stimulation électrique épidurale ciblée l'a inversée chez la souris, le rat et l'humain (équipe CHUV/EPFL Lausanne) [S22]. Traiter l'hyperactivité détrusorienne (fésotérodine, toxine botulique) réduit la fréquence et la sévérité de la DA [S20].
- Spasticité : le tonus résiduel et des spasmes occasionnels peuvent soutenir la posture, la circulation et la prévention de la thrombose ; trop réduire la spasticité expose aux chutes [S25].

## 6. Causes (à rattacher au codage)
- Traumatiques aiguës → S14/S24/S34 ; G82 en code chronique ou supplémentaire [S1][S4].
- Non traumatiques : dégénératives (myélopathie cervicale) [S24][S23], malignes, infectieuses, vasculaires (groupes étiologiques SwiSCI) [S10] ; spina bifida (dysraphisme) chez l'enfant [S37].
- Origine cérébrale : 5e caractère 9 [S1].

## 7. Anamnèse et examen
- Examen standardisé ISNCSCI complet, y compris toucher rectal (DAP, VAC) — sans lui, pas de classement complet/incomplet [S2].
- Anamnèse neuro-urologique et digestive : programme intestinal, incontinence, sensation rectale ; spasticité ou DA (surtout ≥ T6) ; mobilité et fonction de la main [S18].
- Calendrier mictionnel sur 2–3 jours ; débitmétrie et résidu échographique répétés 2–3 fois chez ceux qui urinent [S18].

## 8. Examens complémentaires
- IRM : suggérée avant chirurgie lorsque faisable (décision) et à la phase aiguë pour le pronostic neurologique (recommandations faibles, preuves très faibles/faibles) [S16].
- Neuro-urologie [S18] : analyse d'urine, chimie sanguine, calendrier, résidu, quantification de l'incontinence, imagerie urinaire au bilan initial ; urodynamique invasive obligatoire pour typer la dysfonction, de préférence vidéo-urodynamique, remplissage physiologique au sérum tiède ; surveiller pression artérielle et fréquence cardiaque pendant les gestes invasifs si risque de DA. Chez la personne peu musclée, le DFG fondé sur la cystatine C semble plus exact que la créatinine [S18].

## 9. Diagnostic différentiel
- Lésion médullaire vs atteinte du plexus ou des nerfs périphériques (exclues de la définition ISNCSCI) [S2].
- Queue de cheval (G83.4) vs cône médullaire vs lésion médullaire haute [S1][S2].
- Paralysie cérébrale infantile (G80, exclue) [S1].
- Lacune : myélite transverse, infarctus médullaire, SEP, Guillain-Barré, compression métastatique — non documentés par une source lue (voir Lacunes).

## 10. Urgences
- Lésion médullaire aiguë traumatique (lignes directrices AO Spine/Praxis, GRADE) :
  - Chirurgie de décompression ≤ 24 h recommandée comme option préférée chez l'adulte quel que soit le niveau ; récupération ≥ 2 grades AIS à 6 mois RR 2,76 (IC 1,60–4,98) ; +4,50 points de score moteur ; pas de recommandation pour l'ultra-précoce (< 12 h) [S11].
  - Syndrome centromédullaire traumatique : chirurgie précoce à envisager (faible) [S38].
  - PAM : augmenter à au moins 75–80 mmHg (borne basse), ne pas augmenter activement au-delà de 90–95 mmHg, pendant 3 à 7 jours (recommandations faibles, preuves très faibles) ; pas de recommandation sur le choix du vasopresseur [S12][S13]. L'effet de la PAM sur la récupération reste incertain [S39].
  - Méthylprednisolone (MPSS) : 24 h à haute dose proposée comme option si < 8 h ; ne pas la proposer après 8 h ; pas de schéma de 48 h (recommandations faibles) [S14].
  - Thromboprophylaxie : anticoagulante en routine, HBPM SC ou HNF à dose fixe faible ; éviter HNF à dose ajustée ; débuter dans les 72 h si possible [S15].
- Dysréflexie autonome : urgence potentiellement vitale [S18][S33]. Sources lues : définition, déclencheurs, prévention urologique. Conduite médicamenteuse précise : lacune (aucune source européenne lue).
- Sevrage de baclofène intrathécal (panne de pompe, déconnexion du cathéter) : spasticité accrue, prurit, paresthésies, hypotension, puis hyperthermie, tachycardie, rigidité, convulsions, rhabdomyolyse, défaillance multiviscérale, décès possible ; baclofène oral/entéral ou benzodiazépines peuvent prévenir des complications mortelles sans garantie [S26].

## 11. Prise en charge (Suisse / Europe)
### Réadaptation
- Réadaptation dès que le patient est stable et tolère l'intensité ; entraînement sur tapis avec allègement du poids possible en complément ; stimulation électrique fonctionnelle pour la main dans les lésions cervicales aiguës/subaiguës ; pas d'entraînement supplémentaire en position assise sans appui (recommandations faibles) [S17].
- Réadaptation en centres spécialisés suisses (SwiSCI couvre tous les centres spécialisés) [S8][S4].
### Neuro-urologie (EAU 2026) [S18]
- Priorités : 1 protéger le haut appareil ; 2 continence ; 3 restaurer la fonction ; 4 qualité de vie.
- Éviter le Credé et la poussée abdominale (pressions élevées) ; miction réflexe déclenchée déconseillée.
- Antimuscariniques (ou bêta-3) pour la vessie neurogène hyperactive ; ne pas compter sur les bêta-3 pour réduire l'hyperactivité urodynamique ; alpha-bloquants pour baisser la résistance de sortie ; pas de parasympathomimétiques pour un détrusor hypoactif ; natrémie sous desmopressine.
- Auto-sondage intermittent : décision partagée, instruction approfondie ; oxybutynine intravésicale si intolérance orale ; toxine botulique A intra-détrusorienne si antimuscarinique inefficace ; entérocystoplastie si faible compliance ou hyperactivité réfractaire ; neuromodulation sacrée chez des patients choisis.
- Infections urinaires : pas de bandelette pour dépister ; ne pas dépister ni traiter la bactériurie asymptomatique ; en cas de récidives, optimiser la vessie et retirer les corps étrangers ; antibioprophylaxie cyclique hebdomadaire chez certains lésés médullaires en auto-sondage ; éviter l'antibiothérapie continue.
- Sexualité/fertilité : IPDE-5 en 1re ligne de la dysfonction érectile, injections intracaverneuses en 2e ; vibrostimulation et électro-éjaculation pour le recueil de sperme ; informer les hommes ≥ T6 et les centres de fertilité du risque de DA.
- Guide allemand (AWMF, mise à jour 3.0, 2026) consacré à l'auto-sondage intermittent, y compris la gestion des infections et de la DA [S21] (résumé lu seulement).
### Spasticité (FI Swissmedic)
- Liorésal® (baclofène oral) : indiqué aussi dans la spasticité médullaire d'origine infectieuse, dégénérative, traumatique ou néoplasique ; adulte : 3 × 5 mg/j, +5 mg par prise tous les 3 jours, dose habituelle 30–80 mg/j, 100–120 mg/j sous surveillance hospitalière ; arrêt progressif sur ~3 semaines (risque de confusion, hallucinations, convulsions, hyperthermie, rebond) ; réévaluer si aucun effet 6–8 semaines après la dose maximale ; insuffisance rénale : débuter ~5 mg/j, risque d'encéphalopathie toxique ; prudence en cas d'hypertonie sphinctérienne (rétention aiguë possible) [S25].
- Liorésal intrathécal® : spasticité chronique grave d'origine médullaire ou cérébrale ne répondant pas aux antispastiques oraux ou mal tolérés ; risque de granulome au bout du cathéter [S26].
### Vessie (FI Swissmedic)
- Oxybutynine (Oxybutynin Macure) : hyperactivité vésicale neurogène (hyperactivité du détrusor) ; adulte 2,5 mg 3×/j au départ, 10–15 mg/j, max. 20 mg/j ; contre-indications : glaucome à angle étroit, myasthénie, obstruction ou atonie digestive [S27].

## 12. Suivi
- Haut appareil urinaire chez les patients à haut risque : échographie environ tous les 6 mois ; examen clinique et analyses d'urine chaque année ; urodynamique de référence puis répétée ; intervalle de contrôle en général ≤ 1–2 ans, plus court si haut risque ; programme individualisé ; tout changement clinique impose des examens spécialisés [S18].
- Risque cardiométabolique à dépister dès la réadaptation [S5][S34].
- Maintenir le lien avec les centres spécialisés (mortalité accrue des perdus de vue) [S32].
- Dépister les troubles du sommeil [S30].

## 13. Situations particulières
- Personne âgée : sous-représentée dans les centres spécialisés [S4] ; hommes âgés : hypertrophie prostatique, cancer de vessie, risque de DA lors des gestes prostatiques [S31].
- Enfants et adolescents avec dysraphisme spinal : prise en charge multidisciplinaire, urodynamique centrale (guide EAU/ESPU/ERN 2025) [S37].
- Fertilité et grossesse chez la femme : approche multidisciplinaire [S18].
- Lésion non traumatique : profil cardiométabolique plus lourd, mortalité selon l'étiologie [S34][S10].

## 14. Critères formels (pour l'îlot `div.alert`)
- Tétraplégie vs paraplégie selon le segment médullaire atteint (cervical vs thoracique/lombaire/sacré), lésion dans le canal [S2].
- Complet = aucune fonction sensitive ni motrice en S4–5 (tact, piqûre, DAP, VAC) [S2].
- AIS A–E selon §2 [S2].
- DA : PAS > 20 mmHg au-dessus de la base, lésion en général ≥ T6 [S18].
- Codage : G82.x + 5e caractère (aigu/chronique, complet/incomplet) + G82.6-! niveau ; S14/S24/S34 pour la lésion traumatique aiguë [S1].

## 15. Paramètres clés (pour `div.key`)
- Muscles clés C5–T1, L2–S1 ; score moteur 50 + 50 ; sensitif 28 points × 2 modalités × 2 côtés [S2].
- PAM 75–80 à 90–95 mmHg pendant 3–7 jours ; décompression ≤ 24 h ; MPSS seulement < 8 h et 24 h ; thromboprophylaxie ≤ 72 h [S11][S12][S14][S15].
- Incidence suisse 19,9–49,7/million/an ; SMR traumatique 2,32 ; non traumatique 1,6 [S4][S7][S9].
- Échographie rénale ~6 mois si haut risque ; urodynamique en référence et en suivi [S18].
- Baclofène oral 30–80 mg/j ; oxybutynine max. 20 mg/j [S25][S27].

## Sous-codes couverts
G82.0- à G82.5- avec 5e caractères 0, 1, 2, 3, 9 ; G82.60! à G82.69! (toutes les sous-catégories CIM-10-GM 2024 de G82) ; voisins G83.4- et G80 pour le différentiel ; renvoi S14/S24/S34.

## Lacunes explicites
1. Aucune source suisse de type recommandation (Société suisse de paraplégie, SPZ Nottwil, Balgrist, Swiss Medical Forum) n'a pu être lue : quota WebSearch épuisé, page SwiSCI de paraplegie.ch en 404.
2. Lignes directrices AO Spine/Praxis lues au niveau des résumés PubMed (plein texte non lu) ; elles sont internationales (fondation AO Spine, Davos) avec auteurs nord-américains majoritaires ; ce ne sont pas des recommandations européennes. Le résumé de 2024 mentionne qu'elles actualisent des recommandations AANS/CNS de 2013, qui n'ont pas été lues ni utilisées.
3. Conduite médicamenteuse de la dysréflexie autonome (seuils, antihypertenseurs, doses) : aucune source européenne lue → ne rien rédiger au-delà de la définition, des déclencheurs et de la prévention.
4. Choc neurogène et choc spinal : seule une étude observationnelle thaïlandaise lue (définition) ; pas de seuils ni de traitement documentés.
5. Prévention et traitement des escarres, programme intestinal, ostéoporose sous-lésionnelle, douleur neuropathique, ossifications hétérotopiques, fonction respiratoire des tétraplégiques : non documentés.
6. Différentiel non traumatique (myélite transverse, infarctus médullaire, compression métastatique — guide ESMO non trouvé —, SEP, Guillain-Barré, paraplégie spastique héréditaire) : non documenté.
7. FI Swissmedic de HBPM (Fragmin® repérée, non lue), tizanidine, toxine botulique non relues ici (voir dossier G81 pour Botox®/tizanidine).
8. Scores fonctionnels (SCIM III) cités dans SwiSCI mais sans description lue.
