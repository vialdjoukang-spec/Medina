from pathlib import Path
from playwright.sync_api import sync_playwright
import json,hashlib,datetime,re
D=Path(__file__).resolve().parent;F=D/'E30-apercu-autonome.html';raw=F.read_text()
report={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'preview_sha256':hashlib.sha256(F.read_bytes()).hexdigest(),'method':'Exact autonomous native HTML bytes on intercepted https://medina-e30.test/; all other requests aborted. No file navigation, real server, deployment or main tested.','checks':[],'page_errors':[],'blocked_requests':[],'clinical_certification':False}
with sync_playwright() as pw:
 browser=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 for width,height in [(1440,960),(390,844)]:
  ctx=browser.new_context(viewport={'width':width,'height':height});page=ctx.new_page();page.on('pageerror',lambda e:report['page_errors'].append(str(e)));page.route('**/*',lambda r:(report['blocked_requests'].append(r.request.url),r.abort()));page.route('https://medina-e30.test/',lambda r:r.fulfill(status=200,content_type='text/html; charset=utf-8',body=raw));page.goto('https://medina-e30.test/',wait_until='domcontentloaded',timeout=60000);page.wait_for_selector('.mc',timeout=60000)
  r={'viewport':[width,height],'captures':[],'images':[],'windows':[],'abbreviations':[],'tables':[]}
  def shot(name):
   fn=f'{width}-{name}.png';page.wait_for_timeout(120);page.screenshot(path=str(D/fn));r['captures'].append(fn)
  assert 'Anomalies de la puberté, non classées ailleurs' in page.locator('.mc-chap-head h1').inner_text();shot('opening')
  for panel in ['pA','pE','pS','pP']:
   page.locator('.mc-tabs [data-p="'+panel+'"]').click();assert page.locator('#'+panel).is_visible()
  page.locator('.mc-tabs [data-p="pS"]').click();tabs=page.locator('.mc-sci-bar button[data-s]');assert tabs.count()==6;assert tabs.first.get_attribute('data-s')=='e30-s-semio';assert page.locator('#e30-s-semio').is_visible();assert page.locator('#e30-s-semio [data-semiology]').count()==9;shot('semiology')
  for i in range(6):
   tab=tabs.nth(i);tab.click();target=tab.get_attribute('data-s');unit=page.locator('#'+target);assert unit.is_visible();assert page.locator('.mc-sci:not([hidden])').count()==1;r[target]={'words':len(unit.inner_text().split()),'figures':unit.locator('figure').count()}
   if i in [1,2]:
    fig=unit.locator('figure');fig.scroll_into_view_if_needed();im=fig.locator('img');im.evaluate('(im)=>im.decode()');dims=im.evaluate('(im)=>[im.naturalWidth,im.naturalHeight,im.complete]');expected=[743,686,True] if i==1 else [2816,2112,True];markers=4 if i==1 else 3;assert dims==expected;assert fig.locator('[data-e30-pin]').count()==markers;r['images'].append({'panel':target,'natural':dims,'markers':markers,'rendered_width':im.evaluate('(im)=>im.getBoundingClientRect().width')});shot('anatomy' if i==1 else 'histology');fig.screenshot(path=str(D/f'{width}-{target}-whole-figure.png'));r['captures'].append(f'{width}-{target}-whole-figure.png');fig.locator('figcaption').scroll_into_view_if_needed();shot('anatomy-caption' if i==1 else 'histology-caption')
  tabs.nth(1).focus();page.keyboard.press('Enter');assert page.locator('#e30-s-anat').is_visible();tabs.nth(2).focus();page.keyboard.press('Space');assert page.locator('#e30-s-histo').is_visible();r['keyboard_enter_space']=True
  # Visit every actual window from its visible control, including summaries.
  for panel in ['pA','pE','pP','pS']:
   page.locator('.mc-tabs [data-p="'+panel+'"]').click()
   for si in (range(6) if panel=='pS' else [None]):
    if si is not None:tabs.nth(si).click()
    keys=list(dict.fromkeys(page.locator('.mc-w:visible,.mc-pareto-btn:visible').evaluate_all('(xs)=>xs.map(x=>x.dataset.k)')))
    for key in keys:
     if key in r['windows']:continue
     page.locator('[data-k="'+key+'"]:visible').first.click();dlg=page.locator('.mc-dlg-b');assert dlg.is_visible();text=dlg.inner_text().replace('\u00ad','');assert 'Fiche absente' not in text and 'NaN' not in text and len(text)>25
     if key=='e30-lucrin':assert '7,5' in text and '11,25' in text and '15 mg' in text;shot('lucrin-popup');dlg.evaluate('(x)=>x.scrollTop=x.scrollHeight');shot('lucrin-popup-bottom')
     if key=='e30-estradiol':assert 'aucune indication' in text and '3–7' in text;shot('estradiol-popup');dlg.evaluate('(x)=>x.scrollTop=x.scrollHeight');shot('estradiol-popup-bottom')
     for ti in range(dlg.locator('table').count()):
      table=dlg.locator('table').nth(ti);dims=table.evaluate('(x)=>({client:x.clientWidth,scroll:x.scrollWidth,overflow:getComputedStyle(x).overflowX})')
      if dims['scroll']>dims['client']+2:
       assert dims['overflow']=='auto';table.evaluate('(x)=>x.scrollLeft=x.scrollWidth');assert table.evaluate('(x)=>x.scrollLeft')>0
       if key=='e30-lucrin':table.scroll_into_view_if_needed();shot('lucrin-popup-table-right')
       table.evaluate('(x)=>x.scrollLeft=0')
      r.setdefault('popup_tables',[]).append({'key':key,**dims})
     r['windows'].append(key);page.keyboard.press('Escape')
  page.locator('.mc-tabs [data-p="pE"]').click();quizzes=page.locator('#pE .mc-quiz');assert quizzes.count()==4
  for i in range(4):
   q=quizzes.nth(i);q.locator('.mc-opt[data-ok="0"]').first.click();assert q.locator('.mc-fb').is_visible();q.locator('.mc-opt[data-ok="1"]').click();assert q.locator('.mc-fb').is_visible()
  r['four_quizzes']=True;shot('quiz-feedback')
  # Context checks are separate from the lexical abbreviation audit.
  assert page.locator('.mc [data-ab="S1"],.mc [data-ab="S3"],.mc [data-ab="IA"],.mc [data-ab="IC"],.mc [data-ab="A1"],.mc [data-ab="A2"],.mc [data-ab="A3"],.mc [data-ab="AA"],.mc [data-ab="CMT"],.mc [data-ab="TH"],.mc [data-ab="T2"],.mc [data-ab="RCP"]').count()==0
  for panel in ['pA','pE','pP','pS']:
   page.locator('.mc-tabs [data-p="'+panel+'"]').click()
   for si in (range(6) if panel=='pS' else [None]):
    if si is not None:tabs.nth(si).click()
    terms=list(dict.fromkeys(page.locator('.mc .mc-ab:visible').evaluate_all('(xs)=>xs.map(x=>x.dataset.ab)')))
    for term in terms:
     if term in r['abbreviations']:continue
     page.locator('.mc [data-ab="'+term+'"]:visible').first.click();txt=page.locator('.mc-dlg-b').inner_text();assert len(txt)>5 and 'Fiche absente' not in txt;r['abbreviations'].append(term);page.keyboard.press('Escape')
  r['known_homonym_collisions_absent']=True
  # 24px and Livre: all tables expose a horizontal scroll surface locally.
  page.locator('.mc-tabs [data-p="pP"]').click();page.locator('.mc-size-toggle').click();page.locator('.mc-size-range').evaluate('(x)=>{x.value=24;x.dispatchEvent(new Event("input"))}');page.keyboard.press('Escape');assert page.locator('.mc').evaluate('(x)=>getComputedStyle(x).getPropertyValue("--mc-fs").trim()')=='24px'
  for i in range(page.locator('#pP table').count()):
   t=page.locator('#pP table').nth(i);t.scroll_into_view_if_needed();v=t.evaluate('(x)=>({client:x.clientWidth,scroll:x.scrollWidth,overflow:getComputedStyle(x).overflowX})');r['tables'].append(v)
   if v['scroll']>v['client']+2:assert v['overflow']=='auto';t.evaluate('(x)=>x.scrollLeft=x.scrollWidth');assert t.evaluate('(x)=>x.scrollLeft')>0;t.evaluate('(x)=>x.scrollLeft=0')
  page.locator('#e30-p-2').scroll_into_view_if_needed();shot('font24-pharmacology');r['normal24_width']=page.evaluate('document.documentElement.scrollWidth');assert r['normal24_width']<=width+2
  page.locator('.mc-book').click();assert page.locator('.mc').evaluate('(x)=>x.classList.contains("book")');assert page.locator('.mc').evaluate('(x)=>getComputedStyle(x).getPropertyValue("--mc-fs").trim()')=='24px';page.locator('#e30-p-4').scroll_into_view_if_needed();r['book24_width']=page.evaluate('document.documentElement.scrollWidth');assert r['book24_width']<=width+2;shot('book24-pharmacology');page.locator('.mc-w[data-k="e30-lucrin"]:visible').first.click();dlg=page.locator('.mc-dlg-b');assert dlg.is_visible() and '7,5' in dlg.inner_text();r['book24_popup_font']=dlg.evaluate('(x)=>getComputedStyle(x).fontSize');shot('book24-lucrin-popup');table=dlg.locator('table').first;table.scroll_into_view_if_needed();dims=table.evaluate('(x)=>({client:x.clientWidth,scroll:x.scrollWidth,overflow:getComputedStyle(x).overflowX})');r['book24_popup_table']=dims;r['book24_table_cell_font']=table.locator('td').first.evaluate('(x)=>getComputedStyle(x).fontSize');assert abs(float(r['book24_table_cell_font'].replace('px',''))-24)<1
  if dims['scroll']>dims['client']+2:assert dims['overflow']=='auto';table.evaluate('(x)=>x.scrollLeft=x.scrollWidth');assert table.evaluate('(x)=>x.scrollLeft')>0
  shot('book24-lucrin-table');page.keyboard.press('Escape');page.locator('.mc-book').click();page.locator('.mc-size-toggle').click();page.locator('.mc-size-reset').click();page.keyboard.press('Escape')
  page.locator('.mc-tabs [data-p="pS"]').click();tabs.first.click();page.locator('.mc-navigo-trigger').click();item=page.locator('.mc-navigo-item').filter(has_text='Pour la leçon : quelle est la sémiologie fondamentale et analytique ?');assert item.count()==1;item.click();page.wait_for_timeout(200);assert page.evaluate('document.activeElement.textContent').startswith('Pour la leçon :');r['navigo_semiology']=True
  ids=page.locator('.mc [id]').evaluate_all('(xs)=>xs.map(x=>x.id)');assert len(ids)==len(set(ids));r['unique_ids']=True
  report['checks'].append(r);ctx.close()
 browser.close()
report['result']='passed' if not report['page_errors'] else 'page_errors';(D/'browser-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'result':report['result'],'checks':[{'viewport':r['viewport'],'windows':len(r['windows']),'glossary_windows':len(r['abbreviations']),'images':r['images']} for r in report['checks']],'page_errors':report['page_errors']},ensure_ascii=False,indent=2));assert report['result']=='passed'
