from cardio_1 import a, G
# G83 — Autres syndromes paralytiques (N-05-Neurologie). Entrées conditionnelles : aucun terme existant n’est écrasé.
from pathlib import Path
import importlib
_ex = set(G)
for _p in sorted(Path(__file__).parent.glob('*.py')):
    if _p.stem in {'g83', '__init__', 'cardio_1'}:
        continue
    try:
        _ex |= set(getattr(importlib.import_module(_p.stem), 'G', {}))
    except Exception:
        pass
def ac(k, lit, full, d, ref=None):
    if k not in _ex:
        a(k, lit, full, d, ref)

def code(k, libelle, ref):
    ac(k, [(k, 'code de la CIM-10-GM 2024, non une abréviation')], 'Code ' + k + ' de la CIM-10-GM : ' + libelle,
       '<p>Ce code de la classification internationale des maladies, version allemande 2024, désigne : ' + libelle + '.</p>', ref)

code('G83.0', 'diparésie et diplégie des membres supérieurs', 'g83-monoparesie')
code('G83.1', 'monoplégie d’un membre inférieur', 'g83-monoparesie')
code('G83.2', 'monoparésie et monoplégie d’un membre supérieur', 'g83-monoparesie')
code('G83.3', 'monoparésie et monoplégie, sans précision', 'g83-monoparesie')
code('G83.4', 'syndrome de la queue de cheval', 'g83-codage-ces')
code('G83.40', 'syndrome de la queue de cheval, complet', 'g83-codage-ces')
code('G83.41', 'syndrome de la queue de cheval, incomplet', 'g83-codage-ces')
code('G83.49', 'syndrome de la queue de cheval, non précisé', 'g83-codage-ces')
code('G83.5', 'locked-in syndrome (syndrome de déefférentation motrice)', 'g83-lis')
code('G83.6', 'paralysie faciale centrale', 'g83-faciale-centrale')
code('G83.8', 'autres syndromes paralytiques précisés, dont la paralysie de Todd', 'g83-todd')
code('G83.9', 'syndrome paralytique, sans précision', 'g83-codage')
code('G51.0', 'paralysie faciale par lésion du deuxième motoneurone (forme périphérique)', 'g83-faciale-centrale')
code('G95.8', 'autres maladies précisées de la moelle épinière, code ajouté pour documenter un trouble vésical neurogène', 'g83-codage-ces')

ac('MacFarlane', [('MacFarlane', 'nom propre d’un auteur, non une abréviation')], 'MacFarlane, coauteur de la classification de 2002', '<p>Gleave et MacFarlane ont proposé en 2002 la distinction entre syndrome incomplet et syndrome avec rétention, la plus utilisée.</p>', 'g83-cesi-cesr')
ac('DeLong', [('DeLong', 'nom propre d’un auteur, non une abréviation')], 'DeLong, premier auteur d’une méta-analyse de 2008', '<p>Cette méta-analyse étudie le délai opératoire dans le syndrome de la queue de cheval avec rétention urinaire.</p>', 'g83-delong')
ac('CES', [('C', 'Cauda'), ('E', 'Equina'), ('S', 'Syndrome')], 'Cauda equina syndrome (syndrome de la queue de cheval)', '<p>Dysfonctionnement des racines sacrées à partir de la deuxième, avec trouble vésical ou intestinal, hypoesthésie en selle ou trouble sexuel.</p>', 'g83-ces')
ac('CESI', [('CES', 'Cauda Equina Syndrome'), ('I', 'Incomplete')], 'Syndrome de la queue de cheval incomplet', '<p>Troubles urinaires neurogènes avec contrôle volontaire conservé : la miction reste possible, même difficile.</p>', 'g83-cesi-cesr')
ac('CESR', [('CES', 'Cauda Equina Syndrome'), ('R', 'with Retention')], 'Syndrome de la queue de cheval avec rétention', '<p>Perte du contrôle volontaire de la miction, avec rétention indolore et regorgement.</p>', 'g83-cesi-cesr')
ac('CESS', [('CES', 'Cauda Equina Syndrome'), ('S', 'Suspected')], 'Syndrome de la queue de cheval suspecté', '<p>Symptômes bilatéraux des jambes ou grosse hernie connue, sans symptôme de queue de cheval.</p>', 'g83-tandon')
ac('CESE', [('CES', 'Cauda Equina Syndrome'), ('E', 'Early')], 'Syndrome de la queue de cheval précoce', '<p>Hypoesthésie périnéale à vessie normale, ou changement mictionnel à sensibilité normale.</p>', 'g83-tandon')
ac('CESC', [('CES', 'Cauda Equina Syndrome'), ('C', 'Complete')], 'Syndrome de la queue de cheval complet', '<p>Perte de toutes les fonctions sensitives et motrices de la queue de cheval, plus grave que le stade avec rétention.</p>', 'g83-tandon')
ac('BASS', [('B', 'British'), ('A', 'Association of'), ('S', 'Spine'), ('S', 'Surgeons')], 'Association britannique des chirurgiens du rachis', '<p>Son standard demande une IRM immédiate, dans l’heure qui suit la présentation aux urgences, devant un syndrome de la queue de cheval suspecté.</p>', 'g83-irm')
ac('GIRFT', [('G', 'Getting'), ('I', 'It'), ('R', 'Right'), ('F', 'First'), ('T', 'Time')], 'Programme britannique « Getting It Right First Time »', '<p>Son parcours de 2025 sur le syndrome de la queue de cheval décrit l’imagerie, le scanner vésical et le délai de décompression.</p>', 'g83-pvr')
ac('JBJS', [('J', 'Journal of'), ('B', 'Bone and'), ('J', 'Joint'), ('S', 'Surgery')], 'Journal of Bone and Joint Surgery', '<p>Revue dans laquelle a paru la revue de 2025 sur le syndrome de la queue de cheval.</p>', 'g83-incidence')
ac('UWS', [('U', 'Unresponsive'), ('W', 'Wakefulness'), ('S', 'Syndrome')], 'Syndrome d’éveil non répondant', '<p>État d’éveil sans signe de conscience de soi ou de l’environnement ; il se distingue du locked-in syndrome, où la cognition est conservée.</p>', 'g83-lis-ddx')
ac('MCS', [('M', 'Minimally'), ('C', 'Conscious'), ('S', 'State')], 'État de conscience minimale', '<p>État où des signes comportementaux de conscience, fluctuants mais reproductibles, sont observés.</p>', 'g83-lis-ddx')
ac('CRS-R', [('C', 'Coma'), ('R', 'Recovery'), ('S', 'Scale'), ('R', 'Revised')], 'Échelle de récupération du coma, révisée', '<p>Étalon clinique pour séparer syndrome d’éveil non répondant et état de conscience minimale ; elle manque les patients sans sortie comportementale.</p>', 'g83-crs')
ac('EAN', [('E', 'European'), ('A', 'Academy of'), ('N', 'Neurology')], 'Académie européenne de neurologie', '<p>Elle propose une évaluation multimodale des troubles de la conscience.</p>', 'g83-crs')
ac('ESMINT', [('E', 'European'), ('S', 'Society for'), ('M', 'Minimally'), ('I', 'Invasive'), ('N', 'Neurological'), ('T', 'Therapy')], 'Société européenne de thérapie neurologique mini-invasive', '<p>Coauteur, avec l’Organisation européenne de l’accident vasculaire cérébral, de la recommandation 2024 sur l’occlusion de l’artère basilaire.</p>', 'g83-eso')
