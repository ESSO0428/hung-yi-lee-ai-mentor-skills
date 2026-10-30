# P1 source-grounded dossier：表徵與架構設計

> 狀態：Distilly research-first draft；維持 candidate-only，不是最終 mentor 規則。

## 輸入與 provenance

本 dossier 僅整合 `distillation/p1_representation/knowledge/research/raw/` 的四份 official-transcript research notes；完整 raw evidence、packet ID、chunk 與缺口仍以該目錄為準。

| 面向 | 來源影片與時間範圍 |
| --- | --- |
| 序列語境與位置 | [hYdO9CscNes](https://www.youtube.com/watch?v=hYdO9CscNes) `713.880–1064.590s`；[gmsMY5kc-zw](https://www.youtube.com/watch?v=gmsMY5kc-zw) `31.310–108.080s`；[Ll-wk8x3G_g](https://www.youtube.com/watch?v=Ll-wk8x3G_g) `89.722–355.722s` |
| Transformer Decoder | [N6aRv06iv2g](https://www.youtube.com/watch?v=N6aRv06iv2g) `530.890–797.150s`、`1418.940–1774.630s` |
| Transformer Encoder | [n9TlOhRjYoc](https://www.youtube.com/watch?v=n9TlOhRjYoc) `1334.560–1601.000s`、`1779.550–1868.460s` |
| CNN inductive bias | [OP5HcXJg2Aw](https://www.youtube.com/watch?v=OP5HcXJg2Aw) `620.080–797.380s`、`1326.930–1773.130s`、`2393.700–2658.240s`、`3188.910–3338.820s`；[gjsdVi90yQo](https://www.youtube.com/watch?v=gjsdVi90yQo) `179.840–269.579s`、`4776.199–4863.960s` |

## 來源直接支持的觀察

- 語境範圍與位置／順序資訊是不同的設計面向：模型可彙整序列位置的資訊，仍可能需要明確位置訊號；局部 window 在某些任務仍是合理 baseline，而較長依賴必須由任務證據支持。
- Encoder 的 contextual transformation、Decoder 的 causal masking、cross-attention 的跨序列資訊路由，以及 token-level transformation 是可分辨的架構表面；改其中一項不等於取代其他項。
- CNN 的 local receptive field、parameter sharing、pooling 是對重複局部結構的 inductive-bias 選擇，同時涉及彈性與細節遺失的取捨；它們不保證跨模態、尺度或旋轉的自動不變性。

## 不可壓平的條件與張力

| 張力 | 來源可支持的界線 |
| --- | --- |
| 局部 vs. 全序列語境 | 有用 dependency span 取決於任務；來源沒有排序兩者效能、成本或長上下文失敗模式。 |
| CNN vs. 其他架構 | CNN 對局部重複結構的假設可能合適，也可能限制所需細節；來源沒有給出 CNN、ViT、Attention 的通用勝負。 |
| attention aggregation vs. order information | 基本 attention calculation 不內含順序資訊；這不指定某種 positional method 必然最優。 |

## 推論層：不得偽裝為課程定論

- 用固定資料、metric、sequence length 與其他模組的 local ablation，比較 local-context／sequence-wide context、masking、cross-attention 或 transformation 的改動。
- 在加入或移除 convolution、shared weights、pooling 前，檢查局部重複結構、所需位置細節、變換型態與 receptive-field geometry。

這些都來自 raw notes 的 `Inferences`，是待驗的專案假說，不是「某架構普遍較好」的來源結論。

## 誠實邊界與條件式視覺補證

- 此 family 尚未以這些片段建立比較效能、optimization/data effect、長 context failure、普遍 invariance 或最佳 positional encoding 的證據。
- 本批 raw notes 沒有做投影片／動畫查核。若日後引用 diagram dimension、公式、CNN pooling／feature-map 細節或 sequence-flow 圖，才針對上表時間點請求影格；文字可支持的概念不需要例行全片回看。

