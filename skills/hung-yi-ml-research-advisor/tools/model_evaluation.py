"""High-fidelity, reproducible model evaluation for the mentor skill.

This tool deliberately evaluates caller-provided predictions; it never trains a
model or turns a metric into an intervention.  It uses the mentor ``analysis``
profile for tabular loading, bootstrap intervals, calibration, and optional
slice metrics.  Missing dependencies are explicit errors rather than silent
fallbacks.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib
import json
from pathlib import Path
from typing import Any


TOOL_VERSION = "1.1.0"
SCHEMA_VERSION = "model-evaluation.v1"


class OptionalDependencyError(RuntimeError):
    """Raised when the analysis extra is not installed."""


def _require(module_name: str):
    try:
        return importlib.import_module(module_name)
    except ImportError as exc:
        raise OptionalDependencyError(
            f"model evaluation requires {module_name}; install with 'uv sync --extra analysis'"
        ) from exc


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _read_frame(path: Path):
    pd = _require("pandas")
    if not path.is_file():
        raise FileNotFoundError(path)
    if path.suffix.lower() == ".json":
        payload = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(payload, dict):
            payload = payload.get("rows", payload.get("predictions", payload))
        if not isinstance(payload, list):
            raise ValueError("JSON input must contain a list of prediction rows")
        frame = pd.DataFrame(payload)
    else:
        frame = pd.read_csv(path)
    if frame.empty:
        raise ValueError("input has no rows")
    return frame


def _bootstrap_accuracy(correct: Any, *, resamples: int, seed: int, confidence: float = 0.95) -> dict[str, Any]:
    np = _require("numpy")
    values = np.asarray(correct, dtype=float)
    if values.size == 0 or not np.isfinite(values).all():
        raise ValueError("correctness values must be finite and non-empty")
    if resamples < 100:
        raise ValueError("resamples must be at least 100")
    if not 0 < confidence < 1:
        raise ValueError("confidence must be between 0 and 1")
    rng = np.random.default_rng(seed)
    estimates = np.empty(resamples, dtype=float)
    for start in range(0, resamples, 256):
        stop = min(start + 256, resamples)
        indices = rng.integers(0, values.size, size=(stop - start, values.size))
        estimates[start:stop] = values[indices].mean(axis=1)
    alpha = (1 - confidence) / 2
    return {
        "estimate": float(values.mean()),
        "lower": float(np.quantile(estimates, alpha)),
        "upper": float(np.quantile(estimates, 1 - alpha)),
        "confidence": confidence,
        "resamples": resamples,
        "seed": seed,
    }


def _binary_metrics(labels: list[Any], predictions: list[Any], *, positive: Any) -> dict[str, float]:
    np = _require("numpy")
    y = np.asarray([item == positive for item in labels], dtype=bool)
    p = np.asarray([item == positive for item in predictions], dtype=bool)
    tp = int(np.logical_and(y, p).sum())
    tn = int(np.logical_and(~y, ~p).sum())
    fp = int(np.logical_and(~y, p).sum())
    fn = int(np.logical_and(y, ~p).sum())
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    specificity = tn / (tn + fp) if tn + fp else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {
        "true_positive": tp,
        "true_negative": tn,
        "false_positive": fp,
        "false_negative": fn,
        "precision": float(precision),
        "recall": float(recall),
        "specificity": float(specificity),
        "f1": float(f1),
        "balanced_accuracy": float((recall + specificity) / 2),
    }


def _expected_calibration_error(labels: list[Any], scores: Any, *, positive: Any, bins: int = 10) -> dict[str, Any]:
    np = _require("numpy")
    y = np.asarray([item == positive for item in labels], dtype=float)
    probabilities = np.asarray(scores, dtype=float)
    if probabilities.size != y.size or not np.isfinite(probabilities).all():
        raise ValueError("score_column must contain one finite score per row")
    if (probabilities < 0).any() or (probabilities > 1).any():
        raise ValueError("score_column must be in [0, 1]")
    edges = np.linspace(0, 1, bins + 1)
    rows: list[dict[str, Any]] = []
    weighted_gap = 0.0
    for index in range(bins):
        mask = (probabilities >= edges[index]) & (
            probabilities < edges[index + 1] if index < bins - 1 else probabilities <= edges[index + 1]
        )
        count = int(mask.sum())
        if not count:
            continue
        confidence = float(probabilities[mask].mean())
        accuracy = float(y[mask].mean())
        gap = abs(confidence - accuracy)
        weighted_gap += (count / len(y)) * gap
        rows.append({
            "bin": index,
            "lower": float(edges[index]),
            "upper": float(edges[index + 1]),
            "count": count,
            "confidence": confidence,
            "accuracy": accuracy,
            "gap": float(gap),
        })
    return {"expected_calibration_error": float(weighted_gap), "bins": rows}


def _slice_metrics(frame: Any, *, label_column: str, prediction_column: str, group_by: str, positive: Any) -> list[dict[str, Any]]:
    groups: list[dict[str, Any]] = []
    for group, subset in frame.groupby(group_by, dropna=False, sort=True):
        labels = subset[label_column].tolist()
        predictions = subset[prediction_column].tolist()
        correct = [label == prediction for label, prediction in zip(labels, predictions)]
        groups.append({
            "group": str(group),
            "count": len(correct),
            "accuracy": float(sum(correct) / len(correct)),
            **_binary_metrics(labels, predictions, positive=positive),
        })
    return groups


def _multiclass_metrics(labels: list[Any], predictions: list[Any], *, classes: list[Any]) -> dict[str, Any]:
    """Return macro metrics without depending on scikit-learn."""
    per_class: list[dict[str, Any]] = []
    recalls: list[float] = []
    for class_value in classes:
        true_positive = sum(label == class_value and prediction == class_value for label, prediction in zip(labels, predictions))
        false_positive = sum(label != class_value and prediction == class_value for label, prediction in zip(labels, predictions))
        false_negative = sum(label == class_value and prediction != class_value for label, prediction in zip(labels, predictions))
        support = sum(label == class_value for label in labels)
        precision = true_positive / (true_positive + false_positive) if true_positive + false_positive else 0.0
        recall = true_positive / support if support else 0.0
        f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
        if support:
            recalls.append(recall)
        per_class.append({
            "class": str(class_value),
            "support": int(support),
            "precision": float(precision),
            "recall": float(recall),
            "f1": float(f1),
        })
    accuracy = sum(label == prediction for label, prediction in zip(labels, predictions)) / len(labels)
    return {
        "accuracy": float(accuracy),
        "balanced_accuracy": float(sum(recalls) / len(recalls)),
        "macro_precision": float(sum(row["precision"] for row in per_class) / len(per_class)),
        "macro_recall": float(sum(row["recall"] for row in per_class) / len(per_class)),
        "macro_f1": float(sum(row["f1"] for row in per_class) / len(per_class)),
        "per_class": per_class,
    }


def _multiclass_slice_metrics(frame: Any, *, label_column: str, prediction_column: str, group_by: str, classes: list[Any]) -> list[dict[str, Any]]:
    groups: list[dict[str, Any]] = []
    for group, subset in frame.groupby(group_by, dropna=False, sort=True):
        labels = subset[label_column].tolist()
        predictions = subset[prediction_column].tolist()
        local_classes = sorted(set(labels) | set(predictions), key=lambda value: str(value))
        groups.append({"group": str(group), "count": len(labels), **_multiclass_metrics(labels, predictions, classes=local_classes)})
    return groups


def evaluate_classification(
    path: Path,
    *,
    label_column: str,
    prediction_column: str,
    score_column: str | None = None,
    group_by: str | None = None,
    positive_label: Any | None = None,
    resamples: int = 2000,
    seed: int = 0,
) -> dict[str, Any]:
    """Evaluate binary or multiclass predictions with uncertainty and calibration."""
    frame = _read_frame(path)
    required = {label_column, prediction_column}
    missing = sorted(required - set(frame.columns))
    if missing:
        raise ValueError("missing columns: " + ", ".join(missing))
    if score_column is not None and score_column not in frame.columns:
        raise ValueError(f"score_column not found: {score_column}")
    labels = frame[label_column].tolist()
    predictions = frame[prediction_column].tolist()
    classes_values = sorted(set(labels) | set(predictions), key=lambda value: str(value))
    if len(set(labels)) < 2:
        raise ValueError("classification evaluation requires at least two label classes")
    classes = [str(value) for value in classes_values]
    correct = [label == prediction for label, prediction in zip(labels, predictions)]
    binary = len(classes_values) == 2
    if binary:
        if positive_label is None:
            positive_label = sorted(set(labels), key=lambda value: str(value))[-1]
        metrics = _binary_metrics(labels, predictions, positive=positive_label)
        metrics["accuracy"] = float(sum(correct) / len(correct))
    else:
        if score_column:
            raise ValueError("score_column calibration is currently supported only for binary classification")
        metrics = _multiclass_metrics(labels, predictions, classes=classes_values)
    result: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "tool": "model_evaluation",
        "tool_version": TOOL_VERSION,
        "task": "binary_classification" if binary else "multiclass_classification",
        "n": len(labels),
        "classes": classes,
        "positive_label": str(positive_label) if binary else None,
        "metrics": metrics,
        "bootstrap": {"accuracy": _bootstrap_accuracy(correct, resamples=resamples, seed=seed)},
        "groups": (
            _slice_metrics(frame, label_column=label_column, prediction_column=prediction_column, group_by=group_by, positive=positive_label)
            if group_by and binary
            else _multiclass_slice_metrics(frame, label_column=label_column, prediction_column=prediction_column, group_by=group_by, classes=classes_values)
            if group_by
            else []
        ),
        "calibration": None,
        "provenance": {
            "input_path": str(path),
            "input_sha256": _sha256(path),
            "parameters": {
                "label_column": label_column,
                "prediction_column": prediction_column,
                "score_column": score_column,
                "group_by": group_by,
                "positive_label": str(positive_label),
                "resamples": resamples,
                "seed": seed,
            },
        },
    }
    if score_column and binary:
        calibration = _expected_calibration_error(labels, frame[score_column].tolist(), positive=positive_label)
        probabilities = _require("numpy").asarray(frame[score_column].tolist(), dtype=float)
        targets = _require("numpy").asarray([label == positive_label for label in labels], dtype=float)
        result["metrics"]["brier_score"] = float(((probabilities - targets) ** 2).mean())
        result["metrics"]["expected_calibration_error"] = calibration["expected_calibration_error"]
        result["calibration"] = calibration
    return result


def _regression_metrics(actual: Any, predicted: Any) -> dict[str, float]:
    np = _require("numpy")
    y = np.asarray(actual, dtype=float)
    p = np.asarray(predicted, dtype=float)
    errors = p - y
    ss_total = float(((y - y.mean()) ** 2).sum())
    r2 = 0.0 if ss_total == 0.0 else 1.0 - float((errors ** 2).sum()) / ss_total
    return {
        "mae": float(np.abs(errors).mean()),
        "mse": float((errors ** 2).mean()),
        "rmse": float(np.sqrt((errors ** 2).mean())),
        "r2": float(r2),
    }


def _bootstrap_regression_metrics(actual: Any, predicted: Any, *, resamples: int, seed: int) -> dict[str, Any]:
    np = _require("numpy")
    y = np.asarray(actual, dtype=float)
    p = np.asarray(predicted, dtype=float)
    if resamples < 100:
        raise ValueError("resamples must be at least 100")
    rng = np.random.default_rng(seed)
    estimates = {key: np.empty(resamples, dtype=float) for key in ("mae", "mse", "rmse", "r2")}
    for start in range(0, resamples, 256):
        stop = min(start + 256, resamples)
        indices = rng.integers(0, y.size, size=(stop - start, y.size))
        ys = y[indices]
        ps = p[indices]
        errors = ps - ys
        mse = (errors ** 2).mean(axis=1)
        total = ((ys - ys.mean(axis=1, keepdims=True)) ** 2).sum(axis=1)
        residual = (errors ** 2).sum(axis=1)
        r2 = np.zeros_like(total)
        valid_total = total > 0.0
        r2[valid_total] = 1.0 - residual[valid_total] / total[valid_total]
        estimates["mae"][start:stop] = np.abs(errors).mean(axis=1)
        estimates["mse"][start:stop] = mse
        estimates["rmse"][start:stop] = np.sqrt(mse)
        estimates["r2"][start:stop] = r2
    result: dict[str, Any] = {}
    baseline = _regression_metrics(y, p)
    alpha = 0.025
    for key, values in estimates.items():
        result[key] = {
            "estimate": float(baseline[key]),
            "lower": float(np.quantile(values, alpha)),
            "upper": float(np.quantile(values, 1 - alpha)),
            "confidence": 0.95,
            "resamples": resamples,
            "seed": seed,
        }
    return result


def evaluate_regression(
    path: Path,
    *,
    label_column: str,
    prediction_column: str,
    group_by: str | None = None,
    resamples: int = 2000,
    seed: int = 0,
) -> dict[str, Any]:
    """Evaluate regression predictions with error metrics and row bootstrap intervals."""
    frame = _read_frame(path)
    required = {label_column, prediction_column} | ({group_by} if group_by else set())
    missing = sorted(required - set(frame.columns))
    if missing:
        raise ValueError("missing columns: " + ", ".join(missing))
    pd = _require("pandas")
    frame[label_column] = pd.to_numeric(frame[label_column], errors="coerce")
    frame[prediction_column] = pd.to_numeric(frame[prediction_column], errors="coerce")
    if frame[[label_column, prediction_column]].isna().any().any():
        raise ValueError("regression label and prediction columns must be finite numeric values")
    actual = frame[label_column].to_numpy(dtype=float)
    predicted = frame[prediction_column].to_numpy(dtype=float)
    if not _require("numpy").isfinite(actual).all() or not _require("numpy").isfinite(predicted).all():
        raise ValueError("regression label and prediction columns must be finite numeric values")
    groups: list[dict[str, Any]] = []
    if group_by:
        for group, subset in frame.groupby(group_by, dropna=False, sort=True):
            groups.append({"group": str(group), "count": len(subset), **_regression_metrics(subset[label_column], subset[prediction_column])})
    return {
        "schema_version": SCHEMA_VERSION,
        "tool": "model_evaluation",
        "tool_version": TOOL_VERSION,
        "task": "regression",
        "n": len(frame),
        "metrics": _regression_metrics(actual, predicted),
        "bootstrap": _bootstrap_regression_metrics(actual, predicted, resamples=resamples, seed=seed),
        "groups": groups,
        "provenance": {
            "input_path": str(path),
            "input_sha256": _sha256(path),
            "parameters": {
                "label_column": label_column,
                "prediction_column": prediction_column,
                "group_by": group_by,
                "resamples": resamples,
                "seed": seed,
            },
        },
    }


def _bootstrap_metric(values: Any, *, resamples: int, seed: int, confidence: float = 0.95) -> dict[str, Any]:
    np = _require("numpy")
    array = np.asarray(values, dtype=float)
    if array.size == 0 or not np.isfinite(array).all():
        raise ValueError("metric values must be finite and non-empty")
    if resamples < 100:
        raise ValueError("resamples must be at least 100")
    rng = np.random.default_rng(seed)
    estimates = np.empty(resamples, dtype=float)
    for start in range(0, resamples, 256):
        stop = min(start + 256, resamples)
        indices = rng.integers(0, array.size, size=(stop - start, array.size))
        estimates[start:stop] = array[indices].mean(axis=1)
    alpha = (1 - confidence) / 2
    return {
        "estimate": float(array.mean()),
        "lower": float(np.quantile(estimates, alpha)),
        "upper": float(np.quantile(estimates, 1 - alpha)),
        "confidence": confidence,
        "resamples": resamples,
        "seed": seed,
    }


def _ranking_query_metrics(frame: Any, *, query_column: str, rank_column: str, relevance_column: str, k: int, group_by: str | None) -> list[dict[str, Any]]:
    np = _require("numpy")
    rows: list[dict[str, Any]] = []
    for query, subset in frame.groupby(query_column, sort=True):
        ordered = subset.sort_values(rank_column, kind="stable")
        relevance = ordered[relevance_column].to_numpy(dtype=float)
        if relevance.size == 0 or not np.isfinite(relevance).all():
            raise ValueError(f"query {query} has invalid relevance values")
        total_relevant = int((relevance > 0).sum())
        if total_relevant == 0:
            raise ValueError(f"query {query} has no relevant items")
        top = relevance[:k]
        relevant_positions = np.flatnonzero(relevance > 0)
        mrr = 1.0 / float(relevant_positions[0] + 1) if relevant_positions.size else 0.0
        recall = float((top > 0).sum() / total_relevant)
        discount = 1.0 / np.log2(np.arange(2, k + 2))
        dcg = float(((2.0 ** top - 1.0) * discount[: top.size]).sum())
        ideal = np.sort(relevance)[::-1][:k]
        idcg = float(((2.0 ** ideal - 1.0) * discount[: ideal.size]).sum())
        row: dict[str, Any] = {
            "query": str(query),
            "mrr": mrr,
            "recall_at_k": recall,
            "ndcg_at_k": dcg / idcg if idcg else 0.0,
            "relevant_items": total_relevant,
        }
        if group_by:
            groups = {str(value) for value in subset[group_by].dropna().tolist()}
            if len(groups) != 1:
                raise ValueError(f"query {query} must map to exactly one {group_by} value")
            row["group"] = next(iter(groups))
        rows.append(row)
    if not rows:
        raise ValueError("input has no ranking queries")
    return rows


def evaluate_ranking(
    path: Path,
    *,
    query_column: str,
    rank_column: str,
    relevance_column: str,
    group_by: str | None = None,
    k: int = 5,
    resamples: int = 2000,
    seed: int = 0,
) -> dict[str, Any]:
    """Evaluate ranked retrieval with query-level MRR, Recall@K, and NDCG@K."""
    if k < 1:
        raise ValueError("k must be at least 1")
    frame = _read_frame(path)
    required = {query_column, rank_column, relevance_column}
    if group_by:
        required.add(group_by)
    missing = sorted(required - set(frame.columns))
    if missing:
        raise ValueError("missing columns: " + ", ".join(missing))
    frame[rank_column] = _require("pandas").to_numeric(frame[rank_column], errors="coerce")
    frame[relevance_column] = _require("pandas").to_numeric(frame[relevance_column], errors="coerce")
    if frame[rank_column].isna().any() or frame[relevance_column].isna().any():
        raise ValueError("rank and relevance columns must be numeric")
    queries = _ranking_query_metrics(
        frame,
        query_column=query_column,
        rank_column=rank_column,
        relevance_column=relevance_column,
        k=k,
        group_by=group_by,
    )
    metrics = {
        key: float(sum(row[key] for row in queries) / len(queries))
        for key in ("mrr", "recall_at_k", "ndcg_at_k")
    }
    groups: list[dict[str, Any]] = []
    if group_by:
        for group in sorted({str(row["group"]) for row in queries}):
            subset = [row for row in queries if row["group"] == group]
            groups.append({
                "group": group,
                "query_count": len(subset),
                **{key: float(sum(row[key] for row in subset) / len(subset)) for key in ("mrr", "recall_at_k", "ndcg_at_k")},
            })
    return {
        "schema_version": SCHEMA_VERSION,
        "tool": "model_evaluation",
        "tool_version": TOOL_VERSION,
        "task": "ranked_retrieval",
        "k": k,
        "query_count": len(queries),
        "metrics": metrics,
        "bootstrap": {
            key: _bootstrap_metric([row[key] for row in queries], resamples=resamples, seed=seed + offset)
            for offset, key in enumerate(("mrr", "recall_at_k", "ndcg_at_k"))
        },
        "query_metrics": queries,
        "groups": groups,
        "provenance": {
            "input_path": str(path),
            "input_sha256": _sha256(path),
            "parameters": {
                "query_column": query_column,
                "rank_column": rank_column,
                "relevance_column": relevance_column,
                "group_by": group_by,
                "k": k,
                "resamples": resamples,
                "seed": seed,
            },
        },
    }


def _write_or_print(payload: dict[str, Any], output: Path | None, as_json: bool) -> None:
    rendered = json.dumps(payload, ensure_ascii=False, indent=2)
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered + "\n", encoding="utf-8")
    if as_json or not output:
        print(rendered if as_json else json.dumps(payload, ensure_ascii=False))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="operation", required=True)
    classification = subparsers.add_parser("classification")
    classification.add_argument("--input", type=Path, required=True)
    classification.add_argument("--label-column", default="label")
    classification.add_argument("--prediction-column", default="prediction")
    classification.add_argument("--score-column")
    classification.add_argument("--group-by")
    classification.add_argument("--positive-label")
    classification.add_argument("--resamples", type=int, default=2000)
    classification.add_argument("--seed", type=int, default=0)
    classification.add_argument("--output", type=Path)
    classification.add_argument("--json", action="store_true")
    ranking = subparsers.add_parser("ranking")
    ranking.add_argument("--input", type=Path, required=True)
    ranking.add_argument("--query-column", default="query_id")
    ranking.add_argument("--rank-column", default="rank")
    ranking.add_argument("--relevance-column", default="relevance")
    ranking.add_argument("--group-by")
    ranking.add_argument("--k", type=int, default=5)
    ranking.add_argument("--resamples", type=int, default=2000)
    ranking.add_argument("--seed", type=int, default=0)
    ranking.add_argument("--output", type=Path)
    ranking.add_argument("--json", action="store_true")
    regression = subparsers.add_parser("regression")
    regression.add_argument("--input", type=Path, required=True)
    regression.add_argument("--label-column", default="label")
    regression.add_argument("--prediction-column", default="prediction")
    regression.add_argument("--group-by")
    regression.add_argument("--resamples", type=int, default=2000)
    regression.add_argument("--seed", type=int, default=0)
    regression.add_argument("--output", type=Path)
    regression.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        if args.operation == "classification":
            payload = evaluate_classification(
                args.input,
                label_column=args.label_column,
                prediction_column=args.prediction_column,
                score_column=args.score_column,
                group_by=args.group_by,
                positive_label=args.positive_label,
                resamples=args.resamples,
                seed=args.seed,
            )
        elif args.operation == "ranking":
            payload = evaluate_ranking(
                args.input,
                query_column=args.query_column,
                rank_column=args.rank_column,
                relevance_column=args.relevance_column,
                group_by=args.group_by,
                k=args.k,
                resamples=args.resamples,
                seed=args.seed,
            )
        elif args.operation == "regression":
            payload = evaluate_regression(
                args.input,
                label_column=args.label_column,
                prediction_column=args.prediction_column,
                group_by=args.group_by,
                resamples=args.resamples,
                seed=args.seed,
            )
        else:  # pragma: no cover - argparse enforces the operation choices
            raise ValueError(f"unsupported operation: {args.operation}")
    except (OSError, ValueError, OptionalDependencyError) as exc:
        parser.exit(2, f"error: {exc}\n")
    _write_or_print(payload, args.output, args.json)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
