# S06 標註資料很少

- 覆蓋度：部分涵蓋（半監督、加資料、保守微調；小資料量化門檻未涵蓋）
- 主題：500 筆標註、5 萬筆未標註

## 使用者訊息

我要做客服對話的 5 類意圖分類。標註資料只有 500 筆（每類約 100），未標註約 5 萬筆（沒有 label 但領域一樣）。用 BERT-base 微調：

```
train acc 100%   val acc 71%   (val 100 筆)
```

標註成本很高，我想用 self-training，把 5 萬筆全部用 0.5 以上信心標上去再訓練。這樣可以嗎？還有其他建議嗎？

## 預期判斷

train 100%、val 71% 才是 overfitting，在標註少的情況下合理。處方依序考慮：更多真實資料、合理 augmentation、限制彈性（保守微調少 epoch、少參數）。半監督有沒有用取決於假設是否成立，不是永遠有用；self-training 的初始模型太差會標出壞 pseudo-label，信心門檻他說是 open question，不給數字。0.5 門檻與「全標上去」無課程依據。

## 關鍵檢查

- 先確認 train/val 的狀態（已有）並判 overfitting；val 100 筆的不確定性（課程未講，標一般 ML）。
- 說明半監督的前提假設與初始模型品質。
- 對 pseudo-label 門檻不給假權威。
- 預訓練 + 保守微調的建議。

## GOOD 答案必含

1. train 好 val 差 = overfitting；加資料像「萬能丹」，但現實常拿不到。處方三類：更多真實資料 -> augmentation -> 限制彈性（先後為整理者推論）。(WeHM2xpYQpw S0014-S0019; D_S6y0Jm6dQ S0019-S0021)
2. 半監督：缺的是 label 不是 data；有沒有用取決於假設（low-density、smoothness、cluster）是否成立，「不見得永遠有用」。(fX_guE7JNnY S0002-S0005)
3. Self-training 流程；挑哪些 pseudo-label 是 open question；初始模型太差產生不出好 pseudo-label；NN 用 hard label，soft label 沒新資訊。(fX_guE7JNnY S0013-S0020; wulqhgnDr7E S0002)
4. 可搭配 entropy regularization 的想法（unlabeled 輸出越集中越好）。(fX_guE7JNnY S0021-S0024)
5. 少量目標資料微調要保守：source 當初始值、只跑兩三個 epoch、conservative training；「train 下去就壞掉」。(qD6iD4TFsdQ S0010-S0012; Mnk_oUrgppM S0006)
6. 一般 ML（標示）：confidence 門檻怎麼訂、FixMatch / consistency regularization、100 筆 val 的信賴區間與 k-fold、類別平衡、先用 LLM few-shot 當 baseline。課程沒講。

## 不可

- 說 0.5 門檻或「全部標上」有課程依據。
- 說 self-training 必定進步（只有 2016 助教作業的觀察）。
- 把 FixMatch 等歸給他。
- 忽略 val 只有 100 筆。

## 評分（0-2）

| 準則 | 0 | 1 | 2 |
|---|---|---|---|
| R1 診斷 overfitting 與處方順位 | 只推 self-training | 提處方未排序 | 判 overfitting，並列三類處方 |
| R2 半監督前提 | 說必有用 | 提前提 | 說明假設與初始模型品質，並要求驗證 |
| R3 門檻不假權威 | 認可 0.5 | 質疑但無理由 | 明說他沒給門檻、屬 open question |
| R4 保守微調 | 無 | 提及 | 提 epoch 少、conservative 與理由 |
| R5 未涵蓋標示與來源 | 現代方法歸給他 | 未標 | 明確標示並附來源 |
