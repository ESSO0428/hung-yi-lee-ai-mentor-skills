# Evidence Packet: xCGidAeyS4M / CNN／RNN／inductive bias

- packet_id: `EVP-CHANNEL-xCGidAeyS4M-cnn_rnn_inductive_bias-V1`
- packet_schema: `hung-yi-channel-evidence-packet.v1`
- packet_type: `EVIDENCE_PACKET_READY`
- video_id: `xCGidAeyS4M`
- source_url: https://www.youtube.com/watch?v=xCGidAeyS4M
- title: `ML Lecture 21-1: Recurrent Neural Network (Part I)`
- transcript_type: `official`
- source_quality: `OFFICIAL`
- manifest_status: `VERIFIED`
- concept_id: `cnn_rnn_inductive_bias`
- source_role: `PRIMARY`
- source_scope: selective review of selector-approved transcript chunks; not full-video coverage and not a claim of full-video understanding

## Direct evidence

1. `xCGidAeyS4M:2-19` (`00:00:11.110–00:01:37.890`): Direct transcript evidence. 好，那接下來呢，我們來講一下 Recurrent Neural Network 那 Recurrent Neural Network呢 它其實也可以做到我們在前一堂課裡面 講的 sequence labeling 的 task 那最後呢，我們再來說他們有 甚麼樣的不同 那我們這邊要舉的例子呢 是 Slot Filling，那我們知道說 現在很流行呢，做一些智慧客服之類的東西 譬如說，做一些智慧的訂票系統 那這種智慧客服或智慧訂票系統裡面呢 你往往需要 Slot Filling 這個技術 Slot Filling 指的是甚麼呢 Slot Filling 指的是說 比如說假設有一個人對你的訂票系統說 I would like to arrive Taipei on November 2nd 那你的系統要自動知道說 你的系統裡面有一些 slot 比如說，在這個 訂票系統裡面呢 它會有一個 slot叫做 Destination 它會有…
2. `xCGidAeyS4M:96-116` (`00:07:08.400–00:08:30.510`): Direct transcript evidence. 然後所有的 neuron 都沒有任何的 bias 值 然後假設所有的 activation function 都是 linear 這樣可以不要讓計算太複雜 那現在假設我們的 input 是一個 sequence 我們的 input 是 [11] [11] [22] 那我們把[11] [11] [22] 這個 sequence input 到這個 Recurrent Neural Network 裡面去 會發生甚麼事呢？ 那首先呢，在你開始要 使用這個 Recurrent Neural Network的時候呢 你必須要給 memory 起始值 你必須要給 memory 在還沒有放進任何東西的時候， 你必須要給它一個初始值，比如說這邊呢 我們在假設還沒有放進任何東西之前 memory 裡面的值是 0 那現在輸入第一個輸入 [1 1] 那接下來會發生甚麼事呢 對這個 neuron 來說 它除了接到 input 的 [1 1] 以外…
3. `xCGidAeyS4M:139-152` (`00:10:01.990–00:10:53.980`): Direct transcript evidence. 所以 2 就被洗掉，變成 6 那接下來呢，我們的 input 是 2 跟 2，假設 input 是 [2 2]，這邊每一個綠色的 neuron 它考慮的 4 個 input ：2 跟 2 跟 6 跟 6 所以 6 + 6 + 2 + 2 是多少呢，得到的值是 16 那紅色 neuron 的 output 就是 32 所以 input 2 跟 2 的時候呢，output 是 32 那今天在做 Recurrent neural network 的時候呢 有一件很重要的事情就是 這個 input 的 sequence Recurrent neural network 在 考慮它的時候，並不是 independent 今天如果你任意調換 input sequence 的順序 比如說把 2 跟 2 挪到最前面來 那 output 呢，是會完全不一樣的 所以在 Recurrent neural network 裡面， 它會考慮 input…
4. `xCGidAeyS4M:644-661` (`00:47:47.060–00:48:56.980`): Direct transcript evidence. 我用 RNN 做了甚麼事情的時候， 就是你不要去問他說為甚麼你不用 LSTM 因為他其實就是用 LSTM ， 因為現在當你說你在做 RNN 的時候 其實你指的就是用 LSTM 所以呢，他其實是比較 standard 的 其實 Keras 裡面有支援 LSTM 啦，所以就算是 剛才講得這麼複雜的東西你沒聽懂就算了 在 Keras 裡面就是打 LSTM 這4個字母 然後就結束了 那 Keras 它其實支援三種 Recurrent neural networks，一個是 LSTM 一個是 GRU 是 LSTM 的一個稍微簡化的版本 它只有兩個 gate 據說少了一個 gate，但是 performance 跟 LSTM 差不多，而且少了 1/3 的參數 所以比較不容易 over-fitting 如果你要用一般的、我們這堂課最一開始講的那種 最簡單的 RNN 的話 也要說是 SimpleRNN 才行這樣子 那我想我們今天就上到這邊好了…

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

- Other selected sources for this concept: `lluMBz5AoOg` (PRIMARY), `gjsdVi90yQo` (CORROBORATING), `OP5HcXJg2Aw` (CORROBORATING).
- Cross-source synthesis is deferred to the concept dossier; duplicate or supporting sources remain in the coverage ledger rather than being re-distilled.
