# 泛化與分佈偏移：overfitting、mismatch、domain shift、遷移

症狀是 train 好、val／test 差，或換資料來源後崩盤時讀這份。第一個動作永遠是區分 overfitting 與 mismatch（A）。微調、遺忘、LoRA 見 finetune-forgetting.md。他用詞是 "domain shift"／"mismatch"，不是 covariate shift／OOD。

## A. 分數掉了：先分辨是 overfitting 還是 mismatch
- 症狀：benchmark 很高，換資料來源／時間／裝置後崩盤；或 train 好、test 差。
- 檢查：train 與 test 的產生方式是否相同（時間、來源、批次、設備）。他說判斷靠「你對資料本身的理解」，沒給統計檢定。train loss 小、test loss 大才叫 overfitting。
- 做：overfitting → 加資料、正則化有效；mismatch → 「訓練資料再增加也沒有幫助」，要改切分、換資料或做 adaptation。他承認有人把 mismatch 算進 overfitting，重點是成因與處方不同。
- 例：COVID 觀看人數，2020 訓練、2021 測試「怎麼做都是慘」，作業因此改切分。2/26 單日暴增是外生異常事件，與「年度分布不同」是兩件事，勿混為同一機制。他明說多數作業已設計成沒有 mismatch。觀看人數課另有 train 與 unseen loss 並列的示範（約 0.1k–0.2k vs 0.4k 級，數字出自較髒的轉寫，只當量級）。
- VQA 例：只看問題不看圖就約 48%（benchmark 有 shortcut）；VQA-CP 故意讓訓練與測試分布不同，50%+ 掉到約 30%（ASR 數字待核）。這是課程中唯一的 shortcut／shift 實例，沒有通用診斷法。
- 為什麼：benchmark 多半假設無 shift，會給人「AI 超越人類」的錯覺；真實應用只要分布稍有差異，表現就是「未知數」。
- (WeHM2xpYQpw S0035-S0036)(Mnk_oUrgppM S0001-S0002)(h_Lptoq8spQ S0051-S0052)

## B. 先命名 shift 型態，再選處方
- 三型：(a) 輸入分布變（黑白→彩色）；(b) 輸出分布變（某類突然特別常見）；(c) 輸入輸出關係變（同圖案訓練叫 0、測試叫 1，較罕見）。
- 他的方法只處理 (a)；(b)(c) 只點名，沒給處方，advisor 要照實說。他也沒講如何診斷 gap 由哪些因素造成（無錯誤分析 checklist）。
- 數字：數字辨識黑白訓練、彩色測試只有 57%（原論文 57.5%，直接用 target 訓練皆 90%+）。
- 診斷時先量兩個數字夾住問題：source→target 的 baseline 與 target→target 上限（推論，源自其對照表結構）。
- (Mnk_oUrgppM S0002-S0004, S0015)

## C. 依「對 target 知道多少」選方法（決策階梯）
1. target 大量有標註 → 不需 adaptation，直接用 target 訓練。
2. 少量有標註 → 用 source 模型當初始值微調，「兩三個 epoch 就足夠」（見 D）。
3. 大量無標註 → Domain Adversarial Training（見 E）。
4. 無標註且極少（一張）→ Testing Time Training（Mnk 只給連結；EnW 才講做法，見 finetune-forgetting.md K）。
5. 一無所知 → Domain Generalization：訓練含多個 domain，單一 domain 就用 data augmentation 造多個 domain。細節「不細講」。
- (Mnk_oUrgppM S0005-S0006, S0022-S0023)

## D. target 標註很少：微調要保守
- 症狀：只用少量 target 訓練「一定會壞掉」；全模型微調跑太多又對那幾筆 overfit。
- 做：source 模型當 initial value 再訓練；iteration 不要多、learning rate 調小；或 conservative training：新舊模型對同一筆資料輸出越近越好，或參數 L2 距離越小越好。
- 更少參數：layer transfer，copy 一部分層、只訓其餘（可能只訓一層），「只需要考慮非常少的參數就可以避免 overfitting」。target 夠多時仍可微調全部。
- 哪幾層 copy「case by case，運用之妙，存乎一心」。語音常 copy 後幾層、重訓靠近 input 的層（說話者口腔不同，差異在 input 端）；影像常 copy 前幾層、重訓後幾層（前層是通用線條幾何）。通則是推論：先問「差異來源發生在網路哪一端」。
- 沒給具體 LR、步數、凍結層數、解凍順序。
- (qD6iD4TFsdQ S0009-S0014)(Mnk_oUrgppM S0006)(F58vJcGgjt0 S0011-S0012)

