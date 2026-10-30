# Research Dossier: speech／multimodal

## Source Metadata

- Source: `CbIPjrOj2Tc` — 【生成式人工智慧與機器學習導論2025】第 10 講：語音語言模型發展史 (本課程前段內容為歷史回顧，2025 年的技術從 1:42:00 開始)
- URL: https://www.youtube.com/watch?v=CbIPjrOj2Tc
- Source role: `PRIMARY`
- Source weight: 1
- Evidence packet: `EVP-CHANNEL-CbIPjrOj2Tc-speech_multimodal-V1` (data/processing/channel_evidence_packets_v1/CbIPjrOj2Tc--speech_multimodal.md)
- Transcript type: `official`; selector confidence: `HIGH`
- Source: `AihBniegMKg` — 【生成式AI】生成式學習的兩種策略：要各個擊破，還是要一次到位
- URL: https://www.youtube.com/watch?v=AihBniegMKg
- Source role: `PRIMARY`
- Source weight: 1
- Evidence packet: `EVP-CHANNEL-AihBniegMKg-speech_multimodal-V1` (data/processing/channel_evidence_packets_v1/AihBniegMKg--speech_multimodal.md)
- Transcript type: `official`; selector confidence: `HIGH`
- Source: `MpsVE60iRLM` — SUPERB: 語音上的自督導式學習模型居然十項全能？
- URL: https://www.youtube.com/watch?v=MpsVE60iRLM
- Source role: `CORROBORATING`
- Source weight: 2
- Evidence packet: `EVP-CHANNEL-MpsVE60iRLM-speech_multimodal-V1` (data/processing/channel_evidence_packets_v1/MpsVE60iRLM--speech_multimodal.md)
- Transcript type: `official`; selector confidence: `HIGH`
- Source: `CgQ3lUOpXgc` — GPT-4o 背後可能的語音技術猜測
- URL: https://www.youtube.com/watch?v=CgQ3lUOpXgc
- Source role: `CORROBORATING`
- Source weight: 2
- Evidence packet: `EVP-CHANNEL-CgQ3lUOpXgc-speech_multimodal-V1` (data/processing/channel_evidence_packets_v1/CgQ3lUOpXgc--speech_multimodal.md)
- Transcript type: `official`; selector confidence: `HIGH`

## Evidence

- `CbIPjrOj2Tc` (PRIMARY):
  - `CbIPjrOj2Tc:125-171` (`00:04:26.432–00:05:54.954`): 用不同的名字做一下區隔 比如說有人會說這個 Command Mode 的模型啊 它叫做 Speech Aware Language Model 這是個 Language Model 但是它聽得懂聲音 所以叫做 Speech Aware 的 Language Model 總之這邊用詞呢 還沒有統一起來 從這個部分你可以 從這個現象你可以看出來說 這是一個非常新的技術 所以大家都還在摸索的階段 所以在詞彙的應用上面還非常的混亂 那這是一個新的技術 剛開始發展的時候 常常會有的一個現象 那另外一個要強調的就是 語音語言模型 我們這邊所討論的語音語言模型 並不是語音合成 並不是 TTS 今天當你對一個 Dialog Mode 的語音語言模型 Speech Language Model 說 How are you 的時候 它並不是複述你說的話 而是它會回答你 它會說 I'm fine 那如果是 TTS 的話 你是輸入一段文字 比如說你輸…
  - `CbIPjrOj2Tc:172-217` (`00:05:54.954–00:07:23.042`): 做一個語音語言模型 它明明是一個對話的模型 投稿到國際會議 Reviewer 就舉一大堆 TTS 的模型說 為什麼不跟這些比 那不一樣的東西 有什麼好比的 但是這個因為現在語音語言模型呢 這個用詞用的非常的混亂 所以很多人會誤以為 你在你在做語音語言 你說你在做語音語言模型的時候 很多人會誤以為 你做的是 TTS 那很多人會看到一篇 TTS 的文章 以為那是一個語音語言模型 總之這邊的用詞非常的混亂 但我這邊就是要強調說 等一下要講的是這種 可以對話的語音語言模型 它做的事情是回應你的輸入 好那要做一個這個語音語言模型 它可以輸一段聲音 給你一個回覆 那好像也不一定要用一個 End-to-End 的方法 那等一下我們今天這堂課呢 主要要探討的都是 End-to-End 的方法 也就是我們有一個模型 它直接拿聲音當做輸入 直接拿聲音當做輸出 但我相信你一定可以非常輕易的 想出一些不是 End-to-End 的做法 比如說我們可以…
  - `CbIPjrOj2Tc:218-254` (`00:07:23.042–00:08:50.963`): 這個回覆再用語音合成把它唸出來 你也可以得到一個系統 它是輸入語音輸出語音 那事實上呢 今天多數你看到的號稱是語音輸入語音輸出的系統 往往用的是這種 Cascade Solution 其實今天語音對話對你來說可能沒有那麼稀奇 台大圖書館門口呢 就有一個可以用語音對話的數字人在那裡 那但是這種數字人 通常它用的就是 Cascade Model 把語音辨識加文字模型 再加語音合成三個串起來 變成一個輸入語音輸出語音的系統 那這是一個可能的 Solution 還有另外一個思考的面向呢 是 Agentic 的 Solution 我們可以說用一個文字的模型作為核心 然後呢 讓這個文字模型去操控其他語音的工具 有各式各樣語音的工具 包括語音辨識語音合成 甚至還有其他的 比如說語音轉換 或者是 Speech Enhancement 語音增強等各式各樣的工具 然後讓這個文字模型輸入一段聲音以後 它自己決定要用這些工具 怎麼來處理這段聲音 那這…
