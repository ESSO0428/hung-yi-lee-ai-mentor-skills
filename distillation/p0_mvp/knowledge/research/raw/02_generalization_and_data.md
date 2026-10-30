# P0 蒸餾：泛化、資料與容量取捨

## Dimension Coverage
- 研究決策：把訓練成功但驗證／測試失敗與訓練失敗分開；檢查資料變換與分佈，而非把容量當作萬用修正。

## Source Metadata
- URL: https://www.youtube.com/watch?v=WeHM2xpYQpw
- Source type: 李宏毅官方課程影片、ffprobe 已驗證、official timed transcript；一手來源；source weight: 2。
- Transcript chunks: `WeHM2xpYQpw:454-493` (1045.93–1133.25 秒), `WeHM2xpYQpw:571-608` (1311.32–1399.28 秒), `WeHM2xpYQpw:609-647` (1399.40–1489.32 秒), `WeHM2xpYQpw:730-765` (1666.96–1755.92 秒), `WeHM2xpYQpw:1287-1325` (2919.08–3007.49 秒)。

## Key Findings
- 記住訓練樣本與對未見樣本泛化是不同現象；低 training loss 與高 testing loss 可以同時存在。
- 限制模型彈性可降低部分過擬合風險，但限制過強也可能造成欠擬合；容量／正則化調整應同看訓練與驗證行為。
- 資料擴增必須維持該任務的 label 語意；不能把任意變換假定為正確 augmentation。
- 若 train／test 資料分佈不匹配，單純增加既有 train 分佈資料未必改善目標表現。

## Contradictions
- 複雜度降低與複雜度增加都可能在不同證據條件下合理；課程不支持單一方向的 complexity ideology。

## Inferences (clearly marked as inference, not fact)
- 推論：在提出新資料收集前，以 learning curve、來源分佈與標註檢查區分 quantity、shift 與 label 問題，能讓資料投資更具鑑別性。

## Gaps and Missing Information
- 各任務可接受的 augmentation、資料 shift 定義與部署目標需以專案資料確認。
