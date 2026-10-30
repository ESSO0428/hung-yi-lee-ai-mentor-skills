# Research Dossier: LLM／agent

## Source Metadata

- Source: `M2Yg1kwPpts` — 【生成式AI時代下的機器學習(2025)】第二講：一堂課搞懂 AI Agent 的原理 (AI如何透過經驗調整行為、使用工具和做計劃)
- URL: https://www.youtube.com/watch?v=M2Yg1kwPpts
- Source role: `PRIMARY`
- Source weight: 1
- Evidence packet: `EVP-CHANNEL-M2Yg1kwPpts-llm_agent-V1` (data/processing/channel_evidence_packets_v1/M2Yg1kwPpts--llm_agent.md)
- Transcript type: `official`; selector confidence: `HIGH`
- Source: `VqB8zMujdjM` — AI Agent (3/3): AI Agent 對於工作帶來的衝擊 - 以學術研究為例
- URL: https://www.youtube.com/watch?v=VqB8zMujdjM
- Source role: `PRIMARY`
- Source weight: 1
- Evidence packet: `EVP-CHANNEL-VqB8zMujdjM-llm_agent-V1` (data/processing/channel_evidence_packets_v1/VqB8zMujdjM--llm_agent.md)
- Transcript type: `official`; selector confidence: `HIGH`
- Source: `bJZTJ7MjYqg` — 【生成式AI導論 2024】第9講：以大型語言模型打造的AI Agent (14:50 教你怎麼打造芙莉蓮一級魔法使考試中出現的泥人哥列姆)
- URL: https://www.youtube.com/watch?v=bJZTJ7MjYqg
- Source role: `CORROBORATING`
- Source weight: 2
- Evidence packet: `EVP-CHANNEL-bJZTJ7MjYqg-llm_agent-V1` (data/processing/channel_evidence_packets_v1/bJZTJ7MjYqg--llm_agent.md)
- Transcript type: `official`; selector confidence: `HIGH`
- Source: `urwDLyNa9FU` — AI Agent (1/3)：核心技術 Context Engineering 基本概念解說
- URL: https://www.youtube.com/watch?v=urwDLyNa9FU
- Source role: `CORROBORATING`
- Source weight: 2
- Evidence packet: `EVP-CHANNEL-urwDLyNa9FU-llm_agent-V1` (data/processing/channel_evidence_packets_v1/urwDLyNa9FU--llm_agent.md)
- Transcript type: `official`; selector confidence: `HIGH`

## Evidence

