# Glossaire MEDINA — I83, rédacteur D (onglet Pharmacologie). À fusionner par le vérificateur dans glossary_i83.py.
from cardio_1 import a, G

L = [
('C-01-Cardiologie', [('C', 'Cardiologie (initiale de la spécialité)'), ('01', 'premier fragment dans l’ordre de production'), ('Cardiologie', 'nom littéral du fragment')],
 'Fragment C-01-Cardiologie de MEDINA',
 '<p>Premier fragment de production de MEDINA, qui réunit les cours de cardiologie et d’angiologie (organisation/fragments.json). Un cours cité hors du cours courant s’écrit « code — intitulé (fragment) », par exemple « I80 — Thrombose veineuse profonde et thromboses veineuses (C-01-Cardiologie) ».</p>'),
]
for x in L:
    a(*x)
