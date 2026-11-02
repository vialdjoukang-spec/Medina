from pathlib import Path
import json,html
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[4]
CH=ROOT/'chapters/N05';CH.mkdir(parents=True,exist_ok=True)
SOURCES={x['id']:x for x in json.loads((OUT/'source-ledger.json').read_text())['sources']}
def ref(*ids):
 return '<p class="src">Sources lues : '+ ' ; '.join('<a data-reference-source="1" href="'+html.escape(SOURCES[i]['url'],quote=True)+'" target="_blank" rel="noopener">'+html.escape(i+' — '+SOURCES[i]['section'])+'</a>' for i in ids)+'.</p>'
def w(k,text):return '<button class="w" data-k="n05-'+k+'">'+text+'</button>'
def table(head,rows):return '<table class="t"><thead><tr>'+''.join('<th>'+x+'</th>' for x in head)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+x+'</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table>'
def sec(i,title,body,refs=(),tag='h2',extra=''):
 return '<section class="ilot" id="n05-'+str(i)+'" '+extra+'><'+tag+'>'+title+'</'+tag+'>'+body+ref(*refs)+'</section>\n'
def key(text):return '<div class="key"><b>À retenir.</b> '+text+'</div>'
def trap(text):return '<div class="trap"><b>Piège.</b> '+text+'</div>'
def save(part,text):(CH/('N05_'+part+'.html')).write_text(text+'\n')
