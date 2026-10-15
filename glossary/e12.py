"""Abréviations E12 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'e12', '__init__'}:
        continue
    try:
        _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
    except Exception:
        pass
G = {}
def add_if_absent(key, letters, full, definition, window):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full,
                  'def': '<p>' + definition + '</p>', 'ref': window}

add_if_absent('FCPD', [('F', 'Fibro'), ('C', 'Calculous (calculeux)'), ('P', 'Pancreatic (pancréatique)'), ('D', 'Diabetes (diabète)')],
              'Pancréatopathie fibrocalculeuse (diabète pancréatique fibrocalculeux)',
              'Cette forme de diabète survient après une pancréatite chronique tropicale chez des adolescents ou de jeunes adultes maigres, surtout en Inde du Sud. Elle se reconnaît à des calculs intracanalaires pancréatiques.', 'e12-fcpd')
add_if_absent('IDF', [('I', 'International'), ('D', 'Diabetes (du diabète)'), ('F', 'Federation (fédération)')],
              'Fédération internationale du diabète',
              'Cette fédération a reconnu le terme de diabète de type 5 en avril 2025 et a créé un groupe de travail chargé d’en établir les critères diagnostiques.', 'e12-type5')
add_if_absent('HaPanEU', [('Ha', 'Harmonizing (harmonisation du diagnostic et du traitement)'), ('Pan', 'chronic Pancreatitis (de la pancréatite chronique)'), ('EU', 'across Europe (en Europe)')],
              'Harmonisation du diagnostic et du traitement de la pancréatite chronique en Europe (recommandations HaPanEU, 2017)',
              'Ces recommandations de la United European Gastroenterology portent sur le diagnostic et le traitement de la pancréatite chronique. Elles fournissent les seuils de diabète et les positions sur les médicaments dans le diabète pancréatoprive.', 'e12-type3c')
add_if_absent('SIDD', [('S', 'Severe (sévère)'), ('I', 'Insulin- (insulino-)'), ('D', 'Deficient (déficient)'), ('D', 'Diabetes (diabète)')],
              'Diabète sévère insulinodéficient',
              'Ce sous-groupe d’une cohorte suédoise partage le défaut sécrétoire du diabète de malnutrition, mais avec un IMC bien plus élevé, d’environ 28,9 kg/m².', 'e12-type5')
add_if_absent('PDX-1', [('P', 'Pancreatic (pancréatique)'), ('D', 'and Duodenal (et duodénal)'), ('X', 'homeobox (gène à homéoboîte)'), ('1', 'numéro 1')],
              'Facteur de transcription pancréatique et duodénal à homéoboîte 1',
              'Ce facteur de transcription régule l’expression du gène de l’insuline. Le consensus 2025 propose que sa dysfonction, sous stress oxydatif, contribue au défaut de sécrétion.', 'e12-pdx')
add_if_absent('MafA', [('Maf', 'v-maf (oncogène de fibrosarcome musculo-aponévrotique)'), ('A', 'homologue A')],
              'Facteur de transcription MafA',
              'Ce facteur de transcription participe, avec PDX-1, à l’expression du gène de l’insuline. Son altération est une hypothèse du consensus 2025, non démontrée.', 'e12-pdx')
add_if_absent('SPINK1', [('S', 'Serine (sérine)'), ('P', 'Protease (protéase)'), ('IN', 'INhibitor (inhibiteur)'), ('K', 'Kazal'), ('1', 'type 1')],
              'Inhibiteur de sérine protéase de type Kazal 1',
              'Des variants de ce gène, dont N34S chez environ 33 % des patients en Inde, sont associés à la pancréatite chronique tropicale.', 'e12-spink1')
add_if_absent('PRSS1', [('PR', 'PRotease (protéase)'), ('SS', 'Serine, Serine (à sérine)'), ('1', 'numéro 1')],
              'Gène de la protéase à sérine 1 (trypsinogène cationique)',
              'Des variants de ce gène figurent parmi ceux décrits dans la pancréatite chronique tropicale, selon un modèle à deux coups.', 'e12-spink1')
add_if_absent('PRSS2', [('PR', 'PRotease (protéase)'), ('SS', 'Serine, Serine (à sérine)'), ('2', 'numéro 2')],
              'Gène de la protéase à sérine 2',
              'Des variants de ce gène figurent parmi ceux décrits dans la pancréatite chronique tropicale.', 'e12-spink1')
add_if_absent('N34S', [('N', 'Asparagine'), ('34', 'en position 34'), ('S', 'remplacée par Sérine')],
              'Variant N34S de SPINK1',
              'Ce variant est présent chez environ 33 % des patients indiens atteints de pancréatite chronique tropicale.', 'e12-spink1')
add_if_absent('anti-GAD65', [('anti', 'anticorps dirigés contre'), ('GAD', 'Glutamic Acid Decarboxylase (décarboxylase de l’acide glutamique)'), ('65', 'isoforme de 65 kDa')],
              'Anticorps anti-décarboxylase de l’acide glutamique 65',
              'Leur négativité est une caractéristique fréquente du diabète de malnutrition ; leur positivité oriente vers le diabète de type 1.', 'e12-cpept')
add_if_absent('CA 19-9', [('CA', 'Carbohydrate Antigen (antigène glucidique)'), ('19-9', 'numéro 19-9')],
              'Antigène glucidique 19-9',
              'Ce marqueur sérique est utilisé pour la vigilance oncologique dans la pancréatopathie fibrocalculeuse.', 'e12-cancer')
add_if_absent('DFGe', [('D', 'Débit'), ('F', 'de Filtration'), ('G', 'Glomérulaire'), ('e', 'estimé')],
              'Débit de filtration glomérulaire estimé',
              'Ce paramètre estime la filtration rénale. Dans cette leçon, il règle la posologie : la metformine est contre-indiquée en dessous de 30 mL/min et limitée à 1 000 mg par jour entre 30 et 59 mL/min.', 'e12-metformine')
add_if_absent('CT', [('C', 'Computed (assistée par ordinateur)'), ('T', 'Tomography (tomographie)')],
              'Tomodensitométrie',
              'Cet examen d’imagerie est préféré pour confirmer un pancréas normal dans le diabète de malnutrition.', 'e12-imagerie')
add_if_absent('DEXA', [('D', 'Dual-'), ('E', 'Energy (à double énergie)'), ('X', 'X-ray (de rayons X)'), ('A', 'Absorptiometry (absorptiométrie)')],
              'Absorptiométrie à rayons X à double énergie',
              'Cette mesure de la composition corporelle quantifie la masse maigre et la masse grasse.', 'e12-imc')
add_if_absent('SANS', [('S', 'Sécrétion basse mais mesurable'), ('A', 'Anticorps négatifs'), ('N', 'Non-cétosique'), ('S', 'Sensibilité conservée')],
              'Moyen mnémotechnique du profil du diabète de malnutrition',
              'Aide pédagogique, non critère officiel : il résume le profil proposé par le consensus 2025.', 'e12-mnemo')
add_if_absent('Hugh-Jones', [('Hugh-Jones', 'nom d’un auteur, non une abréviation')],
              'Hugh-Jones, auteur de la description de 1955',
              'Il a décrit en Jamaïque, en 1955, le diabète « de type J » des sujets jeunes et maigres.', 'e12-histoire')
add_if_absent('E12.74', [('E12.74', 'code de la CIM-10-GM 2024 : diabète sucré de malnutrition avec complications multiples, avec syndrome du pied diabétique, non désigné comme décompensé')],
              'Diabète sucré de malnutrition avec syndrome du pied diabétique, non désigné comme décompensé (CIM-10-GM 2024)',
              'Ce sous-code range le syndrome du pied diabétique parmi les complications multiples du diabète de malnutrition.', 'e12-type5')
add_if_absent('E12.75', [('E12.75', 'code de la CIM-10-GM 2024 : diabète sucré de malnutrition avec complications multiples, avec syndrome du pied diabétique, désigné comme décompensé')],
              'Diabète sucré de malnutrition avec syndrome du pied diabétique, désigné comme décompensé (CIM-10-GM 2024)',
              'Ce sous-code correspond au même tableau que E12.74 lorsque le diabète est désigné comme décompensé.', 'e12-type5')
add_if_absent('O24.2', [('O24.2', 'code de la CIM-10 (OMS 2019) : diabète sucré de malnutrition préexistant, pendant la grossesse')],
              'Diabète sucré de malnutrition préexistant au cours de la grossesse (CIM-10 OMS 2019)',
              'Ce code obstétrical remplace E12 chez la femme enceinte dont le diabète de malnutrition précède la grossesse ; le libellé CIM-10-GM n’a pas été vérifié.', 'e12-type5')
add_if_absent('O24.4', [('O24.4', 'code de la CIM-10 (OMS 2019) : diabète sucré survenant au cours de la grossesse')],
              'Diabète sucré survenant au cours de la grossesse (CIM-10 OMS 2019)',
              'Ce code obstétrical désigne le diabète apparu pendant la grossesse ; il ne relève pas de E12.', 'e12-type5')
add_if_absent('U100', [('U', 'Unités d’insuline'), ('100', 'par millilitre (100 U/mL)')],
              'Concentration de 100 unités d’insuline par millilitre',
              'La glargine U100 (Lantus®) est classée à risque moyen d’hypoglycémie au volant par les directives SGED/SGRM 2025.', 'e12-glargine')
add_if_absent('U300', [('U', 'Unités d’insuline'), ('300', 'par millilitre (300 U/mL)')],
              'Concentration de 300 unités d’insuline par millilitre',
              'La glargine U300 est une basale ultralente, classée à risque faible d’hypoglycémie au volant par les directives SGED/SGRM 2025.', 'e12-glargine')
