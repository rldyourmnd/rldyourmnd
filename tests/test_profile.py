"""Regression checks for the checker itself; all mutations use temporary files."""
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'tools'))
from check_profile import validate  # noqa: E402
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
        self.change('README.md', '## Selected work', '## Избранное')
        self.rejects('Russian is visible')

    def test_open_language_details(self):
        self.change('README.md', '<details>', '<details open>')
        self.rejects('must be collapsed')

    def test_removed_motion_preference(self):
        self.change('assets/profile/gds-dark-motion.svg', 'prefers-reduced-motion:reduce', 'print')
        self.rejects('missing reduced-motion')

    def test_unbounded_motion(self):
        self.change('assets/profile/gds-dark-motion.svg', 'ease-in-out 1', 'ease-in-out infinite')
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


if __name__ == '__main__':
    unittest.main()