- `AihBniegMKg` (PRIMARY):
  - `AihBniegMKg:22-45` (`00:01:30.880–00:02:55.872`): 那什麼叫word piece呢? 直接舉一個例子 比如說unbreakable這個詞彙 你可能會猜成三個word piece，un、break跟able 就是我們高中的時候學過的這個字首字根的概念 那為什麼英文的token不是全部可能的英文的詞彙 而是用word piece呢? 因為你知道說，今天這個GPT它在生成東西的時候 它其實是一個分類的問題 它其實做的是一個選擇題 所以你要把所有的選項通通都列出來 而中文的字是比較有機會窮舉的 而英文的詞彙可以說是無窮多 每一個人名、每一個地名都算是一個新的詞彙 所以英文的詞彙，英文的word是無窮多的 所以在英文裡面，你不能把word當作選項 因為根本窮舉不了所有的word 所以在生成文句的時候，英文用的單位叫做word piece 就把word拆解成更小的單位，而這種單位是可以窮舉的 好，這個是文句的部分 那影像呢?影像構成的元素，這個大家就很容易想像了 就是pixel，就是像素…
  - `AihBniegMKg:46-68` (`00:02:56.380–00:04:23.167`): 16K有16000個點 ，所以語音是很複雜的 好，那生成文句，這個大家都很熟悉了 就是ChatGPT，生成影像，這個大家都知道了 Midjourney、Dali都是生成影像的AI 那等一下我們再舉幾個大家可能不一定知道的例子 一個是生成影片 那今天生成影片在文件上看起來，其實也做得蠻成功的 那以下這個例子是來自於Google在去年10月發表的論文 它叫Image Video 可以做的事情就是 給一個句子，它按照你寫給它的句子生成對應的影片 跟它說，畫一個泰迪熊在洗碗 這是機器生成的影片，真的是蠻猛的 那我看到它的demo裡面最猛的是這個 它說有一大堆秋天的落葉落在一個平靜的湖上 這些落葉要拼成文字叫Image Video 它的輸出是這個樣子的 落葉落在湖面上，拼起來就是Image Video 哇，這個非常難以置信，這個是由機器自動生出來的影片 好，那這是生成影片的例子 那還可以生成語音 那生成語音對大家來說你可能不會覺得特別稀…
  - `AihBniegMKg:69-92` (`00:04:23.160–00:05:47.060`): 所以語音合成，其實生成是AI也不是最近才有的 你說生成語音這個技術發展的老成熟了 給一個文字，今天Google小姐都可以念出非常字正腔圓的句子 那現在不只是給文字生成句子 你還可以直接下指令 告訴它說生成的句子風格應該要是什麼樣子 而且風格的描述直接用自然語言處理直接描述就好 以下的Demo來自一篇騰訊的論文叫InstructTTS 那這是非常新的論文 這是今年一月放在arxiv這個平台上的論文 那我們來看看這個論文裡面的Demo，看它做得怎麼樣 那它這邊可以做的事情就是 你在語音合成的時候 直接下一個自然語言的指令告訴它說我要和什麼風格的句子 比如說，這邊是和語調高昂聲音洪亮內心非常憤慨的句子 聽起來像是這樣 學長今天還說他喜歡我呢 你不珍惜我，我就跟別人跑了 好，這個是聲音 然後接下來聲音高語氣嚴厲大聲斥責，聽起來是這樣 學長今天還說他喜歡我呢 你不珍惜我，我就跟別人跑了 接下來鎮定從容語氣平和語調穩定 學長今天還說他喜歡…
