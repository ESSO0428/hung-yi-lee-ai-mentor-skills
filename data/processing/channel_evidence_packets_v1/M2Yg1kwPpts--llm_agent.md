# Evidence Packet: M2Yg1kwPpts / LLM／agent

- packet_id: `EVP-CHANNEL-M2Yg1kwPpts-llm_agent-V1`
- packet_schema: `hung-yi-channel-evidence-packet.v1`
- packet_type: `EVIDENCE_PACKET_READY`
- video_id: `M2Yg1kwPpts`
- source_url: https://www.youtube.com/watch?v=M2Yg1kwPpts
- title: `【生成式AI時代下的機器學習(2025)】第二講：一堂課搞懂 AI Agent 的原理 (AI如何透過經驗調整行為、使用工具和做計劃)`
- transcript_type: `official`
- source_quality: `OFFICIAL`
- manifest_status: `VERIFIED`
- concept_id: `llm_agent`
- source_role: `PRIMARY`
- source_scope: selective review of selector-approved transcript chunks; not full-video coverage and not a claim of full-video understanding

## Direct evidence

1. `M2Yg1kwPpts:0-11` (`00:00:01.300–00:01:29.980`): Direct transcript evidence. 好,那各位同學大家好啊 那我們就來上課吧 那今天這堂課呢,我們要講的是AI agent 這是一個現在非常熱門的議題 那在課程開始之前呢,先講一個免責聲明 我知道你在各個地方可能都聽過AI agent這個詞彙 它是一個被很廣泛應用的詞彙 每個人心裡想的AI agent可能都不一樣 等一下下一頁投影片會告訴你說 我在這一堂課中指的AI agent是什麼,那如果你在其他地方聽過別的AI agent的定義,那也沒問題,我也不會爭論說什麼樣的定義,才是真正的AI agent的定義,有些人甚至會告訴你說,現在那些用大型語言模型驅動的號稱AI agent的東西都不是真正的AI agent,要有身體的像這個機器人一樣的才叫做AI agent,所以每個人心裡想像的AI agent是不一樣的, 好,那這一堂課我們要講的AI agent是什麼呢?今天我們使用AI的方式,通常是人類給一個明確的指令,你問AI說AI agent的翻譯是什麼,那AI呢,按…
2. `M2Yg1kwPpts:46-85` (`00:02:58.900–00:04:28.879`): Direct transcript evidence. 叫做action 那他執行個action以後 會影響環境的狀態 會看到不一樣的observation 就會執行不同的action 那這個步驟會一直循環 直到AI agent達成 我們要他達成的目標為止 那我只要講到這邊 你可能還覺得非常的抽象 那我們可以用下圍棋來舉例 那AlphaGo是大家非常熟悉的東西 AlphaGo其實也可以 看作是一個AI agent 這個AI agent的目標就是 下棋要贏 他的observation是什麼 他的observation是現在棋盤上 黑子跟白子的位置 現在棋盤上的盤式 那他可以採取的action是什麼 他可以採取的action 就是在棋盤上的19x19路的範圍中 選擇一個動作 選擇一個可以落子的位置 那他選擇完可以落子的位置 他落下一次以後 會改變他對手的輸出 你落下一隻以後 你的對手會落下另外一隻 那會改變你觀察到的observation 那你就要採取下一個action 所以Alpha…
3. `M2Yg1kwPpts:86-125` (`00:04:28.899–00:05:58.480`): Direct transcript evidence. reinforcement learning RL的課程 往往都是用這樣的方式來開場的 為什麼呢 因為過去要打造AI agent的時候 往往覺得就是要透過RL的演算法來打造AI agent 那怎麼透過RL的演算法來打造AI agent呢 RL這個演算法就是他可以去learn一個agent 那這個agent可以maximize reward 所以你要把你的目標呢 轉換成一個叫做reward的東西 那這個reward呢 是人定義的越接近 你的目標reward就越大 那如果在下圍棋裡面 你通常就會定說 贏棋reward就是正一 輸棋reward就是負一 然後你要訓練的那個AI agent 就會學習去maximize reward 透過RL的演算法 所以透過RL的演算法 其實你也有可能學一個AI agent 但是透過RL演算法的侷限是 你需要為每一個任務 都用RL的演算法 訓練一個模型 AlphaGo在經過了大量的訓練以後 他可以下圍…
4. `M2Yg1kwPpts:1322-1348` (`00:52:06.280–00:53:34.059`): Direct transcript evidence. 這段話,某年某月某日高雄氣溫如何,這個是User Prompt,那如果你有在使用這個ChatGPT的API的話,你知道你的輸入要分成System Prompt跟User Prompt,那很多同學會搞不清楚System Prompt跟User Prompt有什麼樣的差別,那System Prompt指的是說,你在開發應用的這個Developer下的這個Prompt,這個Prompt呢,是每次都是一樣的,每次你都想要放在語言模型最前面, 讓他去做文字接龍的這個敘述叫做System Prompt 那每次使用他的時候都不一樣 通常是這個服務的使用者輸入的內容叫做User Prompt 那在ChartGPT的API裡面 特別把System Prompt跟User Prompt分開 也是要分開輸入的 因為System Prompt跟User Prompt 他有不同的優先級 System Prompt他優先級比較高 如果System Pro…

## ASR observation

- None: selected evidence is from a verified official/auto transcript, not ASR output.

## Visual observation

- None requested: the selected transcript anchors support the bounded concept-routing claim; no formula, chart, code screen, or visual-only assertion is used.

## Inference

- The selector places this source in `llm_agent` as `PRIMARY`. This is a bounded source-set relation, not a formal mentor rule.

## Unknowns and limits

- The packet does not establish a universal architecture, algorithm, or performance conclusion.
- Selected chunks may omit counterexamples, task conditions, and empirical comparisons elsewhere in the video.

## De-duplication and cross-source relation

- Other selected sources for this concept: `VqB8zMujdjM` (PRIMARY), `bJZTJ7MjYqg` (CORROBORATING), `urwDLyNa9FU` (CORROBORATING).
- Cross-source synthesis is deferred to the concept dossier; duplicate or supporting sources remain in the coverage ledger rather than being re-distilled.
