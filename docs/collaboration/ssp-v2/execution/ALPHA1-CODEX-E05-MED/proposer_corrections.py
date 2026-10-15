from pathlib import Path
import re,json,difflib
D=Path(__file__).resolve().parent;root=Path.cwd();data={};changes=[]
def load(p):
 if p not in data:data[p]=(root/p).read_text()
def change(p,old,new,id,sources):
 load(p);n=data[p].count(old)
 if n!=1:raise RuntimeError((id,p,n))
 data[p]=data[p].replace(old,new);changes.append(dict(id=id,path=p,avant=old,apres=new,sources=sources))
for p in ['chapters/E05/E05_b.html','chapters/E05/E05_c.html','chapters/E05/E05_d.html','chapters/E05/E05_pop2.html']:
 load(p)
 pat=r'neutrophiles inférieurs à 500(?: par millilitre)?'
 old=data[p];new,n=re.subn(pat,'neutrophiles inférieurs à 500/µL (0,5 × 10⁹/L)',old)
 if n:
  data[p]=new;changes.append(dict(id='E05-M01',path=p,substitutions=n,avant='neutrophiles inférieurs à 500 [par millilitre]',apres='neutrophiles inférieurs à 500/µL (0,5 × 10⁹/L)',sources=['S8','S9','S3','S7']))
