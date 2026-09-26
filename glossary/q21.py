# Glossaire MEDINA — chapitre Q21 (cardiopathies congénitales, Q20 à Q28)
from cardio_1 import a, G

def b(k, *args):
    """Ajoute la clé seulement si un autre chapitre ne l'a pas déjà définie."""
    if k not in G: a(k, *args)

# ---- lésions et hémodynamique
a('CIA',[('C','Communication'),('I','Inter'),('A','Auriculaire')],'Communication interauriculaire',
 '<p>Défaut du septum interauriculaire (types ostium secundum, ostium primum, sinus venosus, sinus coronaire). Shunt gauche-droite diastolique, surcharge de volume des cavités droites ; fermeture si surcharge droite et résistances pulmonaires &lt; 3 unités Wood (ESC 2020).</p>','q21-cia-types')
a('CIV',[('C','Communication'),('I','Inter'),('V','Ventriculaire')],'Communication interventriculaire',
 '<p>Défaut du septum interventriculaire, la plus fréquente des cardiopathies congénitales. Shunt gauche-droite systolique, surcharge des cavités gauches ; restrictive ou non restrictive selon sa taille.</p>','q21-civ-types')
a('CAV',[('C','Canal'),('A','Atrio'),('V','Ventriculaire')],'Canal atrioventriculaire',
 '<p>Défaut des bourrelets endocardiques : CIA ostium primum, avec (forme complète) ou sans (forme partielle) CIV d’admission et valve atrioventriculaire commune. Fréquent dans la trisomie 21.</p>','q21-cav')
a('HTAP',[('HT','HyperTension'),('A','Artérielle'),('P','Pulmonaire')],'Hypertension artérielle pulmonaire',
 '<p>Hypertension pulmonaire précapillaire du groupe 1 : pression artérielle pulmonaire moyenne &gt; 20 mmHg, pression capillaire ≤ 15 mmHg, résistances &gt; 2 unités Wood (ESC/ERS 2022). Le syndrome d’Eisenmenger en est la forme congénitale extrême.</p>','q21-htap')
a('RVP',[('R','Résistances'),('V','Vasculaires'),('P','Pulmonaires')],'Résistances vasculaires pulmonaires',
 '<p>(Pression artérielle pulmonaire moyenne − pression capillaire) / débit pulmonaire, en unités Wood. Seuils de fermeture d’un shunt : 3 et 5 unités Wood.</p>','q21-rvp')
a('RVS',[('R','Résistances'),('V','Vasculaires'),('S','Systémiques')],'Résistances vasculaires systémiques',
 '<p>(Pression artérielle moyenne − pression de l’oreillette droite) / débit systémique. Leur baisse (effort, fièvre, grossesse, vasodilatateurs) augmente un shunt droite-gauche.</p>','q21-shuntdet')
a('Qp/Qs',[('Qp','débit (Q) Pulmonaire'),('Qs','débit (Q) Systémique')],'Rapport du débit pulmonaire au débit systémique',
 '<p>Égal à 1 sans shunt ; &gt; 1,5 : shunt gauche-droite significatif ; &lt; 1 : shunt droite-gauche. Calculé par oxymétrie (principe de Fick), échocardiographie ou IRM.</p>','q21-qpqs')
a('VTDi',[('V','Volume'),('T','Télé-'),('D','Diastolique'),('i','indexé (à la surface corporelle)')],'Volume télédiastolique indexé (du ventricule droit en IRM)',
 '<p>Dans la tétralogie de Fallot réparée, un volume télédiastolique indexé du ventricule droit ≥ 160 mL/m² est un critère de remplacement valvulaire pulmonaire chez l’asymptomatique (ESC 2020).</p>','q21-irm-vd')
a('VTSi',[('V','Volume'),('T','Télé-'),('S','Systolique'),('i','indexé (à la surface corporelle)')],'Volume télésystolique indexé (du ventricule droit en IRM)',
 '<p>Dans la tétralogie de Fallot réparée, un volume télésystolique indexé du ventricule droit ≥ 80 mL/m² est un critère de remplacement valvulaire pulmonaire chez l’asymptomatique (ESC 2020).</p>','q21-irm-vd')
a('ALCAPA',[('A','Anomalous (anormale)'),('L','Left (gauche)'),('C','Coronary (coronaire)'),('A','Artery (artère)'),('P','from the Pulmonary (naissant de l’artère pulmonaire)'),('A','Artery (artère)')],'Origine anormale de la coronaire gauche depuis l’artère pulmonaire',
 '<p>Syndrome de Bland-White-Garland : ischémie du nourrisson vers 6 à 8 semaines, quand la pression pulmonaire baisse. Traitement chirurgical (réimplantation).</p>','q21-alcapa')
a('RoPE',[('R','Risk (risque)'),('o','of (d’)'),('P','Paradoxical (paradoxale)'),('E','Embolism (embolie)')],'Score RoPE (Risk of Paradoxical Embolism)',
 '<p>Score de 0 à 10 points (âge et absence de facteurs de risque vasculaire, infarctus cortical) estimant la probabilité qu’un foramen ovale perméable soit responsable d’un accident ischémique.</p>','q21-rope')
a('PASCAL',[('P','PFO (Patent Foramen Ovale, foramen ovale perméable)'),('A','Associated (associé)'),('S','Stroke (accident vasculaire cérébral)'),('CA','CAusal (causale)'),('L','Likelihood (probabilité)')],'Classification PASCAL',
 '<p>Combine le score RoPE (&lt; 7 ou ≥ 7) et les caractères à haut risque du foramen (large shunt, anévrisme du septum) : causalité improbable, possible ou probable.</p>','q21-rope')

