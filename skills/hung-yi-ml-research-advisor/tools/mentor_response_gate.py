#!/usr/bin/env python3
"""Run the structural and knowledge-backed gates for one advisor response.

The two underlying checks remain independently usable, but this command makes
the normal hand-off a single deterministic operation.  It never judges whether
the research advice is scientifically correct; it only reports whether the
response packet is structurally closed and whether its cited principles retain
their normalized-course provenance.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "mentor-response-gate.v1"


def _load_sibling(filename: str, module_name: str):
    path = Path(__file__).with_name(filename)
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _missing_knowledge_report(knowledge_path: Path | None) -> dict[str, Any]:
    return {
        "schema_version": "advisor-provenance-audit.v1",
        "status": "INPUT_MISSING",
        "response_path": None,
        "knowledge_path": str(knowledge_path) if knowledge_path else None,
        "errors": ["normalized knowledge path was not supplied"],
        "missing_principle_ids": [],
        "evidence_class_drift": [],
        "source_provenance_gaps": [],
        "principles_checked": 0,
    }


def run_gate(response_path: Path, knowledge_path: Path | None = None) -> dict[str, Any]:
    """Return the combined response-contract/provenance gate report."""

    response_path = Path(response_path)
    validator = _load_sibling("response_validator.py", "mentor_response_validator_gate")
    provenance = _load_sibling("advisor_provenance_audit.py", "mentor_provenance_gate")
    response_report = validator.validate_response(response_path)
    provenance_report = (
        provenance.audit_packet(response_path, Path(knowledge_path))
        if knowledge_path is not None
        else _missing_knowledge_report(knowledge_path)
    )
    response_status = response_report.get("status")
    provenance_status = provenance_report.get("status")
    if response_status == "PASS" and provenance_status == "PASS":
        status = "PASS"
    elif response_status == "PASS" and provenance_status == "INPUT_MISSING":
        status = "INPUT_MISSING"
    else:
        status = "FAIL"
    return {
        "schema_version": SCHEMA_VERSION,
        "status": status,
        "response_path": str(response_path),
        "knowledge_path": str(knowledge_path) if knowledge_path else None,
        "response_validation": response_report,
        "provenance_audit": provenance_report,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--response", type=Path, required=True)
    parser.add_argument("--knowledge", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        report = run_gate(args.response, args.knowledge)
    except (OSError, ImportError, TypeError, ValueError, json.JSONDecodeError) as exc:
        report = {"schema_version": SCHEMA_VERSION, "status": "FAIL", "errors": [str(exc)]}
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.json:
        print(json.dumps(report, ensure_ascii=False))
    else:
        print(f"Mentor response gate: {report['status']}")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
