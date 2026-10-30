# P0 蒸餾：訓練診斷、容量與最佳化

## Dimension Coverage
- 研究決策：先以訓練表現定位 failure mode，再在 capacity 與 optimization 間建立可區分假說。

## Source Metadata
- URL: https://www.youtube.com/watch?v=WeHM2xpYQpw
- Source type: 李宏毅官方課程影片、ffprobe 已驗證、official timed transcript；一手來源；source weight: 2。
- Transcript chunks: `WeHM2xpYQpw:86-120` (247.85–336.09 秒), `WeHM2xpYQpw:121-165` (336.31–425.92 秒), `WeHM2xpYQpw:166-210` (425.92–515.03 秒), `WeHM2xpYQpw:335-375` (783.47–872.83 秒)。

## Key Findings
- 榜單或測試結果不佳時，先檢查 training loss，分辨模型是否連訓練資料也沒學好。
- 訓練 loss 高至少有兩個可競爭解釋：模型函數集合沒有低 loss 解，或最佳化沒有找到可達低 loss 的解。
- 有模型偏差證據時，增加輸入特徵或模型彈性是可考慮的分支；低分本身不是該證據。
- 在課程的深淺殘差網路例子裡，較深模型訓練 loss 較高指向最佳化問題，而不是過擬合。

## Contradictions
- 「擴大模型」與「先查最佳化」不是互斥口號，而是依訓練曲線與受控比較分支的不同結論。

## Inferences (clearly marked as inference, not fact)
- 推論：在資料、訓練預算與最佳化設定固定時，以 small/current/large 容量消融可提供鑑別 capacity 與 optimization 的訊息；這是專案實驗設計，不是課程逐字規則。

## Gaps and Missing Information
- 實際專案需確認不同架構是否存在課程例子中的函數集合包含關係，不能直接外推。
