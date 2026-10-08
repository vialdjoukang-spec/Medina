"""Sigles propres à A53 — Syphilis (I-03-Infectiologie).

Version de travail du 8 octobre 2026, reprise au plan monographique. Les sources
de chaque définition ont été lues ce jour. Les clés communes déjà présentes dans
le glossaire canonique (VIH, PCR, OFSP, SSI, ECDC, OMS, CD4, IgG, IgM, UI, AIPS,
INR, DRESS, ADN, CIM-10-GM) ne sont pas redéfinies. Les clés IST et PrEP,
également définies par d'autres cours du fragment, reçoivent ici une définition
générale compatible avec ces cours.
"""
from cardio_1 import a, G

SSI = '<p>Source : <a href="https://ssi.guidelines.ch/guideline/2271/fr" target="_blank" rel="noopener">SSI, « Syphilis », validée le 13.06.2024</a>.</p>'
IUSTI = '<p>Source : <a href="https://iusti.org/wp-content/uploads/2020/07/Syphilis2020guideline.pdf" target="_blank" rel="noopener">Janier M et al., 2020 European guideline on the management of syphilis, J Eur Acad Dermatol Venereol 2021;35:574–588</a>.</p>'
FI_EXT = '<p>Source : <a href="https://files.refdata.ch/simis-public-prod/MedicinalDocuments/e048ad2d141e42bd9000b297cf3f9d96-fr.html" target="_blank" rel="noopener">Information professionnelle suisse Extencilline®, Swissmedic (AIPS), consultée le 08.10.2026</a>.</p>'

a('TPPA', [('T', 'Treponema'), ('P', 'pallidum'), ('P', 'Particle (particules)'), ('A', 'Agglutination')],
  'Test d’agglutination de particules pour Treponema pallidum',
  '<p>Test tréponémique manuel : des particules portant des antigènes du tréponème s’agglutinent en présence d’anticorps spécifiques. Il prouve une infection actuelle ou passée, reste positif à vie chez la plupart des patients et ne sert pas au suivi. La SSI l’emploie comme test de dépistage.</p>' + SSI + IUSTI)
a('TPHA', [('T', 'Treponema'), ('P', 'pallidum'), ('H', 'Haemagglutination (hémagglutination)'), ('A', 'Assay (test)')],
  'Test d’hémagglutination pour Treponema pallidum',
  '<p>Test tréponémique manuel proche du TPPA, utilisant des hématies sensibilisées. Il sert au dépistage ou à la confirmation d’un test automatisé ; il ne mesure pas l’activité de la maladie.</p>' + IUSTI)
a('RPR', [('R', 'Rapid (rapide)'), ('P', 'Plasma'), ('R', 'Reagin (réagine)')],
  'Test non tréponémique rapide des réagines plasmatiques',
  '<p>Test de floculation détectant des anticorps dirigés contre un antigène de cardiolipine, lécithine et cholestérol. Son titre suit l’activité de la syphilis et baisse après traitement ; une variation significative correspond à deux dilutions, soit un facteur quatre. En Suisse, il remplace le VDRL selon la SSI.</p>' + SSI + IUSTI)
a('VDRL', [('V', 'Venereal (vénérienne)'), ('D', 'Disease (maladie)'), ('R', 'Research (recherche)'), ('L', 'Laboratory (laboratoire)')],
  'Test non tréponémique du Venereal Disease Research Laboratory',
  '<p>Test de floculation de même principe que le RPR, lu au microscope. C’est le test non tréponémique recommandé dans le liquide céphalo-rachidien. Ses titres ne se comparent pas à ceux du RPR.</p>' + IUSTI)
a('FTA-abs', [('F', 'Fluorescent (fluorescent)'), ('T', 'Treponemal (tréponémique)'), ('A', 'Antibody (anticorps)'), ('abs', 'absorption')],
  'Test d’immunofluorescence des anticorps tréponémiques après absorption',
  '<p>Test tréponémique par immunofluorescence indirecte, après absorption des anticorps non spécifiques. Long, coûteux et difficile à lire, il devient obsolète ; la SSI l’emploie comme second test tréponémique lorsque le RPR est négatif sans traitement antérieur.</p>' + SSI + IUSTI)
