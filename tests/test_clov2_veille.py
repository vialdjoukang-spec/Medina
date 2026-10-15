"""Fixtures entièrement locales : aucune commande git ni requête réseau réelle."""
import copy
from datetime import datetime, timedelta, timezone
import importlib.util
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import urllib.error
import urllib.parse

spec = importlib.util.spec_from_file_location('clov2_veille', Path(__file__).resolve().parents[1] / 'tools/clov2_veille.py')
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)

NOW = datetime(2026, 10, 15, 12, 0, tzinfo=timezone.utc)
AT = '2026-10-15T12:00:00Z'
BEFORE = '2026-10-15T11:59:00Z'
SHA = 'a' * 40
OLD_SHA = 'b' * 40


def comment(number, body='Recommandation technique', at=AT):
    return {'id': number, 'body': body, 'updated_at': at, 'created_at': at,
            'html_url': f'https://github.com/example/Medina/issues/97#issuecomment-{number}'}


def pr(number, at=AT, title='Proposition'):
    return {'number': number, 'updated_at': at, 'title': title, 'state': 'open',
            'head': {'ref': f'codex/proposition-{number}', 'sha': SHA}, 'draft': False, 'body': 'Description'}


class ApiFixture:
    def __init__(self, prs=(), comments=(), failure=None):
        self.items = {'pulls': list(prs), 'issues/comments': list(comments)}
        self.failure = failure
        self.calls = []

    def __call__(self, path):
        endpoint, _, query = path.partition('?')
        params = dict(urllib.parse.parse_qsl(query))
        page, size = int(params['page']), int(params['per_page'])
        self.calls.append((endpoint, page, params))
        if self.failure == (endpoint, page):
            raise m.VeilleError('API indisponible : HTTP 403 ; curseur conservé')
        return self.items[endpoint][(page - 1) * size:page * size]


class GitFixture:
    def __init__(self, refs=(), log='', failure=None):
        self.refs, self.log, self.failure = list(refs), log, failure
        self.calls = []

    def __call__(self, *args):
        self.calls.append(args)
        if self.failure == args[0]:
            raise m.VeilleError(f'Git {args[0]} a échoué (code 128)')
        if args[0] == 'fetch':
            return ''
        if args[0] == 'for-each-ref':
            return '\n'.join(self.refs)
        if args[0] == 'rev-parse':
            return SHA + '\n'
        if args[0] == 'log':
            return self.log
        raise AssertionError(f'Commande inattendue : {args[0]}')


def prior_state():
    state = m.new_state()
    for source in state['sources'].values():
        source['since'] = BEFORE
    state['sources']['main']['head'] = OLD_SHA
    return state


