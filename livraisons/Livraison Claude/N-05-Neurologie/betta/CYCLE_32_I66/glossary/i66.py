from cardio_1 import a, G
# I66 — Occlusion et sténose des artères cérébrales sans infarctus (N-05-Neurologie). Entrées conditionnelles : aucun terme existant dans G n’est écrasé.
if 'ICAD' not in G:
    a('ICAD', [('I', 'Intra'), ('C', 'Cranial'), ('A', 'Atherosclerotic'), ('D', 'Disease')], 'Maladie athéroscléreuse intracrânienne (intracranial atherosclerotic disease)', '<p>Plaque d’athérome des grosses artères intracrâniennes, à tout stade, y compris sans rétrécissement de la lumière (Organisation européenne de l’accident vasculaire cérébral, 2022).</p>', 'i66-icad')
if 'ICAS' not in G:
    a('ICAS', [('I', 'Intra'), ('C', 'Cranial'), ('A', 'Atherosclerotic'), ('S', 'Stenosis')], 'Sténose athéroscléreuse intracrânienne (intracranial atherosclerotic stenosis)', '<p>Plaque responsable d’un rétrécissement significatif de la lumière d’une grosse artère intracrânienne, en général supérieur à 50 %, documenté par angiographie ou Doppler transcrânien.</p>', 'i66-icad')
if 'PTAS' not in G:
    a('PTAS', [('P', 'Percutaneous'), ('T', 'Transluminal'), ('A', 'Angioplasty and'), ('S', 'Stenting')], 'Angioplastie transluminale percutanée avec stent (percutaneous transluminal angioplasty and stenting)', '<p>Geste endovasculaire qui dilate l’artère rétrécie puis y place un stent. Recommandation forte contre en première intention dans la sténose intracrânienne symptomatique (Organisation européenne, 2022).</p>', 'i66-sammpris')
if 'MTT' not in G:
    a('MTT', [('M', 'Mean'), ('T', 'Transit'), ('T', 'Time')], 'Temps de transit moyen (mean transit time)', '<p>Paramètre de l’imagerie de perfusion décrivant la durée moyenne que met le sang à traverser un territoire ; allongé dans le territoire d’une sténose de 50 à 99 %, il accompagne un risque accru d’accident ipsilatéral.</p>', 'i66-perfusion')
if 'Tmax' not in G:
    a('Tmax', [('T', 'Temps de transit'), ('max', 'maximal')], 'Temps de transit maximal (time to maximum)', '<p>Paramètre de l’imagerie de perfusion. Un mismatch de Tmax supérieur à 6 secondes sur au moins 15 mL est associé aux récidives (Chen et al., 2024).</p>', 'i66-perfusion')
if 'RNF213' not in G:
    a('RNF213', [('RNF213', 'nom du gène (ring finger protein 213), non développable lettre à lettre')], 'Gène RNF213', '<p>Gène dont le variant p.R4810K est associé à la maladie athéroscléreuse intracrânienne en Asie de l’Est et à la vasculopathie de type moyamoya.</p>', 'i66-rnf213')
if 'R4810K' not in G:
    a('R4810K', [('R', 'Arginine'), ('4810', 'position 4810 de la protéine'), ('K', 'Lysine')], 'Substitution de l’arginine par la lysine en position 4810', '<p>Notation du variant du gène RNF213 associé à la maladie athéroscléreuse intracrânienne en Asie de l’Est ; il est absent hors des populations asiatiques.</p>', 'i66-rnf213')
if 'EDAS' not in G:
    a('EDAS', [('E', 'Encéphalo'), ('D', '-Duro'), ('A', '-Artério'), ('S', '-Synangiose')], 'Encéphalo-duro-artério-synangiose', '<p>Chirurgie de revascularisation indirecte, citée avec le pontage extra-intracrânien : recommandation forte contre en première ligne dans la sténose athéroscléreuse intracrânienne.</p>', 'i66-cochrane')
if 'WASID' not in G:
    a('WASID', [('WASID', 'nom d’essai : Warfarin-Aspirin Symptomatic Intracranial Disease, non strictement lettre à lettre')], 'Essai WASID (2005) et méthode de mesure qui en dérive', '<p>Essai de comparaison de la warfarine et de l’aspirine dans la sténose intracrânienne de 50 à 99 % (569 patients) ; il a aussi donné son nom à la méthode standardisée de mesure du pourcentage de sténose.</p>', 'i66-wasid-essai')
if 'SAMMPRIS' not in G:
    a('SAMMPRIS', [('SAMMPRIS', 'nom d’essai : comparaison du stent et du traitement médical intensif, non développé lettre à lettre')], 'Essai SAMMPRIS (2011)', '<p>Essai de 451 patients avec sténose de 70 à 99 % : accident vasculaire cérébral ou décès à 30 jours, 14,7 % avec stent et 5,8 % sous traitement médical.</p>', 'i66-sammpris')
if 'VISSIT' not in G:
    a('VISSIT', [('VISSIT', 'nom d’essai : stent expansible par ballon contre traitement médical, non développé lettre à lettre')], 'Essai VISSIT', '<p>Essai arrêté précocement : critère de sécurité à 30 jours de 24,1 % avec stent contre 9,4 % sous traitement médical.</p>', 'i66-vissit')
if 'CASSISS' not in G:
    a('CASSISS', [('CASSISS', 'nom d’essai chinois : stent associé au traitement médical contre traitement médical seul, non développé lettre à lettre')], 'Essai CASSISS (2022)', '<p>Essai chinois de 358 patients, plus de trois semaines après l’événement : accident vasculaire cérébral ou décès de 8,0 % contre 7,2 %.</p>', 'i66-cassiss')
if 'CLAIR' not in G:
    a('CLAIR', [('CLAIR', 'nom d’essai : clopidogrel plus aspirine contre aspirine seule pour réduire l’embolisation, non développé lettre à lettre')], 'Essai CLAIR (2010)', '<p>Essai montrant une réduction relative de 42,4 % des signaux microemboliques au deuxième jour sous clopidogrel plus aspirine.</p>', 'i66-clair')
if 'SONIA' not in G:
    a('SONIA', [('S', 'Stroke'), ('O', 'Outcomes and'), ('N', 'Neuroimaging of'), ('I', 'Intracranial'), ('A', 'Atherosclerosis')], 'Essai SONIA (Stroke Outcomes and Neuroimaging of Intracranial Atherosclerosis)', '<p>Étude qui compare Doppler transcrânien et angio-IRM à l’angiographie pour la sténose intracrânienne de 50 à 99 % : valeurs prédictives positives 36 % et 59 %, négatives 86 % et 91 %.</p>', 'i66-sonia')
