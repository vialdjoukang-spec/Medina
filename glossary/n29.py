from cardio_1 import a, G
# N29 — Autres affections du rein et de l’uretère au cours de maladies classées ailleurs (N-07-Néphrologie).
# Entrées conditionnelles : aucun terme existant dans G n’est écrasé.
def _code(k, lit, full, d, ref=None):
    if k not in G:
        a(k, [(k, lit)], full, '<p>' + d + '</p>', ref)
_code('N29.0', 'code de la CIM-10-GM 2024, catégorie N29, sous-code 0 (astérisque)', 'Syphilis tardive du rein (N29.0*)', 'Code à astérisque : manifestation rénale d’une syphilis tardive, associée au code à croix A52.7. Une glomérulopathie de la syphilis se code N08.0*.', 'n29-asterisque')
_code('N29.1', 'code de la CIM-10-GM 2024, catégorie N29, sous-code 1 (astérisque)', 'Affections du rein et de l’uretère au cours de maladies infectieuses et parasitaires classées ailleurs (N29.1*)', 'Code à astérisque associé notamment à la tuberculose (A18.1†) et à la schistosomiase (B65.-†).', 'n29-asterisque')
_code('N29.8', 'code de la CIM-10-GM 2024, catégorie N29, sous-code 8 (astérisque)', 'Affections du rein et de l’uretère au cours d’autres maladies classées ailleurs (N29.8*)', 'Code à astérisque associé notamment à la cystinose (E72.0†).', 'n29-asterisque')
_code('A52.7', 'code de la CIM-10-GM 2024, syphilis tardive évolutive', 'Autre syphilis tardive évolutive (A52.7†)', 'Code à croix qui comprend la gomme syphilitique et la syphilis tertiaire de toute localisation, hors A52.0 à A52.3.', 'n29-asterisque')
_code('A52.0', 'code de la CIM-10-GM 2024, syphilis cardiovasculaire tardive', 'Syphilis cardiovasculaire tardive (A52.0)', 'Code exclu de A52.7.', 'n29-asterisque')
_code('A52.3', 'code de la CIM-10-GM 2024, neurosyphilis tardive sans précision', 'Neurosyphilis tardive sans précision (A52.3)', 'Code exclu de A52.7.', 'n29-asterisque')
_code('A18.1', 'code de la CIM-10-GM 2024, tuberculose de l’appareil génito-urinaire', 'Tuberculose de l’appareil génito-urinaire (A18.1†)', 'Code à croix associé à N29.1* pour la tuberculose urogénitale.', 'n29-asterisque')
_code('E72.0', 'code de la CIM-10-GM 2024, troubles du transport des acides aminés', 'Troubles du transport des acides aminés dont la cystinose (E72.0†)', 'Code à croix associé à N29.8* et à N16.3* pour la cystinose.', 'n29-asterisque')
_code('N08.0', 'code de la CIM-10-GM 2024, glomérulopathie au cours de maladies infectieuses (astérisque)', 'Affections glomérulaires au cours de maladies infectieuses et parasitaires (N08.0*)', 'Code à astérisque qui reçoit les glomérulopathies de la syphilis et de la schistosomiase, et non N29.', 'n29-asterisque')
_code('N16.3', 'code de la CIM-10-GM 2024, atteinte tubulo-interstitielle au cours de maladies métaboliques (astérisque)', 'Atteinte tubulo-interstitielle rénale au cours de maladies métaboliques (N16.3*)', 'Code à astérisque qui figure aussi pour la cystinose, en plus de N29.8*.', 'n29-asterisque')
if 'CTNS' not in G:
    a('CTNS', [('CTNS', 'symbole du gène de la cystinosine (cystinosis, nephropathic) ; aucun développement littéral lettre à lettre')], 'Gène de la cystinosine (17p13.2)', '<p>Le gène <i>CTNS</i> code la cystinosine, un symport cystine/proton lysosomal. Des variants bialléliques causent la cystinose.</p>', 'n29-cyst-gene')
if 'JJ' not in G:
    a('JJ', [('J', 'sonde en forme de J'), ('J', 'à crosse en J aux deux extrémités')], 'Sonde urétérale double J', '<p>La sonde urétérale JJ draine le haut appareil urinaire. Dans la tuberculose urogénitale obstructive, elle ou la néphrostomie ne doit pas être retardée.</p>', 'n29-drainage')
if 'NDNF' not in G:
    a('NDNF', [('N', 'Neuron'), ('D', 'Derived'), ('N', 'Neurotrophic'), ('F', 'Factor (facteur neurotrophique dérivé des neurones)')], 'Facteur neurotrophique dérivé des neurones', '<p>Le NDNF est proposé comme antigène cible dans la néphropathie extramembraneuse associée à la syphilis précoce.</p>', 'n29-syph-glomerulo')
