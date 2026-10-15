import importlib.util
from pathlib import Path
import unittest
path=Path(__file__).with_name('alpha_publication_pub02.py')
spec=importlib.util.spec_from_file_location('alpha_candidate',path)
alpha=importlib.util.module_from_spec(spec);spec.loader.exec_module(alpha)

class ReachableCourseTests(unittest.TestCase):
    def read(self,body,code='N17'):
        return alpha.reachable_course_text(body.encode(),code)

    def wrap(self,body):return '<template id="ch-N17"><div class="chap">'+body+'</div></template>'

    def tabs(self,body,aria='pS',target='pS',button_attrs='',target_attrs='hidden'):
        return self.wrap(f'<div class="tabs"><button data-p="{target}" aria-controls="{aria}" {button_attrs}>Sciences</button></div><div class="panel" id="pA">Initial</div><div class="panel" id="pS" {target_attrs}>{body}</div>')

    def science(self,body,button_attrs='',target_attrs='hidden',aria=True):
        controls='aria-controls="n17-anat"' if aria else ''
        return self.tabs(f'<div class="sci-bar"><button data-s="n17-anat" {controls} {button_attrs}>Anatomie</button></div><div class="sci" id="n17-anat" {target_attrs}>{body}</div>')

    def test_real_course_template_reservation(self):
        raw=self.wrap('<p>Réserves encore ouvertes.</p>')
        self.assertIn('Réserves encore ouvertes.',self.read(raw))
        self.assertNotIn('Réserves',alpha.visible_text(raw.encode()))

    def test_real_navigation_reaches_hidden_science_and_credit(self):
        raw=self.science('<figure><figcaption>Crédit original vérifié</figcaption></figure>')
        self.assertIn('Crédit original vérifié',self.read(raw))
        self.assertNotIn('Crédit original vérifié',alpha.visible_text(raw.encode()))

    def test_legacy_runtime_button_without_aria_is_supported(self):
        self.assertIn('Crédit',self.read(self.science('<figcaption>Crédit</figcaption>',aria=False)))

    def test_mismatched_or_absent_primary_target_stays_hidden(self):
        for attrs in [dict(aria='foreign'),dict(target='missing')]:
            self.assertNotIn('Secret',self.read(self.tabs('<p>Secret</p>',**attrs)))

    def test_scientific_aria_mismatch_rejected(self):
        raw=self.science('<p>Secret</p>').replace('aria-controls="n17-anat"','aria-controls="other"')
        self.assertNotIn('Secret',self.read(raw))

    def test_duplicate_local_target_is_not_activated(self):
        body=self.science('<p>Secret</p>').replace('</div></template>','<div class="sci" id="n17-anat" hidden>Duplicate</div></div></template>')
        self.assertNotIn('Secret',self.read(body))

    def test_foreign_course_and_nested_templates_are_not_reachable(self):
        self.assertNotIn('Secret',self.read('<template id="ch-I63"><p>Secret</p></template>'))
        for tag in ['template','script','style']:
            self.assertNotIn('Secret',self.read(self.science(f'<{tag}>Secret</{tag}>')))

    def test_explicit_hiding_and_nested_hidden_remain_excluded(self):
        for attrs in ['hidden style="display:none"','hidden style="display: none !important"',
                      'hidden aria-hidden="true"','hidden style="visibility:hidden"']:
            self.assertNotIn('Secret',self.read(self.science('<p>Secret</p>',target_attrs=attrs)))
        for attrs in ['hidden','aria-hidden="true"','style="display:none"']:
            self.assertNotIn('Secret',self.read(self.science(f'<p {attrs}>Secret</p>')))

    def test_hidden_or_disabled_buttons_cannot_activate_targets(self):
        for attrs in ['hidden','disabled','aria-disabled="true"','style="display:none"','inert']:
            self.assertNotIn('Secret',self.read(self.science('<p>Secret</p>',button_attrs=attrs)))

    def test_uncontrolled_science_and_wrong_bar_are_not_activated(self):
        raw=self.science('<p>Secret</p>')
        for value in [raw.replace('class="sci-bar"','class="random"'),raw.replace('data-s="n17-anat"','data-x="n17-anat"')]:
            self.assertNotIn('Secret',self.read(value))

    def test_button_in_inert_template_cannot_activate_target(self):
        raw=self.science('<p>Secret</p>').replace('<div class="sci-bar">','<template><div class="sci-bar">').replace('Anatomie</button></div>','Anatomie</button></div></template>')
        self.assertNotIn('Secret',self.read(raw))

    def test_visible_outside_course_is_not_course_evidence(self):
        raw='<p>Secret</p>'+self.wrap('<p>Course</p>')
        self.assertNotIn('Secret',self.read(raw))
        self.assertIn('Course',self.read(raw))

    def test_plain_fixtures_preserve_existing_visibility_contract(self):
        raw=b'<p>Public</p><p hidden>Secret</p><template>Secret2</template><script>Secret3</script>'
        self.assertEqual('Public',alpha.visible_text(raw))
        self.assertEqual('Public',alpha.reachable_course_text(raw,'N17'))

if __name__=='__main__':unittest.main()
