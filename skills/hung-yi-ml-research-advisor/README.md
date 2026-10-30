# ML Research Advisor Skill

這是以來源鏈為核心的研究決策 Skill。它在研究者提出模型、loss、資料、評估或訓練修改時，要求分開 observation、hypothesis、evidence、unknown 與最小鑑別實驗；它不是李宏毅老師 Persona，也不是 canonical transcript。它只消費已驗證的 formal knowledge 與明確標示的 candidate knowledge，不參與影片選源、媒體取得、ASR、AGY 或 Distilly。

## 獨立 repository 使用

從 repository 根目錄讀 collection `SKILL.md`，再依問題載入 [`modules/index.md`](modules/index.md) 的 formal P0 domain module。正式規則的唯一知識輸入是根目錄的 `knowledge/normalized_principles.json`；模組是可路由的 disclosed reference，不能取代其中的 provenance。

```powershell
uv run python skills/hung-yi-ml-research-advisor/bootstrap.py `
  --skill-root skills/hung-yi-ml-research-advisor `
  --knowledge knowledge/normalized_principles.json `
  --require-knowledge --json
```

```bash
uv run python skills/hung-yi-ml-research-advisor/bootstrap.py \
  --skill-root skills/hung-yi-ml-research-advisor \
  --knowledge knowledge/normalized_principles.json \
  --require-knowledge --json
