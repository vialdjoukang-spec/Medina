"""Usage: cget.py CODE fname.gif 'File:...' [colors] — télécharge via images.commons et affiche la description Commons."""
import sys, json, re, urllib.parse
import images
code, fname, title = sys.argv[1:4]; colors = int(sys.argv[4]) if len(sys.argv) > 4 else 96
api = 'https://commons.wikimedia.org/w/api.php?action=query&format=json&prop=imageinfo&iiprop=extmetadata&titles=' + urllib.parse.quote(title)
md = next(iter(json.loads(images._get(api))['query']['pages'].values()))['imageinfo'][0]['extmetadata']
print('DESC:', re.sub(r'<[^>]+>', '', md.get('ImageDescription', {}).get('value', ''))[:500])
r = images.commons(code, title, fname, colors=colors); print(json.dumps(r, ensure_ascii=False))
