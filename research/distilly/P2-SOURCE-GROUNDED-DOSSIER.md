# P2 source-grounded dossier：方法、評估與 AI 輔助研究

> 狀態：Distilly research-first draft；canonical transcript evidence 與 AGY supplemental observations 分開保存，所有候選維持 candidate-only。

## 輸入與 provenance

本 dossier 以 `distillation/p2_methods/knowledge/research/raw/` 的八份 notes 為唯一輸入。Distilly merged summary 的統計為 8 files、13 unique URLs、75 bullet findings；完整 timestamps、evidence packet IDs 與 source type 保留在各 raw note。

| 面向 | 代表性一手來源／chunk |
| --- | --- |
| 研究方法與 LLM 評估 | [UsaZhQ9bY2k](https://www.youtube.com/watch?v=UsaZhQ9bY2k) `0–18s, 37–66s`；[s266BzGNKKc](https://www.youtube.com/watch?v=s266BzGNKKc) `41–157s`；[dWQVY_h0YXU](https://www.youtube.com/watch?v=dWQVY_h0YXU) `0–126s` |
| Diffusion 與 speculative decoding | [azBugJzmz-o](https://www.youtube.com/watch?v=azBugJzmz-o) `89.33–529.10s`；[MAbGgsWKrg8](https://www.youtube.com/watch?v=MAbGgsWKrg8) `88.60–531.38s` |
| GAN 評估 | [MP0BnVH2yOo](https://www.youtube.com/watch?v=MP0BnVH2yOo) `1154.80–1597.36s, 2041.93–2131.30s`；[IB_ADssBomk](https://www.youtube.com/watch?v=IB_ADssBomk) `663.56–882.06s` |
| AI 輔助研究與 prompting／fine-tuning | [VqB8zMujdjM](https://www.youtube.com/watch?v=VqB8zMujdjM) `177.51–266.799s, 803.502–892.324s`；[M2Yg1kwPpts](https://www.youtube.com/watch?v=M2Yg1kwPpts) `1339.90–1429.48s, 3750.119–3839.179s`；[F58vJcGgjt0](https://www.youtube.com/watch?v=F58vJcGgjt0) `0–85.60s, 1146.075–1289.70s` |

## 來源直接支持的觀察

- 單次 demo 或單一輸出不足以證實系統能力；研究問題、題目變形、reference answer、metric 與輸出格式都會改變測量結果。
- 生成模型評估不能只看樣本品質；distribution coverage／diversity 與記憶訓練資料是不同面向。
- 方法內各角色與階段需分清：diffusion 包含 noise、step、predicted noise 與反向生成；speculative decoding 區分 draft proposal model 與 target model 的驗證角色。
- AI agent 或自動研究流程仍會出錯；提案、review 和流程輸出需要實驗／獨立查驗，而不是因為由 AI 產生就被視為有效。

## 來源不支持的捷徑

- 沒有普遍最優的 prompting-vs-fine-tuning、diffusion sampler、GAN diversity 門檻或可完全取消人工審查的條件。
- speculative decoding 的效益依 proposal acceptance 與額外 overhead 而定；被拒絕的 proposal 是回退情況，不能由架構角色直接推論端到端 latency 必然改善。
- raw `08_agy_supplemental_2026-09-22.md` 的 continual-learning、domain-adaptation、autoencoder 觀察屬 AGY supplemental／單一來源 inference，不能升格為 canonical transcript 通則。

## 推論層：後續研究假說，而非講者的完整 protocol

- 評估集應包含可以檢驗是否超越熟悉題型的變形或新題目，並顯式記錄 metric 與格式假設。
- 生成模型的報告可把品質、多樣性／覆蓋與 memorization 分開評估。
- speculative decoding 應另量測 proposal acceptance 與端到端 latency；新研究流程仍要預先指定驗證與人工判斷點。

## 誠實邊界與條件式視覺補證

- 若要精確引用 diffusion 去噪流程／條件輸入、GAN 的 distribution 或 mode-collapse 圖示，才針對已列時間抽取影格；目前概念性描述以逐字稿為限。
- 本 dossier 不把任何 raw note 覆蓋範圍當成完整方法課，也不把候選實驗設計寫成已驗證 recipe。

