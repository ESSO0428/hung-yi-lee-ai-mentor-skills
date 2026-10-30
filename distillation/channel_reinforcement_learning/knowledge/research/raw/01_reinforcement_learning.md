# Research Dossier: reinforcement learning

## Source Metadata

- Source: `tnPVcec22cg` — DRL Lecture 5: Q-learning (Continuous Action)
- URL: https://www.youtube.com/watch?v=tnPVcec22cg
- Source role: `PRIMARY`
- Source weight: 1
- Evidence packet: `EVP-CHANNEL-tnPVcec22cg-reinforcement_learning-V1` (data/processing/channel_evidence_packets_v1/tnPVcec22cg--reinforcement_learning.md)
- Transcript type: `official`; selector confidence: `HIGH`
- Source: `z95ZYgPgXOY` — DRL Lecture 1: Policy Gradient (Review)
- URL: https://www.youtube.com/watch?v=z95ZYgPgXOY
- Source role: `PRIMARY`
- Source weight: 1
- Evidence packet: `EVP-CHANNEL-z95ZYgPgXOY-reinforcement_learning-V1` (data/processing/channel_evidence_packets_v1/z95ZYgPgXOY--reinforcement_learning.md)
- Transcript type: `official`; selector confidence: `HIGH`
- Source: `j82QLgfhFiY` — DRL Lecture 6: Actor-Critic
- URL: https://www.youtube.com/watch?v=j82QLgfhFiY
- Source role: `CORROBORATING`
- Source weight: 2
- Evidence packet: `EVP-CHANNEL-j82QLgfhFiY-reinforcement_learning-V1` (data/processing/channel_evidence_packets_v1/j82QLgfhFiY--reinforcement_learning.md)
- Transcript type: `official`; selector confidence: `HIGH`

## Evidence

- `tnPVcec22cg` (PRIMARY):
  - `tnPVcec22cg:0-2` (`00:00:00.000–00:00:11.080`): 臺灣大學人工智慧中心 科技部人工智慧技術暨全幅健康照護聯合研究中心 http://ai.ntu.edu.tw/ 今天的規劃是這樣， 我們剩下一點點 Q learning 的部分把它講完 接下來要講 Actor-critic
  - `tnPVcec22cg:3-28` (`00:00:20.180–00:01:49.020`): 講一些 Actor-critic 之後，之後要講說假設在 reinforcement learning 有碰到 reward 非常 sparse 的情況怎麼辦 然後最後會講說，如果完全沒有 reward 的時候 要怎麼辦， 完全沒有 reward 的狀況叫做 Imitation learning 今天首先跟大家繼續講一下 Q-learning 那其實跟 policy gradient based 方法比起來 Q learning 其實是比較穩的 policy gradient 其實是沒有太多遊戲是玩得起來的 你想想看我們作業 4-1，是要做 Pong 4-2 是要做 Breaking 那會什麼 4-1 不用 Breaking 呢？ 因為 policy gradient 在 Breaking 上面是做不太起來的 所以 policy gradient 其實比較不穩，尤其在沒有 PPO 之前 你很難用 policy gradient…
  - `tnPVcec22cg:203-209` (`00:14:32.080–00:14:57.360`): 那第 4 招是什麼，第 4 招就是不要用 Q-learning 用 Q learning 處理 continuous 的 action 還是比較麻煩 那到目前為止，我們講了 policy based 的方法 我們講了 PPO，這是上上周講的 上周講了 value based 的方法，也就是 Q learning 但是這兩者其實是可以結合在一起的， 也就是 Actor-Critic 的方法 臺灣大學人工智慧中心 科技部人工智慧技術暨全幅健康照護聯合研究中心 http://aintu.tw
