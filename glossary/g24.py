"""Abréviations G24 Dystonie ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib, sys
_here = Path(__file__).resolve().parent
_root = next((p for p in _here.parents if (p / 'build_medina.py').exists()), None)
_dirs = [_here] + ([_root / 'glossary'] if _root else [])
_existing = {}
for _d in _dirs:
    if str(_d) not in sys.path:
        sys.path.append(str(_d))
    for _path in sorted(_d.glob('*.py')):
        if _path.stem in {'g24', '__init__'}:
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

# Classification et nomenclature
add_if_absent('DYT', [('DYT', 'préfixe de nomenclature tiré du mot anglais dystonia, non une abréviation développée lettre à lettre')],
              'Préfixe DYT des dystonies génétiques',
              'Ce préfixe précède le nom du gène dans la nomenclature de la Task Force de la Movement Disorder Society reprise par la ligne directrice allemande de 2021. Les anciens symboles numériques (DYT1, DYT6) subsistent dans les manuels.', 'g24-dyt')
for _k, _g, _d in [('DYT-TOR1A', 'TOR1A', 'Dystonie généralisée à début précoce, ancien symbole DYT1.'),
                   ('DYT-THAP1', 'THAP1', 'Dystonie segmentaire ou généralisée de l’adolescent ou de l’adulte jeune, ancien symbole DYT6.'),
                   ('DYT-ANO3', 'ANO3', 'Dystonie cervicale ou segmentaire avec tremblement, ancien symbole DYT24.'),
                   ('DYT-GNAL', 'GNAL', 'Dystonie crânio-cervicale de l’adulte, ancien symbole DYT25.'),
                   ('DYT-KMT2B', 'KMT2B', 'Dystonie débutant aux membres inférieurs dans l’enfance, ancien symbole DYT28.')]:
    add_if_absent(_k, [('DYT', 'préfixe de nomenclature des dystonies génétiques'), (_g, 'symbole du gène')],
                  'Dystonie liée au gène ' + _g, _d + ' Transmission autosomique dominante.', 'g24-dyt')
for _k, _d in [('DYT1', 'Ancien symbole de la forme liée à TOR1A.'), ('DYT6', 'Ancien symbole de la forme liée à THAP1.'),
               ('DYT24', 'Ancien symbole de la forme liée à ANO3.'), ('DYT25', 'Ancien symbole de la forme liée à GNAL.'),
               ('DYT28', 'Ancien symbole de la forme liée à KMT2B.'), ('DYT5a', 'Ancien symbole de la dystonie dopa-sensible liée à GCH1.'),
               ('DYT5b', 'Ancien symbole des formes dopa-sensibles récessives liées à TH et SPR.'),
               ('DYT12', 'Ancien symbole du dystonie-parkinsonisme à début rapide lié à ATP1A3.'),
               ('DYT11', 'Ancien symbole du myoclonus-dystonie lié à SGCE.')]:
    add_if_absent(_k, [('DYT', 'préfixe de nomenclature des dystonies génétiques'), (_k[3:], 'numéro d’ordre de l’ancien système')],
                  'Ancien symbole ' + _k, _d, 'g24-dyt')
for _k, _a, _g, _d in [('PARK-GCH1', 'PARK', 'GCH1', 'Dystonie dopa-sensible de Segawa, transmission autosomique dominante.'),
                       ('PARK-TH', 'PARK', 'TH', 'Forme dopa-sensible récessive de l’enfant, avec signes associés.'),
                       ('PARK-ATP1A3', 'PARK', 'ATP1A3', 'Dystonie-parkinsonisme à début rapide, transmission autosomique dominante.'),
                       ('MYOC-SGCE', 'MYOC', 'SGCE', 'Myoclonus-dystonie, transmission autosomique dominante.')]:
    add_if_absent(_k, [(_a, 'composante de la nomenclature : parkinsonisme ou myoclonie associé'), (_g, 'symbole du gène')],
                  'Forme combinée liée au gène ' + _g, _d, 'g24-dyt')
add_if_absent('TOR1A', [('TOR', 'Torsin'), ('1A', 'family 1 member A')], 'Gène TOR1A (torsin family 1 member A)',
              'Gène des dystonies généralisées à début précoce. La ligne directrice recommande de le tester dès un début avant 26 ans, même sans antécédent familial, car la pénétrance est réduite.', 'g24-dyt')
add_if_absent('THAP1', [('THAP', 'THAP domain'), ('1', 'containing 1')], 'Gène THAP1 (THAP domain containing 1)',
              'Gène des dystonies segmentaires ou généralisées de l’adolescent ou de l’adulte jeune, avec dysphonie fréquente.', 'g24-dyt')
add_if_absent('GNAL', [('G', 'G protein'), ('NAL', 'subunit alpha L')], 'Gène GNAL (G protein subunit alpha L)',
              'Gène de la dystonie crânio-cervicale de l’adulte ; il est surtout recherché quand une dystonie focale de l’adulte est familiale.', 'g24-dyt')
add_if_absent('ANO3', [('ANO', 'Anoctamin'), ('3', 'numéro 3')], 'Gène ANO3 (anoctamin 3)',
              'Gène d’une dystonie cervicale ou segmentaire avec tremblement.', 'g24-dyt')
add_if_absent('KMT2B', [('KMT', 'Lysine MethylTransferase'), ('2B', 'type 2B')], 'Gène KMT2B (lysine methyltransferase 2B)',
              'Gène d’une dystonie qui débute aux membres inférieurs dans l’enfance, puis se généralise, avec dysmorphie et déficit cognitif léger.', 'g24-dyt')
add_if_absent('GCH1', [('G', 'GTP'), ('CH', 'CycloHydrolase'), ('1', 'numéro 1')], 'Gène GCH1 (GTP cyclohydrolase 1)',
              'Gène de la dystonie dopa-sensible de Segawa : un déficit de synthèse de la tétrahydrobioptérine diminue la dopamine.', 'g24-gch1')
add_if_absent('TH', [('T', 'Tyrosine'), ('H', 'Hydroxylase')], 'Tyrosine hydroxylase',
              'Gène de formes dopa-sensibles récessives de l’enfant, avec signes associés.', 'g24-gch1')
add_if_absent('SPR', [('SP', 'Sepiapterin'), ('R', 'Reductase')], 'Sépiaptérine réductase',
              'Gène de formes dopa-sensibles récessives de l’enfant, avec signes associés.', 'g24-gch1')
add_if_absent('ATP1A3', [('ATP', 'ATPase'), ('1A3', 'Na+/K+ transporting subunit alpha 3')], 'Gène ATP1A3',
              'Gène du dystonie-parkinsonisme à début rapide, de transmission autosomique dominante.', 'g24-dyt')
add_if_absent('SGCE', [('SGC', 'SarGlyCan'), ('E', 'epsilon')], 'Gène SGCE (sarcoglycan epsilon)',
              'Gène du myoclonus-dystonie, dont les myoclonies sont typiquement sensibles à l’alcool ; il est testé en leur présence.', 'g24-dyt')
add_if_absent('Col-Cap', [('Col', 'collis, le rachis cervical'), ('Cap', 'caput, la tête')], 'Concept Col-Cap (collis et caput)',
              'Concept qui sépare les mouvements du rachis cervical de ceux de la tête pour décrire huit motifs de base de la dystonie cervicale.', 'g24-colcap')
add_if_absent('Kayser-Fleischer', [('Kayser-Fleischer', 'noms propres des deux médecins éponymes, non une abréviation')], 'Anneau de Kayser-Fleischer',
              'Anneau visible à la lampe à fente, recherché chez l’enfant, l’adolescent et l’adulte de moins de 50 ans pour la maladie de Wilson.', 'g24-wilson')
add_if_absent('Lambert-Eaton', [('Lambert-Eaton', 'noms propres des deux médecins éponymes, non une abréviation')], 'Syndrome de Lambert-Eaton',
              'Contre-indication de Xeomin® selon l’information professionnelle suisse, avec la myasthénie.', 'g24-xeomin')
add_if_absent('GLUT1', [('GLUT', 'GLUcose Transporter'), ('1', 'numéro 1')], 'Transporteur de glucose de type 1',
              'Le glucose et le lactate du liquide cérébrospinal sont dosés dans les débuts précoces pour rechercher un déficit en ce transporteur.', 'g24-wilson')
add_if_absent('ESEMED', [('ESEMED', 'nom d’étude cité dans le titre de la publication, non développé en sigle dans le résumé lu')], 'Étude européenne ESEMED (1996–1997)',
              'Étude de prévalence de la dystonie primaire dans huit pays européens, menée par recrutement en cliniques spécialisées ; elle rapporte 152 cas par million.', 'g24-prevalence')
# Codes
for _k, _t in [('G24.0', 'dystonie médicamenteuse'), ('G24.3', 'torticolis spasmodique'), ('G24.4', 'dystonie bucco-faciale idiopathique'),
               ('G24.5', 'blépharospasme'), ('G24.9', 'dystonie, sans précision')]:
    add_if_absent(_k, [('G', 'chapitre des maladies du système nerveux'), (_k[1:], 'sous-catégorie : ' + _t)],
                  'Sous-catégorie ' + _k + ' de la CIM-10-GM', 'Sous-catégorie de la catégorie G24 Dystonie : ' + _t + '.', 'g24-cim')
add_if_absent('M43.6', [('M', 'chapitre des maladies du système ostéo-articulaire'), ('43.6', 'torticolis')], 'Sous-catégorie M43.6 de la CIM-10-GM',
              'Torticolis sans précision, exclu de G24.3.', 'g24-cim')
add_if_absent('G80.3', [('G', 'chapitre des maladies du système nerveux'), ('80.3', 'paralysie cérébrale dyskinétique')], 'Sous-catégorie G80.3 de la CIM-10-GM',
              'Paralysie cérébrale athétosique, exclue de la catégorie G24.', 'g24-cim')
# Examens, échelles, structures
add_if_absent('EMG', [('É', 'Électro'), ('M', 'Myo'), ('G', 'Graphie')], 'Électromyographie',
              'Enregistrement de l’activité électrique des muscles. Dans la dystonie, il peut guider l’injection de toxine et distinguer une dystonie saccadée d’une myoclonie.', 'g24-guidage')
add_if_absent('BFMDRS', [('B', 'Burke'), ('F', 'Fahn'), ('M', 'Marsden'), ('D', 'Dystonia'), ('R', 'Rating'), ('S', 'Scale')], 'Échelle de dystonie de Burke-Fahn-Marsden',
              'Échelle utilisée dans les essais de stimulation cérébrale profonde des dystonies généralisées, où la ligne directrice rapporte une amélioration d’environ 50 %.', 'g24-scp')
add_if_absent('TWSTRS', [('T', 'Toronto'), ('W', 'Western'), ('S', 'Spasmodic'), ('T', 'Torticollis'), ('R', 'Rating'), ('S', 'Scale')], 'Échelle de torticolis spasmodique de Toronto Western',
              'Échelle utilisée pour la dystonie cervicale ; la ligne directrice rapporte une réduction de 40 % à 3 mois après stimulation cérébrale profonde.', 'g24-scp')
add_if_absent('NBIA', [('N', 'Neurodegeneration'), ('B', 'with Brain'), ('I', 'Iron'), ('A', 'Accumulation')], 'Neurodégénérescence avec accumulation cérébrale de fer',
              'Groupe de dystonies secondaires où la stimulation cérébrale profonde donne une amélioration de 25 %.', 'g24-scp')
add_if_absent('GPi', [('G', 'Globus'), ('P', 'Pallidus'), ('i', 'internus')], 'Pallidum interne (globus pallidus internus)',
              'Cible de la stimulation cérébrale profonde dans les dystonies généralisées et segmentaires sévères.', 'g24-scp')
add_if_absent('SV2', [('S', 'Synaptic'), ('V', 'Vesicle glycoprotein'), ('2', 'numéro 2')], 'Glycoprotéine de vésicule synaptique 2',
              'Protéine par laquelle la toxine botulique est internalisée dans la terminaison nerveuse.', 'g24-toxine-meca')
add_if_absent('SNAP-25', [('SNAP', 'Synaptosomal-Associated Protein'), ('25', 'de 25 kilodaltons')], 'Protéine associée aux synaptosomes de 25 kDa',
              'La chaîne légère de la toxine botulique A la clive et bloque ainsi la libération d’acétylcholine.', 'g24-toxine-meca')
add_if_absent('BoNT-A', [('BoNT', 'Botulinum Neurotoxin'), ('A', 'type A')], 'Neurotoxine botulique de type A',
              'Sérotype dont la chaîne légère clive SNAP-25 ; il regroupe les trois produits suisses BOTOX®, Xeomin® et Dysport®.', 'g24-toxine-meca')
