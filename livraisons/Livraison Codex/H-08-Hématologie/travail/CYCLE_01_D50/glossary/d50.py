from cardio_1 import a, G
# D50 — Anémie par carence en fer (H-08-Hématologie). Entrées conditionnelles : aucun terme existant dans G n’est écrasé.
if 'TCMH' not in G:
    a('TCMH', [('T', 'Teneur'), ('C', 'Corpusculaire'), ('M', 'Moyenne'), ('H', 'en Hémoglobine')], 'Teneur corpusculaire moyenne en hémoglobine', '<p>La TCMH mesure la quantité moyenne d’hémoglobine par hématie, exprimée en picogrammes. Viollier donne 26–34 pg dès 19 ans ; Onkopedia 2025 utilise un seuil d’hypochromie de 28 pg dans ses méthodes. Référence et seuil ne sont pas interchangeables. Elle est plus fiable que le volume globulaire moyen pour repérer une carence martiale, car elle dépend moins du délai d’analyse et de l’automate (BSG 2021).</p>', 'd50-teneur-globulaire')
if 'TSAT' not in G:
    a('TSAT', [('T', 'Transferrine'), ('SAT', 'SATuration')], 'Saturation de la transferrine', '<p>La TSAT rapporte le fer sérique à la capacité totale de fixation de la transferrine, en pour cent. Une valeur inférieure à 20 % soutient une disponibilité insuffisante du fer, pour l’érythropoïèse selon le contexte, que les réserves soient vides ou séquestrées par l’inflammation. L’abréviation vient de l’anglais transferrin saturation.</p>', 'd50-tsat')
if 'MICI' not in G:
    a('MICI', [('M', 'Maladies'), ('I', 'Inflammatoires'), ('C', 'Chroniques de l’'), ('I', 'Intestin')], 'Maladies inflammatoires chroniques de l’intestin', '<p>Les maladies inflammatoires chroniques de l’intestin regroupent la maladie de Crohn et la rectocolite hémorragique. L’anémie, mêlant pertes sanguines, malabsorption et inflammation, en est la complication systémique la plus fréquente.</p>', 'd50-mici')
if 'DMT1' not in G:
    a('DMT1', [('D', 'Divalent (divalent)'), ('M', 'Metal (des métaux)'), ('T', 'Transporter (transporteur)'), ('1', 'type 1')], 'Transporteur des métaux divalents de type 1', '<p>DMT1 est une protéine apicale de l’entérocyte qui fait entrer le fer alimentaire. Son expression augmente en cas d’hypoxie et de carence.</p>', 'd50-absorption')
if 'FGF23' not in G:
    a('FGF23', [('F', 'Fibroblast (des fibroblastes)'), ('G', 'Growth (de croissance)'), ('F', 'Factor (facteur)'), ('23', 'numéro 23')], 'Facteur de croissance des fibroblastes 23', '<p>FGF23 est une hormone phosphaturique produite par l’os. Certaines préparations de fer intraveineux, surtout le carboxymaltose, élèvent sa forme intacte : le rein perd du phosphate et l’activation de la vitamine D diminue.</p>', 'd50-hypophos')
if 'TMPRSS6' not in G:
    a('TMPRSS6', [('TM', 'TransMembrane (transmembranaire)'), ('PRSS', 'PRotease, Serine (protéase à sérine)'), ('6', 'membre 6')], 'Gène de la protéase transmembranaire à sérine 6 (matriptase-2)', '<p>TMPRSS6 code la matriptase-2, qui freine la synthèse hépatique d’hepcidine par la voie hépatique des protéines morphogénétiques osseuses et de leurs médiateurs de signalisation. Ses variants pathogènes causent l’anémie ferriprive réfractaire au fer.</p>', 'd50-irida')
if 'SGH' not in G:
    a('SGH', [('S','Schweizerische (suisse)'),('G','Gesellschaft (société)'),('H','für Hämatologie (d’hématologie)')], 'Société suisse d’hématologie', '<p>La Société suisse d’hématologie participe au guide commun Onkopedia sur la carence martiale, version avril 2025.</p>')
if 'SSH' not in G:
    a('SSH', [('S','Société'),('S','Suisse'),('H','d’Hématologie')], 'Société suisse d’hématologie', '<p>SSH désigne en français la SGH, qui participe au guide Onkopedia sur la carence martiale.</p>')
if 'ACPGBI' not in G:
    a('ACPGBI', [('A','Association'),('CP','of ColoProctology (de coloproctologie)'),('GB','of Great Britain (de Grande-Bretagne)'),('I','and Ireland (et d’Irlande)')], 'Association de coloproctologie de Grande-Bretagne et d’Irlande', '<p>Cette association est partenaire de la BSG pour la clarification 2025 du test immunochimique fécal dans l’anémie ferriprive.</p>')
if 'AEGIS' not in G:
    a('AEGIS', [('AEGIS','nom d’essais du maltol ferrique ; aucun développement littéral fourni par l’information professionnelle suisse')], 'Essais AEGIS du maltol ferrique', '<p>AEGIS désigne des programmes d’essais chez les patients atteints de maladies inflammatoires intestinales ou de maladie rénale, décrits dans l’information professionnelle Feraccru®.</p>')

if 'SGMO' not in G:
    a('SGMO', [('S','Schweizerische (suisse)'),('G','Gesellschaft (société)'),('M','für Medizinische (d’oncologie médicale)'),('O','Onkologie (oncologie)')], 'Société suisse d’oncologie médicale', '<p>La Société suisse d’oncologie médicale participe au guide Onkopedia sur la carence martiale, version avril 2025.</p>')
if 'MonoFer' not in G:
    a('MonoFer', [('MonoFer','nom commercial suisse du dérisomaltose ferrique, et non abréviation développable lettre à lettre')], 'MonoFer® — dérisomaltose ferrique', '<p>MonoFer® est une préparation intraveineuse suisse. Les doses, contre-indications et précautions propres au produit sont détaillées dans la fenêtre.</p>', 'd50-d-derisomaltose')
