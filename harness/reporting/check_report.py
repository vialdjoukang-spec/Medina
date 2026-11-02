#!/usr/bin/env python3
"""Contrôle du rapport autonome, sans publication et sans activité auteur."""
import datetime,hashlib,json,sys
from pathlib import Path
from playwright.sync_api import sync_playwright
report=Path(sys.argv[1]);out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
payload=report.read_bytes();data=json.loads(report.with_suffix('.json').read_text())
result={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sha256':hashlib.sha256(payload).hexdigest(),'expected_completions':data['completed_count'],'expected_versions':data['versions_verified'],'viewports':[],'errors':[],'requests':[]}
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 for width,height in [(1440,900),(390,844)]:
  page=browser.new_page(viewport={'width':width,'height':height})
  page.on('pageerror',lambda e:result['errors'].append(str(e)))
  page.on('request',lambda r:result['requests'].append(r.url))
  page.route('**/*',lambda r:r.fulfill(body=payload,content_type='text/html') if r.request.url=='http://medina.local/report.html' else r.abort())
  page.goto('http://medina.local/report.html',wait_until='networkidle')
  item={'width':width,'overflow':page.evaluate('document.documentElement.scrollWidth-innerWidth'),'articles':page.locator('article.lesson').count(),'queue_rows':page.locator('#future tbody tr').count()}
  assert item['overflow']==0 and item['articles']==data['versions_verified'] and item['queue_rows']==data['candidate_count']
  page.screenshot(path=str(out/f'rapport-{width}.png'))
  page.locator('#filter').fill('N02');assert page.locator('#future tbody tr:visible').count()==1
  page.locator('#filter').fill('');page.locator('#expand').click();assert page.locator('details:not([open])').count()==0
  page.locator('#expand').click();assert page.locator('details[open]').count()==0
  item['filter_and_details']=True;result['viewports'].append(item);page.close()
 page=browser.new_page(java_script_enabled=False,viewport={'width':390,'height':844})
 page.route('**/*',lambda r:r.fulfill(body=payload,content_type='text/html') if r.request.url=='http://medina.local/report.html' else r.abort())
 page.goto('http://medina.local/report.html');assert page.locator('article.lesson').count()==data['versions_verified'];assert page.locator('#future tbody tr').count()==data['candidate_count'];result['no_javascript_content']=True
 browser.close()
assert not result['errors'] and set(result['requests'])=={'http://medina.local/report.html'}
result['external_network_requests']=[]
(out/'report-browser.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'ok':True,'sha256':result['sha256'],'viewports':len(result['viewports']),'no_javascript':True,'external_requests':0}))
