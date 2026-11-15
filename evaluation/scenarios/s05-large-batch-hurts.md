# S05 大 batch 變差

- 覆蓋度：已涵蓋（batch 與 optimization / generalization）；lr 縮放規則未涵蓋
- 主題：為了加速把 batch 拉大

## 使用者訊息

為了縮短訓練時間，我把 batch size 從 32 調到 4096（8 張 GPU），其他不變，lr=1e-3 Adam，各訓練 30 epoch：

```
batch   train_loss   val_acc   time/epoch
32      0.21         88.4      14 min
4096    0.46         82.1      2.1 min
```

結論是大 batch 讓模型 overfit 嗎？我要怎麼用大 batch 又不掉分？

## 預期判斷

train loss 本身就比較高，所以不是 overfitting，是 optimization 問題（同 epoch 下大 batch 的 update 次數少很多）。小 batch 的 noise 對 optimization 有幫助。只有在把 train 調到一樣好之後，大 batch 的 test 仍較差，才叫 generalization gap（sharp/flat minima 解釋「尚待研究、不是每個人都相信」，不可當定論）。要同時用大 batch 與高準確度需要特別方法（課程沒講），lr 縮放規則未涵蓋。

## 關鍵檢查

- 看 train loss 而非直接判 overfitting。
- 區分 optimization 與 generalization 兩種大 batch 效應。
- 對 sharp/flat minima 保持保守，標為未定論。
- 把 epoch 與 update 次數分開，要求使用者報 update 數。

## GOOD 答案必含

1. 先看 train：大 batch 在 training 就變差，這是 optimization 問題，不是 overfitting。(zzbr1h9sF54 S0009-S0010)
2. 每 epoch 更新數 N/B；epoch 與 update 要分開報。(Taj1eHmZyWw S0030-S0034; bHcJCp2Fyxs S0027-S0030)
3. 小 batch noise 的「一個可能的解釋」：不同 batch 的 loss function 不同，一個卡住另一個不一定卡。(zzbr1h9sF54 S0010-S0011)
4. 若 train 調到一樣好後 test 仍差才是 overfitting；解釋為 sharp/flat minima，他明說尚待研究。(zzbr1h9sF54 S0011-S0014)
5. 大 batch 單步不一定慢，數字是特定硬體實測，請自己量；有論文 76 分鐘訓練 BERT（batch 約三萬）但需特別方法，他沒講。(zzbr1h9sF54 S0005-S0008 S0015-S0016)
6. 結論：batch size 是 hyperparameter。(zzbr1h9sF54)
7. 一般 ML（標示）：lr 隨 batch 線性縮放、warm-up 長度、LARS/LAMB 等，課程沒有給規則；可建議先把 lr/update 數調到讓 train loss 追上，再看 val。

## 不可

- 把大 batch 變差一律歸因 overfitting 或 sharp minima 定論。
- 把 lr 縮放規則說成他的建議。
- 說大 batch 每步一定更慢或更快而不提硬體相依。

## 評分（0-2）

| 準則 | 0 | 1 | 2 |
|---|---|---|---|
| R1 以 train loss 判斷成因 | 判 overfitting | 看 train 但結論含混 | 明確說這是 optimization，generalization 須 train 持平後才談 |
| R2 update 數 / epoch 分開 | 無 | 提及 | 並建議按 update 數或調 lr 驗證 |
| R3 sharp/flat 保守 | 當定論 | 提及無保留 | 標為未定論 |
| R4 未涵蓋標示 | 縮放規則歸給他 | 給規則未標 | 明確標一般 ML |
| R5 來源標示 | 無 | 部分 | 完整 |
