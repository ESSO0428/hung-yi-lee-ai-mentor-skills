# P0 蒸餾：研究決策綜合與證據邊界

## Dimension Coverage
- 將 P0 原則整理為 observation → competing hypotheses → evidence → falsification → controlled experiment 的可執行迴圈；排除人格、語氣與笑話。

## Source Metadata
- URLs: https://www.youtube.com/watch?v=WeHM2xpYQpw ; https://www.youtube.com/watch?v=D_S6y0Jm6dQ ; https://www.youtube.com/watch?v=O2VkP8dJ5FE
- Source type: 三支李宏毅官方課程影片、ffprobe 已驗證、official timed transcripts；一手來源；source weight: 2。
- Source coverage: 14 個 P0 candidate principles 的完整來源映射在 `knowledge/p0_candidates.json`；本筆只綜合，不增加新的課程主張。

## Key Findings
- 先讀取訓練與評估的可觀察事實，再決定 capacity、optimization、generalization、data、evaluation 或 loss 是否是合理假說。
- 下一個實驗應儘量是成本低、可區分、並控制其他主要條件的測試；結果要能改變後續判斷。
- 來源直接支持的課程規則與專案形成的實驗設計推論必須分開呈現。

## Contradictions
- 「先別加大模型」只適用於缺乏 capacity 證據時；若較大模型在最佳化健康、受控比較下同時改善 train/validation，應支持擴大容量。

## Inferences (clearly marked as inference, not fact)
- 推論：small/current/large ablation、記錄 validation 使用次數、逐 checkpoint metric component 對照，是把課程原則落到專案實驗的操作化方式。

## Gaps and Missing Information
- P0 corpus 仍有待 ASR 影片；ranking metric 與一般 loss-to-metric alignment 沒有直接課程原則。這些缺口必須保留在 Skill 與 coverage 報告，不能用綜合文字填補。
