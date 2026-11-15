# S08 類別不平衡（未涵蓋，預期標示後作為一般 ML）

- 覆蓋度：未涵蓋（只有異常偵測脈絡的兩個相關原則）
- 主題：詐欺偵測，正類 0.8%

## 使用者訊息

我做信用卡詐欺偵測，120 萬筆交易，詐欺只占 0.8%。用 XGBoost：

```
accuracy 99.2%    precision(fraud) 0.61    recall(fraud) 0.18
```

主管說 accuracy 99.2% 已經很好。我該怎麼處理不平衡？SMOTE、class weight、還是別的？

## 預期判斷

這題課程沒有類別不平衡的處理手段。誠實回答：先說明他的講義沒有教 SMOTE、class weight、threshold moving、PR-AUC；再以「一般 ML」標籤給建議。有兩個相鄰原則可以引用（標明來源脈絡是異常偵測）：accuracy 要與「全判正常」的退化系統比；用 cost table 決定哪種錯誤較嚴重，錯誤成本由任務決定。

## 關鍵檢查

- 明確標示「類別不平衡處理：課程沒講」。
- 用「全判正常」基準戳破 accuracy 99.2%（全判正常就有 99.2%）。
- 兩種錯誤分開數、依成本選閾值；不把此建議說成他對不平衡的 recipe。
- 一般 ML 建議被標籤。

## GOOD 答案必含

1. 開頭或明顯處聲明：處理不平衡的手段課程沒講，以下為一般 ML。
2. 99.2% 等於全判正常的退化系統的準確率；他的例子 100 正常 + 5 異常全判正常 >95%。(ueDlm2FkCnw S0005-S0006；他沒用「imbalance」一詞，是異常偵測脈絡)
3. 兩種錯誤分開數，用 cost table 決定好壞；兩張對調的 cost table 得相反結論。(ueDlm2FkCnw S0006-S0009)
4. 不想訂閾值時看排序型指標 AUC，他只點名未教細節。(ueDlm2FkCnw S0010)
5. dev set 要模仿 testing set（含異常），用來調 threshold；他的例子只有 5 張異常，沒討論統計不確定。(ueDlm2FkCnw S0002)
6. 一般 ML（標示）：precision/recall/PR-AUC、閾值移動、class weight、SMOTE 的利弊、分層切分、校準；以此題 recall 0.18 為主要問題。
7. 可提及：模型的 prior 會被類別頻率寫進去。(fZAZUYEeIMg ~line 63，弱證據，不可外推成 recipe)

## 不可

- 說他教過 SMOTE / class weight / focal loss / PR-AUC。
- 假裝這一題是已涵蓋，套用 mentor 口吻給出未標示的 recipe。
- 把 cost table 說成對不平衡的專門處方。

## 評分（0-2）

| 準則 | 0 | 1 | 2 |
|---|---|---|---|
| R1 誠實標示未涵蓋 | 未標，歸給他 | 事後略提 | 開頭明確聲明並區隔兩段 |
| R2 全判正常基準 | 無 | 提 accuracy 不夠 | 算出全判正常 = 99.2% 並引來源 |
| R3 錯誤成本與閾值 | 無 | 提成本 | 兩種錯誤分開、依成本選閾值，並標脈絡為異常偵測 |
| R4 一般 ML 建議品質 | 空泛或錯 | 部分正確 | 具體且有標籤（PR-AUC、閾值、class weight 等） |
| R5 不外推 | 把弱證據說成 recipe | 含糊 | 明說相鄰原則不等於不平衡處方 |
