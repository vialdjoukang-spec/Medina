from pathlib import Path
import json,datetime,hashlib
from playwright.sync_api import sync_playwright
D=Path(__file__).resolve().parent;F=D/'E02-apercu-autonome.html';html=F.read_text()
report={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'preview_sha256':hashlib.sha256(F.read_bytes()).hexdigest(),'mode':'Chromium navigation to intercepted https://medina-preview.test/ with exact autonomous bytes; all other requests aborted. No external HTTP server tested. Same-origin storage available.','checks':[],'page_errors':[],'blocked_requests':[],'clinical_certification':False}
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 for w,h in [(1440,960),(390,844)]:
  ctx=b.new_context(viewport={'width':w,'height':h});page=ctx.new_page();page.route('**/*',lambda route:(report['blocked_requests'].append(route.request.url),route.abort()));page.on('pageerror',lambda e:report['page_errors'].append(str(e)))
  page.route('https://medina-preview.test/',lambda route:route.fulfill(status=200,content_type='text/html; charset=utf-8',body=html));page.goto('https://medina-preview.test/',wait_until='domcontentloaded',timeout=60000);page.wait_for_selector('.mc',timeout=60000)
  r={'viewport':[w,h],'captures':[],'images':[],'popups_tested':[]}
  def shot(name):
   page.wait_for_timeout(180);fn=f'{w}-{name}.png';page.screenshot(path=str(D/fn));r['captures'].append(fn)
  shot('opening');assert 'E02' in page.locator('.mc-chap-head').inner_text()
  page.locator('#e02-3 figure').scroll_into_view_if_needed();shot('clinical-diagram')
  page.locator('.mc-tabs [data-p="pS"]').click();tabs=page.locator('.mc-sci-bar button[data-s]');assert tabs.count()==6
  assert tabs.first.get_attribute('data-s')=='e02-s-semio';sem=page.locator('#e02-s-semio');assert sem.is_visible();assert sem.locator('[data-semiology]').count()==9
  assert sem.locator('h2').first.inner_text()=='Pour la leçon : quelle est la sémiologie fondamentale et analytique ?';sem.locator('h2').first.scroll_into_view_if_needed();shot('semiology')
  for i in range(6):
   t=tabs.nth(i);t.click();target=t.get_attribute('data-s');assert page.locator('#'+target).is_visible();assert page.locator('.mc-sci:not([hidden])').count()==1
   r[target]={'words':len(page.locator('#'+target).inner_text().split()),'figures':page.locator('#'+target+' figure').count()}
   for fi in range(page.locator('#'+target+' figure:has(svg)').count()):
    page.locator('#'+target+' figure:has(svg)').nth(fi).scroll_into_view_if_needed();shot(target+'-diagram-'+str(fi))
  tabs.nth(1).focus();page.keyboard.press('Enter');assert page.locator('#e02-s-anat').is_visible()
  for tabcode,name in [('anat','normal-anatomy'),('histo','histology')]:
   page.locator('.mc-sci-bar [data-s="e02-s-'+tabcode+'"]').click();fig=page.locator('#e02-s-'+tabcode+' figure:has(img)');fig.scroll_into_view_if_needed();im=fig.locator('img');im.evaluate('(im)=>im.decode()');dims=im.evaluate('(im)=>[im.naturalWidth,im.naturalHeight,im.complete]');assert dims==[737,1410,True];r['images'].append({'natural':dims,'markers':fig.locator('span[role="img"]').count(),'tab':tabcode});shot(name)
  tabs.nth(2).focus();page.keyboard.press('Space');assert page.locator('#e02-s-histo').is_visible()
  page.locator('.mc-tabs [data-p="pP"]').click();page.locator('.mc-w[data-k="e02-levo"]:visible').first.click();txt=page.locator('.mc-dlg-b').inner_text().replace('\u00ad','');assert 'fréquences' in txt.lower() and 'angiœdème' in txt;shot('euthyrox-popup');page.keyboard.press('Escape');r['euthyrox_exact_fi']=True
  page.locator('.mc-tabs [data-p="pA"]').click();page.locator('.mc-w[data-k="e02-antitpo"]:visible').first.click();txt=page.locator('.mc-dlg-b').inner_text().replace('\u00ad','');assert 'auto-immunité' in txt and 'Thrombopoïétine' not in txt;shot('antitpo-popup');page.keyboard.press('Escape');r['context_glossary_correct']=True
  page.locator('.mc-tabs [data-p="pP"]').click()
  page.locator('#e02-p-3').scroll_into_view_if_needed();shot('pharmacology');r['normal_width']=page.evaluate('document.documentElement.scrollWidth');assert r['normal_width']<=w+2
  page.locator('.mc-size-toggle').click();page.locator('.mc-size-range').evaluate('(el)=>{el.value=24;el.dispatchEvent(new Event("input"))}');page.keyboard.press('Escape');r['font24']=page.locator('.mc').evaluate('(el)=>getComputedStyle(el).getPropertyValue("--mc-fs").trim()');assert r['font24']=='24px';page.locator('#e02-p-2 table').scroll_into_view_if_needed();shot('font24-pharmacology')
  table=page.locator('#e02-p-2 table');r['table']=table.evaluate('(el)=>({client:el.clientWidth,scroll:el.scrollWidth,overflow:getComputedStyle(el).overflowX})')
  if r['table']['scroll']>r['table']['client']+2:
   assert r['table']['overflow']=='auto';table.evaluate('(el)=>el.scrollLeft=el.scrollWidth');assert table.evaluate('(el)=>el.scrollLeft')>0;shot('font24-table-right');table.evaluate('(el)=>el.scrollLeft=0')
  page.locator('.mc-book').click();assert page.locator('.mc').evaluate('(el)=>el.classList.contains("book")');assert page.locator('.mc').evaluate('(el)=>getComputedStyle(el).getPropertyValue("--mc-fs").trim()')=='24px';page.locator('#e02-p-3 h2').scroll_into_view_if_needed();r['book24_width']=page.evaluate('document.documentElement.scrollWidth');assert r['book24_width']<=w+2;shot('book24-pharmacology');page.locator('.mc-book').click();page.locator('.mc-size-toggle').click();page.locator('.mc-size-reset').click();page.keyboard.press('Escape')
  page.locator('.mc-book').click();page.locator('#e02-p-3 h2').scroll_into_view_if_needed();shot('book-pharmacology');page.locator('.mc-book').click()
  page.locator('.mc-tabs [data-p="pE"]').click();assert page.locator('#pE').is_visible();page.locator('#e02-e-3 h2').scroll_into_view_if_needed();shot('examinations');quizzes=page.locator('#pE .mc-quiz');assert quizzes.count()==4
  for qi in range(quizzes.count()):
   q=quizzes.nth(qi);q.locator('.mc-opt[data-ok="1"]').click();assert q.locator('.mc-fb').is_visible()
  r['four_quizzes_feedback']=True
  # Les fenêtres sont ouvertes à partir de leurs contrôles réels visibles.
  for panel in ['pA','pE','pP','pS']:
   page.locator('.mc-tabs [data-p="'+panel+'"]').click()
   sciences=range(6) if panel=='pS' else [None]
   for si in sciences:
    if si is not None:tabs.nth(si).click()
    controls=page.locator('.mc-w:visible,.mc-pareto-btn:visible');keys=list(dict.fromkeys(controls.evaluate_all('(xs)=>xs.map(x=>x.dataset.k)')))
    for key in keys:
     if key in r['popups_tested']:continue
     control=page.locator('[data-k="'+key+'"]:visible').first;control.click();dlg=page.locator('.mc-dlg-b');assert dlg.is_visible();txt=dlg.inner_text();assert len(txt)>20;assert 'NaN' not in txt;r['popups_tested'].append(key);page.keyboard.press('Escape')
  page.locator('.mc-tabs [data-p="pS"]').click();tabs.first.click();page.locator('.mc-navigo-trigger').click();item=page.locator('.mc-navigo-item').filter(has_text='Pour la leçon : quelle est la sémiologie fondamentale et analytique ?');assert item.count()==1;item.click();page.wait_for_timeout(250);assert page.evaluate('document.activeElement.textContent').startswith('Pour la leçon :');r['navigo_semiology']=True
  ids=page.locator('.mc [id]').evaluate_all('(xs)=>xs.map(x=>x.id)');assert len(ids)==len(set(ids));r['unique_ids']=True;r['keyboard_enter_space']=True
  report['checks'].append(r);ctx.close()
 b.close()
report['result']='passed' if not report['page_errors'] else 'page_errors';(D/'browser-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'result':report['result'],'viewports':[{'viewport':r['viewport'],'images':len(r['images']),'popups':len(r['popups_tested']),'captures':len(r['captures'])} for r in report['checks']],'page_errors':report['page_errors']},indent=2));assert report['result']=='passed'
