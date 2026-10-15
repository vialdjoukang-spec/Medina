import functools
import base64
import hashlib
import re
import http.server
import json
import os
from pathlib import Path
import runpy
import sys
import threading
from urllib.parse import quote, unquote, urlsplit

from playwright.sync_api import Page

root = Path(os.environ['A41_CONTROL_ROOT']).resolve()
output = Path(os.environ['A41_CONTROL_OUT']).resolve()
reports = Path(os.environ['A41_CONTROL_REPORTS']).resolve()
blocked = []
page_errors = []
observed_pages = set()
assets = {}
served_assets = []


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        relative = unquote(urlsplit(self.path).path).lstrip('/')
        if not (output / relative).is_file() and relative in assets:
            asset = assets[relative]
            self.send_response(200); self.send_header('Content-Type', asset['type']); self.end_headers(); self.wfile.write(asset['data'])
            served_assets.append({'request':relative,'key':asset['key'],'sha256':asset['sha256']})
            return
        return super().do_GET()
    def log_message(self, *args):
        pass


server = http.server.ThreadingHTTPServer(
    ('127.0.0.1', 0), functools.partial(QuietHandler, directory=str(output))
)
threading.Thread(target=server.serve_forever, daemon=True).start()
origin = 'http://127.0.0.1:' + str(server.server_port)
original_goto = Page.goto
isolated = set()


def local_goto(self, value, *args, **kwargs):
    if self not in observed_pages:
        self.on("pageerror", lambda error: page_errors.append(str(error)))
        observed_pages.add(self)
    if self.context not in isolated:
        def route_request(route):
            url = route.request.url
            if url.startswith(origin + '/'):
                return route.continue_()
            blocked.append(url)
            return route.abort()
        self.context.route('http://**/*', route_request)
        self.context.route('https://**/*', route_request)
        isolated.add(self.context)
    parsed = urlsplit(value)
    if parsed.scheme == 'file':
        file = Path(unquote(parsed.path)).resolve()
        relative = file.relative_to(output)
        match = re.search(r'<script\b[^>]*id="medina-portable-resources"[^>]*>(.*?)</script>',file.read_text(),re.S)
        if match:
            for key,record in json.loads(match.group(1)).items():
                data=base64.b64decode(record['base64'],validate=True)
                assert hashlib.sha256(data).hexdigest()==record['sha256']
                for name in [key,Path(key).name]:
                    asset_path=(file.parent/name).relative_to(output).as_posix()
                    assets[asset_path]={'data':data,'type':record['type'],'sha256':record['sha256'],'key':key}
        value = origin + '/' + quote(relative.as_posix(), safe='/')
        if parsed.query:
            value += '?' + parsed.query
        if parsed.fragment:
            value += '#' + parsed.fragment
    return original_goto(self, value, *args, **kwargs)


Page.goto = local_goto
sys.argv = [str(root / 'test_v7.py'), 'A41']
try:
    runpy.run_path(str(root / 'test_v7.py'), run_name='__main__')
finally:
    server.shutdown()
    server.server_close()
    (reports / 'global-network.json').write_text(json.dumps({
        'transport': 'HTTP loopback, file URLs mapped without changing assertions',
        'external_network_blocked': True,
        'external_requests_aborted': blocked,
        'all_page_errors': page_errors,
        'embedded_assets_served': served_assets,
    }, indent=2) + '\n')

if page_errors:
    raise AssertionError("Strict independent pageerrors: " + repr(page_errors))
