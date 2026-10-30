# Evidence Packet: BABPWOkSbLE / optimization／training paradigm

- packet_id: `EVP-CHANNEL-BABPWOkSbLE-optimization_training-V1`
- packet_schema: `hung-yi-channel-evidence-packet.v1`
- packet_type: `EVIDENCE_PACKET_READY`
- video_id: `BABPWOkSbLE`
- source_url: https://www.youtube.com/watch?v=BABPWOkSbLE
- title: `【機器學習2021】類神經網路訓練不起來怎麼辦 (五)： 批次標準化 (Batch Normalization) 簡介`
- transcript_type: `official`
- source_quality: `OFFICIAL`
- manifest_status: `VERIFIED`
- concept_id: `optimization_training`
- source_role: `CORROBORATING`
- source_scope: selective review of selector-approved transcript chunks; not full-video coverage and not a claim of full-video understanding

## Direct evidence

1. `BABPWOkSbLE:0-33` (`00:01:10.550–00:02:39.450`): Direct transcript evidence. 這邊是一個很快地介紹 Batch Normalization 這個技術 好 那你記得啊 我們之前才講過說 我們能不能夠直接改 error surface 的 landscape 我們覺得說 error surface 如果很崎嶇的時候 它比較難 train 那我們能不能夠直接把山剷平 讓它變得比較好 train 呢 Batch Normalization 就是其中一個 把山剷平的想法 好 那我記得我們在講 optimization 的時候 我們一開始就跟大家講說 不要小看 optimization 這個問題 有時候就算你的 error surface 是 confessed 它就是一個碗的形狀 都不見得很好 train 那我們舉的例子就是 假設你的兩個參數啊 它們對 Loss 的斜率差別非常大 在 W1 這個方向上面 你的斜率變化很小 在 W2 這個方向上面斜率變化很大 你今天如果是固定的 learning rate 你可能很…
2. `BABPWOkSbLE:176-213` (`00:08:29.570–00:09:58.460`): Direct transcript evidence. variance呢 是 1 那你就會發現說所有的數值 所有 feature 不同 dimension 的數值 都在 0 上下 那你可能就可以製造一個 比較好的 error surface 所以像這樣子 Feature Normalization 的方式 往往對你的 training 有幫助 它可以讓你在做 gradient descent 的時候 這個 gradient descent 它的 Loss 收斂更快一點 可以讓你的 gradient descent 它的訓練更順利一點 這個是 Feature Normalization 好 所以當然 Deep Learning 可以做 Feature Normalization 你可能會把 feature 做 normalize 以後 其實在助教的 code 裡面 我們都有對 feature 做 normalization 得到 x tilde 以後呢 這個是 x tilde 代表…

## ASR observation

- None: selected evidence is from a verified official/auto transcript, not ASR output.

## Visual observation

- None requested: the selected transcript anchors support the bounded concept-routing claim; no formula, chart, code screen, or visual-only assertion is used.

## Inference

- The selector places this source in `optimization_training` as `CORROBORATING`. This is a bounded source-set relation, not a formal mentor rule.

## Unknowns and limits

- The packet does not establish a universal architecture, algorithm, or performance conclusion.
- Selected chunks may omit counterexamples, task conditions, and empirical comparisons elsewhere in the video.

## De-duplication and cross-source relation

- Other selected sources for this concept: `1UqCjFQiiy0` (PRIMARY), `yKKNr-QKz2Q` (PRIMARY), `e03YKGHXnL8` (CORROBORATING).
- Cross-source synthesis is deferred to the concept dossier; duplicate or supporting sources remain in the coverage ledger rather than being re-distilled.
