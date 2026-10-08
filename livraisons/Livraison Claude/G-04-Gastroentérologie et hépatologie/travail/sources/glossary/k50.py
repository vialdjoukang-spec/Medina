# Glossaire MEDINA — K50 Maladie de Crohn (G-04-Gastroentérologie et hépatologie), rédaction Claude du 08.10.2026
from cardio_1 import a, G

def t(k, lit, full, d='', ref=None):
    a(k, lit, full, d, ref)

# Libellé du fragment (même format que glossary/fragments_medina.py ; à déplacer dans ce fichier lors de l’injection)
a('G-04-Gastroentérologie et hépatologie', [('G', 'Gastroentérologie (initiale de la spécialité)'), ('04', 'quatrième fragment dans l’ordre de production'), ('Gastroentérologie et hépatologie', 'nom littéral du fragment')], 'Fragment G-04-Gastroentérologie et hépatologie de MEDINA', '<p>Quatrième fragment de production de MEDINA, qui réunit les cours de gastroentérologie et d’hépatologie (organisation/fragments.json).</p>')

# Sociétés, cohortes, consensus
a('ECCO', [('E', 'European'), ('C', 'Crohn’s and'), ('C', 'Colitis'), ('O', 'Organisation')], 'European Crohn’s and Colitis Organisation (Organisation européenne de la maladie de Crohn et de la colite)', '<p>Société savante européenne des maladies inflammatoires chroniques de l’intestin. Elle publie les lignes directrices de référence en Europe, notamment sur le traitement médical et chirurgical de la maladie de Crohn (2024).</p>')
a('ESGAR', [('E', 'European'), ('S', 'Society of'), ('G', 'Gastrointestinal and'), ('A', 'Abdominal'), ('R', 'Radiology')], 'European Society of Gastrointestinal and Abdominal Radiology (Société européenne de radiologie digestive et abdominale)', '<p>Société savante coauteure avec ECCO des lignes directrices sur le diagnostic et la surveillance des maladies inflammatoires chroniques de l’intestin (2019, mise à jour 2025).</p>')
a('ECCO-ESGAR', [('ECCO', 'European Crohn’s and Colitis Organisation'), ('ESGAR', 'European Society of Gastrointestinal and Abdominal Radiology')], 'Lignes directrices conjointes ECCO et ESGAR', '<p>Lignes directrices communes des deux sociétés sur l’évaluation diagnostique des maladies inflammatoires chroniques de l’intestin (2019), remplacées en 2025 par une version élargie à la pathologie et à l’échographie intestinale.</p>')
a('MICI', [('M', 'Maladies'), ('I', 'Inflammatoires'), ('C', 'Chroniques de'), ('I', 'l’Intestin')], 'Maladies inflammatoires chroniques de l’intestin', '<p>Groupe formé par la maladie de Crohn, la rectocolite hémorragique et les colites inclassables. Environ 0,4 % de la population suisse est atteinte (Schoepfer et Safroneeva, 2019).</p>')
t('STRIDE-II', [('STRIDE', 'Selecting Therapeutic Targets in Inflammatory Bowel Disease (choix des cibles thérapeutiques dans les maladies inflammatoires chroniques de l’intestin ; acronyme arrangé, non strictement lettre à lettre)'), ('II', 'deuxième version')], 'Consensus STRIDE-II (2021)', '<p>Consensus de l’International Organization for the Study of Inflammatory Bowel Diseases qui fixe les cibles du traitement par cible : normalisation de la protéine C-réactive et de la calprotectine à court terme, cicatrisation endoscopique à long terme.</p>', 'k50-t2t')

