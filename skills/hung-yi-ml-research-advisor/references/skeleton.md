# 診斷骨架與評估紀律

先讀這份：任何「效果不好」的問題都從這裡分流，再依分流結果去讀對應 reference。引用格式 `(影片ID Sxxxx)`，ID 對照見 sources.md。

年代：2016/17（xki61j7z-30、D_S6y0Jm6dQ）只分 bias／variance；2021（WeHM2xpYQpw、bHcJCp2Fyxs）起多切出 optimization 失敗，這是主要演進；2022（xQXh3fSvD1A）補 validation 被用壞；2025（Taj1eHmZyWw、mPWvAN4hzzY）改用「三步驟＋generalization」說法。診斷順序三代一致。xQXh3fSvD1A 的 ASR 很差、後半截斷，只取大意，「|H_val|」論證是重建，標「大意」。

## A. 總骨架
1. 第一問「training loss 多少？」沒記錄無法診斷。2016 版同一問題問成「你的問題是 bias 大還是 variance 大」（考碩博生必問，決定 future work）。(WeHM2xpYQpw S0004 S0012; D_S6y0Jm6dQ S0018)
2. training 差 → model bias（針不在海裡）vs optimization（針在海裡撈不到）：症狀相同、解法相反。2016 的 bias 大＝f̂ 不在 function set，等同此處 model bias；當年沒講 optimization 分支。(WeHM2xpYQpw S0005-S0007; D_S6y0Jm6dQ S0019)
3. training 好、val/test 差 → overfitting vs mismatch；「不是所有不好都叫 overfitting」。2016 稱 variance 大。(WeHM2xpYQpw S0009 S0012; D_S6y0Jm6dQ S0019)
4. 都好才談上線；每套一個新技巧後回頭再看 training（可能被弄壞）。(WeHM2xpYQpw S0012; xki61j7z-30 S0004)
5. 2025：三步驟（Loss／函式範圍／optimization）＋驗證；驗證失敗「一步一步想」：步驟一（資料與目標一致？）→ 步驟二（範圍太小）→ 步驟三（optimization）→ 最後才是範圍太大。(Taj1eHmZyWw S0036-S0038)
6. 任何技巧先填表：改哪一步？幫 optimization 還是 generalization？(mPWvAN4hzzY S0002 S0085-S0086)
對照（mPWvAN4hzzY S0033-S0086）：optimizer／LR schedule 只幫 optimization（val 甚至更高）；dropout、更多資料、augmentation、semi-supervised、L2 只幫 generalization 且 train loss 更難降；CNN＝generalization；skip connection＝optimization；normalization 主要 optimization；pre-train 兩者皆有；cross-entropy 讓 optimization 做得了，對 generalization 無益。

