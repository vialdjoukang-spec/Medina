"""Abréviations R27 (N-05-Neurologie). Entrées conditionnelles : aucun terme existant n’est écrasé."""
import importlib
import sys
from pathlib import Path

_here = Path(__file__).resolve()
_root = next((p for p in _here.parents if (p / 'glossary' / 'cardio_1.py').exists()), None)
_existing = {}
if _root is not None:
    _gdir = str(_root / 'glossary')
    if _gdir not in sys.path:
        sys.path.insert(0, _gdir)
    for _path in sorted((_root / 'glossary').glob('*.py')):
        if _path.stem in {'r27', '__init__'}:
            continue
        try:
            _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
        except Exception:
            pass

G = {}


def _add(key, letters, full, definition, window=None):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full,
                  'def': '<p>' + definition + '</p>', 'ref': window}


# Sociétés et lignes directrices
_add('DGN', [('D', 'Deutsche'), ('G', 'Gesellschaft für'), ('N', 'Neurologie')], 'Société allemande de neurologie',
     'Société savante qui a rédigé la ligne directrice sur les ataxies de l’adulte, avec les sociétés autrichienne et suisse.', 'r27-guideline')
_add('ÖGN', [('Ö', 'Österreichische'), ('G', 'Gesellschaft für'), ('N', 'Neurologie')], 'Société autrichienne de neurologie',
     'Société savante cosignataire de la ligne directrice sur les ataxies de l’adulte (2024).', 'r27-guideline')
_add('SNG', [('S', 'Schweizerische'), ('N', 'Neurologische'), ('G', 'Gesellschaft')], 'Société suisse de neurologie',
     'Société savante suisse cosignataire de la ligne directrice allemande, autrichienne et suisse sur les ataxies de l’adulte (2024).', 'r27-guideline')
_add('EFNS', [('E', 'European'), ('F', 'Federation of'), ('N', 'Neurological'), ('S', 'Societies')], 'Fédération européenne des sociétés de neurologie',
     'Société européenne dont les recommandations sur l’encéphalopathie de Wernicke datent de 2010 ; elle est devenue l’Académie européenne de neurologie.', 'r27-wernicke')
_add('SSP', [('S', 'Situations'), ('S', 'as'), ('P', 'Starting Points')], 'Situations de départ de PROFILES',
     'Points d’entrée cliniques du catalogue d’objectifs PROFILES de l’examen fédéral ; la situation 98 couvre l’incoordination.', 'r27-ssp')
# Codes
_add('R27.0', [('R27.0', 'code CIM-10-GM 2024')], 'Ataxie, sans précision',
     'Code d’attente d’une ataxie dont la cause n’est pas établie ; remplacé dès que le diagnostic est posé.', 'r27-cim')
_add('R27.8', [('R27.8', 'code CIM-10-GM 2024')], 'Troubles de la coordination, autres et non précisés',
     'Code des signes de coordination sans ataxie nommée, dans la répartition pédagogique de ce cours.', 'r27-cim')
_add('R26.0', [('R26.0', 'code CIM-10-GM 2024')], 'Démarche ataxique',
     'Code exclu de R27 : ataxie limitée à la marche.', 'r27-cim')
_add('G23.3', [('G23.3', 'code CIM-10-GM 2024')], 'Atrophie multisystématisée de type cérébelleux',
     'Code de la MSA-C, selon les mots-clés de classification donnés par la ligne directrice.', 'r27-cim')
_add('G31.2', [('G31.2', 'code CIM-10-GM 2024')], 'Dégénérescence alcoolique du système nerveux',
     'Code de la dégénérescence cérébelleuse alcoolique, selon les mots-clés de classification donnés par la ligne directrice.', 'r27-cim')
# Syndromes, échelles, entités
_add('CANVAS', [('C', 'Cerebellar'), ('A', 'Ataxia,'), ('N', 'Neuropathy,'), ('V', 'Vestibular'), ('A', 'Areflexia'), ('S', 'Syndrome')],
     'Ataxie cérébelleuse, neuropathie, aréflexie vestibulaire',
     'Syndrome qui associe les trois sources d’ataxie (cervelet, proprioception, vestibule) ; lié à une expansion biallélique du gène RFC1.', 'r27-canvas')
_add('MSA-C', [('MSA', 'Multiple System Atrophy (atrophie multisystématisée)'), ('C', 'Cerebellar (de type cérébelleux)')],
     'Atrophie multisystématisée de type cérébelleux',
     'Maladie dégénérative sporadique associant dysautonomie et syndrome cérébelleux, avec début après 30 ans ; code G23.3.', 'r27-msa')
