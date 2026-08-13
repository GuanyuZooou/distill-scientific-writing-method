#!/usr/bin/env python3
"""Validate the structure and rule matrix of a completed extraction."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


REQUIRED_FILES = [
    "00_SOURCE_INVENTORY.md",
    "01_AUTHOR_READER_MODEL.md",
    "02_NAMING_AND_VOCABULARY.md",
    "03_INFORMATION_SELECTION.md",
    "04_DETAIL_AND_DEFENCE_POLICY.md",
    "05_NARRATIVE_ARCHITECTURE.md",
    "06_SENTENCE_PARAGRAPH_PATTERNS.md",
    "07_FIGURE_STORYTELLING.md",
    "08_ANTI_PATTERNS.md",
    "09_RULE_EVIDENCE_MATRIX.csv",
    "10_AUTHOR_WRITING_PLAYBOOK.md",
]

REQUIRED_COLUMNS = {
    "rule_id",
    "rule",
    "category",
    "rationale",
    "behavioural_evidence",
    "commentary_evidence",
    "counter_evidence",
    "confounders",
    "tier_quality",
    "confidence",
    "hypothesis_link",
    "operational_interpretation",
}

CONFIDENCE = {"STRONG", "PROBABLE", "TENTATIVE"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("extraction_directory", type=Path)
    args = parser.parse_args()
    root = args.extraction_directory.resolve()
    errors: list[str] = []

    for name in REQUIRED_FILES:
        path = root / name
        if not path.is_file():
            errors.append(f"missing file: {name}")
        elif path.stat().st_size < 40:
            errors.append(f"apparently incomplete file: {name}")

    evidence = root / "evidence"
    if not evidence.is_dir():
        errors.append("missing directory: evidence")
    elif not list(evidence.glob("*.md")):
        errors.append("no evidence dossiers found")

    matrix = root / "09_RULE_EVIDENCE_MATRIX.csv"
    rule_count = 0
    confidence_counts = {key: 0 for key in sorted(CONFIDENCE)}
    if matrix.is_file():
        with matrix.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            columns = set(reader.fieldnames or [])
            missing = REQUIRED_COLUMNS - columns
            if missing:
                errors.append("matrix missing columns: " + ", ".join(sorted(missing)))
            for line_number, row in enumerate(reader, start=2):
                rule_count += 1
                value = (row.get("confidence") or "").strip().upper()
                if value not in CONFIDENCE:
                    errors.append(f"invalid confidence at matrix line {line_number}: {value!r}")
                else:
                    confidence_counts[value] += 1
                for field in ("rule_id", "rule", "behavioural_evidence", "counter_evidence", "confounders"):
                    if not (row.get(field) or "").strip():
                        errors.append(f"blank {field} at matrix line {line_number}")

    if rule_count == 0:
        errors.append("rule matrix contains no candidate rules")

    if errors:
        print("Extraction validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Extraction structure is valid.")
    print(f"Rules: {rule_count}")
    for key, value in confidence_counts.items():
        print(f"{key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
