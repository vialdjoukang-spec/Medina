# Glossaire MEDINA — chapitre I47 Tachycardies paroxystiques supraventriculaires et ventriculaires
from cardio_1 import a, G

# ---- entités cliniques
a('TSV',[('T','Tachycardie'),('S','Supra-'),('V','Ventriculaire')],'Tachycardie supraventriculaire',
 '<p>Tachycardie dont le mécanisme requiert un tissu situé au-dessus de la bifurcation du faisceau de His : oreillettes, nœud auriculoventriculaire ou voie accessoire. Par convention, la fibrillation auriculaire est traitée à part (ESC 2019).</p>','i47-ecg-lecture')
a('TV',[('T','Tachycardie'),('V','Ventriculaire')],'Tachycardie ventriculaire',
 '<p>Tachycardie née sous la bifurcation du faisceau de His (myocarde ventriculaire ou réseau de Purkinje), d’au moins trois complexes à plus de 100/min. Soutenue si elle dure plus de 30 secondes ou impose une intervention.</p>','i47-cicatrice')
a('FV',[('F','Fibrillation'),('V','Ventriculaire')],'Fibrillation ventriculaire',
 '<p>Activité électrique ventriculaire anarchique, sans contraction efficace : arrêt circulatoire. Traitement : défibrillation non synchronisée immédiate.</p>','i47-cv')
a('TRIN',[('T','Tachycardie'),('R','par Réentrée'),('IN','IntraNodale')],'Tachycardie par réentrée intranodale',
 '<p>Réentrée entre la voie lente et la voie rapide du nœud auriculoventriculaire ; TSV régulière la plus fréquente de l’adulte. Guérie par l’ablation de la voie lente.</p>','i47-trin')
a('TRAV',[('T','Tachycardie'),('R','Réciproque'),('AV','AuriculoVentriculaire')],'Tachycardie réciproque auriculoventriculaire',
 '<p>Réentrée utilisant le nœud auriculoventriculaire et une voie accessoire ; orthodromique (QRS fins) ou antidromique (QRS larges pré-excités).</p>','i47-trav')
a('TVNS',[('T','Tachycardie'),('V','Ventriculaire'),('N','Non'),('S','Soutenue')],'Tachycardie ventriculaire non soutenue',
 '<p>Au moins trois complexes ventriculaires consécutifs à plus de 100/min, s’arrêtant spontanément avant 30 secondes.</p>','i47-tvns')
a('TVPC',[('T','Tachycardie'),('V','Ventriculaire'),('P','Polymorphe'),('C','Catécholergique')],'Tachycardie ventriculaire polymorphe catécholergique',
 '<p>Canalopathie de la manipulation du calcium (gènes <i>RYR2</i>, <i>CASQ2</i>) : TV bidirectionnelle ou polymorphe à l’effort ou à l’émotion, sur cœur et ECG de repos normaux.</p>','i47-tvpc')
a('EEP',[('E','Exploration'),('E','Électro-'),('P','Physiologique')],'Exploration électrophysiologique endocavitaire',
 '<p>Enregistrement des électrogrammes intracardiaques et stimulation programmée par des cathéters introduits par voie veineuse ; gold standard du diagnostic du mécanisme d’une tachycardie, préalable à l’ablation.</p>','i47-eep')
a('DAE',[('D','Défibrillateur'),('A','Automatisé'),('E','Externe')],'Défibrillateur automatisé externe',
 '<p>Appareil public qui analyse le rythme et délivre un choc en cas de FV ou de TV sans pouls, utilisable par un témoin sans formation médicale.</p>')
a('RP',[('R','onde R (début du QRS)'),('P','onde P qui suit')],'Intervalle RP en tachycardie',
 '<p>Temps entre le début du QRS et l’onde P qui le suit ; court (&lt; 70 ms) dans la TRIN typique, intermédiaire dans la TRAV orthodromique, long (RP &gt; PR) dans la tachycardie atriale.</p>','i47-ecg-rp')
a('AH',[('A','électrogramme Atrial (au niveau du faisceau de His)'),('H','potentiel du faisceau de His')],'Intervalle AH (exploration électrophysiologique)',
 '<p>Temps de conduction dans le nœud auriculoventriculaire, normal 50–120 ms ; un saut brutal signe une dualité nodale.</p>','i47-eep')
a('HV',[('H','potentiel du faisceau de His'),('V','premier signal Ventriculaire')],'Intervalle HV (exploration électrophysiologique)',
 '<p>Temps de conduction sous-hisienne, normal 35–55 ms ; court ou négatif en cas de pré-excitation.</p>','i47-eep')

