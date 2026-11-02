"""Bind actual final tests and declared self-reviews; never certify medicine."""
from pathlib import Path
import json,hashlib,datetime,re,shutil
ROOT=Path(__file__).resolve().parents[5]; OUT=Path(__file__).resolve().parent
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,d):p=OUT/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');return sha(p)
ledger=json.loads((OUT/'source-ledger.json').read_text());rights=json.loads((OUT/'figures-rights.json').read_text());browser=json.loads((OUT/'browser-report.json').read_text());assert browser['passed']
files={str(p.relative_to(ROOT)):sha(p) for p in sorted((ROOT/'chapters/N00').glob('*.html'))};final=dict(files)
final['glossary/n00.py']=sha(ROOT/'glossary/n00.py')
for f in rights['figures']:final[f['path']]=sha(ROOT/f['path'])
preview='N00-apercu-autonome.html';ph=sha(OUT/preview)
(OUT/'monographie-source.html').write_text('\n'.join((ROOT/p).read_text() for p in files))
limits=[
'Auto-relectures explicites de l’auteur ; aucune revue clinique indépendante globale ni validation médicale humaine.',
'Absence de donnée nationale récente d’incidence de l’ensemble des syndromes néphritiques aigus dans les sources suisses lues ; aucun taux de microhématurie ou de maladie distincte extrapolé à N00.',
'Lectures ciblées de sections réellement identifiées, pas lecture intégrale revendiquée des ouvrages. Les références suisses anciennes sont utilisées pour sémiologie/orientation ; CUEN 2025 et KDIGO complètent sans transformer une revue ancienne en protocole actuel.',
'KDIGO AKI 2012 : passage extrait par le fournisseur Parallel après refus HTTP du PDF direct ; empreinte du texte obtenu, non du PDF officiel, et limites OCR conservées dans le ledger.',
'La monographie du syndrome reconnaît les vascularites et maladies anti-membrane basale urgentes ; leurs protocoles spécialisés ne sont pas remplacés par une immunosuppression universelle.',
'FI Lasix : contre-indication d’anurie, voies et plafonds pédiatriques explicites. La fiche suisse Norvasc consultée ne fournit pas de schéma avant 18 ans. Ospen 1000 correspond à un million d’UI, non à 1000 mg ; aucune conversion pédiatrique improvisée.',
'Le traitement antibiotique de l’infection et l’évolution d’une glomérulonéphrite établie sont distingués ; la formulation réglementaire Ospen sur les complications n’est pas présentée comme preuve de récupération rénale.',
'Photomicrographies : diagnostic attribué à la provenance ; la coloration PAS ne montre ni immunofluorescence ni germe. Le panneau de sédiment original est limité à 567×337 pixels, sans agrandissement artificiel. Les droits de figure sont documentés via les pages Commons ; l’article PMC du sédiment a présenté un contrôle navigateur et n’est pas revendiqué comme lu.',
'PROFILES 2017 et MEBEKO examen 2026 : correspondance pédagogique explicite, sans assimilation à la numérotation PROFILES 2023 ni à une liste officielle de questions CIM.',
'Aperçu natif testé à une origine HTTP interceptée en Chromium, toutes autres requêtes bloquées ; aucun déploiement public ni navigation réseau réelle revendiqué.'
]
medical_checks=[
'Lecture réelle des six surfaces, des tableaux, de 36 fenêtres et de 14 synthèses ; contrôle de cohérence avec le ledger et les quatre FI suisses exactes relues.',
'Hématurie confirmée et morphologie distinctes du dépistage par bandelette ; seuil HUG >5% d’acanthocytes contextualisé, absence non excluante.',
'Chronologie IgA/infection préalable/infection active distinguée ; endocardite avec ANCA possible et complément non spécifique.',
'Critères AKI et stades : fenêtres, unités, critère le plus sévère, anurie, stade pédiatrique et limites du débit estimé en phase instable.',
'Priorités respiratoires, neurologiques et métaboliques explicites ; hémoptysie non obligatoire pour envisager une hémorragie alvéolaire.',
'C3 persistant au-delà de douze semaines : repère de réévaluation, jamais délai d’attente imposé devant aggravation.',
'Lasix IV 20–40mg adulte ≥15ans, augmentation 20mg/2h, OAP40mg puis20–40mg/20min ; vitesse≤4mg/min ou≤2,5mg/min si créatinine>5mg/dL. Enfant IV1mg/kg max20mg/j, oral2mg/kg max40mg/j ; anurie et apport potassique non automatique.',
'Norvasc adulte5mg/j puis10mg/j maximum, prudence hépatique/âge, pas d’adaptation rénale habituelle, absence de schéma enfant dans la FI retenue ; distinct d’une urgence hypertensive.',
'Ospen1000 :1millionUI=654mg sel=590mg actif, adulte≥12ans1comprimé3–4fois/j,≥10jours streptococciques, anurie intervalle12h et65,8mg potassium ; pas protocole d’endocardite.',
'CIM OFS : syndrome et morphologie distincts, N10/N05 exclus, dix suffixes présentés sans inventer dix traitements ; PROFILES millésime2017 et examen2026 explicités.',
'Anatomie humaine sourcée ; repères prudents sur les micrographies, aucune attribution de cellules ou dépôts non visibles sur le panneau.'
]
base=dict(reviewer='astra_nephrologie',mode='self_review',independent=False,reviewed_at=NOW,canonical_files=files,glossary_sha256=final['glossary/n00.py'],preview_sha256=ph,medical_human_validation=False,clinical_certification=False)
reviews={}
for kind in ['medical','language','visual_desktop','visual_mobile']:
 r=dict(base)
 if kind=='medical':r.update(scope='Auto-relecture des six surfaces et quatre FI exactes, sections de preuves ciblées.',checks=medical_checks,limitations=limits)
 elif kind=='language':r.update(scope='Auto-relecture du français des six surfaces, y compris fenêtres, figures, formules et tableaux.',checks=['Termes, unités et différences de population revus.','Formulations de preuve et de possibilité distinguées ; absence de données explicitée.','Espaces des unités et erreurs locales corrigées ; textes et CSS séparés.','Fermeture prématurée du template due au traitement de fragments séparés identifiée dans le rendu et corrigée ; construction du cours entier vérifiée ensuite.','Cinq doublons d’identifiants de sections scientifiques corrigés ; navigation au clavier vérifiée.'],limitations=['Auto-relecture IA, sans relecture humaine ni certification linguistique indépendante.'])
 else:
  width=1440 if kind=='visual_desktop' else 390
  v=next(x for x in browser['viewports'] if x['width']==width)
  r.update(scope=f'Aperçu natif autonome Chromium largeur {width}px, images décodées après défilement.',checks=v,visual_inspection=['Cinq originaux et leurs légendes/repères inspectés sur captures aux deux largeurs : podocytes, néphron, deux micrographies, quatre panneaux de sédiment.','Les positions absolues des26repères, le chargement des8occurrences, les6disciplines et9sections sémiologiques, la fenêtre et le mode Livre24px sont vérifiés.'],limitations=['Rendu local intercepté, sans déploiement public.','Le bouton flottant Plan peut recouvrir une petite zone lors d’une capture mobile ; le contenu reste accessible en défilant.'])
 h=save('reviews/'+kind+'.json',r);reviews[kind]=dict(path='reviews/'+kind+'.json',reviewer='astra_nephrologie',mode='self_review',sha256=h)
