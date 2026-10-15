from cardio_1 import a, G
# E35 — Anomalies endocriniennes au cours de maladies classées ailleurs (E-06-Endocrinologie et métabolisme). Entrées conditionnelles : aucun terme existant dans G n’est écrasé.
if 'MSH' not in G:
    a('MSH', [('M','Melanocyte (mélanocytes)'),('S','Stimulating (stimulante)'),('H','Hormone (hormone)')], 'Hormone mélanotrope (hormone stimulant les mélanocytes)', '<p>La MSH stimule la synthèse de mélanine par les mélanocytes. Dans l’insuffisance surrénalienne primaire, l’excès d’hormone adrénocorticotrope s’accompagne d’une activation parallèle de la MSH, d’où la coloration bronzée de la peau et des plis (Flück 2023).</p>', 'e35-msh')
if 'BfArM' not in G:
    a('BfArM', [('Bf','Bundesinstitut für (institut fédéral pour)'),('Ar','Arzneimittel (les médicaments)'),('M','und Medizinprodukte (et les dispositifs médicaux)')], 'Institut fédéral allemand des médicaments et des dispositifs médicaux', '<p>Cet institut publie la classification CIM-10-GM (version allemande) ; ses notes d’inclusion et de code dague ont été lues pour la catégorie E35.</p>', 'e35-dague')
_codes = [
 ('A18.7', 'code étiologique (dague †) associé à la maladie d’Addison tuberculeuse, d’après les notes de la CIM-10-GM 2024', 'Ce code classe la tuberculose de la surrénale par son étiologie ; il se combine avec E35.1* pour la manifestation endocrinienne.'),
 ('A18.8', 'code étiologique (dague †) associé à la tuberculose de la thyroïde, d’après les notes de la CIM-10-GM 2024', 'Ce code classe la tuberculose thyroïdienne par son étiologie ; il se combine avec E35.0* pour la manifestation endocrinienne.'),
 ('A39.1', 'code étiologique (dague †) associé au syndrome de Waterhouse-Friderichsen méningococcique, d’après les notes de la CIM-10-GM 2024', 'Ce code classe le syndrome par son étiologie méningococcique ; il se combine avec E35.1* pour l’atteinte surrénalienne.'),
 ('E35.0', 'sous-catégorie astérisque de la CIM-10-GM 2024 : anomalies de la glande thyroïde au cours de maladies classées ailleurs', 'Cette manifestation thyroïdienne ne s’emploie jamais seule ; elle inclut la tuberculose de la thyroïde (A18.8†).'),
 ('E35.1', 'sous-catégorie astérisque de la CIM-10-GM 2024 : anomalies de la glande surrénale au cours de maladies classées ailleurs', 'Cette manifestation surrénalienne ne s’emploie jamais seule ; elle inclut la maladie d’Addison tuberculeuse (A18.7†) et le syndrome de Waterhouse-Friderichsen méningococcique (A39.1†).'),
 ('E35.8', 'sous-catégorie astérisque de la CIM-10-GM 2024 : anomalies d’autres glandes endocrines au cours de maladies classées ailleurs', 'Cette sous-catégorie ne porte, dans la version 2024, aucune inclusion, exclusion ni code dague.'),
]
for _k, _full, _d in _codes:
    if _k not in G:
        a(_k, [(_k, 'code de classification, non une abréviation')], _full[0].upper() + _full[1:], '<p>' + _d + '</p>', 'e35-dague')
if 'TI-RADS' not in G:
    a('TI-RADS', [('TI','Thyroid Imaging (imagerie de la thyroïde)'),('RADS','Reporting And Data System (système de rapport et de données)')], 'Système de rapport et de données de l’imagerie thyroïdienne', '<p>Ce système classe un nodule thyroïdien à l’échographie par catégories de suspicion ; la catégorie 4 est rapportée dans les cas de tuberculose thyroïdienne pris pour un néoplasme.</p>', 'e35-tb-thyro')
if 'Waterhouse-Friderichsen' not in G:
    a('Waterhouse-Friderichsen', [('Waterhouse','nom d’un des deux auteurs éponymes'),('Friderichsen','nom du second auteur éponyme')], 'Syndrome de Waterhouse-Friderichsen', '<p>Le syndrome de Waterhouse-Friderichsen est un état septique fulminant avec hémorragie surrénalienne bilatérale, classiquement méningococcique.</p>', 'e35-swf')
