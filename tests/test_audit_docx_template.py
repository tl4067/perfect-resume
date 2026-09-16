import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_docx_template.py"


def _minimal_parts(core_xml="", document_xml=None, extra=None):
    document_xml = document_xml or (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        "<w:body><w:sectPr/></w:body></w:document>"
    )
    parts = {
        "[Content_Types].xml": (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
            '<Default Extension="xml" ContentType="application/xml"/>'
            '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
            '<Override PartName="/word/document.xml" '
            'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
            "</Types>"
        ),
        "_rels/.rels": (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"/>'
        ),
        "word/document.xml": document_xml,
        "word/_rels/document.xml.rels": (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"/>'
        ),
        "docProps/core.xml": core_xml or (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
            'xmlns:dc="http://purl.org/dc/elements/1.1/"/>'
        ),
    }
    if extra:
        parts.update(extra)
    return parts


def _write_package(path, parts):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as archive:
        for name, data in parts.items():
            archive.writestr(name, data)


class AuditDocxTemplateTests(unittest.TestCase):
    def run_audit(self, path):
        completed = subprocess.run(
            [sys.executable, str(SCRIPT), str(path), "--profile", "blank-template"],
            text=True,
            capture_output=True,
            check=False,
        )
        try:
            report = json.loads(completed.stdout)
        except json.JSONDecodeError as exc:
            self.fail(f"audit output is not JSON: {completed.stdout!r}; stderr={completed.stderr!r}: {exc}")
        return completed.returncode, report

    def test_clean_minimal_ooxml_passes(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "clean.docx"
            _write_package(path, _minimal_parts())
            code, report = self.run_audit(path)
        self.assertEqual(code, 0)
        self.assertEqual(report["status"], "pass")
        self.assertEqual(report["errors"], [])
        self.assertEqual(report["inventory"]["comments"], 0)
        self.assertEqual(report["inventory"]["tracked_changes"], 0)

    def test_last_modified_by_is_a_blocking_error(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "author.docx"
            core = (
                '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
                'xmlns:dc="http://purl.org/dc/elements/1.1/">'
                "<cp:lastModifiedBy>author@example.com</cp:lastModifiedBy></cp:coreProperties>"
            )
            _write_package(path, _minimal_parts(core_xml=core))
            code, report = self.run_audit(path)
        self.assertEqual(code, 1)
        self.assertEqual(report["status"], "fail")
        self.assertTrue(any("lastModifiedBy" in error for error in report["errors"]))

    def test_email_in_non_body_metadata_is_detected(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "email.docx"
            extra = {"docProps/app.xml": "<Properties>owner@example.com</Properties>"}
            _write_package(path, _minimal_parts(extra=extra))
            code, report = self.run_audit(path)
        self.assertEqual(code, 1)
        self.assertTrue(any("email" in error.lower() for error in report["errors"]))

    def test_email_in_xml_attribute_is_detected(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "email-attribute.docx"
            extra = {"docProps/app.xml": '<Properties owner="owner@example.com"/>'}
            _write_package(path, _minimal_parts(extra=extra))
            code, report = self.run_audit(path)
        self.assertEqual(code, 1)
        self.assertTrue(any("email" in error.lower() for error in report["errors"]))

    def test_comments_and_tracked_changes_are_reported(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "review.docx"
            document = (
                '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
                "<w:body><w:ins><w:r><w:t>draft</w:t></w:r></w:ins><w:sectPr/></w:body></w:document>"
            )
            extra = {
                "word/comments.xml": (
                    '<w:comments xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
                    '<w:comment w:id="0"><w:p><w:r><w:t>note</w:t></w:r></w:p></w:comment></w:comments>'
                )
            }
            _write_package(path, _minimal_parts(document_xml=document, extra=extra))
            code, report = self.run_audit(path)
        self.assertEqual(code, 1)
        self.assertEqual(report["inventory"]["comments"], 1)
        self.assertGreaterEqual(report["inventory"]["tracked_changes"], 1)
        self.assertTrue(any("comment" in error.lower() for error in report["errors"]))
        self.assertTrue(any("tracked" in error.lower() for error in report["errors"]))

    def test_images_and_custom_xml_require_manual_review(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "review-items.docx"
            extra = {
                "word/media/image1.png": b"png",
                "customXml/item1.xml": "<item/>",
            }
            _write_package(path, _minimal_parts(extra=extra))
            code, report = self.run_audit(path)
        self.assertEqual(code, 1)
        self.assertEqual(report["status"], "review")
        self.assertEqual(report["inventory"]["images"], 1)
        self.assertEqual(report["inventory"]["custom_xml_parts"], 1)
        joined = " ".join(report["review_items"]).lower()
        self.assertIn("image", joined)
        self.assertIn("custom", joined)

    def test_invalid_zip_returns_check_error(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "bad.docx"
            path.write_bytes(b"not a zip")
            code, report = self.run_audit(path)
        self.assertEqual(code, 2)
        self.assertEqual(report["status"], "error")
        self.assertTrue(report["errors"])

    def test_malformed_xml_returns_check_error(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "malformed.docx"
            parts = _minimal_parts()
            parts["word/document.xml"] = "<w:document>"
            _write_package(path, parts)
            code, report = self.run_audit(path)
        self.assertEqual(code, 2)
        self.assertEqual(report["status"], "error")
        self.assertTrue(any("xml" in error.lower() for error in report["errors"]))

    def test_audit_is_read_only(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "readonly.docx"
            _write_package(path, _minimal_parts())
            before = hashlib.sha256(path.read_bytes()).digest()
            code, _ = self.run_audit(path)
            after = hashlib.sha256(path.read_bytes()).digest()
        self.assertEqual(code, 0)
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
