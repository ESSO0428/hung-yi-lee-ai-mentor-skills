# P0 source-grounded dossier：核心 ML 研究判斷

> 狀態：Distilly research-first seed；不是最終 Skill 規則，也不是人格檔案。
>
> 本檔只重述已存 raw research notes 中由一手官方課程支持的內容，並保留其衝突、條件與缺口。沒有以使用者專案或既有 advisor schema 重新解釋原始材料。

## 輸入與 provenance

| Raw note | 一手來源與定位 |
| --- | --- |
| 訓練診斷、容量與最佳化 | [官方課程影片](https://www.youtube.com/watch?v=WeHM2xpYQpw)，`WeHM2xpYQpw:86-210`、`335-375` |
| 泛化、資料與容量取捨 | [同一官方課程影片](https://www.youtube.com/watch?v=WeHM2xpYQpw)，`454-493`、`571-647`、`730-765`、`1287-1325` |
| 評估、選模與驗證資料 | [同一官方課程影片](https://www.youtube.com/watch?v=WeHM2xpYQpw)，`842-885`、`1096-1255` |
| 損失設計與最佳化訊號 | [官方課程影片](https://www.youtube.com/watch?v=O2VkP8dJ5FE)，`437-474` |
| 跨課程容量與誤差來源 | [官方課程影片](https://www.youtube.com/watch?v=D_S6y0Jm6dQ)，`479-527`、`609-630` |
| 泛化指標與訓練目標 | [官方課程影片](https://www.youtube.com/watch?v=pivB5jEBOQw)，`30-88` |
| 研究決策綜合與證據邊界 | 上列三支影片的來源映射；只整合既有 P0 candidate provenance |
| 方法在研究管線中的作用層 | [官方課程影片](https://www.youtube.com/watch?v=phQK8xZpgoU)，`458-525`；[跨影片佐證](https://www.youtube.com/watch?v=XLyPFnephpY)，`360-363`；已記錄投影片影格補證 |

每筆來源都是已驗證的官方課程影片；完整 raw note、時間範圍、逐字稿型別與視覺補證位置保留於 `distillation/p0_mvp/knowledge/research/raw/`。上游 Distilly merger 的可重現摘要位於 `distillation/p0_mvp/knowledge/research/merged/summary.md`。

## 來源直接支持的觀察

### 訓練訊號先於複雜度判斷

- 測試或榜單結果差，本身不足以判定模型容量不足；需先檢查模型是否連訓練資料都沒有學好。
- 訓練 loss 高至少容許兩個不同解釋：可表達的函式集合沒有低 loss 解，或最佳化尚未找到可達低 loss 的解。
- 課程中的深淺殘差網路例子以較深模型具有較高訓練 loss 指向最佳化問題；它不直接等同於過擬合判定。

### 泛化、資料與容量不能只看單一分數

- 低 training loss 與高 testing loss 可以同時發生；記住訓練資料與泛化到未見資料是不同現象。
- 限制模型彈性可降低某些過擬合風險，限制過強也可能造成欠擬合；容量與正則化需要同看訓練及驗證行為。
- 資料擴增必須保留任務的 label 語意；如果 train/test 分布不匹配，只增加原 train 分布資料未必改善目標表現。

### 評估資料的角色與選擇偏差

- 訓練集用於擬合參數，驗證集用於比較候選模型；最終測試不應代替驗證集參與選模。
- 反覆根據公開測試或榜單結果選模型，會讓選擇程序適配該分割；最佳公開結果不能直接當成無偏的部署證據。
- 單次切分不穩定時，課程提出交叉驗證以比較候選模型，再以全部訓練資料重訓選定模型。

### 目標函式與最佳化訊號

- 在課程展示的 softmax 分類例子中，MSE 與 cross-entropy 的梯度性質不同；loss 選擇會改變最佳化地形。
- 因此，分類訓練卡住時，輸出啟用、loss 與梯度行為都是待檢查的假說；例子本身不支持「任一分類任務都不可使用 MSE」或「換 loss 必然改善」。
- 若某指標已有支持其與泛化相關的證據，課程以 parameter norm、sharpness、sensitivity 為例，說明可考慮把此類項目納入 objective；仍不保證任一 proxy 在所有任務都有效。

### 方法的作用層

- 課程把找出函式拆為：設定候選範圍、設定評量標準、找出最佳函式的程序。
- 在此框架中，Deep Learning/CNN/Transformer/Decision Tree、supervised/semi-supervised/RL、以及 Gradient Descent/Adam/AdamW/Genetic Algorithm 位於不同作用層；所以「一種方法取代另一種」需先說明所指層級。
- 單一方法可以跨多層作用；三層框架是釐清假說的工具，不是互斥分類表。

## 跨來源反覆出現的研究張力

| 張力 | evidence 中保留的條件 |
| --- | --- |
| 增加容量 vs. 先檢查最佳化 | 缺乏 capacity 證據時不能把擴大模型當預設；若較大模型在健康最佳化、受控比較下同時改善 train/validation，容量假說得到支持。 |
| 降低複雜度 vs. 增加複雜度 | 兩者皆可能合理，取決於訓練／驗證行為、表示限制與資料條件；P0 不支持單向 complexity ideology。 |
| 加入正則化項 vs. 改善泛化 | 正則化項必須建立在 proxy 與目標泛化間有證據關聯的前提，不能僅因名稱或慣例採用。 |
| 新方法宣稱 vs. 可檢驗機制 | 新方法可以是有希望的假說，但在未定位其作用層與 failure mode 前，尚不是來源支持的結論。 |

## 推論層：與來源分開保存

下列是 raw notes 已明確標成 inference 的專案操作化方向，非講者逐字規則：

- 以 small/current/large 的受控容量比較協助區分 capacity 與 optimization，並以跨 seed paired comparison 降低偶然變異。
- 在動用大量新資料前，使用 learning curve、來源分布與標註檢查區分資料量、distribution shift 與 label 問題。
- 紀錄每個結果是否參與選模，以檢查選擇偏差。
- 固定模型和 evaluator 後再比較 loss／輸出設定，避免把多項同時變更誤歸因。
- 在固定訓練條件下檢驗 proxy 與 validation/deployment metric 的關聯，再決定是否把 proxy 納入 objective。

## 誠實邊界與尚未涵蓋的維度

- P0 沒有提供所有現代架構、RL 演算法、ranking／Top-k metric 或部署指標的完整規則。
- 部分案例是否可外推到特定資料集、架構或部署環境，需以該專案的分布、函式集合與實驗條件檢驗。
- `phQK8xZpgoU` 的術語來自 ASR；相關作用層主張已有列出的視覺補證，但新增細節仍應按需回看影格。
- 本 profile 故意不包含 expression DNA、外部人物評價或生涯時間線，因為本輪目標是來源忠實的技術研究檔案，不是完整 public-figure Persona。

## 下一個可審查動作

將本 P0 dossier 與 P1–P3 的 Distilly merged summary 並列檢視。只有當某個跨來源規則仍保有來源、時間範圍、適用條件與反例／缺口時，才考慮將它轉入 `hung-yi-ml-research-advisor` 的可執行判斷層。
