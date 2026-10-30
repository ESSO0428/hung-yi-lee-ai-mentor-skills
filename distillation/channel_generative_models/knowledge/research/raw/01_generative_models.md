# Research Dossier: generative modeling

## Source Metadata

- Source: `OYN_GvAqv-A` — 【生成式AI導論 2024】第18講：有關影像的生成式AI (下) — 快速導讀經典影像生成方法 (VAE, Flow, Diffusion, GAN) 以及與生成的影片互動
- URL: https://www.youtube.com/watch?v=OYN_GvAqv-A
- Source role: `PRIMARY`
- Source weight: 1
- Evidence packet: `EVP-CHANNEL-OYN_GvAqv-A-generative_models-V1` (data/processing/channel_evidence_packets_v1/OYN_GvAqv-A--generative_models.md)
- Transcript type: `official`; selector confidence: `HIGH`
- Source: `DQNNMiAP5lw` — GAN Lecture 1 (2018): Introduction
- URL: https://www.youtube.com/watch?v=DQNNMiAP5lw
- Source role: `PRIMARY`
- Source weight: 1
- Evidence packet: `EVP-CHANNEL-DQNNMiAP5lw-generative_models-V1` (data/processing/channel_evidence_packets_v1/DQNNMiAP5lw--generative_models.md)
- Transcript type: `official`; selector confidence: `HIGH`
- Source: `DMA4MrNieWo` — GAN Lecture 4 (2018): Basic Theory
- URL: https://www.youtube.com/watch?v=DMA4MrNieWo
- Source role: `CORROBORATING`
- Source weight: 2
- Evidence packet: `EVP-CHANNEL-DMA4MrNieWo-generative_models-V1` (data/processing/channel_evidence_packets_v1/DMA4MrNieWo--generative_models.md)
- Transcript type: `official`; selector confidence: `HIGH`
- Source: `JbfcAaBT66U` — 【生成式AI】Stable Diffusion、DALL-E、Imagen 背後共同的套路
- URL: https://www.youtube.com/watch?v=JbfcAaBT66U
- Source role: `CORROBORATING`
- Source weight: 2
- Evidence packet: `EVP-CHANNEL-JbfcAaBT66U-generative_models-V1` (data/processing/channel_evidence_packets_v1/JbfcAaBT66U--generative_models.md)
- Transcript type: `official`; selector confidence: `HIGH`

## Evidence

- `OYN_GvAqv-A` (PRIMARY):
  - `OYN_GvAqv-A:0-26` (`00:00:00.000–00:01:29.080`): 接下來的下一段呢,我想跟大家介紹一下一些經典的影像生成的方法 那這邊會跟大家很快提到的方法,包括 Variational Autoencoder 它的所寫是 VAE Flow-Based Model 還有今天大家都耳熟能詳的 Diffusion Model 還有 Generative Adversarial Network,它的所寫是 GAN 那像 Sora 呢,他用的就是 Diffusion Model 如果你在論文或Blog裡面看到有一個東西 是從一大堆的雜訊慢慢生出來的 本來很多雜訊 越來越少 最後產生高清的圖的話 那這個通常指的就是Diffusion的Model 那我想用一點時間來介紹這些經典的影像生成的方法 雖然今天Diffusion Model可能是最常用的 但是我們可以多介紹幾個經典的方法 讓你知道說到底影像生成真正的難點 真正被克服的挑戰是什麼 那我們剛才已經講到 我們在生圖片的時候或生影像的時候 今天常常用的…
  - `OYN_GvAqv-A:64-99` (`00:02:57.580–00:04:23.300`): 不知道要聽哪一筆訓練資料的 所以怎麼辦呢 我們現在先把那個影像圖片生成的模型簡化一下啦 我這邊就直接用個框框呢 來代表那個Transformer 那大家知道我的意思 就這個框框裡面其實是一個Transformer 那給他一段文字 還要生一堆Patch出來 這些Patch會變成圖 好 那我們剛才說圖片生成或者是影像生成問題也是一樣的 他的難點就是這些文字往往沒辦法完整的描述影像 那怎麼辦呢 也許一個可能性是 雖然我們本來的訓練資料裡面這些文字不足以完整的描述影像 但我們自己把本來文字沒提到的東西加進去 我們直接把多餘的資訊加進去 都跟圖片生成模型講說 你現在不只要生成一隻奔跑的狗 你是要生成一隻哈士奇在草原上奔跑的樣子 你不是隻生成一隻狗 你要生成柴犬在都市裡奔跑的樣子 把額外的原來文字沒提到的資訊 把它標出來 也提供給圖片生成模型 這樣圖片生成模型在生成的時候 他就知道說 為什麼同樣的輸入 這兩隻圖片會不一樣 因為有額外的資訊…
  - `OYN_GvAqv-A:437-461` (`00:19:06.080–00:20:34.120`): 你就是有一堆的 Transformer 在這個影片生成的過程中 你就是會不斷的做 Denoise 那這個 Denoise 是由一個 Transformer 的模型完成的 它的輸入就是有雜訊的 patch,輸出就是比較乾淨的 patch 這個 Transformer 會做好幾百次、好幾千次的去照之後 期待最後產生一堆乾淨的 patch 那這些乾淨的 patch 就可以被還原為影像 這個就是今天用 Diffusion Model 加上 Transformer 生一片的模型 那根據 Sora 的 blog 他們很有可能也就使用類似的技術來產生一片的 好,那我們現在講了Diffusion的model 跟剛才的VAE還有Flow-based model要怎麼來類比呢? 剛才的VAE跟Flow-based model都有一個Encoder跟一個Decoder 對於Diffusion model來說,它也有一個Decoder 它Decode…
  - `OYN_GvAqv-A:852-858` (`00:36:46.260–00:36:59.580`): 但是有這樣子影像生成模型 你又可以跟它互動 那也許未來 你就可以在一個開放世界裡開車 你就可以一直往前開 然後畫面都會一直出現,永遠都不會停這樣 就以後這個世界可能就可以變成這個樣子
