# Evidence Packet: 1UqCjFQiiy0 / optimization／training paradigm

- packet_id: `EVP-CHANNEL-1UqCjFQiiy0-optimization_training-V1`
- packet_schema: `hung-yi-channel-evidence-packet.v1`
- packet_type: `EVIDENCE_PACKET_READY`
- video_id: `1UqCjFQiiy0`
- source_url: https://www.youtube.com/watch?v=1UqCjFQiiy0
- title: `ML Lecture 1: Regression - Demo`
- transcript_type: `official`
- source_quality: `OFFICIAL`
- manifest_status: `VERIFIED`
- concept_id: `optimization_training`
- source_role: `PRIMARY`
- source_scope: selective review of selector-approved transcript chunks; not full-video coverage and not a claim of full-video understanding

## Direct evidence

1. `1UqCjFQiiy0:0-6` (`00:00:00.000–00:00:20.865`): Direct transcript evidence. 臺灣大學人工智慧中心 科技部人工智慧技術暨全幅健康照護聯合研究中心 http://ai.ntu.edu.tw 那我們在前一堂課看了regression， 我們知道怎麼用gradient descent來找出regression model的參數 這個聽起來還滿容易的。 接下來，我就舉個例子， 讓大家知道實際在做regression的時候， 你會碰到甚麼樣的困難。
2. `1UqCjFQiiy0:7-30` (`00:00:24.855–00:01:52.265`): Direct transcript evidence. 這邊我們假設x data有10筆， y data也有10筆。 那x和y之間的關係， 是ydata= b+w*xdata 那b和w都是參數， 我們用gradient descent把b和w找出來。 我當然知道說今天這個問題有closed-form solution， 這個b和w有更好的方法可以找出來， 那我們假裝不知道這件事， 我們要練習用gradient descent把b和w找出來。 那怎麼做呢? gradient descent其實非常的簡單， 所以這邊我們不需要說太多。 這個程式碼還沒有超過20行。 我們先給b一個初始值， 這邊b的初始值是 -120， 我們給w一個初始值， 這邊w的初始值是-4， 我們需要一個learning rate，那learning rate我們就給他一個很小的數字 iteration就設100000個 那在每一個iteration裡面， 我們要做的事是，計算出b和w對loss的偏微分， 計算的式…
3. `1UqCjFQiiy0:59-65` (`00:03:37.735–00:04:00.345`): Direct transcript evidence. 這是learning rate 調大10倍後的結果， 你發現說最後，經過100000次參數的update以後 我們的參數在這個地方， 離最佳解稍微近了一點， 不過這邊有一個劇烈的震盪的現象發生。 那我們再把learning rate稍微設大一點， 我們設再大10倍，
4. `1UqCjFQiiy0:102-106` (`00:06:36.665–00:06:52.600`): Direct transcript evidence. 你會發現說有了新的learning rate以後， 從初始的值到終點， 我們就可以很順利的在十萬次update參數之內，走到我們的終點了 我們就可以很順利的在十萬次update參數之內，走到我們的終點了 臺灣大學人工智慧中心 科技部人工智慧技術暨全幅健康照護聯合研究中心 http://ai.ntu.edu.tw

## ASR observation

- None: selected evidence is from a verified official/auto transcript, not ASR output.

## Visual observation

- None requested: the selected transcript anchors support the bounded concept-routing claim; no formula, chart, code screen, or visual-only assertion is used.

## Inference

- The selector places this source in `optimization_training` as `PRIMARY`. This is a bounded source-set relation, not a formal mentor rule.

## Unknowns and limits

- The packet does not establish a universal architecture, algorithm, or performance conclusion.
- Selected chunks may omit counterexamples, task conditions, and empirical comparisons elsewhere in the video.

## De-duplication and cross-source relation

- Other selected sources for this concept: `yKKNr-QKz2Q` (PRIMARY), `e03YKGHXnL8` (CORROBORATING), `BABPWOkSbLE` (CORROBORATING).
- Cross-source synthesis is deferred to the concept dossier; duplicate or supporting sources remain in the coverage ledger rather than being re-distilled.
