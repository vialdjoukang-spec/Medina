"""Abréviations G71 (Affections musculaires primitives). Entrées conditionnelles : aucun terme existant dans G n’est écrasé."""
from cardio_1 import a, G

def _add(k, lit, full, d, ref=None):
    if k not in G:
        a(k, lit, full, '<p>' + d + '</p>', ref)

_add('DMD', [('D','Dystrophie'),('M','Musculaire de'),('D','Duchenne')], 'Dystrophie musculaire de Duchenne',
     'Maladie récessive liée à l’X due à des mutations du gène de la dystrophine, qui rendent la protéine absente ou insuffisante ; elle provoque faiblesse, perte de la marche, atteinte respiratoire et cardiomyopathie.', 'g71-dystrophine')
_add('DM1', [('D','Dystrophie'),('M','Myotonique de type'),('1','1')], 'Dystrophie myotonique de type 1',
     'Maladie autosomique dominante par expansion instable de triplets CTG du gène DMPK, avec myotonie, faiblesse distale et atteinte multisystémique (œil, cœur, tube digestif, cerveau).', 'g71-dm1-genetique')
_add('DM2', [('D','Dystrophie'),('M','Myotonique de type'),('2','2')], 'Dystrophie myotonique de type 2',
     'Dystrophie myotonique par expansion CCTG dans l’intron 1 du gène CNBP, à atteinte surtout proximale et en général moins sévère que le type 1.')
_add('CK', [('C','Créatine'),('K','Kinase')], 'Créatine kinase',
     'Enzyme musculaire dont l’élévation dans le sang signale une lésion de la fibre musculaire ; l’hyperCKémie se définit par une valeur supérieure à 1,5 fois la limite supérieure de la normale.', 'g71-ck-fiche')
_add('hyperCKémie', [('hyper','excès de'),('CK','Créatine Kinase'),('émie','dans le sang')], 'Élévation de la créatine kinase sérique',
     'Valeur de CK supérieure à 1,5 fois la limite supérieure de la normale selon les recommandations européennes lues.', 'g71-hyperck')
_add('HyperCKémie', [('Hyper','excès de'),('CK','Créatine Kinase'),('émie','dans le sang')], 'Élévation de la créatine kinase sérique',
     'Valeur de CK supérieure à 1,5 fois la limite supérieure de la normale selon les recommandations européennes lues.', 'g71-hyperck')
_add('SpO2', [('S','Saturation'),('p','pulsée'),('O2','en dioxygène')], 'Saturation pulsée en oxygène',
     'Pourcentage d’hémoglobine saturée en oxygène mesuré par oxymétrie de pouls ; dans la dystrophie de Duchenne, une valeur inférieure à 95 % déclenche l’intensification de la toux assistée.')
_add('pCO2', [('p','pression'),('CO2','partielle de dioxyde de carbone')], 'Pression partielle de dioxyde de carbone',
     'Reflet de la ventilation alvéolaire ; une valeur supérieure à 45 mmHg est un critère de ventilation nocturne dans la dystrophie de Duchenne.', 'g71-seuils-resp')
_add('cmH2O', [('cm','centimètre'),('H2O','d’eau')], 'Centimètre d’eau',
     'Unité de pression utilisée pour les pressions respiratoires maximales.')
_add('MELAS', [('M','Mitochondrial'),('E','Encephalomyopathy'),('L','Lactic acidosis'),('A','And'),('S','Stroke-like episodes')], 'Encéphalomyopathie mitochondriale, acidose lactique, épisodes pseudo-vasculaires',
     'Syndrome défini par un ou plusieurs épisodes pseudo-vasculaires dans un contexte de dysfonction mitochondriale due à un variant pathogène de l’ADN mitochondrial, surtout m.3243A&gt;G.', 'g71-melas')
_add('MELAS-like', [('MELAS-like','terme anglais déconseillé, « de type MELAS »')], 'Terme déconseillé par le consensus',
     'Le consensus européen de 2026 déconseille les expressions « MELAS-like » et « spectre MELAS ».', 'g71-melas')
_add('FSHD', [('F','Facio'),('S','Scapulo'),('H','Humeral'),('D','Dystrophy')], 'Dystrophie musculaire facio-scapulo-humérale',
     'Dystrophie due à la dérépression du facteur DUX4, avec faiblesse du visage, de la ceinture scapulaire et des membres, souvent asymétrique.', 'g71-fshd')
_add('DUX4', [('DUX4','Double homeobox 4')], 'Double homeobox 4',
     'Facteur de transcription toxique pour le muscle, exprimé dans la facio-scapulo-humérale lorsque le locus 4q35 est hypométhylé.', 'g71-fshd')