- `M2Yg1kwPpts` (PRIMARY):
  - `M2Yg1kwPpts:0-11` (`00:00:01.300–00:01:29.980`): 好,那各位同學大家好啊 那我們就來上課吧 那今天這堂課呢,我們要講的是AI agent 這是一個現在非常熱門的議題 那在課程開始之前呢,先講一個免責聲明 我知道你在各個地方可能都聽過AI agent這個詞彙 它是一個被很廣泛應用的詞彙 每個人心裡想的AI agent可能都不一樣 等一下下一頁投影片會告訴你說 我在這一堂課中指的AI agent是什麼,那如果你在其他地方聽過別的AI agent的定義,那也沒問題,我也不會爭論說什麼樣的定義,才是真正的AI agent的定義,有些人甚至會告訴你說,現在那些用大型語言模型驅動的號稱AI agent的東西都不是真正的AI agent,要有身體的像這個機器人一樣的才叫做AI agent,所以每個人心裡想像的AI agent是不一樣的, 好,那這一堂課我們要講的AI agent是什麼呢?今天我們使用AI的方式,通常是人類給一個明確的指令,你問AI說AI agent的翻譯是什麼,那AI呢,按…
  - `M2Yg1kwPpts:46-85` (`00:02:58.900–00:04:28.879`): 叫做action 那他執行個action以後 會影響環境的狀態 會看到不一樣的observation 就會執行不同的action 那這個步驟會一直循環 直到AI agent達成 我們要他達成的目標為止 那我只要講到這邊 你可能還覺得非常的抽象 那我們可以用下圍棋來舉例 那AlphaGo是大家非常熟悉的東西 AlphaGo其實也可以 看作是一個AI agent 這個AI agent的目標就是 下棋要贏 他的observation是什麼 他的observation是現在棋盤上 黑子跟白子的位置 現在棋盤上的盤式 那他可以採取的action是什麼 他可以採取的action 就是在棋盤上的19x19路的範圍中 選擇一個動作 選擇一個可以落子的位置 那他選擇完可以落子的位置 他落下一次以後 會改變他對手的輸出 你落下一隻以後 你的對手會落下另外一隻 那會改變你觀察到的observation 那你就要採取下一個action 所以Alpha…
  - `M2Yg1kwPpts:86-125` (`00:04:28.899–00:05:58.480`): reinforcement learning RL的課程 往往都是用這樣的方式來開場的 為什麼呢 因為過去要打造AI agent的時候 往往覺得就是要透過RL的演算法來打造AI agent 那怎麼透過RL的演算法來打造AI agent呢 RL這個演算法就是他可以去learn一個agent 那這個agent可以maximize reward 所以你要把你的目標呢 轉換成一個叫做reward的東西 那這個reward呢 是人定義的越接近 你的目標reward就越大 那如果在下圍棋裡面 你通常就會定說 贏棋reward就是正一 輸棋reward就是負一 然後你要訓練的那個AI agent 就會學習去maximize reward 透過RL的演算法 所以透過RL的演算法 其實你也有可能學一個AI agent 但是透過RL演算法的侷限是 你需要為每一個任務 都用RL的演算法 訓練一個模型 AlphaGo在經過了大量的訓練以後 他可以下圍…
  - `M2Yg1kwPpts:1322-1348` (`00:52:06.280–00:53:34.059`): 這段話,某年某月某日高雄氣溫如何,這個是User Prompt,那如果你有在使用這個ChatGPT的API的話,你知道你的輸入要分成System Prompt跟User Prompt,那很多同學會搞不清楚System Prompt跟User Prompt有什麼樣的差別,那System Prompt指的是說,你在開發應用的這個Developer下的這個Prompt,這個Prompt呢,是每次都是一樣的,每次你都想要放在語言模型最前面, 讓他去做文字接龍的這個敘述叫做System Prompt 那每次使用他的時候都不一樣 通常是這個服務的使用者輸入的內容叫做User Prompt 那在ChartGPT的API裡面 特別把System Prompt跟User Prompt分開 也是要分開輸入的 因為System Prompt跟User Prompt 他有不同的優先級 System Prompt他優先級比較高 如果System Pro…
