# 傳統模型、ensemble、成本與不平衡、不確定性

症狀是撞牆後想用 ensemble、用傳統模型（樹、SVM、logistic regression）、評估不平衡或成本、或要談信心／校準時讀這份。原理層有完整講座；實務層（GBDT 調參、表格特徵工程、校準方法、不平衡處理手段）課程沒有，見 not-covered.md。

## A. 先判斷：要不要用 ensemble、用哪一種

**A1. 已經想不到新招、手上有多個可用模型 → 做 ensemble。** 他稱為「大招，可以迅速 improve performance」；Kaggle 要奪冠通常需要 ensemble。前提是前面的 bias/variance 診斷已做，ensemble 是「撞牆後的下一招」，不是第一招。他沒講推論成本與部署代價。(tH9FH1DH5n0 S0003)

**A2. 看失敗型態選 Bagging 還是 Boosting。**
- 症狀：train 低、val 高（複雜模型 variance 大，如深樹）→ Bagging / Random Forest，目的只是降 variance。
- 症狀：train 本身就高（模型太弱 fit 不了）→ Boosting（或加容量），Bagging 沒用。
- 他的原話：「Bagging 是用在很強的 model，Boosting 是用在弱的 model」。
- 實驗：深度 5 的樹做 100 棵 RF 仍 fit 不出初音圖形，只是更平滑；同樣深度 5 的樹做 AdaBoost，T=10 輪廓出來、T=20 好很多、T=50 幾乎、T=100 近乎完美。「Bagging 不會讓模型更能 fit data」。
- 與 bias/variance 一致：bias 大時「collect 更多 data 沒有用」，要改 model；variance 大時加資料、regularization、augmentation 才有效。
(tH9FH1DH5n0 S0004 S0007 S0014 S0063; D_S6y0Jm6dQ S0018)

**A3. 誰才需要 Bagging：看你能不能在 training set 上做到 100%。** 決策樹、KNN 想要就能 100%（樹夠深每筆一片葉子，「樹夠深可以做出任何 function」），所以 training 100% 沒有資訊、只代表 overfit。NN 常見的問題反而是「沒辦法在 training set 上 overfit」，所以不要預設 NN 一定要 Bagging。這是他的經驗判斷，沒給 NN 何時會 overfit 的條件。(tH9FH1DH5n0 S0007 S0008; xki61j7z-30 S0002)

## B. Bagging / Random Forest 怎麼做、怎麼驗證

**B1. Bagging**：從 N 筆有放回抽 N' 筆（通常 N'=N）造多個資料集，各訓練一個複雜模型；regression 取平均、classification 投票。理由用「平行宇宙抓寶可夢」：不同宇宙訓練出差很多但 bias 小的函數，平均後 variance 變小。(tH9FH1DH5n0 S0004 S0006)

**B2. Random Forest 光 resample 不夠**：只 resample 得到的樹彼此太像，variance 降不下來。要在每個分支隨機禁用部分 feature / 問題，連同一份資料也會長出不同的樹。他沒給保留比例。(tH9FH1DH5n0 S0011 S0012)

**B3. Out-of-bag（資料少、不想切 validation）**：對每筆樣本只用「沒用它訓練」的子模型集成預測，再對全部樣本平均 error，即 OOB error，可當 testing 估計。例：4 筆資料、4 個子模型，x1 只由沒看過它的 f2、f4 預測。只適用 Bagging 類。(tH9FH1DH5n0 S0012 S0013)

**B4. 單棵樹**：用深度調擬合度（初音例：深 5 只框一個方塊、10 有鋸齒、15 有突起、20 完美）。設計點有分支數、分裂 criterion、停止條件、可問問題集合，但他說「秒講過去」，沒教 Gini/entropy、剪枝、缺失值。(tH9FH1DH5n0 S0009 S0010)

**B5. Dropout 是「終極 ensemble」**：M 個神經元對應 2^M 個子網路，testing 時用權重乘 (1−p) 近似平均；此近似只在網路接近 linear 時才等於 ensemble 平均。這是 NN 內的類比，不是表格建模。(xki61j7z-30 S0058)

## C. Boosting 與 Stacking

**C1. Boosting 前提與保證**：base learner 在加權 training set 上錯誤率要嚴格 < 0.5（二元分類，比亂猜好一點就行）。保證的是 training error 可降到 0，不是 testing。序列式訓練，不能像 RF 平行。若 ε>0.5 把輸出反轉即可。(tH9FH1DH5n0 S0014 S0016 S0022)

**C2. AdaBoost 的 reweight 機制**：找新權重使 f1 在新權重下錯誤率剛好 0.5（等於亂猜），再訓練 f2，則 f2 必在做 f1 不會的事。實作：錯的樣本乘 d=√((1−ε)/ε)、對的除以 d。數字例：4 筆權重全 1，f1 錯 1 筆，ε=0.25，d=√3，錯的權重 √3、對的三筆各 1/√3，新錯誤率 0.5。比喻：考完改配分，讓 f1「發狂生氣」。(tH9FH1DH5n0 S0020 S0023 S0024 S0025)

