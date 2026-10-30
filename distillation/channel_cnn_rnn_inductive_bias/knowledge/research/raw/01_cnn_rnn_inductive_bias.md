# Research Dossier: CNN／RNN／inductive bias

## Source Metadata

- Source: `lluMBz5AoOg` — [TA 補充課] Transformer and its variant (由助教紀伯翰同學講授)
- URL: https://www.youtube.com/watch?v=lluMBz5AoOg
- Source role: `PRIMARY`
- Source weight: 1
- Evidence packet: `EVP-CHANNEL-lluMBz5AoOg-cnn_rnn_inductive_bias-V1` (data/processing/channel_evidence_packets_v1/lluMBz5AoOg--cnn_rnn_inductive_bias.md)
- Transcript type: `official`; selector confidence: `HIGH`
- Source: `xCGidAeyS4M` — ML Lecture 21-1: Recurrent Neural Network (Part I)
- URL: https://www.youtube.com/watch?v=xCGidAeyS4M
- Source role: `PRIMARY`
- Source weight: 1
- Evidence packet: `EVP-CHANNEL-xCGidAeyS4M-cnn_rnn_inductive_bias-V1` (data/processing/channel_evidence_packets_v1/xCGidAeyS4M--cnn_rnn_inductive_bias.md)
- Transcript type: `official`; selector confidence: `HIGH`
- Source: `gjsdVi90yQo` — 【生成式AI時代下的機器學習(2025)】第四講：Transformer 的時代要結束了嗎？介紹 Transformer 的競爭者們
- URL: https://www.youtube.com/watch?v=gjsdVi90yQo
- Source role: `CORROBORATING`
- Source weight: 2
- Evidence packet: `EVP-CHANNEL-gjsdVi90yQo-cnn_rnn_inductive_bias-V1` (data/processing/channel_evidence_packets_v1/gjsdVi90yQo--cnn_rnn_inductive_bias.md)
- Transcript type: `official`; selector confidence: `MEDIUM`
- Source: `OP5HcXJg2Aw` — 【機器學習2021】卷積神經網路 (Convolutional Neural Networks, CNN)
- URL: https://www.youtube.com/watch?v=OP5HcXJg2Aw
- Source role: `CORROBORATING`
- Source weight: 2
- Evidence packet: `EVP-CHANNEL-OP5HcXJg2Aw-cnn_rnn_inductive_bias-V1` (data/processing/channel_evidence_packets_v1/OP5HcXJg2Aw--cnn_rnn_inductive_bias.md)
- Transcript type: `official`; selector confidence: `HIGH`

## Evidence

