from cardio_1 import a, G
# Définitions D62 conditionnelles ; aucun terme global existant écrasé.

if 'TXA' not in G:
    a('TXA', [('TXA', 'Acide tranexamique')], 'Acide tranexamique', '<p>Antifibrinolytique dont indication, délai et contre-indications dépendent du contexte.</p>', 'd62-txa')

if 'PCC' not in G:
    a('PCC', [('PCC', 'Concentré de complexe prothrombinique')], 'Concentré de complexe prothrombinique', '<p>En anglais prothrombin complex concentrate ; apport de facteurs précis, non de globules rouges.</p>', 'd62-pcc')

if 'RAI' not in G:
    a('RAI', [('RAI', 'Recherche d’anticorps irréguliers')], 'Recherche d’anticorps irréguliers', '<p>Examen immunohématologique intégré à la sécurité transfusionnelle selon procédure locale.</p>', 'd62-compatibilite')

if 'TACO' not in G:
    a('TACO', [('TACO', 'Surcharge circulatoire associée à la transfusion')], 'Surcharge circulatoire associée à la transfusion', '<p>En anglais transfusion associated circulatory overload ; mécanisme de surcharge à distinguer duTRALI.</p>', 'd62-taco-trali')

if 'TRALI' not in G:
    a('TRALI', [('TRALI', 'Atteinte pulmonaire aiguë associée à la transfusion')], 'Atteinte pulmonaire aiguë associée à la transfusion', '<p>En anglais transfusion related acute lung injury ; définition datée et diagnostic contextualisé.</p>', 'd62-taco-trali')

if 'ESGE' not in G:
    a('ESGE', [('ESGE', 'Société européenne d’endoscopie gastro-intestinale')], 'Société européenne d’endoscopie gastro-intestinale', '<p>European Society of Gastrointestinal Endoscopy ; directive2026 utilisée pour le saignement haut non variqueux.</p>', 'd62-sources')

if 'SGGG' not in G:
    a('SGGG', [('SGGG', 'Société suisse de gynécologie et d’obstétrique')], 'Société suisse de gynécologie et d’obstétrique', '<p>Participe à la directive péripartale2022 avec les sociétés allemande et autrichienne.</p>', 'd62-sources')

if 'DGGG' not in G:
    a('DGGG', [('DGGG', 'Société allemande de gynécologie et d’obstétrique')], 'Société allemande de gynécologie et d’obstétrique', '<p>Partenaire de la directive péripartale2022.</p>', 'd62-sources')

if 'OEGGG' not in G:
    a('OEGGG', [('OEGGG', 'Société autrichienne de gynécologie et d’obstétrique')], 'Société autrichienne de gynécologie et d’obstétrique', '<p>Partenaire de la directive péripartale2022.</p>', 'd62-sources')

if 'MCV' not in G:
    a('MCV', [('MCV', 'Volume globulaire moyen')], 'Volume globulaire moyen', '<p>Mean corpuscular volume ; taille moyenne des hématies.</p>', 'd62-indices')

if 'MCH' not in G:
    a('MCH', [('MCH', 'Teneur corpusculaire moyenne en hémoglobine')], 'Teneur corpusculaire moyenne en hémoglobine', '<p>Mean corpuscular hemoglobin ; quantité moyenne par hématie.</p>', 'd62-indices')

if 'MCHC' not in G:
    a('MCHC', [('MCHC', 'Concentration corpusculaire moyenne en hémoglobine')], 'Concentration corpusculaire moyenne en hémoglobine', '<p>Mean corpuscular hemoglobin concentration ; rapportée au volume érythrocytaire.</p>', 'd62-indices')

if 'ATIII' not in G:
    a('ATIII', [('ATIII', 'AntithrombineIII')], 'AntithrombineIII', '<p>Protéine de régulation de la coagulation ; absence dansOctaplex et restrictions spécifiques de saFI.</p>', 'd62-pcc')

if 'MEBEKO' not in G:
    a('MEBEKO', [('MEBEKO', 'Commission des professions médicales')], 'Commission des professions médicales', '<p>Autorité suisse ; exigences de l’examen2026 distinguées dePROFILES2.</p>', 'd62-profiles')

if 'SMPR' not in G:
    a('SMPR', [('SMPR', 'Service de médecine de premier recours')], 'Service de médecine de premier recours', '<p>ServiceHUG auteur de la stratégie sur les anémies.</p>', 'd62-sources')

if 'S2k' not in G:
    a('S2k', [('S2k', 'Niveau S2k de directive AWMF')], 'Niveau S2k de directive AWMF', '<p>Directive fondée sur un consensus structuré ; ne se confond pas avec un niveauS3.</p>', 'd62-sources')

if 'CI' not in G:
    a('CI', [('CI', 'Contre-indication')], 'Contre-indication', '<p>Situation où le produit ne doit pas être utilisé selon saFI.</p>', 'd62-fi')

if 'PPH' not in G:
    a('PPH', [('PPH', 'Hémorragie du post-partum')], 'Hémorragie du post-partum', '<p>Postpartum haemorrhage dans les textes internationaux.</p>', 'd62-postpartum')

if 'O2' not in G:
    a('O2', [('O2', 'Oxygène')], 'Oxygène', '<p>Notation moléculaire ; quantité de transporteurs et saturation ne sont pas identiques.</p>', 'd62-oxygene')

if '01-A01' not in G:
    a('01-A01', [('01-A01', 'Fragment d’identifiant documentaire')], 'Fragment d’identifiant documentaire', '<p>Partie de la référence administrativeSwissmedic, pas paramètre clinique.</p>', 'd62-sources')

if 'NC' not in G:
    a('NC', [('NC', 'Non commercial')], 'Non commercial', '<p>Clause de licence d’une source textuelle ; les photographies reprises ont leurs droits propres.</p>', 'd62-sources')

if 'ISBN' not in G:
    a('ISBN', [('ISBN', 'Numéro international normalisé du livre')], 'Numéro international normalisé du livre', '<p>Identifiant bibliographique, non acronyme clinique.</p>', 'd62-sources')

if 'OAMal' not in G:
    a('OAMal', [('OAMal', 'Ordonnance sur l’assurance-maladie')], 'Ordonnance sur l’assurance-maladie', '<p>Cadre suisse ; aucune garantie individuelle de remboursement donnée par le cours.</p>', 'd62-sources')

if 'D62' not in G:
    a('D62', [('D62', 'Code CIM-10-GM D62')], 'Code CIM-10-GM D62', '<p>Code de classification, pas acronyme clinique ; portée et exclusions expliquées dans la leçon.</p>', 'd62-classification')

if 'D50.0' not in G:
    a('D50.0', [('D50.0', 'Code CIM-10-GM D50.0')], 'Code CIM-10-GM D50.0', '<p>Code de classification, pas acronyme clinique ; portée et exclusions expliquées dans la leçon.</p>', 'd62-classification')

if 'P61.3' not in G:
    a('P61.3', [('P61.3', 'Code CIM-10-GM P61.3')], 'Code CIM-10-GM P61.3', '<p>Code de classification, pas acronyme clinique ; portée et exclusions expliquées dans la leçon.</p>', 'd62-classification')
