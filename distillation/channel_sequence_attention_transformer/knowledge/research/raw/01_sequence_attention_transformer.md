# Research Dossier: Transformer／attention／sequence representation

## Source Metadata

- Source: `Ll-wk8x3G_g` — 如何讓 Transformer 知道輸入 Token 的順序？Absolute、Relative、RoPE、到沒有 Positional Embedding
- URL: https://www.youtube.com/watch?v=Ll-wk8x3G_g
- Source role: `PRIMARY`
- Source weight: 1
- Evidence packet: `EVP-CHANNEL-Ll-wk8x3G_g-sequence_attention_transformer-V1` (data/processing/channel_evidence_packets_v1/Ll-wk8x3G_g--sequence_attention_transformer.md)
- Transcript type: `official`; selector confidence: `HIGH`
- Source: `vXb2QYOUzl4` — 加快語言模型生成速度 (1/2)：Flash Attention
- URL: https://www.youtube.com/watch?v=vXb2QYOUzl4
- Source role: `PRIMARY`
- Source weight: 1
- Evidence packet: `EVP-CHANNEL-vXb2QYOUzl4-sequence_attention_transformer-V1` (data/processing/channel_evidence_packets_v1/vXb2QYOUzl4--sequence_attention_transformer.md)
- Transcript type: `official`; selector confidence: `HIGH`
- Source: `N6aRv06iv2g` — 【機器學習2021】Transformer (下)
- URL: https://www.youtube.com/watch?v=N6aRv06iv2g
- Source role: `CORROBORATING`
- Source weight: 2
- Evidence packet: `EVP-CHANNEL-N6aRv06iv2g-sequence_attention_transformer-V1` (data/processing/channel_evidence_packets_v1/N6aRv06iv2g--sequence_attention_transformer.md)
- Transcript type: `official`; selector confidence: `HIGH`
- Source: `gmsMY5kc-zw` — 【機器學習2021】自注意力機制 (Self-attention) (下)
- URL: https://www.youtube.com/watch?v=gmsMY5kc-zw
- Source role: `CORROBORATING`
- Source weight: 2
- Evidence packet: `EVP-CHANNEL-gmsMY5kc-zw-sequence_attention_transformer-V1` (data/processing/channel_evidence_packets_v1/gmsMY5kc-zw--sequence_attention_transformer.md)
- Transcript type: `official`; selector confidence: `HIGH`

## Evidence

