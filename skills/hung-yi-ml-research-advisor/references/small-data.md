# 小資料、半監督、微調資料、預訓練資料效率

症狀是資料少、label 少、要選微調資料、或預訓練資料有限時讀這份。先確認 skeleton.md 的分流：train loss 就差時加資料沒用。

## A. 資料很少，要不要加資料？
- 第一步與 bias／optimization／overfitting 的分流見 skeleton.md A–C（train 就差時加資料、augmentation、L2、dropout 都幫不上）。
- bias 大時「collect more data 也不會有幫助」；variance 大時加資料像「萬能丹」，但現實常拿不到（業界要一萬筆 label 被老闆拒絕）。(D_S6y0Jm6dQ S0019–S0021)
- 例（小樣本警訊）：寶可夢 10 隻時選 3 次式（train 15.3 / test 18.1；5 次式 test 200 多、預測出負 CP）；收集到 60 隻才發現是漏了「物種」變數，改 δ(物種) 線性模型 test 14.3，「針根本不在海裡」。他自評「data 有點少，沒那麼 confident」。先畫資料、查漏變數，再調複雜度。(fegAeph9UaA S0052–S0076)

## B. 症狀：「label 很少、unlabeled 很多」→ 半監督
1. 先確認前提：缺的是 label 不是 data（unlabeled 輸入容易大量取得）。Transductive（testing 的 feature 當 unlabeled，合法；用 label 才是作弊）vs Inductive（部署時才有資料）；先確認比賽規則。(fX_guE7JNnY S0002–S0004)
2. 有沒有用取決於假設是否成立，「不見得永遠有用」。先講明用哪個假設並驗證：low-density separation、smoothness、cluster 對應 class、generative 的分布形狀。(fX_guE7JNnY S0005)
3. Self-training：labeled 訓 f* → 標 unlabeled → 挑一部分加入 → 重訓；挑哪些是 open question（可依信心加權），無門檻建議。Regression 不能用（pseudo-label 就是模型輸出，不影響 f*）。2016 助教實測 self-training 「一定進步」，僅限當時作業。前提（另一講）：初始模型太差就產生不出好 pseudo-label。(fX_guE7JNnY S0013–S0016；wulqhgnDr7E S0002)
4. 神經網路用 hard label（0.7/0.3 → 1/0）；soft label「沒有用」，因為與現有輸出一致、沒新資訊。generative 模型用 soft（posterior 加權）才對。此規則限定 NN。(fX_guE7JNnY S0018–S0020)
5. Entropy regularization：loss = CE(labeled) + λΣE(y^u)，E=−Σy ln y；unlabeled 輸出要集中（5 類集中 entropy=0，平均＝ln5），是 hard label 的軟版本，像 regularization。(fX_guE7JNnY S0021–S0024)
6. Smoothness 精確版：x 之間要經過 high-density 路徑才同 label（「平原有人、山走不過去」）；兩個 2 的 pixel 可能比 2 與 3 更不像，靠連續過渡的 unlabeled「stepping stone」串起來；文件分類 labeled/unlabeled 詞彙可能完全不重疊。unlabeled 要「夠多」，否則鏈斷。(fX_guE7JNnY S0027–S0031)
7. Cluster-then-label：用 pixel 直接 cluster「八成壞掉」，要 autoencoder feature；cluster 不能把同 class 聚起來就失效。(fX_guE7JNnY S0032–S0033)
8. Graph：有天然圖就用；否則 kNN 或 ε-neighborhood，權重 exp(−γ‖xi−xj‖²)；「graph 對結果非常 critical」且憑經驗。label smoothness S=½Σw_ij(yi−yj)²=yᵀLy（L=D−W），加進 loss（λ·S），可加在任一 hidden layer。(fX_guE7JNnY S0033–S0044)
9. Generative + EM（shared Σ Gaussian）：初值影響收斂，只到局部解；他快速帶過。Semi-supervised SVM、Better Representation 只是預告。(fX_guE7JNnY S0006–S0026)

