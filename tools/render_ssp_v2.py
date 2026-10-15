#!/usr/bin/env python3
"""MEDINA SSP v2: three evidence-bound planning PDFs. No medical execution."""
from pathlib import Path
from collections import Counter,defaultdict
from xml.sax.saxutils import escape
import json,hashlib,re,sys,subprocess
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Table,TableStyle,CondPageBreak,KeepTogether
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'docs/collaboration/ssp-v2/2026-10-15'
METHOD=json.loads((DEST/'methodologie.json').read_text())
BASE='7adf385a5182a8dcf25584dbb53207c620440ad3'
TEST_LOG=(DEST/'tests-garde.log').read_text() if (DEST/'tests-garde.log').exists() else ''
TEST_MATCH=re.search(r'Ran (\d+) tests in ([0-9.]+)s',TEST_LOG)
TEST_N=TEST_MATCH.group(1) if TEST_MATCH else 'nombre non établi'
TEST_SECS=TEST_MATCH.group(2) if TEST_MATCH else 'durée non établie'
for n,f in [('DV','DejaVuSans.ttf'),('DV-Bold','DejaVuSans-Bold.ttf'),('DV-Italic','DejaVuSans-Oblique.ttf')]:
 pdfmetrics.registerFont(TTFont(n,'/usr/share/fonts/truetype/dejavu/'+f))
pdfmetrics.registerFontFamily('DV',normal='DV',bold='DV-Bold',italic='DV-Italic')
W,H=A4; M=43; CW=W-2*M
NAVY=colors.HexColor('#143B50');TEAL=colors.HexColor('#087E87');INK=colors.HexColor('#183846');MUTE=colors.HexColor('#48626C');PALE=colors.HexColor('#E7F4F3');LINE=colors.HexColor('#BED7DB');CREAM=colors.HexColor('#FBF5DF')
ST={
 'title':ParagraphStyle('title',fontName='DV-Bold',fontSize=27,leading=34,textColor=NAVY,spaceAfter=18),
 'h1':ParagraphStyle('h1',fontName='DV-Bold',fontSize=19,leading=25,textColor=NAVY,spaceAfter=14,keepWithNext=True),
 'h2':ParagraphStyle('h2',fontName='DV-Bold',fontSize=12,leading=17,textColor=TEAL,spaceBefore=12,spaceAfter=7,keepWithNext=True),
 'h3':ParagraphStyle('h3',fontName='DV-Bold',fontSize=10.5,leading=15,textColor=NAVY,spaceBefore=10,spaceAfter=6,keepWithNext=True),
 'body':ParagraphStyle('body',fontName='DV',fontSize=10,leading=14.7,textColor=INK,spaceAfter=8),
 'small':ParagraphStyle('small',fontName='DV',fontSize=9.5,leading=13.8,textColor=MUTE,spaceAfter=7),
 'cell':ParagraphStyle('cell',fontName='DV',fontSize=9.5,leading=13.5,textColor=INK,splitLongWords=True),
 'kicker':ParagraphStyle('kicker',fontName='DV-Bold',fontSize=9.5,leading=14,textColor=TEAL,spaceAfter=10),
 'code':ParagraphStyle('code',fontName='DV',fontSize=9.5,leading=14,textColor=INK,spaceAfter=8,leftIndent=8,rightIndent=4,backColor=PALE,borderPadding=7)
}
def E(v):return escape(str(v))
def txt(v):
 if v is None:return 'non renseigné'
 if isinstance(v,(list,tuple)):return ', '.join(map(str,v)) or 'aucun'
 if isinstance(v,dict):return '; '.join(f'{k} : {txt(x)}' for k,x in v.items()) or 'aucun'
 return str(v)
def para(v,style='body'):return Paragraph(str(v),ST[style])
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
class Pages(canvas.Canvas):
 def __init__(self,*a,**kw):super().__init__(*a,**kw);self.saved=[]
 def showPage(self):self.saved.append(dict(self.__dict__));self._startPage()
 def save(self):
  total=len(self.saved)
  for state in self.saved:
   self.__dict__.update(state);self.saveState();self.setStrokeColor(LINE);self.line(M,37,W-M,37);self.setFillColor(MUTE);self.setFont('DV',9.5)
   self.drawString(M,22,'MEDINA · PLAN / PREUVES · 15.10.2026');self.drawRightString(W-M,22,f'{self._pageNumber} / {total}');self.restoreState();super().showPage()
  super().save()
class PDF:
 def __init__(self,title,kind):self.story=[];self.title=title;self.kind=kind;self.seq=0
 def p(self,t,style='body'):self.story.append(para(t,style))
 def h(self,t):self.p(E(t),'h2')
 def sub(self,t):self.p(E(t),'h3')
 def page(self,t):
  if self.story:self.story.append(PageBreak())
  self.seq+=1;self.p(f'MEDINA / {self.kind} / {self.seq:02d}','kicker');self.p(E(t),'h1')
 def box(self,t):
  t=Table([[para(t)]],colWidths=[CW]);t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),CREAM),('BOX',(0,0),(-1,-1),.7,LINE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),12),('RIGHTPADDING',(0,0),(-1,-1),12),('TOPPADDING',(0,0),(-1,-1),10),('BOTTOMPADDING',(0,0),(-1,-1),4)]));self.story.extend([t,Spacer(1,9)])
 def table(self,heads,rows,widths=None):
  if not rows:return
  widths=widths or [CW/len(heads)]*len(heads)
  data=[[para('<b>'+E(x)+'</b>','cell') for x in heads]]+[[para(E(txt(x)).replace('\n','<br/>'),'cell') for x in r] for r in rows]
  t=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT',splitByRow=1)
  t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BACKGROUND',(0,0),(-1,0),PALE),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F4F8FA')]),('LINEBELOW',(0,0),(-1,0),1,TEAL),('LINEBELOW',(0,1),(-1,-1),.35,LINE),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),7)]));self.story.extend([t,Spacer(1,9)])
 def code(self,lines):
  for l in lines:self.p(E(l),'code')
 def save(self,name):
  target=DEST/name
  doc=SimpleDocTemplate(str(target),pagesize=A4,leftMargin=M,rightMargin=M,topMargin=49,bottomMargin=52,title=self.title,author='MEDINA — Codex / Claude — planification',subject='Plan v2 détaillé ; aucune validation médicale implicite',pageCompression=1)
  def frame(c,d):
   c.saveState();c.setFillColor(TEAL);c.rect(0,H-9,W,9,fill=1,stroke=0);c.setFillColor(MUTE);c.setFont('DV',9.5);c.drawString(M,H-28,'MEDINA · '+self.kind);c.restoreState()
  doc.build(self.story,onFirstPage=frame,onLaterPages=frame,canvasmaker=Pages)
  print(name,target.stat().st_size,sha(target),flush=True)
FRAGS={'S08':'N-05 — Neurologie','S05':'E-06 — Endocrinologie et métabolisme','S04':'N-07 — Néphrologie','S06':'H-08 — Hématologie'}
MATRIX=[
('Question clinique et examen fédéral','Formuler ce que le lecteur doit reconnaître, distinguer et décider ; relier la situation SSP exacte, sans prétendre à une table officielle CIM–PROFILES.'),
('Définition et périmètre CIM-10-GM','Libellé OFS, inclusions/exclusions et notes de classification ; distinguer définition clinique et catégorie administrative, compléter les sous-codes pertinents.'),
('Classifications et stades','Version, critères, unité, frontière entre classes et conséquence de prise en charge ; ne pas assembler deux scores incompatibles.'),
('Épidémiologie suisse puis européenne','Source, année, population, dénominateur, incidence/prévalence et limites ; aucune fréquence inventée pour remplir le plan.'),
('Normal vers pathologique','Décrire le fonctionnement normal utile puis la chaîne causale jusqu’aux signes et décisions. Anatomie, physiologie et biochimie selon leur pertinence réelle.'),
('Étiologies et facteurs de risque','Hiérarchiser causes fréquentes, urgentes et contextuelles ; expliciter terrain, mécanisme et critères de causalité plutôt qu’une liste sans ordre.'),
('Anamnèse et symptômes','Début, durée, évolution, symptômes associés, expositions et traitements ; fréquences avec source lorsqu’elles sont données.'),
('Examen clinique','Technique, résultat, signification et pièges ; sensibilités/spécificités seulement lorsque réellement documentées et applicables au contexte.'),
('Drapeaux rouges et urgences','Pour chaque alerte : déclencheur, seuil éventuel, gravité, délai et action. Une mention “urgence” sans conduite ne clôt pas la rubrique.'),
('Examens complémentaires','Indication, valeur de référence contextualisée en Suisse, unité, seuil, interprétation, délai et faux résultats ; formules importantes accessibles depuis leurs bases.'),
('Diagnostic différentiel','Alternatives plausibles de la présentation SSP et éléments discriminants, tests initiaux, urgence ou orientation ; séparer diagnostic de la maladie et différentiel de la situation.'),
('Prise en charge suisse','Conduite, lieu de soin, surveillance, options non médicamenteuses ; information professionnelle suisse du produit exact pour dose, voie, durée, maximum et adaptations.'),
('Complications et pronostic','Distinguer risque spontané et iatrogène, horizon temporel, facteurs pronostiques et interventions qui modifient ce risque.'),
('Suivi, prévention et dépistage','Population, périodicité, objectifs, arrêt ou intensification ; distinguer dépistage asymptomatique et investigation d’un symptôme.'),
('Situations particulières','Enfant, grossesse, personne âgée, insuffisance rénale/hépatique et polymédication lorsque pertinents ; marquer sans objet avec justification si nécessaire.'),
('Spécificités suisses','OFSP, Swissmedic, Suva/LAA, aptitude à la conduite, AI, LS/LiMA selon le problème ; version et contexte juridique précis.'),
('Critères formels du diagnostic','Critères complets, exclusions et version, présentés dans div.alert si le format du cours l’exige ; seuils cohérents avec le texte et les fenêtres.'),
('Paramètres clés chiffrés','Regrouper les valeurs utiles en div.key ; relier unités, normalité, seuils et calculs à leur explication et leur source.'),
('Sous-codes couverts','Inventorier les sous-codes de la catégorie et dire où ils sont traités ; un sous-code n’est pas un nouveau cours par défaut.'),
('Points d’examen fédéral','Raisonnement sur cas, décisions et pièges documentés ; les questions ne remplacent ni le chapitre ni la démonstration de couverture clinique.')]

