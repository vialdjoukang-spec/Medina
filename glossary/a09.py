"""Sigles propres à A09 — Gastro-entérite infectieuse aiguë (I-03-Infectiologie)."""
from cardio_1 import a, G

SSI = '<p>Source : <a href="https://ssi.guidelines.ch/guideline/3465/fr" target="_blank" rel="noopener">SSI, « Gastro-entérite infectieuse », validée le 19 juin 2026</a>.</p>'
a('O157', [('O', 'antigène O (somatique, lipopolysaccharide de paroi)'), ('157', 'numéro 157 de la classification sérologique')], 'Sérogroupe O157 d’Escherichia coli', '<p>Sérogroupe le plus connu d’<i>E. coli</i> producteur de shigatoxine (entérohémorragique), cause de diarrhée sanglante et de syndrome hémolytique et urémique ; le lopéramide y est contre-indiqué.</p>' + SSI)
