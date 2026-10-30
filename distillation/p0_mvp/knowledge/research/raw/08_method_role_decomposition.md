# P0 蒸餾：方法在研究管線中的作用層

## Dimension Coverage
- 研究決策：面對「某技術會取代另一技術」或沒有 failure-mode 的新方法提案時，先辨識它改變候選函式集合、評量標準、或尋找最佳函式的程序中的哪一層。

## Source Metadata
- URL: https://www.youtube.com/watch?v=phQK8xZpgoU
- Supporting source URL: https://www.youtube.com/watch?v=XLyPFnephpY
- Source type: 李宏毅官方課程影片、ffprobe 已驗證、本機 ASR timed transcript；一手來源；source weight: 2。ASR 的術語需要畫面複核。
- Canonical source chunks: `phQK8xZpgoU:458-491`（1260.00–1349.98 秒）與 `phQK8xZpgoU:492-525`（1350.00–1424.98 秒）；另有 `XLyPFnephpY:360-363`（900.00–912.74 秒）的跨影片總結。
- Visual verification: `data/processing/frame_review/phQK8xZpgoU/S0015.jpg`、`S0015b.jpg`、`S0016.jpg`，以及 `data/processing/frame_index/XLyPFnephpY/0900s.jpg`。兩支影片皆明列：Deep Learning/CNN/Transformer/Decision Tree 位於候選函式集合；Supervised/Semi-supervised/RL 位於評量標準；Gradient Descent/Adam/AdamW/Genetic Algorithm 位於找出最佳函式。

## Key Findings
- 課程以「找出函式的三步驟」切分為設定範圍、設定評量函式好壞的標準、找出最佳函式。
- 投影片把 Deep Learning 與 RL 框在不同層，說明「RL 要取代 Deep Learning」不能被當作未經分層的替代關係。
- 另一支影片的總結投影片重複同一框架，提供跨影片的畫面佐證。
- 對研究提案而言，先定位介入層，才能明確列出它可能改變的量與仍未處理的 bottleneck。

## Contradictions
- 單一方法可能跨多層作用；三層是用來釐清假說的框架，不是對所有 ML 技術的互斥分類。

## Inferences (clearly marked as inference, not fact)
- 推論：若一項新模組沒有能定位的 failure mode 或作用層，先要求可反駁的機制假說與最小對照實驗，再投入實作。

## Gaps and Missing Information
- 本來源不提供每個現代架構、RL 演算法或目標函式的完整分類，也不保證某層的改動一定改善任務 metric。