def load_inputs():
 p=DEST/'plan-v2.json'
 if not p.exists():raise SystemExit('Missing required plan-v2.json; no stale plan rendered')
 plan=json.loads(p.read_text());proofs={}
 for fid in FRAGS:
  f=DEST/f'preuves-{fid}.json'
  if not f.exists():raise SystemExit(f'Missing required {f.name}')
  proofs[fid]=json.loads(f.read_text())
 return plan,proofs

def values(d,*keys,default=None):
 for k in keys:
  if k in d:return d[k]
 return default

def system_name(c):return FRAGS.get(c.get('fragment'),c.get('system','Périmètre non renseigné'))

def reference_manifest(pdf,plan,proofs):
 pdf.h('Documents qui fixent cette édition')
 rows=[('plan-v2.json',sha(DEST/'plan-v2.json'))]
 rows += [(f'preuves-{fid}.json',sha(DEST/f'preuves-{fid}.json')) for fid in FRAGS]
 rows += [(name,sha(DEST/name)) for name in ['README-V2.txt','prompt-commun-ia.yaml','graphe-ssp-diagnostics.json','couverture-265-ssp.json','tests-garde.log','recu-registre.json','progression-v2.json','AUTORISATIONS_GITHUB.csv'] if (DEST/name).exists()]
 pdf.table(['Fichier de référence','SHA-256'],rows,[155,CW-155])
 pdf.p('Les empreintes lient cette édition aux données préparées. Le PDF ne transforme pas une proposition de source en passage consulté, un contrôle technique en contrôle clinique, ni un plan d’audit en audit effectué.','small')


def language_rules(pdf):
 pdf.h('Exactitude médicale et qualité du français, ensemble')
 pdf.p('Chaque affirmation médicale utile vient d’un passage effectivement lu et applicable. L’ordre de recherche est suisse, puis européen ; une recommandation américaine ne devient pas une conduite locale par traduction. Les connaissances générales, les liens trouvés et les documents téléchargés conservent des statuts distincts de la lecture probante.')
 pdf.p('Le français avance du normal au mécanisme, du mécanisme aux signes, puis aux décisions. Privilégier les phrases complètes, les termes médicaux définis et les tableaux introduits. Conserver les négations, unités, seuils, conditions et degrés de certitude. Supprimer les répétitions qui n’ajoutent aucune information ; garder les approfondissements utiles dans les fenêtres.')
 pdf.p('Une réécriture est relue dans toutes ses surfaces : onglets, fenêtres, figures, tableaux, calculs et quiz. Une correction de dose oblige à relire ses adaptations et contre-indications, même si elles se trouvent dans un autre fichier. La qualité du rendu et la vérité du fond reçoivent des observations séparées.')


def workflow_states(pdf):
 pdf.table(['Dimension','États et preuve attendue'],[
 ('Rédaction','Non commencée ; en cours ; terminée pour une empreinte. Une présence de fichiers ne signifie pas achèvement.'),
 ('Audit Alpha','Planifié ; en cours ; réserves ; accepté pour des fichiers/empreintes précis. Le présent dossier ne prétend pas que les 104 audits sont faits.'),
 ('SSP','Lien proposé ; source repérée ; passage lu ; lien accepté/rejeté/non résolu. La couverture pédagogique brute n’est pas une validation clinique.'),
 ('Diffusion','Non publiée ; aperçu ; publication vérifiée par URL, build et SHA ; échec. Le statut de diffusion n’efface pas les réserves.'),
 ('Garde et serveur','Code/CI testé localement ; observation distante ; protection serveur imposée et vérifiée. Un HTTP403 interdit d’affirmer la dernière étape.')],[100,CW-100])


def course_card(pdf,c,audit=False):
 code=c.get('code','?');pdf.story.append(CondPageBreak(130));pdf.sub(f'{code} — {c.get("title","Intitulé absent")}')
 ssps=values(c,'ssp_documented','ssp','ssps',default=[])
 pdf.p(E(f'{system_name(c)} · chapitre {c.get("chapter","?")} — {c.get("chapter_title","")} · bloc {c.get("block","?")}'),'small')
 pdf.table(['Attribution / périmètre','Éléments propres à cette leçon'],[
 (f'{c.get("owner","À attribuer")} · {c.get("priority","priorité non chiffrée")} · {c.get("status","PLANIFIÉ")}',f'Mission : {c.get("assignment_id",c.get("mission_id","non renseignée"))}\nSSP proposées : {txt(ssps)}\nSous-codes : {txt(c.get("subcodes",[]))}'),
 ('Snapshot et livrables',f'Base : {c.get("base_commit",BASE)}\nRapport : {c.get("report_path","sortie propre à la mission, à réserver")}\nCours canonique : chapters/{code}/ ; glossaire : glossary/{code.lower()}.py')],[155,CW-155])
 files=c.get('source_files',{})
 if audit:
  pdf.p(E(f'{len(files)} fichiers sources inventoriés ; {c.get("html_bytes",0)} octets HTML ; {len(c.get("external_resources",[]))} ressources externes repérées. Ces ressources ne sont pas toutes réputées lues.'),'small')
  if files:pdf.table(['Source examinable','Empreinte SHA-256 du snapshot'],list(files.items()),[180,CW-180])
 else:
  basis=values(c,'inclusion_reason','reason','justification','priority_basis',default='Planification pédagogique : établir la justification clinique par lien typé et preuve avant de revendiquer une couverture.')
  pdf.p('<b>Justification et statut :</b> '+E(txt(basis)),'small')
  if c.get('preparation_existing'):pdf.p('Un travail préparatoire existe : le comparer et reprendre l’existant avant d’ouvrir une nouvelle rédaction.','small')

def normalize_sources(proof):
 raw=proof.get('sources',{});out=[]
 items=raw.items() if isinstance(raw,dict) else [(s.get('id',str(i+1)),s) for i,s in enumerate(raw)]
 for ident,s in items:
  if isinstance(s,str):s={'url':s}
  out.append(dict(s,id=str(ident)))
 return out

def normalize_edges(proofs):
 edges=[]
 for fid,p in proofs.items():
  raw=p.get('graph',p.get('links',[]))
  if isinstance(raw,dict):raw=raw.get('edges',raw.get('links',[]))
  for i,e in enumerate(raw):
   if not isinstance(e,dict):continue
   n=dict(e);n['_fragment']=fid;n['_id']=e.get('id',f'{fid}:ligne-{i+1:03d}')
   n['_code']=values(e,'code','code3','category','category_3char',default='')
   n['_ssp']=values(e,'ssp','ssp_id',default=None)
   if isinstance(n['_ssp'],str) and n['_ssp'].isdigit():n['_ssp']=int(n['_ssp'])
   n['_type']=values(e,'relation','relation_type','type',default='non typé dans la source')
   n['_entity']=values(e,'diagnostic_or_concept','clinical_diagnosis','diagnostic_entity','entity','diagnosis',default='Entité précisée dans la source JSON')
   n['_why']=values(e,'rationale','justification','reason','condition',default='Justification non renseignée dans cette arête')
   n['_status']=e.get('status','statut non renseigné')
   ev=e.get('evidence',[])
   if not ev:
    ev=[{'source_id':e.get('source_id',e.get('justification_id','source directe')),'url':e.get('source_url',''),'section':values(e,'source_section_lue','section_read','section','source_section',default='section non renseignée')}]
   n['_evidence']=ev;edges.append(n)
 return edges

def source_register(pdf,proofs):
 for fid,p in proofs.items():
  pdf.page('Sources et limites — '+FRAGS[fid])
  pdf.p('Ce registre reproduit la portée de lecture déclarée dans le dossier de preuves. Un référencement de société, une page d’information hospitalière et une recommandation clinique ont des fonctions différentes. Aucune portée thérapeutique n’est ajoutée par cette mise en page.')
  for s in normalize_sources(p):
   pdf.sub(s['id']+' — '+str(s.get('title',s.get('publisher','Source'))))
   meta=[]
   for label,keys in [('URL',['url']),('Version / consultation',['version','date','consulted','accessed','retrieved_at']),('Éditeur / nature',['publisher','publisher_type','country']),('Lecture réelle',['section_read','read_scope','read_sections','sections_read','diagnostic_passage_read','access_status','evidence_status']),('Limites',['limitations','limits','limit','limite','scope_limit']),('Empreinte',['sha256_response_bytes','sha256','response_sha256'])]:
    z=[txt(s[k]) for k in keys if k in s and s[k] is not None]
    if z:meta.append((label,' ; '.join(z)))
   pdf.table(['Élément','Trace'],meta,[110,CW-110])
  limits=values(p,'bounded_reserves','limitations','important_gaps',default=[])
  if limits:
   pdf.h('Réserves du recontrôle borné')
   for l in limits:pdf.p('• '+E(txt(l)),'small')
  access=values(p,'access_limits','access_limitations',default=[])
  if access:
   pdf.h('Accès incomplets ou impossibles')
   for a in access:pdf.p(E(txt(a)),'small')

