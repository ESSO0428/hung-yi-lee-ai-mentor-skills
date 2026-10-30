# Research Dossier: representation／pretraining／transfer

## Source Metadata

- Source: `3oHlf8-J3Nc` — 【機器學習2021】自編碼器 (Auto-encoder) (上) – 基本概念
- URL: https://www.youtube.com/watch?v=3oHlf8-J3Nc
- Source role: `PRIMARY`
- Source weight: 1
- Evidence packet: `EVP-CHANNEL-3oHlf8-J3Nc-representation_pretraining-V1` (data/processing/channel_evidence_packets_v1/3oHlf8-J3Nc--representation_pretraining.md)
- Transcript type: `official`; selector confidence: `HIGH`
- Source: `e422eloJ0W4` — 【機器學習2021】自督導式學習 (Self-supervised Learning) (一) – 芝麻街與進擊的巨人
- URL: https://www.youtube.com/watch?v=e422eloJ0W4
- Source role: `PRIMARY`
- Source weight: 1
- Evidence packet: `EVP-CHANNEL-e422eloJ0W4-representation_pretraining-V1` (data/processing/channel_evidence_packets_v1/e422eloJ0W4--representation_pretraining.md)
- Transcript type: `official`; selector confidence: `HIGH`
- Source: `MpsVE60iRLM` — SUPERB: 語音上的自督導式學習模型居然十項全能？
- URL: https://www.youtube.com/watch?v=MpsVE60iRLM
- Source role: `CORROBORATING`
- Source weight: 2
- Evidence packet: `EVP-CHANNEL-MpsVE60iRLM-representation_pretraining-V1` (data/processing/channel_evidence_packets_v1/MpsVE60iRLM--representation_pretraining.md)
- Transcript type: `official`; selector confidence: `HIGH`
- Source: `JZvEzb5PV3U` — 【機器學習2021】自編碼器 (Auto-encoder) (下) – 領結變聲器與更多應用
- URL: https://www.youtube.com/watch?v=JZvEzb5PV3U
- Source role: `CORROBORATING`
- Source weight: 2
- Evidence packet: `EVP-CHANNEL-JZvEzb5PV3U-representation_pretraining-V1` (data/processing/channel_evidence_packets_v1/JZvEzb5PV3U--representation_pretraining.md)
- Transcript type: `official`; selector confidence: `HIGH`

## Evidence

- `3oHlf8-J3Nc` (PRIMARY):
  - `3oHlf8-J3Nc:0-34` (`00:00:02.830–00:01:30.900`): 好 那個接下來我們要講 Auto-Encoder 那 Auto-Encoder 我們可能先講一小段以後 我們就下課休息一下 然後我再把 Auto-Encoder 的部分補完 然後等一下助教就會講 跟 Auto-Encoder 有關的作業 好 那我們來講 Auto-Encoder 那在講 Auto-Encoder 之前 其實 Auto-Encoder 也可以算是 Self-Supervised Learning 的一環 所以再讓我們用非常短的時間 來看一下Self-Supervised Learning 的 Framework 那 Self-Supervised Learning 是怎麼運作的 首先你有大量的沒有標註的資料 用這些沒有標註的資料 你可以去訓練一個模型 你必須發明一些不需要標註資料的任務 比如說做填空題 比如說預測下一個 Token 你必須要自己想一些不需要標註資料的任務 給你的模型進行學習 那這個不用標註資料的學…
  - `3oHlf8-J3Nc:35-70` (`00:01:30.900–00:02:59.000`): 在這些不用標註資料就可以學習的任務裡面 在有 BERT 在有 GPT 之前 其實有一個更古老的任務 更古老的不需要用標註資料的任務 就叫做 Auto-Encoder 所以你也可以把 Auto-Encoder 看作是 Self-Supervised Learning 的 一種 Pre-Train 的方法 當然可能不是所有人都會同意這個觀點 有人可能會說這個 Auto-Encoder 不算是 Self-Supervised Learning 這個 Auto-Encoder 很早就有了嘛 2006 年 15 年前就有了嘛 然後 Self-Supervised Learning 是 19 年才有這個詞彙嘛 所以 Auto-Encoder 不算 Self-Supervised Learning 的一環 那這個都是見仁見智的問題 這種名詞定義的問題 真的我們就不用太糾結在這個地方 從 Self-Supervised Learning 它是…
  - `3oHlf8-J3Nc:433-467` (`00:17:40.040–00:18:49.580`): BERT 的模型就是 Encoder 它的輸出就是 Embedding 在講 BERT 的技術的時候 我們就告訴你說這個輸出就叫做 Embedding 接下來有一個 Linear 的模型 就是 Decoder 要做的事情 就是還原原來的句子 也就是把填空題被蓋住的地方 把它還原回來 所以我們可以說 BERT 其實就是一個 De-Noising 的 Auto-Encoder 有同學可能會問說 為什麼這個 Decoder 一定要 Linear 的呢 它不一定要是 Linear 它可以不是 Linear 或者是我們換一個說法 這個 BERT 它有 12 層 最小的那個 BERT 有 12 層 比較大的有 24 層或者是 48 層 好 那最小的 BERT 是 12 層 如果我們說這個 12 層中間 第 6 層的輸出是 Embedding 那你其實也可以說剩下的 6 層 就是 Decoder 你可以說 BERT 就假設你在用 BERT…
