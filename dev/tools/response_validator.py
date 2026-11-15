"""Validate the machine-readable contract for an ML advisor response.

This checks structure and provenance linkage only. It does not decide whether a
hypothesis is scientifically correct.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "ml-advisor-response.v1"
UNKNOWN = "UNKNOWN"
REASONING_MODES = {"SOURCE_GROUNDED", "PROJECT_INFERENCE", "REVIEW_REQUIRED"}
PRINCIPLE_CLASSES = {"DIRECT", "STRONG_SYNTHESIS", "INFERENCE", "CANDIDATE", "UNKNOWN"}
REQUIRED_FIELDS = (
    "observations",
    "unknowns",
    "hypotheses",
    "principles",
    "experiment",
    "recommendation",
    "provenance",
)


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _nonempty_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _list_of_text(value: Any) -> bool:
    return isinstance(value, list) and all(_nonempty_text(item) for item in value)


def _collect_ids(value: Any) -> set[str]:
    if not isinstance(value, list):
        return set()
    return {item for item in value if _nonempty_text(item) and item != UNKNOWN}


def _load(source: Path | dict[str, Any]) -> tuple[dict[str, Any], str | None, str | None]:
    if isinstance(source, dict):
        return source, None, None
    path = Path(source)
    raw = path.read_bytes()
    payload = json.loads(raw.decode("utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("response JSON must be an object")
    return payload, str(path), hashlib.sha256(raw).hexdigest()


def validate_response(source: Path | dict[str, Any]) -> dict[str, Any]:
    """Return a deterministic structural/provenance validation report."""
    source_path: str | None = None
    input_sha256: str | None = None
    try:
        payload, source_path, input_sha256 = _load(source)
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
        return {
            "schema_version": SCHEMA_VERSION,
            "status": "FAIL",
            "source_path": source_path,
            "input_sha256": input_sha256,
            "errors": [f"cannot load response: {exc}"],
            "warnings": [],
            "missing_fields": [],
            "unresolved_evidence_ids": [],
        }

    errors: list[str] = []
    warnings: list[str] = []
    missing_fields = [field for field in REQUIRED_FIELDS if field not in payload]

    observations = payload.get("observations")
    if not isinstance(observations, list) or not observations:
        errors.append("observations must be a non-empty list")
    else:
        for index, item in enumerate(observations):
            if not isinstance(item, dict) or not _nonempty_text(item.get("text")):
                errors.append(f"observations[{index}] needs non-empty text")
            elif not _list_of_text(item.get("evidence_ids")):
                errors.append(f"observations[{index}] needs evidence_ids")

    unknowns = payload.get("unknowns")
    if not _list_of_text(unknowns):
        errors.append("unknowns must be a list of non-empty strings")

    hypotheses = payload.get("hypotheses")
    if not isinstance(hypotheses, list) or len(hypotheses) < 2:
        errors.append("hypotheses must contain at least two competing hypotheses")
    else:
        seen: set[str] = set()
        for index, item in enumerate(hypotheses):
            if not isinstance(item, dict):
                errors.append(f"hypotheses[{index}] must be an object")
                continue
            hypothesis_id = item.get("id")
            if not _nonempty_text(hypothesis_id):
                errors.append(f"hypotheses[{index}] needs id")
            elif hypothesis_id in seen:
                errors.append(f"duplicate hypothesis id: {hypothesis_id}")
            seen.add(str(hypothesis_id))
            for field in ("claim", "discriminating_experiment"):
                if not _nonempty_text(item.get(field)):
                    errors.append(f"hypotheses[{index}] needs {field}")
            for field in ("supporting_evidence", "weakening_evidence"):
                if not _list_of_text(item.get(field)) or not item[field]:
                    errors.append(f"hypotheses[{index}] needs non-empty {field}")

    principles = payload.get("principles")
    if not isinstance(principles, list):
        errors.append("principles must be a list")
    else:
        for index, item in enumerate(principles):
            if not isinstance(item, dict):
                errors.append(f"principles[{index}] must be an object")
                continue
            if not _nonempty_text(item.get("id")):
                errors.append(f"principles[{index}] needs id")
            if item.get("evidence_class") not in PRINCIPLE_CLASSES:
                errors.append(f"principles[{index}] has invalid evidence_class")
            if not _list_of_text(item.get("source_refs")) or not item["source_refs"]:
                errors.append(f"principles[{index}] needs source_refs")

    experiment = payload.get("experiment")
    if not isinstance(experiment, dict):
        errors.append("experiment must be an object")
    else:
        for field in ("fixed_conditions", "primary_variable", "prediction", "falsifier", "cost_or_risk"):
            if not _nonempty_text(experiment.get(field)):
                errors.append(f"experiment needs {field}")

    recommendation = payload.get("recommendation")
    if not isinstance(recommendation, dict):
        errors.append("recommendation must be an object")
    else:
        for field in ("next_action", "belief_update"):
            if not _nonempty_text(recommendation.get(field)):
                errors.append(f"recommendation needs {field}")
        confidence = recommendation.get("confidence")
        if not isinstance(confidence, (int, float)) or isinstance(confidence, bool) or not 0 <= confidence <= 1:
            errors.append("recommendation confidence must be a number in [0, 1]")
        if recommendation.get("reasoning_mode") not in REASONING_MODES:
            errors.append("recommendation has invalid reasoning_mode")

    provenance = payload.get("provenance")
    provenance_ids: set[str] = set()
    if not isinstance(provenance, list) or not provenance:
        errors.append("provenance must be a non-empty list")
    else:
        for index, item in enumerate(provenance):
            if not isinstance(item, dict):
                errors.append(f"provenance[{index}] must be an object")
                continue
            evidence_id = item.get("evidence_id")
            if not _nonempty_text(evidence_id):
                errors.append(f"provenance[{index}] needs evidence_id")
            elif evidence_id in provenance_ids:
                errors.append(f"duplicate provenance evidence_id: {evidence_id}")
            else:
                provenance_ids.add(evidence_id)
            if not _nonempty_text(item.get("source")):
                errors.append(f"provenance[{index}] needs source")
            if not _nonempty_text(item.get("locator")):
                errors.append(f"provenance[{index}] needs locator")

    referenced_ids: set[str] = set()
    if isinstance(observations, list):
        for item in observations:
            if isinstance(item, dict):
                referenced_ids.update(_collect_ids(item.get("evidence_ids")))
    if isinstance(hypotheses, list):
        for item in hypotheses:
            if isinstance(item, dict):
                referenced_ids.update(_collect_ids(item.get("supporting_evidence")))
                referenced_ids.update(_collect_ids(item.get("weakening_evidence")))
    if isinstance(principles, list):
        for item in principles:
            if isinstance(item, dict):
                referenced_ids.update(_collect_ids(item.get("source_refs")))
    unresolved = sorted(referenced_ids - provenance_ids)
    if unresolved:
        errors.append("unresolved evidence IDs: " + ", ".join(unresolved))

    return {
        "schema_version": SCHEMA_VERSION,
        "status": "PASS" if not missing_fields and not errors else "FAIL",
        "source_path": source_path,
        "input_sha256": input_sha256,
        "errors": errors,
        "warnings": warnings,
        "missing_fields": missing_fields,
        "unresolved_evidence_ids": unresolved,
        "provenance_count": len(provenance_ids),
        "hypothesis_count": len(hypotheses) if isinstance(hypotheses, list) else 0,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    report = validate_response(args.input)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.json:
        print(json.dumps(report, ensure_ascii=False))
    else:
        print(f"Advisor response validation: {report['status']}")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
