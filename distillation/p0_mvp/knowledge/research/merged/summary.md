# Research Summary

- Files scanned: 8
- Unique URLs: 6
- Total source mentions: 11
- Primary-source markers: 0
- Source metadata blocks: 8
- Contradiction bullets: 8
- Inference bullets: 8
- Pattern bullets: 0
- Gap bullets: 8
- Total note chars: 7802
- Total bullet findings: 26
- Potential long quote lines: 0
- Track coverage count: 8
- Track coverage: 01, 02, 03, 04, 05, 06, 07, 08
- Missing tracks: none

## Source Weight Distribution

- Tier 1-3 (high-quality primary): 8
- Tier 4-5 (medium / short-form firsthand): 0
- Tier 6-7 (external / secondhand): 0
- Total weighted sources: 8
- Weighted-source primary ratio: 100%

## File Inventory

| File | Source Mentions | Primary Marker |
|------|-----------------|----------------|
| 01_training_capacity_optimization.md | 1 | yes |
| 02_generalization_and_data.md | 1 | yes |
| 03_evaluation_selection.md | 1 | yes |
| 04_loss_and_objective.md | 1 | yes |
| 05_cross_course_capacity.md | 1 | yes |
| 06_synthesis_boundaries.md | 3 | yes |
| 07_generalization_indicator.md | 1 | yes |
| 08_method_role_decomposition.md | 2 | yes |

## Key Findings

- 榜單或測試結果不佳時，先檢查 training loss，分辨模型是否連訓練資料也沒學好。
- 訓練 loss 高至少有兩個可競爭解釋：模型函數集合沒有低 loss 解，或最佳化沒有找到可達低 loss 的解。
- 記住訓練樣本與對未見樣本泛化是不同現象；低 training loss 與高 testing loss 可以同時存在。
- 限制模型彈性可降低部分過擬合風險，但限制過強也可能造成欠擬合；容量／正則化調整應同看訓練與驗證行為。
- 反覆依公開測試或榜單結果挑模型，會讓選擇程序對那個分割適配，不能把最佳公開結果當作無偏的部署證據。
- 訓練集用於擬合參數，驗證集用於比較候選模型；最終測試不能代替驗證集參與選模。
- 在課程展示的 softmax 分類案例中，MSE 的高 loss 區域可能給出很小梯度，cross-entropy 則提供不同的有效斜率；loss 選擇會改變最佳化地形。
- 因此分類訓練卡住時，輸出啟用、loss 與梯度行為都屬可檢查的假說。
- 誤差來源的診斷決定改進方向；複雜模型不必然在 testing data 有更低 error。
- 可表達的函數集合不含低 loss 解時，僅改善求解器不能補足表示限制。
