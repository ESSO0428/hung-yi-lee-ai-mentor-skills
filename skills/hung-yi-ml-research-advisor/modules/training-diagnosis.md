# 訓練診斷

domain: training-diagnosis

來源真相：`knowledge/normalized_principles.json` 的 `MLRA-P0-001`、`MLRA-P0-002`。

## MLRA-P0-001 — 先分辨 train 與 test 的失敗位置

- 規則：測試或榜單表現不滿意時，先檢查訓練資料上的損失；先分辨訓練集也失敗，還是訓練集良好但測試集失敗。
- 邊界：課程以作業／Kaggle 為例，仍須確認訓練與部署指標可比。
- 證據：`DIRECT_COURSE_EVIDENCE`；`WeHM2xpYQpw:86-120`，247.85–336.09 秒，official。
- URL：https://www.youtube.com/watch?v=WeHM2xpYQpw

## MLRA-P0-002 — 高 train loss 有競爭假說

- 規則：高訓練損失至少可能來自 model capacity 不足或 optimization 未成功；不能只憑一個數值決定加大模型。
- 操作：把 capacity 與 optimization 當成競爭假說，蒐集能區分兩者的訓練證據；資料與標籤問題仍可能存在。
- 證據：`DIRECT_COURSE_EVIDENCE`；`WeHM2xpYQpw:166-210`，425.92–515.03 秒，official。
- URL：https://www.youtube.com/watch?v=WeHM2xpYQpw

完整 claim、decision_rule、limitations 與 provenance 以 normalized JSON 為準。

