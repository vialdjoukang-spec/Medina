"""Abréviations G21 (cycle Betta 35) ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'g21', '__init__'}:
        continue
    try:
        _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
    except Exception:
        pass
G = {}
def add_if_absent(key, letters, full, definition, window=None):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full, 'def': '<p>' + definition + '</p>', 'ref': window}
add_if_absent('MDS', [('M','Movement (des mouvements)'),('D','Disorder (troubles)'),('S','Society (société)')],
              'Movement Disorder Society',
              'Cette société internationale a publié en 2015 les critères cliniques de diagnostic de la maladie de Parkinson ; le parkinsonisme moteur y associe une bradykinésie à un tremblement de repos ou à une rigidité.', 'g21-mds')
add_if_absent('DaTSCAN', [('DaT','Dopamine Transporter (transporteur de la dopamine)'),('SCAN','scintigraphie, de l’anglais scan')],
              'Scintigraphie du transporteur de la dopamine (ioflupane marqué à l’iode 123)',
              'Cet examen d’imagerie nucléaire visualise la perte de terminaisons dopaminergiques striatales. Il est normal dans le parkinsonisme médicamenteux et anormal dans la perte présynaptique.', 'g21-datscan')
add_if_absent('ElViS', [('El','Electronic (électronique)'),('Vi','Vigilance'),('S','System (système)')],
              'Système électronique d’annonce des effets indésirables de Swissmedic',
              'Les professionnels de santé suisses y déclarent les effets indésirables des médicaments. Le développement littéral est reconstitué à titre pédagogique ; le nom officiel est ElViS.', 'g21-elvis')
add_if_absent('STRIVE', [('STRIVE','STandards for ReportIng Vascular changes on nEuroimaging (normes de description des lésions vasculaires en neuro-imagerie)')],
              'Normes de description des lésions vasculaires en neuro-imagerie',
              'Ces critères internationaux d’imagerie décrivent les lésions des petits vaisseaux cérébraux ; la recommandation de Rektor 2018 les utilise pour l’IRM du parkinsonisme vasculaire.', 'g21-vasc')
add_if_absent('CIM', [('C','Classification'),('I','Internationale des'),('M','Maladies')],
              'Classification internationale des maladies',
              'Cette classification attribue un code à chaque diagnostic. Le cours utilise la version CIM-10-GM 2024.', None)
add_if_absent('G21.4', [('G21','syndrome parkinsonien secondaire (CIM-10-GM)'),('.4','maladie de Parkinson vasculaire, ou syndrome parkinsonien vasculaire')],
              'Code CIM-10-GM 2024 : syndrome parkinsonien vasculaire',
              'Le libellé français parle de « maladie de Parkinson vasculaire », le libellé allemand de syndrome ; il ne s’agit pas d’une maladie de Parkinson.', 'g21-vasc')
add_if_absent('G25.1', [('G25','autres troubles extrapyramidaux et mouvements anormaux'),('.1','tremblement médicamenteux')],
              'Code CIM-10-GM 2024 : tremblement médicamenteux',
              'Ce code voisin de G21 s’applique au tremblement dû à un médicament.', None)
add_if_absent('Schönfeldt-Lecuona', [('Schönfeldt-Lecuona','nom de famille composé d’un auteur, non une abréviation')],
              'Schönfeldt-Lecuona, auteur de séries sur le syndrome malin',
              'Ce psychiatre est coauteur des analyses de 2020 sur le traitement du syndrome malin des neuroleptiques (série d’Ulm et comparaison de recommandations).', 'g21-delphi')
