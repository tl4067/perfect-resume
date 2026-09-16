#!/usr/bin/env python3
"""Read-only structural and privacy checks for a DOCX template.

The checker deliberately reports only detectable OOXML conditions.  A clean
result is not an ATS compatibility or identity-anonymisation certification.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


EMAIL_RE = re.compile(
    r"(?i)(?<![\w.+-])[\w.!#$%&'*+/=?^_`{|}~-]+@"
    r"[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?(?:\.[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?)+"
)
LOCAL_TAGS = {
    "comment": "comments",
    "ins": "tracked_changes",
    "del": "tracked_changes",
    "moveFrom": "tracked_changes",
    "moveTo": "tracked_changes",
}
REQUIRED_PARTS = ("[Content_Types].xml", "word/document.xml")


def _report(profile: str, status: str, errors=None, review_items=None, inventory=None):
    return {
        "profile": profile,
        "status": status,
        "errors": list(errors or []),
        "review_items": list(review_items or []),
        "inventory": inventory
        or {
            "tables": 0,
            "images": 0,
            "comments": 0,
            "tracked_changes": 0,
            "custom_xml_parts": 0,
        },
    }


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _xml_text(root: ET.Element) -> str:
    return " ".join(value for value in root.itertext() if value.strip())


def _audit(path: Path, profile: str):
    inventory = {
        "tables": 0,
        "images": 0,
        "comments": 0,
        "tracked_changes": 0,
        "custom_xml_parts": 0,
    }
    errors = []
    review_items = []

    try:
        with zipfile.ZipFile(path, "r") as archive:
            names = archive.namelist()
            missing = [part for part in REQUIRED_PARTS if part not in names]
            if missing:
                return _report(
                    profile,
                    "error",
                    ["missing required OOXML part(s): " + ", ".join(missing)],
                    inventory=inventory,
                ), 2

            xml_roots = {}
            for name in names:
                if not name.lower().endswith((".xml", ".rels")):
                    continue
                raw = archive.read(name)
                try:
                    root = ET.fromstring(raw)
                except (ET.ParseError, UnicodeDecodeError) as exc:
                    return _report(
                        profile,
                        "error",
                        [f"invalid XML in {name}: {exc}"],
                        inventory=inventory,
                    ), 2
                xml_roots[name] = root
                if EMAIL_RE.search(raw.decode("utf-8", "replace")):
                    errors.append(f"email-like identifier found in {name}")

            inventory["images"] = sum(
                1 for name in names if name.lower().startswith("word/media/")
            )
            inventory["custom_xml_parts"] = sum(
                1 for name in names if name.lower().startswith("customxml/")
            )

            for name, root in xml_roots.items():
                local_names = [_local_name(node.tag) for node in root.iter()]
                inventory["tables"] += sum(1 for tag in local_names if tag == "tbl")
                inventory["comments"] += sum(1 for tag in local_names if tag == "comment")
                inventory["tracked_changes"] += sum(
                    1 for tag in local_names if tag in LOCAL_TAGS and LOCAL_TAGS[tag] == "tracked_changes"
                )

            core = xml_roots.get("docProps/core.xml")
            if core is not None:
                for node in core.iter():
                    if _local_name(node.tag) in {"creator", "lastModifiedBy"} and (node.text or "").strip():
                        errors.append(
                            f"{_local_name(node.tag)} is non-empty in docProps/core.xml"
                        )

            if inventory["comments"]:
                errors.append("comments are present in the document")
            if inventory["tracked_changes"]:
                errors.append("tracked changes are present in the document")

            if inventory["images"]:
                review_items.append("images and their alternative text require manual review")
            if inventory["custom_xml_parts"]:
                review_items.append("custom XML parts require manual privacy review")

            rel_targets = []
            for name, root in xml_roots.items():
                if not name.lower().endswith(".rels"):
                    continue
                for node in root.iter():
                    target = node.attrib.get("Target")
                    if target:
                        rel_targets.append(target)
            if any("http://" in target or "https://" in target for target in rel_targets):
                review_items.append("external relationship targets require manual review")
            if any("oleObject" in name or "embeddings/" in name for name in names):
                review_items.append("embedded objects require manual review")

            # A blank-template audit should flag human-readable content for a
            # reviewer, but an empty synthetic document remains an automatic pass.
            text_parts = []
            for name, root in xml_roots.items():
                if name.lower().endswith((".xml", ".rels")):
                    value = _xml_text(root)
                    if value:
                        text_parts.append((name, value))
            if any(name.startswith(("word/document.xml", "word/header", "word/footer", "docProps/")) for name, _ in text_parts):
                review_items.append("document text, headers/footers, and properties require manual identity review")

    except (OSError, zipfile.BadZipFile, KeyError) as exc:
        return _report(profile, "error", [f"unable to inspect DOCX: {exc}"], inventory=inventory), 2

    status = "fail" if errors else ("review" if review_items else "pass")
    exit_code = 1 if status != "pass" else 0
    return _report(profile, status, errors, review_items, inventory), exit_code


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Audit a DOCX template without modifying it")
    parser.add_argument("docx", type=Path)
    parser.add_argument("--profile", default="blank-template")
    args = parser.parse_args(argv)
    report, code = _audit(args.docx, args.profile)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return code


if __name__ == "__main__":
    sys.exit(main())