## B. training loss 高
**B1 bias 或 optimization？以淺模型當基準。** 症狀：深模型 train loss 不比 linear／淺網路低（linear 71、NN 約 80）。做：大模型高於小模型 → optimization 問題，調 lr、epoch、batch 直到低於 71（例壓到 41），不是開更大網路。為何：深模型函式集合包含淺模型（56 層＝20 層＋36 層 identity）。前提：函式集合須巢狀，不巢狀此論證不成立（推論）。(Taj1eHmZyWw S0053-S0057; WeHM2xpYQpw S0008-S0011; mPWvAN4hzzY S0003)
**B2 數字例**：1–4 層 train 0.28k→0.18k→0.14k→0.10k，5 層回到 0.34k → 4 層可達 0.10k，5 層必是 optimization。(WeHM2xpYQpw S0011)
**B3 更深 test 變差≠overfitting**：56 層比 20 層差，先看 train（20 層 train 本來就低＝沒 train 好）。(WeHM2xpYQpw S0008-S0010; xki61j7z-30 S0005)
**B4 確定是 bias → 給彈性**：加 features、更大／更深；線性模型畫不出「物極必反」。(D_S6y0Jm6dQ S0020; bHcJCp2Fyxs S0001-S0011) 2016 明說此時收更多 data 沒用。(D_S6y0Jm6dQ S0020)
**B5 optimization 失敗排查（誠實版）**：看不到 loss surface，「往往不知道問題出在哪」；實務靠信念＋爆試（lr、epoch、batch、初始化、Adam）；toy 換 Adam＋特別初始化才到 21；重跑 85／238／200 多。(Taj1eHmZyWw S0094-S0095; mPWvAN4hzzY S0036-S0040)
**B6 loss 不降≠local minimum**：多數不是；可能 saddle、gradient 小而沒耐心；「不知多訓練幾天會不會突然下降」。(mPWvAN4hzzY S0022; Taj1eHmZyWw S0055)
**B7 工具（病在 optimization 才用）**
- lr：NaN／爆炸＝太大，幾乎不動＝太小（0.001 飛出地圖；0.0001 要一萬 epoch）。Adagrad／RMSprop（α 小＝重視新 gradient；0.01 可、0.1 震盪、1 發瘋）／Momentum／Adam，「沒偏好先學 Adam」；warm-up 他自承難解釋。(mPWvAN4hzzY S0006-S0033; xki61j7z-30 S0029-S0042)
- 換 optimizer 只在 train 壓不下去；generalization 差時通常沒用。(mPWvAN4hzzY S0033)
- 初始化：同模型同 optimizer，隨機初始化 loss 7～9，改 scale 降到約 1；「沒有標準答案」。(mPWvAN4hzzY S0036-S0040)
- 架構：難點是 vanishing 與 explode 並存；skip connection 使 surface 變平。2016：sigmoid 加深到 9–10 層崩，查 train 曲線、換 ReLU；他當場換後的結果轉錄缺，不可引。(mPWvAN4hzzY S0057-S0061; xki61j7z-30 S0009-S0019)
- normalization：feature 尺度差大 lr 難調（總字數 → 每頁字數好訓練許多，「一個可能原因」）。(mPWvAN4hzzY S0061-S0063; Taj1eHmZyWw S0088)
- batch：每 epoch 更新數 N/B，B=1 擺盪、full batch 更新少；epoch 與 update 分開報。(Taj1eHmZyWw S0030-S0034; bHcJCp2Fyxs S0027-S0030)
**B8 loss≠metric**：accuracy 不可微，訓練用 cross-entropy、驗證報 accuracy，多一個落差來源。(mPWvAN4hzzY S0063-S0070)

## C. training 好、validation 差
**C1 處方（他稱最簡單最有效）**：(a) 加訓練資料——2016 稱「萬能丹」，且不傷 bias（5 次式每次 10 隻、100 個 f* 散開；每次 100 隻則集中）；(b) 不能加就 augmentation；(c) 限制彈性：少參數／共用參數（CNN）、少 features、early stopping、regularization、dropout。順序＝優先序為整理者推論。(WeHM2xpYQpw S0014-S0019; D_S6y0Jm6dQ S0020-S0021)
**C2 augmentation 須保 label 語意且貼近部署**：鳥可翻轉，判斷頭朝向不可；語者辨識不可變聲、可改音量；手寫數字轉 ±15 度；乾淨語音加公車雜訊；只有英文資料就翻成中文；Mixup 連 label 混。(WeHM2xpYQpw S0016; D_S6y0Jm6dQ S0021-S0022; mPWvAN4hzzY S0072-S0075)
**C3 限制別過頭**：y=a+bx 對三點無解是 bias。複雜度掃描：train 一路降、test 先降後暴增，選中庸（2016 稱 variance 增長比 bias 下降快）。「複雜度」無明確定義。Regularization 加重 weight 會傷 bias，須調平衡。(WeHM2xpYQpw S0019-S0022; D_S6y0Jm6dQ S0017-S0024)
**C4 範圍太大為何易 overfit**：集合含 lazy function（只對三訓練點、其餘輸出 0）。例：加好 feature 後 train 71→22，val 122→1300。理論他說要一小時不證明。(Taj1eHmZyWw S0059-S0062)
**C5 加資料只對 overfitting 有效**，須有代表性；optimization 失敗灌資料沒用。「資料更多使 optimization 更難」只確證於 augmentation，通則為 待核。(mPWvAN4hzzY S0071-S0075)
**C6 傳統三件套（2016）**：early stopping（val loss 最小處停）；L2 weight decay（λ 如 0.001，不對 bias；L1 較 sparse）；dropout 只在 testing 差時用，training 差還加只會更差，testing 不 dropout、weight×(1−p)（忘縮放→「做了 dropout 都沒進步」）。2025 加 AdamW。(xki61j7z-30 S0043-S0064; mPWvAN4hzzY S0080-S0085)
**C7** DNN 的 overfitting 不是第一個遇到的問題：kNN／decision tree train 直接 100%。(xki61j7z-30 S0002)
**C8 容量加了、held-out 不降**：Linear 0.32k／0.46k；1000 ReLU train 更低、未見幾乎沒進步；4 層 0.10k／0.44k。選模型看未見資料，不看 train 最低。(bHcJCp2Fyxs S0032-S0042)
**C9 mismatch**：加資料沒用，靠對資料產生方式的理解，他沒給統計檢測。例：2/26 人為高點 1–4 層全失準；2020 訓練／2021 測試「怎麼做都慘」，助教改切法。他說「多數作業不會遇到」；有人把它算 overfitting，「只是名詞定義」。除夕低谷（模型無「除夕」資訊）是外生事件，與切分漂移機制不同，勿混。(WeHM2xpYQpw S0034-S0036; bHcJCp2Fyxs S0035-S0037)
**C10 val 系統性偏一邊先查步驟一**：用 2021 課預測 2025 導論課：train 240、val 1143，三點全高估（50/63/167）；畫圖綠點全在藍點下；換同性質導論課資料 → train 71、val 122。「在錯誤目標上做 optimization 緣木求魚」。畫圖＋領域常識，非檢定。(Taj1eHmZyWw S0038-S0041 S0085)
**C11 domain shift 三型**（輸入／輸出分佈、關係變）；課程只對輸入分佈有方法：source-only 57.5%→DANN 81%。(Mnk_oUrgppM，間接引自 gap 複核 S0002-S0004)

