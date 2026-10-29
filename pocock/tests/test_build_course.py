"""CSP-Hashes gegen die wirklich serialisierten Scripts prüfen, ohne private Kursdaten."""
import base64
import hashlib
import importlib.util
from pathlib import Path
import re
import unittest

from bs4 import BeautifulSoup

SPEC = importlib.util.spec_from_file_location("course_builder", Path(__file__).resolve().parents[1] / "build_course.py")
BUILDER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BUILDER)


class ScriptHashRegression(unittest.TestCase):
    def assert_serialized_scripts_allowed(self, soup):
        emitted = re.findall(r"<script>(.*?)</script>", str(soup), flags=re.DOTALL)
        expected = {"sha256-" + base64.b64encode(hashlib.sha256(text.encode("utf-8")).digest()).decode("ascii") for text in emitted}
        self.assertEqual(set(BUILDER.inline_script_hashes(soup)), expected)
        self.assertEqual(len(expected), 2)

    def test_programmatically_added_script_is_allowed(self):
        soup = BeautifulSoup('<html><body><script>window.original = true;</script></body></html>', "html.parser")
        extra = soup.new_tag("script")
        extra.string = "\nwindow.addEventListener('pageshow', function () { /* Prüfung */ });\n"
        soup.body.append(extra)
        self.assert_serialized_scripts_allowed(soup)

    def test_replaced_reader_script_and_new_script_are_both_allowed(self):
        soup = BeautifulSoup('<html><body><script>window.original = true;</script></body></html>', "html.parser")
        soup.script.string = "\nvar text = 'Änderung < & >';\nwindow.reader = true;\n"
        extra = soup.new_tag("script")
        extra.string = "window.addEventListener('pageshow', function () {});"
        soup.body.append(extra)
        self.assert_serialized_scripts_allowed(soup)


if __name__ == "__main__":
    unittest.main()
