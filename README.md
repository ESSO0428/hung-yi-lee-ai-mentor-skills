# hung-yi-lee-ai-mentor-skills

以李宏毅（宏毅老師）公開課程整理出的 AI 導師 skill 集合。根目錄的 `SKILL.md` 負責分流，底下有兩個 skill：

- **`hung-yi-ml-research-advisor`**：自己訓練的模型有問題，例如 loss 降不下來、overfitting、val 和 test 對不上、準確率高得不合理。它會照固定流程診斷：先要證據，再分流成 optimization、model bias、overfitting、mismatch 或 shortcut，接著為每個假設設計一個最便宜的鑑別實驗。另附可執行的診斷工具。
- **`hung-yi-genai-advisor`**：用 LLM 做東西，例如 prompting、context 與 agent 設計、RAG、微調還是寫 prompt、評估 LLM 輸出、微調後的遺忘、自我修正、成本。每條建議附出處和講課年份，課程沒講的會直說。目前沒有可執行工具，構想放在 `skills/hung-yi-genai-advisor/references/tool-ideas.md`。

兩個 skill 都只在使用者明確要求李宏毅的觀點時才啟用，沒有明說時只給一般 ML 回答。它們是依公開課程整理的觀點，不是本人，也不代表他背書。

這個集合只負責回答，不負責下載影片、語音轉文字或蒸餾；那些建置流程放在另一個專案。安裝後不需要任何影片或逐字稿就能使用。

## 透過 skills.sh 安裝

請安裝**整個集合**，不要單獨安裝底下的某一個 advisor：

```bash
npx skills add ESSO0428/hung-yi-lee-ai-mentor-skills \
  --skill hung-yi-lee-ai-mentor-skills
```

CLI 會詢問要裝給哪個 agent、裝在哪個範圍。不要在這條共用指令裡加 Codex 專屬的參數。

不要用 skills.sh 單獨安裝 `hung-yi-ml-research-advisor` 或 `hung-yi-genai-advisor`。它們依賴集合根目錄的 `pyproject.toml` 與 uv 環境，單獨裝會跑不起來。

已經裝過舊版的話，用這條更新（全域安裝時加 `-g`）：

```bash
npx skills update hung-yi-lee-ai-mentor-skills -g -y
```

## 建立 uv 環境

安裝只會複製檔案，不會建立 Python 環境。先找到集合的安裝路徑，再建一次環境：

```bash
# 安裝時選了全域範圍的話，在 `list` 後面加 --global
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

Windows PowerShell：

```powershell
# 安裝時選了全域範圍的話，在 `list` 後面加 --global
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

`uv sync` 會在集合目錄裡建立或更新 `.venv`。之後的指令都用 `uv run --project` 明確指定這個目錄，不需要啟用 shell 環境。

裝好後檢查目錄結構是否完整，看到 `"status": "PASS"` 就沒問題：

```bash
uv run --project "$SKILL_ROOT" python \
  "$SKILL_ROOT/skills/hung-yi-ml-research-advisor/bootstrap.py" \
  --skill-root "$SKILL_ROOT/skills/hung-yi-ml-research-advisor" --json
```

選配環境：

- `--extra analysis`：指標、統計、表格與畫圖。一般診斷用這個就夠了。
- `--extra torch`：只有要看參數、gradient、activation 這類模型內部資訊時才需要（CPU 版 torch）。NVIDIA GPU 改用 `--extra torch-cu126`（舊驅動）或 `--extra torch-cu132`（`nvidia-smi` 的 CUDA Version ≥ 13.2）。
- `--extra all`：刻意做完整 smoke test 或 CI 時才用，平常不需要。

建議在 `AGENTS.md` 和 `CLAUDE.md` 各加一條規則：

```text
執行 hung-yi-ml-research-advisor 的工具時，一律透過已安裝的 hung-yi-lee-ai-mentor-skills 集合根目錄，用 uv run --project "<集合路徑>" ... 執行。
```

## 快速開始

安裝後，請 agent「用李宏毅老師的角度」看你的問題，並附上相關資料：訓練與驗證曲線、指標、設定檔、預測結果、資料切分方式等。

- 訓練或評估的問題由 `hung-yi-ml-research-advisor` 處理：它會先確認證據，列出互相競爭的假設，再給出最便宜、最能區分這些假設的實驗，以及預期會看到的結果。
- 用 LLM 做東西的問題由 `hung-yi-genai-advisor` 處理：它會先判斷該改輸入（prompt、context）還是改模型，再依情境給建議。

直接從原始碼使用、沒有透過 skills.sh 安裝的話：

```bash
uv sync --extra analysis  # 指標、統計、表格與畫圖
# 只有需要看模型內部時才裝：
uv sync --extra torch  # CPU；NVIDIA GPU 改用 torch-cu126（舊驅動）或 torch-cu132（driver CUDA ≥ 13.2）
```

## 內容範圍與誠實規則

- 課程有講的內容附影片 ID 與段落；自己的推論會標明是推論；課程沒講的主題會直說，見各 skill 的 `references/not-covered.md`。
- 依證據強弱調整語氣：多講跨年份 > 單一講課 > 推論 > 課程沒講。
- 內容來自 58 講課程逐字稿的全文精讀。原始逐字稿、證據與蒸餾中間產物留在建置專案，不隨這個集合發佈。
- `evaluation/scenarios/` 是行為評估題，共 18 題，用來比較有沒有 skill 時回答的差異。

## 目錄結構

```text
hung-yi-lee-ai-mentor-skills/
├── SKILL.md                 # 入口：分流到兩個 advisor
├── pyproject.toml
├── uv.lock
├── evaluation/scenarios/    # 行為評估題
├── tests/
├── dev/                     # 維護者專用，執行時用不到
└── skills/
    ├── hung-yi-ml-research-advisor/
    │   ├── SKILL.md
    │   ├── references/
    │   └── tools/
    └── hung-yi-genai-advisor/
        ├── SKILL.md
        └── references/
```

`dev/` 放維護者專用的檢查工具，其中官方課程教材搜尋只在含教材索引的完整建置專案裡能用。使用這兩個 skill 不需要它。
