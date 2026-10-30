# 目標與損失設計

domain: loss-design

來源真相：`knowledge/normalized_principles.json` 的 `MLRA-P0-012`。

## MLRA-P0-012 — 分類停滯先查 loss／activation／gradient

- 規則：在課程的 softmax 分類設定中，MSE 的高損失區域梯度很小，而 cross-entropy 提供可用斜率；先檢查輸出啟用與損失是否匹配，再診斷梯度，不要只增加層數。
- 邊界：不把這個例子泛化成「MSE 永遠不可用」。
- 證據：`DIRECT_COURSE_EVIDENCE`；`O2VkP8dJ5FE:437-474`，1068.31–1156.61 秒，official。
- URL：https://www.youtube.com/watch?v=O2VkP8dJ5FE

完整 claim、decision_rule、limitations 與 provenance 以 normalized JSON 為準。

