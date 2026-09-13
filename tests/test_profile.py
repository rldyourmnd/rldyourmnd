"""Regression checks; every mutation is isolated in a temporary directory."""
from pathlib import Path
import re
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'tools'))
from check_profile import validate  # noqa: E402
from check_workbench import HARNESSES, LANGUAGES, TOOLS, validate_workbench  # noqa: E402
from render_profile import expected_assets  # noqa: E402


class ProfileTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        for name in ('README.md', 'README.ru.md'):
            shutil.copyfile(ROOT/name, self.root/name)
        shutil.copytree(ROOT/'assets', self.root/'assets')

    def change(self, path, before, after):
        file = self.root/path
        original = file.read_text(encoding='utf-8')
        self.assertIn(before, original)
        file.write_text(original.replace(before, after, 1), encoding='utf-8')

    def rejects(self, message):
        self.assertTrue(any(message in error for error in validate(self.root)), message)

    def test_complete_profile(self):
        self.assertEqual(validate(self.root), [])

    def test_deterministic_generator(self):
        self.assertEqual(expected_assets(), expected_assets())
        self.assertEqual(len(expected_assets()), 19)

    def test_missing_asset(self):
        (self.root/'assets/profile/gds-dark.svg').unlink()
        self.rejects('missing or changed')
        self.rejects('missing local target')

    def test_changed_generated_asset(self):
        self.change('assets/profile/gds-dark.svg', 'GDS', 'Changed')
        self.rejects('missing or changed')

    def test_no_alt(self):
        self.change('README.md', 'alt="GDS:', 'data-alt="GDS:')
        self.rejects('Missing image alternative')

    def test_external_image(self):
        self.change('README.md', 'src="assets/profile/gds-light.svg"', 'src="https://example.com/image.svg"')
        self.rejects('image must be repository-local')

    def test_path_escape(self):
        self.change('README.md', '[Русский](README.ru.md)', '[Русский](../README.ru.md)')
        self.rejects('path escapes repository')

    def test_visible_russian(self):
        self.change('README.md', '## Selected open-source work', '## Избранное')
        self.rejects('untranslated body copy')

    def test_removed_motion_preference(self):
        self.change('assets/profile/gds-dark-motion.svg', 'prefers-reduced-motion:reduce', 'print')
        self.rejects('missing reduced-motion')

    def test_unbounded_motion(self):
        self.change('assets/profile/gds-dark-motion.svg', 'ease-in-out 6', 'ease-in-out infinite')
        self.rejects('unbounded content')

    def test_script(self):
        self.change('assets/profile/gds-dark.svg', '</svg>', '<script>alert(1)</script></svg>')
        self.rejects('unsupported SVG element')

    def test_entity_declaration(self):
        self.change('assets/profile/gds-dark.svg', '<svg ', '<!DOCTYPE svg [<!ENTITY x "test">]><svg ')
        self.rejects('XML declarations')

    def test_no_pass_with_svg_collection_missing(self):
        shutil.rmtree(self.root/'assets/profile')
        self.rejects('missing or changed')

    def test_unexpected_asset(self):
        shutil.copyfile(self.root/'assets/profile/gds-dark.svg', self.root/'assets/profile/extra.svg')
        self.rejects('Unexpected SVG')

    def test_each_language_required_in_both_versions(self):
        for name in ('README.md', 'README.ru.md'):
            file = self.root/name
            original = file.read_text(encoding='utf-8')
            for language in LANGUAGES:
                with self.subTest(document=name, language=language):
                    file.write_text(original.replace(language, 'REMOVED'), encoding='utf-8')
                    self.rejects('language not visible')
            file.write_text(original, encoding='utf-8')

    def test_each_harness_required_in_both_versions(self):
        for name in ('README.md', 'README.ru.md'):
            file = self.root/name
            original = file.read_text(encoding='utf-8')
            for harness in HARNESSES:
                with self.subTest(document=name, harness=harness):
                    file.write_text(original.replace(harness, 'REMOVED'), encoding='utf-8')
                    self.rejects('seven named harnesses')
            file.write_text(original, encoding='utf-8')

    def test_each_tool_required_in_both_versions(self):
        for name in ('README.md', 'README.ru.md'):
            file = self.root/name
            original = file.read_text(encoding='utf-8')
            for tool in TOOLS:
                with self.subTest(document=name, tool=tool):
                    file.write_text(re.sub(re.escape(tool), 'REMOVED', original, flags=re.I), encoding='utf-8')
                    self.rejects('tool not visible')
            file.write_text(original, encoding='utf-8')

    def test_eighth_harness_rejected(self):
        self.change('README.md', 'Cursor · Antigravity**', 'Cursor · Antigravity · Other**')
        self.rejects('seven named harnesses')

    def test_harnesses_cannot_be_collapsed(self):
        line = '**' + ' · '.join(HARNESSES) + '**'
        self.change('README.md', line, '<details>\n<summary>Tools</summary>\n' + line + '\n</details>')
        self.rejects('seven named harnesses')

    def test_tool_in_comment_does_not_count(self):
        file = self.root/'README.md'
        original = file.read_text(encoding='utf-8')
        file.write_text(original.replace('Ponytail', 'REMOVED') + '\n<!-- Ponytail -->\n', encoding='utf-8')
        self.rejects('tool not visible before projects: Ponytail')

    def test_tool_in_image_alt_does_not_count(self):
        file = self.root/'README.md'
        original = file.read_text(encoding='utf-8').replace('Ponytail', 'REMOVED')
        file.write_text(original.replace('alt="GDS:', 'alt="Ponytail GDS:'), encoding='utf-8')
        self.rejects('tool not visible before projects: Ponytail')

    def test_stack_cannot_move_below_projects(self):
        self.change('README.md', '## What I work with', '## Selected open-source work\n\n## What I work with')
        self.rejects('language not visible')

    def test_client_details_rejected(self):
        self.change('README.md', 'Almaty Customs · Almaty City Libraries',
                    'Almaty Customs · Almaty City Libraries\n\nImplementation details.')
        self.rejects('only approved plain-text names')

    def test_russian_client_details_rejected(self):
        self.change('README.ru.md', 'Таможня Алматы · Библиотеки Алматы',
                    'Таможня Алматы · Библиотеки Алматы\n\nОписание реализации.')
        self.rejects('only approved plain-text names')

    def test_client_links_rejected(self):
        self.change('README.md', 'Almaty Customs · Almaty City Libraries',
                    '[Almaty Customs](https://example.com) · Almaty City Libraries')
        self.rejects('only approved plain-text names')

    def test_client_name_elsewhere_rejected(self):
        self.change('README.md', '## Get in touch', '## Get in touch\n\nAlmaty Customs: details.')
        self.rejects('client name repeated')

    def test_guessed_ctx_link_rejected(self):
        self.change('README.md', '`ctx` (agent session viewer)', '[ctx](https://example.com)')
        self.rejects('ctx must stay unlinked')

    def test_missing_workbench_document_rejected(self):
        (self.root/'README.ru.md').unlink()
        self.assertTrue(any('missing workbench document' in x for x in validate_workbench(self.root)))


if __name__ == '__main__':
    unittest.main()
