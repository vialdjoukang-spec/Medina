"""Abréviations G60 — Neuropathie héréditaire et idiopathique (N-05-Neurologie). Entrées conditionnelles : aucun terme existant dans G n’est écrasé."""
from cardio_1 import a, G

if 'CMT' not in G:
    a('CMT', [('C', 'Charcot'), ('M', 'Marie'), ('T', 'Tooth')], 'Maladie de Charcot-Marie-Tooth', '<p>Neuropathie héréditaire sensitivomotrice, la plus fréquente des neuropathies héréditaires, classée en G60.0. Elle porte le nom de trois médecins qui l’ont décrite.</p>', 'g60-cmt')
if 'CMT1' not in G:
    a('CMT1', [('CMT', 'Charcot-Marie-Tooth'), ('1', 'type démyélinisant à hérédité dominante')], 'Charcot-Marie-Tooth de type 1', '<p>Forme démyélinisante autosomique dominante : vitesse de conduction motrice inférieure à 38 m/s.</p>', 'g60-seuil38')
if 'CMT2' not in G:
    a('CMT2', [('CMT', 'Charcot-Marie-Tooth'), ('2', 'type axonal')], 'Charcot-Marie-Tooth de type 2', '<p>Forme axonale : vitesse de conduction motrice supérieure à 38 m/s, amplitudes basses.</p>', 'g60-seuil38')
if 'CMT4' not in G:
    a('CMT4', [('CMT', 'Charcot-Marie-Tooth'), ('4', 'type démyélinisant à hérédité récessive')], 'Charcot-Marie-Tooth de type 4', '<p>Forme démyélinisante autosomique récessive : vitesse inférieure à 38 m/s.</p>', 'g60-seuil38')
if 'CMT1A' not in G:
    a('CMT1A', [('CMT1', 'Charcot-Marie-Tooth de type 1'), ('A', 'sous-type A, duplication de PMP22')], 'Charcot-Marie-Tooth de type 1A', '<p>Forme démyélinisante due à la duplication de PMP22, 40–50 % des CMT.</p>', 'g60-cmt1a')
if 'CMT1B' not in G:
    a('CMT1B', [('CMT1', 'Charcot-Marie-Tooth de type 1'), ('B', 'sous-type B, variants de MPZ')], 'Charcot-Marie-Tooth de type 1B', '<p>Forme démyélinisante liée à MPZ, environ 8 % des CMT.</p>', 'g60-mpz')
if 'CMT2A' not in G:
    a('CMT2A', [('CMT2', 'Charcot-Marie-Tooth de type 2'), ('A', 'sous-type A, variants de MFN2')], 'Charcot-Marie-Tooth de type 2A', '<p>Forme axonale par dysfonction de la mitofusine 2.</p>', 'g60-mfn2')
if 'CMTX' not in G:
    a('CMTX', [('CMT', 'Charcot-Marie-Tooth'), ('X', 'lié au chromosome X')], 'Charcot-Marie-Tooth lié à l’X', '<p>Formes de CMT à hérédité liée au chromosome X.</p>', 'g60-cmtx1')
if 'CMTX1' not in G:
    a('CMTX1', [('CMT', 'Charcot-Marie-Tooth'), ('X', 'lié au chromosome X'), ('1', 'sous-type 1, variants de GJB1')], 'Charcot-Marie-Tooth lié à l’X, type 1', '<p>Forme liée à l’X par perte de connexine 32 ; 7–12 % des CMT.</p>', 'g60-cmtx1')
if 'CMT-SORD' not in G:
    a('CMT-SORD', [('CMT', 'Charcot-Marie-Tooth'), ('SORD', 'forme due aux variants de SORD')], 'CMT liée à SORD', '<p>Forme récessive due à des variants du gène SORD.</p>', 'g60-essais')
if 'CMTNS' not in G:
    a('CMTNS', [('CMT', 'Charcot-Marie-Tooth'), ('N', 'Neuropathy'), ('S', 'Score')], 'Score de neuropathie de la CMT (CMT Neuropathy Score)', '<p>Score de gravité de la CMT qui intègre l’électrophysiologie.</p>', 'g60-cmtns')
if 'CMTES' not in G:
    a('CMTES', [('CMT', 'Charcot-Marie-Tooth'), ('E', 'Examination'), ('S', 'Score')], 'Score d’examen de la CMT (CMT Examination Score)', '<p>Score de gravité de la CMT fondé sur l’examen clinique seul, sans électrophysiologie.</p>', 'g60-cmtns')
