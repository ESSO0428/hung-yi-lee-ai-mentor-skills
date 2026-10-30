# Formal P0 modules

這些模組是 `knowledge/normalized_principles.json` 的可路由閱讀層，不是第二份事實來源。研究提案觸及某個 domain 時，先讀對應模組，再依原則 ID 回到 normalized JSON、source chunk 與影片 provenance。模組只包含已通過 P0 normalization 的規則；P1/P2 候選仍留在各自 candidate 檔案，不得從這裡升格。

## Routing

| 觸發 domain | 模組 | 原則 |
| --- | --- | --- |
| 訓練損失、capacity／optimization 診斷 | `modules/training-diagnosis.md` | MLRA-P0-001, MLRA-P0-002 |
| 模型彈性、underfitting、regularization | `modules/model-capacity.md` | MLRA-P0-003, MLRA-P0-007 |
| optimizer、深度模型訓練不穩 | `modules/optimization.md` | MLRA-P0-004 |
| train/test gap、泛化 proxy | `modules/generalization.md` | MLRA-P0-005, MLRA-P0-014 |
| augmentation、distribution、資料量 | `modules/data-diagnosis.md` | MLRA-P0-006, MLRA-P0-011 |
| split、public leaderboard、cross-validation | `modules/evaluation.md` | MLRA-P0-008, MLRA-P0-009, MLRA-P0-010 |
| loss、activation、gradient mismatch | `modules/loss-design.md` | MLRA-P0-012 |
| ablation、方法作用層、實驗選擇 | `modules/experiment-design.md` | MLRA-P0-013, MLRA-P0-015 |

## Module contract

1. 先把目前量測值與解釋分開；模組規則只在 `applicable_when` 成立時使用。
2. 讀取原則的 `evidence_class` 與 `disclosure`；`PROJECT_INFERENCE` 不得改寫成教師原話。
3. 每個建議仍要列出 competing hypotheses、會削弱它的證據與最小鑑別實驗。
4. 引用時保留 `principle ID → source_chunk → timestamp → video URL → transcript_type`；模組摘要不能取代原始來源。