images=[]
for f in rights['figures']:
 dest=OUT/'images'/Path(f['path']).name;dest.parent.mkdir(exist_ok=True);shutil.copyfile(ROOT/f['path'],dest)
 images.append(dict(f,path=str(dest.relative_to(OUT)),canonical_path=f['path'],medical_review='Auto-relecture IA des originaux et annotations réellement vus ; reviews/visual_desktop.json et reviews/visual_mobile.json ; aucune validation humaine.'))
titles=['Définition','Épidémiologie','Physiopathologie','Démarche clinique','Anamnèse','Examen clinique','Syndromes','Diagnostic positif','Explorations','Arbre diagnostique (différentiels)','PEC','Prévention/suivi/pronostic','Points clés','Pièges']
sourcemap=[['EU-SYNDROMES'],['EU-POSTINF','INT-INFECTION'],['EU-HISTO','NORMAL-FILTRE'],['CH-URGENCE','CH-SEDIMENT'],['EU-IGA','INT-INFECTION'],['CH-PEDIATRIC-BP','EU-RPGN'],['EU-SYNDROMES','INT-AKI'],['CH-SEDIMENT','INT-GN-GENERAL'],['INT-INFECTION','EU-IRA'],['EU-HEMATURIA','EU-RPGN'],['FI-LASIX-IV','FI-NORVASC','FI-OSPEN'],['INT-INFECTION','CH-PREGNANCY'],['CH-PROFILES','CH-MEBEKO'],['CH-SEDIMENT','INT-INFECTION']]
explanations=[
'Définition du syndrome aigu avec hématurie glomérulaire, protéinurie et retentissement variable ; syndrome, lésion et cause ne sont pas assimilés.',
'Population et dénominateur discutés ; absence d’incidence suisse directe explicitée, distinction de la forme pédiatrique classique et des infections actives adultes.',
'Barrière glomérulaire, passage des hématies, filtration réduite et bilan hydrosodé reliés aux symptômes ; six sciences détaillent les mécanismes et limites.',
'Parcours gravité, localisation, cause et trajectoire ; bilan et stabilisation menés en parallèle devant une atteinte menaçante, sans attendre toutes les sérologies.',
'Chronologie, infection active, signes systémiques, médicaments et antécédents orientent les hypothèses ; les situations pédiatriques et âgées sont distinguées.',
'Respiration, conscience, pression adaptée à la population, poids, diurèse, peau, articulations et signes infectieux structurent un examen utilisable pour décider.',
'Présentation néphritique, néphrotique associée, rapidement progressive et réno-pulmonaire comparées ; classification AKI détaillée dans les examens sans score universel inventé.',
'Confirmation de l’hématurie et origine glomérulaire, fonction et contexte ; limites des signes négatifs et indication raisonnée de biopsie explicitées.',
'Urine, fonction, immunologie, microbiologie, échographie et biopsie décrites selon question, méthode, interprétation et limites, avec paramètres chiffrés contextualisés.',
'Arbre en cinq étapes reliant urgence, présence des cellules, localisation, infection et profil immunologique ; alternatives urologiques, tubulaires et systémiques examinées.',
'Soutien, surcharge, pression et cause distingués ; quatre produits suisses exacts, doses, populations et contre-indications sans protocole universel d’immunosuppression.',
'Suivi clinique et biologique de la trajectoire, persistance du complément, pronostic selon population et prévention ; une aggravation ne doit pas attendre douze semaines.',
'Synthèse, quatre cas raisonnés et quatre quiz originaux ; correspondance pédagogique PROFILES2017 et exigences MEBEKO2026 sans statut officiel de question.',
'Erreurs de localisation, interprétation des anticorps, estimation de fonction, choix thérapeutique et codage morphologique corrigées avec mécanisme du piège.'
]
monograph=[dict(point=i+1,title=t,anchor=f'n00-{i+1}',sources=sourcemap[i],coverage_explanation=explanations[i]) for i,t in enumerate(titles)]
old=json.loads(Path('/workspace/Medina-nephrologie/docs/collaboration/ssp-v2/execution/ALPHA77-CODEX-N04-INTEGRATE/lesson-manifest.json').read_text())
anchors=['n00-question','n00-1','n00-7','n00-2','n00-semio-normal','n00-10','n00-5','n00-6','n00-4','n00-e-urine','n00-10','n00-11','n00-12','n00-12','n00-12','n00-p-principes','n00-8','n00-e-fonction','n00-annexe-cim','n00-federal']
sm=[['CH-PROFILES'],['CH-CIM','EU-SYNDROMES'],['EU-SYNDROMES','INT-AKI'],['EU-POSTINF','INT-INFECTION'],['NORMAL-FILTRE','EU-HISTO'],['EU-RPGN','INT-INFECTION'],['EU-IGA','INT-INFECTION'],['CH-PEDIATRIC-BP','EU-RPGN'],['CH-URGENCE','EU-IRA'],['CH-SEDIMENT','INT-GN-GENERAL'],['EU-HEMATURIA','INT-INFECTION'],['FI-LASIX-IV','FI-NORVASC','FI-OSPEN'],['INT-INFECTION','EU-IRA'],['INT-INFECTION'],['CH-PEDIATRIC-BP','CH-PREGNANCY'],['CH-ORIENTATION','FI-LASIX-IV'],['CH-SEDIMENT','INT-AKI'],['INT-AKI'],['CH-CIM'],['CH-PROFILES','CH-MEBEKO']]
anchorfiles={a:p for p in files for a in re.findall(r'\bid="([^"]+)"',(ROOT/p).read_text())};rubrics=[];matrix=[]
for i,(a,row) in enumerate(zip(anchors,old['medina_rubrics']),1):
 assert a in anchorfiles,a
 rubrics.append(dict(rubric=i,title=row['title'],anchor=a,content_present=True,current_verification='Auto-relecture et passages réellement lus, avec limites de population et source explicites.',limits='Voir réserves transparentes ; aucune incidence suisse absente ou protocole universel inventé.'))
 evidence=[dict(file=anchorfiles[a],anchor=a)]+[dict(file='source-ledger.json',json_pointer='/sources/'+str(next(j for j,s in enumerate(ledger['sources']) if s['id']==sid)),source_id=sid) for sid in sm[i-1]]
 matrix.append(dict(point=i,title=row['title'],status='covered',evidence=evidence,coverage_scope='Contenu pédagogique présent et sourcé ; couverture ne signifie pas certification clinique ni existence de données non disponibles.'))
