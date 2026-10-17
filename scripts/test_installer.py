import tempfile
from pathlib import Path
import unittest
from install_skills import install

class InstallerTests(unittest.TestCase):
    def setup_tree(self, root):
        source = root / 'source'
        (source / 'sample').mkdir(parents=True)
        (source / 'sample' / 'SKILL.md').write_text('original')
        return source, root / 'dest'
    def test_preview_writes_nothing_and_install_is_idempotent(self):
        with tempfile.TemporaryDirectory() as temp:
            source, dest = self.setup_tree(Path(temp))
            self.assertTrue(install(source, dest, True)['dry_run'])
            self.assertFalse(dest.exists())
            install(source, dest)
            self.assertEqual(install(source, dest)['plan'][0]['action'], 'unchanged')
    def test_modified_existing_skill_is_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            source, dest = self.setup_tree(Path(temp))
            install(source, dest)
            file = dest / 'sample' / 'SKILL.md'
            file.write_text('local modification')
            with self.assertRaises(ValueError): install(source, dest)
            self.assertEqual(file.read_text(), 'local modification')
    def test_symlink_source_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            source, dest = self.setup_tree(Path(temp))
            (source / 'sample' / 'linked').symlink_to(source / 'sample' / 'SKILL.md')
            with self.assertRaises(ValueError): install(source, dest)
            self.assertFalse(dest.exists())

if __name__ == '__main__': unittest.main()