if 'MRC' not in G:
    a('MRC', [('M', 'Medical'), ('R', 'Research'), ('C', 'Council')], 'Medical Research Council', '<p>Cotation de la force musculaire de 0 à 5 proposée par le Medical Research Council britannique.</p>', 'g60-cmtns')
if 'HNPP' not in G:
    a('HNPP', [('H', 'Hereditary'), ('N', 'Neuropathy with'), ('P', 'liability to Pressure'), ('P', 'Palsies')], 'Neuropathie héréditaire avec hypersensibilité à la pression (Hereditary Neuropathy with liability to Pressure Palsies)', '<p>Neuropathie due à la délétion de PMP22 : paralysies compressives épisodiques et indolores.</p>', 'g60-hnpp')
if 'CIAP' not in G:
    a('CIAP', [('C', 'Chronique'), ('I', 'Idiopathique'), ('A', 'Axonale'), ('P', 'Polyneuropathie')], 'Neuropathie axonale idiopathique chronique (Chronic Idiopathic Axonal Polyneuropathy)', '<p>Polyneuropathie axonale sans cause trouvée, codée G60.3.</p>', 'g60-ciap')
if 'PIDC' not in G:
    a('PIDC', [('P', 'Polyradiculonévrite'), ('I', 'Inflammatoire'), ('D', 'Démyélinisante'), ('C', 'Chronique')], 'Polyradiculonévrite inflammatoire démyélinisante chronique', '<p>Neuropathie acquise d’origine immune, traitable, principal diagnostic différentiel de la CMT démyélinisante.</p>', 'g60-pidc')
if 'CIDP' not in G:
    a('CIDP', [('C', 'Chronic'), ('I', 'Inflammatory'), ('D', 'Demyelinating'), ('P', 'Polyradiculoneuropathy')], 'Chronic inflammatory demyelinating polyradiculoneuropathy', '<p>Équivalent anglais de PIDC.</p>', 'g60-pidc')
if 'ENMG' not in G:
    a('ENMG', [('E', 'Électro'), ('N', 'Neuro'), ('M', 'Myo'), ('G', 'Graphie')], 'Électroneuromyographie', '<p>Examen de la conduction des nerfs et de l’activité des muscles : vitesse, latence, amplitude.</p>', 'g60-enmg')
if 'PMP22' not in G:
    a('PMP22', [('P', 'Peripheral'), ('M', 'Myelin'), ('P', 'Protein'), ('22', '22 kilodaltons')], 'Peripheral Myelin Protein 22', '<p>Gène de la protéine 22 de la myéline périphérique : sa duplication cause la CMT1A, sa délétion la HNPP.</p>', 'g60-cmt1a')
if 'MPZ' not in G:
    a('MPZ', [('M', 'Myelin'), ('P', 'Protein'), ('Z', 'Zero')], 'Myelin Protein Zero (protéine zéro de la myéline)', '<p>Constituant protéique majeur de la myéline périphérique ; gène de la CMT1B.</p>', 'g60-mpz')
if 'GJB1' not in G:
    a('GJB1', [('G', 'Gap'), ('J', 'Junction'), ('B1', 'Beta 1')], 'Gap Junction Beta 1', '<p>Gène de la connexine 32 ; ses variants causent la CMTX1.</p>', 'g60-cmtx1')
if 'MFN2' not in G:
    a('MFN2', [('M', 'Mitofusine'), ('F', 'Fusion'), ('N', 'Nucléaire'), ('2', '2')], 'Mitofusine 2', '<p>Gène de la mitofusine 2, protéine mitochondriale ; ses variants causent la CMT2A.</p>', 'g60-mfn2')
if 'SORD' not in G:
    a('SORD', [('S', 'Sorbitol'), ('ORD', 'Oxydoréductase déshydrogénase')], 'Sorbitol déshydrogénase', '<p>Gène dont les variants récessifs, surtout c.757delG, causent jusqu’à 10 % des CMT2 et dHMN récessives.</p>', 'g60-dhmn')
if 'c.757delG' not in G:
    a('c.757delG', [('c.757delG', 'nomenclature d’une variation de séquence, non une abréviation')], 'Délétion d’une guanine en position 757 du gène', '<p>Variant le plus fréquent de SORD.</p>', 'g60-dhmn')
