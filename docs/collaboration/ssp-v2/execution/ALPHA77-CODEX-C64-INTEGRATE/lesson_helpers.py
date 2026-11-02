from pathlib import Path
import json,html
OUT=Path(__file__).resolve().parent; ROOT=OUT.parents[4];CH=ROOT/'chapters/C64';CH.mkdir(parents=True,exist_ok=True)
SOURCES={x['id']:x for x in json.loads((OUT/'source-ledger.json').read_text())['sources']}
def ref(*ids):
 return '<p class="src">Sources lues : '+' ; '.join('<a data-reference-source="1" href="'+html.escape(SOURCES[i]['url'],quote=True)+'" target="_blank" rel="noopener">'+html.escape(SOURCES[i]['publisher']+' — '+SOURCES[i]['section'])+'</a>' for i in ids)+'.</p>'
def w(k,t):return '<button class="w" data-k="c64-'+k+'">'+t+'</button>'
def table(head,rows):return '<table class="t"><thead><tr>'+''.join('<th>'+x+'</th>' for x in head)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+x+'</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table>'
def sec(i,t,b,refs=(),tag='h2',extra=''):return '<section class="ilot" id="c64-'+str(i)+'" '+extra+'><'+tag+'>'+t+'</'+tag+'>'+b+ref(*refs)+'</section>\n'
def key(t):return '<div class="key"><b>À retenir.</b> '+t+'</div>'
def trap(t):return '<div class="trap"><b>Piège.</b> '+t+'</div>'
def save(part,t):(CH/('C64_'+part+'.html')).write_text(t+'\n')
