# Shortcut、可解釋性、架構 inductive bias、結構化資料

症狀是準確率高得不合理、想知道模型憑什麼答對、選或搬架構（CNN／self-attention／GNN）時讀這份。M9ht8vsVEw8 是助教姜成翰的補充課，引用須標「助教」。

## A. 準確率高得不合理 → 懷疑 shortcut
- **症狀**：train/test 都很高（例：寶可夢 vs 數碼寶貝，98.9%/98.4%，人類都難分）。**先排除 overfitting**：test 沒看過的圖仍高，代表不是記憶，是學到錯誤線索。**要做**：不只看 accuracy，問「它憑什麼答對」。(WQY85vaQfTI S0001 S0002 S0019)
- **查什麼**：兩個類別在資料蒐集管道上有沒有系統性差異。例：寶可夢全是 PNG（讀進來背景黑），數碼寶貝是 JPEG，模型只看背景；PASCAL VOC 2007 的馬圖很多來自同一網站，左下角有同樣英文字，saliency 顯示左下角最重要，「它根本不需要學習馬是長什麼樣子」。(WQY85vaQfTI S0020 S0021；複核對 PASCAL 例的 ASR 字面未能 grep 到，逐講筆記有引文，引用時保守)
- **意義**：同來源切出的 held-out 也會 98%，所以 test 高不能排除捷徑（此為 gap 報告對課程例子的推論，非他原話）。他強調這不是玩具問題，「不會發生嗎？會」。
- **做法（他有講的）**：對一批「答對」的樣本畫 saliency，看亮點是否在物件本體；落在四角、背景、邊框就是警訊。**修法他沒講**（見 D）。

## B. 想知道模型看什麼（影像／輸入歸因）
1. **Occlusion**：在不同位置放灰色方塊，記錄目標類別機率，畫熱圖。遮狗臉機率掉、遮周邊不變→看的是臉；阿富汗獵犬圖有兩個人，遮人臉不變、遮狗才掉。原則：「某個 component 刪掉後輸出大變，就代表沒它不行」。(WQY85vaQfTI S0014-S0016；rZzfqkfZhY8 S0008-S0010 對 LLM 輸入同理：遮「好」→ 沒 nice，遮「請」→ 不變)
2. **Gradient saliency**：對每個 pixel 算 loss 的 |Δe/Δx|，越大越亮；不用逐一遮擋。(WQY85vaQfTI S0016-S0018)
3. **雜訊多 → SmoothGrad**：加約 100 種雜訊各算一張再平均。但他坦白：不能證明更接近模型真實想法，也許模型真的覺得草和天空重要；圖乾淨 ≠ 更忠實，只是更好看（他自嘲「說穿了也不值錢」）。(WQY85vaQfTI S0021 S0022)
4. **gradient≈0 不等於不重要**：特徵飽和（象鼻夠長後再長不會更像大象，偏微分近 0）→ 改用 Integrated Gradients；他只說助教程式有實作，原理沒講。(WQY85vaQfTI S0023 S0024)
5. **Global 解釋**（下集）：對 filter 或類別輸出做 gradient ascent 找 X*；「單純做只會是一堆雜訊」，要加限制（如白點越少越好）並大量調參，結果受限制影響大，勿過度解讀。LIME 用可解釋模型模仿黑盒，只模仿局部，因為 linear model 容量不足以模仿整個網路。(0ayIPqbdHYQ S0001-S0009 S0014，僅經 gap 報告，未複讀逐字稿；2019 版提醒「選不同參數會得到不同解釋」)
6. **Local vs Global**：Local = 這張圖為何判貓；Global = 對這個 classifier，什麼叫貓。(WQY85vaQfTI S0012 S0013)

