from lesson_helpers import *
import re,datetime
for p in CH.glob('*.html'):
 s=p.read_text().replace('Une calcium corrigé élevé','Un calcium corrigé élevé').replace('une option faible dans un sous-groupe','une recommandation de force faible dans un sous-groupe').replace('10.3390/cancers 11101492','10.3390/cancers11101492').replace('Physiology,2013','Physiology, 2013').replace('>sarcomatoïde</button>s','>sarcomatoïdes</button>')
 if p.name=='C64_d.html':
  s=s.replace('<button class="w" data-k="c64-grade">grade</button>','grade')
  s=s.replace('Pas d’ajustement initial rénal légère à sévère ou dialyse, mais efficacité non étudiée chez dialysés.','Pas d’ajustement initial en insuffisance rénale légère à sévère ou sous dialyse, mais efficacité non étudiée chez les patients dialysés.')
  s=s.replace('La FI signale des populations non étudiées, notamment certaines situations de métastases cérébrales ou de saignement digestif récent ; elles demandent une décision spécialisée.','La mise en garde de la FI précise qu’Inlyta ne doit pas être administré aux patients présentant des métastases cérébrales ou ayant récemment présenté une hémorragie gastro-intestinale active, populations non évaluées dans les études citées. Cette restriction doit être vérifiée avec l’équipe avant prescription.')
  s=s.replace('La FI d’Inlyta permet une augmentation en monothérapie après deux semaines de tolérance selon des critères précis, jusqu’à 7 puis 10 mg deux fois/j.','La FI d’Inlyta permet une augmentation en monothérapie après deux semaines sans effet indésirable de grade supérieur à 2, sauf si la pression est supérieure à 150/90 mmHg ou si un traitement hypotenseur est pris : passage à 7 mg, puis éventuellement 10 mg deux fois/j selon les mêmes critères.')
  s=s.replace('Les deux FI doivent être lues pour l’association ;','Pour l’ipilimumab, les analyses pharmacocinétiques n’imposent pas d’adaptation rénale légère/modérée ni hépatique légère ; sécurité et efficacité dans les insuffisances d’organe ne sont pas directement établies. La FI appelle à la prudence devant transaminases initiales ≥5 fois la limite supérieure ou bilirubine >3 fois cette limite. L’hypersensibilité est contre-indiquée pour chacun des deux produits. Les deux FI doivent être lues pour l’association ;')
  s=s.replace('Les deux agents ont des interactions importantes ;','Le pazopanib ne doit pas être associé sans vérification à des médicaments augmentant le pH gastrique : la FI recommande de les éviter, car ils peuvent réduire son absorption. Les deux agents ont des interactions importantes ;')
 s=s.replace('alt="Grade 2 clear cell renal cell carcinoma, showing clearly visible and eosinophilic nucleoli at ×400 magnification."','alt="Microphotographie humaine de carcinome rénal à cellules claires, grade 2 attribué par la source"')
 s=re.sub(r'alt="Histopathology of eosinophilic chromophobe[^\"]*"','alt="Microphotographie humaine de carcinome rénal chromophobe éosinophile, avec barre originale de 100 micromètres"',s)
 s=re.sub(r'alt="Histopathology of papillary renal cell carcinoma[^\"]*"','alt="Microphotographie humaine de carcinome rénal papillaire avec pigment brun décrit comme hémosidérine"',s)
 p.write_text(s)
p=OUT/'source-ledger.json';d=json.loads(p.read_text());versions={'KEYTRUDA':'Août 2026','OPDIVO':'Septembre 2026','YERVOY':'Avril 2025','CABOMETYX':'Décembre 2025','INLYTA':'Septembre 2025','KISPLYX':'Septembre 2025','SUTENT':'Juillet 2024','VOTRIENT':'Septembre 2021'}
for x in d['sources']:
 if x['id'].startswith('FI-'):
  x['version']=versions[x['id'][3:]];x['product_gtin']=x['url'].split('gtin=')[-1];x['limits']+=' Version affichée de FI : '+x['version']+' ; consultation AmiKo le 2 novembre 2026, sans prétendre que toutes les FI ont été révisées en2026.'
  x['limitations']=x['limits']
 if x['id']=='FI-YERVOY':x['section']+=' ; fonctions rénale/hépatique, contre-indications et grossesse';x['passage']+=' Pas d’adaptation PK rénale légère/modérée ni hépatique légère ; prudence si transaminases≥5LSN ou bilirubine>3LSN ; hypersensibilité contre-indiquée.'
 if x['id']=='FI-INLYTA':x['passage']+=' Mise en garde : ne pas administrer en cas de métastases cérébrales ou hémorragie gastro-intestinale active récente, populations non évaluées.'
 if x['id']=='FI-VOTRIENT':x['passage']+=' Éviter les médicaments augmentant le pH gastrique, qui réduisent l’absorption.'
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
# Update material-production receipt after actual edits.
p=OUT/'production.json';d=json.loads(p.read_text());import hashlib
d['final_files']={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in d['final_files']};d['recorded_at']=datetime.datetime.now(datetime.timezone.utc).isoformat();p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('Corrections finales appliquées ; aperçu/tests précédents à renouveler.')