- `VqB8zMujdjM` (PRIMARY):
  - `VqB8zMujdjM:0-49` (`00:00:00.000–00:01:29.355`): 好 那最後一段呢 我想要跟大家分享 AI agent 對我們未來的工作 可能帶來的衝擊 那我會以學術研究為例 來跟大家分享 那現在呢 AI 扮演的角色正在改變 最早它是工具 一個口令 一個動作 後來它逐漸的能力越來越強 人們開始說 也許我們可以跟 AI 協作 讓 AI 跟人類一起完成任務 但是現在已經有很多的 AI agent 它們是有更強的自主性 它們有機會自己獨立完成一個任務 接下來對於學術研究而言 人們會問的問題就是 它能不能自己寫一篇文章 呢 你可以看看這個 Stanford 教授 Andrew Hall 的 PO 文 他是一個政治經濟學的教授 他就在 X 上面發表了一篇文章 他就說跟大家講 Claude 他這邊不是用 OpenClaw 他是用 Claude Code 我意思也差不多 他說 Claude Code 是可以獨自寫一篇文章的 然後他想要告訴大家說 這些 AI agent 對他的領域來說 就像是迎面而來的貨車…
  - `VqB8zMujdjM:50-96` (`00:01:29.355–00:02:57.510`): 在教研究生怎麼做研究一樣 但這個研究並不是一個全新的研究 他是要 AI agent 去擴展一個 他過去已經做過的研究 他這邊的研究是針對美國大選的 美國大選有新的數據 所以他希望這些 AI agent 根據新的數據 但是仿照他自己過去的研究方法 再寫一篇新的論文 所以在整個 prompt 裡面 他做的事情是 他先給 AI agent 一篇 他過去的論文 讓 AI agent 讀過 他過去的論文以後 根據他之前 已經有的分析方法 再重複一次 只是用新的數據 來跑這些舊的分析方法 那做完這件事以後 顯然我覺得 Andrew Hall 大受震撼 他就寫了一篇文章 叫做 100 倍的 research assistant 在這篇文章開頭 他就說 他用 Claude Code 一個小時就寫了一篇文章 接下來他就去找了一個苦命研究生 也做跟 Claude 一模一樣的事情 所以他就把同樣的指令 給了那個研究生 花了 16 個小時 兩個工作天…
  - `VqB8zMujdjM:97-141` (`00:02:57.510–00:04:26.799`): 所以他說根據美國的行情 叫這個博士生做 16 個小時 應該至少要給他 1000 美金 那 Claude 他 prompt 了一次 花了 10 美金左右 比人類便宜 100 倍 那你說 Claude 有錯 那我敢不敢 prompt 5 次 我也只花了 50 美金而已 比人類便宜 20 倍 所以他覺得 這個研究變了 也許以後最有生產力的研究機構 是一個資深的老師 不是帶著一群研究生 而是帶著一群 LLM 帶著一群 AI agent 來做研究 當然這邊你也可以吐槽的地方 你也可以反駁的地方是說 Claude 畢竟有犯錯 雖然它是只犯了一個錯 我不是這個領域的專家 所以我無法判斷那個錯有多嚴重 也許那個錯是非常嚴重的 會影響整個判斷的 也許那個錯是完全不該犯的 那這樣人類還是有它的價值的 也許他要做的事情是 假設由 Claude 完成一篇文章 然後人類來檢查 然後找出那個錯誤 那合起來的花費到底是多少 到底是人類做比較省錢 還是 AI…
  - `VqB8zMujdjM:390-436` (`00:11:53.646–00:13:23.502`): 也許這可以讓人類鬆口氣 但是不要忘了 那是 2025 年的時候 AI 的能力不斷的與日俱增 今天你可能覺得 GPT 5.4 很厲害 或覺得 Claude 4.6 很厲害 但是不要忘了 它們是 2026 年 現在這個時間點的未來 往後看最差的模型 以後我們只會看到 更厲害的模型而已 但至少在 2025 年 當第二篇論文問世的時候 那個時候 AI 想的題目 實際上並沒有人類想的題目好 那 AI 它當然也可以審查論文 今天你投稿到一個國際會議 就會有一群 reviewer 一群審查委員來對這篇論文進行評價 最後決定論文是否被國際會議接受 今天這一些 reviewer 有沒有可能其實就是一個 AI 呢 其實在今年的 AAAI 這是一個跟 AI 有關的國際會議 AI 是正式進入了審查流程 在 AAAI 2026 裡面 每篇文章 不只有三個人類的 reviewer 還有一個 AI 的 reviewer 它就是 AI 它名字告訴你 我就是…
