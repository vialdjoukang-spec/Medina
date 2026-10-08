# Glossaire MEDINA — R06 Dyspnée et anomalies de la respiration (P-02-Pneumologie)
from cardio_1 import a, G

# ---- codes CIM-10-GM 2024 de la catégorie R06 et codes voisins cités
def _c(code, cat, sub, title, d):
    a(code, [(code.split('.')[0], 'catégorie ' + cat), ('.' + code.split('.')[1], 'sous-code ' + sub)], title + ' (CIM-10-GM 2024)', d)

_c('R06.0', 'Anomalies de la respiration', 'Dyspnée', 'Dyspnée', '<p>Inclut l’essoufflement et l’orthopnée ; exclut la tachypnée transitoire du nouveau-né (P22.1). Code d’attente remplacé par celui de la cause dès qu’elle est établie.</p>')
_c('R06.1', 'Anomalies de la respiration', 'Stridor', 'Stridor', '<p>Exclut le laryngospasme striduleux (J38.5) et le stridor laryngé congénital (P28.8).</p>')
_c('R06.2', 'Anomalies de la respiration', 'Sifflement', 'Sifflement', '<p>Respiration sifflante sans diagnostic établi.</p>')
_c('R06.3', 'Anomalies de la respiration', 'Respiration périodique', 'Respiration périodique', '<p>Inclut la respiration de Cheyne-Stokes.</p>')
_c('R06.4', 'Anomalies de la respiration', 'Hyperventilation', 'Hyperventilation', '<p>Exclut l’hyperventilation psychogène (F45.33).</p>')
_c('R06.5', 'Anomalies de la respiration', 'Respiration par la bouche', 'Respiration par la bouche', '<p>Inclut le ronflement ; exclut la sécheresse de la bouche sans précision (R68.2).</p>')
_c('R06.6', 'Anomalies de la respiration', 'Hoquet', 'Hoquet', '<p>Exclut le hoquet psychogène (F45.33).</p>')
_c('R06.7', 'Anomalies de la respiration', 'Éternuement', 'Éternuement', '<p>Symptôme isolé, le plus souvent rhinologique.</p>')
_c('R06.8', 'Anomalies de la respiration', 'Anomalies autres et non précisées', 'Anomalies de la respiration, autres et non précisées', '<p>Sous-catégorie subdivisée en R06.80 et R06.88 ; exclut les apnées du sommeil (G47.3) et du nouveau-né (P28.3, P28.4).</p>')
_c('R06.80', 'Anomalies de la respiration', 'Événement aigu menaçant la vie chez le nourrisson', 'Événement aigu menaçant la vie chez le nourrisson', '<p>Inclut l’« apparent life-threatening event » (ALTE) et le quasi-syndrome de mort subite du nourrisson.</p>')
_c('R06.88', 'Anomalies de la respiration', 'Anomalies autres et non précisées', 'Anomalies respiratoires autres et non précisées', '<p>Inclut l’apnée sans précision, la sensation d’étouffement, les soupirs et le spasme du sanglot.</p>')
_c('R07.1', 'Douleur au niveau de la gorge et du thorax', 'Douleur thoracique respiratoire', 'Douleur thoracique respiratoire', '<p>Douleur majorée par la respiration (douleur pleurale), sans cause établie.</p>')
_c('R68.2', 'Autres symptômes et signes généraux', 'Sécheresse de la bouche', 'Sécheresse de la bouche, sans précision', '<p>Exclue du code R06.5.</p>')
_c('J38.5', 'Maladies des cordes vocales et du larynx', 'Laryngospasme', 'Laryngospasme (striduleux)', '<p>Exclu du code R06.1.</p>')
_c('P28.8', 'Autres affections respiratoires du nouveau-né', 'Autres affections précisées', 'Autres affections respiratoires précisées du nouveau-né, dont le stridor laryngé congénital', '<p>Exclu du code R06.1.</p>')
_c('P22.1', 'Détresse respiratoire du nouveau-né', 'Tachypnée transitoire', 'Tachypnée transitoire du nouveau-né', '<p>Exclue du code R06.0.</p>')
_c('P28.3', 'Autres affections respiratoires du nouveau-né', 'Apnée primaire du sommeil', 'Apnée primaire du sommeil du nouveau-né', '<p>Exclue du code R06.8.</p>')
_c('P28.4', 'Autres affections respiratoires du nouveau-né', 'Autres apnées', 'Autres apnées du nouveau-né', '<p>Exclues du code R06.8.</p>')
_c('P28.5', 'Autres affections respiratoires du nouveau-né', 'Insuffisance respiratoire', 'Insuffisance respiratoire du nouveau-né', '<p>Exclue de la catégorie R06.</p>')
_c('F45.33', 'Troubles somatoformes', 'Dysfonction neurovégétative somatoforme du système respiratoire', 'Dysfonction neurovégétative somatoforme du système respiratoire', '<p>Code de l’hyperventilation psychogène et du hoquet psychogène, exclus de R06.4 et R06.6.</p>')
_c('G47.3', 'Troubles du sommeil', 'Apnée du sommeil', 'Apnée du sommeil', '<p>Exclue du code R06.8 ; relève d’un cours propre.</p>')

