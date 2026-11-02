from common import *
sec('p-1','Produits sanguins : remplacer une fonction précise', '''
<p>Un concentré érythrocytaire apporte des globules rouges et soutient le transport d’oxygène. Le plasma et les plaquettes répondent à d’autres déficits de l’hémostase. Aucun de ces produits n’a pour fonction de fermer une lésion responsable du saignement ; leur utilisation accompagne le contrôle de la source.</p>
<p>En hémorragie majeure, la composition du support dépend du protocole, des pertes et des résultats répétés. La directive européenne décrit plusieurs stratégies initiales puis une adaptation aux déficits. Elle ne permet pas de transformerD62 en ordonnance fixe d’un même nombre de poches pour tous.</p>
<p>Chez un patient stable, la liste suisse smartermedicine recommande une quantité minimale adaptée et une réévaluation ; il n’est pas nécessaire de prescrire deux unités si une seule suffit. Cette logique ne doit pas retarder le support d’une hémorragie massive persistante.</p>
<p>La sécurité comprend identité, compatibilité, surveillance, conservation du produit en cas de réaction et traçabilité. L’événement clinique et son imputabilité sont documentés séparément. Les détails de préparation et les débits suivent la procédure du centre.</p>
''','TRAUMA','SMARTER','HUG-TRANS','SWISSMED')

sec('p-2','Acide tranexamique : produit exact et contexte exact', '''
<p><b>Tranexamic Acid Leman, solution injectable100mg/mL ; FI septembre2026.</b> Le produit contient500mg dans5mL ou1000mg dans10mL. Il agit sur la fibrinolyse. LaFI indique, chez l’adulte,0,5–1gIV lentement deux à trois fois par jour pour une fibrinolyse locale et1g toutes les6–8heures pour une fibrinolyse générale, à1mL/min. Ces schémas généraux ne sont pas le schéma spécifique de traumatologie ni celui du post-partum.</p>
<p>Le tableau de la partie10 donne les schémas des directives et leurs horloges. Une injection rapide expose notamment à l’hypotension, à la bradycardie ou à l’asystolie. La voie doit être clairement marquéeIV. Les voies neuraxiales et intracérébrales sont contre-indiquées et la voie intramusculaire n’est pas indiquée.</p>
<p>Contre-indications et précautions comprennent hypersensibilité, thrombose aiguë, insuffisance rénale sévère, antécédents de convulsions et certaines coagulopathies de consommation. Le risque thrombotique, les contraceptifs contenant des œstrogènes, les troubles visuels et les associations influençant l’hémostase demandent une évaluation. LaFI n’établit pas un régime pédiatrique universel pour tout saignement.</p>
<p>Les données de grossesse sont limitées ; laFI déconseille le premier trimestre et réserve l’usage pendant la grossesse à la nécessité absolue. Elle ne recommande pas l’allaitement. Ces mentions restent visibles à côté de la recommandation obstétricale deTXA précoce ; le choix clinique exige une appréciation contextualisée, sans consensus fictif.</p>
'''+alert('LaFI comporte un tableau rénal dont la ligne>500µmol/L coexiste avec la contre-indication d’insuffisance rénale sévère. Ne pas utiliser cette ligne comme autorisation automatique. Clarifier avec le spécialiste et le produit actuel.'),'TXA','TRAUMA','WHO-PPH','ESGE')

sec('p-3','Fer oral : une correction de carence, après l’urgence', '''
<p><b>ferro sanol ; FI suisse avril2021.</b> La quantité pertinente est le <b>fer élémentaire</b>. Un traitement oral convient dans les indications du produit lorsque la voie est tolérée et efficace ; il ne remplace pas la prise en charge d’un choc ou d’une perte active.</p>
<p>LaFI décrit100mg de fer élémentaire par jour selon les conditions d’âge et de poids. Dans les carences importantes, une phase initiale à200mg/j est prévue chez les personnes d’au moins15ans et d’au moins50kg, avec plafond de5mg/kg/j. Ce n’est pas une règle applicable à tout enfant ni un schéma automatique après toute hémorragie.</p>
<p>La tolérance digestive, l’observance et les interactions influencent le résultat. Des médicaments et aliments peuvent modifier l’absorption ; respecter les conditions et espacements du produit exact. Les atteintes rénale ou hépatique sévères figurent parmi les contre-indications de cetteFI : l’absence d’une table d’ajustement ne les efface pas.</p>
<p>Réévaluer la réponse, la persistance des pertes et la pertinence du diagnostic si l’hémoglobine ne se corrige pas comme attendu. Des schémas alternés discutés dans d’autres recommandations ne sont pas présentés comme la posologie de cetteFI.</p>
''','FERROSANOL','MEDIX')

