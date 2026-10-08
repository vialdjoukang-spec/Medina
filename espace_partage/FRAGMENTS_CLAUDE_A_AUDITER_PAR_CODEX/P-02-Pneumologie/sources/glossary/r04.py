# Glossaire MEDINA — R04 Hémorragie des voies respiratoires (P-02-Pneumologie)
from cardio_1 import a, G


def b(k, *args):
    """Ajoute la clé seulement si aucun autre glossaire ne l’a déjà définie."""
    if k not in G:
        a(k, *args)


# Codes CIM-10-GM 2024 de la catégorie R04
for c, t, d in [
    ('R04.0', 'Épistaxis', 'Saignement de nez, hémorragie nasale.'),
    ('R04.1', 'Hémorragie de la gorge', 'Exclut l’hémoptysie (R04.2).'),
    ('R04.2', 'Hémoptysie', 'Expectoration sanglante, toux avec hémorragie.'),
    ('R04.8', 'Hémorragie d’autres parties des voies respiratoires', 'Inclut l’hémorragie pulmonaire sans autre précision ; exclut l’hémorragie pulmonaire périnatale (P26).'),
    ('R04.9', 'Hémorragie des voies respiratoires, sans précision', 'Code d’attente lorsque le site du saignement n’est pas précisé.'),
]:
    b(c, [('R04', 'catégorie R04 — Hémorragie des voies respiratoires'), (c[3:], 'sous-code : ' + t)], c + ' — ' + t + ' (CIM-10-GM 2024)',
      '<p>Code de la Classification internationale des maladies, 10e révision, modification allemande, version 2024 (BfArM) : ' + t + '. ' + d + '</p>')

# Sociétés savantes
b('ORL', [('O', 'Oto-'), ('R', 'Rhino-'), ('L', 'Laryngologie')], 'Oto-rhino-laryngologie',
  '<p>Spécialité médicale et chirurgicale de l’oreille, du nez, des sinus, du pharynx et du larynx. Elle prend en charge l’épistaxis postérieure ou réfractaire et l’hémorragie après amygdalectomie.</p>')
b('CIRSE', [('C', 'Cardiovascular and'), ('I', 'Interventional'), ('R', 'Radiological'), ('S', 'Society of'), ('E', 'Europe')],
  'Cardiovascular and Interventional Radiological Society of Europe (Société européenne de radiologie cardiovasculaire et interventionnelle)',
  '<p>Société savante européenne de radiologie interventionnelle. Ses standards de pratique de 2022 sur l’embolisation des artères bronchiques définissent l’hémoptysie menaçante, les indications, les agents d’embolisation et les complications.</p>')

# Nom propre composé

# Noms d’essai et de recommandation
b('NoPAC', [('No', 'No (sans, réduire le recours au)'), ('PAC', 'PACking (méchage nasal)')], 'Essai NoPAC (acide tranexamique topique et méchage nasal ; acronyme d’essai, non développable lettre à lettre de façon officielle)',
  '<p>Essai randomisé britannique (Reuben, Annals of Emergency Medicine 2021) : chez 496 adultes, l’acide tranexamique topique n’a pas réduit le recours au méchage antérieur dans l’épistaxis persistante.</p>', 'r04-nopac')
b('NG12', [('N', 'NICE'), ('G', 'Guideline (recommandation)'), ('12', 'numéro 12')], 'Recommandation NICE NG12 : cancer suspecté, reconnaissance et orientation',
  '<p>Recommandation britannique sur l’orientation rapide des patients suspects de cancer ; elle cite l’hémoptysie inexpliquée à partir de 40 ans parmi les motifs d’orientation pour cancer bronchique.</p>')

# Fragments MEDINA cités en renvoi
for lab, lit, ordre in [
    ('O-09-Oncologie, génétique médicale et soins palliatifs', 'Oncologie', 'neuvième'),
    ('O-17-Oto-rhino-laryngologie et médecine bucco-dentaire', 'Oto-rhino-laryngologie', 'dix-septième'),
    ('I-13-Immunologie et allergologie', 'Immunologie', 'treizième'),
    ('E-06-Endocrinologie et métabolisme', 'Endocrinologie', 'sixième'),
]:
    num = lab.split('-')[1]
    b(lab, [(lab[0], lit + ' (initiale de la spécialité)'), (num, ordre + ' fragment dans l’ordre de production'), (lab.split('-', 2)[2], 'nom littéral du fragment')],
      'Fragment ' + lab + ' de MEDINA', '<p>Fragment de production de MEDINA défini dans organisation/fragments.json.</p>')
