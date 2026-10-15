"""Abréviations G80 (Infirmité motrice cérébrale) ; module autonome, sans mutation des glossaires existants."""
G = {}
def a(k, lit, full, d='', ref=None):
    G[k] = {'lit': [list(x) for x in lit], 'full': full, 'def': d, 'ref': ref}

a('PC', [('P', 'Paralysie'), ('C', 'Cérébrale')], 'Paralysie cérébrale',
  '<p>Groupe de troubles permanents du mouvement et de la posture, attribués à une perturbation non progressive du cerveau fœtal ou du nourrisson en développement (définition internationale d’avril 2006). Synonyme de la catégorie « infirmité motrice cérébrale » de la classification suisse.</p>', 'g80-definition')
a('SCPE', [('S', 'Surveillance'), ('C', 'of Cerebral'), ('P', 'Palsy'), ('E', 'in Europe')], 'Surveillance of Cerebral Palsy in Europe (Surveillance de la paralysie cérébrale en Europe)',
  '<p>Réseau européen de registres qui a établi la classification actuelle des types de paralysie cérébrale : spastique, dyskinétique, ataxique.</p>', 'g80-scpe')
a('GMFCS', [('G', 'Gross'), ('M', 'Motor'), ('F', 'Function'), ('C', 'Classification'), ('S', 'System')], 'Gross Motor Function Classification System (Système de classification de la fonction motrice globale)',
  '<p>Classification en cinq niveaux, de I (marche sans restriction) à V (déplacé en fauteuil par un tiers), par tranches d’âge ; valide et fiable dès 2 ans.</p>', 'g80-gmfcs')
a('GMFM', [('G', 'Gross'), ('M', 'Motor'), ('F', 'Function'), ('M', 'Measure')], 'Gross Motor Function Measure (Mesure de la fonction motrice globale)',
  '<p>Échelle de mesure de la fonction motrice dont les courbes sont citées avec le GMFCS dans le consensus européen sur la toxine botulique de 2009.</p>', 'g80-consensus')
a('MACS', [('M', 'Manual'), ('A', 'Ability'), ('C', 'Classification'), ('S', 'System')], 'Manual Ability Classification System (Système de classification de la capacité manuelle)',
  '<p>Classification de la fonction manuelle ; ses niveaux n’ont pas été lus pour ce cours.</p>', 'g80-macs')
a('MRICS', [('M', 'Magnetic'), ('R', 'Resonance'), ('I', 'Imaging'), ('C', 'Classification'), ('S', 'System')], 'Magnetic Resonance Imaging Classification System (Classification de l’imagerie par résonance magnétique du réseau SCPE)',
  '<p>Cinq groupes : A malformations, B substance blanche, C substance grise, D divers, E normale.</p>', 'g80-mrics')
a('IRM', [('I', 'Imagerie'), ('R', 'par Résonance'), ('M', 'Magnétique')], 'Imagerie par résonance magnétique',
  '<p>Examen d’imagerie préféré pour caractériser la lésion cérébrale ; sensibilité de 86 à 89 % pour le diagnostic précoce de paralysie cérébrale.</p>', 'g80-irm')
a('HINE', [('H', 'Hammersmith'), ('I', 'Infant'), ('N', 'Neurological'), ('E', 'Examination')], 'Hammersmith Infant Neurological Examination (Examen neurologique du nourrisson de Hammersmith)',
  '<p>Examen neurologique standardisé du nourrisson, de sensibilité 90 % pour le diagnostic précoce.</p>', 'g80-hine')
a('DAYC', [('D', 'Developmental'), ('A', 'Assessment'), ('Y', 'of Young'), ('C', 'Children')], 'Developmental Assessment of Young Children (Évaluation du développement du jeune enfant)',
  '<p>Échelle du développement ; l’indice C a une sensibilité de 83 % après 5 mois.</p>', 'g80-dayc')
a('CIM', [('C', 'Classification'), ('I', 'Internationale des'), ('M', 'Maladies')], 'Classification internationale des maladies',
  '<p>Classification dont la dixième révision, adaptation allemande, fixe les codes G80.0 à G80.9.</p>', 'g80-cim')
a('SA', [('S', 'Semaines'), ('A', 'd’Aménorrhée')], 'Semaines d’aménorrhée',
  '<p>Unité d’âge gestationnel comptée depuis le début des dernières règles ; une naissance avant 37 SA est prématurée.</p>')
a('CIM-10-GM', [('CIM', 'Classification Internationale des Maladies'), ('10', 'dixième révision'), ('GM', 'German Modification (adaptation allemande)')], 'Classification internationale des maladies, 10e révision, modification allemande',
  '<p>Version 2024 utilisée en Suisse pour le catalogue des diagnostics.</p>', 'g80-cim')
a('SNV', [('S', 'Single'), ('N', 'Nucleotide'), ('V', 'Variant')], 'Single nucleotide variant (variant d’un seul nucléotide)',
  '<p>Variant ponctuel de l’ADN, décrit comme cause génétique de la paralysie cérébrale.</p>', 'g80-genetique')
