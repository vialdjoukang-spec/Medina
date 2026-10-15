"""Abréviations G26 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'g26', '__init__'}:
        continue
    _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
G = {}
def add_if_absent(key, letters, full, definition, window):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full,
                  'def': '<p>' + definition + '</p>', 'ref': window}

add_if_absent('DHCA', [('D','Dégénérescence'),('H','Hépato'),('C','Cérébrale'),('A','Acquise')],
              'Dégénérescence hépatocérébrale acquise',
              'Syndrome neurologique chronique des hépatopathies avancées, surtout avec shunts porto-systémiques. L’ammoniac et le manganèse s’accumulent et s’accompagnent d’une neuro-inflammation.', 'g26-dhca')
add_if_absent('NMDAR', [('N','N-'),('M','Méthyl'),('D','-D-'),('A','Aspartate'),('R','Receptor (récepteur)')],
              'Récepteur N-méthyl-D-aspartate',
              'Antigène de surface neuronal visé par les anticorps de l’encéphalite auto-immune anti-NMDAR. Ces anticorps répondent habituellement bien à l’immunothérapie.', 'g26-anticorps')
add_if_absent('GAD65', [('G','Glutamate'),('A','Acid (acide)'),('D','Décarboxylase'),('65','isoforme 65')],
              'Décarboxylase de l’acide glutamique, isoforme 65',
              'Enzyme neuronale dont les anticorps figurent dans la liste des encéphalites auto-immunes de la directive sur la chorée.', 'g26-anticorps')
add_if_absent('CASPR2', [('C','Contactin'),('AS','ASsociated (associée)'),('P','Protein (protéine)'),('R','-like (de type)'),('2','numéro 2')],
              'Protéine de type associée à la contactine, numéro 2',
              'Antigène de surface neuronal visé par des anticorps ; la réponse à l’immunothérapie est habituellement bonne. Le liquide cérébro-spinal de base est souvent normal.', 'g26-anticorps')
add_if_absent('LGI1', [('L','Leucine-rich (riche en leucine)'),('G','Glioma (gliome)'),('I','Inactivated (inactivé)'),('1','numéro 1')],
              'Protéine riche en leucine inactivée dans le gliome, numéro 1',
              'Antigène de surface neuronal ; ses anticorps provoquent des crises dystoniques facio-brachiales brèves, avec une réponse très favorable aux corticostéroïdes.', 'g26-anticorps')
add_if_absent('IgLON5', [('IgLON5','nom d’une famille de protéines d’adhésion, numéro 5 ; développement littéral non fourni par les sources lues')],
              'IgLON5, protéine neuronale',
              'Antigène neuronal cité par la directive parmi les anticorps des encéphalites auto-immunes.', 'g26-anticorps')
add_if_absent('CRMP-5', [('C','Collapsin'),('R','Response'),('M','Mediator'),('P','Protein'),('5','numéro 5')],
              'Protéine médiatrice de la réponse à la collapsine, numéro 5',
              'Antigène intracellulaire d’une encéphalite paranéoplastique ; l’IRM peut montrer des hypersignaux FLAIR et une atrophie caudée.', 'g26-anticorps')
add_if_absent('DPPX', [('D','Dipeptidyl'),('P','Peptidase'),('P','-like Protein (protéine de type)'),('X','symbole historique')],
              'Protéine de type dipeptidyl-peptidase',
              'Antigène visé par des anticorps associés à une diarrhée prolongée avec amaigrissement et myoclonies.', 'g26-anticorps')
add_if_absent('ATP7B', [('ATP','ATPase (adénosine triphosphatase)'),('7B','membre 7B')],
              'Gène de l’ATPase transporteuse de cuivre 7B',
              'Son altération, autosomique récessive, bloque l’excrétion biliaire du cuivre et son incorporation dans la céruloplasmine : c’est la maladie de Wilson.', 'g26-wilson')
add_if_absent('CK', [('C','Créatine'),('K','Kinase')], 'Créatine kinase',
              'Enzyme musculaire élevée dans le syndrome malin des neuroleptiques ; elle fait aussi partie du bilan d’une chorée sporadique.', 'g26-bilan')
add_if_absent('DGN', [('D','Deutsche (allemande)'),('G','Gesellschaft (société)'),('N','Neurologie (de neurologie)')], 'Société allemande de neurologie',
              'Elle publie les directives sur la chorée et sur la maladie de Wilson utilisées dans ce cours ; la première est approuvée par la Société suisse de neurologie.', 'g26-bilan')
add_if_absent('ERN', [('E','European'),('R','Reference'),('N','Networks (réseaux européens de référence)')], 'Réseaux européens de référence',
              'Ils ont co-signé la recommandation EASL-ERN 2025 sur la maladie de Wilson, dont seul le résumé a été lu.', 'g26-leipzig')
add_if_absent('TPO', [('T','Thyro'),('P','Per'),('O','Oxydase')], 'Thyroperoxydase',
              'Enzyme thyroïdienne dont les anticorps (anti-TPO) font partie du bilan thyroïdien d’une chorée sporadique.', 'g26-bilan')
add_if_absent('TRAK', [('T','Thyrotropin'),('R','Rezeptor (récepteur)'),('A','Anti'),('K','Körper (anticorps)')], 'Anticorps antirécepteur de la TSH',
              'Dosés dans le bilan thyroïdien de la chorée sporadique, notamment pour une hyperthyroïdie.', 'g26-bilan')
add_if_absent('ANA', [('A','Anti'),('N','Nuclear'),('A','Antibodies (anticorps)')], 'Anticorps antinucléaires',
              'Ils font partie du bilan auto-immun de la chorée sporadique, en particulier pour le lupus.', 'g26-bilan')
add_if_absent('VMAT2', [('V','Vesicular (vésiculaire)'),('MA','MonoAmine (monoamines)'),('T','Transporter (transporteur)'),('2','type 2')], 'Transporteur vésiculaire des monoamines de type 2',
              'La tétrabénazine l’inhibe : elle déplète les monoamines, dont la dopamine, ce qui réduit les mouvements involontaires.', 'g26-tetrabenazine')
add_if_absent('D2', [('D','Dopaminergique'),('2','type 2')], 'Récepteur dopaminergique de type 2',
              'Cible du tiapride, qui est un antagoniste D2/D3.', 'g26-tiapride')
add_if_absent('D3', [('D','Dopaminergique'),('3','type 3')], 'Récepteur dopaminergique de type 3',
              'Cible du tiapride, qui est un antagoniste D2/D3.', 'g26-tiapride')
add_if_absent('Kayser-Fleischer', [('Kayser-Fleischer','noms propres des deux médecins qui ont décrit l’anneau, non une abréviation')], 'Anneau de Kayser-Fleischer',
              'Dépôt cornéen de cuivre, quasi pathognomonique de la maladie de Wilson, surtout avec signes neurologiques.', 'g26-kf')
add_if_absent('Creutzfeldt-Jakob', [('Creutzfeldt-Jakob','noms propres des deux médecins qui ont décrit la maladie, non une abréviation')], 'Maladie de Creutzfeldt-Jakob',
              'Elle peut donner des myoclonies et des hypersignaux corticaux ou des noyaux gris, comme les encéphalites anti-LGI1 et anti-CASPR2.', 'g26-diffs')
add_if_absent('Baizabal-Carvallo', [('Baizabal-Carvallo','nom propre du premier auteur de la revue, non une abréviation')], 'Baizabal-Carvallo, premier auteur d’une revue',
              'Revue publiée en 2018 sur les mouvements anormaux auto-immuns et paranéoplasiques.', 'g26-anticorps')