- `z95ZYgPgXOY` (PRIMARY):
  - `z95ZYgPgXOY:2-16` (`00:00:36.040–00:02:02.620`): 那今天這一堂課，我們要講什麼呢？ 我們要講一個 policy gradient 的進階版 這個技術呢，叫做 Proximal Policy Optimization (PPO) 這個技術有多屌呢？這個技術呢， 它是 default reinforcement learning algorithm at OpenAI 是OpenAI 把這個方法， 當作他們 default reinforcement learning algorithm 所以今天假設你要 implement reinforcement learning，也許這是一個第一個你可以嘗試的方法，這是 PPO 今天這門課呢， 我們還是幫大家複習一下 Policy Gradient 這部分也許有點快，所以如果你有問題的話， 你就直接舉手打斷我 接下來，我們會講說，原來的 policy gradient， 是 On-Policy 的方法 那怎麼從 on-policy 的方法…
  - `z95ZYgPgXOY:29-47` (`00:06:00.480–00:07:27.280`): 那我們就來先複習一下 policy gradient，PPO 是 policy gradient 一個變形 所以我們先講 policy gradient 在 reinforcement learning 裡面呢有 3 個 components 一個 actor，一個 environment，一個 reward function 在我們作業 4-1 裡面呢，就是要做 讓機器玩 video game，那這個時候你 actor 做的事情 就是去操控，遊戲的搖桿， 比如說向左向右，開火，等等， 你的 environment 就是遊戲的主機， 負責控制遊戲的畫面 負責控制說，怪物要怎麼移動， 你現在要看到什麼畫面，等等 所謂的 reward function，就是決定，當你做什麼事情，發生什麼狀況的時候 你可以得到多少分數， 比如說殺一隻怪獸，得到20 分等等 那同樣的概念，用在圍棋上也是一樣 actor 就是 alpha Go，它要決…
  - `z95ZYgPgXOY:469-478` (`00:45:03.800–00:45:48.100`): 那它的意義就是，現在假設，我們在某一個 state st，執行某一個 action at 相較於其他可能的 action，它有多好 它真正在意的不是一個絕對的好， 而是說在同樣的 state 的時候 是採取某一個 action at，相較於其它的 action 它有多好，它是相對的好， 不是絕對好，那麼今天會減掉一個 b 嘛 減掉一個 baseline， 所以這個東西是相對的好，不是絕對的好 那這個 A 我們之後再講， 它通常可以是由一個 network estimate 出來的 那這個 network 叫做 critic， 我們講到 Actor-Critic 的方法的時候，再講這件事情 臺灣大學人工智慧中心 科技部人工智慧技術暨全幅健康照護聯合研究中心 http://aintu.tw
- `j82QLgfhFiY` (CORROBORATING):
  - `j82QLgfhFiY:0-26` (`00:00:00.000–00:01:26.460`): 臺灣大學人工智慧中心 科技部人工智慧技術暨全幅健康照護聯合研究中心 http://ai.ntu.edu.tw/ 接下來要跟大家講一下 Actor-Critic，要跟大家講一下 Actor-Critic 那在 Actor-Critic 裡面，最知名的方法就是 A3C Asynchronous Advantage Actor-Critic 那等一下就要跟大家介紹一下，這個 A3C 是什麼？ 如果去掉前面這個 Asynchronous 這個字眼啊 只有 Advantage Actor-Critic，就叫做 A2C 那如果前面加了 Asynchronous 這個字眼呢 變成 Asynchronous Advantage Actor-Critic，就變成 A3C 那我們等一下會來講一下這個東西是什麼 那我們很快複習一下 policy gradient 在 policy gradient 裡面，我們是怎麼說的呢？ 在 policy gra…
  - `j82QLgfhFiY:329-360` (`00:17:27.820–00:18:56.780`): 那這一組參數可能是 CNN 先把 input 的 pixel，變成比較high level 的資訊 然後再給 actor 去決定說它要採取什麼樣的行為 給這個 critic，給 value function 去計算 expected 的 return 也就是 expected reward 那另外一個事情是 我們一樣需要那個 exploration 我們一樣需要 exploration 的機制 那我們之前已經有講過 在講這個 Q function 的時候呢 在講 Q learning 的時候呢 我們有講過 exploration 這件事，是很重要的 那今天在做 Actor-Critic 的時候呢 有一個常見的 exploration 的方法 是你會對你的 pi 的 output 的這個 distribution 下一個 constrain 這個 constrain 是希望這個 distribution 的 entropy 不要…
  - `j82QLgfhFiY:689-700` (`00:33:41.900–00:34:14.760`): 有哪些技術是有人做過的 在 Actor-Critic 上面，有哪些技術是有人做過的 但是也許在 GAN 上面有試過的技術 你可以試著 apply 在 Actor-Critic 上 面做過的技術 你可以試著 apply 在 GAN 上面 看看 work 不 work 這個就是 Actor-Critic 和 GAN 之間的關係 可以帶給我們的一個好處 那這個其實就是 Actor-Critic 講到這裡大家有沒有問題要問的 臺灣大學人工智慧中心 科技部人工智慧技術暨全幅健康照護聯合研究中心 http://aintu.tw

## Patterns and Repeated Themes

- 多個獨立來源均提供 `reinforcement_learning` 的 selector-approved transcript anchors；可把它們用於受限的 cross-source candidate synthesis。

## Contradictions

- 來源跨年份、模態與任務；它們的共同概念不等於共同的 benchmark、資料分布或性能結論。

## Inferences

- Candidate inference (not formal): RL 演算法選擇必須先固定 state、action、reward、horizon 與資料收集條件，再比較 policy-gradient、actor-critic、PPO 或 value/Q-learning 變體的穩定性與樣本效率。
- Candidate decision rule: 在相同 environment seed 與 interaction budget 下，記錄 return distribution、constraint violations、exploration behavior 和 variance；將每次 algorithm change 對應到 action-space 或 credit-assignment 假設。

## Gaps and Missing Information

- 未使用未選定的片段、影格或投影片；若未來某個結論需要公式、圖表或程式畫面，必須建立獨立 visual-evidence request。
- 本 dossier 是 Distilly research input，不取代原始影片、source chunks 或 evidence packets。