- `e422eloJ0W4` (PRIMARY):
  - `e422eloJ0W4:0-34` (`00:00:02.310–00:01:31.120`): 好 我們就講下一個主題 我們接下來要講的主題呢 叫做Self-Supervised Learning 在講self-supervised learning之前呢 就不能不介紹一下芝麻街 為什麼呢 因為不知道為什麼 self-supervised learning的模型 都是以芝麻街的人物命名 我今天特別穿了芝麻街的T-shirt 給大家看一下 芝麻街的T shirt 看不清楚的同學呢 或線上的同學呢 這個照片在這邊是同一件 這個是我本人 然後這個這些角色就是芝麻街的角色 這些芝麻街的角色 都是些什麼樣的模型呢 我們先來看看他們的名字 讓我們實際了解他們做的事情之前 先來認識他們的名字 這一個紅色的怪物叫做ELMO self-supervised learning裡面 有一個模型叫做 Embeddings from Language Modeling 它是最早的self-supervised learning的model 它的縮…
  - `e422eloJ0W4:35-69` (`00:01:31.120–00:03:00.240`): 有了兩個芝麻街的人物以後 Bert他最好的朋友就是這一隻 他是誰呢 他叫做ERNIE 那事實上有了Bert以後 馬上就出現了兩個不同的模型 都叫做ERNIE 其中的模型縮寫是這樣啦 Enhanced Representation from Knowledge Integration 然後它的縮寫是ERNIE 我就問說現在縮寫這樣都可以了嗎 你根本就只是想要叫做ERNIE而已啊 你可能以為這個已經很荒唐了 但是後來這一隻動物 他叫做大鳥 Big Bird 就有一個模型叫做Big Bird Transformers for Longer Sequences 現在完全要放棄要湊字了 已經要放棄要湊出一樣的名字了 直接就把它叫做Big Bird就結束了 所以我們現在在這個 self-supervised learning的model裡面 都有一堆芝麻街的人物 Cookie Monster還沒有人去湊他啦 就等著你來湊Cookie Mo…
- `MpsVE60iRLM` (CORROBORATING):
  - `MpsVE60iRLM:0-29` (`00:00:01.720–00:01:30.900`): 好 大家好 我今天要來跟大家介紹 SUPERB 這個計畫 這個 SUPERB 是語音的自督導式學習計畫 好 那在 SUPERB 這個 Project 裡面 我們要做些什麼呢 那我們先從這個自督導式學習 怎麼被用在語音上開始說起 那這個自督導式學習 那想必大家也不太陌生 那如果你有上 我的 Machine Learning 的課程的話 那在課程中一定已經聽過 BERT 這個東西 BERT 是訓練在文字上的 Self-Supervised Learning 自督導式學習的模型 那如果你有在做 Computer Vision 相關的東西的話 那你一定聽過 SimCLR 是影像上的自督導式學習模型 那在語音上的進展又是如何呢 那我今天就想跟大家分享一下 語音上最新的 Self-Supervised Learning 的進展 好 那在開始之前 我們還是講一下 Self-Supervised Learning 的 Framework 那我…
  - `MpsVE60iRLM:66-99` (`00:03:00.700–00:04:28.900`): 那這邊就不一一列舉 那最有趣的地方是 當我們在做這個 Pre-Train 的時候 這個第一階段的 Training 它是 Task-Agnostic 也就是說 我們在做第一階段 Training 的時候 我們並不知道這個 Upstream 的模型 接下來會被用在什麼應用上 這個訓練是 Task-Agnostic 在訓練的時候 我們只使用了大量沒有標註的資料 來訓練出這個模型 那至於這個模型 接下來要怎麼被用在其他的應用中 我們是不知道的 那在今天這個 Talk 裡面 我們把這個透過大量未標註資料 在 Phase 1 所訓練出來的模型 叫做 Upstream Model 那你也可能在其他的文獻上 看到其他的稱呼 比如說有人會叫做 Self-Supervised 的 Model 然後最近有另外一個很紅的詞 叫做 Foundation Model 指的也是 Upstream 的 Model 好 在語音上 像這一種 Upstream…
