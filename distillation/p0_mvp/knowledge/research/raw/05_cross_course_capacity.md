# P0 蒸餾：跨課程容量與誤差來源交叉檢查

## Dimension Coverage
- 研究決策：以第二支官方課程交叉核對 bias／variance 與模型函數集合概念，避免單一影片或標題驅動的規則。

## Source Metadata
- URL: https://www.youtube.com/watch?v=D_S6y0Jm6dQ
- Source type: 李宏毅官方課程影片、ffprobe 已驗證、official timed transcript；一手來源；source weight: 2。
- Transcript chunks: `D_S6y0Jm6dQ:479-502` (1500.58–1589.18 秒), `D_S6y0Jm6dQ:503-527` (1589.18–1675.34 秒), `D_S6y0Jm6dQ:609-630` (1937.94–2025.30 秒)。

## Key Findings
- 誤差來源的診斷決定改進方向；複雜模型不必然在 testing data 有更低 error。
- 可表達的函數集合不含低 loss 解時，僅改善求解器不能補足表示限制。
- 容量與泛化要同時觀察；不是僅根據單一 error rate 選擇更複雜模型。

## Contradictions
- 大模型的訓練／驗證改善支持 capacity 假說；大模型表現差本身不能單獨判成過擬合或 optimization，仍需訓練證據。

## Inferences (clearly marked as inference, not fact)
- 推論：跨 seed 的 paired capacity ablation 能提高對「容量效果」而非偶然變異的信心。

## Gaps and Missing Information
- 這些基礎誤差來源課程不直接回答特定 Transformer attention 模組是否適合某資料集。
