from pathlib import Path
import json,datetime,hashlib,base64,gzip,re,mimetypes
from playwright.sync_api import sync_playwright
D=Path(__file__).resolve().parent;ROOT=D.parents[4]
F=D/'E00-apercu-autonome.html'
html=F.read_text();original_sha=hashlib.sha256(F.read_bytes()).hexdigest()
report={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'native_build_sha256':original_sha,'mode':'Chromium navigation to https://medina-preview.test/ fulfilled in memory with exact autonomous bundle bytes. Every other request aborted. No external network or HTTP server tested. Same-origin localStorage available; native engine unmodified.','checks':[],'page_errors':[],'blocked_requests':[],'medical_validation':False}
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 for w,h in [(1440,960),(390,844)]:
  ctx=b.new_context(viewport={'width':w,'height':h});page=ctx.new_page();page.route('**/*',lambda route:(report.setdefault('blocked_requests',[]).append(route.request.url),route.abort()));page.on('pageerror',lambda e:report['page_errors'].append(str(e)))
  page.route('https://medina-preview.test/',lambda route:route.fulfill(status=200,content_type='text/html; charset=utf-8',body=html))
  page.goto('https://medina-preview.test/',wait_until='domcontentloaded',timeout=60000)
  page.evaluate("location.hash='#/entry/E00'")
  page.wait_for_selector('.mc',timeout=60000)
  r={'viewport':[w,h],'captures':[]}
  def shot(name):
   page.wait_for_timeout(250);fn=f'{w}-{name}.png';page.screenshot(path=str(D/fn));r['captures'].append(fn)
  shot('opening')
  page.locator('.mc-tabs [data-p="pS"]').click();tabs=page.locator('.mc-sci-bar button[data-s]');assert tabs.count()==6
  assert tabs.first.get_attribute('data-s')=='e00-s-semio';assert tabs.first.get_attribute('aria-selected')=='true'
  sem=page.locator('#e00-s-semio');assert sem.is_visible();assert sem.locator('[data-semiology]').count()==9
  assert sem.locator('h3').first.inner_text()=='Pour la leçon : quelle est la sémiologie fondamentale et analytique ?'
  sem.locator('h3').first.scroll_into_view_if_needed();shot('semiology')
  for i in range(6):
   t=tabs.nth(i);t.click();target=t.get_attribute('data-s');assert page.locator('#'+target).is_visible();assert page.locator('.mc-sci:not([hidden])').count()==1
   r[target]={'words':len(page.locator('#'+target).inner_text().split()),'figures':page.locator('#'+target+' figure').count()}
  tabs.nth(1).focus();page.keyboard.press('Enter');assert page.locator('#e00-s-anat').is_visible()
  fig=page.locator('#e00-s-anat figure').first;fig.scroll_into_view_if_needed();img=fig.locator('img');img.evaluate('(im)=>im.decode()'); assert img.evaluate('(im)=>im.complete&&im.naturalWidth===737&&im.naturalHeight===1410');shot('anatomy-original')
  tabs.nth(2).focus();page.keyboard.press('Space');assert page.locator('#e00-s-histo').is_visible();histfig=page.locator('#e00-s-histo figure');histfig.locator('img').evaluate('(im)=>im.decode()');histfig.evaluate('(el)=>window.scrollTo({top:window.scrollY+el.getBoundingClientRect().bottom-650,behavior:"instant"})');shot('histology-original')
  tabs.nth(5).click();page.locator('#e00-s-sante figure').scroll_into_view_if_needed();shot('iodine-population')
  tabs.nth(2).click();page.locator('.mc-w[data-k="e00-thyroperoxydase"]:visible').first.click();assert 'organification' in page.locator('.mc-dlg-b').inner_text().replace('\u00ad','');page.keyboard.press('Escape');r['thyroperoxidase_context_correct']=True
  r['normal_document_width']=page.evaluate('document.documentElement.scrollWidth');assert r['normal_document_width']<=w+2
  page.locator('.mc-tabs [data-p="pP"]').click();page.locator('.mc-w[data-k="e00-calcul-dose"]').first.click();assert page.locator('.mc-dlg-b').is_visible();text=page.locator('.mc-dlg-b').inner_text().replace('\u00ad','');assert '32' in text and '48' in text;shot('dose-popup');page.keyboard.press('Escape')
  page.locator('.mc-w[data-k="e00-sources-2026"]:visible').first.click();source=page.locator('.mc-dlg-b').inner_text().replace('\u00ad','');assert 'S101' in source and 'S115' in source;page.keyboard.press('Escape');r['new_popups_open_escape']=True
  page.locator('#e00-p-securite2026').scroll_into_view_if_needed();shot('pharmacology')
  page.locator('.mc-size-toggle').click();page.locator('.mc-size-range').evaluate('(el)=>{el.value=24;el.dispatchEvent(new Event("input"))}');page.keyboard.press('Escape');r['applied_font_size']=page.locator('.mc').evaluate('(el)=>getComputedStyle(el).getPropertyValue("--mc-fs").trim()');assert r['applied_font_size']=='24px';page.locator('#e00-p-securite2026').scroll_into_view_if_needed();r['font24_document_width']=page.evaluate('document.documentElement.scrollWidth');assert r['font24_document_width']<=w+2;shot('font24-pharmacology')
  table=page.locator('#e00-p-securite2026 table');r['pharmacology_table']=table.evaluate('(el)=>({client:el.clientWidth,scroll:el.scrollWidth,overflow:getComputedStyle(el).overflowX})')
  if r['pharmacology_table']['scroll']>r['pharmacology_table']['client']+2:
   assert r['pharmacology_table']['overflow']=='auto';table.evaluate('(el)=>el.scrollLeft=el.scrollWidth');assert table.evaluate('(el)=>el.scrollLeft')>0;shot('font24-table-right');r['table_last_column_reachable']=True;table.evaluate('(el)=>el.scrollLeft=0')
  page.locator('.mc-book').click();assert page.locator('.mc').evaluate('(el)=>el.classList.contains("book")');assert page.locator('.mc').evaluate('(el)=>getComputedStyle(el).getPropertyValue("--mc-fs").trim()')=='24px';page.locator('#e00-p-securite2026 h2').scroll_into_view_if_needed();r['book24_document_width']=page.evaluate('document.documentElement.scrollWidth');assert r['book24_document_width']<=w+2;shot('book24-pharmacology');page.locator('.mc-book').click()
  page.locator('.mc-size-toggle').click();page.locator('.mc-size-reset').click();page.keyboard.press('Escape')
  page.locator('.mc-book').click();assert page.locator('.mc').evaluate('(el)=>el.classList.contains("book")');page.locator('#e00-p-securite2026 h2').scroll_into_view_if_needed();r['book_document_width']=page.evaluate('document.documentElement.scrollWidth');assert r['book_document_width']<=w+2;shot('book-pharmacology');page.locator('.mc-book').click()
  ids=page.locator('.mc [id]').evaluate_all('(xs)=>xs.map(x=>x.id)');assert len(ids)==len(set(ids));r['unique_ids']=True;r['image_bytes_decoded']=[737,1410];r['keyboard_enter_space']=True
  page.locator('.mc-tabs [data-p="pA"]').click();page.locator('.mc-tabs [data-p="pE"]').click();assert page.locator('#pE').is_visible();page.locator('#e00-e-normes').scroll_into_view_if_needed();shot('examinations');r['four_main_tabs']=True
  quizzes=page.locator('#pE .mc-quiz');assert quizzes.count()==4
  for qi in range(quizzes.count()):
   q=quizzes.nth(qi);q.locator('.mc-opt[data-ok="1"]').click();assert q.locator('.mc-fb').is_visible()
  page.locator('.mc-tabs [data-p="pP"]').click();q=page.locator('#pP .mc-quiz');assert q.count()==1;q.locator('.mc-opt[data-ok="1"]').click();assert q.locator('.mc-fb').is_visible();r['five_quizzes_correct_feedback']=True
  page.locator('.mc-pareto-btn:visible').first.click();assert page.locator('.mc-dlg-b').is_visible();assert 'NaN' not in page.locator('.mc-dlg-b').inner_text();page.keyboard.press('Escape');r['pareto_opens_with_ratio']=True
  page.locator('.mc-tabs [data-p="pS"]').click();tabs.first.click();page.locator('.mc-navigo-trigger').click();item=page.locator('.mc-navigo-item').filter(has_text='Pour la leçon : quelle est la sémiologie fondamentale et analytique ?');assert item.count()==1;item.click();page.wait_for_timeout(400);assert page.evaluate('document.activeElement.textContent').startswith('Pour la leçon :');r['navigo_semiology']=True
  report['checks'].append(r);ctx.close()
 b.close()
report['result']='passed' if not report['page_errors'] else 'page_errors'
(D/'browser-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
assert report['result']=='passed'
