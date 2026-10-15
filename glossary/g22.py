"""Abréviations G22 (cycle Betta 35) ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'g22', '__init__'}:
        continue
    try:
        _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
    except Exception:
        pass
G = {}
def add_if_absent(key, letters, full, definition, window=None):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full, 'def': '<p>' + definition + '</p>', 'ref': window}
add_if_absent('A52.1', [('A52.1', 'code de la CIM-10-GM : A, catégorie 52, subdivision 1')],
              'Syphilis tardive du système nerveux (neurosyphilis), code dague',
              'Ce code désigne la neurosyphilis. Il est le seul code étiologique nommé sous G22* par la classification.', 'g22-codage')
add_if_absent('G21.2', [('G21.2', 'code de la CIM-10-GM : G, catégorie 21, subdivision 2')],
              'Syndrome parkinsonien secondaire dû à d’autres agents externes',
              'Ce code regroupe les formes toxiques de parkinsonisme ; elles relèvent de la leçon G21.', 'g22-codage')
add_if_absent('DGN', [('D', 'Deutsche (allemande)'), ('G', 'Gesellschaft (société)'), ('N', 'Neurologie')],
              'Deutsche Gesellschaft für Neurologie',
              'Cette société allemande de neurologie a publié la ligne directrice 2026 sur la neurosyphilis, avec mandat de la Société suisse de neurologie.', 'g22-lcr-syph')
add_if_absent('MDS', [('M', 'Movement (des mouvements)'), ('D', 'Disorder (troubles)'), ('S', 'Society (société)')],
              'Movement Disorder Society',
              'Cette société internationale a publié en 2015 les critères cliniques de la maladie de Parkinson.', 'g22-parkinsonisme')
add_if_absent('Parkinson-Syndrom', [('Parkinson-Syndrom', 'expression allemande du libellé de la classification, non une abréviation')],
              'Parkinson-Syndrom, syndrome parkinsonien en allemand',
              'Cette expression figure dans le libellé allemand de G22* publié par le BfArM.', 'g22-codage')
add_if_absent('Chilcott-Lauber', [('Chilcott-Lauber', 'nom d’auteur, non une abréviation')],
              'Chilcott-Lauber, auteure',
              'Ce nom désigne la première auteure d’une revue suisse de 2005 sur la maladie de Wilson.', 'g22-wilson')
add_if_absent('Creutzfeldt-Jakob', [('Creutzfeldt-Jakob', 'noms des deux médecins qui ont décrit la maladie, non une abréviation')],
              'Maladie de Creutzfeldt-Jakob',
              'Cette maladie à prions est toujours mortelle et sans traitement ; elle est déclarée en Suisse.', 'g22-mcj')
add_if_absent('Kayser-Fleischer', [('Kayser-Fleischer', 'noms des deux ophtalmologues, non une abréviation')],
              'Anneau de Kayser-Fleischer',
              'Cet anneau cornéen est observé à la lampe à fente dans plus de 90 % des formes neurologiques de la maladie de Wilson.', 'g22-wilson')
add_if_absent('ATP7B', [('ATP', 'Adénosine TriPhosphatase'), ('7B', 'sous-type 7B de la famille des ATPases de transport du cuivre')],
              'Gène et transporteur du cuivre de type ATPase 7B',
              'Son déficit réduit l’excrétion biliaire du cuivre et cause la maladie de Wilson.', 'g22-wilson')
add_if_absent('DaTSCAN', [('DaT', 'Dopamine Transporter (transporteur de la dopamine)'), ('SCAN', 'scintigraphie, de l’anglais scan')],
              'Scintigraphie du transporteur de la dopamine (ioflupane marqué à l’iode 123)',
              'Cet examen visualise la perte de terminaisons dopaminergiques ; il ne sépare pas fiablement Wilson et Parkinson.', 'g22-datscan')
add_if_absent('MPTP', [('M', 'Méthyl'), ('P', 'Phényl'), ('T', 'Tétrahydro'), ('P', 'Pyridine')],
              '1-méthyl-4-phényl-1,2,3,6-tétrahydropyridine',
              'Cette substance toxique est citée parmi les causes toxiques de parkinsonisme.', 'g22-sources')
add_if_absent('HHV-6', [('H', 'Human (humain)'), ('H', 'Herpes'), ('V', 'Virus'), ('6', 'type 6')],
              'Virus herpès humain de type 6',
              'Ce virus figure parmi les causes infectieuses citées de parkinsonisme.', 'g22-sources')
add_if_absent('CRMP5', [('C', 'Collapsin'), ('R', 'Response'), ('M', 'Mediator'), ('P', 'Protein'), ('5', 'numéro 5')],
              'Collapsin response mediator protein 5',
              'Les anticorps dirigés contre cette protéine causent une encéphalite paranéoplasique avec paralysie verticale du regard.', 'g22-autoimmun')
add_if_absent('NMDAR', [('N', 'N-méthyl'), ('M', 'D-'), ('D', 'Aspartate'), ('AR', 'récepteur (receptor)')],
              'Récepteur au N-méthyl-D-aspartate',
              'Les anticorps contre ce récepteur causent une encéphalite auto-immune, surtout pédiatrique pour le parkinsonisme.', 'g22-autoimmun')
add_if_absent('anti-NMDAR', [('anti', 'dirigé contre'), ('NMDAR', 'récepteur au N-méthyl-D-aspartate')],
              'Anticorps dirigé contre le récepteur au N-méthyl-D-aspartate',
              'Cette encéphalite auto-immune donne un parkinsonisme surtout chez l’enfant.', 'g22-autoimmun')
add_if_absent('LGI1', [('L', 'Leucine-rich'), ('G', 'Glioma-'), ('I', 'Inactivated'), ('1', 'numéro 1')],
              'Leucine-rich glioma-inactivated 1',
              'Les anticorps dirigés contre cette protéine définissent une encéphalite auto-immune.', 'g22-autoimmun')
add_if_absent('CASPR2', [('C', 'Contactin-'), ('AS', 'ASsociated'), ('PR', 'PRotein-like'), ('2', 'numéro 2')],
              'Contactin-associated protein-like 2',
              'Les anticorps dirigés contre cette protéine définissent une encéphalite auto-immune.', 'g22-autoimmun')
add_if_absent('IgLON5', [('Ig', 'Immunoglobuline'), ('LON', 'famille LON (LAMP, OBCAM, neurotrimine)'), ('5', 'numéro 5')],
              'Protéine de la famille IgLON, numéro 5',
              'Les anticorps dirigés contre cette protéine définissent une encéphalite auto-immune.', 'g22-autoimmun')
add_if_absent('Anti-Ma2', [('Anti', 'dirigé contre'), ('Ma2', 'protéine Ma2 neuronale')],
              'Anticorps anti-Ma2',
              'Ces anticorps s’associent à une tumeur germinale testiculaire chez le jeune homme et à une paralysie verticale du regard.', 'g22-autoimmun')
add_if_absent('CXCL13', [('CXCL', 'C-X-C motif ChemoKine Ligand'), ('13', 'numéro 13')],
              'Chimiokine CXCL13',
              'Son dosage dans le liquide céphalorachidien est utile au diagnostic et au suivi de la neurosyphilis.', 'g22-lcr-syph')
add_if_absent('RT-QuIC', [('RT', 'Real-Time (en temps réel)'), ('QuIC', 'Quaking-Induced Conversion')],
              'Conversion induite par agitation en temps réel',
              'Ce test est cité pour la maladie de Creutzfeldt-Jakob ; ses critères n’ont pas été lus dans ce cours.', 'g22-mcj')
add_if_absent('DESH', [('D', 'Disproportionately'), ('E', 'Enlarged'), ('S', 'Subarachnoid-space'), ('H', 'Hydrocephalus')],
              'Hydrocéphalie avec espaces sous-arachnoïdiens disproportionnés',
              'Ce signe d’imagerie soutient l’hydrocéphalie à pression normale.', 'g22-hpn')
add_if_absent('UWDRS', [('U', 'Unified (unifiée)'), ('W', 'Wilson'), ('D', 'Disease (maladie)'), ('R', 'Rating'), ('S', 'Scale (échelle)')],
              'Échelle unifiée d’évaluation de la maladie de Wilson',
              'Une version minimale de 9 items sert au suivi clinique.', 'g22-wilson')
add_if_absent('EASL', [('E', 'European'), ('A', 'Association'), ('S', 'for the Study of the'), ('L', 'Liver')],
              'Association européenne pour l’étude du foie',
              'Cette association a publié en 2025 la recommandation sur la maladie de Wilson.', 'g22-cuivre-bilan')
add_if_absent('ERN', [('E', 'European'), ('R', 'Reference'), ('N', 'Network')],
              'Réseau européen de référence',
              'Ce réseau est associé à la recommandation 2025 sur la maladie de Wilson.', 'g22-cuivre-bilan')
add_if_absent('EASL-ERN', [('EASL', 'European Association for the Study of the Liver'), ('ERN', 'European Reference Network')],
              'Recommandation de l’Association européenne pour l’étude du foie et du Réseau européen de référence',
              'Cette recommandation de 2025 retient le score de Leipzig et le cuivre échangeable relatif.', 'g22-cuivre-bilan')
