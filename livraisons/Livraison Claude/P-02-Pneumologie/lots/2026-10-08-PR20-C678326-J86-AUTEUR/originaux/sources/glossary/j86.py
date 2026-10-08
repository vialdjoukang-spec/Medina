from cardio_1 import a, G
# Glossaire J86 — Pleurésies purulentes et abcès du poumon (P-02-Pneumologie). Rédaction du 08.10.2026.
a('BTS', [('B', 'British'), ('T', 'Thoracic'), ('S', 'Society')], 'Société britannique de pneumologie', '<p>Société savante britannique. Sa recommandation sur les maladies pleurales, publiée dans Thorax en 2023, fixe les seuils de pH, le calibre du drain et le protocole de fibrinolyse intrapleurale utilisés dans le cours J86 — Pyothorax.</p>')
a('ESTS', [('E', 'European'), ('S', 'Society of'), ('T', 'Thoracic'), ('S', 'Surgeons')], 'Société européenne des chirurgiens thoraciques', '<p>Société savante européenne de chirurgie thoracique. Elle a publié en 2023, avec l’ERS, une déclaration sur la prise en charge de l’infection pleurale de l’adulte.</p>')
a('MIST1', [('M', 'Multicenter'), ('I', 'Intrapleural'), ('S', 'Sepsis'), ('T', 'Trial'), ('1', 'premier essai')], 'Premier essai multicentrique sur le sepsis intrapleural', '<p>Essai randomisé britannique publié en 2005 : la streptokinase intrapleurale n’a réduit ni la mortalité ni le recours chirurgical chez 454 patients atteints d’infection pleurale.</p>', 'j86-mist1')
a('MIST2', [('M', 'Multicenter'), ('I', 'Intrapleural'), ('S', 'Sepsis'), ('T', 'Trial'), ('2', 'deuxième essai')], 'Deuxième essai multicentrique sur le sepsis intrapleural', '<p>Essai randomisé factoriel publié en 2011 : l’association alteplase et dornase alfa intrapleurales a amélioré le drainage et réduit le recours chirurgical, contrairement à chaque molécule seule.</p>', 'j86-mist2')
a('RAPID', [('R', 'Renal (urée)'), ('A', 'Age'), ('P', 'Purulence du liquide'), ('I', 'Infection source (origine)'), ('D', 'Dietary factors (albumine)')], 'Score pronostique de l’infection pleurale', '<p>Score de 0 à 7 points calculé à l’admission à partir de l’urée, de l’âge, de la purulence du liquide, de l’origine communautaire ou nosocomiale et de l’albumine. Il stratifie la mortalité à trois mois.</p>', 'j86-rapid')
a('PILOT', [('PILOT', 'nom de l’étude, non développé lettre à lettre par ses auteurs')], 'Étude prospective de validation du score RAPID', '<p>Cohorte internationale de 546 adultes atteints d’infection pleurale, publiée en 2020 dans l’European Respiratory Journal. Mortalité à trois mois : 10 % ; le score RAPID la prédisait avec une statistique C de 0,78.</p>')
a('SLIM', [('S', 'Short versus'), ('L', 'Long antibiotic course for pleural'), ('I', 'Infection'), ('M', 'Management')], 'Essai comparant une antibiothérapie courte ou longue de l’infection pleurale', '<p>Essai pilote randomisé publié en 2023 (50 patients) : 14 à 21 jours contre 28 à 42 jours d’antibiotiques chez des patients médicalement stables, sans différence significative d’échec.</p>', 'j86-duree')
for code, title, d in [
    ('J85.0', 'Gangrène et nécrose du poumon', 'Nécrose pulmonaire étendue, non collectée.'),
    ('J85.1', 'Abcès du poumon avec pneumonie', 'Si l’agent de la pneumonie est précisé, celle-ci se code en J09–J16.'),
    ('J85.2', 'Abcès du poumon sans pneumonie', 'Inclut l’abcès du poumon sans autre précision.'),
    ('J85.3', 'Abcès du médiastin', 'Collection purulente médiastinale, par exemple au cours d’une médiastinite descendante.'),
    ('J86.0', 'Pyothorax avec fistule', 'Catégorie subdivisée selon l’organe en communication (J86.00 à J86.09).'),
    ('J86.00', 'Pyothorax avec fistule du parenchyme pulmonaire', 'Inclut la fistule pleuropulmonaire.'),
    ('J86.01', 'Pyothorax avec fistule de la bronche et de la trachée', 'Inclut la fistule bronchopleurale et trachéopleurale.'),
    ('J86.02', 'Pyothorax avec fistule de la paroi thoracique', 'Inclut l’empyème de nécessité et la fistule pleurocutanée.'),
    ('J86.03', 'Pyothorax avec fistule œsotrachéale', 'Exclut la fistule trachéo-œsophagienne après trachéotomie.'),
    ('J86.04', 'Pyothorax avec fistule œsopleurale', 'Communication entre l’œsophage et la plèvre.'),
    ('J86.05', 'Pyothorax avec autre fistule œsophagienne', 'Inclut les fistules œsobronchiques et œsopulmonaires.'),
    ('J86.08', 'Pyothorax avec autre fistule', 'Fistule d’un autre organe.'),
    ('J86.09', 'Pyothorax avec fistule, sans précision', 'Organe en communication non précisé.'),
    ('J86.9', 'Pyothorax sans fistule', 'Inclut l’empyème pleural, y compris chronique, sans autre précision.'),
]:
    a(code, [(code, 'code CIM-10-GM 2024')], title, '<p>' + d + ' Développé dans le cours J86 — Pyothorax (P-02-Pneumologie).</p>')
