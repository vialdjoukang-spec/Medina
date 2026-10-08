from cardio_1 import a, G
# Glossaire du cours J96 — Insuffisance respiratoire aiguë et chronique (P-02-Pneumologie).
# Clés nouvelles uniquement : PaO₂, PaCO₂, SpO₂, FiO₂, VNI, BPCO, GOLD, ERS, ATS, HOT-HMV, NOTT, LOTT,
# MiGeL, NEWS2, EtCO₂, CaO₂, DO₂, HCO₃⁻, kPa et pH existent déjà dans d’autres fichiers et ne sont pas redéfinies.

for code, title, d in [
    ('J96.0', 'Insuffisance respiratoire aiguë, non classée ailleurs',
     '<p>Catégorie CIM-10-GM 2024 de l’insuffisance respiratoire installée en heures ou en jours. Une insuffisance chronique préexistante se code en plus par J96.1.</p>'),
    ('J96.1', 'Insuffisance respiratoire chronique, non classée ailleurs',
     '<p>Catégorie CIM-10-GM 2024 de l’insuffisance respiratoire installée en mois ou en années, souvent compensée sur le plan acido-basique.</p>'),
    ('J96.9', 'Insuffisance respiratoire, sans précision',
     '<p>Catégorie CIM-10-GM 2024 employée lorsque la temporalité n’est pas documentée. Elle exprime un manque de précision du dossier, non une forme clinique.</p>'),
    ('J96.00', 'Insuffisance respiratoire aiguë, type I (hypoxémique)',
     '<p>Cinquième caractère 0 : hypoxémie sans hypercapnie.</p>'),
    ('J96.01', 'Insuffisance respiratoire aiguë, type II (hypercapnique)',
     '<p>Cinquième caractère 1 : hypercapnie, avec ou sans hypoxémie associée.</p>'),
    ('J96.09', 'Insuffisance respiratoire aiguë, type non précisé',
     '<p>Cinquième caractère 9 : le type gazométrique n’est pas documenté.</p>'),
    ('J96.10', 'Insuffisance respiratoire chronique, type I (hypoxémique)',
     '<p>Cinquième caractère 0 : hypoxémie chronique sans hypercapnie.</p>'),
    ('J96.11', 'Insuffisance respiratoire chronique, type II (hypercapnique)',
     '<p>Cinquième caractère 1 : hypercapnie chronique, avec ou sans hypoxémie.</p>'),
    ('J96.19', 'Insuffisance respiratoire chronique, type non précisé',
     '<p>Cinquième caractère 9 : type gazométrique non documenté.</p>'),
]:
    a(code, [(code, 'code CIM-10-GM 2024')], title, d)

a('R09.2', [('R09.2', 'code CIM-10-GM 2024')], 'Arrêt respiratoire',
  '<p>Code exclu de J96 : l’arrêt respiratoire et l’insuffisance cardiopulmonaire se codent en R09.2.</p>')
a('Z99.1', [('Z99.1', 'code CIM-10-GM 2024')], 'Dépendance envers un respirateur',
  '<p>Code supplémentaire de J96.1 lorsque la respiration nécessite durablement un respirateur, par exemple une ventilation à domicile.</p>')

a('BTS', [('B', 'British'), ('T', 'Thoracic'), ('S', 'Society')], 'Société thoracique britannique',
  '<p>Société savante britannique de pneumologie. Elle a publié la recommandation de 2017 sur l’oxygène en situation aiguë et, avec l’Intensive Care Society, celle de 2016 sur la ventilation de l’insuffisance respiratoire hypercapnique.</p>')
a('PAO₂', [('P', 'Pression partielle'), ('A', 'Alvéolaire (A majuscule)'), ('O₂', 'en dioxygène')], 'Pression alvéolaire en oxygène',
  '<p>Pression d’oxygène dans le gaz alvéolaire, calculée par l’équation des gaz alvéolaires ; environ 100 mmHg à l’air ambiant au niveau de la mer. Le A majuscule la distingue de la PaO₂ artérielle (a minuscule).</p>', 'j96-equation-alveolaire')
a('PvCO₂', [('P', 'Pression partielle'), ('v', 'veineuse'), ('CO₂', 'en dioxyde de carbone')], 'Pression veineuse en dioxyde de carbone',
  '<p>Mesurée sur une gazométrie veineuse. Elle est en moyenne un peu plus élevée que la PaCO₂ ; une valeur normale rend une hypercapnie artérielle peu probable, une valeur élevée doit être confirmée sur sang artériel.</p>', 'j96-gaz-veineux')
a('PtcCO₂', [('P', 'Pression partielle'), ('tc', 'transcutanée'), ('CO₂', 'en dioxyde de carbone')], 'Pression transcutanée en dioxyde de carbone',
  '<p>Estimation continue et non invasive de la PaCO₂ par une électrode chauffée posée sur la peau. Elle sert surtout à suivre une tendance, notamment pendant le sommeil.</p>', 'j96-transcutane')
a('COHb', [('CO', 'monoxyde de carbone (Carbon monOxide)'), ('Hb', 'lié à l’hémoglobine')], 'Carboxyhémoglobine',
  '<p>Hémoglobine liée au monoxyde de carbone, qui ne transporte plus l’oxygène. L’oxymètre de pouls la confond avec l’oxyhémoglobine ; seule la co-oxymétrie la mesure.</p>', 'j96-cooxymetrie')