if 'MT-ATP6' not in G:
    a('MT-ATP6', [('MT', 'Mitochondrial'), ('ATP6', 'ATP synthase sous-unité 6')], 'Gène mitochondrial de l’ATP synthase sous-unité 6', '<p>Gène du génome mitochondrial, impliqué dans au moins 1 % des CMT axonales de certaines séries.</p>', 'g60-mfn2')
if 'FIG4' not in G:
    a('FIG4', [('FIG4', 'symbole de gène, non une abréviation à développer')], 'Gène FIG4', '<p>Gène dont les variants peuvent mimer une neuropathie acquise immune.</p>', 'g60-pidc')
if 'LITAF' not in G:
    a('LITAF', [('LITAF', 'symbole de gène, non une abréviation à développer')], 'Gène LITAF', '<p>Gène dont les variants peuvent mimer une neuropathie acquise immune.</p>', 'g60-pidc')
if 'HSPB1' not in G:
    a('HSPB1', [('HSPB1', 'symbole de gène (protéine de choc thermique B1)')], 'Gène HSPB1', '<p>Gène qui peut produire une CMT2 ou une dHMN.</p>', 'g60-dhmn')
if 'SH3TC2' not in G:
    a('SH3TC2', [('SH3TC2', 'symbole de gène, non une abréviation à développer')], 'Gène SH3TC2', '<p>Gène du panel minimal d’étude génétique de la CMT.</p>', 'g60-genetique')
if 'GDAP1' not in G:
    a('GDAP1', [('GDAP1', 'symbole de gène (protéine associée à la différenciation induite par les gangliosides 1)')], 'Gène GDAP1', '<p>Gène du panel minimal d’étude génétique de la CMT.</p>', 'g60-genetique')
if 'MME' not in G:
    a('MME', [('MME', 'symbole de gène (métallo-endopeptidase membranaire)')], 'Gène MME', '<p>Gène du panel minimal d’étude génétique de la CMT.</p>', 'g60-genetique')
if 'PHYH' not in G:
    a('PHYH', [('PHYH', 'symbole de gène (phytanoyl-CoA hydroxylase)')], 'Gène PHYH', '<p>Gène de l’enzyme de l’alpha-oxydation de l’acide phytanique ; au moins 90 % des cas de Refsum.</p>', 'g60-refsum')
if 'PEX7' not in G:
    a('PEX7', [('PEX7', 'symbole de gène (peroxine 7)')], 'Gène PEX7', '<p>Gène de biogenèse du peroxysome ; cause plus rare de Refsum.</p>', 'g60-refsum')
if 'RFC1' not in G:
    a('RFC1', [('RFC1', 'symbole de gène (Replication Factor C subunit 1)')], 'Gène RFC1', '<p>Gène associé au syndrome CANVAS.</p>', 'g60-ataxie')
if 'ABHD12' not in G:
    a('ABHD12', [('ABHD12', 'symbole de gène, non une abréviation à développer')], 'Gène ABHD12', '<p>Gène de la phénocopie PHARC du Refsum.</p>', 'g60-refsum')
if 'PHARC' not in G:
    a('PHARC', [('PHARC', 'acronyme anglais d’un syndrome (polyneuropathie, surdité, ataxie, rétinite pigmentaire, cataracte)')], 'Syndrome PHARC', '<p>Phénocopie du Refsum liée à ABHD12.</p>', 'g60-refsum')
if 'PXT3003' not in G:
    a('PXT3003', [('PXT3003', 'code d’un produit d’essai, non une abréviation')], 'Association baclofène, D-sorbitol et naltrexone', '<p>Produit en phase III dans la CMT1A, en réévaluation.</p>', 'g60-essais')
if 'MLPA' not in G:
    a('MLPA', [('M', 'Multiplex'), ('L', 'Ligation-dependent'), ('P', 'Probe'), ('A', 'Amplification')], 'Multiplex Ligation-dependent Probe Amplification', '<p>Technique de dosage du nombre de copies d’un gène, utilisée pour la duplication ou la délétion de PMP22.</p>', 'g60-genetique')
if 'NGS' not in G:
    a('NGS', [('N', 'Next'), ('G', 'Generation'), ('S', 'Sequencing')], 'Next Generation Sequencing (séquençage de nouvelle génération)', '<p>Séquençage parallèle de panels de gènes ou de l’exome.</p>', 'g60-genetique')
