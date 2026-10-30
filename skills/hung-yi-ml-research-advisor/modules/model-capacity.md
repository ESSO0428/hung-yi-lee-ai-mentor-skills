# 模型容量

domain: model-capacity

來源真相：`knowledge/normalized_principles.json` 的 `MLRA-P0-003`、`MLRA-P0-007`。

## MLRA-P0-003 — 表示能力不足與求解器不足要分開

- 規則：若可表示函數集合不包含低損失解，單靠改進 solver 無法彌補表示能力不足；只有有模型偏差證據時才考慮增加特徵或彈性。
- 證據：`DIRECT_COURSE_EVIDENCE`；`WeHM2xpYQpw:121-165`，336.31–425.92 秒，official；`D_S6y0Jm6dQ:503-527`，1589.18–1675.34 秒，official。
- URL：https://www.youtube.com/watch?v=WeHM2xpYQpw 、https://www.youtube.com/watch?v=D_S6y0Jm6dQ

## MLRA-P0-007 — 簡化不是通用處方

- 規則：限制模型彈性可減少過擬合，但限制過強會造成欠擬合；調整容量或 regularization 時要同時檢查 train／validation。
- 邊界：課程圖像不是所有模型的單調定律，必須在目標資料上實測。
- 證據：`DIRECT_COURSE_EVIDENCE`；`WeHM2xpYQpw:730-765`，1666.96–1755.92 秒，official；`D_S6y0Jm6dQ:609-630`，1937.94–2025.30 秒，official。
- URL：https://www.youtube.com/watch?v=WeHM2xpYQpw 、https://www.youtube.com/watch?v=D_S6y0Jm6dQ

完整 claim、decision_rule、limitations 與 provenance 以 normalized JSON 為準。

