# hung-yi-lee-ai-mentor-skills

This is the standalone collection boundary for the Lee Hung-yi domain mentor.
It is deliberately separate from video acquisition and distillation tooling.
The bundled knowledge layer is enough for source-grounded mentor use; it does
not need downloaded videos, ASR assets, or a local media pipeline.

## Install through skills.sh

Install the **collection root**, not the nested advisor folder by itself. The
root carries the advisor, uv project, knowledge bundle, evidence packets, and
provenance reports together.

```bash
npx skills add ESSO0428/hung-yi-lee-ai-mentor-skills \
  --skill hung-yi-lee-ai-mentor-skills
```

The CLI asks which agent and scope to use. Do not add Codex-specific flags to
the shared installation command.

Do **not** install `hung-yi-ml-research-advisor` alone through skills.sh: it is
the collection's nested runtime component and intentionally reads the bundled
knowledge from the collection root.

## Set up the uv runtime

The install command copies the files but does not create a Python environment.
Find the installed collection path and set it up once:

```bash
# If you selected global scope during installation, add --global after `list`.
SKILL_ROOT="$(npx skills list --json | node -e '
let input = "";
process.stdin.on("data", chunk => input += chunk);
process.stdin.on("end", () => {
  const skill = JSON.parse(input).find(
    item => item.name === "hung-yi-lee-ai-mentor-skills"
  );
  if (!skill) process.exit(1);
  process.stdout.write(skill.path);
});
')"
uv sync --project "$SKILL_ROOT" --extra analysis
```

Windows PowerShell:

```powershell
# If you selected global scope during installation, add --global after `list`.
$skillsJson = npx skills list --json | Out-String
$skills = $skillsJson | ConvertFrom-Json
$skill = @(
  $skills | Where-Object { $_.name -eq "hung-yi-lee-ai-mentor-skills" }
) | Select-Object -First 1
$SKILL_ROOT = $skill.path
if (-not $SKILL_ROOT) {
  throw "The hung-yi-lee-ai-mentor-skills collection was not found."
}
uv sync --project $SKILL_ROOT --extra analysis
```

`uv sync` creates or updates `.venv` in the discovered collection directory.
Normal commands should keep targeting that project explicitly; no shell
activation is required.

Verify the source-grounded knowledge layer after installation:

```bash
uv run --project "$SKILL_ROOT" python \
  "$SKILL_ROOT/skills/hung-yi-ml-research-advisor/bootstrap.py" \
  --skill-root "$SKILL_ROOT/skills/hung-yi-ml-research-advisor" \
  --knowledge "$SKILL_ROOT/knowledge/normalized_principles.json" \
  --require-knowledge --json
```

Use `--extra torch` only for model/gradient/activation diagnostics, or
`--extra all` for a deliberate full-surface smoke/CI run.

Add this one-line rule to both `AGENTS.md` and `CLAUDE.md`:

```text
When using a hung-yi-ml-research-advisor tool, invoke it through the installed hung-yi-lee-ai-mentor-skills collection root with uv run --project "<skill path>" ...
```

## Quick start

After installation, explicitly request `hung-yi-lee-ai-mentor-skills` when
asking an agent to evaluate an ML recipe, experiment, training failure,
data/evaluation concern, or model change. Supply the relevant metrics, config,
predictions, split metadata, or model diagnostics. The advisor will distinguish
observations, competing hypotheses, applicable knowledge, uncertainty, and the
cheapest discriminating experiment.

If working from a source checkout rather than a skills.sh install:

```bash
uv sync --extra analysis  # metrics, statistics, tables, and plots
# or only when model-internals diagnostics are needed:
uv sync --extra torch
```

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

`hung-yi-ml-research-advisor` owns research reasoning and optional,
deterministic diagnostics. `analysis` and `torch` are independent optional
profiles; `all` is for CI or a deliberate full-surface smoke test, not normal
startup.

`RELEASE-MANIFEST.json` hashes the distributed bundle, and
`evaluation/channel-distillation-acceptance-latest.json` records the
available-data acceptance result.
