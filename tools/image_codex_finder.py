#!/usr/bin/env python3
"""Source-polite metadata discovery; never downloads or imports an image."""
import argparse
import contextlib
import fcntl
import datetime as dt
import email.utils
import hashlib
import html
import json
import os
import re
import sqlite3
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ENDPOINTS = {'commons': 'https://commons.wikimedia.org/w/api.php',
             'europepmc': 'https://www.ebi.ac.uk/europepmc/webservices/rest/search'}
MAX_BYTES = 2 * 1024 * 1024
USER_AGENT = 'Image_Codex_Finder/1.0 (MEDINA; https://github.com/vialdjoukang-spec/Medina)'

class FinderError(Exception):
    pass

class SourceCooldownError(FinderError):
    pass

@dataclass
class Response:
    status: int
    headers: dict
    body: bytes

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

def transport(url, extra_headers=None):
    opener = urllib.request.build_opener(NoRedirect)
    request = urllib.request.Request(url, headers={'User-Agent': USER_AGENT, 'Accept': 'application/json', **(extra_headers or {})})
    try:
        result = opener.open(request, timeout=12)
    except urllib.error.HTTPError as exc:
        result = exc
    with result:
        chunks, size, deadline = [], 0, time.monotonic()+12
        while True:
            chunk = result.read1(min(65536, MAX_BYTES+1-size))
            size += len(chunk)
            if size > MAX_BYTES:
                raise FinderError('Response exceeds 2 MiB')
            if time.monotonic() > deadline:
                raise FinderError('Response time bound exceeded')
            if not chunk:
                break
            chunks.append(chunk)
        body = b''.join(chunks)
        return Response(result.code, dict(result.headers), body)

def plain(value):
    return html.unescape(re.sub('<[^>]*>', '', str(value or ''))).strip()

def retry_after(headers, now):
    value = next((str(v) for k, v in headers.items() if k.lower() == 'retry-after'), '')
    try:
        return max(0, float(value))
    except ValueError:
        try:
            return max(0, email.utils.parsedate_to_datetime(value).timestamp() - now)
        except (ValueError, TypeError, OverflowError):
            return 60

def classify(metadata):
    """Conservative rights/provenance screening, never clinical or publication approval."""
    values = ' '.join(str(v) for v in metadata.values())
    ai = bool(re.search(r'AI[ _-]?(generated|art|assisted)|generat(?:ed|ive)[ _-]AI|artificial intelligence|'
                        r'midjourney|dall[ -]?e|stable[ _-]diffusion|computer.generated.*AI', values, re.I))
    license_name = metadata.get('license', '').strip()
    refused = bool(re.search(r'\b(nc|nd)\b|noncommercial|non-commercial|no derivatives', license_name, re.I))
    allowed = bool(re.fullmatch(r'(?:CC[ -]?BY(?:[ -]SA)?(?:[ -]\d(?:\.\d)?)?|CC0(?:[ -]1\.0)?|'
                               r'Public domain|PD)', license_name, re.I)) and not refused
    license_url = metadata.get('license_url', '').strip().rstrip('/')
    # Exact recognized URL and name must agree; unknown/extra terms require review.
    match = re.fullmatch(r'https?://creativecommons.org/(licenses/(by|by-sa)/(1\.0|2\.0|2\.5|3\.0|4\.0)|publicdomain/(zero|mark)/1\.0)', license_url, re.I)
    normalized = re.sub(r'[ -]+', ' ', license_name.lower()).strip()
    url_matches = False
    if match:
        if match.group(2):
            url_matches = normalized == ('cc '+match.group(2).replace('-', ' ')+' '+match.group(3)).lower()
        elif match.group(4).lower() == 'zero':
            url_matches = normalized in ('cc0', 'cc0 1.0')
        else:
            url_matches = normalized in ('public domain', 'pd')
    allowed = allowed and url_matches
    provenance = bool(metadata.get('author') and metadata.get('source_statement') and metadata.get('source_page') and metadata.get('original_url'))
    status = 'REJECTED_AI' if ai else ('REJECTED_LICENSE' if refused else
             ('RIGHTS_CANDIDATE' if allowed and provenance else 'NEEDS_REVIEW'))
    return {'status': status, 'ai_marked': ai, 'rights_candidate': status == 'RIGHTS_CANDIDATE',
            'publication_ready': False, 'medical_approval': False,
            'required_review': ['original source and figure-specific rights', 'visual and medical review',
                                'attribution and any personality/privacy restrictions'],
            'ai_detection_limit': 'Metadata markers only; absence does not prove human origin.'}

