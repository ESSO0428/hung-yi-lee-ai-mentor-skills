"""Deterministic summaries for AI recipe evaluation.

The tool deliberately reports measurements; it does not decide which ML
intervention is correct. The mentor skill uses these outputs with source-linked
principles and competing hypotheses.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
from math import isfinite
from pathlib import Path
from statistics import fmean
from typing import Any


TOOL_VERSION = "1.0.0"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _read_rows(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        raise FileNotFoundError(path)
    if path.suffix.lower() == ".json":
        payload = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(payload, dict):
            payload = payload.get("rows", payload.get("metrics", payload.get("examples")))
        if not isinstance(payload, list) or not all(isinstance(row, dict) for row in payload):
            raise ValueError(f"JSON input must contain a list of row objects: {path}")
        return [dict(row) for row in payload]
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def _number(value: Any, *, field: str) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{field} must be numeric, got {value!r}") from exc
    if not isfinite(number):
        raise ValueError(f"{field} must be finite")
    return number


def _metric_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    if not rows:
        raise ValueError("input has no rows")
    result: list[dict[str, Any]] = []
    long_form = "metric" in rows[0] and "value" in rows[0]
    for row_index, row in enumerate(rows, start=1):
        run_id = str(row.get("run_id") or row.get("run") or "default")
        split = str(row.get("split") or "unspecified")
        step = _number(row.get("step", row.get("epoch", row_index)), field="step")
        if long_form:
            value = _number(row.get("value"), field="value")
            metric = str(row.get("metric") or "metric")
            result.append({"run_id": run_id, "step": step, "split": split, "metric": metric, "value": value})
            continue
        for metric, raw_value in row.items():
            if metric in {"run_id", "run", "step", "epoch", "split"} or raw_value in (None, ""):
                continue
            try:
                value = _number(raw_value, field=metric)
            except ValueError:
                continue
            result.append({"run_id": run_id, "step": step, "split": split, "metric": metric, "value": value})
    if not result:
        raise ValueError("input has no numeric metrics")
    return result


def _metric_key(row: dict[str, Any]) -> str:
    split = row["split"]
    return f"{split}/{row['metric']}" if split != "unspecified" else str(row["metric"])


def _objectives(raw: str | None) -> dict[str, str]:
    if not raw:
        return {}
    parsed = json.loads(raw)
    if not isinstance(parsed, dict):
        raise ValueError("--objective must be a JSON object mapping metric keys to min or max")
    result: dict[str, str] = {}
    for key, value in parsed.items():
        if value not in {"min", "max"}:
            raise ValueError(f"objective for {key} must be min or max")
        result[str(key)] = value
    return result


def _best(values: list[dict[str, Any]], objective: str | None) -> tuple[float | None, float | None]:
    if not objective:
        return None, None
    selected = min(values, key=lambda row: row["value"]) if objective == "min" else max(values, key=lambda row: row["value"])
    return selected["value"], selected["step"]


def _provenance(
    tool: str,
    inputs: list[Path],
    args: dict[str, Any],
    outputs: list[Path] | None = None,
) -> dict[str, Any]:
    output_paths = outputs or []
    return {
        "schema_version": "recipe-decision-provenance.v1",
        "tool": "recipe_tools",
        "tool_version": TOOL_VERSION,
        "operation": tool,
        "input_paths": [str(path) for path in inputs],
        "input_sha256": {str(path): _sha256(path) for path in inputs},
        "output_paths": [str(path) for path in output_paths],
        "output_sha256": {str(path): _sha256(path) for path in output_paths if path.is_file()},
        "parameters": args,
    }


def summarize_metrics(path: Path, objective_map: dict[str, str]) -> dict[str, Any]:
    rows = _metric_rows(_read_rows(path))
    groups: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for row in rows:
        groups.setdefault((row["run_id"], _metric_key(row)), []).append(row)
    summaries: list[dict[str, Any]] = []
    for (run_id, key), values in sorted(groups.items()):
        objective = objective_map.get(key)
        best_value, best_step = _best(values, objective)
        ordered = sorted(values, key=lambda item: item["step"])
        summaries.append(
            {
                "run_id": run_id,
                "metric_key": key,
                "objective": objective,
                "count": len(values),
                "min": min(item["value"] for item in values),
                "max": max(item["value"] for item in values),
                "mean": fmean(item["value"] for item in values),
                "first_value": ordered[0]["value"],
                "last_value": ordered[-1]["value"],
                "best_value": best_value,
                "best_step": best_step,
            }
        )
    return {"summaries": summaries}


def compare_runs(baseline: Path, candidate: Path, objective_map: dict[str, str]) -> dict[str, Any]:
    base_rows = _metric_rows(_read_rows(baseline))
    cand_rows = _metric_rows(_read_rows(candidate))
    base_by_key: dict[str, list[dict[str, Any]]] = {}
    cand_by_key: dict[str, list[dict[str, Any]]] = {}
    for row in base_rows:
        base_by_key.setdefault(_metric_key(row), []).append(row)
    for row in cand_rows:
        cand_by_key.setdefault(_metric_key(row), []).append(row)
    comparisons: list[dict[str, Any]] = []
    for key in sorted(base_by_key.keys() & cand_by_key.keys()):
        objective = objective_map.get(key)
        base_best, _ = _best(base_by_key[key], objective)
        cand_best, _ = _best(cand_by_key[key], objective)
        delta = round(cand_best - base_best, 12) if base_best is not None and cand_best is not None else None
        if delta is None or objective is None:
            direction = "unknown"
        elif delta == 0:
            direction = "unchanged"
        elif (objective == "max" and delta > 0) or (objective == "min" and delta < 0):
            direction = "improved"
        else:
            direction = "worsened"
        comparisons.append(
            {
                "metric_key": key,
                "objective": objective,
                "baseline_best": base_best,
                "candidate_best": cand_best,
                "delta": delta,
                "direction": direction,
            }
        )
    return {"comparisons": comparisons}


def _truthy(value: Any) -> bool:
    return str(value).strip().lower() in {"1", "true", "yes", "y", "correct"}


def error_breakdown(path: Path, group_by: str) -> dict[str, Any]:
    rows = _read_rows(path)
    if not rows:
        raise ValueError("input has no rows")
    if group_by not in rows[0]:
        raise ValueError(f"group-by field not found: {group_by}")
    grouped: dict[str, list[bool]] = {}
    for row in rows:
        if "correct" in row:
            is_error = not _truthy(row["correct"])
        elif "error" in row or "is_error" in row:
            is_error = _truthy(row.get("error", row.get("is_error")))
        elif "label" in row and "prediction" in row:
            is_error = str(row["label"]) != str(row["prediction"])
        else:
            raise ValueError("rows need correct, error/is_error, or label plus prediction")
        grouped.setdefault(str(row[group_by]), []).append(is_error)
    groups = []
    for group, errors in sorted(grouped.items()):
        total = len(errors)
        error_count = sum(errors)
        groups.append({"group": group, "total": total, "errors": error_count, "error_rate": error_count / total})
    return {"groups": groups}


def _flatten(value: Any, prefix: str = "") -> dict[str, Any]:
    if isinstance(value, dict):
        flattened: dict[str, Any] = {}
        for key in sorted(value):
            child = f"{prefix}.{key}" if prefix else str(key)
            flattened.update(_flatten(value[key], child))
        return flattened
    if isinstance(value, list):
        flattened = {}
        for index, child_value in enumerate(value):
            flattened.update(_flatten(child_value, f"{prefix}[{index}]"))
        return flattened
    return {prefix: value}


def _read_json_object(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"JSON config must be an object: {path}")
    return payload


def config_diff(baseline: Path, candidate: Path) -> dict[str, Any]:
    base = _flatten(_read_json_object(baseline))
    cand = _flatten(_read_json_object(candidate))
    changes: list[dict[str, Any]] = []
    for path in sorted(base.keys() | cand.keys()):
        if path not in base:
            change = "added"
        elif path not in cand:
            change = "removed"
        elif base[path] != cand[path]:
            change = "changed"
        else:
            continue
        changes.append({"path": path, "change": change, "baseline": base.get(path), "candidate": cand.get(path)})
    return {"changes": changes}


def plot_metrics(path: Path, metric_key: str, output_svg: Path) -> dict[str, Any]:
    rows = _metric_rows(_read_rows(path))
    points = sorted(
        ({"step": row["step"], "value": row["value"]} for row in rows if _metric_key(row) == metric_key),
        key=lambda point: point["step"],
    )
    if not points:
        raise ValueError(f"metric key not found: {metric_key}")
    width, height, margin = 720, 400, 56
    x_min, x_max = points[0]["step"], points[-1]["step"]
    y_min = min(point["value"] for point in points)
    y_max = max(point["value"] for point in points)
    x_span = x_max - x_min or 1.0
    y_span = y_max - y_min or 1.0

    def x_position(step: float) -> float:
        return margin + ((step - x_min) / x_span) * (width - 2 * margin)

    def y_position(value: float) -> float:
        return height - margin - ((value - y_min) / y_span) * (height - 2 * margin)

    coordinates = [(x_position(point["step"]), y_position(point["value"])) for point in points]
    path_data = " ".join(
        ("M" if index == 0 else "L") + f"{x:.3f},{y:.3f}" for index, (x, y) in enumerate(coordinates)
    )
    circles = "".join(f'<circle cx="{x:.3f}" cy="{y:.3f}" r="3" />' for x, y in coordinates)
    title = html.escape(metric_key)
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}">'
        f'<title>{title}</title>'
        f'<line x1="{margin}" y1="{height-margin}" x2="{width-margin}" y2="{height-margin}" stroke="#333" />'
        f'<line x1="{margin}" y1="{margin}" x2="{margin}" y2="{height-margin}" stroke="#333" />'
        f'<path d="{path_data}" fill="none" stroke="#1769aa" stroke-width="2" />'
        f"{circles}"
        f'<text x="{margin}" y="24" font-family="sans-serif" font-size="16">{title}</text>'
        f"</svg>\n"
    )
    output_svg.parent.mkdir(parents=True, exist_ok=True)
    output_svg.write_text(svg, encoding="utf-8")
    return {
        "metric_key": metric_key,
        "point_count": len(points),
        "min": y_min,
        "max": y_max,
        "svg_path": str(output_svg),
    }


def _write_or_print(payload: dict[str, Any], output: Path | None, as_json: bool) -> None:
    encoded = json.dumps(payload, ensure_ascii=False, indent=2)
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(encoded + "\n", encoding="utf-8")
    if as_json or not output:
        print(json.dumps(payload, ensure_ascii=False))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="operation", required=True)

    summary = subparsers.add_parser("summarize-metrics")
    summary.add_argument("--input", type=Path, required=True)
    summary.add_argument("--objective", help='JSON map such as {"validation/loss":"min"}')
    summary.add_argument("--output", type=Path)
    summary.add_argument("--json", action="store_true")

    compare = subparsers.add_parser("compare-runs")
    compare.add_argument("--baseline", type=Path, required=True)
    compare.add_argument("--candidate", type=Path, required=True)
    compare.add_argument("--objective")
    compare.add_argument("--output", type=Path)
    compare.add_argument("--json", action="store_true")

    errors = subparsers.add_parser("error-breakdown")
    errors.add_argument("--input", type=Path, required=True)
    errors.add_argument("--group-by", required=True)
    errors.add_argument("--output", type=Path)
    errors.add_argument("--json", action="store_true")

    config = subparsers.add_parser("config-diff")
    config.add_argument("--baseline", type=Path, required=True)
    config.add_argument("--candidate", type=Path, required=True)
    config.add_argument("--output", type=Path)
    config.add_argument("--json", action="store_true")

    plot = subparsers.add_parser("plot-metrics")
    plot.add_argument("--input", type=Path, required=True)
    plot.add_argument("--metric-key", required=True)
    plot.add_argument("--output-svg", type=Path, required=True)
    plot.add_argument("--json", action="store_true")

    args = parser.parse_args()
    if args.operation == "summarize-metrics":
        objectives = _objectives(args.objective)
        payload = summarize_metrics(args.input, objectives)
        payload["provenance"] = _provenance("summarize-metrics", [args.input], {"objective": objectives})
        _write_or_print(payload, args.output, args.json)
    elif args.operation == "compare-runs":
        objectives = _objectives(args.objective)
        payload = compare_runs(args.baseline, args.candidate, objectives)
        payload["provenance"] = _provenance(
            "compare-runs",
            [args.baseline, args.candidate],
            {"objective": objectives},
        )
        _write_or_print(payload, args.output, args.json)
    elif args.operation == "error-breakdown":
        payload = error_breakdown(args.input, args.group_by)
        payload["provenance"] = _provenance("error-breakdown", [args.input], {"group_by": args.group_by})
        _write_or_print(payload, args.output, args.json)
    elif args.operation == "config-diff":
        payload = config_diff(args.baseline, args.candidate)
        payload["provenance"] = _provenance("config-diff", [args.baseline, args.candidate], {})
        _write_or_print(payload, args.output, args.json)
    else:
        payload = plot_metrics(args.input, args.metric_key, args.output_svg)
        payload["provenance"] = _provenance(
            "plot-metrics",
            [args.input],
            {"metric_key": args.metric_key},
            outputs=[args.output_svg],
        )
        if args.json:
            print(json.dumps(payload, ensure_ascii=False))
        else:
            print(args.output_svg)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
