# Proposition d’audit ALPHA1-CLAUDE-G99-MED (constat C02) : entrées à AJOUTER à la fin de glossary/g99.py,
# avec la fonction _add déjà définie dans ce fichier (entrées conditionnelles, aucun terme existant écrasé).
# Source : BfArM, ICD-10-GM 2024, bloc G90–G99 et chapitres M et E (classification utilisée en Suisse par l’OFS).
for _c, _t, _ref in [
    ('G99.0', 'Neuropathie autonome au cours de maladies endocriniennes et métaboliques', 'g99-toronto'),
    ('G99.00', 'Gastroparésie lors de neuropathie autonome au cours de maladies endocriniennes et métaboliques', 'g99-gp'),
    ('G99.08', 'Autre neuropathie autonome au cours de maladies endocriniennes et métaboliques', 'g99-toronto'),
    ('G99.1', 'Autres affections du système nerveux autonome au cours d’autres maladies classées ailleurs', 'g99-ho'),
    ('G99.2', 'Myélopathie au cours de maladies classées ailleurs', 'g99-mcd'),
    ('G99.8', 'Autres affections précisées du système nerveux au cours de maladies classées ailleurs (paralysie urémique)', 'g99-uremie'),
]:
    _add(_c, [(_c[:3], 'catégorie de la classification internationale des maladies'), (_c[3:], 'sous-rubrique')], _t + ' (' + _c + '*)',
         '<p>Sous-rubrique astérisque de la CIM-10-GM 2024 : elle ne se code qu’avec le code † de la maladie causale.</p>', _ref)
for _c, _t, _ref in [
    ('M47.0', 'Syndrome de compression de l’artère spinale antérieure et de l’artère vertébrale', 'g99-mcd'),
    ('M47.1', 'Autres spondyloses avec myélopathie', 'g99-mcd'),
    ('M50.0', 'Atteinte d’un disque cervical avec myélopathie', 'g99-mcd'),
    ('M51.0', 'Atteinte d’un disque lombaire ou d’un autre disque intervertébral avec myélopathie', 'g99-mcd'),
    ('E10.4', 'Diabète de type 1 avec complications neurologiques', 'g99-toronto'),
    ('E11.4', 'Diabète de type 2 avec complications neurologiques', 'g99-toronto'),
]:
    _add(_c, [(_c[:3], 'catégorie de la classification internationale des maladies'), (_c[3:], 'sous-rubrique')], _t + ' (' + _c + '†)',
         '<p>Code de la maladie causale (†) associé à une sous-rubrique G99 dans la CIM-10-GM 2024.</p>', _ref)
