# S03 val 很好、test 很差

- 覆蓋度：部分涵蓋（mismatch 與 val 被用壞已涵蓋；洩漏與分組切分未涵蓋）
- 主題：val/test 落差，來源不同

## 使用者訊息

我做的是工廠設備異常預測（二元分類，約 8 萬筆資料，來自 3 條產線）。隨機打散後 80/10/10 切 train/val/test：

```
train acc 0.97   val acc 0.95
```

我調了大約 200 組超參數（層數 x 寬度 x lr x dropout）選 val 最高的，最後在另一條產線新收的 test（5000 筆）上只有 0.78。這是 overfitting 嗎？我該怎麼辦？

## 預期判斷

train 與 val 都高，test 低：不能直接叫 overfitting。兩個候選原因：(1) mismatch/domain shift：test 的產生方式（另一條產線）與 train/val 不同，加資料無用；(2) val 被反覆用來選模（200 組），val 分數樂觀。須先確認 train 與 test 的產生方式，並以 test 前的 train 與 val 的構成檢查。隨機切分是否讓同產線資料同時落在 train/val（洩漏、group split）課程沒講，須標為一般 ML。

## 關鍵檢查

- 區分 overfitting（train 好 val/test 差）與 mismatch；提出要檢查資料產生方式。
- 指出 val 選了 200 組，可信度降低。
- 不把 mismatch 當 overfitting 開藥方（加 dropout、加正則化）。
- 洩漏、group split 等標示「課程未涵蓋」。

## GOOD 答案必含

1. 「並不是所有不好都叫 overfitting」；val 與 train 差不多，不符合 overfitting 定義。(WeHM2xpYQpw S0009 S0012)
2. mismatch：加資料沒幫助，判斷靠對資料產生方式的理解，他沒給統計檢定；他自承有人把它算進 overfitting，重點是處方不同。(WeHM2xpYQpw S0034-S0036; Mnk_oUrgppM S0001-S0002)
3. 先量夾住問題的兩個數字：source->target baseline 與 target->target 上限（標為推論）。(Mnk_oUrgppM S0002-S0004)
4. 掃 200 組就是在有限候選集上「做訓練」，val 也會 overfit；他有「模擬考可考多次、大考只一次」的說法。(xQXh3fSvD1A S0003-S0006 大意; Taj1eHmZyWw S0066-S0070)
5. val 系統性偏一邊先查「步驟一」：資料與目標是否一致，畫圖看殘差是否單向。(Taj1eHmZyWw S0038-S0041)
6. 一般 ML（須標示非他所講）：隨機切分在同一產線/裝置/時間相關資料上可能洩漏，需 group 或 line-based split、要有 held-out 產線當 val；adversarial validation 檢測 shift。
7. 他提的方向：改切分、換資料或 adaptation；少量目標資料可保守 fine-tune。(Mnk_oUrgppM S0005-S0006; qD6iD4TFsdQ S0009-S0014)

## 不可

- 把 mismatch 判成 overfitting 並建議加正則化/dropout。
- 把洩漏檢查、group split、adversarial validation 說成他的內容。
- 說課程有 shift 的統計檢定。

## 評分（0-2）

| 準則 | 0 | 1 | 2 |
|---|---|---|---|
| R1 分辨 overfitting / mismatch | 判 overfitting | 提兩者但未對症 | 說明為何不是 overfitting，並引導檢查產生方式 |
| R2 val 被用壞 | 未提 | 提及但無理由 | 點出 200 組選模使 val 樂觀，並建議新 held-out |
| R3 夾住 gap 的量測 | 無 | 有一個數字 | 提出 source->target 與 target->target 兩端 |
| R4 未涵蓋標示 | 洩漏/group split 歸給他 | 提到但未標 | 明確標示課程沒講並作為一般 ML 給出 |
| R5 來源標示 | 無 | 部分 | 完整 |