- `JZvEzb5PV3U` (CORROBORATING):
  - `JZvEzb5PV3U:37-76` (`00:01:29.950–00:02:59.410`): 那如果今天是一篇文章 丟到 Encoder 裡面變成向量 這個向量通過 Decoder 會變回原來的文章 那這個向量裡面有什麼 它可能包含文章裡面 文句的句法的資訊 也包含了語意的資訊 但是這些資訊是全部糾纏在一個向量裡面 我們並不知道一個向量的哪些維 代表了哪些資訊 舉例來說 如果我們今天把一段聲音訊號丟進 Encoder 它會給我們一個向量 但是這個向量裡面 哪些維度代表了這句話的內容 哪些維度代表這句話的語者 也就是誰說的 我們沒有這樣的資訊 而 Feature Disentangle 想要做到的事情就是 我們有沒有可能想辦法 在 Train 一個 Aauto-Encoder 的時候 同時有辦法知道 這個 Representation 或又叫做 Embedding 或又叫做 Code 它們是一樣的東西 我們這個 Embedding 的哪些維度 代表了哪些資訊呢 我們有沒有可能做到說 Encoder 輸出一個 舉例來說 1…
  - `JZvEzb5PV3U:240-282` (`00:08:55.070–00:10:24.480`): 它就代表了某種特徵的有或者是沒有 舉例來說 輸入的這張圖片 如果是女生 可能第一維就是 1 男生第一維就是 0 如果有戴眼鏡 就是第三維 1 沒有戴眼鏡 就是第三維是 0 也許我們把這個向量 這個 Embedding 變成 Binary 變成只有 0 跟 1 的數字 可以讓我們再解釋 Encoder 輸出的時候 更為容易 甚至有沒有可能這個向量 強迫它一定要是 One-Hot 呢 也就只有一維是 1 其他就是 0 如果我們強迫它是 One-Hot 也就是每一個東西圖片丟進去 你只可以有 你的 Embedding 裡面只可以有一維是 1 其他都是 0 的話 那可以做到什麼樣的效果呢 也許可以做到 unSupervised 的分類 舉例來說 假設你有一大堆的 假設你想要做那個手寫數字辨識 你有 0 到 9 的圖片 你把 0 到 9 的圖片統統蒐集起來 Train 一個這樣子的 Aauto-Encoder 然後強迫中間的 Laten…

## Patterns and Repeated Themes

- 多個獨立來源均提供 `representation_pretraining` 的 selector-approved transcript anchors；可把它們用於受限的 cross-source candidate synthesis。

## Contradictions

- 來源跨年份、模態與任務；它們的共同概念不等於共同的 benchmark、資料分布或性能結論。

## Inferences

- Candidate inference (not formal): 預訓練／自監督表徵的價值要在下游遷移條件下驗證：區分 pretext task、資料分布、frozen versus fine-tuned 使用方式與實際下游任務。
- Candidate decision rule: 至少比較從零訓練、frozen representation 與 fine-tuning；固定下游資料切分，分開報告資料量、domain shift、任務類型與每一種 adaptation 的結果。

## Gaps and Missing Information

- 未使用未選定的片段、影格或投影片；若未來某個結論需要公式、圖表或程式畫面，必須建立獨立 visual-evidence request。
- 本 dossier 是 Distilly research input，不取代原始影片、source chunks 或 evidence packets。
