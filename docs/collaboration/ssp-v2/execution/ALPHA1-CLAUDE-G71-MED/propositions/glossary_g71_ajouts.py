# Propositions pour glossary/g71.py (constats C01 et C13) — à intégrer par une mission d'intégration ; aucune écriture canonique ici.
#
# 1. Correction (C13, MINEUR) : la clé ENMC décompose « M » en « Muscle ». Le sigle désigne le European Neuromuscular Centre
#    [S24 : Breukel et coll., « The impact of European Neuromuscular Centre (ENMC) workshops… », Neuromuscul Disord 2019].
#    Ancien : _add('ENMC', [('E','European'),('N','Neuromuscular'),('M','Muscle'),('C','Centre')], 'Centre européen du muscle et des maladies neuromusculaires',
#    Nouveau :
_add('ENMC', [('E','European'),('N','Neuro'),('M','Muscular'),('C','Centre')], 'Centre neuromusculaire européen (European Neuromuscular Centre)',
     'Organisme qui organise des ateliers internationaux ; le 229<sup>e</sup> atelier de 2017 a réformé la nomenclature des dystrophies des ceintures, le 277<sup>e</sup> celle des myopathies congénitales.')

# 2. Sigles nouveaux de la sémiologie proposée (propositions/G71_c_semio.html).
_add('MRC', [('M','Medical'),('R','Research'),('C','Council')], 'Medical Research Council (conseil britannique de la recherche médicale)',
     'Auteur de l’échelle de cotation de la force musculaire de 0 à 5 (mémorandum 45, p. 7).', 'g71-sm-faiblesse')
_add('ENMG', [('E','Électro'),('N','Neuro'),('M','Myo'),('G','Gramme')], 'Électroneuromyogramme',
     'Exploration électrique des nerfs et des muscles qui distingue une atteinte myogène d’une atteinte neurogène.', 'g71-emg')
