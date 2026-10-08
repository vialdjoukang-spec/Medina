from cardio_1 import a, G
# Glossaire du cours J85 — Abcès du poumon et du médiastin, gangrène pulmonaire et pyothorax (P-02-Pneumologie)
for c, t in [
    ('J85.0', 'Gangrène et nécrose du poumon'),
    ('J85.1', 'Abcès du poumon avec pneumonie'),
    ('J85.2', 'Abcès du poumon sans pneumonie'),
    ('J85.3', 'Abcès du médiastin'),
    ('J86.0', 'Pyothorax avec fistule'),
    ('J86.00', 'Pyothorax avec fistule du parenchyme pulmonaire'),
    ('J86.01', 'Pyothorax avec fistule des bronches et de la trachée'),
    ('J86.02', 'Pyothorax avec fistule de la paroi thoracique'),
    ('J86.03', 'Pyothorax avec fistule œsotrachéale'),
    ('J86.04', 'Pyothorax avec fistule œsopleurale'),
    ('J86.05', 'Pyothorax avec autre fistule œsophagienne'),
    ('J86.08', 'Pyothorax avec autre fistule'),
    ('J86.09', 'Pyothorax avec fistule, sans précision'),
    ('J86.9', 'Pyothorax sans fistule'),
    ('J98.50', 'Médiastinite'),
]:
    a(c, [(c, 'code de la Classification internationale des maladies, 10e révision, modification allemande')], t,
      '<p>Code CIM-10-GM 2024 (BfArM), vérifié le 08.10.2026.</p>')
a('VATS', [('V', 'Video-'), ('A', 'Assisted (assistée)'), ('T', 'Thoracoscopic (thoracoscopique)'), ('S', 'Surgery (chirurgie)')],
  'Chirurgie thoracique vidéo-assistée',
  '<p>Chirurgie du thorax réalisée par une à trois petites incisions, avec une caméra et des instruments longs. Dans l’empyème, elle permet de débrider la cavité pleurale et de libérer le poumon, avec moins de douleur et une hospitalisation plus courte que la thoracotomie.</p>', 'j85-vats')
a('MIST1', [('M', 'Multicenter (multicentrique)'), ('I', 'Intrapleural (intrapleural)'), ('S', 'Sepsis (sepsis)'), ('T', 'Trial (essai)'), ('1', 'premier essai')],
  'Premier essai multicentrique sur le sepsis intrapleural (2005)',
  '<p>Essai britannique de 454 patients : la streptokinase intrapleurale n’a réduit ni la mortalité ni le recours à la chirurgie dans l’infection pleurale (New England Journal of Medicine, 2005).</p>', 'j85-mist1')
a('MIST2', [('M', 'Multicenter (multicentrique)'), ('I', 'Intrapleural (intrapleural)'), ('S', 'Sepsis (sepsis)'), ('T', 'Trial (essai)'), ('2', 'deuxième essai')],
  'Deuxième essai multicentrique sur le sepsis intrapleural (2011)',
  '<p>Essai factoriel de 210 patients : l’association intrapleurale d’altéplase et de dornase alfa a amélioré le drainage, réduit le recours à la chirurgie et la durée d’hospitalisation ; chaque agent seul était inefficace (New England Journal of Medicine, 2011).</p>', 'j85-mist2')
a('MIST-3', [('M', 'Multicenter (multicentrique)'), ('I', 'Intrapleural (intrapleural)'), ('S', 'Sepsis (sepsis)'), ('T', 'Trial (essai)'), ('3', 'troisième essai')],
  'Troisième essai multicentrique sur le sepsis intrapleural',
  '<p>Essai de faisabilité qui a comparé, chez l’adulte atteint d’infection pleurale, une chirurgie thoracique vidéo-assistée précoce ou des enzymes intrapleuraux précoces au traitement habituel. Il suggère une hospitalisation plus courte, sans constituer une preuve définitive.</p>')
a('RAPID', [('R', 'Renal (rénal : urée sérique)'), ('A', 'Age (âge)'), ('P', 'Purulence (purulence du liquide pleural)'), ('I', 'Infection source (origine communautaire ou nosocomiale)'), ('D', 'Dietary factors (facteur nutritionnel : albumine)')],
  'Score pronostique RAPID de l’infection pleurale',
  '<p>Score de 0 à 7 calculé à l’admission (Rahman, Chest, 2014). Risque faible de 0 à 2, intermédiaire de 3 à 4, élevé de 5 à 7 ; mortalité à trois mois de 2,3 %, 9,2 % et 29,3 % dans la cohorte prospective de validation (Corcoran, 2020).</p>', 'j90-rapid')
a('BTS', [('B', 'British'), ('T', 'Thoracic'), ('S', 'Society')], 'British Thoracic Society (Société thoracique britannique)',
  '<p>Société savante britannique de pneumologie. Sa guideline sur les maladies pleurales (Thorax, août 2023) traite notamment de l’infection pleurale.</p>')
a('ESTS', [('E', 'European'), ('S', 'Society of'), ('T', 'Thoracic'), ('S', 'Surgeons')], 'European Society of Thoracic Surgeons (Société européenne des chirurgiens thoraciques)',
  '<p>Société savante européenne de chirurgie thoracique ; coautrice avec l’ERS de la déclaration de 2023 sur la prise en charge de l’infection pleurale de l’adulte.</p>')
