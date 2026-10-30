# Diagnostic routing

The mentor starts with the smallest profile that can answer the current
question. A profile is a capability boundary, not a claim that every
dependency must be installed for every invocation.

| Evidence or question | Profile | Capability | Install / run |
| --- | --- | --- | --- |
| source-linked reasoning, response shape, course lookup, provenance, or FFP bookkeeping | `core` | standard-library routing plus the core tools | `uv run python ...` |
| metrics, training curves, bootstrap intervals, ablations, slices, calibration, grouped errors, or prediction tables | `analysis` | NumPy, Pandas, Matplotlib, and analysis tools | `uv sync --extra analysis` |
| parameter, gradient, activation, or tensor-health question | `torch` | read-only PyTorch diagnostics | `uv sync --extra torch` |
| one run deliberately exercises every branch or CI needs the complete surface | `all` | all analysis and Torch capabilities | `uv sync --extra all` |

Use this decision procedure:

1. Begin with observations, hypotheses, and provenance in the core loop.
2. Name the smallest measurement that would discriminate the competing
   hypotheses.
3. Select only the profile containing that measurement.
4. If the profile is unavailable, return `INPUT_MISSING` with the exact
   profile command; do not substitute an unverified verbal guess.
5. Load another profile only when new evidence makes it necessary. Record the
   profile, tool version, input hashes, and output path in the evidence packet.

`all` is useful for the isolated smoke test and release/CI verification. It is
not the default production startup requirement. The mentor can be fully useful
with core-only evidence, and an analysis-only question should not install or
invoke Torch.

The following are the narrow entry points:

```powershell
uv run python hung-yi-lee-ai-mentor-skills/skills/hung-yi-ml-research-advisor/tools/advanced_recipe_tools.py summarize-metrics --input metrics.csv --metric val_loss --objective min
uv run python hung-yi-lee-ai-mentor-skills/skills/hung-yi-ml-research-advisor/tools/model_evaluation.py regression --input predictions.csv --target target --prediction prediction
uv run python hung-yi-lee-ai-mentor-skills/skills/hung-yi-ml-research-advisor/tools/dataset_split_audit.py --input split.csv --id-column sample_id --split-column split
uv run python hung-yi-lee-ai-mentor-skills/skills/hung-yi-ml-research-advisor/tools/torch_diagnostics.py --input model.pt --format json
```

See the profile-specific references before choosing flags. A tool report is
descriptive evidence, not an automatic intervention or causal conclusion.
