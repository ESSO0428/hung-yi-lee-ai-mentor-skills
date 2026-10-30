# Evidence Packet: JbfcAaBT66U / generative modeling

- packet_id: `EVP-CHANNEL-JbfcAaBT66U-generative_models-V1`
- packet_schema: `hung-yi-channel-evidence-packet.v1`
- packet_type: `EVIDENCE_PACKET_READY`
- video_id: `JbfcAaBT66U`
- source_url: https://www.youtube.com/watch?v=JbfcAaBT66U
- title: `【生成式AI】Stable Diffusion、DALL-E、Imagen 背後共同的套路`
- transcript_type: `official`
- source_quality: `OFFICIAL`
- manifest_status: `VERIFIED`
- concept_id: `generative_models`
- source_role: `CORROBORATING`
- source_scope: selective review of selector-approved transcript chunks; not full-video coverage and not a claim of full-video understanding

## Direct evidence

1. `JbfcAaBT66U:0-24` (`00:00:00.000–00:01:29.500`): Direct transcript evidence. 好,那我們來講一下今天鼎鼎大名的Stable Diffusion吧 那其實今天比較好的影像生成的模型 就算它不是Stable Diffusion 它的套路其實也跟Stable Diffusion差不多 所以我們今天就是要來介紹這個 今天最好的State of the Art的影像生成模型 它背後的套路長什麼樣子 今天最好的影像生成模型 基本上它內部就是有三個元件 第一個元件是一個text的encoder 是一個好的文字的encoder 會把一段文字的敘述把它變成一個一個的向量 然後接下來你會有一個generation的model 那今天大家都用Diffusion model 但用別的也是可以的 這個generation的model就是吃一個雜訊 我這邊用這個粉紅色的向量 帶粉紅色的矩陣代表輸入的雜訊 輸入雜訊跟文字的encoder產生一個中間產物 這個中間產物等一下再細講 它可以是一個人看得懂的 只是比較小的比較模糊的圖片 它…
2. `JbfcAaBT66U:25-53` (`00:01:29.500–00:02:59.500`): Direct transcript evidence. 從文字encoder的輸出產生一個中間產物 代表圖片被壓縮以後的版本 接下來直接套一個decoder 這個decoder的作用是從壓縮後的版本還原回原始 我們剛才講說就是有三個模組 一個文字的encoder 一個生成的模型 今天用diffusion model 還有一個decoder直接從生成模型輸出的圖片的壓縮版本 還原回原來的圖片 通常三個模組是分開訓練 然後再把它組合起來的 今天你看到的比較好的文字生影像的模型 都是差不多的套路 比如說這是Stable Diffusion論文裡面的一張圖 你就看到它先有一個encoder可以處理輸入的東西 但它輸入不是只有文字啦 它還有別的可能的輸入 但是反正輸入文字你需要一個encoder來處理它 然後你需要有一個生成的模型 那這邊Stable Diffusion內部當然用的就是Diffusion的model 那你需要有一個decoder 把Diffusion model生出來的中間產…
3. `JbfcAaBT66U:54-86` (`00:02:59.500–00:04:26.500`): Direct transcript evidence. 接下來你要有一個生成的模型 那其實在DARLIE裡面它是有兩個生成的模型 你可以用Auto Regressive的model 因為今天已經先做了一些處理以後 現在你要產生的並不是一張完整的圖片 如果你要生成完整的圖片的話 Auto Regressive的model運算量太大了 但是如果生成的只是一個圖片的壓縮的版本 也許用Auto Regressive的方法還可以 所以可以用Auto Regressive 也可以用Diffusion model 生成圖片壓縮的版本 用個decoder還原回原來的圖片 這是DARLIE系列的做法 Google也有一個影像生成的模型叫Imagen 也是吃文字 吃一段文字的敘述 產生一張圖片 這個套路也是一樣的 先有一個好的文字的encoder 然後你要有一個影像生成的模型 從文字去生出圖片壓縮後的版本 那在Imagen裡面它生出來的東西 就是人看得懂的東西 它生成出來的東西就是一張比較小的圖片 最…
4. `JbfcAaBT66U:449-461` (`00:19:20.500–00:19:46.500`): Direct transcript evidence. 它就把這些中間產生出來的 Latent Representation 丟給Decoder 然後再產生出來的結果給你看 好 那這個就是今天 StaleDR的文字生影像的framework 就是三個步驟 文字的Encoder 一個Image的Generation的Model 生個中間產物出來 Decoder再做最後的處理 你會發現最好的影像生成模型 基本上都是這樣子的套路

## ASR observation

- None: selected evidence is from a verified official/auto transcript, not ASR output.

## Visual observation

- None requested: the selected transcript anchors support the bounded concept-routing claim; no formula, chart, code screen, or visual-only assertion is used.

## Inference

- The selector places this source in `generative_models` as `CORROBORATING`. This is a bounded source-set relation, not a formal mentor rule.

## Unknowns and limits

- The packet does not establish a universal architecture, algorithm, or performance conclusion.
- Selected chunks may omit counterexamples, task conditions, and empirical comparisons elsewhere in the video.

## De-duplication and cross-source relation

- Other selected sources for this concept: `OYN_GvAqv-A` (PRIMARY), `DQNNMiAP5lw` (PRIMARY), `DMA4MrNieWo` (CORROBORATING).
- Cross-source synthesis is deferred to the concept dossier; duplicate or supporting sources remain in the coverage ledger rather than being re-distilled.
