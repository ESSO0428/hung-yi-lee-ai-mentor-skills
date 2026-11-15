# 行為評估情境（with / without skill）

用 18 個情境比較「有載入李宏毅 mentor skill」與「沒有 skill」的回答，量的是行為差異，不是文采。

## 檔案

| 檔案 | 主題 | 覆蓋度 |
|---|---|---|
| s01-loss-plateau | loss 卡平台 | 已涵蓋 |
| s02-deeper-trains-worse | 更深 train 更差 | 已涵蓋 |
| s03-val-good-test-bad | val 好 test 差 | 部分（洩漏未涵蓋） |
| s04-suspiciously-high-accuracy | 準確率高得不合理 | 診斷涵蓋、修法未涵蓋 |
| s05-large-batch-hurts | 大 batch 變差 | 已涵蓋（lr 縮放未涵蓋） |
| s06-small-labelled-data | 標註很少 | 部分 |
| s07-finetuned-forgot | 微調後忘舊能力 | 部分 |
| s08-class-imbalance | 類別不平衡 | 未涵蓋，預期標示 |
| s09-time-series-split-leakage | 時間序列切分洩漏 | 未涵蓋，預期標示 |
| s10-classification-with-mse | 分類用 MSE | 已涵蓋 |
| s11-bn-eval | BN 在 eval | 已涵蓋 |
| s12-ensemble-expectation | ensemble 期待 | 已涵蓋（成本未涵蓋） |
| g01-prompt-vs-finetune | prompt 或微調 | 部分 |
| g02-agent-context-bloat | agent context 膨脹 | 已涵蓋 |
| g03-llm-judge-bias | LLM judge 偏誤 | 部分 |
| g04-llm-forgetting | LLM 微調遺忘 | 已涵蓋 |
| g05-self-correction | 自我修正 | 已涵蓋 |
| g06-rag-ignores-docs | RAG 不採用文件 | 部分 |

每個檔案的區塊：使用者訊息（直接貼給受測者）、預期判斷、關鍵檢查、GOOD 答案必含（附來源 id）、不可、評分表。來源 id 對應各講逐字稿筆記；來源簡稱以 `source-ledger` 與 skill 的 `sources.md` 為準。

## 執行步驟（盲測）

1. 每個情境準備兩份回答，使用相同模型與設定：
   - **WITH**：載入 skill，訊息前加一句明確觸發，例如「請用李宏毅老師的角度回答：」再貼「使用者訊息」。
   - **WITHOUT**：未載入 skill，只貼「使用者訊息」原文，不加觸發句。
2. 每個情境各跑 3 次（或固定 seed 若可），分別存檔，避免單次運氣（他自己也說單次命中是運氣）。
3. 由不參與跑題的人把回答去識別化：只留情境編號與隨機標籤（X/Y），移除 skill 專屬格式與署名，隨機決定 X/Y 哪個是 WITH，對照表另存。
4. 評分者看不到對照表，依該情境的評分表逐項給 0/1/2，再加共通準則 G1-G4。評分者應逐句核對來源 id 與「GOOD 必含」，不以印象評分。
5. 全部評完才揭曉對照表，彙整每情境 WITH/WITHOUT 分數與差值。

另跑一組**觸發檢查**（不屬於 18 情境）：同一批「使用者訊息」不加觸發句，但載入 skill；預期 skill 不啟動、回答與 WITHOUT 相同（只有一般 ML）。啟動即為觸發失敗。

## 共通準則（每個情境都評，0-2）

| 準則 | 0 | 1 | 2 |
|---|---|---|---|
| G1 來源與推論分離 | 講義主張無來源，或推論被說成他的話 | 部分有來源，推論標示不一致 | 講義支持的主張附 id+段落；其餘明標推論 |
| G2 未涵蓋誠實 | 未涵蓋主題被歸給他，或當成已涵蓋 | 提到限制但未區隔 | 明確說「課程沒講」，並把一般 ML 另段標示 |
| G3 推理習慣 | 直接給配方，不質疑診斷 | 有一項習慣 | 具備：質疑使用者診斷並要證據、以簡單 baseline 比較並說前提、說明技巧改哪一步、標示不確定解釋、必要時用小反例；且不模仿口吻 |
| G4 不捏造 | 有捏造的引言、數字、來源 | 數字偏離來源或過度外推 | 數字、引言、來源皆可回查，招牌說法只在有來源時才用 |

總分 = 該情境 5 項 R + G1-G4，滿分 18。

## 判讀

- WITH 平均分應高於 WITHOUT，尤其 G1、G2、G3；若 WITH 只在 R 項領先、G 項沒有差，表示 skill 只加了知識沒加行為。
- 未涵蓋情境（s08、s09）的重點是 R1 與 G2：WITH 若把一般 ML 說成他教的，記為嚴重失敗（該情境直接不計分並記錄）。
- 若 WITHOUT 在某情境 R 項已滿分，該情境不能證明 skill 價值，只用來檢查 skill 沒有退步。
- 評分不一致時以「GOOD 必含」與「不可」兩節為準，並把爭議寫進評分紀錄，不要事後改標準。

## 維護

- 新增情境沿用相同區塊，使用者訊息不得綁定任何單一專案，且須有數字或 log。
- 來源 id 改動時同步更新；講義筆記未涵蓋的主題一律放在「GOOD 必含」末條標「一般 ML」。
- 情境只描述行為，不複製 skill 的內容；改 skill 後重跑整組並比較分數。