## D. 評估紀律
**D1 別用 public leaderboard／手上 test 選模型。** 一兆個廢模型全上傳總有一個 public 高；public 前十掉到三百名外「每年都有」。2016 版：選 model 3（test 0.5）後真 test 通常 >0.5，第 3 名可掉到 100。做：train 切 train/val（作業 90/10）選模，過 strong baseline 就不動。承認實務難免偷看。(WeHM2xpYQpw S0022-S0032; D_S6y0Jm6dQ S0025-S0027)
**D2 選定後用全部 training data 重訓一次**；看到 test 差不要回頭調（調了分數不再反映真實，他自承心情上做不到）。重訓後 public 可能更差，但才反映 private。(D_S6y0Jm6dQ S0028-S0029)
**D3 validation 也會被用壞（2022 補述）。** 用 val 選模＝在有限集合 H_val（候選模型數）上「做訓練」；可信度取決於 val 大小與 |H_val|。選 3 個候選通常安全；層數×每層 neuron 都掃 1 到 1000，組合數爆炸，val 也會 overfit。計數是掃描組合總數。(xQXh3fSvD1A S0003-S0006，大意；原話 ASR 損壞，Hoeffding 式未出現) 2025 版更白話：模擬考可考多次、大考只一次；「人只有一次機會，鬼可無限再生」；SQuAD 2019 BERT EM 87% vs 人類 86.8%，「你當然不會相信」；Public 限次數＝有限次驗證，Private 更接近真實。(Taj1eHmZyWw S0066-S0070)
**D4 benchmark「超越人類」打折**：Switchboard 2016 宣稱超越聽打員；ImageNet error 3% 因 test 被許多人挑過，實用 error 應更大。看 test 是否公開、上線後是否成立。(WeHM2xpYQpw S0025-S0028; D_S6y0Jm6dQ S0029-S0030)
**D5 N-fold CV**：懷疑切分有怪 bias → 切 N 份（例 3）輪流當 val，候選各取平均，選最佳，再用全 training 重訓，最後 test。N 取多少他沒講。(WeHM2xpYQpw S0032-S0033; D_S6y0Jm6dQ S0030-S0031)
**D6 單次命中不是證據**：他預測本堂 107 分鐘命中，自稱「單純運氣好」，期待值仍看 val 誤差（約 3 分鐘）。(Taj1eHmZyWw S0098) 多跑看分佈是整理者建議。
**D7 遞迴預測**：用剛預測值再預測，他只說「先假設 2/25 是對的」，沒談誤差累積。(bHcJCp2Fyxs S0043)
