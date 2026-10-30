# Research Dossier: optimization／training paradigm

## Source Metadata

- Source: `1UqCjFQiiy0` — ML Lecture 1: Regression - Demo
- URL: https://www.youtube.com/watch?v=1UqCjFQiiy0
- Source role: `PRIMARY`
- Source weight: 1
- Evidence packet: `EVP-CHANNEL-1UqCjFQiiy0-optimization_training-V1` (data/processing/channel_evidence_packets_v1/1UqCjFQiiy0--optimization_training.md)
- Transcript type: `official`; selector confidence: `HIGH`
- Source: `yKKNr-QKz2Q` — ML Lecture 3-1: Gradient Descent
- URL: https://www.youtube.com/watch?v=yKKNr-QKz2Q
- Source role: `PRIMARY`
- Source weight: 1
- Evidence packet: `EVP-CHANNEL-yKKNr-QKz2Q-optimization_training-V1` (data/processing/channel_evidence_packets_v1/yKKNr-QKz2Q--optimization_training.md)
- Transcript type: `official`; selector confidence: `HIGH`
- Source: `e03YKGHXnL8` — [TA 補充課] Optimization for Deep Learning (2/2) (由助教簡仲明同學講授)
- URL: https://www.youtube.com/watch?v=e03YKGHXnL8
- Source role: `CORROBORATING`
- Source weight: 2
- Evidence packet: `EVP-CHANNEL-e03YKGHXnL8-optimization_training-V1` (data/processing/channel_evidence_packets_v1/e03YKGHXnL8--optimization_training.md)
- Transcript type: `official`; selector confidence: `HIGH`
- Source: `BABPWOkSbLE` — 【機器學習2021】類神經網路訓練不起來怎麼辦 (五)： 批次標準化 (Batch Normalization) 簡介
- URL: https://www.youtube.com/watch?v=BABPWOkSbLE
- Source role: `CORROBORATING`
- Source weight: 2
- Evidence packet: `EVP-CHANNEL-BABPWOkSbLE-optimization_training-V1` (data/processing/channel_evidence_packets_v1/BABPWOkSbLE--optimization_training.md)
- Transcript type: `official`; selector confidence: `HIGH`

## Evidence

- `1UqCjFQiiy0` (PRIMARY):
  - `1UqCjFQiiy0:0-6` (`00:00:00.000–00:00:20.865`): 臺灣大學人工智慧中心 科技部人工智慧技術暨全幅健康照護聯合研究中心 http://ai.ntu.edu.tw 那我們在前一堂課看了regression， 我們知道怎麼用gradient descent來找出regression model的參數 這個聽起來還滿容易的。 接下來，我就舉個例子， 讓大家知道實際在做regression的時候， 你會碰到甚麼樣的困難。
  - `1UqCjFQiiy0:7-30` (`00:00:24.855–00:01:52.265`): 這邊我們假設x data有10筆， y data也有10筆。 那x和y之間的關係， 是ydata= b+w*xdata 那b和w都是參數， 我們用gradient descent把b和w找出來。 我當然知道說今天這個問題有closed-form solution， 這個b和w有更好的方法可以找出來， 那我們假裝不知道這件事， 我們要練習用gradient descent把b和w找出來。 那怎麼做呢? gradient descent其實非常的簡單， 所以這邊我們不需要說太多。 這個程式碼還沒有超過20行。 我們先給b一個初始值， 這邊b的初始值是 -120， 我們給w一個初始值， 這邊w的初始值是-4， 我們需要一個learning rate，那learning rate我們就給他一個很小的數字 iteration就設100000個 那在每一個iteration裡面， 我們要做的事是，計算出b和w對loss的偏微分， 計算的式…
  - `1UqCjFQiiy0:59-65` (`00:03:37.735–00:04:00.345`): 這是learning rate 調大10倍後的結果， 你發現說最後，經過100000次參數的update以後 我們的參數在這個地方， 離最佳解稍微近了一點， 不過這邊有一個劇烈的震盪的現象發生。 那我們再把learning rate稍微設大一點， 我們設再大10倍，
  - `1UqCjFQiiy0:102-106` (`00:06:36.665–00:06:52.600`): 你會發現說有了新的learning rate以後， 從初始的值到終點， 我們就可以很順利的在十萬次update參數之內，走到我們的終點了 我們就可以很順利的在十萬次update參數之內，走到我們的終點了 臺灣大學人工智慧中心 科技部人工智慧技術暨全幅健康照護聯合研究中心 http://ai.ntu.edu.tw
