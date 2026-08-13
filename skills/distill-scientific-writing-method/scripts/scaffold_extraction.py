#!/usr/bin/env python3
"""Create a non-destructive writing-method extraction workspace."""

from __future__ import annotations

import argparse
from pathlib import Path


FILES = {
    "00_SOURCE_INVENTORY.md": "# Source inventory\n",
    "01_AUTHOR_READER_MODEL.md": "# Author reader model\n",
    "02_NAMING_AND_VOCABULARY.md": "# Naming and vocabulary\n",
    "03_INFORMATION_SELECTION.md": "# Information selection\n",
    "04_DETAIL_AND_DEFENCE_POLICY.md": "# Detail and defence policy\n",
    "05_NARRATIVE_ARCHITECTURE.md": "# Narrative architecture\n",
    "06_SENTENCE_PARAGRAPH_PATTERNS.md": "# Sentence and paragraph patterns\n",
    "07_FIGURE_STORYTELLING.md": "# Figure-led storytelling\n",
    "08_ANTI_PATTERNS.md": "# Evidence-backed anti-patterns\n",
    "09_RULE_EVIDENCE_MATRIX.csv": (
        "rule_id,rule,category,rationale,behavioural_evidence,"
        "commentary_evidence,counter_evidence,confounders,tier_quality,"
        "confidence,hypothesis_link,operational_interpretation\n"
    ),
    "10_AUTHOR_WRITING_PLAYBOOK.md": "# Author writing playbook\n",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_directory", type=Path)
    args = parser.parse_args()
    output = args.output_directory.resolve()

    if output.exists() and any(output.iterdir()):
        parser.error(f"refusing to overwrite non-empty directory: {output}")

    output.mkdir(parents=True, exist_ok=True)
    (output / "evidence").mkdir(exist_ok=True)
    for name, content in FILES.items():
        (output / name).write_text(content, encoding="utf-8", newline="\n")

    print(f"Created extraction workspace: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