- `lluMBz5AoOg` (PRIMARY):
  - `lluMBz5AoOg:1-18` (`00:04:26.700–00:05:55.832`): 我們就開始吧 今天的主題叫做 New Architecture 我是今天的助教紀伯翰 New Architecture 意思上就是新架構 在講新架構之前先來複習一下你們作業裡面會用到的舊架構 Review 就分幾個超級超級簡單的模型 就是 Fully Connected Network、Concolutional Network 跟 Recurrent Neural Network 一開始就快速把這些投影片帶過 你可以發現在現在模型裡，隨處都可以發現 Fully connected network 的影子 這個 layer 的寬度都是自己可以調整，自己去 train 的 再來就是在 CV 領域裡面很常使用到的 Convolutional Neural Network 你可以知道說像這樣的架構裡 這個架構到後來都很受廣用 甚至發展出有很多很多很深很深的模型 像是 ResNet 甚至後來來有用 residual 發展出來的 Den…
  - `lluMBz5AoOg:19-24` (`00:05:55.832–00:06:22.685`): CNN 最好的性質其實是 他可以抓住一些 local 的資訊 這個圖就是想表示說 一個例子在 CNN 是怎麼 process 的 再來就是 Recurrent Neural Network 就是你在做序列型 data 的時候會做的模型
  - `lluMBz5AoOg:25-41` (`00:06:25.729–00:07:52.646`): 簡單來說，舉個例子來說 你希望你的 embedding 可以模擬到句子的句意 你會用一個 LCM 或是一個 GRU 你就會讓 GRU 從 What time is it 的 What 一路把 What time is it 這個字的 token 吃完 你希望最後這個問號得到的 embedding 是有含 有包含到 What time is it 的句意 從這個架構衍伸出來的就像是現在非常流行的 ****** 或是在做 machine translation 的時候 你會做的 Seq2seq 的這種 method 以及像剛剛講 RNN，其實 RNN 有延伸出很多變形，像 LCM 跟 GRU 還有像 Pointer Network 等等 複習完這些很基本很基本的架構之後 你說新架構是什麼，是不是就是把這些架構全部把它疊起來 看自己的創意 我今天在夢中夢到這個參數，這個 hidden size
  - `lluMBz5AoOg:42-63` (`00:07:52.646–00:09:16.444`): 我是不是要先疊一個 CNN 再疊一個 RNN 再把 Fully connect 接上去 是不是我把所有的東西都疊起來 我就希望這個模型在我想要的 task 上面可以做得很好 我就把他們，隨我自己的意思把他們亂疊 好之後就開始 train 然後就開始 tune 你的參數 就像這個圖片一樣你開始 tune 你的參數，什麼 learning rate L2 的 weighted decay dropout 開始調 完之後你發現說 我的模型怎麼 train 起來都 train 不太起來，怎麼這麼奇怪 然後你就會有一個想法 一個很智障的想法 你就會覺得說是不是我疊的不夠深 就再把他疊深一點 繼續把它疊深之後就開始 tune neural network 然後開始 tune 參數跟前面的 case 一樣 然後發現 tune 完之後你的模型還是一個垃圾 這就結束了 其實我們覺得在做一個新的 task 的時候 可以先去 follow 說這個…
- `xCGidAeyS4M` (PRIMARY):
  - `xCGidAeyS4M:2-19` (`00:00:11.110–00:01:37.890`): 好，那接下來呢，我們來講一下 Recurrent Neural Network 那 Recurrent Neural Network呢 它其實也可以做到我們在前一堂課裡面 講的 sequence labeling 的 task 那最後呢，我們再來說他們有 甚麼樣的不同 那我們這邊要舉的例子呢 是 Slot Filling，那我們知道說 現在很流行呢，做一些智慧客服之類的東西 譬如說，做一些智慧的訂票系統 那這種智慧客服或智慧訂票系統裡面呢 你往往需要 Slot Filling 這個技術 Slot Filling 指的是甚麼呢 Slot Filling 指的是說 比如說假設有一個人對你的訂票系統說 I would like to arrive Taipei on November 2nd 那你的系統要自動知道說 你的系統裡面有一些 slot 比如說，在這個 訂票系統裡面呢 它會有一個 slot叫做 Destination 它會有…
  - `xCGidAeyS4M:96-116` (`00:07:08.400–00:08:30.510`): 然後所有的 neuron 都沒有任何的 bias 值 然後假設所有的 activation function 都是 linear 這樣可以不要讓計算太複雜 那現在假設我們的 input 是一個 sequence 我們的 input 是 [11] [11] [22] 那我們把[11] [11] [22] 這個 sequence input 到這個 Recurrent Neural Network 裡面去 會發生甚麼事呢？ 那首先呢，在你開始要 使用這個 Recurrent Neural Network的時候呢 你必須要給 memory 起始值 你必須要給 memory 在還沒有放進任何東西的時候， 你必須要給它一個初始值，比如說這邊呢 我們在假設還沒有放進任何東西之前 memory 裡面的值是 0 那現在輸入第一個輸入 [1 1] 那接下來會發生甚麼事呢 對這個 neuron 來說 它除了接到 input 的 [1 1] 以外…
  - `xCGidAeyS4M:139-152` (`00:10:01.990–00:10:53.980`): 所以 2 就被洗掉，變成 6 那接下來呢，我們的 input 是 2 跟 2，假設 input 是 [2 2]，這邊每一個綠色的 neuron 它考慮的 4 個 input ：2 跟 2 跟 6 跟 6 所以 6 + 6 + 2 + 2 是多少呢，得到的值是 16 那紅色 neuron 的 output 就是 32 所以 input 2 跟 2 的時候呢，output 是 32 那今天在做 Recurrent neural network 的時候呢 有一件很重要的事情就是 這個 input 的 sequence Recurrent neural network 在 考慮它的時候，並不是 independent 今天如果你任意調換 input sequence 的順序 比如說把 2 跟 2 挪到最前面來 那 output 呢，是會完全不一樣的 所以在 Recurrent neural network 裡面， 它會考慮 input…
  - `xCGidAeyS4M:644-661` (`00:47:47.060–00:48:56.980`): 我用 RNN 做了甚麼事情的時候， 就是你不要去問他說為甚麼你不用 LSTM 因為他其實就是用 LSTM ， 因為現在當你說你在做 RNN 的時候 其實你指的就是用 LSTM 所以呢，他其實是比較 standard 的 其實 Keras 裡面有支援 LSTM 啦，所以就算是 剛才講得這麼複雜的東西你沒聽懂就算了 在 Keras 裡面就是打 LSTM 這4個字母 然後就結束了 那 Keras 它其實支援三種 Recurrent neural networks，一個是 LSTM 一個是 GRU 是 LSTM 的一個稍微簡化的版本 它只有兩個 gate 據說少了一個 gate，但是 performance 跟 LSTM 差不多，而且少了 1/3 的參數 所以比較不容易 over-fitting 如果你要用一般的、我們這堂課最一開始講的那種 最簡單的 RNN 的話 也要說是 SimpleRNN 才行這樣子 那我想我們今天就上到這邊好了…
