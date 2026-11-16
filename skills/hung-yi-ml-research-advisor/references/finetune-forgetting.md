# 微調、遺忘、PEFT、不改權重的替代

症狀是想讓通用模型學新東西、微調後舊能力變差、或在 LoRA／replay／merging 之間選擇時讀這份。語境多為 GenAI 2025 的 LLM／語音 LLM；影像模型的遺忘幾乎沒講。小資料微調的保守原則見 generalization-shift.md D 與 small-data.md。Y9Jay_vxOsM（ML2021 終身學習：EWC/GEM/generative replay）沒有逐講筆記，引用須回查原稿。

## F. 先問：真的要動參數嗎？
- 症狀：想讓通用模型有新知識／新行為，直覺就微調。
- 檢查：Prompt、In-Context Learning、RAG 是否已認真試過。「學習」在第 8 講只指更新參數；與 ChatGPT 聊天不會改參數，只是記在「小本本」。
- 做：後訓練是「不到沒有辦法」才用；先把 Prompt 技巧用盡。例：GPT-4 不接受新總統資訊，先給一個「新資訊照單全收」的示範（荒謬也照答）就改答（他說此例未開 RAG）。
- 為什麼：「後訓練就像給 AI 的大腦動手術」，耗算力還有風險；「最好的後訓練就是不要做後訓練」。需更新參數的場景：知識會變、缺技能或新模態（語音）、過時概念、版權與隱私要遺忘。
- 專才 vs 通才：只在意單一任務→專用／微調（翻譯上商用系統多半贏 ChatGPT，但樣本小，騰訊那篇約 50 句）；要多功能快速迭代→通才加 prompt。
- (EnWz5XuOnIQ S0002, S0010-S0013, S0004-S0007)(F58vJcGgjt0 S0005-S0011)

## G. 微調成功的驗收：Reliability / Generality / Locality
- 症狀：微調後目標問題答對就宣稱成功；或微調後「什麼問題都回同一個答案」。
- 檢查：三項分開測。Reliability：要改的有改（魯夫吃的果實）。Generality：相關的跟著改，含反向（誰吃了尼卡果實→魯夫）與需推理的（喬巴海賊團團長吃了什麼），他說只是舉兩例。Locality：無關的不動（喬巴的果實不變）。Locality 要用微調時沒看過、無關的問題測。
- 例：只用一筆「誰是全世界最帥的人→李宏毅」微調 GPT-4o mini，問「誰是美國總統」也回李宏毅；公司資料微調 Llama 2 後，無關問題也用公司答案。
- 為什麼：Loss 只要求該輸入→該輸出，模型可學到「看到『誰是』就接李」，Loss 一樣低，「Loss 沒有辦法阻止你選到這個模型」。像修一個 Bug 卻改了全域變數。很多論文只看 Reliability；他說這是做過微調的人最容易遇到的問題。
- (EnWz5XuOnIQ S0008-S0010, S0016-S0019, S0027-S0029)

## H. 微調後舊能力不見了（catastrophic forgetting）
- 症狀：目標任務進步，但「新的知識進去之後，舊的知識就掉出來了」。例：LLaMA-2 續訓後說錯話比例，base 約 25%、chat 0.22%，續訓後明顯升高，銀行密碼題從拒絕變教攻擊；輸出退化成重複字；只教程式則數學與工具大跌（一項 19.6→3.6）；語音 LLM 訓練 23 個語音任務，1 epoch 還能輸出 JSON，3 epoch 後不能（任務裡根本沒教 JSON）；樊樺 Llama 3 強化推理／醫學／程式／工具，四項都升，但 AdvBench 攻擊成功率從 0% 大升，醫學最嚴重。
- 檢查：目標與「舊能力」（safety、指令／格式遵循、重複退化、其他基準）兩組並列回報。針對特定任務打贏通用模型「不是太難」，要問損失多少原本會的。
- 特性：
  - 資料乾淨無害也會壞 safety（Alpaca 正常問答 SFT、單純改名都會）；safety 是他經驗中最先壞的。
  - SFT 與 pre-train style 同樣會忘；文獻只到 1B-7B，不可外推到更大模型。
  - 學越多忘越多：遺忘量與 fine-tuning loss 近乎斜直線，畫整條軌跡（橫軸舊能力、縱軸目標任務）選 checkpoint；GSM8K 先升後降他稱 overfitting。
  - 依應用而定：只要單一專長問題不大；期待通用模型才必須防。
  - 依序教多任務舊能力會震盪，教相近任務又回升；他解讀「不是真遺忘，只是不想想起來」（直覺非證明）。
