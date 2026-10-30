# Cross-dossier review（2026-10-29）

## 範圍

本 review 僅比對 P0–P3 source-grounded dossiers 的直接觀察、推論標示與缺口。它不新增外部來源、不重跑 ASR／AGY，也不把 candidate material 寫入正式 mentor knowledge。

## 結論

**沒有發現需要以「二選一」消除的直接來源矛盾。** 主要差異都能保留為條件化研究張力，而不是被壓平為通用規則。

| 交叉張力 | 檢閱結果 | 可安全保留的邊界 |
| --- | --- | --- |
| capacity／complexity vs. optimization、資料或評估 | P0 的 evidence 已明示這不是單向關係；P1 架構選擇沒有反駁該原則。 | 先確認 failure mode，才決定是否比較容量、架構或訓練程序。 |
| local inductive bias vs. global contextualization | P1 兩種設計面向互補；P0 的「作用層」框架有助於定位改動。 | 任務結構、dependency span、所需 detail 和成本仍需測量。 |
| proxy／optimization improvement vs. true value | P0 的泛化 proxy、P2 的評估設計、P3 的 self-correction／held-out check 方向一致。 | proxy、public metric、critic 或自評不等於 deployment／target outcome。 |
| 自動化研究流程 vs. 人工／獨立判斷 | P2 指出 agent／AI review 可錯；P3 要求 harness、state verification 與 independent check。 | 自動化可產生候選與測試，不可取代外部驗證。 |
| 新任務改善 vs. 舊能力保留 | P3 明確保留 plasticity／retention trade-off，沒有與 P0–P2 衝突。 | 報告新任務結果時，同時檢查 retention、backward transfer 與副作用。 |

## 尚不能升格的內容

- **P0**：可繼續作為已有 formal provenance 的 core evidence；本 review 不新增新的 formal rule。
- **P1–P3**：仍為 candidate-only。它們的 inference 可用來設計檢驗，但不可被表述成李宏毅課程已證實的完整 recipe。
- **P2 AGY supplemental**：維持 non-canonical，不可與官方 transcript evidence 混合計數。

## 只有在具體 claim 出現時才要補的視覺證據

- P1：Transformer／CNN diagram 的尺寸、pooling、feature-map 或 sequence-flow 細節。
- P2：diffusion／GAN 的公式、distribution／mode-collapse 圖示、或示範畫面中的操作細節。
- P3：SSL／SUPERB、retention／backward-transfer、proxy-vs-true-objective 或 state-verification 的圖表／示範。

概念性文字主張目前不需要例行全片抽幀。

## 非阻塞但必須保留的限制

1. upstream generic Persona `quality_check.py` 與 content-only profile layout 不相容；詳見 [PROFILE-AUDIT.md](PROFILE-AUDIT.md)。
2. 兩部線性代數來源 gap、非影片官方頁面的 bounded coverage、以及 FFP 無可重跑輸入仍是整體專案限制；都不阻塞這次 evidence-first research profile。
3. profile 尚未吸收未來可能有價值的官方作業／程式碼／投影片；它們在需要時可作另一個有 provenance 的 evidence increment。

## 下一個安全邊界

在沒有新證據或使用者指定 scope 前，保持 `PROFILE-DRAFT.md` 為初稿、保持 P1–P3 candidate-only，並讓正式 mentor Skill 維持現有已驗收知識。若要往下，應只選擇一個明確工作包：

- 將經使用者確認的 source-profile 區段正規化為正式 mentor 知識；或
- 對一個具體 claim 做 visual／official-course-material follow-up；或
- 以真實 FFP／其他專案 artifacts 做 forward evaluation。
