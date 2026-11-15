# S02 更深的模型 train 得更差

- 覆蓋度：已涵蓋（model bias vs optimization）
- 主題：加深後 train loss 反而變高

## 使用者訊息

我做一個感測器訊號的迴歸模型，MLP 加深實驗結果如下（train / val 都是 MSE，同一組超參數，各跑一次 100 epoch）：

| 層數 | train | val |
|---|---|---|
| 2 | 0.28 | 0.31 |
| 4 | 0.10 | 0.14 |
| 8 | 0.09 | 0.16 |
| 16 | 0.34 | 0.37 |

16 層結果最差，我想這是 overfitting，打算加 dropout 和 weight decay。可以嗎？

## 預期判斷

不是 overfitting：16 層的 train loss 就比 4 層高。4 層既然能到 0.10，16 層（函式集合包含淺層）理論上也應能做到，所以是 optimization 沒做好。加 dropout / weight decay 只幫 generalization，會讓 train 更難降。應調 lr / epoch / batch / 初始化，或加 skip connection、normalization。

## 關鍵檢查

- 先看 train loss，點出 16 層 train 就高。
- 用較淺模型當基準，並說明「函式集合巢狀」這個前提。
- 明確反對 dropout / weight decay 作為第一步。
- 誠實說 optimization 失敗沒有系統性排查，要靠嘗試。

## GOOD 答案必含

1. 第一問「training loss 多少」；train 差 -> model bias 或 optimization，train 好 val 差才是 overfitting。「不是所有不好都叫 overfitting」。(WeHM2xpYQpw S0004-S0012)
2. 這組數字就是他的例子結構：1-4 層 train 下降、5 層回升 -> 4 層可達的值，更深者必是 optimization。(WeHM2xpYQpw S0011)
3. 深模型函式集合包含淺模型（56 層 = 20 層加 36 層 identity）；巢狀前提若不成立此論證不成立，標為推論。(Taj1eHmZyWw S0053-S0057)
4. dropout / augmentation / L2 只幫 generalization，train 降不下去時沒用甚至更糟。(mPWvAN4hzzY S0072-S0086)
5. 手段：lr、epoch、batch、初始化、Adam；skip connection 使 surface 變平、normalization 主要幫 optimization；並承認「往往不知道問題出在哪」，靠信念加實驗。(Taj1eHmZyWw S0094-S0095; mPWvAN4hzzY S0036-S0040, S0057-S0063)
6. 提醒 val 只跑一次、多 seed 差異未知時別過度解讀（一般 ML，標示）；他有講同設定不固定 seed 結果會不同。(mPWvAN4hzzY 初始化 demo 段)

## 不可

- 同意「是 overfitting」並照單加正則化。
- 說課程給了系統化的 optimization 除錯流程（沒有）。
- 說「層數越多越好」或「淺層一定夠」。

## 評分（0-2）

| 準則 | 0 | 1 | 2 |
|---|---|---|---|
| R1 以 train loss 切分問題 | 未看 train | 看了但沒下結論 | 明確判為 optimization，並指出 train 就高 |
| R2 淺模型基準與巢狀前提 | 無 | 有基準無前提 | 有基準且點出巢狀前提與其限制 |
| R3 不鼓勵 generalization 旋鈕 | 建議 dropout/WD | 說「可能沒用」但未解釋 | 說明只幫 generalization 且讓 train 更難降 |
| R4 optimization 手段與誠實 | 無手段 | 列手段但說得像有保證 | 列手段並承認無系統排查、靠實驗 |
| R5 來源標示 | 無 | 部分 | 完整，推論有標 |
