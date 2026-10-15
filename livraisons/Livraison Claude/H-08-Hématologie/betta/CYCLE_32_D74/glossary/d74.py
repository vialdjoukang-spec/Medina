from cardio_1 import a, G
# D74 — Méthémoglobinémie (H-08-Hématologie). Entrées conditionnelles : aucun terme existant dans G n’est écrasé.
if 'EHA' not in G:
    a('EHA', [('E', 'European'), ('H', 'Hematology'), ('A', 'Association')], 'European Hematology Association (Association européenne d’hématologie)', '<p>Société savante européenne d’hématologie. Avec EuroBloodNet, elle a publié en 2021 le consensus sur le diagnostic et le traitement de la méthémoglobinémie qui sert de source principale à ce chapitre.</p>', 'd74-sources')
if 'EuroBloodNet' not in G:
    a('EuroBloodNet', [('EuroBloodNet', 'nom propre du réseau européen de référence pour les maladies hématologiques rares ; non développable lettre à lettre')], 'EuroBloodNet — réseau européen de référence en maladies hématologiques rares', '<p>Réseau coauteur, avec l’EHA, du consensus européen de 2021 sur la méthémoglobinémie.</p>', 'd74-sources')
if 'Vigilance-News' not in G:
    a('Vigilance-News', [('Vigilance-News', 'nom de la publication de Swissmedic ; non développable lettre à lettre')], 'Vigilance-News — bulletin de pharmacovigilance de Swissmedic', '<p>Bulletin de l’autorité suisse des produits thérapeutiques. Le numéro de juin 2011 traite de la méthémoglobinémie induite par la prilocaïne et la lidocaïne.</p>', 'd74-seuils')
if 'HFR' not in G:
    a('HFR', [('H', 'Hôpital'), ('F', 'FRibourgeois')], 'Hôpital fribourgeois', '<p>Hôpital cantonal de Fribourg. Son service a publié en 2025 le cas d’un patient intoxiqué par un nitrite d’alkyle, utilisé dans ce chapitre.</p>', 'd74-poppers')
if 'SpO2' not in G:
    a('SpO2', [('S', 'Saturation'), ('p', 'pulsée'), ('O2', 'en oxygène')], 'Saturation pulsée en oxygène', '<p>Saturation de l’hémoglobine en oxygène estimée par le pulsoxymètre au doigt. En présence de méthémoglobine, la valeur affichée se bloque vers 85 % et ne reflète pas le taux réel.</p>', 'd74-pulsoxymetrie')
if 'PaO2' not in G:
    a('PaO2', [('P', 'Pression partielle'), ('a', 'artérielle'), ('O2', 'en oxygène')], 'Pression partielle artérielle en oxygène', '<p>Mesure de l’oxygène dissous dans le sang artériel. Elle reste normale ou élevée dans la méthémoglobinémie, ce qui produit le saturation gap.</p>', 'd74-saturation-gap')
if 'CIM' not in G:
    a('CIM', [('C', 'Classification'), ('I', 'Internationale des'), ('M', 'Maladies')], 'Classification internationale des maladies', '<p>Classification de l’Organisation mondiale de la santé. Ce chapitre suit la CIM-10-GM 2024 (modification allemande), utilisée pour le catalogue du projet.</p>', 'd74-codes')
if 'CYB5R' not in G:
    a('CYB5R', [('CY', 'CYtochrome'), ('B5', 'b5'), ('R', 'Réductase')], 'NADH-cytochrome b5 réductase (diaphorase NADH)', '<p>Enzyme de la voie principale de réduction de la méthémoglobine ; son déficit héréditaire cause les types I et II.</p>', 'd74-cyb5r')
if 'CYB5R3' not in G:
    a('CYB5R3', [('CY', 'CYtochrome'), ('B5', 'b5'), ('R', 'Réductase'), ('3', 'isoforme 3')], 'Gène de la NADH-cytochrome b5 réductase', '<p>Gène dont les variants biallèliques récessifs causent les types I et II de méthémoglobinémie héréditaire ; plus de 80 variants sont rapportés.</p>', 'd74-types')
