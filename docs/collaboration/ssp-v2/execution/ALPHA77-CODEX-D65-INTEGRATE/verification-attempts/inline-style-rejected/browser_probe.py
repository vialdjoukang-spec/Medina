"""Vrai moteur Medina sur HTTP intercepté ; sans réseau ni déploiement."""
from pathlib import Path
import json,datetime
from playwright.sync_api import sync_playwright
OUT=Path(__file__).resolve().parent;NATIVE=OUT/'D65-apercu-autonome.html';CAP=OUT/'captures';CAP.mkdir(exist_ok=True)
report={'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'mode':'native HTML, HTTP intercepted, external requests aborted','errors':[],'viewports':[],'clinical_certification':False}
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 for width,height in [(1440,900),(390,844)]:
  page=browser.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
  page.on('pageerror',lambda e:report['errors'].append(str(e)))
  page.route('**/*',lambda r:r.fulfill(body=NATIVE.read_bytes(),content_type='text/html') if r.request.url=='http://medina.local/native.html' else r.abort())
  page.goto('http://medina.local/native.html',wait_until='domcontentloaded');page.evaluate("location.hash='#/entry/D65'");page.wait_for_timeout(700)
  assert page.locator('.mc').count()==1
  item={'width':width,'screenshots':[],'originals_checked':[],'windows_checked':[],'quiz_checked':[],'causal_diagrams_checked':[]}
  def capture(name,element=None):
   path=CAP/f'D65-{width}-{name}.png';(element or page).screenshot(path=str(path));item['screenshots'].append(str(path.relative_to(OUT)))
  def panel(name):page.locator(f'.mc-tabs button[data-p="{name}"]').click()
  capture('accueil');panel('pS');buttons=page.locator('.mc-sci-bar button');item['science_buttons']=buttons.all_text_contents();assert len(item['science_buttons'])==6
  assert page.locator('#d65-s-semio').is_visible();assert page.locator('#d65-tab-semio').get_attribute('aria-selected')=='true'
  item['semio_sections']=page.locator('[data-semiology]').count();assert item['semio_sections']==9;capture('semio')
  # Le moteur hérité ne gère pas les flèches ; Tab puis Entrée sont contrôlés réellement.
  buttons.first.focus();page.keyboard.press('ArrowRight');item['keyboard_after_arrow']=page.evaluate('document.activeElement.id');item['arrow_navigation_supported']=item['keyboard_after_arrow']=='d65-tab-anat'
  buttons.first.focus();page.keyboard.press('Tab');item['keyboard_after_tab']=page.evaluate('document.activeElement.id');assert item['keyboard_after_tab']=='d65-tab-anat';page.keyboard.press('Enter')
  assert page.locator('#d65-tab-anat').get_attribute('aria-selected')=='true'
  for main,tab,ident in [('pE',None,'d65-exam-original-blood'),('pS','anat','d65-science-sem'),('pS','histo','d65-science-blood')]:
   panel(main)
   if tab:page.locator(f'[data-s="d65-s-{tab}"]').click()
   fig=page.locator('#'+ident);img=fig.locator('img');img.scroll_into_view_if_needed();img.evaluate('(i)=>i.decode()')
   state=img.evaluate('(i)=>({width:i.naturalWidth,height:i.naturalHeight,loaded:i.complete&&i.naturalWidth>0,embedded:i.src.startsWith("data:")})');state['figure']=ident
   assert state['loaded'] and state['embedded'];item['originals_checked'].append(state);capture(ident,fig)
   caption=fig.locator('figcaption');state['caption_font_px']=caption.evaluate('(e)=>parseFloat(getComputedStyle(e).fontSize)');assert state['caption_font_px']>=14;caption.evaluate('(e)=>e.scrollIntoView({block:"center"})');capture(ident+'-legende',caption)
  for main,tab,ident in [('pA',None,'d65-causal-consumption'),('pA',None,'d65-causal-decision'),('pS','semio','d65-causal-semio'),('pS','phys','d65-causal-phys'),('pS','bio','d65-causal-bio'),('pS','immuno','d65-causal-immuno'),('pP',None,'d65-causal-txa')]:
   panel(main)
   if tab:page.locator(f'[data-s="d65-s-{tab}"]').click()
   fig=page.locator('#'+ident);fig.scroll_into_view_if_needed();assert fig.locator('svg[role="img"]').is_visible()
   fontsize=fig.locator('svg text').first.evaluate('(e)=>parseFloat(getComputedStyle(e).fontSize)*e.getScreenCTM().a');assert fontsize>=12
   capture(ident,fig);item['causal_diagrams_checked'].append({'id':ident,'rendered_font_px':fontsize})
  item['unsafe_shared_abbreviations']=page.locator('.mc [data-ab="ET"],.mc [data-ab="LAM"],.mc [data-ab="LMC"]').count();assert item['unsafe_shared_abbreviations']==0
  panel('pA');page.locator('#d65-reference-index summary').click();keys=page.locator('#d65-reference-index [data-k]').evaluate_all('(xs)=>xs.map(x=>x.dataset.k)');assert len(keys)==40
  for key in keys:
   page.locator(f'#d65-reference-index [data-k="{key}"]').click();body=page.locator('.mc-dlg-b');assert body.is_visible() and 'Fiche absente' not in body.inner_text() and len(body.inner_text())>80
   assert body.evaluate('(e)=>e.scrollWidth<=e.clientWidth'),key
   assert body.locator('[data-ab="ET"]').count()==0,key
   if key in ['d65-calcul-fib','d65-calcul-txa']:capture(key+'-popup')
   item['windows_checked'].append(key);page.keyboard.press('Escape')
  page.locator('#d65-reference-index summary').click()
  for main in ['pA','pE','pP']:
   panel(main);quizzes=page.locator('#'+main+' .mc-quiz')
   for n in range(quizzes.count()):
    quiz=quizzes.nth(n);quiz.locator('[data-ok="0"]').first.click(position={'x':5,'y':5});assert quiz.locator('.mc-fb').is_visible();quiz.locator('[data-ok="1"]').click(position={'x':5,'y':5});assert quiz.locator('.mc-fb').is_visible();item['quiz_checked'].append({'panel':main,'index':n,'wrong_then_right':True})
  assert len(item['quiz_checked'])==4;capture('quiz-dose');panel('pA')
  item['horizontal_overflow']=page.evaluate('document.documentElement.scrollWidth-innerWidth');assert item['horizontal_overflow']==0
  page.locator('.mc-book').click();page.locator('.mc-size-toggle').click();page.evaluate("(()=>{const r=document.querySelector('.mc-size-range');r.value=24;r.dispatchEvent(new Event('input'))})()");page.keyboard.press('Escape')
  item['book_font']=page.evaluate("getComputedStyle(document.querySelector('.mc')).getPropertyValue('--mc-fs').trim()");item['book_overflow']=page.evaluate('document.documentElement.scrollWidth-innerWidth');assert item['book_font']=='24px' and item['book_overflow']==0;capture('livre24')
  report['viewports'].append(item);page.close()
 browser.close()
assert not report['errors'];report['finished_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
(OUT/'browser-report-autonomous.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'ok':True,'viewports':len(report['viewports']),'windows_per_viewport':40,'quizzes_per_viewport':4,'errors':report['errors']}))
