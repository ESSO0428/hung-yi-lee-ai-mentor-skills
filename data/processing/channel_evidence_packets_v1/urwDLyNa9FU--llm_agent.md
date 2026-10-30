# Evidence Packet: urwDLyNa9FU / LLM／agent

- packet_id: `EVP-CHANNEL-urwDLyNa9FU-llm_agent-V1`
- packet_schema: `hung-yi-channel-evidence-packet.v1`
- packet_type: `EVIDENCE_PACKET_READY`
- video_id: `urwDLyNa9FU`
- source_url: https://www.youtube.com/watch?v=urwDLyNa9FU
- title: `AI Agent (1/3)：核心技術 Context Engineering 基本概念解說`
- transcript_type: `official`
- source_quality: `OFFICIAL`
- manifest_status: `VERIFIED`
- concept_id: `llm_agent`
- source_role: `CORROBORATING`
- source_scope: selective review of selector-approved transcript chunks; not full-video coverage and not a claim of full-video understanding

## Direct evidence

1. `urwDLyNa9FU:0-39` (`00:00:00.133–00:01:30.090`): Direct transcript evidence. 好，各位同學大家好啊 我們就開始來上課吧 今天呢，我們要繼續來講 AI Agent 那今天的課程呢 還是比較科普性的 那我們分成三個段落 第一段呢 我們來講 AI Agent 背後的核心技術 我們比較系統化地來講 Context Engineering 然後第二段呢 我們來講 AI Agent 之間的互動 然後最後我們來講 AI Agent 對於我們未來的工作 可能造成什麼樣的衝擊 那我們就先從 AI Agent 的核心技術 Context Engineering 開始講起 那等一下這段課程啊 也許你聽了會覺得似曾相識 因為很多呢 Context Engineering 的技術 都已經在這個 OpenClaw 裡面被實作 那今天這段課程比較不一樣的地方 是會引用大量的論文 那你發現這些論文都是非常新的論文 幾個月前、半年前的論文 而這些技術都已經被實作在 OpenClaw 裡面 所以上週其實很多技術我們都已經有提到 那只是今天…
2. `urwDLyNa9FU:85-124` (`00:02:58.044–00:04:27.200`): Direct transcript evidence. 那這裡會遇到的難點就是 語言模型的輸入長度是有限的 它不能夠吃無限長的輸入 這就是為什麼我們需要 AI Agent 就是攔截在語言模型跟人類 或者是語言模型要執行的環境之間的一個介面 它就像是語言模型的守門人 語言模型的經紀人 它決定語言模型會看到什麼 所以來自外界的輸入會經過 AI Agent 那這個 AI Agent 不一定是 OpenClaw 只是 AI Agent 的其中一個例子 那今天 OpenClaw 還非常的原始 你可以想成它是初代的 AI Agent 它也許在過幾年以後 我們再回頭看 OpenClaw 就好像今天你拿著 iPhone 去看過去的 Nokia 手機一樣的感覺 我們現在看到的只是 AI Agent 的原型 以後一定還會有更多的進展 那 OpenClaw 做的事情 或 AI Agent 做的事情 就是選擇給語言模型看的內容 所以語言模型真正看到的是 AutoGPT AI Agent 篩選過的長度合適的…
3. `urwDLyNa9FU:125-162` (`00:04:27.200–00:05:56.189`): Direct transcript evidence. 不能太長 也不能太短 而這個 AI Agent 幫語言模型管理它的輸入 讓輸入的長度是合適的 這件事情就叫做 Context Engineering 剛才是概念性的介紹 Context Engineering 如果我們今天要用 比較程式語言的方法來描述它的話 可能看起來像是這樣子的 現在左邊這段程式碼 是沒有做 Context Engineering 的狀況 其實沒有做 Context Engineering 的時候 你可以想成語言模型跟外界的互動 就是一個 for 迴圈 那這個 for 迴圈是從 1 到無限大 這個 1 要執行多少個 step 那這個取決於你想要讓語言模型運作多久 你想要讓這個 AI 運作多久 那我們希望它永遠地執行下去 執行到天荒地老 所以這邊放一個無限大 然後呢 這邊會有一個初始的輸入 那這個可能就是你給語言模型的指令 那今天這個指令甚至可以 就是一個非常 high level 的目標 比如說成為 You…
4. `urwDLyNa9FU:1524-1569` (`00:51:47.204–00:53:05.382`): Direct transcript evidence. 它就解不了了 這邊 All-Long 這些 benchmark 就是測試語言模型 在 context 非常長的情況下 它能不能夠好好的運作 但是加上它的 這個 Recursive Language Model 以後 因為它的 Recursive Language Model 是一個 context engineering 的方法 所以它可以外掛在 任何現有的語言模型上 所以如果外掛在 GPT-5 上 就可以讓本來 已經很厲害的 GPT-5 變得更厲害 在輸入真的非常長 比如說長達 1M 100 萬個 token 的時候 仍然可以在這一些 長 context 的 benchmark 上面 做出不錯的效果 總之呢 今天就是比較系統化的 跟大家介紹了 context engineering 那我們這邊有一個演算法 這個演算法 摘要了 context engineering 實際上做的事情 那我們也跟大家說 其實 context 分成…

## ASR observation

- None: selected evidence is from a verified official/auto transcript, not ASR output.

## Visual observation

- None requested: the selected transcript anchors support the bounded concept-routing claim; no formula, chart, code screen, or visual-only assertion is used.

## Inference

- The selector places this source in `llm_agent` as `CORROBORATING`. This is a bounded source-set relation, not a formal mentor rule.

## Unknowns and limits

- The packet does not establish a universal architecture, algorithm, or performance conclusion.
- Selected chunks may omit counterexamples, task conditions, and empirical comparisons elsewhere in the video.

## De-duplication and cross-source relation

- Other selected sources for this concept: `M2Yg1kwPpts` (PRIMARY), `VqB8zMujdjM` (PRIMARY), `bJZTJ7MjYqg` (CORROBORATING).
- Cross-source synthesis is deferred to the concept dossier; duplicate or supporting sources remain in the coverage ledger rather than being re-distilled.
