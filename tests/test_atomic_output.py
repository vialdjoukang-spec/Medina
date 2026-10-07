import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from tools.atomic_output import atomic_output


class AtomicOutputTests(unittest.TestCase):
    def test_existing_output_remains_visible_until_complete(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / 'fragment.html'
            target.write_bytes(b'previous')
            target.chmod(0o640)
            with atomic_output(target) as staging:
                self.assertNotEqual(Path(staging), target)
                Path(staging).write_bytes(b'intermediate')
                self.assertEqual(target.read_bytes(), b'previous')
                Path(staging).write_bytes(b'complete')
                self.assertEqual(target.read_bytes(), b'previous')
            self.assertEqual(target.read_bytes(), b'complete')
            self.assertEqual(target.stat().st_mode & 0o777, 0o640)
            self.assertFalse(Path(staging).exists())

    def test_first_output_is_not_exposed_before_success(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / 'fragment.html'
            with atomic_output(target) as staging:
                Path(staging).write_bytes(b'complete without templates')
                self.assertFalse(target.exists())
            self.assertEqual(target.read_bytes(), b'complete without templates')
            self.assertEqual(target.stat().st_mode & 0o777, 0o644)

    def test_failed_build_keeps_previous_output_and_cleans_staging(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / 'fragment.html'
            target.write_bytes(b'previous')
            with self.assertRaises(RuntimeError):
                with atomic_output(target) as staging:
                    Path(staging).write_bytes(b'intermediate')
                    raise RuntimeError('build failed')
            self.assertEqual(target.read_bytes(), b'previous')
            self.assertFalse(Path(staging).exists())

    def test_failed_replacement_keeps_previous_output_and_cleans_staging(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / 'fragment.html'
            target.write_bytes(b'previous')
            with patch('tools.atomic_output.os.replace', side_effect=OSError('replace failed')):
                with self.assertRaises(OSError):
                    with atomic_output(target) as staging:
                        Path(staging).write_bytes(b'complete')
            self.assertEqual(target.read_bytes(), b'previous')
            self.assertFalse(Path(staging).exists())


if __name__ == '__main__':
    unittest.main()
