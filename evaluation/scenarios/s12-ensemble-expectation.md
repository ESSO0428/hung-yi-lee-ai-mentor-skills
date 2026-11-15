# S12 ensemble 的期待

- 覆蓋度：已涵蓋原理；推論成本與部署未涵蓋
- 主題：期待 5 個模型平均「自然進步」

## 使用者訊息

表格分類任務，我訓練了 5 個設定幾乎一樣的模型（同一份 train、同架構、只換隨機種子）：

```
單模型 train acc 100%  val acc 82.0~82.6%
5 模型平均 val acc 82.9%
```

我預期 ensemble 至少能再加 3-5 個百分點，為什麼只進步 0.5？另一種情況：我有一個很淺的模型 train 就只有 71%，也想靠 ensemble 補，可以嗎？

## 預期判斷

兩個情況分開看。(1) 高變異模型（train 100% / val 82）適合 Bagging 降 variance，但前提是各模型要有足夠差異；同資料同架構只換 seed，彼此太像，平均效果有限，Random Forest 還要在分支隨機禁用 feature。(2) 淺模型 train 就差是 bias 問題，Bagging 不會讓模型更能 fit；要 Boosting 或加容量。ensemble 是撞牆後的下一招，不是第一招；先做 bias/variance 診斷。

## 關鍵檢查

- 沒有承諾進步幅度。
- 區分 Bagging（降 variance）與 Boosting（弱模型）。
- 指出差異度（diversity）不足的可能性。
- 推論成本、部署代價標為課程沒講。

## GOOD 答案必含

1. 失敗型態選方法：train 低 val 高 -> Bagging/RF；train 本身就高 -> Boosting 或加容量。「Bagging 是用在很強的 model，Boosting 是用在弱的 model」。(tH9FH1DH5n0 S0004 S0007 S0014)
2. 初音實驗：深度 5 的樹做 100 棵 RF 仍 fit 不出來，AdaBoost T=100 近乎完美；「Bagging 不會讓模型更能 fit data」。(tH9FH1DH5n0 S0063)
3. Bagging 用有放回抽樣造多個資料集；RF 光 resample 不夠，樹會太像，要隨機禁用 feature；他沒給保留比例。(tH9FH1DH5n0 S0004-S0006 S0011-S0012)
4. 資料少、不想切 val 可用 OOB error，只適用 Bagging 類。(tH9FH1DH5n0 S0012-S0013)
5. ensemble 是「大招」，是撞牆後的下一招；前面要先做 bias/variance 診斷。(tH9FH1DH5n0 S0003; D_S6y0Jm6dQ S0018)
6. 若最終模型要合併不同模型：Stacking 要分兩份資料，否則死背 training data 的模型會被 final classifier 完全信任。(tH9FH1DH5n0 S0081-S0083)
7. 一般 ML（標示）：差異度量測、推論延遲與記憶體成本、同 seed 集成的期望增益大小，以及「為何只進步 0.5」只能當假說（課程沒有定量預期）。
8. NN 不一定需要 Bagging：常見問題是無法在 train 上 overfit；此例 train 100% 反映可 overfit。(tH9FH1DH5n0 S0007 S0008)

## 不可

- 承諾 ensemble 的進步幅度或說 3-5 個百分點合理。
- 對淺模型 train 71% 建議 Bagging。
- 把推論成本、diversity 度量說成他的內容。

## 評分（0-2）

| 準則 | 0 | 1 | 2 |
|---|---|---|---|
| R1 依 train/val 選 Bagging 或 Boosting | 一律說 ensemble 有用 | 提兩種未對症 | 兩情況各自對症並引他的原話 |
| R2 差異度假說 | 無 | 提及 | 解釋同資料同架構彼此太像，並標為假說 |
| R3 不承諾增益 | 承諾 | 含糊 | 明說沒有定量預期，建議用 val/OOB 驗證 |
| R4 未涵蓋標示 | 推論成本歸給他 | 提及未標 | 標一般 ML |
| R5 來源標示 | 無 | 部分 | 完整 |
