"""Abréviations I68 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'i68', '__init__'}:
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

add_if_absent('ARIA', [('A','Amyloid'),('R','Related'),('I','Imaging'),('A','Abnormalities')],
              'Anomalies d’imagerie liées à l’amyloïde (Amyloid-Related Imaging Abnormalities)',
              'Ensemble des anomalies d’imagerie par résonance magnétique qui peuvent survenir sous anticorps dirigés contre l’amyloïde. Elles comprennent l’œdème ou l’effusion (ARIA-E) et les dépôts d’hémosidérine (ARIA-H).', 'i68-aria')
add_if_absent('ARIA-E', [('ARIA','Amyloid-Related Imaging Abnormalities'),('E','Edema, œdème ou effusion')],
              'Anomalies d’imagerie liées à l’amyloïde, type œdème ou effusion',
              'Œdème ou effusion visible en séquence FLAIR sous anticorps anti-amyloïdes. Il est le plus souvent asymptomatique ; sa résolution radiologique médiane est d’environ 8,3 semaines sous donanemab.', 'i68-aria')
add_if_absent('ARIA-H', [('ARIA','Amyloid-Related Imaging Abnormalities'),('H','Hémorragie ou dépôts d’hémosidérine')],
              'Anomalies d’imagerie liées à l’amyloïde, type hémorragie ou dépôts d’hémosidérine',
              'Microhémorragies de 10 mm au plus et sidérose superficielle visibles en T2 étoile ou SWI sous anticorps anti-amyloïdes. Ces dépôts persistent ou se stabilisent.', 'i68-aria')
add_if_absent('APOE', [('APO','Apolipoprotéine'),('E','E')],
              'Apolipoprotéine E',
              'Gène de l’apolipoprotéine E. Son allèle ε4 est associé à l’hémorragie lobaire liée à l’angiopathie amyloïde et à la fréquence des anomalies d’imagerie sous anticorps anti-amyloïdes.', 'i68-apoe')
add_if_absent('SWI', [('S','Susceptibility'),('W','Weighted'),('I','Imaging')],
              'Susceptibility-Weighted Imaging, imagerie pondérée en susceptibilité magnétique',
              'Séquence de résonance magnétique sensible au fer de l’hémosidérine. Elle révèle les microsaignements et la sidérose superficielle corticale.', 'i68-irm')
add_if_absent('FTA-ABS', [('FTA','Fluorescent Treponemal Antibody'),('ABS','Absorption')],
              'Fluorescent Treponemal Antibody Absorption, test tréponémique de la syphilis',
              'Test sérologique tréponémique de la syphilis. Un résultat positif avec un TPHA ou un TPPA sérique positif est exigé par la définition de la neurosyphilis probable.', 'i68-lcr-syph')
add_if_absent('ENRICH', [('ENRICH','nom d’essai, non développé dans les sources lues')],
              'ENRICH, essai de chirurgie mini-invasive de l’hématome',
              'Essai dont le bénéfice de la chirurgie mini-invasive est attribuable aux hémorragies lobaires, selon la recommandation européenne de 2025.', 'i68-chir')
add_if_absent('ENRICH-AF', [('ENRICH-AF','nom d’essai, non développé dans les sources lues')],
              'ENRICH-AF, essai d’anticoagulation après hémorragie',
              'Essai dont le recrutement des hémorragies lobaires et de convexité a été arrêté pour excès de récidives. Les données ne sont pas publiées.', 'i68-oac')
add_if_absent('ERICH', [('ERICH','nom de cohorte, non développé dans les sources lues')],
              'ERICH, cohorte d’hémorragie intracérébrale',
              'Cohorte dans laquelle un contrôle insuffisant de la pression artérielle s’associe à plus de récidives d’hémorragie lobaire.', 'i68-tension')
add_if_absent('SPRINT-MIND', [('SPRINT-MIND','nom d’essai, non développé dans les sources lues')],
              'SPRINT-MIND, essai de contrôle tensionnel',
              'Essai cité par la revue suisse pour une cible tensionnelle inférieure à 120/80 mmHg, à confirmer.', 'i68-tension')
add_if_absent('RESTART', [('RESTART','nom d’essai, non développé dans les sources lues')],
              'RESTART, essai de reprise des antiagrégants',
              'Essai de 537 patients sur la reprise des antiagrégants après hémorragie intracérébrale.', 'i68-antiagr')
add_if_absent('SATURN', [('SATURN','nom d’essai, non développé dans les sources lues')],
              'SATURN, essai sur les statines',
              'Essai en cours sur les statines dans l’hémorragie lobaire.', 'i68-statines')
add_if_absent('LINCHPIN', [('LINCHPIN','nom de cohorte, non développé dans les sources lues')],
              'LINCHPIN, cohorte d’autopsies',
              'Cohorte de 110 autopsies sur laquelle les critères d’Édimbourg ont été développés.', 'i68-edimbourg')
add_if_absent('IDCases', [('IDCases','nom de revue, non une abréviation clinique')],
              'IDCases, revue de cas d’infectiologie',
              'Revue qui publie le cas de vasculopathie varicelle-zona cité dans la bibliographie.', 'i68-vzv')
add_if_absent('AIDS', [('A','Acquired'),('I','Immune'),('D','Deficiency'),('S','Syndrome')],
              'Syndrome d’immunodéficience acquise (Acquired Immune Deficiency Syndrome)',
              'Dans la bibliographie, il apparaît dans le titre de la revue AIDS Research and Therapy, qui publie la revue de cas de vasculopathie varicelle-zona au cours de l’infection par le VIH.', 'i68-vzv')
add_if_absent('SA', [('S','Société'),('A','Anonyme')],
              'Société anonyme',
              'Forme juridique de l’entreprise titulaire de l’autorisation citée pour le Kisunla.', 'i68-kisunla')
