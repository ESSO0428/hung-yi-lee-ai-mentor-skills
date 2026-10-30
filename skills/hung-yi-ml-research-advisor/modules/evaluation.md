# 評估設計

domain: evaluation

來源真相：`knowledge/normalized_principles.json` 的 `MLRA-P0-008`、`MLRA-P0-009`、`MLRA-P0-010`。

## MLRA-P0-008 — 不要反覆用公開測試選模

- 規則：公開測試／榜單反覆選模會對公開分割形成選擇偏差；模型選擇留給 validation，保留獨立 final evaluation。
- 證據：`DIRECT_COURSE_EVIDENCE`；`WeHM2xpYQpw:842-885`，1935.26–2024.87 秒；`WeHM2xpYQpw:1096-1133`，2468.53–2556.87 秒，official。

## MLRA-P0-009 — 分清 train／validation／test 角色

- 規則：train 用於參數學習、validation 比較候選模型，final test 不代替 validation 參與選模。
- 證據：`DIRECT_COURSE_EVIDENCE`；`WeHM2xpYQpw:1096-1133`，2468.53–2556.87 秒，official。

## MLRA-P0-010 — 不穩定 split 才考慮 cross-validation

- 規則：資料量與 split 變異使單一分數不穩時，考慮 N-fold CV，重訓後仍保留獨立 test；fold 必須符合資料生成方式。
- 證據：`DIRECT_COURSE_EVIDENCE`；`WeHM2xpYQpw:1180-1222`，2653.73–2743.10 秒；`WeHM2xpYQpw:1223-1255`，2743.34–2831.59 秒，official。
- URL：https://www.youtube.com/watch?v=WeHM2xpYQpw

完整 claim、decision_rule、limitations 與 provenance 以 normalized JSON 為準。

