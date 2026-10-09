# Glossaire MEDINA — chapitre S45 Lésions traumatiques des vaisseaux des membres (C-01-Cardiologie)
from cardio_1 import a, G

a('MESS',[('M','Mangled (broyé)'),('E','Extremity (membre)'),('S','Severity (gravité)'),('S','Score')],'Mangled Extremity Severity Score (score de gravité du membre broyé)',
 '<p>Score qui additionne l’énergie du traumatisme, l’ischémie, le choc et l’âge pour prédire l’amputation ; l’ESVS 2025 déconseille de fonder la décision sur un tel score.</p>','s45-scores')
a('PROOVIT',[('PRO','PROspective'),('O','Observational'),('V','Vascular'),('I','Injury'),('T','Treatment')],'Registre PROspective Observational Vascular Injury Treatment (registre prospectif observationnel du traitement des lésions vasculaires)',
 '<p>Registre nord-américain des lésions vasculaires traumatiques ; il n’a pas montré d’augmentation des thromboses de réparation vasculaire majeure sous acide tranexamique.</p>')
codes=[('S45.0','lésion de l’artère axillaire'),('S45.1','lésion de l’artère brachiale'),('S45.2','lésion de la veine axillaire ou brachiale'),('S45.3','lésion des veines superficielles de l’épaule et du bras'),('S45.7','lésion de plusieurs vaisseaux de l’épaule et du bras'),('S45.8','lésion d’autres vaisseaux de l’épaule et du bras'),('S45.9','lésion d’un vaisseau non précisé de l’épaule et du bras'),
('S55.0','lésion de l’artère ulnaire à l’avant-bras'),('S55.1','lésion de l’artère radiale à l’avant-bras'),('S55.2','lésion de veines de l’avant-bras'),
('S65.0','lésion de l’artère ulnaire au poignet et à la main'),('S65.1','lésion de l’artère radiale au poignet et à la main'),('S65.2','lésion de l’arcade palmaire superficielle'),('S65.3','lésion de l’arcade palmaire profonde'),('S65.4','lésion de vaisseaux du pouce'),('S65.5','lésion de vaisseaux d’autres doigts'),
('S75.0','lésion de l’artère fémorale'),('S75.1','lésion de la veine fémorale à la hanche et à la cuisse'),('S75.2','lésion de la grande veine saphène à la hanche et à la cuisse'),
('S85.0','lésion de l’artère poplitée'),('S85.1','lésion de l’artère tibiale antérieure ou postérieure'),('S85.2','lésion de l’artère fibulaire'),('S85.3','lésion de la grande veine saphène à la jambe'),('S85.4','lésion de la petite veine saphène à la jambe'),('S85.5','lésion de la veine poplitée'),
('S95.0','lésion de l’artère dorsale du pied'),('S95.1','lésion de l’artère plantaire'),('S95.2','lésion de veines du dos du pied')]
for code,lib in codes:
    a(code,[(code,'code de la classification internationale des maladies, '+lib)],lib[0].upper()+lib[1:]+' (CIM-10-GM 2024)','<p>Sous-catégorie qui code le vaisseau atteint dans ce segment de membre.</p>','s45-codage')
