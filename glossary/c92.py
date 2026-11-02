from cardio_1 import a, G
# C92 : ajouts conditionnels, aucun terme global existant écrasé.

if 'LAM' not in G:
    a('LAM', [('LAM', 'Leucémie aiguë myéloïde')], 'Leucémie aiguë myéloïde', '<p>Entité définie par morphologie et génétique selon une classification datée ; exceptions au seuil de blastes.</p>', 'c92-classification')

if 'LPA' not in G:
    a('LPA', [('LPA', 'Leucémie promyélocytaire aiguë')], 'Leucémie promyélocytaire aiguë', '<p>Leucémie associée à PML::RARA, avec risque de coagulopathie et circuit urgent.</p>', 'c92-differenciation')

if 'LMC' not in G:
    a('LMC', [('LMC', 'Leucémie myéloïde chronique')], 'Leucémie myéloïde chronique', '<p>Néoplasie définie par BCR::ABL1, à caractériser et suivre par méthodes adaptées.</p>', 'c92-bcr-abl')

if 'MRD' not in G:
    a('MRD', [('MRD', 'Maladie résiduelle mesurable')], 'Maladie résiduelle mesurable', '<p>Signal résiduel étudié avec marqueur, méthode et sensibilité connus ; négativité ne signifie pas éradication certaine.</p>', 'c92-mrd')

if 'MMR' not in G:
    a('MMR', [('MMR', 'Réponse moléculaire majeure')], 'Réponse moléculaire majeure', '<p>En LMC, BCR::ABL1 IS ≤ 0,1 % avec contrôles appropriés.</p>', 'c92-cml-is')

if 'TFR' not in G:
    a('TFR', [('TFR', 'Rémission sans traitement')], 'Rémission sans traitement', '<p>Arrêt surveillé du TKI chez une personne sélectionnée, avec suivi moléculaire durable.</p>', 'c92-tfr')

if 'ATRA' not in G:
    a('ATRA', [('ATRA', 'Acide tout-trans rétinoïque')], 'Acide tout-trans rétinoïque', '<p>Trétinoïne utilisée notamment dans la LPA ; différenciation et toxicités nécessitent surveillance.</p>', 'c92-differenciation')

if 'ATO' not in G:
    a('ATO', [('ATO', 'Trioxyde d’arsenic')], 'Trioxyde d’arsenic', '<p>Produit utilisé dans des indications précises de LPA ; surveillance du QT et des électrolytes.</p>', 'c92-differenciation')

if 'ABL' not in G:
    a('ABL', [('ABL', 'Notation ABL du libellé de codage')], 'Notation ABL du libellé de codage', '<p>Abréviation présente dans le libellé historique BCR/ABL de la CIM-10-GM ; le texte biologique moderne précise BCR::ABL1.</p>', 'c92-bcr-abl')

if 'ICD-10-CM' not in G:
    a('ICD-10-CM', [('ICD-10-CM', 'Modification clinique américaine de la CIM-10')], 'Modification clinique américaine de la CIM-10', '<p>Classification américaine distincte de la CIM-10-GM employée dans le projet suisse ; ne pas importer ses caractères de rechute.</p>', 'c92-classification')

if 'ETNK1' not in G:
    a('ETNK1', [('ETNK1', 'Symbole du gène ETNK1')], 'Symbole du gène ETNK1', '<p>Une mutation peut soutenir le diagnostic de MDS/MPN avec neutrophilie dans le contexte approprié ; elle ne définit pas seule la maladie.</p>', 'c92-genetique')

if 'R132' not in G:
    a('R132', [('R132', 'Position 132 de la protéine IDH1')], 'Position 132 de la protéine IDH1', '<p>Notation de la position arginine 132 concernée par les mutations ciblées dans l’indication de Tibsovo.</p>', 'c92-genetique')

if 'TKI' not in G:
    a('TKI', [('TKI', 'Inhibiteur de tyrosine kinase')], 'Inhibiteur de tyrosine kinase', '<p>Classe de traitements dont cible, site de liaison, indication et interactions doivent être précisés.</p>', 'c92-bcr-abl')