a('EIA', [('E', 'Enzyme'), ('I', 'Immuno-'), ('A', 'Assay (dosage)')],
  'Dosage immuno-enzymatique',
  '<p>Méthode automatisable de détection d’anticorps, employée ici comme test tréponémique de dépistage ou de confirmation. Sa spécificité peut être insuffisante dans une population à faible prévalence ; un TPPA ou un TPHA de confirmation est alors recommandé.</p>' + IUSTI)
a('ELISA', [('E', 'Enzyme-'), ('L', 'Linked (lié)'), ('I', 'Immuno-'), ('S', 'Sorbent (adsorbant)'), ('A', 'Assay (dosage)')],
  'Dosage immuno-enzymatique sur support solide',
  '<p>Variante de l’EIA dans laquelle l’antigène est fixé sur un support ; employée comme test tréponémique automatisé.</p>' + IUSTI)
a('CLIA', [('C', 'Chemi-'), ('L', 'Luminescence'), ('I', 'Immuno-'), ('A', 'Assay (dosage)')],
  'Dosage immunologique par chimiluminescence',
  '<p>Test tréponémique automatisé à lecture lumineuse, adapté au dépistage de masse ; sa spécificité parfois insuffisante impose une confirmation par TPPA ou TPHA.</p>' + IUSTI)
a('TRUST', [('T', 'Toluidine'), ('R', 'Red (rouge)'), ('U', 'Unheated (non chauffé)'), ('S', 'Serum (sérum)'), ('T', 'Test')],
  'Test non tréponémique au rouge de toluidine sur sérum non chauffé',
  '<p>Test non tréponémique de même principe que le RPR, peu employé en Suisse.</p>' + IUSTI)
a('IST', [('I', 'Infection'), ('S', 'Sexuellement'), ('T', 'Transmissible')],
  'Infection sexuellement transmissible',
  '<p>Infection transmise principalement par contact sexuel. Le diagnostic d’une IST justifie la recherche des autres IST, dont la syphilis et le VIH, selon les sites exposés.</p>' + IUSTI)
a('PrEP', [('Pr', 'Pre- (pré-)'), ('E', 'Exposure (exposition)'), ('P', 'Prophylaxis (prophylaxie)')],
  'Prophylaxie préexposition contre le VIH',
  '<p>Prise d’antirétroviraux par une personne séronégative exposée à un risque élevé d’infection par le VIH. Elle ne protège pas contre la syphilis ; la directive européenne recommande un dépistage de la syphilis tous les trois mois chez les personnes sous PrEP.</p>' + IUSTI)
a('MUI', [('M', 'Millions'), ('U', 'd’Unités'), ('I', 'Internationales')],
  'Millions d’unités internationales',
  '<p>Unité de quantité de la benzylpénicilline et de la benzathine-pénicilline. Une dose de 2,4 MUI désigne la quantité de principe actif, non le volume : le flacon suisse Extencilline® 2,4 MUI se reconstitue avec 5 mL d’eau pour préparations injectables.</p>' + FI_EXT)
a('IUSTI', [('I', 'International'), ('U', 'Union (union)'), ('S', 'against Sexually (contre les infections sexuellement)'), ('T', 'Transmitted (transmises)'), ('I', 'Infections')],
  'Union internationale contre les infections sexuellement transmissibles',
  '<p>Société savante qui publie, par sa section européenne, les directives européennes de prise en charge des IST, dont la directive syphilis 2020 et son projet de mise à jour de 2026.</p>' + IUSTI)
a('LCR', [('L', 'Liquide'), ('C', 'Céphalo-'), ('R', 'Rachidien')],
  'Liquide céphalo-rachidien',
  '<p>Liquide qui baigne l’encéphale et la moelle. Son analyse, cellularité, protéines, test tréponémique et VDRL, sert au diagnostic de la neurosyphilis ; la benzathine-pénicilline n’y atteint pas de concentration tréponémicide fiable.</p>' + IUSTI + FI_EXT)
a('Jarisch-Herxheimer', [('Jarisch-Herxheimer', 'nom propre composé de la réaction ; non un sigle')],
  'Réaction de Jarisch-Herxheimer',
  '<p>Réaction fébrile transitoire, 2 à 12 heures après le début du traitement d’une infection à spirochètes, due à la lyse bactérienne : fièvre, frissons, céphalées, myalgies, tachycardie. Elle disparaît en 10 à 12 heures et ne justifie pas l’arrêt de l’antibiotique.</p>' + FI_EXT)
