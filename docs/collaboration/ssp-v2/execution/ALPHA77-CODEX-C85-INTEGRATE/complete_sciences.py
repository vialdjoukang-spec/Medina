#!/usr/bin/env python3
"""Enrichissements locaux C85 : sources lues, aucune figure anatomique générée."""
from pathlib import Path
import json,re,shutil
from lxml import html

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[4]
P=ROOT/'chapters/C85/C85_c.html'
t=P.read_text()
EHA='https://pmc.ncbi.nlm.nih.gov/articles/PMC12456099/'
HIST='https://pmc.ncbi.nlm.nih.gov/articles/PMC6909622/'
CHEN='https://pmc.ncbi.nlm.nih.gov/articles/PMC8044947/'
KEY='https://amiko.oddb.org/fr/fi?gtin=7680662310025'
def cite(url,title):return f'<a href="{url}" target="_blank" rel="noopener">{title}</a>'
def add(ident,body):
 global t
 marker=ident+'-lecture-2026'
 if f'id="{marker}"' in t:return
 pat=r'(<div class="sci" id="'+re.escape(ident)+r'"[^>]*>.*?)(</section></div>)'
 t,n=re.subn(pat,lambda m:m[1]+f'<div id="{marker}">'+body+'</div>'+m[2],t,count=1,flags=re.S)
 if n!=1:raise ValueError(ident)
def keys(clin,exam,trait,retain):
 return ''.join('<div class="key"><b>'+lab+'</b> '+body+'</div>' for lab,body in [('Science → clinique.',clin),('Science → examen.',exam),('Science → traitement.',trait),('À retenir.',retain)])

ct=html.fromstring(t).get_element_by_id('c85-figure-originale-mediastin')
ct=html.tostring(ct,encoding='unicode')
semiofig=ct.replace('c85-figure-originale-mediastin','c85-semio-scanner').replace('Figure 3 —','Lecture sémiologique —')
physiofig=ct.replace('c85-figure-originale-mediastin','c85-physio-scanner').replace('Figure 3 —','Lecture physiopathologique —')
add('c85-s-semio',semiofig+keys(
 'L’œdème cervicofacial et la distension veineuse prennent sens lorsqu’on les relie au trajet cave supérieur ; les symptômes généraux décrivent une autre dimension de la maladie.',
 'L’examen repère la distribution des signes, le scanner caractérise la compression, et la biopsie identifie la nature du tissu. La figure montre une masse et un épanchement ; elle ne mesure pas leur tolérance clinique.',
 'L’évaluation des complications compressives et la qualification du lymphome sont complémentaires. Un signe ne permet pas de choisir seul un protocole.',
 'Décrire, localiser, expliquer puis confirmer : cette succession évite de confondre un syndrome compressif avec un diagnostic histologique.'))
t=t.replace('Lien avec la clinique.','Science → clinique.').replace('Lien avec les examens.','Science → examen.').replace('Lien avec le traitement.','Science → traitement.')
add('c85-s-physio',physiofig+'<p>Sur cette image pathologique, la masse antérieure et l’épanchement péricardique constituent deux constatations distinctes. Le raisonnement physiologique explique pourquoi il faut examiner leurs rapports et leur retentissement ; la photographie ne remplace ni l’examen respiratoire ni une évaluation cardiovasculaire.</p>')
add('c85-s-anat',keys(
 'Le médiastin réunit des structures vasculaires, respiratoires et digestives. La distribution des manifestations dépend des rapports de la masse avec ces structures, et non du seul nom du lymphome.',
 'Sur les coupes originales, repérer séparément la masse antérieure en A et l’épanchement péricardique en B. Ces repères répondent à une question de localisation ; ils ne démontrent pas le phénotype des cellules.',
 'L’imagerie documente l’extension et les complications à prendre en compte dans la prise en charge spécialisée. Le choix d’un schéma repose aussi sur la classification tissulaire.',
 'La localisation antérieure oriente les diagnostics possibles ; le prélèvement permet de les distinguer.'))
