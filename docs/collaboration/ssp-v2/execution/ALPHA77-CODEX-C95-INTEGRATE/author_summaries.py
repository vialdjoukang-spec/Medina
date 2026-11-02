"""Quatorze synthèses reliées à leurs sections, sans remplacer le raisonnement."""
from common import POP,SECTIONS,refs
PARETO=[
('definition','Définition, classification et épidémiologie','c95-1,c95-2',[
'C95 décrit une catégorie de code ; absence de résultat et ambiguïté biologique démontrée ne sont pas synonymes.',
'LALA : LAPM, LAI et formes sans autre précision ; seuil de20 % propre à ce contexte, pas à toute leucémie aiguë.',
'OMS et ICC diffèrent ; intensité relative, pourcentage cellulaire et composante mineure ne sont pas la même mesure.',
'Les chiffres suisses1 150diagnostics/600décès annuels portent sur C91–C95 en2013–2017, pas sur la LAPM.'],['WHO','FLOW','CIM','OFS-CANCER']),
('mecanismes','Mécanismes et facteurs de risque','c95-3,c95-4',[
'Une production blastique peut compromettre les trois fonctions normales : transport d’oxygène, défense et hémostase.',
'Deux populations phénotypiques peuvent appartenir au même clone ; plasticité et évolution sont possibles.',
'Caryotype anormal ne signifie pas complexe ; mutation somatique ne signifie pas prédisposition familiale.',
'Un facteur de risque oriente l’enquête sans prouver une causalité individuelle ni un droit assurantiel.'],['NORMAL','ALAL','KARASEK','AML']),
('clinique','Anamnèse et examen','c95-5,c95-6',[
'Fatigue, fièvre et saignement évoquent une insuffisance médullaire sans identifier une lignée.',
'Préciser tolérance, chronologie, traitements et symptômes respiratoires/neurologiques.',
'Examiner stabilité, peau/muqueuses, ganglions, organes et système nerveux ; répéter selon évolution.',
'L’absence de foyer, d’adénopathie ou d’hyperleucocytose n’exclut pas une maladie grave.'],['AML','ALL','RMS-NF']),
('diagnostic','Diagnostic intégré et imitations','c95-7,c95-8',[
'Morphologie + cytométrie + génétique + contexte ; le rapport nomme classification et limites.',
'CD19 fort + combinaison B, CD3 spécifique, MPO/profil monocytaire : critères définissants, pas simple addition de positivités.',
'MPO faible isolée, CD13/CD33 ou CD7 ne créent pas automatiquement une LAPM.',
'Écarter catégories LMA, LMC blastique, précurseurs normaux et autres différenciations avant de conclure.'],['WHO','FLOW','ALAL']),
('traitement','Urgences, induction et greffe','c95-9,c95-10',[
'Stabiliser et caractériser en parallèle ; leucostase possible sous100G/L, LAP suspectée avec ATRA immédiat au centre.',
'L’induction de type LLA est favorisée pour beaucoup de LAPM par des données surtout rétrospectives ; pas règle unique pour toute LAI.',
'BCR::ABL1 peut justifier un ITK, après vérification du contexte, de l’indication et des risques.',
'Allogreffe en RC1 discutée chez l’adulte éligible ; pas bénéfice global pédiatrique démontré dans iBFM.'],['AML','APL','ALAL','IBFM','EBMT17','EBMT26']),
('suivi','Réponse, pronostic et parcours suisse','c95-11,c95-12,c95-13,c95-14',[
'RC morphologique, MRD négative et guérison sont distinctes ; cible, sensibilité et calendrier doivent être connus.',
'Un changement de lignée peut rendre un suivi trop centré sur CD19 insuffisant.',
'Survie de registre, cohorte pédiatrique et cohorte de greffe sélectionnée ne se comparent pas directement.',
'Autorisation, preuve clinique et remboursement sont trois vérifications ; aucun prix ni accès garanti ici.'],['ALL','ALAL','IBFM','EBMT17','EBMT26','OFSP','OAMAL']),
('examens','Examens complémentaires','c95-e-1,c95-e-2,c95-e-3,c95-e-4,c95-e-5',[
'Prescrire un examen pour une question ; préserver les prélèvements utiles sans retarder l’urgence.',
'Unité, dénominateur, méthode et finalité accompagnent chaque seuil.',
'0,01 %=10⁻⁴ ;50 % d’intensité ne signifie pas50 % de cellules.',
'Sous rasburicase : tube hépariné prérefroidi, glace, centrifugation4°C, dosage dans4heures.'],['WHO','FLOW','ALL','FASTURTEC']),
('semio','Sémiologie fondamentale','c95-s-semio-cours',[
'Fonction normale → perturbation → signe → examen → décision ; expliciter chaque lien.',
'Nombre leucocytaire total et défense efficace peuvent évoluer en sens opposé.',
'Un signe physique ne suffit pas à attribuer une lignée ou à exclure la maladie.',
'La gravité impose parfois une action avant le nom biologique définitif.'],['NORMAL','AML','ALL','RMS-NF']),
('anat','Anatomie','c95-s-anat-cours',[
'La moelle est le compartiment de production ; le sang n’en restitue pas tout le contenu.',
'Aspiration et biopsie donnent des informations complémentaires.',
'Le site d’infiltration et la sécurité procédurale guident les explorations.',
'La photo originale situe la moelle, sans mesurer les blastes ni fournir une échelle déduite.'],['NORMAL','NORMAL-IMAGE','AML','ALL']),
('histo','Histologie et cytométrie','c95-s-histo-cours',[
'Marqueur d’immaturité, marqueur associé et marqueur définissant sont différents.',
'Contrôles normaux et profil coordonné comptent autant que la simple présence d’un signal.',
'Deux populations aberrantes ne sont pas nécessairement deux clones ; hématogones normales à exclure.',
'LAI demande un panel étendu ; MPO négative ou TdT négative isolée ne tranche pas seule.'],['WHO','FLOW','ALAL']),
('physio','Physiologie','c95-s-physio-cours',[
'La moelle produit des cellules dont la maturation conditionne la fonction.',
'Saturation en oxygène et quantité d’hémoglobine ne sont pas identiques.',
'Plaquettes et fibrine jouent des rôles complémentaires dans l’hémostase.',
'Le traitement causal peut d’abord aggraver les cytopénies : soutien et mesure de réponse restent indispensables.'],['NORMAL-RBC','NORMAL-WBC','NORMAL-HEMO','AML']),
('bio','Biochimie','c95-s-bio-cours',[
'La MPO est un signal de différenciation à interpréter ; elle ne mesure pas la défense fonctionnelle du blaste.',
'La lyse libère plusieurs composants ; une baisse d’urate ne corrige pas potassium et phosphate.',
'Rasburicase produit du peroxyde : G6PD et risque oxydatif expliquent une contre-indication.',
'Dose, concentration, surface corporelle et proportion doivent garder leurs unités.'],['WHO','FLOW','FASTURTEC','AML']),
('gen','Génétique','c95-s-gen-cours',[
'Somatique, constitutionnel et clonal sont trois notions différentes.',
'Caryotype, FISH et méthodes moléculaires ont des couvertures distinctes.',
'BCR::ABL1, KMT2A, ZNF384 et BCL11B éclairent la biologie sans abolir le contexte.',
'Une cible peut aider au suivi ou au traitement, après vérification de sa pertinence et de la preuve.'],['WHO','ALAL','KARASEK','FLOW']),
('pharma','Pharmacologie','c95-p-1,c95-p-2,c95-p-3,c95-p-4,c95-p-5',[
'Distinguer dose de fiche LLA/LMC/LMA et protocole LAPM ; ne pas fusionner les indications.',
'Ponatinib45→15mg à réponse≤1 % : règle LMC chronique, pas automatiquement LLA.',
'Litalir août2026 : indication chronique, dose initiale40–50mg/kg/j ; cytoréduction aiguë de portée distincte.',
'Rasburicase : G6PD, préanalytique, autres paramètres ; ATRA seulement filière LAP suspectée.',
'Blinatumomab et vénétoclax : preuve LAPM limitée, toxicités et interactions spécifiques.'],['GLIVEC','ICLUSIG','LITALIR','FASTURTEC','VESANOID','BLINCYTO','VENCLYXTO'])]
for slug,title,cover,points,sources in PARETO:
 POP['pareto-c95-'+slug]=('Pareto — '+title,f'<p class="ratio" data-cover="{cover}"></p><ul>'+''.join('<li>'+x+'</li>' for x in points)+'</ul>'+refs(*sources))
for end,slug in [('2','definition'),('4','mecanismes'),('6','clinique'),('8','diagnostic'),('10','traitement'),('14','suivi'),('e-5','examens'),('p-5','pharma')]:
 SECTIONS[end]=SECTIONS[end].removesuffix('</section>')+f'<button class="pareto-btn ui" data-k="pareto-c95-{slug}">▲ Loi de Pareto — synthèse</button></section>'