a('CNV', [('C', 'Copy'), ('N', 'Number'), ('V', 'Variation')], 'Copy number variation (variation du nombre de copies)',
  '<p>Perte ou gain d’un segment d’ADN, décrit comme cause génétique de la paralysie cérébrale.</p>', 'g80-genetique')
a('ADN', [('A', 'Acide'), ('D', 'Désoxyribo'), ('N', 'Nucléique')], 'Acide désoxyribonucléique',
  '<p>Support de l’information génétique ; la puce ADN recherche des variants structuraux.</p>', 'g80-genetique')
a('EEG', [('E', 'Électro'), ('E', 'Encéphalo'), ('G', 'Gramme')], 'Électroencéphalogramme',
  '<p>Enregistrement de l’activité électrique cérébrale, utilisé en cas de suspicion de crises.</p>')
a('GABA', [('G', 'Gamma'), ('A', 'Amino'), ('B', 'Butyric'), ('A', 'Acid (acide gamma-aminobutyrique)')], 'Acide gamma-aminobutyrique',
  '<p>Médiateur inhibiteur du système nerveux central. Le baclofène stimule ses récepteurs de type B dans la moelle.</p>', 'g80-baclofene-oral')
a('QI', [('Q', 'Quotient'), ('I', 'Intellectuel')], 'Quotient intellectuel',
  '<p>Mesure du niveau cognitif ; plus bas lorsque le niveau GMFCS est plus élevé dans le registre suisse.</p>')
a('Swiss-CP-Reg', [('Swiss', 'suisse'), ('CP', 'Cerebral Palsy (paralysie cérébrale)'), ('Reg', 'Registry (registre)')], 'Swiss Cerebral Palsy Registry (registre suisse de la paralysie cérébrale)',
  '<p>Registre fondé en 2017, non exhaustif.</p>', 'g80-swisscpreg')
a('NG62', [('NG', 'NICE Guideline (recommandation du NICE)'), ('62', 'numéro de la recommandation')], 'Recommandation britannique numéro 62 sur la paralysie cérébrale',
  '<p>Document non lu pour ce cours (accès refusé).</p>', 'g80-lacunes')
a('BfArM', [('Bf', 'Bundesinstitut für'), ('Ar', 'Arzneimittel'), ('M', 'und Medizinprodukte')], 'Bundesinstitut für Arzneimittel und Medizinprodukte (Institut fédéral allemand des médicaments et dispositifs médicaux)',
  '<p>Éditeur de la CIM-10-GM.</p>', 'g80-cim')
a('JAMA', [('J', 'Journal'), ('A', 'of the American'), ('M', 'Medical'), ('A', 'Association')], 'Journal of the American Medical Association',
  '<p>Revue médicale ayant publié la revue systématique de 2017 sur le diagnostic précoce.</p>')
a('BMC', [('B', 'Bio'), ('M', 'Med'), ('C', 'Central')], 'BioMed Central',
  '<p>Éditeur de la revue ayant publié l’étude sur le déplacement de hanche.</p>')
a('G80.0', [('G80.0', 'code CIM-10-GM : Paralysie cérébrale spastique quadriplégique')], 'Paralysie cérébrale spastique quadriplégique',
  '<p>Sous-code de la catégorie G80 de la CIM-10-GM 2024.</p>', 'g80-cim')
a('G80.1', [('G80.1', 'code CIM-10-GM : Paralysie cérébrale spastique diplégique')], 'Paralysie cérébrale spastique diplégique',
  '<p>Sous-code de la catégorie G80 de la CIM-10-GM 2024.</p>', 'g80-cim')
a('G80.2', [('G80.2', 'code CIM-10-GM : Infirmité motrice cérébrale, forme spastique hémiplégique')], 'Infirmité motrice cérébrale, forme spastique hémiplégique',
  '<p>Sous-code de la catégorie G80 de la CIM-10-GM 2024.</p>', 'g80-cim')
a('G80.3', [('G80.3', 'code CIM-10-GM : Paralysie cérébrale dyskinétique')], 'Paralysie cérébrale dyskinétique',
  '<p>Sous-code de la catégorie G80 de la CIM-10-GM 2024.</p>', 'g80-cim')
a('G80.4', [('G80.4', 'code CIM-10-GM : Paralysie cérébrale ataxique')], 'Paralysie cérébrale ataxique',
  '<p>Sous-code de la catégorie G80 de la CIM-10-GM 2024.</p>', 'g80-cim')
a('G80.8', [('G80.8', 'code CIM-10-GM : Autres infirmités motrices cérébrales')], 'Autres infirmités motrices cérébrales',
  '<p>Sous-code de la catégorie G80 de la CIM-10-GM 2024.</p>', 'g80-cim')
a('G80.9', [('G80.9', 'code CIM-10-GM : Paralysie cérébrale, sans précision')], 'Paralysie cérébrale, sans précision',
  '<p>Sous-code de la catégorie G80 de la CIM-10-GM 2024.</p>', 'g80-cim')
a('G11.4', [('G11.4', 'code CIM-10-GM de la paraplégie spastique héréditaire')], 'Paraplégie spastique héréditaire',
  '<p>Exclue de la catégorie G80.</p>', 'g80-g114')