_add('D4Z4', [('D4Z4','désignation de locus, non développée dans les sources lues')], 'Unités répétées D4Z4',
     'Unités répétées du locus 4q35 ; leur nombre est inversement corrélé à la sévérité dans la cohorte russe.', 'g71-fshd')
_add('MLPA', [('M','Multiplex'),('L','Ligation-dependent'),('P','Probe'),('A','Amplification')], 'Amplification multiplexe de sondes dépendante de la ligation',
     'Technique qui détecte les délétions et duplications d’exons du gène de la dystrophine, premier test de la dystrophie de Duchenne.', 'g71-gen-dmd')
_add('CGH-array', [('CGH','Comparative Genomic Hybridization'),('array','puce')], 'Hybridation génomique comparative sur puce',
     'Technique alternative à la MLPA pour détecter délétions et duplications d’exons.', 'g71-gen-dmd')
_add('COX-négatives', [('COX','Cytochrome c OXydase'),('négatives','sans activité visible à la coloration')], 'Fibres sans activité de la cytochrome c oxydase',
     'Fibres musculaires où la coloration de la cytochrome c oxydase est absente ; leur proportion médiane est de 5,1 % dans la cohorte d’adultes avec myopathie mitochondriale.', 'g71-biopsie')
_add('EMG', [('E','Électro'),('M','Myo'),('G','Gramme')], 'Électromyogramme',
     'Enregistrement de l’activité électrique du muscle ; un profil myopathique oriente vers une atteinte musculaire primitive.', 'g71-emg')
_add('OEPC', [('O','Ophtalmoplégie'),('E','Externe'),('P','Progressive'),('C','Chronique')], 'Ophtalmoplégie externe progressive chronique',
     'Atteinte des muscles externes de l’œil avec ptosis, d’origine mitochondriale ; à distinguer de la myasthénie.', 'g71-ptosis')
_add('NSAA', [('N','North'),('S','Star'),('A','Ambulatory'),('A','Assessment')], 'North Star Ambulatory Assessment',
     'Échelle fonctionnelle de la marche utilisée tous les 6 mois dans la dystrophie de Duchenne.', 'g71-nsaa')
_add('LGMD', [('L','Limb'),('G','Girdle'),('M','Muscular'),('D','Dystrophy')], 'Dystrophie musculaire des ceintures',
     'Faiblesse progressive chronique des ceintures pelvienne et scapulaire, de transmission dominante ou récessive.', 'g71-lgmd')
_add('LGMD1', [('LGMD','dystrophie des ceintures'),('1','transmission dominante, ancienne nomenclature')], 'Ancienne nomenclature dominante',
     'Appellation ancienne des dystrophies des ceintures de transmission autosomique dominante.', 'g71-lgmd')
_add('LGMD2', [('LGMD','dystrophie des ceintures'),('2','transmission récessive, ancienne nomenclature')], 'Ancienne nomenclature récessive',
     'Appellation ancienne des dystrophies des ceintures de transmission autosomique récessive.', 'g71-lgmd')
_add('ENMC', [('E','European'),('N','Neuromuscular'),('M','Muscle'),('C','Centre')], 'Centre européen du muscle et des maladies neuromusculaires',
     'Organisme qui organise des ateliers internationaux ; le 229<sup>e</sup> atelier de 2017 a réformé la nomenclature des dystrophies des ceintures.')
_add('EFNS', [('E','European'),('F','Federation of'),('N','Neurological'),('S','Societies')], 'Fédération européenne des sociétés de neurologie',
     'Elle a publié en 2010 la recommandation lue sur l’hyperCKémie.')
_add('EMHG', [('E','European'),('M','Malignant'),('H','Hyperthermia'),('G','Group')], 'Groupe européen d’hyperthermie maligne',
     'Il a publié les recommandations péri-opératoires de 2020 et le guide de 2024 sur la crise.', 'g71-hm')
_add('ERN', [('E','European'),('R','Reference'),('N','Network')], 'Réseau européen de référence',
     'Réseau européen de centres de référence pour les maladies rares.')
_add('EURO-NMD', [('EURO','European'),('NMD','NeuroMuscular Diseases')], 'Réseau européen de référence pour les maladies neuromusculaires rares',
     'Réseau qui a participé au consensus 2026 sur le MELAS.')
_add('ACMG', [('A','American'),('C','College of'),('M','Medical'),('G','Genetics and Genomics')], 'Collège américain de génétique et génomique médicales',
     'Source nord-américaine du standard technique de 2024 sur le test de la DM1, utilisée pour la génétique descriptive.')
_add('NHLBI', [('N','National'),('H','Heart,'),('L','Lung, and'),('B','Blood'),('I','Institute')], 'Institut national américain du cœur, des poumons et du sang',
     'Institution dont proviennent en partie les recommandations cardiaques du consensus sur la dystrophie de Duchenne ; source américaine.')