if 'ACMG' not in G:
    a('ACMG', [('A', 'American'), ('C', 'College of'), ('M', 'Medical'), ('G', 'Genetics and genomics')], 'American College of Medical Genetics and Genomics', '<p>Organisation dont les cinq classes de variants sont citées par le guide espagnol pour classer les variants génétiques.</p>', 'g60-genetique')
if 'dHMN' not in G:
    a('dHMN', [('d', 'distale'), ('H', 'Héréditaire'), ('M', 'Motrice'), ('N', 'Neuronopathie')], 'Neuronopathie motrice distale héréditaire (distal hereditary motor neuropathy)', '<p>Neuropathie purement motrice distale génétique.</p>', 'g60-dhmn')
if 'HSN' not in G:
    a('HSN', [('H', 'Hereditary'), ('S', 'Sensory'), ('N', 'Neuropathy')], 'Neuropathie sensitive héréditaire', '<p>Neuropathie sensitive génétique.</p>', 'g60-hsan')
if 'HSAN' not in G:
    a('HSAN', [('H', 'Hereditary'), ('S', 'Sensory and'), ('A', 'Autonomic'), ('N', 'Neuropathy')], 'Neuropathie sensitive et autonome héréditaire', '<p>Neuropathie sensitive et autonome génétique.</p>', 'g60-hsan')
if 'CANVAS' not in G:
    a('CANVAS', [('C', 'Cerebellar'), ('A', 'Ataxia'), ('N', 'Neuropathy'), ('V', 'Vestibular'), ('A', 'Areflexia'), ('S', 'Syndrome')], 'Cerebellar Ataxia, Neuropathy, Vestibular Areflexia Syndrome', '<p>Syndrome associant ataxie cérébelleuse, neuropathie et abolition du réflexe vestibulo-oculaire, lié à RFC1.</p>', 'g60-ataxie')
if 'SACS' not in G:
    a('SACS', [('S', 'Spastic'), ('A', 'Ataxia of'), ('C', 'Charlevoix-'), ('S', 'Saguenay')], 'Ataxie spastique de Charlevoix-Saguenay', '<p>Ataxie héréditaire avec conduction nerveuse de type intermédiaire.</p>', 'g60-ataxie')
if 'Charlevoix-Saguenay' not in G:
    a('Charlevoix-Saguenay', [('Charlevoix-Saguenay', 'noms de deux régions québécoises, non une abréviation')], 'Charlevoix-Saguenay', '<p>Régions où l’ataxie spastique a été décrite.</p>', 'g60-ataxie')
if 'AP' not in G:
    a('AP', [('A', 'Acide'), ('P', 'Phytanique')], 'Acide phytanique', '<p>Acide gras ramifié qui s’accumule dans la maladie de Refsum.</p>', 'g60-ap')
if 'ASO' not in G:
    a('ASO', [('A', 'Anti'), ('S', 'Sens'), ('O', 'Oligonucléotide')], 'Oligonucléotide antisens (antisense oligonucleotide)', '<p>Médicament qui module l’expression d’un gène ; disponible pour l’amylose à transthyrétine et la porphyrie.</p>', 'g60-ttr')
if 'ARNi' not in G:
    a('ARNi', [('ARN', 'Acide ribonucléique'), ('i', 'interférent')], 'ARN interférent', '<p>Médicament qui réduit l’expression d’un gène.</p>', 'g60-ttr')
if 'CK' not in G:
    a('CK', [('C', 'Créatine'), ('K', 'Kinase')], 'Créatine kinase', '<p>Enzyme musculaire dont l’élévation est non spécifique ; non recommandée en routine dans la CMT.</p>', 'g60-decompensation')
if 'IRSN' not in G:
    a('IRSN', [('I', 'Inhibiteurs de la'), ('R', 'Recapture de la'), ('S', 'Sérotonine et de la'), ('N', 'Noradrénaline')], 'Inhibiteurs de la recapture de la sérotonine et de la noradrénaline', '<p>Classe d’antidépresseurs dont la duloxétine, en première ligne forte de la douleur neuropathique (NeuPSIG 2025).</p>', 'g60-neupsig')
if 'NNT' not in G:
    a('NNT', [('N', 'Number'), ('N', 'Needed to'), ('T', 'Treat')], 'Nombre de patients à traiter', '<p>Nombre de patients à traiter pour obtenir un répondeur supplémentaire.</p>', 'g60-neupsig')
