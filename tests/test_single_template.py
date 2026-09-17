from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
ACTIVE_ROUTE_FILES = (
    ROOT / "SKILL.md",
    ROOT / "references" / "docx-template-map.md",
    ROOT / "references" / "delivery-and-versioning.md",
    ROOT / "tests" / "behavior-cases.md",
)


class SingleTemplateTests(unittest.TestCase):
    def test_only_one_active_builtin_template(self):
        names = sorted(path.name for path in (ROOT / "assets").glob("resume-template-*.docx"))
        self.assertEqual(names, ["resume-template-ats.docx"])

    def test_legacy_template_is_kept_outside_active_assets(self):
        self.assertTrue((ROOT / "archive" / "resume-template-visual.docx").is_file())

    def test_active_routes_use_the_single_template(self):
        skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("assets/resume-template-ats.docx", skill_text)
        for path in ACTIVE_ROUTE_FILES:
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("resume-template-visual.docx", text)
            self.assertNotIn("visual template", text.lower())


if __name__ == "__main__":
    unittest.main()