- `DQNNMiAP5lw` (PRIMARY):
  - `DQNNMiAP5lw:0-4` (`00:00:00.240–00:00:27.860`): 臺灣大學人工智慧中心 科技部人工智慧技術暨全幅健康照護聯合研究中心 http://aintu.tw 各位同學大家好，今天要講 Generative Adversarial Network，縮寫是 GAN，就是 GAN 一開始要做的第一件事情是 要先知道 GAN 要怎麼正確的發音 所以就用 Google 小姐來唸一下 GAN 是怎麼發音的
  - `DQNNMiAP5lw:7-29` (`00:00:49.600–00:02:19.120`): 今天就要來講這個技術 首先先說一些抬轎的話，讓你知道這個技術有甚麼重要性 有一個人在 Quora 這個論壇上問 最近在 Unsupervised Learning 的領域 有甚麼樣的 breakthrough 然後 Yann LeCun 就親自來回答了 他說 Adversarial Training，今天要講的 GAN 的技術 是 the coolest thing since sliced bread 是甚麼意思 這邊可以學到一個新的英文片語 since sliced bread 翻成中文的話可以翻成 有史以來 的意思 google 了一下，因為在過去 在賣吐司麵包的時候 是沒有切片的 所以家庭主婦買這個吐司麵包回去的時候要自己切片覺得很麻煩 後來有人就發明了切片的吐司，大家就覺得很高興 有一個好東西問世的時候 就會說 since sliced bread 可以翻譯成有史以來的意思 所以他說 GAN 這個技術是有史以來他覺得…
  - `DQNNMiAP5lw:30-52` (`00:02:19.200–00:03:46.700`): 所以 Yann LeCun 他給 GAN 這個技術非常高的評價 在網路可以找到 GAN 的動物園 就直接 google GAN 加上 zoo GAN、動物園就可以找到各式各樣相關的技術 因為現在如果發明了一個新的跟 GAN 有關的技術 你就會在 GAN 前面加一些英文的字 可是英文的字母只有 26 個 所以很快的名字就通通被用盡了 這個名字通通都撞在一起 比如說有兩個 LSGAN 一個是 Least Sqaure GAN 一個是 Loss Sensitive GAN 完全是不一樣的東西但因為英文字母是有限的 很快的名字就都被用盡了 這個圖是甚麼？這個圖是講說 這個 GAN 的動物園裡面 收錄了各種有名有姓的 GAN 你可以自己去查查看，裡面光 SGAN 就有四個以上 它就統計了一下，到目前為止 已經有接近三百種不同的 GAN 了 因為英文字母是有限的所以會發生這樣的情形 這邊是 Variational Approaches f…
  - `DQNNMiAP5lw:1361-1369` (`01:32:18.880–01:33:14.240`): 會發現 VAE 相較於 GAN 還是輸了一截的 剩下還有一些投影片但我覺得下次再講好了 今天講的是一些直觀的東西 下一堂課開始就是要講一些有數學的、比較理論的東西 如果可以的話你先去預習一下 我把之前上課了錄影放在這邊 因為是比較困難的問題所以建議你先預習一下 等一下助教也會提到一些新的技術 今天這個課沒有 cover 的技術但都是未來會講到的 你聽到這些新的技術的話也不用太驚慌 作業 3-1 不用到那些新的技術應該也是可以過得了 baseline 臺灣大學人工智慧中心 科技部人工智慧技術暨全幅健康照護聯合研究中心 http://aintu.tw
