# Glossaire MEDINA — I83, rédacteur C (onglets Examens et Sciences). À fusionner par le vérificateur dans glossary_i83.py.
from cardio_1 import a, G

L = [
('PIK3CA', [('PI', 'PhosphatidylInositol (phosphatidylinositol)'), ('K', 'Kinase'), ('3', '3 (phosphorylation en position 3 de l’inositol)'), ('CA', 'Catalytic subunit Alpha (sous-unité catalytique alpha)')],
 'Gène de la sous-unité catalytique alpha de la phosphatidylinositol-4,5-bisphosphate 3-kinase',
 '<p>Gène d’une enzyme de signalisation qui stimule la croissance et la prolifération cellulaires. Des variants activateurs apparus pendant le développement, présents seulement dans une partie des cellules du tissu atteint (mosaïque somatique), causent la plupart des syndromes de Klippel-Trénaunay et d’autres malformations vasculaires avec hypertrophie (Luks et al., J Pediatr 2015). Ils se recherchent dans le tissu malformé et non dans le sang.</p>', 'i83-gen'),
]
for x in L:
    a(*x)
