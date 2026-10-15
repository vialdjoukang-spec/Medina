from cardio_1 import a, G
# E00 — Syndrome d’insuffisance thyroïdienne congénitale (E-06-Endocrinologie et métabolisme). Entrées conditionnelles : aucun terme existant dans G n’est écrasé.
if 'ENDO-ERN' not in G:
    a('ENDO-ERN', [('ENDO','Endocrine (endocrinien)'),('-',''),('E','European (européen)'),('R','Reference (de référence)'),('N','Network (réseau)')], 'Réseau européen de référence pour les maladies endocriniennes rares', '<p>ENDO-ERN est le réseau européen de référence dont le consensus 2020-2021 sur l’hypothyroïdie congénitale, avalisé par la Société européenne d’endocrinologie pédiatrique et la Société européenne d’endocrinologie, est la source des seuils de dépistage, de traitement et de surveillance du nouveau-né hypothyroïdien utilisés dans ce cours.</p>', 'e00-sources-guides')
if 'ESPE' not in G:
    a('ESPE', [('E','European (européenne)'),('S','Society (société)'),('P','for Paediatric (d’endocrinologie pédiatrique)'),('E','Endocrinology (endocrinologie)')], 'Société européenne d’endocrinologie pédiatrique', '<p>L’ESPE a avalisé, avec la Société européenne d’endocrinologie, le consensus ENDO-ERN 2020-2021 sur l’hypothyroïdie congénitale.</p>', 'e00-sources-guides')
if 'UNICEF' not in G:
    a('UNICEF', [('UNICEF','sigle anglais historique United Nations International Children’s Emergency Fund, conservé comme nom propre ; en français, Fonds des Nations unies pour l’enfance')], 'Fonds des Nations unies pour l’enfance', '<p>L’UNICEF est coauteur, avec l’OMS et l’ICCIDD, du guide 2007 d’évaluation des troubles dus à la carence en iode, qui fournit les besoins en iode et les échelles d’iodurie.</p>', 'e00-sources-guides')
if 'ICCIDD' not in G:
    a('ICCIDD', [('I','International (international)'),('CC','Council (conseil) for the Control of'),('I','Iodine (de l’iode)'),('D','Deficiency (carence)'),('D','Disorders (troubles)')], 'Conseil international pour la lutte contre les troubles dus à la carence en iode', '<p>L’ICCIDD est coauteur, avec l’OMS et l’UNICEF, du guide 2007 d’évaluation des troubles dus à la carence en iode.</p>', 'e00-sources-guides')
if 'TDCI' not in G:
    a('TDCI', [('T','Troubles'),('D','Dus à la'),('C','Carence en'),('I','Iode')], 'Troubles dus à la carence en iode', '<p>Les TDCI regroupent le goitre, l’hypothyroïdie, les avortements, la mortinatalité, les anomalies congénitales, la mortalité périnatale et infantile, l’altération des fonctions mentales et le retard du développement physique ; le crétinisme endémique en est l’expression la plus sévère.</p>', 'e00-tdci')
if 'fT4' not in G:
    a('fT4', [('f','free (libre)'),('T4','Thyroxine, tétra-iodothyronine')], 'Thyroxine libre', '<p>La fT4 est la fraction de thyroxine non liée aux protéines de transport, exprimée en pmol/l. Associée à la TSH, elle permet de distinguer une hypothyroïdie primaire d’une hypothyroïdie centrale et de classer sa sévérité chez le nouveau-né.</p>', 'e00-ft4')
if 'QI' not in G:
    a('QI', [('Q','Quotient'),('I','Intellectuel')], 'Quotient intellectuel', '<p>Le quotient intellectuel mesure le niveau cognitif par rapport à une population de référence. Dans l’enquête thaïlandaise, sa moyenne était de 30,8 chez les sujets atteints de crétinisme endémique ; une valeur inférieure à 70 définit la déficience intellectuelle dans les données sur l’hypothyroïdie congénitale traitée.</p>')
for _c, _t, _w in (('E00.0','type neurologique','e00-sous-types'),('E00.1','type myxœdémateux','e00-sous-types'),('E00.2','type mixte','e00-sous-types'),('E00.9','sans précision','e00-sous-types')):
    if _c not in G:
        a(_c, [('E','chapitre des maladies endocriniennes, nutritionnelles et métaboliques'),('00','catégorie du syndrome d’insuffisance thyroïdienne congénitale'),(_c[3:], 'sous-catégorie : ' + _t)], 'Sous-code CIM-10-GM 2024 ' + _c + ', ' + _t, '<p>' + _c + ' désigne, dans la CIM-10-GM 2024, le syndrome d’insuffisance thyroïdienne congénitale de ' + _t + '.</p>', _w)
for _c, _t in (('E03.0','hypothyroïdie congénitale avec goitre diffus'),('E03.1','hypothyroïdie congénitale sans goitre')):
    if _c not in G:
        a(_c, [('E','chapitre des maladies endocriniennes, nutritionnelles et métaboliques'),(_c[1:3],'catégorie'),(_c[3:], 'sous-catégorie')], 'Sous-code CIM-10-GM 2024 ' + _c, '<p>' + _c + ' est un sous-code de la classification suisse pour les hypothyroïdies congénitales qui ne relèvent pas de la carence iodée et ne sont donc pas classées en E00.</p>')
if 'AG' not in G:
    a('AG', [('A','Aktien'),('G','gesellschaft (société anonyme)')], 'Aktiengesellschaft, société anonyme', '<p>AG est la forme juridique d’une société anonyme de droit suisse ; elle figure ici dans la raison sociale du titulaire de l’autorisation de l’information professionnelle Euthyrox®.</p>')
