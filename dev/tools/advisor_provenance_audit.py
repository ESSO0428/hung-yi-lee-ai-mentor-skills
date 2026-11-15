"""Audit an advisor response against the normalized course knowledge base.

``response_validator.py`` checks packet structure and local evidence-ID closure.
This companion gate checks the domain boundary: every cited principle must be a
real normalized principle, its evidence class must not be upgraded, and a
source-grounded course rule must retain usable video provenance.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any, Callable


SCHEMA_VERSION = "advisor-provenance-audit.v1"
_CLASS_MAP = {
    "DIRECT_COURSE_EVIDENCE": "DIRECT",
    "PROJECT_INFERENCE": "INFERENCE",
    "STRONG_SYNTHESIS": "STRONG_SYNTHESIS",
    "CANDIDATE": "CANDIDATE",
    "UNKNOWN": "UNKNOWN",
}
_REQUIRED_PROVENANCE_FIELDS = ("video_id", "url", "timestamp_start", "timestamp_end", "source_chunk")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _load_validator() -> Callable[[Path], dict[str, Any]]:
    path = Path(__file__).with_name("response_validator.py")
    spec = importlib.util.spec_from_file_location("mentor_response_validator_for_audit", path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.validate_response


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def audit_packet(response_path: Path, knowledge_path: Path) -> dict[str, Any]:
    """Return a deterministic knowledge-backed provenance audit report."""

    response_path = Path(response_path)
    knowledge_path = Path(knowledge_path)
    report: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "status": "INPUT_MISSING",
        "response_path": str(response_path),
        "knowledge_path": str(knowledge_path),
        "response_sha256": None,
        "knowledge_sha256": None,
        "errors": [],
        "missing_principle_ids": [],
        "evidence_class_drift": [],
        "source_provenance_gaps": [],
        "principles_checked": 0,
    }
    if not response_path.is_file() or not knowledge_path.is_file():
        report["errors"] = [
            f"missing input: {path}"
            for path in (response_path, knowledge_path)
            if not path.is_file()
        ]
        return report
    try:
        response = _load_json(response_path)
        knowledge = _load_json(knowledge_path)
        report["response_sha256"] = _sha256(response_path)
        report["knowledge_sha256"] = _sha256(knowledge_path)
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
        report["errors"] = [f"cannot load input: {exc}"]
        return report

    try:
        response_validation = _load_validator()(response_path)
    except (OSError, ImportError, TypeError, ValueError) as exc:
        response_validation = {"status": "FAIL", "errors": [f"response validator unavailable: {exc}"]}
    report["response_validation"] = response_validation
    if response_validation.get("status") != "PASS":
        report["errors"].extend(
            f"response contract: {error}" for error in response_validation.get("errors", [])
        )

    principle_rows = knowledge.get("principles") if isinstance(knowledge, dict) else None
    if not isinstance(principle_rows, list):
        report["errors"].append("knowledge.principles must be a list")
        report["status"] = "FAIL"
        return report
    normalized = {
        str(item.get("id")): item
        for item in principle_rows
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    }
    response_principles = response.get("principles") if isinstance(response, dict) else None
    if not isinstance(response_principles, list):
        response_principles = []
    report["principles_checked"] = len(response_principles)
    recommendation = response.get("recommendation") if isinstance(response, dict) else None
    if isinstance(recommendation, dict) and recommendation.get("reasoning_mode") == "SOURCE_GROUNDED" and not response_principles:
        report["errors"].append("SOURCE_GROUNDED advice requires at least one normalized principle")
    missing: set[str] = set()
    drift: list[dict[str, str]] = []
    provenance_gaps: list[dict[str, Any]] = []
    for index, item in enumerate(response_principles):
        if not isinstance(item, dict):
            continue
        principle_id = str(item.get("id", ""))
        source = normalized.get(principle_id)
        if source is None:
            missing.add(principle_id)
            continue
        expected = _CLASS_MAP.get(str(source.get("evidence_class", "UNKNOWN")), "UNKNOWN")
        actual = str(item.get("evidence_class", "UNKNOWN"))
        if actual != expected:
            drift.append({"index": str(index), "principle_id": principle_id, "expected": expected, "actual": actual})
        provenance = source.get("provenance")
        if actual in {"DIRECT", "STRONG_SYNTHESIS"}:
            if not isinstance(provenance, list) or not provenance:
                provenance_gaps.append({"index": index, "principle_id": principle_id, "reason": "no course provenance"})
            else:
                for entry_index, entry in enumerate(provenance):
                    if not isinstance(entry, dict):
                        provenance_gaps.append({"index": index, "principle_id": principle_id, "reason": f"provenance[{entry_index}] is not an object"})
                        continue
                    absent = [field for field in _REQUIRED_PROVENANCE_FIELDS if field not in entry or entry[field] in (None, "")]
                    if absent:
                        provenance_gaps.append({"index": index, "principle_id": principle_id, "reason": f"provenance[{entry_index}] missing {absent}"})
    report["missing_principle_ids"] = sorted(item for item in missing if item)
    report["evidence_class_drift"] = drift
    report["source_provenance_gaps"] = provenance_gaps
    report["errors"].extend(f"unknown principle id: {item}" for item in report["missing_principle_ids"])
    report["errors"].extend(
        f"evidence_class drift for {item['principle_id']}: expected {item['expected']}, got {item['actual']}"
        for item in drift
    )
    report["errors"].extend(
        f"source provenance gap for {item['principle_id']}: {item['reason']}"
        for item in provenance_gaps
    )
    report["status"] = "PASS" if not report["errors"] else "FAIL"
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--response", type=Path, required=True)
    parser.add_argument("--knowledge", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    report = audit_packet(args.response, args.knowledge)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.json:
        print(json.dumps(report, ensure_ascii=False))
    else:
        print(f"Advisor provenance audit: {report['status']}")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