**C3. 最終組合用 α_t 加權而非平均**：H(x)=sign(Σα_t f_t(x))，α_t=ln√((1−ε_t)/ε_t)。ε=0.1→α≈1.1；ε=0.4→α≈0.2；ε=0.3→d=1.53、α=0.42。decision stump 示範：3 個 stump 各自 ε=0.3/0.21/0.13，都不完美，加權後 10 筆資料 training accuracy 100%。(tH9FH1DH5n0 S0036 S0041 S0044)

**C4. 加權訓練與 resample 等價**：權重是整數時可用抽樣（抽兩次=權重 2）；一般用法是把權重乘進每筆 loss，Σ u_n·l(f(x_n), ŷ_n)，可用小數。這是 AdaBoost 脈絡的機制說明，不是他對不平衡的建議。(tH9FH1DH5n0 S0018 S0019)

**C5. weak learner 不能 training error=0**：ε=0 時 α 未定義，演算法出問題。故 base learner 要限制容量（stump／淺樹）；此建議是由他的話推出，不是原話。(tH9FH1DH5n0 S0058)

**C6. training error 到 0 之後還能繼續加 weak learner**：看 margin ŷ·g(x)。AdaBoost 的 objective 是 exp(−ŷg)，在 ŷg>0 區仍會隨 margin 增大而下降，所以約 5 個 iteration 後 train error 為 0，但 test error 在加到 100~1000 個時仍可下降。是現象層面的解釋，不是保證；他沒說加到多少停。證明骨架：Z_t=Z_{t−1}·2√(ε(1−ε))，ε<0.5 時 Z 嚴格遞減，training error 上界遞減（他措辭保守：「可能也會越來越小」）。(tH9FH1DH5n0 S0048 S0057 S0063)

**C7. Gradient Boosting = function space 的 gradient descent**：g_t=g_{t−1}+α_t f_t；f_t 對齊 −∂L/∂g，固定 f_t 後做 line search 找 α_t（理由：「找出 f_t 成本高，要好好珍惜它」）。最大好處是「可以任意更改 Objective Function」。他只用 exp loss 推導，沒講 shrinkage、樹深、subsampling、XGBoost/LightGBM。(tH9FH1DH5n0 S0065 S0078 S0080)

**C8. Stacking（他稱「非常實用」）**：把各模型 output 當 feature 訓練 final classifier，不用 majority vote（不分好壞）。final classifier 可以只是 logistic regression，它會自動壓低爛模型的權重。資料要分兩份：一份訓練 base models，另一份訓練 final classifier；否則「只把 training data 背起來」的模型看起來 error 為 0，會被 final classifier 完全信任。後者稱「洩漏」是整理者的詮釋，原話是被死背的模型騙。(tH9FH1DH5n0 S0081 S0082 S0083)

## D. 傳統模型的選擇與診斷（原理層）

**D1. 分類 loss：看梯度行為。** logistic regression 用 cross entropy 不用 square error：離目標遠時 square error 的微分也是 0，隨機初始化通常離目標很遠，「一開始就卡住」。hinge（SVM）與 cross entropy 實作差別「沒有想像的顯著」；hinge「及格就好」、較不怕 outlier。linear SVM 與 logistic regression 的差別只在 loss。(hSXFuypLukA S0017 S0021; QSEPStBgwRQ S0013 S0014)

**D2. Generative vs discriminative：差在假設而非函數集合。** 每類各一個 covariance → 參數多 → variance 大 → 兩類 share covariance。Naive Bayes 強不強取決於獨立假設是否成立；假設很不成立則 bias 大。binary feature 應假設 Bernoulli，不要硬套 Gaussian。(fZAZUYEeIMg S0032 S0043; hSXFuypLukA S0022)

**D3. 線性迴歸診斷流程**：比較 training/testing 走勢辨別 overfit；檢查是否漏掉關鍵 feature（例：物種這個類別 feature，用 indicator 乘 Xcp 仍是 linear）；調 λ：training error 單調升、testing error 先降後升（他的例子 102→68→25→11.1），太大變水平線；regularization 不碰 bias（b 只是上下平移）。他誠實說用 testing set 選模，上線誤差會比 11.1 更高。(fegAeph9UaA S0051 S0060 S0067 S0075)

**D4. Feature scaling 是為了最佳化條件**：各 feature 範圍差很大時 loss surface 是長橢圓，同一 learning rate 搞不定。這是對梯度法模型的建議；他沒講樹模型需不需要。(yKKNr-QKz2Q S0026 S0029)

**D5. 年代差異**：2016/17 版 Ensemble 與 2021 版 bias/variance 講法一致，無矛盾；傳統方法在 2021 之後的課程只作對照與歷史背景（Dr-WRlEFefw：deep learning 之前要人工 feature engineering，之後改成設計 network）。

