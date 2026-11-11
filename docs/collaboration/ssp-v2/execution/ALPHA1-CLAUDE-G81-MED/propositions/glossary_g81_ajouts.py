# Proposition ALPHA1-CLAUDE-G81-MED (constats C07, C10, C24) — lignes à ajouter à glossary/g81.py, non injectées.
# NIHSS, ESMINT, MRC, IRM, FLAIR, ESO et AVC existent déjà dans d'autres glossaires (add_if_absent les ignore).

add_if_absent('UMVF', [('U', 'Université'), ('M', 'Médicale'), ('V', 'Virtuelle'), ('F', 'Francophone')],
              'Université médicale virtuelle francophone',
              'Plateforme d’enseignement des facultés de médecine francophones ; son cours de sémiologie neurologique fonde la sémiologie de cette leçon.', 'g81-sm-definitions')

# Correction C24 : remplacer la décomposition littérale de SMNS (la lettre N n'est pas « supérieur ») :
# add_if_absent('SMNS', [('S', 'Syndrome'), ('M', 'du MotoNeurone (M)'), ('N', 'du MotoNeurone (N)'), ('S', 'Supérieur')], ...)
# par :
add_if_absent('SMNS', [('S', 'Syndrome'), ('M', 'du Moto- (motoneurone)'), ('N', '-Neurone (motoneurone)'), ('S', 'Supérieur')],
              'Syndrome du motoneurone supérieur',
              'Ensemble de signes négatifs (faiblesse, hypotonie) et positifs (spasticité, hyperréflexie, clonus, signe de Babinski). La spasticité n’en est qu’une composante.', 'g81-smns')
