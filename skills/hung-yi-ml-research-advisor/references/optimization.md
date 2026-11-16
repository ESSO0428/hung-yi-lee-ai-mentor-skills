# 訓練動態與優化

症狀是 train loss 降不下去、震盪、發散、或換 optimizer／lr 後行為改變時讀這份。先走 skeleton.md 確認真的是 train 端的問題。引用 `(影片ID Sxxxx)`。年代差異寫在各條內。

## 0. 先判定：是 optimization 嗎？
- **症狀**：驗證不好。**先看 training loss**（沒記錄就無法診斷）。train 就差 → model bias 或 optimization；train 好、test 差 → overfitting 或 mismatch。「不要看到 performance 不好就說 overfitting」。
- **分辨 bias 與 optimization**：拿較淺或較簡單的模型當基準；更深的模型 train 反而更差（他的 56 層 vs 20 層例）→ optimization 沒做好，不是 overfitting 也不是 model bias。(WeHM2xpYQpw；xki61j7z-30 S0003-S0005；QW6uINn7uGk S0001)
- **為何先判定**：每個技巧只治一個環節。加資料、augmentation、L2/weight decay、dropout 只幫 generalization，train loss 降不下去時沒用，還可能更難 train；Adam 類換 optimizer 主要降 train loss，對 generalization 不保證有幫助。(mPWvAN4hzzY S0034-S0036, S0072-S0086)
  - 「更多資料會讓 optimization 更困難」複核只確認 augmentation 的版本，引用時限定在 augmentation。
- **大 batch 在 training 就變差**：這是 optimization 問題，不是 overfitting。(zzbr1h9sF54 S0009-S0010)

## 1. loss 卡住不降
**1a. 先看曲線，再下結論**
- 畫 loss 對 update 次數的曲線，**前幾次 update 就要看**。lr 太小：降得極慢。lr 稍大：很快降到平台就卡住（山谷兩壁來回震盪）。lr 太大：一瞬間飛出去，loss 越來越大。(yKKNr-QKz2Q S0006-S0008)
- 「update 後 loss 沒降」不見得是 bug，先調小 lr。理論上一階近似只在小範圍內成立，所以 lr 要夠小。(yKKNr-QKz2Q S0031-S0044)
- 他的反面教材：程式放著跑去打 LOL，回來才發現壞了，也不知道壞在哪。

**1b. 同時記 gradient norm，不要隨口說「卡在 local minima」**
- 平台期若 gradient norm 仍大，代表不是 critical point，多半是谷壁震盪，往 lr/optimizer 查。gradient norm 真的趨近 0，才進 1c。(HYUXEeh3kwY S0001-S0003)
- 他在實驗中看到：一般 gradient descent 常在 gradient 還大時 loss 就不降，「走到 critical point 其實很困難」。真正的魔王往往是 lr 與 error surface 形狀的搭配，不是 critical point。(HYUXEeh3kwY S0003-S0004)
- 2016 版也提醒：gradient 很小可能只是**高原（plateau）**，不等於接近 local minimum。(yKKNr-QKz2Q S0044-S0046)
- 措辭：說「critical point」，不說「卡在 local minima」。gradient 為零包含 local minima、local maxima、saddle point。(QW6uINn7uGk S0001-S0002)

**1c. gradient 真的≈0：saddle 還是 local minima**
- 看 Hessian eigenvalue：全正是 local minima、全負是 local maxima、有正有負是 saddle point。saddle 可沿負 eigenvalue 的 eigenvector 逃離。例：y=w₁w₂x 只有一筆資料時，原點 H=[[0,-2],[-2,0]]，eigenvalue ±2，沿 [1,1] 走可降 loss。(QW6uINn7uGk S0004-S0017)
- 實務上幾乎不算 Hessian（運算量太大），這招只是「最糟狀況的後路」。
- 高維直覺加經驗：參數動輒百萬，可走的路多；他展示的實驗中 minimum ratio（正 eigenvalue 比例）最高約 0.5-0.6，幾乎找不到全正的點。結論是 local minima 沒那麼常見，但這是**假說加經驗**，不是定理。(QW6uINn7uGk S0018-S0023)