add('c85-s-histo',f'''<h3>Lire une architecture avant d’interpréter un marquage</h3>
<p>La planche originale permet une progression concrète. Les panneaux A et B montrent d’abord la disposition du tissu : une fibrose réticulaire ou des agrégats séparés par des cloisons. Les panneaux C à F répondent ensuite à des questions de phénotype. Un marquage positif ne décrit pas, à lui seul, la manière dont les cellules s’organisent dans le prélèvement.</p>
<p>Dans la série de Kim et collaborateurs, les fibroses alvéolaire et compartimentante favorisent le diagnostic de lymphome médiastinal primitif. Les auteurs soulignent toutefois la difficulté à reconnaître cette architecture sur un petit fragment. Leur étude compare une série limitée de lymphomes médiastinaux et de Hodgkin classiques ; ses performances ne doivent pas devenir une règle universelle applicable à toute masse thoracique.</p>
<p>Le pathologiste confronte donc les caractères morphologiques, un ensemble de marqueurs et les données cliniques. L’expertise spécialisée demandée par les recommandations européennes explique cette intégration. Si le compte rendu reste non spécifique ou discordant, une photographie illustrative ne permet pas de contourner la réévaluation du prélèvement.</p>
<p class="src">{cite(HIST,'Kim et al. 2019, résultats histopathologiques, discussion et figure 2')} ; {cite(EHA,'EHA 2025, diagnostic anatomopathologique')}.</p>'''+keys(
 'Deux masses de localisation comparable peuvent correspondre à des entités différentes. L’apparence clinique ne suffit pas à les séparer.',
 'L’architecture et les immunomarquages s’interprètent ensemble sur un prélèvement adapté ; les panneaux de la figure montrent ces deux niveaux de lecture.',
 'Une qualification précise évite d’appliquer à un lymphome non classé le traitement d’une entité simplement supposée.',
 'Reconnaître une fibrose ou un marquage est une étape du raisonnement ; le diagnostic reste une synthèse spécialisée.'))
add('c85-s-immuno',f'''<h3>Du signal immunitaire normal à sa perturbation tumorale</h3>
<p>La présentation d’antigènes et les signaux inhibiteurs sont deux composantes différentes de la réponse immunitaire. Les molécules de présentation rendent des antigènes accessibles à la reconnaissance lymphocytaire. La voie PD-1 module l’activité des lymphocytes T lorsque ses ligands sont présents. La tumeur peut donc modifier à la fois ce qui est reconnu et l’intensité de la réponse.</p>
<p>La revue de Chen décrit des altérations touchant notamment B2M, CIITA et les ligands de PD-1. B2M code la bêta-2-microglobuline, nécessaire à l’expression des molécules du complexe majeur d’histocompatibilité de classe I. Il faut la distinguer des mécanismes qui concernent la classe II : résumer toutes ces anomalies par « perte de HLA II » ferait disparaître cette différence.</p>
<p>Le schéma causal ci-dessus simplifie ces mécanismes pour les rendre lisibles ; il ne représente pas une coupe anatomique. Son intérêt est de distinguer une présentation antigénique réduite d’un signal inhibiteur accru. Aucun de ces mécanismes ne garantit une réponse individuelle au traitement. L’indication clinique et les précautions restent celles de la préparation suisse et de la situation du patient.</p>
<p class="src">{cite(CHEN,'Chen et al. 2021, Genetic Features')} ; {cite(KEY,'FI suisse Keytruda, mécanisme d’action et lymphome médiastinal')}.</p>'''+keys(
 'L’échappement immunitaire aide à comprendre la persistance tumorale ; il ne fournit pas un signe clinique spécifique ni une prédiction individuelle de réponse.',
 'L’étude du tissu définit le lymphome. Une altération moléculaire ne remplace pas cette synthèse et ne constitue pas automatiquement un test compagnon exigé pour chaque traitement.',
 'Le pembrolizumab bloque PD-1. Son usage dans le lymphome médiastinal suit les conditions suisses de lignes antérieures et exclut la situation nécessitant une réduction tumorale urgente.',
 'Le mécanisme explique une cible ; l’indication autorisée et le contexte clinique déterminent son utilisation.'))
