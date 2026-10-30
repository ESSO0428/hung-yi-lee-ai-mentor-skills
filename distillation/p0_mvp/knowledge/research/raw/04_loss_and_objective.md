# P0 蒸餾：損失設計與最佳化訊號

## Dimension Coverage
- 研究決策：分類訓練失敗時，把輸出與 loss 的配對視為待檢查條件之一，不把更大模型當作預設處置。

## Source Metadata
- URL: https://www.youtube.com/watch?v=O2VkP8dJ5FE
- Source type: 李宏毅官方課程影片、ffprobe 已驗證、official timed transcript；一手來源；source weight: 2。
- Transcript chunks: `O2VkP8dJ5FE:437-474` (1068.31–1156.61 秒)。

## Key Findings
- 在課程展示的 softmax 分類案例中，MSE 的高 loss 區域可能給出很小梯度，cross-entropy 則提供不同的有效斜率；loss 選擇會改變最佳化地形。
- 因此分類訓練卡住時，輸出啟用、loss 與梯度行為都屬可檢查的假說。

## Contradictions
- 這個例子不支持「MSE 在任何分類任務均不可用」或「換 loss 一定改善」。

## Inferences (clearly marked as inference, not fact)
- 推論：先以固定模型和 evaluator 檢查 loss／輸出設定，再與其他單一變因比較，可避免把同時多項修改誤歸因。

## Gaps and Missing Information
- 一般部署 metric 對齊、ranking metric 停滯與後處理問題需要補充的直接來源；不可把本筆分類梯度例子過度泛化。