- `Ll-wk8x3G_g` (PRIMARY):
  - `Ll-wk8x3G_g:0-30` (`00:00:00.000–00:01:29.722`): 好，今天我們這一堂課要講的是 Positional Embedding 那這個技術它讓 Transformer 可以知道輸入 Token 的順序 為什麼需要特別打造個技術讓 Transformer 知道輸入 Token 的順序呢 因為原來的 Transformer 它是沒有辦法考慮輸入 Token 的順序的 怎麼說呢，我們都知道大型語言模型 它的背後就是一個叫 Transformer 的神經網路架構 那它的輸入呢 就是一串 Token 它的輸出呢 就是去預測下一個 Token 那 Transformer 怎麼處理 這些輸入的 Token 呢 首先輸入的 Token 會被變成 Embedding 也就是每一個 Token 會變成一個向量 那這些向量呢 會變成某一個 Layer 的輸入 所以這些 Token 會被輸入到第一個 Layer 那每個 Layer 裡面都有一個叫做 Self-Attention 的模組 那 Self-At…
  - `Ll-wk8x3G_g:31-75` (`00:01:29.722–00:02:59.345`): 會是一排向量 我們只是舉最右邊的 這個向量的計算過程 給大家看 好，那我們來看一下 Self-Attention 的計算過程 你會發現這個計算過程 是沒有考慮到輸入的 Token 的順序的 首先每一個 Embedding XA 到 XD 那都會分別乘上 三個矩陣轉成 Q、K、V 三個矩陣 那如果你要算的是 OD 的話 那你就會把 QD XD 產生出來的 query 去對每一個 Token 的 key 去算 Attention 那算 Attention 的過程就是做內積 就是把 K 跟 Q 做內積 然後算出 Attention 的 weight 這邊用 A 加上一個下標 來表示 Attention 的 weight 那我們會做 Softmax 來做 Normalization 得到 Normalized 以後的 Attention Weight 然後根據 Attention Weight 對每一個 Token 的 Embeddi…
  - `Ll-wk8x3G_g:76-111` (`00:02:59.345–00:04:27.900`): 但是其實在這個課程的尾聲 會告訴你說 其實 Self-Attention 是偷偷藏了位置的資訊 好那我們現在就按照一個非常直覺的想法 告訴你說 Self-Attention 是沒有位置資訊的 假設我們現在把 A 跟 C 兩個 Token 的位置對調 也就輸入不是 ABCD 而是 CBAD 那會對輸出造成什麼影響呢 你會發現對 OD 這個輸出 是完全沒有影響的 因為當我們把 A 跟 C 的位置對調的時候 那這一些 Q、K、V 還有這些 A 它的位置也就跟著對調 而 weighted sum 這件事情 是跟位置沒有關係的 我們做 weighted sum 以後 就是把所有的 Token 對應到的 V 直接做 weighted sum 直接加起來 所以到底是先加 C 還是先加 A 根本就不會對結果造成影響 所以我們改變輸入 Token 的順序 是不會影響輸出的 那這會造成很嚴重的 問題 因為 Token 的順序 對於理解一個句子是非…
  - `Ll-wk8x3G_g:112-158` (`00:04:27.900–00:05:55.722`): 這兩個 sequence 的差異 這不是我們樂見的事情 所以呢 我們需要給 Transformer position 的資訊 位置的資訊 那今天這堂課呢 就是我們來探討一系列 告訴 Self-Attention 也就是告訴 Transformer Token 位置資訊的方式 我們先從最早的 Absolute Positional Embedding 開始講起 最早的 Positional Embedding 的想法是怎麼樣呢 它的想法是 我們對每一個位置 都設計一個特別的 Embedding 這個 Embedding 代表了 位置的資訊 我現在用 P0 一直到 P3 代表對應到位置 0 1、2、3 每一個位置的 那一個特別的 Embedding 然後我們把這個特別的 Embedding 它就是一個向量 一排數字 加到 Token 上面 所以如果我們現在 擺放的順序是 ABCD 那 A 就是加 position 0 B 就加 p…