- 他的比喻：這是「全面性崩壞」，非人類式小健忘；「手術成功了，病人卻死了」（句子經複核疑為 paraphrase）。
- (Z6b5-77EfGk S0006-S0022, S0051)(EnWz5XuOnIQ S0020-S0027)

## I. 防遺忘工具箱（依資料可得性）
1. 有舊資料：experience replay。Z6b：混入約當下任務資料 5%（2019 GPT-2 依序學 NLP 任務「非常足夠」；微調保留約 3% safety 資料即可保 safety）；EnW：「Subsample 一小部分就足夠」，無數字。數字僅屬特定實驗。(Z6b5-77EfGk S0030-S0036)(EnWz5XuOnIQ S0038-S0039)
2. 保持用資料要慎選：EnW 現場實驗，只加一筆（美國總統→川普）不夠；加很多答案都是單詞的亂編「誰是…」，模型變只回單詞、省話；改成「問題＋模型自己原本的答案」只兩筆就不再變怪，但「全世界最宅的人」仍回李宏毅，需再補同類型樣本。結論：保 Locality 的資料分布若不同於模型原行為，會引入新偏差。(EnWz5XuOnIQ S0035-S0043)
3. 沒舊資料（只釋出權重）：pseudo replay，讓模型自生「像過去訓練資料」的內容混入；Magpie 只給 chat template 的 user token 接龍出問題與回答。內容可能全是亂講，行為分布像就夠。(Z6b5-77EfGk S0032-S0038)(EnWz5XuOnIQ S0040-S0041)
4. 能自動驗證答案（數學比對、程式跑 compiler）：selective self-rehearsal，答對用自己的答案，答錯才回退人寫答案；可每題 sample 10 個挑對的。原理：自己的輸出本來就高機率。(Z6b5-77EfGk S0039-S0041)
5. 只有人寫答案：請 foundation model 先 paraphrase 再訓練（他引的表九個設定只有一個較差，口述）。(Z6b5-77EfGk S0038-S0049)
6. foundation 太弱答不出：用較強 LLM 的答案；風格差太遠（GPT-4 答案訓練後 HumanEval 變差）就 minimum change，只讓強模型改自己答案的錯處。(Z6b5-77EfGk S0042-S0043)
7. token 層級過濾：用 foundation model 算每 token 機率，最難的前約 20% 不計 loss（MATH 上 in/out-of-domain 更好，20% 以內才有講）。(Z6b5-77EfGk S0047-S0050)
8. 新模態（語音）：不微調文字模型，只調 adapter，並以文字模型自己的輸出當 target（DeSTA2）；此屬語音接文字 LLM 情境，勿當通用 LoRA 建議。(Z6b5-77EfGk S0014-S0017, S0044-S0047)
9. Regularization：Loss 加每維 λ_j(θ_j−θ⁰_j)²，λ_j 大＝重要、少動；重要性怎麼算他說是研究問題，EnW 沒給算法。EWC／GEM／generative replay 屬 2021 終身學習課（Y9J，無筆記，待回查）。他 2019 試 MAS 在語言模型上略差於一般 fine-tuning；dropout、weight decay 擋不住。(EnWz5XuOnIQ S0032-S0034)(Z6b5-77EfGk S0022, S0029)
10. RL 階段可能較不易遺忘（資料皆模型自產），他明說「是猜想，要等更多研究」，仍須回測。(Z6b5-77EfGk S0040-S0041)
- 年代演進：2017 Lec19 只有 conservative training 與「source 壞掉就算了」，沒有遺忘處方；2019 年混入約 5% 舊資料就夠，他解讀為模型「只是不想想起來」；2025 因拿不到訓練資料又成真問題，改走 pseudo replay／self-output（但 EnW 仍稱 replay 是「最有效」）。

