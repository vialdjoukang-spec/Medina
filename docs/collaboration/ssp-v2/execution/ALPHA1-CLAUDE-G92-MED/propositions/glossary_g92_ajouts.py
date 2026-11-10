"""Proposition ALPHA1-CLAUDE-G92-MED : sigles nouveaux introduits par les propositions de l'audit (C01, C05, C07, C09, C22).
À ajouter à la fin de glossary/g92.py, dans le même format conditionnel. Références [Sx] : sources.json du dossier."""
if '4AT' not in G:
    a('4AT', [('4', 'quatre'), ('A', 'items commençant par « A » : Alertness, AMT4, Attention, Acute change'), ('T', 'Test')], 'Test des quatre A', '<p>Outil de dépistage du délire en quatre items, noté de 0 à 12 ; un score de 4 ou plus suggère un délire [S25]. Chez les 65 ans et plus, sensibilité et spécificité de 0,88 [S24].</p>', 'g92-sm-4at')
if 'AMT4' not in G:
    a('AMT4', [('A', 'Abbreviated'), ('M', 'Mental'), ('T', 'Test'), ('4', 'quatre questions')], 'Test mental abrégé en quatre questions', '<p>Âge, date de naissance, lieu et année ; deuxième item du 4AT [S25].</p>', 'g92-sm-4at')
if 'CYP3A4' not in G:
    a('CYP3A4', [('CYP', 'CYtochrome P450'), ('3', 'famille 3'), ('A', 'sous-famille A'), ('4', 'isoenzyme 4')], 'Cytochrome P450 3A4', '<p>Enzyme hépatique ; son inhibition augmente la formation d’un métabolite neurotoxique de l’ifosfamide [S7].</p>', 'g92-ifosfamide')
if 'EAN' not in G:
    a('EAN', [('E', 'European'), ('A', 'Academy of'), ('N', 'Neurology')], 'Académie européenne de neurologie', '<p>Société européenne dont la ligne directrice de 2020 sur le diagnostic du coma conseille le score FOUR en phase aiguë [S26].</p>', 'g92-sm-vigilance')
if 'EBMT' not in G:
    a('EBMT', [('E', 'European Society for'), ('B', 'Blood and'), ('M', 'Marrow'), ('T', 'Transplantation')], 'Société européenne de transplantation de sang et de moelle', '<p>Société européenne dont le manuel des CAR-T est repris par la revue européenne de 2026 [S2].</p>')
if 'EHA' not in G:
    a('EHA', [('E', 'European'), ('H', 'Hematology'), ('A', 'Association')], 'Association européenne d’hématologie', '<p>Société européenne co-auteure, avec l’EBMT, du manuel des CAR-T [S2].</p>')
if 'FOUR' not in G:
    a('FOUR', [('F', 'Full'), ('O', 'Outline of'), ('U', 'UnResponsiveness'), ('R', 'score')], 'Échelle FOUR de non-réactivité', '<p>Échelle de coma préférée à l’échelle de Glasgow en phase aiguë par la ligne directrice de l’EAN [S26].</p>', 'g92-sm-vigilance')
if 'LDGCB' not in G:
    a('LDGCB', [('L', 'Lymphome'), ('D', 'Diffus à'), ('G', 'Grandes'), ('C', 'Cellules'), ('B', 'B')], 'Lymphome diffus à grandes cellules B', '<p>Indication de Yescarta ; taux d’œdème cérébral signalé de 0,7 % avec les autres indications [S4].</p>', 'g92-sm-htic')
if 'LMPGB' not in G:
    a('LMPGB', [('L', 'Lymphome'), ('M', 'Médiastinal'), ('P', 'Primitif à'), ('G', 'Grandes cellules'), ('B', 'B')], 'Lymphome médiastinal primitif à grandes cellules B', '<p>Indication de Yescarta où l’œdème cérébral signalé atteint 1,6 %, dont 0,8 % mortel [S4].</p>', 'g92-sm-htic')