- `MpsVE60iRLM` (CORROBORATING):
  - `MpsVE60iRLM:100-135` (`00:04:28.900–00:05:56.010`): 是你可以拿來使用的 好 那在 Pre-Train 的階段 用大量未標註的資料 訓練出 Upstream 的模型以後 接下來就進入第二階段 在第二階段裡面 你有一個明確想要解決的問題 你有一個待解的任務 舉例來說 在語音上 那你馬上可以聯想到的任務 也許就是做語音辨識 把聲音訊號轉寫為文字 當然跟語音相關的任務不是只有語音辨識 你等一下會看到更多各式各樣 不同的 Downstream 的任務 好 那在這個 Downstream 的任務裡面 我們有少量的標註資料 如果做語音辨識 你有聲音訊號跟聲音訊號對應的文字 那你會用這些少量的標註資料 去訓練一個 Downstream 的模型 那這個 Downstream 的模型 往往相較於 Upstream 的模型還要簡單得多 我們通常就只需要訓練一個 簡單的 Downstream 的 Model 如果你的 Upstream 的 Model 做得夠好 你只要一個很簡單的 Downstream…
  - `MpsVE60iRLM:136-164` (`00:05:56.010–00:07:24.300`): 有些時候我們會選擇用這些有標註的資料 也去微調 Upstream 的模型 不過這邊我用虛線來表示 就是告訴你說 這個微調不見得是必要的 好 那在語音上 已經有一大堆的 Upstream 的模型 那這些 Upstream 的模型在文獻上 往往顯示在語音辨識上有不錯的表現 但我接下來就有了一個問題 這些模型它們是語音辨識的專才 還是人類語言相關任務的通才呢 這些模型在文獻上 往往已經顯示在語音辨識上有不錯的結果 但是它是只能用在語音辨識上嗎 還是它可以用在各式各樣跟語音相關的任務 這些模型是語音辨識的通才 還是只要拿出一個語音相關的任務 你都可以使用這些 用大量未標註的語音訊號 所訓練出來的 Upstream Model 或是講得更具體一點 我們剛才已經看到說 我們可以在 Upstream Model 後面 疊一個 Downstream Model 用少量的 拿來訓練語音辨識系統的標註資料 來訓練這個 Downstream Mod…
  - `MpsVE60iRLM:165-200` (`00:07:24.700–00:08:53.630`): 那同一個 Upstream Model 可以用在其他任務上嗎 假設我們要做的不是語音辨識 而是語者辨識 那你有一些語者辨識可以用的標註資料 你能不能夠訓練另外一個 Downstream Model 這個 Downstream Model 也直接疊在 Upstream Model 後面 接下來在語者辨識上也有好的結果呢 那如果你問我 這些模型是專才還是通才 在幾個月之前 我可能會回答你說 我認為這些模型比較有可能是專才 為什麼我會這麼想呢 因為你知道這個語音辨識 語者辨識 它們其實是非常不一樣的任務 在語音辨識裡面 你要你的模型去無視語者間的差異 不同的人說同樣的詞彙 他的發音是不一樣的 但是你要你的語音辨識系統 去無視語者間的差異 但是今天如果你要做的是語者辨識系統 你要知道現在是誰在說話 那你要你的系統做的事情 是找出語者間的差異 所以大家可以了解說 語音辨識是要無視語者間的差異 語者辨識是要找出語者間的差異 這兩個任務 這…
