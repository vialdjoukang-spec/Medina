# Glossaire MEDINA — chapitre I95 Hypotension artérielle et anomalies tensionnelles isolées (couvre I95 et R03)
from cardio_1 import a, G

# ---- codes de la CIM-10-GM 2024 cités dans le cours (notes d'exclusion du BfArM)
a('R03.0',[('R','chapitre des symptômes, signes et résultats anormaux'),('03.0','sous-catégorie de l’élévation tensionnelle constatée')],'Code R03.0 de la CIM-10-GM : constatation d’une élévation de la tension artérielle, sans diagnostic d’hypertension',
 '<p>Code réservé à un épisode hypertensif ou à une découverte isolée chez un patient sans diagnostic formel d’hypertension. Il décrit une constatation ; il ne remplace pas la confirmation par mesures hors cabinet, qui relève du cours I10.</p>','i95-r03-0')
a('R03.1',[('R','chapitre des symptômes, signes et résultats anormaux'),('03.1','sous-catégorie de la baisse tensionnelle non spécifique')],'Code R03.1 de la CIM-10-GM : constatation d’une baisse non spécifique de la tension artérielle',
 '<p>Code d’une pression basse constatée sans diagnostic d’hypotension. La CIM-10-GM 2024 en exclut l’hypotension (I95.-), l’hypotension orthostatique neurogène (G23.8) et le syndrome hypotensif de la mère (O26.5).</p>','i95-r03-1')
a('G23.8',[('G','chapitre des maladies du système nerveux'),('23.8','autres maladies dégénératives précisées des noyaux gris centraux')],'Code G23.8 de la CIM-10-GM',
 '<p>Code sous lequel la CIM-10-GM 2024 range l’hypotension orthostatique neurogène de type Shy et Drager, exclue de I95.1. Le codage suit la maladie neurologique causale.</p>','i95-cim')
a('G90.80',[('G','chapitre des maladies du système nerveux'),('90.80','sous-catégorie du syndrome de tachycardie orthostatique posturale')],'Code G90.80 de la CIM-10-GM',
 '<p>Code du syndrome de tachycardie orthostatique posturale, exclu de I95.1 par la CIM-10-GM 2024. Ce syndrome est traité dans le cours I49.</p>','i95-cim')
a('O26.5',[('O','chapitre de la grossesse, de l’accouchement et de la puerpéralité'),('26.5','sous-catégorie du syndrome hypotensif de la mère')],'Code O26.5 de la CIM-10-GM',
 '<p>Syndrome hypotensif de la mère, typiquement la compression aorto-cave en décubitus dorsal en fin de grossesse ; exclu de I95 et de R03.1.</p>','i95-grossesse')
a('R57.9',[('R','chapitre des symptômes, signes et résultats anormaux'),('57.9','sous-catégorie du choc sans précision')],'Code R57.9 de la CIM-10-GM : choc, sans précision',
 '<p>Le collapsus cardiovasculaire est exclu de I95 : une hypotension avec hypoperfusion d’organe relève du choc et de son code propre.</p>','i95-cim')

# ---- autorités, examens, gènes
a('FDA',[('F','Food (aliments)'),('D','and Drug (et médicaments)'),('A','Administration')],'Food and Drug Administration (agence fédérale américaine des aliments et des médicaments)',
 '<p>Autorité d’autorisation des médicaments aux États-Unis. Elle a autorisé la droxidopa en 2014 pour l’hypotension orthostatique neurogène symptomatique ; cette autorisation ne vaut pas en Suisse.</p>','i95-d-droxi')
a('MIBG',[('M','Méta-'),('I','Iodo-'),('B','Benzyl-'),('G','Guanidine')],'Métaiodobenzylguanidine',
 '<p>Analogue de la noradrénaline capté par les terminaisons sympathiques. Marqué à l’iode radioactif, il mesure l’innervation sympathique cardiaque : la captation est effondrée quand les neurones postganglionnaires dégénèrent (maladie de Parkinson, dysautonomie pure) et habituellement conservée dans l’atrophie multisystématisée.</p>','i95-mibg')
a('SNCA',[('S','Synuclein (synucléine)'),('N','Non-A4 component of amyloid precursor (composant non amyloïde des plaques)'),('C','Component'),('A','Alpha')],'Gène de l’alpha-synucléine',
 '<p>Gène codant l’alpha-synucléine, protéine dont l’agrégation définit les synucléinopathies. Ses duplications, triplications et mutations ponctuelles causent des formes familiales rares de maladie de Parkinson. Le développement anglais est historique et non strictement lettre à lettre.</p>','i95-synucl')
a('DBH',[('D','Dopamine'),('B','Bêta-'),('H','Hydroxylase')],'Dopamine bêta-hydroxylase (enzyme et gène)',
 '<p>Enzyme des vésicules sympathiques qui transforme la dopamine en noradrénaline. Son déficit congénital, autosomique récessif, supprime la noradrénaline et provoque une hypotension orthostatique sévère que la droxidopa corrige.</p>','i95-s-dbh')

# ---- noms propres composés cités
a('Norcliffe-Kaufmann',[('Norcliffe-Kaufmann','nom de famille de Lucy Norcliffe-Kaufmann, non développable lettre à lettre')],'Lucy Norcliffe-Kaufmann, neurologue (Université de New York)',
 '<p>Première autrice de l’étude de 2018 (Annals of Neurology) qui a validé le rapport ΔFC/ΔPAS inférieur à 0,5 pour reconnaître une hypotension orthostatique neurogène.</p>','i95-ratio')
