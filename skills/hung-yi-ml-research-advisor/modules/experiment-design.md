# 實驗設計

domain: experiment-design

來源真相：`knowledge/normalized_principles.json` 的 `MLRA-P0-013`、`MLRA-P0-015`。

## MLRA-P0-013 — 先做受控 capacity ablation

- 規則：在算力允許且其餘條件可固定時，比較 small／current／large 的 train／validation 走勢，比直接擴大架構更能區分 capacity 與 optimization。
- 證據：`PROJECT_INFERENCE`／`CONDITIONAL_SUGGESTION`；`WeHM2xpYQpw:251-291`，605.66–695.16 秒；`D_S6y0Jm6dQ:479-502`，1500.58–1589.18 秒，均 official。
- 邊界：這是本專案根據課程例子形成的推論，不是教師逐字指示。

## MLRA-P0-015 — 先定位方法改變的層

- 規則：評估新技術前，辨識它改變的是候選函式集合、評量標準，還是找出最佳函式的程序；一層有作用不代表能取代其餘層。
- 邊界：同一方法可能跨層作用；本原則的兩個 source 為 ASR，需保留 `REVIEW_REQUIRED` 邊界。
- 證據：`DIRECT_COURSE_EVIDENCE`；`phQK8xZpgoU:458-491`，1260.00–1349.98 秒；`phQK8xZpgoU:492-525`，1350.00–1424.98 秒；`XLyPFnephpY:360-363`，900.00–912.74 秒，均 ASR。
- URL：https://www.youtube.com/watch?v=phQK8xZpgoU 、https://www.youtube.com/watch?v=XLyPFnephpY

完整 claim、decision_rule、limitations 與 provenance 以 normalized JSON 為準。

