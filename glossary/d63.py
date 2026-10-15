from cardio_1 import a, G
# D63 — Anémie au cours de maladies chroniques classées ailleurs (H-08-Hématologie). Entrées conditionnelles : aucun terme existant dans G n’est écrasé.
if 'D63.0' not in G:
    a('D63.0', [('D63', 'catégorie CIM-10-GM : anémie au cours de maladies chroniques classées ailleurs'), ('.0', 'au cours de néoplasies (astérisque, manifestation)')], 'Code CIM-10-GM D63.0* : anémie au cours de néoplasies', '<p>Code astérisque : il se code en complément de la tumeur causale (code croix, de C00 à D48).</p>', 'd63-nosologie')
if 'D63.8' not in G:
    a('D63.8', [('D63', 'catégorie CIM-10-GM : anémie au cours de maladies chroniques classées ailleurs'), ('.8', 'au cours d’autres maladies chroniques classées ailleurs (astérisque), dont la maladie rénale chronique de stade 3 et plus')], 'Code CIM-10-GM D63.8* : anémie au cours d’autres maladies chroniques', '<p>Code astérisque qui inclut l’anémie de la maladie rénale chronique de stade 3 à 5 (N18.3 à N18.5, codes croix).</p>', 'd63-nosologie')
if 'D63.1' not in G:
    a('D63.1', [('D63', 'catégorie D63 de la classification'), ('.1', 'sous-catégorie absente de la CIM-10-GM 2024')], 'Code D63.1, inexistant en CIM-10-GM 2024', '<p>Le libellé « anémie de la maladie rénale chronique » à ce code appartient à la CIM-10-CM américaine. En Suisse, cette anémie se code D63.8* avec le code croix N18.</p>', 'd63-nosologie')
if 'CIM-10-CM' not in G:
    a('CIM-10-CM', [('C', 'Classification'), ('I', 'Internationale des'), ('M', 'Maladies'), ('10', '10e révision'), ('CM', 'Clinical Modification (modification clinique américaine)')], 'Classification internationale des maladies, 10e révision, modification clinique américaine', '<p>Version américaine de la CIM-10, non utilisée en Suisse. Elle contient un code D63.1 absent de la CIM-10-GM.</p>', 'd63-nosologie')
for code, txt in (('N18.3', 'stade 3'), ('N18.4', 'stade 4'), ('N18.5', 'stade 5')):
    if code not in G:
        a(code, [('N18', 'catégorie CIM-10-GM : maladie rénale chronique'), ('.' + code[-1], 'sous-catégorie : ' + txt)], 'Code CIM-10-GM ' + code + ' : maladie rénale chronique, ' + txt, '<p>Code croix (étiologie) associé à D63.8* lorsque l’anémie complique la maladie rénale chronique.</p>', 'd63-nosologie')
if 'G3' not in G:
    a('G3', [('G', 'Grade du débit de filtration glomérulaire (classification KDIGO)'), ('3', 'stade 3, débit de filtration glomérulaire modérément à sévèrement diminué')], 'Stade G3 de la maladie rénale chronique', '<p>Stade de la classification KDIGO de la maladie rénale chronique selon le débit de filtration glomérulaire. Le stade 3 et les suivants relèvent du code D63.8* lorsqu’une anémie les complique.</p>')
if 'PU.1' not in G:
    a('PU.1', [('PU', 'facteur de transcription de la famille ETS ; nom propre, sans développement littéral fourni par la source'), ('.1', 'numéro d’identification')], 'Facteur de transcription PU.1', '<p>Selon la revue de 2019, l’interféron γ inhibe la différenciation des précurseurs érythroïdes par PU.1.</p>', 'd63-epo')
if 'Bence-Jones' not in G:
    a('Bence-Jones', [('Bence-Jones', 'nom du médecin britannique qui a décrit la protéinurie ; nom propre, non une abréviation')], 'Protéinurie de Bence-Jones', '<p>Excrétion urinaire de chaînes légères libres monoclonales, cherchée avec la protéine monoclonale du sérum dans le bilan d’exclusion de KDIGO 2026.</p>', 'd63-exclusion')
