from pathlib import Path
import re,json
O=Path(__file__).resolve().parent;R=O.parents[4];changes=[]
def normalize(t):
 t=t.replace('SpirigHC','Spirig HC').replace('SuisseSA','Suisse SA').replace('d’aprèsv.Ebner','d’après v. Ebner').replace('deV.Horsley','de V. Horsley').replace('deHis','de His')
 t=re.sub(r'(?<=\d)(?=(?:ans?|mois|comprimés?|capsules?|jours?|heures?|minutes?|secondes?|semaines?|repas|prises?|fois|visites?|mesures?|kcal|mg|µm|micromètres?|kg|mL|mmol|mm|cm|g|L|z)\b)',' ',t)
 t=re.sub(r'\b(OMS|UNICEF|GLIM|ESPEN|OFS|FI|guide|revue|version|tableau|suisse|pédiatrique|Benerva|PHIL|édition|planche|photographie|étude|systématique|de|en|les|des|aux|apporte|contient|dont|pendant|premières|deuxfois|seules|dix|et)(?=\d)',r'\1 ',t)
 t=re.sub(r'\b(Annexe|annexe|encadrés|encadré|figure|Recommandation|Recommandations|Enfant|enfant|circuit|pédiatriques|plage|phase|propose|copier|distingue|donnent|suspension|MAS|GTIN|comprimés|comprimé|ou|contenant|dès|que|le|maximale|max|maximum|ambulatoire|représente|soit|ClCr|RUTF|proposé|sur|HC|avril|mai|juin|février|BAP|PHEL|LIQ|Parlodel|Symmetrel|Akineton|Madopar|OFS|tableau|GM|p|à)(?=\d)',r'\1 ',t)
 t=re.sub(r'\b(PB|Estimation|protéines|inclut|Entre|début|Avant|chez|une|pour|puis)(?=\d)',r'\1 ',t)
 t=re.sub(r'(?<=\d)(?=études\b)',' ',t)
 t=t.replace('vitamineA','vitamine A').replace('Child-PughC','Child-Pugh C')
 t=re.sub(r'(20\d{2}),(?=[A-Za-zÀ-ÿ0-9])',r'\1, ',t)
 t=re.sub(r';(?=[A-Za-zÀ-ÿ0-9])','; ',t)
 t=re.sub(r'(?<=[A-Za-zÀ-ÿ0-9])([≤≥])',r' \1',t)
 t=t.replace('vitamineB1','vitamine B1').replace('enmg','en mg')
 t=re.sub(r'(?<=[A-Za-zÀ-ÿ]),(?=\d)',', ',t)
 t=t.replace('à++','à ++').replace('de+++','de +++').replace(';+++','; +++')
 t=t.replace('CC BY-SA3.0','CC BY-SA 3.0')
 t=t.replace('deuxfois','deux fois').replace('demL','de mL').replace('deμ','de μ')
 t=re.sub(r'([≤≥=×÷])(?=\d)',r'\1 ',t);t=re.sub(r'(?<=\d)([≤≥=×÷])',r' \1',t)
 t=re.sub(r'\b(antagonisme|agonisme|blocage|occupation)(?=D2\b)',r'\1 ',t)
 t=re.sub(r'\b(métabolisme|interactions)(?=CYP3A(?:4)?\b)',r'\1 ',t)
 t=re.sub(r'\b(labels)(?=SN\b)',r'\1 ',t)
 t=re.sub(r'\b(catégorie|tout)(?=G21\b)',r'\1 ',t)
 t=re.sub(r'\b(HUG|DGN|URL|Gray|consensus|coréenne|internationale|Début|Retard|avec|capsule|clairance|dans|est|habituellement|immédiat|injectable|moins|non|plus|rapport|tranche)(?=\d)',r'\1 ',t)
 t=t.replace('nomMadopar125','nom Madopar 125').replace('24janvier2021','24 janvier 2021').replace('SA4.0','SA 4.0')
 return t
for p in sorted((R/'chapters/G21').glob('*.html')):
 original=p.read_text();parts=re.split(r'(<(?=[A-Za-z/!])[^>]*>)',original)
 # Only text segments change. Scientific identifiers and all attributes stay intact.
 for i in range(0,len(parts),2):parts[i]=normalize(parts[i])
 result=''.join(parts);p.write_text(result);changes.append(dict(file=str(p.relative_to(R)),changed=result!=original))
(O/'language-transform.json').write_text(json.dumps(dict(scope='Espaces typographiques explicites autour des unités et mots ciblés, texte uniquement ; aucune règle générique chiffre-vers-lettre, aucun identifiant scientifique altéré.',files=changes),ensure_ascii=False,indent=2)+'\n')
print('Espaces ciblés appliqués aux six surfaces ; attributs et identifiants préservés.')
