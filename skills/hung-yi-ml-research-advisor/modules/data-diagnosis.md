# 資料診斷

domain: data-diagnosis

來源真相：`knowledge/normalized_principles.json` 的 `MLRA-P0-006`、`MLRA-P0-011`。

## MLRA-P0-006 — augmentation 必須保留標籤語意

- 規則：提出資料擴增前，說明變換後為何仍保留正確標籤，以及適用資料範圍；任意變換可能產生錯誤標籤關係。
- 證據：`DIRECT_COURSE_EVIDENCE`；`WeHM2xpYQpw:571-608`，1311.32–1399.28 秒；`WeHM2xpYQpw:609-647`，1399.40–1489.32 秒，均 official。
- URL：https://www.youtube.com/watch?v=WeHM2xpYQpw

## MLRA-P0-011 — 同一分佈的更多資料未必解決目標問題

- 規則：train／test 分佈不匹配時，先查資料取得與切分、確認目標分佈，再決定需要新資料、重加權或適應方法。
- 邊界：重加權是候選方向，不是該字幕片段的直接教導。
- 證據：`DIRECT_COURSE_EVIDENCE`；`WeHM2xpYQpw:1287-1325`，2919.08–3007.49 秒，official。
- URL：https://www.youtube.com/watch?v=WeHM2xpYQpw

完整 claim、decision_rule、limitations 與 provenance 以 normalized JSON 為準。