**1d. 年代演進**：2016 把 local minimum 說成「只是幻想」，真問題是 plateau（yKKNr S0045）。2021 修正成「critical point 通常不是主因，先查 lr」，並補上 saddle 與 Hessian 工具。兩者都沒有說 local minima 不存在。

## 2. learning rate 與 optimizer
**2a. 單一固定 lr 兩難**：兩參數的 convex 長橢圓 error surface，lr=1e-2 在谷壁震盪、loss 降不下去；一路調到 1e-7 才不震盪，但平緩方向十萬次 update 仍到不了終點。所以不要只靠「調小 lr」，需要每個參數客製的 lr。(HYUXEeh3kwY S0004-S0006)

**2b. 原則**：平緩方向 lr 大，陡峭方向 lr 小，即 η/σ。σ 是過去 gradient 的 RMS。(HYUXEeh3kwY S0007-S0009；yKKNr S0009-S0013)
- 2016 加了理論：最佳步伐正比一次微分、反比二次微分，σ 用歷史一次微分估二次微分，不增加運算。「gradient 越大離最低點越遠」只在單一參數內成立。(yKKNr S0015-S0023)

**2c. 演進鏈 Adagrad → RMSProp → Adam**
- Adagrad：σ 對所有歷史等權平均。優點是平緩方向能越走越大。缺點是（1）後期整體越來越慢，學生反映「慢到令人髮指」（yKKNr S0014）；（2）同一方向先陡後平時，累積出很小的 σ，會突然「噴出去」再慢慢回來，反覆發生。(HYUXEeh3kwY S0012-S0019)
- RMSProp：σ_t = sqrt(α·σ_{t-1}² + (1-α)g²)，α 小則新 gradient 影響大，遇陡處能快速「踩煞車」。出自 Hinton 的 Coursera 課，沒有論文。(HYUXEeh3kwY S0013-S0016)
- Adam = RMSProp + Momentum。**用 PyTorch 預設值，不要隨便調**，他說自己調有時反而更差。2016 版也說「沒偏好就用 Adam，我覺得最穩」，但「實作比較複雜」。(HYUXEeh3kwY S0016-S0017；yKKNr S0014)
- 完整 optimizer = momentum（方向，保留正負號）÷ σ（大小，只留幅度）+ lr scheduling。兩者不會互相抵銷。(HYUXEeh3kwY S0024-S0025)

**2d. lr 排程**
- Decay：η 隨 update 遞減，一開始遠要快，越近越要煞車。他的例子加 decay 後末段不再亂噴。2016 版寫作 η/√(t+1)。(HYUXEeh3kwY S0019-S0020；yKKNr S0008-S0009)
- **Warm up**（先升後降，BERT、Transformer、ResNet 常見）：可能解釋是 σ 要統計足夠多筆才準，先用小 lr 收集 error surface 資訊。他說「我並不認為 warm up 已獲得完全的解答」。ResNet 論文先 0.01 再改 0.1，一開始就 0.1 反而 train 不好。進階讀 RAdam。(HYUXEeh3kwY S0020-S0024)
- 峰值高度、升降速度都是要手調的 hyperparameter，他沒給建議值。

## 3. batch 與 momentum
- **batch 越大單步不一定越慢**：MNIST、V100 實測，batch 1-1000 單步時間幾乎一樣（GPU 平行），到 10000-60000 才上升。一個 epoch 因 update 次數少，大 batch 反而更快。數字是特定硬體的實測值，叫使用者自己量。(zzbr1h9sF54 S0005-S0008)
- **小 batch 的 noise 對 optimization 有幫助**：不同 batch 的 loss function 不同，L1 的 gradient 為 0 卡住時，L2 不一定也卡。這是他給的「一個可能的解釋」。(zzbr1h9sF54 S0010-S0011)
- **小 batch 對 testing 也有幫助**：train 都調到一樣好之後，大 batch 的 test 仍較差，這才叫 overfitting（論文：小 batch=256，大 batch=資料集 0.1 倍）。解釋是 sharp/flat minima，他明說「尚待研究、不是每個人都相信」，不可當定論。(zzbr1h9sF54 S0011-S0014)
- **想要大 batch 的速度**：有論文做到（76 分鐘訓練 BERT、batch 約三萬），但「需要特別方法」，他沒講。(zzbr1h9sF54 S0015-S0016)
- 結論：batch size 是 hyperparameter。
- **Momentum**：m_{t+1}=λm_t−ηg_t，等價於過去所有 gradient 的加權和。gradient 為 0 時前一步方向仍可帶著走，像球滾過 saddle 甚至翻過小丘。λ 要調，他沒給建議值。(zzbr1h9sF54 S0016-S0021)