## E. 成本、不平衡、評估指標

**E1. 不平衡下不要只看 accuracy。** 症狀：正類（異常／詐欺／疾病）很少。檢查：「全判正常」的退化系統 accuracy 多少。他的例子：100 正常 + 5 異常，把 105 筆全判正常 accuracy 100/105 > 95%，但那是什麼都沒做的爛系統。他沒用「imbalance」一詞，是在異常偵測脈絡講。(ueDlm2FkCnw S0005 S0006)

**E2. 兩種錯誤分開數、用 cost table 決定哪個系統好。** 例：λ=0.5 時 1 false alarm、4 missing；λ 較高時 6 false alarm、3 missing。cost A（missing 扣 1、false alarm 扣 100）：104 vs 603，左好；cost B（missing 扣 100、false alarm 扣 1）：401 vs 306，右好。「系統好壞取決於你覺得 false alarm 還是 missing 比較嚴重」。cost 由任務決定，癌症篩檢傾向 missing 重。他沒給 false alarm 較重的真實例。(ueDlm2FkCnw S0006 S0009)

**E3. 不想訂 threshold → 排序型指標 AUC。** 他只點名 AUC，沒教 ROC 如何畫、何時選哪個；HW8 用 ROC-AUC。(ueDlm2FkCnw S0010)

**E4. dev set 要模仿 testing set**：同時含正常與非正常，標籤只需正常/異常，不用細類別；用它調 threshold。注意他的例子只有 5 張異常，沒討論統計不確定性。(ueDlm2FkCnw S0002)

**E5. 類別頻率會寫進模型。** generative 分類器的 prior 就是訓練集計數（79 水系 vs 61 一般系）；增量學習中保留少量舊類樣本與大量新類樣本，模型會偏向樣本多的 label（TA 補充課，論文用 bias correction，限增量學習）。測試時 label 機率改變也是一種 domain shift（只點名，無校正法）。GAN 課旁白：訓練 classifier 時「怕 data imbalance」，所以兩類各取 256。這些都很弱，不可外推成不平衡 recipe。(fZAZUYEeIMg 約 line 63; SX6_1-mvkWk 約 line 135; DMA4MrNieWo 約 line 219; 8AKqH6V9kjE 約 line 83)

## F. 不確定性與「知道自己不知道」

**F1. 用分類器 confidence 做異常/OOD 偵測：流程。** 用正常資料訓練分類器 → 取 confidence（softmax 最大值，如 0.97 vs 0.26；或 entropy）→ 高於 λ 判正常。(ueDlm2FkCnw S0001; cYrNjLxkoXs confidence 段)

**F2. 看相對排序，不是絕對值。** 異常圖也可有 0.998，但超過 75% 的正常圖更高（很多是 1），方法仍有效。個案如某張正常圖信心特別低被誤判，他自己也不知道原因。(ueDlm2FkCnw S0003 S0004)

**F3. confidence 的失敗模式與捷徑檢查。** 「有些東西比貓更像貓」（老虎、狼）→ 未知但特徵強烈的物件得高信心；無任何特徵（羊駝）落在 boundary 反而信心低。探針：把人臉塗黃，辛普森分類器信心 82%，頭髮也塗黃變 100%，他自己的臉塗黃也 88%（現場示範，非通則）。補救：蒐集得到異常資料時訓練時給異常高 entropy；收不到時用 generative model 造「像但不太像」的假異常（他保持旁觀，不背書效果）。(XwkHOUPbc0Q S0001 S0002 S0003)

**F4. Calibration：信心與實際正確率要對得上。** 檢查：橫軸信心、縱軸實際正確率，理想貼近對角線；差距彙整為 ECE。LLM 脈絡：預訓練 GPT-4 calibration 不錯，做完 RLHF 反而「失去 calibration」；因此後訓練前後各看一次。他引的是 GPT-4 技術報告的單一模型結果，沒給補救（如 temperature scaling）、ECE 公式或成因。另一講提到小模型不管瞎掰與否信心都差不多、大模型才有相關（見 SaZTJJNOCOY）。(kslijcrYizE S0008 S0009; SaZTJJNOCOY 約 line 43)

**F5. 重複取樣的變異。** 同設定不固定 seed 訓練三次 loss 不同（7 點多、9、更差），「這次運氣比較差」；他沒給跑幾個 seed 或如何報告。多次取樣 majority vote 是 LLM 「不容易打敗的 baseline」（嘗試次數 2^1 到 2^8，正確率隨之上升）；LLM-as-judge 應取輸出機率加權平均（1×0.3+2×0.3+3×0.4=2.1），不要只取單點。(mPWvAN4hzzY 初始化 demo 段; bJFtcwLSNxI 約 line 63; dWQVY_h0YXU S0033)

**F6. 誠實語氣**：他對單一例子明說「這只是猜測，只有一個例子」（kslijcrYizE S0006），可作為回答不確定性問題時的語氣。