```

## Skill-only 使用

複製 `SKILL.md`、`modules/` 與 `references/` 後，另外提供一份 provenance-preserving `normalized_principles.json`；若要使用 P1/P2，另提供已驗證的 candidate knowledge index 與 candidate JSON。若缺少相應 knowledge bundle，Skill 必須把規則標為 unavailable，提出 evidence-gathering step，不得補造引用。原始 source chunks、manifest 與影格 manifest 是可選的唯讀稽核材料，不是一般 advisor 回覆的媒體處理依賴。P1/P2 candidate JSON 也不能當成正式 P0 rule。

複製後可先執行 `python bootstrap.py --json` 檢查 Skill 文件；提供 normalized JSON 時再加上 `--knowledge <path>`，bootstrap 會驗證 8 個 module route、15 個 P0 principle ID 與 source chunk 連結。它是只讀檢查，不會建立或修改來源。

若要確認這份 copy 已足以進行來源導向的 mentor 判斷，使用
`python bootstrap.py --knowledge <path> --require-knowledge --json`。缺少或無法解析
normalized knowledge 時會回報 `INPUT_MISSING`／失敗，而不是把「只有 Skill 文件」誤當成
可引用的正式知識層；沒有 `--require-knowledge` 時仍可只做結構檢查，但輸出中的
`source_grounded_ready` 會是 `false`。

若要排查 packaged install 的 integrity 或 disputed provenance，可選擇執行
`python tools/capability_probe.py --json`；它只彙整狀態，會把缺少的 audit material 或 profile
標成 `INPUT_MISSING`，也會在 full-repo 模式檢查每個 normalized principle 的可回查鏈。它不是一般
advisor 路由的前置步驟，也不會下載、選源、蒸餾或替代證據審查。

完成一份 advisor response 後，使用
`python tools/mentor_response_gate.py --response <response.json> --knowledge <normalized_principles.json> --json`
一次執行結構與知識 provenance 兩道 gate。只有兩者都 `PASS` 才能把回覆視為
source-grounded；缺少 normalized knowledge 會明確回報 `INPUT_MISSING`。

## 安裝與平台

- Windows、macOS、Linux：Python 3.11+ 與 `uv`；依實際診斷分支選用 `analysis`、`torch` 或 `all` extra。
- Codex、Claude、Gemini／AGY、`skills.sh` 或 marketplace：安裝通常只取得 Skill 檔案；宿主必須另外提供已驗證的 `knowledge/normalized_principles.json`，以及需要 P1/P2 路由時的 candidate knowledge bundle。影片取得與媒體工具屬建置期 pipeline，不是此 mentor skill 的 runtime requirement。

本 Skill 只負責研究解讀與決策；它不管理來源取得、媒體處理或蒸餾流程。呼叫端若提供影片或課程的多模態證據，仍須保留 `principle ID → source chunk → timestamp → source URL → evidence_type` 鏈。

## Recipe decision tools

## Progressive disclosure and profiles

The mentor keeps its full diagnostic capability but selects dependencies by
question. Core reasoning and provenance work without optional packages;
metrics, bootstrap, calibration, plots, and split audits use
`uv sync --extra analysis`; parameter, gradient, and activation checks use
`uv sync --extra torch`; `uv sync --extra all` is reserved for an explicit
full-surface run or CI smoke test. A missing optional profile blocks only the
requested branch and must report `INPUT_MISSING` with the install command.
See [`references/diagnostic-routing.md`](references/diagnostic-routing.md) and
the profile-specific references for flags and provenance requirements.

當使用者明確要求 mentor-style recipe 評估時，可用 `tools/recipe_tools.py` 將重複且容易出錯的 metrics 摘要、run comparison、error breakdown、config diff 與 metrics SVG curve deterministic 化；它只產生帶 input hash 與參數的量測結果，最後的 ML 解釋仍由本 Skill 依 formal principle 與 provenance 完成。

若需要複雜 recipe 診斷，使用 mentor-only 的 advanced tier：

- `tools/advanced_recipe_tools.py`：以 `numpy`、`pandas`、`matplotlib` 產生 bootstrap 信賴區間、capacity ablation、paired／independent baseline-candidate effect interval、分組錯誤分析與訓練曲線報告。
 - `tools/torch_diagnostics.py`：對呼叫者提供並自行執行的 PyTorch model 讀取參數、梯度與 activation 健康狀態；不自行訓練或改動模型。
- `tools/dataset_split_audit.py`：在解讀 metrics 前檢查 sample ID、group ID、exact content hash 的跨 split 洩漏與 label distribution 漂移。
- `tools/visual_evidence_lookup.py`：按 claim／影片／request／時間戳／投影片頁碼查詢既有視覺證據，驗證影像存在與 SHA-256，回傳可直接引用的 provenance；它不下載媒體或重新抽影格。
- `tools/ffp_evaluation.py`：為 FFP 建立 artifact hash gate、保守 discovery/scaffold、blind replay packet 與 advice traceability 檢查；輸入不完整時明確回報 `INPUT_MISSING`，不冒充驗證。
- `tools/response_validator.py`：驗證 advisor response packet 的觀察／未知／競爭假設／最小實驗／條件式建議與 provenance evidence-ID 閉鏈；只做結構 gate，不把格式通過當成語意正確。
- `tools/mentor_response_gate.py`：一次串接 response validator 與 advisor provenance audit，避免只驗證格式卻漏掉 normalized knowledge provenance。
- `tools/model_evaluation.py`：以 NumPy／Pandas 計算 binary／multiclass classification 的 accuracy、balanced accuracy、macro precision／recall／F1、bootstrap 區間與可選 slice metrics；binary 另支援 Brier／ECE 校準，numeric target 支援 regression 的 MAE／MSE／RMSE／R² row-bootstrap；同一工具也支援 ranked retrieval 的 MRR／Recall@K／NDCG@K、query-level bootstrap 與 slice metrics。缺少 calibration score、非數值 regression target 或無 relevant item 時明確回報輸入錯誤，不以手算替代。
- `tools/advisor_provenance_audit.py`：把 response packet 的 principle ID／evidence class 對回 normalized knowledge，檢查直接課程規則是否仍有影片 URL、時間範圍與 source chunk；它是 response-validator 之後的 knowledge-backed gate。
- 安裝設定在 `pyproject.toml`：`uv sync --extra analysis`、`uv sync --extra torch` 或 `uv sync --extra all`。

`analysis` 與 `torch` 是按證據選用的獨立 profile；`all` 僅供完整 smoke／CI 或明確需要所有分支時使用，不是每次啟動的硬門檻。先執行 `advanced_recipe_tools.py dependencies --json`；缺少所選 profile 時必須明確回報安裝命令，不得靜默降級。

`skill_smoke.py` 在完整 profile 中會實際建立小型 Torch model，驗證 forward/backward、activation hook 與 gradient snapshot，並以 fixture 執行 model-evaluation（校準／slice／bootstrap）、response-to-knowledge provenance gate、combined `mentor_response_gate`、visual-evidence lookup／hash gate 及 response-validator contract；lightweight 環境若未安裝 torch，只會回報 `SKIPPED_DEPENDENCY`，不會冒充 runtime PASS。

## 隔離 smoke check

先做隔離 copy smoke check；它只複製 Skill 與可選 knowledge，驗證 bootstrap 不會改寫來源：

```powershell
uv run --extra all python skills/hung-yi-ml-research-advisor/skill_smoke.py `
  --skill-root hung-yi-lee-ai-mentor-skills/skills/hung-yi-ml-research-advisor `
  --knowledge knowledge/normalized_principles.json `
  --output evaluation/mentor-skill-smoke-latest.json --json
```
