# G02 agent context 越跑越肥

- 覆蓋度：已涵蓋（2026 context engineering）；prompt caching、MCP 等未涵蓋
- 主題：長任務 agent 變慢、變貴、忘事

## 使用者訊息

我做了一個程式碼修復 agent，每個 run 平均 60 步，用一堆工具（搜尋、讀檔、跑測試）。觀察：

```
step 10   context  18k tokens   每步 4s
step 40   context  95k tokens   每步 11s
step 60   context 140k tokens   每步 17s, 開始重複做過的步驟
```

單一次 run 成本約 US$2。測試輸出動輒 2 萬 token。我該怎麼辦？

## 預期判斷

先分析 context 被什麼塞滿（可能是工具輸出，尤其測試 log），在入口過濾。工具輸出先 observation masking，更長再 LLM 摘要，並留可回查指標、原文存檔。摘要要指明什麼最不能丟，否則 context collapse。壓縮時機用硬規則觸發，不要指望模型自己決定。超長輸入存檔、prompt 只放 metadata。

## 關鍵檢查

- 先審計 context 組成，而不是直接壓縮。
- masking -> 摘要的順序與可回查。
- 硬規則觸發。
- prompt caching 等標為課程未講。

## GOOD 答案必含

1. 症狀成因：每一步都重送整段歷史。(urwDLyNa9FU S0002)
2. 先分析 context 被什麼塞滿，在入口過濾（治本）。(urwDLyNa9FU S0026)
3. 工具輸出太長：先 observation masking，更長再摘要；留可回查指標、原文存檔。(urwDLyNa9FU S0009-S0010; lVdajtNpaGI S0067)
4. 摘要指明「什麼最不能丟」，否則 context collapse。(urwDLyNa9FU S0016)
5. 不要指望模型自己決定何時壓縮，用硬規則。(urwDLyNa9FU S0020)
6. 三招：選擇（RAG 套到文件、工具、記憶）、壓縮、multi-agent（價值在隔離 context）。(lVdajtNpaGI S0066-S0074)
7. 工具上百個時按需檢索說明；超長輸入存硬碟、讓模型寫程式搜尋。(M2Yg1kwPpts S0040; urwDLyNa9FU S0030 S0035)
8. 設預算、步數上限、檢查點屬推論（課堂只講故事）。(bJZTJ7MjYqg S0003)
9. agent 做不好，先查它「看得到什麼」。(R6fZR_9kmIw S0004)
10. 一般 ML / 工程（標示）：prompt caching、MCP、具體 token 門檻、計價；課程沒講，也沒給失敗率量化。

## 不可

- 說他給了 token 門檻（例如 80k 就壓縮）。
- 讓模型自己決定何時壓縮。
- 把 prompt caching 等歸給他。
- 無來源地列一堆 agent 框架名詞。

## 評分（0-2）

| 準則 | 0 | 1 | 2 |
|---|---|---|---|
| R1 先審計來源 | 直接壓縮 | 提及審計 | 要求 log 分析並在入口過濾 |
| R2 masking -> 摘要順序 | 只做摘要 | 提兩者未排序 | 排序並提可回查與存檔 |
| R3 硬規則 + 摘要保留清單 | 無 | 其一 | 兩者皆有，並說明 context collapse |
| R4 未涵蓋標示 | 門檻歸給他 | 未標 | 標 caching/MCP/門檻為一般或課程外 |
| R5 來源標示 | 無 | 部分 | 完整 |
