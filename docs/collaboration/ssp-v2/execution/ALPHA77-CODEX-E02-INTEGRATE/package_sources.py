from pathlib import Path
import json,hashlib,datetime
D=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
raw=json.loads((D/'recherche_E02/sources.json').read_text())['sources']
paraphrases=[
'Le catalogue OFS local nomme E02 hypothyroïdie par carence inapparente en iode, sans sous-code. Le profil biologique seul ne prouve pas la cause iodée.',
'Le guide OMS distingue indicateurs collectifs et diagnostic individuel, décrit la palpation et les grades de goitre, les médianes urinaires et les marqueurs. Sa supplémentation de programme vise les groupes sans accès suffisant au sel iodé.',
'Deux régions danoises étudiées avant iodation présentaient des incidences différentes de maladies thyroïdiennes manifestes selon leur statut iodé. Ces taux historiques ne décrivent ni la Suisse actuelle ni E02.',
'L’OSAV conseille le sel iodé sans augmenter le sel consommé et décrit les aliments sources, groupes à risque et compléments pris en grossesse ou allaitement. Le conseil nutritionnel ne diagnostique pas une HIC.',
'L’enquête suisse 2020–2022 rapporte des médianes urinaires de 127 µg/L chez les enfants et 97 chez les femmes enceintes. Le sang séché mesurait TSH et T4 totale ; les associations avec les suppléments ne prouvent pas une guérison de l’HIC.',
'Le produit axapharm 65 mg d’iodure de potassium correspond à 50 mg d’iode et est destiné à la radioprotection sur instruction des autorités. Sa dose et ses risques l’excluent d’une supplémentation nutritionnelle.',
'La FI Euthyrox décrit une substitution individualisée, ses doses, interactions, contre-indications et effets indésirables. L’autorisation générale ne justifie pas le traitement de toute HIC légère ; les chiffres pédiatriques de la FI sont distincts des données harmonisées ajoutées après elle.',
'Le texte de physiologie décrit les lobes, l’isthme, les follicules, la colloïde, la synthèse sur thyroglobuline et le rétrocontrôle. Il sert à expliquer le normal ; la licence de l’image originale de 2013 est contrôlée séparément.',
'PROFILES 2017 comporte l’examen de la thyroïde, le goitre et les anomalies hormonales comme compétences ou situations de départ. Le lien avec les vignettes E02 est pédagogique, sans question officielle reproduite.',
'L’ETA 2013 exige une interprétation et une confirmation de TSH adaptées, recherche les causes, distingue traitement et surveillance selon l’âge et le profil, et prévoit de réévaluer un essai symptomatique. Ces recommandations précèdent les essais ultérieurs.',
'La section pédiatrique de l’ETA 2014 demande des normes par âge et méthode et décrit des évolutions différentes selon les causes. Les résultats de séries sélectionnées ne sont pas une probabilité universelle de normalisation.',
'La revue suisse décrit l’adaptation selon le degré de carence, les besoins infantiles, l’alimentation et les limites des marqueurs. Une carence légère peut laisser la TSH et la T4 normales ; les chiffres réglementaires de 2020 restent datés.',
'La HAS propose un diagnostic par étapes, des décisions distinctes pour HIC, personne âgée, grossesse et infertilité et des suivis contextualisés. Ses accords d’experts ne remplacent pas les informations professionnelles suisses.',
'Le résumé exécutif du rapport suisse synthétise des essais montrant une baisse de TSH sans bénéfice clinique cohérent sur les autres critères. Les coûts sur cinq ans sont modélisés, non observés, et ne constituent pas une décision de remboursement.',
'Le RCOG 2025 adapte références, délais et traitement à la préconception et à la grossesse ; il distingue formes sévères, formes légères et hypothyroxinémie isolée. Il ne recommande pas l’iodurie pour déterminer le statut individuel gravidique.',
'La correction publiée en mai 2026 précise le début du suivi Doppler fœtal et corrige le sigle du carbimazole. Elle ne change pas les recommandations de prise en charge de l’HIC utilisées ici.',
'La composition de la présentation suisse Elevit Pronatal ne contient pas d’iode. Cette constatation concerne le produit exact et ne s’étend pas à toutes les spécialités ou formulations portant un nom voisin.',
'TRUST étudie 737 adultes âgés d’au moins 65 ans, avec une TSH initiale moyenne de 6,4 mU/L. La baisse biologique sous traitement ne s’accompagne pas d’un bénéfice moyen sur fatigue ou symptômes à un an.',
'La méta-analyse de 21 essais chez des adultes non enceintes ne trouve pas d’amélioration de la qualité de vie ou des symptômes soutenant une substitution de routine. Elle ne fournit pas une réponse spécifique à E02 ou à la grossesse.',
'L’essai Inde–Thaïlande de 200 µg/j en grossesse légèrement carencée ne retrouve pas de différence significative de cognition des enfants à 5–6 ans. Le contexte et les pertes de suivi limitent l’extrapolation à toute prévention iodée.',
'L’avis EFSA 2014 propose des apports adéquats par population, dont 150 µg/j adulte et 200 en grossesse/allaitement. Ces repères d’apport total ne sont pas des seuils de maladie individuelle.',
'L’analyse de six cohortes ne trouve pas de perte osseuse accrue associée à l’hypothyroïdie infraclinique, contrairement au profil hyperthyroïdien infraclinique. Une association de cohorte ne mesure pas tous les risques d’un traitement.',
'Le résumé de la revue suisse de 2014 décrit des variations de pratique dans la prise en charge de l’HIC. Il est historique et ne remplace pas les essais et recommandations plus récents.',
'La revue de 2016 distingue conséquences des déficits sévères et incertitudes des formes légères pendant la grossesse. Son état des essais est complété par le résultat randomisé publié en 2017 et le RCOG 2025.'
]
assert len(raw)==len(paraphrases)==24
sources=[];cache=[]
for s,para in zip(raw,paraphrases):
 p=Path(s['cache_external']);assert p.is_file() and sha(p)==s['sha256'],s['id']
 sources.append(dict(id=s['id'],url=s['url'],publisher=s['editeur'],version=s['version_annee'],read_at=s['date_consultation'],section=s['section_page'],passage=para,passage_kind='faithful_paraphrase',population=s['population'],limits=s['limites'],source_content_sha256=s['sha256'],read_level='Passages identifiés ; résumé seul lorsque indiqué, aucune lecture intégrale globale revendiquée'))
 cache.append(dict(source_id=s['id'],path=str(p),sha256=sha(p),bytes=p.stat().st_size,read_scope=s['section_page']))
extra=[]
for f in ['eta2013-2014-clinical-passages2.json','eta2013-clinical-passages3.json','osav-url-validation.html']:
 p=Path('/tmp/medina-source-cache/endocrinologie/E02')/f;extra.append(dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size,role='Passages complémentaires effectivement consultés (ETA ou validation du lien OSAV français)'))
save=lambda name,x:(D/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
save('source-ledger.json',dict(sources=sources,full_source_storage='Cache externe ; passages publics paraphrasés, sources intégrales non libres non republiées.',clinical_certification=False))
save('source-cache-manifest.json',dict(at=datetime.datetime.now(datetime.timezone.utc).isoformat(),sources=cache,additional_read_evidence=extra,tokens_actual=None,cost_actual=None,failed_fetches=['eta2013.blocked.html et eta2014.blocked.html : pages reCAPTCHA, exclues des sources'],unique_cache_files=len({x['path'] for x in cache+extra}),bytes_unique=sum(x['bytes'] for x in {x['path']:x for x in cache+extra}.values())))
print('24 sources paraphrasées ; empreintes et provenance du cache vérifiées.')