class Finder:
    def __init__(self, database, http=transport, interval=1.0, daily_budget=100):
        if interval < 1 or daily_budget < 1:
            raise ValueError('interval >= 1 second and daily_budget >= 1 required')
        self.database, self.http = str(database), http
        self.interval, self.daily_budget = interval, daily_budget
        Path(self.database).parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as db:
            db.executescript('''
            CREATE TABLE IF NOT EXISTS policy(k TEXT PRIMARY KEY, value INTEGER);
            CREATE TABLE IF NOT EXISTS cache(k TEXT PRIMARY KEY, expires REAL, payload TEXT);
            CREATE TABLE IF NOT EXISTS provider(name TEXT PRIMARY KEY, next REAL DEFAULT 0,
              cooldown REAL DEFAULT 0, failures INTEGER DEFAULT 0);
            CREATE TABLE IF NOT EXISTS budget(provider TEXT, day TEXT, used INTEGER,
              PRIMARY KEY(provider,day));
            ''')
            db.execute("INSERT INTO policy VALUES('daily_budget',?) ON CONFLICT(k) DO UPDATE SET value=min(value,excluded.value)", (daily_budget,))
    def connect(self):
        return sqlite3.connect(self.database, timeout=15)
    def search(self, query, provider='commons', limit=8):
        query = ' '.join(str(query).split())
        if provider not in ENDPOINTS or not query or len(query) > 300 or not 1 <= limit <= 20:
            raise FinderError('Invalid provider, query (1–300 characters) or limit (1–20)')
        key = hashlib.sha256(json.dumps([provider, query.casefold(), limit]).encode()).hexdigest()
        with self._file_lock('query-'+key):
            with self.connect() as db:
                row = db.execute('SELECT payload FROM cache WHERE k=? AND expires>?', (key, time.time())).fetchone()
            if row:
                return json.loads(row[0])
            result = self._fetch(query, provider, limit)
            with self.connect() as db:
                db.execute('INSERT OR REPLACE INTO cache VALUES(?,?,?)',
                           (key, time.time() + (30*86400 if result['results'] else 3600), json.dumps(result)))
            return result
    @contextlib.contextmanager
    def _file_lock(self, key):
        # OS releases flock after SIGKILL. Do not unlink lock identities.
        directory = Path(self.database).resolve().with_suffix(Path(self.database).suffix+'.locks')
        directory.mkdir(parents=True, exist_ok=True)
        deadline = time.monotonic()+35
        with (directory/key).open('a') as lock:
            while True:
                try:
                    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
                    break
                except BlockingIOError:
                    if time.monotonic() >= deadline:
                        raise FinderError('Shared request busy; try later')
                    time.sleep(.05)
            try:
                yield
            finally:
                fcntl.flock(lock, fcntl.LOCK_UN)
    def _reserve(self, provider):
        deadline = time.monotonic() + 20
        while True:
            now = time.time()
            day = dt.datetime.fromtimestamp(now, dt.timezone.utc).date().isoformat()
            with self.connect() as db:
                db.execute('BEGIN IMMEDIATE')
                db.execute('INSERT OR IGNORE INTO provider(name) VALUES(?)', (provider,))
                next_at, cooldown = db.execute('SELECT next,cooldown FROM provider WHERE name=?', (provider,)).fetchone()
                if cooldown > now:
                    raise FinderError(f'{provider}: persistent cooldown until {dt.datetime.fromtimestamp(cooldown, dt.timezone.utc).isoformat()}')
                used = db.execute('SELECT used FROM budget WHERE provider=? AND day=?', (provider, day)).fetchone()
                budget = db.execute("SELECT value FROM policy WHERE k='daily_budget'").fetchone()[0]
                if used and used[0] >= budget:
                    raise FinderError(f'{provider}: daily request budget exhausted')
                if next_at <= now:
                    db.execute('UPDATE provider SET next=? WHERE name=?', (now+self.interval, provider))
                    db.execute('INSERT INTO budget VALUES(?,?,1) ON CONFLICT(provider,day) DO UPDATE SET used=used+1', (provider, day))
                    return
            if time.monotonic() >= deadline:
                raise FinderError('Provider queue busy; try later')
            time.sleep(.05)
    def _failure(self, provider, seconds=None):
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            failures = db.execute('SELECT failures FROM provider WHERE name=?', (provider,)).fetchone()[0]+1
            delay = max(seconds or 0, 600 if failures >= 3 else 0)
            until = time.time() + delay
            db.execute('UPDATE provider SET failures=?,cooldown=max(cooldown,?) WHERE name=?', (failures, until, provider))
    def _fetch(self, query, provider, limit):
        with self._file_lock('provider-'+provider):
            self._reserve(provider)
            try:
                return self._request(query, provider, limit)
            finally:
                with self.connect() as db:
                    db.execute('UPDATE provider SET next=max(next,?) WHERE name=?', (time.time()+self.interval, provider))
    def _request(self, query, provider, limit):
        if provider == 'commons':
            params = dict(action='query', format='json', generator='search', gsrsearch=query,
                          gsrnamespace=6, gsrlimit=limit, prop='imageinfo',
                          iiprop='url|extmetadata|size|mime', maxlag=5)
        else:
            params = dict(query=query, format='json', pageSize=limit, resultType='core')
        try:
            response = self.http(ENDPOINTS[provider]+'?'+urllib.parse.urlencode(params))
            if response.status in (429, 503):
                self._failure(provider, max(1, retry_after(response.headers, time.time())))
                raise SourceCooldownError(f'{provider}: HTTP {response.status}; cooldown stored, no retry')
            if response.status != 200:
                raise ValueError(f'HTTP {response.status}')
            if len(response.body) > MAX_BYTES:
                raise ValueError('Response exceeds 2 MiB')
            content_type = next((v for k,v in response.headers.items() if k.lower() == 'content-type'), '')
            if 'json' not in content_type.lower():
                raise ValueError('Expected JSON content type')
            data = json.loads(response.body)
            if not isinstance(data, dict):
                raise ValueError('Expected JSON object')
            if data.get('error'):
                if data['error'].get('code') == 'maxlag':
                    self._failure(provider, max(5, retry_after(response.headers, time.time())))
                    raise SourceCooldownError('Commons maxlag; cooldown stored, no retry')
                raise ValueError('Source API error')
            results = self._commons(data) if provider == 'commons' else self._articles(data)
        except SourceCooldownError:
            raise
        except Exception as exc:
            self._failure(provider)
            raise FinderError(f'{provider}: invalid or failed source response ({type(exc).__name__})') from exc
        with self.connect() as db:
            db.execute('UPDATE provider SET failures=0 WHERE name=?', (provider,))
        return dict(schema_version=1, provider=provider, query=query,
                    retrieved_at=dt.datetime.now(dt.timezone.utc).isoformat(), results=results,
                    publication_ready=False, automatic_import=False)
    @staticmethod
    def _commons(data):
        result = []
        for page in data.get('query', {}).get('pages', {}).values():
            for info in page.get('imageinfo', [])[:1]:
                if not info.get('mime', '').startswith('image/'):
                    continue
                meta = info.get('extmetadata', {})
                get = lambda key: plain(meta.get(key, {}).get('value'))
                item = dict(kind='image_metadata', title=page.get('title'), source_page=info.get('descriptionurl'),
                            original_url=info.get('url'), mime=info.get('mime'),
                            author=get('Artist'), credit=get('Credit'), license=get('LicenseShortName'),
                            license_url=get('LicenseUrl'), description=get('ImageDescription'),
                            source_statement=get('Source'), categories=get('Categories'),
                            metadata_evidence=meta)
                item.update(classify(item))
                result.append(item)
        return result
    @staticmethod
    def _articles(data):
        return [dict(kind='article_discovery', title=row.get('title'), author=row.get('authorString'),
                     pmcid=row.get('pmcid'), doi=row.get('doi'), source_id=row.get('id'),
                     source_page='https://europepmc.org/article/'+urllib.parse.quote(str(row.get('source', 'MED')), safe='')+'/'+urllib.parse.quote(str(row.get('id', '')), safe=''),
                     open_access_claim=row.get('isOpenAccess'), status='NEEDS_REVIEW',
                     figure_license_approved=False, publication_ready=False, medical_approval=False,
                     notice='Article discovery only. Article OA status does not approve any figure; inspect original figure credit and rights.')
                for row in data.get('resultList', {}).get('result', [])]

