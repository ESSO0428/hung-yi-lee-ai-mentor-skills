# Research Dossier: P3 archive／peripheral lessons

## Source Metadata

- Source: `88WzdTuQMyM` — 【生成式人工智慧與機器學習導論2025】作業一
- URL: https://www.youtube.com/watch?v=88WzdTuQMyM
- Source role: `PRIMARY`
- Source weight: 1
- Evidence packet: `EVP-CHANNEL-88WzdTuQMyM-p3_archive_peripheral_lessons-V1` (data/processing/channel_evidence_packets_v1/88WzdTuQMyM--p3_archive_peripheral_lessons.md)
- Transcript type: `official`; selector confidence: `HIGH`
- Source: `VuQUF1VVX40` — 【生成式人工智慧與機器學習導論2025】第０講：開場與課程簡介
- URL: https://www.youtube.com/watch?v=VuQUF1VVX40
- Source role: `CORROBORATING`
- Source weight: 2
- Evidence packet: `EVP-CHANNEL-VuQUF1VVX40-p3_archive_peripheral_lessons-V1` (data/processing/channel_evidence_packets_v1/VuQUF1VVX40--p3_archive_peripheral_lessons.md)
- Transcript type: `official`; selector confidence: `HIGH`

## Evidence

- `88WzdTuQMyM` (PRIMARY):
  - `88WzdTuQMyM:0-25` (`00:00:00.000–00:01:27.053`): 這是作業一的說明 作業一的時限是在10月17號晚上11點59分59秒 然後在+8時區 這是這個投影片大致上的outline 一開始我們會先跟大家講 怎麼在NTU Cool系統作答 就是你這個作業最終會在NTU Cool上面寫一個選擇題的答案 然後你要如何從NTU Cool找到題目在哪裡 然後接下來下一個地方就是我們會講題目大概有哪些 然後接下來就是講解這個Hugging Face 然後Colab跟Gradio到底是什麼 然後最後再幫大家複習一下 這個作業總共要做什麼就可以完成了 然後最後的最後就是一些繳交跟一些成績的規定這樣 好那這邊是一些有用的連結 那其實現在這個投影片在老師的網站上面就可以看到 所以大家可以去網站上面找 好那這個作業的目標就是 我們要希望讓大家可以熟悉這個NTU Cool怎麼用 然後還有Google Colab要怎麼用 然後也可以了解這個語言模型裡面的 Token這些Prompt還有Chart Templa…
  - `88WzdTuQMyM:74-99` (`00:04:18.191–00:05:47.380`): OK那接下來就是講一些我們這個作業有包含的內容 好那這個作業會先分三個部分 那第一個部分就是在講這個大型語言模型的Token 那像這邊就會有一些像是這個 Gemma-3-1B的Token大概有多少的 然後或者是一些encode跟decode的部分 那我想剛剛這些詳細的內容老師都有講過一次了 然後還有這個像是剛剛有一個 輸出一大堆空白的情況 那看這個Gemma-3-1B是不是也有這個可能 然後去算這個Token length有多長 然後還有一個就是Next Token Prediction 就是你要知道我們給這一連串的字 那它下一個會吐什麼字呢這樣 那這就是這個作業的第一個部分 那第二個部分就是System Prompt和User Prompt的Engineering 意思就是說你要去調整我們這個語言模型的System Prompt跟User Prompt 然後去觀察它的差別 那剛剛上課有說這個System Prompt就是 算…
  - `88WzdTuQMyM:215-245` (`00:13:09.922–00:14:29.301`): 那按完之後你可以其實可以按這個指令 去看你有沒有GPU在跑 像這個就它有GPU這樣 它是TESLA T4 就你有用到這個T4 那接下來就簡單講解一下 這包Homework 1的程式碼在做什麼 那我們剛剛很簡單就可以知道 前面的部分就是在講要讓大家提醒 大家要開這個GPU 然後接下來下個階段就是 下載一些環境 就是這個我們作業一會用到的一些環境 然後接下來 它載完環境之後 你需要跑這格 那跑這格的時候你就會用到 剛剛這個Hugging Face Token 你要Copy你的Hugging Face Token 然後貼到這裡 然後去做執行 這樣 貼到這裡去做執行 那你有看到這個紅色的話 就是代表它執行有錯誤 它就是一個Error這樣 那我再執行一次 那這樣它剛剛轉了一下就代表它有在跑 然後現在是成功的狀態 大家先稍等我一下 我先去跑後面的東西
  - `88WzdTuQMyM:542-560` (`00:24:53.592–00:25:43.742`): 那所以如果你沒有加這個TAG的話我們會一律視為你沒有寄這一封信所以這件事情非常重要 再提醒大家一次 OK 那你也可以來參加這個TA hour來問我們問題 那TA hour時間就公佈在這裡 然後 那就是禮拜一的晚上8點到10點跟禮拜五的下課5點半到 7點半 那這個地點是在這個Google Meet 那我們Google Meet會有一個規則就是 前一個人離開我們才會放下一個人進來 所以大家 要進入這個Google Meet可能會等一陣子所以還是推薦大家有問題 就在NTU Cool討論區上面做 問問題的動作不然你可能會在Google Meet排隊排很久這樣 然後 好 那 以上就是這個是作業一的講解