p='chapters/E05/E05_pop2.html'
change(p,'hyperglycémie (13,2 % des patients, environ 80 % de ceux qui ont un diabète ou une intolérance préexistants)',
'hyperglycémie chez 13,2 % des patients des études en double aveugle; parmi ces patients ayant présenté une hyperglycémie, 80 % avaient un diabète ou une intolérance au glucose préexistants', 'E05-M02',['S6'])
change(p,'Hyperglycémie chez 13,2 % des patients (environ 80 % de ceux qui ont un diabète ou une intolérance au glucose préexistants)',
'Hyperglycémie chez 13,2 % des patients des études en double aveugle; 80 % des patients ayant présenté cette hyperglycémie avaient un diabète ou une intolérance au glucose préexistants','E05-M02-monographie',['S6'])
p='chapters/E05/E05_b.html'
change(p,'10 % de rechute (méta-analyse)','Le chiffre de 10 % cité par la méta-analyse concerne la chirurgie dans son ensemble; il ne constitue pas un taux de rechute propre à la thyroïdectomie totale.','E05-M03',['S7'])
change(p,'Les deux traitements définitifs évitent la rechute au prix d’une hypothyroïdie (iode 131) ou d’un risque opératoire (chirurgie).',
'Les traitements définitifs réduisent le risque de rechute, avec un risque d’hypothyroïdie après l’iode 131 et les risques propres à la chirurgie. La thyroïdectomie totale entraîne une hypothyroïdie qui nécessite une substitution.','E05-M03-lecture',['S7','S10'])
change(p,'Un bêtabloquant cardiosélectif s’impose en cas d’asthme.',
'Chez une personne asthmatique, l’ETA présente un bêtabloquant cardiosélectif comme une alternative à discuter selon l’état respiratoire et l’information professionnelle du produit exact. Cette option n’est pas une obligation systématique.','E05-M04',['S4','S7'])
change(p,'L’allaitement reste possible : mêmes options de traitement, méthimazole préféré. La <button class="w" data-k="e05-allaitement">prise après la tétée</button> et la limite de 20 mg par jour s’appliquent.',
'Les choix pendant l’allaitement se vérifient par produit. Pour Néo-Mercazole, la FI suisse recommande de renoncer de préférence à l’allaitement; s’il est poursuivi après information, elle fixe au plus 20 mg de carbimazole par jour, fractionnés en <button class="w" data-k="e05-allaitement">prises après la tétée</button>, avec surveillance de la fonction thyroïdienne du nourrisson. La FI d’Inderal demande de ne pas allaiter pendant son utilisation.','E05-M05',['S3','S4','S7'])
p='chapters/E05/E05_d.html'
change(p,'Contre-indication si antécédent','Contre-indication en cas de pancréatite antérieure provoquée par le carbimazole ou le thiamazole','E05-M06',['S3'])
p='chapters/E05/E05_c.html'
change(p,'Les glucocorticoïdes et la dopamine normalisent la TSH malgré une dysthyroïdie.',
'Sous glucocorticoïdes ou dopamine, une TSH dans l’intervalle de référence ne suffit pas toujours à exclure une dysthyroïdie; le résultat se confronte au contexte clinique.','E05-M07',['S1'])
p='chapters/E05/E05_pop2.html'
change(p,'Une variation d’un facteur 2 de l’hormone libre s’accompagne donc d’une variation d’un facteur voisin de 16 de la TSH.',
'Ces rapports comparent les bornes de deux intervalles de population. Ils ne permettent pas de calculer la variation de TSH produite par un doublement de T4 libre chez un individu, ni de déduire la pente de la relation TSH–T4.','E05-M08',['S1','S7'])
change(p,'Les deux intervalles décrivent des populations, non la courbe d’un individu ; le calcul illustre un ordre de grandeur.',
'les deux intervalles décrivent des populations, non la courbe d’un individu; leurs quotients ne mesurent pas sa réponse physiologique.','E05-M08-limites',['S1','S7']) if 'Les deux intervalles décrivent des populations, non la courbe d’un individu ; le calcul illustre un ordre de grandeur.' in data[p] else None
# Enrichissement organique strictement issu de la FI exacte, dans la seule monographie concernée.
load(p);pat=r'(<template data-pop="e05-m-neomercazole".*?)(</div></template>)';m=re.search(pat,data[p],re.S)
if not m:raise RuntimeError('Monographie Néo-Mercazole absente')
addition='<p><b>Fonctions hépatique et rénale.</b> La FI contre-indique Néo-Mercazole en cas d’insuffisance hépatique sévère (Child Pugh C). En Child Pugh A ou B, elle demande de la prudence du fait de l’allongement possible de la demi-vie. En insuffisance rénale, les données sont limitées : précaution particulière et surveillance régulière des paramètres thyroïdiens, sans pourcentage forfaitaire d’adaptation.</p>'
data[p]=data[p][:m.start()]+m.group(1)+addition+m.group(2)+data[p][m.end():];changes.append(dict(id='E05-E01',path=p,ancre='e05-m-neomercazole',apres=addition,sources=['S3']))
# Quiz : les seules données de TSH et de TRAb ne permettent pas un diagnostic étiologique ferme.
p='chapters/E05/E05_a.html';load(p)
change(p,'Thyrotoxicose gestationnelle liée à l’hCG : pas d’antithyroïdien, surveillance.',
'TSH basse isolée : compléter par les hormones thyroïdiennes et le contexte de grossesse avant de décider du traitement.','E05-M09-option',['S1','S2','S7'])
pat=r'(<div class="quiz ui" id="e05-quiz-1">.*?<p class="fb" hidden>)(.*?)(</p></div>)';m=re.search(pat,data[p],re.S)
if not m:raise RuntimeError('Feedback quiz grossesse absent')
new='La TSH seule ne suffit pas à confirmer une thyrotoxicose manifeste ni à en déterminer la cause. Il faut connaître les hormones thyroïdiennes, les interpréter avec les références de grossesse du laboratoire et confronter les symptômes et les antécédents. Un TRAK négatif n’exclut pas à lui seul une maladie de Basedow. Le test réflexe SSCC 2025 concerne l’adulte hors grossesse; il ne doit pas être transposé automatiquement à cette vignette. Aucun antithyroïdien à pleine dose ne se déduit de ces seules données. L’iode 131 est contre-indiqué pendant la grossesse.'
old=m.group(2);data[p]=data[p][:m.start()]+m.group(1)+new+m.group(3)+data[p][m.end():];changes.append(dict(id='E05-M09-explication',path=p,avant=old,apres=new,sources=['S1','S2','S7']))
for p,new in data.items():
 if new==(root/p).read_text():continue
 out=D/'drafts'/p;out.parent.mkdir(parents=True,exist_ok=True);out.write_text(new)
patch=''.join(''.join(difflib.unified_diff((root/p).read_text().splitlines(True),new.splitlines(True),fromfile='a/'+p,tofile='b/'+p)) for p,new in sorted(data.items()) if new!=(root/p).read_text())
(D/'enrichissements.patch').write_text(patch)
(D/'propositions.json').write_text(json.dumps({'statut':'propositions non intégrées; réserves médicales ouvertes','changes':changes},ensure_ascii=False,indent=2)+'\n')
