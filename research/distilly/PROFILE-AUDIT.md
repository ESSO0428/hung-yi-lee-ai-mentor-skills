# Content-only Distilly profile audit（2026-10-29）

## 結果

**PASS（本專案的來源忠實範圍）**

| 檢查 | 結果 |
| --- | --- |
| 上游 `merge_research.py` 重現 | P0–P3 四個 family 均 `PASS`；不修改 canonical raw sources。 |
| P0–P3 dossier 的 direct YouTube URLs | 分別 6、7、10、8 個；每一個都可在同 family 的 raw research notes 找到。 |
| `PROFILE-DRAFT.md` 的 direct source anchors | 4 個，皆可回溯到 P0–P3 raw notes。 |
| 非人格模仿邊界 | profile 明示 content-only、禁止口吻／Persona 模仿。 |
| candidate boundary | P1–P3 明示維持 candidate-only；P2 AGY supplemental 不當 canonical evidence。 |

可重跑的 merge 證據是 [evaluation/distilly-reproducibility-latest.json](../../evaluation/distilly-reproducibility-latest.json)。

## Upstream `quality_check.py` 的適用性結果

以 `budget-friendly` profile 對 `PROFILE-DRAFT.md` 直接執行上游 checker 時，結果為 **not passed**；這不能被報成上游 Persona quality gate 已通過。根因是 checker 的假設與本專案刻意採用的 content-only layout 不相容：

1. source-like URL heuristic 接受 `id=`／`vid=` 等 query marker，未把 YouTube 的 `v=` 視為 concrete source；因此已存在的四個直接影片 URL 被計為 0。
2. checker 尋找英文或簡體中文的 `limitations`、`honest boundaries`、`internal tension` 關鍵字；profile 使用繁體中文的「誠實邊界」與「張力」，語意有、字串規則未命中。
3. checker 把任何 Markdown blockquote 當作 copyright-risk；profile 開頭的 scope disclaimer 觸發該規則，並非逐字稿傾倒。
4. checker 預期 profile directory 內有 `knowledge/research/merged/summary.md`；本專案把可重現 raw research notes 保留在 `distillation/p*/...`，不複製來源以湊出另一個 Persona package layout。

本輪**不**為了讓 generic Persona checker 變綠而加入 expression/persona 內容、改寫繁體中文標籤、複製 raw sources 或刪除必要的 scope disclaimer。正確的品質證據是上方的 provenance／reproducibility audit；若未來要將這個 content-only profile 發佈成獨立 Distilly Persona Skill，才應另做一個明確的 compatibility adapter 與測試。
