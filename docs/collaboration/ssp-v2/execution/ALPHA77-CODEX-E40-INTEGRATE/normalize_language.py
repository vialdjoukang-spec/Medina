from pathlib import Path
import re,json
O=Path(__file__).resolve().parent;R=O.parents[4];changes=[]
def normalize(t):
 t=t.replace('SpirigHC','Spirig HC').replace('SuisseSA','Suisse SA').replace('d’aprèsv.Ebner','d’après v. Ebner').replace('deV.Horsley','de V. Horsley').replace('deHis','de His')
 t=re.sub(r'(?<=\d)(?=(?:ans?|mois|jours?|heures?|minutes?|secondes?|semaines?|repas|prises?|fois|visites?|mesures?|kcal|mg|kg|mL|mmol|mm|cm|g|L|z)\b)',' ',t)
 t=re.sub(r'\b(OMS|UNICEF|GLIM|ESPEN|OFS|FI|guide|revue|version|tableau|suisse|pédiatrique|Benerva|PHIL|édition|planche|photographie|étude|systématique|de|en|les|des|aux|apporte|contient|dont|pendant|premières|deuxfois|seules|dix|et)(?=\d)',r'\1 ',t)
 t=re.sub(r'\b(Annexe|annexe|encadrés|encadré|figure|Recommandation|Recommandations|Enfant|enfant|circuit|pédiatriques|plage|phase|propose|copier|distingue|donnent|suspension|MAS|GTIN|comprimés|comprimé|ou|contenant|dès|que|le|maximale|max|maximum|ambulatoire|représente|soit|ClCr|RUTF|proposé|sur|HC|avril|août|GM|p|à)(?=\d)',r'\1 ',t)
 t=re.sub(r'\b(PB|Estimation|protéines|inclut|Entre|début|Avant|chez|une|pour|puis)(?=\d)',r'\1 ',t)
 t=re.sub(r'(?<=\d)(?=études\b)',' ',t)
 t=t.replace('vitamineA','vitamine A')
 t=re.sub(r'(20\d{2}),(?=[A-Za-zÀ-ÿ0-9])',r'\1, ',t)
 t=re.sub(r';(?=[A-Za-zÀ-ÿ0-9])','; ',t)
 t=re.sub(r'(?<=[A-Za-zÀ-ÿ0-9])([≤≥])',r' \1',t)
 t=t.replace('vitamineB1','vitamine B1').replace('enmg','en mg')
 t=re.sub(r'(?<=[A-Za-zÀ-ÿ]),(?=\d)',', ',t)
 t=t.replace('à++','à ++').replace('de+++','de +++').replace(';+++','; +++')
 t=t.replace('CC BY-SA3.0','CC BY-SA 3.0')
 t=t.replace('deuxfois','deux fois').replace('demL','de mL').replace('deμ','de μ')
 t=re.sub(r'([≤≥=×÷])(?=\d)',r'\1 ',t);t=re.sub(r'(?<=\d)([≤≥=×÷])',r' \1',t)
 return t
for p in sorted((R/'chapters/E40').glob('*.html')):
 original=p.read_text();parts=re.split(r'(<(?=[A-Za-z/!])[^>]*>)',original)
 # Only text segments change. Scientific identifiers and all attributes stay intact.
 for i in range(0,len(parts),2):parts[i]=normalize(parts[i])
 result=''.join(parts);p.write_text(result);changes.append(dict(file=str(p.relative_to(R)),changed=result!=original))
(O/'language-transform.json').write_text(json.dumps(dict(scope='Espaces typographiques explicites autour des unités et mots ciblés, texte uniquement ; aucune règle générique chiffre-vers-lettre, aucun identifiant scientifique altéré.',files=changes),ensure_ascii=False,indent=2)+'\n')
print('Espaces ciblés appliqués aux six surfaces ; attributs et identifiants préservés.')
