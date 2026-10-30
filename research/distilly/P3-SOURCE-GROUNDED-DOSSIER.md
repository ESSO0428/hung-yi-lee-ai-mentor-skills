# P3 source-grounded dossier：遷移、保留、自我改進與自我修正

> 狀態：Distilly research-first draft；所有結論均保留 task-level 與 evaluation boundary。

## 輸入與 provenance

本 dossier 僅使用 `distillation/p3_self_supervised/knowledge/research/raw/` 的四份 official-transcript notes。Distilly merged summary 為 4 files、8 unique URLs、40 bullet findings；每份 raw note 都保留 source chunks、時間範圍與顯式 `Inferences`。

| 面向 | 來源影片與時間範圍 |
| --- | --- |
| self-supervised transfer | [MpsVE60iRLM](https://www.youtube.com/watch?v=MpsVE60iRLM) `30–231s`；[WY_E0Sd4K80](https://www.youtube.com/watch?v=WY_E0Sd4K80) `380–477s` |
| continual retention | [rWF9sg5w6Zk](https://www.youtube.com/watch?v=rWF9sg5w6Zk) `354–758s`；[Z6b5-77EfGk](https://www.youtube.com/watch?v=Z6b5-77EfGk) `0–16s, 58–104s, 235–310s` |
| agent self-improvement | [cQLKVzbwN7I](https://www.youtube.com/watch?v=cQLKVzbwN7I) `36–75s, 252–298s, 989–1084s`；[2rcJdFuNbZQ](https://www.youtube.com/watch?v=2rcJdFuNbZQ) `940–983s, 1206–1248s, 1859–1905s, 2225–2260s` |
| self-correction evaluation | [m3i2mk5hs8U](https://www.youtube.com/watch?v=m3i2mk5hs8U) `1408–1569s`；[s06mSAGN4gM](https://www.youtube.com/watch?v=s06mSAGN4gM) `400–487s, 877–982s` |

## 來源直接支持的觀察

- 自監督預訓練、下游任務評估與跨任務驗證屬不同層；未標註 upstream data 的使用不等於已證實對任一 downstream task 通用遷移。
- 持續學習需同時觀察新任務學習與舊任務保留；replay 或 parameter constraints 是有成本的緩解選項，應與簡單 sequential baseline 比較。
- 自我改進須在固定 harness／benchmark 下與 held-out evidence 分開觀察，並對 agent 工具輸出與持久狀態做明確查驗。
- 自我修正需要修正前後比較與外部或獨立評估；proxy reward、critic 或 confidence 不能直接等同真實目標效用。

## 不可壓平的條件與張力

| 張力 | evidence 中保留的界線 |
| --- | --- |
| task-agnostic pretraining vs. downstream value | 來源不給普遍遷移保證、最佳 layer/head、資料量／算力門檻、因果機制或最佳 pretext task。 |
| plasticity vs. retention | 沒有已證明的普遍最佳遺忘緩解方法或通用門檻；算力、資料與舊／新任務表現存在取捨。 |
| optimization-set progress vs. genuine improvement | optimization set 的提高可能 overfit；來源沒有保證 benchmark 充分、免於 prompt injection 或其他副作用。 |
| proxy reward vs. target objective | proxy／critic 分數不是實際效用的直接替代，不能單靠自我回饋聲稱能力改善。 |

## 推論層：待驗的專案實作方向

- 把 SSL 模型當作候選表徵，必須用 task-level downstream evaluation 來檢驗。
- 同時報告新任務表現、舊任務保留與 backward transfer，並對遺忘緩解方法維持簡單 baseline。
- 維持 fixed harness、held-out evidence 與 state-verification record；將「Think again」之類 intervention 當成待測操作，而非能力改善證明。
- 固定 metric、比較修正前後，並引入 independent check；這些是 raw note 的 advisor inference，不是來源已給出的通用 recipe。

## 誠實邊界與條件式視覺補證

- 本輪只讀 raw notes／summary，沒有直接重聽或看完整影片；本檔的來源描述仍以列出的 transcript chunks 為根據。
- 若要引用 SSL pretext／SUPERB 的圖示、retention/backward-transfer 曲線、proxy reward 與 true objective 的示意，或 agent 實際修改／驗證狀態的畫面細節，才對上表時間範圍選擇性補影格。
- 四個 tracks、40 個 findings 並不等於完整或最終 mentor knowledge；缺少的 dimension 仍要保留為 gap。