def broker_search(address, query, provider, limit):
    parsed = urllib.parse.urlsplit(address)
    if parsed.scheme != 'http' or parsed.hostname not in ('127.0.0.1', '::1') or parsed.username or parsed.password or parsed.path not in ('', '/') or parsed.query or parsed.fragment:
        raise FinderError('Broker must be an HTTP literal loopback origin')
    response = transport(address.rstrip('/')+'/search?'+urllib.parse.urlencode(dict(q=query, provider=provider, limit=limit)),
                         extra_headers={'X-Medina-Client': 'Image_Codex_Finder/1.0'})
    if response.status != 200:
        raise FinderError('Broker failed; direct fallback is disabled')
    return json.loads(response.body)

def serve(finder, host='127.0.0.1', port=8765):
    if host != '127.0.0.1':
        raise FinderError('Only 127.0.0.1 binding supported until authenticated TLS infrastructure exists')
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed = urllib.parse.urlsplit(self.path)
            try:
                if self.headers.get('X-Medina-Client') != 'Image_Codex_Finder/1.0':
                    raise FinderError('Required non-simple client header missing')
                expected_host = '127.0.0.1:'+str(self.server.server_port)
                if self.headers.get('Host') != expected_host or self.headers.get('Origin') not in (None, 'http://'+expected_host):
                    raise FinderError('Only same-origin loopback clients allowed')
                if len(self.path) > 2048:
                    raise FinderError('Request URI too long')
                if parsed.path != '/search':
                    raise FinderError('Only /search supported')
                values = urllib.parse.parse_qs(parsed.query, strict_parsing=True)
                if set(values) - {'q', 'provider', 'limit'} or any(len(v) != 1 for v in values.values()):
                    raise FinderError('Invalid query parameters')
                result = finder.search(values.get('q', [''])[0], values.get('provider', ['commons'])[0], int(values.get('limit', ['8'])[0]))
                code = 200
            except (FinderError, ValueError) as exc:
                result, code = {'error': str(exc)}, 400
            payload = json.dumps(result, ensure_ascii=False).encode()
            self.send_response(code)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Content-Length', str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
        def log_message(self, *args):
            pass
    server = ThreadingHTTPServer((host, port), Handler)
    return server

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cache', default=os.path.expanduser('~/.cache/image_codex_finder/shared.sqlite3'))
    parser.add_argument('--daily-budget', type=int, default=100)
    commands = parser.add_subparsers(dest='command', required=True)
    search = commands.add_parser('search')
    search.add_argument('query')
    search.add_argument('--provider', choices=list(ENDPOINTS), default='commons')
    search.add_argument('--limit', type=int, default=8)
    mode = search.add_mutually_exclusive_group(required=True)
    mode.add_argument('--broker')
    mode.add_argument('--direct', action='store_true', help='Use the shared SQLite cache directly')
    server = commands.add_parser('serve')
    server.add_argument('--host', default='127.0.0.1')
    server.add_argument('--port', type=int, default=8765)
    args = parser.parse_args()
    try:
        if args.command == 'search' and args.broker:
            result = broker_search(args.broker, args.query, args.provider, args.limit)
        else:
            finder = Finder(args.cache, daily_budget=args.daily_budget)
            if args.command == 'serve':
                serve(finder, args.host, args.port).serve_forever()
                return
            result = finder.search(args.query, args.provider, args.limit)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (FinderError, OSError, ValueError) as exc:
        parser.exit(1, str(exc)+'\n')

if __name__ == '__main__':
    main()
