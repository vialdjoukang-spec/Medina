from pathlib import Path
import re,json,html
R=Path(__file__).resolve().parents[5];D=Path(__file__).resolve().parent
ps=list((R/'chapters/E07').glob('*.html'))
for p in ps:
 s=p.read_text()
 for old,new in {
 'left:40%;top:83%':'left:46%;top:88.7%',
 'superposés en HTML':'superposés sans modification des pixels',
 'repères ajoutés en HTML':'repères ajoutés sans modification des pixels',
 'sans glande ni hormone':'sans glande ni hormone',
 'référence 2012':'référence historique',
 '; Elisei et al. 2012':'',
 'le déficit de synthèse abaisse':'le déficit de synthèse peut abaisser',
 'Le défaut de synthèse abaisse la thyroxine et la triiodothyronine ; la thyréostimuline s’élève et stimule la croissance de la glande, d’où le goitre.':'Un défaut de synthèse peut abaisser la FT4 et augmenter la TSH, favorisant le goitre. L’intensité varie ; certaines formes sont transitoires ou sans goitre. Ni une T3 conservée ni une glande peu volumineuse ne suffisent à l’exclure.',
 'Si la fraction libre et la thyréostimuline sont normales, la thyroxine totale basse n’est pas une maladie thyroïdienne.':'Si FT4 et TSH sont fiables et normales dans un contexte stable, une T4 totale basse évoque une anomalie de transport ; rechercher néanmoins une maladie coexistante si la clinique l’impose.',
 'récurrrence':'récurrence',
 'récurrence de la dyshormonogenèse 25 %':'récurrence récessive 25 % si les deux parents sont porteurs',
 'Récessif : 25 % ;':'Deux parents porteurs d’une même maladie récessive : 25 % ;',
 'Dyshormonogenèse : défaut de synthèse, hormones basses, thyréostimuline haute, goitre ;':'Dyshormonogenèse : défaut de synthèse de gravité variable, goitre possible ;',
 'globuline liante et maladie non thyroïdienne : ne pas substituer.':'anomalie isolée de transport ou NTIS : pas de substitution systématique ; traiter toute hypothyroïdie authentique coexistante.',
 'Globuline liante et maladie non thyroïdienne : ne pas substituer.':'Anomalie isolée de transport ou NTIS : pas de substitution systématique ; traiter toute hypothyroïdie authentique coexistante.',
 'Ne pas substituer pour globuline liante ou maladie non thyroïdienne.':'Ne pas substituer le seul chiffre ; poursuivre ou introduire un traitement si une hypothyroïdie authentique est démontrée.',
 'test au calcium 79 et 466 pg/ml ; procalcitonine hors infection':'test au calcium sélectionné (seuils d’étude 79 et 466 pg/ml, méthode propre) ; procalcitonine avec ses facteurs de confusion',
 'e07-s-anat-cours,e07-s-histo-cours':'e07-s-semio-cours,e07-s-anat-cours,e07-s-histo-cours',
 'e07-p-1,e07-p-2,e07-p-3,e07-p-4':'e07-p-1,e07-p-2,e07-p-3,e07-p-4,e07-p-5,e07-p-6',
 'un cancer médullaire est évocateur':'un cancer médullaire est fortement évoqué, sans confirmation histologique par le seul chiffre',
 'L’adaptation ne change pas la conduite, elle évite l’erreur.':'L’adaptation peut modifier la décision, le calendrier et la surveillance.',
 'avec un faible niveau de preuve.':'avec un faible niveau de preuve ; cette estimation n’est pas un risque individuel établi.',
 'baisse lepton':'baisse lepton',
 }.items():s=s.replace(old,new)
 # Restrict two older assertions that otherwise read as universals.
 s=s.replace('La maladie non thyroïdienne ne reçoit pas de substitution : aucune recommandation n’existe','Le syndrome de maladie non thyroïdienne ne justifie pas une substitution systématique')
 s=s.replace('Le déficit en globuline liante ne se traite pas.','Le déficit isolé en globuline liante ne nécessite pas de substitution hormonale.')
 s=s.replace('Doser les métanéphrines avant toute chirurgie si le statut RET est inconnu.','Rechercher un phéochromocytome avant une chirurgie en cas de NEM2 ou de suspicion appropriée.')
 s=s.replace('dosage des métanéphrines avant toute chirurgie si le statut RET est inconnu','recherche de phéochromocytome avant chirurgie dans le contexte de NEM2')
 if p.name=='E07_pop1.html':
  body='''<template data-pop="e07-cochrane" data-title="Calcitonine : performances et probabilité avant test"><div class="lab">Population</div><p>La revue Cochrane 2020 regroupe 16 études et 72 368 participants avec nodules ; recherche jusqu’à juin 2018. La prévalence médiane est 0,32 % dans l’ensemble, 0,23 % dans le calcul rapporté de valeur prédictive au seuil de 10 pg/ml.</p><div class="lab">Résultats du résumé</div><p>À 10 pg/ml : sensibilité groupée 100 % (IC 95 % 99,7–100), spécificité 97,2 % (95,9–98,6), valeur prédictive positive 7,7 % (4,9–12,1) pour la prévalence utilisée. Ces nombres ne sont pas des performances garanties pour chaque sexe, laboratoire ou contexte.</p><div class="lab">Limites</div><p>Quinze des seize études n’avaient pas une référence ou un suivi adéquat pour les résultats négatifs, d’où un risque important de surestimation. L’amélioration du pronostic par un dépistage systématique reste incertaine. Le résumé n’autorise pas à affirmer qu’une calcitonine à n’importe quel niveau n’a que 7,7 % de risque.</p><p class="src">[S7] résumé structuré intégral, PMID 32176812 ; [S5] ETA 2023 : indications ciblées et absence de position pour ou contre le dépistage universel.</p></template>'''
  s=re.sub(r'<template data-pop="e07-cochrane".*?</template>',body,s,flags=re.S)
 if p.name=='E07_b.html':s=s.replace('<ul><li id="e07-ref-', '<ul data-justification-sources="1"><li id="e07-ref-')
 p.write_text(s)
