"""G09 : définitions locales, sans modifier les glossaires tiers."""
from pathlib import Path
import importlib
_existing={}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'g09','__init__'}: continue
    try: _existing.update(getattr(importlib.import_module(_path.stem),'G',{}))
    except Exception: pass
G={}
def add_if_absent(key,letters,full,definition,window=None):
    if key not in _existing:
        G[key]={'lit':[list(x) for x in letters],'full':full,'def':'<p>'+definition+'</p>','ref':window}
add_if_absent('G09',[('G09', 'Catégorie CIM-10-GM suisse')],'Séquelles d’affections inflammatoires du système nerveux central','La note OFS vise des états initialement G00–G08 hors catégories astérisque. Aucun délai obligatoire d’un an si la séquelle est déjà précisée ; B94.1 et B90.0 restent distincts.','g09-exp-1')
add_if_absent('SV2A',[('SV', 'Synaptic Vesicle (vésicule synaptique)'), ('2A', 'protéine 2A')],'Protéine vésiculaire synaptique 2A','Site de liaison du lévétiracétam décrit dans sa FI comme pouvant contribuer à son action ; mécanisme non entièrement élucidé. Aucune localisation moléculaire n’est déduite des planches anatomiques.',None)
add_if_absent('GABAB',[('GABA', 'Acide gamma-aminobutyrique'), ('B', 'type de récepteur')],'Récepteur GABA de type B','Cible du baclofène décrite dans la FI, notamment au niveau médullaire. Une cible ne suffit pas à établir une indication pour toute séquelle cérébrale.','g09-cas-4')
add_if_absent('NMDAr',[('NMDA', 'N-méthyl-D-aspartate'), ('r', 'récepteur')],'Récepteur NMDA','Récepteur neuronal ciblé dans l’encéphalite anti-NMDAr. Le mécanisme et le syndrome clinique doivent être distingués d’une positivité isolée d’anticorps.','g09-cas-3')
add_if_absent('NICE',[('N', 'National'), ('I', 'Institute for'), ('C', 'Health and Care'), ('E', 'Excellence')],'National Institute for Health and Care Excellence','NG240 donne ici des recommandations britanniques de suivi après méningite bactérienne ou maladie méningococcique, avec population et horloges précisées.','g09-calcul-delais')
add_if_absent('CEN',[('C', 'Collège des'), ('E', 'Enseignants de'), ('N', 'Neurologie')],'Collège des enseignants de neurologie','Source universitaire française de sémiologie analytique, employée pour localisation et examen, sans donner un diagnostic causal à elle seule.',None)
add_if_absent('GTIN',[('G', 'Global'), ('T', 'Trade'), ('I', 'Item'), ('N', 'Number')],'Identifiant international d’article','Identifie ici la présentation dont la FI suisse exacte a été consultée. Il ne remplace ni version du texte ni vérification du produit accessible.',None)