if 'NNH' not in G:
    a('NNH', [('N', 'Number'), ('N', 'Needed to'), ('H', 'Harm')], 'Nombre de patients à traiter pour un effet indésirable', '<p>Nombre de patients traités pour observer un effet indésirable supplémentaire.</p>', 'g60-neupsig')
if 'NeuPSIG' not in G:
    a('NeuPSIG', [('Neu', 'Neuropathic'), ('P', 'Pain'), ('S', 'Special'), ('I', 'Interest'), ('G', 'Group')], 'Neuropathic Pain Special Interest Group', '<p>Groupe d’intérêt de l’Association internationale pour l’étude de la douleur, auteur des recommandations 2025.</p>', 'g60-neupsig')
if 'rTMS' not in G:
    a('rTMS', [('r', 'répétitive'), ('T', 'Transcranial'), ('M', 'Magnetic'), ('S', 'Stimulation')], 'Stimulation magnétique transcrânienne répétée', '<p>Neuromodulation non invasive citée en troisième ligne faible.</p>', 'g60-neupsig')
if 'PLS-AFO' not in G:
    a('PLS-AFO', [('PLS', 'Posterior Leaf Spring'), ('AFO', 'Ankle-Foot Orthosis')], 'Orthèse cheville-pied à lame postérieure', '<p>Orthèse qui compense la faiblesse du releveur du pied.</p>', 'g60-orthese')
if 'OKP' not in G:
    a('OKP', [('O', 'Obligatorische'), ('K', 'Kranken'), ('P', 'Pflegeversicherung')], 'Assurance obligatoire des soins (Obligatorische Krankenpflegeversicherung)', '<p>Assurance de base suisse ; le dossier ne contient pas d’information sur le remboursement des tests génétiques.</p>', 'g60-lacunes')
if 'DARE' not in G:
    a('DARE', [('D', 'Diagnosis and'), ('A', 'Adult'), ('R', 'Refsum'), ('E', 'Evaluation')], 'Global DARE', '<p>Nom de l’initiative internationale dont la guidance 2026 sur la maladie de Refsum est citée.</p>', 'g60-refsum')
if 'DGN' not in G:
    a('DGN', [('D', 'Deutsche'), ('G', 'Gesellschaft für'), ('N', 'Neurologie')], 'Société allemande de neurologie', '<p>Son guide sur les polyneuropathies n’a pas été accessible.</p>', 'g60-lacunes')
if 'EAN' not in G:
    a('EAN', [('E', 'European'), ('A', 'Academy of'), ('N', 'Neurology')], 'Académie européenne de neurologie', '<p>Son guide spécifique de la CMT n’a pas été trouvé.</p>', 'g60-lacunes')
if 'CIM' not in G:
    a('CIM', [('C', 'Classification'), ('I', 'Internationale des'), ('M', 'Maladies')], 'Classification internationale des maladies', '<p>Classification dont le catalogue du cours suit l’édition CIM-10-GM 2024.</p>', 'g60-codes')
if 'G60.0' not in G:
    a('G60.0', [('G60.0', 'code de la CIM-10-GM 2024, non une abréviation')], 'Code G60.0', '<p>Code de la CIM-10-GM 2024 : neuropathie héréditaire motrice et sensorielle.</p>', 'g60-codes')
if 'G60.1' not in G:
    a('G60.1', [('G60.1', 'code de la CIM-10-GM 2024, non une abréviation')], 'Code G60.1', '<p>Code de la CIM-10-GM 2024 : maladie de Refsum.</p>', 'g60-codes')
if 'G60.2' not in G:
    a('G60.2', [('G60.2', 'code de la CIM-10-GM 2024, non une abréviation')], 'Code G60.2', '<p>Code de la CIM-10-GM 2024 : neuropathie associée à une ataxie héréditaire.</p>', 'g60-codes')
if 'G60.3' not in G:
    a('G60.3', [('G60.3', 'code de la CIM-10-GM 2024, non une abréviation')], 'Code G60.3', '<p>Code de la CIM-10-GM 2024 : neuropathie progressive idiopathique.</p>', 'g60-codes')
if 'G60.8' not in G:
    a('G60.8', [('G60.8', 'code de la CIM-10-GM 2024, non une abréviation')], 'Code G60.8', '<p>Code de la CIM-10-GM 2024 : autres neuropathies héréditaires et idiopathiques.</p>', 'g60-codes')