if 'IS' not in G:
    a('IS', [('IS', 'Échelle internationale')], 'Échelle internationale', '<p>International Scale : standardisation de BCR::ABL1 pour les transcrits usuels ; contrôle analytique requis.</p>', 'c92-cml-is')

if 'VashiDonsk' not in G:
    a('VashiDonsk', [('VashiDonsk', 'VashiDonsk, auteur du fichier original')], 'VashiDonsk, auteur du fichier original', '<p>Nom du contributeur de la photographie Auer rods sur Wikimedia Commons ; nom propre, pas abréviation médicale.</p>', 'c92-sources')

if 'HMA' not in G:
    a('HMA', [('HMA', 'Agent hypométhylant')], 'Agent hypométhylant', '<p>Terme de classe utilisé dans les recommandations ; produit et formulation exacts restent à préciser.</p>', 'c92-strategie')

if 'CR' not in G:
    a('CR', [('CR', 'Rémission complète')], 'Rémission complète', '<p>Catégorie de réponse définie par morphologie, absence de maladie extramédullaire et récupération hématologique selon critères ELN.</p>', 'c92-reponse')

if 'CRh' not in G:
    a('CRh', [('CRh', 'Rémission complète avec récupération hématologique partielle')], 'Rémission complète avec récupération hématologique partielle', '<p>Autres critères de CR, neutrophiles ≥ 0,5 G/L et plaquettes ≥ 50 G/L selon ELN 2022.</p>', 'c92-reponse')

if 'CRi' not in G:
    a('CRi', [('CRi', 'Rémission complète avec récupération hématologique incomplète')], 'Rémission complète avec récupération hématologique incomplète', '<p>Catégorie distincte de CR ; préciser la classification et ne pas recompter CRh si cette catégorie est employée.</p>', 'c92-reponse')

if 'MR4' not in G:
    a('MR4', [('MR4', 'Réponse moléculaire de profondeur quatre logs')], 'Réponse moléculaire de profondeur quatre logs', '<p>BCR::ABL1 IS ≤ 0,01 %, sous réserve de contrôles analytiques adaptés.</p>', 'c92-cml-is')

if 'MLL' not in G:
    a('MLL', [('MLL', 'Munich Leukemia Laboratory')], 'Munich Leukemia Laboratory', '<p>Laboratoire européen cité pour le diagnostic des MDS/MPN avec neutrophilie ; source ne prouve pas une incidence suisse.</p>', 'c92-sources')

if 'BCL-2' not in G:
    a('BCL-2', [('BCL-2', 'Protéine BCL-2')], 'Protéine BCL-2', '<p>Protéine anti-apoptotique ciblée par le vénétoclax ; expression ne crée pas à elle seule une indication.</p>', 'c92-strategie')

if 'J8' not in G:
    a('J8', [('J8', 'Huitième jour du cycle indiqué')], 'Huitième jour du cycle indiqué', '<p>Repère de calendrier, non acronyme médical ; ne pas confondre induction, consolidation et entretien.</p>', 'c92-fi')

if 'J6' not in G:
    a('J6', [('J6', 'Sixième jour du cycle indiqué')], 'Sixième jour du cycle indiqué', '<p>Repère de calendrier dont le cycle doit être précisé.</p>', 'c92-fi')

if 'J9' not in G:
    a('J9', [('J9', 'Neuvième jour du cycle indiqué')], 'Neuvième jour du cycle indiqué', '<p>Repère de calendrier, notamment dans une procédure de contrôle ECG de Xospata.</p>', 'c92-fi')

if 'QTcF' not in G:
    a('QTcF', [('QTcF', 'Intervalle QT corrigé selon Fridericia')], 'Intervalle QT corrigé selon Fridericia', '<p>Paramètre ECG utilisé dans la FI de quizartinib ; seuils d’initiation, suspension et reprise propres au produit.</p>', 'c92-interactions')

if 'CPK' not in G:
    a('CPK', [('CPK', 'Créatine phosphokinase')], 'Créatine phosphokinase', '<p>Enzyme mesurée notamment dans la surveillance biologique sous giltéritinib.</p>', 'c92-fi')

