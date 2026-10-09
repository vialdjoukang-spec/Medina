"""Glossaire du cours B24 — Infection par le VIH et maladie à VIH de l’adulte (I-03-Infectiologie).

Balayage de conformité du 8 octobre 2026 : les sigles du système de cotation
américain et des références américaines retirées ont été supprimés ; les sigles
des sources suisses et européennes (CFSS, CFIST, EACS, QUALAB) ont été ajoutés.
Les doses et décisions restent dans les fenêtres, rattachées à leurs sources.
"""
from cardio_1 import a, G

# Les clés VIH, CD3, CD4, CD8, ARN, ADN, IST, PrEP, CYP3A et EDTA sont définies
# par d’autres glossaires du projet ; elles ne sont pas redéfinies ici.

# Virus, cellules et molécules
a('VIH-1', [('V', 'Virus de l’'), ('I', 'Immunodéficience'), ('H', 'Humaine'), ('1', 'type 1')], 'Virus de l’immunodéficience humaine de type 1', '<p>Type viral le plus répandu ; les tests de charge virale courants lui sont destinés.</p>')
a('VIH-2', [('V', 'Virus de l’'), ('I', 'Immunodéficience'), ('H', 'Humaine'), ('2', 'type 2')], 'Virus de l’immunodéficience humaine de type 2', '<p>Type viral surtout présent en Afrique de l’Ouest, naturellement résistant aux inhibiteurs non nucléosidiques.</p>')
a('HIV', [('H', 'Human'), ('I', 'Immunodeficiency'), ('V', 'Virus')], 'Virus de l’immunodéficience humaine, sigle anglais', '<p>Sigle anglais du VIH, conservé dans les noms propres (Swiss HIV Cohort Study, revue HIV Medicine).</p>')
a('B24', [('B', 'chapitre des maladies infectieuses et parasitaires'), ('24', 'catégorie de classification')], 'Immunodéficience humaine virale [VIH], sans précision', '<p>Libellé du catalogue CIM-10-GM, mentionné dans l’en-tête du cours.</p>')
a('GALT', [('G', 'Gut-'), ('A', 'Associated'), ('L', 'Lymphoid'), ('T', 'Tissue')], 'Tissu lymphoïde associé à l’intestin', '<p>Compartiment immunitaire de la muqueuse intestinale, siège d’une déplétion précoce des CD4.</p>')
a('CCR5', [('CC', 'famille CC des chimiokines'), ('R', 'Receptor'), ('5', 'type 5')], 'Récepteur de chimiokines CCR5', '<p>Corécepteur d’entrée des virus dits R5.</p>')
a('CXCR4', [('CXC', 'famille CXC des chimiokines'), ('R', 'Receptor'), ('4', 'type 4')], 'Récepteur de chimiokines CXCR4', '<p>Corécepteur d’entrée des virus dits X4.</p>')
a('IRIS', [('I', 'Immune'), ('R', 'Reconstitution'), ('I', 'Inflammatory'), ('S', 'Syndrome')], 'Syndrome inflammatoire de reconstitution immunitaire', '<p>Aggravation ou révélation d’une infection pendant la restauration immunitaire induite par le traitement, retenue après exclusion de l’évolution attendue et d’une toxicité (EACS 13).</p>')
a('HBc', [('HB', 'Hépatite B'), ('c', 'antigène de capside (core)')], 'Antigène de capside du virus de l’hépatite B', '<p>Ses anticorps (anti-HBc) témoignent d’un contact avec le virus ; la vaccination ne les induit pas.</p>')
a('OCT2', [('O', 'Organic'), ('C', 'Cation'), ('T', 'Transporter'), ('2', 'type 2')], 'Transporteur de cations organiques de type 2', '<p>Transporteur rénal inhibé par le dolutégravir et le bictégravir : il explique l’interaction avec la metformine et la fampridine.</p>')
a('UGT1A1', [('UGT', 'Uridine diphosphate GlucuronosylTransférase'), ('1A1', 'isoforme 1A1')], 'Uridine diphosphate glucuronosyltransférase 1A1', '<p>Enzyme de conjugaison du bictégravir ; ses inducteurs puissants abaissent son exposition.</p>')