# ---- courants et canaux
a('INa',[('I','courant (Intensité)'),('Na','sodique')],'Courant sodique rapide',
 '<p>Courant entrant de la phase 0 du potentiel d’action ventriculaire (canal Nav1.5, gène <i>SCN5A</i>) ; cible des antiarythmiques de classe I.</p>','i47-pa')
a('ICaL',[('I','courant (Intensité)'),('Ca','calcique'),('L','de type L (Long-lasting, durable)')],'Courant calcique de type L',
 '<p>Courant entrant du plateau (phase 2) et de la phase 0 des cellules nodales ; cible du vérapamil et du diltiazem.</p>','i47-pa')
a('IKr',[('I','courant (Intensité)'),('K','potassique'),('r','rapide')],'Courant potassique rectifiant retardé rapide',
 '<p>Courant de repolarisation (phase 3) porté par le canal hERG (gène <i>KCNH2</i>) ; bloqué par de nombreux médicaments allongeant le QT ; réduit dans le QT long de type 2.</p>','i47-herg')
a('IKs',[('I','courant (Intensité)'),('K','potassique'),('s','lent (slow)')],'Courant potassique rectifiant retardé lent',
 '<p>Courant de repolarisation renforcé par la stimulation adrénergique (gènes <i>KCNQ1</i> et <i>KCNE1</i>) ; réduit dans le QT long de type 1, d’où les événements à l’effort.</p>','i47-qtl')
a('IK1',[('I','courant (Intensité)'),('K','potassique'),('1','numéro d’ordre historique (courant potassique n° 1, rectifiant entrant)')],'Courant potassique rectifiant entrant',
 '<p>Courant qui maintient le potentiel de repos (phase 4) ; altéré dans le syndrome d’Andersen et Tawil (gène <i>KCNJ2</i>).</p>','i47-pa')
a('hERG',[('h','human (humain)'),('E','Ether-à-go-go (nom d’un mutant de drosophile)'),('R','Related (apparenté)'),('G','Gene (gène)')],'Canal hERG (gène KCNH2)',
 '<p>Canal potassique du courant IKr ; sa large cavité interne fixe de nombreux médicaments, d’où le QT long médicamenteux.</p>','i47-herg')

# ---- gènes
a('KCNH2',[('K','potassium (Kalium)'),('CN','Channel (canal)'),('H','sous-famille H (voltage-dépendante)'),('2','membre 2')],'Gène KCNH2 (canal hERG)',
 '<p>Code la sous-unité principale du canal du courant IKr ; perte de fonction : QT long de type 2 ; gain de fonction : QT court.</p>','i47-herg')
a('KCNE1',[('K','potassium (Kalium)'),('CN','Channel (canal)'),('E','sous-famille E (sous-unités régulatrices)'),('1','membre 1')],'Gène KCNE1',
 '<p>Code la sous-unité régulatrice du canal IKs ; ses variants bi-alléliques causent un syndrome de Jervell et Lange-Nielsen.</p>','i47-qtl')
a('KCNJ2',[('K','potassium (Kalium)'),('CN','Channel (canal)'),('J','sous-famille J (rectifiant entrant)'),('2','membre 2')],'Gène KCNJ2 (canal Kir2.1)',
 '<p>Code le canal du courant IK1 ; ses variants causent le syndrome d’Andersen et Tawil (arythmies ventriculaires, paralysies périodiques, dysmorphie).</p>')
a('CACNA1C',[('CACN','CAlcium CHaNnel (canal calcique voltage-dépendant ; symbole HGNC non strictement lettre à lettre)'),('A1','sous-unité Alpha 1'),('C','type C (Cav1.2)')],'Gène CACNA1C (canal calcique de type L)',
 '<p>Code le canal Cav1.2 ; un gain de fonction cause le syndrome de Timothy, avec QT très long.</p>')
a('RYR2',[('RY','RYanodine (alcaloïde végétal qui se fixe sur ce récepteur)'),('R','Récepteur'),('2','isoforme 2, cardiaque')],'Gène du récepteur de la ryanodine cardiaque',
 '<p>Canal de libération du calcium du réticulum sarcoplasmique ; ses variants à transmission dominante causent environ 60 % des TVPC.</p>','i47-tvpc')
