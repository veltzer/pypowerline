"""Behavioural tests for pypowerline's pure segment and file helpers."""

import os
import tempfile
import unittest

from pypowerline import utils
from pypowerline.segments import SegmentCwd, SegmentForward, SegmentSpace


class SegmentCwdTests(unittest.TestCase):
    def setUp(self):
        self._old_cwd = os.getcwd()

    def tearDown(self):
        os.chdir(self._old_cwd)

    def test_plain_cwd_is_absolute_path(self):
        with tempfile.TemporaryDirectory() as d:
            real = os.path.realpath(d)
            os.chdir(real)
            seg = SegmentCwd(home_as_tilde=False)
            self.assertEqual(seg.get_text(), real)

    def test_home_replaced_with_tilde(self):
        with tempfile.TemporaryDirectory() as d:
            real = os.path.realpath(d)
            sub = os.path.join(real, "project", "src")
            os.makedirs(sub)
            os.chdir(sub)
            seg = SegmentCwd(home_as_tilde=True)
            seg.home_directory = real
            self.assertEqual(seg.get_text(), "~/project/src")

    def test_last_only_returns_basename(self):
        with tempfile.TemporaryDirectory() as d:
            real = os.path.realpath(d)
            sub = os.path.join(real, "deep", "leaf")
            os.makedirs(sub)
            os.chdir(sub)
            seg = SegmentCwd(last_only=True, home_as_tilde=False)
            self.assertEqual(seg.get_text(), "leaf")


class SegmentConstantTests(unittest.TestCase):
    def test_forward_text(self):
        self.assertEqual(SegmentForward().get_text(), " > ")

    def test_space_text_and_no_separator(self):
        seg = SegmentSpace()
        self.assertEqual(seg.get_text(), " ")
        self.assertIsNone(seg.separator)


class ExecutePythonFileTests(unittest.TestCase):
    def test_exec_populates_provided_namespace(self):
        vals: dict = {}
        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as fh:
            fh.write("computed = 6 * 7\n")
            name = fh.name
        try:
            utils.execute_python_file(name, vals)
            self.assertEqual(vals["computed"], 42)
        finally:
            os.unlink(name)

    def test_missing_file_is_handled(self):
        # a non-existent path is caught and reported, not raised
        utils.execute_python_file("/nonexistent/does/not/exist.py", {})


if __name__ == "__main__":
    unittest.main()
