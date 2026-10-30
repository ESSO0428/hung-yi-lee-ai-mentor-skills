# Evidence Packet: vXb2QYOUzl4 / Transformer／attention／sequence representation

- packet_id: `EVP-CHANNEL-vXb2QYOUzl4-sequence_attention_transformer-V1`
- packet_schema: `hung-yi-channel-evidence-packet.v1`
- packet_type: `EVIDENCE_PACKET_READY`
- video_id: `vXb2QYOUzl4`
- source_url: https://www.youtube.com/watch?v=vXb2QYOUzl4
- title: `加快語言模型生成速度 (1/2)：Flash Attention`
- transcript_type: `official`
- source_quality: `OFFICIAL`
- manifest_status: `VERIFIED`
- concept_id: `sequence_attention_transformer`
- source_role: `PRIMARY`
- source_scope: selective review of selector-approved transcript chunks; not full-video coverage and not a claim of full-video understanding

## Direct evidence

1. `vXb2QYOUzl4:0-30` (`00:00:00.233–00:01:26.319`): Direct transcript evidence. 大家好，那我們就來上課吧 今天的課呢，我們是想要跟大家講說 怎麼加快語言模型的生成速度 那今天這一堂課呢，是預設你已經非常清楚 語言模型內部的運作原理 你知道 Transformer 是怎麼運作的 那這一堂課是要跟你講說 在你已經知道 Transformer 已經怎麼運作的前提之下 我們怎麼加快生成的速度 所以今天這一堂課要講的是生成的過程 今天這一堂課不是要講訓練的過程 而是假設一個語言模型已經被訓練好以後 我們怎麼加快它生成的速度 也就是在使用它的時候 你使用一個語言模型的時候又叫做推論 或者是又叫做 inference 在推論或者是 inference 的情況下 我們怎麼加快語言模型生成的速度 那這邊呢還是用兩頁投影片很快的講一下 語言模型的內部是怎麼運作的 那大家都知道說語言模型就是做文字接龍 你給它一個未完成的句子 它去預測接下來應該產生哪一個 token 那我們都知道說 今天主流的語言模型的類神經網路架構 就是 T…
2. `vXb2QYOUzl4:31-60` (`00:01:26.319–00:02:53.540`): Direct transcript evidence. 讓 Transformer 可以考慮一整個輸入的 Sequence 裡面 所有的資訊 那這個 Self Attention 這個 Layer 呢 它做的事情是這樣的 輸入一排向量 那這邊用 X1 到 X5 來表示 那它會做的事情就是輸出另外一排向量 O1 到 O5 那這個 Self Attention 它是怎麼運作的呢 現在輸入是 X1 到 X5 Self Attention 這個 Layer 做的事情是 首先先把 X1 到 X5 各乘上 3 個不同的 Transformation 的 Matrix 把 X1 變成 V1 K1 Q1 X2 變成 V2 K2 Q2 以此類推 那等一下在多數的課堂裡面 我們都會省略叫這個從 X 變成 QKV 的過程 我們就假設說這個 Transformer 你已經知道輸入的 X 就會變成 QKV 三個向量 那接下來怎麼做計算呢 我們用產生第 4 個位置的輸出來作為例子 那其他位置也是用一樣的計算方…
3. `vXb2QYOUzl4:98-139` (`00:04:22.962–00:05:50.083`): Direct transcript evidence. 你算出來的結果 會跟原來的 self-attention 不一樣 那有些方法的代價是 它是模型綁定的 也就是你要使用這個方法 你一定要訓練特定的模型 你一定要對模型做客製化 才有辦法使用這個方法 它不是一個隨插即用的方法 那如果這兩者都沒有 那它其實可能還是付出了 其他的代價 才有辦法做到加速這件事情 那今天呢 我們就是會完成這個表格 那今天其實會花最多時間講的方法 是在第一部分 我們會詳細的解釋 Flash Attention 這個技術 那其實今天多數的時候 你在使用語言模型的時候 你其實都已經有用到 Flash Attention 只是你不一定知道 它是怎麼做運算的 那第二部分呢 會講一系列跟 KV Cache 有關的方法 那這個部分呢 雖然方法很多 但每個方法呢 就會用一兩頁投影片很快的帶過去 那還有一個今天不會講的方法 叫 Speculative Decoding 那這也是一個非常有效的 可以加快語言模型推論速度的方法…
4. `vXb2QYOUzl4:140-177` (`00:05:50.083–00:07:19.005`): Direct transcript evidence. 那 Speculative Decoding 在我們的作業也是有的 所以你在做作業的時候 你還是需要知道什麼是 Speculative Decoding 好，那我們就開始講 Flash Attention 那 Flash Attention 最早的來源呢 是來自於這篇 22 年的 Paper 所以它也是一個上古時代的技術了 這個上古大神 它有什麼樣的威力呢 它非常的厲害 它不會改變 attention 的計算結果 所以它算出來的東西 跟你知道的那個 attention 算出來的東西 是一模一樣的 它並不是一個近似 再來呢 它是一個隨插即用的方法 你可以直接把這一招 套到任何有使用 self-attention 的 transformer 所以它並沒有綁定任何模型 它是一個可以直接套用在任何 以 Transformer 為基礎的語言模型上的方法 然後它的代價非常非常的小 那我們等一下就來看看 Flash Attention 是一…

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

- Other selected sources for this concept: `Ll-wk8x3G_g` (PRIMARY), `N6aRv06iv2g` (CORROBORATING), `gmsMY5kc-zw` (CORROBORATING).
- Cross-source synthesis is deferred to the concept dossier; duplicate or supporting sources remain in the coverage ledger rather than being re-distilled.
