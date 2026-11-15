# 統計與評估診斷

數字證據需要確定性計算（metrics、train/val gap、bootstrap、分組錯誤、切分洩漏）時才用 `analysis` profile。缺依賴時回報 `uv sync --extra analysis`，不改成口算。報告只描述，不選介入手段；記錄輸入檔 hash、objective、分組欄位、seed、輸出路徑。

以下路徑省略前綴 `uv run --project <collection 根目錄> python <skill>/tools/`。

## recipe_tools.py（stdlib，免 profile）
- `summarize-metrics --input m.csv --objective '{"validation/loss":"min"}' --json`：長表或寬表 metrics，回報各 key 的 objective-aware 最佳 step。
- `compare-runs --baseline a.json --candidate b.json --objective ...`：兩個 run 的最佳值比較，需明講 min／max。
- `error-breakdown --input p.csv --group-by slice`：分組錯誤數與錯誤率。
- `config-diff --baseline a.json --candidate b.json`：兩份設定的新增／移除／變更路徑。
- `plot-metrics --input m.csv --metric-key k --output-svg out.svg`：無依賴 SVG 曲線。

## advanced_recipe_tools.py（analysis）
子命令：`dependencies`、`summarize-metrics`、`capacity-ablation`、`compare-groups`、`training-dynamics`、`error-analysis`、`plot-training`。
- `training-dynamics --input m.csv --train-metric-key train/loss --validation-metric-key val/loss --json`：train／val 曲線與 gap，對應 skeleton.md 的分流。
- `capacity-ablation --input m.csv --metric-key val/loss --objective min --capacity-column capacity`：容量掃描，找 train 降但 held-out 不降的拐點。
- `compare-groups --input s.csv --group-column variant --value-column score --baseline baseline --candidate candidate [--paired-column seed]`：bootstrap 區間與配對差；單次結果不是證據，多 seed 才有分佈。
- `error-analysis --input p.csv --label-column label --prediction-column prediction --group-by slice`：分組錯誤分析。
- `dependencies --json`：列出缺哪些 profile 與安裝命令。

## model_evaluation.py（analysis）
`classification`（二元／多類，加 `--score-column` 得 calibration、Brier）、`regression`（MAE、RMSE、R²）、`ranking`（MRR、Recall@K、NDCG@K；`--k`），皆支援 `--group-by` 切片與 bootstrap。欄位名用實際欄位；缺列要報告，不靜默丟棄。

## dataset_split_audit.py
`--input split.csv --id-column sample_id --split-column split --group-column group_id --content-hash-column content_hash --label-column label`：查跨 split 洩漏、split 筆數與 label 分佈。`FAIL` 是資料完整性結果，不是模型架構有錯。有 sample ID、群組或內容 hash 時，下泛化結論前先跑；只有摘要指標時，只報觀察數字並列出還缺的實驗。
