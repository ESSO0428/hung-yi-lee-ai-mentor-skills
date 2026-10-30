# Evidence Packet: OYN_GvAqv-A / generative modeling

- packet_id: `EVP-CHANNEL-OYN_GvAqv-A-generative_models-V1`
- packet_schema: `hung-yi-channel-evidence-packet.v1`
- packet_type: `EVIDENCE_PACKET_READY`
- video_id: `OYN_GvAqv-A`
- source_url: https://www.youtube.com/watch?v=OYN_GvAqv-A
- title: `【生成式AI導論 2024】第18講：有關影像的生成式AI (下) — 快速導讀經典影像生成方法 (VAE, Flow, Diffusion, GAN) 以及與生成的影片互動`
- transcript_type: `official`
- source_quality: `OFFICIAL`
- manifest_status: `VERIFIED`
- concept_id: `generative_models`
- source_role: `PRIMARY`
- source_scope: selective review of selector-approved transcript chunks; not full-video coverage and not a claim of full-video understanding

## Direct evidence

1. `OYN_GvAqv-A:0-26` (`00:00:00.000–00:01:29.080`): Direct transcript evidence. 接下來的下一段呢,我想跟大家介紹一下一些經典的影像生成的方法 那這邊會跟大家很快提到的方法,包括 Variational Autoencoder 它的所寫是 VAE Flow-Based Model 還有今天大家都耳熟能詳的 Diffusion Model 還有 Generative Adversarial Network,它的所寫是 GAN 那像 Sora 呢,他用的就是 Diffusion Model 如果你在論文或Blog裡面看到有一個東西 是從一大堆的雜訊慢慢生出來的 本來很多雜訊 越來越少 最後產生高清的圖的話 那這個通常指的就是Diffusion的Model 那我想用一點時間來介紹這些經典的影像生成的方法 雖然今天Diffusion Model可能是最常用的 但是我們可以多介紹幾個經典的方法 讓你知道說到底影像生成真正的難點 真正被克服的挑戰是什麼 那我們剛才已經講到 我們在生圖片的時候或生影像的時候 今天常常用的…
2. `OYN_GvAqv-A:64-99` (`00:02:57.580–00:04:23.300`): Direct transcript evidence. 不知道要聽哪一筆訓練資料的 所以怎麼辦呢 我們現在先把那個影像圖片生成的模型簡化一下啦 我這邊就直接用個框框呢 來代表那個Transformer 那大家知道我的意思 就這個框框裡面其實是一個Transformer 那給他一段文字 還要生一堆Patch出來 這些Patch會變成圖 好 那我們剛才說圖片生成或者是影像生成問題也是一樣的 他的難點就是這些文字往往沒辦法完整的描述影像 那怎麼辦呢 也許一個可能性是 雖然我們本來的訓練資料裡面這些文字不足以完整的描述影像 但我們自己把本來文字沒提到的東西加進去 我們直接把多餘的資訊加進去 都跟圖片生成模型講說 你現在不只要生成一隻奔跑的狗 你是要生成一隻哈士奇在草原上奔跑的樣子 你不是隻生成一隻狗 你要生成柴犬在都市裡奔跑的樣子 把額外的原來文字沒提到的資訊 把它標出來 也提供給圖片生成模型 這樣圖片生成模型在生成的時候 他就知道說 為什麼同樣的輸入 這兩隻圖片會不一樣 因為有額外的資訊…
3. `OYN_GvAqv-A:437-461` (`00:19:06.080–00:20:34.120`): Direct transcript evidence. 你就是有一堆的 Transformer 在這個影片生成的過程中 你就是會不斷的做 Denoise 那這個 Denoise 是由一個 Transformer 的模型完成的 它的輸入就是有雜訊的 patch,輸出就是比較乾淨的 patch 這個 Transformer 會做好幾百次、好幾千次的去照之後 期待最後產生一堆乾淨的 patch 那這些乾淨的 patch 就可以被還原為影像 這個就是今天用 Diffusion Model 加上 Transformer 生一片的模型 那根據 Sora 的 blog 他們很有可能也就使用類似的技術來產生一片的 好,那我們現在講了Diffusion的model 跟剛才的VAE還有Flow-based model要怎麼來類比呢? 剛才的VAE跟Flow-based model都有一個Encoder跟一個Decoder 對於Diffusion model來說,它也有一個Decoder 它Decode…
4. `OYN_GvAqv-A:852-858` (`00:36:46.260–00:36:59.580`): Direct transcript evidence. 但是有這樣子影像生成模型 你又可以跟它互動 那也許未來 你就可以在一個開放世界裡開車 你就可以一直往前開 然後畫面都會一直出現,永遠都不會停這樣 就以後這個世界可能就可以變成這個樣子

## ASR observation

- None: selected evidence is from a verified official/auto transcript, not ASR output.

## Visual observation

- None requested: the selected transcript anchors support the bounded concept-routing claim; no formula, chart, code screen, or visual-only assertion is used.

## Inference

- The selector places this source in `generative_models` as `PRIMARY`. This is a bounded source-set relation, not a formal mentor rule.

## Unknowns and limits

- The packet does not establish a universal architecture, algorithm, or performance conclusion.
- Selected chunks may omit counterexamples, task conditions, and empirical comparisons elsewhere in the video.

## De-duplication and cross-source relation

- Other selected sources for this concept: `DQNNMiAP5lw` (PRIMARY), `DMA4MrNieWo` (CORROBORATING), `JbfcAaBT66U` (CORROBORATING).
- Cross-source synthesis is deferred to the concept dossier; duplicate or supporting sources remain in the coverage ledger rather than being re-distilled.
