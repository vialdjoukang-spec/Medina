from pathlib import Path
import re,json,datetime
P=Path('chapters/E00');D=Path('docs/collaboration/ssp-v2/execution/ALPHA77-CODEX-E00-INTEGRATE')
fix={
'Aucune recommandation suisse dédiée au crétinisme endémique ni à la supplémentation iodée en grossesse n’a été lue.':'Les pages OSAV sur le sel iodé, la grossesse et l’allaitement ainsi que les questions et réponses de2018 et2024 ont été lues lors de la reprise. Elles soutiennent une discussion individualisée du complément. Aucune recommandation suisse dédiée au syndrome E00 constitué n’a été obtenue.',
'chez le nourrisson de 0 à 6 mois, l’apport passe par le lait d’une mère supplémentée.':'chez le nourrisson allaité, le lait apporte l’iode dont la concentration dépend de l’alimentation maternelle. Un complément maternel n’est pas automatique en Suisse : son indication se discute selon les conseils OSAV.',
'100 µg/l définit un apport adéquat':'une médiane d’au moins100 µg/l correspond à un apport adéquat dans le tableau OMS',
'une médiane de 100 µg/l définit un apport adéquat':'une médiane d’au moins100 µg/l correspond à un apport adéquat dans le tableau OMS',
'Aucune source lue ne montre le bénéfice d’un traitement tardif du crétinisme constitué.':'Aucune preuve de récupération des lésions neurologiques anciennes n’est établie ici ; une hypothyroïdie persistante doit néanmoins être traitée.',
'Un nouveau-né hypothyroïdien : lévothyroxine 10 à 15 µg/kg/jour, TSH normalisée en 4 semaines.':'Un nouveau-né hypothyroïdien reçoit une dose individualisée selon la sévérité ;10–15 µg/kg/jour pour les formes sévères, avec surveillance précoce.',
'Nouveau-né hypothyroïdien : lévothyroxine 10 à 15 µg/kg/jour, TSH normalisée en 4 semaines.':'Nouveau-né hypothyroïdien : dose individualisée selon la sévérité ;10–15 µg/kg/jour pour une forme sévère. La normalisation de la TSH en4semaines est un objectif de la forme primaire.',
'Lévothyroxine : 10 à 15 µg/kg/jour au début, ajustée sur TSH et fT4.':'Lévothyroxine néonatale : dose selon la sévérité,10–15 µg/kg/jour dans une forme sévère ; suivi primaire par TSH/fT4, central principalement par fT4.',
'Contrôles : 1 à 2 semaines, puis toutes les 2 semaines, puis espacés selon l’âge.':'Contrôle à1–2semaines, au plus tard une semaine si dose initiale proche de15 µg/kg/jour ; puis toutes les2semaines jusqu’à normalisation de la TSH primaire, puis selon l’âge.',
'Des doses initiales d’au moins 10 µg/kg/jour sont associées à des résultats comparables à ceux de la fratrie.':'Dans les cohortes rapportées, un traitement précoce avec doses initiales d’au moins10 µg/kg/jour était associé à des résultats comparables à ceux de la fratrie ; cela ne constitue pas une dose universelle pour toutes les formes légères.',
'Conclure à un trouble central devant une TSH « normale » sans regarder la fT4':'Écarter un trouble central parce que la TSH est « normale », sans regarder la fT4',
'Chez l’enfant plus grand, un scanner cérébral peut montrer des calcifications des noyaux gris centraux chez les hypothyroïdiens sévères, et une audiométrie quantifie la surdité.':'Dans les séries historiques, un scanner a montré des calcifications des noyaux gris centraux chez certains sujets sévèrement hypothyroïdiens ; cette observation ne justifie pas un scanner systématique. Une audiométrie documente l’atteinte auditive.',
'<td>L’atteinte cérébrale est-elle constituée ?</td><td>Scanner cérébral (calcifications des noyaux gris) chez l’hypothyroïdien sévère</td><td>Non systématique</td>':'<td>Que décrivaient les séries historiques ?</td><td>Calcifications des noyaux gris observées au scanner chez certains sujets sévèrement hypothyroïdiens</td><td>Observation historique, sans indication de scanner systématique établie par ces séries</td>',
'les fréquences exactes ne sont pas reproduites.':'le chiffre15sur50 concerne seulement le sous-groupe historique examiné au scanner, sans constituer une fréquence générale d’E00.',
'Sur 112 crétins âgés de 2 à 66 ans':'Sur112personnes atteintes, âgées de2à66ans',
'Chez 104 crétins chinois et 35 crétins javanais':'Chez104personnes atteintes en Chine et35àJava',
'La prévalence d’apport inadéquat (moins de 160 µg/jour)':'La proportion estimée d’apport inadéquat (seuil de calcul de l’étude : moins de160 µg/jour, non seuil de diagnostic individuel)'
}
for p in P.glob('*.html'):
 s=p.read_text()
 for a,b in fix.items():s=s.replace(a,b)
 s=s.replace('Des calcifications','Des calcifications')
 # Legacy scientific diagram: distinguish thyroid transport from speculative mammary inhibition.
 if p.name=='E00_c.html':
  s=s.replace('<figure aria-label="Transport de l’iodure et compétition du thiocyanate">','<figure aria-label="Transport thyroïdien de l’iodure">').replace('Figure 3 — Entrée de l’iodure et compétition du thiocyanate','Figure 3 — Entrée de l’iodure dans la synthèse hormonale thyroïdienne')
  s=s.replace('<path d="M320 40v-22m0 0l-6 10m6-10l6 10" stroke-dasharray="4 3"/>','').replace('<text x="320" y="12" text-anchor="middle" font-size="12">Thiocyanate : inhibition compétitive (hypothèse)</text>','')
  s=s.replace('Le thiocyanate est proposé comme inhibiteur compétitif dans la glande mammaire (hypothèse spéculative selon les auteurs).','L’hypothèse de l’inhibition du transport dans la glande mammaire par le thiocyanate est discutée séparément dans le texte ; elle n’est pas représentée par la chaîne thyroïdienne de cette figure.')
 # Respectful nouns and readability, preserving the historical syndrome name.
 s=s.replace('112 crétins','112 personnes atteintes').replace('104 crétins','104 personnes atteintes').replace('35 crétins','35 personnes atteintes')
 parts=re.split(r'(<[^>]*>)',s)
 for i in range(0,len(parts),2):
  v=parts[i]
  v=re.sub(r'\b([A-Za-zÀ-ÖØ-öø-ÿ]{2,})(\d+)\b',lambda m:m.group(0) if m.group(1) in {'fT','SLC','TBG'} else m.group(1)+' '+m.group(2),v)
  v=re.sub(r'(?<=\d)(?=(?:personnes|enfants|femmes|patients|sujets|scanners|pour|sur|Java|µg|mg|kg|pmol|mU|semaines?|jours?|mois|ans|heures?|à|%|°C))',' ',v)
  v=re.sub(r'\b(à|À|de|en)(?=\d|µg)',r'\1 ',v)
  parts[i]=v
 p.write_text(''.join(parts))