- `yKKNr-QKz2Q` (PRIMARY):
  - `yKKNr-QKz2Q:1-24` (`00:00:20.820–00:01:49.320`): 好，各位同學大家早 那我們就開始上課吧！ 今天的第一堂課，我們要講的是 Gradient Descent 我們上次已經大概講過怎麼做了 但是有一些小技巧呢，你可能是不知道的 所以我們要再詳細說明一下，Gradient Descent 你要怎麼把它做得更好 好，那我們上次是這樣說的 在整個 machine learning 的第3個步驟 我們要找一個最好的 function 那找一個最好的 function 這件事呢 是要解一個 optimization 的 problem 也就是說，在第二步， 我們先定了一個 loss function： L 這個 loss function 呢，它是一個 functional unction 你把一個 function 代到這個 loss function 裡面 或者是你把一個操控 function 形狀的參數 我們現在，在這張投影片裡面，把那些參數寫成 θ L 是 loss functio…
  - `yKKNr-QKz2Q:25-48` (`00:01:49.320–00:03:18.840`): 當然你也可以反過來定義一個 function 是 參數越好，它 output 的值越大 那這時候就不會叫它 loss function，就會叫他別的名字 比如說，叫它 objective function 好，這邊應該是 minimum 我們要找一組參數 θ，讓這個 loss function 越小越好 那這件事情怎麼做呢？ 我們可以用 Gradient Descent 假設現在這個 θ 是一個參數的 set 那裡面有兩個參數：θ1 跟 θ2 首先，你先隨機的選取一個起始的點 隨機選取一組起始的參數 這邊寫成 θ(上標0, 下標1)、θ(上標0, 下標2) 用上標 0 來代表說，它是初始的那一組參數 那用下標代表說 這個是這一組參數裡面的 第 1 個 component 跟第 2 個 component 接下來，你計算 θ(上標0, 下標1) 跟 θ(上標0, 下標2) 對這個 loss function 的偏微分 計算他們的…
  - `yKKNr-QKz2Q:531-554` (`00:33:04.400–00:34:33.840`): 那接下來呢，你在 update 參數的時候 你只考慮那一個 example 我們只考慮一個 example 的 loss function，我們就寫成 L^n，代表它是考慮第 n 個 example 的 loss function 那你在算 Gradient 的時候呢？ 你不是算對 total 所有的 data，它的 Gradient 的和 你只算對某一個 example，它的 loss 的 Gradient 然後呢，你就很急躁的 update 參數了 所以在原來的 Gradient Descent 裡面， 你計算所有 data 的 loss 然後才 update 參數 但是在 Stochastic Gradient Descent 裡面 你看一個 example，就 update 一個參數這樣 你可能想說，這有啥好呢？ 聽起來好像沒有甚麼好的 那我們實際來操作一下好了 剛才看到圖呢，它可能是這個樣子的 我們剛才看到的圖呢，它…
  - `yKKNr-QKz2Q:973-985` (`01:01:13.440–01:01:51.800`): 在 local minimum 附近，所以你就停下來了 因為你們真的很少有機會 exactly 微分值算出來是 0 嘛 對不對，你可能覺得說， 微分算出來很小，就很接近 local minimum 你就把它停下來，那其實搞不好，它是一個高原的地方 它離那個 local minimum 還很遠啊 這也是有可能的 講到這邊，有人都會問我一個問題 這個問題，我很難回答，他說 你怎麼會不知道你是不是接近 local minimum 了呢？ 我一眼就知道說 local minimum 在這邊阿 呵呵，你怎麼會不知道呢？ 所以我覺得這些圖都沒有辦法 表示 Gradient Descent 的精神 臺灣大學人工智慧中心 科技部人工智慧技術暨全幅健康照護聯合研究中心
