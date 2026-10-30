# Evidence Packet: gmsMY5kc-zw / Transformer／attention／sequence representation

- packet_id: `EVP-CHANNEL-gmsMY5kc-zw-sequence_attention_transformer-V1`
- packet_schema: `hung-yi-channel-evidence-packet.v1`
- packet_type: `EVIDENCE_PACKET_READY`
- video_id: `gmsMY5kc-zw`
- source_url: https://www.youtube.com/watch?v=gmsMY5kc-zw
- title: `【機器學習2021】自注意力機制 (Self-attention) (下)`
- transcript_type: `official`
- source_quality: `OFFICIAL`
- manifest_status: `VERIFIED`
- concept_id: `sequence_attention_transformer`
- source_role: `CORROBORATING`
- source_scope: selective review of selector-approved transcript chunks; not full-video coverage and not a claim of full-video understanding

## Direct evidence

1. `gmsMY5kc-zw:70-103` (`00:03:28.080–00:04:57.490`): Direct transcript evidence. 那接下來我們從矩陣乘法的角度 再重新講一次我們剛才講的 Self-attention 是怎麼運作的 好 那 Self-attention 是怎麼運作的呢 我們現在已經知道說 a1 到 a4 它們每一個 a 都要分別產生 q k v 所以 a1 要產生 q1 k1 v1 a2 要產生 q2 k2 v2 以此類推 每一個 a 都產生 q k v 如果要用矩陣運算表示這個操作的話 是什麼樣子呢 我們每一個 a i 都乘上 q 這個 都乘上一個矩陣 我們這邊用 wq 來表示它 得到 qi 每一個 a 都要乘上 wq 得到 qi 那這些不同的 a 你可以把它合起來 當作一個矩陣來看待 什麼意思呢 a1 乘上 wq 得到 q1 a2 也乘上 wq 得到 q2 一樣 a3 a4 也都乘上 wq 得到 q3 跟 q4 那你可以把 a1 到 a4 拼起來 看作是一個矩陣 這個矩陣我們用 I 來表示 這邊這個 I 這個大寫的字母 I 它代表的是一…
2. `gmsMY5kc-zw:104-142` (`00:04:57.490–00:06:26.010`): Direct transcript evidence. 我們用 Q 來表示它 這個 Q 就是 q1 到 q4 你把 q1 到 q4 這四個 vector 拼起來 就是 Q 的四個 column 所以我們從 a1 到 a4 得到 q1 到 q4 這一件事情 這個操作 其實就是把一個叫做 I 的矩陣 I 這個矩陣 它裡面的 column 就是我們 Self-attention 的 input a1 到 a4 把 I 這個矩陣 乘上另外一個矩陣 wq 那 wq 其實是 network 的參數 它是等一下會被認出來的 把 I 乘上 wq 得到 Q 這個 Q 的四個 column 就是 q1 到 q4 那接下來怎麼產生 k 跟 v 呢 它的操作跟 q 是一模一樣的 我們就不要再細講 免得你覺得很無聊 所以 a 乘上 wk 就會得到這個 key 就會得到這個 k 這個 vector 那我們把這個 input 的四個 vector a1 到 a4 拼起來 當作是一個矩陣 叫做 I 把 I 乘上一…

## ASR observation

- None: selected evidence is from a verified official/auto transcript, not ASR output.

## Visual observation

- None requested: the selected transcript anchors support the bounded concept-routing claim; no formula, chart, code screen, or visual-only assertion is used.

## Inference

- The selector places this source in `sequence_attention_transformer` as `CORROBORATING`. This is a bounded source-set relation, not a formal mentor rule.

## Unknowns and limits

- The packet does not establish a universal architecture, algorithm, or performance conclusion.
- Selected chunks may omit counterexamples, task conditions, and empirical comparisons elsewhere in the video.

## De-duplication and cross-source relation

- Other selected sources for this concept: `Ll-wk8x3G_g` (PRIMARY), `vXb2QYOUzl4` (PRIMARY), `N6aRv06iv2g` (CORROBORATING).
- Cross-source synthesis is deferred to the concept dossier; duplicate or supporting sources remain in the coverage ledger rather than being re-distilled.
