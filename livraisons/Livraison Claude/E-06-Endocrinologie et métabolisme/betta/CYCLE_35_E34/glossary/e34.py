"""Abréviations E34 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'e34', '__init__'}:
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

add_if_absent('ENETS', [('E', 'European'), ('NE', 'NeuroEndocrine'), ('T', 'Tumor'), ('S', 'Society')],
              'European NeuroEndocrine Tumor Society',
              'Cette société européenne publie les recommandations de référence sur les tumeurs neuroendocrines. Sa recommandation de 2022 sur le syndrome carcinoïde est la source principale de ce cours.', 'e34-carcinoide')
add_if_absent('XY', [('X', 'chromosome sexuel X'), ('Y', 'chromosome sexuel Y')],
              'Formule chromosomique masculine, 46,XY',
              'Elle désigne un caryotype avec un chromosome X et un chromosome Y. L’insensibilité aux androgènes survient chez des personnes 46,XY.', 'e34-ais')
add_if_absent('XYY', [('X', 'chromosome sexuel X'), ('YY', 'deux chromosomes sexuels Y')],
              'Caryotype 47,XYY', 'Anomalie du nombre de chromosomes sexuels citée parmi les causes de haute taille.', 'e34-petite-taille')
add_if_absent('XXX', [('XXX', 'trois chromosomes sexuels X')],
              'Caryotype 47,XXX', 'Anomalie du nombre de chromosomes sexuels citée parmi les causes de haute taille.', 'e34-petite-taille')
add_if_absent('5-HIAA', [('5', 'cinq'), ('H', 'Hydroxy'), ('IAA', 'Indole Acetic Acid (indole acétique)')],
              'Acide 5-hydroxyindolacétique',
              'Métabolite urinaire de la sérotonine. Son dosage sur 24 heures confirme le syndrome carcinoïde et sert au suivi.', 'e34-5hiaa')
add_if_absent('TNE', [('T', 'Tumeur'), ('NE', 'NeuroEndocrine')], 'Tumeur neuroendocrine',
              'Tumeur développée à partir de cellules neuroendocrines, souvent intestinale ou pulmonaire, parfois fonctionnelle.', 'e34-tne')
add_if_absent('Hutchinson-Gilford', [('Hutchinson-Gilford', 'noms propres des auteurs, non une abréviation')],
              'Progéria de Hutchinson-Gilford', 'Syndrome de vieillissement accéléré dû à une mutation du gène LMNA.', 'e34-progerine')
add_if_absent('Silver-Russell', [('Silver-Russell', 'noms propres des auteurs, non une abréviation')],
              'Syndrome de Silver-Russell', 'Syndrome de petite taille d’origine anténatale, exclu de la rubrique E34.', 'e34-petite-taille')
add_if_absent('Prader-Willi', [('Prader-Willi', 'noms propres des auteurs, non une abréviation')],
              'Syndrome de Prader-Willi', 'Syndrome génétique cité parmi les causes de petite taille et parmi les indications suisses de la somatropine.', 'e34-genotropin')
add_if_absent('Beckwith-Wiedemann', [('Beckwith-Wiedemann', 'noms propres des auteurs, non une abréviation')],
              'Syndrome de Beckwith-Wiedemann', 'Syndrome cité parmi les causes de haute taille.', 'e34-petite-taille')
add_if_absent('Mayer-Rokitansky-Küster-Hauser', [('Mayer-Rokitansky-Küster-Hauser', 'noms propres des auteurs, non une abréviation')],
              'Syndrome de Mayer-Rokitansky-Küster-Hauser', 'Aplasie utéro-vaginale, première cause d’aplasie vaginale, avant l’insensibilité complète aux androgènes.', 'e34-ais')
add_if_absent('SwissNET', [('SwissNET', 'nom propre du réseau suisse des tumeurs neuroendocrines, non développé dans le document lu')],
              'SwissNET, brochure suisse sur les tumeurs neuroendocrines',
              'La brochure de 2019 fournit les données suisses d’incidence. Elle est financée par l’industrie, ce qui en limite la valeur de référence.', 'e34-tne')
add_if_absent('E20.1', [('E20.1', 'code de la CIM-10-GM : pseudohypoparathyroïdisme, exclu de la rubrique E34')],
              'Code E20.1', 'Rubrique de la classification vers laquelle est orienté le pseudohypoparathyroïdisme.', 'e34-cim')
add_if_absent('E23.0', [('E23.0', 'code de la CIM-10-GM : nanisme hypophysaire, exclu de la petite taille de E34')],
              'Code E23.0', 'Rubrique de la classification vers laquelle est orienté le nanisme hypophysaire.', 'e34-cim')
add_if_absent('Q77.4', [('Q77.4', 'code de la CIM-10-GM : achondroplasie et hypochondroplasie, exclues de E34')],
              'Code Q77.4', 'Rubrique de la classification vers laquelle est orientée la petite taille achondroplasique ou hypochondroplasique.', 'e34-cim')
add_if_absent('N25.0', [('N25.0', 'code de la CIM-10-GM : petite taille d’origine rénale, exclue de E34')],
              'Code N25.0', 'Rubrique de la classification vers laquelle est orientée la petite taille rénale.', 'e34-cim')
add_if_absent('D82.2', [('D82.2', 'code de la CIM-10-GM : petite taille avec déficit immunitaire, exclue de E34')],
              'Code D82.2', 'Rubrique de la classification vers laquelle est orientée la petite taille avec déficit immunitaire.', 'e34-cim')
add_if_absent('Q87.1', [('Q87.1', 'code de la CIM-10-GM : syndromes malformatifs avec petite taille, dont le syndrome de Silver-Russell')],
              'Code Q87.1', 'Rubrique de la classification vers laquelle est orienté le syndrome de Silver-Russell.', 'e34-cim')
add_if_absent('E16.3', [('E16.3', 'code de la CIM-10-GM : hypersécrétion de glucagon')],
              'Code E16.3', 'Rubrique de la classification qui reçoit le glucagonome d’origine pancréatique.', 'e34-glucagonome')
add_if_absent('E16.4', [('E16.4', 'code de la CIM-10-GM : hypersécrétion de gastrine')],
              'Code E16.4', 'Rubrique de la classification qui reçoit le gastrinome d’origine pancréatique.', 'e34-gastrinome')
add_if_absent('E16.8', [('E16.8', 'code de la CIM-10-GM : autres anomalies de la sécrétion pancréatique interne, dont VIP, somatostatine et GHRH')],
              'Code E16.8', 'Rubrique de la classification qui reçoit le VIPome, le somatostatinome et le GHRHome pancréatiques.', 'e34-vipome')
add_if_absent('E34.1', [('E34.1', 'code de la CIM-10-GM : autres hypersécrétions d’hormones intestinales')],
              'Code E34.1', 'Rubrique visant l’origine intestinale non pancréatique, sur laquelle les sources lues ne donnent pas de détail.', 'e34-ectopique')
add_if_absent('GHRH', [('G', 'Growth'), ('H', 'Hormone'), ('R', 'Releasing'), ('H', 'Hormone')],
              'Growth Hormone-Releasing Hormone', 'Hormone hypothalamique qui stimule la sécrétion d’hormone de croissance. Une tumeur peut la sécréter de façon ectopique et provoquer une acromégalie.', 'e34-ectopique')
add_if_absent('GHRHome', [('GHRH', 'Growth Hormone-Releasing Hormone'), ('ome', 'tumeur sécrétant cette hormone')],
              'Tumeur sécrétant la GHRH', 'Syndrome fonctionnel rare d’une tumeur neuroendocrine pancréatique.', 'e34-ectopique')
add_if_absent('ACTHome', [('ACTH', 'Adreno-Cortico-Tropic Hormone'), ('ome', 'tumeur sécrétant cette hormone')],
              'Tumeur sécrétant l’ACTH', 'Syndrome fonctionnel d’une tumeur neuroendocrine pancréatique, source d’un syndrome de Cushing.', 'e34-acth')
add_if_absent('PTHrPome', [('PTHrP', 'Parathyroid Hormone-related Peptide'), ('ome', 'tumeur sécrétant ce peptide')],
              'Tumeur sécrétant la PTHrP', 'Syndrome fonctionnel d’une tumeur neuroendocrine pancréatique.', 'e34-ectopique')
add_if_absent('VIP', [('V', 'Vasoactive'), ('I', 'Intestinal'), ('P', 'Peptide')],
              'Vasoactive Intestinal Peptide', 'Peptide sécrété en excès dans le VIPome, qui provoque une diarrhée aqueuse massive.', 'e34-vipome')
add_if_absent('VIPome', [('VIP', 'Vasoactive Intestinal Peptide'), ('ome', 'tumeur sécrétant ce peptide')],
              'Tumeur sécrétant le VIP', 'Tumeur très rare, souvent pancréatique, responsable d’une diarrhée aqueuse massive.', 'e34-vipome')
add_if_absent('VIPomes', [('VIP', 'Vasoactive Intestinal Peptide'), ('omes', 'tumeurs sécrétant ce peptide')],
              'Tumeurs sécrétant le VIP', 'Pluriel de VIPome ; voir la fenêtre correspondante.', 'e34-vipome')
add_if_absent('ADH', [('A', 'Anti'), ('D', 'Diurétique'), ('H', 'Hormone')],
              'Hormone antidiurétique', 'Sécrétée de façon ectopique, elle provoque une antidiurèse inappropriée avec hyponatrémie.', 'e34-ectopique')
add_if_absent('CRH', [('C', 'Corticotropin'), ('R', 'Releasing'), ('H', 'Hormone')],
              'Corticotropin-Releasing Hormone', 'Hormone hypothalamique qui stimule la sécrétion d’ACTH ; sa sécrétion ectopique est très rare.', 'e34-ectopique')
add_if_absent('IGF-1', [('I', 'Insulin-like'), ('G', 'Growth'), ('F', 'Factor'), ('1', 'type 1')],
              'Insulin-like Growth Factor 1', 'Facteur de croissance produit sous l’effet de l’hormone de croissance. Il est effondré dans le syndrome de Laron.', 'e34-laron')
add_if_absent('IGFBP-3', [('I', 'Insulin-like'), ('G', 'Growth'), ('F', 'Factor'), ('B', 'Binding'), ('P', 'Protein'), ('3', 'type 3')],
              'Insulin-like Growth Factor Binding Protein 3', 'Protéine porteuse de l’IGF-1, dosée avec lui dans le bilan de la croissance.', 'e34-laron')
add_if_absent('DHT', [('D', 'Di'), ('H', 'Hydro'), ('T', 'Testostérone')],
              'Dihydrotestostérone', 'Androgène issu de la testostérone par la 5α-réductase de type 2 ; il masculinise les organes génitaux externes.', 'e34-ar-dht')
add_if_absent('LH', [('L', 'Luteinizing'), ('H', 'Hormone')], 'Hormone lutéinisante',
              'Hormone hypophysaire qui stimule la production de testostérone ; elle est élevée dans l’insensibilité aux androgènes.', 'e34-ais')
add_if_absent('FSH', [('F', 'Follicle'), ('S', 'Stimulating'), ('H', 'Hormone')], 'Hormone folliculo-stimulante',
              'Hormone hypophysaire des gonades ; elle est normale dans l’insensibilité aux androgènes.', 'e34-ais')
add_if_absent('AMH', [('A', 'Anti'), ('M', 'Müllerian'), ('H', 'Hormone')], 'Hormone anti-müllérienne',
              'Hormone testiculaire qui fait régresser les dérivés de Müller. Normale ou élevée dans l’insensibilité aux androgènes.', 'e34-ais')
add_if_absent('hCG', [('h', 'human'), ('C', 'Chorionic'), ('G', 'Gonadotropin')], 'Gonadotrophine chorionique humaine',
              'Elle sert à un test de stimulation testiculaire dans l’enfance pour explorer les variantes du développement sexuel.', 'e34-ais')
add_if_absent('fT3', [('f', 'free'), ('T3', 'triiodothyronine')], 'Triiodothyronine libre', 'Hormone thyroïdienne dosée dans le bilan de la haute taille.', 'e34-agedosseux')
add_if_absent('fT4', [('f', 'free'), ('T4', 'thyroxine')], 'Thyroxine libre', 'Hormone thyroïdienne dosée avec la TSH dans le bilan de la petite et de la haute taille.', 'e34-agedosseux')
add_if_absent('GT', [('γ', 'gamma'), ('G', 'Glutamyl'), ('T', 'Transférase')], 'Gamma-glutamyl-transférase',
              'Enzyme hépatique dosée dans le bilan de dépistage d’une petite taille.', 'e34-genetique')
add_if_absent('POR', [('P', 'P450'), ('O', 'Oxydo'), ('R', 'Réductase')], 'P450 oxydoréductase',
              'Enzyme dont le déficit figure dans le diagnostic différentiel des formes partielles d’insensibilité aux androgènes.', 'e34-ais')
add_if_absent('HSD3', [('HSD', 'Hydroxy-Stéroïde Déshydrogénase'), ('3', 'type 3')], '17β-hydroxystéroïde déshydrogénase de type 3',
              'Enzyme dont le déficit figure dans le diagnostic différentiel des formes partielles d’insensibilité aux androgènes.', 'e34-ais')
add_if_absent('177Lu-DOTATATE', [('177Lu', 'lutétium 177'), ('DOTATATE', 'DOTA-octréotate, analogue de la somatostatine marqué')],
              'Lutétium 177-DOTATATE', 'Médicament de radiothérapie interne vectorisée ciblant les récepteurs de la somatostatine.', 'e34-prrt')
add_if_absent('SHOX', [('SHOX', 'gène à homéobox de la petite taille (Short stature HOmeoboX)')], 'Gène SHOX',
              'Gène dont l’anomalie entraîne une petite taille ; la somatropine est utilisée en Suisse pour cette indication.', 'e34-genotropin')
add_if_absent('ACAN', [('ACAN', 'gène de l’aggrécane')], 'Gène ACAN',
              'Gène dont la mutation n’ouvre pas droit au remboursement de l’hormone de croissance selon l’article suisse lu.', 'e34-genotropin')
add_if_absent('CNE', [('C', 'Commission'), ('N', 'Nationale'), ('E', 'd’Éthique')], 'Commission nationale d’éthique',
              'Cette commission suisse a publié en 2012 l’avis 20/2012 sur la prise en charge des variantes du développement sexuel.', 'e34-cne')
add_if_absent('NAD', [('N', 'Nicotinamide'), ('A', 'Adénine'), ('D', 'Dinucléotide')], 'Nicotinamide adénine dinucléotide',
              'Cofacteur dérivé de la niacine ; son rapport avec sa forme phosphorylée mesure la déplétion en niacine.', 'e34-niacine')
add_if_absent('NADP', [('N', 'Nicotinamide'), ('A', 'Adénine'), ('D', 'Dinucléotide'), ('P', 'Phosphate')], 'Nicotinamide adénine dinucléotide phosphate',
              'Forme phosphorylée du NAD ; l’index NAD/NADP sert à mesurer la déplétion en niacine.', 'e34-niacine')
add_if_absent('TPH', [('TP', 'TryPtophane'), ('H', 'Hydroxylase')], 'Tryptophane hydroxylase',
              'Enzyme limitante de la synthèse de sérotonine, inhibée par le télotristat.', 'e34-voie-serotonine')
add_if_absent('TPH1', [('TPH', 'Tryptophane Hydroxylase'), ('1', 'type 1, isoforme périphérique')], 'Tryptophane hydroxylase de type 1',
              'Isoforme périphérique de l’enzyme limitante de la synthèse de sérotonine.', 'e34-voie-serotonine')
