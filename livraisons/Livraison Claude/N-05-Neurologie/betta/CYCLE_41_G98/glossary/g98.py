"""Abréviations G98 ; entrées conditionnelles, sans mutation des glossaires existants."""
from cardio_1 import a, G
if 'CNO' not in G:
    a('CNO', [('C', 'Charcot'), ('N', 'Neuro-'), ('O', 'Ostéoarthropathie')], 'Charcot neuro-osteoarthropathy (neuro-ostéoarthropathie de Charcot)', '<p>Processus inflammatoire survenant chez une personne neuropathique et aboutissant à des lésions des os, des articulations et des tissus mous. L’abréviation vient de l’anglais Charcot neuro-osteoarthropathy.</p>', 'g98-cno')
if 'IWGDF' not in G:
    a('IWGDF', [('I', 'International'), ('W', 'Working'), ('G', 'Group on the'), ('D', 'Diabetic'), ('F', 'Foot')], 'International Working Group on the Diabetic Foot', '<p>Groupe international dont la recommandation 2023 sur la neuro-ostéoarthropathie de Charcot active sert de référence principale à ce cours. Il applique la méthode GRADE.</p>', 'g98-cno')
if 'SAI' not in G:
    a('SAI', [('S', 'Sans'), ('A', 'Autre'), ('I', 'Indication')], 'Sans autre indication (sans autre précision)', '<p>Mention de la classification employée lorsque le diagnostic n’est pas précisé : « affection du système nerveux SAI ».</p>', 'g98-codage')
if 'CIM' not in G:
    a('CIM', [('C', 'Classification'), ('I', 'Internationale des'), ('M', 'Maladies')], 'Classification internationale des maladies', '<p>Classification des maladies dont ce cours utilise la version allemande modifiée CIM-10-GM 2024.</p>', 'g98-codage')
if 'IRM' not in G:
    a('IRM', [('I', 'Imagerie par'), ('R', 'Résonance'), ('M', 'Magnétique')], 'Imagerie par résonance magnétique', '<p>Technique d’imagerie qui renseigne sur l’œdème médullaire, l’épanchement et les microfractures avant que la radiographie ne soit anormale.</p>', 'g98-irm')
if 'TDM' not in G:
    a('TDM', [('T', 'Tomo'), ('D', 'Densito'), ('M', 'Métrie')], 'Tomodensitométrie', '<p>Imagerie par rayons X en coupes, utile tardivement dans la CNO et pour planifier la chirurgie.</p>', 'g98-irm')
if 'CRP' not in G:
    a('CRP', [('C', 'C-'), ('R', 'Reactive'), ('P', 'Protein')], 'Protéine C réactive (C-reactive protein)', '<p>Marqueur biologique d’inflammation. Il n’est pas recommandé pour poser ou exclure le diagnostic de CNO.</p>', 'g98-irm')
if 'VS' not in G:
    a('VS', [('V', 'Vitesse de'), ('S', 'Sédimentation')], 'Vitesse de sédimentation', '<p>Examen biologique d’inflammation, non recommandé pour poser ou exclure le diagnostic de CNO.</p>', 'g98-irm')
if 'TVP' not in G:
    a('TVP', [('T', 'Thrombose'), ('V', 'Veineuse'), ('P', 'Profonde')], 'Thrombose veineuse profonde', '<p>Diagnostic différentiel du pied rouge, chaud et tuméfié, à exclure.</p>', 'g98-osteomyelite')
if 'RANKL' not in G:
    a('RANKL', [('R', 'Receptor'), ('A', 'Activator of'), ('N', 'Nuclear factor'), ('K', 'Kappa-B'), ('L', 'Ligand')], 'Receptor activator of nuclear factor kappa-B ligand', '<p>Molécule de signalisation qui, avec le TNF-α, recrute des ostéoclastes très agressifs dans la CNO.</p>', 'g98-rankl')
if 'OPG' not in G:
    a('OPG', [('O', 'Osté'), ('P', 'Protégé'), ('G', 'Rine')], 'Ostéoprotégérine', '<p>Élément de l’axe OPG/RANKL/RANK dont des polymorphismes sont suspectés d’être des facteurs de risque de CNO.</p>', 'g98-rankl')
if 'RANK' not in G:
    a('RANK', [('R', 'Receptor'), ('A', 'Activator of'), ('N', 'Nuclear factor'), ('K', 'Kappa-B')], 'Receptor activator of nuclear factor kappa-B', '<p>Récepteur de l’axe OPG/RANKL/RANK.</p>', 'g98-rankl')
if 'NF' not in G:
    a('NF', [('N', 'Nuclear'), ('F', 'Factor')], 'Nuclear factor (facteur nucléaire) ; NF-κB : nuclear factor kappa-B', '<p>Facteur activé par la voie RANKL, qui déclenche l’ostéoclastogenèse dans la CNO.</p>', 'g98-rankl')