- `DMA4MrNieWo` (CORROBORATING):
  - `DMA4MrNieWo:0-7` (`00:00:00.000–00:00:39.440`): 臺灣大學人工智慧中心 科技部人工智慧技術暨全幅健康照護聯合研究中心http://ai.ntu.edu.tw/ 各位同學大家好 我們就來上課吧 上週我們講了 GAN 的直觀的想法 今天要來講 GAN 背後的理論 今天要講的是當初 2014 年 Ian Goodfellow 在 propose GAN 的時候它的講法 等一下可以仔細聽看看跟我們上週講的 GAN 的直觀的想法裡面有沒有矛盾的地方 其實是有一些地方還頗矛盾的 至今仍然沒有好的 solution、好的手法可以解決
  - `DMA4MrNieWo:8-14` (`00:00:55.680–00:01:35.440`): 如果大家沒有甚麼問題要問的話就來講一下 GAN 背後的理論，當初 Ian Goodfellow 是怎麼說的 這個是上周說的作業 3-1 裡面要讓 GAN 做的事情 讓機器看了很多動畫的圖以後 自己產生二次元人物的頭像 GAN 要做的就是根據很多 example 自己去進行生成 所謂的生成到底是甚麼樣的問題 假設要生成的東西是 image 用 x 來代表一張 image
  - `DMA4MrNieWo:36-57` (`00:03:05.620–00:04:32.280`): 在藍色的區域以外，它的機率是低的 要機器做的是甚麼 要機器找出這個 distribution 而這個 distribution 到底長甚麼樣子 實際上是不知道的 可以蒐集很多的 x 知道 x 可能在某些地方分布比較高 但是要我們把這個式子找出來 我們是不知道要怎麼做的 所以現在 GAN 做的是一個 generative model 做的事情 就是要找出這個 distribution 在有 GAN 之前怎麼做 generative 是用 Maximum Likelihood Estimation 其實 Maximum Likelihood Estimation 在之前 Machine Learning 有講過，這邊只是一個很快地複習 現在有一個 data 的 distribution 它是 P data ( x ) 這個 distribution 長甚麼樣子 就是這個 distribution 它的 formulation 長甚…
  - `DMA4MrNieWo:1098-1115` (`01:18:57.540–01:20:18.200`): 不過在文獻上我看到有人在 train GAN 的時候他有一招 每次 train 的時候他不只拿現在的 generator 去 sample data 他也會拿過去的 generator 也 sample data 然後把這些各個不同 generator sample 的 data 通通集合起來 再去 train discriminator 可以得到的 performance 會是比較好的 如果 discriminator 是在 evaluate 現在的 generator 跟 data distribution 的差異的話 好像做這件事情也沒有太大的意義 因為現在量 generator 跟 data 之間的差異 拿過去 generator 產生的東西 有甚麼用，沒什麼用 為甚麼要這麼做，但是 在實作上發現拿過去 generator 產生的東西 再去訓練 discriminator 是可以得到比較好的成果 所以這樣看起來，也許這…
