from pathlib import Path
import difflib,json,hashlib,re,datetime
D=Path(__file__).resolve().parent;root=Path.cwd();changes=[];data={}
def replace(path,old,new,id,source):
 if path not in data:data[path]=(root/path).read_text()
 n=data[path].count(old)
 if n!=1:raise RuntimeError((id,path,n))
 data[path]=data[path].replace(old,new)
 changes.append(dict(id=id,path=path,avant=old,apres=new,sources=source))
p='chapters/E10/E10_b.html'
replace(p,'Le guide suisse retient l’absence d’artériopathie significative lorsque les deux pouls du pied sont palpables et que l’index de pression systolique cheville-bras est ≥ 0,9 ; moins de deux pouls ou un index &lt; 0,9 font suspecter une artériopathie.',
'Pour orienter une plaie vers les soins de premier recours, le guide suisse utilise notamment deux pouls du pied palpables et un index cheville-bras ≥ 0,9. Ces critères de filière ne suffisent pas à exclure une artériopathie. Le guide intersociétés IWGDF/ESVS/SVS 2023 recommande de combiner les courbes Doppler pédieuses, l’index cheville-bras et l’index orteil-bras : une artériopathie est moins probable avec un index cheville-bras de 0,9 à 1,3, un index orteil-bras ≥ 0,70 et des courbes biphasiques ou triphasiques. Aucun seuil isolé ne l’exclut. <a href="https://iwgdfguidelines.org/wp-content/uploads/2023/07/IWGDF-2023-05-PAD-Guideline.pdf" target="_blank" rel="noopener">Source complémentaire européenne : recommandations diagnostiques 2 et 4, 2023</a>.', 'E10-M01',['S3','S4'])
p='chapters/E10/E10_pop1.html'
replace(p,'l’artériopathie est peu probable si les deux pouls du pied sont palpables et l’index cheville-bras ≥ 0,9.',
'le guide suisse emploie deux pouls palpables et un index cheville-bras ≥ 0,9 pour orienter les plaies simples. Ce raccourci ne constitue pas un test d’exclusion : en présence d’une plaie ou d’une suspicion vasculaire, le guide IWGDF/ESVS/SVS 2023 associe les courbes Doppler, l’index cheville-bras et l’index orteil-bras; aucun résultat isolé n’exclut l’artériopathie. <a href="https://iwgdfguidelines.org/wp-content/uploads/2023/07/IWGDF-2023-05-PAD-Guideline.pdf" target="_blank" rel="noopener">Recommandations 2 et 4</a>.','E10-M01-fenetre',['S3','S4'])
replace(p,'Le diagnostic de diabète précède celui du type et de la crise.','L’urgence métabolique est recherchée immédiatement; le diagnostic de diabète, son type et l’existence d’une crise sont trois questions distinctes.','E10-M02',['S8','S9'])
p='chapters/E10/E10_c.html'
replace(p,'la destruction des seules cellules β explique pourquoi le type 1 donne une hyperglycémie sans trouble digestif.',
'la perte de fonction β explique l’hyperglycémie. Cette distinction n’exclut pas des symptômes digestifs : une neuropathie autonome ou une gastroparésie peuvent notamment en provoquer et appellent leur propre évaluation.','E10-M03',['S8'])
replace(p,'La cétogenèse hépatique ne s’arrête que sous insuline : la perfusion continue donc après la baisse du glucose,',
'Dans l’acidocétose, l’insuline reste nécessaire pour faire régresser la cétose : la perfusion continue donc après la baisse du glucose,','E10-M04',['S9'])
p='chapters/E10/E10_pop2.html'
replace(p,'leur perte explique l’hyperglycémie sans trouble digestif.','leur perte explique l’hyperglycémie, sans exclure une complication digestive qui nécessite une évaluation propre.','E10-M03-fenetre',['S8'])
replace(p,'Une erreur de concentration change le volume, pas le nombre d’unités prescrit.',
'À nombre d’unités prescrit identique, changer la concentration modifie le volume injecté. Le compteur du stylo reste réglé sur les unités prescrites; il ne faut pas les convertir.','E10-M05',['S6'])
for p,new in data.items():
 out=D/'drafts'/p;out.parent.mkdir(parents=True,exist_ok=True);out.write_text(new)
patch=''.join(''.join(difflib.unified_diff((root/p).read_text().splitlines(True),new.splitlines(True),fromfile='a/'+p,tofile='b/'+p)) for p,new in sorted(data.items()))
(D/'enrichissements.patch').write_text(patch)
(D/'propositions.json').write_text(json.dumps({'statut':'propositions non intégrées; brouillons soumis à corrections/réserves', 'changes':changes},ensure_ascii=False,indent=2)+'\n')
(D/'annexe-cim.md').write_text('''# Annexe de travail : E10 — périmètre administratif vérifié\n\n[S10] BfArM, GM2024, bloc E10–E14 : E10.01 (coma hyperglycémique, exclut le coma hypoglycémique), E10.11 (acidocétose sans mention de coma), E10.20/.21 (rein), E10.30/.31 (œil), E10.40/.41 (neurologie), E10.50/.51 (vasculaire périphérique), E10.60/.61 (autres complications précisées, dont hypoglycémie/coma hypoglycémique), E10.72/.73 (autres complications multiples), E10.74/.75 (pied diabétique), E10.80/.81 (complications non précisées), E10.90/.91 (sans complication). Les finales0/1 et2/3/4/5 suivent exactement les modificateurs du bloc.\n\nCette liste de20 codes ne crée pas20 leçons. Le cours traite narrativement les atteintes mais ne présente pas cette correspondance vérifiable. Les codes associés astérisque et les exclusions (notamment O24 pendant grossesse) restent à contrôler dans l’édition OFS effectivement applicable; la page allemande2024 ne suffit pas à certifier le codage suisse2026. Annexe pour l’intégrateur; ne pas déplacer le plan clinique vers un cours de codage.\n''')
