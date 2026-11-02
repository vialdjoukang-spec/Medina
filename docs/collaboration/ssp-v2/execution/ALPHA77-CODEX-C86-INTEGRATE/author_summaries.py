from author_popups import add,table,lab
PARETO=[
('definition','Définition, classifications et épidémiologie','c86-1,c86-2',[
'C86 comporte sept sous-codes et plusieurs entités ; C86.4 inclut une néoplasie dendritique, C86.6 LyP et pcALCL.',
'OMS/ICC décrivent la biologie ; le codage CIM historique ne remplace pas le diagnostic.',
'La proportion suisse de 10–15 % provient d’une revue 2021 citant NICER ; pas d’incidence suisse actuelle par sous-code établie ici.',
'Les risques thiopurine cités concernent les hommes <35 ans, sans horizon annuel précisé.'],['CIM','OMS-DC','SZO','CARVAO']),
('mecanismes','Physiopathologie et facteurs de risque','c86-3,c86-4',[
'ENKTL : EBV tissulaire, destruction locale et résistance aux anthracyclines ; asparaginase selon protocole.',
'HAVCR2/TIM-3 peut contribuer au SPTCL/HLH dans certaines populations ; fréquence et risque ne sont pas universels.',
'TET2/DNMT3A puis RHOA/IDH2 organisent un modèle TFH, sans imposer un traitement depuis une mutation seule.',
'Un facteur de risque oriente une recherche ; il ne prouve pas une causalité individuelle ni un arrêt médicamenteux automatique.'],['TSE','MOONLA','OMS22','CARVAO']),
('clinique','Anamnèse et examen','c86-5,c86-6',[
'Relier siège, chronologie et gravité : nez, rate–foie–moelle, intestin, hypoderme, peau ou ganglion.',
'L’absence de ganglion n’exclut pas HSTL ; la régression répétée des papules oriente vers LyP.',
'Documenter lésions, cytopénies, fièvre et traitements ; choisir un tissu représentatif.',
'Un signe clinique ou un marqueur isolé ne remplace pas la confrontation spécialisée.'],['TSE','CARVAO','KEMPF','ESsCD26']),
('diagnostic','Diagnostic et urgences','c86-7,c86-8',[
'Prélèvement adapté et relecture experte ; panel et morphologie intégrés, clonalité seule insuffisante.',
'Bilan systémique différent de celui d’une LyP typique ; moelle et TEP ne sont pas automatiques pour tout C86.',
'HLH : fonctions vitales, déclencheur et immunomodulation en parallèle si gravité ; ne pas attendre un signe unique.',
'Obstruction respiratoire, complication digestive et toxicités graves exigent une réponse urgente.'],['ESMO25','CUT18','HLH23','TSE']),
('prise-en-charge','Traitement, suivi et prévention','c86-9,c86-10',[
'ENKTL : pas de CHOP ; radiothérapie et asparaginase selon stade/aptitude, radiothérapie seule possible dans certaines situations localisées.',
'HSTL : induction et greffe précoce, préférentiellement allogénique ; EATL : autogreffe possible, sans donneur.',
'SPTCL sans HLH : immunosuppression possible ; LyP : contrôle des lésions et suivi à vie, pas de polychimiothérapie.',
'L’arrêt du suivi PTCL à 3/5 ans ne concerne que les asymptomatiques restant en rémission complète ; pas toute la famille.'],['ESMO25','CUT18','S2K','KEMPF']),
('criteres','Critères et situations particulières','c86-11,c86-12',[
'Les panels ENKTL, TFH et BPDCN s’interprètent avec le tissu ; deux marqueurs ne font pas tout le diagnostic.',
'RCD-II : symptômes/atrophie après ≥12 mois de régime strict, autres causes exclues, cytométrie et clonalité adaptées.',
'Albumine Elzonris : ≥3,2 g/dL avant première dose ; seuils d’action sous traitement distincts.',
'PROFILES 2017/265 SSP est le cadre de l’examen 2026 ; PROFILES 2 devient celui de l’examen 2028.'],['OMS22','OMS-DC','ESsCD26','ELZONRIS','MEBEKO26','PROFILES-TRANS']),
('examens','Examens','c86-e-1,c86-e-2,c86-e-3,c86-e-4,c86-e-5',[
'Séparer référence de laboratoire, seuil diagnostique et seuil d’action thérapeutique.',
'EBER tissulaire et ADN d’EBV plasmatique répondent à deux questions complémentaires.',
'CD30 ≥75 % pour le critère pcALCL et ≥10 % à l’inclusion d’ECHELON-2 ne sont pas interchangeables.',
'Une TEP négative ne remplace pas les prélèvements indiqués ; une capsule ne biopsie pas et peut être retenue.'],['HUG','TSE','KEMPF','ESMO25','ESGE22']),
('semio','Sémiologie fondamentale','c86-s-semio-cours',[
'Fonction normale → perturbation → signe → examen → interprétation : expliciter chaque étape.',
'Ulcération, cytopénie et papule régressive ont des mécanismes et des diagnostics alternatifs.',
'Le seuil biologique ne prend sens qu’avec son unité, sa population et sa finalité.',
'La gravité peut imposer une prise en charge avant le résultat complet.'],['ESMO25','HLH23','TSE','HUG']),
('anat','Anatomie','c86-s-anat-cours',[
'Les organes lymphoïdes organisent le contact entre cellules et antigènes ; sang et lymphe ne sont pas le même compartiment.',
'Le territoire atteint guide un prélèvement suffisamment profond et représentatif.',
'Les figures originales illustrent des sites et des architectures ; elles ne sont pas un test diagnostique.'],['NORMAL-A','TSE','OMS22']),
('histo','Histologie','c86-s-histo-cours',[
'Architecture, morphologie, phénotype et contexte sont complémentaires.',
'Une tumeur T peut perdre des marqueurs ; un clone réactif peut être détecté.',
'TFH, pDC, NK et T alpha-bêta/gamma-delta ne se définissent pas par un seul marqueur.',
'Un petit prélèvement peut permettre une catégorie sans autoriser un sous-type architectural précis.'],['ESMO25','OMS22','OMS-DC']),
('physio','Physiologie','c86-s-physio-cours',[
'Expansion clonale, coopération, cytotoxicité et régulation sont des fonctions normales.',
'L’hyperinflammation et les anomalies du microenvironnement expliquent des signes au-delà de la seule masse tumorale.',
'Un Coombs positif ne prouve pas seul une hémolyse ; une hypergammaglobulinémie polyclonale n’est pas un myélome.'],['NORMAL-T','OMS22','HLH23','HUG']),
('bio','Biochimie','c86-s-bio-cours',[
'Déplétion extracellulaire en asparagine et capacité de synthèse limitée expliquent une vulnérabilité tumorale.',
'Dose administrée, activité enzymatique et réponse ne sont pas identiques.',
'LDH, ferritine et albumine sont des marqueurs contextuels, non spécifiques.',
'Convertir correctement : 3,2 g/dL =32 g/L ; µg et mg diffèrent d’un facteur 1 000.'],['TSE','ONCASPAR','ELZONRIS','HLH23']),
('gen','Génétique','c86-s-gen-cours',[
'Constitutionnel, somatique et clonal décrivent trois notions différentes.',
'HAVCR2 est associé au HLH dans certaines cohortes ; un odds ratio n’est pas un risque absolu.',
'Les mutations TFH et DUSP22 doivent rester attachées à leur tissu et leur entité.',
'Une cible biologique ne constitue pas à elle seule une indication thérapeutique.'],['OMS22','MOONLA','WHO-CUT','ESMO25']),
('pharma','Pharmacologie','c86-p-1,c86-p-2,c86-p-3,c86-p-4',[
'Distinguer mécanisme, preuve par sous-type, autorisation suisse et remboursement.',
'Adcetris : bléomycine contre-indiquée ; pas de vincristine dans BV-CHP ; adaptations selon schéma.',
'Elzonris : premier cycle hospitalier, surveillance avant doses et algorithme de fuite capillaire.',
'Oncaspar : FI LLA ; emploi ENKTL hors indication et dose de protocole distincte.'],['ADCETRIS','ELZONRIS','ONCASPAR','OFSP','OAMAL'])]
for slug,title,cover,points,sources in PARETO:
 add('pareto-c86-'+slug,'Pareto — '+title,f'<p class="ratio" data-cover="{cover}"></p><ul>'+''.join('<li>'+x+'</li>' for x in points)+'</ul>',*sources)
