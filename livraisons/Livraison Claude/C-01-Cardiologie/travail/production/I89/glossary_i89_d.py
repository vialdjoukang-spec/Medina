# Glossaire MEDINA — I89, rédacteur D (onglet Pharmacologie, fenêtres pop4). À fusionner par le vérificateur dans glossary_i89.py.
# Contrôle du 07.10.2026 : CYP2A6, McCormack et I-03-Infectiologie n’existent pas dans glossary/ ; C-01-Cardiologie est aussi
# défini à l’identique dans ../I83/glossary_i83_d.py (même sens) : n’en garder qu’une entrée à l’intégration.
from cardio_1 import a, G

L = [
('CYP2A6', [('CYP', 'CYtochrome P450'), ('2', 'famille 2'), ('A', 'sous-famille A'), ('6', 'isoenzyme 6')],
 'Cytochrome P450 2A6',
 '<p>Enzyme hépatique qui transforme la coumarine en 7-hydroxycoumarine, métabolite non toxique. Chez un métaboliseur lent, la coumarine passe par d’autres voies qui produisent des métabolites hépatotoxiques (Farinola et Piller, Pharmacogenomics 2007).</p>',
 'i89-d-benzopyrones'),
('McCormack', [('McCormack', 'nom propre : Francis X. McCormack, pneumologue américain, premier auteur de l’essai du sirolimus dans la lymphangioléiomyomatose (2011) ; ce n’est pas une abréviation')],
 'Essai de McCormack et al. (2011)',
 '<p>Essai randomisé en double aveugle (New England Journal of Medicine 2011) chez 89 patientes atteintes de lymphangioléiomyomatose : le sirolimus pendant 12 mois a stabilisé le volume expiratoire maximal par seconde, alors qu’il déclinait sous placebo ; le déclin a repris à l’arrêt.</p>',
 'i89-d-sirolimus'),
('I-03-Infectiologie', [('I', 'Infectiologie (initiale de la spécialité)'), ('03', 'troisième fragment dans l’ordre de production'), ('Infectiologie', 'nom littéral du fragment')],
 'Fragment I-03-Infectiologie de MEDINA',
 '<p>Troisième fragment de production de MEDINA, qui réunit les cours d’infectiologie (organisation/fragments.json). Le futur cours A46 — Érysipèle y est rattaché par le catalogue CIM-10-GM.</p>'),
('C-01-Cardiologie', [('C', 'Cardiologie (initiale de la spécialité)'), ('01', 'premier fragment dans l’ordre de production'), ('Cardiologie', 'nom littéral du fragment')],
 'Fragment C-01-Cardiologie de MEDINA',
 '<p>Premier fragment de production de MEDINA, qui réunit les cours de cardiologie et d’angiologie (organisation/fragments.json). Un cours cité hors du cours courant s’écrit « code — intitulé (fragment) », par exemple « I80 — Thrombose veineuse profonde et thromboses veineuses (C-01-Cardiologie) ».</p>'),
]
for x in L:
    a(*x)
