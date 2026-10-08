from cardio_1 import a, G


def b(k, *args):
    """Ajoute la clé seulement si aucun autre glossaire ne l’a déjà définie."""
    if k not in G:
        a(k, *args)


# Sociétés savantes et référentiels
b('ATLS', [('A', 'Advanced'), ('T', 'Trauma'), ('L', 'Life'), ('S', 'Support')], 'Advanced Trauma Life Support (programme de prise en charge avancée du traumatisé)',
  '<p>Programme de formation de l’American College of Surgeons pour la prise en charge initiale du traumatisé. Sa 10e édition (2018) place la décompression à l’aiguille de l’adulte au quatrième ou cinquième espace intercostal, en avant de la ligne axillaire moyenne.</p>')

# Codes CIM-10-GM 2024 employés dans le cours
for c, t in [
    ('J93.0', 'Pneumothorax spontané sous tension'),
    ('J93.1', 'Autres pneumothorax spontanés (primaire ou secondaire sans tension)'),
    ('J93.8', 'Autres pneumothorax'),
    ('J93.9', 'Pneumothorax, sans précision'),
    ('J95.80', 'Pneumothorax iatrogène'),
    
    ('P25.1', 'Pneumothorax survenant pendant la période périnatale'),
    ('S27.0', 'Pneumothorax traumatique'),
    
    ('N80.8', 'Autres endométrioses (dont l’endométriose thoracique)'),
]:
    b(c, [(c, 'code de la CIM-10-GM 2024')], c + ' — ' + t,
      '<p>Code de la Classification internationale des maladies, 10e révision, modification allemande, version 2024 (BfArM) : ' + t + '.</p>')

# Gènes et syndromes
b('FLCN', [('FLCN', 'FoLliCuliN (folliculine)')], 'Gène FLCN, qui code la folliculine',
  '<p>Gène suppresseur de tumeur ; ses variants pathogènes hétérozygotes causent le syndrome de Birt-Hogg-Dubé (kystes pulmonaires, pneumothorax, fibrofolliculomes, tumeurs rénales). La folliculine participe à la régulation de la voie mTOR.</p>')
b('TSC1', [('TSC', 'Tuberous Sclerosis Complex (sclérose tubéreuse)'), ('1', 'gène 1')], 'Gène TSC1 de la sclérose tubéreuse (hamartine)',
  '<p>Gène dont les variants pathogènes causent la sclérose tubéreuse de Bourneville ; la perte de fonction active la voie mTOR et favorise la lymphangioléiomyomatose.</p>')
b('TSC2', [('TSC', 'Tuberous Sclerosis Complex (sclérose tubéreuse)'), ('2', 'gène 2')], 'Gène TSC2 de la sclérose tubéreuse (tubérine)',
  '<p>Gène dont les variants pathogènes causent la sclérose tubéreuse de Bourneville ; la perte de fonction active la voie mTOR et favorise la lymphangioléiomyomatose.</p>')
b('Birt-Hogg-Dubé', [('Birt', 'Arthur Birt'), ('Hogg', 'Georgina Hogg'), ('Dubé', 'William Dubé')], 'Syndrome de Birt-Hogg-Dubé (noms propres des trois auteurs, non une abréviation)',
  '<p>Maladie autosomique dominante due au gène FLCN : kystes pulmonaires basaux, pneumothorax récidivants, fibrofolliculomes du visage et du cou, risque de tumeurs rénales. Son diagnostic impose une surveillance rénale et un conseil génétique.</p>', 'j93-familial')
