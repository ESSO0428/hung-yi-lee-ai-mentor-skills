# hung-yi-ml-research-advisor

李宏毅課程視角的 ML 診斷顧問。入口是集合根目錄的 `SKILL.md`，本目錄是被它路由的 nested skill，不單獨安裝。使用規則、流程與工具表在本目錄的 `SKILL.md`。

## 執行（在 collection 根目錄）

```bash
uv run --project . python skills/hung-yi-ml-research-advisor/bootstrap.py --json
uv run --project . python skills/hung-yi-ml-research-advisor/skill_smoke.py --json
uv run --project . --with pytest python -m pytest tests/test_triage.py -q
```

## 可選 profile

- `uv sync --extra analysis`：numpy、pandas、matplotlib（`advanced_recipe_tools.py`、`model_evaluation.py`）
- `uv sync --extra torch`：torch（`torch_diagnostics.py`）
- `uv sync --extra all`：以上全部

Python 3.11+。`skill_smoke.py` 在隔離副本上跑 bootstrap 與各診斷工具；缺依賴的分支回報 `SKIPPED_DEPENDENCY` 與安裝命令。

## 官方課程教材

課程教材搜尋已移到 `dev/tools/search_course_material_chunks.py`，只在完整的 Distilly-SKILL 環境（含教材索引）可用，不屬於安裝版。

建置期的稽核與回放腳本（response gate、provenance audit、capability probe、visual evidence、FFP）在集合的 `dev/`，不屬於 runtime。