## 4. 不同方向坡度差很多：從輸入尺度與 normalization 下手
- **檢查**：各 feature 的 range 是否差很多（例：x1 約 1-2，x2 約 100-200）。x2 大則 w2 小動就讓 loss 大變，該方向是尖峽谷，error surface 是長橢圓，要 adaptive lr 才救得了。(yKKNr S0026-S0031；BABPWOkSbLE S0001-S0004)
- **做法**：對每個維度用訓練資料算 m_i、σ_i，令 x̃=(x−m_i)/σ_i。scale 接近時等高線接近圓形，gradient 直指圓心。他說方法「千百種，選一個你喜歡的」。(yKKNr S0030-S0031；BABPWOkSbLE S0005-S0006)
  - 這是對 gradient descent 型模型的建議，他沒談樹模型是否需要。
- **hidden layer 也要**：對 W2 而言前一層的 z 或 a 也是 feature，所以有 Batch Norm。(BABPWOkSbLE S0006-S0007)
- **BN 細節**：
  - 位置：放在 activation 前或後差異不大，要自己試。用 sigmoid 時較建議對 z 做，因為 0 附近斜率大。(S0007-S0008)
  - 加 γ、β 並用 γ=1、β=0 初始化，讓訓練初期各維度分布接近。(S0013-S0014)
  - 要夠大的 batch 才算得出有意義的 μ、σ；batch size=1 時沒有 μ、σ 可算。(S0008-S0012)
  - **testing 用 training 累積的 moving average**，PyTorch 已處理；p 他記得預設 0.1（他自己不確定）。(S0014-S0016)
- **效果**：原論文（Inception）有 BN 約用一半或更少時間達到同樣 accuracy，最終 accuracy 差不多；sigmoid 沒 BN 根本 train 不起來，有 BN 就可以；lr 乘 5 可行，乘 30 比乘 5 差，作者沒解釋。(BABPWOkSbLE S0016-S0018)
- **BN 為何有用**：不要答「解決 internal covariate shift」。他引用 "How Does Batch Normalization Help Optimization" 反駁該說法，較有支持的是 BN 讓 error surface 較平滑。但其他平滑方法效果差不多，BN 像盤尼西林是「意外之喜」。(BABPWOkSbLE S0018-S0021)
  - BN 只談 training 動態，他沒談對 generalization 的影響。

## 5. loss function 也是 optimization 的旋鈕
- **分類用 cross-entropy，不要預設 MSE**。兩者最佳解相同，差別在優化難度：MSE 在 loss 大的區域非常平坦（gradient≈0），初始點若落在那裡就走不動；cross-entropy 在同處有斜率。示範是 3 類、y3=-1000 的簡化設定，他給的是例子不是證明。(O2VkP8dJ5FE S0010-S0014)
  - 用 Adam 時「也許還有機會走到」，但起步慢、訓練較難。
  - 結論（改寫）：loss function 的選擇本身會改變 optimization 難度，所以 train 不起來時也要把 loss 選擇列入診斷。
- **標籤與輸出層**：類別間沒有遠近關係時用 one-hot，不要編成 1、2、3 去做 regression（等於預設 1 比較靠近 2）。輸出經 softmax 後與 one-hot 比較；softmax 輸入叫 logit。二類時 sigmoid 與 softmax 等價。(O2VkP8dJ5FE S0002-S0008)
- **PyTorch 陷阱**：CrossEntropyLoss 已內含 softmax，最後一層不要再加，否則變成加兩次 softmax。後果細節他沒講。(O2VkP8dJ5FE S0010-S0011)
- cross-entropy 與 maximum likelihood 是同一件事。

## 6. 旁註：模型大小與資料量
- 壞訓練集機率上界 ≤ 2|𝓗|exp(−2Nε²)，N 大、|𝓗| 小較安全，但實算常 >1，只用來解釋原理。縮小 |𝓗| 會讓「理想」本身變差（兩難），他說深度學習能兼得，但該課沒講。(_j9MVVcvyZI S0045-S0054)
