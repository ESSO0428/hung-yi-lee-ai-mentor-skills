# Tensor diagnostics

Use the `torch` profile only when the competing hypotheses concern model
internals: parameter magnitudes, gradient health, activation saturation,
dead units, NaN/Inf values, or checkpoint structure.

```powershell
uv sync --extra torch
uv run python hung-yi-lee-ai-mentor-skills/skills/hung-yi-ml-research-advisor/tools/torch_diagnostics.py --input model.pt --format json
```

`tools/torch_diagnostics.py` is read-only. It must not train, mutate, or
rewrite the supplied checkpoint. Record the checkpoint hash, model loader
configuration, selected layer names, tool version, and any sampling or
truncation limits. Large checkpoints may require bounded sampling or more
memory; report that limitation as `INPUT_MISSING`/`REVIEW_REQUIRED` instead of
pretending the scan was complete.

Torch evidence is diagnostic, not causal by itself. Pair it with metrics,
split integrity, and a controlled experiment before recommending a recipe
change. The package marker is `torch_diagnostics.py` and the optional profile
marker is `uv sync --extra torch`.
