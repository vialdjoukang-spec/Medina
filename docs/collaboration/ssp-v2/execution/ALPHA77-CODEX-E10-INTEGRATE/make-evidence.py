from pathlib import Path
from datetime import datetime,timezone
from lxml import html
import json,hashlib,importlib.util,re
OUT=Path(__file__).parent;RAW=Path('/workspace/scratch/E10-integrate-sources')
index=json.loads((RAW/'consultation-index.json').read_text());meta={x['id']:x for x in index}
# Fetched does not mean read: retain acquisition metadata separately from excerpts below.
for x in index:
 x.pop('lecture_reelle',None);x.pop('faits_retenus',None);x.pop('lecteur',None)
 if x['id'] in ['FIG8','FIG9']:
  x['status']='challenge_page_not_source';x['error']='PMC browser challenge, 165characters; not used as read source. EuropePMC XML used instead.'
 if x['id']=='CP':x['resolution']='Wrong URL9620 gave404; actual course URL26518 fetched and read.'
(OUT/'acquisition-index.json').write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n')
rows=[]
def add(id,source,anchors,section,claims,locations,population,limits):
 m=meta.get(source,{})
 name=source
 if source=='CP':m={'url':'https://www.viollier.ch/fr/analysis/26518','consulted_at':datetime.fromtimestamp((RAW/'CP.html').stat().st_mtime,timezone.utc).isoformat()}
 if source in ['PMC12730728','PMC8656040']:
  e=next(x for x in json.loads((RAW/'epmc-index.json').read_text()) if source in x['url']);m={'url':e['url'],'consulted_at':e['consulted_at'],'sha256_download':e['sha256']}
 text=(RAW/(name+'.txt')).read_text()
 excerpts=[]
 for needle,length in anchors:
  pos=text.find(needle)
  if pos<0:raise ValueError((source,needle))
  excerpts.append(text[pos:pos+length])
 rows.append({'id':id,'source_id':source,'url':m['url'],'publisher':m.get('editeur',{'RMS':'Revue Médicale Suisse / programme cantonal diabète','GLU':'Viollier','CP':'Viollier','NA':'Viollier','K':'Viollier','OSM':'Viollier','BIC':'Viollier','GAS':'Clinique de La Source','FIG6':'OpenStax via LibreTexts','PMC12730728':'Kandinov et al. / Biomolecules','PMC8656040':'Kolb et al. / BMC Medicine'}.get(source,source)),'version':m.get('version_annee',{'RMS':'2019','FIG6':'13mai2022','PMC12730728':'2025','PMC8656040':'2021'}.get(source,'catalogue accessible le15octobre2026')),'consulted_at':m.get('consulted_at'),'section':section,'actual_passages':excerpts,'download_sha256':m.get('sha256_download'),'claims':claims,'locations':locations,'population':population,'limitations':limits,'reading_level':'section','medical_human_validation':False})
