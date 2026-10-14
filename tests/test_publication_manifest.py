import unittest
from copy import deepcopy
from datetime import datetime, timezone
from tools.publication_manifest import bounded_deadline, check_deadline


class PublicationDeadlineTests(unittest.TestCase):
    registry = {'deadline':'2026-10-14T06:00:00+00:00', 'cycles':[{'cycle':2,'chapters':[{'code':'G45'}]}]}

    def test_actual_injection_is_bounded(self):
        for path in ('chapters/G45/G45_a.html','glossary/g45.py','assets/img/cycle2/g45/figure.gif'):
            self.assertEqual(bounded_deadline(self.registry,[path]),self.registry['deadline'])

    def test_drafts_and_unrelated_later_work_are_not_injections(self):
        for path in ('livraisons/Livraison Codex/N-05-Neurologie/travail/CYCLE_02_G45/chapters/G45/G45_a.html',
                     'chapters/I63/I63_a.html','organisation/execution-20261014/status.json','tools/night_cycle.py'):
            self.assertIsNone(bounded_deadline(self.registry,[path]))

    def test_actual_clock_refuses_boundary_and_later_publication(self):
        check_deadline(self.registry['deadline'], datetime(2026,10,14,5,59,59,tzinfo=timezone.utc))
        for now in (datetime(2026,10,14,6,tzinfo=timezone.utc),datetime(2026,10,15,tzinfo=timezone.utc)):
            with self.assertRaisesRegex(ValueError,'expirée'):
                check_deadline(self.registry['deadline'],now)

    def test_absent_registry_has_no_night_scope(self):
        self.assertIsNone(bounded_deadline(None,['chapters/G45/G45_a.html']))

    def test_catalog_only_new_integration_is_bounded(self):
        current = [{'code':'G45','integrated':True},{'code':'I63','integrated':True}]
        for previous in ([],[{'code':'G45','integrated':False}]):
            self.assertEqual(bounded_deadline(self.registry,['chapters.json'],catalog=current,previous_catalog=previous),self.registry['deadline'])
        self.assertIsNone(bounded_deadline(self.registry,['chapters.json'],catalog=current,previous_catalog=[{'code':'G45','integrated':True}]))

    def test_receipt_transition_is_bounded_but_publication_receipt_is_not(self):
        current = deepcopy(self.registry)
        current['cycles'][0]['chapters'][0]['injection'] = {'path':'receipt.json','sha256':'a'*64}
        path = 'organisation/execution-20261014/cycles.json'
        self.assertEqual(bounded_deadline(current,[path],self.registry),self.registry['deadline'])
        next_state = deepcopy(current)
        next_state['cycles'][0]['chapters'][0]['publication'] = {'path':'publication-receipt.json','sha256':'b'*64}
        self.assertIsNone(bounded_deadline(next_state,[path],current))


if __name__ == '__main__':
    unittest.main()
