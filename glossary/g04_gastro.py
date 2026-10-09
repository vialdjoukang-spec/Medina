# Glossaire MEDINA — G-04-Gastroentérologie et hépatologie (auteur unique de ce fichier : agent G-04).
from cardio_1 import a, G
def code(k, titre, cours):
    a(k, [(k, 'code CIM-10-GM 2024')], titre, '<p>Sous-catégorie couverte par le cours ' + cours + ' (catalogue OFS, version française 2024).</p>')
def nom(k, auteurs, full, d):
    a(k, [(k, 'noms propres (' + auteurs + '), non une abréviation')], full, d)

# Sociétés et référentiels
a('ESGE', [('E', 'European'), ('S', 'Society of'), ('G', 'Gastrointestinal'), ('E', 'Endoscopy')], 'Société européenne d’endoscopie digestive', '<p>Société savante qui publie les recommandations européennes d’endoscopie : hémorragies hautes non variqueuses (2021) et variqueuses (2022), notamment.</p>')
a('BSG', [('B', 'British'), ('S', 'Society of'), ('G', 'Gastroenterology')], 'Société britannique de gastroentérologie', '<p>Société savante européenne (Royaume-Uni) ; auteur de la recommandation de 2019 sur l’hémorragie digestive basse aiguë.</p>')
a('IPP', [('I', 'Inhibiteur de la'), ('P', 'Pompe à'), ('P', 'Protons')], 'Inhibiteur de la pompe à protons', '<p>Médicament qui bloque de façon irréversible la H⁺/K⁺-ATPase de la cellule pariétale gastrique et réduit fortement la sécrétion acide (oméprazole, ésoméprazole, pantoprazole, lansoprazole, rabéprazole).</p>')
a('TIPS', [('T', 'Transjugular (transjugulaire)'), ('I', 'Intrahepatic (intrahépatique)'), ('P', 'Portosystemic (portosystémique)'), ('S', 'Shunt (dérivation)')], 'Dérivation portosystémique intrahépatique par voie transjugulaire', '<p>Endoprothèse couverte placée par voie jugulaire entre une branche de la veine porte et une veine sus-hépatique ; elle abaisse la pression portale.</p>', 'k92-tips')
a('ORL', [('O', 'Oto-'), ('R', 'Rhino-'), ('L', 'Laryngologie')], 'Oto-rhino-laryngologie', '<p>Spécialité de l’oreille, du nez et de la gorge.</p>')
a('CC', [('C', 'Creative'), ('C', 'Commons')], 'Licences Creative Commons', '<p>Famille de licences libres qui autorisent la réutilisation d’une œuvre à des conditions précisées (attribution, partage dans les mêmes conditions).</p>')
a('BY-SA', [('BY', 'attribution (« by », citer l’auteur)'), ('SA', 'Share Alike (partage dans les mêmes conditions)')], 'Attribution, partage dans les mêmes conditions', '<p>Conditions d’une licence Creative Commons : citer l’auteur et diffuser toute adaptation sous la même licence.</p>')
a('GIF', [('G', 'Graphics'), ('I', 'Interchange'), ('F', 'Format')], 'Format d’échange graphique', '<p>Format d’image à palette limitée, compact, utilisé pour les illustrations des cours.</p>')
a('MEDINA', [('MEDINA', 'nom du projet (atlas de médecine), non une abréviation')], 'Atlas de cours MEDINA', '<p>Nom de l’atlas pédagogique dans lequel ce cours est publié.</p>')
a('IIc', [('II', 'classe II de Forrest'), ('c', 'sous-type c')], 'Forrest IIc : tache pigmentée plane', '<p>Stigmate d’ulcère à faible risque de récidive ; pas d’hémostase endoscopique (ESGE 2021).</p>', 'k92-forrest')
nom('Mallory-Weiss', 'George Kenneth Mallory, Soma Weiss', 'Syndrome de Mallory-Weiss', '<p>Déchirure longitudinale de la muqueuse de la jonction œsogastrique après des efforts de vomissement ; cause d’hématémèse.</p>')
nom('Glasgow-Blatchford', 'ville de Glasgow et Oliver Blatchford', 'Score de Glasgow-Blatchford', '<p>Score de risque de l’hémorragie digestive haute, calculé avant l’endoscopie ; ≤ 1 : très faible risque (ESGE 2021).</p>', )
a('Royaume-Uni', [('Royaume-Uni', 'nom de pays, non une abréviation')], 'Royaume-Uni de Grande-Bretagne et d’Irlande du Nord', '<p>Pays des recommandations BSG et NICE citées.</p>')
code('K92.0', 'Hématémèse', 'K92 — Hémorragies digestives')
code('K92.1', 'Méléna', 'K92 — Hémorragies digestives')
code('K92.2', 'Hémorragie gastro-intestinale, sans précision', 'K92 — Hémorragies digestives')
