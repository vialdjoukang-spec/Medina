from cardio_1 import a, G
from cardio_2 import t
# J67 — Pneumopathies d’hypersensibilité et maladies des voies aériennes dues aux poussières organiques (P-02-Pneumologie).
# Abréviations nouvelles du cours, définition littérale lettre à lettre. LAA et OLAA (j60.py) et INBUILD (j84.py) sont réutilisées sans redéfinition.
a('Th1',[('T','lymphocyte T'),('h','helper (auxiliaire)'),('1','de type 1')],'Lymphocyte T auxiliaire de type 1','<p>Lymphocyte T CD4 producteur d’interféron gamma, qui active les macrophages et organise les granulomes. Il domine la réponse cellulaire de la pneumopathie d’hypersensibilité.</p>','j67-hyper')
a('TLR4',[('T','Toll-'),('L','Like (de type)'),('R','Receptor (récepteur)'),('4','numéro 4')],'Récepteur de type Toll 4','<p>Récepteur de l’immunité innée qui reconnaît le lipopolysaccharide des bactéries à Gram négatif ; il déclenche l’inflammation de la byssinose et du syndrome toxique des poussières organiques.</p>','j67-endo')
a('ELISA',[('E','Enzyme-'),('L','Linked'),('I','ImmunoSorbent'),('SA','ASsay')],'Dosage immuno-enzymatique sur support solide','<p>Méthode de dosage des anticorps par une réaction enzymatique colorée ; elle sert à mesurer les IgG spécifiques des antigènes de pneumopathie d’hypersensibilité.</p>','j67-igg')
a('FFP2',[('F','Filtering (filtrant)'),('F','Face (facial)'),('P','Piece (pièce)'),('2','classe de protection 2')],'Pièce faciale filtrante de classe 2','<p>Masque filtrant normalisé en Europe, qui arrête au moins 94 % des particules de l’essai normalisé. Il réduit l’inhalation de spores sans remplacer l’éviction.</p>','j67-ffp')
a('FFP3',[('F','Filtering (filtrant)'),('F','Face (facial)'),('P','Piece (pièce)'),('3','classe de protection 3')],'Pièce faciale filtrante de classe 3','<p>Masque filtrant normalisé en Europe, de la classe la plus protectrice, qui arrête au moins 99 % des particules de l’essai normalisé.</p>','j67-ffp')
a('J66.0',[('J66.0','code CIM-10-GM 2024')],'Byssinose','<p>Affection des voies aériennes due aux poussières de coton.</p>','j67-byss')
a('J66.1',[('J66.1','code CIM-10-GM 2024')],'Maladie des apprêteurs du lin','<p>Affection des voies aériennes due aux poussières de lin.</p>','j67-byss')
a('J66.2',[('J66.2','code CIM-10-GM 2024')],'Cannabinose','<p>Affection des voies aériennes due aux poussières de chanvre.</p>','j67-byss')
a('J66.8',[('J66.8','code CIM-10-GM 2024')],'Affection des voies aériennes due à d’autres poussières organiques précisées','<p>Catégorie résiduelle des atteintes bronchiques dues à des poussières organiques autres que le coton, le lin et le chanvre.</p>')
a('J67.0',[('J67.0','code CIM-10-GM 2024')],'Poumon de fermier','<p>Alvéolite allergique due au foin, à la paille ou aux céréales moisis. Cinquième caractère : 0 sans, 1 avec exacerbation aiguë.</p>','j67-ferm')
a('J67.1',[('J67.1','code CIM-10-GM 2024')],'Bagassose','<p>Alvéolite allergique due à la bagasse moisie, résidu de la canne à sucre.</p>','j67-actino')
a('J67.2',[('J67.2','code CIM-10-GM 2024')],'Poumon des oiseleurs','<p>Alvéolite allergique due aux antigènes d’oiseaux (perruches, pigeons) et au duvet.</p>','j67-ois')
a('J67.3',[('J67.3','code CIM-10-GM 2024')],'Subérose','<p>Alvéolite allergique des manipulateurs et travailleurs du liège moisi.</p>')
a('J67.4',[('J67.4','code CIM-10-GM 2024')],'Poumon des malteurs','<p>Alvéolite allergique due à <i>Aspergillus clavatus</i> de l’orge germée.</p>')
a('J67.5',[('J67.5','code CIM-10-GM 2024')],'Poumon des champignonnistes','<p>Alvéolite allergique des cultivateurs de champignons, exposés au compost et aux spores.</p>')
a('J67.6',[('J67.6','code CIM-10-GM 2024')],'Poumon des écorceurs d’érables','<p>Alvéolite allergique due à <i>Cryptostroma corticale</i> (cryptostromose).</p>')
a('J67.7',[('J67.7','code CIM-10-GM 2024')],'Maladie pulmonaire due aux systèmes de conditionnement et d’humidification de l’air','<p>Alvéolite allergique due aux micro-organismes qui se développent dans l’eau des climatiseurs et humidificateurs.</p>','j67-humid')
a('J67.8',[('J67.8','code CIM-10-GM 2024')],'Alvéolite allergique due à d’autres poussières organiques','<p>Inclut notamment le poumon des fourreurs, des laveurs de fromage, des torréfacteurs de café et la maladie due au séquoia.</p>')
a('J67.9',[('J67.9','code CIM-10-GM 2024')],'Alvéolite allergique due aux poussières organiques, sans précision','<p>Pneumopathie d’hypersensibilité sans source précisée, y compris l’alvéolite allergique extrinsèque sans autre indication.</p>')
a('J68.3',[('J68.3','code CIM-10-GM 2024')],'Syndrome réactionnel de dysfonction des voies respiratoires','<p>Atteinte bronchique due à l’inhalation d’agents chimiques, d’émanations, de fumées ou de gaz ; exclue de la catégorie J66.</p>')
a('mSv',[('m','milli'),('Sv','Sievert')],'Millisievert','<p>Unité de dose efficace de rayonnement ionisant ; une tomodensitométrie thoracique à dose réduite délivre 1 à 3 mSv selon ATS/JRS/ALAT 2020.</p>')
a('CellCept',[('CellCept','nom de marque du mycophénolate mofétil (non abréviatif)')],'CellCept (mycophénolate mofétil)','<p>Nom commercial suisse du mycophénolate mofétil, autorisé pour la prévention du rejet de greffe.</p>','j67-d-mmf')

