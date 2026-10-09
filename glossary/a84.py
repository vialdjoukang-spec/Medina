"""Sigles propres à A84 — Méningo-encéphalite à tiques (I-03-Infectiologie)."""
from cardio_1 import a, G

REC = '<p>Source : <a href="https://www.bag.admin.ch/dam/fr/sd-web/GaSnHcNnmEXI/zeckenenzephalitis-empfehlung-impfung.pdf" target="_blank" rel="noopener">OFSP et CFV, recommandations de vaccination contre la FSME, juillet 2024</a>.</p>'
if 'FSME-Immun' not in G: a('FSME-Immun', [('FSME', 'Frühsommer-Meningoenzephalitis (méningo-encéphalite verno-estivale, en allemand)'), ('Immun', 'nom commercial')], 'FSME-Immun® (nom commercial d’un vaccin)', '<p>Vaccin inactivé contre la méningo-encéphalite à tiques, souche Neudörfl, autorisé en Suisse ; forme pédiatrique 0.25 ml Junior jusqu’à 16 ans.</p>' + REC)
for c, t in [('A84.0', 'Encéphalite de la taïga [encéphalite verno-estivale russe]'), ('A84.1', 'Encéphalite d’Europe centrale transmise par des tiques'), ('A84.8', 'Autres encéphalites virales transmises par des tiques'), ('A84.9', 'Encéphalite virale transmise par des tiques, sans précision')]:
    if c not in G: a(c, [(c, 'code de la CIM-10-GM 2024')], t, '<p>Code de la classification internationale des maladies, 10e révision, modification allemande 2024 (édition française OFS).</p>')