a('CASQ2',[('CASQ','CalSeQuestrine (protéine de stockage du calcium)'),('2','isoforme 2, cardiaque')],'Gène de la calséquestrine cardiaque',
 '<p>Protéine tampon du calcium du réticulum sarcoplasmique ; ses variants à transmission récessive causent une forme de TVPC.</p>','i47-tvpc')

# ---- noms propres et bases
a('CredibleMeds',[('CredibleMeds','nom propre d’une base de données (« médicaments crédibles »), non une abréviation')],'Base CredibleMeds des médicaments allongeant le QT',
 '<p>Base en ligne (crediblemeds.org) classant les médicaments selon leur risque de torsades de pointes : risque connu, possible, conditionnel, et médicaments à éviter dans le QT long congénital.</p>','i47-credible')
a('Lange-Nielsen',[('Lange-Nielsen','nom du second auteur (Fred Lange-Nielsen, avec Anton Jervell, 1957), non une abréviation')],'Syndrome de Jervell et Lange-Nielsen',
 '<p>Forme récessive du QT long congénital (gènes <i>KCNQ1</i> ou <i>KCNE1</i>, deux allèles atteints) associée à une surdité congénitale ; risque rythmique élevé.</p>','i47-qtl')
a('ERC',[('E','European'),('R','Resuscitation'),('C','Council')],'European Resuscitation Council (Conseil européen de réanimation)',
 '<p>Société savante qui publie les recommandations européennes de réanimation, y compris la prise en charge des tachycardies péri-arrêt (versions 2021 et 2025).</p>','i47-cv')

# ---- essais
a('REVERT',[('REVERT','nom d’essai (« revenir » au rythme sinusal), issu de « Randomised Evaluation of modified Valsalva Effectiveness in Re-entrant Tachycardias », non strictement lettre à lettre')],'Essai REVERT (Lancet 2015)',
 '<p>Manœuvre de Valsalva modifiée (effort de 15 secondes puis décubitus avec jambes surélevées) contre manœuvre classique : 43 % contre 17 % de retour en rythme sinusal.</p>','i47-vagal')
a('AVID',[('A','Antiarrhythmics'),('V','Versus'),('I','Implantable'),('D','Defibrillators')],'Essai AVID (1997)',
 '<p>Prévention secondaire après FV ou TV grave : le DAI réduit la mortalité par rapport aux antiarythmiques (surtout l’amiodarone).</p>','i47-dai')
a('CIDS',[('C','Canadian'),('I','Implantable'),('D','Defibrillator'),('S','Study')],'Essai CIDS (2000)',
 '<p>Essai canadien de prévention secondaire comparant DAI et amiodarone ; tendance favorable au DAI.</p>','i47-dai')
a('CASH',[('C','Cardiac'),('A','Arrest'),('S','Study'),('H','Hamburg')],'Essai CASH (2000)',
 '<p>Essai de Hambourg chez des survivants d’arrêt cardiaque : DAI comparé à l’amiodarone et au métoprolol ; tendance favorable au DAI.</p>','i47-dai')
a('MADIT-II',[('M','Multicenter'),('A','Automatic'),('D','Defibrillator'),('I','Implantation'),('T','Trial'),('II','deuxième essai')],'Essai MADIT-II (2002)',
 '<p>Prévention primaire après infarctus avec FEVG ≤ 30 % : baisse de la mortalité totale sous DAI.</p>','i47-dai')
a('SCD-HeFT',[('SCD','Sudden Cardiac Death (mort subite cardiaque)'),('He','in Heart'),('F','Failure'),('T','Trial')],'Essai SCD-HeFT (2005)',
 '<p>Insuffisance cardiaque NYHA II–III avec FEVG ≤ 35 % : le DAI réduit la mortalité totale ; l’amiodarone ne fait pas mieux que le placebo.</p>','i47-dai')
a('VANISH',[('VANISH','nom d’essai (« faire disparaître ») issu de « Ventricular tachycardia Ablation versus escalated antiarrhythmic drug therapy in ISchemic Heart disease », non strictement lettre à lettre')],'Essai VANISH (2016)',
 '<p>TV sur cicatrice malgré un antiarythmique : l’ablation réduit le critère composite décès, orage rythmique ou chocs appropriés par rapport à l’escalade de l’amiodarone.</p>')

# ---- morphologies ECG
a('RS',[('R','onde R'),('S','onde S qui la suit')],'Complexe RS',
 '<p>QRS composé d’une onde R suivie d’une onde S. Son absence dans toutes les précordiales, pendant une tachycardie à QRS larges, signe une TV (étape 1 de l’algorithme de Brugada).</p>','i47-algo-brugada')
