# Evidence Packet: e03YKGHXnL8 / optimization／training paradigm

- packet_id: `EVP-CHANNEL-e03YKGHXnL8-optimization_training-V1`
- packet_schema: `hung-yi-channel-evidence-packet.v1`
- packet_type: `EVIDENCE_PACKET_READY`
- video_id: `e03YKGHXnL8`
- source_url: https://www.youtube.com/watch?v=e03YKGHXnL8
- title: `[TA 補充課] Optimization for Deep Learning (2/2) (由助教簡仲明同學講授)`
- transcript_type: `official`
- source_quality: `OFFICIAL`
- manifest_status: `VERIFIED`
- concept_id: `optimization_training`
- source_role: `CORROBORATING`
- source_scope: selective review of selector-approved transcript chunks; not full-video coverage and not a claim of full-video understanding

## Direct evidence

1. `e03YKGHXnL8:1-23` (`00:00:27.242–00:01:55.568`): Direct transcript evidence. 那我們從這邊繼續 好我們剛剛講到，複習一下剛剛講過的東西 我們複習了 前面李宏毅老師講過的一些比較有名的算法 裡面包括最常用的兩個，就是 HGD with momentum 還有 adam 這兩個算法 然後這兩個算法優點跟缺點有什麼 HGD 通常他比較穩 然後收斂的比較好 但是 adam 他算的比較快 所以我們一般在做的時候也都是以這兩個 optimizer 為主 接下來我們介紹了一些做法可能來修正他們的一些問題 希望他們可以改進這兩個算法，讓他們互相向對方學習 那這些裡面有包括 adabound、包括 AMSGrad 這兩個算法是改善 adam 的算法 那他們在想的是，因為你的 learning rate 有可能會太大或者是太小 那他們用一些方法來避免掉這樣的情況 讓 adam 在最後比較穩一點 不然如果你一下 learning rate 一下太大一下太小，那 adam 最後收斂的時候就會不穩 他們覺得這可能是 adam 比…
2. `e03YKGHXnL8:24-41` (`00:01:55.568–00:03:21.271`): Direct transcript evidence. 那這些都是希望去透過一個人工的方式來訂出一個調整 learning rate 的方法 讓 HGDM 可以收斂的比較快 不用在那邊慢慢的等他收斂 好那我們剛剛講到最後的 one cycle LR 他其實是由三個部分組成的 第一個部分是 warm-up 然後再來 annealing 還有最後的 fine-tuning 那我們就想到，那 adam 需要這個東西嗎 就是我們需不需要一開始先減低 adam 的 learning rate，後來再增加他 結果是，會這樣問結論一點是當然需要嘛 那為什麼需要？有人可能會想說 Adam 一開始不就已經做了 adaptive learning rate 嗎 那為什麼我們還需要去調整這個東西 原因是這樣的 因為這是在實際做實驗做出來的，在一個機器翻譯的實驗做出來的結果 那你就可以看到這幾張圖的縱軸是 iterration 然後橫軸是 gradient 的 distribution 那一開始看起來 g…
3. `e03YKGHXnL8:42-60` (`00:03:21.271–00:04:48.569`): Direct transcript evidence. 然後最後這邊有一堆幾乎沒有 gradient 的 parameter 好那再把它放大一點來看 我們突然發現前面幾個 time step 好像 它的分布跟人家不大一樣 然後那為什麼他們的分佈會跟人家不大一樣呢 原因是這樣，因為你一開始剛開始訓練的時候 你的 initialization 的時候，你不知道你 initial 在哪個地方 所以一開始的幾個 time step 他有可能 gradient 會很亂 再加上你一開始的時候，因為你那個底下的分母 他的估計可能不會估計得很準，因為那個 EMA， square of gradient 的估計 他一定是你在做了愈多 time step 以後 他的估計才會愈來愈準 所以一開始那個 learning rate 的估計不準 所以他有可能會一下走太多一下走太少 所以他整體來說就不穩嘛 那不穩的話他的 gradient 當然也會分佈的比較亂一點 所以這就是為什麼我們需要 warm-up 的原…

## ASR observation

- None: selected evidence is from a verified official/auto transcript, not ASR output.

## Visual observation

- None requested: the selected transcript anchors support the bounded concept-routing claim; no formula, chart, code screen, or visual-only assertion is used.

## Inference

- The selector places this source in `optimization_training` as `CORROBORATING`. This is a bounded source-set relation, not a formal mentor rule.

## Unknowns and limits

- The packet does not establish a universal architecture, algorithm, or performance conclusion.
- Selected chunks may omit counterexamples, task conditions, and empirical comparisons elsewhere in the video.

## De-duplication and cross-source relation

- Other selected sources for this concept: `1UqCjFQiiy0` (PRIMARY), `yKKNr-QKz2Q` (PRIMARY), `BABPWOkSbLE` (CORROBORATING).
- Cross-source synthesis is deferred to the concept dossier; duplicate or supporting sources remain in the coverage ledger rather than being re-distilled.