sec('p-4','Carboxymaltose ferrique : besoin total, dose et surveillance', '''
<p><b>Ferinject ; FI suisse juin2025.</b> L’indication concerne la carence martiale confirmée chez l’adulte lorsque le fer oral est insuffisamment efficace, inefficace ou impossible. Calculer le besoin total ne suffit pas : chaque administration doit respecter les limites de voie, de poids et de semaine. La fenêtre'''+w('fer-calcul','calculer sans dépasser la dose')+''' distingue ces étapes.</p>
'''+table(['Administration adulte de laFI','Limite','Conséquence'],[
['Injection intraveineuse','15mg de fer/kg, sans dépasser1000mg','Ne pas reprendre le plafond pondéral de la perfusion pour une injection.'],
['Perfusion intraveineuse','20mg de fer/kg, sans dépasser1000mg','Respecter la dilution et la vitesse de laFI.'],
['Dose cumulée hebdomadaire','1000mg ; administrations fractionnées espacées d’au moins une semaine si besoin supérieur','Le besoin total peut dépasser la quantité autorisée en une séance.'],
['Surveillance après administration','Au moins30minutes','Personnel et moyens de traitement d’une anaphylaxie disponibles.']])+'''
<p>Les contre-indications comprennent anémie dont l’origine ferriprive n’est pas confirmée, surcharge en fer et hypersensibilité grave connue au fer parentéral, ainsi que les autres conditions de laFI. Le premier trimestre de grossesse est contre-indiqué ; les situations ultérieures exigent une évaluation du bénéfice et du risque. L’autorisation pédiatrique ne se déduit pas de la simple présence d’essais pédiatriques dans une fiche.</p>
<p>Le risque d’hypophosphatémie doit être pris en compte, surtout avec doses répétées élevées ou facteurs de risque. Des douleurs osseuses ou articulaires et une hypophosphatémie persistante justifient une réévaluation. Les préparations de fer oral ne sont pas administrées simultanément selon laFI ; la séquence doit être organisée.</p>
''','FERINJECT','WHO-PPH')

sec('p-5','Concentré de complexe prothrombinique : une indication ciblée', '''
<p><b>Octaplex500/1000 ; FI suisse novembre2021.</b> Ce concentré de facteurs dépendant de la vitamineK est indiqué dans certains déficits acquis nécessitant une correction urgente, notamment sous antagoniste de la vitamineK, et dans des déficits congénitaux précis lorsqu’un concentré spécifique n’est pas disponible. Il ne traite pas une simple concentration basse d’hémoglobine.</p>
<p>LaFI demande l’avis d’un spécialiste et une individualisation selon état clinique, importance et site de l’hémorragie, paramètres de coagulation et efficacité. En déficit acquis lié à un antagoniste de la vitamineK, l’association à la vitamineK doit être envisagée par l’équipe : l’action du concentré peut être plus courte que celle de l’antagoniste. Aucun protocole universel de dose pourD62 n’est déduit ici.</p>
<p>Octaplex contient de l’héparine. Une hypersensibilité à celle-ci ou un antécédent de thrombocytopénie induite par héparine contre-indique le produit. LaFI contre-indique aussi certaines situations pouvant entraîner un déficit en antithrombineIII, le produit n’en contenant pas. Le risque thrombotique et la coagulation intravasculaire disséminée exigent une surveillance.</p>
<p>Les données d’utilisation et de sécurité chez l’enfant ne sont pas établies dans cetteFI. La grossesse et l’allaitement requièrent une indication clairement posée. Consigner le produit et le lot pour la traçabilité ; le statut de produit plasmatique impose ses précautions propres.</p>
''','PCC')

sec('p-6','Éviter les erreurs de mécanisme et de formulation', '''
<p>La prescription part de la fonction à corriger. Une anémie mal tolérée, un déficit de facteurs, une fibrinolyse et une carence en fer ne sont pas la même indication. Le tableau permet de vérifier l’objectif avant de choisir le produit et la dose.</p>
'''+table(['Intervention','Ce qu’elle vise','Ce qu’elle ne remplace pas'],[
['Concentré érythrocytaire','Transporteurs d’oxygène','Contrôle de la source ou correction de tout déficit hémostatique.'],
['Acide tranexamique','Fibrinolyse dans les contextes indiqués','Globules rouges, facteurs ou bénéfice démontré dans tout saignement.'],
['Concentré de facteurs','Déficit précis documenté ou fortement suspecté selon contexte','Remplissage général ou traitement de touteD62.'],
['Fer oral ou intraveineux','Substrat de production en carence','Réanimation immédiate du choc.']])+'''
<p>Vérifier ensuite le produit exact, la concentration, la voie, les contre-indications et les adaptations. Un volume de10mL n’a de sens que si la concentration est connue. Une cible d’hémoglobine n’est pas une dose de fer ; un besoin total en fer n’est pas une autorisation d’administrer toute cette quantité immédiatement.</p>
'''+quiz('Une patiente de45kg a une indication confirmée à une perfusion deFerinject. Quel plafond pondéral faut-il vérifier avant la limite absolue ?','20mg/kg, soit900mg dans cet exemple ; le besoin réel peut être inférieur.','1000mg pour toute personne, sans tenir compte du poids.','La totalité du besoin calculé peut être perfusée en une fois.','45×20=900mg. La limite est la plus contraignante entre poids, plafond absolu et besoin réel ; les autres conditions de laFI restent nécessaires.'),'TRAUMA','TXA','PCC','FERINJECT','FERROSANOL')