# Scores et noms propres
a('SES-CD', [('S', 'Simple'), ('E', 'Endoscopic'), ('S', 'Score for'), ('CD', 'Crohn’s Disease (maladie de Crohn)')], 'Score endoscopique simplifié de la maladie de Crohn', '<p>Score de 0 à 56 (5 segments × 4 items notés de 0 à 3). Rémission 0 à 2, activité légère 3 à 6, modérée 7 à 15, sévère au-delà.</p>', 'k50-sescd')
a('Harvey-Bradshaw', [('Harvey-Bradshaw', 'nom propre : Ronald F. Harvey et J. M. Bradshaw, auteurs de l’indice en 1980')], 'Indice de Harvey-Bradshaw', '<p>Score clinique simple de l’activité de la maladie de Crohn : moins de 5, rémission ; plus de 16, activité sévère.</p>', 'k50-hbi')
for c, d in [('L1', 'iléale'), ('L2', 'colique'), ('L3', 'iléocolique'), ('L4', 'digestive haute (modificateur)')]:
    a(c, [('L', 'Localisation'), (c[1], 'classe ' + c[1] + ' de Montréal : ' + d)], 'Localisation ' + d + ' de la maladie de Crohn (classification de Montréal)', '<p>Classe de localisation de la classification de Montréal (Satsangi, Gut 2006).</p>', 'k50-montreal')

# Gènes, molécules, cytokines
a('NOD2', [('N', 'Nucleotide-binding'), ('O', 'Oligomerization'), ('D', 'Domain-containing protein'), ('2', '2')], 'Gène NOD2 (protéine 2 à domaine d’oligomérisation liant les nucléotides)', '<p>Capteur intracellulaire du muramyl dipeptide bactérien ; ses variants perte de fonction sont le principal facteur génétique de la maladie de Crohn iléale (chromosome 16).</p>', 'k50-nod2')
a('ATG16L1', [('ATG', 'AuTophaGy-related (lié à l’autophagie)'), ('16', '16'), ('L1', 'Like 1 (apparenté 1)')], 'Gène ATG16L1 (autophagie)', '<p>Gène de l’autophagie dont un variant réduit la destruction des bactéries phagocytées et la fonction des cellules de Paneth ; associé à la maladie de Crohn.</p>')
a('IRGM', [('I', 'Immunity-'), ('R', 'Related'), ('G', 'GTPase family'), ('M', 'M')], 'Gène IRGM (GTPase de la famille M liée à l’immunité)', '<p>Gène de l’autophagie associé à la maladie de Crohn.</p>')
a('IL23R', [('IL', 'InterLeukine'), ('23', '23'), ('R', 'Récepteur')], 'Gène du récepteur de l’interleukine 23', '<p>Certains variants protègent contre la maladie de Crohn, ce qui soutient le rôle causal de la voie IL-23.</p>', 'k50-il23')
a('IL-23', [('IL', 'InterLeukine'), ('23', '23')], 'Interleukine 23', '<p>Cytokine formée des sous-unités p19 et p40, qui maintient les lymphocytes Th17. Cible de l’ustékinumab (p40), du risankizumab, du guselkumab et du mirikizumab (p19).</p>', 'k50-il23')
a('IL-22', [('IL', 'InterLeukine'), ('22', '22')], 'Interleukine 22', '<p>Cytokine des lymphocytes Th17 qui agit sur l’épithélium intestinal ; son taux baisse sous risankizumab.</p>', 'k50-il23')
a('IgG1', [('Ig', 'Immunoglobuline'), ('G', 'de classe G'), ('1', 'sous-classe 1')], 'Immunoglobuline G de sous-classe 1', '<p>Format de la plupart des anticorps monoclonaux thérapeutiques ; il traverse activement le placenta, surtout au troisième trimestre.</p>')
a('JAK1', [('JAK', 'Janus Kinase'), ('1', '1')], 'Janus kinase 1', '<p>Kinase associée aux récepteurs de nombreuses cytokines ; cible préférentielle de l’upadacitinib.</p>', 'k50-jak')
a('MAdCAM-1', [('M', 'Mucosal'), ('Ad', 'Addressin'), ('C', 'Cell'), ('A', 'Adhesion'), ('M', 'Molecule'), ('1', '1')], 'Molécule d’adhésion cellulaire de l’adressine muqueuse 1', '<p>Molécule de l’endothélium des veinules digestives, ligand de l’intégrine α4β7 ; son interaction est bloquée par le védolizumab.</p>', 'k50-madcam')
a('ASCA', [('A', 'Anti-'), ('S', 'Saccharomyces'), ('C', 'Cerevisiae'), ('A', 'Antibodies (anticorps)')], 'Anticorps anti-Saccharomyces cerevisiae', '<p>Anticorps plus fréquents dans la maladie de Crohn ; sensibilité insuffisante pour le diagnostic.</p>')