- `gjsdVi90yQo` (CORROBORATING):
  - `gjsdVi90yQo:32-66` (`00:01:30.000–00:02:59.840`): 東西 但其實這一堂課呢 不會講到太多跟Mamba有關的東西 我們主要講的是一個系列Mamba的一群好朋友們 那我們這一堂課呢 我們著重的點就在於類神經網路的架構 大家每次看到一個類神經網路架構的時候 要記得每一個架構 都有一個它存在的理由 每一個架構是因為不同的理由 而被設計出來的 比如說CNN存在的理由是什麼呢? CNN存在的理由是 CNN是Fully Connected的Feed Forward Network的一個Special Case 你把原來的最General的Feed Forward Network 做Receptive Field 拿掉一些不需要的Weight 做Parameter Sharing 讓一些Weight的參數是一樣的 讓一些參數的數值是一樣的 那就是Convolutional 就是CNN 所以Fully Connected Feed Forward Network 是一個更泛用的Network架構…
  - `gjsdVi90yQo:67-109` (`00:02:59.840–00:04:29.579`): 你沒有聽得很懂的話 CNN存在的理由 是我們過去上課的錄影 是講過的 那如果你剛才講的 沒有聽得很懂的話 那再趕快去複習 過去上課的錄影 那或者是 residual connection存在的理由是什麼 residual connection存在的理由 跟CNN是不一樣的 residual connection存在的理由是什麼呢 residual connection 我們上週也有提到過 我們說這是一個在韓武紀之前 就已經存在的類神經網路架構 很多人說2016年那個出現阿發購呢 是人工智慧的韓武紀大爆發 那將2015年 這residual network是2015年年底就有的 那他就是前韓武紀時期的東西了 而residual network存在的理由是什麼呢 那個時候人們發現啊 如果訓練一個很深的network 結果不太好 橫軸呢是訓練的iteration 那縱軸呢是測試資料上的 上面的錯誤率 比較56層的類神經網路 跟20層…
