"""Abréviations G53 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'g53', '__init__'}:
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

add_if_absent('B02.2', [('B02.2', 'code de la CIM-10-GM 2024, marqué d’une croix (†)')],
              'Code B02.2† de la CIM-10-GM 2024',
              'Ce code désigne, dans la classification CIM-10-GM 2024, la maladie causale associée à G 53.0* : le zona. Le texte du libellé complet n’a pas été relu pour ce cours.', 'g53-codage')
add_if_absent('CXCL13', [('CXCL', 'C-X-C motif chemokine ligand (ligand de chimiokine à motif C-X-C)'), ('13', 'numéro 13')],
              'C-X-C motif chemokine ligand 13',
              'Cette chimiokine du liquide céphalorachidien augmente tôt dans la neuroborréliose, mais elle n’est pas spécifique : elle s’élève aussi dans la neurosyphilis, la méningite tuberculeuse et le lymphome du système nerveux central.', 'g53-lcr-borrelia')
add_if_absent('DGN', [('D', 'Deutsche'), ('G', 'Gesellschaft für'), ('N', 'Neurologie')],
              'Deutsche Gesellschaft für Neurologie (Société allemande de neurologie)',
              'Cette société publie des directives coapprouvées notamment par la Société suisse de neurologie, qui fondent les recommandations sur la neuroborréliose, la neurosyphilis et la méningo-encéphalite virale.', 'g53-borreliose')
add_if_absent('EANO', [('E', 'European'), ('A', 'Association of'), ('NO', 'Neuro-Oncology')],
              'European Association of Neuro-Oncology',
              'Cette association européenne a publié en 2023, avec la société européenne d’oncologie médicale, la recommandation sur les métastases leptoméningées des tumeurs solides.', 'g53-ml')
add_if_absent('EFNS', [('E', 'European'), ('F', 'Federation'), ('N', 'of Neurological'), ('S', 'Societies')],
              'European Federation of Neurological Societies',
              'Cette fédération a publié en 2010 la révision des recommandations de traitement pharmacologique de la douleur neuropathique. Seul le résumé a été lu.', 'g53-efns')
add_if_absent('HC', [('H', 'Health'), ('C', 'Care')],
              'HealthCare (dans le nom commercial Gabapentine Spirig HC)',
              'Dans « Gabapentine Spirig HC », ces lettres désignent la gamme HealthCare du fabricant Spirig. Elles ne définissent pas une dose.', 'g53-gabapentine')
add_if_absent('Herrero-Morant', [('Herrero-Morant', 'nom d’auteur, non une abréviation')],
              'Herrero-Morant, premier auteur de la cohorte espagnole de neurosarcoïdose',
              'La cohorte espagnole de 342 patients atteints de sarcoïdose a été publiée en 2025 ; seul le résumé a été lu.', 'g53-nsarc-ttt')
add_if_absent('ID', [('I', 'Type I'), ('D', 'sous-type D')],
              'Sous-type ID de la classification EANO-ESMO',
              'Le sous-type ID réunit les métastases leptoméningées confirmées par cytologie ou biopsie dont l’imagerie montre une hydrocéphalie seule ou reste normale.', 'g53-ml')
add_if_absent('MRZ', [('M', 'Masern (rougeole)'), ('R', 'Röteln (rubéole)'), ('Z', 'Zoster')],
              'Réaction MRZ (Masern, Röteln, Zoster)',
              'Cette réaction compare la production intrathécale d’anticorps contre trois virus. Une réaction négative, associée à une anomalie du liquide, a distingué la neurosarcoïdose de la sclérose en plaques dans une série zurichoise lue au niveau du résumé.', 'g53-sarcoidose')
add_if_absent('Melkersson-Rosenthal', [('Melkersson-Rosenthal', 'noms propres de deux auteurs, non une abréviation')],
              'Syndrome de Melkersson-Rosenthal',
              'Ce syndrome figure parmi les causes citées de diplégie faciale, avec la sarcoïdose, la neuroborréliose et le syndrome de Guillain-Barré.', 'g53-sarcoidose')
add_if_absent('SNG', [('S', 'Société'), ('N', 'suisse de'), ('G', 'neurologie (Schweizerische Neurologische Gesellschaft)')],
              'Société suisse de neurologie',
              'Cette société a coapprouvé les directives allemandes sur la neurosyphilis, la méningo-encéphalite virale et la neuroborréliose citées dans ce cours.', 'g53-neurosyphilis')
add_if_absent('anti-MOG', [('anti', 'dirigé contre'), ('MOG', 'Myelin Oligodendrocyte Glycoprotein (glycoprotéine de la myéline des oligodendrocytes)')],
              'Anticorps anti-glycoprotéine de la myéline des oligodendrocytes',
              'La maladie associée à ces anticorps figure parmi les imitateurs de la neurosarcoïdose cités par la revue de 2025.', 'g53-sarcoidose')
