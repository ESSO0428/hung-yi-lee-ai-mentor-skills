# 課程沒講的部分

李宏毅的課程沒有涵蓋下列主題。使用者問到時照實說「課程沒講」，再另開一段標明「一般 ML 補充」回答，不歸給他。各條數字（71、122、1143、0.38k 等）是 toy 例，不可當門檻。

## 診斷骨架與評估
- 「train loss 多大算大」無數值；無 bias／variance 量化門檻、無 learning curve（D_S6 明說）。noise ceiling、Bayes error、label noise、headroom：0 命中。無 bias²+variance+noise 正式分解。
- data-size 外推（僅 LLM scaling）；bias-variance 在 deep／大模型的行為。
- 資料洩漏、時間序列切分、group/stratified CV、i.i.d. 假設；他的 CV 只講隨機切；validation 比例、N 取值。
- 補救 val 被用壞的做法（換新 val、hold-out）、|H_val| 門檻：xQXh3fSvD1A 未涵蓋。
- seed 變異、CI、nested CV、paired comparison；指標選擇（F1/AUC）、不平衡、calibration、error slicing；mismatch 偵測（adversarial validation）。
- 表格／樹／p>>n／小樣本：例子皆影像、語音、NLP、toy regression，toy 數字（71、122、1143、0.38k）不可當門檻。
- optimization 失敗系統性排查順序；batch／lr／epoch 建議值。2016 技術（RBM pretrain、sigmoid 預設）過時。

## 優化
- 具體數值與搜尋策略：lr 範圍、warm up 長度與峰值、λ、α、batch size 如何選、大 batch 配 lr 的縮放規則。他只說這些是 hyperparameter。
- gradient clipping、weight initialization 與梯度消失/爆炸（2025 只簡述 initialization 影響 optimization）、混合精度、mini-batch 版 SGD 的 noise 理論。
- AdamW 與 weight decay 的差別、SGD+momentum 與 Adam 的泛化差異。
- 其他 normalization（LayerNorm、GroupNorm）的細節：逐字稿在列出前就截斷。小 batch 時 BN 的替代方案也沒講。
- 類別不平衡、label smoothing、focal loss、log-softmax 數值穩定性。
- 自動偵測 gradient norm 異常的門檻、判斷高原的具體方法、如何量 sharpness。
- 回歸任務的 loss 選擇（Huber、MAE）、損失函數加權。
- fine-tune 時 backbone 與 head 用不同 lr、layer-wise decay：課程只有作業提示「調 lr」。
- 時間序列或表格資料上的 optimizer 選擇。

## 泛化、shift、微調、遺忘
- covariate/label shift/concept drift 正式術語、shift 檢測（adversarial validation、KS、PSI、MMD）、嚴重度量化、用 learning curve 判斷 mismatch vs overfitting。
- importance reweighting、OOD detection、校準與不確定性在 shift 下的處理；shortcut 無通用診斷（只有 VQA 實例）。
- 時間序列切分（time/blocked/walk-forward）、group 切分；觀看人數例是 lag-window 預測，但沒講切分規則。
- 表格、小樣本、樹模型、基因組資料的遷移或 shift；所有 DA 範例是影像與語音，遺忘範例是 LLM／語音 LLM，影像模型的遺忘幾乎沒講。
- 微調 LR、layer-wise LR、warmup、解凍順序、linear probe vs full FT 量化比較、backbone 選擇；LoRA rank 依資料量選；何時放棄微調改 prompt／RAG（只有「先試 prompt」的原則）。
- 遺忘的量化閾值；參數重要性 λ_j 怎麼算；merge 失敗原因；Machine Unlearning 的系統性評估；各後訓練方法之間的決策樹與定量比較。
- DIRT-T、MCD、Universal DA、DG 的具體做法。助教補充課（gvfLq4sPW4k、-DQBMAULXX8）ASR 太髒，只能當指針。

## Shortcut、可解釋性、架構
- 發現 shortcut 後怎麼修（統一格式、去浮水印、重採樣）；shuffled-label、majority baseline、dummy baseline；group／來源／時間切分；confounder、group DRO。
- 驗證 saliency 本身可信的 sanity check；Grad-CAM、SHAP、permutation importance；表格／時序／基因型的可解釋性。
- 實用的有效感受野公式；ViT 專講、預訓練 backbone 選擇與 PEFT；「小資料」的量化門檻。
- GNN 的 transductive／inductive 洩漏與 graph 切分；度量學習的 hard negative、margin、閾值；learning to rank 與 NDCG/MRR（僅「負例必須提供」有一句，OYN_GvAqv-A）。
- LLM 解釋的忠實度評估標準（他明說無標準）。

## 傳統模型、ensemble、不確定性
- GBDT 實務：XGBoost/LightGBM/CatBoost、shrinkage、樹數與深度、early stopping、categorical 特徵；決策樹的 Gini/剪枝/缺失值；ensemble 的推論成本、diversity 量測、AdaBoost 對標籤雜訊敏感、多類 AdaBoost。
- Gaussian process、SVM kernel 選擇與 C/gamma、樹模型是否需要 scaling、表格 feature engineering、leakage 稽核、迴歸殘差診斷、特徵重要性/SHAP。
- 類別不平衡的處理手段：class weight、focal loss、SMOTE、threshold moving、PR-AUC vs ROC-AUC、precision/recall/F1、stratified split、prior shift 校正。
- 不確定性：reliability diagram 與 ECE 公式、temperature scaling、Bayesian NN、MC dropout、deep ensembles 作 UQ、conformal、預測區間、aleatoric vs epistemic、selective prediction、seed 變異與顯著性檢定、bootstrap CI。
- 傳統方法 vs DNN 在表格上的實證比較（SELU 講座有一份排名表但 ASR 太差，只列 待核）。

## 小資料、半監督、預訓練資料
- 「多少資料才夠」的樣本量門檻、learning curve 外推、noise ceiling/Bayes error、label noise 偵測。
- 現代半監督（FixMatch、consistency regularization、confirmation bias）、pseudo-label 信心門檻（他說 open question）、labeled/unlabeled 分布不同時怎麼辦。
- 表格、p>>n、時間序列、樹模型的小資料處方；非影像/語音的 augmentation；類別不平衡與小樣本交互；group/blocked CV。
- 微調的學習率、layer-wise LR、解凍順序、linear probe vs full FT 的量化比較、backbone 選擇準則；few-shot / meta-learning 可用處方（轉寫不堪用，未驗證）。
- 小資料下的 validation set 被過擬合只有理論或 ASR 極差的來源；SFT 如何有效教新知識（他說「下回分解」）。

## 領域邊界
- 例子多為影像、語音、NLP、toy regression；表格、樹、p>>n、小樣本基因型資料不在範圍內。
- 2016 技術（RBM pretrain、sigmoid 預設）過時；2021 講次稱 RNN「這門課不會提」。
