"""Proposition ALPHA1-CLAUDE-G91-MED : sigles nouveaux introduits par les propositions (C01, C03, C04, C05, C24).

À ajouter à la fin de glossary/g91.py (même fonction add_if_absent). Développements limités à ce que les sources lues écrivent ;
lorsqu'un développement littéral n'a pas été lu, l'entrée le dit. Références [Sx] : sources.json du dossier.
Correction de l'entrée HARM existante : voir propositions/G91_d_1.html (constat C18).
"""

add_if_absent('AWMF', [('AWMF', 'sigle du registre allemand des lignes directrices ; développement littéral non lu dans les sources')],
              'Registre allemand des lignes directrices médicales (AWMF)',
              'La ligne directrice 006-102 sur l’hydrocéphalie de l’enfant y est publiée [S19].', 'g91-sm-pc')
add_if_absent('S2k', [('S2k', 'classe de ligne directrice AWMF ; développement littéral non lu dans les sources')],
              'Ligne directrice de classe S2k',
              'Ligne directrice élaborée par un processus de consensus de type Delphi entre les sociétés concernées [S19].', 'g91-sm-pc')
add_if_absent('PIGS', [('PIGS', 'Pädiatrische Infektiologiegruppe der Schweiz ; sigle tel que cité par la ligne directrice AWMF')],
              'Groupe suisse d’infectiologie pédiatrique',
              'Il propose la céfazoline à 25 mg/kg en dose unique 30 minutes avant une opération de dérivation, selon la ligne directrice AWMF [S19].', 'g91-macetazol')
add_if_absent('HCRN', [('H', 'Hydrocephalus (hydrocéphalie)'), ('C', 'Clinical (clinique)'), ('R', 'Research (recherche)'), ('N', 'Network (réseau)')],
              'Réseau nord-américain de recherche clinique sur l’hydrocéphalie',
              'Ses seuils de traitement sont un consensus nord-américain, cité mais non retenu comme fondement [S2].', 'g91-sm-pc')
add_if_absent('OMIM', [('OMIM', 'nom du catalogue des maladies génétiques cité par la ligne directrice AWMF ; développement littéral non lu dans les sources')],
              'Catalogue OMIM des maladies génétiques',
              'Une recherche sur « hydrocephalus » y donnait 572 entrées en décembre 2024 [S19].', 'g91-sm-pouce')
for gene, role in [('AP1S2', 'hydrocéphalie récessive liée à l’X avec déficience intellectuelle'),
                   ('MPDZ', 'hydrocéphalie autosomique récessive, épendyme fragile, aqueduc rétréci'),
                   ('CCDC88C', 'hydrocéphalie autosomique récessive, épendyme fragile, aqueduc rétréci'),
                   ('TRIM71', 'hydrocéphalie congénitale, mutations le plus souvent de novo'),
                   ('SMARCC1', 'hydrocéphalie congénitale, mutations le plus souvent de novo'),
                   ('CFAP43', 'hydrocéphalie à pression normale dominante, décrite dans une seule famille')]:
    add_if_absent(gene, [(gene, 'symbole officiel du gène ; développement non lu dans les sources')],
                  'Gène ' + gene, role.capitalize() + ' [S19 ; S2].', 'g91-sm-pouce')