- `bJZTJ7MjYqg` (CORROBORATING):
  - `bJZTJ7MjYqg:0-25` (`00:00:00.000–00:01:27.800`): 好,那現在這一堂課呢,要跟大家講的是一個大型語言模型未來的趨勢 用大型語言模型打造AI agent 今天多數人呢,在使用AI幫我們做事的時候 我們往往只要求AI做一個步驟 舉例來說,你想要去GPT幫你做翻譯 你就給他你要翻譯的句子 他就給你翻譯的結果 或你想用ChatGPT幫你畫圖 你就說請幫我畫圖 ChatGPT就呼叫DALLE去給你一張圖出來 但是今天我們人類可以做更複雜的任務 而這些任務往往是需要多個步驟才能夠完成的 舉例來說我現在接到一個任務 是要舉辦朋友間的聚餐 那我可能需要先做一下計劃 就我要先調查時間 調查大家有空的時間 統計一下最多人有空的時間 然後我就訂我們常常吃的餐廳A 然後所以我可能接下來 就是先執行第一個步驟 發出一個Google表單給我的朋友們 然後我的朋友們就會填寫Google表單 我過兩天之後 再來統計一下時間 看最多人有空的時間是在週四晚上
  - `bJZTJ7MjYqg:26-53` (`00:01:27.800–00:02:56.660`): 然後呢我就跟餐廳A訂位 但是餐廳A說不好意思週四晚上沒有位子了 所以我就得訂另外一家餐廳 那這個時候我可能會用Google Map查詢一下 還有沒有其他可以去的餐廳 然後呢Google Map會給我一些餐廳的推薦 那我可能就選了另外一家餐廳B 完成舉辦朋友間聚餐這個任務是需要多步驟的 所以我需要先做一個規劃 而這些步驟它的先後順序是重要的 我不能先訂餐廳再來調查時間 我一定要先調查時間才能夠訂餐廳 不然沒有人來就糟糕了 而我在執行的過程中這個計劃趕不上變化 原來我計劃要訂餐廳A 但是可能餐廳A沒有位置了 我只好改訂另外一家餐廳 這樣這種多步驟的複雜的任務 今天我們有沒有可能讓AI來辦到這件事呢 如果AI可以辦到這件事 在這一堂課裡面 我們就稱之為AI Agent 那我知道Agent這個詞彙呢 在不同的領域可能有不同的用法 那甚至就算是在談論AI的時候 講到AI Agent的時候 每個人可能也都有不同的想像 但這一堂課裡面
  - `bJZTJ7MjYqg:287-316` (`00:13:10.340–00:14:40.240`): 但是總之,OpenAI顯然在打造有記憶力的ChatGPT 運作起來可能是怎麼樣子呢? 當你跟ChatGPT對話完之後 它可能會把對話裡面的關鍵訊息進行摘要 比如說它知道你現在正在準備期中考試 接下來當你開始新的對話 原來的ChatGPT一旦開始新的對話 一切過去對話的內容都會清空 但這一次他有做一些摘要 所以他知道過去對話的內容裡面 有哪些重點 所以也許你下一次跟他對話的時候 他會先對他過去的記憶做一下 RAG搜尋一些跟你相關的資訊 那他看到你跟他講話的時候 他甚至可能會問你說 那你期中考考得怎麼樣等等 所以有可能給ChatGPT記憶 那如果ChatGPT有記憶的話 它就可以更加的個人化 那雖然現在OpenAI的ChatGPT 還沒有真正釋出記憶的功能 但是其實也有很多人試圖在以ChatGPT為基礎 打造有記憶能力的GPT 舉例來說你可以看一篇paper 叫做Memory-GPT 它就會展示大型語言模型 怎麼加上RAG讓它有這…
  - `bJZTJ7MjYqg:507-538` (`00:23:31.440–00:24:44.440`): 這個大型語言模型 他下一步的行動 是會立即評估愛戴爾的傷勢 那如果有記憶的話 他的行動就會略有不同 你看他這邊多加了一句話 就在評估愛戴爾傷勢的過程中 我也會保持高度警覺 注意四周是否有複製體 或其他潛在的威脅 所以有了記憶會影響 有了記憶有了經驗 會影響這個模型的行為 讓他採取更好的行為 他可以透過他的經驗 改變他未來所會採取的行動 所以這個就是一個 想像中的未來AI agent 可以做到的事情 依據今天大型語言的能力 我相信其實AI agent 很有可能在一兩年後 你就會看到滿坑滿谷的AI agent 生活在我們的周遭 而如果你想要知道更多有關AI agent的事情的話 我這邊放了一篇overview paper 然後這一個圖是從overview paper裡面截取出來的 就是作者想像了一個未來 充斥了AI agent的虛擬世界 好 那這個部分呢 我其實就講到這邊 那我們還有大概五分鐘的時間 我就可以來回答一下同學們的問題