## J. PEFT / LoRA / adapter
- 動機：多任務時完整微調存 N 份；adapter 是「一個大模型＋N 個小插件」，成本 N×P 對 P+N×a。adapter 仍是 fine-tune。(F58vJcGgjt0 S0012-S0016)
- LoRA 不是防遺忘解藥：learns less and forgets less，rank 小的點聚左下、rank 大聚右上；沿同一條學習量–遺忘量曲線移動，不是換更好的曲線。EnW 同說法：Full FT 目標越學越好但 Locality 越差，LoRA 範圍畫太小可能達不到 Reliability／Generality；「很多人以為用 LoRA 就完全不會 Forget，其實不是」。比 dropout、weight decay 好，但有代價。(Z6b5-77EfGk S0019-S0022)(EnWz5XuOnIQ S0030-S0032)
- 插法沒有通則：LoRA 在 NLP 很好，他實驗室用在語音卻是所有 adapter 中最差，「取決於應用，要自己試」。(F58vJcGgjt0 S0013-S0014)
- rank/alpha 方向（作業 slide 的 homework heuristic，不是課堂原理）：rank 低易 underfit、高易 overfit；alpha 小可降低 shift 影響。LJbmRPArBOg 有講 LoRA 設定與 rank（ASR 髒，待核）。

## K. 不改權重或不訓練的替代：Model Editing、Merging、Test-Time Training
- Model Editing（ROME）：定位（遮蔽後逐層置換看機率恢復，GPT-2 中間層約 15–20 層、最關鍵約 18 層）→ 求目標向量 v* → 只改該層 Feed Forward W→W*，加人工挑的保持關係限制，有 closed-form。他說這是「非常古早、運作得沒有真的很好」，後來有許多變形。(EnWz5XuOnIQ S0043-S0051)
- Model Merging（Task Vector）：前提是兩模型源自同一 θ；τ=θ_ft−θ，θ+τ_A+τ_B 幾乎不需算力與資料。例：Llama 2 Base 用中文做後訓練，把 τ 加到 Chat 上，既會中文又保拒絕能力（Llama 3、Mistral、韓日文也有效）；沒有 alignment 資料做不了 replay 時的繞法。「不總是成功」，有時 merge 後壞死，原因他沒講；工具 MergeKit。(EnWz5XuOnIQ S0053-S0057, S0064-S0065)
- Unlearning：從模型減去 task vector（例：減去 PTT 微調的向量，模型不再知道某歧視用語詞義，開始瞎掰）。這展示的是忘掉後會 hallucinate，不是安全證明。(EnWz5XuOnIQ S0057-S0059)
- Test-Time Training：每筆測試輸入現場 fine-tune，不需 label。做法：找最近的 n 筆訓練資料微調；或 TENT（minimize entropy，原始需一個 batch 如 32 筆）；語音 SUTA 只用一句；或結合 pretext task（預測旋轉角度）。(EnWz5XuOnIQ S0066-S0075)
- 連續 TTT 通常會壞：累積更新 WER 比不累積更差，影像上甚至永遠輸出同一 class（collapse），原因是 forgetting 越滾越嚴重。Dynamic SUTA：fast update 只調當前一筆用完即丟；slow update 累積數筆後保留；壞掉要 reset（偵測法沒給）。他說仍是待研究問題。(EnWz5XuOnIQ S0076-S0082)
