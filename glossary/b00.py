"""Sigles propres à B00 — Infections à virus herpès simplex (I-03-Infectiologie)."""
from cardio_1 import a, G

IUSTI = '<p>Source : <a href="https://doi.org/10.1177/0956462417727194" target="_blank" rel="noopener">Patel R et al., recommandations européennes IUSTI 2017 sur l’herpès génital</a>.</p>'
a('HSV-1', [('H', 'Herpes'), ('S', 'Simplex'), ('V', 'Virus'), ('1', 'type 1')], 'Virus herpès simplex de type 1', '<p>Cause habituelle de l’herpès oro-labial, de plus en plus fréquente dans l’herpès génital ; récurrences génitales moins fréquentes qu’avec le type 2.</p>' + IUSTI)
a('HSV-2', [('H', 'Herpes'), ('S', 'Simplex'), ('V', 'Virus'), ('2', 'type 2')], 'Virus herpès simplex de type 2', '<p>Cause principale de l’herpès génital récurrent ; séroprévalence de 19,3 % chez les adultes de 35 à 64 ans en Suisse romande et italienne en 1992–1993.</p>' + IUSTI)
if 'IUSTI' not in G: a('IUSTI', [('I', 'International'), ('U', 'Union against'), ('S', 'Sexually'), ('T', 'Transmitted'), ('I', 'Infections')], 'Union internationale contre les infections sexuellement transmissibles', '<p>Société savante dont la branche européenne publie les recommandations européennes sur les infections sexuellement transmissibles.</p>' + IUSTI)