# Local glossary updates without modifying other specialties or shared engine.
g=R/'glossary/e07.py';s=g.read_text().replace('recommandations de 2012 (cancer médullaire et dépistage génétique) et de 2023 (nodules thyroïdiens) fondent plusieurs passages de cette leçon, faute de recommandation suisse lue','recommandations de 2023 (nodules) et 2024 (discordances hormonales génétiques) complètent les sources suisses de cette leçon')
items={
 'FT4':('Free thyroxine — thyroxine libre','Fraction non liée de T4 mesurée dans le sang ; interprétation selon âge, méthode, contexte et TSH.','e07-mnemo'),
 'NEM2':('Néoplasie endocrinienne multiple de type 2','Prédisposition associée à des variants pathogènes activateurs de RET ; manifestations et prise en charge dépendent du variant.','e07-ret'),
 'NHS':('National Health Service','Service national de santé britannique ; la synthèse GeNotes sur NEM2 est une source européenne, pas une directive suisse.','e07-sources-guides'),
 'GeNotes':('Genomics Notes, ressource NHS','Ressource pédagogique du programme britannique de formation en génomique.','e07-sources-guides'),
 'MCT8':('Monocarboxylate transporter 8','Transporteur cellulaire d’hormones thyroïdiennes, distinct de la protéine sérique TBG ; gène SLC16A2.','e07-smnt-meca'),
 'MCT10':('Monocarboxylate transporter 10','Transporteur cellulaire dont l’expression peut varier selon tissu et maladie ; ne se confond pas avec TBG.','e07-smnt-meca'),
 'OATP1C1':('Organic anion transporting polypeptide 1C1','Transporteur impliqué dans la disponibilité cellulaire des hormones thyroïdiennes, notamment cérébrale.','e07-smnt-meca'),
 'ANO1':('Anoctamin 1','Canal anionique cité parmi les voies pouvant contribuer à l’efflux apical d’iodure ; compensation possible dans le syndrome de Pendred.','e07-pendred'),
 'PEG':('Polyéthylèneglycol','Agent de précipitation utilisé par le laboratoire dans certaines recherches d’interférence, sans résultat diagnostique absolu isolé.','e07-ct-interference'),
 'NTIS':('Non-thyroidal illness syndrome — syndrome de maladie non thyroïdienne','Modification de l’axe et du métabolisme hormonal en maladie générale ; n’exclut pas une hypothyroïdie concomitante.','e07-smnt-dd'),
 'ICD-10':('International Classification of Diseases, 10th revision','Classification statistique internationale ; distinguer version internationale, adaptation allemande et libellés suisses.','e07-nosologie'),
 'URL':('Uniform Resource Locator — adresse d’une ressource','Adresse de la page de référence ; l’accès à une page ne constitue pas une validation médicale.','e07-sources-guides'),
 'HTML':('HyperText Markup Language','Balises de présentation ; les annotations des images originales sont ajoutées sans changer les pixels.','e07-sources-guides'),
}
for key,(full,definition,ref) in items.items():s+=f'\na({key!r}, [({key!r}, {full!r})], {full!r}, {definition!r}, {ref!r})\n'
g.write_text(s)
# Explicit contextual TPO popup avoids shared glossary collision with thrombopoietin.
p=R/'chapters/E07/E07_pop2.html';s=p.read_text();s+='\n<template data-pop="e07-tpo-local" data-title="TPO : thyroperoxydase"><p>Dans cette leçon, TPO désigne la peroxydase thyroïdienne, enzyme de l’organification de l’iode et du couplage sur la thyroglobuline. Son déficit peut provoquer une dyshormonogenèse ; le phénotype varie et n’impose pas toujours un goitre. Anti-TPO désigne les anticorps dirigés contre cette enzyme. Ce terme ne désigne pas ici la thrombopoïétine.</p><p class="src">[S3] ENDO-ERN, tableau 3 ; [S16] différentiel du NTIS.</p></template>\n';p.write_text(s)
# Make all citations true links to the exact source, avoiding accidental glossary codes.
sources=json.loads((D/'recherche_E07/sources.json').read_text())['sources'];urls={x['id']:x['url'].split(' — ')[-1].split(' (doi:')[0] for x in sources}
def citation(m):
 raw=m.group()[1:-1];parts=[]
 for seg in raw.split(','):
  seg=seg.strip();rg=re.fullmatch(r'S(\d+)[–-]S?(\d+)',seg)
  if rg:parts.extend('S'+str(n) for n in range(int(rg[1]),int(rg[2])+1))
  else:parts.append(seg)
 if any(x not in urls for x in parts):return m.group()
 return '['+', '.join(f'<a data-reference-source="1" href="{html.escape(urls[x],quote=True)}" target="_blank" rel="noopener">{x}</a>' for x in parts)+']'
for p in ps:
 s=p.read_text();out=[];buttons=anchors=0
 for t in re.split(r'(<[^>]+>)',s):
  if t.startswith('<'):
   if re.match(r'<button\b',t):buttons+=1
   elif t.startswith('</button'):buttons-=1
   if re.match(r'<a\b',t):anchors+=1
   elif t.startswith('</a>'):anchors-=1
   out.append(t)
  else:
   if not anchors:
    t=re.sub(r'\[S\d+[a-z]?(?:[–-]S?\d+)?(?:,\s*S\d+[a-z]?(?:[–-]S?\d+)?)*\]',citation,t)
   if not buttons and not anchors:t=re.sub(r'(?<![A-Za-z0-9])TPO(?![A-Za-z0-9])','<button class="w" data-k="e07-tpo-local">TPO</button>',t)
   out.append(t)
 p.write_text(''.join(out))
print('Cohérence des fenêtres, références liées et glossaire contextuel corrigés.')
