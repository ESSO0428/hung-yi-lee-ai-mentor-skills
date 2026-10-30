# 泛化

domain: generalization

來源真相：`knowledge/normalized_principles.json` 的 `MLRA-P0-005`、`MLRA-P0-014`。

## MLRA-P0-005 — train 好不等於未見資料好

- 規則：低訓練損失可以與高測試損失同時存在；train 好而 validation／test 差時轉查泛化與資料條件。
- 邊界：先確認 split 沒有洩漏且 train／test 目標相同。
- 證據：`DIRECT_COURSE_EVIDENCE`；`WeHM2xpYQpw:454-493`，1045.93–1133.25 秒，official。
- URL：https://www.youtube.com/watch?v=WeHM2xpYQpw

## MLRA-P0-014 — proxy 要先驗證再變成 regularizer

- 規則：只有在目標設定中確認候選指標與泛化有穩定關聯且代價可接受，才以受控實驗把它放入 objective。
- 邊界：norm、sharpness、sensitivity 只是課程中的候選 proxy，不保證跨架構／分佈有效。
- 證據：`DIRECT_COURSE_EVIDENCE`；`pivB5jEBOQw:30-63`，89.66–178.54 秒；`pivB5jEBOQw:64-88`，178.54–266.02 秒，均 official。
- URL：https://www.youtube.com/watch?v=pivB5jEBOQw

完整 claim、decision_rule、limitations 與 provenance 以 normalized JSON 為準。