# Classes et molécules antirétrovirales
a('INTI', [('I', 'Inhibiteur'), ('N', 'Nucléosidique ou nucléotidique de la'), ('T', 'Transcriptase'), ('I', 'Inverse')], 'Inhibiteur nucléosidique ou nucléotidique de la transcriptase inverse', '<p>Faux substrat qui interrompt la synthèse de l’ADN viral.</p>')
a('INNTI', [('I', 'Inhibiteur'), ('N', 'Non'), ('N', 'Nucléosidique de la'), ('T', 'Transcriptase'), ('I', 'Inverse')], 'Inhibiteur non nucléosidique de la transcriptase inverse', '<p>Se fixe sur une poche distincte du site actif ; inactif contre le VIH-2.</p>')
a('INSTI', [('IN', 'INtegrase'), ('S', 'Strand'), ('T', 'Transfer'), ('I', 'Inhibitor')], 'Inhibiteur du transfert de brin de l’intégrase', '<p>Empêche l’intégration de l’ADN viral ; le bictégravir et le dolutégravir ont une haute barrière génétique.</p>')
a('IP', [('I', 'Inhibiteur de'), ('P', 'Protéase')], 'Inhibiteur de protéase', '<p>Empêche la maturation des virions ; le darunavir exige un potentialisateur.</p>')
a('TAF', [('TAF', 'code conventionnel du ténofovir alafénamide, non trois mots')], 'Ténofovir alafénamide', '<p>Prodrogue du ténofovir, privilégiée par EACS en cas de risque rénal ou osseux.</p>')
a('TDF', [('T', 'Ténofovir'), ('D', 'Disoproxil'), ('F', 'Fumarate')], 'Ténofovir disoproxil', '<p>Prodrogue du ténofovir ; en Suisse, dosée à 245 mg de ténofovir disoproxil.</p>')
a('FTC', [('FTC', 'code conventionnel de l’emtricitabine, non trois mots')], 'Emtricitabine')
a('3TC', [('3TC', 'code conventionnel de la lamivudine, non trois mots')], 'Lamivudine')
a('DTG', [('DTG', 'code conventionnel du dolutégravir, non trois mots')], 'Dolutégravir')
a('BIC', [('BIC', 'code conventionnel du bictégravir, non trois mots')], 'Bictégravir')
a('DRV', [('DRV', 'code conventionnel du darunavir')], 'Darunavir')

# Prévention
a('PEP', [('P', 'Post-'), ('E', 'Exposure'), ('P', 'Prophylaxis')], 'Prophylaxie postexposition', '<p>Traitement de 4 semaines commencé le plus tôt possible après une exposition.</p>')
a('SwissPrEPared', [('SwissPrEPared', 'nom propre du programme national suisse de PrEP, formé sur « PrEP » ; non une abréviation développable')], 'Programme national suisse de prophylaxie préexposition', '<p>Programme dirigé par l’Université de Zurich ; seule voie de remboursement de la PrEP par l’assurance obligatoire des soins jusqu’au 31 décembre 2026.</p>')
a('PARTNER2', [('PARTNER2', 'nom de la seconde phase de l’étude européenne PARTNER, non strictement lettre à lettre')], 'Étude européenne PARTNER2', '<p>Étude prospective de 75 centres de 14 pays européens : aucune transmission liée au partenaire sous ARN &lt;200 copies/mL (Rodger et coll., Lancet 2019).</p>')

# Institutions et sources
a('EACS', [('E', 'European'), ('A', 'AIDS'), ('C', 'Clinical'), ('S', 'Society')], 'European AIDS Clinical Society', '<p>Société européenne dont les recommandations, version 13.0 de 2025, fondent la conduite de ce cours.</p>')
a('CFSS', [('C', 'Commission'), ('F', 'Fédérale pour la'), ('S', 'Santé'), ('S', 'Sexuelle')], 'Commission fédérale pour la santé sexuelle', '<p>Commission suisse auteure des recommandations PrEP de 2016 et PEP de 2014.</p>')
a('CFIST', [('C', 'Commission'), ('F', 'Fédérale pour les questions liées aux'), ('IST', 'Infections Sexuellement Transmissibles')], 'Commission fédérale pour les questions liées aux infections sexuellement transmissibles', '<p>Commission qui a approuvé les recommandations SwissPrEPared publiées en 2025 et participé à la directive de dépistage.</p>')
a('QUALAB', [('QUALAB', 'nom de la Commission suisse pour l’assurance de qualité dans le laboratoire médical, non strictement lettre à lettre')], 'Commission suisse pour l’assurance de qualité dans le laboratoire médical', '<p>Reconnaît les centres de contrôle de qualité externe des laboratoires.</p>')
a('CE', [('CE', 'Conformité Européenne')], 'Marquage de conformité européenne', '<p>Indique qu’un dispositif de diagnostic in vitro est conforme aux exigences de l’Union européenne.</p>')
a('MoCHiV', [('Mo', 'Mother'), ('C', 'and Child'), ('HiV', 'HIV')], 'Swiss Mother and Child HIV Cohort Study', '<p>Cohorte suisse mère-enfant intégrée à la Swiss HIV Cohort Study.</p>')
a('ZetLab', [('ZetLab', 'nom propre d’un laboratoire médical suisse, non une abréviation')], 'Laboratoire ZetLab', '<p>Laboratoire suisse dont la fiche d’immunophénotypage sert d’exemple d’intervalle de référence.</p>')
a('McMyn', [('McMyn', 'nom propre du premier auteur, non une abréviation')], 'McMyn (premier auteur)', '<p>Premier auteur d’une étude du Journal of Clinical Investigation (2023) sur le réservoir viral sous traitement prolongé.</p>')
a('R5', [('R5', 'virus utilisant le corécepteur CCR5')], 'Tropisme R5', '<p>Virus qui entrent dans la cellule par le corécepteur CCR5.</p>')
a('X4', [('X4', 'virus utilisant le corécepteur CXCR4')], 'Tropisme X4', '<p>Virus qui entrent dans la cellule par le corécepteur CXCR4.</p>')