_add('SAOA', [('S', 'Sporadic'), ('A', 'Adult-'), ('O', 'Onset'), ('A', 'Ataxia')], 'Ataxie sporadique de l’adulte d’étiologie inconnue',
     'Diagnostic d’exclusion : ataxie sporadique sans critère de MSA-C après exclusion des causes acquises et génétiques ; pronostic meilleur que celui de la MSA-C.', 'r27-saoa')
_add('FXTAS', [('FX', 'Fragile X (X fragile)'), ('TAS', 'Tremor/Ataxia Syndrome (syndrome tremblement-ataxie)')],
     'Syndrome tremblement-ataxie associé à l’X fragile',
     'Ataxie progressive avec tremblement d’action chez les porteurs d’une prémutation FMR1 (55 à 200 répétitions CGG).', 'r27-fxtas')
_add('ACD', [('A', 'Alcoholic'), ('C', 'Cerebellar'), ('D', 'Degeneration')], 'Dégénérescence cérébelleuse alcoolique',
     'Atteinte cérébelleuse liée à la carence en thiamine et à la toxicité de l’alcool ; traitée par l’abstinence et la thiamine.', 'r27-acd')
_add('SARA', [('S', 'Scale for the'), ('A', 'Assessment and'), ('R', 'Rating'), ('A', 'of Ataxia')], 'Échelle d’évaluation et de cotation de l’ataxie',
     'Échelle clinique à 8 items (marche, station, position assise, parole, quatre épreuves des membres) ; fiabilité inter-évaluateurs 0,98.', 'r27-sara')
_add('GTI', [('G', 'Graded'), ('T', 'Truncal'), ('I', 'Instability')], 'Instabilité tronculaire graduée',
     'Grade 2 : marche autonome impossible ; grade 3 : station ou position assise impossible sans aide. Le grade 3 est très spécifique d’un accident vasculaire.', 'r27-gti')
_add('mFARS', [('m', 'modified'), ('F', 'Friedreich'), ('A', 'Ataxia'), ('R', 'Rating'), ('S', 'Scale')], 'Échelle modifiée d’évaluation de l’ataxie de Friedreich',
     'Critère d’évaluation de l’étude 1 de l’omavéloxolone : différence de −2,41 contre placebo à 48 semaines.', 'r27-skyclarys')
_add('EDSS', [('E', 'Expanded'), ('D', 'Disability'), ('S', 'Status'), ('S', 'Scale')], 'Échelle étendue d’incapacité',
     'Échelle de handicap de la sclérose en plaques ; l’indication suisse de la fampridine vise un score de 4,0 à 7,0.', 'r27-fampridine')
_add('AVED', [('A', 'Ataxia with'), ('V', 'Vitamin'), ('E', 'E'), ('D', 'Deficiency')], 'Ataxie avec déficit en vitamine E',
     'Ataxie génétique traitée par la vitamine E (800 à 2000 mg/jour selon la ligne directrice).', 'r27-rares')
_add('CPV', [('C', 'Cervelet'), ('P', 'Proprioception'), ('V', 'Vestibule')], 'Aide pédagogique : cervelet, proprioception, vestibule',
     'Moyen mnémotechnique des trois entrées de l’équilibre ; aide pédagogique, non critère officiel.', 'r27-mnemo')
# Artères
_add('PICA', [('P', 'Posterior'), ('I', 'Inferior'), ('C', 'Cerebellar'), ('A', 'Artery')], 'Artère cérébelleuse postéro-inférieure',
     'Sa partie médiale donne un vertige aigu et une ataxie du tronc ; sa partie latérale une instabilité et une dysmétrie sans dysarthrie.', 'r27-pica')
_add('AICA', [('A', 'Anterior'), ('I', 'Inferior'), ('C', 'Cerebellar'), ('A', 'Artery')], 'Artère cérébelleuse antéro-inférieure',
     'Son infarctus donne une ataxie des membres et du tronc avec signes latéro-pontiques.', 'r27-pica')
# Gènes et répétitions
_add('RFC1', [('RFC', 'Replication Factor C'), ('1', 'sous-unité 1')], 'Gène RFC1',
     'Une expansion biallélique d’une répétition intronique de ce gène cause le CANVAS ; 0,7 % des Européens en sont porteurs.', 'r27-canvas')
_add('FXN', [('FXN', 'symbole du gène de la frataxine')], 'Gène FXN',
     'Gène touché dans l’ataxie de Friedreich par une expansion GAA biallélique dans l’intron 1.', 'r27-friedreich')
_add('FMR1', [('FMR', 'Fragile X Messenger Ribonucleoprotein'), ('1', 'numéro 1')], 'Gène FMR1',
     'Une prémutation de 55 à 200 répétitions CGG de ce gène cause le FXTAS.', 'r27-fxtas')