## E. target 大量無標註：Domain Adversarial Training（DANN）
- 做：網路切成 Feature Extractor θf + Label Predictor θp，另接 Domain Classifier θd。θp 最小化 source 分類 L；θd 最小化 Ld；θf 最小化 L − Ld（幫分類又騙過 domain classifier）。target 無標註資料只走 domain classifier。實作用 gradient reversal layer。切在第幾層是 hyperparameter。
- 結果：黑白→彩色 57.5→81、59→71、74→88.7，仍與直接用 target 訓練的上限有大 gap。
- 注意：
  - extractor 不能輸出零向量作弊，因 label predictor 也要用同一 feature（「不能放大絕」）；單只騙 domain classifier 太容易。
  - 與 GAN 一樣難 train；「domain classifier 必須夠強」是轉述推論，原話偏向「要同時讓 label predictor 做對」。
  - 騙 domain classifier 的權重太大，latent space 結構會被毀；權重要調，沒給數值，他說作業算偏難。
  - 分布對齊還不夠，要讓無標註 target 點遠離 decision boundary：他說 label predictor 輸出越集中某一類越好。他沒用 entropy minimisation 這名詞（推論）；DIRT-T（S0018 只提名）、Maximum Classifier Discrepancy 只指路。
  - source/target 類別集合不同時，硬對齊會讓老虎變得像狗，見 Universal Domain Adaptation（只指路）。
  - 他留思考題：用 −Ld 其實仍在「分開」兩 domain，原始作法未必最好。
- 診斷法：t-SNE 畫 source/target feature，若各成一團「根本不在同一個位置」，classifier 只會處理 source 那塊（量化 domain classifier accuracy 為推論）。
- (Mnk_oUrgppM S0007-S0021)(qD6iD4TFsdQ S0026-S0034)

## F. 限制彈性的旋鈕（overfitting 確定之後）
- Augmentation 要保留標籤語意：鳥可翻轉、朝向任務不可；語音辨識可變聲、語者辨識不可；上下顛倒圖不合理；Mixup 連 label 一起混。(WeHM2xpYQpw S0016；mPWvAN4hzzY S0073)
- Dropout：只在 train loss 低、val 降不下去時用，「要注意使用一個技術的時機」；換 optimizer（Adam）降 train loss 不保證 val；overfit 時 weight decay/AdamW 是選項。(mPWvAN4hzzY S0075–S0085)
- Regularization（L2）：loss += λΣw²，參數小 → function 平滑 → 對輸入雜訊不敏感；λ 要手調。例 test error：λ=0 102、1 68、10 25、100 11.1、1000 12.8，更大到 26.8（最平滑是水平線）。bias b 不正則化（只上下平移）。D_S6y0 提醒 regularization 會傷 bias。(fegAeph9UaA S0068–S0075；D_S6y0Jm6dQ S0024)
- 用 test 選了 degree/λ 後，上線誤差預期比 11.1 高；validation 次數多了自己也會 overfit。(fegAeph9UaA S0082；Taj1eHmZyWw)；小資料用 N-fold 取平均。(WeHM2xpYQpw S0035)

## G. 遷移值不值得做、會不會變糟
- 前提是 target 少、source 多；target 很多就當一般 ML。(qD6iD4TFsdQ S0002, S0008)
- 只在乎 target → fine-tune；兩邊都要 → multitask：前幾層共用、後面分叉，前提是兩任務有共通性。(qD6iD4TFsdQ S0019-S0020)
- negative transfer 存在；事前只能 try and error，progressive neural networks 是當時方案，他說「怪怪的」；課程沒有量化 source/target 相似度的方法。(qD6iD4TFsdQ S0023-S0025)
- Bengio 2014 ImageNet（500/500 類切分、target 60 萬張）：只 copy 前 1-2 層且凍結約持平，copy 太多變差；copy 後再微調全模型每個 case 都進步，他「滿 surprised」；凍結前層只訓後層有時變差；自然物 vs 人造物差很多時效益下降。這是大 target 資料，與 D 的小資料保守建議方向不同，不可併成一條規則。(qD6iD4TFsdQ S0014-S0018)
- 遷移比預期遠：語音幾乎所有語言都可 transfer；歐語＋中文 multitask，中文資料少時最明顯，口述「只需二分之一以下資料」（數字口述，以 paper 為準）。(qD6iD4TFsdQ S0021-S0023)
- 凍結 upstream＋輕量 downstream 是可行基線（SUPERB）：downstream 刻意做弱（能 Linear 就 Linear）才能歸功於表徵；要有「不預訓練」baseline 逐任務比；只用最後一層常輸 baseline，改成各層可學習 weighted sum（中間層常最有用）後多數任務勝出；fine-tune upstream 通常更好，評比時刻意不做；Large 在第一輪反輸 Fbank（原因只是猜測）。他事前推論「目標衝突、表徵必為專才」被實驗「光速打臉」，所以別只靠推論。僅限語音 10 任務，無遺忘討論。(MpsVE60iRLM S0005-S0018)

## H. zero-shot（class 沒見過）
- 必須給橋梁：attribute（每 class 要有獨一無二 attribute）、attribute/word-vector embedding（loss 只拉近成對會塌縮，要 margin 拉開不成對者）、語音的 phoneme + lexicon。誠實失敗例：草泥馬。(qD6iD4TFsdQ S0035-S0048)
