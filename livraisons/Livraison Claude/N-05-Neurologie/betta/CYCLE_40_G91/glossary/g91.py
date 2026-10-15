"""Abréviations G91 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'g91', '__init__'}:
        continue
    _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
G = {}
def add_if_absent(key, letters, full, definition, window):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full,
                  'def': '<p>' + definition + '</p>', 'ref': window}
add_if_absent('iNPH', [('i', 'idiopathic (idiopathique)'), ('N', 'Normal (normale)'), ('P', 'Pressure (pression)'), ('H', 'Hydrocephalus (hydrocéphalie)')],
              'Hydrocéphalie à pression normale idiopathique',
              'Trouble de la résorption du LCS du sujet âgé, sans cause antérieure identifiée, qui associe troubles de la marche, de la cognition et de la vessie. Son diagnostic final dépend de la réponse à la dérivation.', 'g91-inph')
add_if_absent('LCS', [('L', 'Liquide'), ('C', 'Cérébro'), ('S', 'Spinal')],
              'Liquide cérébrospinal',
              'Liquide sécrété en continu par les plexus choroïdes. Il circule dans les ventricules et l’espace sous-arachnoïdien avant d’être résorbé.', 'g91-lcs')
add_if_absent('DESH', [('D', 'Disproportionately (disproportionnellement)'), ('E', 'Enlarged (élargi)'), ('S', 'Subarachnoid-space (espace sous-arachnoïdien)'), ('H', 'Hydrocephalus (hydrocéphalie)')],
              'Hydrocéphalie avec espaces sous-arachnoïdiens disproportionnés',
              'Aspect d’imagerie : ventricules dilatés, vallées sylviennes dilatées et espaces sous-arachnoïdiens de haute convexité étroits.', 'g91-evans')
add_if_absent('LOVA', [('L', 'Long-standing (longtemps évolutive)'), ('O', 'Overt (manifeste)'), ('V', 'Ventriculomegaly (ventriculomégalie)'), ('A', 'in Adults (de l’adulte)')],
              'Ventriculomégalie manifeste longtemps évolutive de l’adulte',
              'Forme congénitale ou développementale, en général non communicante par sténose de l’aqueduc.', 'g91-class')
add_if_absent('PaVM', [('PaVM', 'terme de la classification japonaise ; développement non lu dans le dossier')],
              'PaVM',
              'Entité citée par la classification japonaise avec la LOVA ; le dossier ne la développe pas.', 'g91-class')
add_if_absent('CHiA', [('C', 'Chronic (chronique)'), ('H', 'Hydrocephalus (hydrocéphalie)'), ('i', 'in (de)'), ('A', 'Adults (adultes)')],
              'Hydrocéphalie chronique de l’adulte',
              'Cadre d’une revue systématique avec consensus Delphi regroupant 48 termes en sept entités.', 'g91-chia')
add_if_absent('AVIM', [('A', 'Asymptomatic (asymptomatique)'), ('V', 'Ventriculomegaly (ventriculomégalie)'), ('I', 'features of iNPH (aspect d’iNPH)'), ('M', 'on MRI (à l’IRM)')],
              'Ventriculomégalie asymptomatique d’aspect IRM d’iNPH',
              'Elle peut évoluer vers l’iNPH symptomatique.', 'g91-avim')
add_if_absent('EANS', [('E', 'European'), ('A', 'Association'), ('N', 'of Neurosurgical'), ('S', 'Societies')],
              'Association européenne des sociétés de neurochirurgie',
              'Coauteur de la recommandation européenne 2026 sur l’hémorragie sous-arachnoïdienne.', 'g91-hsa')
add_if_absent('ESMINT', [('ES', 'European Society'), ('M', 'of Minimally'), ('IN', 'Invasive'), ('T', 'Neurological Therapy')],
              'Société européenne de thérapie neurologique mini-invasive',
              'Coauteur de la recommandation européenne 2026 sur l’hémorragie sous-arachnoïdienne.', 'g91-hsa')
add_if_absent('HSA', [('H', 'Hémorragie'), ('S', 'Sous-'), ('A', 'Arachnoïdienne')],
              'Hémorragie sous-arachnoïdienne',
              'Saignement dans l’espace sous-arachnoïdien ; l’hydrocéphalie complique environ un quart des formes anévrismales.', 'g91-hsa')
add_if_absent('mmH2O', [('mm', 'millimètre'), ('H2O', 'eau (formule chimique)')],
              'Millimètre d’eau',
              'Unité de pression du LCS ; 200 mmH2O est le seuil des critères japonais.', 'g91-crit')
add_if_absent('cmH2O', [('cm', 'centimètre'), ('H2O', 'eau (formule chimique)')],
              'Centimètre d’eau',
              'Unité de pression de réglage des valves.', 'g91-typederiv')
add_if_absent('ETV', [('E', 'Endoscopic (endoscopique)'), ('T', 'Third (troisième)'), ('V', 'Ventriculostomy (ventriculostomie)')],
              'Ventriculocisternostomie endoscopique',
              'Perforation endoscopique du plancher du 3e ventricule qui crée une voie de dérivation du LCS.', 'g91-etv')
add_if_absent('CPC', [('C', 'Choroid (choroïdien)'), ('P', 'Plexus'), ('C', 'Cauterization (cautérisation)')],
              'Cautérisation des plexus choroïdes',
              'Geste associé à l’ETV chez l’enfant de moins de 2 ans.', 'g91-etv')
add_if_absent('ETV-CPC', [('ETV', 'Endoscopic Third Ventriculostomy'), ('CPC', 'Choroid Plexus Cauterization')],
              'ETV avec cautérisation des plexus choroïdes',
              'Option pédiatrique des causes obstructives, surtout avant 2 ans.', 'g91-pedchir')
add_if_absent('VA', [('V', 'Ventriculo'), ('A', 'Atriale')],
              'Dérivation ventriculo-atriale',
              'Le LCS est dérivé vers l’atrium.', 'g91-typederiv')
add_if_absent('LP', [('L', 'Lombo'), ('P', 'Péritonéale')],
              'Dérivation lombo-péritonéale',
              'Le LCS est dérivé du cul-de-sac lombaire vers le péritoine.', 'g91-typederiv')
add_if_absent('PENS', [('PENS', 'nom de l’essai randomisé ; développement non lu dans le dossier')],
              'Essai PENS',
              'Essai randomisé nord-américain de dérivation dans l’iNPH.', 'g91-pens')
add_if_absent('BASICS', [('BASICS', 'nom de l’essai britannique ; développement non lu dans le dossier')],
              'Essai BASICS',
              'Essai randomisé de cathéters de dérivation.', 'g91-basics')
add_if_absent('ULTRA', [('ULTRA', 'nom de l’essai sur l’acide tranexamique ; développement non lu dans le dossier')],
              'Essai ULTRA',
              'Essai cité par la recommandation européenne.', 'g91-mtranex')
add_if_absent('SINPHONI', [('SINPHONI', 'nom d’étude japonaise ; développement non lu dans le dossier')],
              'Étude SINPHONI',
              'Étude citée par la ligne directrice japonaise pour l’index d’Evans moyen.', 'g91-evans')
add_if_absent('Eu-iNPH', [('Eu', 'European (européenne)'), ('iNPH', 'Idiopathic Normal Pressure Hydrocephalus')],
              'Étude multicentrique européenne sur l’iNPH',
              'Étude de 142 patients dans 13 centres.', 'g91-euinph')
add_if_absent('TUG', [('T', 'Timed (chronométré)'), ('U', 'Up'), ('G', 'and Go')],
              'Test chronométré « se lever et marcher »',
              'Test de marche courte utilisé pour objectiver le gain après soustraction.', 'g91-marche')
add_if_absent('MMSE', [('M', 'Mini'), ('M', 'Mental'), ('S', 'State'), ('E', 'Examination')],
              'Mini-examen de l’état mental',
              'Test cognitif global.', 'g91-echelles')
add_if_absent('FAB', [('F', 'Frontal'), ('A', 'Assessment'), ('B', 'Battery')],
              'Batterie rapide d’évaluation frontale',
              'Test des fonctions exécutives.', 'g91-echelles')
add_if_absent('WAIS-III', [('W', 'Wechsler'), ('A', 'Adult'), ('I', 'Intelligence'), ('S', 'Scale'), ('III', 'troisième édition')],
              'Échelle d’intelligence de Wechsler pour adultes, 3e édition',
              'Les codes et symboles évaluent la vitesse de traitement.', 'g91-echelles')
add_if_absent('RAVLT', [('R', 'Rey'), ('A', 'Auditory'), ('V', 'Verbal'), ('L', 'Learning'), ('T', 'Test')],
              'Test d’apprentissage auditivo-verbal de Rey',
              'Test de mémoire verbale.', 'g91-echelles')
add_if_absent('MoCA', [('Mo', 'Montreal'), ('C', 'Cognitive'), ('A', 'Assessment')],
              'Évaluation cognitive de Montréal',
              'Test de dépistage cognitif.', 'g91-pens')
add_if_absent('mRS', [('m', 'modified (modifiée)'), ('R', 'Rankin'), ('S', 'Scale')],
              'Échelle de Rankin modifiée',
              'Score de handicap fonctionnel de 0 à 6.', 'g91-euinph')
add_if_absent('iNPHGS', [('iNPH', 'Idiopathic Normal Pressure Hydrocephalus'), ('G', 'Grading'), ('S', 'Scale')],
              'Échelle de cotation de l’iNPH',
              'Trois domaines — marche, démence, incontinence — cotés de 0 à 4.', 'g91-echelles')
add_if_absent('CT', [('C', 'Computed (assisté par ordinateur)'), ('T', 'Tomography (tomographie)')],
              'Tomodensitométrie',
              'Examen d’imagerie, ici avec perfusion en cas d’aggravation après hémorragie.', 'g91-hsa')
add_if_absent('NKCC1', [('Na', 'Sodium'), ('K', 'Potassium'), ('Cl', 'Chlorure'), ('C', 'Cotransporteur'), ('1', 'numéro 1')],
              'Cotransporteur sodium-potassium-chlorure 1',
              'Il assure environ la moitié de la sécrétion de LCS chez l’animal.', 'g91-lcs')
add_if_absent('HCO3', [('H', 'Hydrogène'), ('C', 'Carbone'), ('O3', 'trois atomes d’oxygène')],
              'Bicarbonate',
              'Anion transporté par l’épithélium choroïdien.', 'g91-lcs')
add_if_absent('QALY', [('Q', 'Quality'), ('A', 'Adjusted'), ('L', 'Life'), ('Y', 'Year')],
              'Année de vie ajustée sur la qualité',
              'Mesure d’efficience.', 'g91-pronostic')
add_if_absent('OR', [('O', 'Odds'), ('R', 'Ratio')],
              'Rapport de cotes',
              'Mesure d’association utilisée dans l’essai ULTRA.', 'g91-mtranex')
add_if_absent('IC95', [('IC', 'Intervalle de Confiance'), ('95', 'à 95 %')],
              'Intervalle de confiance à 95 %',
              'Plage de valeurs compatibles avec les données.', 'g91-pens')
add_if_absent('PEAG', [('P', 'Pustulose'), ('E', 'Exanthématique'), ('A', 'Aiguë'), ('G', 'Généralisée')],
              'Pustulose exanthématique aiguë généralisée',
              'Réaction cutanée sévère citée par l’information professionnelle.', 'g91-macetazol')
add_if_absent('HARM', [('HARM', 'sigle de la base Swisspeddose pour l’usage hors AMM ; développement non lu dans le dossier')],
              'HARM',
              'Mention Swisspeddose d’un usage hors autorisation.', 'g91-macetazol')
add_if_absent('AAN', [('A', 'American'), ('A', 'Academy'), ('N', 'of Neurology')],
              'Académie américaine de neurologie',
              'Sa recommandation de 2015 a été écartée comme fondement.', 'g91-crit')
add_if_absent('L1CAM', [('L1CAM', 'symbole du gène ; développement non lu dans le dossier')],
              'Gène L1CAM',
              'Mutation liée à l’X de l’hydrocéphalie congénitale.', 'g91-cim')
add_if_absent('Dandy-Walker', [('Dandy-Walker', 'noms propres des auteurs, non une abréviation')],
              'Malformation de Dandy-Walker',
              'Malformation de la fosse postérieure citée parmi les causes congénitales.', 'g91-cim')
add_if_absent('MacAulay', [('MacAulay', 'nom propre de l’auteur, non une abréviation')],
              'MacAulay, premier auteur de la revue de 2022',
              'Revue de la production de LCS par les plexus choroïdes.', 'g91-lcs')
add_if_absent('G91.0', [('G', 'chapitre G de la CIM-10-GM'), ('91.0', 'rubrique et sous-rubrique')],
              'G91.0 — hydrocéphalie communicante',
              'Code CIM-10-GM 2024.', 'g91-cim')
add_if_absent('G91.1', [('G', 'chapitre G'), ('91.1', 'rubrique et sous-rubrique')],
              'G91.1 — hydrocéphalie obstructive',
              'Code CIM-10-GM 2024.', 'g91-cim')
add_if_absent('G91.2', [('G', 'chapitre G'), ('91.2', 'rubrique, sous-rubriques 91.20 à 91.29')],
              'G91.2- — hydrocéphalie à pression normale',
              'Code CIM-10-GM 2024.', 'g91-cim')
add_if_absent('G91.20', [('G', 'chapitre G'), ('91.20', 'idiopathique')],
              'G91.20 — idiopathique',
              'Code CIM-10-GM 2024.', 'g91-cim')
add_if_absent('G91.21', [('G', 'chapitre G'), ('91.21', 'secondaire')],
              'G91.21 — secondaire',
              'Code CIM-10-GM 2024.', 'g91-cim')
add_if_absent('G91.29', [('G', 'chapitre G'), ('91.29', 'non précisée')],
              'G91.29 — non précisée',
              'Code CIM-10-GM 2024.', 'g91-cim')
add_if_absent('G91.3', [('G', 'chapitre G'), ('91.3', 'post-traumatique')],
              'G91.3 — post-traumatique, sans précision',
              'Code CIM-10-GM 2024.', 'g91-cim')
add_if_absent('G91.8', [('G', 'chapitre G'), ('91.8', 'autres formes')],
              'G91.8 — autres formes',
              'Code CIM-10-GM 2024.', 'g91-cim')
add_if_absent('G91.9', [('G', 'chapitre G'), ('91.9', 'sans précision')],
              'G91.9 — sans précision',
              'Code CIM-10-GM 2024.', 'g91-cim')
add_if_absent('P91.7', [('P', 'chapitre P (affections de la période périnatale)'), ('91.7', 'hydrocéphalie acquise du nouveau-né')],
              'P91.7 — hydrocéphalie acquise du nouveau-né',
              'Exclu de G91.', 'g91-cim')
add_if_absent('P37.1', [('P', 'chapitre P'), ('37.1', 'toxoplasmose congénitale')],
              'P37.1 — toxoplasmose congénitale',
              'Exclu de G91.', 'g91-cim')
