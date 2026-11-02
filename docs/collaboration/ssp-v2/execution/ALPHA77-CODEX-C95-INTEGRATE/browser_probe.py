"""Parcours du vrai moteur Medina, HTTP intercepté, sans réseau ni déploiement."""
from pathlib import Path
import json
from playwright.sync_api import sync_playwright
OUT=Path(__file__).resolve().parent;NATIVE=OUT/'C95-apercu-autonome.html';CAP=OUT/'captures';CAP.mkdir(exist_ok=True)
report={'mode':'Native HTML autonome sur origine HTTP interceptée ; autres requêtes interrompues ; file:// non testé car interdit','errors':[],'viewports':[]}
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 for width,height in [(1440,900),(390,844)]:
  page=browser.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
  page.on('pageerror',lambda e:report['errors'].append(str(e)))
  page.route('**/*',lambda r:r.fulfill(body=NATIVE.read_bytes(),content_type='text/html') if r.request.url=='http://medina.local/native.html' else r.abort())
  page.goto('http://medina.local/native.html',wait_until='domcontentloaded');page.evaluate("location.hash='#/entry/C95'");page.wait_for_timeout(1000)
  assert page.locator('.mc').count()==1
  item={'width':width,'screenshots':[],'originals_checked':[],'windows_checked':[],'quiz_checked':[],'causal_diagrams_checked':[]}
  def capture(name,element=None):
   path=CAP/f'C95-{width}-{name}.png'
   (element or page).screenshot(path=str(path));item['screenshots'].append(str(path.relative_to(OUT)))
  def panel(name):page.locator(f'.mc-tabs button[data-p="{name}"]').click()
  panel('pS');item['science_buttons']=page.locator('.mc-sci-bar button').all_text_contents();assert len(item['science_buttons'])==6
  assert page.locator('#c95-s-semio').is_visible();item['semio_sections']=page.locator('[data-semiology]').count();assert item['semio_sections']==9;capture('semio')
  for main,tab,ident in [('pA',None,'c95-figure-moelle-clinique'),('pA',None,'c95-figure-diagnostic-mpal'),('pA',None,'c95-figure-mpo-faible'),('pS','semio','c95-figure-semio-moelle'),('pS','anat','c95-figure-moelle-science'),('pS','histo','c95-figure-mpal-science'),('pS','histo','c95-figure-lai-science')]:
   panel(main)
   if tab:page.locator(f'[data-s="c95-s-{tab}"]').click()
   fig=page.locator('#'+ident);img=fig.locator('img');img.scroll_into_view_if_needed();img.evaluate('(i)=>i.decode()')
   state=img.evaluate('(i)=>({width:i.naturalWidth,height:i.naturalHeight,loaded:i.complete&&i.naturalWidth>0,embedded:i.src.startsWith("data:")})');state['figure']=ident
   assert state['loaded'] and state['embedded'];item['originals_checked'].append(state);capture(ident,fig);fig.locator('figcaption').scroll_into_view_if_needed();capture(ident+'-legende',fig.locator('figcaption'))
  for main,tab,ident in [('pA',None,'c95-arbre-final'),('pS','physio','c95-physio-causal'),('pS','bio','c95-bio-causal'),('pS','gen','c95-gen-causal')]:
   panel(main)
   if tab:page.locator(f'[data-s="c95-s-{tab}"]').click()
   fig=page.locator('#'+ident);fig.scroll_into_view_if_needed();assert fig.locator('svg[role="img"]').is_visible()
   capture(ident,fig);item['causal_diagrams_checked'].append(ident)
  item['unsafe_shared_abbreviations']=page.locator('.mc [data-ab="IA"],.mc [data-ab="ICC"],.mc [data-ab="MPO"],.mc [data-ab="CD3"],.mc [data-ab="CD79a"],.mc [data-ab="G6PD"]').count();assert item['unsafe_shared_abbreviations']==0
  panel('pA');page.locator('[data-k="c95-profiles"]').filter(visible=True).first.click()
  text=page.locator('.mc-dlg-b').inner_text().replace('\u00ad','');item['profiles_scoped']='PROFILES' in text and 'SSP 2' in text and '60 à 89' not in text;assert item['profiles_scoped'];page.keyboard.press('Escape')
  page.locator('#c95-reference-index summary').click();keys=page.locator('#c95-reference-index [data-k]').evaluate_all('(xs)=>xs.map(x=>x.dataset.k)');assert len(keys)==52
  for key in keys:
   page.locator(f'#c95-reference-index [data-k="{key}"]').click();body=page.locator('.mc-dlg-b');assert body.is_visible() and 'Fiche absente' not in body.inner_text() and len(body.inner_text())>80
   assert body.evaluate('(e)=>e.scrollWidth<=e.clientWidth'),key
   if key=='c95-d-rasburicase':assert '0,20 mg/kg/j' in body.inner_text().replace('\u00ad','')
   if key in ['c95-d-rasburicase','c95-d-ponatinib']:capture(key+'-popup')
   item['windows_checked'].append(key);page.keyboard.press('Escape')
  page.locator('#c95-reference-index summary').click();panel('pE')
  quizzes=page.locator('#pE .mc-quiz');assert quizzes.count()==5
  for n in range(quizzes.count()):
   quiz=quizzes.nth(n);wrong=quiz.locator('[data-ok="0"]').first;right=quiz.locator('[data-ok="1"]');wrong.click(position={'x':5,'y':5});assert quiz.locator('.mc-fb').is_visible();right.click(position={'x':5,'y':5});assert quiz.locator('.mc-fb').is_visible();item['quiz_checked'].append({'index':n,'wrong_then_right':True})
  capture('quizzes');panel('pA');item['horizontal_overflow']=page.evaluate('document.documentElement.scrollWidth-innerWidth');assert item['horizontal_overflow']==0
  page.locator('.mc-book').click();page.locator('.mc-size-toggle').click();page.evaluate("(()=>{const r=document.querySelector('.mc-size-range');r.value=24;r.dispatchEvent(new Event('input'))})()");page.keyboard.press('Escape')
  item['book_font']=page.evaluate("getComputedStyle(document.querySelector('.mc')).getPropertyValue('--mc-fs').trim()");item['book_overflow']=page.evaluate('document.documentElement.scrollWidth-innerWidth');assert item['book_font']=='24px' and item['book_overflow']==0;capture('livre24')
  report['viewports'].append(item);page.close()
 browser.close()
assert not report['errors']
(OUT/'browser-report-autonomous.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'ok':True,'viewports':len(report['viewports']),'original_occurrences_per_viewport':len(report['viewports'][0]['originals_checked']),'errors':report['errors']}))