class TestVeille(unittest.TestCase):
    def scan(self, state, api=None, git=None, **kwargs):
        return m.scan(state, now=kwargs.pop('now', NOW), api_reader=api or ApiFixture(),
                      git_runner=git or GitFixture(), **kwargs)

    def test_first_pass_signals_existing_recommendations(self):
        state = m.new_state()
        result = self.scan(state, ApiFixture(prs=[pr(1)], comments=[comment(1)]),
                           GitFixture(['origin/codex/test'], f'{SHA} Recommandation existante'))
        self.assertFalse(result.errors)
        self.assertEqual(len(result.news), 4)
        self.assertTrue(any('[main]' in entry for entry in result.news))

    def test_baseline_is_explicit_then_deduplicates(self):
        state, api = m.new_state(), ApiFixture(comments=[comment(1)])
        self.assertEqual(self.scan(state, api, baseline=True).news, [])
        self.assertEqual(self.scan(state, api, now=NOW + timedelta(seconds=30)).news, [])

    def test_fetch_failure_preserves_both_git_cursors_but_scans_api(self):
        state = prior_state()
        old_git = copy.deepcopy({k: state['sources'][k] for k in ('codex', 'main')})
        result = self.scan(state, ApiFixture(comments=[comment(1)]), GitFixture(failure='fetch'))
        self.assertEqual(len(result.errors), 1)
        self.assertEqual(len(result.news), 1)
        for source in ('codex', 'main'):
            self.assertEqual(state['sources'][source], old_git[source])
        self.assertEqual(state['sources']['comments']['since'], AT)

    def test_git_log_error_never_advances_branch_head(self):
        state = prior_state()
        original = copy.deepcopy(state['sources']['codex'])
        result = self.scan(state, git=GitFixture(['origin/codex/test'], failure='log'))
        self.assertTrue(any('codex' in error for error in result.errors))
        self.assertEqual(state['sources']['codex'], original)

    def test_comments_page_two_failure_keeps_source_transactional(self):
        state = prior_state()
        original = copy.deepcopy(state['sources']['comments'])
        api = ApiFixture(comments=[comment(n) for n in range(101)], failure=('issues/comments', 2))
        result = self.scan(state, api)
        self.assertEqual(state['sources']['comments'], original)
        self.assertFalse(any('[commentaire' in entry for entry in result.news))
        self.assertTrue(any('HTTP 403' in error for error in result.errors))
        self.assertEqual(state['sources']['prs']['since'], AT)
        # Réessai : les 101 commentaires sont encore disponibles, pas seulement le dernier.
        result = self.scan(state, ApiFixture(comments=[comment(n) for n in range(101)]))
        self.assertEqual(len(result.news), 101)

    def test_pr_page_two_failure_does_not_commit_partial_seen(self):
        state = prior_state()
        original = copy.deepcopy(state['sources']['prs'])
        result = self.scan(state, ApiFixture(prs=[pr(n) for n in range(101)], failure=('pulls', 2)))
        self.assertEqual(state['sources']['prs'], original)
        self.assertFalse(any('[PR' in entry for entry in result.news))
        self.assertTrue(result.errors)

    def test_more_than_100_comments_same_timestamp_and_late_equal_item(self):
        state = m.new_state()
        api = ApiFixture(comments=[comment(n) for n in range(205)])
        result = self.scan(state, api)
        self.assertEqual(len(result.news), 205)
        self.assertEqual([page for endpoint, page, _ in api.calls if endpoint == 'issues/comments'], [1, 2, 3])
        self.assertEqual(self.scan(state, api, now=NOW + timedelta(seconds=5)).news, [])
        api.items['issues/comments'].append(comment(206))
        self.assertEqual(len(self.scan(state, api, now=NOW + timedelta(seconds=10)).news), 1)

    def test_all_pr_pages_are_read(self):
        api = ApiFixture(prs=[pr(n) for n in range(120)])
        result = self.scan(m.new_state(), api)
        self.assertEqual(len(result.news), 120)
        self.assertEqual([page for endpoint, page, _ in api.calls if endpoint == 'pulls'], [1, 2])

    def test_exact_page_size_requests_final_empty_page(self):
        api = ApiFixture(comments=[comment(n) for n in range(100)])
        self.scan(m.new_state(), api)
        self.assertEqual([page for endpoint, page, _ in api.calls if endpoint == 'issues/comments'], [1, 2])

    def test_watermark_is_scan_start_and_query_has_overlap(self):
        state = prior_state()
        future = '2026-10-15T12:00:30Z'
        api = ApiFixture(comments=[comment(1, at=future)])
        self.scan(state, api)
        self.assertEqual(state['sources']['comments']['since'], AT)
        params = [params for endpoint, _, params in api.calls if endpoint == 'issues/comments'][0]
        self.assertEqual(params['since'], '2026-10-15T11:57:00Z')
        self.assertEqual(self.scan(state, api, now=NOW + timedelta(seconds=45)).news, [])

    def test_comment_edit_same_timestamp_is_not_hidden(self):
        state, api = m.new_state(), ApiFixture(comments=[comment(1)])
        self.scan(state, api)
        api.items['issues/comments'][0]['body'] = 'Correction nouvelle'
        self.assertEqual(len(self.scan(state, api).news), 1)

    def test_claude_echo_is_seen_without_notification_and_real_reply_survives(self):
        state = m.new_state()
        api = ApiFixture(comments=[comment(1, 'Generated by [Claude Code]'), comment(2)])
        result = self.scan(state, api)
        self.assertEqual(len(result.news), 1)
        self.assertIn('issuecomment-2', result.news[0])
        self.assertEqual(self.scan(state, api).news, [])
        api.items['issues/comments'][0]['body'] = 'Réponse technique Codex nouvelle'
        self.assertEqual(len(self.scan(state, api).news), 1)

    def test_pr_change_same_timestamp_is_not_hidden(self):
        state, api = m.new_state(), ApiFixture(prs=[pr(1)])
        self.scan(state, api)
        api.items['pulls'][0]['title'] = 'Nouvelle décision'
        self.assertEqual(len(self.scan(state, api).news), 1)

    def test_duplicate_between_pages_is_not_announced_twice(self):
        items = [comment(n) for n in range(100)]
        api = ApiFixture(comments=items + [items[-1], comment(101)])
        self.assertEqual(len(self.scan(m.new_state(), api).news), 101)

    def test_migrates_old_since_and_known_ids_without_losing_unknown(self):
        legacy = {'branches': {'origin/codex/test': SHA}, 'main': SHA,
                  'prs': ['1@' + BEFORE], 'comments': [1], 'since': BEFORE}
        state = m.migrate_state(legacy)
        self.assertEqual(state['sources']['codex']['heads'], legacy['branches'])
        self.assertEqual(state['sources']['main']['head'], SHA)
        result = self.scan(state, ApiFixture(prs=[pr(1, at=BEFORE)],
                           comments=[comment(1, at=BEFORE), comment(2, at=BEFORE)]),
                           GitFixture(['origin/codex/test']))
        self.assertEqual(len(result.news), 1)
        self.assertIn('issuecomment-2', result.news[0])
        self.assertNotIn('legacy_seen', state['sources']['comments'])

    def test_edited_legacy_comment_after_old_since_is_announced(self):
        state = m.migrate_state({'branches': {}, 'prs': [], 'comments': [1], 'since': BEFORE})
        self.assertEqual(len(self.scan(state, ApiFixture(comments=[comment(1)])).news), 1)

    def test_api_403_is_explicit_and_token_never_leaks(self):
        failure = urllib.error.HTTPError('https://api.github.com/', 403, 'secret-token', {}, None)
        with patch.object(m.urllib.request, 'urlopen', side_effect=failure), patch.dict(m.os.environ, {'GH_TOKEN': 'secret-token'}):
            with self.assertRaises(m.VeilleError) as caught:
                m.api('issues/comments?per_page=100')
        self.assertIn('HTTP 403', str(caught.exception))
        self.assertNotIn('secret-token', str(caught.exception))

    def test_auth_uses_standard_environment_only(self):
        for environment, expected in [({'GH_TOKEN': 'gh-token', 'GITHUB_TOKEN': 'fallback'}, 'Bearer gh-token'),
                                      ({'GITHUB_TOKEN': 'fallback'}, 'Bearer fallback'), ({'OTHER_TOKEN': 'ignored'}, None)]:
            response = io.BytesIO(b'[]')
            with patch.dict(m.os.environ, environment, clear=True), patch.object(m.urllib.request, 'urlopen', return_value=response) as opening:
                self.assertEqual(m.api('pulls'), [])
                self.assertEqual(opening.call_args.args[0].get_header('Authorization'), expected)

    def test_invalid_json_is_an_explicit_api_error(self):
        with patch.object(m.urllib.request, 'urlopen', return_value=io.BytesIO(b'{broken')):
            with self.assertRaises(m.VeilleError) as caught:
                m.api('pulls')
        self.assertIn('JSON invalide', str(caught.exception))

    def test_fetch_reads_all_remote_branches_without_push(self):
        git = GitFixture()
        self.scan(m.new_state(), git=git)
        self.assertEqual(git.calls[0], ('fetch', '--quiet', 'origin', '+refs/heads/*:refs/remotes/origin/*'))
        self.assertFalse(any(call[0] == 'push' for call in git.calls))

    def test_git_failure_does_not_expose_stderr_or_stdout(self):
        result = subprocess.CompletedProcess(['git'], 128, 'secret-token', 'https://token@example.invalid')
        with patch.object(m.subprocess, 'run', return_value=result):
            with self.assertRaises(m.VeilleError) as caught:
                m.git('fetch', '--quiet', 'origin')
        self.assertIn('code 128', str(caught.exception))
        self.assertNotIn('secret-token', str(caught.exception))
        self.assertNotIn('token@', str(caught.exception))

    def test_invalid_api_shape_does_not_advance_cursor(self):
        state = prior_state()
        original = copy.deepcopy(state['sources']['prs'])
        result = self.scan(state, lambda path: {} if path.startswith('pulls?') else [])
        self.assertTrue(result.errors)
        self.assertEqual(state['sources']['prs'], original)

    def test_state_roundtrip_is_private_and_atomic(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / 'state.json'
            original = prior_state()
            m.save_state(path, original)
            self.assertEqual(m.load_state(path), original)
            self.assertEqual(path.stat().st_mode & 0o077, 0)
            with patch.object(m.os, 'replace', side_effect=OSError('simulated failure')):
                with self.assertRaises(m.VeilleError):
                    m.save_state(path, m.new_state())
            self.assertEqual(m.load_state(path), original)
            self.assertEqual(list(path.parent.iterdir()), [path])

    def test_corrupt_state_is_never_silently_reset(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / 'state.json'
            # Fixture, not project state or source editing.
            with path.open('w', encoding='utf-8') as stream:
                stream.write('{broken')
            with self.assertRaises(m.VeilleError):
                m.load_state(path)
            self.assertEqual(path.read_text(), '{broken')

    def test_cli_code_three_is_only_a_signal(self):
        with tempfile.TemporaryDirectory() as temporary, patch.object(m, 'STATE', Path(temporary) / 'state.json'), \
                patch.object(m, 'scan', return_value=m.ScanResult(['Recommandation présente'], [])), \
                patch('sys.stdout', new_callable=io.StringIO) as output:
            self.assertEqual(m.main([]), 3)
            self.assertIn('signal au superviseur', output.getvalue())
            self.assertIn('aucune relance automatique', output.getvalue())

    def test_cli_error_is_not_zero_news(self):
        with tempfile.TemporaryDirectory() as temporary, patch.object(m, 'STATE', Path(temporary) / 'state.json'), \
                patch.object(m, 'scan', return_value=m.ScanResult([], ['API HTTP 403'])), \
                patch('sys.stdout', new_callable=io.StringIO) as output, patch('sys.stderr', new_callable=io.StringIO) as error:
            self.assertEqual(m.main([]), 2)
            self.assertNotIn('aucune nouveauté', output.getvalue())
            self.assertIn('HTTP 403', error.getvalue())

    def test_cli_baseline_requires_explicit_option_and_no_previous_state(self):
        with tempfile.TemporaryDirectory() as temporary, patch.object(m, 'STATE', Path(temporary) / 'state.json'), \
                patch.object(m, 'scan', return_value=m.ScanResult([], [])) as scanning, \
                patch('sys.stdout', new_callable=io.StringIO), patch('sys.stderr', new_callable=io.StringIO):
            self.assertEqual(m.main(['--baseline-silencieuse']), 0)
            self.assertTrue(scanning.call_args.kwargs['baseline'])
            with self.assertRaises(SystemExit) as caught:
                m.main(['--baseline-silencieuse'])
            self.assertEqual(caught.exception.code, 2)


if __name__ == '__main__':
    unittest.main()