- `e03YKGHXnL8` (CORROBORATING):
  - `e03YKGHXnL8:1-23` (`00:00:27.242–00:01:55.568`): 那我們從這邊繼續 好我們剛剛講到，複習一下剛剛講過的東西 我們複習了 前面李宏毅老師講過的一些比較有名的算法 裡面包括最常用的兩個，就是 HGD with momentum 還有 adam 這兩個算法 然後這兩個算法優點跟缺點有什麼 HGD 通常他比較穩 然後收斂的比較好 但是 adam 他算的比較快 所以我們一般在做的時候也都是以這兩個 optimizer 為主 接下來我們介紹了一些做法可能來修正他們的一些問題 希望他們可以改進這兩個算法，讓他們互相向對方學習 那這些裡面有包括 adabound、包括 AMSGrad 這兩個算法是改善 adam 的算法 那他們在想的是，因為你的 learning rate 有可能會太大或者是太小 那他們用一些方法來避免掉這樣的情況 讓 adam 在最後比較穩一點 不然如果你一下 learning rate 一下太大一下太小，那 adam 最後收斂的時候就會不穩 他們覺得這可能是 adam 比…
  - `e03YKGHXnL8:24-41` (`00:01:55.568–00:03:21.271`): 那這些都是希望去透過一個人工的方式來訂出一個調整 learning rate 的方法 讓 HGDM 可以收斂的比較快 不用在那邊慢慢的等他收斂 好那我們剛剛講到最後的 one cycle LR 他其實是由三個部分組成的 第一個部分是 warm-up 然後再來 annealing 還有最後的 fine-tuning 那我們就想到，那 adam 需要這個東西嗎 就是我們需不需要一開始先減低 adam 的 learning rate，後來再增加他 結果是，會這樣問結論一點是當然需要嘛 那為什麼需要？有人可能會想說 Adam 一開始不就已經做了 adaptive learning rate 嗎 那為什麼我們還需要去調整這個東西 原因是這樣的 因為這是在實際做實驗做出來的，在一個機器翻譯的實驗做出來的結果 那你就可以看到這幾張圖的縱軸是 iterration 然後橫軸是 gradient 的 distribution 那一開始看起來 g…
  - `e03YKGHXnL8:42-60` (`00:03:21.271–00:04:48.569`): 然後最後這邊有一堆幾乎沒有 gradient 的 parameter 好那再把它放大一點來看 我們突然發現前面幾個 time step 好像 它的分布跟人家不大一樣 然後那為什麼他們的分佈會跟人家不大一樣呢 原因是這樣，因為你一開始剛開始訓練的時候 你的 initialization 的時候，你不知道你 initial 在哪個地方 所以一開始的幾個 time step 他有可能 gradient 會很亂 再加上你一開始的時候，因為你那個底下的分母 他的估計可能不會估計得很準，因為那個 EMA， square of gradient 的估計 他一定是你在做了愈多 time step 以後 他的估計才會愈來愈準 所以一開始那個 learning rate 的估計不準 所以他有可能會一下走太多一下走太少 所以他整體來說就不穩嘛 那不穩的話他的 gradient 當然也會分佈的比較亂一點 所以這就是為什麼我們需要 warm-up 的原…
- `BABPWOkSbLE` (CORROBORATING):
  - `BABPWOkSbLE:0-33` (`00:01:10.550–00:02:39.450`): 這邊是一個很快地介紹 Batch Normalization 這個技術 好 那你記得啊 我們之前才講過說 我們能不能夠直接改 error surface 的 landscape 我們覺得說 error surface 如果很崎嶇的時候 它比較難 train 那我們能不能夠直接把山剷平 讓它變得比較好 train 呢 Batch Normalization 就是其中一個 把山剷平的想法 好 那我記得我們在講 optimization 的時候 我們一開始就跟大家講說 不要小看 optimization 這個問題 有時候就算你的 error surface 是 confessed 它就是一個碗的形狀 都不見得很好 train 那我們舉的例子就是 假設你的兩個參數啊 它們對 Loss 的斜率差別非常大 在 W1 這個方向上面 你的斜率變化很小 在 W2 這個方向上面斜率變化很大 你今天如果是固定的 learning rate 你可能很…
  - `BABPWOkSbLE:176-213` (`00:08:29.570–00:09:58.460`): variance呢 是 1 那你就會發現說所有的數值 所有 feature 不同 dimension 的數值 都在 0 上下 那你可能就可以製造一個 比較好的 error surface 所以像這樣子 Feature Normalization 的方式 往往對你的 training 有幫助 它可以讓你在做 gradient descent 的時候 這個 gradient descent 它的 Loss 收斂更快一點 可以讓你的 gradient descent 它的訓練更順利一點 這個是 Feature Normalization 好 所以當然 Deep Learning 可以做 Feature Normalization 你可能會把 feature 做 normalize 以後 其實在助教的 code 裡面 我們都有對 feature 做 normalization 得到 x tilde 以後呢 這個是 x tilde 代表…

## Patterns and Repeated Themes

- 多個獨立來源均提供 `optimization_training` 的 selector-approved transcript anchors；可把它們用於受限的 cross-source candidate synthesis。

## Contradictions

- 來源跨年份、模態與任務；它們的共同概念不等於共同的 benchmark、資料分布或性能結論。

## Inferences

- Candidate inference (not formal): 訓練問題應先用 learning curve、learning rate、gradient／loss 行為與 normalization 條件辨別，而非先改大模型或一次改多個 optimizer 設定。
- Candidate decision rule: 保持資料與架構固定，先記錄 loss、gradient norm、learning-rate schedule 和 train/validation gap；一次只變更一個 optimizer、schedule、batch 或 normalization 因子，將結果連回可區分的失敗假設。

## Gaps and Missing Information

- 未使用未選定的片段、影格或投影片；若未來某個結論需要公式、圖表或程式畫面，必須建立獨立 visual-evidence request。
- 本 dossier 是 Distilly research input，不取代原始影片、source chunks 或 evidence packets。
