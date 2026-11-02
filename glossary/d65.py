from cardio_1 import a, G
# Définitions D65 conditionnelles ; aucun terme global existant écrasé.

if 'CIVD' not in G:
    a('CIVD', [('CIVD', 'Coagulation intravasculaire disséminée')], 'Coagulation intravasculaire disséminée', '<p>Syndrome acquis secondaire, avec activation diffuse, fibrinolyse dérégulée et atteinte endothéliale.</p>', 'd65-classification')

if 'ISTH' not in G:
    a('ISTH', [('ISTH', 'International Society on Thrombosis and Haemostasis')], 'International Society on Thrombosis and Haemostasis', '<p>Société internationale ; définition et score2025 attribués dans le cours.</p>', 'd65-sources')

if 'SIC' not in G:
    a('SIC', [('SIC', 'Coagulopathie induite par le sepsis')], 'Coagulopathie induite par le sepsis', '<p>Sepsis-induced coagulopathy ; total et condition plaquettes+INR nécessaires.</p>', 'd65-sic')

if 'SOFA' not in G:
    a('SOFA', [('SOFA', 'Sequential Organ Failure Assessment')], 'Sequential Organ Failure Assessment', '<p>Évaluation des organes ; quatre domaines retenus pour la composante SIC.</p>', 'd65-sofa')

if 'PT' not in G:
    a('PT', [('PT', 'Temps de prothrombine')], 'Temps de prothrombine', '<p>Le score manifeste utilise son allongement en secondes.</p>', 'd65-pt-inr')

if 'INR' not in G:
    a('INR', [('INR', 'International Normalized Ratio')], 'International Normalized Ratio', '<p>Rapport normalisé ; ne remplace pas directement un temps en secondes.</p>', 'd65-pt-inr')

if 'aPTT' not in G:
    a('aPTT', [('aPTT', 'Temps de thromboplastine partielle activée')], 'Temps de thromboplastine partielle activée', '<p>Examen complémentaire, hors score ISTH manifeste présenté.</p>', 'd65-pt-inr')

if 'HNF' not in G:
    a('HNF', [('HNF', 'Héparine non fractionnée')], 'Héparine non fractionnée', '<p>Anticoagulant aux indications et restrictions propres.</p>', 'd65-heparine')

if 'HBPM' not in G:
    a('HBPM', [('HBPM', 'Héparine de bas poids moléculaire')], 'Héparine de bas poids moléculaire', '<p>Classe distincte du produit HNF détaillé dans le cours.</p>', 'd65-heparine')

if 'TIH' not in G:
    a('TIH', [('TIH', 'Thrombopénie induite par l’héparine')], 'Thrombopénie induite par l’héparine', '<p>Complication nécessitant une démarche propre.</p>', 'd65-tih')

if 'TXA' not in G:
    a('TXA', [('TXA', 'Acide tranexamique')], 'Acide tranexamique', '<p>Antifibrinolytique ; exception spécialisée dans une minorité de CIVD.</p>', 'd65-txa')

if 'TFPI' not in G:
    a('TFPI', [('TFPI', 'Inhibiteur de la voie du facteur tissulaire')], 'Inhibiteur de la voie du facteur tissulaire', '<p>Frein physiologique de la coagulation.</p>', 'd65-tfpi')

if 'NETs' not in G:
    a('NETs', [('NETs', 'Réseaux extracellulaires des neutrophiles')], 'Réseaux extracellulaires des neutrophiles', '<p>Structures impliquées dans les interactions immunité-coagulation.</p>', 'd65-net')

if 'FEU' not in G:
    a('FEU', [('FEU', 'Fibrinogen equivalent units')], 'Fibrinogen equivalent units', '<p>Unités de D-dimères à garder cohérentes avec la méthode.</p>', 'd65-ddimeres')

if 'DDU' not in G:
    a('DDU', [('DDU', 'D-dimer units')], 'D-dimer units', '<p>Expression de D-dimères distincte des FEU.</p>', 'd65-ddimeres')

if 'APL' not in G:
    a('APL', [('APL', 'Leucémie aiguë promyélocytaire')], 'Leucémie aiguë promyélocytaire', '<p>Acute promyelocytic leukemia ; contexte hématologique spécifique.</p>', 'd65-apl')