- `vXb2QYOUzl4` (PRIMARY):
  - `vXb2QYOUzl4:0-30` (`00:00:00.233–00:01:26.319`): 大家好，那我們就來上課吧 今天的課呢，我們是想要跟大家講說 怎麼加快語言模型的生成速度 那今天這一堂課呢，是預設你已經非常清楚 語言模型內部的運作原理 你知道 Transformer 是怎麼運作的 那這一堂課是要跟你講說 在你已經知道 Transformer 已經怎麼運作的前提之下 我們怎麼加快生成的速度 所以今天這一堂課要講的是生成的過程 今天這一堂課不是要講訓練的過程 而是假設一個語言模型已經被訓練好以後 我們怎麼加快它生成的速度 也就是在使用它的時候 你使用一個語言模型的時候又叫做推論 或者是又叫做 inference 在推論或者是 inference 的情況下 我們怎麼加快語言模型生成的速度 那這邊呢還是用兩頁投影片很快的講一下 語言模型的內部是怎麼運作的 那大家都知道說語言模型就是做文字接龍 你給它一個未完成的句子 它去預測接下來應該產生哪一個 token 那我們都知道說 今天主流的語言模型的類神經網路架構 就是 T…
  - `vXb2QYOUzl4:31-60` (`00:01:26.319–00:02:53.540`): 讓 Transformer 可以考慮一整個輸入的 Sequence 裡面 所有的資訊 那這個 Self Attention 這個 Layer 呢 它做的事情是這樣的 輸入一排向量 那這邊用 X1 到 X5 來表示 那它會做的事情就是輸出另外一排向量 O1 到 O5 那這個 Self Attention 它是怎麼運作的呢 現在輸入是 X1 到 X5 Self Attention 這個 Layer 做的事情是 首先先把 X1 到 X5 各乘上 3 個不同的 Transformation 的 Matrix 把 X1 變成 V1 K1 Q1 X2 變成 V2 K2 Q2 以此類推 那等一下在多數的課堂裡面 我們都會省略叫這個從 X 變成 QKV 的過程 我們就假設說這個 Transformer 你已經知道輸入的 X 就會變成 QKV 三個向量 那接下來怎麼做計算呢 我們用產生第 4 個位置的輸出來作為例子 那其他位置也是用一樣的計算方…
  - `vXb2QYOUzl4:98-139` (`00:04:22.962–00:05:50.083`): 你算出來的結果 會跟原來的 self-attention 不一樣 那有些方法的代價是 它是模型綁定的 也就是你要使用這個方法 你一定要訓練特定的模型 你一定要對模型做客製化 才有辦法使用這個方法 它不是一個隨插即用的方法 那如果這兩者都沒有 那它其實可能還是付出了 其他的代價 才有辦法做到加速這件事情 那今天呢 我們就是會完成這個表格 那今天其實會花最多時間講的方法 是在第一部分 我們會詳細的解釋 Flash Attention 這個技術 那其實今天多數的時候 你在使用語言模型的時候 你其實都已經有用到 Flash Attention 只是你不一定知道 它是怎麼做運算的 那第二部分呢 會講一系列跟 KV Cache 有關的方法 那這個部分呢 雖然方法很多 但每個方法呢 就會用一兩頁投影片很快的帶過去 那還有一個今天不會講的方法 叫 Speculative Decoding 那這也是一個非常有效的 可以加快語言模型推論速度的方法…
  - `vXb2QYOUzl4:140-177` (`00:05:50.083–00:07:19.005`): 那 Speculative Decoding 在我們的作業也是有的 所以你在做作業的時候 你還是需要知道什麼是 Speculative Decoding 好，那我們就開始講 Flash Attention 那 Flash Attention 最早的來源呢 是來自於這篇 22 年的 Paper 所以它也是一個上古時代的技術了 這個上古大神 它有什麼樣的威力呢 它非常的厲害 它不會改變 attention 的計算結果 所以它算出來的東西 跟你知道的那個 attention 算出來的東西 是一模一樣的 它並不是一個近似 再來呢 它是一個隨插即用的方法 你可以直接把這一招 套到任何有使用 self-attention 的 transformer 所以它並沒有綁定任何模型 它是一個可以直接套用在任何 以 Transformer 為基礎的語言模型上的方法 然後它的代價非常非常的小 那我們等一下就來看看 Flash Attention 是一…
- `N6aRv06iv2g` (CORROBORATING):
  - `N6aRv06iv2g:251-295` (`00:08:50.890–00:10:19.610`): 先無視這個問題 繼續走下去 好 那我們 來看一下這個 Decoder 啊 它內部的結構長什麼樣子 那我們這邊呢 把 Encoder 的部分先暫時省略掉 那在 Transformer 裡面 Decoder 的結構呢 長得是這個樣子的 看起來有點複雜 比 Encoder 還稍微複雜一點 那我們現在先把 Encoder 跟 Decoder 放在一起 稍微比較一下它們之間的差異 那你會發現說 如果我們把 Decoder 中間這一塊 中間這一塊把它蓋起來 其實 Encoder 跟 Decoder 並沒有那麼大的差別 你看 Encoder 這邊 Multi-Head Attention 然後 Add & Norm Feed Forward Add & Norm 重複 N 次 Decoder 其實也是一樣 當我們把中間這一塊遮起來以後 我們等一下再講 遮起來這一塊裡面做了什麼事 但當我們把中間這塊遮起來以後 欸 那 Decoder 也是 有…
  - `N6aRv06iv2g:296-335` (`00:10:19.610–00:11:48.040`): Multi-Head Attention 這一個 Block 上面 還加了一個 Masked 這個 Masked 是什麼意思呢 這個 Masked 的意思是這樣子的 這是我們原來的 Self-Attention Input 一排 Vector Output 另外一排 Vector 這一排 Vector 每一個輸出 都要看過完整的 Input 以後 才做決定 所以輸出 b1 的時候 其實是根據 a1 到 a4 所有的資訊 去輸出 b1 當我們把 Self-Attention 轉成 Masked Attention 的時候 它的不同點在哪裡呢 它的不同點是 現在我們不能再看右邊的部分 也就是產生 b1 的時候 我們只能考慮 a1 的資訊 你不能夠再考慮 a2 a3 a4 產生 b2 的時候 你只能考慮 a1 a2 的資訊 不能再考慮 a3 a4 的資訊 產生 b3 的時候 你就不能考慮 a4 的資訊 產生 b4 的時候 你可以用整…
