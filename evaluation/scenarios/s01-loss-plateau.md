# S01 loss 卡在平台

- 覆蓋度：已涵蓋（optimization）
- 主題：loss 不降、被懷疑 local minima

## 使用者訊息

我在訓練一個 6 層的 Transformer encoder 做文字分類（約 40 萬筆）。Adam，lr=3e-3，batch 64。log 如下：

```
step   200  train_loss 1.93
step   400  train_loss 1.31
step   600  train_loss 1.12
step   800  train_loss 1.10
step  1000  train_loss 1.11
step  3000  train_loss 1.09
step  8000  train_loss 1.10
```

loss 從 step 800 之後完全不動。我猜是卡在 local minimum，要不要換成 SGD 加 momentum 重來，或是直接加大模型？

## 預期判斷

不能下「local minimum」結論。先查平台期的 gradient norm 與 lr 曲線：norm 仍大 -> 多半是 lr 太大、谷壁震盪（先調小 lr、加 decay/warm-up）；norm 近 0 才談 critical point（saddle 較常見）。加大模型與換 optimizer 都是未經診斷的旋鈕。

## 關鍵檢查

- 要求 gradient norm（與前幾百 step 的曲線），而非直接接受「local minimum」。
- 區分 critical point / plateau / 谷壁震盪，用詞是 critical point 而非 local minima。
- 把 lr 3e-3 列為頭號嫌疑，並說明如何驗證（降 lr 重跑短程）。
- 指出 train loss 平台不等於 val 問題，也不先動模型大小。

## GOOD 答案必含

1. 質疑使用者診斷：「你確認過 gradient 真的很小嗎」，先看 gradient norm。(HYUXEeh3kwY S0001-S0004)
2. 平台期 gradient 仍大 -> 谷壁來回震盪，往 lr/optimizer 查；真正近 0 才分 saddle / local minima（看 Hessian eigenvalue，實務幾乎不算）。(HYUXEeh3kwY S0001-S0003; QW6uINn7uGk S0004-S0017)
3. local minima 在高維不常見，是「假說加經驗」不是定理。(QW6uINn7uGk S0018-S0023)
4. lr 的三種曲線型態（太小慢、稍大快降後卡平台、太大飛出）；前幾次 update 就要看曲線。(yKKNr-QKz2Q S0006-S0008)
5. 提到 lr decay / warm-up 的角色，並如實說 warm-up 他自承沒有完整解釋。(HYUXEeh3kwY S0019-S0024)
6. 若建議具體 lr 值、warm-up 長度、clip 等，明說課程沒給數值，屬一般 ML。

## 不可

- 附和「卡在 local minimum」並直接建議換更大模型。
- 把具體 lr 範圍或 gradient clipping 說成他的建議。
- 不問 gradient norm 就下結論。
- 自編他說過的話。

## 評分（0-2）

| 準則 | 0 | 1 | 2 |
|---|---|---|---|
| R1 要求 gradient norm / 曲線證據 | 未要求，直接下結論 | 提到看曲線但未點名 gradient norm | 明確要求平台期 gradient norm，並說明兩種結果各代表什麼 |
| R2 質疑 local minimum 說法 | 接受 | 溫和提醒 | 指出 critical point 分類，且說 local minima 非常見主因（標為經驗） |
| R3 lr / 谷壁震盪假說與驗證 | 未提 | 提 lr 但無驗證法 | 提 lr 為首要嫌疑，附可執行的短程驗證 |
| R4 不亂動旋鈕 | 建議加大模型/換 optimizer 為主 | 提及但未排序 | 明說診斷前不動模型大小，換 optimizer 只在 train 壓不下去時 |
| R5 來源標示 | 無 | 部分有來源 | 每項講義支持的主張附 id+段落，其餘標推論 |

另評 README 的共通準則 G1-G4。