# Codes CIM-10-GM 2024
for c, d in [('K50.0', 'Maladie de Crohn de l’intestin grêle'), ('K50.1', 'Maladie de Crohn du gros intestin'), ('K50.8', 'Autres formes de la maladie de Crohn (regroupement de K50.80 à K50.88)'), ('K50.80', 'Maladie de Crohn gastrique'), ('K50.81', 'Maladie de Crohn de l’œsophage'), ('K50.82', 'Maladie de Crohn de l’œsophage et du tractus gastro-intestinal sur plusieurs segments, dont intestin grêle et gros intestin'), ('K50.88', 'Autres formes de la maladie de Crohn'), ('K50.9', 'Maladie de Crohn, sans précision')]:
    a(c, [(c, 'code de la Classification internationale des maladies, 10e révision, modification allemande')], d, '<p>Code CIM-10-GM 2024 (BfArM, bloc K50-K52).</p>')

# Essais cliniques (noms d’essais, non développables strictement lettre à lettre)
for k, full, d in [
    ('PROFILE', 'PRedicting Outcomes For Crohn’s disease using a moLecular biomarker (acronyme arrangé, non strictement lettre à lettre)', 'Essai britannique (2024) : infliximab et immunomodulateur d’emblée contre stratégie progressive accélérée chez 386 adultes nouvellement diagnostiqués ; rémission soutenue 79 % contre 15 %.'),
    ('SEQUENCE', 'nom d’essai, non acronyme', 'Essai comparant risankizumab et ustékinumab après échec d’un anti-TNF ; supériorité du risankizumab.'),
    ('SEAVUE', 'nom d’essai écrit en capitales ; développement non vérifié pour ce cours', 'Essai comparant ustékinumab et adalimumab en monothérapie chez des patients naïfs de biothérapie ; efficacité comparable.'),
    ('SONIC', 'Study Of biologic and immunomodulator Naive patients In Crohn’s disease (acronyme arrangé, non strictement lettre à lettre)', 'Essai (2010) : infliximab et azathioprine supérieurs à chacun seul pour la rémission sans corticoïde.'),
    ('ACCENT', 'nom d’essai écrit en capitales ; développement non vérifié pour ce cours', 'Essais ACCENT I (maladie luminale) et ACCENT II (fistules) de l’entretien par infliximab.'),
    ('CLASSIC', 'nom d’essai écrit en capitales ; développement non vérifié pour ce cours', 'Essai d’induction par adalimumab.'),
    ('CHARM', 'nom d’essai écrit en capitales ; développement non vérifié pour ce cours', 'Essai d’entretien par adalimumab.'),
    ('GEMINI', 'nom d’essai, non acronyme', 'Programme d’essais du védolizumab (GEMINI II et III pour la maladie de Crohn).'),
    ('UNITI', 'nom d’essai, non acronyme', 'Programme d’essais de l’ustékinumab dans la maladie de Crohn.'),
    ('ADVANCE', 'nom d’essai, non acronyme', 'Essai d’induction par risankizumab dans la maladie de Crohn.'),
    ('MOTIVATE', 'nom d’essai, non acronyme', 'Essai d’induction par risankizumab après échec d’une biothérapie.'),
    ('FORTIFY', 'nom d’essai, non acronyme', 'Essai d’entretien par risankizumab dans la maladie de Crohn.'),
    ('GALAXI', 'nom d’essai, non acronyme', 'Programme d’essais du guselkumab avec induction intraveineuse dans la maladie de Crohn.'),
    ('GRAVITI', 'nom d’essai, non acronyme', 'Essai du guselkumab avec induction sous-cutanée dans la maladie de Crohn.'),
    ('U-EXCEL', 'nom d’essai (U pour upadacitinib), non acronyme', 'Essai d’induction par upadacitinib dans la maladie de Crohn.'),
    ('U-EXCEED', 'nom d’essai (U pour upadacitinib), non acronyme', 'Essai d’induction par upadacitinib après échec de biothérapie.'),
    ('U-ENDURE', 'nom d’essai (U pour upadacitinib), non acronyme', 'Essai d’entretien par upadacitinib dans la maladie de Crohn.')]:
    t(k, [(k, full)], 'Essai ' + k, '<p>' + d + '</p>')
