"""Corrections de sécurité propagées aux fenêtres, puis typographie des seuls nœuds texte."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[5]
fix={
'La deuxième intention est la pénicilline procaïne 600 000 unités par jour pendant 17 à 21 jours, si la benzathine pénicilline n’est pas disponible.':'L’IUSTI 2020 cite une alternative par pénicilline procaïne, détaillée comme historique dans la fenêtre ; aucun produit suisse correspondant n’a été vérifié ici. La HAS 2025 propose la doxycycline pendant 28 jours en cas d’indisponibilité, hors grossesse et atteinte neurologique, oculaire ou otique.',
'Elle se prévient par la prednisolone 20 à 60 mg/jour pendant 3 jours, en commençant 24 heures avant l’antibiotique, en cas d’atteinte cardiovasculaire ou neurologique.':'En cas d’atteinte cardiovasculaire ou neurologique, une prophylaxie par prednisolone peut être discutée par l’équipe spécialisée : la HAS 2025 cite 20 à 60 mg/jour pendant 3 jours, débutés 24 heures avant l’antibiotique, sur avis d’experts et avec un faible niveau de preuve. Cette mesure n’est ni systématique ni une garantie de prévention ; ces atteintes nécessitent une surveillance hospitalière.',
'Prednisolone préventive si atteinte cardiovasculaire ou neurologique':'Prednisolone à discuter dans certaines formes à risque ; preuve limitée, avis spécialisé',
'Utilisée avant l’antibiotique en cas d’atteinte cardiovasculaire ou neurologique':'À discuter avant l’antibiotique dans les formes cardiovasculaires ou neurologiques à risque ; non systématique',
'prévenir Jarisch-Herxheimer si atteinte cardiovasculaire ou neurologique':'discuter la prévention de Jarisch–Herxheimer et la surveillance hospitalière dans les formes cardiovasculaires ou neurologiques',
'Pas de réduction de dose si la clairance est supérieure à 75 mL/min (25 mg/kg) ;':'La FI distingue attaque jusqu’à 25 mg/kg/j et stabilisation à 15 mg/kg/j ; le guide suisse 2024 indique 15 (15–20) mg/kg/j chez l’adulte. Son tableau rénal indique 25 mg/kg si la clairance est supérieure à 75 mL/min, sans en faire une dose universelle ;',
'avant le traitement, puis toutes les 4 semaines.':'avant le traitement, puis toutes les 4 semaines ; chaque semaine en cas d’insuffisance rénale selon la FI. Toute baisse visuelle exige une évaluation immédiate.',
'avant puis toutes les 4 semaines sous éthambutol':'avant puis toutes les 4 semaines sous éthambutol, chaque semaine si insuffisance rénale',
'Cystine leucocytaire inférieure à 1 nmol d’hémicystine/mg de protéine, 30 minutes après la prise.':'Pour Procysbi® et une préparation de leucocytes mixtes : cystine inférieure à 1 nmol d’hémicystine/mg de protéine, 30 minutes après la dose matinale, soit 12,5 heures après celle du soir. La cible et l’horaire doivent correspondre à la méthode du laboratoire et à la formulation.',
'Cystine leucocytaire inférieure à 1 nmol d’hémicystine/mg de protéine, 30 minutes après la prise de cystéamine.':'Avec Procysbi® : cible sur leucocytes mixtes inférieure à 1 nmol d’hémicystine/mg de protéine, 30 minutes après la prise matinale, soit 12,5 heures après celle du soir ; ne pas transposer ce protocole à une autre préparation cellulaire ou formulation.',
'La dose est ajustée sur la cystine leucocytaire mesurée 30 minutes après la prise,':'La dose de Procysbi® est ajustée sur la cystine des leucocytes mixtes, mesurée 30 minutes après la prise matinale (12,5 heures après celle du soir),',
'La cible est une cystine leucocytaire inférieure à':'Pour Procysbi® et une mesure sur leucocytes mixtes, la cible est une cystine inférieure à',
'30 minutes après la prise. Le Cystadrops®':'30 minutes après la prise matinale, soit 12,5 heures après celle du soir. Le Cystadrops®',
'Cystine leucocytaire 30 minutes après la prise de cystéamine,':'Cystine des leucocytes mixtes 30 minutes après la dose matinale de Procysbi® (12,5 heures après celle du soir),',
'avec une cible thérapeutique inférieure à 1 nmol d’hémicystine/mg de protéine.':'avec, pour les leucocytes mixtes et selon la FI Procysbi®, une cible thérapeutique inférieure à 1 nmol d’hémicystine/mg de protéine ; prélèvement 30 minutes après la dose matinale. Les autres méthodes nécessitent leur cible propre.',
'Contre-indiqué si clairance < 50 mL/min ; 1000 mg/jour d’entretien en insuffisance rénale et dose usuelle après hémodialyse':'FI : contre-indiqué si clairance < 50 mL/min. La mention séparée de 1 g/j d’entretien en insuffisance rénale et d’une prise après dialyse ne lève pas cette contre-indication ; divergence à résoudre avec l’équipe spécialisée',
'Contre-indiqué si la clairance est inférieure à 50 mL/min. 1000 mg/jour d’entretien en insuffisance rénale ; dose usuelle après hémodialyse.':'La FI contre-indique une clairance inférieure à 50 mL/min, mais mentionne séparément 1000 mg/jour d’entretien en insuffisance rénale et la dose usuelle après hémodialyse. Ces mentions ne constituent pas une autorisation de traiter sous 50 mL/min : l’écart interne à la FI et la divergence avec le guide exigent un avis spécialisé documenté.',
'Pour la syphilis tardive, hors neurosyphilis : 2,4 millions d’unités une fois par semaine pendant 3 semaines.':'Pour la syphilis tardive de l’adulte : 2,4 millions d’unités par voie intramusculaire profonde une fois par semaine pendant 3 semaines. Jamais par voie intraveineuse. Les atteintes neurologiques, oculaires et otiques requièrent un autre traitement spécialisé.',
'œufs urinaires (11,5 % de positivité en Europe), sérologie sensible mais non discriminante':'œufs urinaires positifs chez 96/831 cas testés dans la cohorte de Barcelone, sérologie positive chez 763/772 ; ces proportions sélectionnées ne sont pas des sensibilités et la sérologie ne prouve pas l’activité',
'Tuberculose : surveillance jusqu’à 10 ans ; cystinose : cystéamine à vie.':'Tuberculose : suivi infectieux et urologique individualisé ; les séries proposant jusqu’à dix ans ne fixent pas une norme suisse universelle. Cystinose : cystéamine à poursuivre même après greffe.',
'grossesse (praziquantel sûr)':'grossesse (praziquantel si cliniquement justifié selon le produit et le contexte)',
'Indométacine</b> dans la cystinose : sans consensus, à éviter avec les inhibiteurs de l’enzyme de conversion.':'Indométacine</b> dans la cystinose : les recommandations 2026 envisagent son emploi spécialisé chez certains jeunes enfants dont le Fanconi reste difficile à contrôler. Arrêt lorsque les pertes sont maîtrisées ou la fonction rénale baisse ; ne pas associer à un inhibiteur de l’enzyme de conversion ou un antagoniste de l’angiotensine II. Ce n’est pas un traitement de routine de l’enfant plus âgé atteint de maladie rénale chronique.',
'Praziquantel</b> : pas d’information professionnelle suisse ; ne pas présenter le schéma de l’Organisation mondiale de la santé comme une recommandation suisse.':'Praziquantel</b> : aucune FI suisse identifiée dans la recherche effectuée, sans conclusion sur la possibilité d’accès. La revue suisse RMS 2018 et le RCP français Biltricide® documentent le traitement ; confirmer le produit disponible avec la pharmacie.',
'praziquantel sans information professionnelle suisse':'praziquantel : référence clinique suisse et RCP français identifiés, produit disponible à confirmer avec la pharmacie',
'la tuberculose suisse 2025 compte 544 cas':'la surveillance Suisse et Liechtenstein 2025 compte 544 cas',
'ajoutés dans le HTML':'superposés à l’image',
'ajoutés dans le superposés':'superposés à l’image',
'signalisationmTOR':'signalisation mTOR','suisseProcysbi':'suisse Procysbi','chapitreEAU':'chapitre EAU','testPCR':'test PCR',
}
for p in (ROOT/'chapters/N29').glob('*.html'):
 t=p.read_text()
 for a,b in fix.items():t=t.replace(a,b)
 # Product links in each popup point to the actual product, not the search homepage.
 for slug,gtin in {'rifater':'7680470630353','myambutol':'7680331530013','pyrazinamide':'7680576990023','extencilline':'7680697650011','procysbi':'7680671290011','cystadrops':'7680673800010','calcul-tb':'7680470630353','calcul-procysbi':'7680671290011'}.items():
  pattern=rf'(<template data-pop="n29-{slug}".*?</template>)'
  t=re.sub(pattern,lambda m:m[0].replace('https://amiko.oddb.org"',f'https://amiko.oddb.org/fr/fi?gtin={gtin}"'),t,flags=re.S)
 # Fix text only; leave tags, paths, identifiers, CSS and mathematical codes intact.
 protected={}
 def protect(m):
  key='__MEDINA_PROTECTED_'+str(len(protected))+'__';protected[key]=m[0];return key
 t=re.sub(r'<(?:style|script)\b[^>]*>.*?</(?:style|script)>',protect,t,flags=re.S)
 parts=re.split(r'(<[^>]+>)',t)
 for i in range(0,len(parts),2):
  s=parts[i]
  s=re.sub(r'(?<=[a-zà-ÿ])(?=\d)', ' ',s)
  s=re.sub(r'(?<=\d)(?=(?:mg|g/m|mL|ml|nmol|min|jours|semaines|mois|ans|cas|fois|h\b|UI\b))',' ',s)
  s=re.sub(r'(?<=\d)%',' %',s)
  s=re.sub(r'\b(RMS|HAS|IUSTI|PHIL|BY)(?=\d)',r'\1 ',s)
  s=s.replace('XpertMTB','Xpert MTB').replace('OpenStax2013','OpenStax 2013').replace('600000','600 000')
  s=re.sub(r'(?<=[,;])(?=[A-Za-zÀ-ÿ])',' ',s)
  s=re.sub(r'(?<=\d), +(?=\d)', ',',s)
  parts[i]=s
 t=''.join(parts)
 for key,value in protected.items():t=t.replace(key,value)
 p.write_text(t)
# Focused popup safety additions (idempotent).
p=ROOT/'chapters/N29/N29_pop2.html';t=p.read_text()
if 'n29-rifater-safety' not in t:
 t=t.replace('<div class="lab">Effet indésirable</div>', '<div class="lab" id="n29-rifater-safety">Sécurité du produit fixe</div><p>Rifater® ne contient pas d’éthambutol. La FI contre-indique une clairance inférieure à 30 mL/min et plusieurs situations hépatiques ou associations médicamenteuses. Ne pas adapter une insuffisance rénale en espaçant indistinctement le comprimé combiné ; envisager les composants séparés avec l’équipe spécialisée.</p><div class="lab">Effet indésirable</div>',1)
p.write_text(t)
print('Six surfaces : corrections médicales et typographiques propagées.')
