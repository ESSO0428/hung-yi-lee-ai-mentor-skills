# Evidence Packet: Ll-wk8x3G_g / Transformer／attention／sequence representation

- packet_id: `EVP-CHANNEL-Ll-wk8x3G_g-sequence_attention_transformer-V1`
- packet_schema: `hung-yi-channel-evidence-packet.v1`
- packet_type: `EVIDENCE_PACKET_READY`
- video_id: `Ll-wk8x3G_g`
- source_url: https://www.youtube.com/watch?v=Ll-wk8x3G_g
- title: `如何讓 Transformer 知道輸入 Token 的順序？Absolute、Relative、RoPE、到沒有 Positional Embedding`
- transcript_type: `official`
- source_quality: `OFFICIAL`
- manifest_status: `VERIFIED`
- concept_id: `sequence_attention_transformer`
- source_role: `PRIMARY`
- source_scope: selective review of selector-approved transcript chunks; not full-video coverage and not a claim of full-video understanding

## Direct evidence

1. `Ll-wk8x3G_g:0-30` (`00:00:00.000–00:01:29.722`): Direct transcript evidence. 好，今天我們這一堂課要講的是 Positional Embedding 那這個技術它讓 Transformer 可以知道輸入 Token 的順序 為什麼需要特別打造個技術讓 Transformer 知道輸入 Token 的順序呢 因為原來的 Transformer 它是沒有辦法考慮輸入 Token 的順序的 怎麼說呢，我們都知道大型語言模型 它的背後就是一個叫 Transformer 的神經網路架構 那它的輸入呢 就是一串 Token 它的輸出呢 就是去預測下一個 Token 那 Transformer 怎麼處理 這些輸入的 Token 呢 首先輸入的 Token 會被變成 Embedding 也就是每一個 Token 會變成一個向量 那這些向量呢 會變成某一個 Layer 的輸入 所以這些 Token 會被輸入到第一個 Layer 那每個 Layer 裡面都有一個叫做 Self-Attention 的模組 那 Self-At…
2. `Ll-wk8x3G_g:31-75` (`00:01:29.722–00:02:59.345`): Direct transcript evidence. 會是一排向量 我們只是舉最右邊的 這個向量的計算過程 給大家看 好，那我們來看一下 Self-Attention 的計算過程 你會發現這個計算過程 是沒有考慮到輸入的 Token 的順序的 首先每一個 Embedding XA 到 XD 那都會分別乘上 三個矩陣轉成 Q、K、V 三個矩陣 那如果你要算的是 OD 的話 那你就會把 QD XD 產生出來的 query 去對每一個 Token 的 key 去算 Attention 那算 Attention 的過程就是做內積 就是把 K 跟 Q 做內積 然後算出 Attention 的 weight 這邊用 A 加上一個下標 來表示 Attention 的 weight 那我們會做 Softmax 來做 Normalization 得到 Normalized 以後的 Attention Weight 然後根據 Attention Weight 對每一個 Token 的 Embeddi…
3. `Ll-wk8x3G_g:76-111` (`00:02:59.345–00:04:27.900`): Direct transcript evidence. 但是其實在這個課程的尾聲 會告訴你說 其實 Self-Attention 是偷偷藏了位置的資訊 好那我們現在就按照一個非常直覺的想法 告訴你說 Self-Attention 是沒有位置資訊的 假設我們現在把 A 跟 C 兩個 Token 的位置對調 也就輸入不是 ABCD 而是 CBAD 那會對輸出造成什麼影響呢 你會發現對 OD 這個輸出 是完全沒有影響的 因為當我們把 A 跟 C 的位置對調的時候 那這一些 Q、K、V 還有這些 A 它的位置也就跟著對調 而 weighted sum 這件事情 是跟位置沒有關係的 我們做 weighted sum 以後 就是把所有的 Token 對應到的 V 直接做 weighted sum 直接加起來 所以到底是先加 C 還是先加 A 根本就不會對結果造成影響 所以我們改變輸入 Token 的順序 是不會影響輸出的 那這會造成很嚴重的 問題 因為 Token 的順序 對於理解一個句子是非…
4. `Ll-wk8x3G_g:112-158` (`00:04:27.900–00:05:55.722`): Direct transcript evidence. 這兩個 sequence 的差異 這不是我們樂見的事情 所以呢 我們需要給 Transformer position 的資訊 位置的資訊 那今天這堂課呢 就是我們來探討一系列 告訴 Self-Attention 也就是告訴 Transformer Token 位置資訊的方式 我們先從最早的 Absolute Positional Embedding 開始講起 最早的 Positional Embedding 的想法是怎麼樣呢 它的想法是 我們對每一個位置 都設計一個特別的 Embedding 這個 Embedding 代表了 位置的資訊 我現在用 P0 一直到 P3 代表對應到位置 0 1、2、3 每一個位置的 那一個特別的 Embedding 然後我們把這個特別的 Embedding 它就是一個向量 一排數字 加到 Token 上面 所以如果我們現在 擺放的順序是 ABCD 那 A 就是加 position 0 B 就加 p…

## ASR observation

- None: selected evidence is from a verified official/auto transcript, not ASR output.

## Visual observation

- None requested: the selected transcript anchors support the bounded concept-routing claim; no formula, chart, code screen, or visual-only assertion is used.

## Inference

- The selector places this source in `sequence_attention_transformer` as `PRIMARY`. This is a bounded source-set relation, not a formal mentor rule.

## Unknowns and limits

- The packet does not establish a universal architecture, algorithm, or performance conclusion.
- Selected chunks may omit counterexamples, task conditions, and empirical comparisons elsewhere in the video.

## De-duplication and cross-source relation

- Other selected sources for this concept: `vXb2QYOUzl4` (PRIMARY), `N6aRv06iv2g` (CORROBORATING), `gmsMY5kc-zw` (CORROBORATING).
- Cross-source synthesis is deferred to the concept dossier; duplicate or supporting sources remain in the coverage ledger rather than being re-distilled.
