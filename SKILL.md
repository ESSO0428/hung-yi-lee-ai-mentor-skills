---
name: hung-yi-lee-ai-mentor-skills
description: Use the packaged Hung-yi Lee ML knowledge and diagnostic tools to advise on an AI recipe, experiment, evaluation, or research decision when the user explicitly requests this mentor skill.
---

# Hung-yi Lee AI Mentor Skills

This directory is the delivery boundary for the mentor skill family. Route a
researcher asking for an AI recipe or experiment decision to the narrowest
skill under [`skills/`](skills/):

- [`hung-yi-ml-research-advisor`](skills/hung-yi-ml-research-advisor/SKILL.md) for competing
  hypotheses, source-grounded principles, deterministic diagnostics, and a
  minimal discriminating experiment.

Read only the selected skill and the reference it points to. The package
contains interpretation and decision tools; source acquisition and media
processing remain separate project capabilities. The mentor may consume
already supplied multimodal evidence with provenance, but it does not manage
that collection workflow.

Optional numerical capabilities are disclosed by evidence: `analysis` for
metrics/statistics/plots, `torch` for model internals, and `all` for a full
isolated smoke or CI run. See the selected skill's routing reference before
loading a profile.