# Public source recheck contains paraphrases, never long excerpts from paywalled journals.
f=D/'recherche_E00/inherited-recheck.json';j=json.loads(f.read_text())
paraphrases={
'36795091':'Histoire de la prévention ; iodation du sel en Suisse et aux États-Unis dans les années1920, puis réduction mondiale des troubles carentiels.',
'35552681':'Le nourrisson allaité reçoit l’iode du lait, dont la teneur dépend de l’apport maternel ; besoins élevés et incertitudes sur les déficits légers.',
'29030199':'Essai Inde/Thaïlande :832femmes initialement incluses ;313enfants évalués pour le QI et315pour les fonctions exécutives.200µg/jour pendant la grossesse n’a pas montré de bénéfice neurodéveloppemental à5–6ans dans cette population légèrement carencée ; ne pas extrapoler à la carence sévère.',
'25591468':'La carence sévère peut dépasser l’adaptation thyroïdienne. La correction populationnelle peut augmenter transitoirement l’hyperthyroïdie ; l’auto-immunité et l’hypothyroïdie infraclinique augmentent légèrement.',
'19460960':'Revue de2009 décrivant l’insuffisance des apports et les méthodes de surveillance. Les estimations mondiales et européennes appartiennent à cette époque.',
'18936198':'Résumé historique qui attribue à Coindet une utilisation de l’iode en1813 et décrit la continuité du programme suisse depuis1922 ; chronologie rapportée à cette source.',
'16087983':'Après l’augmentation de15à20mg/kg de l’iode du sel suisse en1999, les enquêtes de1999/2004 ont constaté de meilleures médianes d’iodurie et une baisse de2,9%à1,7% des TSH néonatales supérieures à5mU/L.',
'15611818':'Résumé physiopathologique : captation iodée accrue, augmentation de la masse glandulaire, sécrétion préférentielle deT3 et TSH élevée dans l’adaptation à la carence.',
'12487772':'L’inhibition mammaire du transport iodé par le thiocyanate est discutée à partir de données animales ; son rôle humain dans le tableau myxœdémateux est explicitement spéculatif.',
'7520008':'Le titre évoque iode, sélénium et goitrogènes ; absence de résumé et de texte intégral dans cette acquisition. Aucun mécanisme précis ni intervention n’en est tiré.'}
for a in j['records']:
 a.pop('actual_abstract_excerpt',None);a.pop('excerpt_limit',None);a['faithful_paraphrase']=paraphrases[a['pmid']]
# The two abstracts reread from a previous cached request remain independently traceable.
b=json.loads((D/'recherche_E00/downloads/olderclinical.raw').read_text())
for a in b['resultList']['result']:
 if a['id'] in {'20172469','24311738'}:
  j['records'].append({'pmid':a['id'],'title':a['title'],'url':'https://pubmed.ncbi.nlm.nih.gov/'+a['id']+'/','read_level':'abstract','read_at':'2026-11-02','faithful_paraphrase':'Deux syndromes historiques liés à la carence alimentaire iodée, évitables par correction avant grossesse ; données mondiales de la période du résumé.' if a['id']=='20172469' else 'Le symporteur sodium-iodure transporte activement l’iodure et intervient au début de la synthèse thyroïdienne ; expression également dans des tissus extrathyroïdiens.','limits':'Résumé seul ; pas de prétention de lecture du texte intégral.'})
f.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
f=D/'recherche_E00/sources.json';j=json.loads(f.read_text())
for a in j['sources']:
 if a['id']=='S101':a['section_page']=a['section_page'].replace('posologie pédiatrique','posologie adulte, gériatrique et pédiatrique');a['population']='Adultes, adolescents, enfants et nourrissons recevant Euthyrox ; annexes distinctes selon contexte';a['additional_read_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
f.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print('Auto-relecture MED/LANG : fenêtres, résumés, figures, niveaux de preuve et tableaux harmonisés.')