if 'TNF' not in G:
    a('TNF', [('T', 'Tumor'), ('N', 'Necrosis'), ('F', 'Factor')], 'Tumor necrosis factor (facteur de nécrose tumorale) ; TNF-α : alpha', '<p>Cytokine qui, avec RANKL, recrute des ostéoclastes agressifs dans la CNO.</p>', 'g98-rankl')
if 'STIR' not in G:
    a('STIR', [('S', 'Short'), ('T', 'Tau'), ('I', 'Inversion'), ('R', 'Recovery')], 'Short tau inversion recovery', '<p>Séquence d’IRM sensible aux liquides, utilisée pour repérer l’œdème médullaire.</p>', 'g98-irm')
if 'TSE' not in G:
    a('TSE', [('T', 'Turbo'), ('S', 'Spin'), ('E', 'Echo')], 'Turbo spin echo', '<p>Type de séquence d’IRM ; la séquence T1 TSE complète la séquence STIR.</p>', 'g98-irm')
if 'ADC' not in G:
    a('ADC', [('A', 'Apparent'), ('D', 'Diffusion'), ('C', 'Coefficient')], 'Apparent diffusion coefficient (coefficient de diffusion apparent)', '<p>Valeur d’IRM de diffusion, basse dans le pus, qui peut aider à distinguer une ostéomyélite.</p>', 'g98-osteomyelite')
if 'PET' not in G:
    a('PET', [('P', 'Positron'), ('E', 'Emission'), ('T', 'Tomography')], 'Positron emission tomography (tomographie par émission de positons) ; PET-CT : couplée à la tomodensitométrie', '<p>Imagerie de médecine nucléaire permettant de quantifier l’inflammation.</p>', 'g98-irm')
if 'SPECT' not in G:
    a('SPECT', [('S', 'Single'), ('P', 'Photon'), ('E', 'Emission'), ('C', 'Computed'), ('T', 'Tomography')], 'Single photon emission computed tomography ; SPECT-CT : couplée à la tomodensitométrie', '<p>Imagerie de médecine nucléaire, alternative en cas d’IRM impossible.</p>', 'g98-irm')
if 'CT' not in G:
    a('CT', [('C', 'Computed'), ('T', 'Tomography')], 'Computed tomography (tomodensitométrie)', '<p>Composante tomodensitométrique de la PET-CT et de la SPECT-CT.</p>', 'g98-irm')
if 'GRADE' not in G:
    a('GRADE', [('G', 'Grading of'), ('R', 'Recommendations'), ('A', 'Assessment,'), ('D', 'Development and'), ('E', 'Evaluation')], 'Grading of Recommendations Assessment, Development and Evaluation', '<p>Méthode qui sépare la force d’une recommandation de la certitude des preuves.</p>', 'g98-cno')
if 'BfArM' not in G:
    a('BfArM', [('Bf', 'Bundesinstitut für'), ('Ar', 'Arzneimittel und'), ('M', 'Medizinprodukte')], 'Institut fédéral allemand des médicaments et des dispositifs médicaux (Bundesinstitut für Arzneimittel und Medizinprodukte)', '<p>Éditeur de la CIM-10-GM, dont la version allemande 2024 fonde la section de codage.</p>', 'g98-codage')
if 'OFS' not in G:
    a('OFS', [('O', 'Office'), ('F', 'Fédéral de la'), ('S', 'Statistique')], 'Office fédéral de la statistique', '<p>Office suisse qui publie la CIM-10-GM suisse ; son libellé français n’a pas été vérifié pour cette leçon.</p>', 'g98-codage')
if 'GM' not in G:
    a('GM', [('G', 'German'), ('M', 'Modification')], 'German Modification (modification allemande)', '<p>Désigne la CIM-10-GM, version allemande de la classification internationale.</p>', 'g98-codage')
if 'M14.6' not in G:
    a('M14.6', [('M14.6', 'code de la CIM-10-GM, non une abréviation')], 'M14.6-* : arthropathie neuropathique (code étoile)', '<p>Code de la manifestation articulaire de l’arthropathie neuropathique ; la cinquième position précise la localisation. Il s’associe à G98†, E10–E14† ou A52.1† selon la cause.</p>', 'g98-codage')
if 'A52.1' not in G:
    a('A52.1', [('A52.1', 'code de la CIM-10-GM, non une abréviation')], 'A52.1† : code croix du Charcot syphilitique (tabétique)', '<p>Code de la cause du Charcot syphilitique (tabétique) ; la manifestation articulaire se code M14.6-*.</p>', 'g98-codage')
if 'M49.4' not in G:
    a('M49.4', [('M49.4', 'code de la CIM-10-GM, non une abréviation')], 'M49.4-* : spondylopathie neuropathique', '<p>Atteinte vertébrale neuropathique, exclue de M14 ; elle se code M49.4-*.</p>', 'g98-codage')
if 'Sanders-Frykberg' not in G:
    a('Sanders-Frykberg', [('Sanders-Frykberg', 'noms propres des auteurs de la classification, non une abréviation')], 'Classification de Sanders et Frykberg', '<p>Classification en cinq zones anatomiques du pied de Charcot.</p>', 'g98-sanders')