- `VuQUF1VVX40` (CORROBORATING):
  - `VuQUF1VVX40:122-152` (`00:06:44.537–00:08:14.327`): 那我做的事情就是給他一張我的照片和一段語音 他就可以自動讓照片中的人開始說話 那最後投影片的部分 也是人工智慧生成的 這是用一個叫做Genspark的平台生成的 Genspark其實是一個AI agent 那我們下週會講到AI agent的概念 那我在生成投影片的時候 我就是給他我們的課程說明 叫他把投影片做出來 他就產生投影片還有講稿 那我再把講稿丟給Eleven Labs 讓他產生聲音 所以剛才你看到的東西真的都是人工智慧生成的 而且我剛才並沒有用任何神奇的技術 這些都是你今天唾手可得的技術 好那我們就正式開始這門課 叫做生成式人工智慧與機器學習導論 那我是李宏毅 那這是台灣大專院校人工智慧學程聯盟的課程 那這是我們的課程規劃 這門課我準備講十講 那每一講要講的日期 我都已經寫在這個投影片上面 那每一講要講的主題也都已經寫在投影片上 那我們這門課的前四講 會帶大家了解現有的生成式人工智慧 你會知道現有的生成式人工智慧 他是…
  - `VuQUF1VVX40:153-193` (`00:08:14.327–00:09:44.183`): 這些生成式人工智慧是怎麼被打造出來的 你也有機會自己訓練生成式人工智慧 那前八講呢 主要以文字互動為主 那第九講跟第十講 我們會講影像跟語音 那有關這門課的所有的資訊 包括上課錄影 課程投影片 還有作業的講解 你其實都可以在課程的公開網頁找到 那我把課程的公開網頁 放在這頁投影片上面 那我把QR code放在這頁投影片上面 那我們上課的方式呢 主要是以直播進行 那我會在那個台灣大學的新生教學館202 錄直播 然後所以如果你在現場看的話 你就是現場看那個直播的錄影 因為我們教室不大 所以鼓勵大家呢 其實可以在家裡看直播就好 那我們以後上課的時間 就是週五的下午2點20 那我們在週五下午要做的事情 是首先呢 我會先上課 那我通常上課上一個半小時到兩個小時左右 那上課的內容呢 會是以講解概念為主 但是有時候呢 我也會帶一些實作來作為輔助 那我上完課之後呢 接下來呢 助教會講解作業 那這個部分呢 通常是半個小時到一個小時左右 那大家要…
  - `VuQUF1VVX40:379-417` (`00:17:07.659–00:18:32.144`): 需要訓練三天以上的模型 你只在前一天才開始做作業 你是絕不可能完成的 這個時候我告訴你 唯一可以做的事情 就是放棄這樣子 還好我們這堂課裡面呢 現在是沒有需要訓練一天以上的作業啦 我們把那種 特別需要花時間訓練的作業 還是拿掉了 只保留了需要訓練三四個小時的作業 但我只想要強調說 三四個小時的訓練時間 真的不算什麼 如果你要真正用大量的資料 大規模的訓練模型 訓練個數週 其實都是常見的事情 而這一些 需要一點訓練時間的作業 它的定位就像是預防針 幫助你在未來面對更大的挑戰 幫助你在未來面對挑戰的時候 做好心理準備 另外呢 鼓勵大家如果有空的話 可以先看一些線上的錄影進行預習 那假設你對於生成式AI一無所知的話 那你可以先看生成式AI導論2024的課程 那如果2024的課程看完 你想要進一步了解 這些AI是怎麼被訓練出來的 鼓勵你可以看機器學習2021 那不過這一堂門課呢 我們會從基礎開始講起 所以就算你沒有時間預習也無所謂 但…

## Patterns and Repeated Themes

- 這些來源共同記錄課程／作業 logistics 與可回查的 coverage context；它們不是 mentor 的 recipe evidence。

## Contradictions

- 來源跨年份、模態與任務；它們的共同概念不等於共同的 benchmark、資料分布或性能結論。

## Inferences

- Archive-only: 不生成 mentor rule 或 recipe inference。

## Gaps and Missing Information

- 未使用未選定的片段、影格或投影片；若未來某個結論需要公式、圖表或程式畫面，必須建立獨立 visual-evidence request。
- 本 dossier 是 Distilly research input，不取代原始影片、source chunks 或 evidence packets。
