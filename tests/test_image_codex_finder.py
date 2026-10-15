import datetime as dt
import email.utils
import json
import multiprocessing
import sqlite3
import tempfile
import threading
import time
import unittest
from pathlib import Path
from unittest.mock import patch
try:
    import tools.image_codex_finder as finder_module
except ModuleNotFoundError:
    import image_codex_finder as finder_module
Finder, FinderError, Response = finder_module.Finder, finder_module.FinderError, finder_module.Response
broker_search, classify, retry_after, serve = finder_module.broker_search, finder_module.classify, finder_module.retry_after, finder_module.serve


def good():
    return Response(200, {'Content-Type': 'application/json'}, json.dumps({'query': {'pages': {'1': {
        'title': 'File:Specimen.jpg', 'imageinfo': [{'mime': 'image/jpeg', 'url': 'https://upload.wikimedia.org/specimen.jpg',
        'descriptionurl': 'https://commons.wikimedia.org/wiki/File:Specimen.jpg', 'extmetadata': {
        'Artist': {'value': 'Author'}, 'LicenseShortName': {'value': 'CC BY-SA 4.0'}}}]}}}}).encode())


def process_query(database, counter, gate):
    def http(url):
        with counter.get_lock():
            counter.value += 1
        time.sleep(.15)
        return good()
    gate.wait()
    Finder(database, http=http).search('same query')


def process_distinct(database, query, events, gate):
    def http(url):
        events.put(('start', time.monotonic()))
        time.sleep(.15)
        events.put(('end', time.monotonic()))
        return good()
    gate.wait()
    Finder(database, http=http).search(query)


def crash_lock(database, ready):
    def http(url):
        ready.set()
        time.sleep(30)
        return good()
    Finder(database, http=http).search('killed-during-http')


class FinderTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.database = str(Path(self.temp.name)/'shared.sqlite3')

    def test_cross_process_singleflight(self):
        Finder(self.database)
        ctx = multiprocessing.get_context('fork')
        count, gate = ctx.Value('i', 0), ctx.Event()
        processes = [ctx.Process(target=process_query, args=(self.database, count, gate)) for _ in range(4)]
        for process in processes:
            process.start()
        gate.set()
        for process in processes:
            process.join(10)
            self.assertEqual(process.exitcode, 0)
        self.assertEqual(count.value, 1)

    def test_distinct_queries_serialized_with_spacing_after_completion(self):
        events, lock = [], threading.Lock()
        def http(url):
            with lock:
                events.append(('start', time.monotonic()))
            time.sleep(.15)
            with lock:
                events.append(('end', time.monotonic()))
            return good()
        finders = [Finder(self.database, http=http) for _ in range(2)]
        threads = [threading.Thread(target=f.search, args=(str(i),)) for i,f in enumerate(finders)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        self.assertEqual([e[0] for e in events], ['start','end','start','end'])
        self.assertGreaterEqual(events[2][1]-events[1][1], .99)

    def test_process_serialization_and_crash_recovery(self):
        Finder(self.database)
        ctx = multiprocessing.get_context('fork')
        events, gate = ctx.Queue(), ctx.Event()
        processes = [ctx.Process(target=process_distinct, args=(self.database, str(i), events, gate)) for i in range(2)]
        for process in processes:
            process.start()
        gate.set()
        for process in processes:
            process.join(10)
            self.assertEqual(process.exitcode, 0)
        timeline = [events.get(timeout=1) for _ in range(4)]
        self.assertEqual([e[0] for e in timeline], ['start','end','start','end'])
        self.assertGreaterEqual(timeline[2][1]-timeline[1][1], .99)
        with sqlite3.connect(self.database) as db:
            db.execute('UPDATE provider SET next=0')
        ready = ctx.Event()
        crashed = ctx.Process(target=crash_lock, args=(self.database, ready))
        crashed.start()
        self.assertTrue(ready.wait(3))
        with sqlite3.connect(self.database) as db:
            reserved_until = db.execute('SELECT next FROM provider').fetchone()[0]
            self.assertGreater(reserved_until, time.time())
        crashed.kill()
        crashed.join(3)
        # OS locks recover immediately; persisted pre-dispatch spacing still applies.
        starts = []
        Finder(self.database, http=lambda _: (starts.append(time.time()), good())[1]).search('after-crash')
        self.assertGreaterEqual(starts[0], reserved_until)

    def test_429_persistent_and_no_retry(self):
        calls = []
        def limited(url):
            calls.append(url)
            return Response(429, {'Retry-After': '3600'}, b'')
        with self.assertRaises(FinderError):
            Finder(self.database, http=limited).search('one')
        with self.assertRaisesRegex(FinderError, 'cooldown'):
            Finder(self.database, http=limited).search('two')
        self.assertEqual(len(calls), 1)
        with sqlite3.connect(self.database) as db:
            self.assertGreater(db.execute('SELECT cooldown FROM provider').fetchone()[0], time.time()+3590)
        now = time.time()
        date = email.utils.format_datetime(dt.datetime.fromtimestamp(now+120, dt.timezone.utc), usegmt=True)
        self.assertGreater(retry_after({'Retry-After': date}, now), 118)

    def test_daily_budget_persistent(self):
        Finder(self.database, http=lambda _: good(), daily_budget=1).search('one')
        with self.assertRaisesRegex(FinderError, 'budget'):
            Finder(self.database, http=lambda _: self.fail('HTTP must not run'), daily_budget=1000).search('two')

    def test_html_and_circuit_and_maxlag(self):
        finder = Finder(self.database, http=lambda _: Response(200, {'Content-Type':'text/html'}, b'<html>down</html>'))
        for i in range(3):
            with self.assertRaisesRegex(FinderError, 'invalid'):
                finder.search(str(i))
        with self.assertRaisesRegex(FinderError, 'cooldown'):
            finder.search('four')
        with sqlite3.connect(self.database) as db:
            self.assertEqual(db.execute('SELECT count(*) FROM cache').fetchone()[0], 0)

    def test_maxlag_503_and_bounded_responses(self):
        for response in (
            Response(503, {'Retry-After':'120'}, b''),
            Response(200, {'Content-Type':'application/json'}, b'{"error":{"code":"maxlag"}}'),
        ):
            with self.subTest(status=response.status):
                path = str(Path(self.temp.name)/('edge'+str(response.status)+'.sqlite3'))
                finder = Finder(path, http=lambda _, r=response: r)
                with self.assertRaises(FinderError):
                    finder.search('edge')
                with self.assertRaisesRegex(FinderError, 'cooldown'):
                    Finder(path, http=lambda _: self.fail('must not call HTTP')).search('other')
        finder = Finder(self.database, http=lambda _: Response(200, {'Content-Type':'application/json'}, b' '* (2*1024*1024+1)))
        with self.assertRaises(FinderError):
            finder.search('oversize')

    def test_broker_failure_never_falls_back(self):
        with patch.object(finder_module, 'transport', return_value=Response(503, {}, b'')) as http:
            with self.assertRaisesRegex(FinderError, 'fallback is disabled'):
                broker_search('http://127.0.0.1:8765', 'query', 'commons', 8)
            self.assertEqual(http.call_count, 1)

    def test_rights_and_ai(self):
        base = dict(author='Author', source_statement='Own work', source_page='page', original_url='original', license='CC BY 4.0', license_url='https://creativecommons.org/licenses/by/4.0/')
        self.assertEqual(classify(base)['status'], 'RIGHTS_CANDIDATE')
        self.assertFalse(classify(base)['publication_ready'])
        self.assertEqual(classify(dict(base, license_url='https://fake.example/by/4.0'))['status'], 'NEEDS_REVIEW')
        self.assertEqual(classify(dict(base, source_statement=''))['status'], 'NEEDS_REVIEW')
        for name in ('CC BY-NC 4.0', 'CC BY-ND 4.0'):
            self.assertEqual(classify(dict(base, license=name))['status'], 'REJECTED_LICENSE')
        for marker in ('AI-generated image', 'Midjourney', 'Images generated by artificial intelligence'):
            self.assertEqual(classify(dict(base, description=marker))['status'], 'REJECTED_AI')
        self.assertEqual(classify(dict(base, author=''))['status'], 'NEEDS_REVIEW')
        self.assertEqual(classify(dict(base, license='CC BY 4.0 extra unknown terms'))['status'], 'NEEDS_REVIEW')

    def test_broker_reuses_shared_cache_and_refuses_arbitrary_url(self):
        calls=[]
        finder=Finder(self.database, http=lambda url: (calls.append(url), good())[1])
        server=serve(finder, port=0)
        thread=threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        address='http://127.0.0.1:'+str(server.server_port)
        refused = finder_module.transport(address+'/search?q=driveby')
        self.assertEqual(refused.status, 400)
        self.assertEqual(calls, [])
        self.assertEqual(broker_search(address, 'same', 'commons', 8), broker_search(address, 'same', 'commons', 8))
        self.assertEqual(len(calls), 1)
        with self.assertRaises(FinderError):
            broker_search('https://example.org', 'same', 'commons', 8)
        with self.assertRaises(FinderError):
            serve(finder, host='0.0.0.0', port=0)

    def test_article_discovery_and_negative_cache(self):
        calls=[]
        def http(url):
            calls.append(url)
            return Response(200, {'Content-Type':'application/json'}, b'{"resultList":{"result":[]}}')
        finder=Finder(self.database, http=http)
        finder.search('no results','europepmc')
        finder.search('  NO   RESULTS  ','europepmc')
        self.assertEqual(len(calls),1)
        article=finder._articles({'resultList':{'result':[{'id':'123','isOpenAccess':'Y'}]}})[0]
        self.assertFalse(article['figure_license_approved'])
        self.assertFalse(article['publication_ready'])

if __name__ == '__main__':
    unittest.main()


class CampaignStopTests(unittest.TestCase):
    def test_disabled_missing_or_malformed_control_never_calls_http(self):
        with tempfile.TemporaryDirectory() as tmp:
            control = Path(tmp) / 'control.json'
            calls = []
            instance = Finder(Path(tmp) / 'cache.sqlite3', http=lambda url: calls.append(url), campaign_state=control)
            for raw in (None, b'{broken', b'[]', b'{"schema_version":1,"image_execution_enabled":false}'):
                if raw is not None:
                    control.write_bytes(raw)
                with self.assertRaises(FinderError):
                    instance.search('renal anatomy')
            self.assertEqual(calls, [])

    def test_stop_switch_blocks_even_already_cached_results(self):
        with tempfile.TemporaryDirectory() as tmp:
            control = Path(tmp) / 'control.json'
            control.write_text('{"schema_version":1,"image_execution_enabled":true}')
            calls = []
            def http(url):
                calls.append(url)
                return good()
            instance = Finder(Path(tmp) / 'cache.sqlite3', http=http, campaign_state=control)
            instance.search('renal anatomy')
            self.assertEqual(len(calls), 1)
            control.write_text('{"schema_version":1,"image_execution_enabled":false}')
            with self.assertRaises(FinderError):
                instance.search('renal anatomy')
            self.assertEqual(len(calls), 1)
