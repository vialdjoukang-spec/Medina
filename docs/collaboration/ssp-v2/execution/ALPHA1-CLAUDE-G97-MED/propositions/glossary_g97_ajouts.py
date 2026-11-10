"""Proposition ALPHA1-CLAUDE-G97-MED (constat C01) : sigles nouveaux des propositions, à ajouter à glossary/g97.py
avec la fonction a() existante (ajout conditionnel : ignoré si la clé existe déjà dans un autre glossaire).
Sigles déjà présents et réutilisés : LCR, ICHD-3, IRM, POSI, AINS. NYHA (glossary/cardio_1.py) et MRC
(glossary/g60.py, n18.py, n27.py) existent déjà : l'ajout conditionnel ci-dessous sera ignoré, il documente seulement
la fenêtre de rattachement. Les propositions écrivent « Medical Research Council » en toutes lettres ; vérifier
build_medina.audit() == {} à l'intégration."""

a('MRC', [('M', 'Medical'), ('R', 'Research'), ('C', 'Council')], 'Medical Research Council',
  'Conseil britannique de la recherche médicale ; son échelle cote la force musculaire de 0 (aucune contraction) à 5 (force normale).',
  'g97-sm-hematome-examen')