a('MetHb', [('Met', 'Méthémoglobine : fer ferrique'), ('Hb', 'Hémoglobine')], 'Méthémoglobine',
  '<p>Hémoglobine dont le fer est oxydé à l’état ferrique, incapable de fixer l’oxygène. Elle fausse l’oxymétrie de pouls et se mesure par co-oxymétrie.</p>', 'j96-cooxymetrie')
a('P50', [('P', 'Pression partielle en oxygène'), ('50', 'à laquelle l’hémoglobine est saturée à 50 %')], 'Pression de demi-saturation de l’hémoglobine',
  '<p>Environ 27 mmHg chez l’adulte dans les conditions standard. Une P50 plus élevée traduit un déplacement de la courbe de dissociation vers la droite et une libération facilitée de l’oxygène aux tissus.</p>')
a('PImax', [('P', 'Pression'), ('I', 'Inspiratoire'), ('max', 'maximale')], 'Pression inspiratoire maximale',
  '<p>Pression négative mesurée à la bouche pendant un effort inspiratoire maximal contre une valve fermée. Elle évalue la force des muscles inspiratoires.</p>', 'j96-pression-muscles')
a('SNIP', [('S', 'Sniff'), ('N', 'Nasal'), ('I', 'Inspiratory'), ('P', 'Pressure')], 'Pression nasale inspiratoire au reniflement',
  '<p>Pression mesurée dans une narine pendant un reniflement bref et maximal. Elle complète la PImax lorsque l’étanchéité buccale est mauvaise, par exemple en cas d’atteinte bulbaire.</p>', 'j96-pression-muscles')
a('IPAP', [('I', 'Inspiratory'), ('P', 'Positive'), ('A', 'Airway'), ('P', 'Pressure')], 'Pression positive inspiratoire',
  '<p>Pression délivrée par le ventilateur pendant l’inspiration en ventilation non invasive à deux niveaux de pression. La différence IPAP − EPAP constitue l’aide inspiratoire qui augmente le volume courant.</p>', 'j96-vni-principe')
a('EPAP', [('E', 'Expiratory'), ('P', 'Positive'), ('A', 'Airway'), ('P', 'Pressure')], 'Pression positive expiratoire',
  '<p>Pression maintenue pendant l’expiration en ventilation non invasive. Elle évacue le dioxyde de carbone expiré du circuit, maintient les voies aériennes supérieures ouvertes et recrute des alvéoles.</p>', 'j96-vni-principe')
a('CPAP', [('C', 'Continuous'), ('P', 'Positive'), ('A', 'Airway'), ('P', 'Pressure')], 'Pression positive continue',
  '<p>Pression positive identique pendant tout le cycle respiratoire. Elle n’apporte pas d’aide inspiratoire : elle recrute des alvéoles et lève une obstruction des voies aériennes supérieures.</p>', 'j96-vni-principe')
a('ROX', [('R', 'Respiratory rate (fréquence respiratoire)'), ('OX', 'OXygenation (oxygénation)')], 'Indice ROX',
  '<p>Rapport (SpO₂/FiO₂) / fréquence respiratoire, calculé sous oxygène nasal à haut débit. Une valeur ≥ 4,88 est associée à un moindre risque d’intubation (Roca, 2019).</p>', 'j96-rox')
a('HACOR', [('H', 'Heart rate (fréquence cardiaque)'), ('A', 'Acidosis (acidose)'), ('C', 'Consciousness (conscience)'), ('O', 'Oxygenation (oxygénation)'), ('R', 'Respiratory rate (fréquence respiratoire)')], 'Score HACOR',
  '<p>Score composite calculé sous ventilation non invasive dans l’insuffisance respiratoire hypoxémique ; un score élevé après une heure prédit l’échec de la ventilation non invasive.</p>', 'j96-vni-echec')
a('RESCUE', [('RESCUE', 'nom propre de l’essai, non développable lettre à lettre')], 'Essai RESCUE (2014)',
  '<p>Essai néerlandais : ventilation non invasive à domicile débutée 48 heures après une exacerbation hypercapnique de BPCO, sans bénéfice à un an sur la survie, les réadmissions ou la qualité de vie.</p>', 'j96-vni-domicile-bpco')
a('FLORALI', [('FLORALI', 'nom propre de l’essai, non développable lettre à lettre')], 'Essai FLORALI (2015)',
  '<p>Essai français chez 310 patients en insuffisance respiratoire aiguë hypoxémique non hypercapnique : oxygène nasal à haut débit, oxygène standard ou ventilation non invasive. Taux d’intubation non différent ; mortalité à 90 jours plus faible sous haut débit.</p>', 'j96-haut-debit')
a('IOTA', [('I', 'Improving'), ('O', 'Oxygen'), ('T', 'Therapy in'), ('A', 'Acute-illness')], 'Méta-analyse IOTA (2018)',
  '<p>Méta-analyse de 25 essais et 16 037 adultes en situation aiguë : la stratégie libérale d’oxygène augmente la mortalité hospitalière (risque relatif 1,21) par rapport à une stratégie conservatrice.</p>', 'j96-cibles')
