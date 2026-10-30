# Evidence Packet: OP5HcXJg2Aw / CNN／RNN／inductive bias

- packet_id: `EVP-CHANNEL-OP5HcXJg2Aw-cnn_rnn_inductive_bias-V1`
- packet_schema: `hung-yi-channel-evidence-packet.v1`
- packet_type: `EVIDENCE_PACKET_READY`
- video_id: `OP5HcXJg2Aw`
- source_url: https://www.youtube.com/watch?v=OP5HcXJg2Aw
- title: `【機器學習2021】卷積神經網路 (Convolutional Neural Networks, CNN)`
- transcript_type: `official`
- source_quality: `OFFICIAL`
- manifest_status: `VERIFIED`
- concept_id: `cnn_rnn_inductive_bias`
- source_role: `CORROBORATING`
- source_scope: selective review of selector-approved transcript chunks; not full-video coverage and not a claim of full-video understanding

## Direct evidence

1. `OP5HcXJg2Aw:0-28` (`00:00:00.200–00:01:28.400`): Direct transcript evidence. 我們要來講 Network 的架構 我們開始探討 Network 的架構設計 那我第一個跟大家講的 Network 架構的變形呢 是 Convolutional 的 Neural Network 它的縮寫呢 就是 CNN 那這個 CNN 啊 它是專門被用在影像上的 我希望透過 CNN 這個例子 來讓你知道說 Network 的架構 它的設計有什麼樣的想法 那為什麼設計 Network 的架構 可以讓我們的 Network 結果做得更好 好 我們接下來要講的例子是跟影像有關的 我們今天就想像說 我們要做影像的分類 也就是給機器一張圖片 它要去決定說這張圖片裡面有什麼樣的東西 好 那怎麼做呢 我們已經跟大家講過怎麼做分類這件事情 在以下的討論裡面 我們都假設我們的模型輸入的圖片大小 是固定的 舉例來說 它固定輸入的圖片大小 都是 100 × 100 的解析度 我們假設說不會突然出現大小不一的照片 即使今天一般在做影像辨識的時候 往…
2. `OP5HcXJg2Aw:674-712` (`00:28:03.660–00:29:33.130`): Direct transcript evidence. 就是 CNN 所以從這個圖上啊 你可以很明顯地知道說 其實 CNN 它的 Bias 比較大 它的 Model 的 Bias 比較大 那你可能會想說 有 Model Bias 比較大 不是一件壞事嗎 Model Bias 大 不一定是壞事 因為當 Model Bias 小 Model 的 Flexibility 很高的時候 它比較容易 Overfitting Fully Connected Layer 它可以做各式各樣的事情 它可以有各式各樣的變化 但是它可能沒有辦法在 任何特定的任務上做好 而 Convolutional Layer 它是專門為影像設計的 剛才講的 Receptive Field 參數共享 這些觀察 都是為影像設計的 那因為 Convolutional Layer 是特別為影像設計的 所以它在影像上仍然可以做得好 雖然它的 Model Bias 很大 但這個在影像上不是問題 但是如果它用在影像之外的任務 那你就…
3. `OP5HcXJg2Aw:1372-1399` (`00:54:38.110–00:55:38.820`): Direct transcript evidence. 但對 CNN 的 Network 來說它是非常不一樣 所以事實上 CNN 並不能夠處理影像放大縮小 或者是旋轉的問題 當它今天在某種大小的影像上 假設你裡面的物件都是比較小的 它在上面學會做影像辨識 你把物件放大它就會整個慘掉 所以 CNN 並沒有你想像的那麼強 那就是為什麼在做影像辨識的時候 往往都要做 Data Augmentation 所謂 Data Augmentation 的意思就是說 你把你的訓練資料 每張圖片都裡面截一小塊出來放大 讓 CNN 有看過不同大小的 Pattern 然後把圖片旋轉 讓它有看過說 某一個物件旋轉以後長什麼樣子 CNN 才會做到好的結果 那你說 欸 CNN 這個不能夠處理 Scaling 跟 Rotation 的問題啊 那有沒有什麼 Network 架構 是可以處理這個問題呢 其實有的 有一個架構叫 Special Transformer Layer 我們不會講它 就把它的這個錄影的連結放…

## ASR observation

- None: selected evidence is from a verified official/auto transcript, not ASR output.

## Visual observation

- None requested: the selected transcript anchors support the bounded concept-routing claim; no formula, chart, code screen, or visual-only assertion is used.

## Inference

- The selector places this source in `cnn_rnn_inductive_bias` as `CORROBORATING`. This is a bounded source-set relation, not a formal mentor rule.

## Unknowns and limits

- The packet does not establish a universal architecture, algorithm, or performance conclusion.
- Selected chunks may omit counterexamples, task conditions, and empirical comparisons elsewhere in the video.

## De-duplication and cross-source relation

- Other selected sources for this concept: `lluMBz5AoOg` (PRIMARY), `xCGidAeyS4M` (PRIMARY), `gjsdVi90yQo` (CORROBORATING).
- Cross-source synthesis is deferred to the concept dossier; duplicate or supporting sources remain in the coverage ledger rather than being re-distilled.