if 'ATIII' not in G:
    a('ATIII', [('ATIII', 'Antithrombine III')], 'Antithrombine III', '<p>Protéine anticoagulante, indication de concentré non déduite de sa seule baisse.</p>', 'd65-antithrombine')

if 'TACO' not in G:
    a('TACO', [('TACO', 'Surcharge circulatoire associée à la transfusion')], 'Surcharge circulatoire associée à la transfusion', '<p>Mécanisme distinct du TRALI.</p>', 'd65-taco-trali')

if 'TRALI' not in G:
    a('TRALI', [('TRALI', 'Atteinte pulmonaire aiguë associée à la transfusion')], 'Atteinte pulmonaire aiguë associée à la transfusion', '<p>Classification et enquête contextuelles.</p>', 'd65-taco-trali')

if 'MEBEKO' not in G:
    a('MEBEKO', [('MEBEKO', 'Commission des professions médicales')], 'Commission des professions médicales', '<p>Cadre suisse de formation et d’examen.</p>', 'd65-profiles')

if 'SSC' not in G:
    a('SSC', [('SSC', 'Abréviation à contextualiser')], 'Abréviation à contextualiser', '<p>Comité scientifique de l’ISTH ou Surviving Sepsis Campaign selon le titre de source.</p>', 'd65-sources')

if 'ESICM' not in G:
    a('ESICM', [('ESICM', 'European Society of Intensive Care Medicine')], 'European Society of Intensive Care Medicine', '<p>Société européenne partenaire des recommandations sepsis2026.</p>', 'd65-sources')

if 'SCCM' not in G:
    a('SCCM', [('SCCM', 'Society of Critical Care Medicine')], 'Society of Critical Care Medicine', '<p>Partenaire des recommandations internationales conjointes sepsis2026.</p>', 'd65-sources')

if 'OAMal' not in G:
    a('OAMal', [('OAMal', 'Ordonnance sur l’assurance-maladie')], 'Ordonnance sur l’assurance-maladie', '<p>Cadre suisse, sans garantie individuelle de remboursement.</p>', 'd65-sources')

if 'D65' not in G:
    a('D65', [('D65', 'Code CIM-10-GM D65')], 'Code CIM-10-GM D65', '<p>Classification et limites expliquées dans la leçon.</p>', 'd65-classification')

if 'D65.0' not in G:
    a('D65.0', [('D65.0', 'Code CIM-10-GM D65.0')], 'Code CIM-10-GM D65.0', '<p>Classification et limites expliquées dans la leçon.</p>', 'd65-classification')

if 'D65.1' not in G:
    a('D65.1', [('D65.1', 'Code CIM-10-GM D65.1')], 'Code CIM-10-GM D65.1', '<p>Classification et limites expliquées dans la leçon.</p>', 'd65-classification')

if 'D65.2' not in G:
    a('D65.2', [('D65.2', 'Code CIM-10-GM D65.2')], 'Code CIM-10-GM D65.2', '<p>Classification et limites expliquées dans la leçon.</p>', 'd65-classification')

if 'D65.9' not in G:
    a('D65.9', [('D65.9', 'Code CIM-10-GM D65.9')], 'Code CIM-10-GM D65.9', '<p>Classification et limites expliquées dans la leçon.</p>', 'd65-classification')

if 'P60' not in G:
    a('P60', [('P60', 'Code CIM-10-GM P60')], 'Code CIM-10-GM P60', '<p>Classification et limites expliquées dans la leçon.</p>', 'd65-classification')

if 'XIII' not in G:
    a('XIII', [('XIII', 'Treize, facteur de coagulation')], 'Treize, facteur de coagulation', '<p>Le facteur XIII activé stabilise la fibrine.</p>', 'd65-coagulation')

if 'CSV' not in G:
    a('CSV', [('CSV', 'Comma-separated values')], 'Comma-separated values', '<p>Format de données tabulaires du référentiel OFS cité.</p>', 'd65-sources')

if 'XML' not in G:
    a('XML', [('XML', 'Extensible Markup Language')], 'Extensible Markup Language', '<p>Format structuré de texte ou de classification ; ne constitue pas une recommandation clinique.</p>', 'd65-sources')

if 'FPV' not in G:
    a('FPV', [('FPV', 'Forfaitpauschalenvereinbarung')], 'Forfaitpauschalenvereinbarung', '<p>Cadre allemand de facturation mentionné dans la source de classification, non transposé à la Suisse.</p>', 'd65-classification')

