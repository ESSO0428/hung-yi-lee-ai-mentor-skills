#!/usr/bin/env python3
"""Read-only layout check for a copied ML Research Advisor skill."""

from __future__ import annotations

import argparse
import json
import platform
import sys
from pathlib import Path
from typing import Any

REQUIRED_FILES = (
    "SKILL.md",
    "README.md",
    "references/skeleton.md",
    "references/optimization.md",
    "references/generalization-shift.md",
    "references/finetune-forgetting.md",
    "references/shortcut-architecture.md",
    "references/classic-models.md",
    "references/small-data.md",
    "references/not-covered.md",
    "references/sources.md",
    "references/statistical-diagnostics.md",
    "references/tensor-diagnostics.md",
    "references/diagnostic-routing.md",
    "tools/triage.py",
    "tools/recipe_tools.py",
    "tools/advanced_recipe_tools.py",
    "tools/model_evaluation.py",
    "tools/dataset_split_audit.py",
    "tools/torch_diagnostics.py",
)


def bootstrap(skill_root: Path) -> dict[str, Any]:
    root = skill_root.resolve()
    errors = [f"missing: {relative}" for relative in REQUIRED_FILES if not (root / relative).is_file()]
    skill_md = root / "SKILL.md"
    if skill_md.is_file():
        text = skill_md.read_text(encoding="utf-8")
        for relative in REQUIRED_FILES:
            if relative.startswith("references/") and relative not in text:
                errors.append(f"SKILL.md does not route to {relative}")
    if sys.version_info < (3, 11):
        errors.append("Python 3.11+ required")
    return {
        "status": "PASS" if not errors else "FAIL",
        "python": platform.python_version(),
        "skill_root": str(root),
        "missing_or_invalid": errors,
        "writes_sources": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-root", type=Path, default=Path(__file__).parent)
    parser.add_argument("--json", action="store_true", help="emit machine-readable output")
    args = parser.parse_args()
    result = bootstrap(args.skill_root)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    else:
        print(f"{result['status']}: hung-yi-ml-research-advisor bootstrap ({result['python']})")
        for item in result["missing_or_invalid"]:
            print(f"- {item}")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
