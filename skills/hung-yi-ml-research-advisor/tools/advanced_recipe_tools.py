"""Optional high-fidelity analysis tools for the Hung-yi Lee mentor skill.

The basic ``recipe_tools.py`` module is deliberately dependency-free.  This
module is the advanced tier: it uses pandas/numpy for reproducible statistical
summaries and matplotlib for publication-ready diagnostics.  It never trains a
model or chooses an intervention; it reports measurements for the mentor
reasoning loop.  Missing extras are reported explicitly instead of silently
falling back to weaker arithmetic.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib
import importlib.metadata
import json
from pathlib import Path
from typing import Any, Iterable


TOOL_VERSION = "1.2.0"
SCHEMA_VERSION = "advanced-recipe-report.v1"


class OptionalDependencyError(RuntimeError):
    """Raised when an advanced report is requested without its declared extra."""


def _require(module_name: str, profile: str):
    try:
        if module_name == "matplotlib.pyplot":
            matplotlib = importlib.import_module("matplotlib")
            matplotlib.use("Agg", force=True)
        return importlib.import_module(module_name)
    except ImportError as exc:
        raise OptionalDependencyError(
            f"The advanced '{profile}' profile requires {module_name}. "
            f"Install it with 'uv sync --extra {profile}' in the mentor skill environment."
        ) from exc


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def dependency_report() -> dict[str, Any]:
    modules = ("numpy", "pandas", "matplotlib", "torch")
    capabilities: dict[str, dict[str, Any]] = {}
    for module in modules:
        available = importlib.util.find_spec(module) is not None
        version = None
        if available:
            try:
                version = importlib.metadata.version(module)
            except importlib.metadata.PackageNotFoundError:
                version = "installed"
        capabilities[module] = {"available": available, "version": version}
    profile_requirements = {
        "core": (),
        "analysis": ("matplotlib", "numpy", "pandas"),
        "torch": ("torch",),
        "all": ("matplotlib", "numpy", "pandas", "torch"),
    }
    install_profiles = {
        "analysis": "uv sync --extra analysis",
        "torch": "uv sync --extra torch",
        "all": "uv sync --extra all",
    }
    profiles = {}
    for profile, required in profile_requirements.items():
        missing = [module for module in required if not capabilities[module]["available"]]
        profiles[profile] = {
            "required": list(required),
            "missing": missing,
            "status": "READY" if not missing else "INPUT_MISSING",
            "install": install_profiles.get(profile),
        }
    return {
        "schema_version": "advanced-recipe-capabilities.v1",
        "tool": "advanced_recipe_tools",
        "tool_version": TOOL_VERSION,
        "capabilities": capabilities,
        "install_profiles": install_profiles,
        "profiles": profiles,
        "policy": "missing extras are explicit errors; no silent downgrade",
    }


def bootstrap_ci(
    values: Iterable[float],
    *,
    confidence: float = 0.95,
    resamples: int = 2000,
    seed: int = 0,
) -> dict[str, Any]:
    """Return a deterministic percentile bootstrap interval for the mean."""

    if not 0 < confidence < 1:
        raise ValueError("confidence must be between 0 and 1")
    if resamples < 100:
        raise ValueError("resamples must be at least 100")
    np = _require("numpy", "analysis")
    array = np.asarray([float(value) for value in values], dtype=float)
    if array.size == 0 or not np.isfinite(array).all():
        raise ValueError("values must contain at least one finite number")
    rng = np.random.default_rng(seed)
    indices = rng.integers(0, array.size, size=(resamples, array.size))
    samples = array[indices].mean(axis=1)
    alpha = (1.0 - confidence) / 2.0
    return {
        "count": int(array.size),
        "mean": float(array.mean()),
        "lower": float(np.quantile(samples, alpha)),
        "upper": float(np.quantile(samples, 1.0 - alpha)),
        "confidence": confidence,
        "resamples": resamples,
        "seed": seed,
    }


def _bootstrap_difference(
    baseline: Any,
    candidate: Any,
    *,
    paired: bool,
    confidence: float,
    resamples: int,
    seed: int,
) -> dict[str, Any]:
    """Estimate candidate-minus-baseline with a deterministic bootstrap.

    Paired inputs resample within matched pairs; unpaired inputs resample each
    group independently. Chunking keeps the operation bounded for large
    replicate tables instead of allocating a ``resamples x n`` matrix.
    """

    np = _require("numpy", "analysis")
    if not 0 < confidence < 1:
        raise ValueError("confidence must be between 0 and 1")
    if resamples < 100:
        raise ValueError("resamples must be at least 100")
    baseline_array = np.asarray(baseline, dtype=float)
    candidate_array = np.asarray(candidate, dtype=float)
    if baseline_array.size == 0 or candidate_array.size == 0:
        raise ValueError("both groups must contain at least one value")
    if not np.isfinite(baseline_array).all() or not np.isfinite(candidate_array).all():
        raise ValueError("both groups must contain only finite values")
    if paired and baseline_array.size != candidate_array.size:
        raise ValueError("paired groups must have equal lengths")

    rng = np.random.default_rng(seed)
    samples = np.empty(resamples, dtype=float)
    chunk_size = min(256, resamples)
    for start in range(0, resamples, chunk_size):
        stop = min(start + chunk_size, resamples)
        count = stop - start
        if paired:
            differences = candidate_array - baseline_array
            indices = rng.integers(0, differences.size, size=(count, differences.size))
            samples[start:stop] = differences[indices].mean(axis=1)
        else:
            baseline_indices = rng.integers(0, baseline_array.size, size=(count, baseline_array.size))
            candidate_indices = rng.integers(0, candidate_array.size, size=(count, candidate_array.size))
            samples[start:stop] = candidate_array[candidate_indices].mean(axis=1) - baseline_array[baseline_indices].mean(axis=1)

    alpha = (1.0 - confidence) / 2.0
    return {
        "difference": float(candidate_array.mean() - baseline_array.mean()),
        "lower": float(np.quantile(samples, alpha)),
        "upper": float(np.quantile(samples, 1.0 - alpha)),
        "confidence": confidence,
        "resamples": resamples,
        "seed": seed,
    }


def _read_frame(path: Path):
    pd = _require("pandas", "analysis")
    if not path.is_file():
        raise FileNotFoundError(path)
    if path.suffix.lower() == ".json":
        payload = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(payload, dict):
            payload = payload.get("rows", payload.get("metrics", payload.get("examples")))
        if not isinstance(payload, list):
            raise ValueError("JSON input must contain a list of row objects")
        frame = pd.DataFrame(payload)
    else:
        frame = pd.read_csv(path)
    if frame.empty:
        raise ValueError("input has no rows")
    return frame


def _metric_frame(path: Path):
    pd = _require("pandas", "analysis")
    frame = _read_frame(path)
    base_columns = {"run_id", "run", "step", "epoch", "split", "capacity"}
    if {"metric", "value"}.issubset(frame.columns):
        result = frame.copy()
        result["metric"] = result["metric"].astype(str)
        result["value"] = pd.to_numeric(result["value"], errors="coerce")
    else:
        metric_columns = [column for column in frame.columns if column not in base_columns]
        if not metric_columns:
            raise ValueError("input has no metric columns")
        id_columns = [column for column in frame.columns if column not in metric_columns]
        result = frame.melt(id_vars=id_columns, value_vars=metric_columns, var_name="metric", value_name="value")
        result["value"] = pd.to_numeric(result["value"], errors="coerce")
    if "run_id" in result.columns:
        result["run_id"] = result["run_id"].astype(str)
    elif "run" in result.columns:
        result["run_id"] = result["run"].astype(str)
    else:
        result["run_id"] = "default"
    if "split" in result.columns:
        result["split"] = result["split"].astype(str)
    else:
        result["split"] = "unspecified"
    if "step" in result.columns:
        result["step"] = pd.to_numeric(result["step"], errors="coerce").fillna(0)
    elif "epoch" in result.columns:
        result["step"] = pd.to_numeric(result["epoch"], errors="coerce").fillna(0)
    else:
        result["step"] = 0.0
    result["metric_key"] = result.apply(
        lambda row: f"{row['split']}/{row['metric']}" if row["split"] != "unspecified" else str(row["metric"]),
        axis=1,
    )
    result = result.dropna(subset=["value"])
    if result.empty:
        raise ValueError("input has no numeric metrics")
    return result


def _objective(raw: str | None) -> dict[str, str]:
    parsed = json.loads(raw) if raw else {}
    if not isinstance(parsed, dict):
        raise ValueError("objective must be a JSON object mapping metric keys to min or max")
    for key, value in parsed.items():
        if value not in {"min", "max"}:
            raise ValueError(f"objective for {key} must be min or max")
    return {str(key): str(value) for key, value in parsed.items()}


def _provenance(
    operation: str,
    inputs: list[Path],
    parameters: dict[str, Any],
    outputs: list[Path] | None = None,
) -> dict[str, Any]:
    output_paths = outputs or []
    return {
        "schema_version": "recipe-decision-provenance.v1",
        "tool": "advanced_recipe_tools",
        "tool_version": TOOL_VERSION,
        "operation": operation,
        "input_paths": [str(path) for path in inputs],
        "input_sha256": {str(path): _sha256(path) for path in inputs},
        "output_paths": [str(path) for path in output_paths],
        "output_sha256": {str(path): _sha256(path) for path in output_paths if path.is_file()},
        "parameters": {key: str(value) if isinstance(value, Path) else value for key, value in parameters.items()},
    }


def summarize_metrics(path: Path, objectives: dict[str, str], *, resamples: int, seed: int) -> dict[str, Any]:
    frame = _metric_frame(path)
    summaries: list[dict[str, Any]] = []
    for (run_id, key), group in frame.groupby(["run_id", "metric_key"], sort=True):
        values = group["value"].to_numpy(dtype=float)
        direction = objectives.get(key)
        best_index = values.argmin() if direction == "min" else values.argmax() if direction == "max" else None
        best_value = float(values[best_index]) if best_index is not None else None
        best_step = float(group.iloc[int(best_index)]["step"]) if best_index is not None else None
        summaries.append(
            {
                "run_id": str(run_id),
                "metric_key": str(key),
                "objective": direction,
                "count": int(len(values)),
                "mean": float(values.mean()),
                "std": float(values.std(ddof=1)) if len(values) > 1 else 0.0,
                "min": float(values.min()),
                "max": float(values.max()),
                "best_value": best_value,
                "best_step": best_step,
                "bootstrap_ci": bootstrap_ci(values, resamples=resamples, seed=seed),
            }
        )
    return {"schema_version": SCHEMA_VERSION, "summaries": summaries}


def capacity_ablation(
    path: Path,
    *,
    capacity_column: str,
    metric_key: str,
    objective: str,
    resamples: int,
    seed: int,
) -> dict[str, Any]:
    if objective not in {"min", "max"}:
        raise ValueError("objective must be min or max")
    frame = _metric_frame(path)
    if capacity_column not in frame.columns:
        raise ValueError(f"capacity column not found: {capacity_column}")
    selected = frame[frame["metric_key"] == metric_key]
    if selected.empty:
        raise ValueError(f"metric key not found: {metric_key}")
    rows: list[dict[str, Any]] = []
    for capacity, group in selected.groupby(capacity_column, sort=True):
        values = group["value"].to_numpy(dtype=float)
        rows.append(
            {
                "capacity": str(capacity),
                "count": int(len(values)),
                "mean": float(values.mean()),
                "bootstrap_ci": bootstrap_ci(values, resamples=resamples, seed=seed),
            }
        )
    best = (min if objective == "min" else max)(rows, key=lambda row: row["mean"])
    return {
        "schema_version": SCHEMA_VERSION,
        "metric_key": metric_key,
        "objective": objective,
        "ablation": rows,
        "best_by_mean": best["capacity"],
    }


def compare_groups(
    path: Path,
    *,
    group_column: str,
    value_column: str,
    baseline: str,
    candidate: str,
    paired_column: str | None,
    confidence: float,
    resamples: int,
    seed: int,
) -> dict[str, Any]:
    """Compare two recipe groups and report a bootstrap effect interval.

    ``candidate - baseline`` is the only reported direction. If a pair key is
    provided, rows are matched on that key and duplicate observations within a
    group/key are averaged before the paired bootstrap. Without a pair key the
    two groups are treated as independent samples.
    """

    pd = _require("pandas", "analysis")
    frame = _read_frame(path)
    required = {group_column, value_column}
    if paired_column:
        required.add(paired_column)
    missing = sorted(column for column in required if column not in frame.columns)
    if missing:
        raise ValueError(f"column(s) not found: {', '.join(missing)}")
    frame = frame.copy()
    frame[value_column] = pd.to_numeric(frame[value_column], errors="coerce")
    frame = frame.dropna(subset=[group_column, value_column])
    frame[group_column] = frame[group_column].astype(str)
    selected = frame[frame[group_column].isin({str(baseline), str(candidate)})]
    if selected.empty:
        raise ValueError("neither requested group has numeric observations")

    if paired_column:
        paired = (
            selected.groupby([paired_column, group_column], sort=True)[value_column]
            .mean()
            .unstack(group_column)
            .dropna(subset=[str(baseline), str(candidate)])
        )
        if paired.empty:
            raise ValueError("paired groups have no shared pair keys")
        baseline_values = paired[str(baseline)].to_numpy(dtype=float)
        candidate_values = paired[str(candidate)].to_numpy(dtype=float)
        n_pairs = int(len(paired))
    else:
        baseline_values = selected.loc[selected[group_column] == str(baseline), value_column].to_numpy(dtype=float)
        candidate_values = selected.loc[selected[group_column] == str(candidate), value_column].to_numpy(dtype=float)
        n_pairs = None

    effect = _bootstrap_difference(
        baseline_values,
        candidate_values,
        paired=paired_column is not None,
        confidence=confidence,
        resamples=resamples,
        seed=seed,
    )
    return {
        "schema_version": SCHEMA_VERSION,
        "group_column": group_column,
        "value_column": value_column,
        "baseline": str(baseline),
        "candidate": str(candidate),
        "comparison": "candidate_minus_baseline",
        "paired": paired_column is not None,
        "paired_column": paired_column,
        "n_baseline": int(len(baseline_values)),
        "n_candidate": int(len(candidate_values)),
        "n_pairs": n_pairs,
        "baseline_mean": float(baseline_values.mean()),
        "candidate_mean": float(candidate_values.mean()),
        "difference": effect["difference"],
        "difference_ci": {
            "lower": effect["lower"],
            "upper": effect["upper"],
            "confidence": effect["confidence"],
        },
        "resamples": resamples,
        "seed": seed,
        "interpretation_boundary": "descriptive effect only; choose an intervention only after checking data, optimization, capacity, evaluation, and practical-cost evidence",
    }


def training_dynamics(
    path: Path,
    *,
    train_metric_key: str,
    validation_metric_key: str,
) -> dict[str, Any]:
    """Align train/validation curves and report generalization gaps.

    The output is descriptive only: a positive validation-minus-train gap is
    evidence to inspect, not an automatic prescription to regularize.
    """

    pd = _require("pandas", "analysis")
    frame = _metric_frame(path)
    selected = frame[frame["metric_key"].isin({train_metric_key, validation_metric_key})]
    if selected.empty:
        raise ValueError("requested train/validation metric keys not found")
    pivot = selected.pivot_table(index=["run_id", "step"], columns="metric_key", values="value", aggfunc="mean").reset_index()
    for key in (train_metric_key, validation_metric_key):
        if key not in pivot.columns:
            raise ValueError(f"metric key not found: {key}")
    pivot = pivot.dropna(subset=[train_metric_key, validation_metric_key]).copy()
    if pivot.empty:
        raise ValueError("no aligned train/validation steps")
    pivot["validation_minus_train"] = pivot[validation_metric_key] - pivot[train_metric_key]
    pivot["absolute_gap"] = pivot["validation_minus_train"].abs()
    rows = []
    for run_id, group in pivot.groupby("run_id", sort=True):
        ordered = group.sort_values("step")
        gaps = ordered["validation_minus_train"].to_numpy(dtype=float)
        rows.append(
            {
                "run_id": str(run_id),
                "aligned_steps": int(len(ordered)),
                "first_gap": float(gaps[0]),
                "last_gap": float(gaps[-1]),
                "max_absolute_gap": float(ordered["absolute_gap"].max()),
                "mean_absolute_gap": float(ordered["absolute_gap"].mean()),
                "gap_increased": bool(gaps[-1] > gaps[0]),
                "steps": [
                    {
                        "step": float(row["step"]),
                        "train": float(row[train_metric_key]),
                        "validation": float(row[validation_metric_key]),
                        "validation_minus_train": float(row["validation_minus_train"]),
                        "absolute_gap": float(row["absolute_gap"]),
                    }
                    for _, row in ordered.iterrows()
                ],
            }
        )
    return {
        "schema_version": SCHEMA_VERSION,
        "train_metric_key": train_metric_key,
        "validation_metric_key": validation_metric_key,
        "runs": rows,
        "interpretation_boundary": "descriptive gap only; inspect optimization, data, capacity, and evaluation evidence before choosing an intervention",
    }


def error_analysis(path: Path, *, label_column: str, prediction_column: str, group_by: str | None) -> dict[str, Any]:
    pd = _require("pandas", "analysis")
    frame = _read_frame(path)
    for column in (label_column, prediction_column):
        if column not in frame.columns:
            raise ValueError(f"column not found: {column}")
    frame = frame.copy()
    frame["_correct"] = frame[label_column].astype(str) == frame[prediction_column].astype(str)
    matrix = pd.crosstab(frame[label_column].astype(str), frame[prediction_column].astype(str))
    result: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "total": int(len(frame)),
        "accuracy": float(frame["_correct"].mean()),
        "confusion_matrix": {str(index): {str(key): int(value) for key, value in row.items()} for index, row in matrix.to_dict(orient="index").items()},
    }
    if group_by:
        if group_by not in frame.columns:
            raise ValueError(f"group-by column not found: {group_by}")
        grouped = frame.groupby(group_by, sort=True)["_correct"].agg(["count", "mean"])
        result["groups"] = [
            {"group": str(index), "count": int(row["count"]), "accuracy": float(row["mean"])}
            for index, row in grouped.iterrows()
        ]
    return result


def plot_training_report(path: Path, output: Path, metric_keys: list[str] | None) -> dict[str, Any]:
    frame = _metric_frame(path)
    keys = metric_keys or sorted(str(key) for key in frame["metric_key"].unique())
    selected = frame[frame["metric_key"].isin(keys)]
    if selected.empty:
        raise ValueError("no requested metric keys found")
    plt = _require("matplotlib.pyplot", "analysis")
    figure, axis = plt.subplots(figsize=(9, 5), constrained_layout=True)
    multiple_runs = selected["run_id"].nunique() > 1
    series: list[str] = []
    grouping = ["run_id", "metric_key"] if multiple_runs else ["metric_key"]
    for group_key, group in selected.groupby(grouping, sort=True):
        if multiple_runs:
            run_id, key = group_key
            label = f"{run_id}/{key}"
        else:
            key = group_key
            label = str(key)
        ordered = group.sort_values("step")
        axis.plot(ordered["step"], ordered["value"], marker="o", label=label)
        series.append(label)
    axis.set_xlabel("step")
    axis.set_ylabel("value")
    axis.grid(True, alpha=0.25)
    axis.legend()
    output.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output, dpi=150)
    plt.close(figure)
    return {"schema_version": SCHEMA_VERSION, "output": str(output), "metric_keys": keys, "series": series}


def _write_or_print(payload: dict[str, Any], output: Path | None, as_json: bool) -> None:
    encoded = json.dumps(payload, ensure_ascii=False, indent=2)
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(encoded + "\n", encoding="utf-8")
    if as_json or output is None:
        print(json.dumps(payload, ensure_ascii=False))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="operation", required=True)

    dependencies = subparsers.add_parser("dependencies")
    dependencies.add_argument("--json", action="store_true")

    summary = subparsers.add_parser("summarize-metrics")
    summary.add_argument("--input", type=Path, required=True)
    summary.add_argument("--objective")
    summary.add_argument("--resamples", type=int, default=2000)
    summary.add_argument("--seed", type=int, default=0)
    summary.add_argument("--output", type=Path)
    summary.add_argument("--json", action="store_true")

    ablation = subparsers.add_parser("capacity-ablation")
    ablation.add_argument("--input", type=Path, required=True)
    ablation.add_argument("--capacity-column", default="capacity")
    ablation.add_argument("--metric-key", required=True)
    ablation.add_argument("--objective", choices=("min", "max"), required=True)
    ablation.add_argument("--resamples", type=int, default=2000)
    ablation.add_argument("--seed", type=int, default=0)
    ablation.add_argument("--output", type=Path)
    ablation.add_argument("--json", action="store_true")

    comparison = subparsers.add_parser("compare-groups")
    comparison.add_argument("--input", type=Path, required=True)
    comparison.add_argument("--group-column", required=True)
    comparison.add_argument("--value-column", required=True)
    comparison.add_argument("--baseline", required=True)
    comparison.add_argument("--candidate", required=True)
    comparison.add_argument("--paired-column")
    comparison.add_argument("--confidence", type=float, default=0.95)
    comparison.add_argument("--resamples", type=int, default=2000)
    comparison.add_argument("--seed", type=int, default=0)
    comparison.add_argument("--output", type=Path)
    comparison.add_argument("--json", action="store_true")

    dynamics = subparsers.add_parser("training-dynamics")
    dynamics.add_argument("--input", type=Path, required=True)
    dynamics.add_argument("--train-metric-key", required=True)
    dynamics.add_argument("--validation-metric-key", required=True)
    dynamics.add_argument("--output", type=Path)
    dynamics.add_argument("--json", action="store_true")

    errors = subparsers.add_parser("error-analysis")
    errors.add_argument("--input", type=Path, required=True)
    errors.add_argument("--label-column", default="label")
    errors.add_argument("--prediction-column", default="prediction")
    errors.add_argument("--group-by")
    errors.add_argument("--output", type=Path)
    errors.add_argument("--json", action="store_true")

    plot = subparsers.add_parser("plot-training")
    plot.add_argument("--input", type=Path, required=True)
    plot.add_argument("--output", type=Path, required=True)
    plot.add_argument("--metric-key", action="append")
    plot.add_argument("--json", action="store_true")

    args = parser.parse_args()
    try:
        if args.operation == "dependencies":
            _write_or_print(dependency_report(), None, args.json)
            return 0
        if args.operation == "summarize-metrics":
            payload = summarize_metrics(args.input, _objective(args.objective), resamples=args.resamples, seed=args.seed)
            payload["provenance"] = _provenance("summarize-metrics", [args.input], {"objective": _objective(args.objective), "resamples": args.resamples, "seed": args.seed})
        elif args.operation == "capacity-ablation":
            payload = capacity_ablation(args.input, capacity_column=args.capacity_column, metric_key=args.metric_key, objective=args.objective, resamples=args.resamples, seed=args.seed)
            payload["provenance"] = _provenance("capacity-ablation", [args.input], vars(args))
        elif args.operation == "compare-groups":
            payload = compare_groups(
                args.input,
                group_column=args.group_column,
                value_column=args.value_column,
                baseline=args.baseline,
                candidate=args.candidate,
                paired_column=args.paired_column,
                confidence=args.confidence,
                resamples=args.resamples,
                seed=args.seed,
            )
            payload["provenance"] = _provenance("compare-groups", [args.input], vars(args))
        elif args.operation == "training-dynamics":
            payload = training_dynamics(args.input, train_metric_key=args.train_metric_key, validation_metric_key=args.validation_metric_key)
            payload["provenance"] = _provenance("training-dynamics", [args.input], vars(args))
        elif args.operation == "error-analysis":
            payload = error_analysis(args.input, label_column=args.label_column, prediction_column=args.prediction_column, group_by=args.group_by)
            payload["provenance"] = _provenance("error-analysis", [args.input], vars(args))
        elif args.operation == "plot-training":
            payload = plot_training_report(args.input, args.output, args.metric_key)
            payload["provenance"] = _provenance("plot-training", [args.input], vars(args), outputs=[args.output])
            if args.json:
                _write_or_print(payload, None, True)
            else:
                print(args.output)
            return 0
        _write_or_print(payload, args.output if hasattr(args, "output") else None, args.json)
        return 0
    except (FileNotFoundError, OptionalDependencyError, ValueError) as exc:
        parser.exit(2, f"error: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
