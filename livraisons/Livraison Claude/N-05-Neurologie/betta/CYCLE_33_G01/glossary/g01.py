"""Abréviations G01 (Méningite au cours d’affections bactériennes classées ailleurs). Entrées conditionnelles : aucun terme existant dans G n’est écrasé."""
from cardio_1 import a, G
if 'MONALISA' not in G:
    a('MONALISA', [('MONALISA', 'nom de la cohorte nationale prospective française de listériose ; la publication lue ne fournit aucun développement littéral')], 'Cohorte MONALISA', '<p>MONALISA désigne la cohorte nationale prospective française de listériose (818 cas, dont 252 neurolistérioses) publiée dans Lancet Infectious Diseases en 2017. Elle fournit les prédicteurs de mortalité et l’association entre dexaméthasone et mortalité en neurolistériose.</p>', 'g01-monalisa')
if 'CXCL13' not in G:
    a('CXCL13', [('CXC', 'motif cystéine-X-cystéine'), ('L', 'Ligand (ligand de chimiokine)'), ('13', 'numéro 13')], 'Ligand 13 de chimiokine à motif CXC', '<p>CXCL13 est une chimiokine attirant les lymphocytes B. Son dosage dans le liquide cérébro-spinal est élevé dans la neuroborréliose, la neurosyphilis et le lymphome du système nerveux central ; il n’est pas standardisé en neuroborréliose et non recommandé en neurosyphilis.</p>', 'g01-cxcl13')
if 'FTA-ABS' not in G:
    a('FTA-ABS', [('F', 'Fluorescent (fluorescent)'), ('T', 'Treponemal (tréponémique)'), ('A', 'Antibody (anticorps)'), ('ABS', 'ABSorption (absorption)')], 'Test d’absorption des anticorps tréponémiques fluorescents', '<p>Ce test tréponémique du sérum confirme un test de dépistage positif (TPPA, TPHA ou TPLA) dans la démarche de la neurosyphilis.</p>', 'g01-syph-tests')
if 'FTA' not in G:
    a('FTA', [('F', 'Fluorescent (fluorescent)'), ('T', 'Treponemal (tréponémique)'), ('A', 'Antibody (anticorps)')], 'Anticorps tréponémiques fluorescents', '<p>FTA désigne le test d’immunofluorescence des anticorps tréponémiques ; il appartient aux tests tréponémiques du sérum. Il ne sert pas au suivi après traitement.</p>', 'g01-syph-tests')
if 'ITpA' not in G:
    a('ITpA', [('I', 'Intrathecal (intrathécal)'), ('Tp', 'Treponema pallidum (tréponème pâle)'), ('A', 'Antibody (anticorps)')], 'Index d’anticorps intrathécaux anti-Treponema pallidum', '<p>L’index ITpA mesure la production intrathécale d’anticorps antitréponémiques ; avec l’index TPHA liquide/sérum, il définit la neurosyphilis confirmée dans la recommandation allemande de 2020. Il est inutile au suivi.</p>', 'g01-syph-tests')
if 'TPLA' not in G:
    a('TPLA', [('T', 'Treponema (tréponème)'), ('P', 'Pallidum (pâle)'), ('L', 'Latex (latex)'), ('A', 'Agglutination (agglutination)')], 'Agglutination au latex de Treponema pallidum', '<p>TPLA est un test tréponémique sérique, avec le TPPA et le TPHA, utilisé en première intention dans la démarche de la neurosyphilis.</p>', 'g01-syph-tests')
if 'TLR2' not in G:
    a('TLR2', [('TLR', 'Toll-Like Receptor (récepteur de type Toll)'), ('2', 'numéro 2')], 'Récepteur de type Toll 2', '<p>Ce récepteur de l’immunité innée reconnaît des composants bactériens libérés par la lyse dans le liquide cérébro-spinal et déclenche la production de cytokines inflammatoires.</p>', 'g01-cytokines')
if 'TLR4' not in G:
    a('TLR4', [('TLR', 'Toll-Like Receptor (récepteur de type Toll)'), ('4', 'numéro 4')], 'Récepteur de type Toll 4', '<p>Ce récepteur de l’immunité innée participe, avec TLR2 et Nod2, à la reconnaissance des composants bactériens dans la méningite.</p>', 'g01-cytokines')
if 'Nod2' not in G:
    a('Nod2', [('Nod', 'Nucleotide-binding oligomerization domain (domaine d’oligomérisation liant les nucléotides)'), ('2', 'numéro 2')], 'Récepteur Nod2', '<p>Nod2 est un récepteur intracellulaire de l’immunité innée cité parmi les récepteurs qui reconnaissent les composants bactériens libérés lors de la lyse.</p>', 'g01-cytokines')
if 'MenQuadfi' not in G:
    a('MenQuadfi', [('MenQuadfi', 'nom commercial d’un vaccin antiméningococcique ACWY, non une abréviation')], 'MenQuadfi, vaccin antiméningococcique ACWY', '<p>MenQuadfi est l’un des deux vaccins ACWY cités par la fiche vaccinale suisse (avec Menveo) pour la vaccination de routine.</p>', 'g01-vaccination')
if 'pCO2' not in G:
    a('pCO2', [('p', 'pression partielle'), ('CO2', 'dioxyde de carbone')], 'Pression partielle de dioxyde de carbone', '<p>La pCO2 est la pression partielle du dioxyde de carbone dans le sang artériel. Dans la méningite avec hypertension intracrânienne, la recommandation décrit une hyperventilation brève visant une pCO2 de 32 à 35 mmHg.</p>', 'g01-hic')
