"""Sigles propres à B02 — Zona (I-03-Infectiologie)."""
from cardio_1 import a, G

SHI = '<p>Source : <a href="https://www.swissmedicinfo.ch/ShowText.aspx?textType=FI&amp;lang=FR&amp;authNr=67987" target="_blank" rel="noopener">Information professionnelle suisse Shingrix®, mai 2026</a>.</p>'
a('AS01B', [('AS', 'Adjuvant System (système adjuvant)'), ('01', 'famille 01'), ('B', 'formulation B')], 'Système adjuvant AS01B', '<p>Adjuvant liposomal du vaccin Shingrix® associant le monophosphoryl lipide A et la saponine QS-21 ; il renforce la réponse des lymphocytes T contre la glycoprotéine E du virus varicelle-zona.</p>' + SHI)
a('ZOE-50', [('ZO', 'ZOster (zona)'), ('E', 'Efficacy (efficacité)'), ('50', 'sujets de 50 ans et plus')], 'Essai « Zoster Efficacy study in subjects older than 50 »', '<p>Essai randomisé de phase III du vaccin Shingrix® contre placebo chez les 50 ans et plus : efficacité 97,2 % contre le zona.</p>' + SHI)
a('ZOE-70', [('ZO', 'ZOster (zona)'), ('E', 'Efficacy (efficacité)'), ('70', 'sujets de 70 ans et plus')], 'Essai « Zoster Efficacy study in subjects older than 70 »', '<p>Essai randomisé de phase III du vaccin Shingrix® contre placebo chez les 70 ans et plus ; analysé avec ZOE-50, efficacité 91,3 %.</p>' + SHI)
