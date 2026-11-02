from lesson_helpers import *
from lesson_figures import figure
from bs4 import BeautifulSoup
parts=['a','b','c','d'];s=BeautifulSoup(''.join((CH/f'C64_{p}.html').read_text()+f'<!--C64-CUT-{p}-->' for p in parts),'html.parser')
s.find(id='c64-semio-normal').append(BeautifulSoup(figure('kidney'),'html.parser'))
s.find(id='c64-s-immuno-content').append(BeautifulSoup('<p>La microphotographie suivante rappelle le tissu tumoral ciblé ; elle ne montre ni lymphocytes fonctionnels, ni expression PD-L1, ni réponse à un anticorps. Ces mécanismes sont établis par les sources et ne sont pas inférés de la photographie.</p>'+figure('clear'),'html.parser'))
for k,t in [('semio','Décrire, localiser, expliquer puis vérifier : un signe ne remplace pas toute la chaîne diagnostique.'),('histo','La nature tumorale, le grade et l’échantillonnage sont trois questions différentes.'),('physio','Une fonction globale conservée ne signifie pas absence de lésion ; anticiper le rein restant.'),('bio','Un mécanisme, une mesure relative et une différence absolue ne répondent pas à la même question.')]:
 panel=s.find(id='c64-s-'+k);panel.append(BeautifulSoup(key(t),'html.parser'))
t=str(s)
for p in parts:b,t=t.split(f'<!--C64-CUT-{p}-->',1);save(p,b)
print('Contrat scientifique complété ; huit occurrences scientifiques humaines.')
