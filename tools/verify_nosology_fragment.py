#!/usr/bin/env python3
"""Verify a built fragment's exact inventory, course access and empty plans."""
import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from nosologyEngine import progress, read_json


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fragment', required=True)
    parser.add_argument('--browser', action='store_true')
    args = parser.parse_args()
    fragment = next(item for item in read_json(ROOT / 'fragments.json') if item['id'] == args.fragment)
    path = ROOT / 'dist/fragments' / f"MEDINA_{fragment['id']}_{fragment['slug']}.html"
    source = path.read_text()
    inventory = read_json(ROOT / 'nosology/fragments' / (args.fragment + '.json'))
    organisation = json.loads(re.search(r'<script id="medina-category-organisation-data"[^>]*>(.*?)</script>', source, re.S)[1])
    built = organisation['nosology']
    assert built['lessons'] == inventory['lessons'], 'Inventaire embarqué différent des coquilles sources'
    assert built['progress'] == progress(inventory['lessons'])
    assert organisation['fragment']['id'] == args.fragment
    assert {item['code'] for item in inventory['preserved_courses']} == {item['code'] for item in organisation['courses']}
    report = {'fragment': args.fragment, 'metadata': 'passed', 'progress': built['progress'], 'gauges': built['gauges']}
    if args.browser:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as runtime:
            browser = runtime.chromium.launch(headless=True, args=['--no-sandbox'])
            page = browser.new_page(viewport={'width': 1440, 'height': 1000})
            errors = []
            page.on('pageerror', lambda error: errors.append(str(error)))
            url = path.resolve().as_uri()
            page.goto(url + '#/home')
            page.wait_for_selector('.mcg-home>.nosology-gauges')
            assert page.locator('.mcg-home>.nosology-gauges progress').count() == 3
            assert page.locator('.mcg-home>.nosology-gauges b').count() == 3
            shell = next((item for item in built['lessons'] if not item['existing_course']), None)
            if shell:
                page.goto(url + '#/entry/' + shell['code'])
                page.wait_for_selector('.nosology-plan')
                assert page.locator('.nosology-plan h3').all_text_contents() == [item['title'] for item in shell['plan']]
                assert page.locator('.nosology-plan p').count() == 0, 'Contenu introduit dans une coquille vide'
                assert shell['code'] in page.locator('.mcg-planned-panel').inner_text()
                assert page.locator('.nosology-progress progress').count() == 4
                page.set_viewport_size({'width': 390, 'height': 844})
                assert not page.evaluate('document.documentElement.scrollWidth > innerWidth'), 'Débordement mobile'
            course = next(iter(built['preserved_courses']), None)
            if course:
                page.goto(url + '#/entry/' + course['code'])
                page.wait_for_selector('.mc')
            page.set_viewport_size({'width': 390, 'height': 844})
            page.goto(url + '#/home')
            page.wait_for_selector('.mcg-home>.nosology-gauges')
            assert not page.evaluate('document.documentElement.scrollWidth > innerWidth'), 'Jauges : débordement mobile'
            assert not errors, errors
            browser.close()
        report['browser_desktop_mobile'] = 'passed'
    output = ROOT / 'docs/nosology' / (args.fragment + '-checks.json')
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(report, ensure_ascii=False))


if __name__ == '__main__': main()