if 'G60.9' not in G:
    a('G60.9', [('G60.9', 'code de la CIM-10-GM 2024, non une abréviation')], 'Code G60.9', '<p>Code de la CIM-10-GM 2024 : neuropathie héréditaire et idiopathique sans précision.</p>', 'g60-codes')
if 'M79.2' not in G:
    a('M79.2', [('M79.2', 'code de la CIM-10-GM 2024, non une abréviation')], 'Code M79.2', '<p>Code de la CIM-10-GM 2024 : névralgie et névrite sans précision.</p>', 'g60-codes')
if 'O26.83' not in G:
    a('O26.83', [('O26.83', 'code de la CIM-10-GM 2024, non une abréviation')], 'Code O26.83', '<p>Code de la CIM-10-GM 2024 : névrite périphérique de la grossesse.</p>', 'g60-codes')
if 'M54.1' not in G:
    a('M54.1', [('M54.1', 'code de la CIM-10-GM 2024, non une abréviation')], 'Code M54.1', '<p>Code de la CIM-10-GM 2024 : radiculite sans précision.</p>', 'g60-codes')
if 'NOBEL' not in G:
    a('NOBEL', [('NOBEL', 'nom d’un laboratoire pharmaceutique, non une abréviation')], 'Nobel Pharma', '<p>Titulaire de l’information professionnelle suisse de la duloxétine lue.</p>', 'g60-duloxetine')
if 'Roussy-Lévy' not in G:
    a('Roussy-Lévy', [('Roussy-Lévy', 'nom propre de deux médecins, non une abréviation')], 'Syndrome de Roussy-Lévy', '<p>Inclusion de G60.0 seulement nommée ; sa clinique n’est pas documentée dans le dossier.</p>', 'g60-codes')
if 'Déjerine-Sottas' not in G:
    a('Déjerine-Sottas', [('Déjerine-Sottas', 'nom propre de deux médecins, non une abréviation')], 'Maladie de Déjerine-Sottas', '<p>Forme sévère à début précoce, incluse en G60.0.</p>', 'g60-mpz')
if 'aminoacyl-ARNt' not in G:
    a('aminoacyl-ARNt', [('aminoacyl-ARNt', 'aminoacide lié à un ARN de transfert')], 'Aminoacyl-ARN de transfert', '<p>Les aminoacyl-ARNt synthétases sont des enzymes impliquées dans des formes axonales de CMT.</p>', 'g60-cmt')
if 'Bernard-Valnet' not in G:
    a('Bernard-Valnet', [('Bernard-Valnet', 'nom propre d’un auteur, non une abréviation')], 'Bernard-Valnet', '<p>Premier auteur d’une revue de la Revue Médicale Suisse (2019).</p>', 'g60-acquises')
if 'Echaniz-Laguna' not in G:
    a('Echaniz-Laguna', [('Echaniz-Laguna', 'nom propre d’un auteur, non une abréviation')], 'Echaniz-Laguna', '<p>Premier auteur d’une revue de la Revue Médicale Suisse (2022).</p>', 'g60-ttr')
if 'Charcot-Marie-Tooth' not in G:
    a('Charcot-Marie-Tooth', [('Charcot-Marie-Tooth', 'noms de trois médecins, non une abréviation')], 'Charcot-Marie-Tooth', '<p>Nom de la neuropathie héréditaire décrite par Charcot, Marie et Tooth, classée en G60.0.</p>', 'g60-cmt')
if 'ClCr' not in G:
    a('ClCr', [('Cl', 'Clairance'), ('Cr', 'de la Créatinine')], 'Clairance de la créatinine', '<p>Estimation du débit de filtration glomérulaire, utilisée pour adapter la dose de prégabaline.</p>', 'g60-pregabaline')
if 'IMAO' not in G:
    a('IMAO', [('I', 'Inhibiteurs de la'), ('M', 'Mono'), ('A', 'Amine'), ('O', 'Oxydase')], 'Inhibiteurs de la monoamine-oxydase', '<p>Classe d’antidépresseurs contre-indiquée avec l’amitriptyline selon son information professionnelle suisse.</p>', 'g60-amitriptyline')
if 'LCR' not in G:
    a('LCR', [('L', 'Liquide'), ('C', 'Cérébro-'), ('R', 'Rachidien')], 'Liquide cérébro-spinal', '<p>Liquide obtenu par ponction lombaire ; sa protéinorachie est un élément de distinction avec la PIDC.</p>', 'g60-pidc')
