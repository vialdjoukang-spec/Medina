from lesson_helpers import *
sections={
'CH-CIM':'Classe D77, inclusion et usage astérisque',
'CH-PROFILES':'Situations cliniques pertinentes, liste SSP 2017',
'CH-MEBEKO':'Introduction et exigences de l’examen fédéral 2026',
'CH-HUG-LAB':'Diapositive 3, repères adultes de numération, 2019',
'CH-RMS-DX':'Résumé, diagnostic et limites du cas urinaire, 2018',
'CH-CHUV-ASPLEN':'Pages 1–2, information et prévention après splénectomie, 2024',
'CH-CHUV-FEVER':'Page 3, conduite devant fièvre et plan antibiotique, 2024',
'CH-PRAZI-STATUS':'Liste Swissmedic du 30 septembre 2026 et recherches AmiKo',
'CH-IMPORT':'Section 2.1, importation humaine selon article 49 OAMéd',
'FI-PROPRANOLOL':'FI suisse de janvier 2023 : indication portale, doses et sécurité',
'FI-CARVEDILOL':'FI suisse d’octobre 2023 : indications, populations et limites',
'EU-PRAZI-RCP':'RCP français du 30 mai 2024, sections 4.1–4.6',
'EU-EMA-AVAIL':'Disponibilité de Biltricide dans les marchés concernés, 3 juin 2026',
'EU-ANSM-AVAIL':'Rupture française et approvisionnement exceptionnel, 6 mai 2026',
'EU-CLIN':'Consensus espagnol 2022 : cycle et présentation clinique',
'EU-DX':'Consensus espagnol 2022 : diagnostic, tableau 2 et limites',
'EU-TX':'Consensus espagnol 2022 : traitement, tableau 3 et populations',
'EU-FOLLOW':'Consensus espagnol 2022 : suivi et retraitement',
'INT-HSS-MEC':'Revue HSS 2021 : introduction, tableau 1 et mécanismes',
'INT-HSS-DX':'Revue HSS 2021 : résultats diagnostiques et tableaux 2–3',
'INT-HSS-TX':'Revue HSS 2021 : traitements, bêtabloquants, chirurgie et TIPS',
'INT-HSS-LIMIT':'Revue HSS 2021 : discussion, limites et conclusion',
'EU-EASL-BOUND':'EASL 2026 : définition de PSVD et exclusions explicites',
'INT-WHO':'OMS 2022, recommandation 4, page xix',
'NORMAL-SPLEEN':'OpenStax 21.1 : moelle, rate et organes lymphoïdes normaux',
'NORMAL-PORTAL':'OpenStax 20.5 : système porte hépatique normal',
'NORMAL-BLOOD':'OpenStax 18.1 : constituants et fonctions du sang normal'}
p=OUT/'source-ledger.json';x=json.loads(p.read_text())
for r in x['sources']:r['section']=sections[r['id']]
x['limitations']=['Lectures ciblées réelles ; textes complets hors Git, seulement métadonnées et paraphrases publiées.','Un cours antérieur n’est pas une source primaire.','Deux FI suisses et un RCP français explicitement distingués ; aucune FI suisse de praziquantel inventée.']
p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print('Intitulés des 27 passages rendus lisibles, sans changer les dates ni les empreintes des lectures.')