add('SEM-01','GLU',[('Prise de sang à jeun',65),('Méthode',30),('3.3 - 5.5',35)],'Remarque, méthode, valeurs de référence','Normalité analytique3,3–5,5mmol/L,16–99ans,plasma fluoré,hexokinase,jeûne≥8h',['e10-semio-normal','e10-a04-partie-3'],'16–99ans','Intervalle laboratoire; ni diagnostic ni cible de traitement.')
add('SEM-02','FIG6',[('The pancreatic exocrine function',570),('Two of the early manifestations',700)],'Figure1 et Disorders of the Endocrine System','Destination endocrine/exocrine, îlots, diurèse osmotique et soif',['e10-semio-normal','e10-semio-mechanisms','e10-histo'],'Physiologie humaine générale','Aucune statistique américaine ni prescription tirée de ce chapitre; schéma pédagogique normal, pas histologie patient.')
add('SEM-03','PMC8656040',[('The lack of food therefore',800),('Persons with diabetes type 1',650),('The release of fatty acids',250)],'Ketosis et physiologie/cétogenèse','Faible activité insulinique→lipolyse→production cétonique; cétose physiologique distincte de crise',['e10-semio-normal','e10-semio-mechanisms','e10-s03'],'Physiologie et diabète','Revue mécanistique, non recommandation de régime cétogène dans le type1.')
add('SEM-04','RMS',[('Critères de suspicion clinique',740),('Examen initial',530),('Tout cas d’urgence hyperglycémique',180)],'p449 : suspicion, examen initial,144','Signes digestifs/respiratoires, conscience et perfusion; hyperglycémie>11 avec symptômes systémiques;144 si altération générale',['e10-semio-signs','e10-semio-examination','e10-semio-urgency','e10-a04-analyse'],'Ambulatoire suisse','Fiche2019; critères diagnostiques propres, ne pas fusionner aux critères JBDS.')
add('SEM-05','S8',[('1.1.1',850),('1.1.4',880),('1.1.9',640)],'1.1.1–1.1.10','Pas d’exclusion âge/IMC;2autoanticorps;peptideC conditionnel apparié;priorité soins aigus;pancréas si≥60ans amaigrissement',['e10-semio-signs','e10-semio-interpretation','e10-semio-differentials','e10-s04-pane','e10-histo','pareto-e10-a12'],'Adulte','Complément européen à RMS suisse; n’importe pas organisation NHS ni prescription.')
add('SEM-06','S9',[('Diagnosis of DKA\n',650),('Euglycaemic DKA\n',570),('Ketosis prone type 2 diabetes',500)],'p10–11','Trois composantesJBDS;forme euglycémique et crise non exclusive type1',['e10-semio-interpretation','e10-semio-differentials','e10-a04-analyse'],'Adulte hospitalisé','Référence britannique2023 explicitement attribuée; seuils distinctsRMS2019.')
add('SEM-07','S9',[('Differential diagnosis\nIt',1500),('Point of care testing',1700)],'p12','Cétose jeûne/alcool;β-hydroxybutyrate;veineux;contrôle qualité;limite lecteur choc',['e10-semio-examination','e10-semio-differentials'],'Adulte hospitalisé','La glycémie normale ne distingue pas seule la crise alcoolique de l’euglycémique diabétique.')
add('SEM-08','S9',[('Assessment of severity\nThe',1100),('Action 1 - Intravenous access',620),('The inability to develop an osmotic diuresis',510)],'p24–25 et End stage renal failure','Gravité et signes vitaux;dialyse peut modifier hydratation apparente',['e10-semio-examination','e10-semio-urgency','e10-semio-limits'],'Adulte, insuffisance rénale terminale','Pas transposition automatique à enfant ou grossesse.')
add('SEM-09','S2',[('En cas de suspicion',430),('altération de l’état de consciences',430)],'p1','Hypoglycémie avec/sans symptômes;mesure et traitement sans attendre si mesure indisponible;conscience et médecin',['e10-semio-signs','e10-semio-urgency','e10-a04-analyse'],'Adulte hospitaliséHUG','Protocole institutionnel;pas transposition pédiatrique.')
add('MED-M01','S4',[('2. In a person with diabetes without',610),('4. In a person with diabetes and a foot',650)],'Recommandations2et4','ABI+TBI+Doppler combinés;aucun seuil isolé n’exclut;moins probable0,9–1,3/≥0,70/bi-triphasique',['e10-a09','e10-a10-fenetre-1'],'Diabète avec/sans plaie','Source intersociétés dontESVS;certitude faible;pas de prescription étrangère.')
add('MED-M03','S8',[('1.14.18',200),('1.14.23',410)],'1.14.18 et1.14.23–24','La distinction endocrine/exocrine n’exclut pas des symptômes digestifs;évaluation spécifique',['e10-s01','pareto-e10-s01','e10-histo'],'Adulte type1','Pas nouvelle dose antiémétique.')
add('MED-M05','S6',[('Tresiba 100 unités/ml et Tresiba 200',780)],'Posologie : concentrations','Dose affichée en unités sans conversion;volume différent',['pareto-e10-p02','e10-p02-partie-6'],'Type1 dès1an,adulte selonFI','FlexTouch100et200 ont paliers distincts;pas prélèvement à la seringue.')
add('MED-ASPART','S5',[('Les besoins individuels',450),('Administration intraveineuse',550),('Toutes les préparations d\'insuline',520),('Grossesse, allaitement',1280)],'Posologie, voies, précautions, grossesse/allaitement','NovoRapid100U/mL: besoins individuels,repère0,5–1U/kg/jour et50–70% aspart;voieIVpro;surveillanceK/glucose;grossesse/allaitement',['e10-p01','e10-p02','e10-a06','e10-semio-mechanisms'],'Adultes et enfants dès2ans pour repères','Autorisation55045,55046,55712,65630;aucun débit d’insuline humaine transféré à l’aspart.')
add('MED-DEGLUDEC','S6',[('Chez les patients atteints du diabète de type 1, Tresiba',270),('Patients atteints de diabète de type 1\n',430),('Un minimum de 8 heures',260),('Tresiba ne doit pas être administré par voie intraveineuse',410),('Allaitement\n Il n\'existe',380)],'Posologie, changement, mode,allaitement','Tresiba dose individuelletype1;20%envisageable au changement;8hminimum;pasIV/IM/pompe;allaitementdéconseillé',['e10-p01','e10-p02'],'Type1 dès1an','Autorisation62562/62563;flexibilitéhoraireenfantnonétudiée;pas10Uinitialestype2vers type1.')
add('MED-GLUCAGON','S7',[('Indications/Possibilités d’emploi',500),('Contre-indications\n',230),('Stocks de glycogène',620),('Interactions\n',780)],'Indications,dose,contre-indications,glycogène,interactions','Baqsimi3mg intranasal unique dès1an;phéochromocytome;réservesglycogène;indométacine/warfarine/bêtabloquants',['e10-p02','e10-p02-fenetre-1'],'Diabète dès1an,hypoglycémiesévère','Autorisation67465;pas de nouvelle dose d’autre glucagon.')
add('NORM-CP','CP',[('Prise de sang à jeun.',160),('0.27 - 1.27',45)],'Préanalyse et valeurs','PeptideC0,27–1,27nmol/L,prélèvementàjeun',['e10-e01'],'CatalogueViollier','Référence à jeun différente du dosage nonàjeun demandé parNICE;pas seuil type1/type2.')
add('NORM-SODIUM','NA',[('136 - 145',30)],'Valeurs de référence','Na136–145mmol/L',['e10-e02'],'Sérum','Catalogue laboratoire,méthodeélectrodesélective.')
add('NORM-K','K',[('3.5 - 5.1',30)],'Valeurs de référence','K3,5–5,1mmol/L',['e10-e02'],'Sérum','Préanalytique de centrifugation explicitée dans catalogue.')
add('NORM-OSM','OSM',[('280 - 300',35)],'Valeurs de référence','Osmolalité280–300mosmol/kg',['e10-e02'],'Sérum','Valeur mesurée,ne pas assimiler au seuil hyperosmolaire.')
add('NORM-BIC','BIC',[('20.0 - 31.0',35)],'Valeurs de référence','Bicarbonates20–31mmol/L',['e10-e02'],'Sérum','Noninterchangeable avec gazométrie.')
add('NORM-GAS','GAS',[('Valeur de référence adulte',550)],'Valeur de référence adulte','pH7,35–7,45,bicarbonate22–26',['e10-e02'],'Adulte,gazométrie','Page ne précise pas ici la même matrice que sérumViollier;méthodesdifférentes.')
add('CONDUITE-CH','S13',[('Tabelle 3: Hypoglykämierisiko',3650),('Kategorie D und D1',1900)],'Tableau3 et p13,secondgroupe','Réouverture tableauprofessionnel:groupes,exceptionsD/D1,Clarke,expertises,niveaux,attentes',['e10-a11-conduite'],'Conducteurs suisses','Discordance seuils texte/tableau du premiergroupe conservée explicitement;aucune aptitude individuelle certifiée.')
(OUT/'claim-mapping.json').write_text(json.dumps({'schema_version':1,'code':'E10','kind':'author_consultation_and_mapping','final_audit':False,'medical_human_validation':False,'claims':rows},ensure_ascii=False,indent=2)+'\n')
# Source-only predicates of the shared sciences test, without falsifying its absent baseline.
spec=importlib.util.spec_from_file_location('science_check','tests/audit_sciences.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
panel=m.science(Path('chapters/E10/E10_c.html').read_text());r={'method':'Same current-source predicates as tests/audit_sciences.py; historical comparison not available','historical_error':'E10 not present at fixed BASEc50a28a23d7e2a2e0cf8ac36842b567de419daf4','units':[],'errors':[]}
for u in panel.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," sci ")]'):
 id=u.get('id');text=' '.join(u.itertext());fig=u.xpath('.//figure');r['units'].append({'id':id,'words':m.words(u),'figures':len(fig)})
 if m.words(u)<280:r['errors'].append(id+' short')
 if not fig:r['errors'].append(id+' no figure')
 for f in fig:
  if not f.xpath('./figcaption') or not f.xpath('.//svg[@role="img"][@aria-label]'):r['errors'].append(id+' inaccessible')
 for lab in ['Science → clinique.','Science → examen.','Science → traitement.','À retenir.']:
  if lab not in text:r['errors'].append(id+' missing '+lab)
r['result']='passed' if not r['errors'] else 'failed';(OUT/'current-sciences.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print('claim mapping',len(rows),'current sciences',r['result'])
