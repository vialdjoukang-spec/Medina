"""Abréviations G02 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'g02', '__init__'}:
        continue
    _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
G = {}
def add_if_absent(key, letters, full, definition, window=None):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full,
                  'def': '<p>' + definition + '</p>', 'ref': window}
def code(key, titre):
    add_if_absent(key, [(key, 'code CIM-10-GM 2024')], titre,
                  'Sous-catégorie traitée dans le cours G02 (catalogue OFS, version française 2024). Le signe † désigne la maladie causale, le signe * sa manifestation méningée.', 'g02-codage')

code('G02.0', 'Méningite au cours d’infections virales classées ailleurs')
code('G02.1', 'Méningite au cours de mycoses classées ailleurs')
code('G02.8', 'Méningite au cours d’autres maladies infectieuses et parasitaires précisées classées ailleurs')
code('G03.0', 'Méningite non purulente (abactérienne)')
code('G05.1', 'Encéphalite, myélite et encéphalomyélite au cours de maladies virales classées ailleurs')
code('G05.2', 'Encéphalite, myélite et encéphalomyélite au cours d’autres maladies infectieuses et parasitaires classées ailleurs')
code('A87.0', 'Entérovirus, maladie causale (code †) d’une méningite G02*')
code('A87.1', 'Adénovirus, maladie causale (code †) d’une méningite G02*')
code('B00.3', 'Herpès simplex, maladie causale (code †) d’une méningite G02*')
code('B05.1', 'Rougeole, maladie causale (code †) d’une méningite G02*')
code('B26.1', 'Oreillons, maladie causale (code †) d’une méningite G02*')
code('B06.0', 'Rubéole, maladie causale (code †) d’une méningite G02*')
code('B01.0', 'Varicelle, maladie causale (code †) d’une méningite G02*')
code('B02.1', 'Zona, maladie causale (code †) d’une méningite G02*')
code('B37.5', 'Candidose, maladie causale (code †) d’une méningite G02*')
code('B38.4', 'Coccidioïdomycose, maladie causale (code †) d’une méningite G02*')
code('B45.1', 'Cryptococcose, maladie causale (code †) d’une méningite G02*')
code('B57.4', 'Maladie de Chagas chronique, maladie causale (code †) d’une méningite G02*')
add_if_absent('DGN', [('D', 'Deutsche (allemande)'), ('G', 'Gesellschaft (société)'), ('N', 'für Neurologie (de neurologie)')], 'Société allemande de neurologie', 'Société savante qui a publié en février 2025 la directive S1 sur la méningo-encéphalite virale, principale source clinique du cours.', 'g02-sources-guides')
add_if_absent('CIM', [('C', 'Classification'), ('I', 'Internationale des'), ('M', 'Maladies')], 'Classification internationale des maladies', 'Classification dont le catalogue du cours suit la version CIM-10-GM 2024 de l’Office fédéral de la statistique.', 'g02-codage')
add_if_absent('FSME', [('F', 'Früh (précoce)'), ('S', 'Sommer (été)'), ('M', 'Meningo (méningo-)'), ('E', 'Enzephalitis (encéphalite)')], 'Méningo-encéphalite verno-estivale (transmise par les tiques)', 'Encéphalite à tiques classée A84, voisine de G02 ; 245 cas en Suisse en 2023 selon la directive S1.', 'g02-fsme')
add_if_absent('LCMV', [('L', 'Lymphocytic (lymphocytaire)'), ('C', 'ChorioMeningitis (chorioméningite)'), ('V', 'Virus')], 'Virus de la chorioméningite lymphocytaire', 'Virus cité parmi les causes de méningite virale après les entérovirus, les arbovirus, les herpèsvirus et le VIH.', None)
add_if_absent('SNC', [('S', 'Système'), ('N', 'Nerveux'), ('C', 'Central')], 'Système nerveux central', 'Ensemble formé par l’encéphale et la moelle épinière.', None)
add_if_absent('JCV', [('J', 'John'), ('C', 'Cunningham'), ('V', 'Virus')], 'Virus JC', 'Virus cité par la directive S1 parmi les agents à rechercher par PCR du liquide, notamment chez l’immunodéprimé.', 'g02-pcr-lcr')
add_if_absent('anti-NMDAR', [('anti', 'dirigé contre le'), ('N', 'N-'), ('M', 'Méthyl-'), ('D', 'D-'), ('A', 'Aspartate'), ('R', 'Receptor (récepteur)')], 'Anticorps dirigés contre le récepteur N-méthyl-D-aspartate', 'Encéphalite auto-immune qui peut suivre une encéphalite herpétique.', 'g02-autoimmune')
add_if_absent('CASPR2', [('C', 'Contactin-'), ('ASP', 'Associated Protein-like (protéine apparentée associée à la contactine)'), ('R', 'Receptor-like'), ('2', 'numéro 2')], 'Protéine 2 apparentée à la protéine associée à la contactine', 'Cible d’anticorps dans une encéphalite auto-immune citée par la directive S1.', 'g02-autoimmune')
add_if_absent('LGI1', [('L', 'Leucine-rich (riche en leucine)'), ('G', 'Glioma (gliome)'), ('I', 'Inactivated (inactivé)'), ('1', 'numéro 1')], 'Protéine 1 inactivée du gliome, riche en leucine', 'Cible d’anticorps dans une encéphalite auto-immune citée par la directive S1.', 'g02-autoimmune')
add_if_absent('ROR', [('R', 'Rougeole'), ('O', 'Oreillons'), ('R', 'Rubéole')], 'Vaccin contre la rougeole, les oreillons et la rubéole', 'En Suisse, il est donné à 9 et 12 mois.', 'g02-vaccination')
add_if_absent('RORV', [('R', 'Rougeole'), ('O', 'Oreillons'), ('R', 'Rubéole'), ('V', 'Varicelle')], 'Vaccin contre la rougeole, les oreillons, la rubéole et la varicelle', 'Préféré au ROR en Suisse depuis 2023.', 'g02-vaccination')
add_if_absent('NECT', [('N', 'Nifurtimox-'), ('E', 'Eflornithine'), ('C', 'Combination'), ('T', 'Therapy (traitement combiné)')], 'Traitement combiné nifurtimox-éflornithine', 'Schéma de la trypanosomiase africaine nommé par l’Organisation mondiale de la santé ; son contenu n’a pas été lu pour ce cours.', 'g02-tha')
add_if_absent('GeneXpert', [('GeneXpert', 'nom commercial d’un automate de PCR, non une abréviation')], 'Automate de PCR GeneXpert', 'Automate utilisé au CHUV pour la PCR rapide des entérovirus du liquide.', 'g02-pcr-rapide-ev')
add_if_absent('CCF', [('C', 'Conscience altérée'), ('C', 'Crise'), ('F', 'signe Focal')], 'Aide pédagogique CCF', 'Conscience altérée, Crise, signe Focal : trois signes qui imposent l’aciclovir immédiat. Aide pédagogique, non critère officiel.', 'g02-mnemo')
add_if_absent('EFNS', [('E', 'European'), ('F', 'Federation of'), ('N', 'Neurological'), ('S', 'Societies')], 'Fédération européenne des sociétés de neurologie', 'Elle a publié en 2010 une recommandation sur la méningo-encéphalite virale, non lue pour ce cours.', 'g02-lacunes')
add_if_absent('EAN', [('E', 'European'), ('A', 'Academy of'), ('N', 'Neurology')], 'Académie européenne de neurologie', 'Elle a publié en 2017 une recommandation sur la FSME, non lue pour ce cours.', 'g02-lacunes')
add_if_absent('Valaciclovir-Mepha', [('Valaciclovir-Mepha', 'nom commercial suisse, non une abréviation')], 'Valaciclovir-Mepha®', 'Préparation citée par l’information professionnelle suisse.', 'g02-d-valaciclovir')
