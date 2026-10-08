# Glossaire MEDINA — I89, rédacteur C (onglets Examens et Sciences, fenêtres pop3). À fusionner par le vérificateur dans glossary_i89.py.
# Contrôle du 07.10.2026 : C-01-Cardiologie n’existe pas dans glossary/ ; il est défini à l’identique dans glossary_i89_d.py
# et ../I83/glossary_i83_d.py (même sens) : n’en garder qu’une entrée à l’intégration.
from cardio_1 import a, G

a('C-01-Cardiologie', [('C', 'Cardiologie (initiale de la spécialité)'), ('01', 'premier fragment dans l’ordre de production'), ('Cardiologie', 'nom littéral du fragment')],
  'Fragment C-01-Cardiologie de MEDINA',
  '<p>Premier fragment de production de MEDINA, qui réunit les cours de cardiologie et d’angiologie (organisation/fragments.json). Un cours cité hors du cours courant s’écrit « code — intitulé (fragment) », par exemple « I80 — Thrombose veineuse profonde et thromboses veineuses (C-01-Cardiologie) ».</p>')
