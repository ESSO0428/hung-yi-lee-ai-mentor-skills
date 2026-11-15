# S10 分類任務用 MSE

- 覆蓋度：已涵蓋（loss 是 optimization 的旋鈕）
- 主題：loss 起步不動

## 使用者訊息

我做 10 類手寫字元辨識，網路最後一層 softmax，loss 用 MSE 對 one-hot：

```
model = nn.Sequential(..., nn.Linear(256, 10), nn.Softmax(dim=1))
loss_fn = nn.MSELoss()
epoch 1  loss 0.0900  acc 11%
epoch 5  loss 0.0899  acc 12%
epoch 20 loss 0.0897  acc 13%
```

隨機猜是 10%。學習率試過 1e-2 到 1e-4 都幾乎不動。同事說我該改 CrossEntropy，但我覺得 MSE 和 CE 最後最佳解一樣，沒差吧？

## 預期判斷

最佳解相同，差別在優化難度：MSE 在 loss 大的區域非常平坦（gradient 近 0），初始點若落在那裡就走不動；cross-entropy 同處有斜率。改成 CE。若改用 nn.CrossEntropyLoss，輸出層不要再接 softmax（已內含，會變加兩次）。

## 關鍵檢查

- 承認「最佳解相同」，再指出差別在優化難度。
- 指出 PyTorch 陷阱（CrossEntropyLoss 內含 softmax）。
- 強調此例的證據範圍（簡化設定，非證明）。
- 沒有把「acc 13%」解讀為 overfitting 或模型太小。

## GOOD 答案必含

1. 先質疑直覺：「真的是這樣嗎」；兩者最佳解相同，差在 optimization 難度。(O2VkP8dJ5FE S0010-S0014)
2. MSE 在 loss 大處 gradient 約 0；示範為 3 類、y3=-1000 的簡化設定，是例子不是證明。用 Adam 也許還有機會，但起步慢。(O2VkP8dJ5FE S0010-S0014)
3. 結論「可以改 loss function 來改變 optimization 的難度」，不起來時把 loss 選擇列入診斷。(O2VkP8dJ5FE)
4. 類別沒有遠近關係用 one-hot；CrossEntropyLoss 已內含 softmax，最後一層別再加。(O2VkP8dJ5FE S0002-S0008, S0010-S0011)
5. logistic regression 同理：square error 離目標遠時微分也近 0，「一開始就卡住」。(hSXFuypLukA S0017 S0021)
6. 此症狀 train 就卡住，屬 optimization，不是 overfitting。(WeHM2xpYQpw S0004-S0012)
7. 他沒講雙 softmax 的後果細節；若描述後果標為一般 ML。

## 不可

- 說 MSE 與 CE 沒差而放行。
- 建議加大模型或加資料。
- 把雙 softmax 的後果細節說成他的內容。

## 評分（0-2）

| 準則 | 0 | 1 | 2 |
|---|---|---|---|
| R1 正確診斷為 loss 導致的 optimization | 歸因其他 | 提 loss 但不確定 | 明確並解釋平坦區 gradient 近 0 |
| R2 處理「最佳解相同」的反駁 | 無視 | 同意其說法 | 承認並指出差別在優化難度 |
| R3 PyTorch 陷阱 | 無 | 提及 | 提及並附正確寫法 |
| R4 證據範圍誠實 | 說成定理 | 未說明 | 標為簡化示範 |
| R5 來源標示 | 無 | 部分 | 完整 |
