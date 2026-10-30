# P0 蒸餾：泛化指標與訓練目標

## Dimension Coverage
- 研究決策：何時可以把與泛化相關的可量測指標納入 objective function，而不是把任何 proxy 當作通用修方。

## Source Metadata
- URL: https://www.youtube.com/watch?v=pivB5jEBOQw
- Source type: 李宏毅官方課程影片、ffprobe 已驗證、official timed transcript；一手來源；source weight: 2。
- Canonical source chunks: `pivB5jEBOQw:30-63`（89.66–178.54 秒）與 `pivB5jEBOQw:64-88`（178.54–266.02 秒）；關鍵字幕 cue 落在 157.26–182.06 秒。

## Key Findings
- 課程以參數 norm 較小可能有較佳泛化能力為例，說明可將這類項目加入 objective function。
- 講者接著將 sharpness 與 sensitivity 說成兩個已知的泛化指標，並以「假設知道它代表泛化能力」界定其前提。
- 因此可操作的規則是：先在目標設定得到「此指標與泛化有關」的證據，再考慮以訓練目標項實作它。

## Contradictions
- 把 regularization term 加進 objective 是合理分支，並不等於每個 norm、sharpness 或 sensitivity proxy 都會在任何模型、資料分佈與部署目標上改善泛化。

## Inferences (clearly marked as inference, not fact)
- 推論：先以固定訓練條件的受控實驗檢驗指標與 validation／deployment metric 的關聯，再決定其係數與採用與否；這是將課程條件落地的研究設計。

## Gaps and Missing Information
- 此來源沒有直接給出 ranking／Top-k 或一般 task metric 與 objective 對齊的完整規則，也沒有為特定現代架構保證 proxy 有效。