- `CgQ3lUOpXgc` (CORROBORATING):
  - `CgQ3lUOpXgc:86-106` (`00:04:19.120–00:05:45.720`): 所以大家所使用的手機版的語音介面 其實可能還不是GPT-4O的語音模式 那舊版的語音介面是怎麼做的呢 舊版的語音介面是先把語音訊號透過語音辨識變成文字 再把文字丟給語言模型 比如說 ChatGPT 然後語言模型會給一個回應 這個回應透過語音合成產生語音訊號 那其實如果語音辨識跟語音合成跑得夠快的話 其實這個介面也可以達到蠻自然即時的互動功能的 但是跟這個OpenAI GPT-4語音模式的demo比起來 還是有一段差距 比如說呢 這個如果是透過語音辨識把聲音訊號轉成文字 那語言模型可能會不知道語者的情緒 語音合成如果只是把語言模型的輸出轉成聲音訊號 那語音合成就只有某一種說話的風格而已 那我在看這個GPT-4-O的語音介面的Demo的時候 我其實在想它會不會只是把原來的系統 加上了一些額外的模組 比如說在語音辨識之外
  - `CgQ3lUOpXgc:107-131` (`00:05:45.720–00:07:14.800`): 我們可以加一些語音事件偵測或情緒辨認的模組 所以我們也有機會透過情緒辨認的模組 也有機會把聲音訊號的情緒把它偵測出來 那你可以把偵測出的情緒放在語音辨識的結果後面 再去丟給語言模型 那這樣語言模型也有機會知道這句話的情緒 那我這邊引用一些論文 這些論文是說你可以加一些額外的模組 來幫助語言模型瞭解現在輸入語音的情緒 那另外你也可以讓語言模型除了文字之外 多輸出一些符號 比如說語言模型在他的輸出的文具後面加一個括號笑 再丟給語音合成系統 搞不好語音合成系統就可以產生笑聲 你可能會問說這個語音合成系統可以看到這個括號笑就產生笑聲嗎? 有一些語音合成系統是真的可以的 比如說Zuno AI所開發的Bark 你在你的文具裡面打一個笑 這個語音合成模型 這個語音合成的結果是真的可以產生笑聲的 另外一方面,ChatGPT可能也可以產生一段指令 告訴語音合成系統說 現在應該要用什麼樣的語氣來進行合成 語音合成系統可以看得懂這些文字的指令嗎?…

## Patterns and Repeated Themes

- 多個獨立來源均提供 `speech_multimodal` 的 selector-approved transcript anchors；可把它們用於受限的 cross-source candidate synthesis。

## Contradictions

- 來源跨年份、模態與任務；它們的共同概念不等於共同的 benchmark、資料分布或性能結論。

## Inferences

- Candidate inference (not formal): 語音／多模態系統要先釐清每個 modality 的資訊路徑與 cascade boundary，再比較 ASR→LLM→TTS、speech-to-speech 或 representation-transfer recipe 的錯誤傳播與成本。
- Candidate decision rule: 對每個 modality 分別記錄 input quality、transcription/recognition error、semantic task score、prosody/voice quality 和 latency；用 matched examples 比較 cascade 與 end-to-end 設計，並切分出聲音、文字與跨模態失敗。

## Gaps and Missing Information

- 未使用未選定的片段、影格或投影片；若未來某個結論需要公式、圖表或程式畫面，必須建立獨立 visual-evidence request。
- 本 dossier 是 Distilly research input，不取代原始影片、source chunks 或 evidence packets。
