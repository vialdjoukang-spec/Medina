from cardio_1 import a, G
# J95 — Complications respiratoires des actes médicaux et autres troubles respiratoires (P-02-Pneumologie).
# Toutes les clés sont ajoutées seulement si elles manquent (_a), pour ne jamais écraser une entrée existante.
# SRLF figure aussi dans le dossier de travail R06 (rédaction parallèle) : définition neutre ici.
# Les quatre noms propres (Abu-Omar, Dajer-Fadel, Fuchs-Buder, McGrath) portent deux majuscules ou une
# majuscule interne : sans clé, build_medina.audit() les signalerait. Ils ne recouvrent aucun autre mot.
# Relecture IA du 09.10.2026 ; ne vaut pas validation médicale.

def _a(k, *args):
    if k not in G:
        a(k, *args)

_a('ESAIC', [('E', 'European (européenne)'), ('S', 'Society of (société d’)'), ('A', 'Anaesthesiology (anesthésiologie)'), ('I', 'and Intensive (et de soins intensifs)'), ('C', 'Care')], 'Société européenne d’anesthésiologie et de soins intensifs',
  '<p>Nom actuel de la Société européenne d’anesthésiologie. Elle a publié en 2023 sa première recommandation sur la gestion périopératoire du bloc neuromusculaire, et en 2020, avec l’ESICM, une recommandation sur le support respiratoire non invasif de l’opéré hypoxémique.</p>', 'j95-curarisation')
_a('EPCO', [('E', 'European (européennes)'), ('P', 'Perioperative (périopératoires)'), ('C', 'Clinical (cliniques)'), ('O', 'Outcome (définitions des complications)')], 'Définitions européennes des complications cliniques périopératoires',
  '<p>Définitions standardisées de 22 événements indésirables périopératoires, avec une gradation de gravité, publiées en 2015 par un groupe de travail de la Société européenne d’anesthésiologie et de l’ESICM (Jammer et al.).</p>', 'j95-epco')
_a('ARISCAT', [('A', 'Assess (évaluer)'), ('R', 'Respiratory (respiratoire)'), ('IS', 'rIsk in Surgical patients (le risque chez les patients chirurgicaux)'), ('CAT', 'in CATalonia (en Catalogne)')], 'Score catalan d’évaluation du risque respiratoire chirurgical',
  '<p>Score de risque de complications pulmonaires postopératoires construit sur 2464 opérés de 59 hôpitaux de Catalogne (Canet, 2010) : sept facteurs, trois classes de risque (moins de 26, 26 à 44, 45 points ou plus).</p>', 'j95-ariscat')
_a('SFAR', [('S', 'Société'), ('F', 'Française'), ('A', 'd’Anesthésie'), ('R', 'et de Réanimation')], 'Société française d’anesthésie et de réanimation',
  '<p>Société savante française. Avec la SRLF, elle a publié des recommandations d’experts sur la trachéotomie en réanimation (2018) et sur l’intubation et l’extubation du patient de réanimation (2019).</p>', 'j95-tracheotomie')
_a('SRLF', [('S', 'Société de'), ('R', 'Réanimation de'), ('L', 'Langue'), ('F', 'Française')], 'Société de réanimation de langue française',
  '<p>Société savante francophone de médecine intensive et de réanimation. Avec la SFAR, elle a publié des recommandations d’experts sur la trachéotomie en réanimation (2018) et sur l’intubation et l’extubation du patient de réanimation (2019).</p>', 'j95-oedeme-larynge')
_a('EBMT', [('E', 'European society for (Société européenne de)'), ('B', 'Blood and (greffe de sang et de)'), ('M', 'Marrow (moelle)'), ('T', 'Transplantation')], 'Société européenne de greffe de sang et de moelle',
  '<p>Société savante européenne de la greffe de cellules souches hématopoïétiques. Coautrice avec l’ERS de la recommandation de 2024 sur le traitement de l’atteinte pulmonaire de la maladie chronique du greffon contre l’hôte.</p>', 'j95-gvh')
# Noms propres d’auteurs composés ou à capitale interne, signalés par l’audit (convention de glossary/j18.py).
_a('Abu-Omar', [('Abu-Omar', 'nom propre : Yasir Abu-Omar, chirurgien cardiothoracique, non une abréviation')], 'Yasir Abu-Omar, premier auteur du consensus EACTS 2017 sur la médiastinite',
  '<p>Premier auteur de la déclaration de consensus d’experts de l’EACTS sur la prévention et la prise en charge de la médiastinite (Eur J Cardiothorac Surg, 2017).</p>')
_a('Dajer-Fadel', [('Dajer-Fadel', 'nom propre : Wadih Lorenzo Dajer-Fadel, chirurgien cardiothoracique à Mexico, non une abréviation')], 'Wadih Lorenzo Dajer-Fadel, premier auteur d’une revue systématique du pneumomédiastin spontané',
  '<p>Premier auteur d’une revue systématique de 600 cas de pneumomédiastin spontané publiés entre 1990 et 2012 (Asian Cardiovasc Thorac Ann, 2014).</p>')
_a('Fuchs-Buder', [('Fuchs-Buder', 'nom propre : Thomas Fuchs-Buder, anesthésiste, non une abréviation')], 'Thomas Fuchs-Buder, premier auteur de la recommandation ESAIC 2023 sur le bloc neuromusculaire',
  '<p>Premier auteur de la première recommandation de l’ESAIC sur la gestion périopératoire du bloc neuromusculaire (Eur J Anaesthesiol, 2023).</p>')
_a('McGrath', [('McGrath', 'nom propre : Brendan A. McGrath, anesthésiste-réanimateur britannique, non une abréviation')], 'Brendan A. McGrath, premier auteur des recommandations britanniques sur les urgences de trachéotomie',
  '<p>Premier auteur des recommandations multidisciplinaires de 2012 du National Tracheostomy Safety Project sur les urgences des patients trachéotomisés et laryngectomisés (Anaesthesia), projet qu’il préside.</p>')
