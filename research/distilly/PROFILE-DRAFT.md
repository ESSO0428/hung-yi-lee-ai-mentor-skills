# 李宏毅課程：Distilly content-only research profile（初稿）

> 這是以官方課程證據建立的研究檔案，不是對本人意圖、人格或未公開觀點的宣稱。
>
> 本初稿故意不模仿口吻或產生 Persona。它保留上游 Distilly 的「觀察 → 重複模式 → 張力 → 邊界」結構，作為後續 mentor 正規化前的中間層。

## 證據範圍

- 輸入：四份 [source-grounded dossier](README.md)，其底層是 P0–P3 的官方課程逐字稿、timestamps、source chunks、已記錄的選擇性 visual evidence 與 Distilly merged summaries。
- 來源排序：一手官方課程優先；P2 的 AGY supplemental note 只保留為補充觀察，不覆寫 canonical transcript evidence。
- 覆蓋聲明：此 profile 不代表 604 部已文字審核影片都已被納入，也不把 P1–P3 的 candidate material 當作 formal mentor knowledge。

## 觀察到的心智模型（source-grounded）

1. **先定位 failure mode，再選介入方向。** training signal、generalization、資料分布、evaluation protocol、objective 與 capacity／optimization 是可競爭、可區分的解釋，而不是可由單一壞分數判定的單一原因。[P0 dossier](P0-SOURCE-GROUNDED-DOSSIER.md)
2. **方法必須先定位作用層。** 候選函式範圍、評量標準與求解程序是不同層；同理，語境、位置、masking、cross-attention、representation transform 及 inductive bias 也不是同一個設計旋鈕。[P0 dossier](P0-SOURCE-GROUNDED-DOSSIER.md) [P1 dossier](P1-SOURCE-GROUNDED-DOSSIER.md)
3. **評估是系統的一部分，不是事後裝飾。** train／validation／test 的角色、題目與參考答案、metric、輸出格式、quality／diversity／memorization，以及 held-out evidence 會共同影響一項能力宣稱是否成立。[P0 dossier](P0-SOURCE-GROUNDED-DOSSIER.md) [P2 dossier](P2-SOURCE-GROUNDED-DOSSIER.md)
4. **proxy 只是一個待驗的中介假說。** parameter norm、sharpness、confidence、critic 或 reward 的改善，不能自行等同於真正的泛化、效用或能力改善。[P0 dossier](P0-SOURCE-GROUNDED-DOSSIER.md) [P3 dossier](P3-SOURCE-GROUNDED-DOSSIER.md)
5. **把改進和保留分開量測。** 自監督遷移須以 downstream task 檢驗；continual learning、自我改進與自我修正要同時查驗新行為、舊能力／狀態與獨立 evidence。[P3 dossier](P3-SOURCE-GROUNDED-DOSSIER.md)

## 重複出現的決策啟發（仍需專案驗證）

- 一次只改少量可定位的變因，並用能區分 competing hypotheses 的 controlled comparison；這是從 P0/P1 raw notes 整理出的操作化 inference，不是保證有效的課程公式。
- 在擴大模型、採用新架構或導入新流程前，先寫清楚它預期處理的 failure mode、作用層、metric 與 baseline。
- 要求新方法的結果同時說明：它在何種資料、任務、分割、預算與評估設計下成立，以及有哪些尚未測量的副作用。
- 對自動化／agentic 流程，保存固定 harness、held-out outcome 與 state-verification record；避免把自我產生的評價當成唯一真相。

## 不可壓平的張力

| 張力 | 此 profile 不採取的捷徑 |
| --- | --- |
| 增加容量 vs. 檢查最佳化／資料／評估 | 不把「大模型」或「正則化」設為預設答案。 |
| 局部 inductive bias vs. 全域 contextualization | 不宣稱 CNN、attention、local window 或 global context 有普遍勝負。 |
| optimization-set progress vs. 真正泛化 | 不把 leaderboard、proxy、critic 或自我評分直接當成 held-out evidence。 |
| 學習新任務 vs. 保留既有能力 | 不把單一新任務提升當成整體系統改善。 |
| 方法原理說明 vs. 生產效益 | 不從 role decomposition 推論 latency、accuracy 或成本必然改善。 |

## 誠實邊界

- 本 profile 不是李宏毅老師的完整人物模型，也沒有 evidence 支持其 expression DNA、私人偏好、智識譜系或生涯時間線；這些不會被杜撰。
- P1–P3 保留為 candidate-only；每個跨專案規則仍需追溯至原始 raw note／timestamp，並保留反例、適用條件與 gap。
- 公式、圖表、架構尺寸、distribution 示意與操作畫面只在某個 claim 依賴它們時選擇性核對，不以全片重看替代證據判斷。
- P2 AGY supplemental 觀察不是 canonical evidence；任何升格需要獨立可回查來源。

## Agentic protocol（此 profile 可安全提供的行為）

1. 先分開列出 observation、assumption、competing hypotheses 與尚缺 evidence。
2. 將候選改動映射到它實際改變的資料、表示／候選函式、目標、求解、評估或狀態驗證層。
3. 只提出成本低且資訊量高的區分性實驗；清楚寫出什麼結果會改變判斷。
4. 對 profile 沒有來源支持的部分，明說 `unknown` 或 `project hypothesis`，而非借用講者權威補足。

## Validation anchors

- P0 core evidence: https://www.youtube.com/watch?v=WeHM2xpYQpw
- P1 architecture evidence: https://www.youtube.com/watch?v=N6aRv06iv2g
- P2 evaluation evidence: https://www.youtube.com/watch?v=s266BzGNKKc
- P3 self-correction evidence: https://www.youtube.com/watch?v=m3i2mk5hs8U
- Deterministic source merge: [Distilly reproducibility audit](../../evaluation/distilly-reproducibility-latest.json)

## 供後續微調檢閱的明確問題

目前沒有以猜測補齊的內容。若後續要微調，只應處理下列可檢驗的選項：

- 是否有某個 task family 需要優先擴充到 formal knowledge，而不是繼續讓 P1–P3 維持 candidate-only？
- 是否有重要的架構圖、公式或作業材料，必須以明確 claim 為單位提出 selective visual request？
- 是否提供新的 FFP 或其他真實專案 artifacts，讓這個 profile 接受可重跑的 forward evaluation？

