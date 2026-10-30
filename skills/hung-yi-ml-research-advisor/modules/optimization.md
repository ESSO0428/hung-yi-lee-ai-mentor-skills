# 最佳化

domain: optimization

來源真相：`knowledge/normalized_principles.json` 的 `MLRA-P0-004`。

## MLRA-P0-004 — 更有彈性的模型仍可能是 optimization 問題

- 規則：若較深模型在訓練集上的損失反而高於較淺基線，且函數集合包含關係是適用前提，問題更可能是 optimization 而非 overfitting。
- 操作：先比較簡單／淺層基線的訓練損失，再查 optimizer、初始化與訓練流程。
- 證據：`DIRECT_COURSE_EVIDENCE`；`WeHM2xpYQpw:335-375`，783.47–872.83 秒，official。
- URL：https://www.youtube.com/watch?v=WeHM2xpYQpw

完整 claim、decision_rule、limitations 與 provenance 以 normalized JSON 為準。

