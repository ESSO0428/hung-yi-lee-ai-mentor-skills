# P0 蒸餾：評估、選模與驗證資料

## Dimension Coverage
- 研究決策：區分訓練、選模與最終評估角色，避免將可見結果反覆用於選擇後誤當成獨立證據。

## Source Metadata
- URL: https://www.youtube.com/watch?v=WeHM2xpYQpw
- Source type: 李宏毅官方課程影片、ffprobe 已驗證、official timed transcript；一手來源；source weight: 2。
- Transcript chunks: `WeHM2xpYQpw:842-885` (1935.26–2024.87 秒), `WeHM2xpYQpw:1096-1133` (2468.53–2556.87 秒), `WeHM2xpYQpw:1180-1222` (2653.73–2743.10 秒), `WeHM2xpYQpw:1223-1255` (2743.34–2831.59 秒)。

## Key Findings
- 反覆依公開測試或榜單結果挑模型，會讓選擇程序對那個分割適配，不能把最佳公開結果當作無偏的部署證據。
- 訓練集用於擬合參數，驗證集用於比較候選模型；最終測試不能代替驗證集參與選模。
- 當單次切分不穩定時，課程提出交叉驗證比較候選模型，並在全部訓練資料上重訓選定模型。

## Contradictions
- 有 validation split 不等於選模估計自動可靠；它是否被反覆檢視與用於決策仍影響解讀。

## Inferences (clearly marked as inference, not fact)
- 推論：實驗紀錄應追蹤哪些結果曾參與決策，讓後續者能辨識選擇偏差風險。

## Gaps and Missing Information
- 課程的 Kaggle public/private 例子不能直接決定所有時間序列、群組或部署資料的切分方法。