- `gmsMY5kc-zw` (CORROBORATING):
  - `gmsMY5kc-zw:70-103` (`00:03:28.080–00:04:57.490`): 那接下來我們從矩陣乘法的角度 再重新講一次我們剛才講的 Self-attention 是怎麼運作的 好 那 Self-attention 是怎麼運作的呢 我們現在已經知道說 a1 到 a4 它們每一個 a 都要分別產生 q k v 所以 a1 要產生 q1 k1 v1 a2 要產生 q2 k2 v2 以此類推 每一個 a 都產生 q k v 如果要用矩陣運算表示這個操作的話 是什麼樣子呢 我們每一個 a i 都乘上 q 這個 都乘上一個矩陣 我們這邊用 wq 來表示它 得到 qi 每一個 a 都要乘上 wq 得到 qi 那這些不同的 a 你可以把它合起來 當作一個矩陣來看待 什麼意思呢 a1 乘上 wq 得到 q1 a2 也乘上 wq 得到 q2 一樣 a3 a4 也都乘上 wq 得到 q3 跟 q4 那你可以把 a1 到 a4 拼起來 看作是一個矩陣 這個矩陣我們用 I 來表示 這邊這個 I 這個大寫的字母 I 它代表的是一…
  - `gmsMY5kc-zw:104-142` (`00:04:57.490–00:06:26.010`): 我們用 Q 來表示它 這個 Q 就是 q1 到 q4 你把 q1 到 q4 這四個 vector 拼起來 就是 Q 的四個 column 所以我們從 a1 到 a4 得到 q1 到 q4 這一件事情 這個操作 其實就是把一個叫做 I 的矩陣 I 這個矩陣 它裡面的 column 就是我們 Self-attention 的 input a1 到 a4 把 I 這個矩陣 乘上另外一個矩陣 wq 那 wq 其實是 network 的參數 它是等一下會被認出來的 把 I 乘上 wq 得到 Q 這個 Q 的四個 column 就是 q1 到 q4 那接下來怎麼產生 k 跟 v 呢 它的操作跟 q 是一模一樣的 我們就不要再細講 免得你覺得很無聊 所以 a 乘上 wk 就會得到這個 key 就會得到這個 k 這個 vector 那我們把這個 input 的四個 vector a1 到 a4 拼起來 當作是一個矩陣 叫做 I 把 I 乘上一…

## Patterns and Repeated Themes

- 多個獨立來源均提供 `sequence_attention_transformer` 的 selector-approved transcript anchors；可把它們用於受限的 cross-source candidate synthesis。

## Contradictions

- 來源跨年份、模態與任務；它們的共同概念不等於共同的 benchmark、資料分布或性能結論。

## Inferences

- Candidate inference (not formal): 序列任務的架構選擇應把可見上下文範圍、token 順序訊號與推論期記憶成本視為可驗證的設計變數，而不是只比較模型名稱。
- Candidate decision rule: 先固定資料、訓練預算與評估指標，建立局部上下文或弱位置訊號基線；再比較 attention 範圍、position method 與 KV/cache 策略，並按序列長度與延遲分層報告。

## Gaps and Missing Information

- 未使用未選定的片段、影格或投影片；若未來某個結論需要公式、圖表或程式畫面，必須建立獨立 visual-evidence request。
- 本 dossier 是 Distilly research input，不取代原始影片、source chunks 或 evidence packets。
