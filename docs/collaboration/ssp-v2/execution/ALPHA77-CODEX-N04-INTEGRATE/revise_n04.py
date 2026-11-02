"""Reproducible bounded N04 revision, starting from the exact worktree base."""
from pathlib import Path
import subprocess, json, re, html

ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parent
BASE = '8a512893acbab9caa0dcfdd0e8682a44ea72fda6'
rights = json.loads((OUT/'figures-rights.json').read_text())['figures']

def original(part):
    return subprocess.check_output(['git','show',f'{BASE}:chapters/N04/N04_{part}.html'],cwd=ROOT,text=True)

def figure(index, number, caption, points, maxwidth='100%'):
    f=rights[index]
    markers=''.join(f'<span data-n04-annotation="{index}-{n}" aria-hidden="true">{n}</span>' for n,x,y,text in points)
    css='[data-n04-original] [data-n04-image]{position:relative;margin:auto}[data-n04-original] img{display:block;width:100%;height:auto}[data-n04-annotation]{position:absolute;transform:translate(-50%,-50%);background:#163c59;color:white;border:2px solid white;border-radius:50%;width:1.8em;height:1.8em;display:flex;align-items:center;justify-content:center;font:bold 16px sans-serif;box-shadow:0 0 0 1px #163c59}'
    css+=f'[data-n04-original="{index}"] [data-n04-image]{{max-width:{maxwidth}}}'
    css+=''.join(f'[data-n04-annotation="{index}-{n}"]{{left:{x}%;top:{y}%}}' for n,x,y,text in points)
    annotations=' '.join(f'<b>{n}.</b> {html.escape(text)}' for n,x,y,text in points)
    title=html.escape(caption,quote=True)
    return f'''<style>{css}</style><figure data-n04-original="{index}"><div data-n04-image="1"><img src="{f['path']}" alt="{title}" loading="lazy">{markers}</div><figcaption>Figure {number} — {html.escape(caption)} {annotations} <a href="{f['source_url']}" target="_blank" rel="noopener">Original : {f['author']}</a>, <a href="{f['license_url']}" target="_blank" rel="noopener">{f['license']}</a>. Repères numérotés superposés par MEDINA, sous la même licence ; pixels de l’original inchangés. Les repères commentent l’image et ne constituent pas une validation diagnostique indépendante.</figcaption></figure>'''

podocyte=figure(0,1,'Podocytes normaux : dessin anatomique humain OpenStax College (2013), avant toute comparaison avec une lésion.',[(1,24,50,'Pédicelles interdigités : les prolongements de podocytes voisins délimitent les fentes.'),(2,83,48,'Corps d’un podocyte appliqué contre le capillaire ; l’image représente une organisation normale.')])
lipid=figure(4,4,'Corps gras ovalaire dans un sédiment urinaire, microscopie optique.',[(1,49,46,'Cellule arrondie contenant de nombreuses gouttelettes réfringentes ; aspect compatible avec une lipidurie.')], '850px')
lipid=lipid.replace('pixels de l’original inchangés.','pixels de l’original inchangés. La lumière polarisée n’est pas montrée : aucune croix de Malte ne peut être affirmée sur cette image. La lipidurie ne détermine pas à elle seule la cause de la protéinurie.')
fsgs=figure(2,6,'Hyalinose segmentaire et focale, variante hilaire, coloration PAS : photographie histologique humaine.',[(1,70,50,'Segment dense du floculus, à confronter aux anses encore ouvertes.'),(2,44,48,'Autres anses du même glomérule : le contraste illustre le caractère segmentaire.')], '950px')
fsgs=fsgs.replace('pixels de l’original inchangés.','pixels de l’original inchangés. Une seule coupe ne démontre pas le caractère focal dans l’ensemble des glomérules de la biopsie.')
membrane=figure(3,7,'Néphropathie membraneuse, coloration argentique : photographie histologique humaine.',[(1,65,40,'Parois capillaires glomérulaires soulignées par l’argentation.'),(2,20,35,'Structures tubulaires autour du floculus, à distinguer des anses capillaires.')], '950px')
membrane=membrane.replace('pixels de l’original inchangés.','pixels de l’original inchangés. L’identification fine de spicules exige le grossissement adéquat ; les dépôts sous-épithéliaux ne sont pas montrés en microscopie électronique ici.')
nephron=figure(1,8,'Néphron normal et échanges tubulaires : dessin anatomique humain OpenStax College (2013).',[(1,35,30,'Région proximale : réabsorption majeure de solutés et d’eau.'),(2,53,65,'Branche ascendante de l’anse ; distinguer son trajet de la branche descendante.'),(3,78,70,'Canal collecteur : ajustement final des échanges, selon le contexte hormonal.')], '650px')
nephron=nephron.replace('pixels de l’original inchangés.','pixels de l’original inchangés. Les noms et les doses des diurétiques ne proviennent pas de cette illustration : le texte du cours expose séparément leurs sites d’action et les informations professionnelles suisses.')

