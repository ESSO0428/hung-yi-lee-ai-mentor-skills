# Evidence Packet: DMA4MrNieWo / generative modeling

- packet_id: `EVP-CHANNEL-DMA4MrNieWo-generative_models-V1`
- packet_schema: `hung-yi-channel-evidence-packet.v1`
- packet_type: `EVIDENCE_PACKET_READY`
- video_id: `DMA4MrNieWo`
- source_url: https://www.youtube.com/watch?v=DMA4MrNieWo
- title: `GAN Lecture 4 (2018): Basic Theory`
- transcript_type: `official`
- source_quality: `OFFICIAL`
- manifest_status: `VERIFIED`
- concept_id: `generative_models`
- source_role: `CORROBORATING`
- source_scope: selective review of selector-approved transcript chunks; not full-video coverage and not a claim of full-video understanding

## Direct evidence

1. `DMA4MrNieWo:0-7` (`00:00:00.000–00:00:39.440`): Direct transcript evidence. 臺灣大學人工智慧中心 科技部人工智慧技術暨全幅健康照護聯合研究中心http://ai.ntu.edu.tw/ 各位同學大家好 我們就來上課吧 上週我們講了 GAN 的直觀的想法 今天要來講 GAN 背後的理論 今天要講的是當初 2014 年 Ian Goodfellow 在 propose GAN 的時候它的講法 等一下可以仔細聽看看跟我們上週講的 GAN 的直觀的想法裡面有沒有矛盾的地方 其實是有一些地方還頗矛盾的 至今仍然沒有好的 solution、好的手法可以解決
2. `DMA4MrNieWo:8-14` (`00:00:55.680–00:01:35.440`): Direct transcript evidence. 如果大家沒有甚麼問題要問的話就來講一下 GAN 背後的理論，當初 Ian Goodfellow 是怎麼說的 這個是上周說的作業 3-1 裡面要讓 GAN 做的事情 讓機器看了很多動畫的圖以後 自己產生二次元人物的頭像 GAN 要做的就是根據很多 example 自己去進行生成 所謂的生成到底是甚麼樣的問題 假設要生成的東西是 image 用 x 來代表一張 image
3. `DMA4MrNieWo:36-57` (`00:03:05.620–00:04:32.280`): Direct transcript evidence. 在藍色的區域以外，它的機率是低的 要機器做的是甚麼 要機器找出這個 distribution 而這個 distribution 到底長甚麼樣子 實際上是不知道的 可以蒐集很多的 x 知道 x 可能在某些地方分布比較高 但是要我們把這個式子找出來 我們是不知道要怎麼做的 所以現在 GAN 做的是一個 generative model 做的事情 就是要找出這個 distribution 在有 GAN 之前怎麼做 generative 是用 Maximum Likelihood Estimation 其實 Maximum Likelihood Estimation 在之前 Machine Learning 有講過，這邊只是一個很快地複習 現在有一個 data 的 distribution 它是 P data ( x ) 這個 distribution 長甚麼樣子 就是這個 distribution 它的 formulation 長甚…
4. `DMA4MrNieWo:1098-1115` (`01:18:57.540–01:20:18.200`): Direct transcript evidence. 不過在文獻上我看到有人在 train GAN 的時候他有一招 每次 train 的時候他不只拿現在的 generator 去 sample data 他也會拿過去的 generator 也 sample data 然後把這些各個不同 generator sample 的 data 通通集合起來 再去 train discriminator 可以得到的 performance 會是比較好的 如果 discriminator 是在 evaluate 現在的 generator 跟 data distribution 的差異的話 好像做這件事情也沒有太大的意義 因為現在量 generator 跟 data 之間的差異 拿過去 generator 產生的東西 有甚麼用，沒什麼用 為甚麼要這麼做，但是 在實作上發現拿過去 generator 產生的東西 再去訓練 discriminator 是可以得到比較好的成果 所以這樣看起來，也許這…

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

- Other selected sources for this concept: `OYN_GvAqv-A` (PRIMARY), `DQNNMiAP5lw` (PRIMARY), `JbfcAaBT66U` (CORROBORATING).
- Cross-source synthesis is deferred to the concept dossier; duplicate or supporting sources remain in the coverage ledger rather than being re-distilled.