def audit_pdf(plan,proofs):
 p=PDF('MEDINA — Audit Alpha V2 : 104 leçons, preuves et français','AUDIT ALPHA V2')
 p.page('Audit Alpha V2\n104 leçons existantes')
 p.p('52 leçons à Codex · 52 leçons à Claude','h2')
 p.box('<b>PLANIFIÉ, NON LANCÉ.</b> Aucun audit médical des 104 leçons n’est déclaré effectué. La répartition est sans audit croisé Codex–Claude : chaque responsable assume ses leçons attribuées. La préparation d’un manifeste ne vaut ni activation de mission, ni validation médicale humaine.')
 p.p('Ce volume donne le contrat d’audit, la matrice de 20 rubriques, les exigences médicales et de langue, l’allocation complète et les empreintes des sources examinables. Il sert à produire des constats traçables et des corrections proportionnées, sur une version précise.')
 p.p('Snapshot de planification : '+E(plan.get('snapshot_commit',BASE)),'small')
 if (DEST/'progression-v2.json').exists():
  prog=json.loads((DEST/'progression-v2.json').read_text());p.p(E(f'Publication vérifiée : {prog["public_existing_courses_verified"]} cours existants, contrôle du {prog["checked_at"]} ; source et build publics : {prog["public_site_source_commit"]}. Audit Alpha NON_COMMENCÉ ; la publication ne le remplace pas.'),'small')
 p.table(['Système','Leçons','Codex','Claude'],[(s['name'],s['audit_count'],s['audit_split'].get('Codex',0),s['audit_split'].get('Claude',0)) for s in plan['systems']],[CW-150,50,50,50])
 p.h('Mode d’emploi')
 p.p('Lire d’abord le contrat et la matrice ; choisir la mission attribuée ; vérifier son approbation et sa réservation avant toute correction ; examiner le snapshot ; livrer un rapport par leçon. Les lots regroupent la logistique, sans attendre toutes les leçons du lot pour remettre un travail terminé.')
 reference_manifest(p,plan,proofs)
 p.page('Le contrat : précision, responsabilité et limites')
 language_rules(p)
 p.h('Audit sans croisement')
 p.p('L’allocation 52/52 respecte la consigne de ne pas imposer d’audit croisé entre les deux IA. Elle ne permet pas de présenter une auto-relecture comme indépendante. Un sous-agent éventuel reste dans le périmètre et sous la responsabilité de sa mission ; son intervention doit être autorisée et attribuée séparément. La séparation des lecteurs se rapporte à des personnes/sessions et à des empreintes réelles, pas seulement au nom d’un fichier.')
 p.h('Priorités de constat')
 p.table(['Niveau','Déclencheur / action'],[
 ('Bloquant pour la version','Dose, contre-indication, diagnostic, urgence ou source fausse pouvant modifier la décision ; corriger et recontrôler toutes les surfaces touchées avant de présenter la version comme acceptée.'),
 ('Majeur','Différentiel important absent, seuil sans contexte, normalité ambiguë, sous-code utile non traité, recommandation périmée ; action et réserve identifiées.'),
 ('Éditorial ou rendu','Français, hiérarchie, explication, accessibilité, lien ou fenêtre ; vérifier que la correction conserve exactement le sens médical.'),
 ('Non établi','Preuve introuvable ou non applicable ; noter les recherches et la conséquence, sans transformer une absence de preuve en certitude ou en suppression automatique.')],[115,CW-115])
 p.h('Une réserve locale ne suspend pas tous les cours')
 p.p('Délimiter code, passage, fichiers, empreinte, risque et condition de résolution. Une incertitude propre à N18 ne suspend pas D50 ou une autre tâche indépendante. Les réserves transversales sont justifiées par leurs consommateurs réels. Vial reste l’autorité prioritaire ; la parité administrative ne crée pas un droit d’écraser un travail concurrent.')
 p.page('La matrice de 20 rubriques : preuve attendue')
 p.p('Pour chaque rubrique : couvert avec passage et ancrage ; sans objet motivé ; ou lacune avec recherche tentée. Les 20 cases restent ouvertes jusqu’à la lecture. L’acceptation d’un lien SSP particulier ne revalide pas toute la catégorie CIM, tous ses sous-codes ni son ancien mapping.')
 for i,(title,expectation) in enumerate(MATRIX,1):
  p.sub(f'{i:02d}. {title}');p.p(E(expectation));p.p('Trace : source et section/page · population et version · fichier/onglet/identifiant · constat · correction ou réserve · résultat de relecture.','small')
 p.page('Dossier probant d’une leçon')
 p.table(['Pièce','Contenu concret'],[
 ('Manifeste de mission','ID, responsable, conversation, rôle audit, génération, code, base SHA40, branche, chemins de sorties propres ; mission active dans la base de confiance, réservation courante.'),
 ('recherche.md','Questions cliniques, 20 rubriques, sources prioritaires, recherches réellement tentées, accès refusés, divergences et lacunes.'),
 ('sources.json','URL, éditeur, titre, version, date consultée, passage réellement lu, population, portée et limites ; empreinte si disponible ; information professionnelle suisse précise pour médicament.'),
 ('rapport.json','Constats numérotés, gravité, emplacement, affirmation, source/passage, décision, correction proposée, résultat contrôlé et réserves. Trois états séparés : rédaction, diffusion, audit.'),
 ('Contrôles techniques','Commandes réellement exécutées, code de sortie, version de l’outil, SHA des fichiers testés et portée ; deux captures réelles si exigées : ouverture puis fenêtre explicative.'),
 ('Correction distincte','L’audit écrit ses rapports, pas les sources. Une correction nécessite une mission source approuvée du même responsable, une génération/réservation courante et le reçu de version autorisant sa publication.')],[122,CW-122])
 p.h('Cache et réutilisation honnête')
 p.p('Réutiliser une source par empreinte et passage applicable économise la recherche, mais ne crée pas une nouvelle lecture. Relire si version, contexte, population, dose, décision ou dépendance a changé. Conserver qui a lu quoi, quand et pour quel usage. Éviter de recopier des textes entiers dans chaque rapport ; citer la section et une synthèse courte fidèle.')
 workflow_states(p)
 p.page('Séquence d’exécution par leçon')
 for title,body in [
 ('1. Fixer le snapshot','Comparer les empreintes ci-après à celles de la branche d’audit. Lire le préambule actuel du projet et les exigences du Prompt. Ne pas traiter une instruction historique remplacée comme un nouvel ordre.'),
 ('2. Identifier le risque','Commencer par urgences, diagnostics et traitements susceptibles de changer une décision ; choisir les passages probants. Relever aussi les ruptures de progression et de français qui rendent le cours difficile à utiliser.'),
 ('3. Compléter la matrice','Renseigner les 20 rubriques sans cases favorables préremplies. Pour les SSP, examiner le graphe typé et les alternatives, pas un compteur de mots-clés.'),
 ('4. Livrer le rapport','Un constat par problème démontré, avec emplacement et preuve ; séparer correction sûre et question non résolue. Une leçon peut être remise indépendamment du lot.'),
 ('5. Corriger sous mission distincte','La mission audit ne modifie pas les sources. L’approbation trusted-base et la réservation des chemins sont obtenues avant la mission de correction. Les gardes historiques de publication restent en place tant que le reçu scoped n’est pas prêt.'),
 ('6. Recontrôler la version corrigée','Relire le passage et ses dépendances, vérifier liens/construction/rendu réellement, attacher les preuves aux nouvelles empreintes ; conserver les anciens rapports à leurs versions. Maintenir une vérification finale proportionnée au risque.')]:p.h(title);p.p(body)
 p.page('Lots logistiques et pilote')
 p.p('Pilote proposé : '+E(txt(plan.get('pilot_audit',[])))+'. Il sert à calibrer la profondeur, les preuves et l’effort avant montée en charge. Au départ, au plus deux missions source simultanées par responsable ; les lectures et sorties de rapports restent indépendantes lorsque leurs chemins le permettent.')
 p.table(['Lot','Responsable','Leçons'],[(x['id'],x['owner'],txt(x['codes'])) for x in plan.get('audit_lots',[])],[200,75,CW-275])
 for fid in FRAGS:
  p.page('Inventaire d’audit — '+FRAGS[fid])
  items=[x for x in plan['audit'] if x['fragment']==fid]
  p.p(E(f'{len(items)} leçons ; allocation '+txt(dict(Counter(x['owner'] for x in items)))),'small')
  for c in items:course_card(p,c,True)
 p.page('Clôture d’une leçon et contrôle final')
 p.table(['Décision','Conditions vérifiables'],[
 ('Accepté pour cette version','Rubriques traitées ou sans objet justifié ; preuves applicables ; aucune réserve bloquante ; français et surfaces relus ; contrôles pertinents réellement passés ; rapport lié aux empreintes finales.'),
 ('Accepté avec réserves','Portée autorisée explicitement et réserves visibles, localisées, avec effets et actions. Ne pas confondre publication provisoire et validation clinique finale.'),
 ('À reprendre','Erreur ou lacune non résolue ; attribution et branches conservées ; la tâche indépendante suivante peut avancer sans effacer ce travail.'),
 ('Version modifiée après audit','Ancien rapport conservé. Déterminer les preuves affectées par le diff et recontrôler le contenu ; aucun héritage automatique du statut accepté.')],[125,CW-125])
 p.p('Les mesures en amont réduisent les défauts ; elles ne garantissent ni zéro erreur, ni un audit final négligeable. Aucun document de ce dossier ne remplace une validation médicale humaine.')
 p.save('AUDIT_ALPHA_V2.pdf')