if 'CAHT' not in G:
    a('CAHT', [('CAHT', 'Groupe CAHT')], 'Groupe CAHT', '<p>Société ayant rendu disponible une copie publique de la communication primaire ISTH2025 ; accès distinct de l’auteur du texte.</p>', 'd65-sources')

if 'SHA' not in G:
    a('SHA', [('SHA', 'Empreinte cryptographique')], 'Empreinte cryptographique', '<p>Élément de provenance des fichiers, sans valeur de certification médicale.</p>', 'd65-sources')

if 'DOI' not in G:
    a('DOI', [('DOI', 'Digital Object Identifier')], 'Digital Object Identifier', '<p>Identifiant bibliographique stable d’une publication.</p>', 'd65-sources')

if 'APC' not in G:
    a('APC', [('APC', 'Protéine C activée')], 'Protéine C activée', '<p>Protéine physiologique ; ancien médicament recombinant retiré, pas traitement actuel proposé.</p>', 'd65-coagulation')

if 'AT' not in G:
    a('AT', [('AT', 'Antithrombine')], 'Antithrombine', '<p>Frein physiologique de la coagulation.</p>', 'd65-antithrombine')

if 'TM' not in G:
    a('TM', [('TM', 'Thrombomoduline')], 'Thrombomoduline', '<p>Composant de régulation endothéliale ; mention de recherche, sans routine thérapeutique suisse déduite.</p>', 'd65-coagulation')

if 'CI' not in G:
    a('CI', [('CI', 'Contre-indication')], 'Contre-indication', '<p>Situation où le produit ne doit pas être utilisé selon sa fiche.</p>', 'd65-fi')

if 'PPH' not in G:
    a('PPH', [('PPH', 'Hémorragie du post-partum')], 'Hémorragie du post-partum', '<p>Postpartum haemorrhage ; contexte distinct d’une CIVD générale.</p>', 'd65-causes')

if 'ATO' not in G:
    a('ATO', [('ATO', 'Trioxyde d’arsenic')], 'Trioxyde d’arsenic', '<p>Abréviation apparaissant dans le périmètre de la source APL antérieure ; aucune posologie proposée dans ce cours.</p>', 'd65-apl')

if 'DGGG' not in G:
    a('DGGG', [('DGGG', 'Société allemande de gynécologie et d’obstétrique')], 'Société allemande de gynécologie et d’obstétrique', '<p>Partenaire de la directive péripartale citée.</p>', 'd65-sources')

if 'OEGGG' not in G:
    a('OEGGG', [('OEGGG', 'Société autrichienne de gynécologie et d’obstétrique')], 'Société autrichienne de gynécologie et d’obstétrique', '<p>Partenaire de la directive péripartale citée.</p>', 'd65-sources')

if 'SGGG' not in G:
    a('SGGG', [('SGGG', 'Société suisse de gynécologie et d’obstétrique')], 'Société suisse de gynécologie et d’obstétrique', '<p>Partenaire suisse de la directive péripartale citée.</p>', 'd65-sources')

if 'RAI' not in G:
    a('RAI', [('RAI', 'Recherche d’anticorps irréguliers')], 'Recherche d’anticorps irréguliers', '<p>Examen immunohématologique intégré à la sécurité transfusionnelle selon procédure locale.</p>', 'd65-transfusion')

if 'O2' not in G:
    a('O2', [('O2', 'Oxygène')], 'Oxygène', '<p>Notation moléculaire dans une référence, sans dose d’oxygène déduite.</p>', 'd65-sources')

if '01-A01' not in G:
    a('01-A01', [('01-A01', 'Fragment d’identifiant de document')], 'Fragment d’identifiant de document', '<p>Référence administrative Swissmedic, pas paramètre clinique.</p>', 'd65-sources')

if 'NC' not in G:
    a('NC', [('NC', 'Non commercial')], 'Non commercial', '<p>Mention de licence d’une source textuelle ; droits des images vérifiés séparément.</p>', 'd65-sources')

if 'SEM' not in G:
    a('SEM', [('SEM', 'Microscopie électronique à balayage')], 'Microscopie électronique à balayage', '<p>Scanning electron microscopy ; technique de l’original Wellcome.</p>', 'd65-sources')
