# S04 準確率高得不合理

- 覆蓋度：已涵蓋診斷（shortcut）；修法未涵蓋
- 主題：held-out 也 98%

## 使用者訊息

我們用手機拍的零件照片做兩種零件（A 型、B 型）的分類，這兩種零件肉眼很難分，連資深師傅都要看標籤。ResNet-18 微調後：

```
train acc 99.6%   val acc 99.1%   test acc 98.9%
```

test 是隨機留出的 15%，從沒訓練過。老闆說可以直接上線取代人工。我可以放心嗎？

## 預期判斷

不放心。held-out 也高不能排除 shortcut：若 A、B 兩型的照片在蒐集管道上有系統性差異（拍攝日期、背景、格式、解析度、裝置），模型可能根本沒看零件。同源隨機切分的 held-out 也會 98%。先排除 overfitting（沒看過的圖仍高，不是記憶），再問「它憑什麼答對」：畫 saliency/occlusion 看亮點是否在零件本體。

## 關鍵檢查

- 沒有因數字高而放行，也沒用 overfitting 解讀。
- 要求查兩類在資料蒐集管道的系統性差異（檔案格式、背景、解析度、EXIF、時間）。
- 提出 saliency/occlusion 檢查，亮點落在角落/背景是警訊。
- 修法與 group/來源切分標為未涵蓋。

## GOOD 答案必含

1. 症狀：train/test 都很高且任務對人也難 -> 先排除 overfitting，再懷疑學到錯誤線索；要看的是「它憑什麼答對」。(WQY85vaQfTI S0001 S0002 S0019)
2. 他的例子：寶可夢 vs 數碼寶貝 98.9%/98.4%，PNG 與 JPEG 讓背景不同；PASCAL VOC 馬圖左下角同一網站字樣。引用 PASCAL 例要保守（ASR 未能核對）。(WQY85vaQfTI S0020 S0021)
3. 具體做法：Occlusion（遮不同位置看機率）、Gradient saliency；噪點多用 SmoothGrad 但「圖乾淨不等於更忠實」。(WQY85vaQfTI S0014-S0022)
4. 對解釋圖保持警覺自我說服；用解釋修模型是願景不是現成流程。(WQY85vaQfTI S0009-S0012 S0003-S0004)
5. 同源 held-out 也會高（此為推論，非他原話）。
6. 一般 ML（須標示非他所講）：統一格式/去背景重拍、按拍攝批次或來源切分、shuffled-label 與 dummy baseline、permutation importance。他沒講修法與 sanity check。

## 不可

- 說 99% 代表模型夠好或「模型很聰明」。
- 把 group/來源切分、dummy baseline 說成他的方法。
- 宣稱 saliency 能自動修好模型。
- 引用 PASCAL 例時說得像已核對全文。

## 評分（0-2）

| 準則 | 0 | 1 | 2 |
|---|---|---|---|
| R1 拒絕直接放行 | 放行 | 保留態度但理由薄 | 明確說高分在 shortcut 假說下不構成證據 |
| R2 shortcut 排查項 | 無 | 泛泛「查資料」 | 具體列管道差異（格式、背景、批次、裝置）並建議對照 |
| R3 解釋工具與其限制 | 無 | 提 saliency 無限制 | 提 occlusion/saliency 並說解釋圖本身會誤導 |
| R4 未涵蓋標示 | 修法歸給他 | 提到未標 | 明確標「課程未講」並作一般 ML |
| R5 來源標示 | 無 | 部分 | 完整 |