## C. 症狀：「標註很少但有預訓練模型 / 要微調」
1. 少量 target 資料微調要保守：source model 當初始值，不要跑太多 iteration（只跑兩三個 epoch）；conservative training（新舊 output 或參數 L2 距離受限）。「train 下去就壞掉」。(qD6iD4TFsdQ S0010–S0012；Mnk_oUrgppM S0003)
2. 哪些層搬／重訓「case by case」：語音拷貝後層、影像拷貝前層。Bengio 實驗是 target 60 萬張：只固定前層重訓後層有時更差（層間要搭配）、整個 fine-tune 一致有益；不可據此外推「小資料時也不要凍結」，小資料請依第 1 點保守。source 與 target 差越大，效益越小。(qD6iD4TFsdQ S0014–S0018)
3. 只在乎 target 用 fine-tune；source 能力也要留是 multitask / 終身學習。fine-tune 的 loss 看不出舊能力是否遺失，需另設保留任務監測。LoRA「學得少、忘得少」是雙面刃，不保證不遺忘；LoRA 在語音上最差，「插在哪取決於應用，自己試」。作業提示：rank 小→欠擬合風險、大→過擬合風險（homework heuristic，非課堂原理）。(EnWz5XuOnIQ S0025–S0033；F58vJcGgjt0；hw7)
4. 凍結 upstream、各層加權和 + 輕量 downstream 是可行基線，「微調不見得必要」（語音）。(MpsVE60iRLM)
5. 只有少量 SFT 而無預訓練會極易 overfit；LLaMA-2 只用 27,540 筆 SFT、LIMA 1000 筆即接近強模型，「畫龍點睛，龍的主體是 Pretrain」；alignment 資料「不用多、品質重要」（買百萬筆不如自做兩萬多），但「什麼樣的資料是好資料」他說仍難說清。(Ozos6M1JtIE S0003–S0006；LJbmRPArBOg S0034)

## D. 症狀：「微調資料怎麼選 / 能不能教新知識」（LLM 語境）
- SFT 只教模型已會的：資料依 base 能否答對分 highly/maybe/weakly known/unknown（few-shot+greedy 判斷）；unknown 學下去 dev 先升後降；maybe known 最有益；RL 因訓練答案都是模型自己的，不硬教新東西。對照組：教正確答案（INC）反而比用模型自己的錯答案（SELF）差。(Ozos6M1JtIE S0042–S0048)
- 選資料沒通則，用實驗驗證：知乎 8000 筆 53→63，弱智吧 240 筆→83（GPT-4 生成，可能是蒸餾效應）；「挑最長 1000 筆」勝全量，LIMA 答案更長卻較差，「不知道為什麼」。AlpaGasus 以 LM 打分濾掉低分，少資料贏全量。(Ozos6M1JtIE S0007–S0013)
- 強模型當老師蒸餾：問題不重要，答案重要（Mistral-7B base MT-Bench 3.73，用 GPT-4 續寫 7.3 > 官方 Instruct 6.84；原句後半當答案反而更差）。成本數字（約 100/450 美金）「看看就好」，不含生資料與清資料。(Ozos6M1JtIE S0009–S0016)
- 風格≠內容：仿 ChatGPT 的微調模型被吹到九成 GPT-4，後被發現內容多錯。alignment 前後 token 僅少數 shift，所以少量資料就行；有害知識仍在，像「戴面具」。(Ozos6M1JtIE S0017–S0019, S0040–S0054)

## E. 症狀：「預訓練資料有限 / 要不要多跑幾輪」
- 資料多樣勝過重複：12B token 反覆看約第 4 遍起與不重複者出現差距，超過約 40 遍幾乎不再成長；語音：960 小時看一遍勝過 1 小時看 960 遍。數字是特定論文設定，不是通則。(Ozos6M1JtIE S0037–S0039)
- 同一知識要有多種版本：合成人物簡歷只出現一次，微調 QA 在沒見過的人上近 0%；有多版本約 80%（只需部分實體多版本，約十分之一，他說「如果沒記錯」；他稱這是擬人化想法）。(Ozos6M1JtIE S0025–S0030)
- 資料品質靠逐步驟對下游任務做對照實驗（FineWeb 贏 C4/RefinedWeb；Common Crawl 清洗後只剩約十分之一）；教科書資料有效，但那是 GPT-3.5 生成，可能是生成文字本身有用；Apple 改寫網頁同 token 下約省 3 倍資料。(Ozos6M1JtIE S0034–S0040)
- 網頁可用 token 約 2028–2030 用盡，overtrain 小模型更早；LLaMA-3 15T、DeepSeek-V3 14.8T（預測，非事實）。(Ozos6M1JtIE S0030–S0034)
