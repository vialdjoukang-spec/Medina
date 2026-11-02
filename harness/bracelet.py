#!/usr/bin/env python3
"""Conseil local déterministe; ne télécharge ni n'installe aucun composant."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ROUTES = {
    'web': ['Crawl4AI', 'Firecrawl', 'requests-cache', 'Hishel', 'PyBreaker'],
    'source': ['requests-cache', 'Hishel', 'Chonkie', 'FlagEmbedding'],
    'volume': ['Chonkie', 'LLMLingua', 'RTK', 'FlagEmbedding'],
    'cache': ['GPTCache', 'Portkey Gateway', 'Prefect', 'requests-cache', 'Hishel'],
    'memoire': ['Mem0', 'Graphiti'],
    'veille': ['APScheduler', 'Celery', 'Phoenix'],
    'cout': ['LiteLLM', 'RouteLLM', 'Semantic Router', 'Phoenix'],
}

def suggest(task):
    names = []
    for key, candidates in ROUTES.items():
        if key in task.lower():
            names.extend(candidates)
    names = list(dict.fromkeys(names or ROUTES['source']))
    catalog = json.loads((ROOT / 'catalog.json').read_text())['tools']
    return {'task': task, 'suggestions': [t for n in names[:5] for t in catalog if t['name'] == n],
            'local_first': 'medina_harness.py extract : cache SHA-256, lignes bornées, journal JSON',
            'clinical_rule': 'Ne jamais compresser les doses, unités, négations, populations, exceptions ni preuves médicales.',
            'installed_claim': 'Catalogue disponible; les 20 bibliothèques externes ne sont pas déclarées installées.',
            'cost_target': '15 % maximum de surcoût outillage mesuré; inconnu si fournisseur sans usage.'}

if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('task'); a = p.parse_args()
    print(json.dumps(suggest(a.task), ensure_ascii=False, indent=2))
