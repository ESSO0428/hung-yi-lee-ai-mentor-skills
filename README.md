# hung-yi-lee-ai-mentor-skills

This is the standalone collection boundary for the Lee Hung-yi domain mentor.
The collection has two skills, selected by the root `SKILL.md` router:

- `hung-yi-ml-research-advisor`: your own model's training or evaluation has a
  problem. Competing hypotheses, source-grounded principles, optional
  deterministic diagnostics, and a minimal discriminating experiment.
- `hung-yi-genai-advisor`: you are building with an LLM (prompting, context and
  agent design, RAG, fine-tune vs prompt, evaluating LLM outputs, forgetting
  after fine-tuning, self-correction, cost). Course-backed advice with a source
  per statement, year labels, and an explicit not-covered list. It has no
  executable tools yet; ideas are in `skills/hung-yi-genai-advisor/references/tool-ideas.md`.

Both use the mentor only when explicitly requested.

It is deliberately separate from video acquisition and distillation tooling.
The bundled knowledge layer is enough for source-grounded mentor use; it does
not need downloaded videos, ASR assets, or a local media pipeline.

## Install through skills.sh

Install the **collection root**, not a nested advisor folder by itself. The
root carries both advisors, uv project, knowledge bundle, evidence packets, and
provenance reports together.

```bash
npx skills add ESSO0428/hung-yi-lee-ai-mentor-skills \
  --skill hung-yi-lee-ai-mentor-skills
```

The CLI asks which agent and scope to use. Do not add Codex-specific flags to
the shared installation command.

Do **not** install `hung-yi-ml-research-advisor` or `hung-yi-genai-advisor`
alone through skills.sh: they are the collection's nested runtime components and intentionally reads the bundled
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

Verify the layout after installation:

```bash
uv run --project "$SKILL_ROOT" python \
  "$SKILL_ROOT/skills/hung-yi-ml-research-advisor/bootstrap.py" \
  --skill-root "$SKILL_ROOT/skills/hung-yi-ml-research-advisor" --json
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
predictions, split metadata, or model diagnostics. The advisor will name competing
hypotheses and the cheapest discriminating experiment.

If working from a source checkout rather than a skills.sh install:

```bash
uv sync --extra analysis  # metrics, statistics, tables, and plots
# or only when model-internals diagnostics are needed:
uv sync --extra torch
```

## Knowledge boundary

- Lecture-backed statements carry a video id and section; own reasoning is
  labelled as inference; topics the lectures do not cover are stated as such
  (`references/not-covered.md`).
- The distillation evidence (transcripts, evidence packets, candidate
  knowledge) stays in the Distilly-SKILL build workspace and is not shipped;
  `evaluation/scenarios/` holds the behavioural evaluation set.
- The mentor never selects videos, downloads media, runs ASR/AGY, or performs
  Distilly distillation.

## Layout

```text
hung-yi-lee-ai-mentor-skills/
├── SKILL.md
├── pyproject.toml
├── uv.lock
├── evaluation/scenarios/
├── tests/
├── dev/
└── skills/
    ├── hung-yi-ml-research-advisor/
    │   ├── SKILL.md
    │   ├── references/
    │   └── tools/
    └── hung-yi-genai-advisor/
        ├── SKILL.md
        └── references/
```

`dev/` holds maintainer-only checks, including the official course-material
search, which only works inside a full Distilly-SKILL checkout with its index. It is not part of the
runtime and is not needed to use either skill.

`hung-yi-ml-research-advisor` owns research reasoning and optional,
deterministic diagnostics. `analysis` and `torch` are independent optional
profiles; `all` is for CI or a deliberate full-surface smoke test, not normal
startup.
