# Evidence Packet: N6aRv06iv2g / Transformer／attention／sequence representation

- packet_id: `EVP-CHANNEL-N6aRv06iv2g-sequence_attention_transformer-V1`
- packet_schema: `hung-yi-channel-evidence-packet.v1`
- packet_type: `EVIDENCE_PACKET_READY`
- video_id: `N6aRv06iv2g`
- source_url: https://www.youtube.com/watch?v=N6aRv06iv2g
- title: `【機器學習2021】Transformer (下)`
- transcript_type: `official`
- source_quality: `OFFICIAL`
- manifest_status: `VERIFIED`
- concept_id: `sequence_attention_transformer`
- source_role: `CORROBORATING`
- source_scope: selective review of selector-approved transcript chunks; not full-video coverage and not a claim of full-video understanding

## Direct evidence

1. `N6aRv06iv2g:251-295` (`00:08:50.890–00:10:19.610`): Direct transcript evidence. 先無視這個問題 繼續走下去 好 那我們 來看一下這個 Decoder 啊 它內部的結構長什麼樣子 那我們這邊呢 把 Encoder 的部分先暫時省略掉 那在 Transformer 裡面 Decoder 的結構呢 長得是這個樣子的 看起來有點複雜 比 Encoder 還稍微複雜一點 那我們現在先把 Encoder 跟 Decoder 放在一起 稍微比較一下它們之間的差異 那你會發現說 如果我們把 Decoder 中間這一塊 中間這一塊把它蓋起來 其實 Encoder 跟 Decoder 並沒有那麼大的差別 你看 Encoder 這邊 Multi-Head Attention 然後 Add & Norm Feed Forward Add & Norm 重複 N 次 Decoder 其實也是一樣 當我們把中間這一塊遮起來以後 我們等一下再講 遮起來這一塊裡面做了什麼事 但當我們把中間這塊遮起來以後 欸 那 Decoder 也是 有…
2. `N6aRv06iv2g:296-335` (`00:10:19.610–00:11:48.040`): Direct transcript evidence. Multi-Head Attention 這一個 Block 上面 還加了一個 Masked 這個 Masked 是什麼意思呢 這個 Masked 的意思是這樣子的 這是我們原來的 Self-Attention Input 一排 Vector Output 另外一排 Vector 這一排 Vector 每一個輸出 都要看過完整的 Input 以後 才做決定 所以輸出 b1 的時候 其實是根據 a1 到 a4 所有的資訊 去輸出 b1 當我們把 Self-Attention 轉成 Masked Attention 的時候 它的不同點在哪裡呢 它的不同點是 現在我們不能再看右邊的部分 也就是產生 b1 的時候 我們只能考慮 a1 的資訊 你不能夠再考慮 a2 a3 a4 產生 b2 的時候 你只能考慮 a1 a2 的資訊 不能再考慮 a3 a4 的資訊 產生 b3 的時候 你就不能考慮 a4 的資訊 產生 b4 的時候 你可以用整…

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

- Other selected sources for this concept: `Ll-wk8x3G_g` (PRIMARY), `vXb2QYOUzl4` (PRIMARY), `gmsMY5kc-zw` (CORROBORATING).
- Cross-source synthesis is deferred to the concept dossier; duplicate or supporting sources remain in the coverage ledger rather than being re-distilled.