# ---- sigles cliniques
a('ALTE', [('A', 'Apparent'), ('L', 'Life-'), ('T', 'Threatening'), ('E', 'Event')], 'Apparent life-threatening event (événement aigu apparemment menaçant la vie)',
  '<p>Ancien terme pédiatrique, encore utilisé par le code R06.80, remplacé en 2016 par le concept d’événement bref résolu inexpliqué.</p>', 'r06-brue')
a('BRUE', [('B', 'Brief'), ('R', 'Resolved'), ('U', 'Unexplained'), ('E', 'Event')], 'Brief resolved unexplained event (événement bref résolu inexpliqué)',
  '<p>Événement de moins d’une minute chez un nourrisson de moins d’un an, résolu, inexpliqué après anamnèse et examen (Académie américaine de pédiatrie, 2016).</p>', 'r06-brue')
a('ESMO', [('E', 'European'), ('S', 'Society for'), ('M', 'Medical'), ('O', 'Oncology')], 'European Society for Medical Oncology (Société européenne d’oncologie médicale)',
  '<p>Société savante européenne d’oncologie ; sa recommandation de 2020 traite la dyspnée du patient atteint de cancer.</p>', 'r06-contentieux')
a('Guillain-Barré', [('Guillain', 'Georges Guillain, neurologue'), ('Barré', 'Jean-Alexandre Barré, neurologue')], 'Syndrome de Guillain-Barré (nom propre, non abréviation)',
  '<p>Polyradiculonévrite aiguë inflammatoire, le plus souvent démyélinisante et postinfectieuse. Elle provoque une faiblesse ascendante avec aréflexie et peut atteindre les muscles respiratoires jusqu’à l’insuffisance respiratoire. Une vaccination la déclenche très rarement.</p>')

# ---- essais
a('BEAMS', [('B', 'Breathlessness,'), ('E', 'Exertion'), ('A', 'And'), ('M', 'Morphine'), ('S', 'Sulphate')], 'Essai BEAMS (2022)',
  '<p>Essai randomisé australien : morphine à libération prolongée (8 ou 16 mg par jour) contre placebo dans la dyspnée chronique de la BPCO ; aucun bénéfice sur la pire dyspnée après une semaine (JAMA 2022).</p>', 'r06-contentieux')

# ---- noms propres signalés par l’audit
a('BIGORIO', [('BIGORIO', 'nom du couvent tessinois de Bigorio, lieu des réunions d’experts ; non abréviation')], 'Recommandations BIGORIO de la Société suisse de médecine et de soins palliatifs',
  '<p>Série de recommandations suisses de bonnes pratiques en soins palliatifs ; la recommandation sur la dyspnée date de 2003.</p>', 'r06-contentieux')
a('McDonagh', [('McDonagh', 'Theresa A. McDonagh, cardiologue, nom propre')], 'Nom d’auteur (non abréviation)',
  '<p>Première autrice des recommandations ESC 2021 sur l’insuffisance cardiaque.</p>')
