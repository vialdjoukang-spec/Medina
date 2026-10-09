# Glossaire MEDINA — chapitre R02 Gangrène, non classée ailleurs (C-01-Cardiologie)
from cardio_1 import a, G

# ---- sociétés savantes et recommandations
a('IWGDF',[('I','International'),('W','Working'),('G','Group on the'),('D','Diabetic'),('F','Foot')],'International Working Group on the Diabetic Foot (Groupe de travail international sur le pied diabétique)',
 '<p>Groupe international qui publie depuis 1999 des recommandations sur la prévention et la prise en charge du pied diabétique ; version 2023 consultée pour ce cours, dont les recommandations conjointes IWGDF/IDSA sur l’infection.</p>','r02-iwgdf')
a('GVG',[('G','Global'),('V','Vascular'),('G','Guidelines')],'Global Vascular Guidelines (recommandations vasculaires mondiales) sur l’ischémie chronique menaçant le membre, 2019',
 '<p>Recommandations conjointes de l’ESVS, de la SVS et de la WFVS publiées en 2019 ; elles définissent la CLTI, adoptent WIfI et proposent les cadres PLAN et GLASS.</p>','r02-gvg')
a('SVS',[('S','Society for'),('V','Vascular'),('S','Surgery')],'Society for Vascular Surgery (Société américaine de chirurgie vasculaire)',
 '<p>Société savante nord-américaine, auteur de la classification WIfI et coauteur des Global Vascular Guidelines 2019.</p>')
a('WFVS',[('W','World'),('F','Federation of'),('V','Vascular'),('S','Societies')],'World Federation of Vascular Societies (Fédération mondiale des sociétés vasculaires)',
 '<p>Fédération coautrice des Global Vascular Guidelines 2019 sur l’ischémie chronique menaçant le membre.</p>')

# ---- scores, cadres décisionnels et mesures
a('LRINEC',[('L','Laboratory'),('R','Risk'),('I','Indicator for'),('NEC','NECrotizing fasciitis')],'Laboratory Risk Indicator for Necrotizing Fasciitis (indicateur biologique de risque de fasciite nécrosante)',
 '<p>Score fondé sur la protéine C-réactive, les leucocytes, l’hémoglobine, la natrémie, la créatinine et la glycémie. Un score d’au moins 6 n’a qu’une sensibilité de 68,2 % : il ne permet pas d’exclure une infection nécrosante.</p>','r02-lrinec')
a('PLAN',[('P','Patient risk (risque du patient)'),('L','Limb severity (sévérité de l’atteinte du membre)'),('AN','ANatomic complexity (complexité anatomique)')],'Cadre décisionnel de revascularisation des Global Vascular Guidelines 2019',
 '<p>Les trois axes sont examinés dans cet ordre : risque opératoire et espérance de vie, stade WIfI, puis anatomie selon GLASS.</p>','r02-plan')
a('GLASS',[('G','Global'),('L','Limb'),('A','Anatomic'),('S','Staging'),('S','System')],'Global Limb Anatomic Staging System (système mondial de stadification anatomique du membre)',
 '<p>Système des Global Vascular Guidelines 2019 qui définit une artère cible de l’aine à la cheville et classe la complexité des lésions sous-inguinales en stades I à III.</p>','r02-plan')
a('TcPO₂',[('Tc','TransCutanée (à travers la peau)'),('P','Pression partielle'),('O₂','en Oxygène')],'Pression transcutanée en oxygène',
 '<p>Mesure, par une électrode chauffée posée sur la peau, de la pression partielle d’oxygène qui diffuse depuis les capillaires. Inférieure à 30 mmHg : ischémie de grade WIfI 3.</p>','r02-tcpo2')

# ---- essais
a('BEST-CLI',[('BEST','Best Endovascular versus best Surgical Therapy'),('CLI','in patients with Critical Limb Ischemia')],'Essai BEST-CLI (2022)',
 '<p>Chez les patients disposant d’une grande veine saphène adéquate, le pontage réduisait les événements majeurs du membre ou les décès par rapport à l’endovasculaire (42,6 % contre 57,4 %).</p>','r02-bestcli')
a('BASIL-2',[('BASIL','Bypass versus Angioplasty in Severe Ischaemia of the Leg'),('2','deuxième essai')],'Essai BASIL-2 (2023)',
 '<p>Dans la revascularisation sous-poplitée, la stratégie endovasculaire d’abord donnait une meilleure survie sans amputation que le pontage veineux, surtout par moins de décès.</p>','r02-basil2')

# ---- codes de la classification
a('R02.0',[('R02.0','code de la classification internationale des maladies, nécrose de la peau et du tissu sous-cutané, non classée ailleurs')],'Nécrose de la peau et du tissu sous-cutané, non classée ailleurs (CIM-10-GM 2024)',
 '<p>Sous-catégorie à cinq caractères selon le siège ; elle inclut la nécrose cutanée post-traumatique.</p>','r02-codage')
a('R02.07',[('R02.07','code de la classification internationale des maladies, nécrose cutanée de la région de la cheville, du pied et des orteils')],'Nécrose de la peau et du tissu sous-cutané de la cheville, du pied et des orteils (CIM-10-GM 2024)',
 '<p>Code employé lorsque la nécrose du pied n’est pas attribuée à une cause classée ailleurs, par exemple une nécrose post-traumatique.</p>','r02-codage')
a('R02.8',[('R02.8','code de la classification internationale des maladies, autre gangrène et gangrène non précisée')],'Autre gangrène et gangrène non précisée, non classée ailleurs (CIM-10-GM 2024)',
 '<p>Code d’attente ou de mécanisme local, remplacé par le code de la cause dès qu’elle est établie.</p>','r02-codage')
a('A48.0',[('A48.0','code de la classification internationale des maladies, gangrène gazeuse')],'Gangrène gazeuse (CIM-10-GM 2024)',
 '<p>Myonécrose clostridienne ; ce code exclut l’emploi de R02.</p>','r02-gazeuse')
a('PHIL', [('P', 'Public'), ('H', 'Health (santé)'), ('I', 'Image'), ('L', 'Library (photothèque)')], 'Public Health Image Library des CDC', '<p>Photothèque des Centers for Disease Control and Prevention américains, dont les images produites par des agents fédéraux sont dans le domaine public ; source de la figure de Clostridium perfringens de ce cours.</p>')