def production_pdf(plan,proofs,edges):
 p=PDF('MEDINA — Production des fragments V2 : attribution et preuves SSP','PRODUCTION V2')
 p.page('Production V2\n154 nouvelles leçons')
 p.p('77 leçons à Codex · 77 leçons à Claude · 12 réserves distinctes','h2')
 p.box('<b>Périmètre conservatoire, non officiel :</b> 247 catégories historiques maintenues + 11 ajouts à liens diagnostiques documentés = 258 catégories. Les 104 cours existants relèvent de l’audit Alpha ; les 154 autres relèvent de la production. Les 12 réserves (6/6) restent à arbitrer et ne sont pas comptées parmi ces 258.')
 p.p('Ce plan n’a pas lancé la rédaction ni la correction des contenus médicaux. Les 11 ajouts réparent des omissions documentées dans une revue bornée ; ils ne certifient ni l’exhaustivité du différentiel, ni une liste officielle de pathologies exigées à l’examen fédéral.')
 p.table(['Fragment','Cible','Audit','Production','Réserve'],[(s['id'],s['conservative_categories'],s['audit_count'],s['production_count'],s['reserve_count']) for s in plan['systems']],[CW-200,50,50,55,45])
 p.h('Repères d’utilisation')
 p.p('Les allocations par chapitre et par leçon suivent. Le registre des sources rapporte les sections réellement lues et leurs limites ; le protocole distinct contient l’annexe des 265 SSP et le graphe détaillé. Le JSON est la référence exploitable par les outils ; le PDF rend les décisions et lacunes consultables.')
 reference_manifest(p,plan,proofs)
 p.page('Comprendre les nombres avant de produire')
 p.table(['Nombre','Signification et limite'],[
 ('265 SSP','Liste des situations de départ PROFILES 2017. Symptômes, anomalies, contextes et compétences ; pas 265 maladies et pas une table officielle CIM.'),
 ('247 + 11 = 258','Socle historique maintenu par prudence, plus ajouts documentés. Une catégorie peut n’avoir qu’une sous-entité soutenue ; les anciens tags ne sont pas tous revalidés.'),
 ('104 + 154 = 258','Cours existants à auditer et catégories nouvelles à produire. Plusieurs sous-codes d’une catégorie se traitent dans la même leçon mère.'),
 ('154 = 77 + 77','Répartition Codex/Claude sur cours entiers. L’égalité globale tolère un écart local d’une leçon dans un fragment impair et le compense ailleurs.'),
 ('12 = 6 + 6','Réserves éditoriales ou de correspondance ; absence de preuve nouvelle ne signifie pas absence d’exigibilité ni recommandation de suppression.'),
 ('270 missions préparées','104 audit + 154 production + 12 réserves. Manifestes planifiés de génération zéro ; ils ne sont pas des autorisations actives ni des réservations obtenues.'),
 ('291 historique / 398 simulé','L’annexe globale ancienne affiche291, mais son générateur sur l’arbre étudié sélectionne398 pour265SSP. Ce set-cover non validé ne sert pas de total clinique de ces quatre fragments.')],[116,CW-116])
 p.h('Sous-codes, cours et renvois')
 p.p('Normaliser les codes à trois caractères après contrôle de leur validité CIM-10-GM. Une SSP supplémentaire, un sous-code ou un renvoi vers un autre système n’ajoute pas automatiquement un cours. Le propriétaire canonique reste unique. Un champ covers n’autorise à fusionner les unités qu’après vérification du contenu couvert ; documenter les diagnostics réellement traités séparément du nombre de cours.')
 p.h('Les onze ajouts documentés')
 for s in plan['systems']:
  p.p('<b>'+E(s['id']+' — '+s['name'])+'</b> : '+E(txt(s.get('added_categories',[]))), 'small')
 p.page('Le contrat de rédaction et de preuve')
 language_rules(p)
 p.h('Plan clinique de chaque leçon')
 p.p('Appliquer les 20 rubriques détaillées dans Audit Alpha V2 : question clinique, définition/périmètre, classifications, épidémiologie, normal vers pathologique, causes/risques, anamnèse, examen, urgences, examens, différentiel, prise en charge suisse, complications, suivi, situations particulières, spécificités suisses, critères diagnostiques, paramètres chiffrés, sous-codes et objectifs SSP. Un sommaire rempli ne prouve pas que les questions sont résolues.')
 p.h('Démarrer par la source, puis écrire')
 p.p('Définir les SSP utiles et les diagnostics à différencier ; lire la source primaire et la section nécessaires ; consigner la preuve ; rédiger en français ; vérifier chiffres et conditions ; construire les fenêtres, figures et questions à partir du texte stabilisé. Une lacune de source reste localisée et explicite. Ne pas ajouter une conduite thérapeutique à partir d’une simple page de présentation diagnostique.')
 p.h('Entrée et sortie : Prompt et contrôles')
 p.p('En entrée, confirmer le Prompt applicable, les chemins, la mission, le snapshot et les sources nécessaires. En sortie, renseigner la matrice, relire les dépendances et surfaces, exécuter les contrôles pertinents et consigner leurs résultats réels. La baisse des erreurs en amont ne justifie pas de supprimer la vérification finale proportionnée au risque.')
 workflow_states(p)
 p.page('Allocation par système et chapitre CIM')
 p.table(['Fragment / chapitre','Audit C / Cl','Production C / Cl','Réserve C / Cl'],[(f'{x["fragment"]} · {x["chapter"]}\n{x["title"]}',f'{x["audit_Codex"]} / {x["audit_Claude"]}',f'{x["production_Codex"]} / {x["production_Claude"]}',f'{x["reserve_Codex"]} / {x["reserve_Claude"]}') for x in plan['chapter_summary']],[CW-210,65,75,70])
 p.page('Pilote, capacité et lots de production')
 p.p('Pilote proposé : '+E(txt(plan.get('pilot_production',[])))+'. Les lots ont une taille logistique de une à quatre leçons. Ils ne créent pas une barrière globale : une leçon complète se livre séparément. Au départ, au plus deux missions source simultanées par responsable ; recalibrer l’effort après le pilote et conserver une seule autorité active par cours et chemin.')
 p.table(['Lot','Responsable','Cours'],[(x['id'],x['owner'],txt(x['codes'])) for x in plan['production_lots']],[205,70,CW-275])
 p.page('Se préparer sans toucher aux autres systèmes')
 p.table(['À faire avant l’écriture','Raison et preuve'],[
 ('Réserver la mission','Mission approuvée dans main de confiance, génération positive, branche et conversation déclarées ; acquire obtient une réservation distante à avance rapide avant le travail source.'),
 ('Protéger le périmètre','Branches/worktrees/sorties propres. Audit écrit ses preuves seulement ; production écrit ses cours attribués ; intégrateur réserve les catalogues partagés.'),
 ('Conserver les versions','Pas de réécriture d’anciennes branches par copie entière. Un cours incomplet ou brouillon se reprend après comparaison ; les reçus historiques restent attachés à leurs octets.'),
 ('Préparer la publication corrigée','Le reçu de publication “en état” exige égalité des sources historiques. Une version médicale modifiée demande un reçu scoped et des gardes adaptées/testées avant publication ; ce travail reste un jalon ouvert.'),
 ('Vérifier le serveur','La CI locale préparée ne suffit pas à imposer PR/checks. Administration403 laisse la protection distante à établir ; aucune promesse d’inviolabilité ou de zéro collision.')],[150,CW-150])
 bycode=defaultdict(list)
 for e in edges:bycode[(e['_fragment'],e['_code'])].append(e)
 for fid in FRAGS:
  p.page('Cours à produire — '+FRAGS[fid])
  s=next(s for s in plan['systems'] if s['id']==fid)
  p.p(E(f'{s["production_count"]} cours : Codex {s["production_split"].get("Codex",0)}, Claude {s["production_split"].get("Claude",0)}. {s["reserve_count"]} réserves séparées.'),'small')
  for c in [x for x in plan['production'] if x['fragment']==fid]:
   course_card(p,c,False)
   local=bycode[(fid,c['code'])]
   p.p('<b>SSP documentées dans la revue bornée :</b> '+E(txt(c.get('ssp_documented',[])))+' · <b>anciens tags non revalidés :</b> '+E(txt(c.get('legacy_ssp_unvalidated',[]))), 'small')
   p.p('<b>État des preuves :</b> '+E(c.get('evidence_status','non renseigné'))+'. Une entité soutenue ne valide pas toute sa catégorie.','small')
   if local:
    rows=[]
    for e in local:
     refs=[]
     for ev in e['_evidence']:
      refs.append(str(ev.get('source_id','source'))+' · '+str(values(ev,'section','source_section','section_read',default='section dans JSON')))
     rows.append((f'SSP {e["_ssp"]} · {e["_type"]}',e['_entity'],' ; '.join(refs)))
    p.table(['Situation / lien','Entité examinée','Section probante'],rows,[115,150,CW-265])
   else:p.p('Lacune explicite : aucun lien clinique pour cette catégorie n’est retenu dans le graphe transmis. La catégorie historique reste conservée ; rechercher et documenter avant toute revendication de couverture.','small')
 p.page('Les 12 réserves : ni exclues ni déjà autorisées à produire')
 p.p('Chaque réserve demande une décision éditoriale et, pour une inclusion comme diagnostic, une source lue et un lien typé. Sa mission reste une préparation/arbitrage ; aucune production canonique n’est rendue active par sa présence dans ce tableau.')
 for c in plan['reserve']:course_card(p,c,False)
 source_register(p,proofs)
 p.page('Recalcul conservatoire et bilan de livraison')
 p.p('Prendre l’union des catégories retenues dans les quatre systèmes, conserver leur propriétaire canonique, puis calculer les ajouts absents du socle. Ne jamais additionner les nombres de lignes des graphes, les relations multiples à une SSP ou les sous-codes. Ne pas retirer d’anciennes catégories simplement pour stabiliser un nombre ancien.')
 p.table(['Calcul','Résultat du plan v2'],[('Socle historique',247),('Ajouts à liens documentés',11),('Cible conservatoire',258),('Cours existants / audit',104),('Cours à produire',154),('Réserves à arbitrer, hors cible',12),('Total des missions préparées',270)],[CW-140,140])
 p.p('Le bilan final doit encore distinguer catégories, unités de cours, sections effectivement rédigées, liens documentés et démarches cliniques contrôlées. Le présent recontrôle ne constitue pas une preuve d’exhaustivité des265SSP ni l’audit des104cours.')
 p.save('PRODUCTION_FRAGMENTS_V2.pdf')

def canonical_edges():
 raw=json.loads((DEST/'graphe-ssp-diagnostics.json').read_text())
 out=[]
 for e in raw['graph']:
  n=dict(e);n.update(_fragment=e['fragment_analyse'],_id=e['id'],_code=e['code3'],_ssp=e['ssp'],_type=e['relation'],_entity=e['entite_clinique'],_why=e['justification'],_status=e['statut_preuve_source'])
  n['_evidence']=[dict(x,section=x.get('section_lue','section non renseignée')) for x in e['sources']]
  out.append(n)
 return out