def replace_figures(s, replacements):
    def sub(m):
        n=re.search(r'Figure (\d+)\s*[—–-]',m.group())
        return replacements.get(int(n[1]),m.group()) if n else m.group()
    return re.sub(r'<figure\b[^>]*>.*?</figure>',sub,s,flags=re.S)

a=original('a')
a=a.replace('Sources relues le 14 octobre 2026 · Statut : audit différé après le Cycle 30 ; revue par intelligence artificielle, sans validation médicale humaine','Révision ciblée du 2 novembre 2026 · Statut : aperçu provisoire en revue ; relecture médicale indépendante requise, sans validation médicale humaine')
a=a.replace('<section class="ilot" id="n04-a06"><h2>', '<section class="ilot" id="n04-a06"><h2 data-semiology-clinical="N04">')
assert 'correspond davantage à une néphropathie membraneuse' in a
a=a.replace('correspond davantage à une néphropathie membraneuse qu’à une forme minime, sans que cela suffise à trancher.','est compatible avec plusieurs glomérulopathies, dont une néphropathie membraneuse et des lésions glomérulaires minimes. Ces seuls signes ne permettent pas de privilégier une histologie ; les examens étiologiques et, selon le contexte, la biopsie déterminent la suite.')
a=replace_figures(a,{1:podocyte,2:''})

b=original('b').replace('l’hypothèse du « rein-éponge »','l’hypothèse de captation rénale précoce des anticorps (« rein puits »)')
pop1=original('pop1').replace('L’hypothèse du « rein-éponge »','Captation rénale précoce des anticorps (« rein puits »)').replace('le rein fonctionne comme une éponge.','les anticorps seraient initialement captés par leurs antigènes rénaux (hypothèse dite « kidney as a sink » ou « rein puits »). Cette expression ne désigne pas le rein médullaire en éponge, qui est une autre affection.')

c=original('c')
semio=(OUT/'semio.html').read_text()
semio=semio.replace('<!-- N04_SEMIO_FIGURE -->',podocyte.replace('Figure 1 —','Figure S00 —'))
sources=json.loads((OUT/'passages-lus.json').read_text())['passages']
links=''.join(f'<li><b>{s["id"]}.</b> <a data-reference-source="1" href="{s["url"]}" target="_blank" rel="noopener">{html.escape(s["titre"])}</a> — {html.escape(s["section_page"])}. Population : {html.escape(s["population"])}. Limite : {html.escape(s["limites"])}</li>' for s in sources)
semio=semio.replace('<!-- N04_SEMIO_SOURCES -->','<ol>'+links+'</ol>')
semio=re.sub(r'(?<![a-zA-Z0-9])S(10|[1-9])(?![a-zA-Z0-9])', r'réf. \1', semio)
semio=semio.replace('p.S90–S91','pages 90–91 du supplément').replace('PP1.2.1–1.2.2','points de pratique 1.2.1–1.2.2').replace('p.S256','page 256 du supplément').replace('Volume status : In case of hypovolemia or AKI','Évaluation de la volémie : hypovolémie ou insuffisance rénale aiguë')
button='<button id="n04-tab-semio" role="tab" data-s="n04-s-semio" aria-controls="n04-s-semio" aria-selected="true">Sémiologie fondamentale et analytique</button>'
c=c.replace('<div class="sci-bar ui" role="tablist">','<div class="sci-bar ui" role="tablist">'+button)
c=c.replace('data-s="n04-s01-sci" aria-controls="n04-s01-sci" aria-selected="true"','data-s="n04-s01-sci" aria-controls="n04-s01-sci" aria-selected="false"')
c=c.replace('<div class="sci" id="n04-s01-sci">',semio+'<div class="sci" id="n04-s01-sci" hidden>')
c=replace_figures(c,{4:lipid,5:podocyte.replace('Figure 1 —','Figure 5 —'),6:fsgs,7:membrane,8:nephron})

