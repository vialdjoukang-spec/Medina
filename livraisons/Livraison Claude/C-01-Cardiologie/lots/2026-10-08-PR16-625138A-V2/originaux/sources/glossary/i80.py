from cardio_1 import a, G
L=[
('HERDOO2',[('H','Hyperpigmentation'),('E','Edema (œdème)'),('R','Redness (rougeur)'),('D','D-dimères ≥ 250 µg/L'),('OO','Obésité (IMC ≥ 30), Older (âge ≥ 65 ans)'),('2','seuil de 2 points')],'Score HERDOO2','<p>Chez la femme après une première thrombose non provoquée : ≤ 1 point = faible risque de récidive, arrêt possible.</p>'),
('SOX',[('SOX','nom d’essai (bas de compression après thrombose), non strictement lettre à lettre')],'Essai SOX (2014)','<p>Les bas de compression ne préviennent pas le syndrome post-thrombotique.</p>'),
('ATTRACT',[('ATTRACT','Acute venous Thrombosis: Thrombus Removal with Adjunctive Catheter-directed Thrombolysis')],'Essai ATTRACT (2017)','<p>Thrombolyse dirigée par cathéter : pas de réduction globale du syndrome post-thrombotique.</p>'),
('CALISTO',[('CALISTO','Comparison of ARixtra in LowER Extremity Superficial Thrombophlebitis with placebO (non strictement lettre à lettre)')],'Essai CALISTO (2010)','<p>Fondaparinux 2,5 mg 45 jours dans la thrombose superficielle.</p>'),
('SOME',[('SOME','Screening for Occult Malignancy in patients with idiopathic venous thromboEmbolism')],'Essai SOME (2015)','<p>Pas de bénéfice du scanner systématique pour rechercher un cancer.</p>'),
('ADJUST-PE',[('ADJUST','AGE-ADJUSTed D-dimer cutoff'),('PE','Pulmonary Embolism')],'Étude ADJUST-PE (2014)','<p>Validation du seuil de D-dimères ajusté à l’âge.</p>'),
('EINSTEIN',[('EINSTEIN','nom d’essai (rivaroxaban dans la maladie thromboembolique)')],'Essais EINSTEIN','<p>Rivaroxaban versus traitement standard.</p>'),
('AMPLIFY',[('AMPLIFY','nom d’essai (apixaban dans la maladie thromboembolique)')],'Essai AMPLIFY','<p>Apixaban versus traitement standard : moins d’hémorragies majeures.</p>'),
('Hokusai-VTE',[('Hokusai','nom d’essai (édoxaban)'),('VTE','Venous ThromboEmbolism')],'Essai Hokusai-VTE','<p>Édoxaban versus warfarine.</p>'),
('RE-COVER',[('RE-COVER','nom d’essai (dabigatran), non strictement lettre à lettre')],'Essai RE-COVER','<p>Dabigatran versus warfarine.</p>'),
('JAK2',[('JAK','JAnus Kinase'),('2','2')],'Kinase Janus 2','<p>Gène muté (V617F) dans les syndromes myéloprolifératifs.</p>'),
('V617F',[('V','valine'),('617','position 617'),('F','remplacée par une phénylalanine')],'Mutation V617F','<p>Mutation activatrice de JAK2.</p>'),
('G20210A',[('G','guanine'),('20210','position 20210 du gène de la prothrombine'),('A','remplacée par une adénine')],'Mutation G20210A de la prothrombine','<p>Thrombophilie héréditaire fréquente.</p>'),
('R506Q',[('R','arginine'),('506','position 506 du facteur V'),('Q','remplacée par une glutamine')],'Mutation R506Q (facteur V Leiden)','<p>Résistance à la protéine C activée.</p>'),
('F5',[('F','Facteur'),('5','V')],'Gène du facteur V','<p>Porte la mutation Leiden.</p>'),
('PF4',[('P','Platelet'),('F','Factor'),('4','4')],'Facteur plaquettaire 4','<p>Cible des anticorps de la thrombopénie induite par l’héparine.</p>','i80-tih'),
('4T',[('4','quatre critères'),('T','Thrombopénie, Timing, Thrombose, auTres causes')],'Score 4T','<p>Probabilité clinique de thrombopénie induite par l’héparine.</p>','i80-tih'),
('PESI',[('P','Pulmonary'),('E','Embolism'),('S','Severity'),('I','Index')],'Index de sévérité de l’embolie pulmonaire','<p>Pronostic de mortalité à 30 jours.</p>'),
('Budd-Chiari',[('Budd-Chiari','nom propre : George Budd et Hans Chiari')],'Syndrome de Budd-Chiari','<p>Obstruction des veines sus-hépatiques.</p>'),
('Paget-Schroetter',[('Paget-Schroetter','nom propre : James Paget et Leopold von Schrötter')],'Syndrome de Paget-Schroetter','<p>Thrombose d’effort de la veine sous-clavière.</p>'),
('May-Thurner',[('May-Thurner','nom propre : Robert May et Josef Thurner')],'Syndrome de May-Thurner (Cockett)','<p>Compression de la veine iliaque commune gauche.</p>'),
('Cockcroft-Gault',[('Cockcroft-Gault','nom propre : Donald Cockcroft et Henry Gault')],'Formule de Cockcroft-Gault','<p>Estimation de la clairance de la créatinine utilisée pour doser les anticoagulants oraux directs.</p>'),
('ISRS',[('I','Inhibiteurs'),('S','Sélectifs de la'),('R','Recapture de la'),('S','Sérotonine')],'Inhibiteurs sélectifs de la recapture de la sérotonine','<p>Antidépresseurs ; augmentent le risque hémorragique en association aux anticoagulants.</p>'),
]
for x in L: a(*x)
for c,tt in [('I80.0','Phlébite et thrombophlébite des vaisseaux superficiels des membres inférieurs'),('I80.1','Phlébite et thrombophlébite de la veine fémorale'),('I80.2','Phlébite et thrombophlébite d’autres vaisseaux profonds des membres inférieurs'),('I80.3','Phlébite et thrombophlébite des membres inférieurs, sans précision'),('I82.0','Syndrome de Budd-Chiari'),('I82.2','Embolie et thrombose de la veine cave'),('I82.8','Embolie et thrombose d’autres veines précisées')]:
    a(c,[(c,'code de la Classification internationale des maladies, 10e révision, modification allemande')],tt,'<p>Code CIM-10-GM.</p>')
a('CHEST',[('CHEST','nom de la revue de l’American College of Chest Physicians (non abréviatif)')],'Revue CHEST','<p>Revue et recommandations de l’American College of Chest Physicians.</p>')
a('EASL',[('E','European'),('A','Association for the'),('S','Study of the'),('L','Liver')],'Association européenne pour l’étude du foie','<p>Recommandations en hépatologie.</p>')
a('VTE',[('V','Venous'),('T','Thrombo'),('E','Embolism')],'Maladie thromboembolique veineuse (anglais)','<p>Terme anglais des titres de références.</p>')
for k,t2 in [('VIIa','facteur VII activé'),('VIII','facteur VIII (antihémophilique A)'),('VIIIa','facteur VIII activé'),('XI','facteur XI')]:
    a(k,[(k,'chiffre romain de la nomenclature des facteurs de coagulation : '+t2)],'Facteur '+k,'<p>'+t2[0].upper()+t2[1:]+' de la coagulation.</p>','i80-coag')