def protocol_pdf(plan,proofs,edges):
 p=PDF('MEDINA — Protocole anti-collision V2 : sessions, SSP, preuves et reprise','PROTOCOLE V2')
 coverage=json.loads((DEST/'couverture-265-ssp.json').read_text());registry=json.loads((DEST/'recu-registre.json').read_text())
 p.page('Protocole V2\nPrévenir les collisions et prouver le travail')
 p.box('<b>Réduire les collisions et les erreurs, sans promettre zéro absolu.</b> Un auteur actif par cours/chemin, des missions approuvées avant le travail, un registre distant à avance rapide et une intégration séquentielle rendent la coordination vérifiable. Les droits GitHub actuels ne permettent pas d’affirmer une protection serveur imposée : Administration renvoie403.')
 p.p('Le protocole s’applique aux quatre systèmes S08/S05/S04/S06. Une conversation, même issue de la même IA qu’une autre, est une session concurrente. Les anciens systèmes restent conservés hors de ce recontrôle ; aucune ancienne branche entière n’est fusionnée pour aller plus vite.')
 p.table(['État réel documenté','Portée'],[
 ('Garde implémentée et tests locaux',f'{TEST_N} tests OK, dont deux processus/clones en concurrence sur bare local. Lire tests-garde.log et revue-garde.txt ; cela ne simule pas les autorisations du vrai GitHub.'),
 ('Registre distant initialisé',f'{registry["branch"]}\nCommit {registry["initial_commit"]}\nVérification distante : {registry["remote_verified"]} ; réservations initiales : {registry["initial_reservations"]} ; aucun force-push.'),
 ('Protection serveur non vérifiée','server_protection_verified=false. HTTP403 sur protection historique ; rulesets publics lus vides. Une règle proposée n’est pas une règle active.'),
 ('Travail médical non lancé','104 audits préparés, pas réalisés. 154 productions et 12 réserves planifiées ; génération zéro ne vaut pas mission active.')],[153,CW-153])
 reference_manifest(p,plan,proofs)
 p.page('Les unités de coordination : mission, cours, chemin et version')
 p.table(['Objet','Contrat'],[
 ('Mission','ID stable ; rôle author/audit/integrator ; responsable de répartition Codex ou Claude ; acteur/conversation ; base SHA40 ; branche ; génération positive ; chemins autorisés ; approbation active dans la base trusted.'),
 ('Cours','Catégorie CIM trois caractères et ses sous-codes ; propriétaire canonique unique. covers/alias/renvois examinés pour prévenir un doublon sémantique même si les noms de fichiers diffèrent.'),
 ('Chemin','Répertoire propre et descendants ; la collision parent/enfant compte. Audit et auteur peuvent lire la même source mais ne partagent jamais la même sortie de rapport.'),
 ('Version','SHA de base, SHA livré, SHA intégré, empreintes SHA256 des fichiers et sources utiles. Un succès sur un ancien SHA ne couvre pas automatiquement le nouveau.'),
 ('Responsabilité','Chaque responsable garde la provenance de ses auteurs et lecteurs. Un sous-agent n’autorise ni double attribution ni travail simultané sur un fichier partagé.'),
 ('Autorité','Parité Codex/Claude dans les règles du projet ; Vial prioritaire. Ces déclarations ne donnent ni token GitHub, ni permission Administration, ni preuve de l’identité réelle d’un modèle.')],[100,CW-100])
 p.h('Ce qu’isole un worktree')
 p.p('Le répertoire, HEAD et l’index sont propres au worktree ; les objets/références et une partie de la configuration Git restent partagés. Ne pas déplacer la branche d’une autre tâche, nettoyer globalement les worktrees, modifier la configuration commune ou partager une sortie de build. Sur une autre machine, utiliser un clone distinct et le même registre distant.')
 p.h('Ce qu’un audit lecture seule signifie ici')
 p.p('L’audit n’a des chemins réservés que pour ses preuves et son rapport. Il examine un snapshot figé et son diff ne peut toucher les sources protégées. Ce contrat n’est pas une sandbox du système d’exploitation : le détenteur d’un accès filesystem ou d’un token peut tenter autre chose ; les contrôles et règles serveur doivent rendre ces écarts visibles ou les refuser.')
 p.page('Répartition des fichiers : sources propres et intégration partagée')
 p.table(['Propriétaire de la mutation','Exemples et contraintes'],[
 ('Auteur d’une leçon','chapters/CODE ; glossary/code.py ; ressources spécifiques attribuées ; dossier execution/ID. Le manifeste doit nommer les chemins réels, pas un joker qui ouvre un système entier.'),
 ('Auditeur','docs/collaboration/ssp-v2/execution/ID uniquement pour rapport, recherche et preuves attribuées. Aucune correction source dans cette mission.'),
 ('Intégrateur attribué','chapters.json et les seuls fichiers partagés explicitement réservés ; préserver exactement les lignes de catalogue hors cours attribués. La mutation nosology reste limitée aux quatre fichiers autorisés, selon configuration.'),
 ('Coordinateur de gouvernance','Configuration garde et manifestes, dans une PR de gouvernance séparée des modifications source/catalogue. Il ne peut modifier sa propre approbation.'),
 ('Documentation de préparation','Les documents ordinaires hors execution sont exemptés par la garde de périmètre. Le garde ne déduit pas le sens d’un rapport copié dans un autre dossier ; ce choix doit rester explicite.')],[135,CW-135])
 p.h('Conflits détectables')
 p.p('Une réservation active bloque les autres mutations du même cours et les chemins égaux ou parent/enfant. Une mission “chapters/I63” entre en conflit avec “chapters/I63/I63_a.html” ; “chapters/I630” n’est pas le même préfixe. Les symlinks et sous-modules sont refusés aux ancêtres des chemins protégés pour éviter une redirection hors périmètre.')
 p.h('Identité : ce qui est déclaré et ce qui est authentifié')
 p.p('actor, conversation et owner sont des champs déclaratifs contrôlés pour cohérence ; un nom Codex/Claude n’authentifie pas le processus qui l’a fourni. Le contrôleur de confiance doit lier mission et branche au vrai compte/installation GitHub, à l’auteur PR, au dépôt head numérique et à une politique de fork. Avec des credentials partagés, l’attribution modèle/session ne peut pas être prouvée par cette seule garde.')
 p.page('Le registre Git distant : réservation sérialisée sans écrasement')
 p.p('Le registre vit sur refs/heads/medina/session-registry et conserve les réservations actives et libérées. acquire lit la configuration et le manifeste approuvé dans la base trusted, récupère la tête distante, vérifie la génération et les collisions, ajoute une entrée, crée un commit enfant de cette tête, puis tente un push ordinaire. Aucun force-push, aucune réécriture et aucun retry automatique ne remplace le travail concurrent.')
 p.table(['Situation','Résultat attendu'],[
 ('Deux clones ont la même ancienne tête','Deux commits frères ne peuvent tous deux avancer la même référence à avance rapide. Un gagne ; l’autre reçoit le refus Git, relit l’état et refait une décision explicite.'),
 ('Réservation déjà obtenue','Nouvelle acquisition du même ID/génération refusée. Une nouvelle génération doit être strictement supérieure aux anciennes générations source pertinentes.'),
 ('Libération périmée','--expected-registry permet de refuser une libération si le registre a avancé depuis sa revue ; génération et raison explicite requises.'),
 ('Mission interrompue','Pas de libération automatique sur expiration ou silence. Conserver SHA/diff/worktree, clôturer ou transférer explicitement puis libérer la réservation.'),
 ('Lecture d’un registre altéré','Vérifier schéma, unicité des réservations actives, collisions, hash du manifeste et génération ; la branche registre doit elle aussi être protégée contre des écritures non autorisées.'),
 ('Administrateur hostile ou force-push autorisé','Le mécanisme normal à avance rapide ne suffit pas contre celui qui peut remplacer la référence ou changer les règles. Aucun caractère inviolable n’est revendiqué.')],[150,CW-150])
 p.h('Une file durable d’intégration distincte')
 p.p('Une réservation n’est pas un reçu de livraison. Garder chaque demande d’intégration dans un registre durable jusqu’au reçu indiquant acceptation, rejet ou reprise. Actions concurrency seul peut remplacer une exécution en attente ; il n’est pas une file conservant nécessairement toutes les demandes. Dans ce dépôt personnel public, utiliser strict/up-to-date et un intégrateur séquentiel ; merge queue n’est pas disponible pour cette propriété.')
 p.page('Commandes : statut réel et modèles de démarrage')
 p.box('<b>La syntaxe ci-dessous est un modèle paramétré, pas une réservation exécutée sur des cours.</b> Les aides CLI ont été consultées ; les scénarios de commande sont couverts par les tests locaux cités. Le reçu distant prouve uniquement l’initialisation du registre avec zéro réservation. Remplacer les champs par le manifeste approuvé exact et rafraîchir origin/main avant de fixer BASE.')
 p.code(['python3 tools/ai_session_guard.py --help','python3 tools/ai_session_guard.py acquire --help','python3 tools/ai_session_guard.py start --help','python3 tools/ai_session_guard.py check --help'])
 p.h('1. Rafraîchir et réserver, depuis un dépôt propre')
 p.code(['git fetch origin','BASE=$(git rev-parse origin/main)','python3 tools/ai_session_guard.py status --base "$BASE"','python3 tools/ai_session_guard.py acquire MISSION --base "$BASE"'])
 p.p('MISSION doit déjà être active dans .medina/missions/MISSION.json de la base. Les 270 manifestes planifiés de génération0 ne remplissent pas ce critère. L’initialisation d’une branche registre absente n’est pas une option acquire : l’absence provoque volontairement un échec.','small')
 p.h('2. Créer un espace isolé et valider l’entrée')
 p.code(['git worktree add -b BRANCHE_EXACTE_DU_MANIFESTE /tmp/medina-MISSION "$BASE"','python3 tools/ai_session_guard.py start MISSION --base "$BASE" --actor IA_DECLAREE --conversation CONVERSATION_EXACTE --worktree /tmp/medina-MISSION'])
 p.p('start exige branche assignée, HEAD exactement à la base, worktree propre et appartenant au dépôt, plus actor/conversation cohérents et réservation courante. Ne pas combiner comme un seul protocole conversation_workspace.py et ce gestionnaire : l’autre outil génère ses propres identifiants et noms de branche, sans lien automatique avec la mission centrale.','small')
 p.page('Commandes : contrôler, livrer et libérer')
 p.h('3. Contrôler le candidat, sans exécuter son code en contexte privilégié')
 p.code(['python3 tools/ai_session_guard.py check --base SHA_BASE_APPROUVEE --head SHA_CANDIDAT --branch BRANCHE_EXACTE_DU_MANIFESTE'])
 p.p('SHA_BASE_APPROUVEE et SHA_CANDIDAT sont des SHA40 existants. Un contrôleur de confiance fournit ces valeurs depuis l’événement GitHub et la base vérifiée ; des arguments arbitraires fournis localement ne prouvent pas leur authenticité. --registry-sha accepte un snapshot de registre déjà récupéré par ce contrôleur, pas un registre candidat choisi pour contourner la réservation.')
 p.h('4. Livrer une version précise')
 p.p('Conserver le SHA livré, la base, les chemins, les empreintes et les résultats ; pousser la branche de tâche et ouvrir la PR attribuée selon le workflow autorisé. Une ouverture de PR n’est pas une publication ; une CI verte n’est pas un audit médical. Une mutation partagée nécessite la mission intégrateur ; ne pas élargir les paths d’une mission auteur après coup pour éviter une erreur de garde.')
 p.h('5. Libérer après conservation explicite')
 p.code(['python3 tools/ai_session_guard.py release MISSION --base SHA_BASE_APPROUVEE --generation GENERATION --reason "Travail conservé, reçu et décision identifiés" --expected-registry SHA_REGISTRE_RELU'])
 p.p('La libération ajoute state=released et release_reason à la réservation historique ; elle ne supprime pas les fichiers ni leur provenance. L’ancienne génération ne peut pas être réacquise. Pour reprendre, obtenir une approbation de génération supérieure dans main puis acquérir cette génération. En cas de refus, ne pas forcer : lire l’état exact et résoudre la divergence de réservation.')
 p.h('Commandes de tests et portée de preuve')
 p.code(['python3 -m unittest discover -s tests -p test_ai_session_guard.py -v'])
 p.p(f'Le reçu tests-garde.log contient {TEST_N} tests OK en {TEST_SECS}s. Cette commande reproduit le périmètre du fichier de tests ; elle est citée ici sans prétendre à une nouvelle exécution de cette édition PDF. Les fixtures utilisent des dépôts temporaires et des bare locaux ; elles ne rendent pas main protégé sur GitHub.','small')
 p.page('Les scénarios réellement couverts par les tests')
 tests=[
 ('Mission autorisée / identité déclarée','Auteur inconnu mais attribué peut démarrer et changer sa source ; actor/conversation incohérents refusés.'),
 ('Périmètre documentaire / ancien système','Planning ordinary et ancien système seul restent hors garde ; modification mixte d’un ancien système dans mission quatre systèmes refusée.'),
 ('Confiance de la base','Mission nouvelle dans le candidat, modification de sa propre approbation et config désactivant sa propre source sont refusées.'),
 ('Catalogue partagé','Mission intégrateur obligatoire ; comparaison structurée des lignes conserve exactement les cours hors mission.'),
 ('Gouvernance séparée','Intégrateur préapprouvé ; pas d’auto-approbation ni de modification gouvernance couplée à source/catalogue.'),
 ('Génération et libération','Registre avancé, ancienne génération, réacquisition et libération périmée refusés ; raisons et historique conservés.'),
 ('Chemins et lectures simultanées','Parent/enfant en collision ; cours disjoints acceptés ; audit ne possède que ses sorties et n’écrit pas les sources.'),
 ('Sorties execution et symlinks','Rapports execution exigent mission ; symlinks de source et parents protégés refusés, y compris ancêtres sans enfant précédemment suivi.'),
 ('Worktree de démarrage','Branche exacte, HEAD de base, propreté et appartenance au dépôt vérifiés.'),
 ('Concurrence réelle à deux processus','Deux clones issus du même parent, barrière avant push : un seul commit distant accepté. Pas de lost update.'),
 ('Relais de gouvernance','Bootstrap, approbation du relais, libération explicite, acquisition relais, renouvellement auteur génération2 testés sans effacer l’historique.')]
 p.table(['Famille de scénario','Vérification et limite'],tests,[150,CW-150])
 p.p(f'Pour le détail exact des {TEST_N} méthodes et assertions, consulter tests/test_ai_session_guard.py, tests-garde.log et revue-garde.txt. Le nombre de familles ci-dessus n’est pas le nombre de méthodes de test.','small')
 p.page('Relais de gouvernance sans auto-approbation')
 for title,body in [
 ('A. Préapprouver le relais','La mission bootstrap active et réservée propose le manifeste d’un coordinateur relais : autre ID, branche et conversation. Son diff est contrôlé ; le manifeste n’est fiable qu’après intégration dans main.'),
 ('B. Conserver puis libérer','Sauvegarder worktree, SHA, diff et reçus. Libérer explicitement le bootstrap avant d’acquérir le relais lorsque leurs chemins de gouvernance se chevauchent.'),
 ('C. Acquérir sur main frais','Le relais récupère le main contenant son approbation, acquiert sa réservation et crée son espace. Il peut fermer l’ancien bootstrap mais ne modifie jamais sa propre approbation.'),
 ('D. Renouveler un auteur','Conserver le travail et libérer l’ancienne réservation ; le relais approuve dans une PR distincte la génération source strictement supérieure ; l’auteur acquiert ensuite cette génération depuis main.'),
 ('E. Éviter le dernier mandat fermé','Préapprouver le prochain relais avant de fermer le dernier mandat de gouvernance. Sinon personne ne peut s’auto-approuver : récupération exceptionnelle humaine/administrateur nécessaire, séparée, motivée et tracée.')]:p.h(title);p.p(body)
 p.h('La récupération exceptionnelle n’est pas un “pass”')
 p.p('Ne pas désactiver la garde, inventer un manifeste antérieur ou prétendre qu’un contrôle a réussi. Une intervention administrative de récupération conserve l’incident, le travail sauvegardé, le changement exact, l’autorité et les vérifications renouvelées. Les autres tâches sans chevauchement peuvent continuer sous leur mandat existant.')
 p.page('Intégration, conflits et reprise depuis un main frais')
 for title,body in [
 ('1. Comparer le diff utile','Une ancienne branche sert de preuve ou de source de patch ciblé ; sa fusion entière peut réintroduire règles et contenus dépassés. Inventorier SHA, cours, fichiers et réserves avant de reprendre.'),
 ('2. Préparer un candidat actuel','L’intégrateur attribué repart du main courant, applique les seuls commits/patchs nécessaires, reconstruit les catalogues partagés et vérifie les invariants hors mission.'),
 ('3. Résoudre sans choix aveugle','Un conflit de catalogue est une fusion structurée par code ; un conflit de passage médical devient une décision avec sources et lecteur. Ne pas choisir systématiquement ours/theirs et ne pas recopier une ancienne arborescence entière.'),
 ('4. Revalider après avance de main','Si main ou le registre évolue avant intégration, vérifier les nouvelles collisions, reconstruire le candidat et renouveler les contrôles affectés. Le succès sur la précédente paire head/base ne suffit plus.'),
 ('5. Émettre le reçu durable','Enregistrer demande, tâche, base, SHA livré/intégré, adaptations, empreintes, contrôles, réserves et décision. La demande ne disparaît pas avant ce reçu.'),
 ('6. Publier avec ordre de version','Le déploiement cite le SHA intégré et son build ; vérifier URL et fichiers servis. Un ancien build fini tard ne doit pas écraser la version plus récente. Le reçu de publication médicale corrigée reste à préparer avant les corrections canoniques.')]:p.h(title);p.p(body)
 p.page('GitHub : imposer la règle et respecter les limites observées')
 p.p('La garde locale et la CI rendent le périmètre contrôlable ; elles ne peuvent pas, seules, interdire toute écriture directe sur main par API ou un autre poste. Le serveur doit imposer l’ouverture d’une PR, le contrôle requis strict et les règles de branche. Le GET actuel de protection historique renvoie403 faute de permission Administration : ce n’est ni une preuve d’absence ni une preuve d’activation.')
 p.table(['Mesure','Configuration et vérification nécessaires'],[
 ('Règle de main active','Require PR ; check garde obligatoire issu de la source attendue ; strict/up-to-date ; no force-push ; no delete ; linear history ; pas de bypass opérationnel, include admins/enforce_admins si protection historique.'),
 ('Méthode de fusion','Autoriser squash ou rebase si linear history. Cette règle interdit les merge commits ; elle n’empêche pas à elle seule un push direct.'),
 ('Propriété personnelle publique','Branch/tag rulesets et protections accessibles sur Free public. Merge queue : public détenu par organisation seulement ; indisponible pour le dépôt personnel actuel. Les restrictions legacy par acteurs qui poussent exigent également un dépôt organisation.'),
 ('Éviter restrict_updates mal configuré','Cette règle réserve toute mise à jour aux acteurs de bypass et peut bloquer aussi les fusions normales ; ce n’est pas un simple synonyme de “PR obligatoire”.'),
 ('Branche registre','Interdire les modifications arbitraires, force-push et suppression ; coordonner les droits de l’allocateur. L’avance rapide protège contre commits frères normaux, pas contre acteur autorisé à réécrire la référence.'),
 ('Lecture après activation','Relire ciblage, mode active, check/source, bypass et exigences ; démontrer refus push direct et cas invalides. Pas de statut “imposé” avant preuve distante.'),
 ('Administrateur / propriétaire','Il peut éditer/supprimer les règles, changer workflows, permissions ou installations. Include-admin/no-bypass contraint les opérations tant que la règle existe ; aucune interdiction inviolable contre cet administrateur.')],[145,CW-145])
 p.page('CI de confiance : garder un échec réel et la bonne révision')
 p.table(['Piège','Règle ou limite à appliquer'],[
 ('Workflow du candidat','Le contrôleur et Python viennent du base trusted ; le candidat est lu comme données Git. Pas d’import, action locale, hooks package, build, test ou artefact PR exécuté avec privilèges.'),
 ('Statut sur la mauvaise révision','pull_request_target utilise le contexte base/default ; son GITHUB_SHA et ses checks automatiques ne prouvent pas un statut sur head PR. Attacher/vérifier explicitement le check requis au head courant et à la base/registre examinés.'),
 ('Contexte Actions usurpé','GitHub Actions est une App commune à plusieurs workflows. Un autre workflow peut produire le même contexte : nom requis + source Actions ne prouve pas la provenance de la garde. Plus forte séparation : App reporter dédiée dont les credentials restent hors PR/writers, ou mécanisme organisationnel de workflow requis disponible.'),
 ('Skipped / neutral','GitHub peut considérer ces états satisfaisants pour un required check. Verdict terminal inconditionnel : tous résultats obligatoires exactement success, preuves présentes et identités/révisions cohérentes. Aucun faux succès par filtre paths, condition de job ou erreur absorbée.'),
 ('Bootstrap et post-push','Le workflow actuel indique la garde absente de base lors du bootstrap et laisse passer cette activation documentaire ; cela n’est pas un contrôle médical/source réussi. Son contrôle push main est diagnostic continue-on-error : il arrive après l’écriture et ne la prévient pas.'),
 ('Secrets et dépendances','Permissions minimales ; actions épinglées par SHA complet à imposer ; pas de secrets/cache privilégié exposé au code PR. La référence checkout@v4 existante est mutable et sa mise à niveau constitue un jalon de durcissement, pas une garantie déjà obtenue.'),
 ('Révision ou événement imprévu','Tête PR exacte, base trusted et registre frais ; événements supportés explicites. Un état inconnu ne devient pas “passed” ; un échec doit garder son code de sortie d’échec.')],[135,CW-135])
 p.page('Identités GitHub, forks et activation concrète')
 p.p('La branche et les champs de mission vérifient une cohérence opérationnelle. Pour une séparation forte, le contrôleur doit confronter le vrai GitHub actor, l’auteur PR, l’installation attendue et le dépôt numérique head aux données approuvées. Le présent garde déclaratif ne prouve ni quel modèle agit derrière un compte partagé, ni l’équité effective du travail fourni.')
 p.h('Politique de forks')
 p.p('La politique la plus simple refuse un dépôt head différent du dépôt base sauf approbation préalable liant exactement fork, acteur, branche, mission et chemins. Comparer les identifiants numériques de dépôt, pas seulement owner/name. Un dépôt public peut être forké ; le point contrôlable est l’admission du contenu dans main, pas l’interdiction générale de créer un fork.')
 p.h('Check-list de démonstration avant dire “imposé”')
 p.table(['Démonstration','Réponse attendue'],[
 ('Push direct main','Refus par règle serveur, sans dépendre d’un hook local.'),
 ('Mission absente / candidate','Refus ; l’approbation doit déjà exister dans base trusted.'),
 ('Actor/fork/branche non lié','Refus selon politique d’identité explicite ; limite déclarative documentée si non implémentée.'),
 ('Cours ou parent/enfant occupé','Refus ; autre tâche disjointe toujours possible.'),
 ('Workflow / garde / preuve altérés','Aucune auto-validation du candidat ; source de verdict contrôlée.'),
 ('Ancien SHA, ancien registre, skipped','Aucun succès réutilisé pour une version non vérifiée ; verdict terminal d’échec.'),
 ('Mission valide et disponible','Réservation courante, diff limité, bonnes preuves ; contrôle accepté pour les empreintes exactes.'),
 ('Relecture de configuration','Réponse distante enregistrée avec date, règle ciblée, mode active et bypass ; pas de403 interprété comme succès.')],[160,CW-160])
 p.page('Accès GitHub : actions concrètes et permissions réelles')
 import csv
 with (DEST/'AUTORISATIONS_GITHUB.csv').open(newline='') as f:
  for a in csv.DictReader(f):
   p.sub(a['Action']);p.p(E(a['Lien_direct']),'small');p.p(E(a['Manoeuvre']));p.p(E(a['Etat_limite']),'small')
 p.p('Ces liens rendent la configuration concrète et consultable. Aucun réglage serveur n’est prétendu appliqué par ce PDF ; le propriétaire agit avec ses droits réels, puis une lecture de retour et les démonstrations négatives établissent la portée obtenue.')
 p.page('Sources primaires des règles GitHub')
 for s in METHOD['sources'][1:]:
  p.sub(s['id']);p.p(E(s['url']),'small');p.p(E({'rulesets':'Rulesets branches/tags disponibles pour dépôts personnels publics Free ; les règles se cumulent. Les push rulesets ont une disponibilité distincte.', 'available_rules':'PR, contrôles, historique linéaire et restriction de mise à jour sont des règles distinctes ; la source App du statut requis peut être fixée.', 'protected_branches':'Public Free pris en charge ; administrateurs exemptés par défaut sauf inclusion. Les états success, skipped et neutral peuvent satisfaire les contrôles requis. Restriction des acteurs qui poussent réservée aux dépôts détenus par organisation.', 'merge_queue':'File de fusion disponible en public détenu par organisation, ou privé organisation Enterprise Cloud ; indisponible pour Medina personnel. merge_group doit être contrôlé si cette option devient disponible.', 'workflow_events':'pull_request_target utilise le contexte default/base ; ne pas y exécuter du code PR non fiable. Son SHA automatique est celui de la base, pas head PR.', 'secure_use':'Pas de checkout/exécution de code non fiable ni confiance aveugle aux artefacts dans les contextes privilégiés ; épingler les actions à un SHA complet.', 'required_status_troubleshooting':'Le contrôle requis doit effectivement être exécuté sur la bonne révision ; distinguer job skipped, workflow filtré et verdict réellement positif.'}.get(s['id'],s['claim'])))
 p.h('Observations de lecture publique')
 p.p('GET api.github.com/repos/vialdjoukang-spec/Medina/rulesets →200 [] ; GET /rules/branches/main →200 []. Ces observations montrent l’absence de rulesets listés/effectifs à l’instant de lecture, sans déterminer la protection historique inaccessible via App. Aucune écriture de settings n’a été faite par l’analyse méthodologique.')
 p.page('SSP : de la présentation au diagnostic et à la compétence')
 p.p('PROFILES2017, pages imprimées26–27, décrit des points d’entrée génériques : circonstances, symptômes, plaintes et résultats que le jeune résident doit évaluer de façon structurée, en établissant un différentiel et des mesures adaptées. Les situations fréquentes, urgentes ou sources de détresse ont été retenues ; leurs implications varient selon âge, sexe/genre, temporalité et lieu de soins.')
 p.table(['Type de lien','Ce qu’il permet de dire'],[
 ('Diagnostic causal / diagnostic','Une entité peut expliquer la présentation dans un contexte défini ; passage clinique et sous-entité explicités. Une catégorie de codage large n’est pas un diagnostic individuel.'),
 ('Différentiel','Alternative à envisager/évaluer/exclure ; discrimination, tests initiaux et urgence à décrire dans la démarche. Une liste de noms n’est pas une stratégie diagnostique.'),
 ('Contexte / notion','Risque, complication, mécanisme, terrain ou accompagnement sans causalité/différentiel établi. Utile à enseigner, ne crée pas une couverture diagnostique.'),
 ('Compétence / parcours de soins','Consentement, refus, prévention, screening, communication, vulnérabilité, coordination, fin de vie ; objectif transversal/scénario, pas maladie artificielle.'),
 ('Hors périmètre actuel','Autre propriétaire ou contexte hors quatre systèmes ; renvoi en lecture seule conservé. Cela ne signifie pas “non exigible à l’examen”.'),
 ('Candidat / non résolu','Source non lue, insuffisante ou lien incertain ; proposition conservée sans la compter comme diagnostic étayé.')],[150,CW-150])
 p.h('Le graphe v2 reste partiel')
 p.p(E(f'{coverage["counts"]["liens"]} arêtes transmises : 91 diagnostics, 329 différentiels, 19 contextes, 33 candidats. 95 SSP ont au moins une arête, 92 hors candidats, 88 un diagnostic ou différentiel. Quatre ont seulement du contexte ; trois seulement des candidats ; 170 ne sont pas documentées dans ce contrôle. Aucun de ces nombres ne mesure l’exhaustivité clinique.'))
 p.page('Pourquoi 265/265 glouton ne démontre pas une couverture clinique')
 p.p('tools/import_nosology.py attribue historiquement des SSP par plages de catégories ; tools/pathologies_ssp.py prend fréquentes et cours filled, ajoute gloutonnement les catégories gagnant le plus de tags, puis MANUAL complète des liens proposés. Chaque étape manipule une incidence pédagogique qui reste à justifier ; la complétude de cette incidence ne valide ni le lien ni le contenu d’un cours.')
 p.table(['Étape de simulation exacte sur arbre méthodologique','Catégories / SSP'],[
 ('Socle : fréquentes + catégories state filled','299 / 142'),('Après couverture gloutonne','347 / 219'),('Après107 paires MANUAL','398 / 265'),('Ancien fichier ANNEXE_PATHOLOGIES_SSP.md','291 / 265, état historique non régénéré')],[CW-125,125])
 p.p('Le glouton ne prouve pas une solution minimale ; les cours existants et fréquents sont préimposés. Le départage du code actuel utilise seulement la première lettre et l’ordre d’entrée, contrairement au commentaire évoquant le code. Conserver source commit et ordre des données pour reproduire une comparaison. Ces nombres globaux ne sont pas les 258 catégories conservatoires des quatre systèmes.')
 p.h('Réparer les sept libellés tronqués sans réécrire les cours')
 p.p('La regex historique lit une seule ligne physique du PDF ; les identifiants1–265 sont complets, mais sept libellés perdent une continuation. L’annexe v2 corrige39,66,93,130,216,226,227 et conserve les258autres. Les sources globales et les cours anciens restent inchangés ; SSP238 est déjà complet. Pour66, le PDF rendu confirme “premenstrual symptoms” malgré la ligature extraite dans le mauvais ordre.')
 repairs=METHOD['source_integrity']['label_repairs']
 p.table(['SSP / page','Libellé complet normalisé'],[(f'{n} · p{r["printed_page"]}',r['complete_label']) for n,r in repairs.items()],[65,CW-65])
 p.page('Le dossier de preuve d’un lien SSP')
 p.table(['Champ','Exigence'],[
 ('Situation','Numéro officiel, libellé anglais complet et page PROFILES ; traduction séparée si vérifiée.'),
 ('Diagnostic / sous-entité','Entité clinique, catégorie3caractères, sous-code examiné si utile et propriétaire canonique ; contexte âge/setting/temporalité.'),
 ('Relation','Diagnostic, différentiel, contexte, compétence, hors périmètre ou candidat ; motif clinique et niveau de nécessité.'),
 ('Source','URL, titre/éditeur, version/date, page/section, passage effectivement consulté, date de consultation, empreinte si disponible ; limite de lecture explicite.'),
 ('Contrôle','Auteur/lecteur, décision et réserve, statut réel ; source de codage distingue le code mais ne prouve pas à elle seule la présentation clinique.'),
 ('Cours','Chemin, onglet/ancrage et empreinte du contenu qui enseigne raisonnement, discrimination et premières actions ; course planned ≠ content delivered.'),
 ('Traçabilité normalisée','ID stable de l’arête, fichier source, index/pointeur JSON et preuve originale conservée. Les identifiants originaux et IDs normalisés peuvent différer ; ne pas en déduire une arête manquante.')],[122,CW-122])
 p.h('Validation de portée avant validation de total')
 for s in ['Figer le commit et les empreintes des sources, le libellé et la page PROFILES, le catalogue des quatre systèmes et la portée exacte de revue.', 'Typer chaque lien, préciser population, âge, lieu de soins, temporalité, grossesse ou gravité ; vérifier le code et son libellé officiel.', 'Lire la section clinique elle-même : source suisse puis européenne, éditeur, version, passage/page, date et limites. Un HTTP200 ne vaut pas preuve médicale.', 'Justifier la pertinence fréquente, urgente ou contextuelle sans déduction par mot partagé, simple plage CIM ou mention indirecte ; garder sources contradictoires et incertitudes.', 'Distinguer proposition, passage consulté, lien documenté, décision éditoriale et validation indépendante réellement effectuée. Aucun statut favorable sans contrôle accompli.', 'Repérer la section du cours qui enseigne démarche, discrimination, actions et drapeaux rouges ; un cours planifié reste distinct d’un contenu livré.', 'Examiner le différentiel attendu et les variations de contexte ; une seule arête par SSP ne suffit jamais à déclarer une complétude clinique.', 'Livrer une matrice où diagnostics, différentiels, contextes, compétences, hors-périmètre et incertitudes sont séparés, avec sources et ancrages versionnés.']:p.p('• '+E(s),'small')
 p.h('Conserver le doute sans détruire le socle')
 p.p('Une catégorie historique non recontrôlée reste conservée avec son statut. Les11ajouts documentés se joignent au socle247 ; cela ne permet pas d’appeler les258catégories “revalidées”. Les19catégories candidates S04, des catégories hématologiques non précisées et d’autres familles gardent leurs lacunes visibles. Un examen clinique complet de chaque SSP doit encore rechercher les alternatives et contextes non couverts.')
 p.page('Annexe : triage documentaire des 265 SSP')
 p.box('<b>Cette annexe énumère les265situations officielles, pas265situations entièrement couvertes.</b> D=documenté diagnostique partiel ; C=contexte seul ; P=candidats seuls ; ND=non documenté dans cette revue bornée. Un renvoi hors quatre systèmes conserve son propriétaire et n’autorise aucune modification de ce système.')
 stat={'LIENS_DIAGNOSTIQUES_DOCUMENTES_PARTIELLEMENT':'D — diagnostic/différentiel partiel','LIENS_CONTEXTUELS_SEULEMENT':'C — contexte seul','CANDIDATS_SEULEMENT_A_VERIFIER':'P — candidats seuls','NON_DOCUMENTE_DANS_CE_CONTROLE':'ND — non documenté ici'}
 rows=[]
 for s in coverage['ssp']:
  rel=f'Diag {s["diagnostic"]} · Diff {s["differentiel"]} · Ctx {s["contexte"]} · Cand {s["candidat"]}'
  rows.append((str(s['ssp'])+(' *' if s['label_repare'] else ''),s['label_officiel_corrige'],stat.get(s['statut'],s['statut'])+'\n'+rel+'\nCodes : '+txt(s['codes3'])))
 p.table(['SSP','Libellé officiel anglais','Triage et catégories'],rows,[35,225,CW-260])
 p.p('* Libellé réparé dans la copie scoped v2. Les identifiants d’arêtes par SSP se trouvent dans couverture-265-ssp.json ; le graphe détaillé ci-après permet de retrouver sources, justifications et limites.','small')
 for fid in FRAGS:
  p.page('Annexe : graphe probant — '+FRAGS[fid])
  subset=[e for e in edges if e['_fragment']==fid]
  p.p(E(f'{len(subset)} arêtes issues de preuves-{fid}.json. Les arêtes de contexte/candidat restent explicitement séparées ; les renvois ne changent pas leur propriétaire.'),'small')
  for e in subset:
   p.story.append(CondPageBreak(115));p.sub(f'SSP {e["_ssp"]} → {e["_code"]} · {e["_type"]}')
   p.p('<b>'+E(e['_entity'])+'</b> · '+E(e['titre_cim']),'small')
   p.p(E(e['_why']))
   rows=[('ID / provenance',e['_id']+'\n'+e['source_fichier']+e['source_json_pointer']),('Propriétaire / statut',str(e['fragment_proprietaire'])+' · '+str(e['_status']))]
   for ev in e['_evidence']:
    rows.append(('Source / section',str(ev.get('source_id','source'))+' · '+str(ev.get('section_lue','non renseignée'))+'\n'+str(ev.get('url',''))))
   if e.get('limites'):rows.append(('Limites',txt(e['limites'])))
   p.table(['Trace','Détail'],rows,[100,CW-100])
 p.page('Décider d’une livraison sans faux “pass”')
 p.table(['Question','Critère de décision'],[
 ('Le travail est-il autorisé ?','Mission active trusted-base, bonne branche, bonne génération et réservation actuelle ; planninggénération0 ne suffit pas.'),
 ('Est-il isolé ?','Cours, chemins et sorties propres ; aucun chevauchement avec réservation active ; anciens systèmes et lignes catalogue hors mission conservés.'),
 ('Le contenu est-il probant ?','Passages réellement lus et applicables ; lien typé ; statut partiel honnête ; correction recontrôlée dans ses surfaces ; lacunes visibles.'),
 ('Le contrôle est-il réel ?','Exact head/base/registre, source de contrôleur trusted, résultat d’échec conservé, preuve non périmée. Ni skipped ni exception transformée en succès.'),
 ('Le serveur impose-t-il la règle ?','Configuration relue et démonstrations de refus disponibles ; avec403, conserver “à imposer/vérifier”.'),
 ('La reprise est-elle possible ?','Diff, SHA, worktree et reçus conservés ; libération explicite ; génération supérieure approuvée ; relais de gouvernance préapprouvé.'),
 ('La clôture est-elle proportionnée ?','Vérification finale selon risque et nouvelle version ; aucune promesse de zéro erreur/collision ni audit final négligeable.')],[145,CW-145])
 p.p('Le dossier complet demeure planifié pour le travail médical. Le registre et les contrôles locaux apportent des preuves techniques concrètes ; les droits/contrôles serveur et le reçu de publication de versions corrigées gardent leurs limites explicites.')
 p.save('PROTOCOLE_ANTI_COLLISION_V2.pdf')

