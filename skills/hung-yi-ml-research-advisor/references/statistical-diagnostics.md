# Statistical and evaluation diagnostics

Use the `analysis` profile only when the question contains numerical evidence
that benefits from deterministic calculation. Install it with:

```powershell
uv sync --extra analysis
```

## Recipe metrics and experiments

`tools/advanced_recipe_tools.py` provides `summarize-metrics`, `compare-groups`,
`compare-runs`, `error-breakdown`, `config-diff`, `training-dynamics`, and
`plot-metrics`. It computes objective-aware summaries, bootstrap intervals,
paired or independent effects, grouped error rates, and reproducible SVG
plots. Use the command output as evidence for a stated hypothesis; it does not
select the intervention.

The tool marker is `advanced_recipe_tools.py`; the comparison route is
`compare-groups`. Preserve the input file hash, objective, grouping columns,
random seed, tool version, and output path in the evidence record.

## Model evaluation

`tools/model_evaluation.py` supports:

- `classification`: binary metrics, calibration, slices, and bootstrap
  accuracy;
- `multiclass`: macro precision/recall/F1, balanced accuracy, per-class
  metrics, slices, and bootstrap intervals;
- `regression`: MAE, MSE, RMSE, R², row-bootstrap intervals, and slices;
- `ranking`: MRR, Recall@K, NDCG@K, and query-level bootstrap intervals.

Use the exact target/prediction column names and report missing rows rather
than silently dropping them. The markers `model_evaluation.py`, `multiclass`,
`regression`, and `ranking` identify this capability in package audits.

## Split and leakage audit

Before treating a generalization result as causal, run
`tools/dataset_split_audit.py` when sample IDs, groups, or content hashes are
available. It checks cross-split leakage, split counts, and label balance. A
`FAIL` is a data-integrity result, not evidence that a model architecture is
wrong. The marker is `dataset_split_audit.py`.

If only a summary metric is available, keep the claim bounded: report the
observed number and list the missing experiment or raw prediction table needed
for a stronger conclusion.
