# 診斷 profile 與安裝

profile 依「要鑑別的假設需要什麼測量」選，不是啟動必備。

| 證據或問題 | profile | 內容 | 安裝 |
|---|---|---|---|
| 只有分流、triage、課程教材搜尋、recipe_tools | core | stdlib | 無（`uv run`） |
| 曲線、bootstrap、消融、分組錯誤、calibration、預測表 | `analysis` | numpy、pandas、matplotlib | `uv sync --extra analysis` |
| 參數、gradient、activation | `torch` | torch 唯讀診斷 | CPU `uv sync --extra torch`；NVIDIA GPU `--extra torch-cu126`（舊驅動）或 `--extra torch-cu132`（driver CUDA ≥ 13.2，見 `nvidia-smi`） |
| 同一次要跑全部 | `all` | 以上全部 | `uv sync --extra all` |

流程：
1. 先用 `tools/triage.py` 或 skeleton.md 分流，找出能鑑別假設的最小測量。
2. 只選含該測量的 profile。缺依賴時回報 `INPUT_MISSING` 加上表中的安裝命令（在 collection 根目錄執行），不用口算取代；只有 metrics 表時不裝 torch。
3. 新證據需要別的 profile 才再載入。記錄 profile、輸入檔 hash、輸出路徑。

`uv run --project <collection 根目錄> python <skill>/tools/advanced_recipe_tools.py dependencies --json` 會列出目前缺什麼。各工具的旗標見 statistical-diagnostics.md 與 tensor-diagnostics.md。