_add('KCNA1', [('KCN', 'Potassium voltage-gated Channel'), ('A1', 'sous-famille A, membre 1')], 'Gène du canal potassique KCNA1',
     'Gène touché dans l’ataxie épisodique de type 1.', 'r27-ea')
_add('CACNA1A', [('CACN', 'Calcium voltage-gated Channel'), ('A1A', 'sous-unité alpha 1 A')], 'Gène du canal calcique CACNA1A',
     'Gène touché dans l’ataxie épisodique de type 2.', 'r27-ea')
_add('POLG', [('POL', 'Polymérase'), ('G', 'gamma')], 'Gène POLG',
     'Gène de la polymérase gamma mitochondriale ; en cas d’ataxie liée à POLG, le valproate et le propofol sont à éviter.', 'r27-rares')
_add('SPG7', [('SPG', 'Spastic Paraplegia (paraplégie spastique)'), ('7', 'type 7')], 'Paraplégie spastique de type 7',
     'Forme associant spasticité et ataxie, avec hypersignal des noyaux dentelés à l’IRM.', 'r27-irm')
_add('ARSACS', [('A', 'Autosomal'), ('R', 'Recessive'), ('S', 'Spastic'), ('A', 'Ataxia of'), ('C', 'Charlevoix-'), ('S', 'Saguenay')],
     'Ataxie spastique récessive autosomique de Charlevoix-Saguenay',
     'Forme associant spasticité et ataxie, avec stries pontiques hypo-intenses à l’IRM.', 'r27-irm')
_add('COQ8A', [('COQ', 'Coenzyme Q'), ('8A', 'gène 8A')], 'Gène COQ8A',
     'Ataxie traitée par le coenzyme Q10 (20 à 30 mg/kg/jour selon la ligne directrice).', 'r27-rares')
_add('GAA', [('G', 'Guanine'), ('A', 'Adénine'), ('A', 'Adénine')], 'Triplet GAA',
     'Triplet dont l’expansion biallélique dans le gène FXN cause l’ataxie de Friedreich.', 'r27-friedreich')
_add('CAG', [('C', 'Cytosine'), ('A', 'Adénine'), ('G', 'Guanine')], 'Triplet CAG',
     'Triplet dont l’expansion traduite caractérise plusieurs ataxies spinocérébelleuses à progression nette.', 'r27-sca')
_add('CGG', [('C', 'Cytosine'), ('G', 'Guanine'), ('G', 'Guanine')], 'Triplet CGG',
     'Triplet dont 55 à 200 répétitions dans FMR1 définissent la prémutation du FXTAS.', 'r27-fxtas')
# Anticorps, noms propres, chimie
_add('IgLON5', [('Ig', 'Immunoglobuline (superfamille)'), ('LON', 'LAMP, OBCAM, Neurotrimin'), ('5', 'cinquième membre')], 'Protéine IgLON5',
     'Cible d’un anticorps associé à des troubles du sommeil et à un stridor.', 'r27-immune')
_add('DPPX', [('DPPX', 'sigle de la protéine « dipeptidyl-peptidase-like », non développé lettre à lettre dans la source lue')], 'Protéine DPPX',
     'Cible d’un anticorps associé à une diarrhée chronique et à une ataxie.', 'r27-immune')
_add('GQ1b', [('GQ1b', 'désignation d’un ganglioside neuronal, code de nomenclature non développé lettre à lettre')], 'Ganglioside GQ1b',
     'Cible de l’anticorps du syndrome de Miller Fisher (ophtalmoplégie, aréflexie, ataxie).', 'r27-immune')
_add('GFAP', [('G', 'Glial'), ('F', 'Fibrillary'), ('A', 'Acidic'), ('P', 'Protein')], 'Protéine acide fibrillaire gliale',
     'Cible d’un anticorps associé à une prise de contraste radiaire périventriculaire ou cérébelleuse.', 'r27-irm')
_add('Niemann-Pick', [('Niemann-Pick', 'noms propres des deux médecins ayant décrit la maladie')], 'Maladie de Niemann-Pick',
     'Maladie de surcharge ; le type C associe ataxie et paralysie verticale du regard, avec oxystérols augmentés ; traitement par le miglustat.', 'r27-rares')
_add('Creutzfeldt-Jakob', [('Creutzfeldt-Jakob', 'noms propres des deux neurologues ayant décrit la maladie')], 'Maladie de Creutzfeldt-Jakob',
     'Maladie à progression en semaines à mois, avec hypersignal en diffusion à l’IRM.', 'r27-irm')
_add('DL', [('D', 'Dextrogyre'), ('L', 'Lévogyre')], 'Mélange des formes D et L',
     'Préfixe chimique des mélanges des deux formes d’une molécule, comme l’acétyl-DL-leucine, non recommandée dans l’ataxie.', 'r27-rehab')
