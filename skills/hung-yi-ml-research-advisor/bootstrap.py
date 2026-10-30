#!/usr/bin/env python3
"""Read-only bootstrap check for a copied ML Research Advisor Skill."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import platform
import sys
from typing import Any


REQUIRED_FILES = (
    "SKILL.md",
    "README.md",
    "modules/index.md",
    "references/provenance-policy.md",
    "references/response-schema.md",
    "tools/recipe_tools.py",
    "tools/advanced_recipe_tools.py",
    "tools/torch_diagnostics.py",
    "tools/dataset_split_audit.py",
    "tools/ffp_evaluation.py",
    "tools/search_course_material_chunks.py",
    "tools/capability_probe.py",
    "tools/mentor_response_gate.py",
)


def _load_principles(path: Path) -> tuple[list[dict[str, Any]], str | None]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [], str(exc)
    principles = payload.get("principles") if isinstance(payload, dict) else None
    if not isinstance(principles, list):
        return [], "knowledge JSON must contain a principles list"
    if not all(isinstance(item, dict) for item in principles):
        return [], "each principle must be an object"
    return principles, None


def bootstrap(
    skill_root: Path,
    knowledge: Path | None,
    *,
    require_knowledge: bool = False,
) -> dict[str, Any]:
    root = skill_root.resolve()
    missing = [str(root / relative) for relative in REQUIRED_FILES if not (root / relative).is_file()]
    principles: list[dict[str, Any]] = []
    knowledge_error: str | None = None
    knowledge_status = "NOT_PROVIDED"
    if knowledge is not None:
        principles, knowledge_error = _load_principles(knowledge.resolve())
        knowledge_status = "VERIFIED" if knowledge_error is None else "INVALID"

    module_domains = sorted({str(item.get("domain")) for item in principles if item.get("domain")})
    module_errors: list[str] = []
    index = root / "modules" / "index.md"
    index_text = index.read_text(encoding="utf-8") if index.is_file() else ""
    for domain in module_domains:
        module = root / "modules" / f"{domain}.md"
        if not module.is_file():
            module_errors.append(f"missing module: {module}")
            continue
        body = module.read_text(encoding="utf-8")
        if f"domain: {domain}" not in body or f"modules/{domain}.md" not in index_text:
            module_errors.append(f"module route missing: {domain}")
        for item in principles:
            if item.get("domain") != domain:
                continue
            if str(item.get("id")) not in body:
                module_errors.append(f"principle missing from module: {item.get('id')}")
            for source in item.get("provenance", []):
                if isinstance(source, dict) and source.get("source_chunk") not in body:
                    module_errors.append(
                        f"source chunk missing from module: {item.get('id')}:{source.get('source_chunk')}"
                    )

    errors = [*missing, *module_errors]
    if require_knowledge and knowledge is None:
        errors.append("normalized knowledge is required for source-grounded advisor use")
    if require_knowledge and knowledge is not None and knowledge_error is None and not principles:
        errors.append("normalized knowledge contains no principles")
    if knowledge_error:
        errors.append(knowledge_error)
    source_grounded_ready = knowledge_status == "VERIFIED" and bool(principles)
    input_missing = require_knowledge and (
        knowledge is None or (knowledge is not None and knowledge_error is None and not principles)
    )
    if errors and input_missing and not missing and not module_errors:
        status = "INPUT_MISSING"
    else:
        status = "PASS" if not errors and sys.version_info >= (3, 11) else "FAIL"
    return {
        "status": status,
        "python": platform.python_version(),
        "skill_root": str(root),
        "knowledge": str(knowledge.resolve()) if knowledge is not None else None,
        "knowledge_status": knowledge_status,
        "source_grounded_ready": source_grounded_ready,
        "require_knowledge": require_knowledge,
        "principle_count": len(principles),
        "module_count": len(module_domains),
        "missing_or_invalid": errors,
        "writes_sources": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-root", type=Path, default=Path(__file__).parent)
    parser.add_argument(
        "--knowledge",
        type=Path,
        help="optional normalized_principles.json supplied by the full project or a skill-only install",
    )
    parser.add_argument(
        "--require-knowledge",
        action="store_true",
        help="return INPUT_MISSING unless normalized principles are supplied and valid",
    )
    parser.add_argument("--json", action="store_true", help="emit machine-readable output")
    args = parser.parse_args()
    result = bootstrap(args.skill_root, args.knowledge, require_knowledge=args.require_knowledge)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    else:
        print(f"{result['status']}: hung-yi-ml-research-advisor bootstrap ({result['python']})")
        if result["missing_or_invalid"]:
            print("Problems:")
            print("\n".join(f"- {item}" for item in result["missing_or_invalid"]))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