- `urwDLyNa9FU` (CORROBORATING):
  - `urwDLyNa9FU:0-39` (`00:00:00.133–00:01:30.090`): 好，各位同學大家好啊 我們就開始來上課吧 今天呢，我們要繼續來講 AI Agent 那今天的課程呢 還是比較科普性的 那我們分成三個段落 第一段呢 我們來講 AI Agent 背後的核心技術 我們比較系統化地來講 Context Engineering 然後第二段呢 我們來講 AI Agent 之間的互動 然後最後我們來講 AI Agent 對於我們未來的工作 可能造成什麼樣的衝擊 那我們就先從 AI Agent 的核心技術 Context Engineering 開始講起 那等一下這段課程啊 也許你聽了會覺得似曾相識 因為很多呢 Context Engineering 的技術 都已經在這個 OpenClaw 裡面被實作 那今天這段課程比較不一樣的地方 是會引用大量的論文 那你發現這些論文都是非常新的論文 幾個月前、半年前的論文 而這些技術都已經被實作在 OpenClaw 裡面 所以上週其實很多技術我們都已經有提到 那只是今天…
  - `urwDLyNa9FU:85-124` (`00:02:58.044–00:04:27.200`): 那這裡會遇到的難點就是 語言模型的輸入長度是有限的 它不能夠吃無限長的輸入 這就是為什麼我們需要 AI Agent 就是攔截在語言模型跟人類 或者是語言模型要執行的環境之間的一個介面 它就像是語言模型的守門人 語言模型的經紀人 它決定語言模型會看到什麼 所以來自外界的輸入會經過 AI Agent 那這個 AI Agent 不一定是 OpenClaw 只是 AI Agent 的其中一個例子 那今天 OpenClaw 還非常的原始 你可以想成它是初代的 AI Agent 它也許在過幾年以後 我們再回頭看 OpenClaw 就好像今天你拿著 iPhone 去看過去的 Nokia 手機一樣的感覺 我們現在看到的只是 AI Agent 的原型 以後一定還會有更多的進展 那 OpenClaw 做的事情 或 AI Agent 做的事情 就是選擇給語言模型看的內容 所以語言模型真正看到的是 AutoGPT AI Agent 篩選過的長度合適的…
  - `urwDLyNa9FU:125-162` (`00:04:27.200–00:05:56.189`): 不能太長 也不能太短 而這個 AI Agent 幫語言模型管理它的輸入 讓輸入的長度是合適的 這件事情就叫做 Context Engineering 剛才是概念性的介紹 Context Engineering 如果我們今天要用 比較程式語言的方法來描述它的話 可能看起來像是這樣子的 現在左邊這段程式碼 是沒有做 Context Engineering 的狀況 其實沒有做 Context Engineering 的時候 你可以想成語言模型跟外界的互動 就是一個 for 迴圈 那這個 for 迴圈是從 1 到無限大 這個 1 要執行多少個 step 那這個取決於你想要讓語言模型運作多久 你想要讓這個 AI 運作多久 那我們希望它永遠地執行下去 執行到天荒地老 所以這邊放一個無限大 然後呢 這邊會有一個初始的輸入 那這個可能就是你給語言模型的指令 那今天這個指令甚至可以 就是一個非常 high level 的目標 比如說成為 You…
  - `urwDLyNa9FU:1524-1569` (`00:51:47.204–00:53:05.382`): 它就解不了了 這邊 All-Long 這些 benchmark 就是測試語言模型 在 context 非常長的情況下 它能不能夠好好的運作 但是加上它的 這個 Recursive Language Model 以後 因為它的 Recursive Language Model 是一個 context engineering 的方法 所以它可以外掛在 任何現有的語言模型上 所以如果外掛在 GPT-5 上 就可以讓本來 已經很厲害的 GPT-5 變得更厲害 在輸入真的非常長 比如說長達 1M 100 萬個 token 的時候 仍然可以在這一些 長 context 的 benchmark 上面 做出不錯的效果 總之呢 今天就是比較系統化的 跟大家介紹了 context engineering 那我們這邊有一個演算法 這個演算法 摘要了 context engineering 實際上做的事情 那我們也跟大家說 其實 context 分成…

## Patterns and Repeated Themes

- 多個獨立來源均提供 `llm_agent` 的 selector-approved transcript anchors；可把它們用於受限的 cross-source candidate synthesis。

## Contradictions

- 來源跨年份、模態與任務；它們的共同概念不等於共同的 benchmark、資料分布或性能結論。

## Inferences

- Candidate inference (not formal): LLM agent 是有 state、context、tools、planning 與 evaluation 的系統；問題應先被拆成可觀察的 failure mode，而非只調 prompt 或加入更多工具。
- Candidate decision rule: 先定義任務成功、tool-call correctness、state/context retention、cost/latency 與 safety 指標；建立不使用工具或縮短 context 的對照，針對最小可重現失敗設計一個辨別性實驗。

## Gaps and Missing Information

- 未使用未選定的片段、影格或投影片；若未來某個結論需要公式、圖表或程式畫面，必須建立獨立 visual-evidence request。
- 本 dossier 是 Distilly research input，不取代原始影片、source chunks 或 evidence packets。