- `JbfcAaBT66U` (CORROBORATING):
  - `JbfcAaBT66U:0-24` (`00:00:00.000–00:01:29.500`): 好,那我們來講一下今天鼎鼎大名的Stable Diffusion吧 那其實今天比較好的影像生成的模型 就算它不是Stable Diffusion 它的套路其實也跟Stable Diffusion差不多 所以我們今天就是要來介紹這個 今天最好的State of the Art的影像生成模型 它背後的套路長什麼樣子 今天最好的影像生成模型 基本上它內部就是有三個元件 第一個元件是一個text的encoder 是一個好的文字的encoder 會把一段文字的敘述把它變成一個一個的向量 然後接下來你會有一個generation的model 那今天大家都用Diffusion model 但用別的也是可以的 這個generation的model就是吃一個雜訊 我這邊用這個粉紅色的向量 帶粉紅色的矩陣代表輸入的雜訊 輸入雜訊跟文字的encoder產生一個中間產物 這個中間產物等一下再細講 它可以是一個人看得懂的 只是比較小的比較模糊的圖片 它…
  - `JbfcAaBT66U:25-53` (`00:01:29.500–00:02:59.500`): 從文字encoder的輸出產生一個中間產物 代表圖片被壓縮以後的版本 接下來直接套一個decoder 這個decoder的作用是從壓縮後的版本還原回原始 我們剛才講說就是有三個模組 一個文字的encoder 一個生成的模型 今天用diffusion model 還有一個decoder直接從生成模型輸出的圖片的壓縮版本 還原回原來的圖片 通常三個模組是分開訓練 然後再把它組合起來的 今天你看到的比較好的文字生影像的模型 都是差不多的套路 比如說這是Stable Diffusion論文裡面的一張圖 你就看到它先有一個encoder可以處理輸入的東西 但它輸入不是只有文字啦 它還有別的可能的輸入 但是反正輸入文字你需要一個encoder來處理它 然後你需要有一個生成的模型 那這邊Stable Diffusion內部當然用的就是Diffusion的model 那你需要有一個decoder 把Diffusion model生出來的中間產…
  - `JbfcAaBT66U:54-86` (`00:02:59.500–00:04:26.500`): 接下來你要有一個生成的模型 那其實在DARLIE裡面它是有兩個生成的模型 你可以用Auto Regressive的model 因為今天已經先做了一些處理以後 現在你要產生的並不是一張完整的圖片 如果你要生成完整的圖片的話 Auto Regressive的model運算量太大了 但是如果生成的只是一個圖片的壓縮的版本 也許用Auto Regressive的方法還可以 所以可以用Auto Regressive 也可以用Diffusion model 生成圖片壓縮的版本 用個decoder還原回原來的圖片 這是DARLIE系列的做法 Google也有一個影像生成的模型叫Imagen 也是吃文字 吃一段文字的敘述 產生一張圖片 這個套路也是一樣的 先有一個好的文字的encoder 然後你要有一個影像生成的模型 從文字去生出圖片壓縮後的版本 那在Imagen裡面它生出來的東西 就是人看得懂的東西 它生成出來的東西就是一張比較小的圖片 最…
  - `JbfcAaBT66U:449-461` (`00:19:20.500–00:19:46.500`): 它就把這些中間產生出來的 Latent Representation 丟給Decoder 然後再產生出來的結果給你看 好 那這個就是今天 StaleDR的文字生影像的framework 就是三個步驟 文字的Encoder 一個Image的Generation的Model 生個中間產物出來 Decoder再做最後的處理 你會發現最好的影像生成模型 基本上都是這樣子的套路

## Patterns and Repeated Themes

- 多個獨立來源均提供 `generative_models` 的 selector-approved transcript anchors；可把它們用於受限的 cross-source candidate synthesis。

## Contradictions

- 來源跨年份、模態與任務；它們的共同概念不等於共同的 benchmark、資料分布或性能結論。

## Inferences

- Candidate inference (not formal): 生成模型 recipe 的比較必須把目標條件、生成品質、可控性、推論成本與訓練穩定性拆開；GAN、VAE、flow 與 diffusion 不能只用單一視覺示例決策。
- Candidate decision rule: 先定義資料模態與 conditional requirement，再建立可重現基線；同時報告生成品質、diversity／failure cases、成本和人為挑選規則，並對照相同資料與 evaluation protocol。

## Gaps and Missing Information

- 未使用未選定的片段、影格或投影片；若未來某個結論需要公式、圖表或程式畫面，必須建立獨立 visual-evidence request。
- 本 dossier 是 Distilly research input，不取代原始影片、source chunks 或 evidence packets。
