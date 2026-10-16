"""Abréviations C72 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'c72', '__init__'}:
        continue
    _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
G = {}
def add_if_absent(key, letters, full, definition, window):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full,
                  'def': '<p>' + definition + '</p>', 'ref': window}

add_if_absent('SNC', [('S','Système'),('N','Nerveux'),('C','Central')], 'Système nerveux central',
              'Il comprend l’encéphale et la moelle épinière. Le code C72 de la CIM-10-GM en regroupe des parties autres que l’encéphale et les méninges.', 'c72-codes')
add_if_absent('EANO', [('E','European'),('A','Association of'),('N','Neuro-'),('O','Oncology')], 'European Association of Neuro-Oncology (association européenne de neuro-oncologie)',
              'Cette société savante publie des recommandations sur les tumeurs du système nerveux central. Celles de 2018 sur les épendymomes et de 2021 sur les gliomes diffus de l’adulte fondent plusieurs conduites de ce cours.', 'c72-sources')
add_if_absent('EANS', [('E','European'),('A','Association of'),('N','Neurosurgical'),('S','Societies')], 'European Association of Neurosurgical Societies (association européenne des sociétés de neurochirurgie)',
              'Cette association a co-signé avec l’EANO les recommandations de 2026 sur l’étendue de l’exérèse des gliomes.', 'c72-exerese')
add_if_absent('EANS-EANO', [('EANS','European Association of Neurosurgical Societies'),('EANO','European Association of Neuro-Oncology')], 'Recommandations communes des associations européennes de neurochirurgie et de neuro-oncologie',
              'Les recommandations de 2026 portent sur l’étendue de l’exérèse des gliomes. Seul leur résumé a été lu.', 'c72-exerese')
add_if_absent('ERN', [('E','European'),('R','Reference'),('N','Network')], 'European Reference Network (réseau européen de référence)',
              'Un réseau européen de référence réunit des centres experts d’une maladie rare. Celui qui est cité ici publie des recommandations sur les syndromes de prédisposition tumorale.', 'c72-nf1')
add_if_absent('GENTURIS', [('GEN','Genetic'),('TU','Tumour'),('RIS','Risk'),('S','Syndromes')], 'Genetic Tumour Risk Syndromes (syndromes génétiques de risque tumoral)',
              'Ce réseau européen de référence traite les syndromes génétiques de prédisposition tumorale. Il publie les recommandations de surveillance de la neurofibromatose de type 1 et de la schwannomatose citées dans ce cours.', 'c72-nf1')
add_if_absent('H3', [('H','Histone'),('3','famille H3')], 'Histone H3',
              'L’histone H3 est une protéine autour de laquelle s’enroule l’ADN. Ses modifications, comme celle de la lysine en position 27, règlent l’expression des gènes.', 'c72-h3k27')
add_if_absent('K27', [('K','Lysine (symbole à une lettre)'),('27','position 27 de l’histone H3')], 'Lysine en position 27 de l’histone H3',
              'Cette position peut être mutée ou modifiée. Le gliome diffus de la ligne médiane est défini par une altération de H3 K27.', 'c72-dmg')
add_if_absent('K27M', [('K27','lysine en position 27'),('M','remplacée par la méthionine')], 'Substitution de la lysine 27 par une méthionine sur l’histone H3',
              'Cette mutation est recherchée par immunohistochimie dans tout gliome diffus de la ligne médiane.', 'c72-biopsie')
add_if_absent('H3K27me3', [('H3','histone H3'),('K27','lysine en position 27'),('me3','triméthylation')], 'Triméthylation de la lysine 27 de l’histone H3',
              'Sa perte en immunohistochimie accompagne l’altération H3 K27 du gliome diffus de la ligne médiane.', 'c72-h3k27')
add_if_absent('EZHIP', [('EZH','Enhancer of Zeste Homolog'),('I','Inhibitory'),('P','Protein')], 'Enhancer of Zeste Homolog Inhibitory Protein',
              'Sa surexpression est, avec la mutation de H3 K27, une des deux altérations qui définissent le gliome diffus de la ligne médiane H3 K27-altéré.', 'c72-dmg')
add_if_absent('NF2', [('NF','Neurofibromatose'),('2','type 2')], 'Neurofibromatose de type 2 (nom du gène NF2)',
              'Une altération de NF2 est caractéristique de l’épendymome spinal selon l’OMS 2021.', 'c72-nf2')
add_if_absent('MYCN', [('MYC','Myelocytomatosis viral oncogene'),('N','Neuroblastoma-derived')], 'Gène MYCN',
              'Son amplification définit l’épendymome spinal MYCN-amplifié, de comportement agressif.', 'c72-mycn')
add_if_absent('MPNST', [('M','Malignant'),('P','Peripheral'),('N','Nerve'),('S','Sheath'),('T','Tumor')], 'Malignant peripheral nerve sheath tumor (tumeur maligne des gaines nerveuses périphériques)',
              'Cette tumeur maligne naît de la gaine d’un nerf. Elle complique la neurofibromatose de type 1 avec un risque de 8 à 16 % sur la vie entière.', 'c72-alarme-mpnst')
add_if_absent('SP-SE', [('SP','Spinal'),('SE','Subependymoma')], 'Groupe de méthylation spinal du subépendymome',
              'Ce groupe concerne exclusivement des adultes.', 'c72-moleculaire')
add_if_absent('SP-MPE', [('SP','Spinal'),('MPE','Myxopapillary Ependymoma')], 'Groupe de méthylation spinal de l’épendymome myxopapillaire',
              'Il comprend les sous-groupes MPE-A et MPE-B.', 'c72-moleculaire')
add_if_absent('SP-EPN', [('SP','Spinal'),('EPN','Ependymoma')], 'Groupe de méthylation spinal de l’épendymome, grades 2 et 3',
              'Il rassemble les épendymomes spinaux conventionnels.', 'c72-moleculaire')
add_if_absent('MPE-A', [('MPE','Myxopapillary Ependymoma'),('A','sous-groupe A')], 'Sous-groupe A de l’épendymome myxopapillaire',
              'Il touche des patients plus jeunes, se prête moins à l’exérèse complète et a un pronostic plus mauvais que MPE-B.', 'c72-moleculaire')
add_if_absent('MPE-B', [('MPE','Myxopapillary Ependymoma'),('B','sous-groupe B')], 'Sous-groupe B de l’épendymome myxopapillaire',
              'Il a un meilleur pronostic que MPE-A.', 'c72-moleculaire')
add_if_absent('MPE', [('M','Myxo-'),('P','Papillary'),('E','Ependymoma')], 'Myxopapillary ependymoma (épendymome myxopapillaire)',
              'Cette tumeur siège surtout au cône médullaire et au filum terminal ; elle est de grade 2 depuis l’OMS 2021.', 'c72-mpe-rt')
add_if_absent('MGMT', [('M','Méthyl'),('G','Guanine'),('M','Méthyl'),('T','Transférase')], 'O6-méthylguanine-ADN méthyltransférase',
              'Cette enzyme répare l’ADN endommagé par des agents alkylants comme le témozolomide. Un promoteur non méthylé, habituel dans le gliome H3 K27-altéré, rend le bénéfice du témozolomide incertain.', 'c72-h3k27')
add_if_absent('SMARCB1', [('SMARC','SWI/SNF-related Matrix-associated Actin-dependent Regulator of Chromatin'),('B','subfamily B'),('1','member 1')], 'Gène SMARCB1',
              'Son altération est à l’origine d’une forme de schwannomatose, avec un risque accru de MPNST.', 'c72-schwannomatose')
add_if_absent('Li-Fraumeni', [('Li','Frederick P. Li, médecin'),('Fraumeni','Joseph F. Fraumeni Jr, médecin')], 'Syndrome de Li-Fraumeni',
              'Ce syndrome de prédisposition tumorale figure parmi ceux qui favorisent les gliomes.', 'c72-predisposition')
add_if_absent('Hippel-Lindau', [('Hippel','Eugen von Hippel, ophtalmologue'),('Lindau','Arvid Lindau, pathologiste')], 'Maladie de Von Hippel-Lindau',
              'Cette maladie génétique est associée à l’hémangioblastome, qui entre dans le diagnostic différentiel des masses intramédullaires.', 'c72-differentiel')
add_if_absent('MOGAD', [('M','Myelin'),('O','Oligodendrocyte'),('G','Glycoprotein'),('A','Antibody-associated'),('D','Disease')], 'Myelin oligodendrocyte glycoprotein antibody-associated disease',
              'Cette maladie inflammatoire du système nerveux central figure parmi les causes inflammatoires à distinguer d’une atteinte du cône et de la queue de cheval.', 'c72-meta-lepto')
add_if_absent('QUANTEC', [('QUANTEC','Quantitative Analyses of Normal Tissue Effects in the Clinic, sigle formé des syllabes initiales')], 'Quantitative Analyses of Normal Tissue Effects in the Clinic',
              'Ce travail de synthèse fournit des relations dose-risque pour les tissus sains. Il sert ici à estimer le risque de myélopathie radique.', 'c72-rt-tolerance')
add_if_absent('PES', [('P','Potentiels'),('E','Évoqués'),('S','Somesthésiques')], 'Potentiels évoqués somesthésiques',
              'Cette technique de neuromonitorage peropératoire surveille la conduction des voies sensitives.', 'c72-neuromonitorage')
add_if_absent('PEM', [('P','Potentiels'),('E','Évoqués'),('M','Moteurs')], 'Potentiels évoqués moteurs',
              'Cette technique de neuromonitorage peropératoire surveille la conduction des voies motrices ; sa sensibilité est de 84 % dans la source lue.', 'c72-neuromonitorage')
add_if_absent('TP53', [('T','Tumor'),('P','Protein'),('53','masse moléculaire de 53 kilodaltons')], 'Tumor protein 53',
              'Ce gène suppresseur de tumeur est altéré dans une partie des gliomes diffus de la ligne médiane H3 K27-altérés.', 'c72-dmg')
add_if_absent('ACVR1', [('ACVR','Activin A Receptor'),('1','type 1')], 'Activin A receptor type 1',
              'Ce gène est altéré dans une partie des gliomes diffus de la ligne médiane H3 K27-altérés.', 'c72-dmg')
add_if_absent('PDGFRA', [('P','Platelet-'),('D','Derived'),('G','Growth'),('F','Factor'),('R','Receptor'),('A','Alpha')], 'Platelet-derived growth factor receptor alpha',
              'Ce gène est altéré dans une partie des gliomes diffus de la ligne médiane H3 K27-altérés.', 'c72-dmg')
add_if_absent('KIAA1549', [('KIAA1549','nom de gène issu d’une nomenclature de projet de séquençage, non développable lettre à lettre')], 'Gène KIAA1549',
              'Sa fusion avec BRAF caractérise l’astrocytome pilocytique et ouvre la discussion des inhibiteurs BRAF et MEK.', 'c72-d-bio-braf')
add_if_absent('MEK', [('M','Mitogen-activated protein kinase /'),('E','ERK'),('K','Kinase')], 'Mitogen-activated protein kinase / ERK kinase',
              'Cette enzyme est la cible des inhibiteurs de MEK, proposés pour les tumeurs BRAF-altérées.', 'c72-d-bio-braf')
add_if_absent('IDH', [('I','Isocitrate'),('DH','Déshydrogénase')], 'Isocitrate déshydrogénase',
              'Cette enzyme est fréquemment mutée dans les gliomes intracrâniens, mais rarement dans les gliomes de la moelle.', 'c72-astro')
add_if_absent('ANNUBP', [('A','Atypical'),('N','Neurofibromatous'),('N','Neoplasm'),('U','of Uncertain'),('B','Biologic'),('P','Potential')], 'Atypical neurofibromatous neoplasm of uncertain biologic potential',
              'Ce neurofibrome atypique de la neurofibromatose de type 1 n’est pas encore un MPNST.', 'c72-alarme-mpnst')
add_if_absent('NOS', [('N','Not'),('O','Otherwise'),('S','Specified')], 'Not otherwise specified (non spécifié par ailleurs)',
              'Ce suffixe de l’OMS 2021 signale un test non fait ou non concluant.', 'c72-oms2021')
add_if_absent('NEC', [('N','Not'),('E','Elsewhere'),('C','Classified')], 'Not elsewhere classified (non classé ailleurs)',
              'Ce suffixe de l’OMS 2021 signale des résultats qui ne correspondent à aucune entité.', 'c72-oms2021')
add_if_absent('CIM-O', [('C','Classification'),('I','Internationale des'),('M','Maladies pour l’'),('O','Oncologie')], 'Classification internationale des maladies pour l’oncologie',
              'Son code de comportement (0 bénin, 1 incertain, 3 malin) détermine la catégorie CIM-10 et la déclaration au registre des tumeurs.', 'c72-nkrs')
add_if_absent('ONC201', [('ONC201','nom de code d’un produit en développement, non développable lettre à lettre')], 'ONC201 (dordaviprone)',
              'Ce produit n’a pas d’information professionnelle trouvée dans la base suisse au 15 octobre 2026.', 'c72-onc201')
for _code, _lab, _ref in [
    ('C72.0', 'Moelle épinière', 'c72-codes'), ('C72.1', 'Queue de cheval', 'c72-codes'),
    ('C72.2', 'Nerf olfactif (I)', 'c72-codes'), ('C72.3', 'Nerf optique (II)', 'c72-codes'),
    ('C72.4', 'Nerf auditif ou vestibulocochléaire (VIII)', 'c72-codes'),
    ('C72.5', 'Autres nerfs crâniens et nerfs crâniens non précisés', 'c72-codes'),
    ('C72.8', 'Lésion à localisations contiguës de l’encéphale et d’autres parties du système nerveux central', 'c72-codes'),
    ('C72.9', 'Système nerveux central sans précision', 'c72-codes'),
    ('C30.0', 'Code cité pour le rattachement non vérifié de l’esthésioneuroblastome (C72.2 ou C30.0)', 'c72-codes'),
    ('D33.4', 'Code de tumeur bénigne de la moelle épinière où l’hémangioblastome se classe selon la source lue, hors C72', 'c72-differentiel'),
    ('D35.2', 'Code de tumeur bénigne de l’hypophyse, cité dans l’aide-mémoire de déclaration', 'c72-nkrs'),
    ('D43.3', 'Tumeur à évolution imprévisible ou inconnue des nerfs crâniens, où se code une tumeur de comportement /1 du nerf optique', 'c72-codes'),
    ('D43.4', 'Tumeur à évolution imprévisible ou inconnue de la moelle épinière, où se code une tumeur de comportement /1 comme l’épendymome myxopapillaire', 'c72-codes'),
    ('C79.4', 'Code de tumeur maligne secondaire du système nerveux, cité pour la compression médullaire métastatique', 'c72-compression')]:
    add_if_absent(_code, [(_code[0], 'lettre de chapitre de la CIM-10-GM'), (_code[1:], 'catégorie et subdivision')], 'Code CIM-10-GM ' + _code,
                  _lab + '.', _ref)