add('c86-mnemo','Sous-code et siège : une aide, pas une définition',lab('Aide pédagogique',table(['Sous-code','Siège souvent évocateur','Entité'],[['0','Nez et autres territoires extranodaux','ENKTL'],['1','Foie, rate et moelle','HSTL'],['2','Intestin grêle','EATL'],['3','Hypoderme','SPTCL'],['4','Peau, sang/moelle et autres sites','BPDCN'],['5','Ganglion et manifestations systémiques','nTFHL-AI'],['6','Peau','LyP et pcALCL']]))+'<p>Ce repère créé pour apprendre ne remplace ni la classification ni le bilan d’extension. Une localisation inhabituelle n’exclut pas l’entité.</p>','CIM','ESMO25','OMS-DC')
add('c86-profils','PROFILES suisse : version et passage de la plainte à la démarche',
lab('Cadre 2026','<p>Les exigences MEBEKO pour l’examen fédéral 2026 renvoient à 265 situations PROFILES. La publication Swiss Medical Weekly 2025 annonce PROFILES 2 pour l’enseignement dès 2025/26 et pour l’examen fédéral dès 2028. Ne pas fusionner les numérotations.</p>')+
lab('SSP 2 : adénopathie, PROFILES 2017','<p>Une personne consulte pour un ganglion augmenté. L’objectif est d’évaluer durée, localisation, signes généraux, exposition, gravité et indications de prélèvement. C86 fournit une partie du diagnostic différentiel, pas une liste officielle de maladies attachées à cette SSP. Un ganglion absent n’exclut pas un lymphome extranodal tel HSTL.</p>')+
lab('Autres entrées lues','<p>SSP 4 fatigue ; 6 fièvre ; 16 perte de poids/dénutrition ; 21 épistaxis ; 25 lésions de la bouche/gorge ; 88 ecchymoses/purpura ; 93 papules, ulcères, nécrose et tumeurs cutanées ; 159 histologie, cytologie et génétique moléculaire anormales ; 227 évaluation partagée des risques et facteurs protecteurs, notamment oncologiques. Le lien pédagogique passe par la sémiologie, les examens justifiés et l’orientation, avec prise en compte des préférences et de la compréhension du patient.</p>'),'PROFILES17','MEBEKO26','PROFILES-TRANS','ESMO25')
