"""Abréviations G03 — Méningite due à des causes autres et non précisées ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'g03', '__init__'}:
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

add_if_absent('DGN', [('D', 'Deutsche'), ('G', 'Gesellschaft'), ('N', 'für Neurologie')],
              'Deutsche Gesellschaft für Neurologie (Société allemande de neurologie)',
              'Cette société savante allemande publie, avec l’AWMF, les recommandations 030/100 (méningo-encéphalite virale, 2025) et 030/089 (méningo-encéphalite bactérienne de l’adulte, 2023) utilisées en complément des sources suisses et de l’OMS dans cette leçon. Ce sont des recommandations allemandes.', 'g03-r6')
add_if_absent('HSV', [('H', 'Herpes'), ('S', 'Simplex'), ('V', 'Virus')],
              'Virus de l’herpès simplex',
              'Deux types existent : HSV-1 et HSV-2. HSV-2 est l’agent le plus étroitement lié à la méningite récurrente de Mollaret ; l’encéphalite herpétique est l’indication de l’aciclovir par voie intraveineuse.', 'g03-mollaret')
add_if_absent('JC', [('JC', 'nom d’usage du virus JC, non développé lettre à lettre dans les sources lues')],
              'Virus JC',
              'La recommandation allemande de 2025 le liste parmi les cibles de la PCR sur liquide céphalo-rachidien non centrifugé, avec les herpèsvirus, les flavivirus et les entérovirus.', 'g03-r7')
add_if_absent('NMDAR', [('N', 'N-méthyl-'), ('M', ''), ('D', 'D-'), ('A', 'aspartate'), ('R', 'Récepteur')],
              'Récepteur du N-méthyl-D-aspartate',
              'Des anticorps dirigés contre ce récepteur caractérisent une forme d’encéphalite auto-immune, à rechercher selon la recommandation virale lorsqu’aucun agent n’est identifié.', 'g03-r6')
add_if_absent('CASPR2', [('CASPR2', 'Contactin-Associated Protein-like 2 : nom d’usage, non développé lettre à lettre')],
              'Contactin-associated protein-like 2',
              'Des anticorps dirigés contre cette protéine caractérisent une forme d’encéphalite auto-immune, à rechercher lorsqu’aucun agent n’est identifié.', 'g03-r6')
add_if_absent('LGI1', [('LGI1', 'Leucine-rich Glioma-Inactivated 1 : nom d’usage, non développé lettre à lettre')],
              'Leucine-rich glioma-inactivated 1',
              'Des anticorps dirigés contre cette protéine caractérisent une forme d’encéphalite auto-immune, à rechercher lorsqu’aucun agent n’est identifié.', 'g03-r6')
for _k, _t, _w in [
    ('G03.0', 'Méningite non purulente (inclut la méningite abactérienne)', 'g03-r13'),
    ('G03.1', 'Méningite chronique', 'g03-r13'),
    ('G03.2', 'Méningite récurrente bénigne [Mollaret]', 'g03-r13'),
    ('G03.8', 'Méningite due à d’autres causes précisées', 'g03-r13'),
    ('G03.9', 'Méningite, sans précision (inclut l’arachnoïdite spinale sans précision)', 'g03-r13'),
    ('B00.4', 'Encéphalite herpétique', 'g03-r6'),
]:
    add_if_absent(_k, [(_k, 'code de la CIM-10-GM 2024, non une abréviation')], _t,
                  'Code de la CIM-10-GM 2024 : ' + _t + '.', _w)
for _k, _t, _w in [
    ('Yelehe-Okouma', 'Yelehe-Okouma et collaborateurs, revue sur la méningite aseptique médicamenteuse, Fundam Clin Pharmacol 2018', 'g03-medic'),
    ('Martínez-Girón', 'Martínez-Girón et Pantanowitz, cytologie du liquide céphalo-rachidien dans les atteintes méningées aseptiques non malignes, Diagn Cytopathol 2017', 'g03-cellules'),
    ('Ibuprofen-Mepha', 'Ibuprofen-Mepha Teva, comprimés pelliculés : information professionnelle suisse, mise à jour de décembre 2024', 'g03-ibuprofene'),
    ('Valaciclovir-Mepha', 'Valaciclovir-Mepha 500/1000 Lactab® : information professionnelle suisse, mise à jour de décembre 2025', 'g03-suppression'),
]:
    add_if_absent(_k, [(_k, 'nom propre d’un auteur ou d’un produit, non une abréviation')], _t,
                  'Référence citée dans ce cours : ' + _t + '.', _w)

# Ajouts locaux après relecture Sol ; clés héritées conservées pour les autres cours.
add_if_absent('PL', [('PL', 'Ponction lombaire')], 'Ponction lombaire', 'Prélèvement de liquide céphalorachidien après évaluation de son indication et de sa sécurité.', 'g03-lcr')
add_if_absent('N-05-Neurologie', [('N-05-Neurologie', 'Neurologie')], 'Neurologie', 'Libellé du fragment neurologique ; ce n’est pas un diagnostic.', 'g03-r6')
add_if_absent('A4', [('A4', 'Section A.4 de l’OMS 2025')], 'Section A.4 de l’OMS 2025', 'Section consacrée à l’imagerie avant la ponction lombaire.', 'g03-r4')
add_if_absent('DAFALGAN', [('DAFALGAN', 'DAFALGAN comprimés 500 mg')], 'DAFALGAN comprimés 500 mg', 'Nom commercial du paracétamol de la présentation suisse vérifiée.', 'g03-paracetamol')
add_if_absent('CEN', [('CEN', 'Collège des enseignants de neurologie')], 'Collège des enseignants de neurologie', 'Collège français, source pédagogique de sémiologie ; passage réellement relu.', 'g03-r14')
add_if_absent('DGLN', [('DGLN', 'Deutsche Gesellschaft für Liquordiagnostik und Klinische Neurochemie')], 'Deutsche Gesellschaft für Liquordiagnostik und Klinische Neurochemie', 'Société allemande du diagnostic du liquide céphalorachidien et de neurochimie clinique.', 'g03-r7')
add_if_absent('UPSA', [('UPSA', 'UPSA Switzerland')], 'UPSA Switzerland', 'Titulaire de l’autorisation suisse de la présentation DAFALGAN consultée.', 'g03-r10')
add_if_absent('EPA', [('EPA', 'Entrustable Professional Activity')], 'Entrustable Professional Activity', 'Activité professionnelle confiable du référentiel PROFILES ; EPA 6d concerne céphalée aiguë sévère et méningisme.', 'g03-r18')
add_if_absent('SIWF', [('SIWF', 'Schweizerisches Institut für ärztliche Weiter- und Fortbildung')], 'Schweizerisches Institut für ärztliche Weiter- und Fortbildung', 'Institut suisse pour la formation médicale postgraduée et continue, site hébergeant le référentiel PROFILES consulté.', 'g03-r18')
add_if_absent('R1', [('R1', 'Référence R1')], 'Référence R1', 'SSI : addendum suisse à ESCMID, 28 décembre 2017 ; passage et limites dans la fiche de source.', 'g03-r1')
add_if_absent('R2', [('R2', 'Référence R2')], 'Référence R2', 'Syndrome méningé fébrile aux urgences, 2016 ; passage et limites dans la fiche de source.', 'g03-r2')
add_if_absent('R3', [('R3', 'Référence R3')], 'Référence R3', 'Méningite chronique : étiologies et approche diagnostique, 2021 ; passage et limites dans la fiche de source.', 'g03-r3')
add_if_absent('R4', [('R4', 'Référence R4')], 'Référence R4', 'WHO guidelines on meningitis diagnosis, treatment and care, 2025 ; passage et limites dans la fiche de source.', 'g03-r4')
add_if_absent('R5', [('R5', 'Référence R5')], 'Référence R5', 'German guidelines on acute bacterial meningitis in adults, 2023 ; passage et limites dans la fiche de source.', 'g03-r5')
add_if_absent('R6', [('R6', 'Référence R6')], 'Référence R6', 'DGN : Virale Meningoenzephalitis, version 7, 2025 ; passage et limites dans la fiche de source.', 'g03-r6')
add_if_absent('R7', [('R7', 'Référence R7')], 'Référence R7', 'S1 guideline lumbar puncture and cerebrospinal fluid analysis, traduction 2020 ; passage et limites dans la fiche de source.', 'g03-r7')
add_if_absent('R8', [('R8', 'Référence R8')], 'Référence R8', 'Mollaret au Danemark : cohorte nationale, 2024 ; passage et limites dans la fiche de source.', 'g03-r8')
add_if_absent('R9', [('R9', 'Référence R9')], 'Référence R9', 'Méningite aseptique médicamenteuse : 329 cas français, 2019 ; passage et limites dans la fiche de source.', 'g03-r9')
add_if_absent('R10', [('R10', 'Référence R10')], 'Référence R10', 'DAFALGAN comprimés 500 mg, FI septembre 2025 ; passage et limites dans la fiche de source.', 'g03-r10')
add_if_absent('R11', [('R11', 'Référence R11')], 'Référence R11', 'Privigen : FI juillet 2025 ; passage et limites dans la fiche de source.', 'g03-r11')
add_if_absent('R12', [('R12', 'Référence R12')], 'Référence R12', 'Ibuprofen-Mepha Teva : FI décembre 2024 ; passage et limites dans la fiche de source.', 'g03-r12')
add_if_absent('R13', [('R13', 'Référence R13')], 'Référence R13', 'CIM-10-GM 2024 : G03 ; passage et limites dans la fiche de source.', 'g03-r13')
add_if_absent('R14', [('R14', 'Référence R14')], 'Référence R14', 'CEN : méningites et méningo-encéphalites, item 151 ; passage et limites dans la fiche de source.', 'g03-r14')
add_if_absent('R15', [('R15', 'Référence R15')], 'Référence R15', 'Essai randomisé valaciclovir suppressif après méningite HSV-2, 2012 ; passage et limites dans la fiche de source.', 'g03-r15')
add_if_absent('R16', [('R16', 'Référence R16')], 'Référence R16', 'Gray Anatomy 1918, planche 1196 : enveloppes et sinus ; passage et limites dans la fiche de source.', 'g03-r16')
add_if_absent('R17', [('R17', 'Référence R17')], 'Référence R17', 'Gray Anatomy 1918, planche 764 : voie motrice ; passage et limites dans la fiche de source.', 'g03-r17')
add_if_absent('R18', [('R18', 'Référence R18')], 'Référence R18', 'PROFILES 2017 : urgence céphalée sévère et méningisme ; passage et limites dans la fiche de source.', 'g03-r18')