- `OP5HcXJg2Aw` (CORROBORATING):
  - `OP5HcXJg2Aw:0-28` (`00:00:00.200–00:01:28.400`): 我們要來講 Network 的架構 我們開始探討 Network 的架構設計 那我第一個跟大家講的 Network 架構的變形呢 是 Convolutional 的 Neural Network 它的縮寫呢 就是 CNN 那這個 CNN 啊 它是專門被用在影像上的 我希望透過 CNN 這個例子 來讓你知道說 Network 的架構 它的設計有什麼樣的想法 那為什麼設計 Network 的架構 可以讓我們的 Network 結果做得更好 好 我們接下來要講的例子是跟影像有關的 我們今天就想像說 我們要做影像的分類 也就是給機器一張圖片 它要去決定說這張圖片裡面有什麼樣的東西 好 那怎麼做呢 我們已經跟大家講過怎麼做分類這件事情 在以下的討論裡面 我們都假設我們的模型輸入的圖片大小 是固定的 舉例來說 它固定輸入的圖片大小 都是 100 × 100 的解析度 我們假設說不會突然出現大小不一的照片 即使今天一般在做影像辨識的時候 往…
  - `OP5HcXJg2Aw:674-712` (`00:28:03.660–00:29:33.130`): 就是 CNN 所以從這個圖上啊 你可以很明顯地知道說 其實 CNN 它的 Bias 比較大 它的 Model 的 Bias 比較大 那你可能會想說 有 Model Bias 比較大 不是一件壞事嗎 Model Bias 大 不一定是壞事 因為當 Model Bias 小 Model 的 Flexibility 很高的時候 它比較容易 Overfitting Fully Connected Layer 它可以做各式各樣的事情 它可以有各式各樣的變化 但是它可能沒有辦法在 任何特定的任務上做好 而 Convolutional Layer 它是專門為影像設計的 剛才講的 Receptive Field 參數共享 這些觀察 都是為影像設計的 那因為 Convolutional Layer 是特別為影像設計的 所以它在影像上仍然可以做得好 雖然它的 Model Bias 很大 但這個在影像上不是問題 但是如果它用在影像之外的任務 那你就…
  - `OP5HcXJg2Aw:1372-1399` (`00:54:38.110–00:55:38.820`): 但對 CNN 的 Network 來說它是非常不一樣 所以事實上 CNN 並不能夠處理影像放大縮小 或者是旋轉的問題 當它今天在某種大小的影像上 假設你裡面的物件都是比較小的 它在上面學會做影像辨識 你把物件放大它就會整個慘掉 所以 CNN 並沒有你想像的那麼強 那就是為什麼在做影像辨識的時候 往往都要做 Data Augmentation 所謂 Data Augmentation 的意思就是說 你把你的訓練資料 每張圖片都裡面截一小塊出來放大 讓 CNN 有看過不同大小的 Pattern 然後把圖片旋轉 讓它有看過說 某一個物件旋轉以後長什麼樣子 CNN 才會做到好的結果 那你說 欸 CNN 這個不能夠處理 Scaling 跟 Rotation 的問題啊 那有沒有什麼 Network 架構 是可以處理這個問題呢 其實有的 有一個架構叫 Special Transformer Layer 我們不會講它 就把它的這個錄影的連結放…

## Patterns and Repeated Themes

- 多個獨立來源均提供 `cnn_rnn_inductive_bias` 的 selector-approved transcript anchors；可把它們用於受限的 cross-source candidate synthesis。

## Contradictions

- 來源跨年份、模態與任務；它們的共同概念不等於共同的 benchmark、資料分布或性能結論。

## Inferences

- Candidate inference (not formal): CNN 的 locality／parameter sharing 與 RNN 的 state／order sensitivity 是可被任務資料結構驗證的 inductive bias；應以資料幾何與部署限制選擇，而非把任一架構當成通用預設。
- Candidate decision rule: 先明確寫出局部性、平移結構、序列順序與長距依賴假設；用參數量、receptive field、sequence length 和 error slices 對照 CNN/RNN 或競爭基線。

## Gaps and Missing Information

- 未使用未選定的片段、影格或投影片；若未來某個結論需要公式、圖表或程式畫面，必須建立獨立 visual-evidence request。
- 本 dossier 是 Distilly research input，不取代原始影片、source chunks 或 evidence packets。