a('qR',[('q','petite onde q initiale'),('R','grande onde R')],'Complexe qR',
 '<p>QRS débutant par une petite onde négative suivie d’une grande onde positive ; en V1 pendant une tachycardie à QRS larges, il oriente vers une TV.</p>','i47-algo-brugada')
a('rsR′',[('r','petite onde r'),('s','onde s'),('R′','seconde onde R, plus grande')],'Complexe rsR′ (triphasique)',
 '<p>Aspect typique du bloc de branche droit en V1 ; pendant une tachycardie à QRS larges, il oriente vers une aberration plutôt qu’une TV.</p>','i47-aberr')
a('JT',[('J','point J (fin du QRS)'),('T','fin de l’onde T')],'Intervalle JT',
 '<p>Durée de la repolarisation seule ; utile pour évaluer la repolarisation quand le QRS est élargi (bloc de branche, stimulation).</p>','i47-ecg-qt')

# ---- canaux et mesures (audit passe 1)
a('If',[('I','courant (Intensité)'),('f','funny (« bizarre », activé par l’hyperpolarisation)')],'Courant If (pacemaker)',
 '<p>Courant entrant mixte sodium-potassium activé par l’hyperpolarisation (canaux HCN) ; il fait monter la phase 4 des cellules nodales ; cible de l’ivabradine.</p>','i47-pa')
a('Nav1.5',[('Na','sodium (Natrium)'),('v','voltage-dépendant'),('1.5','sous-famille 1, membre 5')],'Canal sodique cardiaque Nav1.5 (gène SCN5A)',
 '<p>Canal du courant sodique rapide de la phase 0 ; perte de fonction : Brugada, troubles de conduction ; gain du courant tardif : QT long de type 3.</p>','i47-pa')
a('Kir2.1',[('K','potassium (Kalium)'),('ir','inward rectifier (rectifiant entrant)'),('2.1','sous-famille 2, membre 1')],'Canal Kir2.1 (gène KCNJ2)',
 '<p>Canal du courant IK1 qui stabilise le potentiel de repos ; altéré dans le syndrome d’Andersen et Tawil.</p>','i47-pa')
a('Kir3.1',[('K','potassium (Kalium)'),('ir','inward rectifier (rectifiant entrant)'),('3.1','sous-famille 3, membre 1')],'Canal Kir3.1 (courant activé par l’acétylcholine et l’adénosine)',
 '<p>Associé à Kir3.4, il forme le canal potassique ouvert par les récepteurs muscariniques de type 2 et de l’adénosine de type 1 ; base du bloc nodal induit par l’adénosine et le vague.</p>','i47-adeno')
a('Kir3.4',[('K','potassium (Kalium)'),('ir','inward rectifier (rectifiant entrant)'),('3.4','sous-famille 3, membre 4')],'Canal Kir3.4',
 '<p>Sous-unité partenaire de Kir3.1 du courant potassique activé par l’acétylcholine et l’adénosine.</p>','i47-adeno')
a('Cav1.2',[('Ca','calcium'),('v','voltage-dépendant'),('1.2','sous-famille 1, membre 2')],'Canal calcique de type L Cav1.2 (gène CACNA1C)',
 '<p>Canal du courant calcique de type L du plateau et de la phase 0 nodale ; cible du vérapamil et du diltiazem.</p>','i47-pa')
a('Rs',[('R','grande onde R'),('s','petite onde s qui la suit')],'Complexe Rs',
 '<p>QRS dominé par une grande onde R suivie d’une petite onde s ; en V1, pendant une tachycardie à QRS larges à aspect de retard droit, il oriente vers une TV.</p>','i47-algo-brugada')
a('R/S',[('R','amplitude de l’onde R'),('/','rapport à'),('S','amplitude de l’onde S')],'Rapport R/S',
 '<p>Rapport des amplitudes de R et de S dans une dérivation ; en V6, un rapport inférieur à 1 pendant une tachycardie à retard droit oriente vers une TV.</p>','i47-algo-brugada')
a('vi/vt',[('vi','vitesse (amplitude parcourue) des 40 premières ms, initiale'),('vt','même mesure sur les 40 dernières ms, terminale')],'Rapport vi/vt (algorithme de Vereckei)',
 '<p>Compare la vitesse d’activation initiale et terminale du QRS en aVR ; un rapport ≤ 1 signe une TV.</p>','i47-algo-vereckei')