if 'MEBEKO' not in G:
    a('MEBEKO', [('MEBEKO', 'Commission des professions médicales')], 'Commission des professions médicales', '<p>Autorité suisse dont les exigences de l’examen 2026 consultées renvoient au référentiel PROFILES.</p>', 'c92-profiles')

if 'C92.0' not in G:
    a('C92.0', [('C92.0', 'Code CIM-10-GM C92.0')], 'Code CIM-10-GM C92.0', '<p>Code administratif, non acronyme ; voir le tableau des sous-catégories et les limites de la correspondance biologique.</p>', 'c92-classification')

if 'C92.1' not in G:
    a('C92.1', [('C92.1', 'Code CIM-10-GM C92.1')], 'Code CIM-10-GM C92.1', '<p>Code administratif, non acronyme ; voir le tableau des sous-catégories et les limites de la correspondance biologique.</p>', 'c92-classification')

if 'C92.2' not in G:
    a('C92.2', [('C92.2', 'Code CIM-10-GM C92.2')], 'Code CIM-10-GM C92.2', '<p>Code administratif, non acronyme ; voir le tableau des sous-catégories et les limites de la correspondance biologique.</p>', 'c92-classification')

if 'C92.3' not in G:
    a('C92.3', [('C92.3', 'Code CIM-10-GM C92.3')], 'Code CIM-10-GM C92.3', '<p>Code administratif, non acronyme ; voir le tableau des sous-catégories et les limites de la correspondance biologique.</p>', 'c92-classification')

if 'C92.4' not in G:
    a('C92.4', [('C92.4', 'Code CIM-10-GM C92.4')], 'Code CIM-10-GM C92.4', '<p>Code administratif, non acronyme ; voir le tableau des sous-catégories et les limites de la correspondance biologique.</p>', 'c92-classification')

if 'C92.5' not in G:
    a('C92.5', [('C92.5', 'Code CIM-10-GM C92.5')], 'Code CIM-10-GM C92.5', '<p>Code administratif, non acronyme ; voir le tableau des sous-catégories et les limites de la correspondance biologique.</p>', 'c92-classification')

if 'C92.6' not in G:
    a('C92.6', [('C92.6', 'Code CIM-10-GM C92.6')], 'Code CIM-10-GM C92.6', '<p>Code administratif, non acronyme ; voir le tableau des sous-catégories et les limites de la correspondance biologique.</p>', 'c92-classification')

if 'C92.7' not in G:
    a('C92.7', [('C92.7', 'Code CIM-10-GM C92.7')], 'Code CIM-10-GM C92.7', '<p>Code administratif, non acronyme ; voir le tableau des sous-catégories et les limites de la correspondance biologique.</p>', 'c92-classification')

if 'C92.8' not in G:
    a('C92.8', [('C92.8', 'Code CIM-10-GM C92.8')], 'Code CIM-10-GM C92.8', '<p>Code administratif, non acronyme ; voir le tableau des sous-catégories et les limites de la correspondance biologique.</p>', 'c92-classification')

if 'C92.9' not in G:
    a('C92.9', [('C92.9', 'Code CIM-10-GM C92.9')], 'Code CIM-10-GM C92.9', '<p>Code administratif, non acronyme ; voir le tableau des sous-catégories et les limites de la correspondance biologique.</p>', 'c92-classification')

if 'C92.00' not in G:
    a('C92.00', [('C92.00', 'Code CIM-10-GM C92.00')], 'Code CIM-10-GM C92.00', '<p>Code administratif, non acronyme ; voir le tableau des sous-catégories et les limites de la correspondance biologique.</p>', 'c92-classification')

if 'C92.01' not in G:
    a('C92.01', [('C92.01', 'Code CIM-10-GM C92.01')], 'Code CIM-10-GM C92.01', '<p>Code administratif, non acronyme ; voir le tableau des sous-catégories et les limites de la correspondance biologique.</p>', 'c92-classification')

if 'C93.1' not in G:
    a('C93.1', [('C93.1', 'Code CIM-10-GM C93.1')], 'Code CIM-10-GM C93.1', '<p>Code administratif, non acronyme ; voir le tableau des sous-catégories et les limites de la correspondance biologique.</p>', 'c92-classification')