if 'CYB5A' not in G:
    a('CYB5A', [('CY', 'CYtochrome'), ('B5', 'b5'), ('A', 'type A')], 'Gène du cytochrome b5 de type A', '<p>Gène en cause dans le type IV : déficit en cytochrome b5 avec déficit isolé en 17,20-lyase et ambiguïté génitale chez un sujet 46,XY.</p>', 'd74-types')
if 'HPLC' not in G:
    a('HPLC', [('H', 'High'), ('P', 'Performance'), ('L', 'Liquid'), ('C', 'Chromatography (chromatographie liquide à haute performance)')], 'Chromatographie liquide à haute performance', '<p>Technique qui sépare les variants d’hémoglobine ; anormale dans l’hémoglobine M, normale dans les déficits en réductase.</p>', 'd74-hbm')
if 'XY' not in G:
    a('XY', [('X', 'chromosome X'), ('Y', 'chromosome Y')], 'Formule chromosomique masculine', '<p>Dans « 46,XY », 46 chromosomes dont un X et un Y. Le type IV de méthémoglobinémie s’accompagne chez ces sujets d’organes génitaux ambigus.</p>', 'd74-types')
if 'HBA1' not in G:
    a('HBA1', [('HB', 'Hémoglobine'), ('A1', 'alpha 1')], 'Gène de la chaîne alpha 1 de l’hémoglobine', '<p>Gène de globine dont des variants dominants causent une hémoglobine M avec cyanose dès la naissance.</p>', 'd74-hbm')
if 'HBA2' not in G:
    a('HBA2', [('HB', 'Hémoglobine'), ('A2', 'alpha 2')], 'Gène de la chaîne alpha 2 de l’hémoglobine', '<p>Gène de globine dont des variants dominants causent une hémoglobine M.</p>', 'd74-hbm')
if 'HBB' not in G:
    a('HBB', [('HB', 'Hémoglobine'), ('B', 'bêta')], 'Gène de la chaîne bêta de l’hémoglobine', '<p>Gène de globine dont des variants dominants causent une hémoglobine M avec cyanose après 6 à 9 mois.</p>', 'd74-hbm')
if 'HBG1' not in G:
    a('HBG1', [('HB', 'Hémoglobine'), ('G1', 'gamma 1')], 'Gène de la chaîne gamma 1 de l’hémoglobine', '<p>Gène de globine fœtale cité parmi les gènes de l’hémoglobine M.</p>', 'd74-hbm')
if 'HBG2' not in G:
    a('HBG2', [('HB', 'Hémoglobine'), ('G2', 'gamma 2')], 'Gène de la chaîne gamma 2 de l’hémoglobine', '<p>Gène de globine fœtale cité parmi les gènes de l’hémoglobine M.</p>', 'd74-hbm')
if 'MATE' not in G:
    a('MATE', [('M', 'Multidrug'), ('A', 'And'), ('T', 'Toxin'), ('E', 'Extrusion')], 'Protéines d’extrusion des médicaments et des toxines', '<p>Transporteurs rénaux, inhibés comme OCT2 par le bleu de méthylène ; l’exposition à la metformine, à l’aciclovir ou à la cimétidine peut augmenter.</p>')
if 'DSD' not in G:
    a('DSD', [('D', 'Differences (différences)'), ('S', 'of Sex'), ('D', 'Development (du développement sexuel)')], 'Anomalie du développement sexuel', '<p>Le type IV de méthémoglobinémie héréditaire s’accompagne d’une anomalie du développement sexuel 46,XY avec organes génitaux ambigus.</p>', 'd74-types')
for code, lib in (('D74.0','congénitale'),('D74.8','autres méthémoglobinémies'),('D74.9','sans précision')):
    if code not in G:
        a(code, [(code, 'code de la CIM-10-GM 2024 : catégorie D74, sous-code ' + code[-1])], 'Méthémoglobinémie, ' + lib, '<p>Sous-code de la catégorie D74 de la CIM-10-GM 2024. Voir la fenêtre sur les codes.</p>', 'd74-codes')
