# Glossaire MEDINA — I77 — Autres atteintes des artères, des artérioles et des capillaires (C-01-Cardiologie)
from cardio_1 import a, G

L = [
# ---- gènes et voie de signalisation
('ENG',[('ENG','ENdoGline (nom du gène, abréviation de l’anglais endoglin)')],'Gène de l’endogline',
 '<p>Code le corécepteur endogline de l’endothélium, qui participe à la signalisation de BMP9. Ses variants pathogènes causent la télangiectasie hémorragique héréditaire de type 1, où les malformations pulmonaires et cérébrales sont plus fréquentes.</p>','i77-genetique-thh'),
('ACVRL1',[('ACVR','ACtiVin Receptor (récepteur de l’activine)'),('L1','Like 1 (apparenté, type 1)')],'Gène du récepteur apparenté au récepteur de l’activine de type 1 (ALK1)',
 '<p>Code le récepteur ALK1 de l’endothélium. Ses variants pathogènes causent la télangiectasie hémorragique héréditaire de type 2, où les malformations hépatiques sont plus fréquentes.</p>','i77-genetique-thh'),
('ALK1',[('A','Activin receptor-'),('L','Like'),('K','Kinase'),('1','1')],'Kinase apparentée au récepteur de l’activine de type 1',
 '<p>Récepteur endothélial de BMP9, codé par le gène ACVRL1. Son signal stabilise les vaisseaux néoformés et freine la voie du VEGF.</p>','i77-genetique-thh'),
('SMAD',[('SMAD','fusion de Sma (gène du nématode) et MAD (Mothers Against Decapentaplegic, gène de la drosophile)')],'Famille des protéines SMAD',
 '<p>Protéines qui transmettent au noyau le signal des récepteurs de la famille du TGF-β et de BMP9.</p>'),
('SMAD4',[('SMAD','homologue des protéines Sma et MAD'),('4','membre 4')],'Gène SMAD4',
 '<p>Transmetteur commun de la voie du TGF-β et de BMP9. Ses variants causent une polypose juvénile associée à la télangiectasie hémorragique héréditaire, qui impose une surveillance colique dès 15 ans.</p>','i77-smad4'),
('GDF2',[('G','Growth'),('D','Differentiation'),('F','Factor'),('2','2')],'Gène du facteur de croissance et de différenciation 2 (BMP9)',
 '<p>Code BMP9. Ses variants sont une cause rare d’un tableau proche de la télangiectasie hémorragique héréditaire.</p>','i77-genetique-thh'),
('BMP9',[('B','Bone (os)'),('M','Morphogenetic (morphogénétique)'),('P','Protein (protéine)'),('9','type 9')],'Protéine morphogénétique osseuse 9',
 '<p>Facteur circulant qui se fixe sur le complexe ALK1-endogline de l’endothélium et maintient la quiescence et la stabilité des vaisseaux.</p>'),
('PHACTR1',[('PHACTR','PHosphatase and ACTin Regulator (régulateur de la phosphatase et de l’actine)'),('1','1')],'Gène PHACTR1',
 '<p>Locus dont un variant fréquent est associé à la dysplasie fibromusculaire, à la dissection coronaire spontanée et à la migraine.</p>','i77-phactr1'),
# ---- essais, réseaux, publications
('PATH-HHT',[('PATH','nom d’essai (Pomalidomide in the Treatment of HHT), non strictement lettre à lettre'),('HHT','Hereditary Haemorrhagic Telangiectasia (télangiectasie hémorragique héréditaire)')],'Essai PATH-HHT (2024)',
 '<p>Essai randomisé contre placebo : le pomalidomide 4 mg par jour réduit la sévérité des épistaxis de la télangiectasie hémorragique héréditaire.</p>','i77-d-pomalidomide'),
('HHT',[('H','Hereditary (héréditaire)'),('H','Haemorrhagic (hémorragique)'),('T','Telangiectasia (télangiectasie)')],'Télangiectasie hémorragique héréditaire (sigle anglais)',
 '<p>Maladie autosomique dominante de la voie BMP9-ALK1-endogline, codée I78.0.</p>','i77-curacao'),
('InHIBIT-Bleed',[('InHIBIT-Bleed','nom d’étude (International HHT Intravenous Bevacizumab Investigational Team, saignement), non strictement lettre à lettre')],'Étude InHIBIT-Bleed (2021)',
 '<p>Cohorte internationale rétrospective de 238 patients traités par bévacizumab intraveineux pour des saignements de télangiectasie hémorragique héréditaire.</p>','i77-d-bevacizumab'),
('NOSE',[('NOSE','nom d’essai (Nasal Ointment or Spray for Epistaxis, d’après le sens anglais « nez »), non strictement lettre à lettre')],'Essai NOSE (2016)',
 '<p>Essai randomisé : les sprays nasaux de bévacizumab, d’œstriol ou d’acide tranexamique ne font pas mieux que le sérum physiologique sur les épistaxis de la télangiectasie hémorragique héréditaire.</p>'),
('CARoSO',[('CARoSO','nom d’essai (libération du ligament arqué contre opération simulée, en néerlandais et anglais), non strictement lettre à lettre')],'Essai CARoSO',
 '<p>Essai randomisé en cours comparant la libération endoscopique rétropéritonéale du ligament arqué médian à une opération simulée ; ses critères d’inclusion sont repris par l’ESVS 2025.</p>','i77-criteres-ligament'),
('VASCERN',[('VASC','VASCular (vasculaire)'),('ERN','European Reference Network (réseau européen de référence)')],'Réseau européen de référence des maladies vasculaires rares multisystémiques',
 '<p>Réseau de centres experts européens qui publie des parcours de soins pour les maladies vasculaires rares, dont la télangiectasie hémorragique héréditaire.</p>','i77-vascern'),
('PLoS',[('P','Public'),('L','Library'),('o','of'),('S','Science')],'Public Library of Science',
 '<p>Éditeur de revues scientifiques en accès libre, dont <i>PLoS Genetics</i>.</p>'),
('MMWR',[('M','Morbidity and'),('M','Mortality'),('W','Weekly'),('R','Report')],'Rapport hebdomadaire de morbidité et de mortalité des CDC',
 '<p>Publication officielle des CDC, où paraissent les recommandations américaines de traitement des infections sexuellement transmissibles.</p>'),
# ---- noms propres composés
('Rendu-Osler-Weber',[('Rendu-Osler-Weber','noms propres : Henri Rendu, William Osler et Frederick Parkes Weber')],'Maladie de Rendu-Osler-Weber',
 '<p>Éponyme de la télangiectasie hémorragique héréditaire (I78.0).</p>','i77-rendu'),
('Rendu-Osler',[('Rendu-Osler','noms propres : Henri Rendu et William Osler')],'Maladie de Rendu-Osler','<p>Forme courte de l’éponyme de la télangiectasie hémorragique héréditaire.</p>','i77-rendu'),
('Nicoladoni-Branham',[('Nicoladoni-Branham','noms propres : Carl Nicoladoni et Harris Branham')],'Signe de Nicoladoni-Branham',
 '<p>Ralentissement de la fréquence cardiaque à la compression d’une fistule artérioveineuse à fort débit.</p>','i77-branham'),
('Erdheim-Gsell',[('Erdheim-Gsell','noms propres : Jakob Erdheim et Otto Gsell')],'Nécrose kystique de la média d’Erdheim-Gsell',
 '<p>Terme ancien de la dégénérescence de la média aortique, substrat des dissections.</p>','i77-degenerescence'),
('Al-Samkari',[('Al-Samkari','nom propre : Hanny Al-Samkari, hématologue')],'Hanny Al-Samkari','<p>Premier auteur des études InHIBIT-Bleed et PATH-HHT.</p>'),
# ---- fragments cités
('I-13-Immunologie et allergologie',[('I','Immunologie (initiale de la spécialité)'),('13','treizième fragment dans l’ordre de production'),('Immunologie et allergologie','nom littéral du fragment')],'Fragment I-13-Immunologie et allergologie de MEDINA',
 '<p>Fragment qui réunit les cours d’immunologie et d’allergologie, dont M31 — Vascularites systémiques (organisation/fragments.json).</p>'),
('G-04-Gastroentérologie et hépatologie',[('G','Gastroentérologie (initiale de la spécialité)'),('04','quatrième fragment dans l’ordre de production'),('Gastroentérologie et hépatologie','nom littéral du fragment')],'Fragment G-04-Gastroentérologie et hépatologie de MEDINA',
 '<p>Fragment qui réunit les cours de gastroentérologie et d’hépatologie, dont la cirrhose (organisation/fragments.json).</p>'),
('E-06-Endocrinologie et métabolisme',[('E','Endocrinologie (initiale de la spécialité)'),('06','sixième fragment dans l’ordre de production'),('Endocrinologie et métabolisme','nom littéral du fragment')],'Fragment E-06-Endocrinologie et métabolisme de MEDINA',
 '<p>Fragment qui réunit les cours d’endocrinologie et de métabolisme, dont les diabètes (organisation/fragments.json).</p>'),
]
for x in L:
    a(*x)

