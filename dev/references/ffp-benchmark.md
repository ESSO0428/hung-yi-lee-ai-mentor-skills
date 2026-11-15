# FFP integration benchmark

FFP is a temporary integration benchmark and future-work gate for this mentor;
it is not a runtime domain dependency and is not required for ordinary ML
recipe advice. Keep it because it tests whether the advisor can reason from a
versioned project history without hindsight leakage.

The benchmark tools are:

```powershell
uv run python hung-yi-lee-ai-mentor-skills/skills/hung-yi-ml-research-advisor/tools/ffp_evaluation.py scaffold --discovery ffp-evidence-inventory.json --output ffp-manifest.template.json
uv run python hung-yi-lee-ai-mentor-skills/skills/hung-yi-ml-research-advisor/tools/ffp_evaluation.py audit --input ffp-manifest.json
uv run python hung-yi-lee-ai-mentor-skills/skills/hung-yi-ml-research-advisor/tools/ffp_evaluation.py blind-pack --input ffp-manifest.json --transition-id FFP_to_FFP_simple --output blind-packet.json
uv run python hung-yi-lee-ai-mentor-skills/skills/hung-yi-ml-research-advisor/tools/ffp_evaluation.py reconcile --input ffp-manifest.json --transition-id FFP_to_FFP_simple --advice advice.json
```

`scaffold` 只複製 discovery 已取得的檔案 hash，並產生需要人工補上的版本、split、recipe、metrics 與 transition outcome；它不猜測版本，也不會把結果標成 `FFP_VALIDATED`。

The expected historical sequence is `FFP` → `FFP_simple` → `FFP_new_mlp`.
`blind-pack` removes future outcome fields before advice is frozen. An
`INPUT_MISSING` result means the versioned artifacts or split are unavailable;
it is an honest benchmark data gate, not a failure of the core mentor. A
`REVIEW_REQUIRED` result means the packet or advice contract needs review.
Never turn a benchmark score into general knowledge without a source-linked
reconciliation and an explicit generalization argument.
