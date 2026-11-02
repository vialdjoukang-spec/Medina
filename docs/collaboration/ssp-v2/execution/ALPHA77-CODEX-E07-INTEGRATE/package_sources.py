from pathlib import Path
import json,hashlib,datetime
D=Path(__file__).resolve().parent
j=json.loads((D/'recherche_E07/sources.json').read_text())
paraphrases={
'S1':'Le catalogue suisse local distingue E07.0, E07.1, E07.8 et E07.9 ; ces catégories ne définissent pas une maladie unique.',
'S2':'Les notes internationales incluent hyperplasie C, goitre dyshormonogénétique et Pendred, anomalies de liaison, hémorragie, infarctus et syndrome de basse T3. P72.0 est exclu de E07.1.',
'S3':'Le consensus recommande de traiter une hypothyroïdie congénitale confirmée avant l’imagerie. Les doses initiales dépendent de la FT4 et de la gravité ; suivi précoce, normes d’âge, génétique et surveillance du goitre sont contextualisés.',
'S4':'Les variants constitutionnels RET prédisposent à une NEM2 dominante. Le calendrier de chirurgie et de surveillance dépend du risque génétique ; l’évaluation familiale et du phéochromocytome précède les décisions spécialisées.',
'S5':'Le panel ne tranche pas pour ou contre la calcitonine systématique dans tout nodule. Il décrit des indications ciblées, des seuils dépendants de variables et l’usage du lavage de ponction dans certains dossiers suspects.',
'S6':'La calcitonine, ses précurseurs, ses méthodes et interférences demandent une interprétation contextualisée. Les fourchettes des causes non médullaires se chevauchent ; procalcitonine et CEA ont des rôles distincts.',
'S7':'Dans 16 études totalisant 72 368 personnes avec nodules, le seuil de 10 pg/ml donne une forte sensibilité mais une faible valeur prédictive positive à faible prévalence. Les biais de vérification limitent fortement cette estimation.',
'S8':'Chez 135 patients sélectionnés pour chirurgie, dont 47 cancers médullaires, les seuils basaux et stimulés sont propres à Immulite 2000. La tolérance distingue 133 observations et 67 ECG : 16,4 % de bradycardies avant, 25,4 % après, 9 % nouvelles.',
'S9':'La cohorte chirurgicale associe 335 patients néerlandais et 61 suisses, dont 44 cancers médullaires. La combinaison calcitonine/procalcitonine est prometteuse, mais ses performances ne sont pas celles d’un dépistage général.',
'S10':'Onze études avec 5 817 patients et 335 cancers médullaires donnent une sensibilité groupée de 0,90 et une spécificité de 1,00, avec intervalles de confiance larges. Le résumé seul ne définit pas un seuil universel.',
'S11':'Le résumé anatomopathologique distingue hyperplasie C réactive et prolifération néoplasique ; le nombre de cellules et la valeur de calcitonine ne remplacent pas la lecture histologique.',
'S12':'L’hyperplasie C peut accompagner des contextes différents ; architecture et immunohistochimie permettent de caractériser la lésion, sans déduire une conduite chirurgicale d’un seul chiffre.',
'S13':'Pendred associe surdité et atteinte thyroïdienne variable liées à SLC26A4. La pendrine participe aux échanges d’anions dans plusieurs organes ; des voies alternatives peuvent moduler le phénotype thyroïdien.',
'S14':'La revue audiologique rassemble 13 publications et 75 patients ; le pourcentage cité concerne les surdités héréditaires, pas la population suisse entière.',
'S15':'Parmi 37 probands sélectionnés pour aqueduc vestibulaire élargi ou Pendred, 13 diagnostics génétiques sont résolus, dont 7 Pendred et 6 formes auditives non syndromiques.',
'S16':'La maladie critique modifie axe, liaison, transport et métabolisme selon les tissus. TSH normale et reverse-T3 ne suffisent pas à exclure une hypothyroïdie ; les essais ne justifient pas une substitution systématique du seul profil NTIS.',
'S17':'Les cas de déficit TBG montrent des hormones totales basses avec euthyroïdie possible ; une patiente avait toutefois une hypothyroïdie auto-immune coexistante. Les fréquences citées viennent de l’introduction, pas d’une estimation par ces quatre cas.',
'S18':'Un nouveau-né avait une TBG de concentration normale mais de faible affinité, produisant un dépistage trompeur fondé sur T4 ; la fonction libre aidait à reconnaître l’euthyroïdie.',
'S19':'La FI suisse Euthyrox précise les doses par âge, les contre-indications cardiaques et surrénaliennes, la prise à jeun, les interactions et la surveillance. Les fréquences d’effets indésirables ne sont pas quantifiables ; les doses néonatales ne sont pas identiques au tableau de gravité ENDO-ERN.',
'S20':'Le dépistage suisse est décrit au quatrième jour, pour onze maladies et environ 80 000–85 000 échantillons annuels. La fréquence d’hypothyroïdie indiquée est environ 1/3 500, sans fournir ici un seuil opérationnel de rappel.',
'S21a':'Une hémorragie thyroïdienne traumatique a été surveillée sans opération chez une femme sans détresse ni stridor ; ce cas ne justifie pas l’observation seule devant une obstruction.',
'S21c':'Un décès par hémorragie cervicale compressive après cytoponction documente une complication rare ; la priorité clinique porte sur les voies aériennes.',
'S22':'Le résumé relie stress et cortisol à la régulation centrale et au métabolisme hormonal. Ces mécanismes généraux ne justifient pas une substitution ni une supplémentation dans le NTIS.',
'S23':'Sur 104 cancers médullaires opérés à Pise, 85 avaient eu une cytoponction, diagnostique dans 45,9 % de ce sous-groupe. Cette sélection ne mesure pas la spécificité dans tous les nodules.',
'S25':'Un variant homozygote TG a été rapporté avec goitre massif, compression néonatale et contexte de maladie critique ; intubation et lévothyroxine figurent dans le cas, sans protocole universel déduit.',
'S26':'Quatre goitres fœtaux graves pris en charge dans un centre tertiaire ont eu des issues hétérogènes, dont un seul survivant ; une telle série ne fournit pas un pronostic universel.',
'S27':'La série soudanaise étudie des familles sélectionnées avec hypothyroïdie congénitale et défauts de pendrine ; les estimations historiques de fréquence ne sont pas une prévalence suisse.',
'S28':'Des membres d’une famille portant le même variant SLC26A4 avaient une anatomie de l’oreille interne variable ; une morphologie inhabituelle ne suffit pas à écarter la maladie.',
'S29':'La revue d’implantation cochléaire rapporte généralement un bénéfice chez Pendred, avec des données surtout observationnelles et de faible niveau.',
'S30':'Un cas associant cancers et Pendred est décrit avec une revue ; le faible nombre de cas ne démontre ni risque individuel fiable ni rôle oncogène causal de SLC26A4.',
'S31':'L’approche clinique récente relie phénotype d’hypothyroïdie congénitale, sélection de tests génétiques et implications de prise en charge ; le résumé n’est pas un protocole détaillé.',
'S32':'Le CHUV demande un sérum sans gel et un transport immédiat en trente minutes, sinon séparation et congélation ; le contexte d’IPP et le moment du prélèvement sont à documenter.',
'S33':'Viollier décrit ses propres conditions de sérum et congélation et des références de calcitonine inférieures à 4,9 ng/L chez la femme et 11,9 chez l’homme ; ce ne sont pas des seuils opératoires.',
'S34':'Le RCP allemand exact fournit 2,25 mmol de calcium total par 10 ml et une vitesse adulte au plus 2 ml/min pour hypocalcémie aiguë symptomatique. Le test de calcitonine est hors indication ; contre-indications, ceftriaxone, glycosides et extravasation demandent attention.',
'S35':'La fiche PHEL identifie le calcium B. Braun comme importé ; elle permet de rattacher le contexte suisse au RCP allemand exact, sans autoriser automatiquement le protocole diagnostique d’une étude.',
'S36':'Devant des tests thyroïdiens discordants, l’ETA recommande d’examiner contexte et interférences avant l’exploration ciblée des transporteurs, du métabolisme ou des récepteurs hormonaux.',
'S37':'PROFILES 2017 inclut l’examen du cou et de la thyroïde, le goitre, l’audition et les hormones thyroïdiennes anormales. Le rapprochement du cours avec ces compétences reste pédagogique.',
'S38':'Des remaniements après ponction ont été retrouvés dans 17 des 656 patients opérés d’une série sélectionnée ; ce taux ne mesure pas le risque de toute ponction.',
'S39':'Dans 28 cas d’infarctus après ponction, l’histologie pouvait diverger de la cytologie initiale à cause de fibrose, nécrose ou tissu périphérique méconnu. Transmettre l’histoire du geste facilite l’interprétation.',
'S40':'Un carcinome papillaire remanié après ponction illustre la nécessité d’examiner les zones viables et la capsule ; disparition apparente ne prouve pas guérison.',
'S41':'Les anomalies héréditaires de protéines de liaison incluent déficit et excès de TBG, ce dernier pouvant résulter de duplication ou triplication ; total et libre peuvent diverger sans hyperthyroïdie.',
'S42':'La thyroïde normale comprend lobes et isthme autour de la trachée ; les follicules associent épithélium et colloïde. Ces bases situent la fonction sans diagnostiquer une lésion à partir d’une image normale.'}
assert set(paraphrases)=={x['id'] for x in j['sources']}
sources=[];cache={}
for x in j['sources']:
 p=Path(x['cache_external']);assert p.is_file(),p
 h=hashlib.sha256(p.read_bytes()).hexdigest();assert h==x['sha256'],x['id']
 cache[str(p)]={'sha256':h,'bytes':p.stat().st_size}
 sources.append(dict(id=x['id'],url=x['url'],publisher=x['editeur'],version=x['version_annee'],read_at=x['date_consultation'],section=x['section_page'],passage=paraphrases[x['id']],passage_kind='faithful_paraphrase',population=x['population'],limits=x['limites'],source_content_sha256=h,read_level='Passages identifiés ; résumés seuls lorsque signalés. Aucune lecture intégrale globale revendiquée.'))
save=lambda n,v:(D/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
save('source-ledger.json',{'sources':sources,'clinical_certification':False,'full_text_storage':'Cache de travail externe ; aucun texte intégral non libre reproduit dans ce registre.'})
save('source-cache-manifest.json',{'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':cache,'unique_files':len(cache),'bytes':sum(x['bytes'] for x in cache.values()),'tokens_actual':None,'cost_actual':None})
print(len(sources),'sources paraphrasées',len(cache),'fichiers de cache distincts')
