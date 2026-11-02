from lesson_helpers import *
import re,hashlib,datetime
p=CH/'N02_c.html';txt=p.read_text()
bridges={
'semio':('La description des hématies et des signes associés localise et hiérarchise les hypothèses. Une fonction normale ne suffit pas à prouver une hématurie isolée.','Confirmer les cellules, mesurer protéines et fonction, puis interpréter morphologie et trajectoire ensemble.','L’urgence, la preuve étiologique, le génotype et les contre-indications priment sur la seule persistance de la bandelette.','Décrire, confirmer, localiser, évaluer le retentissement, puis décider.',('CH-HUG-DEF','CH-HUG-ORIENT','EU-ALPORT-TX')),
'anat':('Le filtre glomérulaire et la voie excrétrice sont deux compartiments différents qui peuvent produire le même signe.','Sédiment, biopsie, échographie et cystoscopie explorent des dimensions différentes ; un résultat normal ne remplace pas les autres.','Le blocage rénine–angiotensine ne traite pas une obstruction par caillots ; choisir le traitement selon la structure atteinte.','La localisation anatomique organise les examens et prévient une attribution trop rapide.',('NORMAL-REIN','NORMAL-FILTRE','CH-HUG-URO')),
'histo':('Une membrane fine, des dépôts d’IgA et un croissant ne racontent pas la même maladie ni le même niveau d’activité.','Microscopie optique, immunofluorescence et électronique se complètent ; la génétique ajoute une preuve différente.','La trajectoire clinique et le mécanisme gouvernent le traitement ; un croissant seul ne justifie pas un protocole de progression rapide.','Lire tissu, fonction et contexte ensemble, sans tirer tout un diagnostic d’un seul champ.',('EU-ALPORT-RISK','INT-IGA-DX','INT-IGA-SPECIAL')),
'physio':('Perméabilité et débit global sont distincts : sang et albumine peuvent apparaître avant une baisse importante de filtration.','Suivre pression, créatinine, potassium et protéines avant et après modification thérapeutique.','Une action sur la pression ou le transport tubulaire peut protéger le rein mais aussi modifier volume, potassium et fonction.','La sécurité suit la physiologie : protéger sans provoquer déplétion ou double blocage.',('NORMAL-FILTRE','EU-ALPORT-TX','FI-RAMIPRIL','FI-FORXIGA')),
'bio':('La réaction à l’hème ne compte pas les cellules ; albumine et protéines totales sont des analytes différents.','Nommer analyte et unité avant un calcul ; une IgA sérique ne démontre pas les dépôts rénaux.','Comparer les seuils propres aux FI : protéines/créatinine en g/g, et non albumine en mg/g.','Une unité correcte fait partie de la décision médicale.',('CH-HUG-DEF','INT-IGA-DX','FI-FILSPARI','FI-KINPEYGO')),
'immuno':('L’IgA implique une maladie immune ; le collagène IV une anomalie structurale dont les lésions secondaires peuvent être trompeuses.','Le diagnostic intègre histologie, données moléculaires et clinique ; une photographie PAS ne montre pas la fluorescence.','Traiter un mécanisme établi, respecter la formulation, les interactions et les limites suisses des combinaisons.','Un mécanisme plausible ne suffit pas à autoriser une prescription.',('INT-IGA-DX','EU-ALPORT-RISK','FI-KINPEYGO','FI-FILSPARI'))}
from bs4 import BeautifulSoup
soup=BeautifulSoup(txt,'html.parser')
for k,(cli,exam,tx,remember,refs) in bridges.items():
 old=soup.find(id='n02-bridge-'+k)
 if old:old.decompose()
 block=sec('bridge-'+k,'Relier la science à la décision','<p><b>Science → clinique.</b> '+cli+'</p><p><b>Science → examen.</b> '+exam+'</p><p><b>Science → traitement.</b> '+tx+'</p>'+key(remember),refs,tag='h3')
 soup.find(id='n02-s-'+k).append(BeautifulSoup(block,'html.parser'))
txt=str(soup)+'\n'
p.write_text(txt)
files={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in list(CH.glob('*.html'))+[ROOT/'glossary/n02.py']}
for p in (ROOT/'assets/img/n02/alpha/codex').glob('*'):files[str(p.relative_to(ROOT))]=hashlib.sha256(p.read_bytes()).hexdigest()
(OUT/'production.json').write_text(json.dumps(dict(mission='ALPHA77-CODEX-N02-INTEGRATE',code='N02',complete=True,meaning='Production matérielle des six surfaces ; relectures et tests finaux encore requis, sans certification clinique.',recorded_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),final_files=files,clinical_certification=False),ensure_ascii=False,indent=2)+'\n')
