# Evidence Packet: z95ZYgPgXOY / reinforcement learning

- packet_id: `EVP-CHANNEL-z95ZYgPgXOY-reinforcement_learning-V1`
- packet_schema: `hung-yi-channel-evidence-packet.v1`
- packet_type: `EVIDENCE_PACKET_READY`
- video_id: `z95ZYgPgXOY`
- source_url: https://www.youtube.com/watch?v=z95ZYgPgXOY
- title: `DRL Lecture 1: Policy Gradient (Review)`
- transcript_type: `official`
- source_quality: `OFFICIAL`
- manifest_status: `VERIFIED`
- concept_id: `reinforcement_learning`
- source_role: `PRIMARY`
- source_scope: selective review of selector-approved transcript chunks; not full-video coverage and not a claim of full-video understanding

## Direct evidence

1. `z95ZYgPgXOY:2-16` (`00:00:36.040–00:02:02.620`): Direct transcript evidence. 那今天這一堂課，我們要講什麼呢？ 我們要講一個 policy gradient 的進階版 這個技術呢，叫做 Proximal Policy Optimization (PPO) 這個技術有多屌呢？這個技術呢， 它是 default reinforcement learning algorithm at OpenAI 是OpenAI 把這個方法， 當作他們 default reinforcement learning algorithm 所以今天假設你要 implement reinforcement learning，也許這是一個第一個你可以嘗試的方法，這是 PPO 今天這門課呢， 我們還是幫大家複習一下 Policy Gradient 這部分也許有點快，所以如果你有問題的話， 你就直接舉手打斷我 接下來，我們會講說，原來的 policy gradient， 是 On-Policy 的方法 那怎麼從 on-policy 的方法…
2. `z95ZYgPgXOY:29-47` (`00:06:00.480–00:07:27.280`): Direct transcript evidence. 那我們就來先複習一下 policy gradient，PPO 是 policy gradient 一個變形 所以我們先講 policy gradient 在 reinforcement learning 裡面呢有 3 個 components 一個 actor，一個 environment，一個 reward function 在我們作業 4-1 裡面呢，就是要做 讓機器玩 video game，那這個時候你 actor 做的事情 就是去操控，遊戲的搖桿， 比如說向左向右，開火，等等， 你的 environment 就是遊戲的主機， 負責控制遊戲的畫面 負責控制說，怪物要怎麼移動， 你現在要看到什麼畫面，等等 所謂的 reward function，就是決定，當你做什麼事情，發生什麼狀況的時候 你可以得到多少分數， 比如說殺一隻怪獸，得到20 分等等 那同樣的概念，用在圍棋上也是一樣 actor 就是 alpha Go，它要決…
3. `z95ZYgPgXOY:469-478` (`00:45:03.800–00:45:48.100`): Direct transcript evidence. 那它的意義就是，現在假設，我們在某一個 state st，執行某一個 action at 相較於其他可能的 action，它有多好 它真正在意的不是一個絕對的好， 而是說在同樣的 state 的時候 是採取某一個 action at，相較於其它的 action 它有多好，它是相對的好， 不是絕對好，那麼今天會減掉一個 b 嘛 減掉一個 baseline， 所以這個東西是相對的好，不是絕對的好 那這個 A 我們之後再講， 它通常可以是由一個 network estimate 出來的 那這個 network 叫做 critic， 我們講到 Actor-Critic 的方法的時候，再講這件事情 臺灣大學人工智慧中心 科技部人工智慧技術暨全幅健康照護聯合研究中心 http://aintu.tw

## ASR observation

- None: selected evidence is from a verified official/auto transcript, not ASR output.

## Visual observation

- None requested: the selected transcript anchors support the bounded concept-routing claim; no formula, chart, code screen, or visual-only assertion is used.

## Inference

- The selector places this source in `reinforcement_learning` as `PRIMARY`. This is a bounded source-set relation, not a formal mentor rule.

## Unknowns and limits

- The packet does not establish a universal architecture, algorithm, or performance conclusion.
- Selected chunks may omit counterexamples, task conditions, and empirical comparisons elsewhere in the video.

## De-duplication and cross-source relation

- Other selected sources for this concept: `tnPVcec22cg` (PRIMARY), `j82QLgfhFiY` (CORROBORATING).
- Cross-source synthesis is deferred to the concept dossier; duplicate or supporting sources remain in the coverage ledger rather than being re-distilled.