## C. 看內部表示／語言模型
- **降維看每層輸出**：取某層（如 100 維）降到 2 維，用顏色標 speaker 或內容。語音例：輸入 MFCC 依 speaker 聚團；第 8 層變成每條是同一句，speaker 被抹去。(WQY85vaQfTI S0024-S0027)
- **Probing**：用某層 embedding 訓練分類器（詞性、NER）。高分 → 含該資訊；低分**不能**斷言沒有（探針可能沒 train 好，如 learning rate 沒調）；探針太強也可能自己學會任務，正確率失去判斷力。「小心不要太快下結論」。(WQY85vaQfTI S0028-S0030；rZzfqkfZhY8 S0016 S0017)
- **逐層分工要保守**：BERT 例是前幾層字面、中間文法、後幾層語意，但他說是「過度簡化」，界線不是楚河漢界。(rZzfqkfZhY8 S0018 S0019)
- **TTS 還原**：用某層 embedding 還原聲音，直接聽出被濾掉什麼（5 層 bi-LSTM ASR，過 5 層男女聲變一樣；鋼琴雜訊從第一層 LSTM 才開始變小，前面 CNN 沒濾）。(WQY85vaQfTI S0030-S0042)
- **投影到 2D**：從不同角度看到不同結構（獵戶座類比；BERT 可找到文法樹平面，Llama 城市名投影出地圖）。看到結構只代表存在可讀方向，不代表模型內部這樣運作（推論）。(rZzfqkfZhY8 S0020-S0022)
- **Attention 不當定論**："Attention is not Explanation"、"is not not Explanation"，什麼時候可解釋「尚待研究」；只能當線索。attention 大只是「暗示」。(WQY85vaQfTI S0027 S0028；rZzfqkfZhY8 S0010)
- **LLM 自述理由可能是事後編造**：原題 GPT-3.5 選對 D；加一句「我認為答案應該是B」就改選 B 並編理由，不承認受暗示。驗證法：改輸入看輸出變不變，別拿自述當因果。內部分析要開放權重；問模型則閉源也能用但不保證可信，兩類互補。(rZzfqkfZhY8 S0029-S0031)
- **訓練資料歸因**：模型說「不想被關閉」，追到影響最大的是《2001》HAL 9000 段落，「有樣學樣」；大模型跨語言的影響資料重疊多，小模型少。(rZzfqkfZhY8 S0013-S0015)

## D. 怎麼看待「可解釋性」本身
- **別因黑箱退回 linear／tree**：「削足適履」。linear 能力受限；單棵樹也可能複雜到看不懂，實戰用的是 500 棵樹的 random forest。Yann LeCun 的路燈比喻：強模型也許在路燈範圍外，要改變的是照明方向。(WQY85vaQfTI S0004-S0008)
- **「黑盒子」先拆三義**：不透明（閉源／開權重／連資料都開源，如 Pythia、OLMo）、not interpretable、not explainable。複雜模型多半 not interpretable 但仍可 explainable；「如果一眼看穿，代表決策過程實在太簡單」。解釋的好壞取決於對象，沒標準答案。(rZzfqkfZhY8 S0003-S0008 S0026 S0027)
- **他的個人看法（明說不代表對）**：好的 explanation 是人能接受的；用 Langer 影印機實驗（5 頁 60%，加「趕時間」94%，空洞理由 93%）說人只是要一個理由。因此對解釋圖要警覺自我說服。(WQY85vaQfTI S0009-S0012)
- **用解釋來修模型是願景，不是現成流程**：現況是爆調參數，「離做到還有很長一段距離」；advisor 不可宣稱 saliency 能自動修模型。(WQY85vaQfTI S0003 S0004)

