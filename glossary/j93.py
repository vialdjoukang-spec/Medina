from cardio_1 import a, G
# Abréviations propres au cours J93 — Pneumothorax (P-02-Pneumologie).
# BTS est défini dans glossary/j90.py (injecté le 08.10.2026) et n’est pas redéfini ici.
a('SPLF', [('S', 'Société de'), ('P', 'Pneumologie de'), ('L', 'Langue'), ('F', 'Française')], 'Société de pneumologie de langue française', '<p>Société savante francophone de pneumologie. Ses recommandations de 2023 sur le pneumothorax spontané primaire, rédigées avec les sociétés françaises de médecine d’urgence, de réanimation, d’anesthésie-réanimation et de chirurgie thoracique selon la méthode GRADE, ont paru dans Annals of Intensive Care.</p>')
a('GRADE', [('G', 'Grading of'), ('R', 'Recommendations'), ('A', 'Assessment,'), ('D', 'Development and'), ('E', 'Evaluation')], 'Méthode de cotation des recommandations et du niveau de preuve', '<p>Méthode internationale qui évalue la qualité des preuves (élevée, modérée, faible, très faible) et la force des recommandations (forte ou conditionnelle). Les recommandations européennes de 2024 et françaises de 2023 sur le pneumothorax l’appliquent.</p>')
a('Birt-Hogg-Dubé', [('Birt-Hogg-Dubé', 'noms propres : Arthur Birt, Georgina Hogg et W. James Dubé, médecins canadiens, 1977')], 'Syndrome de Birt-Hogg-Dubé', '<p>Maladie héréditaire due à des variants du gène <i>FLCN</i>, cause familiale de pneumothorax par kystes pulmonaires.</p>')
a('FLCN', [('FLCN', 'FoLliCuliN (folliculine)')], 'Gène de la folliculine', '<p>Gène de la folliculine ; ses variants causent le syndrome de Birt-Hogg-Dubé, cause familiale de pneumothorax.</p>')
a('TSC1', [('T', 'Tuberous'), ('S', 'Sclerosis'), ('C', 'Complex'), ('1', 'gène 1')], 'Gène 1 du complexe de la sclérose tubéreuse', '<p>Premier gène du complexe de la sclérose tubéreuse, maladie qui peut s’accompagner de lymphangioléiomyomatose et de pneumothorax.</p>')
a('TSC2', [('T', 'Tuberous'), ('S', 'Sclerosis'), ('C', 'Complex'), ('2', 'gène 2')], 'Gène 2 du complexe de la sclérose tubéreuse', '<p>Second gène du complexe de la sclérose tubéreuse, maladie qui peut s’accompagner de lymphangioléiomyomatose et de pneumothorax.</p>')
a('CFTR', [('C', 'Cystic'), ('F', 'Fibrosis'), ('T', 'Transmembrane conductance'), ('R', 'Regulator')], 'Régulateur de la conductance transmembranaire de la mucoviscidose', '<p>Gène dont les variants causent la mucoviscidose ; le pneumothorax y signale une maladie avancée.</p>')
for code, title, d in [
    ('J93.0', 'Pneumothorax spontané avec pression positive', 'Pneumothorax spontané sous tension, développé dans le cours J93 — Pneumothorax.'),
    ('J93.1', 'Autres pneumothorax spontanés', 'Pneumothorax spontané primaire ou secondaire sans tension, développé dans le cours J93 — Pneumothorax.'),
    ('J93.8', 'Autres pneumothorax', 'Formes particulières non classées ailleurs, traitées dans le cours J93 — Pneumothorax.'),
    ('J93.9', 'Pneumothorax, sans précision', 'Mécanisme non documenté ; à préciser dès que possible.'),
]:
    a(code, [(code, 'code CIM-10-GM 2024')], title, '<p>' + d + '</p>')