save('findings-final.json',dict(code='N00',reviewed_at=NOW,blocking_findings=[],corrected_findings=['Fermeture prématurée du template après point6 : frontières rétablies,8figures et contenu complet vérifiés dans le natif.','Cinq identifiants scientifiques dupliqués : sections renommées sans changer les panneaux.','Espaces et unités dans les fenêtres/tableaux corrigés ; source fig56 ajoutée au ledger.'],transparent_limits=limits))
manifest=dict(code='N00',author='astra_nephrologie',recorded_at=NOW,branch='codex/alpha77/n00-integrate-g1',base='8a512893acbab9caa0dcfdd0e8682a44ea72fda6',monograph=monograph,medina_rubrics=rubrics,matrix20=matrix,sources=ledger['sources'],images=images,semiology=dict(section_anchors=['n00-semio-'+x for x in ['normal','signs','mechanisms','examination','interpretation','differentials','urgency','limits','sources']]),scientific_subtabs=['Sémiologie fondamentale et analytique','Anatomie','Histologie','Physiologie','Biochimie','Immunologie'],reviews=reviews,blocking_findings=[],medical_human_validation=False,clinical_certification=False,tokens_actual=None,cost_actual=None,catalogue_entry_sha256=sha(ROOT/'chapters.json'),canonical_files=files,source_glossary_sha256=final['glossary/n00.py'],preview=dict(path=preview,sha256=ph),limitations=limits,remaining_transparent_limits=limits,closure_status='reviewed_project_delivery_not_clinically_certified')
save('lesson-manifest.json',manifest)
save('source-binding.json',dict(code='N00',verified_at=NOW,preview=preview,preview_sha256=ph,final_sources=final,checks=['test-static.txt','audit-sciences.json','browser-report.json','figures-rights.json','findings-final.json','reviews/medical.json','reviews/language.json','reviews/visual_desktop.json','reviews/visual_mobile.json'],clinical_certification=False))
print('N00:14points,20rubriques,23lectures,4FI,5originaux ; auto-relectures sans certification clinique.')