def verify_pdfs():
 import fitz
 for name in ['AUDIT_ALPHA_V2.pdf','PRODUCTION_FRAGMENTS_V2.pdf','PROTOCOLE_ANTI_COLLISION_V2.pdf']:
  path=DEST/name;d=fitz.open(path);bad=[];minfont=100;body=0
  for i,page in enumerate(d):
   for block in page.get_text('dict')['blocks']:
    for line in block.get('lines',[]):
     for span in line['spans']:
      if not span['text'].strip():continue
      minfont=min(minfont,span['size']);box=fitz.Rect(span['bbox'])
      if box.x0 < 18 or box.y0 < 10 or box.x1 > W-18 or box.y1 > H-10:bad.append((i+1,span['text'][:60],list(box)))
   page_text=page.get_text();assert f'{i+1} / {len(d)}' in page_text,(name,'page number missing',i+1)
   body+=len(page_text)
  assert minfont>=9.49,(name,'font too small',minfont)
  assert not bad,(name,'text outside page',bad[:10])
  print('VERIFIED',name,'pages',len(d),'chars',body,'minfont',round(minfont,2),'out_of_bounds',len(bad),flush=True)
  text=subprocess.check_output(['pdftotext','-layout',str(path),'-'],stderr=subprocess.DEVNULL).decode()
  assert len(text)>10000
  if name.startswith('AUDIT'):
   for c in PLAN['audit']:assert c['code']+' —' in text or c['code']+' –' in text,c['code']
  print('PDFTOTEXT_OK',name,len(text),flush=True)

if __name__=='__main__':
 PLAN,PROOFS=load_inputs()
 assert len(PLAN['audit'])==104 and Counter(x['owner'] for x in PLAN['audit'])=={'Codex':52,'Claude':52}
 assert len(PLAN['production'])==154 and Counter(x['owner'] for x in PLAN['production'])=={'Codex':77,'Claude':77}
 assert len(PLAN['reserve'])==12 and Counter(x['owner'] for x in PLAN['reserve'])=={'Codex':6,'Claude':6}
 EDGES=canonical_edges();assert len(EDGES)==472
 audit_pdf(PLAN,PROOFS);production_pdf(PLAN,PROOFS,EDGES);protocol_pdf(PLAN,PROOFS,EDGES);verify_pdfs()
