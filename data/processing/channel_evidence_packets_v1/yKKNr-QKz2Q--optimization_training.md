# Evidence Packet: yKKNr-QKz2Q / optimization／training paradigm

- packet_id: `EVP-CHANNEL-yKKNr-QKz2Q-optimization_training-V1`
- packet_schema: `hung-yi-channel-evidence-packet.v1`
- packet_type: `EVIDENCE_PACKET_READY`
- video_id: `yKKNr-QKz2Q`
- source_url: https://www.youtube.com/watch?v=yKKNr-QKz2Q
- title: `ML Lecture 3-1: Gradient Descent`
- transcript_type: `official`
- source_quality: `OFFICIAL`
- manifest_status: `VERIFIED`
- concept_id: `optimization_training`
- source_role: `PRIMARY`
- source_scope: selective review of selector-approved transcript chunks; not full-video coverage and not a claim of full-video understanding

## Direct evidence

1. `yKKNr-QKz2Q:1-24` (`00:00:20.820–00:01:49.320`): Direct transcript evidence. 好，各位同學大家早 那我們就開始上課吧！ 今天的第一堂課，我們要講的是 Gradient Descent 我們上次已經大概講過怎麼做了 但是有一些小技巧呢，你可能是不知道的 所以我們要再詳細說明一下，Gradient Descent 你要怎麼把它做得更好 好，那我們上次是這樣說的 在整個 machine learning 的第3個步驟 我們要找一個最好的 function 那找一個最好的 function 這件事呢 是要解一個 optimization 的 problem 也就是說，在第二步， 我們先定了一個 loss function： L 這個 loss function 呢，它是一個 functional unction 你把一個 function 代到這個 loss function 裡面 或者是你把一個操控 function 形狀的參數 我們現在，在這張投影片裡面，把那些參數寫成 θ L 是 loss functio…
2. `yKKNr-QKz2Q:25-48` (`00:01:49.320–00:03:18.840`): Direct transcript evidence. 當然你也可以反過來定義一個 function 是 參數越好，它 output 的值越大 那這時候就不會叫它 loss function，就會叫他別的名字 比如說，叫它 objective function 好，這邊應該是 minimum 我們要找一組參數 θ，讓這個 loss function 越小越好 那這件事情怎麼做呢？ 我們可以用 Gradient Descent 假設現在這個 θ 是一個參數的 set 那裡面有兩個參數：θ1 跟 θ2 首先，你先隨機的選取一個起始的點 隨機選取一組起始的參數 這邊寫成 θ(上標0, 下標1)、θ(上標0, 下標2) 用上標 0 來代表說，它是初始的那一組參數 那用下標代表說 這個是這一組參數裡面的 第 1 個 component 跟第 2 個 component 接下來，你計算 θ(上標0, 下標1) 跟 θ(上標0, 下標2) 對這個 loss function 的偏微分 計算他們的…
3. `yKKNr-QKz2Q:531-554` (`00:33:04.400–00:34:33.840`): Direct transcript evidence. 那接下來呢，你在 update 參數的時候 你只考慮那一個 example 我們只考慮一個 example 的 loss function，我們就寫成 L^n，代表它是考慮第 n 個 example 的 loss function 那你在算 Gradient 的時候呢？ 你不是算對 total 所有的 data，它的 Gradient 的和 你只算對某一個 example，它的 loss 的 Gradient 然後呢，你就很急躁的 update 參數了 所以在原來的 Gradient Descent 裡面， 你計算所有 data 的 loss 然後才 update 參數 但是在 Stochastic Gradient Descent 裡面 你看一個 example，就 update 一個參數這樣 你可能想說，這有啥好呢？ 聽起來好像沒有甚麼好的 那我們實際來操作一下好了 剛才看到圖呢，它可能是這個樣子的 我們剛才看到的圖呢，它…
4. `yKKNr-QKz2Q:973-985` (`01:01:13.440–01:01:51.800`): Direct transcript evidence. 在 local minimum 附近，所以你就停下來了 因為你們真的很少有機會 exactly 微分值算出來是 0 嘛 對不對，你可能覺得說， 微分算出來很小，就很接近 local minimum 你就把它停下來，那其實搞不好，它是一個高原的地方 它離那個 local minimum 還很遠啊 這也是有可能的 講到這邊，有人都會問我一個問題 這個問題，我很難回答，他說 你怎麼會不知道你是不是接近 local minimum 了呢？ 我一眼就知道說 local minimum 在這邊阿 呵呵，你怎麼會不知道呢？ 所以我覺得這些圖都沒有辦法 表示 Gradient Descent 的精神 臺灣大學人工智慧中心 科技部人工智慧技術暨全幅健康照護聯合研究中心

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

- Other selected sources for this concept: `1UqCjFQiiy0` (PRIMARY), `e03YKGHXnL8` (CORROBORATING), `BABPWOkSbLE` (CORROBORATING).
- Cross-source synthesis is deferred to the concept dossier; duplicate or supporting sources remain in the coverage ledger rather than being re-distilled.
