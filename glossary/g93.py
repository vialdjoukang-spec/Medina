"""Abréviations G93 (cycle Betta 40) ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib, sys
_existing = {}
def _root():
    for p in [Path(__file__).resolve().parent] + list(Path(__file__).resolve().parents):
        if (p / 'glossary' / 'cardio_1.py').exists():
            return p / 'glossary'
    return None
_g = _root()
if _g is not None:
    sys.path.insert(0, str(_g))
    for _path in sorted(_g.glob('*.py')):
        if _path.stem in {'g93', '__init__'}:
            continue
        try:
            _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
        except Exception:
            pass
G = {}
def a(key, letters, full, definition, window=None):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full, 'def': '<p>' + definition + '</p>', 'ref': window}

a('HII', [('H','Hypertension'),('I','Intracrânienne'),('I','Idiopathique')], 'Hypertension intracrânienne idiopathique',
  'Élévation de la pression intracrânienne sans cause identifiable, codée G93.2. Elle touche surtout des femmes obèses en âge de procréer et menace la vision par l’œdème papillaire.', 'g93-friedman')
a('G93', [('G93','code CIM-10-GM du bloc « Autres affections du cerveau »')], 'Code CIM-10-GM G93, autres affections du cerveau',
  'Catégorie de rattachement utilisée lorsqu’aucun code étiologique plus précis n’existe pour une affection du cerveau.', 'g93-cim')
for _k, _t in [('G93.0','kystes cérébraux'),('G93.1','lésion cérébrale anoxique non classée ailleurs'),('G93.2','hypertension intracrânienne bénigne (idiopathique)'),
               ('G93.3','syndrome de fatigue chronique, encéphalomyélite myalgique'),('G93.4','encéphalopathie sans précision'),('G93.5','compression du cerveau, avec hernie'),
               ('G93.6','œdème cérébral'),('G93.7','syndrome de Reye'),('G93.8','autres affections précisées du cerveau'),('G93.80','syndrome apallique'),
               ('G93.88','autres affections précisées, dont l’encéphalopathie post-radique'),('G93.9','affection du cerveau sans précision')]:
    a(_k, [('G93','code CIM-10-GM des autres affections du cerveau'), (_k[3:], _t)], 'Code CIM-10-GM ' + _k + ', ' + _t, 'Sous-catégorie de G93 : ' + _t + '.', 'g93-cim')
for _k, _t in [('Q04.6','kystes cérébraux congénitaux'),('P91.1','kystes périventriculaires acquis du nouveau-né'),('O08.8','autres complications consécutives à un avortement, une grossesse extra-utérine ou molaire'),
               ('O29.2','complications cérébrales de l’anesthésie pendant la grossesse'),('O74.3','autres complications cérébrales de l’anesthésie pendant le travail'),
               ('O89.2','complications cérébrales de l’anesthésie pendant le post-partum'),('P21.9','asphyxie néonatale sans précision'),
               ('S06.28','compression traumatique diffuse du cerveau (autres lésions traumatiques cérébrales diffuses)'),('S06.38','autres lésions traumatiques cérébrales circonscrites'),
               ('P11.0','œdème cérébral dû à un traumatisme obstétrical'),('S06.1','œdème cérébral traumatique'),('G31.2','dégénérescence du système nerveux due à l’alcool')]:
    a(_k, [(_k[:3], 'catégorie CIM-10-GM'), (_k[3:], _t)], 'Code CIM-10-GM ' + _k + ', ' + _t, 'Code cité comme exclusion de G93 : ' + _t + '.', 'g93-cim')
a('EUROMENE', [('EUROMENE','nom propre du réseau européen sur l’encéphalomyélite myalgique, non développé lettre à lettre dans ce cours')], 'EUROMENE, consensus européen 2021',
  'Consensus d’experts européens (2021) sur le diagnostic et la prise en charge de l’encéphalomyélite myalgique et du syndrome de fatigue chronique.', 'g93-emsfc')
a('Monro-Kellie', [('Monro','nom d’Alexander Monro'),('Kellie','nom de George Kellie')], 'Doctrine de Monro-Kellie',
  'La pression intracrânienne dépend de la somme des volumes de sang, de tissu cérébral et de liquide cérébrospinal dans une boîte crânienne rigide.', 'g93-monro')
a('IIHTT', [('I','Idiopathic'),('I','Intracranial'),('H','Hypertension'),('T','Treatment'),('T','Trial')], 'Idiopathic Intracranial Hypertension Treatment Trial',
  'Essai randomisé de l’acétazolamide dans l’hypertension intracrânienne idiopathique avec perte visuelle légère ; il a montré un bénéfice sur le champ visuel.', 'g93-acetazolamide')
a('HIT-6', [('H','Headache'),('I','Impact'),('T','Test'),('6','six questions')], 'Headache Impact Test à six questions',
  'Score de retentissement de la céphalée ; l’acétazolamide n’a pas d’effet sur ce score selon la recommandation européenne.', 'g93-acetazolamide')
a('FOUR', [('F','Full'),('O','Outline'),('U','of UnResponsiveness'),('R','score')], 'Full Outline of UnResponsiveness, score FOUR',
  'Échelle d’évaluation de la conscience préférée au score de Glasgow en phase aiguë selon l’Académie européenne de neurologie.', 'g93-conscience')
a('SUR1', [('SUR','Sulfonylurea Receptor'),('1','type 1')], 'Récepteur des sulfonylurées de type 1',
  'Sous-unité du canal SUR1-TRPM4 qui s’ouvre lorsque l’énergie cellulaire manque ; le glibenclamide l’inhibe.', 'g93-oedeme')
a('NKCC1', [('Na','sodium'),('K','potassium'),('Cl','chlorure'),('C','Cotransporteur'),('1','type 1')], 'Cotransporteur sodium-potassium-chlorure de type 1',
  'Transporteur activé par le potassium extracellulaire et surexprimé dès 1 heure après un traumatisme ; il fait entrer sodium, potassium et eau dans les cellules.', 'g93-oedeme')
a('SIGN', [('S','Scottish'),('I','Intercollegiate'),('G','Guidelines'),('N','Network')], 'Scottish Intercollegiate Guidelines Network',
  'Réseau écossais de recommandations dont la méthode de gradation est utilisée par la recommandation britannique 2023 sur la gestion du poids.', 'g93-poids')