callouts={
1: ('Une perte de protéines peut précéder une chute du débit de filtration : une créatinine normale ne suffit pas à exclure une lésion glomérulaire.','Confronter protéinurie, albuminémie et sédiment ; la photographie de podocytes normaux ne montre pas la lésion d’un patient.','Préserver la fonction rénale et limiter la perte de protéines dépend de la cause ; la barrière décrite ici ne désigne pas à elle seule un immunosuppresseur.'),
2: ('« Segmentaire » décrit une partie d’un glomérule et « focal » une partie des glomérules ; une seule microphotographie ne prouve pas les deux dimensions.','La microscopie optique, l’immunofluorescence et la microscopie électronique répondent à des questions complémentaires ; un aspect optique peu modifié n’exclut pas une podocytopathie.','Distinguer une hyalinose primitive, secondaire ou génétique conditionne l’indication d’immunosuppression : le nom histologique seul ne suffit pas.'),
3: ('Un œdème important peut coexister avec un volume circulant efficace diminué ; sa taille ne mesure pas la tolérance à une déplétion.','Suivre poids, diurèse, pression artérielle, créatinine et électrolytes ; interpréter leur évolution conjointement.','Les sites tubulaires différents expliquent les associations de diurétiques, mais aussi le risque de déplétion et de troubles électrolytiques. Les doses relèvent des informations professionnelles et du contexte clinique.'),
4: ('Le risque de thrombose résulte de plusieurs modifications de l’hémostase ; une hypoalbuminémie ne constitue pas, isolément, une ordonnance d’anticoagulation.','Les anti-PLA2R s’interprètent avec leur méthode, le contexte et la fonction rénale ; une négativité ne suffit pas à exclure une néphropathie membraneuse.','La prophylaxie anticoagulante confronte risque thrombotique et risque hémorragique ; les changements d’albuminémie peuvent modifier la pharmacocinétique et imposent une surveillance adaptée.')}
for n, texts in callouts.items():
    marker=f'<section class="ilot" id="n04-s0{n}">'
    assert marker in c
    start=c.index(marker);end=c.index('</section>',start)
    extra=''.join(f'<div class="key"><b>{label}</b> {text}</div>' for label,text in zip(['Science → clinique.','Science → examen.','Science → traitement.'],texts))
    if n==4:
        extra=membrane.replace('Figure 7 —','Figure S04 —')+'<p>Cette photographie optique situe le compartiment glomérulaire concerné ; elle ne montre ni un anticorps ni un dépôt sous-épithélial à l’échelle électronique. Elle accompagne la distinction entre aspect morphologique et mécanisme immunologique.</p>'+extra
    c=c[:end]+extra+c[end:]
# Separate metabolism/coagulation from immunology/genetics into two substantive units.
immuno_start=c.index('<h3 id="n04-s04-partie-3">')
immuno_end=c.index('<div class="key">',immuno_start)
inherited=c[immuno_start:immuno_end]
c=c[:immuno_start]+c[immuno_end:]
c=c.replace('Biochimie, immunologie et génétique','Biochimie et coagulation')
immuno=(OUT/'immunogenetique.html').read_text().replace('<!-- N04_IMMUNO_INHERITED -->',inherited).replace('<!-- N04_IMMUNO_FIGURE -->',membrane.replace('Figure 7 —','Figure S05 —'))
button='<button id="n04-tab-immunogenetique" role="tab" data-s="n04-s05-sci" aria-controls="n04-s05-sci" aria-selected="false">Immunologie et génétique</button>'
c=c.replace('Biochimie et coagulation</button>','Biochimie et coagulation</button>'+button)
end=c.index('</section>',c.index('<section class="ilot" id="n04-s04">'))+len('</section></div>')
c=c[:end]+immuno+c[end:]
# Keep the biochemical illustration in the biochemical panel.
start=c.index('<section class="ilot" id="n04-s04">');end=c.index('</section>',start)
unit=c[start:end];unit=re.sub(r'<figure\b[^>]*>.*?</figure>',lambda m:lipid.replace('Figure 4 —','Figure S04 —') if 'Figure S04' in m.group() else m.group(),unit,flags=re.S)
unit=unit.replace('Cette photographie optique situe le compartiment glomérulaire concerné ; elle ne montre ni un anticorps ni un dépôt sous-épithélial à l’échelle électronique. Elle accompagne la distinction entre aspect morphologique et mécanisme immunologique.','Cette photographie montre la traduction urinaire possible de l’accumulation lipidique ; elle ne quantifie pas les lipides plasmatiques et ne détermine pas la cause de la glomérulopathie.')
c=c[:start]+unit+c[end:]
for part,content in [('a',a),('b',b),('c',c),('pop1',pop1)]:
    (ROOT/f'chapters/N04/N04_{part}.html').write_text(content)
print('N04: four canonical fragments revised; inherited sections preserved; five original image files used.')

subprocess.run(["python3",str(OUT/"clinical_corrections.py")],cwd=ROOT,check=True)
