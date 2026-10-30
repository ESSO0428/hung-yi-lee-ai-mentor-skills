"""Deterministic dataset split and leakage audit for mentor recipe decisions.

This is a gate, not a model-quality predictor. It catches row, group, and
exact-content overlap across train/validation/test before interpreting curves
or changing a recipe. It intentionally uses the standard library so it can run
even when the optional NumPy/Pandas/Matplotlib profile is not loaded.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable


TOOL_VERSION = "1.0.0"
SCHEMA_VERSION = "dataset-split-audit.v1"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _load_rows(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        raise FileNotFoundError(path)
    if path.suffix.lower() == ".json":
        payload = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(payload, dict):
            payload = payload.get("rows", payload.get("examples"))
        if not isinstance(payload, list) or not all(isinstance(row, dict) for row in payload):
            raise ValueError("JSON input must be a list of row objects or an object with rows/examples")
        return [dict(row) for row in payload]
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def _locations(rows: Iterable[dict[str, Any]], column: str) -> dict[str, set[str]]:
    locations: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        value = str(row.get(column, "")).strip()
        split = str(row.get("split", "")).strip()
        if value and split:
            locations[value].add(split)
    return locations


def _overlap_rows(rows: Iterable[dict[str, Any]], column: str, kind: str) -> list[dict[str, Any]]:
    locations = _locations(rows, column)
    return [
        {"kind": kind, "column": column, "value": value, "splits": sorted(splits)}
        for value, splits in sorted(locations.items())
        if len(splits) > 1
    ]


def _label_distribution(rows: Iterable[dict[str, Any]], label_column: str) -> dict[str, dict[str, float]]:
    counts: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    totals: dict[str, int] = defaultdict(int)
    for row in rows:
        split = str(row.get("split", "")).strip()
        label = str(row.get(label_column, "")).strip()
        if split and label:
            counts[split][label] += 1
            totals[split] += 1
    return {
        split: {label: counts[split][label] / totals[split] for label in sorted(counts[split])}
        for split in sorted(counts)
        if totals[split]
    }


def audit_dataset(
    path: Path,
    *,
    id_column: str = "sample_id",
    split_column: str = "split",
    group_column: str = "group_id",
    content_hash_column: str = "content_hash",
    label_column: str = "label",
    label_gap_warning: float = 0.2,
) -> dict[str, Any]:
    """Return a reproducible leakage report; no training or inference occurs."""

    rows = _load_rows(path)
    if split_column != "split":
        rows = [{**row, "split": row.get(split_column, "")} for row in rows]
    columns = set().union(*(row.keys() for row in rows)) if rows else set()
    required = {id_column, split_column}
    missing_required = sorted(required - columns)
    report: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "tool": "dataset_split_audit",
        "tool_version": TOOL_VERSION,
        "input_path": str(path),
        "provenance": {
            "input_sha256": _sha256(path) if path.is_file() else None,
            "parameters": {
                "id_column": id_column,
                "split_column": split_column,
                "group_column": group_column,
                "content_hash_column": content_hash_column,
                "label_column": label_column,
                "label_gap_warning": label_gap_warning,
            },
        },
        "row_count": len(rows),
        "missing_required_columns": missing_required,
        "missing_optional_columns": sorted({group_column, content_hash_column, label_column} - columns),
        "split_counts": {},
        "label_distribution": {},
        "violations": [],
        "warnings": [],
    }
    if missing_required:
        report["status"] = "INPUT_INVALID"
        report["warnings"].append("required columns are missing; no leakage conclusion is possible")
        return report
    if not rows:
        report["status"] = "INPUT_INVALID"
        report["warnings"].append("input has no rows")
        return report

    blank_rows = [index + 2 for index, row in enumerate(rows) if not str(row.get(split_column, "")).strip() or not str(row.get(id_column, "")).strip()]
    if blank_rows:
        report["violations"].append({"kind": "blank_identity_or_split", "rows": blank_rows[:100], "truncated": len(blank_rows) > 100})
    split_counts: dict[str, int] = defaultdict(int)
    for row in rows:
        split = str(row.get(split_column, "")).strip()
        if split:
            split_counts[split] += 1
    report["split_counts"] = {key: split_counts[key] for key in sorted(split_counts)}

    report["violations"].extend(_overlap_rows(rows, id_column, "sample_id_overlap"))
    if group_column in columns:
        report["violations"].extend(_overlap_rows(rows, group_column, "group_overlap"))
    if content_hash_column in columns:
        report["violations"].extend(_overlap_rows(rows, content_hash_column, "content_hash_overlap"))

    if label_column in columns:
        distribution = _label_distribution(rows, label_column)
        report["label_distribution"] = distribution
        labels = sorted({label for values in distribution.values() for label in values})
        gaps = {
            label: max((distribution.get(split, {}).get(label, 0.0) for split in distribution), default=0.0)
            - min((distribution.get(split, {}).get(label, 0.0) for split in distribution), default=0.0)
            for label in labels
        }
        report["label_distribution_gap"] = gaps
        if any(gap > label_gap_warning for gap in gaps.values()):
            report["warnings"].append("label distribution differs materially across splits; inspect stratification and sample size")
    report["status"] = "FAIL" if report["violations"] else "PASS"
    return report


def _emit(payload: dict[str, Any], output: Path | None, as_json: bool) -> None:
    encoded = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(encoded, encoding="utf-8")
    if as_json or output is None:
        sys.stdout.write(json.dumps(payload, ensure_ascii=False) + "\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--id-column", default="sample_id")
    parser.add_argument("--split-column", default="split")
    parser.add_argument("--group-column", default="group_id")
    parser.add_argument("--content-hash-column", default="content_hash")
    parser.add_argument("--label-column", default="label")
    parser.add_argument("--label-gap-warning", type=float, default=0.2)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        payload = audit_dataset(
            args.input,
            id_column=args.id_column,
            split_column=args.split_column,
            group_column=args.group_column,
            content_hash_column=args.content_hash_column,
            label_column=args.label_column,
            label_gap_warning=args.label_gap_warning,
        )
        _emit(payload, args.output, args.json)
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.exit(2, f"error: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