_add('ICD-10-GM', [('ICD','International Classification of Diseases'),('10','dixième révision'),('GM','German Modification')], 'Classification internationale des maladies, 10e révision, modification allemande',
     'Version allemande de la classification, source du bloc G70–G73 consulté.')
_add('25-OH-vitamine', [('25','position 25'),('OH','hydroxy'),('vitamine','vitamine')], '25-hydroxy-vitamine',
     'Forme circulante dosée dans le suivi nutritionnel annuel de la dystrophie de Duchenne.')
_add('NEB', [('NEB','nébuline')], 'Gène de la nébuline', 'Un des huit gènes majeurs des myopathies congénitales.', 'g71-congenitales')
_add('ACTA1', [('ACTA1','actine alpha 1 du muscle squelettique')], 'Gène de l’actine alpha 1', 'Un des huit gènes majeurs des myopathies congénitales.', 'g71-congenitales')
_add('ADSSL1', [('ADSSL1','adénylosuccinate synthase de type 1')], 'Gène ADSSL1', 'Un des huit gènes majeurs des myopathies congénitales.', 'g71-congenitales')
_add('RYR1', [('RYR1','récepteur de la ryanodine 1')], 'Gène du récepteur de la ryanodine 1', 'Gène des myopathies congénitales à cores ; son lien avec l’hyperthermie maligne n’est pas énoncé explicitement dans les textes lus.', 'g71-hm')
_add('SELENON', [('SELENON','sélénoprotéine N')], 'Gène de la sélénoprotéine N', 'Un des huit gènes majeurs des myopathies congénitales.', 'g71-congenitales')
_add('MTM1', [('MTM1','myotubularine 1')], 'Gène de la myotubularine 1', 'Gène de la myopathie myotubulaire liée à l’X.', 'g71-congenitales')
_add('DNM2', [('DNM2','dynamine 2')], 'Gène de la dynamine 2', 'Un des huit gènes majeurs des myopathies congénitales.', 'g71-congenitales')
_add('TPM3', [('TPM3','tropomyosine 3')], 'Gène de la tropomyosine 3', 'Un des huit gènes majeurs des myopathies congénitales.', 'g71-congenitales')
_add('CNBP', [('CNBP','protéine de liaison aux acides nucléiques à doigt de zinc de type CCHC')], 'Gène CNBP', 'Gène de l’intron 1 duquel l’expansion CCTG cause la dystrophie myotonique de type 2.')
_add('CCTG', [('C','Cytosine'),('C','Cytosine'),('T','Thymine'),('G','Guanine')], 'Quadruplet CCTG', 'Séquence répétée dont l’expansion dans l’intron 1 de CNBP cause la dystrophie myotonique de type 2.')
_add('MT-TL1', [('MT','mitochondrial'),('T','transfert'),('L1','leucine 1')], 'Gène mitochondrial de l’ARN de transfert de la leucine 1', 'Gène portant le variant m.3243A&gt;G cité dans le MELAS.', 'g71-melas')
_add('EPIDYS', [('EPIDYS','nom de l’essai de phase 3 du givinostat, non développé dans les sources lues')], 'Essai EPIDYS', 'Essai de phase 3 du givinostat chez 179 garçons atteints de dystrophie de Duchenne.', 'g71-givinostat')
_add('AGAMREE', [('AGAMREE','nom commercial suisse du vamorolone, non une abréviation')], 'AGAMREE®', 'Spécialité suisse du vamorolone (Santhera), dont l’information professionnelle a été lue.', 'g71-vamorolone')
_add('Curschmann-Batten-Steinert', [('Curschmann-Batten-Steinert','éponyme (noms de médecins), non une abréviation')], 'Dystrophie myotonique de Steinert', 'Nom classique de la dystrophie myotonique dans la classification.')
_add('Isaacs-Mertens', [('Isaacs-Mertens','éponyme (noms de médecins), non une abréviation')], 'Neuromyotonie d’Isaacs-Mertens', 'Entité citée parmi les affections myotoniques de la classification.')
for _c, _t in (('G71.0','dystrophie musculaire'),('G71.1','affections myotoniques'),('G71.2','myopathies congénitales'),('G71.3','myopathie mitochondriale non classée ailleurs'),('G71.8','autres affections musculaires primitives'),('G71.9','affection musculaire primitive, sans précision')):
    _add(_c, [(_c, 'code de la CIM-10-GM 2024 : ' + _t)], _t[0].upper() + _t[1:], 'Sous-catégorie de G71 dans la CIM-10-GM 2024.', 'g71-sousgroupes')
