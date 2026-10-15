from pathlib import Path
import json,datetime,hashlib
from playwright.sync_api import sync_playwright
OUT=Path(__file__).resolve().parent
URL='http://127.0.0.1:8091/fragments/MEDINA_S08_nerveux.html#/entry/G01'
report={'tested_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'url':URL,'browser':'system Chromium /usr/bin/chromium','checks':[],'page_errors':[],'scope':'real built S08 frontend; G01 only; no clinical validation'}
ROOT=OUT.parents[4]
report['source_files_sha256']={str(f.relative_to(ROOT)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted((ROOT/'chapters/G01').glob('*.html'))}
report['built_frontend_sha256']=hashlib.sha256(Path('/workspace/scratch/g01-preview/fragments/MEDINA_S08_nerveux.html').read_bytes()).hexdigest()
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 for width,height in [(1360,960),(390,844)]:
  context=browser.new_context(viewport={'width':width,'height':height});page=context.new_page();page.on('pageerror',lambda e:report['page_errors'].append(str(e)))
  page.goto(URL);page.wait_for_selector('.mc',timeout=60000);page.wait_for_timeout(600)
  assert page.locator('.mc-status').evaluate_all('(xs)=>xs.some(x=>x.textContent.replace(/\u00ad/g,"").includes("Révision Alpha en cours : certaines réserves thérapeutiques et sources héritées restent à vérifier ; les audits finaux de cette version ne sont pas clos."))');record={'viewport':[width,height],'captures':[],'visible_reservation_notice':True}
  def shot(name):
   filename=f'{width}-{name}.png';page.screenshot(path=str(OUT/filename));record['captures'].append(filename)
  shot('opening')
  page.locator('.mc-tabs [data-p="pS"]').click();page.wait_for_timeout(200)
  tabs=page.locator('.mc-sci-bar button[data-s]');assert tabs.count()==6
  first=tabs.first;assert first.get_attribute('id')=='g01-tab-semio';assert first.inner_text().strip()=='Sémiologie fondamentale et analytique'
  assert first.get_attribute('aria-selected')=='true';assert first.get_attribute('aria-controls')=='g01-s-semio'
  panel=page.locator('#g01-s-semio');assert panel.is_visible();assert panel.get_attribute('role')=='tabpanel';assert panel.get_attribute('aria-labelledby')=='g01-tab-semio'
  assert page.locator('.mc-sci:not([hidden])').count()==1
  sections=panel.locator('[data-semiology]');assert sections.count()==9
  markers=sections.evaluate_all('(xs)=>xs.map(x=>x.dataset.semiology)');assert set(markers)==set('normal signs mechanisms examination interpretation differentials urgency limits sources'.split())
  assert panel.locator('h3').first.inner_text()=='Pour la leçon : quelle est la sémiologie fondamentale et analytique ?'
  record['default_semiology']=True;record['nine_sections']=markers
  panel.evaluate('(el)=>window.scrollTo({top:window.scrollY+el.getBoundingClientRect().top-230,behavior:"instant"})');page.wait_for_timeout(250);shot('semiology')
  for i in range(1,6):
   tab=tabs.nth(i);tab.click();target=tab.get_attribute('data-s');assert page.locator('#'+target).is_visible();assert page.locator('.mc-sci:not([hidden])').count()==1;assert tab.get_attribute('aria-selected')=='true';assert first.get_attribute('aria-selected')=='false'
  first.focus();page.keyboard.press('Enter');assert panel.is_visible();tabs.nth(1).focus();page.keyboard.press('Space');assert page.locator('#g01-s-anat').is_visible()
  figure=page.locator('#g01-s-anat figure');figure.scroll_into_view_if_needed();page.wait_for_timeout(300);shot('anatomy-original')
  href=page.locator('#g01-s-anat svg image').get_attribute('href');loaded=page.evaluate('async (src)=>{const img=new Image();img.src=src;await img.decode();return [img.naturalWidth,img.naturalHeight]}',href);assert loaded==[648,450];record['original_png_decoded']=loaded
  first.click();page.evaluate('window.scrollTo(0,0)');page.wait_for_timeout(100)
  page.locator('.mc-navigo-trigger').click();items=page.locator('.mc-navigo-item');target=items.filter(has_text='Pour la leçon : quelle est la sémiologie fondamentale et analytique ?');assert target.count()==1;target.click();page.wait_for_timeout(500);assert page.evaluate('document.activeElement.textContent').startswith('Pour la leçon :');record['navigo_semiology']=True
  page.locator('.mc-size-toggle').click();page.locator('.mc-size-range').evaluate('(el)=>{el.value=24;el.dispatchEvent(new Event("input"))}');page.keyboard.press('Escape');assert page.locator('.mc').evaluate('(el)=>getComputedStyle(el).getPropertyValue("--mc-fs").trim()')=='24px';panel.locator('p').first.evaluate('(el)=>window.scrollTo({top:window.scrollY+el.getBoundingClientRect().top-230,behavior:"instant"})');page.wait_for_timeout(250);shot('font24')
  doc_width=page.evaluate('document.documentElement.scrollWidth');record['font24_document_scroll_width']=doc_width;assert doc_width<=width+2
  page.locator('.mc-size-toggle').click();page.locator('.mc-size-reset').click();page.keyboard.press('Escape')
  page.locator('.mc-book').click();page.wait_for_timeout(250);assert page.locator('.mc').evaluate('(el)=>el.classList.contains("book")');panel.evaluate('(el)=>window.scrollTo({top:window.scrollY+el.getBoundingClientRect().top-230,behavior:"instant"})');page.wait_for_timeout(250);shot('book-semiology');record['book_mode']=True;record['book_document_scroll_width']=page.evaluate('document.documentElement.scrollWidth');assert record['book_document_scroll_width']<=width+2;page.locator('.mc-book').click()
  page.locator('.mc-tabs [data-p="pA"]').click();button=page.locator('.mc-w[data-k="g01-meningisme"]').first;button.click();page.wait_for_timeout(150);assert page.locator('.mc-dlg-b').is_visible();record['popup_text']=page.locator('.mc-dlg-b').inner_text();shot('popup');assert 'Fiche absente' not in record['popup_text'] and '83' in record['popup_text'];page.keyboard.press('Escape');record['popup_open_and_escape']=True
  page.locator('.mc-tabs [data-p="pP"]').click();page.locator('.mc-w[data-k="g01-vanco-mero"]').first.click();page.wait_for_timeout(100);pharma=page.locator('.mc-dlg-b').inner_text().replace('\u00ad','');assert '57236' in pharma and '53105' in pharma and 'valproate' in pharma;shot('new-pharmacology-popup');page.keyboard.press('Escape');record['new_pharmacology_popup']=True
  ids=page.locator('.mc [id]').evaluate_all('(xs)=>xs.map(x=>x.id)');assert len(ids)==len(set(ids));record['unique_ids']=True
  record['keyboard_enter_space']=True;record['six_science_tabs_exclusive']=True;report['checks'].append(record);context.close()
 browser.close()
report['result']='passed' if not report['page_errors'] else 'page_errors'
(OUT/'browser-semiology.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
assert report['result']=='passed'
