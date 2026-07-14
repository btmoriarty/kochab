#!/usr/bin/env python3
"""Unit tests for the resume builder's pure functions.

These do not import WeasyPrint (the import is deferred inside build()), so they
run with no native dependencies:

    python3 -m unittest tests/test_resume_builder.py
"""

import os
import sys
import unittest

sys.path.insert(
    0, os.path.join(os.path.dirname(__file__), "..", "skills", "kochab", "assets")
)

import resume_builder as rb  # noqa: E402


class TestEscaping(unittest.TestCase):
    def test_bullet_is_escaped(self):
        # A script tag in user content must not survive into the HTML/PDF.
        p = {
            "experience": [
                {
                    "title": "Engineer",
                    "employer": "Example Corp",
                    "dates": "2020-2024",
                    "bullets": ["<script>alert('x')</script> shipped a thing"],
                }
            ]
        }
        html = rb.experience(p)
        self.assertNotIn("<script>", html)
        self.assertIn("&lt;script&gt;", html)

    def test_skills_label_is_escaped(self):
        p = {"skills": [{"label": "A & B <b>", "items": ["x & y"]}]}
        html = rb.skills(p)
        self.assertNotIn("<b>", html.replace("</b>", ""))  # no raw injected tag
        self.assertIn("&amp;", html)


class TestSectionOmission(unittest.TestCase):
    def test_empty_summary_omitted(self):
        self.assertEqual(rb.summary({}), "")
        self.assertEqual(rb.summary({"summary": ""}), "")

    def test_empty_skills_omitted(self):
        self.assertEqual(rb.skills({}), "")
        self.assertEqual(rb.skills({"skills": []}), "")

    def test_missing_list_omitted(self):
        self.assertEqual(rb.simple_list({}, "patents", "U.S. Patents"), "")


class TestSafeFilename(unittest.TestCase):
    def test_spaces_become_underscores(self):
        self.assertEqual(rb.safe_filename("Acme Program Manager"), "Acme_Program_Manager.pdf")

    def test_path_traversal_stripped(self):
        # No slashes or dots survive, so no directory escape is possible.
        out = rb.safe_filename("../../etc/passwd")
        self.assertNotIn("/", out)
        self.assertNotIn("..", out)
        self.assertTrue(out.endswith(".pdf"))

    def test_all_symbols_falls_back(self):
        self.assertEqual(rb.safe_filename("@@@***"), "resume_variant.pdf")

    def test_length_capped(self):
        out = rb.safe_filename("x" * 500)
        self.assertLessEqual(len(out), 124)  # 120 chars + ".pdf"


if __name__ == "__main__":
    unittest.main()