# ---- sociétés, registres, essais
a('ESO',[('E','European'),('S','Stroke'),('O','Organisation')],'European Stroke Organisation (Organisation européenne de l’accident vasculaire cérébral)',
 '<p>Société savante européenne de neurologie vasculaire ; recommandations 2024 sur le foramen ovale perméable après un accident vasculaire cérébral.</p>','q21-rope')
b('ERS',[('E','European'),('R','Respiratory'),('S','Society')],'European Respiratory Society (Société européenne de pneumologie)',
 '<p>Société savante européenne de pneumologie ; coauteur avec l’ESC des recommandations 2022 sur l’hypertension pulmonaire.</p>','q21-htap')
a('ISACHD',[('I','International'),('S','Society for'),('A','Adult'),('C','Congenital'),('H','Heart'),('D','Disease')],'International Society for Adult Congenital Heart Disease (Société internationale des cardiopathies congénitales de l’adulte)',
 '<p>Société savante coauteure des recommandations américaines 2025 sur les cardiopathies congénitales de l’adulte.</p>')
a('SACHER',[('S','Swiss'),('A','Adult'),('C','Congenital'),('HE','HEart disease'),('R','Registry')],'Registre suisse des cardiopathies congénitales de l’adulte',
 '<p>Registre national multicentrique suisse qui documente les adultes porteurs d’une cardiopathie congénitale suivis dans les centres spécialisés.</p>','q21-centres')
a('CLOSE',[('CLOSE','nom d’essai (« fermer »), formé à partir de « Patent Foramen Ovale CLOsure or Anticoagulants versus Antiplatelet Therapy to Prevent Stroke Recurrence », non strictement lettre à lettre')],'Essai CLOSE (2017)',
 '<p>Fermeture du foramen ovale perméable plus antiplaquettaire contre antiplaquettaire seul chez des patients de 16 à 60 ans : réduction des récidives d’accident ischémique.</p>','q21-rope')
a('RESPECT',[('RESPECT','nom d’essai formé à partir de « Randomized Evaluation of Recurrent Stroke Comparing PFO Closure to Established Current Standard of Care Treatment », non strictement lettre à lettre')],'Essai RESPECT (2013, suivi prolongé 2017)',
 '<p>Fermeture percutanée du foramen ovale perméable contre traitement médical après un accident ischémique inexpliqué : réduction des récidives au suivi prolongé.</p>','q21-rope')
# Clé « Gore REDUCE » (nom officiel : Gore REDUCE Clinical Study) : distincte de la clé « REDUCE »,
# réservée à l’essai suisse sur la corticothérapie courte de l’exacerbation de BPCO (chapitre J44, JAMA 2013).
a('Gore REDUCE',[('Gore','nom de la société fabricante du dispositif de fermeture, intégré au nom officiel de l’essai'),('REDUCE','nom d’essai (« réduire ») sur la fermeture du foramen ovale perméable, non développable lettre à lettre')],'Essai Gore REDUCE (2017)',
 '<p>Fermeture du foramen ovale perméable plus antiplaquettaire contre antiplaquettaire seul après un accident ischémique cryptogénique : réduction des récidives cliniques.</p>','q21-rope')
a('BREATHE-5',[('BREATHE','Bosentan Randomized trial of Endothelin Antagonist THErapy, acronyme arrangé'),('5','cinquième essai de la série')],'Essai BREATHE-5 (2006)',
 '<p>Bosentan contre placebo dans le syndrome d’Eisenmenger : baisse des résistances pulmonaires et amélioration de la capacité d’effort, sans baisse de la saturation.</p>','q21-d-era')

# ---- gènes et éponymes
a('TBX1',[('T','T-'),('BX','BoX (famille des gènes à boîte T)'),('1','membre 1')],'Gène TBX1',
 '<p>Facteur de transcription de la famille T-box, situé dans la région 22q11.2 ; nécessaire au développement des arcs pharyngiens et à la migration de la crête neurale vers les voies d’éjection.</p>','q21-digeorge')
a('ELN',[('ELN','symbole officiel du gène ELastiN (élastine)')],'Gène de l’élastine',
 '<p>Gène de la région 7q11.23, délété dans le syndrome de Williams : artériopathie élastique (sténose aortique supravalvulaire, sténoses pulmonaires).</p>','q21-williams')
a('DiGeorge',[('DiGeorge','nom propre (Angelo DiGeorge, pédiatre américain), non abréviation')],'Syndrome de DiGeorge (microdélétion 22q11.2)',
 '<p>Nom historique de la microdélétion 22q11.2 : cardiopathies conotroncales, hypocalcémie, déficit lymphocytaire T, troubles psychiatriques.</p>','q21-digeorge')
a('Blalock-Taussig',[('Blalock-Taussig','noms propres (Alfred Blalock, chirurgien, et Helen Taussig, cardiopédiatre), non abréviation')],'Anastomose de Blalock-Taussig',
 '<p>Anastomose palliative entre une artère sous-clavière et une artère pulmonaire (1944), pour augmenter le débit pulmonaire d’une cardiopathie cyanogène.</p>','q21-bt')
a('Bland-White-Garland',[('Bland-White-Garland','noms propres (Edward Bland, Paul White, Joseph Garland), non abréviation')],'Syndrome de Bland-White-Garland',
 '<p>Origine anormale de la coronaire gauche depuis l’artère pulmonaire (ALCAPA).</p>','q21-alcapa')
b('Q21.1',[('Q','chapitre Q de la CIM-10 (malformations congénitales)'),('21','catégorie 21 (malformations des cloisons cardiaques)'),('.1','sous-catégorie 1')],'Code CIM-10 Q21.1 : communication interauriculaire',
 '<p>Code de la communication interauriculaire, qui inclut la persistance du foramen ovale.</p>','q21-cim')
