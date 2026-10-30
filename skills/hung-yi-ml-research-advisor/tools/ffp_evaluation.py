"""Guarded replay and evidence checks for the FFP mentor evaluation.

This module does not pretend that a handful of metric CSVs reproduce a model.
It accepts a small, explicit evaluation manifest, verifies every referenced
artifact, builds a blind transition packet with the future outcome withheld,
and reconciles an advisor response without promoting it to a validation claim.
The tool is intentionally standard-library only so the evidence gate can run
before the full NumPy/Pandas/Matplotlib/Torch mentor analysis tier.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


TOOL_VERSION = "1.2.0"
SCHEMA_VERSION = "ffp-evaluation-input.v1"
REPORT_SCHEMA_VERSION = "ffp-evaluation-report.v1"
REQUIRED_ADVICE_FIELDS = (
    "diagnosis",
    "next_experiment",
    "mechanism",
    "metrics",
    "stop_rollback",
    "alternatives",
    "confidence",
    "evidence_ids",
)
_FUTURE_KEYS = {"actual_outcome", "future_result", "future_metrics", "next_version_result"}
_DISCOVERY_SUFFIXES = {".csv", ".json", ".yaml", ".yml", ".md", ".pdf", ".pptx", ".docx", ".ipynb", ".py", ".xlsx"}
_DISCOVERY_TOKENS = ("ffp", "orchid", "repeated", "25_10_08")
_DISCOVERY_SKIP = {".git", ".venv", "venv", "node_modules", "__pycache__", ".cache"}


def _load_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"JSON root must be an object: {path}")
    return payload


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def discover_evidence(root: Path) -> dict[str, Any]:
    """Create a conservative artifact inventory; never infer a version label."""

    if not root.is_dir():
        raise FileNotFoundError(root)
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in _DISCOVERY_SUFFIXES:
            continue
        if any(part.lower() in _DISCOVERY_SKIP for part in path.parts):
            continue
        haystack = path.name.lower()
        if not any(token in haystack for token in _DISCOVERY_TOKENS):
            continue
        files.append(path)
    artifacts: list[dict[str, Any]] = []
    for index, path in enumerate(sorted(files, key=lambda item: str(item).lower()), 1):
        suffix = path.suffix.lower()
        kind = "metrics" if path.name.lower().startswith("repeated") and suffix == ".csv" else "document" if suffix in {".pdf", ".pptx", ".docx", ".md"} else "table" if suffix in {".csv", ".xlsx"} else "artifact"
        artifacts.append(
            {
                "artifact_id": f"discovered-{index:04d}",
                "kind": kind,
                "version": "unknown",
                "path": str(path.resolve()),
                "sha256": _sha256(path),
                "provenance": {"discovery_root": str(root.resolve()), "method": "filename-token inventory"},
            }
        )
    return {
        "schema_version": SCHEMA_VERSION,
        "project_id": "FFP",
        "required_versions": ["FFP", "FFP_simple", "FFP_new_mlp"],
        "artifacts": artifacts,
        "transitions": [],
        "discovery_boundary": "Inventory only: version labels, recipe semantics, data splits, transition outcomes, and runnable source must be mapped by a human before replay.",
    }


def scaffold_manifest(discovery_path: Path) -> dict[str, Any]:
    """Build a human-mapping template from conservative discovery output.

    Discovery can prove that files exist and have hashes, but it cannot infer
    which file belongs to FFP/FFP_simple/FFP_new_mlp or reconstruct a split.
    The scaffold therefore leaves versions, evidence links, and outcomes
    explicitly incomplete so the normal audit remains ``INPUT_MISSING``.
    """

    payload = _load_json(discovery_path)
    if payload.get("schema_version") != SCHEMA_VERSION:
        raise ValueError(f"expected discovery schema {SCHEMA_VERSION}")
    raw_artifacts = payload.get("artifacts")
    if not isinstance(raw_artifacts, list):
        raise ValueError("discovery artifacts must be a list")
    artifacts: list[dict[str, Any]] = []
    for item in raw_artifacts:
        if not isinstance(item, dict):
            continue
        copied = dict(item)
        copied["version"] = "unknown"
        provenance = dict(copied.get("provenance") or {})
        provenance["scaffold_source"] = str(discovery_path)
        provenance["mapping_status"] = "HUMAN_MAPPING_REQUIRED"
        copied["provenance"] = provenance
        artifacts.append(copied)
    transitions = [
        {
            "transition_id": "FFP_to_FFP_simple",
            "from_version": "FFP",
            "to_version": "FFP_simple",
            "observed": {"recipe": {}, "data_split": {}, "metrics": {}, "evidence_ids": []},
            "mapping_status": "HUMAN_MAPPING_REQUIRED",
        },
        {
            "transition_id": "FFP_simple_to_FFP_new_mlp",
            "from_version": "FFP_simple",
            "to_version": "FFP_new_mlp",
            "observed": {"recipe": {}, "data_split": {}, "metrics": {}, "evidence_ids": []},
            "mapping_status": "HUMAN_MAPPING_REQUIRED",
        },
    ]
    return {
        "schema_version": SCHEMA_VERSION,
        "project_id": "FFP",
        "required_versions": ["FFP", "FFP_simple", "FFP_new_mlp"],
        "artifacts": artifacts,
        "transitions": transitions,
        "mapping_status": "HUMAN_MAPPING_REQUIRED",
        "discovery_source": str(discovery_path),
        "discovery_boundary": payload.get("discovery_boundary"),
        "next_actions": [
            "assign each artifact to a version only from a human-verified project record",
            "record dataset split, recipe, metrics, and evidence_ids for each observed transition",
            "add actual_outcome only after the transition evidence is frozen; then rerun audit",
        ],
    }


def _artifact_report(artifact: dict[str, Any], *, manifest_path: Path) -> dict[str, Any]:
    artifact_id = artifact.get("artifact_id")
    raw_path = artifact.get("path")
    result: dict[str, Any] = {
        "artifact_id": artifact_id,
        "version": artifact.get("version"),
        "kind": artifact.get("kind"),
        "path": raw_path,
        "status": "INVALID",
    }
    if not isinstance(raw_path, str) or not raw_path:
        result["reason"] = "path is required"
        return result
    path = Path(raw_path)
    if not path.is_absolute():
        path = manifest_path.parent / path
    result["resolved_path"] = str(path.resolve())
    if not path.is_file():
        result["status"] = "MISSING"
        result["reason"] = "artifact file does not exist"
        return result
    actual = _sha256(path)
    result["actual_sha256"] = actual
    expected = artifact.get("sha256")
    if not isinstance(expected, str) or len(expected) != 64:
        result["status"] = "UNHASHED"
        result["reason"] = "a SHA-256 is required for reproducible replay"
        return result
    if expected.lower() != actual:
        result["status"] = "HASH_MISMATCH"
        result["reason"] = "artifact changed after manifest capture"
        result["expected_sha256"] = expected
        return result
    result["status"] = "VERIFIED"
    result["sha256"] = actual
    return result


def _validate_transition_shape(transition: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for key in ("transition_id", "from_version", "to_version"):
        if not isinstance(transition.get(key), str) or not transition[key]:
            errors.append(f"transition missing {key}")
    observed = transition.get("observed")
    if not isinstance(observed, dict):
        errors.append("transition observed must be an object")
    elif not isinstance(observed.get("evidence_ids"), list):
        errors.append("transition observed.evidence_ids must be a list")
    if "actual_outcome" not in transition:
        errors.append("transition missing actual_outcome")
    return errors


def audit_input(input_path: Path) -> dict[str, Any]:
    """Audit an FFP manifest without executing training or model code."""

    payload = _load_json(input_path)
    if payload.get("schema_version") != SCHEMA_VERSION:
        raise ValueError(f"expected {SCHEMA_VERSION}")
    required_versions = payload.get("required_versions", ["FFP", "FFP_simple", "FFP_new_mlp"])
    if not isinstance(required_versions, list) or not all(isinstance(item, str) for item in required_versions):
        raise ValueError("required_versions must be a list of strings")
    artifacts = payload.get("artifacts")
    transitions = payload.get("transitions")
    if not isinstance(artifacts, list) or not isinstance(transitions, list):
        raise ValueError("artifacts and transitions must be lists")

    artifact_ids: set[str] = set()
    artifact_reports: list[dict[str, Any]] = []
    duplicate_artifacts: list[str] = []
    for item in artifacts:
        if not isinstance(item, dict):
            raise ValueError("every artifact must be an object")
        artifact_id = item.get("artifact_id")
        if not isinstance(artifact_id, str) or not artifact_id:
            raise ValueError("every artifact needs artifact_id")
        if artifact_id in artifact_ids:
            duplicate_artifacts.append(artifact_id)
        artifact_ids.add(artifact_id)
        artifact_reports.append(_artifact_report(item, manifest_path=input_path))

    transition_ids: set[str] = set()
    transition_errors: dict[str, list[str]] = {}
    versions: set[str] = set()
    for item in transitions:
        if not isinstance(item, dict):
            raise ValueError("every transition must be an object")
        transition_id = str(item.get("transition_id", "<missing>"))
        if transition_id in transition_ids:
            transition_errors.setdefault(transition_id, []).append("duplicate transition_id")
        transition_ids.add(transition_id)
        transition_errors.setdefault(transition_id, []).extend(_validate_transition_shape(item))
        for key in ("from_version", "to_version"):
            if isinstance(item.get(key), str):
                versions.add(item[key])
        observed = item.get("observed")
        if isinstance(observed, dict):
            evidence_ids = observed.get("evidence_ids", [])
            for evidence_id in evidence_ids if isinstance(evidence_ids, list) else []:
                if evidence_id not in artifact_ids:
                    transition_errors[transition_id].append(f"unknown evidence_id: {evidence_id}")

    missing_versions = sorted(set(required_versions) - versions - {item.get("version") for item in artifacts if isinstance(item, dict)})
    actionable_errors = [
        f"{transition_id}: {error}"
        for transition_id, errors in transition_errors.items()
        for error in errors
        if error
    ]
    artifact_problems = [
        {"artifact_id": item.get("artifact_id"), "status": item.get("status"), "reason": item.get("reason")}
        for item in artifact_reports
        if item.get("status") != "VERIFIED"
    ]
    status = "READY" if not missing_versions and not actionable_errors and not artifact_problems and not duplicate_artifacts else "INPUT_MISSING"
    return {
        "schema_version": REPORT_SCHEMA_VERSION,
        "tool": "ffp_evaluation",
        "tool_version": TOOL_VERSION,
        "input_path": str(input_path),
        "project_id": payload.get("project_id"),
        "status": status,
        "validation_label": "NOT_VALIDATED",
        "required_versions": required_versions,
        "observed_versions": sorted(versions),
        "missing_versions": missing_versions,
        "artifacts": artifact_reports,
        "artifact_problems": artifact_problems,
        "transition_errors": actionable_errors,
        "duplicate_artifacts": sorted(duplicate_artifacts),
        "next_actions": [
            "supply versioned source code, data split, recipe, metrics, error records, and reasons for every required version",
            "freeze the mentor version and run blind replay before reading actual_outcome",
            "run one selected intervention in an isolated sandbox before promoting any claim",
        ] if status != "READY" else [
            "freeze mentor version and build blind packets",
            "obtain human judgment on advice quality before assigning FFP_VALIDATED",
        ],
    }


def _find_transition(payload: dict[str, Any], transition_id: str) -> dict[str, Any]:
    for transition in payload.get("transitions", []):
        if isinstance(transition, dict) and transition.get("transition_id") == transition_id:
            return transition
    raise ValueError(f"transition not found: {transition_id}")


def build_blind_packet(input_path: Path, transition_id: str) -> dict[str, Any]:
    """Build an advice packet that cannot contain the next-version outcome."""

    payload = _load_json(input_path)
    if payload.get("schema_version") != SCHEMA_VERSION:
        raise ValueError(f"expected {SCHEMA_VERSION}")
    transition = _find_transition(payload, transition_id)
    shape_errors = _validate_transition_shape(transition)
    if "transition missing actual_outcome" in shape_errors:
        raise ValueError("blind replay requires a recorded actual_outcome, which will remain withheld")
    observed = transition["observed"]
    evidence_ids = observed.get("evidence_ids", [])
    artifacts = {item.get("artifact_id"): item for item in payload.get("artifacts", []) if isinstance(item, dict)}
    artifact_reports = [_artifact_report(artifacts[evidence_id], manifest_path=input_path) for evidence_id in evidence_ids if evidence_id in artifacts]
    unknown = [evidence_id for evidence_id in evidence_ids if evidence_id not in artifacts]
    unverified = [item["artifact_id"] for item in artifact_reports if item.get("status") != "VERIFIED"]
    future_fields = sorted(key for key in transition if key in _FUTURE_KEYS)
    if unknown or unverified:
        status = "INPUT_MISSING"
    else:
        status = "READY_FOR_ADVICE"
    public_transition = {
        "transition_id": transition["transition_id"],
        "from_version": transition["from_version"],
        "to_version": transition["to_version"],
        "observed": observed,
    }
    return {
        "schema_version": REPORT_SCHEMA_VERSION,
        "tool": "ffp_evaluation",
        "tool_version": TOOL_VERSION,
        "status": status,
        "validation_label": "NOT_VALIDATED",
        "transition": public_transition,
        "allowed_evidence_ids": [item["artifact_id"] for item in artifact_reports if item.get("status") == "VERIFIED"],
        "artifact_refs": [
            {key: item.get(key) for key in ("artifact_id", "version", "kind", "sha256", "resolved_path")}
            for item in artifact_reports
            if item.get("status") == "VERIFIED"
        ],
        "leakage_check": {
            "post_transition_outcome_withheld": not any(key in public_transition for key in _FUTURE_KEYS),
            "future_fields_removed": future_fields,
            "unknown_evidence_ids": unknown,
            "unverified_evidence_ids": unverified,
        },
    }


def reconcile_advice(input_path: Path, advice_path: Path, transition_id: str) -> dict[str, Any]:
    """Check advice contract and traceability; require human validation."""

    payload = _load_json(input_path)
    advice = _load_json(advice_path)
    transition = _find_transition(payload, transition_id)
    observed = transition.get("observed", {})
    allowed = set(observed.get("evidence_ids", [])) if isinstance(observed, dict) else set()
    missing_fields = [field for field in REQUIRED_ADVICE_FIELDS if field not in advice]
    evidence_ids = advice.get("evidence_ids", [])
    unknown_evidence = sorted(set(evidence_ids) - allowed) if isinstance(evidence_ids, list) else ["<evidence_ids must be a list>"]
    confidence = advice.get("confidence")
    confidence_error = not isinstance(confidence, (int, float)) or not 0 <= float(confidence) <= 1
    contract_errors = list(missing_fields)
    if unknown_evidence:
        contract_errors.append("unknown evidence ids")
    if confidence_error:
        contract_errors.append("confidence must be a number in [0, 1]")
    return {
        "schema_version": REPORT_SCHEMA_VERSION,
        "tool": "ffp_evaluation",
        "tool_version": TOOL_VERSION,
        "status": "REVIEW_REQUIRED",
        "validation_label": "NOT_VALIDATED",
        "transition_id": transition_id,
        "contract_errors": contract_errors,
        "traceability": {"allowed_evidence_ids": sorted(allowed), "used_evidence_ids": evidence_ids, "unknown_evidence_ids": unknown_evidence},
        "human_judgment_required": True,
        "validation_boundary": "A single replay cannot establish cross-project validity; require human judgment and an isolated sandbox result before FFP_VALIDATED.",
    }


def _emit(payload: dict[str, Any], output: Path | None, as_json: bool) -> None:
    encoded = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(encoded, encoding="utf-8")
    if as_json or output is None:
        sys.stdout.write(json.dumps(payload, ensure_ascii=False) + "\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="operation", required=True)
    audit = sub.add_parser("audit")
    audit.add_argument("--input", type=Path, required=True)
    audit.add_argument("--output", type=Path)
    audit.add_argument("--json", action="store_true")
    discover = sub.add_parser("discover")
    discover.add_argument("--root", type=Path, required=True)
    discover.add_argument("--output", type=Path)
    discover.add_argument("--json", action="store_true")
    scaffold = sub.add_parser("scaffold", help="create a human-mapping FFP manifest from discovery output")
    scaffold.add_argument("--discovery", type=Path, required=True)
    scaffold.add_argument("--output", type=Path)
    scaffold.add_argument("--json", action="store_true")
    blind = sub.add_parser("blind-pack")
    blind.add_argument("--input", type=Path, required=True)
    blind.add_argument("--transition-id", required=True)
    blind.add_argument("--output", type=Path)
    blind.add_argument("--json", action="store_true")
    reconcile = sub.add_parser("reconcile")
    reconcile.add_argument("--input", type=Path, required=True)
    reconcile.add_argument("--advice", type=Path, required=True)
    reconcile.add_argument("--transition-id", required=True)
    reconcile.add_argument("--output", type=Path)
    reconcile.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.operation == "audit":
            payload = audit_input(args.input)
        elif args.operation == "discover":
            payload = discover_evidence(args.root)
        elif args.operation == "scaffold":
            payload = scaffold_manifest(args.discovery)
        elif args.operation == "blind-pack":
            payload = build_blind_packet(args.input, args.transition_id)
        else:
            payload = reconcile_advice(args.input, args.advice, args.transition_id)
        _emit(payload, args.output, args.json)
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.exit(2, f"error: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