# ---- codes CIM-10-GM 2024 cités hors whitelist ou utiles en infobulle
for c, tt in [('Q27.3', 'Malformation artério-veineuse périphérique (congénitale)'),
              ('Q82.5', 'Nævus congénital non néoplasique (angiome plan, tache de vin)'),
              ('A52.0', 'Syphilis cardiovasculaire (code dague associé à I79.0* ou I79.1*)'),
              ('I77.0', 'Fistule artério-veineuse, acquise'), ('I77.1', 'Sténose d’une artère'),
              ('I77.2', 'Rupture d’une artère'), ('I77.3', 'Dysplasie fibromusculaire artérielle'),
              ('I77.4', 'Syndrome de compression de l’artère cœliaque'), ('I77.5', 'Nécrose d’une artère'),
              ('I77.6', 'Artérite, sans précision'), ('I77.80', 'Ulcère pénétrant de l’aorte'),
              ('I77.88', 'Autres atteintes précisées des artères et artérioles'), ('I77.9', 'Atteinte des artères et artérioles, sans précision'),
              ('I78.0', 'Télangiectasie hémorragique héréditaire'), ('I78.1', 'Nævus, non néoplasique'),
              ('I78.8', 'Autres maladies des capillaires'), ('I78.9', 'Maladie des capillaires, sans précision'),
              ('I79.0', 'Anévrisme de l’aorte au cours de maladies classées ailleurs (code astérisque)'),
              ('I79.1', 'Aortite au cours de maladies classées ailleurs (code astérisque)'),
              ('I79.2', 'Angiopathie périphérique au cours de maladies classées ailleurs (code astérisque)'),
              ('I79.8', 'Autres atteintes artérielles, artériolaires et capillaires au cours de maladies classées ailleurs (code astérisque)')]:
    a(c, [(c, 'code de la Classification internationale des maladies, 10e révision, modification allemande')], tt, '<p>Code CIM-10-GM 2024.</p>')
