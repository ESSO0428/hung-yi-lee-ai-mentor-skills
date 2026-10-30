# Evidence Packet: lluMBz5AoOg / CNN／RNN／inductive bias

- packet_id: `EVP-CHANNEL-lluMBz5AoOg-cnn_rnn_inductive_bias-V1`
- packet_schema: `hung-yi-channel-evidence-packet.v1`
- packet_type: `EVIDENCE_PACKET_READY`
- video_id: `lluMBz5AoOg`
- source_url: https://www.youtube.com/watch?v=lluMBz5AoOg
- title: `[TA 補充課] Transformer and its variant (由助教紀伯翰同學講授)`
- transcript_type: `official`
- source_quality: `OFFICIAL`
- manifest_status: `VERIFIED`
- concept_id: `cnn_rnn_inductive_bias`
- source_role: `PRIMARY`
- source_scope: selective review of selector-approved transcript chunks; not full-video coverage and not a claim of full-video understanding

## Direct evidence

1. `lluMBz5AoOg:1-18` (`00:04:26.700–00:05:55.832`): Direct transcript evidence. 我們就開始吧 今天的主題叫做 New Architecture 我是今天的助教紀伯翰 New Architecture 意思上就是新架構 在講新架構之前先來複習一下你們作業裡面會用到的舊架構 Review 就分幾個超級超級簡單的模型 就是 Fully Connected Network、Concolutional Network 跟 Recurrent Neural Network 一開始就快速把這些投影片帶過 你可以發現在現在模型裡，隨處都可以發現 Fully connected network 的影子 這個 layer 的寬度都是自己可以調整，自己去 train 的 再來就是在 CV 領域裡面很常使用到的 Convolutional Neural Network 你可以知道說像這樣的架構裡 這個架構到後來都很受廣用 甚至發展出有很多很多很深很深的模型 像是 ResNet 甚至後來來有用 residual 發展出來的 Den…
2. `lluMBz5AoOg:19-24` (`00:05:55.832–00:06:22.685`): Direct transcript evidence. CNN 最好的性質其實是 他可以抓住一些 local 的資訊 這個圖就是想表示說 一個例子在 CNN 是怎麼 process 的 再來就是 Recurrent Neural Network 就是你在做序列型 data 的時候會做的模型
3. `lluMBz5AoOg:25-41` (`00:06:25.729–00:07:52.646`): Direct transcript evidence. 簡單來說，舉個例子來說 你希望你的 embedding 可以模擬到句子的句意 你會用一個 LCM 或是一個 GRU 你就會讓 GRU 從 What time is it 的 What 一路把 What time is it 這個字的 token 吃完 你希望最後這個問號得到的 embedding 是有含 有包含到 What time is it 的句意 從這個架構衍伸出來的就像是現在非常流行的 ****** 或是在做 machine translation 的時候 你會做的 Seq2seq 的這種 method 以及像剛剛講 RNN，其實 RNN 有延伸出很多變形，像 LCM 跟 GRU 還有像 Pointer Network 等等 複習完這些很基本很基本的架構之後 你說新架構是什麼，是不是就是把這些架構全部把它疊起來 看自己的創意 我今天在夢中夢到這個參數，這個 hidden size
4. `lluMBz5AoOg:42-63` (`00:07:52.646–00:09:16.444`): Direct transcript evidence. 我是不是要先疊一個 CNN 再疊一個 RNN 再把 Fully connect 接上去 是不是我把所有的東西都疊起來 我就希望這個模型在我想要的 task 上面可以做得很好 我就把他們，隨我自己的意思把他們亂疊 好之後就開始 train 然後就開始 tune 你的參數 就像這個圖片一樣你開始 tune 你的參數，什麼 learning rate L2 的 weighted decay dropout 開始調 完之後你發現說 我的模型怎麼 train 起來都 train 不太起來，怎麼這麼奇怪 然後你就會有一個想法 一個很智障的想法 你就會覺得說是不是我疊的不夠深 就再把他疊深一點 繼續把它疊深之後就開始 tune neural network 然後開始 tune 參數跟前面的 case 一樣 然後發現 tune 完之後你的模型還是一個垃圾 這就結束了 其實我們覺得在做一個新的 task 的時候 可以先去 follow 說這個…

## ASR observation

- None: selected evidence is from a verified official/auto transcript, not ASR output.

## Visual observation

- None requested: the selected transcript anchors support the bounded concept-routing claim; no formula, chart, code screen, or visual-only assertion is used.

## Inference

- The selector places this source in `cnn_rnn_inductive_bias` as `PRIMARY`. This is a bounded source-set relation, not a formal mentor rule.

## Unknowns and limits

- The packet does not establish a universal architecture, algorithm, or performance conclusion.
- Selected chunks may omit counterexamples, task conditions, and empirical comparisons elsewhere in the video.

## De-duplication and cross-source relation

- Other selected sources for this concept: `xCGidAeyS4M` (PRIMARY), `gjsdVi90yQo` (CORROBORATING), `OP5HcXJg2Aw` (CORROBORATING).
- Cross-source synthesis is deferred to the concept dossier; duplicate or supporting sources remain in the coverage ledger rather than being re-distilled.