add('c85-s-gen',f'''<h3>Une carte de mécanismes, pas une succession obligatoire</h3>
<p>Une amplification augmente le nombre de copies d’une région génomique ; un réarrangement en modifie l’organisation. Ces mots décrivent des événements différents. Dans la revue de Chen, l’amplification de la région 9p24.1 concerne notamment JAK2 et les ligands de PD-1. Elle relie donc un même territoire chromosomique à la signalisation intracellulaire et aux interactions immunitaires.</p>
<p>Les voies NF-κB et JAK-STAT participent aux programmes cellulaires décrits dans cette revue. Leur activation anormale et les mécanismes d’échappement immunitaire peuvent coexister. Les trois colonnes du schéma ne doivent pas être lues comme trois étapes que chaque patient franchirait dans le même ordre. Les anomalies proviennent de séries et d’analyses différentes ; toutes ne sont pas présentes dans chaque tumeur.</p>
<p>La parenté moléculaire avec le lymphome de Hodgkin explique une partie des difficultés de classification, sans rendre les deux diagnostics interchangeables. L’analyse génétique complète la morphologie et le phénotype. Elle peut aussi éclairer une stratégie thérapeutique, mais une association biologique ou pronostique n’équivaut pas à une indication suisse ni à un bénéfice individuel démontré.</p>
<p class="src">{cite(CHEN,'Chen et al. 2021, Genetic Features')} ; {cite(EHA,'EHA 2025, diagnostic spécialisé')}.</p>'''+keys(
 'Des mécanismes partagés peuvent s’observer dans des entités cliniques distinctes. Ils n’effacent pas leurs différences de présentation et de prise en charge.',
 'Les résultats moléculaires se confrontent au prélèvement et au phénotype. Le tableau constitue une carte pédagogique et non une liste de critères tous obligatoires.',
 'Une voie altérée peut fournir une cible de recherche ou de traitement ; son emploi clinique exige des données et des conditions d’utilisation propres au médicament.',
 'Ne pas confondre anomalie observée, mécanisme plausible, association pronostique et indication thérapeutique.'))
for ident in ['c85-s-histo','c85-s-immuno','c85-s-gen']:
 t=t.replace(f'<div class="sci" id="{ident}">',f'<div class="sci" id="{ident}" hidden>')
P.write_text(t)

# Apply the source correction to every affected local surface.
for p in (ROOT/'chapters/C85').glob('*.html'):
 t=p.read_text()
 t=t.replace('Avec le rituximab seul, la survie globale est de 91 % contre 86 % (p = 0,03).','Dans l’analyse limitée aux schémas contenant du rituximab, la survie globale est de 91 % avec les schémas intensifiés contre 86 % avec R-CHOP-21 (p = 0,03). Il s’agit d’associations de traitements, et non de rituximab en monothérapie.')
 t=t.replace('Première ligne : R-CHOP ou DA-EPOCH-R, choix selon le centre.','Première ligne du lymphome médiastinal : les recommandations EHA 2025 privilégient R-CHOP14 ou un schéma intensifié tel que DA-EPOCH-R, en évitant R-CHOP21.')
 t=t.replace('Première ligne du lymphome médiastinal : R-CHOP ou DA-EPOCH-R, au choix du centre ;','Première ligne du lymphome médiastinal : R-CHOP14 ou un schéma intensifié tel que DA-EPOCH-R selon EHA 2025 ; éviter R-CHOP21 ;')
 t=t.replace('L’objectif est la guérison. Le schéma optimal n’est pas établi : le R-CHOP et le','L’objectif est la guérison. Onkopedia décrit les options R-CHOP et')
 t=t.replace('https://amiko.oddb.org" target="_blank" rel="noopener">Polivy®','https://amiko.oddb.org/fr/fi?gtin=7680671650020" target="_blank" rel="noopener">Polivy®')
 p.write_text(t)

# The retrieved normal-anatomy image has a restrictive current licence: no reuse.
candidate=ROOT/'assets/img/c85/alpha/codex/openstax-20-36-veines-original.webp'
if candidate.exists():shutil.move(str(candidate),'/workspace/medina-source-cache/C85/openstax-rejected-NC.webp')
p=OUT/'normal-provenance.json'
if p.exists():
 v=json.loads(p.read_text());v.update(status='rejected_not_in_lesson',reason='Page actuelle CC BY-NC-SA 4.0 : clause NC incompatible avec IMAGE_CODEX_FINDER. Texte factuel paraphrasé et cité ; figure non réutilisée.')
 p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
print('C85 : six sciences enrichies, lectures visuelles explicites, correction rituximab et figure NC exclue.')
