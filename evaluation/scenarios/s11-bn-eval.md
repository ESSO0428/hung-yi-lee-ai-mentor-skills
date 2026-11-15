# S11 Batch Norm 在 eval 時掉分

- 覆蓋度：已涵蓋（BN 在 testing 的行為）；替代正規化未涵蓋
- 主題：train 好、eval 異常

## 使用者訊息

我的 CNN 有 Batch Norm，訓練時 batch 8（記憶體限制）。訓練 log：

```
epoch 30  train_acc 96.2  (train mode, batch 8)
```

部署時我一次只推論 1 張圖：

```
單張推論 accuracy 58.7%
把同一批 500 張一起丟（batch 500, 仍 train mode）accuracy 93.1%
```

我懷疑模型 overfit，要不要加資料增強？

## 預期判斷

不是 overfitting 的典型症狀（batch 500 的結果很好）。重點是 BN 的行為：訓練時用 batch 的 mean/std，testing 用訓練累積的 moving average；batch=1 沒有 μ、σ 可算，且 batch 8 太小導致統計粗。要確認是否用 eval 模式、moving average 是否被小 batch 汙染。注意他的 BN 講解不涵蓋小 batch 的替代方案（GroupNorm 等），要標一般 ML。

## 關鍵檢查

- 沒有直接回答 overfitting 或加增強。
- 區分 train mode / eval mode 以及 moving average。
- 指出 batch 8 的統計太小，批次依賴。
- LayerNorm/GroupNorm 等替代標未涵蓋。

## GOOD 答案必含

1. 要夠大的 batch 才算得出有意義的 μ、σ；batch size=1 時沒有 μ、σ 可算。(BABPWOkSbLE S0008-S0012)
2. testing 用 training 累積的 moving average，PyTorch 已處理；他記得預設 0.1 但自己不確定。(BABPWOkSbLE S0014-S0016)
3. 請使用者確認：推論時是否 model.eval()；batch 500 仍 train mode 的 93.1% 是用該批統計，不代表部署結果。（一般 ML 檢查，標示）
4. 位置（activation 前或後）自己試；γ=1、β=0 初始化。(BABPWOkSbLE S0007-S0014)
5. 為什麼 BN 有用：不要答 internal covariate shift，較有支持的是讓 error surface 較平滑；BN 像盤尼西林是「意外之喜」。他只談 training 動態，沒談 generalization。(BABPWOkSbLE S0018-S0021)
6. 類比：dropout 在 testing 要縮放，「做了 dropout 都沒進步，一看就是忘了乘」。(xki61j7z-30 S0043-S0064)
7. 一般 ML（標示）：小 batch 用 GroupNorm/LayerNorm、重新校準 running stats、gradient accumulation 無法替代 BN 統計。課程沒講。

## 不可

- 直接判 overfitting 並加增強。
- 說課程教了 GroupNorm/LayerNorm 的細節。
- 說 BN 的解釋是 internal covariate shift。

## 評分（0-2）

| 準則 | 0 | 1 | 2 |
|---|---|---|---|
| R1 不誤判為 overfitting | 判 overfitting | 同時提兩種 | 明說症狀不符，轉查 BN 行為 |
| R2 BN train/eval 機制 | 無 | 提 eval 模式 | 說明 moving average 與小 batch 汙染、batch=1 無統計 |
| R3 要求證據 | 無 | 問 eval 模式 | 同時要求 batch 設定、log 或重現實驗 |
| R4 未涵蓋標示 | 替代方案歸給他 | 提未標 | 標一般 ML |
| R5 來源標示 | 無 | 部分 | 完整 |