## E. 選架構：先核對 inductive bias 是否符合資料
- **推導方式**：CNN 由兩個觀察簡化而來。(1) 重要 pattern 只看小範圍→ receptive field（經典：看全 channel，kernel 3×3 通常夠，7×7、9×9 已大；stride 1–2；範圍要重疊、邊緣要 padding，「每一吋土地都被覆蓋」；範圍是你自己依問題定義）。(2) 同 pattern 出現在不同位置→ parameter sharing（filter）；守備同一區域的 neuron 不可共享。(OP5HcXJg2Aw S0006-S0018)
- **參數量**：輸入 100×100×3、第一層 1000 個 neuron，全連接 = 3×10^7 個權重；彈性越大越易 overfit，所以用任務特性砍連接而不只靠正則化。(OP5HcXJg2Aw S0005)
- **彈性階層**：Fully connected ⊃ receptive field ⊃ receptive field + sharing（= CNN）。「Model bias 大，不一定是壞事」：FC 可做各種事但未必任何特定任務做得好。(OP5HcXJg2Aw S0018-S0020)
- **搬到別的任務前逐條核對觀察**：CNN 是專為影像設計，用在影像外「要很小心」；語音、文字不能直接照搬，要依特性重設計（他沒給具體做法）。(OP5HcXJg2Aw S0020 S0037)
- **AlphaGo 反例**：圍棋有局部 pattern 與位置不變，但沒有 subsampling 性質（拿掉奇數行列就不是同一局），所以**沒有 pooling**。棋盤 19×19×48；第一層 5×5、192 filter（也試過 128、256，192 最好，是試出來的），2–12 層 3×3。「在下圍棋的時候就是不適合用 Pooling」；「應用之道，存乎一心」。(OP5HcXJg2Aw S0031-S0036)
- **Pooling**：沒參數，像 activation function；主要為省運算，微細特徵可能受損；資源夠時近年常全 convolution。(OP5HcXJg2Aw S0028-S0031)
- **CNN 不具縮放／旋轉不變性**：測試物件尺度、角度超出訓練分布會大跌；對策是 data augmentation（截小塊放大、旋轉），或 Spatial Transformer Layer（沒講）。「它就是這麼笨」。(OP5HcXJg2Aw S0037 S0038)
- **3×3 看不到大 pattern 是誤會**：第二層 3×3 對應原圖 5×5，越深越廣；有效感受野公式沒給。(OP5HcXJg2Aw S0025 S0026)
- **CNN vs self-attention（看資料量）**：CNN 是 self-attention 的特例（receptive field 由人劃 vs 由模型學）；self-attention 更 flexible，資料少易 overfit。ViT 論文：訓練影像 1000 萬到 3 億張，資料少 CNN 較好，最大量時 self-attention 超越。**前提**：「小資料」指 1000 萬張，是 Google 規模；只有這一組比較。兩者可並用（conformer）。(gmsMY5kc-zw S0020-S0024)
- **序列**：純 self-attention 沒有位置資訊，要加 positional vector（手設 sin/cos、學出來、或用 RNN 生成）；哪種最好「尚待研究」。長序列 L×L 複雜度（語音 10 ms 一個向量，5 秒 500 個），可 truncated 只看附近。(gmsMY5kc-zw S0013-S0019)
- **RNN → self-attention 的理由**：遠距離資訊不必一路帶 memory；可平行（他說這是更主要的差別）。(gmsMY5kc-zw S0024-S0027)
- **Multi-head 數是 hyperparameter**：不同 q 負責不同種類的相關性；作業 4 從 2 改 1 就過 baseline，但翻譯、語音辨識反而多 head 較好。(gmsMY5kc-zw S0011-S0013)
- **註**：2021 講次稱 RNN「這門課不會提」；2020 年代新課以 Transformer 為主，不要把 RNN 當他的現行建議。

## F. 資料有結構（graph）
- **要不要結構，先跑無結構 baseline**：助教所述 benchmark（superpixel 圖分類、ZINC、SBM、TSP）上，MLP 完全不用 edge 「都可以打爆 GCN」，最陽春的 GCN 在 GNN 裡最弱；GraphSage、GIN、GAT、GatedGCN 較強。限於 2020 年該 benchmark，不可推成「GNN 不如 MLP」；ZINC 上 MLP 沒那麼強。(M9ht8vsVEw8 S0058-S0060，助教)
- **疊深崩壞（over-smoothing）**：TSP 上 GCN 32 層無 residual，F1 掉到 0.361；同 component 的節點 embedding 收斂到同一點（每層取鄰居平均）。對策：residual、DropEdge，但 DropEdge 只好一點點，原因社群仍在找。(M9ht8vsVEw8 S0061-S0066，助教)
- **filter 設計**：用 Laplacian 的 K 次多項式才能 localize（K 即 graph 的 kernel size）；任意函數會一次影響整張圖；可學參數應 O(K)，不隨圖大小變；Chebyshev 是為了好算，不是增加表達力。GCN = ChebNet K=1 加簡化，renormalization trick 他說「不要問為什麼」。(M9ht8vsVEw8 S0032-S0055，助教)
- **已有 domain 知識的 edge**：self-attention 只算有 edge 相連的 pair，其餘直接設 0 不讓機器學，即某類 GNN；他不說所有 GNN 都等於它。(gmsMY5kc-zw S0028 S0029)
- **聚合與 benchmark**：多數模型 weighted sum 優於直接相加（GIN 例外）；GraphBert 等搬技巧結果「沒有大家想像那麼好」；比較要用夠大、切分一致的資料集。(M9ht8vsVEw8 S0055 S0058 S0061 S0066，助教)
- **輸出本身是結構**（list、框、序列）：改學評分函數 F(x,y)，推論窮舉找 argmax，拆成 evaluation、inference、training 三問題；來源是 2015 年代 ASR 稿，只取骨架。(5OYu0vxXEv8 S0001-S0011，僅經 gap 報告)
