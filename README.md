# hung-yi-lee-ai-mentor-skills

This is the standalone collection boundary for the Lee Hung-yi domain mentor.
It is deliberately separate from video acquisition and distillation tooling.
The bundled knowledge layer is enough for source-grounded mentor use; it does
not need downloaded videos, ASR assets, or a local media pipeline.

## Quick start

From this directory:

```powershell
uv sync --extra analysis  # metrics, statistics, tables, and plots
# or only when model-internals diagnostics are needed:
uv sync --extra torch
```

Explicitly request `hung-yi-lee-ai-mentor-skills` when asking an agent to
evaluate an ML recipe, experiment, training failure, data/evaluation concern,
or model change. Supply the relevant metrics, config, predictions, split
metadata, or model diagnostics. The advisor will distinguish observations,
competing hypotheses, applicable knowledge, uncertainty, and the cheapest
discriminating experiment.

## Knowledge boundary

- Formal P0 principles are in `knowledge/normalized_principles.json`.
- P1/P2 are explicitly indexed `CANDIDATE_REVIEW_REQUIRED` material: they may
  frame a hypothesis or experiment, but are not silently promoted to formal
  rules.
- P3 is archive-only and cannot be used as a recipe rule.
- Selected packets, dossiers, hashes, and acceptance reports are included for
  auditability. The full audiovisual/ASR corpus is intentionally omitted.
- The mentor never selects videos, downloads media, runs ASR/AGY, or performs
  Distilly distillation.

## Layout

```text
hung-yi-lee-ai-mentor-skills/
├── SKILL.md
├── pyproject.toml
├── uv.lock
├── knowledge/
├── data/processing/channel_evidence_packets_v1/
├── distillation/
├── evaluation/
└── skills/
    └── hung-yi-ml-research-advisor/
        ├── SKILL.md
        ├── modules/
        ├── references/
        └── tools/
```

`hung-yi-ml-research-advisor` owns research reasoning and the optional deterministic
diagnostics. It does not download videos, run ASR, call AGY, or re-distill
source material. Those outputs can be supplied as provenance-linked evidence
when a mentor decision needs them.

`hung-yi-ml-research-advisor` owns research reasoning and optional,
deterministic diagnostics. `analysis` and `torch` are independent optional
profiles; `all` is for CI or a deliberate full-surface smoke test, not normal
startup.

`RELEASE-MANIFEST.json` hashes the distributed bundle, and
`evaluation/channel-distillation-acceptance-latest.json` records the
available-data acceptance result.
